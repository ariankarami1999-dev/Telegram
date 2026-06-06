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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 211K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
وایرال شدن عجیب و غریب موزیک شکیرا برای جام‌جهانی در سراسر دنیا؛ واقعا محشره و همه نسل Z باهاش ویدیو ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/Futball180TV/91168" target="_blank">📅 16:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGybo2KC-z6uGfMMNxMyqYLNl79Mv2oSIV0y_K--wVvMTGsoma2_yxlcShbhSkWTJT2R-xzBm828ZGpro96_rFMRScjOPBT3daw4sTi-i9a00YtmaJIGz4LCv5dHx2ksM9UAeBjHS-O5clyrr2YLWkRJb3-xw0USU6aPhsC2_nCb1BYgP8Z2KQTXH8I8j4uCs4TYHeoVb4_gcyfauASfu2sxOqyKPFX-X38Yepg-g3ebTRqE1mi4r8YG2WJvQAJ5Y09Rosu_7a0NgXpSd3g8OBPViOoY9EiPRkcXfzwknJJ3KjdQjWNLKum7ZT6N4Mpjdi3Z12u9k3oBKxZEwYTtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
🇪🇸
فلورنتینو پرز: عمرا بیخیال ماجرای نگریرا بشم. انگار بعضیا حافظه‌شون خیلی کوتاهه. این بزرگترین فساد تاریخ ورزشه و من تا آخرش میرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/91167" target="_blank">📅 16:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت سوم ورزش در خانه؛ حتما استفاده کنید و واسه‌ دوستای گشادتون بفرستید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/91166" target="_blank">📅 16:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇲🇽
در آستانه جام‌جهانی، معترضان در مکزیک، تندیس‌ بازیکنای جا‌جهانی رو در جریان تظاهراتی برای افزایش حقوق‌ها از جا کندن و لخت کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/91165" target="_blank">📅 15:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه ویدیو از بازیکنای پاری‌سن‌ژرمن موقع ضربه پنالتی بازی با آرسنال منتشر شده که نشون از زرنگی شاگردان انریکه برای گول زدن بازیکنای آرتتا داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/91164" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
💥
رونالدینیو به یامال: این راهی که تو شروع کردی رو من آسفالت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/91163" target="_blank">📅 15:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBPKey0AWKWG7hadyn5G9nKtnSwj0xd0yoyi2kC63ZS1QKJTZ-S-uLvbnLyWUEL7jo1ZMb4S6xkrO_dP7fBhVdn5z3YiU63Xndw7pvSI7QftWkiATDcaTYZB4_EWknKAl25RocIOdI5BmKJbQKtahhhJMFGuMZBbDMRDP1xIF5_Wg9LgKGxmgYHsOmW945nZ2MjAgp2fd5DyBaXqjDvpLwwm-322AeVAzFC03RfTohrBMoSAOUDDjSnZT8w9vEXr9QQIXdE7rjkoAVbQJJitNZKLg6UNxuRtuXUnaTMasdoCZUsk3-1lZWJq2F_AkOzxVR2kPoArYmEoGjNp5r8iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/91162" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
یه سری از دوستان نمایشگاهی ایرانی از بیکاری اومدن برا پرتغالی‌ها چالش جام‌جهانی رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/91161" target="_blank">📅 14:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:  صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.  و حالا فکر می‌کنند بعضی نام‌های جدید…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91160" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucRu9PiUlbXc0-ziElXKWzG6Rw5Lak-ZgABv1CuQGDrjXD99sYOnIGwoKhiVPiINT_Yld0EpaGa0ch_9-U8adADm_i46HkKOwjXuhIGd8OgkLLGupe-hKPqatJm2tk3iWcggfAv0ccVVEyRFuZyv9Ha11P77nXUSLmAbVaJ5BNj0HccgEqY-blgG_D2w4JPTZvM8h-GayvOx6vbBvNXkpzdD_BGbUPufwU29KOtqXoQznLHE6tjU85IFIDakm6_bM8wWG-8gE7hGaj9Uwgn92Qiis-otuBCbisJaekuVJtj0otR14U-1ZLk-bCvBG8Wq8NyW4rupP9LhSFiMMf-9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:
صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.
و حالا فکر می‌کنند بعضی نام‌های جدید ناگهان آن‌ها را قادر می‌سازد تا با بارسلونا مقابله کنند؟ حتی اگر ژوزه مورینیو خودش برگردد، مشکل خیلی عمیق‌تر از این‌هاست.
اگر بارسلونا پروژه‌اش را کامل کند و بازیکنانی که واقعاً نیاز دارد را بیاورد، رقابت بسیار سخت‌تر از آن چیزی خواهد شد که بعضی‌ها تصور می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91159" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
تیم ملی پاراگوئه هم به این شکل سکسی بدرقه شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91158" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gweyh3Z90BKMXbTKR67bd1RhtU5h1rNmRbVd-ZpVa-ITykvYjV5eqhiA-QkGfKiEnkB-wZGqyz69EC3-TDo6751PTV5XdNcJEtB8y7r6sZ38EmC3hfBzGx0v4cbQrmUKd0aBiWmEfpww9nAwI7jSMTvaQ5z_EdWSm9WcqyI1SZL-GHc4sg-_MIhKKmcJzPCK23Ju2ePzI1G5jSqqTKPsikyp-_waqFKzjJ1am_jvGYf34WaGcRysC70bQFfi8IbojgJcztubYFwqDjCZhGPOF8lTI8g-IEnnX370_fB-EL-UeH8f93SBDu0-L9FIE1ilTpz7did4IErvftKrf5fBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دلیتا تو جام جهانی مجری خواهد بود
🍆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91157" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtYwfClyNmiwoTtxPI6dZvr-xa2Sod1IszwQ2bqzLA_men7X-UOWKq6eRmB3PrAKS1urSCOBCmv2CPDVibdMOR3hJePalSBnp2C7rSmacAc5fmxSGM_M3mdBplmqYQ4Mu7gb20VuoPGhvdwMdbgL5yQKAwSavOGXW-Hgp4gq6VSf4XYRn_ZLT0Dpy_CDSOvZJ7kgaaiWCAVSHxp6OnPElF_xbsxFCAGosKpw4v-S_h0tH3u383Uq0S9tWWp5iRq5iOJYAMO8_Jifa40HkqIKmPIu08bpaCiyP4UW5yQSD4OPYTmFztpAylDR5x43wnRlsoiJTRlNpC-mMt3yGRIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 سال مثل برق و باد گذشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91156" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdGE1EeWGNck2qT6dCx8Wb7r2NFchTNSD_hFn2BpbWXsNGyy-k_uC_U6pDxjVvdeQuxL0W8aMJcA8vALVtJCiZ1Er4ZXeLKap8q4tuEG1AvH5JgyXBQ7Ih0mSqWUsPREcbWKVDR0DmwqNGLw8yQNySET3sYb9fcBtECKyf25iEPaqaZzOI80JiVO8nJuwLuGeRHI8qbO7CoBHxWodRfn3Xarr0UpUaLAMuY0hj885NzfVbIAaglmij2PbAK5-onj6D0c1b8GhE4zFbWaxNqcI7kXwA6ktuPLYBa0cMmUwDQmQe90JVokQVWbz2CW8f0q7D2QzVUGnRBU0_YHViU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYVW3ryfu07r8xL8OjLcQJkK89BLE9dAUram6keVba9k2Pd1cNeegqmJUZTpNPHn5SJNhhqgFsfu47qQ3ZNVIjM0ZcVMP3q47pfcrtTSGrvqkfW59-cFz-3lMkpfk7QD_eejtaH4A9Hre7GXDziJaRBGAAbqrgCJohcSUJmJ3ZsBCnaXfp3xP6WtrNZoyuduLUhJT8Dveh3i_YC5wJFdSAt1SlPLWb-zd-JEm2gW6nBe1Kw-5STbkmV-nYM3uUTTnodtXmHeRXUKGTIMA6iOfrZJIwoZrDC-8m31JuQ_edTQn3XUIHtk80XI55CCH-b2nkcc6ijwk6fOFxdzVq9Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZImLL07aXPRlUhilaMQJNN5EfpsBtH1UH483p3OKj8L-F2HluR9bplFcPjEjQTCpb3as4uGUFc2bGd_Fvw8urE4n1GJvOg11LsLm1cKn0GcOi4nW36QZ0Ak3PMuvSv96wN1b4n3yHXE9HJsUMQ4YwigUVz1Ywr6FQiZebsrmFVQU5c40-nkJ591BCpHvcIcGHyJgpB67nPLjfvjXSjoY8mZsY2cLE-VSPSudkG0vRMSVsxbdBLoRSzQ4yaLPqo0ZFRWCCZo6gdojR43X1qr1mVkuuOjvL4KBe-blWOPEtKgomEx_NGvES9ufvO8Z8bwBnP-opFNe7tjXqFb62qGbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDAIOHYnCcuDGA8ZWc7w85Y84ReJoo7VKfAWM056aeFrZD0J7hXZGevHBcJW5JVCFv26Zc940csCzePng9blq8WIjK_UDap-JwXw43H5MEyGi23eZy-a_Rn5UgQqROG3u9XbMWSGdlrZq_0aTIrlRaNyihb3GPYgdmoDCp2TTqRb9MQ29Wm-fLrsTIXCb22z3BGWuSbVwx-5RzsOJtEJpCVHs2IlCLrU0N1b1FsY27QaFU1hHfmKOa0RhFmd0-XsSLlaqWq9xzA-H0KQrhUcqvBkalKtpa5rSpE7l84FHZMUWtRYzBQo3KJzKHcxQx1cwyWu_WD-a_Hs8Nx1rmh0cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🤯
مادلین رایت هستن که بعد از خداحافظی از فوتبال تو سال ۲۰۲۲، به طور کلی وارد OnlyFans شد و درآمد سالانش از حدود ۷۰۰۰ دلار به ۱ میلیون دلار رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91152" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ePsXRWeo0WxxqsLN3Umh3mJ35cEh5zF6XJEhA37nmqHh9ElzqOHo64kIIpo32LNSGUA55gI3NPUT-wqoL1GuGt6_spa1OuT9akWj-TUiEYVkThb71pbYjdivs2kZFkQ5F2-kNqmaG-XLu4SKiVUX61ofMoEwIBuAiLwX4GsttV9OI2SwO2Q6fHXOp4xmHMhluYyxK0BloDRFUyUTBEVe_1DeCwsqQrNuvh_jSlnu9YPBsDO2K6H-rUrbFG2QD3V2X1mbc_C-Nxin1-VpilexOiG7EsTBksFvL6kGVQj5do4TUCHSm1F8uTIYggxdSWYOiq1lejZayFywxzYdT3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91151" target="_blank">📅 13:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
‼️
موسی‌جنپو بازیکن استقلال قراردادش رو فسخ کرد و یه پرونده جدید به لطف علی تاجرنیا برای این‌تیم در فیفا باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91150" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J64Aa2ddxYMNZhhbzlwdSNs58y4zk85aVEPCgZfVXYRhHtoAGKIBdwit0YhI9pE0UT5oO6azu7QW4dileGA9cCFeMdD3IR7HGSwOuZbudoMbApyzp8Qe99jgxBFFpdgDZsH-PCZEoWWhQ-1WUGZuMFXICXNbadiBod3-KcbcpQ9f4ouwp47gsM8GnrIJ_obEAlw9ytjpnNf-845xbo5WEk9jSAMND-P_3WfYfrXgg8um7eTZoqcXdv7mlng9c38VYiLgIz8XGtx1iUfb8ukCpuZlhXnS5aOyU2PjJk2q9GPZX4bKYGcdpWNDqcS0NFYHNZ99fvVqOblZGhXJI424DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از ترانسفرمارکت، یامال و هالند با ۲۰۰ میلیون یورو باارزش‌ترین بازیکنان جهان هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91149" target="_blank">📅 13:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
#فووووووری
#اختصاصی_فوتبال‌180
؛
🔵
ابوالفضل جلالی در لیست خروج باشگاه استقلال قرار گرفت و فصل‌آینده جایی در آبی‌پوشان نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91148" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H3m9WiWezbWX9cNSaDjJWj6rkLRlE-56PpTmRTG2OKVQqX-VBY9gfBPurx7PcAwZ1CKD3DygrNt8yqNKIknfJ9rrk7dWUqLd99MmFjKR108_fb8eXvAFYxuwvrFMIS6uDm2sUZ8ivFFjMn47x-GNdpxRaHLYzVXOgJ_KHE-O0KInm1URuTAaI4-BL1QzSEWDC5CvfpcRguT_qO19VF3rNf-UpDPi6lV5hjI36vbJXLDuSJJG0J33rtIjPQmj1YKiFqEo_UEvyzxyTtT0LkaHzRJhtCfAdsRbJZioTC1-v8yNVdElkz0iwdxM92oDXZ34wuWuii_TLb-bBI_lEMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇩🇪
اولیور کان مدیر تیم‌فوتبال بایرن‌مونیخ:
🎙
اولیسه باید از خودش بپرسد چه می‌خواهد، رئال مادرید او را در گذشته غرق می‌کند و به بهانه اینکه ما در گذشته بهتر بودیم فریبش می‌دهد، مجموعه‌ای از افتخارات و جام‌های قدیمی، اما بایرن مونیخ آینده را به او می‌دهد.
🎙
رئال مادرید باید دست از زندگی کردن بر اساس افتخارات قدیمی بردارد و تلاش کند در آینده پیروز شود. در گذشته نام رئال مادرید بزرگ‌ترین بازیکنان فوتبال جهان را جذب می‌کرد، اما اکنون اینطور نیست و آنها هر تابستان باید بنشینند و بازیکنی را برای پیوستن به تیم قانع کنند، ما گذشته آنها را نداریم و آنها آینده ما را ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91147" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
وزارت خارجه آمریکا:
فقط برای افراد ضروری از جمله بازیکنان و کادرفنی تیم ملی ایران ویزا صادر کردیم و افراد اضافی جایی در آمریکا ندارند و نباید از امکانات ما استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91146" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiOM5CL92d9Oz6OcClQqPxDDmmHPKdKgXqX62Hejl4ojrkpneyRhvfgkSAXxFtR3C0msvAckvFBg_4ii0oatbSWBSzGPiGKXxu69sx5LKc5K2ZBhxLJzciPy-b8TZYaXnIGUwJiTffSQtEpn_B8h-pea5lZsLNMw6LTkBDYCQ_g0_ApLcTwexpyzD8c6zz54uhDeyJIaG87WV0J5qG25J3uL_BDpaIFFhKp7Yf5js_Yk_4i87wiC15-YzId-VKC46Nbe_xC_of8zEfle6fOgqXEGwf0rop30E3GCcsFOwxnXCQRo1xBCHDi6RzDBDhjds5mj_rmhC3axnbdVZ54Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی مختصر تیم‌های گروه A جام‌جهانی
🇲🇽
مکزیک:
لقب: El Tri (سه رنگ)
سرمربی: خاویر آگیره
ستاره اصلی: سانتیاگو خیمنز (مهاجم میلان)
تعداد حضور: ۱۸ دوره (یکی از باقوام‌ترین تیم‌های تاریخ مسابقات)
بهترین مقام: صعود به یک‌چهارم نهایی در سال‌های ۱۹۷۰ و ۱۹۸۶ (هر دو بار در زمان میزبانی خودشان)
دوره قبل (۲۰۲۲): حذف تلخ در مرحله گروهی (پایان رکوردی که ۷ دوره متوالی از گروه صعود می‌کردند)
نحوه صعود: به عنوان یکی از سه میزبان مشترک مسابقات (در کنار آمریکا و کانادا)، بدون شرکت در بازی‌های انتخابی به صورت مستقیم صعود کرد.
وضعیت فعلی: آن‌ها بعد از تغییرات پیاپی روی نیمکت، دوباره به خاویر آگیره باسابقه اعتماد کرده‌اند. با داشتن امتیاز میزبانی و بازی در ورزشگاه مخوف «آزتکا»، فشار و البته پتانسیل زیادی برای صدرنشینی در این گروه دارند.
﻿
🇰🇷
کره‌جنوبی
لقب: جنگجویان تائه‌گوک / تایگرهای آسیا
سرمربی: میونگ-بو هونگ
ستاره اصلی: سون هیونگ-مین (کاپیتان و ستاره سابق تاتنهام) و لی کانگ-این (ستاره پاری‌سن‌ژرمن)
تعداد حضور: ۱۲ دوره (رکورددار بیشترین حضور در میان تیم‌های آسیایی)
بهترین مقام: مقام چهارم جهان در جام جهانی ۲۰۰۲ (به عنوان میزبان مشترک)
دوره قبل (۲۰۲۲): صعود دراماتیک از گروه و حذف در مرحله یک‌هشتم نهایی مقابل برزیل.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در مرحله سوم انتخابی جام جهانی در قاره آسیا
وضعیت فعلی: کره جنوبی ترکیبی از با تجربه‌های باکیفیت در اروپا (مثل کیم مین-جائه در بایرن مونیخ) و جوانان نسل جدید دارد. آن‌ها به نظم تاکتیکی شدید و سرعت بالا در انتقال توپ معروف هستند و مدعی جدی صعود از این گروه به شمار می‌روند.
🇨🇿
جمهوری چک
سرمربی: میروسلاو کوبک
ستاره اصلی: توماس سوچک (هافبک و رهبر وستهم) و پاتریک شیک (مهاجم لورکوزن)
تعداد حضور: ۱۰ دوره (با احتساب دوران چکسلواکی سابق) / این دومین حضور آن‌ها به عنوان کشور مستقل «جمهوری چک» پس از سال ۲۰۰۶ است.
بهترین مقام: دو عنوان نایب‌قهرمانی جهان در سال‌های ۱۹۳۴ و ۱۹۶۲ (در دوران چکسلواکی).
دوره قبل (۲۰۲۲): غایب بودند (نتوانستند جواز حضور را کسب کنند).
نحوه صعود: پس از ناکامی در صعود مستقیم، از طریق مسیر سخت پلی‌آف اروپا (UEFA) موفق شدند بلیت حضور در این جام جهانی را رزرو کنند.
🇿🇦
﻿آفریقای‌جنوبی
لقب: Bafana Bafana (پسران)
سرمربی: هوگو بروس(مربی باسابقه بلژیکی)
ستاره اصلی: لایل فاستر (مهاجم باشگاه برنلی انگلیس)
تعداد حضور: ۴ دوره (پیش از این در سال‌های ۱۹۹۸، ۲۰۰۲ و ۲۰۱۰ حضور داشتند).
بهترین مقام: حضور در مرحله گروهی (آن‌ها تا به حال موفق به صعود از گروه خود نشده‌اند).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: صعود به عنوان یکی از تیم‌های برتر منطقه آفریقا (CAF) پس از یک ماراتن انتخابی فشرده در قاره سیاه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91145" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA_UVDOLhS0zeR_LSSLTXXQ1kdpEtZ7oSODeRLpI-WKTxok0dQhd0jQGtwfLy-td0KWwbQGPU02DmYQ2cfPNFSbxaLrNZppy2Mzqnqi7FcR39mySSB0oT5gLQqVk9RreIe4KxxKsgEiONEL_isiUnQmXiOjneA3S3zirdHTmAkzaNP9YD-rzVcbXAKP4nd5gySSJTNjjl6t8_WQYdkw7-oshBdBgknI-C-kMQGp9P8fBEBuPr_O9ApTR0MSOlrT_QXiWyfFjgqlmfHZvsOV0r3VfnRnp7rsp4KZH4URAgvD0TNA-NuJ54_ZqPrTeh8B9QWEFGZ2qq64JpF3oQSCqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاکا: «من علاقه‌ای ندارم که فرزندانم بدونن که روزی بهترین بازیکن جهان بوده‌ام. فقط می‌خواهم مرا بهترین پدر جهان بدانند»
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91144" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-e4yDA_cPSsig_65DdXqlTpHsZQgFnWBTWRwn-Fdl1Z6gxnXWhdGOS9MloSUwbqMOo2EBt_X9qVE2LNPLK1776xWGA4fHaFTwmyfNdIRfI41UE9K21UpTcgg41M5qWYhT_3NnPv8dJucTHXWMVUGUzbDROSh8t9-JA_f1rWIjRyWN7UVPxZMMBFVPZYcOMzjNol8FKbd2TQkCWRhopd6EeoXm7KAab8srpxJpKZarPKJc9dCiNcxsIyte-i_W_ndXmq7POQj1i6nracO--vfxIX59IK9HaaRafhskO4r07WbYgTc6lcKGWOKuDabnSLtG-5iga5RISrE_gQzq-LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7pDwI8WWoPYCEEQIBGE3Iq2haXU_JHWMCWHkDh2MbY8I2n08al61wVmOfhSPVtWiTtHCyAxWUpgxBvw7-dIt74k8hjzydW1g_vE2KmIlK-6QYDQySIV7XpNyCDE3uVrF49prlWP96VnP5rC_oc5vxLgJH43ONv2aeLKZiAY2UR4PlSd8IwYMkcJ-yXtjvTquCDow600X32WuFScwVfixwaBt2bQ_VYFmXy-MYwyudHYAJFZTQo2UH4AkM9Jm4JOsrJJMO7JHuPotwT8Qn3HZ2TsvmdsPz5FxZAC5BL9cjGXdXwpQUWhrS6XMldu5vumVw9hlRMZCNtVdPSHqNuPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UJLu7vL_BVfqH5u3qACaIFrA6czAH4glnu1bj9QJUZ0YS3cnFy99ZzqTZnBjxb8ps5qhFNWy-1bt_pO8H4ne8-ZypxjCH2yw1KKWSL8okhuYS71LzMB-bsC1yZWHRXz7mbbClH2u9XG734eJPPNvM3GlKm6_yfh8DswPcu9yP0qVXVGcthGhfTZZB_Ip1W5K_U9-iUZLOZj2KDCJ61uHeD9IV2WBQxuJNkYkvB4fVPnIhRcKPh80KYqujgZ7z84H12BeNvZzvOcivAnBlTAiYxkZP7BpUx8yaspCsk-jcZX0s8uZGwjPfOdsE2fYw3q-wJQAWf-MYWEllEw_Shpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت لیگ پایه استان اصفهان: پیشنهاد میشه اگر افسردگی شدید دارید و مدتیه نخدیدید این ویدیو رو تماشا کنین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91132" target="_blank">📅 11:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعی از هوادارای پرسپولیس صبح شنبه رفتن جلو فدراسیون و از مهدی‌تاج میخوان این تیم رو به آسیا بفرسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91131" target="_blank">📅 10:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn0BXD-xp1B-n3TAnhWVwp5eE0zUZMnRXz_HF5YLUEYOOpiTqMcRRKJd25ebxBd2rTjUQI_LD5yYjxxJ7W5GxW17_9IkFMnV4rNXOFNVGq33LvO6rpGyWymREeWm8ZlPTyFBRO-xnMSoC9oen41ao8Gg9YNmXem0OmBQDIH_kfpw1i7lkqMk81mEuAYw0M5q22LGS0Jbm9PUHc-hKZcsB8hUfKwtuAqcPMQFXhzwK59H5kfzzGzO6BblwqA_DdDEUzZwt-kro8fWbkZQqvZq1E2D0FZku9y3-SqBrA5MggzIj0UsxbjbT2xCRnvuMkiQMVUGaqTUFUgIrVllqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری
؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91130" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91129" target="_blank">📅 10:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss6T0DR7HiJ8fWqTqeqdvlWXnwzZlf5oAsPlgYMOFHtylEYStfYwD_dduJgY0SgIM5ruustZkQkUG5_ogICLtNy1QP2vCFyRkBUGB4SSSyWwogayPrTgqRn7HmryBbSsemN3rSN2ZF2TkgKAakoZolI_1a5PcaRnAGuCvz74L9NqbpkocLnfAe0ahwEn_cs64W0CPXi6W9MOe14iyOq7M5BGtU19bM44kxH4hIdf0FG_GVu7bZ6qzg8-7vwwU7ASfoKlrIEOIYLZvd65MPHIJgJ_5CJLHEZp_0ITEoyGUmEH5Y-jdgZGPMqgQk_8MuUaMt7G4QQsVc5PMI6H6K-gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری
؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91128" target="_blank">📅 10:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91127" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زور این دوست عزیزمون از هالک ایرانی بیشتره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91126" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
‼️
پشت پرده اخراج شبانه و غیرقانونی علی دایی و دادکان توسط محمود احمدی‌نژاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91125" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1Fj-KR3eOvkO-X11__cNhS4rzG0d7VATK6SCJV0AjCKQMvWzy3vn7a8nmiGIBO1lGBG4xrMwwiSlsNHs1-mWcWgHfZre42BZKkL5KOnvfgoMCzcXpDTwVkvUP5SZ4e1cxXNb7VUimjP6dIAokKAj7qA4GpV813vpT7GJDzYrmn_GHRXi-nAo4wR4jejkwXmHQF-iZl-pZY0aJ4a669vqJ29_CS6-ncWe-xHsNv43-iM_0gFC0n6vCOKsPDIr6QtYBYliJdVc31vJ0Ny4S5rv4t-fxUIh_o3b7ZbY1AOk7hxdDHaZ9BB93Vcx5KZog-idtOTjx-O5g72102v9jQVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfsMXgnJWi7nGlYMQP-nGNtR9qBh6xLBFnYYI1KpVs3gwD3nW_eQGWErzFkKkfLLHl7T0aysCFo-Em_LC-NDFhuT0pwBas0-FEQHWBbOUIbiE4Z4YI3qI7S_6oJCmImPCcYE8h7EtRuT7SoDNelveProXCKLDi8TweUFGQJp45fc00kqGWJ_Xd1FdFQhHHCtd-iy6Bem_jbW8_1oQKWoX8i-SZEXZOt1x4jOdQqpUKEpyR_2tgYcTYgmATomseLQgzeyG3mOuU-CcjOZrZEn1SmAhekkqlS2CHqKBjm0YADog-gTSAbhdzZV3E_4PvoX60wC-ih2nC5H7E3IB0WP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3j5TMGdgCAhV2Pv5o7GDLoVu_gB8cxON0Nya6yURXDi3kCx0arzpAN_mSvrAedHmTHifmVSjXmNEDKkfc45479lIukioekiW-j8ZGwoqmIqa9do_nGgLWnh8bGpJ1XUzeuizmAL8htx_g2k8emeWGJMQrIdzhCX2GsJyfodLuUvZM2H6YHg-cGdoKkCRf8jjxl8ZvePp17Rweh_2NTUK8fWk7G9be5lYGpv1NT4UgCu9NCiSxplf2q9suY9vosLxMksmtC9MuT8-GVHYgAqNSA1xqP7iAsQkldKlP8N2D4qfLMeLGtxOoWhw07YOeBIGYjlk87tsdp5DnCB142jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKempgzb4IDdo-lCOAhO0-JMj8DOsbKlTs3_Rx1R0uotfaTASr_Zond7_aHkptTkIuEOygx3stIIubNgOoPs6NXy0jYMvz8EzF9wu3Jvaf987sEm0AV-VLDikcig7JUm614cm__CRrJO-w-FPld7BR0rCnM3VqjVc_OpblYxwhfsKPog8JNN8zz4u-HFQkscq1vvOeJ6imFAs3nVoEqFDbbqehIXcZelZtDAM9A2PboQTwE2iTrqqN_T2Rr5S-8mKl6D-Y9UBS4LV4J-D7HGjH4p7sj7YVLCN7JMNZckgjCgj8F18Md9_U1Wu9cP6tp06V3i3TfZPhlkEHlptzsZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktG8yM56tM07r-KrhT0mvzu1K2zogyYISs829eHMKG57zvUZledcWcs0Y_JhOfY7P7xQz5vI09K5w4AAvsMLC2N7mBXDs66RppN9hVr4tk-TjK8RPl6xx5NKsMv2j3c6jznY7nBv_n-VyB3Nw9MLNAsCgDj6Nx-HMy0VEXmIvLtIh7czBz7XjPw9nW_fX7ZWKn2dC5M38zPF465Umt-JhuLzyyvbP2VS2dRK37JFKdWGiI1BkVbKPAjhyoS7_ColyYJ4ccaKnP9h6CvQxSEaF7__QWQo0eQ_LkSaYE_QZKIlE4FyV-f0OzgJKug0PgogyFgwtWTptfjPM9rx5zdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_2P8bSu1dgqGwGJBYUZiCLRR3bktI4wGbIUmdA_lFTj3Gg7AEa8RUQozy0N4UcQk_GgioR1e3nQeOD4joczZqNiLbROyCNKnmcunTaaFPmHt9qH_fdLMuxi9QtBde-rPTo3tIFGpcHIeMUZPbjQekZAnNzAIln7ocw9M6DtTbUEdgFLk8-22wghDaAKDWpbh7nqQcq3amB8TPFDf29zAJc5uUvPq0kYReSqqxtzccpFStlDCcxruNiVX9NBIT82PO7kFJ0xSbaf1Yn8o5mnQLUg4LRvlOrC2g0OX7v937MGgvR_d0iVHPnq7sUnB_7PCt6DBxjM6UT0PRFVVNuzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjCLtEjhx9MES5c_jSZ-DspolCpiUQ98xoSqWZvsEmbBAkYHDWwjjNzhT5JiznB_iDVuqcJSR2taqRWkYphHlO-pe0nsImXgqPehTazCnyFaeu-aofyNeuGo8BH8-fxdhvIg4r3nCC7yOgLZJyzK21o3HDJhvX_MQs52zmJ6yocwhQ2mzDgy1tEgqFkQuO7CHvmjDc_t2sGWgERUR0aFaZ0g3ShPHdHxVn9T5oucwa1VsAxY4VXS-_JtO_BaUGbzqbJzuPHrF-ECphP0NNFA8cB5pfxoid01IzgbSsJ4gs43j6gM0mI0vdTUqa80wzxxrKgbPIJ1ML2ftXaTwuBNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpIL_1pEqEhyp084TeXTYSC98kwhvEDzruKmqlonaKbbLaGbMAWyoimqyjyVRtVy6VCRUeTcDPDt1qejOkQEQMHFjE7S7OCdkmskb43OLTy4fqsA1aIOShSMJ_7e874fitTTYHvmI-XALCT_PPt9NBfWIocHcAEemliIUaTV-3ioGlDZZFcq0zB2F1rP5WJLfRxwoT7lfXazYu8rbHhSUrMLCBfR1KkjytfCtBsyvAq63MKlC9dRJ1t1e8VPfb_ptYHapgcpgH-EPI_nfh5LSNhTOAskuOSk2tVMrJM6LV4u49gkkXvklbAqO8ZKSenFwPypDHNxbrSAQ55rlQsW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارل 18 ساله به دلیل پارگی عضلانی جام جهانی رو از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91106" target="_blank">📅 01:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KnvF7uEZORIc5CHKe8ywUJ8skTEeHyWkbn7ZnU80WujqYI6wHROu2otj60Dtz3OzmwZyQ9LmYA_yEvAkHMaBWbRYn5zVNwncQtBhYyR08YZAMvMrQDVptxZ7OFE6IgROBCUQdRMwWa0j2emNT88kY68hXjIariglvd_h10B25owj1sCqcpcjVH8UGY2zSx-wXVNKQSmkO05vUTPtXeNE_mfM0hnt_LcjERj-_8A0CjLgRhCNZZEcFf9MluJXEAqJSDmf1-8BQVRV9yFxJPGJicSv8HGPXb_KOYVKM4iALCe8S0aWa5qGAqDbntiFkGDJDdxzkA05VLat0itLrORCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری از رومانو: لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91105" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
فوووووووری از رومانو:
لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91104" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMqhqjn4wId8418VU6GousgiGEp2zuleRRmp4pWFkUqUcMQ6mhQIxNgUV4RNzycXTbTNi1goUjOO5hS8oqgBiKTdyPXw3ffLvdHvQncM_KLELPC_OIfIbTJW5OOL1L5gKjetS0CD7hkR8oCn_URwn2Kjxfq1o6eoCQbl0-qoBXsAdB1HQPCjey_Z_kUAqvDCT8PeT2mirQOZf57Q52fmHPCQmL_0u01KDU4cQZcla0K96WBF2BgemHBHARB3vlTLIlzSgLzXYFI4iCgJSBmgXo4GWpK6_5A7gYJgaaYDA2nZaGAQcd2agZ0v2YJ6upL08r3oT515QWTJErhlTZqCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب مایکل اولیسه به یک هوادار رئال که ازش خواسته به رئال بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91103" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=l27ymBxjE6ela19qTDaCXM1UlX_Yrw1hBmFnv4NvUrkRpr5S7f4xrnBab5i-HlISdNIoLiNO1KM1FFsN6K_ukcP55M-8m3318Nv-jwV2NXAJZvj3bOjdi07FkzDVvr10ee7ZtovHOx4M_t9Krwv6gFQayEATt7FQO60pN1Iw2dofC3KFPnM4QMDOP_Z3QzkCifQIKCX0USeZqvpZQfex4emlkcoWc2I39rlp6FnUvQsXTY7vlctMg_s7sYpnoC2QsuksodHdYhCuHXTBOpoN1gOysrdQw7dKNxHfnb5FCqGau3An7pZKFRY4W9TWAbqjxNB7Nt8JR5ZzPxNBrkBlr35KPVc6Za5dKbr0r9lwyn_un-fkXFuqRPyIeUtB2v4FWj_aJi7nsf6JMs5vjgrHgg8K5Ujj452XypQw31TBPZG7_xP11J4IA-_lnCN_7fkCUpqsSji7isudReJSmaL4mFz2iAys2NbpNEFzGdo2nTQL7Eb7i4dhdHP9xIugUQkT7eg4IhJID4qYwhqTKFtYhQ-eLQE63FBbwlyKxrHlS43ooRDQo6WnPO8gwI04xF9d7gX2kdOga21a-2fSRk43lUeCwen2EBRjLYLVkdOX3QlTG2l6HxkWkjHKXwGax_-7pZQb5XhDUoNWgJZh7BtyluV_omKc9Qbdt3cN4rLp09k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=l27ymBxjE6ela19qTDaCXM1UlX_Yrw1hBmFnv4NvUrkRpr5S7f4xrnBab5i-HlISdNIoLiNO1KM1FFsN6K_ukcP55M-8m3318Nv-jwV2NXAJZvj3bOjdi07FkzDVvr10ee7ZtovHOx4M_t9Krwv6gFQayEATt7FQO60pN1Iw2dofC3KFPnM4QMDOP_Z3QzkCifQIKCX0USeZqvpZQfex4emlkcoWc2I39rlp6FnUvQsXTY7vlctMg_s7sYpnoC2QsuksodHdYhCuHXTBOpoN1gOysrdQw7dKNxHfnb5FCqGau3An7pZKFRY4W9TWAbqjxNB7Nt8JR5ZzPxNBrkBlr35KPVc6Za5dKbr0r9lwyn_un-fkXFuqRPyIeUtB2v4FWj_aJi7nsf6JMs5vjgrHgg8K5Ujj452XypQw31TBPZG7_xP11J4IA-_lnCN_7fkCUpqsSji7isudReJSmaL4mFz2iAys2NbpNEFzGdo2nTQL7Eb7i4dhdHP9xIugUQkT7eg4IhJID4qYwhqTKFtYhQ-eLQE63FBbwlyKxrHlS43ooRDQo6WnPO8gwI04xF9d7gX2kdOga21a-2fSRk43lUeCwen2EBRjLYLVkdOX3QlTG2l6HxkWkjHKXwGax_-7pZQb5XhDUoNWgJZh7BtyluV_omKc9Qbdt3cN4rLp09k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">First dance
❤️
Last dance
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91102" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5rluRmqOEQyXoyurpaFvOK9ZImLrh9BfsaE0acYpwEmXh_4VqRD7jLrESNEUsAG19MMoEebzllLConGAXdMajli0sHFl0NLJgmfot_38iQiFxRQk3vTd4ykF7ozm3jH-dr5LWxvq4m3s0RPphROiK_VXwjsogmSDvQYldoGR-1faM5iFbbidB-av7CKUTJZfiaLbhsQ4-trPtwU3WkxJ0rc49J_GfUkHWz_pTQHUzaANE-j8kfGc7cadNw3621NAI0yg-DGLBrihaFXceBth54h3WFaQiPHtulw4Sdyt1rvuxdnfAElWqw9pqSSeNcmgrGJedDLWmT2hsSjShJs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CneoCr4oz0gBih6dXfr6dHxbrH0ym0_Ltr0EA_vqZLH9KIFUNXjHXucCHH5hpHWvnTKNmY2kK6l3BovYdtVh3DN75sIzX82CmUaRxlViqEO0pKA66x55S9pYDPlT5Kh4y7uVtHu7OIgyImzSBSlUCAYCLBVwcZH6ji-e49oxWaIdZ6UvHbQG2m0yIa-ZdOnkDEhk8aTK0Xq2asp8GgvkGbW3VWyo3h0JMC78kSz5FZzZWIZ0kx8-bnMH83_xsImLx2pxQWo0Zw4QLETLQ1xRLg3-x39E7ffNrsJxtcF04RrSGM4H9l_DMO-lkOeTCYDd8f1Vac_bKsjPEVaGw5Cfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zp7yI6eNZaP-cMGQhBKPmLNGfcCbaRVeMGKDJs-wjhUvabs1BpmMulEsmoKgGCiu_xW7aJPIey7r7EY8s2wIMYnqlymiVye4uOwTaZLT1bjMlL7JJOOTP8256NjfepmKDlo9t9_HYhKpn3HyFFji1rOhAOu-tre4o_fwnxz5kgfzZrZ9HoaKa-Lspf_UrII0HEQKkbujNMCv4BXCiKL6uXl5ebmculE9gipm_ZP_tNrTYf-A-pUaEj11HHDdd1ypAlOTwZVnxg5TIzVAvmiDBJXUudDvDX9X5LSJOUJF9R4hbCN9ZEa1TcwujV06mq_xVKlpNAEsKnEiYH1IDJr-4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زید سابق و با کمالات وینیسیوس
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91099" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX9Up0s2BEI8PCGkIwVG8k8P2AWrzHxjXJG4pWL-ArGoC4BdFy4IDiW_Iwdqvs6SmcKIl-X3mkO2-NRoHyNJH0uOfpdvChtd2EpyHJPpyIaxYCUBrl4mHYVxGtG61w1qpWOL8zfNJzr6c5qTwI5jkKcmVglMZ_yv-8rz1t0585utdVFBm900o_WGL9HovSwVjY3azoWcP7vXdqtLRJ_h2itQvTOfyS5WWoKp4_tx47DBtPqRBv7zub93Ph42VvaIgPwVau9g_0dBgo8yrpLX7Cz1sAUiUwlKu_T3oN4Tg8FCgS7OILvZEnCkHNlG7wjBmQqL2VElL9ZadbXgRqzXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال همینقدر میتونه بی رحم باشه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91098" target="_blank">📅 00:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlzjqyJcpySPVjoCmlZF2a7FmJLu5BbOS7cIy5Rthslfe2f2L2wVjW2VFCVXI0rFHQiLIHcKZH7W71t-b3-l8t5248C5XXtJxV6mzM6i1ZI5W2nuZY-1WMzbi0ju2CuAhepr0J9l1XWrG_YaSpjP9CV4Gdyaq1616jLHM0ks0UO5YWd6QxFE-S5QLIG0r65ot9lvwolxZ7bbxvxLG-EEHdLg_RD8Q7q3efGkG6CHyOSSFRm5C-6ESevNoCfIDNU-NVOX4HWGPWJ8mXE87qu4BpQiS5R1w2OKXSx-eCNM9w2jKImeylYq8-0GY9A8MpFNSWaQCKLdEnw8yqjaY_DBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ بازیکن تیم ملی کلمبیا در عکسی که مجبور شدند قبل از رفتن به جام جهانی با رئیس‌جمهور بگیرند، لبخند نمی‌زند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91097" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91096" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNj1jpq7KBLdfItDmhBzwo1WlxaBqk5_oxuetzPAP_kh4mJW7xJpzTvMYPhNQ-2KQe8b9mff6V6_HW23p9diX3SZcEEj1yQWVKmLMnOubtLlIhyKoGOWI2O_XY1rhkdaE_hzHR2Ze4VGK0fkdnjbVlTI8iNojyVnt8Kby7KfTjl7kdpKEgJcz7YodDlHrEFxuo_4l6HOQM_Y1v3T_DjswkaPBaXa_uhqA5bWBxTCaJVZyb9G1s3FtcCHwsBAA2jVMcPP1zUMgoN6e77MCrTpPix3hTtVB9hFP0zebNHmwgO653Qktm2qCfl3NZtsJMXZz5-th_3DUP1SLdg6MZyebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMXcCe6-D6z5tae-hpLGtxHr61-H23wmGAmR5GWpN2-FF86rox4CusIs7G2rO_i0v_hpWt9zXqm_y52qyQi8DOWQrgU07wX5PbtGqrVTEMgv6WBAyhEYI88bwkJc-J_wv2TgzToeBekFMVJZRv0E0GR1k2WaeDEnVu-W9IqRTRc1OzuXRd-_rfnUTNbrBO80SOBp_2KRWwIzM2EqGPrJYw_uAZIemyfx4viBXBxIruYDiVUOpzXsvAU0zx1YmQ740HQDCEA8qu9ZxombsMuyiRglXHAUI9T_B55d-xcf91ky2BwAnSYo1sWNld46KEMKcXbf1MWrj9f50F04rgn0eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91094" target="_blank">📅 00:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91093" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOnDKfIvzhtN5kYUPXKSNx_KDfatM5D3h9g4SNosXl4GfshLkuFkKuQ2xE1woFGDe3n98wYD4JI-KbA6z5z71fdT7OhrgPuKSIuJGB_0AO36jjqPrdm1Z2AdMh15eZ4fLH16ELmkh8IERjqtWIreMUTuYhCivwtsiQC3bISoBUlnhAy1ide986ZJ_7RvUITPovbMAqLlxrO8TOXHpPEjjccSvuw89FLWzdfWrvXQBOgD3DBrp3eWfVwbJWMBuGSq2bFVsw7Y62BxXfRBsqxp3X7VwHoC7jSPsK_jtO0AhERjaH45wa8bt2GVkBIpkOK-WW6EdrTWM_HLq-2SmN_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار بهترین بازیکنای این فصل پنج لیگ معتبر اروپایی در این فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91091" target="_blank">📅 23:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RseNkKUOokYBKeCpa__qDPVE5h9O-XLMRZlcbDE1jXAWRgC0O-MpcKFyuEKrd3aXjpqjYbKG6IgIDrQvqEVEcPISFbajVkuhevKZ0R24FZM_ZwdyqmINbYpjyQxNZn2Qfb8eK6Ecv8HYu-dL65ZV2fIOkcwUtcrDoIG7H5MCnxOsV15HpSan7Py_HcDWPv_vyKuMhyijWAngNoQw84Z_xYBcQwUHy96zAXpLJ2HgPJVtZxE3Z2-6tFx5io_UKSdKEbFL0sYhKoy9H1kL4i3DmrgLtIVWNT5lRc5fOycTgrMzfTXVdc8pTWaDWI_RAO5EhZgNkJOdxjDOv5HL4thuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91090" target="_blank">📅 23:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎙
تاجرنیا:
آمادگی هر تصمیمی در خصوص لیگ برتر را داریم اما اینکه لیگ را نیمه کاره بگذاریم و قهرمان مشخص نشود این خلاف عدالت است!
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91089" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده:
امیدوارم فدراسیون پاداش بهتری از دوره قبلی (حواله ۱۰۰ میلیاردی ماشین) برامون درنظر گرفته باشه. ما همین حالا هم کار بزرگی انجام داده‌ایم
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91088" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=v44TNn4SIft4LLwu2UGNnR9p4_dO-HMrkDdqBEgJ6MYeRpCEkZEjDzH-nGBi55lFokPEtyHjRcOs8T72xyg5jDzew7t_G51DRZbYfKdibTy1onWHHN9SJSrqQ_of0MnzuQxwnLOSvNwVBaWUwdV95cMaZj1nMqa_Dkg2vrArfUyQIF0Csk4FgPX0ZKF3pjZs0cYR9KbtZ54Id4U4V6qshaE0FybH0dkyQj5q0bafgLNadHghP6L-HxY2AcUyN-EeyNpc1vM6rwapUoDWCYIEmOernaplT0RogT1VhuUTb3_HQAX_4OZ1e-M2SUIqHmsyD8aNmfbbUeRhC1beEbboVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=v44TNn4SIft4LLwu2UGNnR9p4_dO-HMrkDdqBEgJ6MYeRpCEkZEjDzH-nGBi55lFokPEtyHjRcOs8T72xyg5jDzew7t_G51DRZbYfKdibTy1onWHHN9SJSrqQ_of0MnzuQxwnLOSvNwVBaWUwdV95cMaZj1nMqa_Dkg2vrArfUyQIF0Csk4FgPX0ZKF3pjZs0cYR9KbtZ54Id4U4V6qshaE0FybH0dkyQj5q0bafgLNadHghP6L-HxY2AcUyN-EeyNpc1vM6rwapUoDWCYIEmOernaplT0RogT1VhuUTb3_HQAX_4OZ1e-M2SUIqHmsyD8aNmfbbUeRhC1beEbboVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی در تهران بعد از جنگ خرداد 405:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/91086" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0GhPN1QfykfCTjOv5cvwbmGRnqFkzrNv0BN-21iupHeH_fi_aw4jT2WlaEKFyZyOAwa-v5tsD3Pac5JgqMsC79ZQ3lNzkaCIY8p41lAva4Hp9_pInDc43Zn3zRrWOqWTXXYas6t2N9kvesMs4ItEbi5Y3ApvVx-s-to8Joeu0A44dQXzHwNExc3TERbyp3GzBYpzfdZ5ZEpZUdiMc21cPkGG91_1t26nZJlDH6LQI-jGZtoA_K5_AVgOUYKDH967gKTmSxeJhlYTzoqsTu-gcdrLIu4baRdVKYDKa_dkNUu6hSmbOisVPAzj9lNSxPXTrvvh2TFFK5UQevA--V5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/91085" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91084" target="_blank">📅 23:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGBtkdv-VlQLCqo42BKCARb4vKt-4gzJ-_GgGbaWCm2Y4UTUkhYkZ6CuFYGwWc2T7XYAV1X_jupDLdm8F-vUrsKbUoOYzb-e1-KcERMfr-6LfySkmHezZD6eV6pOfzcHuGMZLDygcINp_4DfASkzatpqHYshzsxv5H5IjH9jv9wBGwPyNZlsEI-8da9_k-mRBY_wYmBhjU3YLRd9lQAo-TcnYPMa4V_QHm8vRN4sgiFrsspipXsnOWHhSsBPTeMs6RkqF6MxpvCK7bDEouFjIdUn_j42o4EeKELuQYh6d9fyLd6OnBUQw2Pc8nRMOpmUEXwe2s3YpsZpKbYQVeRQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب بازیکنایی که اصلیت فرانسوی دارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91083" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXkcOYWyxruSD1FN7e5gUgJmWJ7157nc-UbIz5z9SOdkGb014_zyWvfoNMyjoXWuv25_KzTptaXS8BuH0jYszcgjqgtSM7ipUx1Yckf0AnRnWmG_Pg6NkKN4mEtpl8YS9q_5jT3Sc26KNNasSrYjf5sR1F-sqclHmU_kFUXzc3JLayBoVSA5Ixi-8zwe8kIxNZ50-yVJrFxIRq9UXpD6jy6T0NEgB-esbh-OQeXnHpBVCpghBPjpi6HTZ9QIE57RUdh7V0M5LVDX5uRWkaozvmnhgP_ZuqVfwpVZC2qee-X70laGYgw-dUwK0NPGblB-feZphF1EPsn2nJy1Y3o2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه تماشاگران فینال چمپیونزلیگ 2026 با یه بازی رندوم از ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91082" target="_blank">📅 22:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl--wib8AjvjuDcU9icFicK1WiYcmpLYgicG2UiRlQn4hY3G0rWXAh_-FUsxBQ0tqm2IM8NzCNPORH7MiZ-aJ_ZgAlWgUrLv98trY4EM8bgrbvF8V0kk3xsA7tXejakPyGwuifAcW0TouMB_5uz1jhT12zgXJ4c0wWB0b-oqBWak8W0Ahq6JAy4uYuzxPYNxZM1KiO207BtQUs78kcy2gEUF1udrMxXak7XDo8d5VV8_HIupsFvFmJD3HRAbo4x6bDfqxfX4kcpqJ6XFh_AxGn0R3lzaYGTFoxhsvHYyHIorwEBX3uYMI2sQEk4ZaMlGof7Fg0lPoXGkeQxBxCPVzw.jpg" alt="photo" loading="lazy"/></div>
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
برزیل در ۱۰ دیدار اخیر خود، شش برد و یک تساوی کسب کرده و در سه بازی شکست خورده است.
✅
مصر در ۱۰ دیدار اخیر خود، پنج برد و چهار تساوی کسب کرده و در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر برزیل  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر مصر  ۱.۹ گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۱.۵ - ضریب : ۱.۱۹
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91081" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atafS-6OftJ7DqG_z8ZRdzpqIskR-G3gwCCLP33JSqXV2F85DmO0WOszvMWoaloT_p_xEkiiqzid_aVUcCgV74deNTm_8Obtns7n71JFT870vpfRWKPYCmggt8jx9ANbdvhEcIloBN0kC3Mz-IfeeyFbSXpYiMfGODD7ma4J0F5CrdYD_ehR7JA9somWfH4P73_hunXu0Wt4jzGs6DFcHVpmA4V7VZGJ-QQdn6e0piHZDyjAyq4DPRajSpdKa5tMV4MSBapP17_s7_bggsy9nSxJxz6jKOduH4uhgRSt1lC_auFO1utafP-CGXx0Cy-b9x9SQ4sOJYfOB1ffcWkr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی: اصلا منطقی نیست که بگویم من اینجا رئیس هستم و دستور می‌دهم چون همیشه درباره تمام تصمیماتی که می‌گیرم با مسی صحبت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91080" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3J3NMcq43ShpfjvzvJtmbDtOAkb1QbFj-FM1GgEnz5uAMw1yhKvaohAG9dbbh4XuAzer3iREJ66IdJjWd7QuSqLZfi1SCmJiMr_eudw9yITn2beiqE-EREivkzKwcmAULg6J_B9UxqthPf85RUewwYEs4E-43wJuyMSd3rtNFPfSSqsxMHoc9JDT6LwiN5w1yn_OE4Bvp6Z0PzIxmOfsg5UGMueJxBKqu46rfOGzDiFTiAoa0wCN0abv9U1XQGBnofSTyYTOndk2t0VzlGOUMPf4SFLBjIjrXHJ-JBPGAISCB79EqCg5cdd4AyG9RQiOnREWOErC9TnN6yuku0G_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فعال در جام جهانی پیش‌رو:
◉ 13 گل — لیونل مسی
◉ 12 گل — کیلیان امباپه
◉ 8 گل — هری کین
◉ 8 گل — نیمار
◉ 8 گل — کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91079" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=S_eUup-pETWC7TTf--MkpbFOSD7oG9YBhqNuEAt2miQlqS0BIXCMog111dRpkT0Z5wdFeCRRZS-dmk645-C4br4lFYPDjf8gLjLbJjLKMtqzoSQ5IC35SHJDLDoCWgvPqE7pc42TZHmaUZvG5EcPSa3Mcw4G9TzBuWOCmCVz3OZCav-4Cz9OrikEpJkbHGQ-Nw2m8ZvR5UOolR7CLgAnMo3ODrsBPnXy9blxM3B3p64lzCzVfrd73hSHzYPeHfDd8Ycr9Q0GDUIsiVjhtdvYYmiul2m9vO7pJwjja8qxlkNTn3ix2yCvVlmKYo1urT--OVF5Ci2pT8tWjl5KDww_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=S_eUup-pETWC7TTf--MkpbFOSD7oG9YBhqNuEAt2miQlqS0BIXCMog111dRpkT0Z5wdFeCRRZS-dmk645-C4br4lFYPDjf8gLjLbJjLKMtqzoSQ5IC35SHJDLDoCWgvPqE7pc42TZHmaUZvG5EcPSa3Mcw4G9TzBuWOCmCVz3OZCav-4Cz9OrikEpJkbHGQ-Nw2m8ZvR5UOolR7CLgAnMo3ODrsBPnXy9blxM3B3p64lzCzVfrd73hSHzYPeHfDd8Ycr9Q0GDUIsiVjhtdvYYmiul2m9vO7pJwjja8qxlkNTn3ix2yCvVlmKYo1urT--OVF5Ci2pT8tWjl5KDww_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91078" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
رویترز : ویزای آمریکا برای ملی پوشان فوتبال ایران صادر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91077" target="_blank">📅 21:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAnqvstqGnKeYc53KoicbYJy7DQbml-SjAlXaVpejjszEjPkkFsqqpKo6yrHDECyPCZKHX9k61MOZnkBs7CaMWquSU_d8iOiL5n6mB1YXUE7GqXpxygf63_SpTOfnNXhT0c6mP48wiV6sql0-fbp52SX6qu1p88OwkQT2D9IbVOb2vRpC5Nc19lEXunjDitqOR-XaAtw7vT9C3imoyliimkSefFrAAFA2_3UHfs07M-SBesSDIuy19DpUQKb50wvP3LnWmgYn5hVvnuW_BXNg37tXV0UW080fBCF9oUkYPgtNfl0fDGFcPB8S6fgtJugDY558RoBeF1dTB56j965Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک جام جهانی هستیم و این پرامپت جذاب مخصوص کساییه که میخوان همچین عکسایی با کیت تیم مورد علاقشون داشته باشن..
Ultra-realistic TV broadcast screenshot, identity preserved exactlyfrom reference image. Young woman sitting in the crowd ata(اسم تیم) home soccer match, filmed by a live broadcast camera.She is seated in stadium chairs, leaned back, looking off to the side with a surprised caught-on-camera expression. She wears a (اسم تیم) home jersey with jeans, casual match-day styling, relaxed pose one arm resting on the chair. The jersey should look like a normal full jersey, not a crop top, not rolled up, not tied. Around her are other fans in stadium seats, blurred. Keep the crowd mixed and natural. Add a scoreboard graphic in the top corner subtle broadcast compression, digital noise, bright stadium lighting, and imperfect live-TV framing Telephoto sports camera look, authentic televised soccer crowd shot, natural skin texture, no smoothing.4K.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91076" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
انریکه ریکلمه: بند فسخ قرارداد ارلینگ هالند کمتر از 180 میلیون یورو است ، اگر به عنوان رئیس رئال انتخاب شوم او به رئال مادرید خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91075" target="_blank">📅 20:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=k52TlIJX9XUfbNWa_QMvpuknc3Q07JqBq3mIy-JPRS7EP9MbV2NmheyADAeRxeOM3SbXvVOdp1mwGZB78PhHL_WSTnwYUAZJRcl2OcHRuSzKGV4aWK3p5SrrRGcf4Xsxh2ny1STwvMvF3CHxQBoZmZl_xs-IPvmZN9zh9QjKkWsau17_T3P3vBXE_PWpy0xBvIaHioDremmnrC7w5mBu_eRxv6mlTDldyFg6CdDmeXinLcTXuF_zVQdxgOmTOhIZ40qPp0AoytCJj4VxsYhT5zcjP4jGT79q8EIw4HlGlLSEmn3U4AU5jjr-Zqh99PYDQMI0oESu4VuZm9-AFhB1DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=k52TlIJX9XUfbNWa_QMvpuknc3Q07JqBq3mIy-JPRS7EP9MbV2NmheyADAeRxeOM3SbXvVOdp1mwGZB78PhHL_WSTnwYUAZJRcl2OcHRuSzKGV4aWK3p5SrrRGcf4Xsxh2ny1STwvMvF3CHxQBoZmZl_xs-IPvmZN9zh9QjKkWsau17_T3P3vBXE_PWpy0xBvIaHioDremmnrC7w5mBu_eRxv6mlTDldyFg6CdDmeXinLcTXuF_zVQdxgOmTOhIZ40qPp0AoytCJj4VxsYhT5zcjP4jGT79q8EIw4HlGlLSEmn3U4AU5jjr-Zqh99PYDQMI0oESu4VuZm9-AFhB1DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
وضعیتم اگه یه سال دیگه ایران بمونم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91074" target="_blank">📅 20:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azCjXNYNXFJZQ9G2vNAjvTawlvmjkdLeZCCK8t3N0qFnf4Z-f9mI6c_53lhMuXaddR3JXSw0gjdKGqTsAQDXfrHjsM1Yzccr06JOaIzaLDYO1c_N884gK_QVuG1kg_14MTo_TAFaE1C77SHEj6pIhY3BKd5_9UoJcUUhIRl9LTJ2ESXQds5OvDPhY-M6PKjE4xkjBLVcLc8WJxoLPOf7hh_NXU3v2ixNobsn_276uVLDM1WAOjs4Q6vPkQtgtMMlWoVvrTasLJHlEL-WNMQl_ICAeseEb3bZ9XW10Qa13xR0Dij0xN3HF5kePAPyyo15PJdxzKJ8AcCdmc3jBSrgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNKUYynMF0C7swtmNo-tsGu38Ww7HID47W-sPvVu75f2nNfedjoFJw3QjlMAphOuyZni-ENvAN4qQN71LbBilwp_CCNPWAwqSckExl1POP5qaSS7kbV1VU1u1GB6hwGVsXWmpb2OhxluSRHom2qWK2-8VkYrj09zJkSDVTLgaCzNTLWw8FWfik8iiA63rYfpiKNlUQZlHavhzjW13pjrpUwzD1MZ9QYXQ9XNtPrCHozE05HGUJtT_08VjfDywB7yRpKqbUuBqL7sRHZPA7CcNbsow2QbjNQGKNcLJngDGon96B-QeCWA2oCqsD6Wula5Qgn8DdlxBD1XJLM25XgM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4cmnM1AcIGYpMzRXWqswSlOKQE1b5JuWi3izFTl7UrrDkCKJnB-48T2t226aISBpTIrFTtb3RK-VOQTLS3zxnTZhpNjkdSCw0-DZ_M2xrXcvF6GvkmraYlUfknDZb6zuHfGisQ7EiWcWAAm3VqCJUkuzhuQGSAXYSd7iC4nXYVzBvvcxEz4OwTguB7y2cImL8Gh2tDPxAiRwlTFro7bVtR3M3_4-FPQVIx9UREg7rRiGVfoAqFWk5wju8mfWRoJbQlw9A01dhxmLVN9SrMvReKpXN_RGhd5TjyI2aOGRAyymJpjkUxr_ujPwjm3izVXw23T4_bPwBrsenS8cci2WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwK2VshNHhlTTcz-JPdQ2P7GFFL5sz8U8t-cxuYY5N0cQg2az_AOqkVkze0-0AeUG_2BpgCdVl4oDjtm23MyD4uPU12HrvoBjYRGToRqWZkrYN__nlpiFyS5zwwbiEnnAICZkOe0kv9M8AkvhHORMUlgYviIeA3cqn9EkHNFPpDew2XqxYxK_L53oE90LUYcZhuD7s_bB9ogDOS4LXO5JlSjG-vrQoWYK2nCKSa_v6wM6gOqG6y0b-kbLcrOxdMj8PFijNJdgx-fwZ-hY97zQlyQCheG7bHJbIdkr_9sy4jDLyA-XlzuQvNWbd04wS9CoiAQS1AyaR3z0zISBRSryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXRFjJatW8fq-A9QLKoh1tRs0-LEryA4W-TorPpw8H-rm8Nco1dDaQKuAChwm1_o_dA66Uny7fTkHMk9b12wGdyn-g8XHz95KsQtlYCbr4uGeIgNKq_c4AXBssKkOjD2qAnLXnPIYC1buL9Ic8cB9AT8h-NZH1RBEeuSgIxDQQ1DQ9fpZ58QXu39n2bUxHfyl4iIqa7aNTJRcHt2fby_jF4xtWq_akAjn8_fDDDNmb1KIlInux7dPna4LnpNmE9yfa7oyrJI7i9rpxnFSTVYOmTAWvkF2fRMiFKQ_8WzSZUu7xeMMWH7dzLZGhG774kUToDml_0s_-trqXSYynO-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqUcCu5dfT2ZH_ai9y_X3A03hi2tK0GzH4JgV-omqr6xyvHaRr1N2yFE5k1hUdlgNOmxqZQuvn1AhKc3_k0GQqRrWhY45Hq6oQyyeR8ar0omG4c3op6SIwb819QqJYdBaSZRcA9jZL1pHEX6Sz0DKmdr_nFrkqEKR-VVYfVFBQv83XffBipMyKAt8hFIjxu84_ZbWhuRjAD9w2IXUeA0n_IS1oTB8uRRaQVyyruh_CuQ42Im2VwU2xHkymHNj1SpkyQfvmeGHrAJilZz-z0Z1D9wUVMdLlRwODmze2yx9QKuifPj6aRc7v6VAH17jXkYI_45ZZgFX3XEa4DLbc1q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzeNLiY8l1m1WOw9akbaOrIsdpa8uwWPLxCwbyr23X8CXhPORGQ00ZDfUxE2NSHeCeKCeVyi74zhQqeq8bz5qGv-YeO9LzOFzphCUSlJzEPcYbETYP0cm0ryoUVHD-EFxLHEEKasCvv6KpefvTEuTGl45nPRxIsiKCqND-jNKz5DEoi8HcWj2hYkMLwbEg0lN69dt0ObBf3ZQr9ttE-IqGEUhwX2UUvs9X7ezZaLLQXKOrW7WHQxjyF8flI-AKgQ6nbKhPlEC78POLgmWyxbixrhCoCvAGZEiJtLIX6YeVU4PsDFzJL0QdUUWlW6VBYFWCrohvcgDh5yyN4smrNZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Se_tDUa4P9ZQwxVv3mQ0vqVBZaFcP4NRatMOL9cV-Ai-dpdgmPSr0dTgU2hEszXy7wMaMk0hB1ALVlJqNXmOcww79fu1e9zsb_erD6GLg_wXk-D2TkZ2Mmq78aSUHW2ikoSyiZPfWYxVTbPS0-T1Q4iCWoTHchjSsn8uE7gHkALrhNAAGk4YjomaniZwwUoqvDWQiefg8TGGfozBM1yWe37_UoDeNaWZsQt0RqXTZIq-4TVjoQ4K849R-52jIyLjHGbj4dBpsT4V8vR1F3H-pTTPzO5CGjmOlH78n5xJHwFFAFgdupVeKlH6i8An893ncKtXZI-D3yJneKKHucdrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_WA_GoDUVgHMPvrAI9quxItxLZ4e4RpdYMX-7Acqf2qwF-Vq59ksq-UX7Yx-z4pbba21LIHJMWGAa_EVLLwtobZJIKtAcnxrspCnU0OhXYRJ3MRfK91P9KUsj7op4ASnQlhYHVeEXhSXAZSsxUx7CjVJztfDtumuGSlQE8iJcSjiw2CHT9O-Pq5NaVZ2W2B7ygFdEgMtAr3wBlq9Xy04j64Einn3zEP7MzeMg6700gUSucPkjEW3o0-NSHU1wu1RlHUgFfrHewrRiWmRzNWs2k1YuByaIi8tieWwS4opuQH2-oFno8zxdXkOIyEPCW7erakYKFWg2ulNHk1Qobjmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwH5pWThk55QoPXgb5ivw4U7Nmrz_VzOutcQ7h-669dxLDaXCarLuamXcf8vPOrq8a9-O30HHi5TzXx8sdXP6M91gZiyY8cVpkN0BsrbhdVmYMQ6wMBTzfQzohCO7gcYCJ21yZJgK21gKWZtcTVnRIcTFBU_5wTphD8WrkY3fgr7mHvw_7DiAotEhWkVf8GosAW57nuYQxEwt134ZCEdFkQ-Obr4dVv61gjXZJJNiAZc2z4gMCA8nkjl_B36cqsvJ-65emGFfqlfB7YNxvx5rJm8ZA432D3014-9RgXHdahz7POzKqtuTUxG_3zpZshmu5mCGv_hWBUkX3IOQvY4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJnABbFU_i4u2AJGITL35klG8NdNBIBB9ZKjSGhzCAvssZrV7qcKasthZ4Vse0ydOxAUOfnitAlxilcLDFLmJGxsr-aQ1bWlyhgL1_jCpHgjvo-fCtXBMzDrI3PTyC_UN1Jiu-Xct4TjxKPOxvU_LYH1NfG0zUkJK7z-3KgNfXQkPiGEoOcVazoQ7TsYCJBhsHsEZSyFl4HBkfbC7Uo8Zm1Q4hp71KKwuwtqux4Js05n6gabxNKVWv9WgviTwl2crFSqtM7Xq33L-8DlGsL9M_tBq0LydPLUXRtC5KicMTmzep8MNL4TFE0KeQp6qJG7JbmWveJoBDhI4mT9qyAfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/btLWclXFm7IXEI4W54Z3EYnmgdwkzYlGy1-rgyVEkMcVaxElSSHIBXTg9oSAo5bQjYUt2O3KrbM5jCmv5jqRxsWuVWQkosf8fruxKJ5mQocWRZa_2EmwPRqbqDBv4mjt8z2fHEcZTl5UE3K8q9AXvV70lflEL13_mpe0wyYU85ZO07hjAOJo5O7sLRABx5qeclTKMHSStYbnu2bp96ZoEOkfMBcG6p3YSkzQAPn0kEadTqGIvIaYRMkdfsGjgGeJ7YDgvIwhq1KM5uxoDexoLaXSEUUp3U64rcugbhF9OxpPQmWEZzUn2cB7roubLg6IOs1YwiCVRZe8hb7RFvDGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phXbZQC5nj8fnw49jBdkQ5Y3A9Dzi7fNdLL2Q__HpUes9WDqjcE_t3wPuTo_sl76H-JWKIopcQHqIYGS9eC2WZU1DChwa6jCIOYZnX5ImHaIhgA6Ij_9GBR5MSt6frKuvqHBaJKCdhDS_dA3Pxn6ud_Fp7IBHJZ23tCvpLKJHuvxY56M4cUbcze72jH0E7dAbIR_CPGArGyfJ_kUNTBGt5f0ykun6-PYVMK9FiT6mCqHNmJ7Q3hh2jswEa8M_sb4BzF9yRo0fdAeH07ayyYzMREgENvQHyn079SYhpz6p3_xiciKjml4xwjMOBQrUyXx_qFX_AUo10BtLVmxWByXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4Eh4ndGL1csi3NyYVFNFjTNmnwY47cWHJIRo3O0kJo96iuAteeH5mLYrtzNZywl5HpiA-aodGJ8La0Si65O8USh2BqdXGbz0FAa7yu7RxiDERAvSm287d4r0RWZJHT8IuzvIfW-hrjM9OEG0ePziDUzVtfF6UdjU9aCRlfh3QGhae9WYvIefoojGmvJCPJGondebhEb7wjeX1rvFHD5O0dse-5Qcc3Utd7FQXSYbx9EGUdvNFyhQJv-9f-2yWnjgvAImdKHSIhZA1CWFD6L2q4P4D4I8ymEe3AK1McN3SXX2OuWFebdyCeJJzf5mEuS5mNJ_jCweKeoTus7mI_W3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=ltuHR56FsPwxXywEiM9c8-SQvMV0GUexV3nS4JvR_696Qml_6wfAxZVnZh2EbdxBD-pKdDhx1vXksJX-shiF621A5X1kouFErQkFGCfB4GaYcqn3E_0m24UksRN8TcijYR9ULZK7bCUkMguSyTHD4o_8x3WuWRukWIzcN1DMicuXE_5YF1KSi-FurkviklbkMInDHuA8jDZI4eL7cN_qR-TB2qPwV-grAwFsrvz8-t4UczjEmLZjF41UO4uWkavcERvyNv1TINKW9CWE6czOs9gdEFfLvozfYGQbsI_lD9mFxSvJ3NHxWQGZU4agUao9vmk6gjemPXxktAPEygOLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=ltuHR56FsPwxXywEiM9c8-SQvMV0GUexV3nS4JvR_696Qml_6wfAxZVnZh2EbdxBD-pKdDhx1vXksJX-shiF621A5X1kouFErQkFGCfB4GaYcqn3E_0m24UksRN8TcijYR9ULZK7bCUkMguSyTHD4o_8x3WuWRukWIzcN1DMicuXE_5YF1KSi-FurkviklbkMInDHuA8jDZI4eL7cN_qR-TB2qPwV-grAwFsrvz8-t4UczjEmLZjF41UO4uWkavcERvyNv1TINKW9CWE6czOs9gdEFfLvozfYGQbsI_lD9mFxSvJ3NHxWQGZU4agUao9vmk6gjemPXxktAPEygOLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIcllzbRjDVoTR3ehCOM3ThNTRcRoB1Z8ZdrZa9xXtD4aeqUub8-_efQjY2gdYAPTVpBrYMfQ4M3sCIOE9mVypPYID2euppnK-AEQX4vvB06zTUee7JPkETReMN06ezKZOek1Yh1Wn-uAFKLiYwWQhtAbCoPUY9rd7lXNe1oAKP5Hc83JXdx6E-Gy79qG9eGKSCYhyjmOE2XIVW9F0K2IoEAa1kYL5Nf_qV5f9F_UGMhe5sSJGf4GSJ0PHtbCxYL_IeJ2isHwZ-96kAzyK6-70XSimzgSN5Lg9AiFeq5Vs7vw_7XjcYdvq47ngrueypt4Iw5rXL-pXeeKhrLDc0VIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE4pUY6UwSLThIfSo8qbv9qiaN7MjBUDrhR2klHh8ZI900ObQBAryE-LsTL4JHRjyVJlBry9rT-agtLDQjYYvtCdzGzBD21zXwi08P2okx43FfD4UnrVUWzjg6X8fYdZidJb9lNEe6iXE9o6JPc5AoNh-USoHIhcPqb4opUGQB_HZ-XUPiQZJM5h8NXdZ5vM-pUZnk9p0Pyxhvr6G9mR2s1-9Nd7tTR0vKIoBepMIAv8F8InlVoUtWkGY7G68fjT-s1nlNYTvk3QQDL35-DrsoZ4K51JJHyIeLWgYngD5TsEnk_ReKbE29rXoe43Nox8_hsTWiB6RQEx8UB79EAW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=RZQYJ-vKzVikX2GPC57EMDtN0ELul0Bs-8SvHaqFHbjj8KzmW3THDM6XIa7_UeN9N5qPI31P8HgxZrMPeqGRTW4itF0zUZtw8uZEqKKzGBvRPJvoBFLkn9WO3JpM4VVmh1PnhxVm__M0mB2Z12il8DGWozEeDZF45_PQy8z_U7WG0u_mGINiKQjBNcBIUS-ZzCoiZaY61Fo6jCoYDgnX66TY2UFtvbnG4xTxPe__F_DcWiKH20YBXaNwG_HMs__NoB8knopPLx1TZ7LG4dU0f1dopoCWWmdD_5DRhy4k-6VzznKSuOGs6nfOxRpW3K4AVZolwdbKhtF8s1BHp4CpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=RZQYJ-vKzVikX2GPC57EMDtN0ELul0Bs-8SvHaqFHbjj8KzmW3THDM6XIa7_UeN9N5qPI31P8HgxZrMPeqGRTW4itF0zUZtw8uZEqKKzGBvRPJvoBFLkn9WO3JpM4VVmh1PnhxVm__M0mB2Z12il8DGWozEeDZF45_PQy8z_U7WG0u_mGINiKQjBNcBIUS-ZzCoiZaY61Fo6jCoYDgnX66TY2UFtvbnG4xTxPe__F_DcWiKH20YBXaNwG_HMs__NoB8knopPLx1TZ7LG4dU0f1dopoCWWmdD_5DRhy4k-6VzznKSuOGs6nfOxRpW3K4AVZolwdbKhtF8s1BHp4CpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8C0nrR0RR3jQxO5x_8e0eZ4uGIlC6c8OX6uudbvn83U8hO5__DgZC2yJk6Za2OmALm3DvvH_RhcsSHbtPqHI2y6JkbM3Rt4OJ6KYcwNZY_tYFFO1EdyjYxA4iZeus7MW6t9uHwEKJOb2_M9Up-Ys3IL-eGXQv4P02s4gaeiQS5jNLSZFdLdTZe_HYslWR_lCeoSq8zC6gWDH1CQOjfb12lrKsepcAW2NCPv0i0XMPgKuPNdXiICY9woGp4e3OCLDDnj9iUjxQZ0_gYUoq2AIIG37fqG5nDSotYcK3gu9QurCeOHT4aVr0Wyi6a76oAQhFiss0mnrM4onMkUDxanJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=Ru6GSsFUqDPVqUzLOT_FrSo7U0jJmv_ZptMby_p1HWxGcH09ZWewsPnPn-3a7DqM8l0uNxZv6Y5BHxWpyuwOs9J2ALBu3gb7L0a7kjanFg7MbfwWDHZJCnePYuXu41LtFsnqXNlMRq0JKJWyQQ1YS3PkT8wEHjmeJ-ZolIO5z4qTSFZpbVWVGtzqUiw4pEhXIbESRkEOrJiHUz9HIbGlkP7ZWDpl118WDZil7umLRJ_xigBrYPe4A6MYVuj1J8e8k-6LJoYPtHnplrzOGMOvNF6glkuDfeqTpxWGrX0UE94YRVauW3ADLe8KJLCG0XT5b4zhwnmCnoG5I3P1Zyw2gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=Ru6GSsFUqDPVqUzLOT_FrSo7U0jJmv_ZptMby_p1HWxGcH09ZWewsPnPn-3a7DqM8l0uNxZv6Y5BHxWpyuwOs9J2ALBu3gb7L0a7kjanFg7MbfwWDHZJCnePYuXu41LtFsnqXNlMRq0JKJWyQQ1YS3PkT8wEHjmeJ-ZolIO5z4qTSFZpbVWVGtzqUiw4pEhXIbESRkEOrJiHUz9HIbGlkP7ZWDpl118WDZil7umLRJ_xigBrYPe4A6MYVuj1J8e8k-6LJoYPtHnplrzOGMOvNF6glkuDfeqTpxWGrX0UE94YRVauW3ADLe8KJLCG0XT5b4zhwnmCnoG5I3P1Zyw2gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzvErL85VesLydUG7gc8FuRqNgxFHeSDP8_C39w4oeA0Pa-YbiptUQE41-FXSbhdbMAErBNUBggS4EGb4LAF56UQV2q2vNeQy3DuaKxjgIXT9VCOJmbb0VM8bm43DzFaKf_wo2VRSSon8ySHNSCbGnmKon94OzugGQ8JtziTi1aQz12pEEAsaflKELDEH0uMW02EaqB8KFRNxVbLoDbZ4J_QXBZtOw5luOqFDspRrcqsg0wPg6uCKd2r4C5KPHJGS8mdczwIJ5x0AhJplkHWphZbj9-XTvcITABZNS5bSBqQ8tAEsWuwXNINFxiW3Iz4XIKz8sR7HU_Rx_RUi6etJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIVFcEvtpJtyDsNvh4gfSvXS8y67yeQOqfcjuG54bHV8ZQO9wRKJXBfpg1VcwleoGI5IbE1B0NsheRJtFnksKpOF4uUkQNHxnjV9i73dhW8fshzl7wKIC4YW5-EERq8cPoVizX7euiXa5OGlKQsmfjwM7X4nOFKZFl4h2k6NjaPJl_-W8Xp0smmg_kd9T4pTAgCFhkkQNes7uRkv_Vp_u4M-17KrRwO1vZZsJv6RAING_2UJDEIS9a3iijRLX-jCR2mPiEBl1CxrIt2pgmMw3mpljYvjaBi6qQS0uRuydVE1FJySZNYU94kYmHSUZzt_OamYAiFzK8NMAeBcoBmRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6BvfMh4-5yAAZpUj5cmr6JJQAf6kwKN0xCFDWIMsC6d-SsBox91tqrk_VwlKNe7GYXPjBszjhI-dei2N5cnFDAAwumiKs5KrQKV1_jfGzTGOvJvhlcZacQ_GAj1TTmhl__K7KNhqx-NcCZtdxLikv8P8wYRDiCEbacy3dj-hWAVXIyfGbIhYGrYivkndWOvloclIepMXzLewBGUtUNi-VvlscJY1F3_Yrly1G6-Chf46fe2zOBQjGBTDwhmKzln6l1h-ei_Ft-6u9_iwQtpUcGYyCTMuVDlDzaUQBMZNykhmQd2h27I2SxGmgtAfnYt9UYICaC_xmerXckfCqALAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaFpGqWe-84OPZhFrj0lBUurWYkXWAMdd1POrl7bm2ftYbZ9QbFjUJChwec7MGcY_K2h318VnLpQRGADp_Qx6Hf-toxDve2fCQ0h12jsNRTWFQZV-PdUcaMgpW_o9H7Bgs3PVPlfXUkYV_-zCMSAgZ92pAmHHilpVZkFSDyAcbrnPELfYy9413vyXtiCpb5JCoBKqp7OGAWzK0bK5If5kxXMt8X29SBERV5mVjFNsG61uX_XGoWlzjsnC7lH2yjWVV7Zoa1ni8wd9mfa-qGsmyaEFgc47mimDCkp_3gZ1nFCRWCe_dg2auUtcXUStrNgUSLd3lLzx0Zd4f3ewWFh9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
