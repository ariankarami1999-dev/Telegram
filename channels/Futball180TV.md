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
<img src="https://cdn5.telesco.pe/file/lO_TI58Ueh6tuC794hPzoJmJuV6wfbk3rQ3fzxlBWu7pZrVLA4VSRqyJFQKd5dUjonz5kSR7la1hItT7T3U3D7jW-FVfAy2WVKh05qhTj7VLMwHjLOrbRMNOvQMug2t53bzMwg0CsVMGyweMhNlvfvPzkEawGs-azcwZks6QAr-EusXUgJ7EizoNInmkZjyOaCEiaaadE7ScI50bd9Vdl5pr8bdd2zexxRx1Ucw__rgXOj0UHdC-FBgahek8QaCDUQEPtPbqNw4_zkYmY6a4x3PvSnZH-Nqe3mJFBNehoJ7aAz60bA_hAap5gFYd6ZdQho7L1qi-XjgNmg7RluU4pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 165K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMjiGIagjBav3j54BznIQxGQ4FdCfMJye7TZ9Ebg2tqLyn8aZLPiIuJNsDQXZVg9Z2mp7pzSnWMTh7eBxqPlhmfP3fRRgHobjZMoBJGloDnSwOz7DwZ-mYr7RmPwY0mY8Q5oz0QlRYoOWJvLukEkyN37Bb3_dG5hqCvd37mJbs8yB3NqmPVDZCS4IcPuTYbNO0WCl6Ie3j0qM-JRTqF5Wz7H0BcNWzqrXV0xRoqaMkEUcUFlsD5hc8-lAUhVyxXpE8aPjdFkbA6Tw0v2i4XgRT5CzEnR1WhPY_bNS7kn1QsB0kygVPh5ePpaO8B8HVfzT8BIaV3tUooi3YdYAHgDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرز : فردا از اولین خرید رونمایی می‌کنم و همینطور این هفته از مربی جدید رونمایی میکنم، این تابستون حداقل ۵ خرید داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/Futball180TV/90776" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیک، یکی از میزبانان جام‌جهانی هم حسابی با این طرفداراش خاطرخواه داره
😂
😊
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/Futball180TV/90775" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بهترین‌گل‌های جام‌جهانی قبلی رو ببینیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/Futball180TV/90774" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=sSBoWciywKFyIGxSVtdD-qK0H1VvXSmL104TeDrAc4s-QkTVQP-oaBbWGTT6t3k7RFP7-upxD4sc8U_JqR0qirphWvRpIV3IanWtI9MG4U_y_bHJLIQVStt9c02v-SoFUjyOrPIA1cRzYhT_Se_t5ntWFD_BxWUkn507-hceIBRZDjSfupvUaKcU6Ck8dIelElECrO8NOIOACj-2-nnBcXi3T_3cDQ7Vax3kdcNUQw4kiONYoERsbNMThBFuUO6eUd0I64AUfih_wUUVweObZ1NHu636-n7xWllE_LrqdUHarEyxAq-wQTsDAFmBAQu2XM9H1RXcootViUmTcmlR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=sSBoWciywKFyIGxSVtdD-qK0H1VvXSmL104TeDrAc4s-QkTVQP-oaBbWGTT6t3k7RFP7-upxD4sc8U_JqR0qirphWvRpIV3IanWtI9MG4U_y_bHJLIQVStt9c02v-SoFUjyOrPIA1cRzYhT_Se_t5ntWFD_BxWUkn507-hceIBRZDjSfupvUaKcU6Ck8dIelElECrO8NOIOACj-2-nnBcXi3T_3cDQ7Vax3kdcNUQw4kiONYoERsbNMThBFuUO6eUd0I64AUfih_wUUVweObZ1NHu636-n7xWllE_LrqdUHarEyxAq-wQTsDAFmBAQu2XM9H1RXcootViUmTcmlR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پنج سیو برتر فصل پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/Futball180TV/90773" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfmIZPSCP78KW-igMSvZLuJ50PFchymgyTz3sVLe4wMRoOKkQGTh77WkZ_EHiM4Pa7SJGaet7J69IitByhopZnIHFLaDT_BaPSe1OX4TNh56_jyT8US3KTTwZCiYLhZEpcnYpWuVFN_8jU5Ag_bv4G9JTWOmxbMTv6F2dgKnfF0litkDEqSYVMp_0scmbYaiNL_MLa0GGQo_nmQJViGmlYREHl-mUAOqRU-1BB80ncnYKvv5XFdFqhqzjtdtJJJoDZ9LJ3Cx4vKBhNTFVOk2D28tTDwpjNQie0F_2YYWadOJYT_Alr5IZTN5GyCe2uJjSwZPQLS-2c2liOHUd80n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🏆
۱۷ روز هیجان‌انگیز و متوالی که هرشب تا صبح فوتبال در پیش داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90772" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLwcfl-bl3xAbkolsPYoGcMRf4JHegS9zabFdk9hEaoeKZumbC5XxEduXO4vNuNOyq2BCY_x9-H905CL7_abIgPgXG7idFsrNFVDqFovkinlOKT6yFIGmJTr46sN5AqvJajNJuMGue0tL-MEHIRaqcVBC03969y0WLLiUAqc9540c4Tk0nWIQopsKJSC6OhTjwJgZR-irWDMY_NcPZc6gPHqM32C9O79Zv-nEaX5_WgEa4uWuypy7cdWnyr6J_rTVKoH8JxUzdZJSfiDJOvZq3JpYsSPklmxcOy4ic5shuGAfQGdEydBKu5mcHaDYtdt3szTiPcWhUZ8Te3Pu9rLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر بدنبال جذب دنی کارواخال برای جانشینی دامفریز
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90771" target="_blank">📅 09:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/90770" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=f8wCEVOFj5FVvZw6Gea3XpjGtCO8su1NxLqvHT89VQD4vx2l1uYt0eAB5qYqZt35IQUae9yTuslsas_jn0-kr1Amc0AyaLoX7KXadLQv6izvAillz3AIDLFZb8aRSF6EI0R4cv0U2pXbfJtHNjrEsc6KzKwvUeI-ld7AvIaQJDFNg9dMzQVJe29Ok1pxHneL9wQyk4Alo-D6ChzGjzfELm4jr9kgbEofit_zsq0CQvdz_O6pMHvLc0i8FFAqCpJaeqIIBSRN4a_hENlHLCfL6V7S4nnX4gBiFccZizG_iAVk1BoFV00krbh3OBlP0QcmkVREg4Fr-0hUTWKLC70Z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=f8wCEVOFj5FVvZw6Gea3XpjGtCO8su1NxLqvHT89VQD4vx2l1uYt0eAB5qYqZt35IQUae9yTuslsas_jn0-kr1Amc0AyaLoX7KXadLQv6izvAillz3AIDLFZb8aRSF6EI0R4cv0U2pXbfJtHNjrEsc6KzKwvUeI-ld7AvIaQJDFNg9dMzQVJe29Ok1pxHneL9wQyk4Alo-D6ChzGjzfELm4jr9kgbEofit_zsq0CQvdz_O6pMHvLc0i8FFAqCpJaeqIIBSRN4a_hENlHLCfL6V7S4nnX4gBiFccZizG_iAVk1BoFV00krbh3OBlP0QcmkVREg4Fr-0hUTWKLC70Z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90769" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWUkIkBw3wlp1Vgew7dfa_Q0YlRejKhXgQNkVa8SVcJJaslXDJpwdXgflmHktE8M7GJ9xI_VlkVOG2LZNYnqLi6AWwDvuAz1vOIl4HuF2PcU7_XJp8C-s2FWqHDlEKZbe7R_415CauRHZBcrPLKmPRzfKPrl8XsuuSkuDWRSPmW8Rj0cz0jhPb67yu4Tbts_5LhvJ8MbN6YXdIDDQOIiqN3vOm-KbTXGhCAzHLkc8gde8BlDaFYfru7j1lUFeA4m_nRw7OALdWkxcvN3rBsHDTomHNqu12FhUhVouvezJOW8y0a8La2zyhFHU7OY7fn7g0SyedPvaRTCNBpWKrsV2HfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWUkIkBw3wlp1Vgew7dfa_Q0YlRejKhXgQNkVa8SVcJJaslXDJpwdXgflmHktE8M7GJ9xI_VlkVOG2LZNYnqLi6AWwDvuAz1vOIl4HuF2PcU7_XJp8C-s2FWqHDlEKZbe7R_415CauRHZBcrPLKmPRzfKPrl8XsuuSkuDWRSPmW8Rj0cz0jhPb67yu4Tbts_5LhvJ8MbN6YXdIDDQOIiqN3vOm-KbTXGhCAzHLkc8gde8BlDaFYfru7j1lUFeA4m_nRw7OALdWkxcvN3rBsHDTomHNqu12FhUhVouvezJOW8y0a8La2zyhFHU7OY7fn7g0SyedPvaRTCNBpWKrsV2HfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اساتید یه چنتا موشک سمت بحرین و کویت ول دادن. ایشالا که دم جام‌جهانی خیره
😐</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/90768" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/90767" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/90766" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه 3-4 میلیون کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل کانالم عضو شید و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/…</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/90765" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5fnwrz3wUBgzY05tdeKtP3td7IjfeJo3Ing5P2oljDH-Bx_xhjGhC5tSExWxHG-dB-E5A4O9Mebe7QCEeYS3ja0gB4DzgncfTI80K5EFnFWVbj6JGmFOWkZxuFnFHHKJ-xsvVQN1LPYQfsf7_rcefssnq9PJuygDuu190bbqoH0HCo6tm0KP-xft-QEVKBQ0YH4xslZ5XE8Fso78yYHxjjc6YDD3p6PjLLpyWR-bYuMXhgZK10MElSoma0OTDQxHjfit_PjGz2JtW7PsRObxKyT0pathrYXzLXQiUsmHyvle-RMoaQVIaT8TbY887u3z1CSNN2yjXRzxBHKKTsBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه
3-4 میلیون
کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل
کانالم عضو
شید
و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/+vt7V5iY0jVhkNWU8</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/90764" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuP3gko7BgUPIhXe3sTHzDvKsKdx865X_RTQrr8twWXqSri48WEgECkiEzEq3tQOaLU121Y7BR5GUGeHoPNiUbmoEcpQaCXcj1jSdCQ_ti97g4IlXrHGX58tMS098Sq2DwAguMWZc0asu4jfXeXZKd_1octivIQCJ6kkXUVmNO60I0xEAvGOV1g-JTGB1nXNdvmocxz35u0i7hJOEd-ymvErm6CheKNJkR1C7NoobxoXXkQeRaxD0_B_OzmmxsNY_7rqT_Dv_UwxYC24Cysio1j741ZJ3YISl7V8CNi8-CXM6ctlFmcLcRODtqlWYLLzxzCUa6m4sgl1KI5xXmZHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6OTq0fDJL94N8RCEqYS7bZWk7eCIu40StEs1ZRrdj0psMef0p-xXdVMCKv51musLstfOUnnoitUm7PaMB9XDuYLMu2tgRIItxE1L1a3_h0xsroDeajSvKF7Rn3TLG3aRI0CEKUm91BGH5uJ2mSPZy0VzaoKJ6rvRT6lc_aqZqoNV3xQmdlSkX1NufqE7we9t-g1wFyPfNSeAf3Eij5UrkccQ5xzTfl9Bozqkr1U8_gXk2X8s4Ix-r2SfUtzASplWOupSYXuAhHxM4uG5ajn_JKIRxYSmDSJ5WafkfLa6hStKEIXgPAZFyqoSHjD-h6CprzrMv5hZGUD3DkLJKAwJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kHid7n_Dms15unWd62WgwLxZXS3YqkE0vwbD2Ja7agE8eHWPnS2mWxu9nbM1V8trxAMuNjLsjS0GuhaWog8GxlBMk0Xa1TAUJmZFIcJ0_BHp5LxceGOLWEZgg5cKoTjBfLupftvhV1qgokGsB19S1J58E5tKeBsHN1lUsY_rU1zZ4PqOS_WMQ0YJM56UGcvEepiXFeSuK1U_g7mvF42dSIE_etdBbmHyL2hRDAai3CoGh49Bw2-E8LH3wglEHIKj3U6bAwr6TGV-AVye_LavvjBwl8VaZIgZsm8LEKJU-gOhmVC_HVtUYVfl6JKw9ZMspyq9DlrI9YRaKQ2dT5lQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlkzjkaal3SuyHbenlwLkWSxSMDvyMMUVGwbDDo92ksnZ9N5Kl2OmlinBOAYDCclsKql5qfooMlripycN2N4CiIJSiP8_B9J6aWoHFJMDeocx3sQ-Ys2JgRDD4SSvjyjplFuY2s88qfBAuou_JB20oDu6STvnt0Spjmrg_0mOpNppvbfGIxrBNVffMqvIk2Clffflj_CYW_0SRD1Knuz9Wl1N1oLtLShyumo-HrmYYKqU_3HeUKT1CRtHQNBDnpff6bwz23pJTHyYPE2bt1wRZoC8inFooEIfBpFrQEUeLSyP9VLLtH5PW43_mIBKu0wE9Era522B2qPDNbGWfdYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90758" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfLx5ICnq3DfT7MzdGR2PkFr3f3M4lfwZJqYE8G10KB_vxG-OwWddjjkqu7q_q4wvlmEtmuKiia9xvirMVUbzjRVRfX3BwYSRxeHAnUkHzM2CYK2KU4m6vl-yF0au4OPxs4TkzvA6Fs9Seg7uz78uySeXhVRiR2t8_9yzofgsDAWCU81LcHN9g_LkAiXQkV9eOFfxCPd_CU8Qrao8vtpHQTFTMEB8S2Dz05aKLhLQaoRoX7iXEk1Uf_EhD8r3iJh8uOknVXlWfffbPVKLaeuaPxPJbWRQIaYwQmjFK2tkhek3_PxcLXw80Dg2fhn5batmE4M6Toh8dnoVVxAHg8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین روش‌های سوپر اپلیکیشن روبیکا برای جذب مخاطب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90757" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7127e40488.mp4?token=upkGLVDUv1ZsceCsAp0G-Whvcl_EPNtklA2d3cfc2Iowrk6X_LNSVMvsmVpADsNWarxrzEBzvIOkJEPQ3-Un_IN4b7aVuOphcIfnC6Rty6FIw-ziOWAu-GLpz85R2_VHz1rW5DwrY-uGn4tXkfYCTFEvYbgd59ZeUAyw2Z01OUdRVVUkVobAel59uVhZIn2Mt6qIoVnl9ax2dNBKW8l3ePXxl97RqeppTSZgE4LK3kZ2kLIHVrHcWZEdyfLjvLysqx-yHL1_AyqdbJK3TC_UZFAzlqbSqUUlgLPsgq7zoGC2Q-v9OdzD1qXK3D_2cEkLWBebyg68mjsb-ih7wNC2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7127e40488.mp4?token=upkGLVDUv1ZsceCsAp0G-Whvcl_EPNtklA2d3cfc2Iowrk6X_LNSVMvsmVpADsNWarxrzEBzvIOkJEPQ3-Un_IN4b7aVuOphcIfnC6Rty6FIw-ziOWAu-GLpz85R2_VHz1rW5DwrY-uGn4tXkfYCTFEvYbgd59ZeUAyw2Z01OUdRVVUkVobAel59uVhZIn2Mt6qIoVnl9ax2dNBKW8l3ePXxl97RqeppTSZgE4LK3kZ2kLIHVrHcWZEdyfLjvLysqx-yHL1_AyqdbJK3TC_UZFAzlqbSqUUlgLPsgq7zoGC2Q-v9OdzD1qXK3D_2cEkLWBebyg68mjsb-ih7wNC2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کفاشیان : آبشو دادیم آقای میثاقی بخوره
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90756" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=Asa35EG0ZPIqYiIybxkIEb-mYb7BXBuWM5P6x1ZeePMNp2BCocxYeR4Fgt9dhcK1lY1aUUJacHqR0xIHHLmCCooWcFPCvjgHA2uUo6-9-yf1zDg9aeb88Owb8OUHpIQQRzQh0XFASikNVKt3q2To_VbL6vcltLZjV1hvrUK0cy3v8ieg5c9ob8rrmHf64_YRjSxxavPrVVlPAgXxrlY6XiLzXWQ_n8mKq0DaG5zBI_2dxz1NwbGhlUQTN1e-E83f1xySuTz24hRi1T-Av8Zy8dI79QQWe13yFVsvhEFDbN6_ZshrbwYTAk7eqD45fSjuZukx6SOZBwjF5zxuBMeIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=Asa35EG0ZPIqYiIybxkIEb-mYb7BXBuWM5P6x1ZeePMNp2BCocxYeR4Fgt9dhcK1lY1aUUJacHqR0xIHHLmCCooWcFPCvjgHA2uUo6-9-yf1zDg9aeb88Owb8OUHpIQQRzQh0XFASikNVKt3q2To_VbL6vcltLZjV1hvrUK0cy3v8ieg5c9ob8rrmHf64_YRjSxxavPrVVlPAgXxrlY6XiLzXWQ_n8mKq0DaG5zBI_2dxz1NwbGhlUQTN1e-E83f1xySuTz24hRi1T-Av8Zy8dI79QQWe13yFVsvhEFDbN6_ZshrbwYTAk7eqD45fSjuZukx6SOZBwjF5zxuBMeIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این شکل شیک و مجلسی تیم ملی ترکیه بدرقه شد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90755" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krDOJXVyDafQzA7PHMPjzevyB-zk2fTwBl48vrtyiDO8qJNuuuyVHM7NnRW0HT27tWGhBOy0B0zCJo-KvhRGPqlKCS2_fbKNGbxJ8QJBmAk1BPirJfSEwCykGXP_EngJg516eRjvyjfdq3BOpuR5GOzEw2ly0Zk8D0S_xUpmU297ha2ZeCVr8z65zDxTHvLHOp-iJHwn6Q5FIZ5k_1rGco00XqAwSHu8rcc4YeeOkXu6mJctTnKAu8IKMGr8eG2EEmoKNsjuiJ3mmeurB7Pd38HXm6TxzLjESQHHiJKUjRpT9YdUr5L_NqByIh877fN_uBsFbHBozHSf--2sdm9PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇩🇿
الجزایر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه دکویپ
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
هلند در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
الجزایر در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر هلند
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر الجزایر
۲.۷
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه : هلند - ضریب :
۱.۳۸
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90754" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff6m-p4d6UzkakbhvfwXVBzUiOgbb6rDyCBUHtprZW7dPLqOiaZj_XTMvzZorAkoPZUkWS0ZrpsKdmeHkTeSkOH8vltU3xe3vUfIcsotiGE2txLyinWV5RBlCctUWHxCd30izOxXN-ZYFSv820Fwe0h4RZof8YRezfZy0vgqm00u_p77HYhXmiIhdAu3D0FvFbjs98zyLPSlFXlj_dJ3ywc5slGz5rQxJR9ySE8YIcfvl69I8tmMALjctgwq-foMI53NJSghsXUVc9I0x7prqEsQgnuoI4A1Zij8HYZJLPrR1yMYRDiL_O2ExHrjBcnbWGNZ4J9lRLu0c2oljvQ7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون ایونت‌هاس که ناهار میری اوین.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90753" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTGn8-m7iNkPo6SyL6P-bf69JZFAjtTlQ-0qcDTz4PpuJ5sD8W4ICLwXAGxe2oZBNo96CtxNOegk1htMTtNXurWrRtmb_jBr2pANh4fK1CXEnvKMOfx9gmbl7odW1IpfGMV-oKLgdKmq20hN12HOREtXS4vbYwFCC3hpunY24WIsyoijd_PRrMDGvaNCv1pi8J63CDBj7UoMfAdUgeYxWqDDV7mqoCAvHuNbYRy-cbf9p-ZsRYL1InV24KQxs6JOC3hnNM-ay6_v-Ae1LnFI-wtJOq2GpGsEwkG8XSquuQA4uvm9IFrwtmTtnvpKr0VCwZZB2WNGqheFPF6yC2A6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریکلمه بدون اینکه خندش بگیره:
میخوام بارسلونا رو در دسته دوم ببینم، خیلی خوشحال میشم حتی اگه کاملاً ناپدید بشن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90751" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzywASFaWOsOcBlDjTs9ZPZGhcEugP9Z_pn0_k0JziwedNccVTbK_y_DsvBSow9BOhu4Bsfdin5GljVO0zOZE4wKoF3aBG7p2jc9UPp5k7JHRhpM3XhBgg3Vk1wuLKqZ6rp20WjU7SSSn8leFSJoRp7U6Y1YvfvXs2YXAjFEgElKPhH8_lUG_cEYRdTI0xu32_rJHEcMH9ur2qP3vFFOi0jgW3kBsCNhDyPnJTQV_vQt4d6QZvLcRBvFUzJsLafjJp8W-iCz6_ICb7vaGBipA2uBlCuSMAUJEmyfgr4hO0pnhSeW-ywKAF3fH-L7fYEC5u7a1KKUQqB7uRKd2O8RRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنسو فاطمه دید تو فوتبال گوهی نمیشه زد تو کار خوانندگی
پست گذاشته ۲ هفته ی دیگه آهنگ میده بیرون
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90750" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsMAF9rbd0Iwc_vEGYBP18uYCuDcuiZc4qirroaRquIJUUUj-UlSseAP56PkAY3SjrsD2s30TreLXvtQ9V__ZmxassnfBoSlR0ksvPc1lgT7mZH0DmP1WyViO8diZR0FfzbgxKUJwyUvSyMF5esZWK80vXRiCkBMct0TIwlGKVoquJDaDLynBggc8SXHXRevPMpmzNfDYDECSuZpo2nb-piul7cLpUD_q2tpGpK2ZVqlCuk6lZStn0LI26gsE2n_9e1N0p9y02DlMDuAnuDNN7GvdvQWRaM5cnDBNON-lKPKqXTIPtTm7AN3USdjqmlQs3SZAKILMwdDmKIJhdn_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدی برای یاران نیوکاسل
بلژیک با برتری ۲ بر صفر در یک بازی دوستانه مقابل کرواسی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90748" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromernesto SUPP</strong></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها 10 گیگ — 200 تومان 20 گیگ — 400 تومان 30 گیگ — 600 تومان 40 گیگ — 800 تومان 50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/90747" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDdJKuRDa7rhI2ugEhBTRdYpAoe5q5wNZsZgh0oR7cTHerVc7xCf7A091DngBVCiHJQSix0jm9fBXkcnewAp4y4rAsRSW5z7w_hlCY8x7raVsfiimuYIHo66eq9LSrGYVkiL8h3ZXG25Fcc0u5U0bnj6r5LODnvDptAruC6xCdL8Lxud1oY-ZX_P1__eYk1IarPw6Vp-NidIREaWEGgFLrCJ9-cUlV4aBDayUBlew2ePQoM-4cVE-sERYBymgfGtT-Vdlvg1kH6hpja9R-0npHSNi90tBfyEP1iEoUrfcT7M6lKCA7AIu8DlUjLN9ZONaf3eA9sXNMjFedNUrA9-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها
10 گیگ — 200 تومان
20 گیگ — 400 تومان
30 گیگ — 600 تومان
40 گیگ — 800 تومان
50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90746" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-zvxam1_7K5rC6UFVT4NImmIV27tH2ICBv1bk2d5UBdpBwnFBA2DuPLSXHiQ6iMrQvS3FMRG6jt-nx88m6YStEdJ5HlXLa36t2bW5TJDpu_7wN4uqMFTJmvPwND0NNjJSmFyVz7nerwDVXHiF58y3dQY7eyX6uRfvElsJkmPELWgwh_Bk1YSn84sgXfY0Oyikeh9nZ_O1IyXdVX0GT9BRM2L6eVKpUynAY_5hsEYaxUdI0b5VP858sLtz2FRyjvSfZkgpN1XeM6TSSS6rvbEmr25xEfnBWPVp2iOpOX4C474sqwkDfmeCqJJt08AlpGoenc3Phq_40HyrGXJDNwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twGOpiOcn9mn6F3cAHxlQP0v6iRlithO79xagh6-ScErOuBE4uyimUv6E9-8U47ftid8s-VuHGsdFzubHkAXIZRe16xcvfoyeC8NTYY4JF7lJIwlTmuj2ZpootMaCkHsGn8n132n6rpHf1QcLPuk_8-eOPqyMI20fYzxLx70-ifUOzx5uf4EpLlF3eSFGV_idJupT43abee7OjOUCSQ_eITUhI0tmnqZq-_Hh8peL3cvHzZUuZZ7WxmoZ1glGgz1LXon-zomaNmAX5lXFSW7p-U29qTdvPqMlb8auRnb_AqYBvGcfFVpDDhWgfCN2SydUIF3okeQiLvbGqYaPRN2vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیه اینجوری تیم ملی ترکیه رو به جام جهانی بدرقه کرد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/90741" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAKyJfZWjwGezC-xey_7FximuonRqz8EN8xaA8gesV1vpazYrOwtgTHd2lzRD8IaZt3bQ-vXBssxO4bDEL672xobEW3jsZPgsLUfK2hTG6YQTALjFsKMP053qQTyhKQZHj8gq5FY8K3M1bojB4wNjuYTyF76UldSJFILmyCaCcmafEI4B3kUqOwxwr-VyBfYH-oxK1O47hbZou_ZIqs1opwh9ynUl_rxAKdgtqxN13kCGbiiBiwhHWspPFie3qyGs8ULaJ8X0KsV1Yvq6gtjT6RvAiTVmDBt6W7h2I0GNSAwSB5KrYgce39UIFKXqeHZRjuNdEtfPBTdiLEnEFw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loXl1LvGr-zBEZ_Gu-NojzhPs_YiC6UzDOI_xFWYLXqLMQ7WA4oqKTGU3a2RrY1oR-dG4KcXMAO9erMjp_PjT6LvakjQpjMQZTM3ZdA85y57M7uMDt1w3XiaMjUJyQumDIfpSSG6rrTti9iYO8FZGvVeD4IEM-e3ZWiujALhls5vNXKUX0ZTnI-PXE_ZWFqNLs0hvQfBiQ2Oi71eQjYMK9VOimzjrwCxnU3cFqtT7zsW8faUnfG-dauaNkkF7UYp8TN6aOi_dalE80ux-dpWdzUcubNwrJ48ZGA3vq4kPSayL8AmAGByvsCajWkg76VusdF3iDMlKlcLnhDY5sGQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe99EbpPwckEet1TZthEY2sMxmTvgxSe5saY8tMo9C972o0tlihdJDqlLyGDU02hrkQAx46MxNG5y2LWF5vMhtgxiByF0SMs0PiFrhnymb81RK6hYKStNlud46mww9QOQq8QJf-bep0Fw1vquuThFpvqMQWtHetktrFIBj6aG1aP6iJUohAFpTVC-dSGhT3Pv8YbD0SEyfQwktxkiFYxKRfa8aYXEbsZmGJnskC5LyWzrj2B5Kep93pcEy8M8c1OANnjVA0FYgxeqv0i603GPybmF4-E_ioT-VxdJzzlkm5fwx8sX1E5B9bNKhu4lSoQ9WB34i0cvuufV9o7HsIhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soSdL6FVBI2AM1DKkcjGylKj29mIG_53vKx50wYa0Yw1Orzx401tJZULsfulv9WohDz8Ny1nUTz1AqWMtiqEqlcun8E6V9XrjnuPe0J1SvimFuoWYe56IfiMUeEqUlQiAhxb8-ohby_cvcyA40VfeRDX5zlm3jTKFUthK-tM1uiA7NDddRCieI1SwFoM5igQlzsfDQiKebrqyVHsKbln6iSXm4PDJXRTidaDr7ii4rwKB3nvhGZSyzrlau67zxyWogE3Cr0ZKxOz-VIGubWt5m09V_CaONl5D-GrsECcR74joZN1D5DOkllKN-O0jQl-U7MqtYm_m-1c88X9FZwTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1-1lGsi4GmNU_EWSFVk_IvIAR6zOiXZC0vnTNAjthU0R8YJfe3hJzHEZI3rhPHhnOfJYjsF5XtiezWdeh7AwE4EPNDex2nEVp00ohxcJUpsNdU5FWcDdSc0TrtzLLLSGvohxVkpAfJgN1NUd0aAJylwshcQRiKQ9koBTxDi_xgZkliuGRzbeO7xTprBHT26kEIn4_dHgiBZmt7gbiC22yah4lxN2WmdlzG1e-2jnoLWeuqwxpTk_lhb5wHRfE9FJuc4PJHYsOmxx5L4AG_BGCHB3RlTCsTOH2hK_p5zVV7jMgwdveK87B0iQWJsSubxj8pnhridlTm5O98HiJ_esw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVTe_bn2QH3e-poAfv3kePCxbFj4IQ23Ii9XpEo0vSSwNTi-nlHtvYFXtgu4RYIm-Nl5_OUfUWmqQRZDTt0zTY7kNExj7w-ywhV7XSZekb2ut4SYpxJvG_LIrvLQKJBc4TkKYksrV-xF1K9V3jm83puReMRU7nqKNEuo61yI7UNpi-354GG0nCpgkbY3dss6KBR7yp7RpxrRZTMBL2Lk1PlIw-lSg-Mn_vL1a0K3fVuJN2f_IDuvKloYkXIkNjgAjaoCOTTokPsiG6ogFNLKOCBGV87Ub9TVWz0sGp8WVDw5mgVocZCG0Pn9czuNuWuMeDeW16NbT7GBsDlIt-UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsmCQN4sulbG7BvH9ckB9YyoD3z7b0SgrFcouP9gExLclXwUB4aiGnQG4DsbZZZ4HKC7mvCiulBvdH_842WGHpbm9UNiGpDXbpzmyE64kVfGnC1qCiaPjUqrw8InKrPhBt3tXi8ObKmOfB3wsMIiTYkTqRQyHjhitCAnZFo351JBXqewTX8D24lsan-gKjJ2_PPapgAezVS3vgj1Axk7Qrd35b1HVPeKctUFS-uvXaMHpxRQUieB2RE2pVt4WNoHj_442pRt3p2yArwScNb3DQK09Cu56a0z3ZHcutpWzABnb0priZc6utytMqfahkIR_Nsu4thHM75K9dom9B5B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfqCehcDMaD_tDl_sOMz6laUL9Y8iWmj2vo0TFbn3q1a1zMZBpWkUp_mjeODI7xc8axnyT3AgzrpBLiZKqxqSwPtM3uxBnwUAdnBGYJHolv4jrjc0mJ_9mjGDdhWtnMz2cwU4924FFaAJQLebnzcXuK4-7xAEghzcy-pRlfKeKkpHvu8kfwNV-kn2Kc8OulhLCDrHcmotsVoGQ4-K-wYUWVUzWlx5t_jsDWF8DWGp_YuTPW18TvVkEHE8_b3Nr9alpZAvqGZLI9OLQBU0W23bimoI_5HZItzBoiR332-aZHrIrcuprrAwTV2cZTuCgrXqVA5WoxJcsrx6KDLdxBICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOHokP6IgUCUlD3Z1aqb_Ncy6kjKPrpU7OHQGVt4ZHNukz2uU4oh2MISR5AbrX3fBrzd8K_16gVw1PjhyAHxyLfc8CW6BZ9wHmzL0VlC8vYCp8oFKoI-YjJqkwrfgM5bp5ate5QkWUajU0IIzHyIXPSLzgNgnsTKM2AfLnb9npBjRM1s_0M_Qy4LKkgNP6EBxsZG0oYUclV2c-_hBAuiMOa8nsiPTFQ6ANeYcdaaKM8yNEnCAVF4npmFdC8ndQryX8ab3dlSZb5qA1gigjZsQMWEMH6pQNqzzsn-w0ziplZqV4qBLyv8xyBSmXsMZ9q4LqtYOEKMDegonM6AlzqwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibPcxACxTLj3Vd4-jAdTII42YYT-T_tuXwpoYh49B0HriyembSfb5FVjm9a2z8-WJNWo4K_33FCi5s6h2qEU3d_j3S5HheWWKHiS7ELrKG099VO5BVQKYH0bnkpy7bJO3fTrG0XnMxA-oCq8Ph76JGq2Eoaviml3-0IPalw3ucKcaemuGFxT1rXOLwcvCi_U9V-JUUNSqhX8B3UBQ-WUTczSNFpyE4Yy9rCKsraCsSTMVR1L5MWvgZRB7OVWtmcueT1PDsIO-qswRxm6ki6scHvzMM_pIQj1fYU0BO6levecFw8T-QJ7rK6L0hzYR7edIaSSYlDYUuJUBz5x1ZboXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90725">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr4SPJvkOp5PGRyKOF6svF2uC_pMtFypheBaZdDJBxT8OaOhnb_F3nMIwWBki7fKkhhid_QrVsfuLX3SLoy0dsmFjlpodpIGue-EmZFBDjL_YLz2tuG_Nh9unnkrFoPHSavbtKfJ8PAZPGOhhO_xbAZTNpEKYWXEy9sPEtAWYyC7VmSYAkwRAOf80anvfe1fwK_afpYWDyqoD7rBsb-GaYALW7NJGFZKL127tiDRZ5X3BhPj8oNcU0GnEOgOkkIHzjY4euM0heJd1ofUZTF18zu5jzF35hjWv14N7PWNpbBD4__x9gPnsHqdYlIP92oEuMbQcTSldyeky7nf5PBv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووری
؛ توافق اولیه رئال‌مادرید با دامفریس حاصل شده. کهکشانی‌ها میخوان تا قبل آغاز جام‌جهانی این معامله رو انجام بدن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90725" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Up7p0NEmRPDw7qSHCFrSSc72fV6k7WpGbT1ZsylYLfV-kuBAQGAZW4RgqUMN6RVOQXSALnHWOO8N5Sh7MJ8KlgmM4QwNblqGbd_xM0oSn5qqUZsCnP9mLRoFXu0OocyshSAT3OGspz5gXayKy6SSl-BopI550rRWzgg9dfxjfjAvo7UA3eB4F77qiSZg_Zuk6hlFEWyZv0ynONUdTFj34tgPrbHQodb9n9idR5TlwGPieuXdFL21-XL4pbFewXS0XAb4a1aPl_25LQvksfXNZK1C91QTqFGmqmVh7g_Zq3-XJDaPLV8YkkzWgCueV9klXFcI8S7XoilAfMg1KPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ادن هازارد برگر فروشی خودشو تو بلژیک افتتاح کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90724" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تاج: 100 هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90723" target="_blank">📅 18:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b72747be.mp4?token=ZN1mPg0azrQvBiw1BapnG86jWuiC49cRLAwOZwT2r5JshLTm1bxcmwCmtrcCgX70SjkKrXOpM0hws-Jphribb5KnDpChdUqmeh5OjkR98d2HmsQdEzYYPxJb_nVLvQLZpBDuMGxvDG-jwoW1VRkxUEN9wSMCTzR7hreYX3aGx1AGNOFneSkfvhP9i6o8soWqlFeG4w2ZqFvym_aECftCwpTRWLutbbfIJSImu5pFoDkDP-_R_KllvEw3d_7qAZu3LUimnHwBw1hexw9tToQVO4P_nnNyXw8kyU-_HjOPgROj4U9UN49HtNfaP8HJ7hYABO7_-YVEQzCkqqt-zo04SmeXj3PGd8uvHDdzte0V3P9rcxKo9wzkEzyEOI6YX6Jd7mlIV338Im8wNV73sq9I1wLm_dRwKs_wy2hm7VUXptligztnMt7vRaLJmjYuwY7rI0rNxpAWTDoKjXf9ki33i8be-c-SbhkXspyeLB1J1DiBKlDCHIjgdqEv-HUKWB3ViZjFRoqbFt2EOwJiWhJuq3A-2yCYCPW-1ho0zS7SeuZpD-DsUq4NYLWuyiO6P2b993r_Mo0uJxeBNChTPr6ZKi6Bvsjm6das65TnoeVWqIJUiCsDy0Drv5PMOHFKlwpyv_swoig0V-TAbawKhEGdBHVsUCFbL_vYnx5WERfAqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b72747be.mp4?token=ZN1mPg0azrQvBiw1BapnG86jWuiC49cRLAwOZwT2r5JshLTm1bxcmwCmtrcCgX70SjkKrXOpM0hws-Jphribb5KnDpChdUqmeh5OjkR98d2HmsQdEzYYPxJb_nVLvQLZpBDuMGxvDG-jwoW1VRkxUEN9wSMCTzR7hreYX3aGx1AGNOFneSkfvhP9i6o8soWqlFeG4w2ZqFvym_aECftCwpTRWLutbbfIJSImu5pFoDkDP-_R_KllvEw3d_7qAZu3LUimnHwBw1hexw9tToQVO4P_nnNyXw8kyU-_HjOPgROj4U9UN49HtNfaP8HJ7hYABO7_-YVEQzCkqqt-zo04SmeXj3PGd8uvHDdzte0V3P9rcxKo9wzkEzyEOI6YX6Jd7mlIV338Im8wNV73sq9I1wLm_dRwKs_wy2hm7VUXptligztnMt7vRaLJmjYuwY7rI0rNxpAWTDoKjXf9ki33i8be-c-SbhkXspyeLB1J1DiBKlDCHIjgdqEv-HUKWB3ViZjFRoqbFt2EOwJiWhJuq3A-2yCYCPW-1ho0zS7SeuZpD-DsUq4NYLWuyiO6P2b993r_Mo0uJxeBNChTPr6ZKi6Bvsjm6das65TnoeVWqIJUiCsDy0Drv5PMOHFKlwpyv_swoig0V-TAbawKhEGdBHVsUCFbL_vYnx5WERfAqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇮🇷
بازم ویدیو ایرانی‌ها برای تیم اردشیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90722" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vstpfCMaF04bFlWDEnC8PSExGgxX2brxspwzYao_ffzgnaMzMGbP8mzQW2DgR9iIgPVbN0Cm31NsP_MeFET7CCmKZv0NJmSsPHuVpYH8aBZQlv08FrCGfBx6dXiF-QsejeXbEu8X__hSd9FjiZNGT_5GGawZmbSDyvFNZj0aGe4AVvj7HBJSzDRO09b-FSWSacr52Z1G7epxyWm4IlJsg7IYARuoLKw4CojjKmqim-ZPorRVUB1OdzZQDtpp8PznJX38vu1Tu6pSQCQM4E0fs395O-O0VwgZI3w0Sy1SVRkkrMdJZzN7qqhKRipx37J3iknDktQLRbgL6_3Nco0VWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
ترکیب امروز بلژیک مقابل کرواسی؛ خلاصه که اردشیر از الان باید حسابی چربش کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90721" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mErgOCdtLKH8MH0yZEhi52Se9LFLzHI4_24ZoOXQZO80JkjtmLnmadrgVwPyI87HbrfWK_tZ21mJB1MzxZsQLrO29XOmCpqTwV9U5LFY5Jc0w5n6EtHsevvouvvJ6nU0Lvl5CBc3PC0PuyOpKIjZaADZfh5KBgApg5KSoOJ-gQyxSHXdqRX4neTpmywd043zJW43zGOTYjSMGd6TKYdQjpEPUDuy_bJgOKBR-ZtyyxCxmZghduBLdUVJTJDIUYw--xdY3Igdvs87u30L2FyK1Y9fGM11QtYGZ-MwOFakN_ayL8NFekN54hXfnlQIJyDNEtRYMKtxQVE4LlZ5l9daKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه هایی با بیشترین نماینده در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90720" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVXNGrWgYW5LZyeAL4Ddi8Jr0ni8HcyqS69N478M-iDiTNCh6bT7fHsxugUFsHQI2r82TTN1Lx2SQb3Nn-uPBwo_0rCwsLww9imUrFxBObGkKZylsupfCGhdE3No8Vb0OmxM3TLfBluVqzlg_Snc4k9oJx3MbS2yShNGrOklQGK28SeCJtvgoZMg8WcLqajB5Bje1XQhiMn3ZGoUTsMxfMIVGVHgr2Jw8t_4Kg1KldgkE1j9GIBA96k_3vqC3-gwZrqnRd1SenazPx4ijHfSRWAgQ3JJcgWrXRmR8d6EvHRSQOCuchWHiBTObieFHSx6a2NDLikfc0zmhCWoVgHYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
اسکالونی سرمربی آرژانتین: مدعی اصلی جام؟ بنظرم اسپانیا قهرمان رقابت‌ها میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90719" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjAAGMnqhtDAOrsYkQ9quctm_pmFCLyJOgRnTR1DxvIIEwa1ykXjjnjIH4zHMTpilJMqxMfXBEgcBM9m2QnZzWcF3v5DWuSDaoUmewZMMA6gt0CX9lSHi-Tg2_yyQmekscrWfu-8I9_NUGlN31Zb6t_-TnwhDjrlvxjExLH_gtvBd67Ki0A4B-BHbaMeGayl0R3gbAomoRIc-Sd8G_HgsR2cky5VU0dgLNQm16N0n0RIE7VPHq9sYI4Mq7zNPC_SUsNc2XArBjQy6AcLwJau4LZZC4Mdu5-JIrKxVMbQ3G-QAhknAG8cFMRj0PtotVT3JlrkxvOy9p0QfP6oq00Z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👟
هری‌کین درباره تصاحب دوباره کفش‌طلا
: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90718" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=XbNOa2ferrhhv3YKmb-zf1cFXM_RhWGkBGyAottGEKTToqlS9b69gUEO4s6BTpnJbRKuU6Uy6SGbdIrjfkX84h_RG1AKbY5xn-PX6mXuyKG2SROjzXRj7InmyDwkl4fI-r1FgF37ShfqRcQn21OJxING1q8wgB7zKIGpzjSDzul7AUETP6p9Ixis5uaaM5Z-4vocT4HkZ0p6WPUxfhawyQnS7DobSKsd66iiGVq9f4CybYQ2YK7WqML62FZV4mOts1i6Yu7tVQx7vsnupN2K_HdLw3dzbmr_gZ81CYa78exay6n_L3i_cwVD85dqQFbNE8LQN2vHxBa63JbvaTKpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=XbNOa2ferrhhv3YKmb-zf1cFXM_RhWGkBGyAottGEKTToqlS9b69gUEO4s6BTpnJbRKuU6Uy6SGbdIrjfkX84h_RG1AKbY5xn-PX6mXuyKG2SROjzXRj7InmyDwkl4fI-r1FgF37ShfqRcQn21OJxING1q8wgB7zKIGpzjSDzul7AUETP6p9Ixis5uaaM5Z-4vocT4HkZ0p6WPUxfhawyQnS7DobSKsd66iiGVq9f4CybYQ2YK7WqML62FZV4mOts1i6Yu7tVQx7vsnupN2K_HdLw3dzbmr_gZ81CYa78exay6n_L3i_cwVD85dqQFbNE8LQN2vHxBa63JbvaTKpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو غمگین و تاسف‌بار از یک گیمر ایرانی...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90717" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">علی تاجرنیا ظرف ۳ روز آینده مطالبات آسانی رو پرداخت خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90716" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPpEKo1neLxmrfhtSYCrtRcFWNOI73eEy-0sut4cGkUHBaImCGw9tS8ufjJDCAr2Iwpj07tLgqH-tt-55m0gxyYOyz7rPpmbWggyvUtVGSIryacplDZ6zcV-Inobw2Jxb77Hj2p7Jxb0n-s2LiFSQ6PoLZ81Ni70Fx0Pu0seH_D1sTlstPtb1z9yf4aFyvPlbHPludytfJgqKatUn4Lv2jMkhOWSZpOs86iJDydKQMcrMaChBLAUuNCsTbe6dTG_Lu69qQatvriZ72UwB6bxiY2i-yTTPzqT2-QfnA2-UY4HdkqPDI38KXmTDwcorQQyY8NPGMaIkTaNWl1qtGZ-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGOVyoGcEmnNz7x9uV3H1pwvdKyN-MI9xiZcyX5_h-Ia9W6jnxkxYz1Y3H5KTuFwVozBKIRnuht_Lu4q5ztNaOvgKspAmas-A-kTuXa2vgnb8mEuErJwIe6NmKczcn_ZmJARTLN1m095OtnFZT7WA0svv9ulRzAXRCORhMZ9p03uzOIyN-LvUyRCnhmg9eF60zeOLB7f9aQIkWJzOIOLPzb4Dd2akEnKYqfLRgM1HekD9ijgGeP8DhQu7o5d5Jp3Ff8lk44tqZY-Gy_6IT85PPZJXX54Y3HBbGOFiD-UR-ERVR6Bw0q9Hsfh5F84YCKMd51uVwz8vXUHMEvgd_QTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=VJJHc6B8b9RX0D_8KpTYLUQd2e1JQ3ARt0bHdvDe3TN3vtQ8i6seBTyBRRlLx64fH75CVDZEIM1BL2oL1lgahOWmHxRtGbUoXdURPHBW-WSNfE89EDjjK5ldoIlR6b8QNbIKjQC-bUEQwrQU2gO7YdACZmIpeCpAWuYPX1EChrg6cEeFIY7QGGCrBHEpUwae-rpHGaXstZKtUPMy3UmZcWAfWifLd80AJp-S_4hIjhfbTG_UpQyCxqJpsgK8Rn-8rvJ9Q1ExhlF4XaR71oycora-9fKZvG7UfIdc_XFvHSoMrfhqv6mIU3v2xAtVB5YZdRcndBqSTCOoDBe79h9O5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=VJJHc6B8b9RX0D_8KpTYLUQd2e1JQ3ARt0bHdvDe3TN3vtQ8i6seBTyBRRlLx64fH75CVDZEIM1BL2oL1lgahOWmHxRtGbUoXdURPHBW-WSNfE89EDjjK5ldoIlR6b8QNbIKjQC-bUEQwrQU2gO7YdACZmIpeCpAWuYPX1EChrg6cEeFIY7QGGCrBHEpUwae-rpHGaXstZKtUPMy3UmZcWAfWifLd80AJp-S_4hIjhfbTG_UpQyCxqJpsgK8Rn-8rvJ9Q1ExhlF4XaR71oycora-9fKZvG7UfIdc_XFvHSoMrfhqv6mIU3v2xAtVB5YZdRcndBqSTCOoDBe79h9O5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhPmQBgP13sm_xhai1wZGl7hkInf2SlffxVLFchGFNMFEba_-rect6nJGMA20iUNgjaAOnzbzHcpzvY27nuhkCvayXy7unn1uzDIxLmpmrqKcH4AkVMSgg-05U-uy4ub3bCT2Fs4AKIX0AdXiZZFUzaNPt5LwE9n5V3p60NjFmNwSiSSJdnUJgAdvji3uzOWu8CFYUrUrp8ogKn0OD46mGJfnjJOqjSI5H8BtAKCkOmQBTAFXcSG3ocVGRegfhdELm28qkQ12wjfsfx8w56gdznsa7oKKS02w5x3whXiwg_EMo3Ix0nqI1h1AlO9ANybulgNOsuisuLn9FIZLVs9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCRVTgeX7CS4KNb8JTf6woz8dLAKMZrlbAjiJ916HGo37ITbnXJPxaMyQZgYmsthkLU2AHQRNcGUpZmPB9Re8XMRNvB3lFr4s_4MrnmhqU09mtxbT90rZSkRjkpmL4izQSPZEbVqKJyVPJuHpwbYN2QBIhfvKI6Qqz7Zky0YjrF-2Nnc2Xv-yXbxjdmgZHu-uESoC8pNUo1PdzI71oEXqyoLxy4yp7cWW--GLbTbU8-vipa9DOk8Nf6dU6YbZnmGfjWmQAx__tHuKyeTYoNPVDzvo98LMpvO3ygeuz04QiK5iDi5slDge47eUx1RiF-d9WWWlZk60i-MmffU5GRKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نظر روبرتو کارلوس از بین نیمار و وینیسیوس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90711" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr3wf9QVjz4j8xmNVpJ9i3iyvz7UYbfSkjvEBsD4D9xfZFuN-RPAbuJSD3zSm_6BFNDEWL8k5Aan3rA3DSf_FR7Sk78ASu5rzF2dZ9wDHUCnREmGa7Eqw_A2f8IfQOuZ9oh-nH5xFypjKIYEd_b5WumN10Csaj1gzxWSroTcj4Rx2TiGJx3CbxmtNNnV3oI0IgF-qpOe2gsa-fKbk3PD1ngjXdhvwaazlFIjO-LdLndctG1pMdpgkFwhgyAd-6JSkvbMdGK2grm9IuRZWOdZK1dD8sfsnRB2z6JlmaK8TDZZF2Dqb3kwQ_stUuE3wHoamz5SDjb9XvKuxNzUqidhbCGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr3wf9QVjz4j8xmNVpJ9i3iyvz7UYbfSkjvEBsD4D9xfZFuN-RPAbuJSD3zSm_6BFNDEWL8k5Aan3rA3DSf_FR7Sk78ASu5rzF2dZ9wDHUCnREmGa7Eqw_A2f8IfQOuZ9oh-nH5xFypjKIYEd_b5WumN10Csaj1gzxWSroTcj4Rx2TiGJx3CbxmtNNnV3oI0IgF-qpOe2gsa-fKbk3PD1ngjXdhvwaazlFIjO-LdLndctG1pMdpgkFwhgyAd-6JSkvbMdGK2grm9IuRZWOdZK1dD8sfsnRB2z6JlmaK8TDZZF2Dqb3kwQ_stUuE3wHoamz5SDjb9XvKuxNzUqidhbCGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تبلیغ جدید مک‌دونالد برای جام جهانی با حضور رونالدینیو، یامال، هنری، بکام و سون
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90710" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uriGIQpteoUmwheyJ9goQk18faJk2XvYdqioPMg1ut7d6Fu8HQb_Ce3QCt_2ppzXxHoOGoW1JOxPUEGmxiQvNDCB830xxEeIu5dRIkfcFNpf5g2A0bUH6kpMw6vxf6_Mwmsf65N9dqEOBeo3yr3tOq_yJIapPX5wDMwHhvP7z_ySPTklmNEHEesk0dd7snLM1OPP1uY9slhWfg5hxjmeTPbaDRuaUPsWxX5DGTIjGg59YJsHECvELJnZIo1B9KHA7LFdqDI7A9yn_LWqU1yzOYiACbZp2Qvqw0eHWtxZqkaWlKmY_NKnOaa_Sz23FJSlJYzP7XViB8TiOJY3yXT59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات
|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90709" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqBJDtOO5gKhNbgVACXewJBbsFcPFVwwcNORaEaAc3R7ve3bTIg2AR0zOmlEBKrKrGSiVfskVPQ-HGQD5Ef6GiYg03w5tJ0Immr9brbC9H_JDiwmk8OiPDcFnuWTSfDwjkHnuseuo64g2SFlH50ZW_vJFJvsCOUXJ4usKzK22BPJNLJcIvuJSXQp6JEImorAMxr-1aO_dcU08cnh3YkL5qji8_6WWS4m82g-Qs4EBRhU0xWNhp_O3ki1quWpWjbD_RSXIm0IorBIAEWLvHQm-ZX-D-YFzPwUlVwd_iV29Nqr9lImifLTUfFPf2NZy8-EveCtZqjwzxhA7PIuTXyRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی
#فووووووری
ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90708" target="_blank">📅 16:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0OFlijzPEP0bboK4pLx3gJ6dwEc8B07sG583Q2FeBRpwKAZ4DUAQUraFkFpMy9ciYzJ5K-2fqzV7_ESyQGh0BGHT16Wt6UlCpiC-tNA0KzIZdyZOsG9yKNKmw8Gd_X5-ZfdpnJPNbArnzALpHZ2-16wUIm8JFbcFFQGW9iJQbmSLJI17ZR-fITPk2IQjGiusUDf_90EfsrbE4g1sZ9xEhjpYCE1Bh5EeGz15kusyqwkoGtJq4n6nY8a_wTKNVr0HBmxienFDiYZM2pQVl2wjEpD1wrp8Z0mbME8CIMaTCR8CXRNhTmMsJpauRGti0QRq9NXM9NwUlivNP0NFs8KCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منتخب فصل لیگ‌برتر انگلیس با رای مردم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90707" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLvTRliOMJIAWVSDEY1-8aSnbVSVLzq4qsHT8rPuN9mOytmWZCTqzetXfbi19TpPnT1qcSDr_ea8WSc5g1LVtUrA1k_cgnKiQTFVuCmInQq-xWF2pYJB8qYKLF9Wh3gM68EZ8JXzd4Q9Fh9xHPdIj7s07QH-CHdlYfJ0OdU0jTALbUQZ_SNith-oaPhMKanjwNPebYvB-BCXm9k52UiTT3W6X01CTTU0SsGrOWIs7EePD5RxhaO7gdsH7sV5GFZqzkNdiCt1VlW661i7_rfBQKHwbib_LrH9-nI0iHPPi_cjvHj5OMBsuXxbSAP9u5HpKtrnCf8rB1whZ52PMH8a9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
عمر مرموش ستاره سیتی هم رفت قاطی مرغا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90706" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2XnMK-l_hNXBNEcWVF3_iFS5TdYDcLivqd8A9bHpsTq7qfIsE--vKd8KOx0lp-nlzPtzYSYN3LvbjnXVmW10ngNsp9CtoKhjcKrhXS8dUfZzhAzBNMKMjfNAEsWmfRAKMwvErab36m2AQEP-wZZWe43ahpSHpDs7YsQskhrM_8HAm2AFSCo5KGMmzr-O1A-KaoJud8kwkCneqM73JuPMPFYWfzj0pYJHs4pG3hhs2hl48PnbTpqbUSp5CmSf2stvF0qfaZxP9hXFDWb4QK6Wib4D953EXrz1Vnugxc6op5FsdpQHFMa2k7lejsa42xMhmeAfnr7NfsDdKL_82G2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوار جام‌جهانی با کسب نمره ۹ در سال ۱۹۸۶، رکورددار تاریخ شده و‌ تا امروز هیچ بازیکنی نتونسته در یک دوره از مسابقات چنین نمره‌ای رو به دست بیاره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90705" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90704" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/90704" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90703" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geiGfV7rtPM16Ghc8FgFYnnCAqVx5PQsFJK4L2Xmsqf9dyKfk6t4kAJSPThDZchp2tzktcayd0YZN_toR0H4eyMVCFw4zwoUxXaMAXBZI9NpsebNK9rIGyYIY9gNSb2YfWuxhhCNyI6ggUQGG5JLTu2YDxEXIHsctRFyBkEQKEvnsF-V1sMgbiSlpc780jFspoWcKJsulMfHfUZ0vT3orDdHF7S6qr04ztuFW7g9nW4Fc5Pgf8p1Cc03SYtA4LZ--DDVUFhGx33Wp8sBPXNXysDUr1_b5J_MuUPuwlyBWzzAhtOjr_0BUaJ99Vafm0q3GeDOl09RQ7gvjoRtRoCXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👀
اتاق شخصی لیونل‌مسی در کمپ آرژانتین؛ مسی خواسته بدون هم‌اتاقی در این رقابت‌ها باشه و از دی‌پائول جدا شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90702" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90701">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=K8bEwV2GGt_n0asNFgxzXoocCenM9umPdMs7vD_yPLWhJvHSP2GzhoeSBIf8h2QPNN8_boHLR6LIx2ZFa5LlHtNYvU2p8pWBobMbmK8danAXjItnHo8OMur5uL9eJDtokHf9mhihigjKvdEi1u8lV5lj_2SAjTbuh2tkk4LEfmCAYmxxHh1LwohJGmh5byTyA1Tdd5WOgWqTaBKJ_T2sQaKbRWimP-b5bxXJ-mgrIeGDX2_lh25iZMidSZvAIo38n3Xs-NaLnxULzobsJVPvnJtSPIoFwJrkLWSgPDlaLyOdntlYuExW0XJYe2SI8lNOL14Hr74NGyYuErx2Gt4Abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=K8bEwV2GGt_n0asNFgxzXoocCenM9umPdMs7vD_yPLWhJvHSP2GzhoeSBIf8h2QPNN8_boHLR6LIx2ZFa5LlHtNYvU2p8pWBobMbmK8danAXjItnHo8OMur5uL9eJDtokHf9mhihigjKvdEi1u8lV5lj_2SAjTbuh2tkk4LEfmCAYmxxHh1LwohJGmh5byTyA1Tdd5WOgWqTaBKJ_T2sQaKbRWimP-b5bxXJ-mgrIeGDX2_lh25iZMidSZvAIo38n3Xs-NaLnxULzobsJVPvnJtSPIoFwJrkLWSgPDlaLyOdntlYuExW0XJYe2SI8lNOL14Hr74NGyYuErx2Gt4Abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇿
🇨🇦
درگیری دیشب بازیکنان ازبکستان با بازیکن کانادا بخاطر تکل خشن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90701" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90700">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG3A4q24sqn8K2swtcJqojuOR0skONuu-JMrM0H0GoztsKZ_zsxub8xRGVnynvTYKD2FPNBRkqAYHNn2t7LVh2H17FcVWOlAiKx6xE-6TcknLDMzJSWZWMoLF9BLFASF-59iOFMM4Xb9mbN0PzFf3YwPUweHOXAcpHcmwTSxXfyyj_Xgl87XIQ3p1Our91m7oNKweOsDtR8aoEzTgwKXLscm-5Vbj6lNtgentzqzxQ968oKpYM1JB6MuzJvddQfGcz2wizAmMwnaPVqCmFxgwqfVEEd8eIDXu4xkFl8QBM6lxw8EZHG65gXJjtuGwgbNUnEeS37GUxnkF3vGP8601w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
یادی‌کنیم از سال ۲۰۲۰ و شاهکار پدری در سن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90700" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90699">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=sORIf3v6hoM7RjnL_FKL7Ctj1taxkNp9ZWtYliCfiKMLPGWlTVZbWkD8USewEc0mWuQMDjkVdafI0dlQ6O54bohbRMuPdIy67cWSQk8cCIQriAQBg9Vy7iqxSlAxAN6rK5MnufLPfsqwdVgpjLPfLrLLWlyc54ZUDvKsHXwXjsFWrcvC8HdMr7kBByACORRmrzyr8NEpoLRRjj3Ua4-ATZRorTZROVf4J5jTQ-MWxy1JIlQ_VkWJwC1lnDWJ-4YZc2ELM8GH854P29Zi7pM4Db-X9ktoHD2HXsM75BcJQ1nQylNQKRdTrnbYYBuZOaxd6HCF-ALbu6qehanQy9FdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=sORIf3v6hoM7RjnL_FKL7Ctj1taxkNp9ZWtYliCfiKMLPGWlTVZbWkD8USewEc0mWuQMDjkVdafI0dlQ6O54bohbRMuPdIy67cWSQk8cCIQriAQBg9Vy7iqxSlAxAN6rK5MnufLPfsqwdVgpjLPfLrLLWlyc54ZUDvKsHXwXjsFWrcvC8HdMr7kBByACORRmrzyr8NEpoLRRjj3Ua4-ATZRorTZROVf4J5jTQ-MWxy1JIlQ_VkWJwC1lnDWJ-4YZc2ELM8GH854P29Zi7pM4Db-X9ktoHD2HXsM75BcJQ1nQylNQKRdTrnbYYBuZOaxd6HCF-ALbu6qehanQy9FdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از روزگاری که مجریان و مهمانان ویژه برنامه جام‌جهانی صداوسیما برا خودشون یه پا جذابیت خاصی داشتن و کلی مخاطب این برنامه‌رو می‌دید...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90699" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lci1m5TR6i2a6ZYTkAGIneiZbOaRrRGe2SrwAsum4nBPUIJMIvrnLB-bXekvLbtotLc4HHi4DSt9LF1ShBuemoB_LccH8p1XdXVIGATxZBWZQEH3H6blK6iDqg0lhboEC5jUutC1VTEcFuGajBCXwRlnpeE2VZV5uRQnN0ezzJEEblvCHICh-XDFrO-RQQdX05YO4WbsaRBXZq1asnNgolK19a4gRvTOWXBPywWdH8fsKgLldIlcp_przO9-JLXqkqhpQgP7rcfqH2dL-jDoLrzIFX0QDahSFY2rtpsoJRCVRbqD4HyQXCwkgdpXxXsmQ6NIqOackaldZnEmpAF2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🔄
برترین پاسورهای تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90698" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛑
تنها سایت روسی فعال در ایران که درگاه ریالی امن داره
💎
شارژ دو برابر با کد هدیه
IRANBET
برای بونوس ۲۰۰٪ این کدهدیه رو وارد کنید
آدرس سایت فقط با فیلتر شکن روی سرور کشور های آسیایی
👇🏻
derbybet.org</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90697" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU8CwyjIOiesYgaa4ZCd-lgLdfn_cVHxXTCZ9umxDePjY7YmHh8fiMGJSphhUhAXSeJBRzmImf5ZpuP4LRnuQYHQK52TUKmOmAqY7DJj5XU1bDZN1y8Q1PTbt_JzFXsiA9MBPfn-yB3AzDRO9Onf5r4Q-opke8173_Hpus2ip-VSkQqi7tvzVYTWIn37On42EmQ6N9KZ7bIDKW3Rn5HTAG-TBAv8x1mvRTxeo040EL7v3FcRUNZeRtyorPFFqZR1mEiMmENSC_zYH18umHEL1Dfy5wo5iE1tHZL6b5rm7Xn7Wi8N1WuizOJim2PvMoghO0KdebVfp32smpFLzJqVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
Derby Bet – تجربه شرط‌بندی در سطح جهانی
━━━━━━━━━━━━━━━
🏆
دارای لایسنس رسمی CURACAO
💳
شارژ حساب با ووچر، رمزارز و درگاه بانکی مستقیم
💸
تسویه‌حساب سریع، امن و تضمین‌شده
🔖
آموزش گام‌به‌گام برای شارژ و برداشت
💎
شارژ دو برابر با کد هدیه
IRANBET
🎁
100%بونوس هدیه واریز اول(
شرایط
)
🎁
100% بونوس هدیه هر شنبه (
شرایط
)
💈
آدرس ورود به سایت
⚠️
💈
دانلود اپلیکیشن دربی بت
📲
💈
اموزش شارژ با کد ووچر
👉
💈
اموزش شارژ با کارت بانکی
👉
━━━━━━━━━━━━━━━
همین حالا ثبت‌نام کنید و تجربه‌ای سطح‌بالا و ایمن از شرط‌بندی داشته باشید.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90696" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gra0w0b91S8siP7EqADdm_lZc-mo8fZZf7x6NIMKPQeHugeOlAZSAesUkEOzSa9IhZVLZ2EnmFlwdwebsz44FzOG_ZBTx-2phOsrSRoVkj8y-oYKc6a8LhfzEPpx8GVF-RtlTqc-4x5AwmcpNFP6LqJimcppFHauimyPGsVzMQ0Jkpdhj1MAa0sAXyYk5Wc2b5njpnP1sghVan5CL0Zwl7LYVb4XFHoEyjXwyCP1f6L-AFn5KeQMYYREDogKBxjlBTfGEHbbXRExFl4RLWkg46AM-EX8C8MMbfj1KuavuT2OFAqrt2f4M1UoqPpxxvolt9o7HOiXK4wt7kZNkuYLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
مکان کمپ ۴۸ تیم جام‌جهانی در یک‌نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90694" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90693" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuIbWHGdl2qMBoMClGum20-MVNhFjHJpeJKfXGjBDYCzZL7ex2wrHCFhceRIpxwCvOugyPpLNIDJJDuC-3_4kMxKT8TTo_PeO9fVnB6U5cThv5SGSKRFScOqbhcXeCl8A3D68H_HtDlOls6OvcvbGfVxu0MP3HWoHR8DB3bIyl4BtIsD6ob6bFa-7ISxRP5GFA5GsHJGOBgrSAWjy2--WuZvbNgQ3JBzob3XhXdqzNZ89WUsQeCsmMMTy7KwezFg3F-z5TApDyNJlh4yWmGb4SJeQ1ISZrms5W5wlPuFs9yQVT6ECtNKyWPb2j3ZNEJYfYresk0gB9lv_70Br8lxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
با اعلام رومانو، بارسلونا با پیشی گرفتن از رقبا حالا در آستانه عقد قرارداد با برناردو سیلوا قرار داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90692" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRplIo8vQ5AZSLmv_w9940NbUKXrAgowdNK7doQtmLgxRWQRFSqVRM6y348BKXaTWEmZl1kTofBnZf7EbQUhHO11OQ63bPKp9-G2Q7MCJ_Dm6brOOqqGTUwROIZApa_xsgg4Q36K4hQDSCYxnMIHIjO2E7UlFM3NWe-6Pv3sD09wBf8k-lZtZ0LTEowGe8C27413ESCzRh-4JKbOuO7nr3lHgOXwNA_gduvvFdAiaeOeQi-OTn_oKBVWJxeQeEWyOnJ8vfQKyptwJm1wNSmucqkb8QBJnlsOBxoRoVHcVlo0gJpuqHBt6JiRpCBksAaDghTvnpSVQ3zu9QhiNh_yIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه آمار این‌فصل مثلث هجومی psg و آمار لیونل‌مسی در سال ۲۰۱۴/۱۵
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90691" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCQz70FxJ7dfSi19cGVmgyz2jyy2aiFuJw2HevPJQmr51S_dO5Xig4E4lIEDx-3JTDXvVfKkDdwAprLPdpzwKo9hmJ9h8sTF3Ou4sG98vSKUENrkCqIniBrBndjcud5tCrMtH6-olK-BXA4xCLgCMI58F07D08HHQPYey3lZis5g94JNPRVVeyUivwf7b-4AhcigezAgzxIsPwupaWfycmCBu0eXXHgz5xw4u6jiJMG647FUHM-RgmHX-GieAPqbd84iIS-T7udSgbv3ZK0gv4eCL8wgNCjtB2Ml_3FuBheZi7On47cShWHSh-rpFjVrX-ne0ewALXUkqYTmKhao4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmDMb74YtT7laRg47hlcS6i7NWL_o7AchfvQCI46krVT16ObHCsn1QC6YKiRZf3It2DsrUX8UeAqmT8B4omhDtz4hV1FUsNCqjuQiV2i5GmraGJIZW37mi7RQcBjHdkkjoH_pBR083xqLuRjV63ZRbJW2Na2CwzLZvIsR7e5LpBLA79RBiuegfOz_IRzTsysyNO5laFbZdde0VolOrbtU5-xKSh7h3kURkmh5J4IzfLdGQN2vtAKuEWKR82j5kNndAa_CWbSeadT0aTcXr_nw6-b6jHoG3tkbXNPlu0BoiR--AXcw8VGvd5DP2tyLT1IbEbUZycgTZFSOWc1iAge_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iutR9XB9Z3ev-04UOBSgcC_wGkL66pyJjsQ2LbRNuqpEeQVC-rtzRPr9VEyM1mzWXyEdFjCe0zWUR0H-NCdJsoN_lcWkqmgIyqE0h8YG9CIBpTX9W6eDD0ZcUA7oOB4_jVNVa9p4tjvdVyuMa0z74zlKlsgP9sAFwULUMII7ehIgDeWoIG-EonzvpJjdFAU0lm9_IOKieYLgdrdCmUEUOGgDq5TH38DU_bMpXI33vPhEmrl-EpHrjBNP0fzxdP2PyzT2pT1-FCEPb1UwmjdjUsDUsP6Sq8IMcvGyN5z_-c75AGyoG1T_MIcXu05m_ckynuc0qP5lOwpIdhHnW9tPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=OtADL8iuQoK8ZT8XTgJ1YMSlAhYlZw-Z0rPNEzgX2fc-8ePKucLCID0tt8GBMxAzrf1fePfmcaq2aOpP41gelw_FM1LL-a2IdGRTNJVXL_kbV2BS28sVs4tQYysAHaOyDlvgO_73kJsC2bFMQ9p3XvMZ7aCzm9myAMJ3RiDssqMY6hLmdtYH4PLFaCRAdu8HuGPl2U5nKhHfy2TYfHxWoGEIwzMCf3Rc7SRKbtA60NNvJGxqZ6Pp43T4FuKK_PJx7BCAo5Ukca04ezL6ucBr8whe6NTecW9sMp5MU6pCehu8xf0GYWBHB2EV8bEAfbP_hcAodoV0TaAQEHsaSlTMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=OtADL8iuQoK8ZT8XTgJ1YMSlAhYlZw-Z0rPNEzgX2fc-8ePKucLCID0tt8GBMxAzrf1fePfmcaq2aOpP41gelw_FM1LL-a2IdGRTNJVXL_kbV2BS28sVs4tQYysAHaOyDlvgO_73kJsC2bFMQ9p3XvMZ7aCzm9myAMJ3RiDssqMY6hLmdtYH4PLFaCRAdu8HuGPl2U5nKhHfy2TYfHxWoGEIwzMCf3Rc7SRKbtA60NNvJGxqZ6Pp43T4FuKK_PJx7BCAo5Ukca04ezL6ucBr8whe6NTecW9sMp5MU6pCehu8xf0GYWBHB2EV8bEAfbP_hcAodoV0TaAQEHsaSlTMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
⭐️
یوونتوس ده‌سال پیش یه ستاره‌ای داشت به نام آرتور ویدال که اینجوری پنالتی میزد و رد خور نداشت سر گل شدنش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90686" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90685" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUNrS1enKzHmolvy5MIaM3GGclBiXm7F4YxVqixwmQKlZRPfdDY-9hnRk4C24Bxcsv9YFVeCn_kP55-ot_oAGDtFnOuQW3OOp-kBln6-yAVWsKANicgaLa8XcHLa02wRHWAmpoQAGIVeSnuTLVTVR2qCGyax-c6DNIlAw3NIsR3O-4FS7hAgHQqdfuMMy74vWpqcjCq6gjYqOfe_-V_DxMZiTD8V2oenpROotz21uD7oXaKd7JC_41sigwv5OD5nwNAia4EVKEZ1V1pAuA9CN4jZOgjiG8maWm5gcFprsKPk11BMnd-SVwpMMjZmN2JJksGPlvePFe3XYdahzIqh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90684" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do3T-FTQsWUz67_8GIHsPVdYuVMYYeRQHDuvevq8gF0hVNfWUf2F-8kLcfzd0i-7qpVQYXRU6kFpKmZ9d5x0mk2zzTyv498zE-bsNY3_8WamUCTCIVz9QEziYUWIdUjGXp9sJigZ_-UsmwQBCzUPtH1xFrsnuxvx75FMY3S4nW-tXr9-g6zLrZPJ_iYIPogUmdAaron4psw-wK42z3WA4U_iJNElEjtUNIaZ7OXQMWrrKcR0XTxWqARD0iN797pboCZ0sFklsNquEFzuZgPPvUv1a4427BNXjfaKo0VtfsVhh2Xvjh9YC1M8whYFRsRmRMl12HmR6VuvmIcJL-HgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو: آندونی ایرائولا به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90683" target="_blank">📅 12:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoENc-eGKx1AtlZi4EqT_JAYLhJX58r_bPM1yQW-qMQON99M6CHMbGo36eFjtRB60J6OGOjwGHqT9e2Yadi_sp_ODTqaGe9vs7Ve0RvWh_yc3Y5tr1yCLN7f9QFD72KbpXk-iQPcM2Gv9MIFq0lygRFf2K0lWYzrUnzLHpgsSwRIKffOWJeVDAkVc4aPZjAaQzAjM-PijmTnBZXmO27kW4DyJPqhe0U5I116t3TkBMc70RDY81jo2WCTSFeH65AK_xwBCG7eXF2rcaTvkhnkf9MS8ajgwcF23hr8bzG0ryI12gO8ryTreCoUdxVAG5x-1LP47qWXQJSOy6Zu08e7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90682" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=EWgA-CZlIhtXIqga60I3NiTqRlzhwpXux6Q3gPCmJTGRVw-xTJw6U2IdY8WYKhym3j5FjK7EFbmdK9Pjjp0GQTwMkUAcDhLK3g8B483ddk8xLuneUWXlnVISkD379SBGpH2X9wkkWBB5tgjP4kNDgL5RqbbK3rtQL6lzlzEGxZ4PjXWkBP6c1-b62pjxRvGTc0uTsewQBy_zTcMf0zfrMdAPwlVY09XKgoKyxlwAwasDDTKOidrQa-7B0X7FJXsRiQaFW8za-9x8B0reZAL33CaNHZV52Euc4kPdMhx2yB22I0sXxwOoH_glFcbaj8gQkTL3a85x6FEi5U3la9_39A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=EWgA-CZlIhtXIqga60I3NiTqRlzhwpXux6Q3gPCmJTGRVw-xTJw6U2IdY8WYKhym3j5FjK7EFbmdK9Pjjp0GQTwMkUAcDhLK3g8B483ddk8xLuneUWXlnVISkD379SBGpH2X9wkkWBB5tgjP4kNDgL5RqbbK3rtQL6lzlzEGxZ4PjXWkBP6c1-b62pjxRvGTc0uTsewQBy_zTcMf0zfrMdAPwlVY09XKgoKyxlwAwasDDTKOidrQa-7B0X7FJXsRiQaFW8za-9x8B0reZAL33CaNHZV52Euc4kPdMhx2yB22I0sXxwOoH_glFcbaj8gQkTL3a85x6FEi5U3la9_39A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇽
مهدی‌تاج: ما کاری نداریم مردم مکزیک مواد فروش یا هرچیزی فروش هستن
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90681" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic5fA0RBpqAFi7TCD874Oqndqq7_joI-jXxAvOpjYDXRlRD267jihNyaPMbNpZ99OywphbX374gf0J4UIK1uAMVSfmkIMcMIzTJdb278NpVdghGIsViWRMs3F7zRfvWb3IreVQT-F7U6y_5_uIECMH96kg6AY2PEflmwe0Ah0OMHpOkhTmfNGcKOOcD-kstLtkqw9te4vfnOfXqFHMWE8PI_auT45LoCpE37CUel-AW8rjTuUVrSgWi44TPC0ePoJRxNs-N22ubIxUDFJlxvpC5gcPRaZxEGkEuXH-ismmgS3b9RMe5qrY8X_5mhq7MlqIh9R8FX__ZtXFiDMNeIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام‌جهانی رو از صداوسیما دنبال میکنن باز باید این دو تا نچسب رو تحمل کنن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90680" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=S12tzLV_6AMwS9L8aDNG0cJGSoIuS68DPaH3Huq-T26tQG1Ko2B-anERr0l6K5OXe8BrSZaSyeh0QTe_Jf7O5jEhSsrBiKYJ_CofSF15tmrRrRIrE4yHXuvZVJw7ry5v1_kD_eAzz4d29e1KHeT1sAU7JFrCFSSTMgarMli8OxYAj0Fvr6aU4sAQStbQ0fyDbbEdXKT9LpwH8zG_6snHoyH53_3Ak0k1XCP_wHxPWe5FLAh-85yd_zIcfkJm6tRsVFGvy1AAahXUDluXgjAkXQPLlj7mKvUi6ApRX6az_R_ZLGJtZSot_VQ5ASAa2m-gAGdVgmIRKi4iRKu6XDWP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=S12tzLV_6AMwS9L8aDNG0cJGSoIuS68DPaH3Huq-T26tQG1Ko2B-anERr0l6K5OXe8BrSZaSyeh0QTe_Jf7O5jEhSsrBiKYJ_CofSF15tmrRrRIrE4yHXuvZVJw7ry5v1_kD_eAzz4d29e1KHeT1sAU7JFrCFSSTMgarMli8OxYAj0Fvr6aU4sAQStbQ0fyDbbEdXKT9LpwH8zG_6snHoyH53_3Ak0k1XCP_wHxPWe5FLAh-85yd_zIcfkJm6tRsVFGvy1AAahXUDluXgjAkXQPLlj7mKvUi6ApRX6az_R_ZLGJtZSot_VQ5ASAa2m-gAGdVgmIRKi4iRKu6XDWP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇺🇸
فرهاد کاظمی مربی سابق لیگ‌برتر: وقتی شعار مرگ بر آمریکا میدید دیگه نباید گدایی ویزا آمریکا رو داشته باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90679" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=rAhZPB2xCJX1_NEBNl2QEXFgeKlVmfsLoh7yrOdzlFOYbyr9-hkeY0o9ambVxkK0w__BxLC5-6XdQx7UVtZEa8MWCVWt4griiPiNJFxzS4yin41XnrMJ_WVWY2im4okc4O3gpTCwfj9z-wmNTgAdC7nNszu8dL7-SWaDWNdjprhLX5i3iqb4OlrTskYJBZ3zG2S0jar7k1dn_R-2Ca6mN6yZ0XimABfsDAj53sWDmKl3dyh37FK19xc3B2tVjxxWTmqMXGkhxyshvSeDoIka65kz5rUym8_RxH9w_fnlLR9arCE4tRT6wH20mMvAHrBZEdqqZ8vm0LhiAdnpz0WW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=rAhZPB2xCJX1_NEBNl2QEXFgeKlVmfsLoh7yrOdzlFOYbyr9-hkeY0o9ambVxkK0w__BxLC5-6XdQx7UVtZEa8MWCVWt4griiPiNJFxzS4yin41XnrMJ_WVWY2im4okc4O3gpTCwfj9z-wmNTgAdC7nNszu8dL7-SWaDWNdjprhLX5i3iqb4OlrTskYJBZ3zG2S0jar7k1dn_R-2Ca6mN6yZ0XimABfsDAj53sWDmKl3dyh37FK19xc3B2tVjxxWTmqMXGkhxyshvSeDoIka65kz5rUym8_RxH9w_fnlLR9arCE4tRT6wH20mMvAHrBZEdqqZ8vm0LhiAdnpz0WW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب خداروشکر تو این مورد هم عقب نموندیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90678" target="_blank">📅 11:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reAFRpq7RE3zR5Lcf23NX6YjdO-XJ88V37JlBm-ZXlVgkgunCSy1TpLEa1nlet6lD5DSyoanm8aitE5ulkePyqTTq1djAjIQibsMUWjhwekEMNnRIhggpDYh_9mBPDiKFMpscYGJOryACt6_Gmtn5xIBk8qBJ1YhZybQXDfoQvGzT8vhlDO1vZxlMM7RzBLroCRMeT2TvwNHjEbYApKbcbJ2RsyjjQvDuR577lTN-vvPVc9ksS0xWXrEnguzmIL_dSZTgKxbtmtXdomvXeORcOXPyPac5Txbz4o9EgPC29MUjZxEyt8YxTWqYFhX4-mBZ9vOriteFu4gCQtFZUMWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKxJVttTPSN5we8g1DznA3Yav4d6AQcoSw3ipFPwQ5cwHmNPBs9zWZeY1nyXf4GRS4QDZEQ0M6blMIp9kO2Ftn-YUmrIUXKyKOnXROk8BOyOjJ4cT_1WFOcC4W6wS3pVAMuY12-WMOqUhDPmwRrUyomsjXCuLc1LDf0WpVqWrjY5h8AHJCrca8tJon_AZXI8GhF2yiBBDuG5omC6xYgiM0cNR3B-DFCgDImaW21ouJ-k0S0Y8BduRIkGWoCC0Y_3S_-BqJAlpKZAB4TFezmKh-0G9rS-aRjIMtdH7gQPKeMwF-vqwZKNUo-jVzB-fWplP2k24CuAdL_SVok6-AbeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0Zm8k8vIrMAN2C24lgB7nsiqT1ZdRRH9pO5pp2o2X_46OTX82XcbQEbXWpUMlKnYXQnAifaDQSU3p8doZo4GGsz4n2ozXKz8xxR7OcTmzISkEJvLvpxGrkgSahHTpThSGvm8nY5ZJyb-dlH2x8hNSnc1wym5vFP9nrOYKB2A3iY_E4OB1ie0HEddIRg3FviCh9bewphZ8h5CvitFVT1xlSbQkACQgraJSjh5ttQ3uUq0CLyPAPuxp6TlQJpDo_DkN8TvpM2GwOr9vJ3eL_8F3z7O7AJn-h8AiiHjTiE1Y3vOqJWLNv7jFmR-hnBKdctAwbBW-GESFlfpzQzyB3ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsYg4GZ-_zYgyOi10KXCFtC6GK-4cZRhcXfUxBkVDPgsGvPP9C9K9Gi6wHTaHgcdhwq_6T6ALzMARrR_mQk5zx2UzQo1LUDhizKXn8IC6YZ0qGhGCAJMCUKmOdWWUjJZBPlT1C_Y2H9KKM-c9NFSrh2g8Oms2_j0nOHzUBMGxhabvaNI1yfeYzsNaIM8Ms40J748sueq-xDvAhwg8xDX16MZR6kQIyFFogD8rbzbAPWUGBNMgxxouafJFxtNL-zZxKQz1xdV4h0ReyqdzFyG64yrujny_5qtGEhUlesZoM91urKVJw8WQTxIW_DvfwXSsDrTt-V28w8IhXNK_hXzMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
آدیداس از طرح استوک‌های جدیدش برای جام‌جهانی رونمایی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90674" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=jRH1TCa1jCc4V-9tE3IWxC-v8pt3_diU-lvFBLxvjZMFOndltSZK5R_nycmOSfD585dXkRFpm-jyix2eznWagsi7ESu52m3A9YDuDhcvi_j6BJznu3b8QOWYkx83GuDPP5H0GbY9yMNWbpziCf_u8OUbzikA1C10AcNYuDNyvCCOJmYRmNXmvau1f0wpvXG1Bc1mE8tS9gYxuzf4OFiYHYg_lcKRdlj1y2Qg13SVBNlBi7xkYNI0O4vRs-cAdLfIKiFnJJT0Uw1fA-ru1hPLILi1cUhZ-KbignAdQa6wKNkhbKHtdBN4PYnHEIlsqgWwExyJw4mSgGMVEQWV5id9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=jRH1TCa1jCc4V-9tE3IWxC-v8pt3_diU-lvFBLxvjZMFOndltSZK5R_nycmOSfD585dXkRFpm-jyix2eznWagsi7ESu52m3A9YDuDhcvi_j6BJznu3b8QOWYkx83GuDPP5H0GbY9yMNWbpziCf_u8OUbzikA1C10AcNYuDNyvCCOJmYRmNXmvau1f0wpvXG1Bc1mE8tS9gYxuzf4OFiYHYg_lcKRdlj1y2Qg13SVBNlBi7xkYNI0O4vRs-cAdLfIKiFnJJT0Uw1fA-ru1hPLILi1cUhZ-KbignAdQa6wKNkhbKHtdBN4PYnHEIlsqgWwExyJw4mSgGMVEQWV5id9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بدل‌های کسخل و ایرانی مسی و رونالدو:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90673" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCapssrg8YPXDspG24r7ezquxDe1dzDth2xVOBpFAJ-RY3xfXqlKrea4db99DqmuOWPs7S0wy8obx7v0-sCmz6JL7iwK7LN8Q14ITZ5D1HNpPaoR3GcIg-AxpzYzpM7USo_5vqa6IlhnJDZxYfGxrL8E3bo-kvSEC0td2m-KwKX17o5Jm_7dawMhp1XmXu6V6RAlEK3etYmdWBWZNsQaW-tGbUuVlMLDxKSRymXPa_KZF807s86Scow0f5JJ4SDjC5k4Hifo8y3CO1bLbqDlG8Bm3B9KzkNsZFzG-oPPyhiBW4U3gT4mY1vBAPbBYcjzN0qw0CDrk0qUy67GxkWPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی سکسی گارناچو
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90672" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=jcRuiTBF-ulArB0S4pPMZbJFrHD1pfFAUNlHF5Kl7gxkvBC_b4DeOgiNB1cXV-vu-hpoOeZeGSKgzBvizCVm0D73FAtZWTId7QrhjbJROj3WPucr5AB_EB8_eKiB0jMCpiww1MlSiu6wcifnjn3nnzFgKfPm8dU4JrD4K7Ge3DCAvV4SIEdgktIGqc7vnBGIr1P1Vf64YYMV2WnrII0QUzKN-fsE5_CWouIon2bTgayrgwjfZmaUHUscHON4vYgJy58Vix2IDKL3xRyVTx9z3UkIR9ec4-3FkBUs9eD1zgpyA0yLKz-y9OU7X3Uc3isw7vNORe4XSmAT1iBfMAG17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=jcRuiTBF-ulArB0S4pPMZbJFrHD1pfFAUNlHF5Kl7gxkvBC_b4DeOgiNB1cXV-vu-hpoOeZeGSKgzBvizCVm0D73FAtZWTId7QrhjbJROj3WPucr5AB_EB8_eKiB0jMCpiww1MlSiu6wcifnjn3nnzFgKfPm8dU4JrD4K7Ge3DCAvV4SIEdgktIGqc7vnBGIr1P1Vf64YYMV2WnrII0QUzKN-fsE5_CWouIon2bTgayrgwjfZmaUHUscHON4vYgJy58Vix2IDKL3xRyVTx9z3UkIR9ec4-3FkBUs9eD1zgpyA0yLKz-y9OU7X3Uc3isw7vNORe4XSmAT1iBfMAG17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
🇸🇳
ویدیوی جنجالی از بازی پریشب آمریکا و سنگال که شدیدا بوی نژادپرستی میده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90671" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=fWzm4_niH-5T_GfiiZu9xBqhOzwk0BVZSfwWABSpPa0ui5lOdXWqcrPiqV2rOwRzGmuAn3dpmzlpiGXriE8ZmTw-d1yet_nkp7vdpSD49rBPNVsTQ_m3Ozwl9v7sRB8W0Yxd_8LDK2q-IC01qQMpwWh6MoJsWqMWNySwnUcuQJ2CWklMfV8au3Dp8GIVytaafpuZo_8io-JQijSDRPWspGLTTyZIVWL9x6U32HR-twiwJMUmRzkTIKcABF2zzJxmB3BSeJws1RsPU8r2ZgYIR110yJeHaLiJzrJfvCeUVJi1G9V0MZfxTKbrGwo4UP69-Xsyqy8U_5WuPGT9kX3Lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=fWzm4_niH-5T_GfiiZu9xBqhOzwk0BVZSfwWABSpPa0ui5lOdXWqcrPiqV2rOwRzGmuAn3dpmzlpiGXriE8ZmTw-d1yet_nkp7vdpSD49rBPNVsTQ_m3Ozwl9v7sRB8W0Yxd_8LDK2q-IC01qQMpwWh6MoJsWqMWNySwnUcuQJ2CWklMfV8au3Dp8GIVytaafpuZo_8io-JQijSDRPWspGLTTyZIVWL9x6U32HR-twiwJMUmRzkTIKcABF2zzJxmB3BSeJws1RsPU8r2ZgYIR110yJeHaLiJzrJfvCeUVJi1G9V0MZfxTKbrGwo4UP69-Xsyqy8U_5WuPGT9kX3Lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇧🇷
صحنه پاره‌کننده از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن بود
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90670" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=UTpavNak0-4Bqha0u0N-0v4VN2s810a3DLYVZTbC2qKgl6PBgK_WPYuSmTKrXSecEQfWlpA_P4KCfdYZWLwJ3xgV9sSOZnBWB07RPgj_T5990esPdn7tNo3GxoEJ6gF-O88gz0-0TTiHz-nJuaT2SEKEXIz6-M7ngJrIVN3Oa5YNGN-lueVo4FicgUOdJrMvFLB8hrbib56_7nOntKaAuCTox9tkJyycV_MVt95KMZAapSEbfzn16OVH5Chf7_Nmwf6s_qsPVIurSjjTTO7Y_xix05Yy7Wt7NlOi0k9D9RHH7cIrhzLrcs6E7pHi16TTBTe1_F3X_n0cW0_GgzTlsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=UTpavNak0-4Bqha0u0N-0v4VN2s810a3DLYVZTbC2qKgl6PBgK_WPYuSmTKrXSecEQfWlpA_P4KCfdYZWLwJ3xgV9sSOZnBWB07RPgj_T5990esPdn7tNo3GxoEJ6gF-O88gz0-0TTiHz-nJuaT2SEKEXIz6-M7ngJrIVN3Oa5YNGN-lueVo4FicgUOdJrMvFLB8hrbib56_7nOntKaAuCTox9tkJyycV_MVt95KMZAapSEbfzn16OVH5Chf7_Nmwf6s_qsPVIurSjjTTO7Y_xix05Yy7Wt7NlOi0k9D9RHH7cIrhzLrcs6E7pHi16TTBTe1_F3X_n0cW0_GgzTlsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید هم واسه جام جهانی آهنگ خونده
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90669" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puJm2Hsa2-K0zQ3HxkfzO5cn3PIWlnMXjYQUsJmxAs8kLdtl-CZ0wUFarLdgv92iY6kqBtKyaWj15dP18P8k_oAie6Uf4TKKqPQFLxcpBKFA815Slo4pqSF_FTEmtAxgqjIdZGeoteOW6ALYH2SWUb-3zvuqi8WANe-UqI5QRhztWTtY1rk67LrBXjWJExf2kNVvZnc12lTuiYTsyVEC89NoYdI9ciQa9tkHUDU6HczH74vVohWViUF6NvYe_pIDnQg_u1O0JnbtDtBWry7YO8RNRUOZryEoQLgDTVjSjQ2OGZgKGA7zCKQRaT6y1UpLsOG1FWghK4x1mFhiXAncHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول چلسی در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90668" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGBI-Yl7RfGzWXN6JLmyQX3kxPSMn9vfo2zn1AFJ-q7SmZEeNmVzjIzqx6LF5g7b84VL7QhkOcoDs2i1nngIrsoWZHLkdZSsTCyNYgmQyTNu12TEn63DNHC-osflNI08mQjM6CVFk5Ds_FwAEOkFBjy09J_U2WOU2WkOVIxCh7-tHTlY4oegRkmsLvMsg9wZn2FcYqsM8d8hdl6XkWHKkdK-NdQNznGWAupSlkpUbp5sJUvnYH1iDyhQjIQAfR4ND36hOlg8tkKQu-6qWEww_ZrWuguC8_dPa2-ZtXuLU6QSa-9goRUFKaU6wtweds68Et9UeGT5MJrhLpQhzGvSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد دمبله در سه‌تیم مختلف؛ معنی واقعی شفا یافته رو در تصویر می‌بینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90667" target="_blank">📅 10:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=B87iQ9NkhRw0JjgEdn2BXD9CgeYpP4wb5zXIfp8jfUhnyYc7dPRS_bc-IjTZgeA9M_fAaxexEufQJN5eMcs5azBXKxIfxR65weJoNRPd_LvueqLlDdc0BjWAQlZAMWcBXwYyLH_766KfLfMgSfO0TUmgTRzOoPeZ1k9kyNOD_TtMxmWdV27zzziMru97CcZr27CzTiq0ZaMQeNdCLtl8bgQC8V_Y9HZ3oMh1spZRqjKw9CgCR5KxfrFMm0fNVKSH6YALSEsUQWRA-8YZi3Bhnnw-zQZPoz-kp3C2Lg3hIIZpd-aRwHVkmv_s3OtjIu-nPM_m5_X7wye_dRxruraGDqFIuWyfHGdZ-PH9dS6B-e6ToIHuErCVcmGsodBfH7Py6Ni5LS5p32A_oqtwN_NxvIUkyl8jAV4PM0CRvyqM2xjRVXOC2wxE3_p25nN5bX-SzHenH9mAtyRhS9RpKGzxVRhIjIJc0m5vvYbjECLA5CG9JQSZyEFBP8awhiQlHIOe_mAATNksWOvFVGjKttP_TDP_6aDzfkeEAFYQ-8vZFYMH50RiTHa-CGKDu6F1-gF7GsN_a8yMlzvOQ31d6He92PAB0G9YtA39X0JKk1Dr-WGTByPyLeN9ac4Sv0av8Z1FhojzA-IF6ZICxuSdKMyJNnJRQwg5EEkhrB3K18V-tKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=B87iQ9NkhRw0JjgEdn2BXD9CgeYpP4wb5zXIfp8jfUhnyYc7dPRS_bc-IjTZgeA9M_fAaxexEufQJN5eMcs5azBXKxIfxR65weJoNRPd_LvueqLlDdc0BjWAQlZAMWcBXwYyLH_766KfLfMgSfO0TUmgTRzOoPeZ1k9kyNOD_TtMxmWdV27zzziMru97CcZr27CzTiq0ZaMQeNdCLtl8bgQC8V_Y9HZ3oMh1spZRqjKw9CgCR5KxfrFMm0fNVKSH6YALSEsUQWRA-8YZi3Bhnnw-zQZPoz-kp3C2Lg3hIIZpd-aRwHVkmv_s3OtjIu-nPM_m5_X7wye_dRxruraGDqFIuWyfHGdZ-PH9dS6B-e6ToIHuErCVcmGsodBfH7Py6Ni5LS5p32A_oqtwN_NxvIUkyl8jAV4PM0CRvyqM2xjRVXOC2wxE3_p25nN5bX-SzHenH9mAtyRhS9RpKGzxVRhIjIJc0m5vvYbjECLA5CG9JQSZyEFBP8awhiQlHIOe_mAATNksWOvFVGjKttP_TDP_6aDzfkeEAFYQ-8vZFYMH50RiTHa-CGKDu6F1-gF7GsN_a8yMlzvOQ31d6He92PAB0G9YtA39X0JKk1Dr-WGTByPyLeN9ac4Sv0av8Z1FhojzA-IF6ZICxuSdKMyJNnJRQwg5EEkhrB3K18V-tKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
استفاده از گاز اشک‌آور توسط ماموران در بازی دیروز بندرعامری و شهرآرکا البرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90666" target="_blank">📅 10:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpLMXXRTJD4nwhwhlJclpPnXpNlFXZ-YcCUuwHzmX84327PRPzpaTuy_3Ct0eIWuKqcRkm5bxv7v4IOZ7-MXEJ5pQ_G3GVabDyYTL9d7dHhczUjBKGLQ7roZ1t-D99oaAqfv2THMdR-ZQMj2bn0NLoD1cD49kTZA_ruAQuZdhLSlvYZAYvYmu9dcdNpXRhp2FxtNJ0ctJLb5vZC9X2leyGUtwl4LKNK90iy7eUVBj-epJR7xk68hE_td3XI9MiAz-sKfo2nLhojqEjGy9hJslc1Y2qu8TYcwbM3jYVAocPDP0tqgPf-jQtuCYv3nZb86jrshPtGsevINGx9GqN94eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 بازیکن برتر حاضر در جام جهانی از دید FOX
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90665" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95b443280.mp4?token=Hzx7CpLAagt1zEzLEKLv64MMGwueBKqDBql_3Cb542EpwkFsqmAnSNesd_g1VZzUSog1tOjcFPkCRyo7Xp8Aqv_yiLnU-Q8cjJx03VhjttP2HqPpdDWztyFW-E7ZyXoJgthT4z5LwHzyvic-jm2RhcnS4NksMZ1hDmZo8cpBrFR0f78c3j2oXr0ZkZ80VGoyhDoq2LgIO0cnkCbRVpZDORQbvsdAtP1HcuFDH64eq0xajsuZn_FuuKB_GDW5To3CjmJonRb0ZhZewg-3yzCIfURl18p7rucvjh_Pk8wKhoez_FPlimQQnH2tUyUh75mU8l4rLwz2paHtkgq9wj7zZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95b443280.mp4?token=Hzx7CpLAagt1zEzLEKLv64MMGwueBKqDBql_3Cb542EpwkFsqmAnSNesd_g1VZzUSog1tOjcFPkCRyo7Xp8Aqv_yiLnU-Q8cjJx03VhjttP2HqPpdDWztyFW-E7ZyXoJgthT4z5LwHzyvic-jm2RhcnS4NksMZ1hDmZo8cpBrFR0f78c3j2oXr0ZkZ80VGoyhDoq2LgIO0cnkCbRVpZDORQbvsdAtP1HcuFDH64eq0xajsuZn_FuuKB_GDW5To3CjmJonRb0ZhZewg-3yzCIfURl18p7rucvjh_Pk8wKhoez_FPlimQQnH2tUyUh75mU8l4rLwz2paHtkgq9wj7zZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از لامین‌یامال در آستانه جام‌جهانی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90664" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgvVdhazVGsNwxe34V0hwI19dx8E6v0qRy7ucbCc3idY_zADrMy6pdBBu2O4MLZVOEMbS3G4BIAsXU2nc4SGRC0R6J8Z79fzdjHIEGE5uc1mGzdI5mfHX3IeISbxOusyxSzSfRqmMXmGRQmIk_Gx4ScmXUGFz3qHgHB7GJycTRgpjQjJrnlH_4Ev5MNbQX1DwdGZc27SSUMMWThmBkKlZ-sxJcnWXzidW7himQ6cqgoUncSRWqOkiqbxd-j_G4rPPvm8O4F66t8TLHJ4xKrUdZx6ACyoMnrN1HnjUFCz49dEQf6pyjoA-JM_hGiS8AlxADmtcZ4RZC52blJGgl3aAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⁉️
🏆
پیش‌بینی اوپتا از قهرمان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90663" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
نماد کشورهای مختلف در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90662" target="_blank">📅 09:33 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
