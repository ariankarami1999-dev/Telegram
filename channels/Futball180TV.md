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
<img src="https://cdn5.telesco.pe/file/m7C5MkWIvgY_2OSkIc2S5LWwZzmxepfG_r5vhUHNV-ZLeWKAKULt7jwxK40y5OuFioqr1mKyhDXv2-Edh2SZaJRGXBprZElMeguQ_38XBNBVr9UxKE5JbnaOkNtqN55RaF1yv7UsJGihDH9zwpaC1BgHXo0nk0VDQKccryTX8pdNSgpv0Zp0EPsaiKm82K7dPmKyccU7OQ4_M3_1SCXloFJ78LSExnm0H8S6hfDk3QYYo16jS7it4HsoX-HSzhrI_CNTIr6LPObh0xCMfwi1I1qp3hnJ8vIo0uJq-7TwYpA4X35nREfBO1BcORgxfnbgBVgeKwVZLQF0ERTtT1USTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 322K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6GsOcQko0QZN2ABR5ay6Yk31gcH1qYZIThg-SGrOy1A5FBC1cWV-tRJFDi6jEyzuq3qRPKQtQrH6LpuGnDVKiB_VTayYoG_kgV7qHTw8PABHhdSsl7g3PCO9XmWhZc6VaFTkpdtNa7AVMCg_nw9rMVnUf6H5VO4EGvEET9QhC65dtsuvZRw_gtvyEmNywRCFT9BtWttK4hx_l_k5hE322zxduRiKaUA9WI6K1apup5IjgTHrHgmrVLDsEPOKaNUwgJn44I3SneKzLZ4cYc6eQE6kgzjlse69b02cvs6xXgLPthU1L_AQCpOd5hXc-gOG7Gp5--YaXGZy4XvzMzYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
سپ‌بلاتر (رئیس سابق فیفا): "هیچ‌کس رسمی‌تر از داور نیست، و اگر کشوری از ورود داور جلوگیری کند، نباید جام جهانی در آن کشور برگزار شود.
"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/91887" target="_blank">📅 21:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5zLeB-kLbJPrnSjcnmV-RHdsDr3R5E9Y-A9QkctfGCcyJsiV1bZbG18JB7MHsFeOeG57jBXpJLllAmMvl3Een2I_yRtyt5D12TKBFkRy6SwsdK1U9VdTjYqAvzJAO7PP8bKeky404TIaZsBKwYHiwsUOaGIkjh7pJUEtQFw0iabojfyIBgRFZUFpAS11N6L9g4l4G5jc9c-RXpAj1ORrWNacqpkPbe00egbbDXFCOj58Y-syQAq-nC-SQhdx0INTxwAQyNkocgK81H2PRoY-rHiGJ2riW76W1yEQf_SFtS_syJUOgueNepmbb1PWsvjl7viwvHhY-YwJErytla19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/91886" target="_blank">📅 21:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
❌
باشگاه استقلال مهمانی اعضای تیمش به مناسبت پایان لیگ‌برتر رو بخاطر شرایط جنگی و احتمال بالای حملات آمریکا و اسرائیل لغو کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/91884" target="_blank">📅 21:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ1rDWlVYu3SqEeqe22jeVQ_wuFoJ-2xPNM1_XFmkpivcSC8dpb4eTXhu57Vf2dYzUr_Qq4HzB3moGinuHR2WX7fDUpk_vL6IQVe4HSxdYc-GEMFBUEGG0WiXE2mfYetXep4wI1lh1YnhgX--mNHlxJOY23xzd274OZz8BrbU7vqQQmaNNIYAwtWWwc1kX9CiEYaW4LCOstVHx-JvzciR6tpTEMRxFlRzgIcE76TEqUWN6l0JutwteUwr0uBH57HLjG3hQiJxMfF_276XVtAjh412WJ_mH0ZI9bXbs8B3gXVg649giEWizvvQ28W5vA6yXAdNAXGIbTvlvbhluH-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQO09vmAcfnmfi7NCzTQ4mDEjuCSeWTIDMFhBPOwxO2QO_uGz8SB1XqLLjHb5HyKyLOuJax6HMOXvU7nqPJH3pPLCfSMh_VvvOBiVq48OB_TH4R45eqqHFD_NlceshI4TlHiCtRvOD3KNU0VaiGGPZYnMUo7ubsUOJ1FUROlSb160CfsgWz_2RssOHRMYRjRHnsrXwUixcNxKGohbJItB7A2w5DRUpOOryvn4-TYomzabOajl2_gMNLVqo0n_JKGkk4mjvwUzh2f_fxVfw9oAn1xvBA6A9IdkgyW9iS_NaE4OCX4wUUazpSWzBjhkrrH0jSTtmGH3y5WDS_JSgOMkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
این یک اشتباه در طراحی نیست
🇵🇱
🇭🇹
پرچم لهستان روی پیراهن هائیتی
در سال ۱۸۰۲، ناپلئون سربازان لهستانی را برای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه استقلال این کشور جنگیدند.
پس از استقلال هائیتی در ۱۸۰۴، ژان ژاک دسالین به لهستانی‌ها تابعیت اعطا کرد.
اکنون و بیش از ۲۰۰ سال بعد، هائیتی با قرار دادن پرچم لهستان روی پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/91882" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=tOm1cExGMO893Gl3BvgTP247J93BA-faZmh2TGJDlWs02U-slf398Fh7sa_pS807QnKblGyF80y5Kv6xYS1wGVmC3bU5aSeJl9jqKM8rPkI6YY8KGbVr4YXPDnZbnc4Vj8tTpRB3y3ROiENZLH5ljsD9mL23SAtNZzE3lwKGZGCJgGiE16yix1NVwu-rIImZiHJbpHnfsqGLJsdzcx3uulyj4_xgcWU65FgSDk0t62uMcwgz8Q-ANWxFA-Gb6njNWjtEw-TYlFAO-Opuy1_3T03_u65myZLlDZErAkv80WosRrl2iX2Dqwbg02M1Pm2BiTbsuwlIsZfM0sr8FjbjQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=tOm1cExGMO893Gl3BvgTP247J93BA-faZmh2TGJDlWs02U-slf398Fh7sa_pS807QnKblGyF80y5Kv6xYS1wGVmC3bU5aSeJl9jqKM8rPkI6YY8KGbVr4YXPDnZbnc4Vj8tTpRB3y3ROiENZLH5ljsD9mL23SAtNZzE3lwKGZGCJgGiE16yix1NVwu-rIImZiHJbpHnfsqGLJsdzcx3uulyj4_xgcWU65FgSDk0t62uMcwgz8Q-ANWxFA-Gb6njNWjtEw-TYlFAO-Opuy1_3T03_u65myZLlDZErAkv80WosRrl2iX2Dqwbg02M1Pm2BiTbsuwlIsZfM0sr8FjbjQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنتکام ویدیو ای از هدف قرار گرفتن یک نفتکش مرتبط با ایران منتشر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/91881" target="_blank">📅 20:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKKmzUfV4_6_wd2qVFLPSC7kg2DwwR7X_HN7ir0OLgZmvUYX7VkyIVTWEkFuuQqTLBzqqufBtnqa5onTdLbnKz3o3Pv8FaGy-j_QCrGOOMoZApgU0l21fR5-9OvuXpnVY67FwNvcyiZJtIpy_7gPRFq6fB6oNph9zquL3EDyp6OGYG_bi9uRVwxOrYDyA71CDP9S2uHSTVWkkuttf3aUNOw4D2MMA3BbjaeA7sZPVlknMkBQ1uYUTHyZFSp6uoVMVMxrerdsm0OTmSJYPFia6fos_55YGje6VJlUxiynx1mBxLGXq6GDEAbARuTVUOkovEjdLTqHoQcDoe8gsiv8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiX1Z7OAfDi3WnGO6hngKrimC117DyMS27yV2H53CoV-w9sYU7TRN-2aY5-2T3jg1CV0HQIEap6Rk5XoxiOZNLFACEUWHZScpPeKwiTtW-zXz-E3nAZ52J10HFqigx4QXZ9uK7qkfs_ul_RKA_H9G73ICUM7SO30nw0zJTzsPnxqj21JuNwAE6Dd3sKcTG07GJcwC5aNRzGI_TqyC1JePYQwx4xHPNgwFwI_nPGc6GO2TT5srJKWH6ufrB4JRIFtgVweSueBvqRiti_3p-6Hj3cZbg2n1DAWsYjW9Phmki--GAvkI7hvwGQihM_1yA7MV82s7zELxUpvYs0V-s1EaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP3RYnI1MkGwE4U4oy0DLLOZGdpD2VCs6Yi3Z8KqUhgnl65HAyAfGHkx8uJgdJ7xu-5WPXt3zCy3h8EGEyMAknf0wzIniFMZJYe79lnsiVpecPp5nM7E6q7mOpuaEejW8ecVKrR4kUIq7hL7JRQyNenI0n6Q3aQg0yQaJS87GFAtG6PwnlKJRu35PVuT9Bf8EsP8LjAmoq4wNYobizBd7CW757V-vjvm7inYLP7Luz-mxzaZSnF7121n8y4ZNPtWV3cClyJz4zzwcUQ2b9jGOg5XLXR7iKB0dJtJfFVJXlenHfgGgRXYEyUHo5CVSNlD2G-1I6Ba-JaiNJvp8le-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فنای جذاب و دوست داشتنی آرژانتین
🇦🇷
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/91878" target="_blank">📅 20:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l81nCQfInd5RD0vUGYviZt25tKvvELQ1gRtlQUF2GUGerZF39Z6itqgHkhOnLU7IaNP3YWEUsj0tJqhWVepncfZoVmDerXoTcReA20ddxqbCX3ujwj2YxR_BeDYq9IrDJ2VhF_HUG2FYv9sMmrhFjkjyAxg6fFSimKDaXOEx8H1a08iqFKPLy51eHeTPJG0IaYTOqm8nj5yFp_W9wvEKp0TUSIoKQism57UNvnTta4RclqYdZfI-EQK3Z7TZYZOpXWnnGwjiKMCXQfGUjlwhWr6EC4VSuaawFkyEMoZFcC3aCpMlbEnlcPKtYmitRRZGIkmGvKkYJyCmJvGtAQoeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توییت پزشکیان: زیرساخت‌های حیاتی شریان حیات مردم هستند. تهدید به هدف قرار دادن آن‌ها (حمل‌ونقل، برق، آب) نشانه قدرت نیست، بلکه نشانه‌ای از ناامیدی در برابر اراده ملت است. ایران با تکیه بر دانش متخصصان، وحدت ملی و همبستگی، در برابر هر فشار یا تهدید استوار خواهد ایستاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/91877" target="_blank">📅 20:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8c0TElCXBvpARAewfG84LActA58gzeX2Xh5UzcNI-FGc495e7UXrkgIO6vfRapove5yH67tGHDml3DYtPBitHQBcjS_EgeirE00-QrAYNm9GNnHUaefvBSPOsmeIql9XoR9i2fikKBGZPAh6kjg_uSdl_z05Z0AZ7by9o-jHK7Fm2TJ_dszm2qnAVoyPKtAhhmxJ_pndIlE51vUX-qVISJdBtCp7AaC3RECRQxVqteImjdW7C-ZeQ0Fq7OC_d7jIvi9ScB_U1OZ1AClYB7pIu9NKxPh9yA1nUFo3eUdrZtjpCiWAf6L8qS5x3_-lcRY80TrZjqHFVbo8ZrZLaRFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رنکینگ تیم‌های حاضر در جام‌ جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/91876" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
قسمت آخر صحبت‌های کله زرد خردادی: فکر می‌کنم ایران می‌خواهد توافقی را منعقد کند، اما خواهیم دید چه میشود، فک‌ میکنم اونا میخوان مذاکره کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91875" target="_blank">📅 19:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/S1EmxeI0jlePKmJ0M2eQ6ZlwU9271ulIIwnkD_MM0e-D1QpenywRUXDoB5nzWIdDte507Kl5kNzWjxTiNiImUrz1mivqcvwpTBzAfnfIPKTVBoGTI_JVfaVRpGDSRgeQFQCa6OeF2CO3Icj-FYPsBvyDSGyr3HdvauyB8Klow2xSvdRCoj7yvvQrqsxfCgBqZEhXkuGNZR3Q3ZOQY0ziaKna0N_VOkLieB7rQEWyXWWXWGTo5mrZZ7AfQtYdqm5CxDF4aOAGecoVuZinXdQOO2_0iqNpnHJ_4QbByoXMsu8bNzxe0MraCplt2ZdVyv5YDFt_JQKaPEPn_wxIoE8n6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ پیش‌بینی جام جهانی در «همراه من» آغاز شد
در لیگ پیش‌بینی «همراه من»، نتیجه بازی‌ها را حدس بزنید، تیم قهرمان را انتخاب کنید و برای صعود در جدول امتیازات رقابت کنید.
💰
هر روز یک میلیارد تومان جایزه
🎮
یک دستگاه PS5 به قید قرعه
⚽️
اگر فکر می‌کنید فوتبال رو بهتر از بقیه می‌شناسید، وقتش رسیده وارد همراه‌من شوید و پیش‌بینی‌تان را ثبت کنید.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91874" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ: تا زمان امضای توافق به ایران با قدرت حمله خواهیم کرد. یا راه حلی پیدا خواهیم کرد. یا آنها را از بین خواهیم برد. آن‌ها ما را احمق فرض می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91873" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ یک ساعت بعد: با خودم تماس تلفنی برقرار کردم تا جلوی حمله رو بگیرم چون به توافق بسیار نزدیک هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91872" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: چندبار داشتیم توافق میکردیم ولی ایرانیا همش لحظه اخر گولمون میزدن
.
اونا فقط بلدن وقت تلف کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91871" target="_blank">📅 19:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ: چند ماهه داریم باهاشون مذاکره میکنیم. توافق براشون خیلی خوب بود ولی امضاش نکردن. کار اشتباهی کردن فاش نمی‌کنم که آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91870" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ: چند ماهه داریم باهاشون مذاکره میکنیم. توافق براشون خیلی خوب بود ولی امضاش نکردن. کار اشتباهی کردن فاش نمی‌کنم که آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91869" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91867" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فووووووری؛ ترامپ: به شدت به ایران حمله خواهیم کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91866" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فووووووری؛ ترامپ: به شدت به ایران حمله خواهیم کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91865" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91863">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4T52Sjr0AFskIRrX5e0L3BLKdj9Ln4HjEJWc5WT8aWs_H6SOwGfQPHnFEgLng4Wi9OJxOTXYiIrxQCapMO2S99f2__UKroTdIyRYvDhYsm94vqJVdhHdlAAmgvVoH8VqUAhVlXv8Dhui2IAV9t3IOnQtV9Ac4zaA0sOI47FraRHFNT6dQDsbCvsuz4PFoQHHtLgDQNzjBrrFNCCIFUAxfeHr0UT3318Yq05ieGEv9V15jLVkdIcX-_qGmZBHX84wfazd96kutnfzMHCAcSAgjaQbq72qdOxxRR7OC2Xq9ZjQ9XwP6TwFODKxSEY60zyNNCnGAWkx1TqHebQkWwc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست داری تو فینال جام جهانی با کدوم تیم روبرو بشی؟
برونو فرناندز:
فرقی برام نداره، هر تیمی باشه. اگه به فینال برسیم، اون موقع بهش فکر می‌کنم. مراکش؟ خب، دوستم نصیر مزراوی اونجاست. هنوز از جام جهانی قبلی یه چیزی تو دلمون مونده، برای همین دوست دارم این دفعه شکستشون بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91863" target="_blank">📅 19:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b88d7249a.mp4?token=KQ08Y55S8tbvEbT95j79dfoghoHqGoz6pb4BB1BHzNrYZXivZaoL33S4LHCXh8tPQAmjfvRrwNjzB3vSWvlZMsMnj-fgk8wE1eykMyMXISPchpmgQrvWnQaEgyVQ0R-LOIu_qyIenp6LwYiSq6H18L4qx7wlC-ohTrw6L6H_H-j6Zn3mkjGVQFZMMvPSMMrdrHtWjGe1a8aDruOK0fAoiyOF4DmIKCM11a9OEHL2tUmjEiLJfXX--ImZLN96tOlG1NvxC9wtApbivT3h7B63HzskFDzraDgKRKaAaO2FTOcbKeqxmmlNHnwcq0pKHqC-2bvaIWt6hqbUem-7qIWWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b88d7249a.mp4?token=KQ08Y55S8tbvEbT95j79dfoghoHqGoz6pb4BB1BHzNrYZXivZaoL33S4LHCXh8tPQAmjfvRrwNjzB3vSWvlZMsMnj-fgk8wE1eykMyMXISPchpmgQrvWnQaEgyVQ0R-LOIu_qyIenp6LwYiSq6H18L4qx7wlC-ohTrw6L6H_H-j6Zn3mkjGVQFZMMvPSMMrdrHtWjGe1a8aDruOK0fAoiyOF4DmIKCM11a9OEHL2tUmjEiLJfXX--ImZLN96tOlG1NvxC9wtApbivT3h7B63HzskFDzraDgKRKaAaO2FTOcbKeqxmmlNHnwcq0pKHqC-2bvaIWt6hqbUem-7qIWWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نصرتی درباره شادی گل جنجالی با شیث رضایی: قسم می‌خورم با او شوخی هم نداشتم! یک دفعه‌ای شد! گفتند شرط‌بندی کردیم! بی‌بی‌سی با من تماس گرفت تا یک چیزی از آن دربیاورد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91862" target="_blank">📅 19:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91861">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMEBlSjplfy1LaSFu8mK2Lwgq1u_RY5zA113R-paeEVXRghy7Cgd1dv3-zKWvAavHzshoJyMwS80PKT8slxkJIQgEs9PZBTcgJmAi7V-CXXJ9CBzUeW42z0hDwKs7HjIHHwy-fCiO4FozzlNrCP8cOA2WCIHJazbqTXRkx7TeboRpC7SGaZsLw-zPpGXcx5QaXy51GSfimfA60NbsMJBY6Dc_yY2kCdRgZuvKsDeJGHmKa0ZpQuLA9vCx7XYhRXMRm-doXHDBabezsoPzL1yJFMAZJe0lc-UbFXrTtxHnDO5pFiVwKXkOEUvI5V3GozR3zvQG84oK10dRGJtCKrnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برند چایکین به تازگی ساعتی طراحی کرده که زمان رو با ممه‌های یه خانم نمایش میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91861" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d10dfe8d.mp4?token=ihxCwqhUeB1tj45eERclJi7_wOyvCOMdQUcJn-AEE6vf-piw1JEoSlaakNYufYetsvm3FsdNhlhq9lMKAtekITN3SK1OGHb5mM_cNOxOXx3a1a29eANdMBlx8FZw-UNNTXylTlFyeNY1i19kKK-5U9IJDuuFW6c4RYVY4VnxzFhaKuwCo9sASxPpqq5G4MuEYFYL3_kc1pjHEB1MpA77JzE7npiVM6fuXBPVq5zqE9DdfkxI740Jg8ipO4sjAQWoBYDkYf3M5BO3aAW2akCICeCDgBxhHKgujLyPN3XMD1XqpzSQ0fMgkgTHX95EQmh2GX-o1h2wFS_OpTeoQdnDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d10dfe8d.mp4?token=ihxCwqhUeB1tj45eERclJi7_wOyvCOMdQUcJn-AEE6vf-piw1JEoSlaakNYufYetsvm3FsdNhlhq9lMKAtekITN3SK1OGHb5mM_cNOxOXx3a1a29eANdMBlx8FZw-UNNTXylTlFyeNY1i19kKK-5U9IJDuuFW6c4RYVY4VnxzFhaKuwCo9sASxPpqq5G4MuEYFYL3_kc1pjHEB1MpA77JzE7npiVM6fuXBPVq5zqE9DdfkxI740Jg8ipO4sjAQWoBYDkYf3M5BO3aAW2akCICeCDgBxhHKgujLyPN3XMD1XqpzSQ0fMgkgTHX95EQmh2GX-o1h2wFS_OpTeoQdnDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
تمامی تغییرات داوری در طول جام‌جهانی. برای اینکه هنگام بازی مغزتون ریپ نزنه، از دستش ندید
👆🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91860" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
💥
🏆
با اعلام فیفا، ۳۵۰ شبکه تلویزیونی که حق پخش جام‌جهانی رو خریداری کردن، فرداشب این بازیکن رو پوشش میدن.
🤡
البته فیفا در نظر نداره که صداوسیما جمهوری اسلامی بدون حق پخش بازیارو با تاخیر یک تا دو دقیقه‌ای و تبلیغات مورد علاقه خودش با بدترین کیفیت ممکن پخش میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91859" target="_blank">📅 18:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQG49dURKXYBrRbxsGip8xtLu6g3KYUzih37rQu3BmGqXE0plYUE2-VGgF9utbWKMeRxtdMAA3jVRdks1_DbPSXiIubwKkOhEe02edjBPnvtSRTIQWWabIDjqYuCjMn3eBm6anOKHSYbWDD8J8oH2k2D3fN2BSSw56IFZgC6yiUdTDtpqMAFaHKTnNuNbhbrCjtifpblRBh6OmpHlpPniHPGWYxCvCC8_x5cUsVNtpBcmFfMoyflQf7lu7uG57l_7zfhwFoUTk3fi0lf4vfSbZXwB4xBpT0FDEvpmKi2xB60448XYemsdsvxd5KggE8M2vdczl0YHn73tIrZQKPdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فیلیپه لام درباره پیروزی 7-1 آلمان مقابل برزیل:
🔹
بعد از اینکه در نیمه اول 5-0 از برزیل جلو بودیم، مربی‌مان یواخیم لوو ما را در رختکن جمع کرد و گفت در نیمه دوم «آرام‌تر بازی کنیم» چون گل های بیشتر برای میزبان‌ تحقیرآمیز خواهد بود.
🔹
متأسفانه، آندره شورله گوش نکرد چون در زمان صحبت های یواخیم لوو در دستشویی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91858" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP5mA42V8q94fAdlZoKuakr1l1WXxA2LVb8cAwOZpCM2BUy7aX53EfqYrV0KO52LLesYVirXbAI1qd1tN8hy2BUD636Yx1o-FtAq5l6qYChII0xIlz2NnUZeibdEETEmuwezwQHmZNl6RuaWuhksfMEfDlvpO103baD9W4hhuAs-b1pN9Imm-fAHs5bmJysWyrxAh6Hsj0OHEzw_BkN-9YhVNqUu6L67dKOTM3C-Xaz4Rx_SbVj1hWUmWhttEsBPEGOS5nqNEG1caEz6kz5e546Lfu62CkXIFgmQYdy2f014IWx2fbcqQ9-4VlIXjZKmMzmyMWvaWqHl42wPAdm1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر صدر همیشه میگفت هیچ وقت دوست نداره وسط یه تورنمنت بمیره، این که مسابقاتی رو دنبال کنی ولی تا آخرش زنده نباشی و ندونی چه تیمی قهرمان میشه، آزار دهندست.
جام جهانی ۲۰۲۶، یک روز دیگه آغاز میشه و ما از همیشه بیشتر دلتنگ تحلیلای دکتر صدر هستیم
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91857" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgwtkcfeEA57xQm7wk8lsMi7O3gRNuPGh5u5u18ety9W97h9HQ_aPwRYWT3O0RPTAVxQLlYgbi-LF-juXH9mCTWo6_yWLZQo86Lx5Y5HaJq6N1R6HRz1-ivbsYc7NQ0h3bwm4c0Kvbg4EaM5xSoNn1b3LrvW7d_aTyLvQi5F38xpLLNtMpJKRmo_s-IK5wPoIlMjXVaOmN0ouTBZgniOYt3hp_S6pON93ZMMdoxup-1ewUddjTeuLznC2ligEqZAT0GyIliBvtzNuSgxCvo0lCsecFBvusVozEK4LRATt_0V_RDQYx3wAvvnv0nZa6Sl2_Ut-nvAUOwPwnok1Dr7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام بر حرام بال
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91856" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🏅
یاسر آسانی به باشگاه استقلال نوتیس داد که اگه تا ۷ روز دیگر مطالباتش پرداخت نشود فسخ میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91855" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj-gbw7p6vbhEn_hQ0BnkIAK1DCHeP02FW1gT9shW1siVTBtULSOWngxifMtwoCjx3aUKPp7XKsC4UzXYmetLzs10Cji8vjG7snn7HIeFi3rQh92T1sZYH-HTA6veh0IHR371OpqPPyd9XYkxgUigw-4T00ZwPOhh4EY0iNSBwzU0cAqbBuIJkWGPfxGka_w6hkZcxxiGG449tysE4myiCaYxwt17rBGikCNwg2rsHNg54GrGwqEYaGfGiM2oNkWAE2nr_ujRc1OrhEpVzvPFlk5SUqoyAaVNYaYo5pxVaY2wbmll6IJV9TbZaoag45-1JmHXD1P-BUDaYm_j7azFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
امروز تولد ۶۷ سالگی کارلتوست.
مردی که یکی از بدترین رئال های تاریخ رو از مرداب بیرون کشید و ۲ بار قهرمان سی‌ال شد.
اون بدون مهاجم نوک، وینگر راست، دفاع راست و چپ، سیتی و بایرن رو برد و چمپ زد!
پس اگر فکر می‌کنید برزیل مدعی جدی و مهم جام‌جهانی محسوب نمیشه، شما هنوز دون کارلو رو نشناختید.
🤌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91854" target="_blank">📅 17:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5KvYlnuH1czjnTUfYB6pyCS8__5KAuppy1CMGH7HPVkSygvw_Rq6GcGpY-8OmmnMiY_2lOFsoMITo1dEcxThkSme0gf2TuYLV3bJNxelpeE60tZEx05scqbIGmj0j504-zfg27jmTQwTjvbkf3mzHnKQQluncW6Pu6FgyYprQO6rZllRkN5IVLS6T_XDdtieulHLc40g9bUzLEsjJw-2c7Dc07tdQeb4qXXm__EAMy4x6JUwGXE3SkJGYxmJlilCqHzv3nhOQdM58_BUjFUF0fBdDo5B34FMIyzQS5FdSjujoY73h4YxaDd9pLfUnlupaWR5Y4jkleEMZip90ZAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌موی فن‌دایک‌در آستانه جام‌جهانی
🎀
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91853" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91852">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMHWzyWpNd8jb-eiZaGGRLN3gYAwTxGxPrVKK-Q-nherb2FNvojIiI1ijNMIceHnXSPCxGRH2DEoceR_Foony1lsych_M2Xy3V73q-99XATddG7juhYYAOCALRgPeMISml4s2gd0o0JkJjDA76GQ-zW4ePik1MGf3wwPUTyjjiaRwL0fiQeuaflEe189WLsyR9h5SB4YjXqmTziahtFeDv4scbwQfJ7gne01gaKl9ApuNT53HxOz09KvIZiiyorq62N20axgSaNNHnV5fweclUShT5rkKVEMtQE4Tw4UX7aSX6KsUsvHmHz7C10U6ArrQAtfjWDZaoxtlATFSkErgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🏆
#فکت
پشم‌ریزون؛ در تاریخ جام‌جهانی هر کشوری که موفق به قهرمانی شده، با سرمربی بومی و داخلی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91852" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: اتلتیکومادرید خودش میدونه که رئال اصلا آلوارز رو نمی‌خواست و صرفا بخاطر شعار پرز در انتخابات، دست به بیانیه دیشب زد. سیمئونه و تیمش اعتقاد دارن بارسا واقعا ستاره تیمشون رو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91851" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0sK3CjBB_qS3FfepfV7uPv4RK8RnY_botH_jR9q6aclpRqNWdg1CjqJcTA1-Acngl7Gz_7ZtCNWsYjLlugzQvRcSFTJN_xC1tv7RZRkn8HyRZrfeytbutNlH_GvaE73fbyeS1F5KsH-7UyCKSAAj3aXObLM6_iPmX44SZEs5KICpTaOQA5cJagYB4PYRlTytiJQmd-5ZvUQJR91MY9bok-piQrcSpC0a-wcof4QyTdBW7jDOi1Z8tXeH6bH2iTU9RmjvCkq1kpcPnNO3nitAjximyRWe3Xrn_lGoXkV989Cnvxv-yZMe5ViLwWJIcSZ00DHwGZp29w8smQwz56lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
🇲🇦
وینچیچ اسلوونیایی داور دیدار برزیل و مراکش شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91850" target="_blank">📅 16:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9a592196.mp4?token=YZINWndBz-nkeE2bB5d_J_ALCybo_H5O3u8TSEpbTG1jQjZt0M4KAWCIRtM0YiWMLU5--HZxjwoFpsEWLE2ZPJofid7alAK0rUusYE7pVa5r3_mp1tKnUnINSamNrjS5g3Ub34smg9a1Ug_FcGu5ScKzkEOUZZfso2T0xMH6v6Re50E6XW49MlD0qsjbs4whGSlkuF8OicAE65tXxhy8NyoKXnP_QvES5v4D4n_lOIvDkuZIHsZ2-ugrmopDAy7hrtChfjPuTE9JhJrbU4wYQVewKggMZY_YO2-5SWlTqiy50H4CNOlnQFM7mssDWUemyJx38deHU6w1jALDnuxCog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9a592196.mp4?token=YZINWndBz-nkeE2bB5d_J_ALCybo_H5O3u8TSEpbTG1jQjZt0M4KAWCIRtM0YiWMLU5--HZxjwoFpsEWLE2ZPJofid7alAK0rUusYE7pVa5r3_mp1tKnUnINSamNrjS5g3Ub34smg9a1Ug_FcGu5ScKzkEOUZZfso2T0xMH6v6Re50E6XW49MlD0qsjbs4whGSlkuF8OicAE65tXxhy8NyoKXnP_QvES5v4D4n_lOIvDkuZIHsZ2-ugrmopDAy7hrtChfjPuTE9JhJrbU4wYQVewKggMZY_YO2-5SWlTqiy50H4CNOlnQFM7mssDWUemyJx38deHU6w1jALDnuxCog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پرستاره ترین جام‌جهانی تاریخ با اختلاف؛ مملو از استعداد، جذبه، کاریزما و aura
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91849" target="_blank">📅 16:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946cc3e4e9.mp4?token=b7C7o04mzejovio2aVrc3_6h48hDaMxuy5uEiQOObTfk4Hjw3mGpE-7EQyc40pYEyqbHFqRXvwFdT5kBOWuj3IcrV3jmJ6q6R2b31UNsB4qOY4amPurdnDiUDRATtJWL2xHDuBcyM7w5AjDCbfvIWp2d1DHkwne1r-mraoKVjb40rg6UhK_dR25VB2wEk0j6R5WUJf5g46rMGLr1Hqq2R_3EUvIUdFNzP2msBZ4QBRNKbqhRjFtugrPnhGzi8RIKA8ZQSXZojw8x6mHSGWV2lxiR-7ENV9JlwrTBlVHU7nT1YGUQPUmbfcILGpsIlv38wYvzkk9gzuOARoL-2Kl2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946cc3e4e9.mp4?token=b7C7o04mzejovio2aVrc3_6h48hDaMxuy5uEiQOObTfk4Hjw3mGpE-7EQyc40pYEyqbHFqRXvwFdT5kBOWuj3IcrV3jmJ6q6R2b31UNsB4qOY4amPurdnDiUDRATtJWL2xHDuBcyM7w5AjDCbfvIWp2d1DHkwne1r-mraoKVjb40rg6UhK_dR25VB2wEk0j6R5WUJf5g46rMGLr1Hqq2R_3EUvIUdFNzP2msBZ4QBRNKbqhRjFtugrPnhGzi8RIKA8ZQSXZojw8x6mHSGWV2lxiR-7ENV9JlwrTBlVHU7nT1YGUQPUmbfcILGpsIlv38wYvzkk9gzuOARoL-2Kl2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
این ترک و اجرا جنیفر لوپز انقدر شاهکاره که بدون هیچ شک و تردیدی تا روز قیامت لقب «بهترین آهنگ تاریخ افتتاحیه جام‌جهانی» رو یدک میکشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91848" target="_blank">📅 16:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrHMX3dlZNTjn-IplX9if1kuGIz_iaV4N9PTtz1ytykgBALNnXIH772Mjeo63XqQpen8vv4eXURu07-9nl0JqwU_lGPMCrCA8Zw4F5N1PhksmjJjlf4jNNC7jYH1x7cEk9_-kls86seadvaLoFx79G1sdVGoMiEsM-xEzaSSFXqmyQTxrkDDdq_6PkKYYl--gvZFsN6LTd_5giPV0pS_Tv6dnTS4_Nlb27rnuiKgkTj7WB-ZXKARijRJsW0Ntug_zwVlcF3Pux6XZVR0sz5md5oZOydy9dVO7jOGuzNl825SnOo4j1igWUFNAzpl6bWfbMr1Z5fTHM7rc2J70aOW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlXfT4LLMM9lR12TX580RW9p6QQ6FP9U-sE_pM2NurCkQXdMnc0k0jRWE0yQlLpJ2kA2cNsBOpCXZeFM0qkgtfUlrbyzHUjGeX45-0L3mB9daDE5HflegX9RyGrefgwXy3rwmkdAM_SleSyZX2bMZYLlrk3Ov3RfTSw68b5vhggBqkw6jLxQAH2YKcy3j8R6sENcqzZQKxLmF18J1q9x7IhJrevjjzoz8I7DSPySlYR0ETQrGXsDfprsDS8dVCWfPf-nxckLI0oKWQy8KjfdDfDyLSOm1D4t24nur-3oQj9-quRQ519R4-78WKomVn1buEaNFctGASb6n6-lVqnLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmn-k_iqQla07NAeYpkcod1sGSLGXCyOh7_zTyBJh4jyCViIqwe_ntj5ij9ygAsqhOYFLBZdexUWQnU4BRFrrp4Iu2rXwRxHCizm0yiQHnmeZUCU1JvA9oxroO-qGKdKgTXnyFCUH3MK9BR-hxMHeJICyhab-STc_sx2T1uJYdtBa5oxiJycRYaJYHLHVsqMbqQYcKG7c4aB3ES6clObSHgsJu1T4T9OhPDd5uCNHWTnSbUFfVjeCxBTRIAe6rcfJUNPUTpSTkyaoA2WuK_HpaGAtLP53sUSXH-DMcErgiw6U9vCvCduV8WNpAEONRxnWFObzUe0QlIe2FHtNg0wzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">10 ژوئن روز جهانی تکست دادن به کراش یا عشق زندگیه، برید تکست بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91845" target="_blank">📅 16:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPM9tsM5mszX5xVBG3XGSWPIDwRlEe0TXiqgFYFA_paQjAItuHxR15O3AKnt3ku4_EvsxS765yunbBV4hCctIBJgY-qTmv3r1DFcmDKYIjqEWiFEfzrSUdDu3JIrxjL70CQu-wxCYw5bzMw1Hc27AWGJX6KE8JBlcldpeMQMjxQgSTYWYM1oKF_N6SDqO4zhBNBzFAaFdDB5tGMZXe-KfAlmd6toJ8R755bUKCvhhwFsC-oebvkwgRA5K62myFStJivAELOnvUlUIrxx9cGmRvPfog-TY0Wq6KK8Wj-Mhty-69uNW6JBGqNVmMzFKnzb0Cug6YyyihdARiBwZT8ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به هر قیمتی نخواستن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91844" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb43e1318.mp4?token=TGWr4V1dzBob-XtzBxaaIwnfNNJmEEaMbdE7NZ3d6uD7XvTq81_QttSjZC2tlXfn4tcJuDmWlajPTWRQQXxh0Ko640zKPzcs7_NxQjenlrZjhk31YsKkIPfEc6X-tc10Uwg2AUsiooFCS-rab-RpO1P2rmubv1Z-YW-KybQy2_0NGJy2pWDr-1eG8EPge9-mQpcDQyWXgy8vn4FwF_aUHtCh9kUvRF9O3zoGxNE-5nUR3ilx2a1P3IHcaah9my2yqVymOv-1B2T_4HvePClMmg_klQg7j2K8RrL-94Lzi6L7NvcuBEyiXBy5gDpiYDeNE9gH9kg1aOpPZ_fT76F-dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb43e1318.mp4?token=TGWr4V1dzBob-XtzBxaaIwnfNNJmEEaMbdE7NZ3d6uD7XvTq81_QttSjZC2tlXfn4tcJuDmWlajPTWRQQXxh0Ko640zKPzcs7_NxQjenlrZjhk31YsKkIPfEc6X-tc10Uwg2AUsiooFCS-rab-RpO1P2rmubv1Z-YW-KybQy2_0NGJy2pWDr-1eG8EPge9-mQpcDQyWXgy8vn4FwF_aUHtCh9kUvRF9O3zoGxNE-5nUR3ilx2a1P3IHcaah9my2yqVymOv-1B2T_4HvePClMmg_klQg7j2K8RrL-94Lzi6L7NvcuBEyiXBy5gDpiYDeNE9gH9kg1aOpPZ_fT76F-dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇱
جمیعت فوق‌العاده هلندی‌ها در آمریکا برای حمایت از کشورشون در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91843" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
#فوووووووری از اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91842" target="_blank">📅 15:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
#
فوووووووری
از اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91841" target="_blank">📅 15:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز: به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91840" target="_blank">📅 15:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
#فووووری از ترامپ:   نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!!! آنها برای مذاکره بر…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91839" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m36wAGXJ9C1MvbkHKYnZm9DnhfDKypwmSlIS6SraIYaqEIJ_hEf5s3-6CDE9CFYVzWW3Z8vPUrwjLeRtw2-FTdGayYdS4HTSdQBt-6nBMYVX9Kqld_ljx2sYV1cDHSSBPa68IU07klBk59wyuCLrzZPTeJQP75Ly19oyMCEPt2qF45H04IuBddneM-h3in6tLmX8wq3guAJPX1tUN2iBwtWXEEPLmURWvHS4R08EYunyFNSnPUfLbhhdWCZ0yV-hU1dblbuMWs83hEf_7eoB3CGB6qsiluASfgey1PDziMA7kPV7Y9dY7YK2csBLjQSkHe9fbazT8ThMZ3KQOjpGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فووووری
از ترامپ:
نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!!! آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91838" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMyj-mMZOiqC6swhm3T7LEmZhGWufhDOkc6yEbv_kkyW3v6C4KWglBLUGmAP5GAMdGjT5viYEp4bvxIC8x9pTAePMgjwyeSC1tSEc7B_pOZwpSTBFzYLIkdAEbimE52vybMFJVSbyTUrdjYqXm0q23AuTKkKJrLhr9Od7SQl9gJHhg96uc4WujgYOT1e5gXT9wFvEOX3q_z0uMu83M9d41ETtBAIj-C1W0K4EC7CWleUJnUWHG9LBx3nmrYrCic8zCYXUb7uyD8ctJZk4AdWJu5SO9hbcOpt7eLrx5c263nV0k6AhVYiW4OkJR5CNWJKPKWk0yag87E2pOEP8d4org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک‌های ناشناخته ژنرال جواب داد و دوکو امروز 1 ساعت تمرین کرد و بدلیل مصدومیت تمرین و ترک کرد. هنوز میزان مصدومیتش مشخص نیست‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91837" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-v-nYaz3tHOwSf3HORhxrZ0S4i3Ts16ZIZ8IDdlXzfFgRiJ5W2sgZwFxQAsm51Afyi2NYcMirnsbq_Ty9ko27sL58UcIlXmBV0I5qwaG7ocoRVF_y8xHeyyQhmGrVi_hCvVXyaZHZseuV4Ln58IGC7gFRN588PiZq9L6ifzxzebySP8-ioxyL7V8QWv7o2NDQ4NXLqDDnDMtF9MVGHFTVEDbm5nsz3-6KcggjUbOUA1mAgXpjdOfXUBpm0smT8AUQ474zc669o3FrETwYgyJzOnVMjucL_stqyiJm5NWyqmNwHmIG2ovdxwQ6Psp5KfrVZHW_915gFp1p_8OP_FMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عمق اسکواد فرانسه برای جام‌ جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91836" target="_blank">📅 14:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlcvsJd7MX-FnmKccSU2MMdy33zQ6huqt7xQjc0M1QDo8G3Tt-o4F0tU27doLewRJ7AwP-O8RTRJFPFxB7f8n_iO_yWufmhKt9F5qr47wyX_C1YVbry67YC5V0H4k_U_p1UC2VST3neoVZcMT61vXugasutQVKZt_n2nBIZImMIHMoTgB_R5hXB3ssHLYmeai1fSo3sY_LggYfmxRgIDAPkiitmQvs6toYQuFNdh_yYnAQUqtJ7Xfg3XhtDFczOssqY0qdyPqm97hinoecSWBslk86u5zODTDgsI_Nu3mR-HUvxbHYNrA9_kAThQNCzVBV1kNvZ-qWIQY9X3VlrUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گرون ترین بازیکنان افتتاحیه جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91835" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_QNHOZJ8NLLp5CpbugPxlzAqeUxQ7cJdErd8mt17fYJRjRD3DBP-2-jIGR7bFWgsBI79OauaYt6HQmKfFq5ymnzeRtt_v8IZFMtoUL6bNhFg-n1kIJ6hNivmy2rBmssGT5YQltP1y7yeY7_1-xk9PjB21d4zZF-yLNJkxsB9cNpgaUjBnWd5_u0IVeij7GwPAMfhyZpiOesVKam2hyYa-BMuJ5Hs2hdhe7wK0LleX2iWn15kuhdzcrKfOq-jqqSa0cSGjNkce2M4Kae7_jBOdMSVoGrvBoHlKHUXwfb7aoK_XJayhlyK9DYzanq7B4KrY1roe1bz6hreUxQb-jT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوین دی‌بروینه:
اون موقع که دوست‌ دختر سابقم کارولین رفت مادرید، با تیبو کورتوا به من خیانت کرد. وقتی فهمیدم، انگار دنیا رو سرم خراب شد. اون هم‌تیمیم تو تیم ملی بود و هر روز باهم چشم تو چشم میشدیم،، تو زمین فوتبال باهم چشم تو چشم میشدیم ولی دیگه هیچوقت باهاش رفیق نشدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91834" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzE_kmQXSaAMalwwWgp6ripSgNd_0Pjg5OfVuWztt3tI0n1LZ9PNZJOSEGp8MLExJ4yAVMgcE5nEMeAjoWWvOsqMxA8N7sygkzZQ2zxAmLkGPtdzBWtHwy498WEGya5grQ2mbJEScKpTqtfRRI6GKX70qlo66xUgTNIVQYH8mbWwsAXp_8mDYVzApgUW4twB0p597PSBagi7kNoG9W7lQC-aJkdpCmb2J3a4WOE2ohPthjNUAie_0JYFN9KVLFs8-lbgpY18CczoHhqHTfxHu6apoLMN6MTTNEk0cXOi3cy7d0PgcrheIXwMWFHwqhqe0lUOuXODNkMthtqOYbU7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91830" target="_blank">📅 13:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار زیبای عربستان‌در آستانه جام‌جهانی
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91829" target="_blank">📅 13:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Ccgjh_viNGwfice94K4Gt53Mf2q_LzOVRSvB0U0Rehku5MaZ2c1_0AuZWVUWgDvwpgtMSRJ072XUWadl5DS2AofC0y3EtDZ_HkD0pbRQcVdSuYStXXHoDi19PelI37Ws3EqVq_kL4E3Ob98_c1kbk5VrOJOolpwgSTbny7HZNEsFOE5tTbZb2ki5jN623DQLq8-PsmRNzaCa_JNayKU8p4X_hl0b0rW7ThuWzCIN6PfmTQjp9DtbBz_5f5VxmG_ORENZtYlRAqpFjczfVjigeUt2bR_maYt1A-8ykoitYXpZIDtrx8KXc4Rf0kf8niT12feAdghGCnBtgBt62_xUzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Ccgjh_viNGwfice94K4Gt53Mf2q_LzOVRSvB0U0Rehku5MaZ2c1_0AuZWVUWgDvwpgtMSRJ072XUWadl5DS2AofC0y3EtDZ_HkD0pbRQcVdSuYStXXHoDi19PelI37Ws3EqVq_kL4E3Ob98_c1kbk5VrOJOolpwgSTbny7HZNEsFOE5tTbZb2ki5jN623DQLq8-PsmRNzaCa_JNayKU8p4X_hl0b0rW7ThuWzCIN6PfmTQjp9DtbBz_5f5VxmG_ORENZtYlRAqpFjczfVjigeUt2bR_maYt1A-8ykoitYXpZIDtrx8KXc4Rf0kf8niT12feAdghGCnBtgBt62_xUzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
جام جهانی 2026 ساعت ۴ صبح در خاورمیانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91826" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaP0njFBjT28akz496dQQpgwNhyr34ZLmj-vPb6D2zNJ5_5fOevXeHv0VbsvOH9Ezn_30MLKx1C3PWe2cPkwA_pDn0YqGspg-9Dv88jhD3St1dMgXQlI7jBfZd3--whcOJ8QChCvQDCON-neR4LZL_NJfH26TSGgumSCcwzUHmLTIOxkUABv0RxIpmlQ1bdGT-717c8NH27DSN9fl7mU180ZKy2PvWC9SCEH-xsFdfyAMCc3C-JLPDdQ39aGaiczT7RhiWrn4M_8eko6oNrgV6_agAJ1Qsj8JyVXtP5d9kdQDRS5KeIg2ES291bwqoXbOIfiOt_JOIJ8Pgs0J3GluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91825" target="_blank">📅 12:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ایان رایت: رفتار میزبان جام‌جهانی نباید اینطور باشه. این جام‌جهانی، جام هرج و مرجه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91824" target="_blank">📅 12:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrgBs9nsRfOVy7yx6KBiVgGEIEBU52NXUwtABmaQu3cBeOkyZNqeu9z9MOdL9hHk5EPCnx_DHLyv6OKUwsoHPwUMYzWhhkyGjCsrme5SCkaOO7EdQA6k8wSS7fG31A04Nn-bkO84ZMdqTxy85Sq1P69tScY5qrJDqyxhgIdBQ3teaTHyU7uIIAL7c3CFe9AUnOH3SPyQDdrRQSrhnNNOU-o2ilXMZSbsfQ6zSR97pa4sia6UX23nP-MPVWckasQYyPYalBld61EQ3Nyg8brGtGAvw453LEadPzps97YKEDad__X__3O8Ce15Mq5xS4_CfYcXkflUAwrBN6K7BiGfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91823" target="_blank">📅 12:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjHNgtFmdHqDUokWfATPdSjLtDVAIkdNpBuDwsIjbwzJe7FcokThfnwNbHIkj2YUijpKDj9-gJfMANwQbFVt6DFirRCpgVp3AzUW0Nk9xatuU_pZblKg_qy9l5msSM8pVtftpYK2Eijcx_AlF4QqWDOkTGbBAJTTRPi84Zgj46mfgTA_qCu5J9QZh_HXRG75T94g7HxY95ayVHhWnE_bNT5j9LUdlrzXnZcQE2KFSt8oTev0LSEPRwy6OzB4qZotN3pOguypjDhZlfJB5RlO9JQn0w8JaIRkrZx7_1CRlKQov4lKqaZ0NMBDj49ZfPAdUD2baY6feH-RnNbGWuAQr5Ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjHNgtFmdHqDUokWfATPdSjLtDVAIkdNpBuDwsIjbwzJe7FcokThfnwNbHIkj2YUijpKDj9-gJfMANwQbFVt6DFirRCpgVp3AzUW0Nk9xatuU_pZblKg_qy9l5msSM8pVtftpYK2Eijcx_AlF4QqWDOkTGbBAJTTRPi84Zgj46mfgTA_qCu5J9QZh_HXRG75T94g7HxY95ayVHhWnE_bNT5j9LUdlrzXnZcQE2KFSt8oTev0LSEPRwy6OzB4qZotN3pOguypjDhZlfJB5RlO9JQn0w8JaIRkrZx7_1CRlKQov4lKqaZ0NMBDj49ZfPAdUD2baY6feH-RnNbGWuAQr5Ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمرینات تیم‌ملی انگلیس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91822" target="_blank">📅 12:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brMgpg1wz-t0haB4qsKUllZIqgzGOWXNgUiPauzuO7vWM1lxPMh7R0A-Fs8S8Sv864CZgm3fhuGJ3OvRCNk8XMuzyAp-HZ0G2sSbQ41uoWyaK0aPTltGNZaBaM2MDV0GvKHZtdQ0ZHY5tMULUm1GlI29ZRHVvXW79T4MUnCabb2owFeYwrXf8WKrpBmCTe_JaJsDW9tamBdoHSTFPC4ScrnhL7EXKeyIa9cq6AhJfyoPq3AaDsrEfz6EPG3oCAQ1Lda4UGk-NL2JNhEpvQ-_mm5Wx1ACcmtT1rtjC-jTA-EncX69zQ7ZCAXGhxkBuXl3ZGv5Kww1YAfskRqDcpR2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJd6Ru8b52ztG-BO_D9JyA0Bjs8Woa4uIgzH2ZR2Bj7H-tBLOP9HI4yjPgtDvH5LvCc30pB2PgSEr3Qwj2PZPo3L4d5h9W8eO459ZCDBe_cDqDuu2dV90CZhGKRdeazdaF3vE6fa7BueqaRRGfPfG2EQIQP8L80uHAmJXK_IsKsxWFW977At2Mv-5x-YorQimYO_9mzna_c1qKUimkhtgrSoMpo-AiMotm0Lu0H3TqqiTNeoRojhwR_qygDfX5i0mxo5ULKyS4SsNFX-G2Y1jpGLVyEz2ehyhAD7AZ5XZq7ttYFhlmhsuffbuksLak4WkL-QJegC06bqR2Y1hxrQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipYJbq4PyaxZi-_6_Zic9tkvB8ZQ4CjYTLQmkgone_HACEvUkg4JzuuHa4RSglh0us9mCubSw1E7JX-_pZxc3vLse1iGMi0AI06qJuOAN5GOp1oGtFdcvSCh7FqGwxjccFkVIgQQu69YF2AeWR1WxxnIAYzQjU-QpLPEFyknj56RDSFEaIbLmFatYjo-no4F1Cyk7QXZL_NBWn9CbCMK0ZjaB4dqbSZDbWRTRbqR7AJRUg-SyUFXyy6DYWLZf6ivkjoq8oqEGugq_3d6ZLBr0UmMmKQn1o3X0kd4SEd4oK_nKh-CPZ3Y0gNq3IhmqcT0RoFigAsnhxdczsZFaEzd1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک و همسرش و بچه‌ای که تو راهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91819" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw6PPjJElrjkT9Ax3lZZfQ2m2Vzo-kNMh5nk5UL5MSdNA3tA951FP963_ueu93IpIVC3k6Qzdk3KudRg2TBI1gR4SwzL3to0x0Rc9CFOOklaksetJDZXzASerJ-05B8BF3BanAQ_UREVwqs0mTANgvI0Djr6ungEyQt6av7zaBuD4ezaq1lEJ1IsieRiOVjKwjxgqnbJ4IAmCQTTPZHw2FVp7GxiCZs-qrFNsIG7eY0UxtJj-hoXUd3ibuMf9YaBlyh2BUI4brDDkBx6PoKCUDtiLEYss64djK7f3a8KTB2fsl7OXyeiTHMvGe0VbFkmubAzriy2kWoDxA59Tm4A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPKmOfOvnP74resIzShUcoJqb9wsfs2kBi7w0B8mdBgeS6rpqJxAQ5aG_lwS3dPI1mEc3vQOR2LFrHzLPITPfLPRbkY_7z3O17aR5_Hm1nbL2bMwS_RNQACRkzcsH-1MJjV-bw-TmTqj8ajig7bRKgJZR1tnkyEgV-tn-hY4NUjJO-AiJyLtA9C4_jBNJYQS0JsnJ2FY5UmUM_5EMsiFgJmEXFjED1i2Lan6B3nQVkgZNrrSp0PapnWQ4bw5gX14jnu_ZnEHCSmtLBFI8cprO-AVr4zZCmUGE5ptI-5S65YSE2BBOc5Bb6U5YptUWB9EFPPtAEVPc3dYz4okzHEKYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی دیبالا چرا هیچ تغییری نمیکنه؟ لاشی هر روز داره جوون‌تر میشه انگار نه انگار که 32 سالشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91817" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfI2P2qTB3PRupDPH89qrKpMvBtFY9e2fL61pbGmVxxJW83LhrHMjn_5huz5jHtXkedwut_rb1WsObBRupB1hvw1vCw-H4icZBCmCbjtq27qKnr-F3-AUVlG4wOzWOiHok5-nIuNWRegm9-1KnJ1gcBrpSA7Dern4qdIE75cdL8-_KMV2tHrbCwYMIlvqBccC_lvHO-imuIIaY4IKMgSp1RK0e6wctBOSh5gLY5cL7hrqQGaxtd7Sjnv6X9LzGeGWqh-Oj1PIoQsXaECK1rrWxO18XkYyv29L4aGWbQiRRneUQ6LkxBvCJl76lWaN47Fk5cIuwFCZ9x5u2slwwOw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر فدراسیون فوتبال جمهوری اسلامی به مناسبت یک روز تا آغاز جام جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91816" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPA3JeioSCIU6vmNmcbYCt7B_Dx9z-6XB224Wi93mybnZgQWy2UaYwFsb1K6xDrlDl0RHCJ84vrJWgaJ_YXFhsYDNXT6jspDvKYisT0kxv0WLePzLzGPBEe1ru01oQLW0RM5xOo2mSbORizpclGWOavHLnvv6bkP4Md1O8rArSHSYBnUenspO-DK6eBmMG09PgQG7KFdUczVt08QwFPZIDEfErAQvhe_VX_UvaxcA9v0mI7vtfx4AB36bVUvfCCESWx7zrIwLFHDZTOgf8WfWeC24TSnmU-HB37dmVz-jfUbPoTpelacV-NpocfcMgbnh1s4JrITnR7NKAtfbuv11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وقتی در آستانه برگزاری ششمین جام جهانی دوران حرفه ای خود هستید، چه احساسی دارید
⁉️
🇦🇷
مسی:
🔵
بله، من واقعاً از همان ابتدا از جام جهانی لذت می برم امروز می خواستم مدتی بازی کنم زیرا با این مصدومیت کوچک وارد اردو تیم شدم.من خوشحالم، از هر لحظه لذت می برم و مثل همیشه هیجان زده هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91814" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=TIiQcBpsQuDIKdMbEAD8AFik7-b2An87Wq8p2yDzJAlYCueVAYOMQJ6s17algMRFHDFgseDne-6_hnxzXpsZ2AI_g7DbTNdr5mpjirxGR5Z92rELDSf9sAWHS4p5-4un9iCKUk0lNM_hau14FwCK6moTcmNmQGtCEKH_yOJG6w_kJi4WmXPqfhQjjAoGivMXQcpSMG9rmtN_Az7AMIETW0RPTw12-23SY9VuYT4VJ_ZgBqnZXon6sP1MYQYXeaKOXiXhMppSjdo5ya9dhJiaX_PHByRCW-vb-ddFGzrr0aLoF2GkD4cNvjJnaFaMkgobCfJQnCRAsU7f_OmF7hp34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=TIiQcBpsQuDIKdMbEAD8AFik7-b2An87Wq8p2yDzJAlYCueVAYOMQJ6s17algMRFHDFgseDne-6_hnxzXpsZ2AI_g7DbTNdr5mpjirxGR5Z92rELDSf9sAWHS4p5-4un9iCKUk0lNM_hau14FwCK6moTcmNmQGtCEKH_yOJG6w_kJi4WmXPqfhQjjAoGivMXQcpSMG9rmtN_Az7AMIETW0RPTw12-23SY9VuYT4VJ_ZgBqnZXon6sP1MYQYXeaKOXiXhMppSjdo5ya9dhJiaX_PHByRCW-vb-ddFGzrr0aLoF2GkD4cNvjJnaFaMkgobCfJQnCRAsU7f_OmF7hp34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
رایان چرکی و دلبری‌های قبل بازیش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91812" target="_blank">📅 11:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucOe3Wq9WYyUHA4zljMw-X7yN5xnyyg4tsxexwWJeieCWCSSX6jgxt7Fk1hw3g1avF7_iRGs96pOsULV1FhvQr9TpeVZTOCnZ3B9KYYEduTesScNtw-eQ-0R7JqQ8YWI7r4pxhB8BWxLC-xqghuB14uClWZsnMtRf9wJiqQg9I1EPHFYtfx1CSqC_2vh-rFoS1e3hbHQb_6C44SV7jmKUqBsu4tZ4k969gx0hJIMvV7ghLPkErIHcmhxXW627LD1vLF3hqvzo4yN7MFIggYuioGZWkZapikhVVKYfx32IP2x8oEquCBg8T1qPLBc8ApUKmH9vRgDalqDPSQlOUGeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال مادرید همکاری خود با آدیداس را تا سال 2034 تمدید کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91811" target="_blank">📅 11:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=pHovZRP85jsf8Z-MaD9i60mjZyYl5ZqXJU4Js-yYEJa2X6dBVGMRHio0GN0rLOoU0szoyBH84DDHHX-Y3ErSSokHJ2NhPgiv5p008o1DN7J0j6tgtF7RrMUk1Zxuz5TZPcq51C604EkCkiUJY356PMDBr5nh0d8DeoTrdq1wN6sEr_iIEyrFwcF3_L6-hRyhG6h-PqA-dqBHkhRifwZ4TP6fkPCZqZxlL6hnRuo8NDIs2ag3_USUwyKpJh7pZj4hVs4qTEdHLsWNA-nzEYWbUnwuPYbnxFjQzunqUfFDJ6CpSGZGLAWCJYlDNcYHKomY7gY76VeM178olAE_Upy6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=pHovZRP85jsf8Z-MaD9i60mjZyYl5ZqXJU4Js-yYEJa2X6dBVGMRHio0GN0rLOoU0szoyBH84DDHHX-Y3ErSSokHJ2NhPgiv5p008o1DN7J0j6tgtF7RrMUk1Zxuz5TZPcq51C604EkCkiUJY356PMDBr5nh0d8DeoTrdq1wN6sEr_iIEyrFwcF3_L6-hRyhG6h-PqA-dqBHkhRifwZ4TP6fkPCZqZxlL6hnRuo8NDIs2ag3_USUwyKpJh7pZj4hVs4qTEdHLsWNA-nzEYWbUnwuPYbnxFjQzunqUfFDJ6CpSGZGLAWCJYlDNcYHKomY7gY76VeM178olAE_Upy6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حین‌بازی رو گذشته قزاقستان، دوربین عنکبوتی معروف از سقف ورزشگاه ول میشه و با خوش شانسی، یه تصویربردار جون سالم به در میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91810" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiuisLQWNyKwf0HxI6_aLDDv4jAQ8SGWdJIUSS-v6AsTGE1YPqJI3QA2yaFcGiGKYMloTlK5wcU9VXqjx50W4Ug4mIh5RzzRjZ0Ag6YvdZd6IMpZwWgMoo7TfPUoQMYBIp1qLcolbF_TXOFLJ5MqLZ6vjvpdcF1g-Dy31qtnCgyUsdPqf0vW2lJy7UhTmxSOTXBpj3fYPMMfnUEmT_54FdY4CrRrAmFCivyio_y9zG2H6c6rRLpmBLzTH8tXmqunKiVhRv9xnq9NN2mCPEVGd-LHxnXRqM04dUUnIWhr1CmSDS8TwlsaCXZ21wSjnTM0si4vWb2T9-wCPICOlmkD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد مسی و کوارتسخلیا در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91809" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JavTvry6uhO1lr-MoBJxnAo5_saPepU7H7E0vlHyHZ6tIVryOi3W3jNyJ0ebkyV7bcca_KBQBiY00wi2aps93sp--G2SOcJ1vIQ_oACcrEW_JLYWauN9LTM88Zbl2AqQrUdEKAxP6efCzgZ-epmQOlCXNXzlG58gJ6lWNZXXHMUtPAbB9_rEZOvCM15WKjI2SIgTVxe7bqx4dXQaWLfDTKGrFDzNiNnU3hWJqnZiA0Rgnjh-gwvPVlxOmklvX1YGcPnmcAguoQnDSL06UNsEUPOFXKun3dRMZSY3kxqX2wvBNCVHpzHwI0t2ujs-zne8wLkX0qGthbUB88TvxOOHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
کیت جذاب نیوکاسل برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91808" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03756286c7.mp4?token=IevLo8ipIYBT8LIRGoRPLdeeUFbY3HMx5VG-57HM2kboZN_mxgwpiWm2gv6wSNkv_3KdaBLGMsSQGsy-oWoznyLWJ2ecw9qBAwC8vBOSM9GvDwWsQrQpQG2prn_GGYyG_PDzcZKWLQJtKq7ylKhPT9D6xD4qHtvfjLGgZJNViGdmA9Brq1DD-pul7c_3U-JlrQxD2i6YqPjj1dF9Icxw52Cg2C0eBpuKLI5YzZIosgiY3DjIs-DLJL4-a0ER5iTeLfcepFY30CFsVdggK1L8Yl7pqjlz6-N_AVq-7n4-upA4Ub08UnaQJF8hn-dtTdZZCbt5mSgyl89qCDP9q1aL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03756286c7.mp4?token=IevLo8ipIYBT8LIRGoRPLdeeUFbY3HMx5VG-57HM2kboZN_mxgwpiWm2gv6wSNkv_3KdaBLGMsSQGsy-oWoznyLWJ2ecw9qBAwC8vBOSM9GvDwWsQrQpQG2prn_GGYyG_PDzcZKWLQJtKq7ylKhPT9D6xD4qHtvfjLGgZJNViGdmA9Brq1DD-pul7c_3U-JlrQxD2i6YqPjj1dF9Icxw52Cg2C0eBpuKLI5YzZIosgiY3DjIs-DLJL4-a0ER5iTeLfcepFY30CFsVdggK1L8Yl7pqjlz6-N_AVq-7n4-upA4Ub08UnaQJF8hn-dtTdZZCbt5mSgyl89qCDP9q1aL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بارندگی در استادیوم آمریکا حین بازی تدارکاتی آرژانتین؛ جام‌جهانی با این روند ریدمان خالصه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91807" target="_blank">📅 10:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFnNkY23sFtgwX8SY3ojzJ3dqtQKWzkXGb8ZHd0rbDZmkAPVlDEBvdGVG45Kee1D8G0YbQw9osf_QDXO9TI81F5ZPUkWFPvTImgSr3lJui3X03tBEdO41EeYGdzHxktGznmT1LdYdWXsx0aob9x3efZ7K8Z-ANCB7tKfluGqVCQQum-qEuy5xq0DxQZ3R1JsuzH-K48ZJbYbakL7EkVkj9eg-WusQCUpfWxR9uQLNpkfDZjua11yGeTyTCJLPkkHPHO2P4YsmXtuh3i7k8VEtB-2Zf9angKOD2Ux0bg7prc-O9srHNG82-XIERtAOlnyOVCJTrSJzh49ZwnhCZpr3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91806" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBZyX-2ph09zlJ44UTS8TL5ad_Yj0ENAnZzcNohKYBS1igZgvFyWweSzLWLpD1q7ZruXZdOYDi7ckgZtvpcQINmL2MvZuVEy54TREuoEYGXCC9OW9MyRq3q-6sFou195_NF40kO_OHeP957nGoW4TXlpcuoEoSQxyXmMPBwvJhMRe6evW9Y9DieD-OmTVIbIG2djMjAPpG3mEGvDhC-0HibIC0YgraUdK3vkrX5HA_qTv3j-FABtOue114SyANoTkD1GEH-YZETq5mv4GOL9tGgLLa7VRMnl4hNsHhk2UgzF5UqKPvTUQWQimi0zjWcVYKpcz8uXR9v4ovwVDMQ7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlBguTo-Ye1_VAYJ8IBRjTfmOPuGEgomwVHZIK9PBr0Yfps_dFKaUsbm_zcW9x3bAleqNflaHEdqYOtbFa0UwzedEQHB_f0e8RvHN-wgEmHQyHQRApbrWqZUAx1y_l6UIHU15aibDbhF6_092HLCRwhrMnXSxOYjvHg5ftdh5J4wDo1WO64rjelANsbPyI7qkRDTqLA_i_sltjnZGQVg-foWqXBvuJD_JV-TBssZSK7BXNWiyUaN9DtWqNbLvQkJ8GmgqzncE7JDX5BIWLu_YnzRl6IXFkcN94UW5SHzCo0T0wlG6WOxeT3OszWLr1ae3jFKhXmDZBdrArlCPt3qJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ کاملا لخت ممنوع بود و این موضوع من را خیلی عقب می‌انداخت. میلیون‌ها دلار داشتم، بهترین ماشین‌ها زیر پایم بود اما تنها در خانه مینشستم و گریه می‌کردم.
🔺
شهرت و پول از بیرون عالی به نظر می‌رسد اما وقتی تو را در جایی که به آن تعلق نداری کاملاً تنها می‌گذارد، آن پول هیچ ارزشی ندارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91804" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzmlxZ2V-OG3ARGRYXPVg-5WuM0gmDT2ScGdtWSEqX40POSMd9t_dIqYvHgSIFnNxNSUcu1pTzJfv74A7VjYfBnrum7wss_CA8sVwcME0kq3A_QCTus6cmvxiP9LyhsyoiztzeXoBcYU1s3STR7Fv-1_OyEgUqaian0mpBSJNH7MvkOkksVGVqMkmYhi7faYQU2Nab0l0xMMMFOxWan949agHyp17Izd6cbCVWJDZlu-cT2FD0XyPA4V_osUa36rBkxXSpS1ud9twwTNbU0THPtbztB8iVqAw4K70HIJNpY7VDD4srVFKgRWjX-rVcJ9vw6p595UpGOLqAg_8GNSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEabe0b_6G8ZJ-mZdtPvfZjfYOegPewc32rICkbegk9j9lHmH-4ptdWfGbykz_R49A1wcl5Tq_vsec4oyQ9DZ6IjQ5oUfwcekIICLFB6y3iDvR8XxH0h1dNcFuDU--0sU3I_zHpqIFlgl2Zo0D1Mjmekm_L9P_SbvMcQhQ7kot5ANg8Cu2mvKg9ZLZIFj7bgNGvrFhus4jJvct_e-bwPC8uwhvEj6cO94w0nPiFsIP7930b6fhTWs_2BR1LpvAKtf2KH9heeiGGGvX_b8XYus_CoUepYiZRm8_3YGfrCLM8mzq27rXJZ2wSpBYa60HMzhom1kd2Mdi9YutrAbHSC-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🏆
-
ورزشگاه سیاتل (Seattle Stadium):
مکان: سیاتل، ایالت واشنگتن
🇺🇸
افتتاح: سال 2002
ظرفیت: حدود 69 هزار نفر
🗣
پر سر و صدا ترین ورزشگاه به دلیل طراحی سقف که صداهای تماشاگران را در داخل ورزشگاه محبوس می‌کند.
🔻
برنامه‌ریزی شده بود تا میزبان بازی‌های بزرگ مانند مسابقات جام جهانی باشد.
🔺
6 بازی را در جام جهانی میزبانی خواهد کرد (۴ بازی در مرحله گروهی + مرحله یک‌شانزدهم نهایی + مرحله یک‌هشتم نهایی).
🔹
مهم‌ترین بازی‌هایی که میزبانی خواهد کرد:
🇪🇬
مصر × ایران
🇮🇷
🇧🇦
بوسنی و هرزگوین × قطر
🇶🇦
😀
بلژیک × مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91802" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=E924zCkiHqXVLciVX7i8zO7s8jBv5ovoF6oELcyjz9HyGEQpkpyhBVHhDCIclIUi1_Q7QP7VSwZ8Jm6bTVxDSduUap-TcCH952H6xFjHTwep3jTkIRagAmAQx5AnQpNsV9MEgKsXmOdDh5ZOo8H5i3swrYq2851KWNfTs6FB_ItDNipceDUQ_Ji42Qi9hNq8hFrO66FbaJBqNowV8Tc35O3yblZ_RMR3Mm9txfdr3tQ-uvfMDxOrwUdsv4LXH8A4PYKEJQNKfmXIHYXOohWtf-zhqMBihM1ngnGMhbc6_zdIVgmjB6udbrPCSRNiOo4c7h6iOoOGZb6DeG8_XXBzgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=E924zCkiHqXVLciVX7i8zO7s8jBv5ovoF6oELcyjz9HyGEQpkpyhBVHhDCIclIUi1_Q7QP7VSwZ8Jm6bTVxDSduUap-TcCH952H6xFjHTwep3jTkIRagAmAQx5AnQpNsV9MEgKsXmOdDh5ZOo8H5i3swrYq2851KWNfTs6FB_ItDNipceDUQ_Ji42Qi9hNq8hFrO66FbaJBqNowV8Tc35O3yblZ_RMR3Mm9txfdr3tQ-uvfMDxOrwUdsv4LXH8A4PYKEJQNKfmXIHYXOohWtf-zhqMBihM1ngnGMhbc6_zdIVgmjB6udbrPCSRNiOo4c7h6iOoOGZb6DeG8_XXBzgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دیشب لیونل‌مسی از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91801" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dvn9ZDhYITYtJduEiU02uQi8GYFjpZrerK_R8kmsI0q0g6-k6Aq4I2lw-K-8x9W-A80p-V6q6DoTTvb5upaVTxyD2jaIF_LQgXWOSPUNvT2y8sRbWjfZTjuUZPWTofsubKOvmDh3wVWGv4WZL2dqW-aRclQJDkyy0hoROgQTAp9IG0ZVdDlIK0BM1Vlj-q68Iu92qJjrb3iPAfFd4SwHiC-EVPj7SAX3Py5u-jwvmfA_DiD6a5r4V_PKi5WgenJE4QWcuEuiQRk4AyHdv_Qm6dnLHw47IzqM67bNvggTRaIJSSCy7H90-NfP7XTz2X_sdPNY2ScRBqZL71o1ZEaGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMt7PrxDe5gyilVkdEC5NkQ712gropeVKSDQR-UDmXR45L54BBqE02Gu8yjjZzV4wxeisyy-parMGl0CQsA0bbIocWL3EeX_c41fbRj-ad3O8YSJkMD_6dThe20pYVhf_a9m841ISlUKfe2WFAPCWr2zLTj1vegQX-RGZLSlPTZonYLHNRmLqJHWF_eufPtA-7BxXy9UsxIssTGxCrAJl9RGI5uYxuk64VL4WErzsyXIpO2AT8nnvh3uteMLGze-HB_S3oMWdDJ6wwNzX-_-ESsFrQiFkY_i84tpq5VoklvHYvbqG-sDensltNVQbyGw8xw8g0671KpxWKAy4B2oUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوفی رین مدل معروف اونلی فنز: هر کس تو جام‌جهانی آقای گل بشه یه شب میتونه با من بخوابه‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91799" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMk3d5Buo0WnxR6grY_dbIWsGM93zITL4jdRvMrsPrJVmOsQ72rLNYhtBlt9OOSJR4-WIR_yp3cURL3UPHh9nuHAbYSYmHkSV2xStRYAObB5e74HcK6FqJ62ubgNBIHo6Rbze4jx8-IPrOVAMXbhuqA7riIdzri17B2KUdPnmLMpvyW7cC3T-SLm33HjUUX5pTOakeyXFe-6BrSzzihmzMhvJI_8xANYDG-t5RcI1a9UnKJbDoKzeIaBkzmRyDhKUb1NfSc3Hr4Llw8LSyCGqyVbn1HhN75TDFy5HfR5H86JUF-ADTOQJ-wiHDq7TkZ-1ZDRYjUAxhF0uBSfxt79hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
در ادامه بازگشت سلیبریدی‌های بی‌خاصیت، دیشب پیام صادقیان هم بعد کلی کسکلک بازی در ترکیه و کارای عجیبش به ایران برگشته و در تجمعات شبانه حاضر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91798" target="_blank">📅 09:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سپاه در جواب حمله دیشب آمریکا؛ حداقل چهار موشک بالستیک ایرانی به سمت پایگاه‌های نظامی آمریکا در بحرین، کویت و اردن شلیک کرد. ولی خب همچنان آتش بس برقراره و مشکلی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91797" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clet88oUI0Rypy8g_NhVJC-m2eG1cPmzNPcOkfTARbJ-laOPBe5F7dV53AxWCJf_PerRW2ZOEkk6oNNj-IVfkFj2FFTzl_m6hlWJAr_FHe3ocuW2WZxp5NDWSHshhL5je6OPnrE1fqaTGzP5omFXaYbQDw-jO64kC3DynxlImbfCODp6bi1VoT3okS0X6DW2fBXMkFeQLuCMu1wToCEUsVdL60pTkrfcC_PSKkcgxqPaLWaY0tYS4EfDH2Y9dikBocBqtiWrX9vKqit-oz-cxaTmFxsB2Pvg2wa4AYMyVRNqD8uSFxvVJEiUhMOjTmblr-gRHzEkH0ogGrLucc6cqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودریگو دی پائول: میخواهیم با جام قهرمانی به کشورمان برگردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91796" target="_blank">📅 08:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO683gTNfHkZdTNLg3LXmwyHP5PCG18OunB0cnJPX7AJwameEUy6E6Yvu9OuJOz78i65rd6h1zRNOCGl12oRUMmPQ1WkaD-QakORawznLkN7DkRsI6veiewihhb1pOv97G4zbf1NZ7M4hULsxy3lRPKs0hL2P7wrWCJvzSpmdNJN-jF9KR-78K9074z7TKwV6Qpz9S39moeMyfakC8vv1IOEVxgPEnejpWVqsB79cq5Ta7GIkuTm-FMnIuB0c1RyuQqyVx_6glG79vL0UVG2mZ2jxjlgnUaW9gSaq2q5zOhcbG1sw_7sDz4VnUO7I52eU_sudWU_eGEuY6aGFp_1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91795" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=CyCtCxc6OQtZeOd2odnepJQzqJOWy3Y2LOuEtLL4VfNv_vHWiZeyA7UNw26zdAacqGrYACito-ibMib9sW7X_tvPxEqYOTCfctkSBcGu5pQkr_j1gtUJLWsACx_pb6YuAqjCHWGR2lamIzofB4aBlnh62Ooj7bbMycp33nstL437-xWEsvOJfomHxOb6_-hmLjzHjtBZv_kPWtl4RxWfwKSXIuStNxLuE7x_jwyTg5VppsZSUvMPmacAzY9-qz9Gvdx0qZNRPyMlQXy6bq1s1m5qmwlF0coORtSzhEXLgt_ofaoFdyknRymPBgpA7eHRN2IBqfPf6Yf5r3nNy4BU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=CyCtCxc6OQtZeOd2odnepJQzqJOWy3Y2LOuEtLL4VfNv_vHWiZeyA7UNw26zdAacqGrYACito-ibMib9sW7X_tvPxEqYOTCfctkSBcGu5pQkr_j1gtUJLWsACx_pb6YuAqjCHWGR2lamIzofB4aBlnh62Ooj7bbMycp33nstL437-xWEsvOJfomHxOb6_-hmLjzHjtBZv_kPWtl4RxWfwKSXIuStNxLuE7x_jwyTg5VppsZSUvMPmacAzY9-qz9Gvdx0qZNRPyMlQXy6bq1s1m5qmwlF0coORtSzhEXLgt_ofaoFdyknRymPBgpA7eHRN2IBqfPf6Yf5r3nNy4BU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گلزنی مسی در بازی دوستانه بامداد امروز مقابل ایسلند که با نتیجه 3_0 به سود آرژانتین به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91794" target="_blank">📅 08:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4D52RbQZuxKDjk6INuCfnMfBbcQpsWOPVPilY7c1iJmYvUnasMBNzYxr_IFJbjGVRUWotElGCo-U74mCLAJqhc-t7eGve7ANS5UBQxOzLHC-lxeS_fJzr83dy-5rGxa-8oN55eS46eld3yUqccEiRHJk-wPfDms9iGajlBWzhiGFM_nLXv1lfzq0GHQlXhMHvyztBaL6z3Opab5gTe24Ey1SI0BhoBNMisqJaGH_1uBnO8_1JB73vxb9gWDX1OgyN-t5ls6u33vWkNKLxLuCL34tyBIAW2gCNAtGPSMoKTmHfFr_fVbZjsnX-ylFrfEQrUmzI9AzOhlrUuaoPdJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرزو رئیس اتلتیکو مادرید:
کون خودتونم پاره کنید آلوارز فروشی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91793" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=tVrjp9q_HsJzyKFxDYn5Qa5U_xAPzicSlGTTcaqiunXAPhPG23TLh94Du53bqbZxb-H_hQUXTAFErxfvvuccw3eNQV8WPEoI8qUqpPe4pPHR9GFEfQHX4p3xwSfI4DwzaIeJsRiZdwe8A_CxtGtC200IYpA5ry__R1lAKjmN_YiCwyfIW0PKPBuSgvhnFTTfI_U8bo7jCHBzRVYiMGF3XNsx-36OS3J9JCfj5kSZrTWB9c61JBWos3FmLjkkmIWYBSMiJ63dwSGp3-EketxiG8RfVJ7snpo3Jgqhk_VnUeGN2oyFZJhM3NwllNY25bTSmgVkkbiEJHlTIXKw4v5GwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=tVrjp9q_HsJzyKFxDYn5Qa5U_xAPzicSlGTTcaqiunXAPhPG23TLh94Du53bqbZxb-H_hQUXTAFErxfvvuccw3eNQV8WPEoI8qUqpPe4pPHR9GFEfQHX4p3xwSfI4DwzaIeJsRiZdwe8A_CxtGtC200IYpA5ry__R1lAKjmN_YiCwyfIW0PKPBuSgvhnFTTfI_U8bo7jCHBzRVYiMGF3XNsx-36OS3J9JCfj5kSZrTWB9c61JBWos3FmLjkkmIWYBSMiJ63dwSGp3-EketxiG8RfVJ7snpo3Jgqhk_VnUeGN2oyFZJhM3NwllNY25bTSmgVkkbiEJHlTIXKw4v5GwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که بغض تتلو بعد تقریبا 3 سال حبس، پشت میله‌های زندان و درحال خوندن آهنگ شکست
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91792" target="_blank">📅 02:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmtE7TUR656lyC1zPGlnJLQtS_NLX6poMHyQtAMPPWkJ0MztWm-34sYGl4T77r9I_uZHqjMfvUV0igE5UYlyaoe-7Q5qR1Nq0nDS2FohzhByCR3u2oh3i55I1n-kb6G2dxLJJ4ul0eYO8NaCG9-4fxZFKymWnUdyhaqdGzWgtL5uM0bfo3cSVn65PgM8EPd3WkixUtItDD5oDqBGI1Xvhr3CGP8nvpqOy8FP4VzWQubRtPGVChEtqu6GNdbEKIjFBSrygRREKptmqb_Qf4pzmBwzixeBsZRC_p7YiLNB57cUdctymtsiutFf9v3L00xTal7Jmjfq9JlA3ehRoZ-Rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
آلوارز شخصا با یکی از مسئولین رده بالای بارسا تماس گرفته و گفته:
من نه با رئال مادرید مذاکره کرده‌ام و نه قصدی برای مذاکره با آنها دارم و فقط میخواهم برای بارسلونا بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91791" target="_blank">📅 02:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=GwGZnd9rSf9N232LMvavdo6kTLwLtTCFykmP8uVI4qAKqe7cXxJz0pqEfpcoPr5ZA_B3sZVOMihhbXQK0KkrQlaqDzZ7V3skSohfCq9EKiJTYBaFU2QpgK-V0xe4vHLHOMU89DyzlRAE-Vii1UJsRPd6znq5vsC6M8uKd1_fSNWZ_gculMp0Fck8EzIn4LVqc3hz8mZ7XozloOX0QZZmh2C0jZV0ICNxFl8Ah4R3bovXSVD6L98uiyBgWX4xt4_HgKhzu-evGu4mHGbcLl78dn_nGRT9ypqqDg6rl2AVH-fyjqQEYzGd_2Md0Qz-62_zPA5hi8xGQTi2ZhWc938mxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=GwGZnd9rSf9N232LMvavdo6kTLwLtTCFykmP8uVI4qAKqe7cXxJz0pqEfpcoPr5ZA_B3sZVOMihhbXQK0KkrQlaqDzZ7V3skSohfCq9EKiJTYBaFU2QpgK-V0xe4vHLHOMU89DyzlRAE-Vii1UJsRPd6znq5vsC6M8uKd1_fSNWZ_gculMp0Fck8EzIn4LVqc3hz8mZ7XozloOX0QZZmh2C0jZV0ICNxFl8Ah4R3bovXSVD6L98uiyBgWX4xt4_HgKhzu-evGu4mHGbcLl78dn_nGRT9ypqqDg6rl2AVH-fyjqQEYzGd_2Md0Qz-62_zPA5hi8xGQTi2ZhWc938mxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات دیوانه وار اوکراین به خط لوله گاز اصلی روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/91789" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:  آمریکا داره ایرانو میزنه ایران داره پایگاه های آمریکا رو میزنه پاکستان داره افغانستانو میزنه اسرائیل داره لبنان رو میزنه ترکیه داره عراقو میزنه یمن داره اسرائیل رو میزنه اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91788" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:
آمریکا داره ایرانو میزنه
ایران داره پایگاه های آمریکا رو میزنه
پاکستان داره افغانستانو میزنه
اسرائیل داره لبنان رو میزنه
ترکیه داره عراقو میزنه
یمن داره اسرائیل رو میزنه
اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/91787" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/91786" target="_blank">📅 01:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/91784" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91783" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/91782" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91781" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5fB7qeQsHiQY3gx-TcofoQXrR0aENrCcyeWyr87SX1UrM7CpmHvnIQCmmp1145ev5KuUyDSspAVQP7PuY7z7Da-tRECxGAJxJOynfjCnLAXrq9pW6xEwZwsG4ATS1hgtggQYrq2TD31mI1aVpT3zu981CPeawK8QRblTfVFPHqLBgjIo-fQzoRIkfDKUwfg5AN1_vmlycjQlhch5hY5uLdWtOB7OPoSXkmFa3VS31WMIHL9RwvPidtFeMF5G0IsvQMGYLddWxHCjGlRmZoZABd8souRVI9hfrSKswSb-SjfSKlrTNhhjNoMhF_cCDua4Dk4hh-Q4TVj_7hoaKVE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙁
سید مجید خواب بود کی بیدارش کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91780" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
فهرست اولیه اهداف آمریکا در حملات فعلی به ایران:
-پایگاه دریایی سیریک
-پایگاه دریایی جاسک
-موقعیت پدافند هوایی بندرعباس
-موقعیت موشکی ساحلی میناب
-موقعیت موشکی ساحلی قشم
-بندر تجاری قشم
-کوه مبارکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91779" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
خاورمیانه امشب تو اوجه : اسرائیل دقایقی پیش به لبنان حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91778" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/91777" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91776" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=Oo25Pj-oucE3-LRhLHPxDPNbGa-QRf6TM7_U96LrSlcjCpTPwx1aKIE79igT_lqg06imPu1u1O1EWtmjfyrM8Cn6aWkUlL7HAXWE_vvvtvO2B53qR7lPKuzC40Sxn1QL6ofKDHfUfDB7UlflnPrO0r2KKz5eQs-yYs3ODmJiqqsjzGbWWJ8bZqR2Vw_I3NlFv8gfBFvBagrFMOe7FtlxuW_sQThwiwd2g3MfH78waG_reDqYZbpngkZgL4NUW2DlXwgtpl-4RtrJbsIfXg3N4spkX2YZHMHoqiI5fFFyy0KZ_aqcXCwH-s2tD8UoJcQ0c_d6ZhqjFfO4X0rfu2HIzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=Oo25Pj-oucE3-LRhLHPxDPNbGa-QRf6TM7_U96LrSlcjCpTPwx1aKIE79igT_lqg06imPu1u1O1EWtmjfyrM8Cn6aWkUlL7HAXWE_vvvtvO2B53qR7lPKuzC40Sxn1QL6ofKDHfUfDB7UlflnPrO0r2KKz5eQs-yYs3ODmJiqqsjzGbWWJ8bZqR2Vw_I3NlFv8gfBFvBagrFMOe7FtlxuW_sQThwiwd2g3MfH78waG_reDqYZbpngkZgL4NUW2DlXwgtpl-4RtrJbsIfXg3N4spkX2YZHMHoqiI5fFFyy0KZ_aqcXCwH-s2tD8UoJcQ0c_d6ZhqjFfO4X0rfu2HIzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از بحرین و کویت هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91775" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
صداوسیما: کشورهای عربی شب بیدار باشن. باهاشون حسابی کار داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91774" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خاورمیانه اونقدر عجیبه بعید نیست نتانیاهو توییت بزنه از آمریکا می‌خوام شلیک رو متوقف کنه و به میز مذاکره برگرده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91773" target="_blank">📅 01:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/91771" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
ترامپ : فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91770" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
سنتکام: در حملات امشب از چندیدن موشک‌کروز استفاده کرده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91769" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: آغاز حملات موشکی سپاه بزودی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91768" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91767" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91766" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccOxoCjkKfwjpDVP0XxddRCVdpQDhQVtmUqlDB4VQkgIgWXK-LoMMnVJx6-5QFZJcS6KQEFDolRKWh0roBNxgdBsKda7T5l2nURl2PvNcNzLtUI4jIsaCzzLQaJBMXW46K1elhH2FIbu5jIRhvOfSVrDAZOgyWYLHBSKy9OGW4GeGdOglj1n-t8TLRK6Ugg7MdHeug4cEkNdwXDooU-EjDTvfU4FV3RetawNBqVS9IBnPVIeySvGCUqkpT3LKdZdK9SB_4UrxCK95sa5pYplcGHi0Ck1LUC4gULrhJqwGUxL3ml3tzPAcZrspwXFEzYpmBjHSocMhiryeLlNd_3Yrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حداقل چهار انفجار بزرگ در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91764" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم  گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91763" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
