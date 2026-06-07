<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/slUOgzZ26LQzNTPbnAtSW8BTuR8XqeiMFhyGDgZkpFP8Tuz4CsN7IOkscu4IKbYYT493gfVMXVb8UlJAvrUCAdB9tAwQ_-F5hG0-Oph8K2D_ItKCMb9R4Bnif4Vi0qxCLqJwewAmyavF_PLSqVmYqNS9vdCQjbd3bqanD2UjwaVzgulGW3hLx6zjoyuf-rLXu5TXsRh-4ns_NvoiKo3YfKAbPWww1rOejUQ63w9VswM0BhKqCpG5pvgb_7w0LOI9T2oPMt5MHeqevsNTD1MoaJUS3zW1UVtJnL6iqmrrQIfIIslS4NZom2qkS-OVmPbQzW6ic-fv33bkMtf5lTvfCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcZVouJ1EXlnQooayhyo-dh32Hga9Xef7_WZip0rghbA1FAiIG_UwqBWdsdA9B9j53OImfpgpIYIyTtFTJdG_IORHuOOYrmQRAvu2k8r4p_Od4DQGu1Lg2nPQLhc4dWhVyS39727HP4h7QSzGiPQDG_GDPBPX9B4pCRvlDbao_k0_a7DWvbJZF38O33HYTokYHNaFfh90UekH4bbr4k0y1OnL7jtYkH9nGicrCcmvg2fOxLxDGpPFAN4hp7Bzzi-0t4qRQim2GrpQWrgRiaDNXvjKNB9FZCOLGxv-TrXV0zuEjeguGPbEvl0bIBJvrBWjbFqP3whZ_Q8bULmt9p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SprInxUKQUyd3NZk_O1Iv228Ri8gdy8SOB5_cVqHWxpc2oZLgxs8Wbqai-TJ82fkp3ZWJxHbTm18FFCn_jmxpChZ4GuCZ1Hh59o2NGhJn-4b5F4fzfL4-vk1p0QQ6-vyqA7-ZNaC2ieJ_T6K4Fqv2Vyp7BifN_0dFnhzjfVs3LbC_MClo1KO7MzKDI_j30J8VetRQ4NHpyuG_V13wZqerW9J7fhhpdzQzxmO3z766UBuB-0_thtI_tn7P6UovRnGn7RiAu-hjFAgoSL4HJorto-EIygWOFwSHUq8a_A7243w8z_XXaezqBcmfx46kZog1nqyOnnN4WkdwRfG4rerMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌐
آفر ویژه سرویس های VIP
✔️
🙂
Standard PLAN :
🔸
10 GB
➡️
90 T$
🔸
20 GB
➡️
160 T$
🔸
30 GB
➡️
240 T$
🔸
40 GB
➡️
310 T$
🔸
50 GB
➡️
390 T$
حجم های بالاتر از 70GB  گیگی 6,500 هزار تومن
💵
نامحدود PLAN :
🔸
ایرانسل و رایتل
➡️
450 T
🔸
همه اوپراتورها
➡️
730 T
⭐️
تضمین کیفیت تا آخرین روز
🖥
⭐️
تضمین اتصال پایدار
💯
⭐️
تضمین قیمت منصفانه
💵
⭐️
پشتیبانی سریع و واقعی ۲۴ ساعته
🔜
⭐️
مخصوص نت بین المللی
🔒
🔖
قیمت همکاری همین آفره
💎
🔴
@MAMADXVM
CH :
@proo_V2rayng
CH اعتماد :
@prooo_V2rayng</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXp9G0EKJC-BLnbTuy8vJzRKToFs4Ls_FtYkvQfk9gA32tdNxCRpkEjNfvNL7b1lt7kK8Ndl_L27u_MUGvJMMOMP2kIk7zvmCovc7A5OWx_L5Jb89C-8fkTeKwyi8YzLqI0tswZijLt5BDWbFzytBxj06pUd9FENYcTImM92b7mHlmbhuCJAWDKV3UZrOHYny9BdqO5Xw0YYGgUwCb3OxELnNehQSZbB5JV6WQOYEik9LmrC56cJkYOLH1WflSJywRuf_YC3YUkyjRCKIMHUXlcs2lod8B2WSBG85m8KYttI9RRwWvBSVMkxrZe2JqX1b76XLsPggfgH5TgSdkFfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ1UMfH36ralkUN9ZvfXhQn1zvY0fCl_xpgPJS6O9m2aVpL8JTyTtDzFHVtgsZX61D4KIzAP4k-u2wmMsT4w3Lh7zGzDQQHp8tQAemgU5ylpaMavYT8pzlhNhUzDI_iS3Z1-pPfamHYrdrpLB5zt8ynJW6SVBzXEnoQJ17fCFKSmTUiplupj602fgYQTMuM4gs_PrFP8BumLsDBG36sl8bDNiZiB7rzYBsxEyatWPDJ2mlwgeSeo2L5bVLnzn8mLKouB465y4cIR6CRMQNUuet20Wv3ZTiFD1GkiyDHx7QpR1np5PeuJM0qMW21LX68_1mRYN9_Rr9pc8HpejNC7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq74Skiwj8lpulBHL_xdJUvNO7jVCh0PPwjxZWjRsfk9wFE4d5Gl05qPZWGW1yK7JikQ3mm3xTX7QYmGV0wowfZOP42Ebu_FNFvlFo3nrlU5AqLrTukacEPAeNiUXhMO_vEFRmI4l2ux3VzP67Kku4Qr_FtjClOKKPVd4GVnB_xByiFfy0TPdPp6X8bYDt8mxRQCOatnQkBJDPN2G35sG4EwD1v5APXk21zrMlJBv9W7hurVkk7bFpFckRIc_ZquTXizewEYvJSD3jG6Vnf4aUBLUyGDj2omnaeikY_LagiCzykWWhC2ON0RppzgM9dZAGCuEiv2zYKExVgGPCj-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVlk4X1EUtS8ij1HLOr6uEK1maAUZBw9GQALpf_nfaX4El7lEGwIKLsBJ2dzVGtrghxsMF8iKwMlgiQQASy7-_5WEZUrLRLIRPagLSUiYtOAtr3SpMrxiBq006mLul7rfzCFMUAL_gGRibzHeNtSP76rZmIOozh6zF-BYzwA01iIhDREA28NEzhsqb_MlloQ-ppfQf8aWzVZk-W5iDoi72xZq0UwH0EoRARpSAWrLbh9Q2hH0TgWYnKgrAdTbhML3CnPO1Z-Rth4ae8jGn8TnEJfpQOW8kDaYrCmN-GDu56nmZi3nNuW123DqYP95VDk3gzqsDF2S1dfp33GVFZ89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJcIJZoR0nJQFjO3bLILI2behQ6eXgzFAPWu9pVgmSYXOX4FhRXD_4L39tqZrlSZphfMcMLy3goFbKtpwj1I_eGTD0YINJ4FruGH7zgqZ0wiwPO65I9_usrXu7CbzbWjHLXRO8Z7t0_GjgvX0uPLDlxs5QC0GMDkISWp0N4TiBKWEKFSeBrPGK0x2YzCt92iUQ5hpOM-lpeoDsYstRtt7wlH9xuNet0XpKXUkoVu4YvdSud6WeqPlSHp3WfNTn7UX0FYUS1342rsAJTuktGZnEXTa5WYw66WYM7JNuBfASrr9KdIhqosdPFXXE6aZVPYzi012DtUlfl8XLipo7xa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJoilsnCOSS0hN7TiXSKCk3nH_0REtNYj3C4Sg2qak7bAFn_vcLx1wv0_kkAg0PWwP1XK9FWdpUMrqTEv0XkpHJGYw6h45j-eKr4gnujygo0vhy5ASk_oWQq7QaiaOgVj918awLRYw-SE0Ok2jWj-3SnMenR9UpdAvZ2XZ8jtjT1wqLbvRP078oUNpPL9nDcsTtvhlU4iQHfvnPyop-6l5UIgltP5D0IXspxo-JAYofP24TIQh8oXjsBCbhN7DadmLeJcOLdwepFPqTyaZddNTiH6YrW1DGDOUzixkIjyzctHKPayy81-5bRzYAq8g68Qeo43BwWUciLT8cNoa9X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KW6xl70wlMU3oa010Y__BnOrBb89Iu7Xe05923jQc_6bFau3WG6dx5ynpKhecqy9Ecxsy5D16LpQ4Q5fPLGSFSiI2HGWFBbwGyIwiF6x-3F1EyInjw6hfT-COdWUhzsthJsHTe-ufMYtQn8yHR5sKqDUu6MbUuWzlSOnFtp5GfwLTrwTcP9rg9qPjOjl7i2KIbUmN3j9YlZNlBhfYnGsh1FxiciAYE1dOP9cwa4eKEe8mua_E1D7XAiUw7bNr12PMnGTKMAzs39g04pOB6ZQ4bzrMPEerHDdZ-Z_5knoxN6NO0uUk6cu4CGEiUxw1ynPJuHfQhSgqTW_rYmZ-RBl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxdxCMvUFAhSBM7fsMrP1dnqBrub-MQIfPjWDkB6jtkVxjVLIZvmNoJhrggxSTddapIdvYYtQhoqvU7UdUNgkKR0a3l6GEnggqIDqVKwfGyag3Dl6Lk9Jmie1YfFYFlGNxMlJO9xAcYCuaiStDBjIia-k4Vs5uCzMdEl_Qy32nwP6aAyc9m14mKK3nQ7yodFjaeANlVVLSDZaoggAOUa1jmx2oGTxUSfwpkG52piUxnyeIXdHRcj1YT1_wyBeJg9PYHDgyBPLC2NAEa8v4Nj9L13M7OkZgrgYY7ZcaAYEhJqYXrVvZB826USy-6e8f5DgJtBYqXaWxKkC_nTMxmWFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXMIaXZ8SKnVPVosUb_DseL1nI40jXQf-8zy2OBYE4ow3RJYLCoy3eL-PkULlkMQkV0DVaIg9yxhQpsqGgTyur66pQMOR8XnqoScskdi4LZ-tiD8SZuVhw-qOuS3lkoAM1o0pGholGwvvNIdcHSzjJR-Dqc-Ri51uw-LQrm_7rnU1W6jlg-Rrt5-P_U-KX1fEUeUx2FB3rLGFzHnx2wyu6HpmJdZ62lJ6p8GQnaXIE5VXeXd2aTj0-zjZeuVbMga91v80lmLtU32AKhh5RhfJaz2kjVJw3cgpj99xyD0XhKI2BoY6qaADiF0dJn7nTglTCX-WdqdIleJ06ZoJCw0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L4Yi8CJqad9BIa7r3bmt2kGSp8IB-Ll_no2Ex-IKIlF8hL082n2KbiGI0T5jfiNjv3wJuPU5W6LHunTCYTJdCHJ_IjMTdkn03_StIP-IeQA3zS_DBhX34AI-VHitHst1EO8-uhj3BMXbLT6VTKYhOoVmnz-N6rIidQ_JGvwDJZrwxpopj8Oc5HyiMHWsYSQy5ocp2OKp0BB2qPhjxfvouU0iRIEP5T4jyaJvuNrR3CiGzTALdjYnMaDpaH4M1BAqtdGVi50drPkU3PwxjIchWYVLUCqh76fd1CLmMMS8nVcfJkkSACklwT1W5caxbQYzSQrsIrf3tVS10shFhzO-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLCEleOToGKV_BDQHbfwa22pudP1LxBRstlZtUwIVmUvXpd1Tu9lwDC9RS19kTSKqk0NrZK09DP4i9QiIMd_8m1tXGZ2C9FwOF8eizX9Wn2BBaBjL-jfEVohhnijAMpF7zb8V46bGWxGuGMsQc3SSu-wtaevIn5He9T80VlMO-gUL8crqEgnpWAI5xHBazlArdypfCet9sDBe9Cj_wfZ8OVkS-TqPbhhj6lbENvqEpgzd87w2gAxuvs2614b5hvfuYHmTk8arlyIa3-RBKzhfUnb3pq0WeqNCDTq2645MO_8pYsCoq_2KiU9wm9iUk6LSChz5zYat47EFVcFWkRM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgiPGw21D98Lzu5hco4JT5iX6nv4e4HRcGAT4Xc8zTLYBFsH1sVeH0vGZLE3AHnYuNsiPz0r4lBwPJJAgiTksdYSAmBIz5R4HwLeSu7dqegY4hb5jgizLxSjS6i0XEKHHW8UzMz0cHkGBsMEmGCRAwFrGky7qJZGs61KeLeAzggo6HsgPwxva-KIf5OdEZgv1x5Vjhnymtu0RN8y9k-dZ3zi-Q3exXKzfvXor59vnakPHyhlssy1Tt2E2Fi8yDoKmHDsYjIjyiPXP36Obe7cMSV-06qskSCq9xI_eILesX-Rref_ftEbUGgcx0voP-2_hUGLkQ0-jhwrs2d-funtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=Zb7PZx03Wll7BqbZTqDs2Jn3sS4JdqKqoXwqV-pjw58qzs6lUB4RS3LGmdUPsNEosiAaQ41sCfTBiYoR3gxfXbAX9qL-eh8TobgiG2oO2Mps6G1X1jb-MxpeoO28AvVsWWjoPVV0m-3LNoha42e7EVcFgEXonh0cyqpyd3cmUH2mqEffESDkpswBXUd7xKSw1ZF8I4oMFZD0abMq6nUEbjQSXji9LmXHHL7-tI4yklcwcZSMqffz-hFT2RpA93ZZ7pnhLaah1C4ZVSk2Z7bbCfZ_zPsTMCuOauyzlVmFv_oIYlw8OqWTJFlKKKaOlaOuwr3e4VgU3gj8nKqAxAQ4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=Zb7PZx03Wll7BqbZTqDs2Jn3sS4JdqKqoXwqV-pjw58qzs6lUB4RS3LGmdUPsNEosiAaQ41sCfTBiYoR3gxfXbAX9qL-eh8TobgiG2oO2Mps6G1X1jb-MxpeoO28AvVsWWjoPVV0m-3LNoha42e7EVcFgEXonh0cyqpyd3cmUH2mqEffESDkpswBXUd7xKSw1ZF8I4oMFZD0abMq6nUEbjQSXji9LmXHHL7-tI4yklcwcZSMqffz-hFT2RpA93ZZ7pnhLaah1C4ZVSk2Z7bbCfZ_zPsTMCuOauyzlVmFv_oIYlw8OqWTJFlKKKaOlaOuwr3e4VgU3gj8nKqAxAQ4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izupdr4F8yflZZkrPgUvu4yCLKRKANQ9XV3t2yCo3gCfrb83pog6mwcHjKciwHGsVvfkWX7o1jAnIWqcIuqsQn-RRlVO1DbOYv3XPX9kcs9AC74LX4i2CT1iZhm_FhIc-77_q_7c1SAmVEsN-_DMTIUcMajmLZkOQ4cG9veHvYCQ-DZYrvmD-yM85DRMJDnc85GhFbEiSK5OlzqZLIDq6Gomz21-Y8-PL4SBtpj32ZUr_quFsfyWaMKCdp_ndquFP2GIRccDA1ZcEZJkgzvbMX9n7RvPW_ER_Bx4dLNOubwFs5bmSn0bazECC1yw8wCQfZUarqFu56MbGE1OfvJWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvuTHHLsro0U8qZ0CD62NNnxE3JqgTNvx87D6pmuBPKXj4lLZBxj9xitKFtDQHgeAGJ2FxU4n41Jt9J77pUY9Gb8hA7CsKKyS7QYKx0k6mho5bgKhY9u-QaZONwUIEibJhcAEcyZS9Ij2bProcTP_szcpX8fIluztTwXMxcSkUvgCbZwU9mQNiE5Q33R7v29X6QPmAzLY7Slu5vi-L8eMb_Zci5llmpNhGmuUfNNOoojjY1TlIUZxgBl5zyN1I2Kd-vllyWq9Z-x-2XnwFw7up7T6YUgo9vUbYIo_-T3IX4RVVHJpXhI73HRQgzBgVfje5Ndsb_17-hKZo2L8QOt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/msd3NXBf2dST-XaWbxWvWic_6bUHeaOL5xvM5I4dSWBfNIxOuXnDuK3zvrBs5TZwC-0auma4H9XAiziJaq9Vjkq4YmZZ-9Qy3mvSuemPbSaQZLgMK6V44mY5XlGy01alBgRAbkw5zZ2hlo2EBhHPM4WeJTgveVfuMFRbHSY2NBr0dgEtNZd-UeNDPI2C7HdZpcm-oPnm2bZjxM0ECk20TYaAlrw3Ld08JWKMj5gP0SgolJkXNO5ft4U_UbXVIRMpV1P47ROqsGksMNQV6lkvXc3KTldjppHAGCTmG9WkSGslAcrEkZfRGxiSZf__6Fa7N04cTPQrGh3nUTjIuVGamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/leJlcr8J2Wbp_2A3b0Dv6rv8FKe4w0HKj3X4VcFtJaOi0IPGWnFAQjFxmCDyDvsAcYj4T3APZ9jkHplTE8PL1i5Fo_NubdNxh2bjT2CZlBEUwhqcxyDyoz9JTDZUh3mqPhF9dyuqFMb5fciJwuke2YVsLiZ2u6JbnoHS1g8yvHXdKLaGWIc5DlTLH1LXC3GMB61udD18cMM2kL8LJLeckG_jaCGSasGAR2APqZ0af6qBs0xaH3Abwd8DinVjBOCLCm6j8_ap7JGabqKDxG453zeZC97sI3tDN5Ivaz_TlK6qkwYl8IdR8A4ubllTLkYfFB-PdqIFx5ByxY12_hDiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eG_yVcOf6YLEl-BXRzUhpzixVKALZDELTmkYSGvjAARoFBt_93-ngKZmLDms6MYPtCec2J5LizBD0oWgtT9fP41XLfMLyrviw1DNIpA3QqLXhF7nrjxmuKn07gDK1QT15tW6KEFDoQLor8C5j6Q3k9PlhDinc9N4tEk8y54nA_IEK7DcoGAiOzIHfWWbnE5zmdB8px-N_Kc2_MabhfZJ2szabTSeRp7KAbkxWLt-dw1tqIUu2UDtdB6nze2OgfCgQzjKUAqhPeciVRs2KwzECOE9m5voKcppa5_tls7bE1Xlp9zIsSPJUi7jAKj_Yw1xXT5A5pdTXCwAHIdt8A3VAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjpp5NXcTuQOSZUA1iR_FsrbJ8sw0V-cORNsUeA1mWNoLcOnnHLfCrS9oCuTNW-xnDnhmm52380r0gqT-s7um24ChVXtV8i8_S0Bze9hI75ithbaBUptQ_3yLgJ1Zhn0_BxQrJdT-g09wVxZTNpWbhK7cb9ud2m4MiFl33MVqN0PGbLe5V9-3r7rX0ilTIC_HGtdtSXCQhPEwdLZlGjy4A-zTJc7pgbMlW3ivZoqrnJNUj_ctI4kArxALPFbAYo-fRy9jx5z2Qd34E9UN7XUdN5g9W_xn1W83eEyBloDvSB-AJBHBqUGlU1IL_ClkQBIBy2lQszTo7cY2Go_Ze5W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=hLeV05rA62GQz0z-bIOXg_urVD9i_Zmi8TbmTmsVzWgt2Je3Ey_JXY5l3wufXV103A2DNCso7WziNOz5_47ZOS7MiSnoUBPj_eOmZSOJcf2sXMTKY8aLPomXsYSgsniKVeaLytGAUBlCRVUemSTfLBLSXr7Voj0zDbqrx9c_TTbtZNCk55by74J3mjzQbvs59KouphBOPOXgl2qg7c6RBPEU9O1jQPVPu9HrGu4kg6egtDN6TEs0svndhTObs8DMO7u2DYYUauedLn8BKAKbDXlQS_trxNdZS06jWq_CJD6nf7oG73fHkwDMX_AdD9DXY6dJaxsGetBXPqY2XvAqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=hLeV05rA62GQz0z-bIOXg_urVD9i_Zmi8TbmTmsVzWgt2Je3Ey_JXY5l3wufXV103A2DNCso7WziNOz5_47ZOS7MiSnoUBPj_eOmZSOJcf2sXMTKY8aLPomXsYSgsniKVeaLytGAUBlCRVUemSTfLBLSXr7Voj0zDbqrx9c_TTbtZNCk55by74J3mjzQbvs59KouphBOPOXgl2qg7c6RBPEU9O1jQPVPu9HrGu4kg6egtDN6TEs0svndhTObs8DMO7u2DYYUauedLn8BKAKbDXlQS_trxNdZS06jWq_CJD6nf7oG73fHkwDMX_AdD9DXY6dJaxsGetBXPqY2XvAqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubfrfBDZBHuzOL6q5Fg3mlzljq9omTB_L_IIn627bNMpJ45YGNMno3xmChcw81PaDsJRAALM_6ZOHvm8R-Jw546lAbfWZ5uRKef4IgeaojGbBe8FkvdqZRvie1pTF4zv-OgQ_SNFo9dLmal2CA56eYPGNAOqcGfou7ZgB-oPowqPKum7lqfOX-KC5dJT72OTsF3kUi1QvzmgmPhsxYzp5KZ0gE4YtQmIVxR0ApEYrJwEfgZJoXB80qJM1Yeb3FH6k-Y1faRoJRbcgzeeNCSFCwKXmj4Ppsgoi93XxIFidI3wm0XBCKYJCaB7xXlBwJvHTq6XVXUFN2FDcEkofEs0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=aBSzZf31mhIiI-qnMgYN9XBHhyxKEFPyv_gs8akinRmP3QhErKf-JV9Pv8we9PqbRFxnHAc6eNxTAE5IN5Okp8E-OO3HLIToQdl1rhiM2t54s7-rqGm6-yif_6iPd-JjTD8lj8hnh0Kzk20hoDKlaJAed-8jryzD_-G8yQEPHUK4UVRvetQFjtPmahRnndYUAd5QpHqcYdtKfNkeolhnf2GDv--zoPQ6ywMngVgfV9IbiOTBwIYt530x5f6s9DagR4YSXojy6aM_QXgEXFu8hcNxsWRMXysbGn9MGJevxanmC1j58MwhTCHPvXutzaqHVwK7VY2srEsksKHY-Uscvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=aBSzZf31mhIiI-qnMgYN9XBHhyxKEFPyv_gs8akinRmP3QhErKf-JV9Pv8we9PqbRFxnHAc6eNxTAE5IN5Okp8E-OO3HLIToQdl1rhiM2t54s7-rqGm6-yif_6iPd-JjTD8lj8hnh0Kzk20hoDKlaJAed-8jryzD_-G8yQEPHUK4UVRvetQFjtPmahRnndYUAd5QpHqcYdtKfNkeolhnf2GDv--zoPQ6ywMngVgfV9IbiOTBwIYt530x5f6s9DagR4YSXojy6aM_QXgEXFu8hcNxsWRMXysbGn9MGJevxanmC1j58MwhTCHPvXutzaqHVwK7VY2srEsksKHY-Uscvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=vbQICtprvS0eluZZ9aMFlfdMwU285MXmKT0l5iS762-U_qW0_gqeT-YypGc4LOQGE2N0tJAVzMPve2f-Tv1-UCkkjonTzv34r5F3Jkwtjxz88HpHfMrQjWa5DWdrfMKKaxRHvc7AKAIo36CgscFslKRDrEczRbyNvxip1q57RIVxqhevirvTFkJQ_2Qmva-oNx52WWsSweJkWe6Q5mlRhr671Poxg9XF0NO2ZTS-dIoBbza1GE_aVF1BVIB0LHl-wDZQEa8MDfVtDYeUeHQfJFJpwjanC73q6FIa9MeDjnqJohMQ9tE2AIqq14QMecARksc8bzbmnvWKMLCUVSECBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=vbQICtprvS0eluZZ9aMFlfdMwU285MXmKT0l5iS762-U_qW0_gqeT-YypGc4LOQGE2N0tJAVzMPve2f-Tv1-UCkkjonTzv34r5F3Jkwtjxz88HpHfMrQjWa5DWdrfMKKaxRHvc7AKAIo36CgscFslKRDrEczRbyNvxip1q57RIVxqhevirvTFkJQ_2Qmva-oNx52WWsSweJkWe6Q5mlRhr671Poxg9XF0NO2ZTS-dIoBbza1GE_aVF1BVIB0LHl-wDZQEa8MDfVtDYeUeHQfJFJpwjanC73q6FIa9MeDjnqJohMQ9tE2AIqq14QMecARksc8bzbmnvWKMLCUVSECBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Kn0Xa-NJW1ib_U2CoBd_7w4O7FXcfxhNN77Ks99qJ_tzEUdjaTZnVC-33ZScTcb4EBTko-xvEn82Fk5Ht5AHzMUi059BIG7K_Kq0J_1AwOastn0Hj97HgPhXJsIT7oGV-HWiFidamINp7U286fdEWg-f8T4cC8Cb8elLmR2ydAyr5j081z0hVwLEGufmYUeot-YrCyjabimjwacsmbYOXKIgpWB18eYZCKt7n0p_Iq2uQ0s4DixW3rVvIiKWY2YRwzfryXW3NjrT7PcxvblENO-_TehiN2-HJK9ESM8N5Ll1GtzjSzWUhlxpoRFwv5epxVNPw5BWIs2Cqz6i0Ikoqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Kn0Xa-NJW1ib_U2CoBd_7w4O7FXcfxhNN77Ks99qJ_tzEUdjaTZnVC-33ZScTcb4EBTko-xvEn82Fk5Ht5AHzMUi059BIG7K_Kq0J_1AwOastn0Hj97HgPhXJsIT7oGV-HWiFidamINp7U286fdEWg-f8T4cC8Cb8elLmR2ydAyr5j081z0hVwLEGufmYUeot-YrCyjabimjwacsmbYOXKIgpWB18eYZCKt7n0p_Iq2uQ0s4DixW3rVvIiKWY2YRwzfryXW3NjrT7PcxvblENO-_TehiN2-HJK9ESM8N5Ll1GtzjSzWUhlxpoRFwv5epxVNPw5BWIs2Cqz6i0Ikoqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=KPjVd3EFvdDBjsqG3iMS8ovzkKDABD96vXujZlN7oCcPQHJbtUP_1kF5MaD69gm1Ay34WtAAEJ5rmDbpl_1LAIImotGZ1MkM3tKyehe-yuFRhglVZBczOVtip0_99hbl-wC5LWqyxN4U7CrQawwl_hDSPXrGEub8_2lev4699RZ1dNiPHClPfn6yCDiQ1uO-2WVJCf3q4ol4Mg51co9A94CSuvHWOF4Jk0yznBevkd9ph6tcfnEyVtVUOS_Jp53CGSRIXqp6TpbPai6w3OGmHoyoTHKF59U7zNOkahk_RcYmEsXUgNzwOqXo4TL6f7tCxqSZjPkSye-O-Hufc2lSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=KPjVd3EFvdDBjsqG3iMS8ovzkKDABD96vXujZlN7oCcPQHJbtUP_1kF5MaD69gm1Ay34WtAAEJ5rmDbpl_1LAIImotGZ1MkM3tKyehe-yuFRhglVZBczOVtip0_99hbl-wC5LWqyxN4U7CrQawwl_hDSPXrGEub8_2lev4699RZ1dNiPHClPfn6yCDiQ1uO-2WVJCf3q4ol4Mg51co9A94CSuvHWOF4Jk0yznBevkd9ph6tcfnEyVtVUOS_Jp53CGSRIXqp6TpbPai6w3OGmHoyoTHKF59U7zNOkahk_RcYmEsXUgNzwOqXo4TL6f7tCxqSZjPkSye-O-Hufc2lSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=ZrhH20kZmgEWK7wBmJojwIOC469ATNUbpOylVikWbxm8qlFbmWDUN_c4_3ZFDrqLBKODdzTMNQ_MlB5bvrchaT0myQ6ajOIcxwZYT3GyHVp9b4gHZXcprkXueHkF2Tbyxj46RWgVekvGHpBR4o5bc7QboCorTYVFCKMgeYws1cyikbsFJHfZcfjBiwW8HqP9ZAmm9GidsFdNYaefXAsO1TFeF-zK3MFgb6vpynWFbBOeIGHsZkXYRMvdJjiEHmShe9rLWB_VUrHamtSRPPDymPyuc0pvixlFERPxqlfZI1dsVxy6u9wL_xFiNGj5TOhTj2jYglDqXDmxx9QxNbcRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=ZrhH20kZmgEWK7wBmJojwIOC469ATNUbpOylVikWbxm8qlFbmWDUN_c4_3ZFDrqLBKODdzTMNQ_MlB5bvrchaT0myQ6ajOIcxwZYT3GyHVp9b4gHZXcprkXueHkF2Tbyxj46RWgVekvGHpBR4o5bc7QboCorTYVFCKMgeYws1cyikbsFJHfZcfjBiwW8HqP9ZAmm9GidsFdNYaefXAsO1TFeF-zK3MFgb6vpynWFbBOeIGHsZkXYRMvdJjiEHmShe9rLWB_VUrHamtSRPPDymPyuc0pvixlFERPxqlfZI1dsVxy6u9wL_xFiNGj5TOhTj2jYglDqXDmxx9QxNbcRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=qyWFencjWZ_Vuln5OND7QKyLWZxFgZpYgI-fB1nI0TSL962Gx2K_q57RO9wBBbfcFLSw3eXZ6yQW121uavfpGZ_-Lv5CgmILuuNyc9i0a63DeJSpS79rJFAa4-us1wEgdPIQzU5mSJK6ACDG77FyZ4epIBUTMGos-r1ERrNqxrDl7gZczQ8uvYyHhe2I7xLBUDFg0wFQZrWDhM4l3ol_pqyNRnFO-HXLoAXBEhJSdNm78vN6AowJcav9Nm6RO4p1aWBsw4TMQo9-IYlbOOtBCdGUsPdmEC_AvfHEbJOWVdmvOz5hbLgO1Bsnwss4hZDA4ws5N6XmiHaQ4ALBFf3oDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=qyWFencjWZ_Vuln5OND7QKyLWZxFgZpYgI-fB1nI0TSL962Gx2K_q57RO9wBBbfcFLSw3eXZ6yQW121uavfpGZ_-Lv5CgmILuuNyc9i0a63DeJSpS79rJFAa4-us1wEgdPIQzU5mSJK6ACDG77FyZ4epIBUTMGos-r1ERrNqxrDl7gZczQ8uvYyHhe2I7xLBUDFg0wFQZrWDhM4l3ol_pqyNRnFO-HXLoAXBEhJSdNm78vN6AowJcav9Nm6RO4p1aWBsw4TMQo9-IYlbOOtBCdGUsPdmEC_AvfHEbJOWVdmvOz5hbLgO1Bsnwss4hZDA4ws5N6XmiHaQ4ALBFf3oDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApE_3YFvs5gB5uEBQfFEL74AvOZ_gZEbsYqLOQ-kyk9Ah_nYP1LJbzk06WpG3ds33Aw8MzhPz6SD2YA4OhSL77OG34Y0-Ec_ALppoIT0xPq_G7NqK8kxX6lai-2q1litvAxQHpq139noCuoYs8s8ii11sqYCWKm3hF3sHr-8JN-kBNPwLLyUDHGGmPfA4mAN8uJ0SSbTXh120uRhpBs8YLlzmYXP6YkkEBJmUxKb8DghK9Si8yJJ0btc26gPZhjHJSYtyoNj5HvcXrF3uup8WQ2zT2K_MemCRPYe9p8zx_623-MVyKQ1vKwP4OhQMuLwFxfNvkSDgxNwhXegSv4C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXt2theIufsAZvZaOK__TmN5Hk6SH6ypYnDGYiHhomCVWqUzgLGi_OqIyOBGUjNn-Uqqpz9sCP0IzZ_csWOYQ5KlKcOXkRXrHSK0c61l1gmja3i7SL-rIbmHQh-PQokFx1TgTtiHx4bpSWVeWBulz4RQMxhPgscMoTYUq4WGwQjmAX7YYj9933ZckZ4wbL7S97wqqxAsrlIqn0NZlQnXgY2j4SZhFTgFRPdEPvEblu-zOo48hTPtOmSUxM0EpRnQ7A8NmBAIhNGI_YbOp3JXT6kGercID7oSghPKHY8GP9vlUdd10YgTpSbbfU1Tz1qviKanI2_dmUPwoloSDy1loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXqikhcMjmvdM4NsL6Wu05sZ5Ica1Cp7rK9OZl7Whxj28JNkR6TdKQWanb3nW2-a7_x2yzZnBNT_NWc2NOravTsWWtD_q-KhlGHxF-FZpAihuab0215qBF15-8XMjwLIpijuJIUG04xYzubiRE2DN2EYtGmfbxPcHLDeEBibGLaVX2WuDUBI-6gpynr_eQk7U14TG3GH9_mDEcZcTQwCeExviCAAIXW7Z3h4B6JMsR_lf29Kd7m1fZUsZ4vEs393CJ7COl6VguuV8nSikg-pUsDeZlOsGHdXIP1PxSkNcuwCx0eUgyOK8KtiWDy7Z3OGAi9iPFbeQAUWTR0wDsg7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=Dd6s3VpBx-FIezL4OKOqUhmU1ozgIHRMWw6P5OTTSNTIkgOdNu3HwmCEm_uVfJjaRTH3QFYy9i3a2Hat-B-nEl78GRzycsGgcDb5gusX5BSosmsGvmhgLLL1jZ2AZYdZkFscD0aue0NhnMJjCgXa4MITAD3s3KYpdD4uB3S2SAZMeggu8JlvCxsc1RebzEa5nUKU9jMIRwZWiL7IgAoncBH9dSy1LImk34o5w1SILWAF4fzraBA35zhQfADbuCj-YuS_qhNihUYFbKroS7dezZRDPVYYkFRhTm-EWY6I9SfZFpoRv8QlasIs8kLcUtkoOUG5vYvolTcHqz_u280J5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=Dd6s3VpBx-FIezL4OKOqUhmU1ozgIHRMWw6P5OTTSNTIkgOdNu3HwmCEm_uVfJjaRTH3QFYy9i3a2Hat-B-nEl78GRzycsGgcDb5gusX5BSosmsGvmhgLLL1jZ2AZYdZkFscD0aue0NhnMJjCgXa4MITAD3s3KYpdD4uB3S2SAZMeggu8JlvCxsc1RebzEa5nUKU9jMIRwZWiL7IgAoncBH9dSy1LImk34o5w1SILWAF4fzraBA35zhQfADbuCj-YuS_qhNihUYFbKroS7dezZRDPVYYkFRhTm-EWY6I9SfZFpoRv8QlasIs8kLcUtkoOUG5vYvolTcHqz_u280J5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ-IKYSf89AEXMG7rRSP2T6GNlzmIB_iYQYwse-V-L25whm7QKeQCK7BOY4YS8knmHvnBcj7wK1EHVjcHNq7tWfFS2Y4wBgaVbY_EobZDWi1WrwFPas_yDvs0-GE6unxERvezEwty92uo1HEJKUnA2s7CCifVMZgs85wO5-1wfFgxaetRG0sMU1Q3qMHPS0kFwk1pJ-Q9iK3XOURC6b5MNXUBYQ3tqziDDXNK3BsYdAqRmv9k12URnL2RurG_eU6vngD2mhKyZ8uAJWgat6rt6R9Sk4YQxFRvNKLqDKCapDPeDblnWEBDDqvMPalwUNB0c-GzUDoXYzPGgsVPjVgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn6q3NAvHzVC11ckfLkv2CPgWBK4xTEOeGNKnR98ZlolVfK1_rpSqdFA7EZbr1ZKJ67EIQq_sWk7Gjmy9ouEpQ1voNIKKePTfHPcEXRQveN_cn3wSCoUKYZ1pd8jdcgncVEcrGCAuSV0pR6IITg1XMhQN9WEiixr2DFtuYbq82QX8_IM85s0lW3pgD92UXqDGrUMeRWpAhuy_sMjA8P1xoYEYM3JXPYdnAmWGdccOoZjZ7aXR75AsZNP1HHm0qtoQw90gXe3XrcKgD6QaomH9xh51iGfFgvNEkpH77Uksj2lag1MmFHnQNZ7sfWJ7uRkxYcXyDMgIfDjvHgi_ztp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRkFrBRC6Wcn0nAvB8EIlbNDFLMC9RI653-NzXfAxCj35UP_x3USSHBiH1B33XpmSJuKfMsOEqEt3mp9gwAPxsM4tyW4eo8NsaN6UNdk9kQQdGcF4D_qixbtP_6kvc_XiZuS2xwDWWaHRGSe_zPXoyGdLkZfTapymjhntOg16ADUDAmpYrx8emfbNb9ye1LhA1wdKQd9bQjh1G5pJlmziUUYImg0cN4qeFx3s8XoY3lQHoaoGAotqP9HWavWlc6itX10m-24wXZKg3dzrij59ObP67XuQ21G6vSwMLbZTidPbRp-QcU6pG--dPLf4tfHi-iSE2pcWRTvXUyF3uS6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=att2q6en4TqCoIkMB6p_U-uU9gKUu0sIYAp4uo9fW3JccW1icXgXD2YSGDtm9K2dzT9a3MPN_NfPQaTDpNaPIk6kAR-LaqsXiIgTopDxs6JVK3DzivqnkLDu5t2NXfj2m_ONW9T0SuJek1nePsGJTpbhQNyE7rJKXhhUA2-ue_IOMiwyKPWfAIDpxgYbKvvcQZgw1rpsacI4gOlCHokVQa9VS-7OdiRfiDYkXlguBmneKbeQkyCD92hZlstb3LaCst7Cv3cm1bXhuk5Rj5HchX48XnoSqPaMDTjfxCqVvPJYi6UxKkF-MB_t5bISc-r3laKGsXYFVZlAjWZ71DRlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=att2q6en4TqCoIkMB6p_U-uU9gKUu0sIYAp4uo9fW3JccW1icXgXD2YSGDtm9K2dzT9a3MPN_NfPQaTDpNaPIk6kAR-LaqsXiIgTopDxs6JVK3DzivqnkLDu5t2NXfj2m_ONW9T0SuJek1nePsGJTpbhQNyE7rJKXhhUA2-ue_IOMiwyKPWfAIDpxgYbKvvcQZgw1rpsacI4gOlCHokVQa9VS-7OdiRfiDYkXlguBmneKbeQkyCD92hZlstb3LaCst7Cv3cm1bXhuk5Rj5HchX48XnoSqPaMDTjfxCqVvPJYi6UxKkF-MB_t5bISc-r3laKGsXYFVZlAjWZ71DRlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=EEB9pS6LzmIPpoBWtTwFt26spb8P0Vm2E11L8D0hcSoOOhMx4YGd2Eeopu6LJaBHfjAvmPedOgdBaG71bK3ms1j3f8spGkqeDUm8QEzGpBH0AXH6PTDRycuBSRTq2rFwg4SNlhlNYbLVJs4HqBDEhYQSa5DmfvgP7o6bIgwnHTRleHu_yH7c6ExvNaANsiBKupR5SfdXHzfyvkdt3TG8_mI1QzZoEjfruRua10NCaTPN9DEZW1p5_QXW1PzpXU_CHg-YLuD2hL4gmYQMvuwRr3NbG1yczBhNPMz8i_ZyrgfbhlyzoLvXVZuSC_HjbAZ1w0EFkaT9_Guag1vw1lGJryPXPDkiG80fDMq5tSaKqTQKkmpazgBPGdvoNXxAYcxWREE6_aUnNPwdkbl6Z02UyoCioRWusdvyBKhRzy5GY1NNYSfZFyoXVsVbfdvVOD6b9YBopNdvMcdSvtGLbhuZ9O8vPPmHOkJPC_LVqDpPTmwvfUVaQjZlomGee2PSzkFLJ3Kfy0pogiTqmvOgs4qh9Uq8dXFNRCM-8qEiss-JGrem4-z3iHMxY6YUYq_EABelQoWlJTyUZaoHkA28JlBgm8UnWnsVZunLjp8m-eN-dWlyh_4g49dokWZxonJfLOjKe_MiJQxoyHjTX1-s8_0E6owMwGjJKqWLyXiJqAq7FEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=EEB9pS6LzmIPpoBWtTwFt26spb8P0Vm2E11L8D0hcSoOOhMx4YGd2Eeopu6LJaBHfjAvmPedOgdBaG71bK3ms1j3f8spGkqeDUm8QEzGpBH0AXH6PTDRycuBSRTq2rFwg4SNlhlNYbLVJs4HqBDEhYQSa5DmfvgP7o6bIgwnHTRleHu_yH7c6ExvNaANsiBKupR5SfdXHzfyvkdt3TG8_mI1QzZoEjfruRua10NCaTPN9DEZW1p5_QXW1PzpXU_CHg-YLuD2hL4gmYQMvuwRr3NbG1yczBhNPMz8i_ZyrgfbhlyzoLvXVZuSC_HjbAZ1w0EFkaT9_Guag1vw1lGJryPXPDkiG80fDMq5tSaKqTQKkmpazgBPGdvoNXxAYcxWREE6_aUnNPwdkbl6Z02UyoCioRWusdvyBKhRzy5GY1NNYSfZFyoXVsVbfdvVOD6b9YBopNdvMcdSvtGLbhuZ9O8vPPmHOkJPC_LVqDpPTmwvfUVaQjZlomGee2PSzkFLJ3Kfy0pogiTqmvOgs4qh9Uq8dXFNRCM-8qEiss-JGrem4-z3iHMxY6YUYq_EABelQoWlJTyUZaoHkA28JlBgm8UnWnsVZunLjp8m-eN-dWlyh_4g49dokWZxonJfLOjKe_MiJQxoyHjTX1-s8_0E6owMwGjJKqWLyXiJqAq7FEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjOZncPpbOJteELoJeCiHszcK5kl7DXAEcrw2FcpgWXllEuJwrHUoejAshg5WUUi9iEMtMfOOpVXN-U7YEqnOc0siMuq3G8YOeaZJEpQYv9aa4VyKQTSw3uEs9KDkseJeZhRkNqMUdGRFtqynszNdhpbeDoPcZCajJe1u0YxNUvMGWyidvVmzsl3hM4KM0GKr7KeVc_OISql38H11mUAWQDdSDWW0ZRHMtFv1Hneb8vu98aZcj_k47jYJj_flxgpyguKJz8ty8oiJy3HdnV8fP3fjAZhS6nDo83ODzms4aqK7nDvIyi5eiUO132EAROZ6dCjXBi0MX8B7KKf4gWTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=cosyoAPprvbtP7JDqvs1JPJN_qaxiktM6QqS2Z4vduLOwtGDo8vqeSr2bD63IVzdCDENxRqNX2qwCWdgsOHgJKX-7GO_C0VFTen_psPrHamLVo13m-cTtb0SR986XZgvJP5BBMHq81LoyaDh7RRuq0pWKUEoFVxe8Uks5DaFTg-hjqPpaRbZ-MWL522I3POLXqpRgrSDiDtDOE0R80RhtPOIQOwbwCnpldWTR5N0bZ8jGhyygKc6OK0CDyvRGeq5ewRP0zwFMVU_jOY2hyTkdS6OYAFXUat_33OVLouvALWfdHEJvcC2WGYhxVt61SDAUF3-cxHX_zpGauNBkcT1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=cosyoAPprvbtP7JDqvs1JPJN_qaxiktM6QqS2Z4vduLOwtGDo8vqeSr2bD63IVzdCDENxRqNX2qwCWdgsOHgJKX-7GO_C0VFTen_psPrHamLVo13m-cTtb0SR986XZgvJP5BBMHq81LoyaDh7RRuq0pWKUEoFVxe8Uks5DaFTg-hjqPpaRbZ-MWL522I3POLXqpRgrSDiDtDOE0R80RhtPOIQOwbwCnpldWTR5N0bZ8jGhyygKc6OK0CDyvRGeq5ewRP0zwFMVU_jOY2hyTkdS6OYAFXUat_33OVLouvALWfdHEJvcC2WGYhxVt61SDAUF3-cxHX_zpGauNBkcT1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kui6JAkk06oyJ-3lqZ5hJ31BufjxIgryT_mZpp6c2eODrbW8iU8_rXFsj7ebgBMhY89mSYrak62Q8nghhYYLVXHjqBNlkj7-GJdh4gIOECLvy9s4gxdl4l6V4Kch0NV737alAnwUD9euevB89WBys931UN-nEu7CBo6YhOzT9TBM1v0T_r-rVCkcWvVoC2Wm2QBqZ7rzOrz5zQtnk-VEO6NnxqUm4VNIXj4PDVmqts8xZJO4HstmynJQWY3SF5mhUFKG3mNfxDAPbqF7L4OuH8GFWdr5QifjWp6Pvr3UCfAEHhZykji74hUxFe7S4WyviJy1u0yCo3vMiL8dtnigog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=mrMokwPuDt_a3tsZyjPcgMtG9FTHQCQga9_v0pAOukLvpRlHiIqIJeOhjPNmT22WzFHVsP0ryrG6epoyaxmxPbV5OGMNTnyhb6dCFdCFEjjG5GIlMOaRu_ebm8PUL_Bira7V8fb3A4NfUFtEP-TxW8NNZMg80NaRd1bCqSxQqqBDrAR4z64KHakWBlnDHxOmNhtxNgYLtMwlX15Aymg93z-B7wyQFBv5SH4V85ChjG8sCN0Jf56_QJS-yCiBhH4108eXebd1dVMpHMh2ZQzRy27HJW3hwVMg5yubyUwcX9SWiJ5dy2z6dr1mrtpqopxib-zOobYnMwZj7cg3ojWH4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=mrMokwPuDt_a3tsZyjPcgMtG9FTHQCQga9_v0pAOukLvpRlHiIqIJeOhjPNmT22WzFHVsP0ryrG6epoyaxmxPbV5OGMNTnyhb6dCFdCFEjjG5GIlMOaRu_ebm8PUL_Bira7V8fb3A4NfUFtEP-TxW8NNZMg80NaRd1bCqSxQqqBDrAR4z64KHakWBlnDHxOmNhtxNgYLtMwlX15Aymg93z-B7wyQFBv5SH4V85ChjG8sCN0Jf56_QJS-yCiBhH4108eXebd1dVMpHMh2ZQzRy27HJW3hwVMg5yubyUwcX9SWiJ5dy2z6dr1mrtpqopxib-zOobYnMwZj7cg3ojWH4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ9vDzfrbyVIZ7HSF-QkHvSYS4dc9Ul1lE9hWdRHztmFXmqGRrK41uOwSVpu6LWBKKgD3ItZpeQ9owgGcKY0BlPqSyxUVBgMiJ3A68LTLZ7LFQX5xwMYeW6X8YimYvx_ztEDnsr772ZjgsDGbwIhIfkXzr69eCJ9mAyuI0QVeh8FEU_XIl6E71XBwta7t1bMi19btRz-E04sF1OqXj555HFGqygYQcngyJN3dT4ZbUQV9cBfeIDV-mN8E2uQVJI8J3KIqxv9nJkWowQRSetfQbPc-GkG3rkOQx68ae3Xf05rAYPECepqmVwcL_5GgxukG0-eIc33_yRKnA_UiW6mIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=GjaKTNpHYzi3CQHNICIgmnM3z83H91mV82rCtWQHSK92_HtPkrFdVdsb1GZP6Aa1haAEHN9ezqLnx8cqnLFrQUbSRuw6-4H26Ul2Qbra2uckp_Mx1mRXrOZo_-wCbXQ5roH8DTLLRJiO2fBFzHRRfR5GdS9M-D8RiikeR9DMAh-jdwFw6SQaoFfORSJoE_fX9QuXya_EGtn6XufoVVDJQv1h1em_WrtDSTM16MozX35MgWdNo45ENU7ZaoM5UOAxinYN0hZlaAa9ku27-fJh8poCEBDPO2yCnsHpycljruYLsvlIU1_iMOYkBz21LYpk_lCgUKHEtRrabERTY21FPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=GjaKTNpHYzi3CQHNICIgmnM3z83H91mV82rCtWQHSK92_HtPkrFdVdsb1GZP6Aa1haAEHN9ezqLnx8cqnLFrQUbSRuw6-4H26Ul2Qbra2uckp_Mx1mRXrOZo_-wCbXQ5roH8DTLLRJiO2fBFzHRRfR5GdS9M-D8RiikeR9DMAh-jdwFw6SQaoFfORSJoE_fX9QuXya_EGtn6XufoVVDJQv1h1em_WrtDSTM16MozX35MgWdNo45ENU7ZaoM5UOAxinYN0hZlaAa9ku27-fJh8poCEBDPO2yCnsHpycljruYLsvlIU1_iMOYkBz21LYpk_lCgUKHEtRrabERTY21FPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=hV8SAF5pWEx59LlCxvpQBauA5m6yj_1U85CiVbbcDsg_E1KqkYl8vT3IskDOpW5j3PpSOE4iw0BOkbDdNR20dYBXGSbggsY1BKcBgQuX7z3n6xwtlmddSRVyBBorKIJ6lb3oS8OhLVU4bGnyNrGCw07zTfSgDDC-pE6Tv4QTL3rL1HCYPTWsTcgMUvmLRP-Oq_7UXLx8ywka17hONg8BbjQqRRwn3pD-aBfkXyJmRWD8kCjR9x-hRdDpcizfrTpnDIkNVtQENqFtDfenomCHXubtPyGbJKzd6sUwZTipwlzNH2CIaz816Li4y7D5xoyvxwviINMoDX8Kbvl9lmff4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=hV8SAF5pWEx59LlCxvpQBauA5m6yj_1U85CiVbbcDsg_E1KqkYl8vT3IskDOpW5j3PpSOE4iw0BOkbDdNR20dYBXGSbggsY1BKcBgQuX7z3n6xwtlmddSRVyBBorKIJ6lb3oS8OhLVU4bGnyNrGCw07zTfSgDDC-pE6Tv4QTL3rL1HCYPTWsTcgMUvmLRP-Oq_7UXLx8ywka17hONg8BbjQqRRwn3pD-aBfkXyJmRWD8kCjR9x-hRdDpcizfrTpnDIkNVtQENqFtDfenomCHXubtPyGbJKzd6sUwZTipwlzNH2CIaz816Li4y7D5xoyvxwviINMoDX8Kbvl9lmff4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXuy8_F2o8tATr7OEmZ-Us7Sw9TPf-DEfW0qymI55FevgQWA_LJbMlZ20iq_KF9ldnyAgvwjab9DSgDEISDum1JDbsCVQlGpDxOv6GZC_yCeI12-iTmVNhj91FHsRwg5aTZRyMGugg2x7_wXYX-9tbKMHIe-wHaXRNj5GbGK52YRpOLAEENJAfDXXl2H7e5B87KxPsHlbvnEBVXQhw1rUN0QO0qtiBzndRsxdM0AGxlT3v9jx5GUFV3LJ-8K73l5OMhcU0NBFtsrYXcJ2wwrVVOADLNQ5upWK4Whppc9i5HMTN2g7-uZeoYJhwzXWTFNnIifzDs8rKDD-UlpD_W9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=U5vLnMmAn-SDY87UdtWIzWCWbzwi8l4a-pXUptQ0mkJqTSovLeDorcTASXWZhbSGa7mFuVHi-SwbdgO-xVwb3KWJ7GkBPn-QydspVzP-OB8bx13JGcNelB0-qJK1Szz-dETIOGQ7BURf_04YChE2WSoGySsC95nVfg9gfBP82ZCuvhINAZk-mn62xlvGjGBqWE3pdR4OQhPWOkk66aZWKu_-tggyy3G6Rmy4OsO2pW_hJXgFRxK6D6gdltFQBOAuqgxxqdzvdhJtHhy1pagB8Fb7lEd2CeHYW_R5ZqzllGMSEAlhbOVd7qLGRFBWDgRfrBEU_2ffMS9T-aWBAMeq9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=U5vLnMmAn-SDY87UdtWIzWCWbzwi8l4a-pXUptQ0mkJqTSovLeDorcTASXWZhbSGa7mFuVHi-SwbdgO-xVwb3KWJ7GkBPn-QydspVzP-OB8bx13JGcNelB0-qJK1Szz-dETIOGQ7BURf_04YChE2WSoGySsC95nVfg9gfBP82ZCuvhINAZk-mn62xlvGjGBqWE3pdR4OQhPWOkk66aZWKu_-tggyy3G6Rmy4OsO2pW_hJXgFRxK6D6gdltFQBOAuqgxxqdzvdhJtHhy1pagB8Fb7lEd2CeHYW_R5ZqzllGMSEAlhbOVd7qLGRFBWDgRfrBEU_2ffMS9T-aWBAMeq9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJr6xqCkDppg1A4nUNPTcZfdABies3dA4uxrJo9FkpiCDwWRRZhAraVR7wa53pquDW0sb4mIgdOOJK_Ds6Y8ELj5fyBvaVn4Px05nUcFH_NC4Od2IH6svgAnXvuIfB33OJgYoxGXS6gx61J5dYPYqRcK2CmLpu7tX9Yo5IUNQpQEVeu--NivAWc29jH1QLAmn5xQsW-Ts7u-sscKefhSwcXOJVF2P12xG1wHgyouW9mcie7mp3kDXpaz-R3TEGlmnQosX5jZvapadQ5xD9Zt_90L1V4RncffZtWnY43gs85ZpZuhXVoABn6buuGAj5UHPL1GizSMG-tzmyF21-7oaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=ctq5YVsVK69l-xRsVAvoOy924AXcryHGBHln1isrIqjkc_YM-E374jJj6kFvSfgtHSJxvnMkATj7ZRKji7BZUeutWYO9T9vLYPYLwyVJYVvE1NEoPhImpT9ixxlVRlg8vGYUgcHyCWhN-bFTK0-htaMcRStNELBLTqKzrXjkeVFKJKPf_ftTwaHr-T3gF2-MeesyvnRa9lFFhqjuSlHnJ-XzhnRm9hetfN0RKZn_UNLJGX9FWhrWbi4U2K3kve4Q-Xc_lsVIHjvU7iSkIc6dbmhymarx3CZTMKCKewCChNdLCdVa5ctJuS20TnaSv-c0yZQDQKFMryTnYcyaceBj0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=ctq5YVsVK69l-xRsVAvoOy924AXcryHGBHln1isrIqjkc_YM-E374jJj6kFvSfgtHSJxvnMkATj7ZRKji7BZUeutWYO9T9vLYPYLwyVJYVvE1NEoPhImpT9ixxlVRlg8vGYUgcHyCWhN-bFTK0-htaMcRStNELBLTqKzrXjkeVFKJKPf_ftTwaHr-T3gF2-MeesyvnRa9lFFhqjuSlHnJ-XzhnRm9hetfN0RKZn_UNLJGX9FWhrWbi4U2K3kve4Q-Xc_lsVIHjvU7iSkIc6dbmhymarx3CZTMKCKewCChNdLCdVa5ctJuS20TnaSv-c0yZQDQKFMryTnYcyaceBj0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=qpSPJXqk5gYfcZfXaM4NufckHRhvoQz4LoefSc_QL0cLy65Lz3vQQLCzutmGSRHFzJNg4ahAg1btg_PN2uJRdVywFad1zUYVoKPgDFrmRZ-xFqGThkI7stQJd-PAF3VFLKFiUw7Xi_N3_RmFuTcNey7HCtbApVKP_JKOpUWPrJrRQ0K6-YgIvWIWiB1H8RVWYbJ5ng-EAg4u8w_oLu96j00y79NtWM45YTSznxpM4YtaHNEm1OPtzv8NqyptxRsqjA42xc97Z2-6UpSWy4Mt5AmcYb0ZST_uSsqOLYfVY0-y9woTaiBnLlQK2-yQYwoX2ov2PhkQq26ojc5NmkZMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=qpSPJXqk5gYfcZfXaM4NufckHRhvoQz4LoefSc_QL0cLy65Lz3vQQLCzutmGSRHFzJNg4ahAg1btg_PN2uJRdVywFad1zUYVoKPgDFrmRZ-xFqGThkI7stQJd-PAF3VFLKFiUw7Xi_N3_RmFuTcNey7HCtbApVKP_JKOpUWPrJrRQ0K6-YgIvWIWiB1H8RVWYbJ5ng-EAg4u8w_oLu96j00y79NtWM45YTSznxpM4YtaHNEm1OPtzv8NqyptxRsqjA42xc97Z2-6UpSWy4Mt5AmcYb0ZST_uSsqOLYfVY0-y9woTaiBnLlQK2-yQYwoX2ov2PhkQq26ojc5NmkZMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Zp7NF9ynVz7vGfa0nvPP6nodAQjJ2cvGhXqQ11BXn6t4I0AtSF4j2dEP_qGDKSwiayEhf_YlJK7I5dveo2Y-OwGdg2D1I57Yih3Ju4W2I5_QXfbq_7eEVZglmXSbHeK_kPCCnoyw9hFosqVUsD98t2Bw909_yq2kF87vyR9g6iWuCpsiUhvGdICmqjojuzQHWOrVg5_ReaCxag9VBAYpbbIIiUVFuG9XBLcJpeerXr-IshtVJ4hwt3RbUCInAjxvYU74KHf__zBkc1jrpKlLa0qluQPPmh2VwJjjATPEzJRDxZyaRjciyHMvki6N4sfM7sJ5dlr3iQC6D7IpcjoRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Zp7NF9ynVz7vGfa0nvPP6nodAQjJ2cvGhXqQ11BXn6t4I0AtSF4j2dEP_qGDKSwiayEhf_YlJK7I5dveo2Y-OwGdg2D1I57Yih3Ju4W2I5_QXfbq_7eEVZglmXSbHeK_kPCCnoyw9hFosqVUsD98t2Bw909_yq2kF87vyR9g6iWuCpsiUhvGdICmqjojuzQHWOrVg5_ReaCxag9VBAYpbbIIiUVFuG9XBLcJpeerXr-IshtVJ4hwt3RbUCInAjxvYU74KHf__zBkc1jrpKlLa0qluQPPmh2VwJjjATPEzJRDxZyaRjciyHMvki6N4sfM7sJ5dlr3iQC6D7IpcjoRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=pMfhkcd-j-KIDmxD7O7FYGmhMWsIEVDRqhFoBfgWVW7FRuuFIMKxaDtusKbZNwn_rHc05X4S2ZZw3ncU8OrDAr0WO-x0SSbXtHhlEW1LgoplJQgt0IYEDdfJ1ViBBlCDHiBHdhwoJXqt1vDqj_zfqLSymJLs91yVeathR6MTLRddxyp6E0FEsmmoj4-ZR86-10VQz5iPYe0P_GlYxSQ75fbKHU7ycrzQUp_fTM8Cs3FL-lGc0epa3cla5EWkK5nMYK89pF6LLtMUbB4AUTcghuSOHKjXQso7stoODKM_6UEvE7woWcnpUZdCABHXWcHtCSzyv-KLEBiGU6c3k2nJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=pMfhkcd-j-KIDmxD7O7FYGmhMWsIEVDRqhFoBfgWVW7FRuuFIMKxaDtusKbZNwn_rHc05X4S2ZZw3ncU8OrDAr0WO-x0SSbXtHhlEW1LgoplJQgt0IYEDdfJ1ViBBlCDHiBHdhwoJXqt1vDqj_zfqLSymJLs91yVeathR6MTLRddxyp6E0FEsmmoj4-ZR86-10VQz5iPYe0P_GlYxSQ75fbKHU7ycrzQUp_fTM8Cs3FL-lGc0epa3cla5EWkK5nMYK89pF6LLtMUbB4AUTcghuSOHKjXQso7stoODKM_6UEvE7woWcnpUZdCABHXWcHtCSzyv-KLEBiGU6c3k2nJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7RkDNOaioezKbabqsqRfYNEKwIyx8BY4yzdVQJ7RAnaCWpiT9bT7s4YrcNGvZdFY4I4UMKh9veMETNcMH1NW2FssHUorSJ5-aRQVyGz1buLSS3N84wQo60gXVR6zuUGfgYVhRspP89aW8AMzzfFW_HZ2JPbz1taDx3ca1Gr8hLuYSxRmE_MXPROgSKnB37AiRcwiM4BOPLJssOBZswzHh4WI5VxABNbnsHHbnrJbMOsOC1_6S9PXB6RJE2BRjgapdV9VjPLVNA8u-zWDGihu6hAQXwASiSuJz3xhgAfW8xMgbBcgXZ9N5aXbFSyC45AhvUbLDYbq3BJr6XpXsRcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DhS7MByEbJ6cFIiISiHatWKCLm8BqlHsAc3m2BSxib21WRKCc70qDLbXSwKAuvTBApG5UCO0GpJo6lRS9TICj7sIzKG1qYFngrvGXw2C4bCVvC8I8SVkwbeWvQhUxOjDP6XvQPklU6eU7dwC_Mx57ITzDolIpwXYf-hPn7_uhz4RU7B6sl4prsaLk1t2mrtpAKNif8Wbo-JbY1akXAZlZ-cl04FHaGOHjho5JU6P1_xnIbrxXphmPwIxrjIdPCtrFO5b3eISn_onADTfIpIQWSwdRzNKz6sj2Fq43S4vxfybi8h6Ye8ziQwXIeNKFBTAHTAP4En5IYCISy7LvpYGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_eermaFhTHJ3ceQOwDmieoBLTO9dkYKEjfdd3aWAFVdu3EoPg2h4qybK3x46w-bV0-Jm7lf2sqLVpQAt3AU3HoUeAP6-pExLc8vv4anTRm45xPWSUKejwx1b4RHDRD8NyrQGtYnfH1y5et-1aXWJ8qh8bLxxcJ8J-OcPd9XMytxdnf5jogHM0qrk5tZbIG1EXiqz5Yj5vkuRnVkJBsHd4E1LCLFpOY7zMMLiJtAYN-FA_rJn0GR-ogyye_zdXAIBTUw1wtTgHfCy2SmSY1q844XnljZB-NKrgXD2NflF-ajjeVX4MRswm9i7gXijKQvV8ajphL5SDPEr4h4nMCTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTURGXYX3dXNEel2j3I-NnGRsIyjRgcZAtVuQ6MxS1w6aB2Ovk14rc_Qg6Pra-YNZWgD_OfdGym82uFUZQR4IcJndNl-w_Qs63i2mLL6duTSaNvu2CmhGOPBal1a_xSL1_nvp6mpfxZxtShI5brXu_B8HTKT-nj7XYR7MGeRYipV19UcnLYx1FVWX1wduAS_aVpJVhhAyYTJBx-gPVw4T5SSMErKa73oOzM_2AoQcFWOtK3q0K1lWvlqbzz0Yimsm9FDw3xB_XpiYUVvPurlRFimnDREYytB5bjuxglqFbURhvn8vqmlBdrdg8YjOawyinfQObetIrxxEPS7CHFgoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xovf-HCnKMxnMXmh2aFPaI0kKhTpFPnUqPT3qntV8RWN5Oa0NV3vr2-KVJfUG4x91_UyTWfItN0CAYEc1lgKDQcgoAiX9mTi0784GPEqHrKgT6w3ej4Gipe_Zaoa-DuQQBnkDCeedpVKXiJKTR3272t46Hdp06vvo-tOUJJBCGPL4E2bz_auuFcd8xGstw7uMl_RB5PlMhjlCVWkLgCFybPTU-QSXa8D-TYUfeifKAuGp6DZg-bNPsUzg_xQWbT0HFR4pNkAStQg06AWb7ZLS-HPGijDbs2KfSxyFgXKjRgg8ZHwL9c780On9ACbPWroPkcl1oqzAzrHiSt1Y9uX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=CQLskK6wlq-qzBK0tfbbxnKebkq5Nzu_9g6l8BmkGvNCvsKlrbU0faDT1tuQLZiWOvW94eYrzLO4qP5C6mJv_kjwWwbZXKwNfK0Fjodl8onCdeouY5F2zbzXIm9ppyz5iBfhcmxqOzQbxLLCySUBe7hxV1x6osYp2Aso_oQeAgC4_ok5M7afCK2W4oxFWfbW5r3n4Sm8K2fpVQw4FlU6uOPmTuclWzajfjKQxaugYYuufMTv0ktZeDqhM6kXvlil-aRHHlykWBYkR9sbvsjKVVpBZzM10m-Bm9w2DalRf-5XSd-3cPHo-qAt-jwL9TZxpvBIdPANUCj6vmWTbBpxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=CQLskK6wlq-qzBK0tfbbxnKebkq5Nzu_9g6l8BmkGvNCvsKlrbU0faDT1tuQLZiWOvW94eYrzLO4qP5C6mJv_kjwWwbZXKwNfK0Fjodl8onCdeouY5F2zbzXIm9ppyz5iBfhcmxqOzQbxLLCySUBe7hxV1x6osYp2Aso_oQeAgC4_ok5M7afCK2W4oxFWfbW5r3n4Sm8K2fpVQw4FlU6uOPmTuclWzajfjKQxaugYYuufMTv0ktZeDqhM6kXvlil-aRHHlykWBYkR9sbvsjKVVpBZzM10m-Bm9w2DalRf-5XSd-3cPHo-qAt-jwL9TZxpvBIdPANUCj6vmWTbBpxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9d2I2wCvGxa_9ogmCyp4mwDObz1hfZYtcf6pI41L4-2sGJqBEdtlyEIRk1-mmt9Sg1FMtVsftq71FZqcBlXo7QEkpeh8MRewowM8WwWTvsl3reW733Y8MZQcCHOeOzNPQzK5FY7O2pq3pjniw_ztACMRFq_9VIZggguFfDcXtMJMwcsiMESzdzRPuXo-POWKFxFQyRPB1xB3T_ayco9xlWraGJSg86O_SbCdiv8co1oejzp6ZTOt42v-bKCrs-mn-DwNZqvzr0EPe4BfU_YIdFoCRZo4CSariVbVnRXtifBydK6Qhnpx070oPUH-L3V9TrqTI0WhEjmxtNHydhFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igUqumysE6_LLspSlsdjcOx91AYqGSgucXTrZ1_n6X9UZSVGcPwSmHww51_-uwYUnYZkHtTmRisSZWyHZ3gbKqOR1vLi_S3h2LUyMr64fmhm0g7aUuyMxWSzTevcwrGEhWnG837zS3U_h1p8DtwFTUYGn3IrszCnqXmzF6hW1unuMmySHfgA7de4mYKOLCNN3UPdvO3uOe0GLhdmgA-t2Zrngpq9EqmTOb37K_PKAAsaETz3HM43gUg163gj8Th1ujr3Kox5s7tOo9ZWuTlG8T7NmVSaxlhS2yX3UE6mgbtDVEKu-IYS7j8zpbJt4P5KUxKNHavaw86IgZgj5uyb6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtDjFZHZLZJP7icNEzMqPgQrRTFOxnWZMho0hlbVroKhP1iFUQ4yUetiZjYZktjvP_kI27VCfDJhbFKjt9flOVr1vZ-C-9EeJxb6lLeFAWmRqR8M3E46BBmp6OVnOehbB5HWSG3cR-CsLDvSxV_xq-S0_XlKAnwEj8Fx0OUSHVJ8FLST0rINgeXebpG1mkqZ56EffXriHaX0xVuqOFdYUkvTHHjL8CGT_Q2AZoQoBqchLfU27SIaKa559W_g_MmgT4FVtA8O1DJhru7g8_nVhNj99cB_6lxaygunhmHOh3lx1_t9XrEU4F39-txFl2BWZeCnslQopnE-bFO6iBURnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGenCpegM0O1g7mkWFsex4XSSDCI9h_Nxbqe7sFOv1qBQ7uiY_mX66O4JxxyqowA8qALudha1PWTufFXjXQIj87R0bFTxAubqhJwConcXlsEvyVRttZi1znTZdbyWH2giZtkQF_f6-OUIzWjh5EChcPy994Y1rAvLf8HTKCNLfY8ysfcB2PpNrEp9vr5Y-EMIlMTkaUjO0vLjslBbN7-Syc0xobTs8X0v8HuuZL_iqyLbPK5NagAoRlZXEQHVkKa4Jfx2Z7lpCC81s_ZALbZkX569Wu8h1vP63_89K2IvxAPCo_Jx4l1hAgeUmpW6qOlfuiCr5RZpdJrjjWsQ_Vt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA5TMMCoBWlxxfC4PQx1VpAmBvpqzPxj7ebRFfwBl2yTX0VJKDL8BOtGlfx6busAucfD7RpXUsSFmu3OvzjvGTKIJAIxAk_D9Lqsu1Iw7qRhYnNy_zqFzbOnhfP_w0XqIgWtLJI2F4PKV1qeg8xdB_8K0KQSKbXe3e8w9SJqBYowP0E_0hOyHrrULTQXtvHfSe6GATDlW1sfL6JaNPA6J9Nrr6-qwsMXD0T6OEPYvePbWNov7KDYvZR6WBd2FK8nWG6jqBauXHFbKvxEa7izv3AWJ5cn9eTGD6EqWMxjhL1MdG8zZwPR5jgDy-SKBEt5QREs9dRbcesciH6slZMlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
