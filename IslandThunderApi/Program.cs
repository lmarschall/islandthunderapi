//https://learn.microsoft.com/de-de/aspnet/core/tutorials/first-web-api?view=aspnetcore-7.0&tabs=visual-studio-code

using Microsoft.EntityFrameworkCore;
using IslandThunderApi.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddDbContext<PlayerContext>(opt =>
    opt.UseInMemoryDatabase("PlayerList"));
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();