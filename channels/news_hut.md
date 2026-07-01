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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBczA6zwqKoD-SIOPC3Ukw5SpYf16Dp1K2wcb_LJUEprG1F7PJTE9IfGP82udCaVc09RBlhKCuEhGIXFwllEc3kFWh2TGahirV5-iU_uve5V7loRf13V_7ImUyZhjK39oTGfZW15t3hH6wNzNPf_hKUBTOC_k3FhLNS69pdcbK7TlSd8-jmBtZ1bcEDOltdCByyTmc6Cl-0-wHc-FeVWCcTvsruWCYKKBjjAWqG_uY0st9mxuq8EmrywMfYEUw3rNc4tIXs8Pw--6UsegRKsGHuCvzMC9jR9Omolaov4e3vgRazPtvVugc8hSiCLiL6n_QMqnMXL4sMlGypa9P2JfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m790PfDEyPG7z95UebgSPYDB4mMWtOjzoBxO4_FAEH_w15e0zPhRUSErK0unqq9JpwGaq6x9rLfMnPxWBufRstWmPzlrg7RR_TllXCsPADrVxXD8_J6y6u3N0drA3ybZdYlGpKjDinRpaJHlEF-M3RkMxVqgBKCTR2ng2WkeAm5q0HYMxAw5GHBdRiuBg7NMqUNZl7c4n035QTyQvhJxuQjNjw52xDex56r_21DFUhWPzUzNISAjxANB7EcYWWoQYbvgkoXdhJUU9CjwBpnl852tCUlIoImwXIsDlw3O8iFXKRJjOd0iomOo8uGjrZ1Nx5ouaHhcq5dJxPCQ4MxxMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvIfb01H-0LAeb_oAfAGusg3T2cDUjVu7qqVuFf-MpA7WckJvU-s1Vd3YlKaQ_aW32010Yms-X7jTHOzDho6YyxY5Ip5ef8dnAHFZqv_moJfhT-nACbUXUsiTd827hxsEy0p_HhRCdcwwzxKGeaXQwy2kmQmqetAiJI1eHIbSvpQGilwabO61_JHrgDlUydR2XAVMefe8woeVKMmIKAEgLVhUuhAdW3DygAbj8WQC00aZL0yBstSPqW7I-YtUvCLmvMvHubKqv2q3BQVQrc7GDOrGWhgbPM1bHm5cJj4z1CoSAs-kQT6ZZ2BnWsAmVl8jIZ2RZmapzbWtUK30fttDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBneLo0u2_UOGTmOUffr4Gs8sG6hESRiaDftGYLGCQZJDtelqNeZLjxXIW8zbdPGplANGtRQ0XFfJ9lmUvjtOtABR3Dwv6o81neOduWi7HgyrwlvuzIeW50Xhlc4zTobavks5SHJDcIsKKrvHrgmuUHzs_FY7Y9TkvnCG3nuPrkEaIJ6CZsLpiLHfg3p1TapK_3TzlBcwiBKkK7WjJWLjTG1g298dfGNG9SmQR_GVy1DRLM7iouWJUKtdzMWlWXdcSRv3WfDqz41AqOzHeF4rLOaO2EQaIqBicGbPGGH3rDfi_KigpGc0NyujrYsKH4ceSTciD3mHN2d3i8PLpHZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiKHhF0ELrnyr79vcU6I56haCbVVgKkE4ylh1S2Sf_2FzHd44SQSA6e7E-xXl3BpgRLwxAGdr-zqcFqA_6M5Mx4nGabI_-zUypaD6Mz9b7BTCRxxSjnAVl6AlPQ_llghjDLKaSkJdbAzYKtpQqPZt6U2pZC5Fx1JVo_bu_2jkoLDy4CuzjMV3GM1fR95O0ThEgDcoIMMrvNGlV8VYTMOLWpuEnYPA8prnNiQ8Q16oCwgkNTvSIGl9LwPZCNrcU9HsMQQxc3_W8JVuZPysh1O9dSUrDHh9fW4lsh5VhducsV05KNBg_xVwEWus9Si5WdD9Y0pggWJ-TYYUuo5JXfvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lV7ONs_qKNoluYCc1YrJ3fN-7NvMxgM2cBTER6_shzy4WKvqFR60BOwAdvlTGSbHvxkm_5szMZ2dbEqXrPeeiviYWddrH3EfLPybmhRjQBe7NUF7MBcYI85IN-Y8vFrCO0vP-qXy-zybU4Iau-Db8dTkfqRgDYJADepp8f7_L6062wZPAkQB83S4ouGNF_ipAkTxpsBi1fF4JK8AxE0YVygEWWzzAVz4JvQikkgFwT3YVTICMePYIVLlL6PMkcszhPVhlZ5ROhaIknmHhUAXC8S0odnIoWU16kHH0ZOxTf39YehlevlXmz8LC2xQDZBWkh1rz9YTpJ3Xq4Ef46fW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6NBDFT2yhxoGK7f83jXn8gI3ckx1I9MsZNrl6MKVVKkQBv4x8zOAtOYbAIQ-YApJgJMmBTz5EXWutPO2wtyx68t3Rrifgeh3apVQc7mu0OKuLl1_4j13D0EDClaXbiPazxRHIhLAej0ldivN9Qdy8KMIwsaSbgYeKYyUlOukAHs1yUAfJjcl1gtmcNseBppNNz3-8yFjxDcFZlCW4uh6ML8BKBXlDSasQeJrwo1UvJfPYbqvzjRjSnnbUW1gNizMifDJ0VxLl2YqAIHou5XLj4p6JHk7qY790etdwsAL53zAMdF1tEAEZNfRcmcIooKAkf1lK4FiUyyGWu60WY1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK2aQlTYUkQ_jzp1RkSUQasDL6u4pDMvuvxakwE7cyqDwKYPAbIgR013NB1epKLAUC2IsaENi2wI8cfdKVojUTNn1c-4Jyif2_lrPVLS5ZDHS-naEDVPenNHTCondPFbR-Ej9EckYh0gZHMdBpZBnJctCP-PtmMtrmq3pT_IpngrhKF78nZbAuith9xt2uUm90s3xJZsQPG_g7hZNblqH1BnRGULl_-zciYr8fM9AJZdp0NnH3Q26Fodg8s68lB1vjcyEJXdOdXWYn3ASuRPulDQv4tpvKLRRNW1QPC100btOzkxS74oB9FZNQGvbveFZ5GI7Z2FyULTqJfO_-g3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOte9Oa4iMxQ79MGqGintt9rPnh6Q47wsLREXK_wXwT-LFHIhj9AOzDZiVIltphpRoFYY6Gnt1vwf9kBMetUKy2FYnu1thQOBuGQ6qSKMMX6jotRT5m8sXpCJxFE0_3vHC1of3agoTPrB56xkMp2UJxSq45vH0LayGmL7HQGSRbELIhO4dr3nKBdcoSr02kxj1Y0kwbKzBmxvQVIgDtrpjR9FH5Uvqw9LWkqC-5M6bh1odavmOYcyFGAMnJRVYxIfVJHasmG2Aqv07eHQxHFRhPCcs_8xJ3nHZlHSdM0e2XpyD-G3WolbAS9hVmW60YMn-1NqkPkUOr3lXZ2Ibz1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQBA7Mr3Z31mcBakVf103l7fWQF_Oq0ucSy5X3c3JODKDjQsCCKxAeQHRIWfJmxwF_NcmCDg7YHqnOgWNUVNo-n5-7C2ZyVresSGiiikv9nANgxnZ9aggbjfeSMl6p2A0MOFglqu4fs4S_GsxumTMt4NfEj1K2L8b1p2bAZ8Hs98JC0pWsmdCkpSU_zUUXyFfgRrzb8jzZFU6oosHUVYUlETartcRo_7L5iGVIQag_DqiFIc0NpMdmXm7fEJAPfc6-KsBbkDvDbgz0t1v9sVmr00ulvn18opBxHo9ORe8R9yWxd7x21gHshSawVZKjCD-2ebKZpCPOYjR8YTIz9Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=nBXjtePW8hV96t3T87OhB06755vksrpGTfJyqH9bPkfKwoFIYylxbr2pF-QrnxzBdYAVzzrh8fXXzFluZ4X7n3Q_IITWZ4hL2IZXlGaRPkK_j5Jt4qlsnfhlBXq5NNmFLgfV1TgxfdRPHK2rraI2c5DdMtdIN0VmRFp_aBo7uMr6IX3mTVP4ByBHmDozRBmOjm1WNbBi_EVmQ8M8rUlv1GXe_DwLICLFO_ClULT9h9dnxVypaRzRm7Rv8dvw8z3Y-UxhsFBRlRaksqcU9QkqD4yacBlCD6kHAqCfSU3cLmUmygXfOA-CjDU8_VT_yb2CMmMh8RFigV73kcvJfkvJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=nBXjtePW8hV96t3T87OhB06755vksrpGTfJyqH9bPkfKwoFIYylxbr2pF-QrnxzBdYAVzzrh8fXXzFluZ4X7n3Q_IITWZ4hL2IZXlGaRPkK_j5Jt4qlsnfhlBXq5NNmFLgfV1TgxfdRPHK2rraI2c5DdMtdIN0VmRFp_aBo7uMr6IX3mTVP4ByBHmDozRBmOjm1WNbBi_EVmQ8M8rUlv1GXe_DwLICLFO_ClULT9h9dnxVypaRzRm7Rv8dvw8z3Y-UxhsFBRlRaksqcU9QkqD4yacBlCD6kHAqCfSU3cLmUmygXfOA-CjDU8_VT_yb2CMmMh8RFigV73kcvJfkvJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv5nTwUF1MYwPxbiYURs-n62NM85ZjBPsZMFi7qF89S97FmmRb6SDrp2am08m9pl4c63r4jleiWu2vv0FisBMRVgHc2pJsJSGjTlgDBMpqigoIiTeUBx9QOU24opHGsvbPQo5qf_vsx9wJJ9ZP9Zsk_Er-Z2CEZGM6zScw3Gx8Ip0SgriT_DRnhDxLvH1vs8cUmAlxw4e_XMcNTp3LZQyNqb2L9ulOs7OCmLBEto_9UEMr54byfHGXzkar4bf3Nk2B8pZUjgJFMb-T6pNOa1pdGfzgbUbyyXtydjlH-pL3BX5IJjnWSKtw5Oiv4kpLcVokLWWxCdjWeq_NFrq9vcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=VIGBer59fksGY9OGax4mN-cFvk5q-MbfVu86w7G8WOCT5MlYqwCYofUh33zDADjVf9L6BjYlSKvEEdfvOEmksmTZflsReVxYmurpJysUqCXBfyECgRyDluQtVcPY2lGWbfZMYsi6gknC81Zm9FJ4pIR_7e0NCZY9qXYiwVAGTwYC2dne11tUhv8sEuzmIYLEKdGI1BRJJV_ES6X3op_d0OVxn7G7Qk0t4iJHXF0TD610KqNnaE1SrUXWhzMU69PEVs6ALqJPmGlu2r70PrcfhSONYuyOzKzPLSbwj6gKp4ohKdP6pdUdLvPVdnpsznmVVCXBI3M5y9wZX1XLTaxNKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=VIGBer59fksGY9OGax4mN-cFvk5q-MbfVu86w7G8WOCT5MlYqwCYofUh33zDADjVf9L6BjYlSKvEEdfvOEmksmTZflsReVxYmurpJysUqCXBfyECgRyDluQtVcPY2lGWbfZMYsi6gknC81Zm9FJ4pIR_7e0NCZY9qXYiwVAGTwYC2dne11tUhv8sEuzmIYLEKdGI1BRJJV_ES6X3op_d0OVxn7G7Qk0t4iJHXF0TD610KqNnaE1SrUXWhzMU69PEVs6ALqJPmGlu2r70PrcfhSONYuyOzKzPLSbwj6gKp4ohKdP6pdUdLvPVdnpsznmVVCXBI3M5y9wZX1XLTaxNKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=G3nAEfVB48wsVCm_fCPO_yKK5qcU0Q3dQlDKENBG1faglSgw452EKQgp4DSjnajf6SeqheZwU0BBLBvAfzkjvo5vI-ocAOkNgrNb8iSXAN3-QsUGiF4FeeIwMFHSqyx1QxPC4fb-hvJj7t3lhycPh6hm6ab22goHtET3eZVMb0FYjb_8557mdvY8zz63SSHqvRbCEYf5casAg_mriScT4nGyIKUp9fqugQDYL_LOezIrLCFWt5Xhh3kHAXOaMKtEQMy61aDzU_h9T3ADEjHwv2wztT-k0btAMQ6sbix_3yn30dcT30IsCj-RXg4HtQVyqkWj7fMWGt8lJHH6P2QbUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=G3nAEfVB48wsVCm_fCPO_yKK5qcU0Q3dQlDKENBG1faglSgw452EKQgp4DSjnajf6SeqheZwU0BBLBvAfzkjvo5vI-ocAOkNgrNb8iSXAN3-QsUGiF4FeeIwMFHSqyx1QxPC4fb-hvJj7t3lhycPh6hm6ab22goHtET3eZVMb0FYjb_8557mdvY8zz63SSHqvRbCEYf5casAg_mriScT4nGyIKUp9fqugQDYL_LOezIrLCFWt5Xhh3kHAXOaMKtEQMy61aDzU_h9T3ADEjHwv2wztT-k0btAMQ6sbix_3yn30dcT30IsCj-RXg4HtQVyqkWj7fMWGt8lJHH6P2QbUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=pYBnt3SHXKOfCWNatC3rNzyWqOJX5uklVlrXXJrqO-5gW6rq3Qb2RtCc8QXlMHY0OafPmCVnD_LdyfWRGtPHFiW3YdGkvn1Ggw4Op0dpQyHu6mmnwuFiylRYXFkpAbZ1A2DZ1f21DhmvQ-x0s7hHXpKfJdgdhUdYm38yPx6KiVO_Mqm8X9JDIs4UQnBKpCO8lLAmy_0JWXG1XdXEYfNbqGpJv8lRZ-OOunMgoiwZwudt0NRQVz3QO4yyhN2R0tTV1fgQ5EMdKNuLYdfMuEcDtS7pi-OsfJGIfgOwYu3QN9BdfO2kIKNZ0CgQTNDRLwKt2bRmB1uCYJ2q8H9XI-sRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=pYBnt3SHXKOfCWNatC3rNzyWqOJX5uklVlrXXJrqO-5gW6rq3Qb2RtCc8QXlMHY0OafPmCVnD_LdyfWRGtPHFiW3YdGkvn1Ggw4Op0dpQyHu6mmnwuFiylRYXFkpAbZ1A2DZ1f21DhmvQ-x0s7hHXpKfJdgdhUdYm38yPx6KiVO_Mqm8X9JDIs4UQnBKpCO8lLAmy_0JWXG1XdXEYfNbqGpJv8lRZ-OOunMgoiwZwudt0NRQVz3QO4yyhN2R0tTV1fgQ5EMdKNuLYdfMuEcDtS7pi-OsfJGIfgOwYu3QN9BdfO2kIKNZ0CgQTNDRLwKt2bRmB1uCYJ2q8H9XI-sRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=X9Ak6lWAD7F8ISwSqLntORB23KQuqn2vR7GN6EIefLnMyAfTD17v9o1McdjmckfxfHk7XWOfQcHmhHz9MSZh1e3kqXXZHLYSGM8oinUVnbiRxOJHGI8cm9cdfxwYF8AE9NfSdzsIRnQD5HuIUnmviA4pgcUjEc2LHnjSVVYa1dDQlaqoJpMi-xfnaR6GNtC1ePgAtO1JEVG-NhLtfLYgIU5fqjX0Dsfi7bW9Z9gaYgARdpoWHSadMKLFuwAC9UC-70-oo1U4fGObRSA5fwMprVaZSveEv7T22gkZmAuK24DNACf58dnHqzlV84E84yv9PJqh6ytOaNc2lUsZXNpidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=X9Ak6lWAD7F8ISwSqLntORB23KQuqn2vR7GN6EIefLnMyAfTD17v9o1McdjmckfxfHk7XWOfQcHmhHz9MSZh1e3kqXXZHLYSGM8oinUVnbiRxOJHGI8cm9cdfxwYF8AE9NfSdzsIRnQD5HuIUnmviA4pgcUjEc2LHnjSVVYa1dDQlaqoJpMi-xfnaR6GNtC1ePgAtO1JEVG-NhLtfLYgIU5fqjX0Dsfi7bW9Z9gaYgARdpoWHSadMKLFuwAC9UC-70-oo1U4fGObRSA5fwMprVaZSveEv7T22gkZmAuK24DNACf58dnHqzlV84E84yv9PJqh6ytOaNc2lUsZXNpidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=l6HkfSnFnvK3WhB4iKhk8zxOS-3TdUT3vRVxOmqCizYXIiPgbdFllq0EdCinHMv8x9vZnOafykoy8r3o1Dgs8tLi7youIJidh8Y1zf1mIxKCxhbvvHzMTnA6hPo-w8tBAAIqsP56huk2lIYFp93BBXOj9-37R_iJ-jeY0jcMFaNlj493oOkIFOaaLTHEKklnFBbH7KznZHsXOof4VCJEk-HFvfRnOqlqEzY3ljzsk2nBNbCHIweSDOhos3H_ttuiXNDrgpRRX_CUTEZ8lgWIHVuVm6zEXXwZqA695MaKTy9OkFkAumDB7Emnq9zg13Tpq1xUjQppd-t6XVuog7A9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=l6HkfSnFnvK3WhB4iKhk8zxOS-3TdUT3vRVxOmqCizYXIiPgbdFllq0EdCinHMv8x9vZnOafykoy8r3o1Dgs8tLi7youIJidh8Y1zf1mIxKCxhbvvHzMTnA6hPo-w8tBAAIqsP56huk2lIYFp93BBXOj9-37R_iJ-jeY0jcMFaNlj493oOkIFOaaLTHEKklnFBbH7KznZHsXOof4VCJEk-HFvfRnOqlqEzY3ljzsk2nBNbCHIweSDOhos3H_ttuiXNDrgpRRX_CUTEZ8lgWIHVuVm6zEXXwZqA695MaKTy9OkFkAumDB7Emnq9zg13Tpq1xUjQppd-t6XVuog7A9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRy2Cg-CszaeAncLdeVlWZv4QzxrKfqvcLE0Cigo62rLCLiW-ezdCR6204rutSDWWjkvNDNKmEi8euLsS18s9auT82i8b1XwSfg_Zaln1eDjl01pLvIE4x2z61whCK6uoZ7NJa2XUuCF5bios8bZ_5O1XkJPAyznPArDBbdBGy33NazIHcIW-RyY6TKN5rhNJUkb83MdNSu_SnEdgYnmXBKXbmCKkEdL6KHfHzJ8oaroZleF8AytXLRSMFKjd9nhjlOUDqk4mG8xEbjX1-v6UG8LF5XPjf31ay8FvCH1-rZWm0V8QCNpl8u0MO8wcOnQvbF_CF-ywf7bBYF0X3zfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=PmikIEt5sotDFZlLLkfyEUwCa6L2mAY7ABVLVdo93HFroMJVNtA2OESr4Ns_xqZAoJ3j9_YsNFbx4J3Y4hahiMRP6hOAJ-9pNd20s2iZ99xuZJ7z_5j5Ts8KoeNzLuzCJee73ca2YcxzuilygEC03KoImBJ-V0zXoeT7ZqIs3SO1eC6l3sDsw6W2_-2MD_lZKr0CsA5LtH6lZtYfR65S0xLPqkOeIJA4VwqHCzsnig0SCmjEs-HHuPrYr-QlDkoRMD0XLJkGV54GQNGYaTrEecvkaNVHkgnCEMHbtci78HcsQlWxJXG56D5JBvWbzZSxEt3dwhUEXBHj-ft0IUcT85fZtjGGNmIlaCnEbgF-6C2GPKpsuvp8yVK1lmxSYGofXweqwJXr9S4ncB5aUJmgVOa6Aou4rHql0KZXODVzBjPCZv3NN-g3rZNJKd85XB0i89PusUyalfQmLdtpTGRTN0TvP087VA8yX6Kx9sTMDzyKBhfoRQCitqRBsZYVDElLitkYLHeXCRG3ec7LT7NHNhHftz6XeKfBR_EzZyN3SLjeCkEKFkJshnGUU4tMmLo2A1H5seodJ6EuTlhoIVrqoKfIctFLBlRz1RBBnkntCVQL3Hk692HL-eDJJAgflMd9lOWD1Kdzwrs_muDoBbfIG45DFva8uLbJ3RxLm0iPoD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=PmikIEt5sotDFZlLLkfyEUwCa6L2mAY7ABVLVdo93HFroMJVNtA2OESr4Ns_xqZAoJ3j9_YsNFbx4J3Y4hahiMRP6hOAJ-9pNd20s2iZ99xuZJ7z_5j5Ts8KoeNzLuzCJee73ca2YcxzuilygEC03KoImBJ-V0zXoeT7ZqIs3SO1eC6l3sDsw6W2_-2MD_lZKr0CsA5LtH6lZtYfR65S0xLPqkOeIJA4VwqHCzsnig0SCmjEs-HHuPrYr-QlDkoRMD0XLJkGV54GQNGYaTrEecvkaNVHkgnCEMHbtci78HcsQlWxJXG56D5JBvWbzZSxEt3dwhUEXBHj-ft0IUcT85fZtjGGNmIlaCnEbgF-6C2GPKpsuvp8yVK1lmxSYGofXweqwJXr9S4ncB5aUJmgVOa6Aou4rHql0KZXODVzBjPCZv3NN-g3rZNJKd85XB0i89PusUyalfQmLdtpTGRTN0TvP087VA8yX6Kx9sTMDzyKBhfoRQCitqRBsZYVDElLitkYLHeXCRG3ec7LT7NHNhHftz6XeKfBR_EzZyN3SLjeCkEKFkJshnGUU4tMmLo2A1H5seodJ6EuTlhoIVrqoKfIctFLBlRz1RBBnkntCVQL3Hk692HL-eDJJAgflMd9lOWD1Kdzwrs_muDoBbfIG45DFva8uLbJ3RxLm0iPoD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=JcIeZ84RjhvkeLDScmoqYQF8Qt3oyWdd3OtNCdw7F82oSW_qQl996FIReHXO7gYHs4EIqnsMQ52ynEGyGfo0SF8gOwpoNYPRNmn7HPth5Go4OC2YcTwQeYqlXAPQi_PDELDI6W-toFXusAfrGB9SyLnYQduCqBFEasT2Fl_J5SYwZWK0Cb37kaj9tMfQJtIviHpwHzj1wMFcGkivlj0KnQxjDQbu_mZAbpnntyYHkUTzZkwycG5qxpj3t9SJ2ES5wkA_9-docd3qHolK9vZRFRfNS71jVUFXy1nsVEXZB2MwYpBqUEIJe5HkhVnQG1PF2Ub4NwE2fcCStPWNT84_mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=JcIeZ84RjhvkeLDScmoqYQF8Qt3oyWdd3OtNCdw7F82oSW_qQl996FIReHXO7gYHs4EIqnsMQ52ynEGyGfo0SF8gOwpoNYPRNmn7HPth5Go4OC2YcTwQeYqlXAPQi_PDELDI6W-toFXusAfrGB9SyLnYQduCqBFEasT2Fl_J5SYwZWK0Cb37kaj9tMfQJtIviHpwHzj1wMFcGkivlj0KnQxjDQbu_mZAbpnntyYHkUTzZkwycG5qxpj3t9SJ2ES5wkA_9-docd3qHolK9vZRFRfNS71jVUFXy1nsVEXZB2MwYpBqUEIJe5HkhVnQG1PF2Ub4NwE2fcCStPWNT84_mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=hMnm1R2xCLBjZ50XYcLIvGR_6UvF-Vi4VMwlE15ZQumOAgBGUpqpRcXvtJBFuLJ5dHtINudhGg0KBm42Pg0kK1pYwvJ4bDvyGBV93isc8khqHZaXdIPtxETkgwcz5uJBQ4fwi02kFRE96E8Jdqwe6sjv5QYdkt-U4WSVVm9fdEZesNLP9ATOXZ5JHmtAj6cekVrf7fo2mVvzttJHFWGPkp33pv_WvkO8_1bWCMp6hp5GfKqytV6Tuvu2PJ2dQnB4f-xFc9RBw2tDTjC045f_YFcLSKCTI8NcxhTEOHDrSRRmRtGn2U85kuH3xY9_UmVih_Z2j2AbIFjgwLuBn8x6lWVNTKZ38J4N-NV3XFAmI2D4oCINAiCb0z1eGQ8vtIX9BUK8NvQhIK2JS8pJPyyOZdrNf-OuCcmoIlRHOsXbrwwkF6rMQhtgzjG1IjcFUDTEjINfazrViLJO9kK46t7_BHVD-6GBaAnd5zUm2p5IS1zhCNMOzu6oEV-6XPE3GPAPfthW3sNcd4K27n-QJmMxtXgztNDj7g-JP9RqEFmbxVxpWZ2yxS4P4zN_PGFA6lWpxvfnQo6QObitMGC3pmNWga6jyHgxVL2T-7UdNxs9-wgTGpKJc5qjipGDOn3YAynd8SjN-t2v2PSQcgFVib5mXXw8GR8j1FDMn0VvKYsBnW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=hMnm1R2xCLBjZ50XYcLIvGR_6UvF-Vi4VMwlE15ZQumOAgBGUpqpRcXvtJBFuLJ5dHtINudhGg0KBm42Pg0kK1pYwvJ4bDvyGBV93isc8khqHZaXdIPtxETkgwcz5uJBQ4fwi02kFRE96E8Jdqwe6sjv5QYdkt-U4WSVVm9fdEZesNLP9ATOXZ5JHmtAj6cekVrf7fo2mVvzttJHFWGPkp33pv_WvkO8_1bWCMp6hp5GfKqytV6Tuvu2PJ2dQnB4f-xFc9RBw2tDTjC045f_YFcLSKCTI8NcxhTEOHDrSRRmRtGn2U85kuH3xY9_UmVih_Z2j2AbIFjgwLuBn8x6lWVNTKZ38J4N-NV3XFAmI2D4oCINAiCb0z1eGQ8vtIX9BUK8NvQhIK2JS8pJPyyOZdrNf-OuCcmoIlRHOsXbrwwkF6rMQhtgzjG1IjcFUDTEjINfazrViLJO9kK46t7_BHVD-6GBaAnd5zUm2p5IS1zhCNMOzu6oEV-6XPE3GPAPfthW3sNcd4K27n-QJmMxtXgztNDj7g-JP9RqEFmbxVxpWZ2yxS4P4zN_PGFA6lWpxvfnQo6QObitMGC3pmNWga6jyHgxVL2T-7UdNxs9-wgTGpKJc5qjipGDOn3YAynd8SjN-t2v2PSQcgFVib5mXXw8GR8j1FDMn0VvKYsBnW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=FXVPIPDaiU8YqJby4ewoInwELKrl1ZFRBf0t8CTHlDAKGtLSDljYaBrVc0arnJBzQMVwRAks8S1o67P2Vj3OX6rqdurm8VR4ICsRVpAzFDCR8n-s0XK5uth0Ojts4L78VNnJkxYK7hZeb9uUiQVyp9wZnqFf-QUCzKIcH-g3aGytthp8gGFmyxHHcM5p3QnCpqtah6Oni92gbMIfCFG4l-hRyeGO8LFL1ZVJSwm4kg2lMMO2NvJ8HY9J9r4CkEfu3v0QNjDPJxEgRRflEroyHcFuz27t8WbIG050rMZgh3I6UQ0vSYGKivVpWX2wXTAQojZ8E_PRzDzrtutNUjbRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=FXVPIPDaiU8YqJby4ewoInwELKrl1ZFRBf0t8CTHlDAKGtLSDljYaBrVc0arnJBzQMVwRAks8S1o67P2Vj3OX6rqdurm8VR4ICsRVpAzFDCR8n-s0XK5uth0Ojts4L78VNnJkxYK7hZeb9uUiQVyp9wZnqFf-QUCzKIcH-g3aGytthp8gGFmyxHHcM5p3QnCpqtah6Oni92gbMIfCFG4l-hRyeGO8LFL1ZVJSwm4kg2lMMO2NvJ8HY9J9r4CkEfu3v0QNjDPJxEgRRflEroyHcFuz27t8WbIG050rMZgh3I6UQ0vSYGKivVpWX2wXTAQojZ8E_PRzDzrtutNUjbRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=kGYQusgR8YgGY3jD3Aw585zlMVvXUXavjEBqyh9H-ffGtlCVedQ2F80lRf2woSnimSJrgQSXutdyRdZGq3LINfVevCxH8lQ8U8KFUDRfwb3gZ1YPxMlp7A5KVoIQtfdw9UjNSQZAZS8jHb88gb1fVA6y6r1QcgWxX_2q5rsfFc32HA0zmn-Iz1QlBNCYZma4HDCx5o8eUl7C_5qSt3X-st2P6sdSeMgxb1tSZ4pTNrh-8mLtarASVkktaROD-d40WGhS9lhvW5jXoCUrK8-PhEgAafEhNdbKFRkLh7F-PzTm0y3agl5a6ND6misrQsrDO_YvcbZCVJ0aFcXlLjI3sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=kGYQusgR8YgGY3jD3Aw585zlMVvXUXavjEBqyh9H-ffGtlCVedQ2F80lRf2woSnimSJrgQSXutdyRdZGq3LINfVevCxH8lQ8U8KFUDRfwb3gZ1YPxMlp7A5KVoIQtfdw9UjNSQZAZS8jHb88gb1fVA6y6r1QcgWxX_2q5rsfFc32HA0zmn-Iz1QlBNCYZma4HDCx5o8eUl7C_5qSt3X-st2P6sdSeMgxb1tSZ4pTNrh-8mLtarASVkktaROD-d40WGhS9lhvW5jXoCUrK8-PhEgAafEhNdbKFRkLh7F-PzTm0y3agl5a6ND6misrQsrDO_YvcbZCVJ0aFcXlLjI3sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=YSsFDKxWdqdCWfcGfqXwx42o9cc0tYheTwXzTz0yKl6CY0ojKKfWtMRtXOxGc26sgVK9qDkeohUiEdR5uW9sfI6iWbwUAlQocQygVXoCnXBC9cbvnXxrzrNymKkLMDbXDHJ277xqBVMc_ukQW_jmoQpt0y6Z_FWG7GBYKerriAPpdqSWcMHkCpUYFjT1Oe1n_U_6MYWbHfR7tpx01P9VtDcoZWf61_e2hr4kqJ3C5pdJoXZxVCBF0qFA9-QovjL3a1mOQJK-03PdcQsh5FcFCPrOrE7JA1CAIg3OULptzJmn7upPzii0BejcQK98TFREJyEx34uRGAV9QzhcC_NiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=YSsFDKxWdqdCWfcGfqXwx42o9cc0tYheTwXzTz0yKl6CY0ojKKfWtMRtXOxGc26sgVK9qDkeohUiEdR5uW9sfI6iWbwUAlQocQygVXoCnXBC9cbvnXxrzrNymKkLMDbXDHJ277xqBVMc_ukQW_jmoQpt0y6Z_FWG7GBYKerriAPpdqSWcMHkCpUYFjT1Oe1n_U_6MYWbHfR7tpx01P9VtDcoZWf61_e2hr4kqJ3C5pdJoXZxVCBF0qFA9-QovjL3a1mOQJK-03PdcQsh5FcFCPrOrE7JA1CAIg3OULptzJmn7upPzii0BejcQK98TFREJyEx34uRGAV9QzhcC_NiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9-tXJhqGH3Rmxh-LOs7qBPOfablxg5qK3Ft_BB_B5EMKliU6ghtxap0hIKN9OhFCa2jEQrQqHG_r1x5zCdL2lh4FWYVTAASs-2KffzgbAMAXflunDdQ-bHBLVr-tp3eXJi0NWMCid7CPQPyI5YF-3CA8QbhGeJc9lXOwFfFUTddokULeuEOnvvXeYK7MoNqSeMNV-WbEtDvBJobYEYrZaeB0orSGb3Ga9dGh6AUQ-kj2gh9XP2IGNdpqvzbBIzNQKdkHRtDCY2Cw8efE6Q2pQVoLqvtw4TUNiXe-_gTQZuqAyXdFHNL-PFhpsKhfYHYxx2lIJYQJixQe2-WBq2clA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diBsh2hL67Sf7zk09iDp5xjY-d_b4PmrXRg4CkZ2IycKy2z0t-n5ABebKiHAwqtSUdcVEeZ3D_vYhelcbijjsdpmxmpukb8cf94bj9n2GZV-r-sRHdW7tBiclLOvGw7G5xOHD66uHKoIQTE7Vj8UslnoJVXWNy8cRm83GANBMCSKkMpD2XJyTWOGViYUjSZof_PrJLYOFTQbxSgn7lRtJVh12ia9QnyHHsGCjlYYhqbHt4DPbLi7gaZxAG_InV_votaXVWbNE8Mro_0Jpv947q9kxRQTxSmG5oenFOzBmR7OpsxrAEcUdU0UE7-g5wxd67v80z8eVFOMHlSvLtoKQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO93Z6USYn_BN2LLCIYokEJZJucvOZX1qvzR58FXhGIzQqIr_9OKPcjYeNeJNvj6Y5Y7P5fvxt0KUr35Z4RzeAi_twO8PXjDM49t2puoT3qiyJycxUMWkbqC5hS6zKoJVgHsKiHBbe8CeaLzSuovE42KlerhGxERFzc2XNQmiNFKZtJDiGCxzUG0nhaVmJo5zfn9zq6jRk5YMgG0idbZr2-9vRlckyPQ3Eq_k5Xp9Y2SIii0e6JVlDJibjae8wNyg1yKs_c6r-wK3RLzSFw2OeB-wG19TOdQcSgUZ8WLg2TF6ML3Q4LM80nQL7lqrvcbdmvzPXb6fuQ2wsoGGFRr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqR0CA7-KiAiGA_stW6wCvFGqZS-MU2WCTBzuNZzqXvod4tqYEgpbIjgbP1qbGNP10vzrT5w-fcX2smoQ5rI6XjQY-84Fk5rg9We87obvvqpF3RZtw50fZ8apX74YcBxwm7T4q7d4fIwlHYIO8XLmZAIyfYAX9_xO603Su6nohYHTEEKGWnNcr7pzbADFgolYhvJSwLud0u_wczefhWsYjof_CE8faDT-uFh8cjOrDD5OCHBELwGyUSYOpGjyRfFZNa-2GZw0eJ76xEe5wLBstu3QsiRnTWAFq_pHkIRCWwQTto6uEOgHi-cWdjxupYS6KFBRqEdcqYDiLVIHdxenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6UTAleIn6T0X8jx6boYzsxeCtBoUVj7Srn7Ygr4sAv_Te7qjHl0kTVEHBQaOVRobY_mDZKzbz09xBPWKnCGE5CRe3wT2p2cMdfDOIt7_1VTqN0J_QCKvBcaVY6UeQ-opwlJ6gqDAwHP_NaUBoDGMzmrKUDEJ8oalneuI8iH7eK2r7RP3m3VK096iAUtDzGpoZ_VcX9jv6lA_4C293oaHczjnhRC4rO4Xpr3icRAm5BXAPOt-TQGnd7QFpx_0cFT_CclIbbNFfjqyUz6-O_am3IsiCZ60Uz2e32T2sdmfHkdnyizsa3ndmDPCHMGjK4O7N_0rrgbdaR7YlcM-iIxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=nk1ZYjH8vM1lLNg0A0FGQBqoo9M9LgJTLVvi8azy1RlmXWTBiWPmAIxBxl3eBX3cTQa7Neea3fX-owGHR4s1KH6PvqCWkXFbhu4U7pRfiI-leqxmlXhyyHIShmdXm6RBoWWaU1nilhh9bOOFv9lJVNfJ1NdoElYIHVSkTj7_QxXB_NrTksOp4Wws_BCoeptd76mM9x8QTbiwXs9vjOTcEaVbKJg-t-YnOd0iwGWfHXB_9XqFwIJtQflOnVNNaiKdKbGLSVdEf7N6zGERaZtU9Jt3ohWlXguK4JsyB_hsF0DKROkkPxbEVHHtIyLkj3v3Y08aR_JFnqr5SNSbXQeDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=nk1ZYjH8vM1lLNg0A0FGQBqoo9M9LgJTLVvi8azy1RlmXWTBiWPmAIxBxl3eBX3cTQa7Neea3fX-owGHR4s1KH6PvqCWkXFbhu4U7pRfiI-leqxmlXhyyHIShmdXm6RBoWWaU1nilhh9bOOFv9lJVNfJ1NdoElYIHVSkTj7_QxXB_NrTksOp4Wws_BCoeptd76mM9x8QTbiwXs9vjOTcEaVbKJg-t-YnOd0iwGWfHXB_9XqFwIJtQflOnVNNaiKdKbGLSVdEf7N6zGERaZtU9Jt3ohWlXguK4JsyB_hsF0DKROkkPxbEVHHtIyLkj3v3Y08aR_JFnqr5SNSbXQeDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=FPq3wE02a8vqxuXWA_CxVfOnElgye2EW0k2_vBBjNCQ7XPJnbPceOnKXYIyY7V96W6EmpkTSwK_KJMVvAw0Wni-qB1bfV0tumCRiOUJUTgLzI0_Pg7OLFUHe46rxoyUVDckngvoGQcB0cR__-yQz4YJ11GWuU-bSmpv-0wiMuEqxIIJAk_yaIhL0pesHR2J7JYobceD2HNs50hm9gxa3w-LAwIKrMQdK9nve5lAHXYffDb3cDCG3DgJKGLVF_F217_01mLP1EiqsQBjLW2kBAZfeyo07BpwAZvNIOhmAFqtdMp-YbixHiO984_mDSmXUe638xD0peY6b4eduJubEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=FPq3wE02a8vqxuXWA_CxVfOnElgye2EW0k2_vBBjNCQ7XPJnbPceOnKXYIyY7V96W6EmpkTSwK_KJMVvAw0Wni-qB1bfV0tumCRiOUJUTgLzI0_Pg7OLFUHe46rxoyUVDckngvoGQcB0cR__-yQz4YJ11GWuU-bSmpv-0wiMuEqxIIJAk_yaIhL0pesHR2J7JYobceD2HNs50hm9gxa3w-LAwIKrMQdK9nve5lAHXYffDb3cDCG3DgJKGLVF_F217_01mLP1EiqsQBjLW2kBAZfeyo07BpwAZvNIOhmAFqtdMp-YbixHiO984_mDSmXUe638xD0peY6b4eduJubEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0k6pS7-vCpVu2t8YrsnwrEw_mWYXplQbQnubfpxO4_dPe-rxnR_1Emt9VDdFxwTFBUHOeSU0hKxWAh3h8PajkJ4ztivwX7hwVfEMFtYuCVR-x1Iv1va_FZNvJ4kAVRNj7rYd_v3JczP4RYo_SlfUR29d8TvJyKhTfz1F32SreGn6y1aa31EodPb1jwXbuNvEHLqKKs01ae65SsZPgs7O2fyFYXxvMxjTnD2TpFoart2FS6yrvgEnkEMs9jyJO_fonf4twITpPo4H7FQoGKeSnmv6IDTISn0GKe9CW3Tb13toJwDc-y3Q14K6VVXGUC1A5CYJnhkAaET-l6NQREwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMFwbQmA4eqf1sWIOnXBRGMezux-9a4wEMyOOzpfaNxcZxUJEJhsBlZv5tCBQ1bkr0n9QRSG4sOwwbZuiX3XGWzPoqMt3SQfPI_uw4o2ACCfffvm4mEXAuTuZN9UhXG20XUOMwukt1aqPRIvP8NlSSLqqhOLSUWoDxl2FoV6ROpRuv310SekDJaT8UvWs7bT34XasnBstE_6AC9h9yyHX_djCxOxq8HcrkFhFgFIN3rpS6w6Ct2zv0dRB4XTNkNUun08yVepwmXrVV4amjW8_pT8N5mRiXDEM_UgfTemUv2sNu1-hVNdX2dtBm4K_ERpfcB4QB3JdcXsv5wkopnfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=Nvmr6ml10PCs81WZklPwKt2BBZHc3tkHygNOhSbX-cIORHxbmHTusTcUPMPIK_1E3saY0U_myjKBthqjDoghLps7Ibr2IcgPwzkdK3B1wi1aAYRl8UKEUVlhGDxSmNtPCWmWGLdYOYqg5SeIoOlfbwpuJbCXjcIESD5X6NLaFjZEiLMhhDB-3KQjcZOQI7a4FiNX0kUSeymz2hkjkyGuHtHGR27fiWiEqcmzMaCPqZeUv5YAbyqqL14PAWTqd3jOQ559pgYhR2DmksSH-ZXmgBqGvH49pof3TvNO6-B6FtBKsvAxWwLdm56-o8SkDmzOpggnTlmQx8VWEyX4_rTkWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=Nvmr6ml10PCs81WZklPwKt2BBZHc3tkHygNOhSbX-cIORHxbmHTusTcUPMPIK_1E3saY0U_myjKBthqjDoghLps7Ibr2IcgPwzkdK3B1wi1aAYRl8UKEUVlhGDxSmNtPCWmWGLdYOYqg5SeIoOlfbwpuJbCXjcIESD5X6NLaFjZEiLMhhDB-3KQjcZOQI7a4FiNX0kUSeymz2hkjkyGuHtHGR27fiWiEqcmzMaCPqZeUv5YAbyqqL14PAWTqd3jOQ559pgYhR2DmksSH-ZXmgBqGvH49pof3TvNO6-B6FtBKsvAxWwLdm56-o8SkDmzOpggnTlmQx8VWEyX4_rTkWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=CJLqktvzyDxj9OSp1SCzR17TMdJsnevehxRML7meaO-kdiwsPlKosmIXIxp2cU-s3IF2eCsII0X1djIVt_jix3o9WPctF_vebbEJRIZQ3f6mk6iwdgD-m-95PReoVJ1BouPBi8Iz0_m4p8-UwHyQWYb5Ms5fbncCJOmHX7k969r1iNOVhtuefxULzgAmKYHZXh0bKfb9n4gDuPpQbMk-nF3FNHormtiiX7o0YEla50SPKjazB9FwGrpANny76vO0CPbAAKc61HratCbnkYmIQttqSaZ28xk1Efqcvcx2wiO-hcFXB9Zp3pAmwxigmSBkVoNZ_UF1bua91IeSrlABKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=CJLqktvzyDxj9OSp1SCzR17TMdJsnevehxRML7meaO-kdiwsPlKosmIXIxp2cU-s3IF2eCsII0X1djIVt_jix3o9WPctF_vebbEJRIZQ3f6mk6iwdgD-m-95PReoVJ1BouPBi8Iz0_m4p8-UwHyQWYb5Ms5fbncCJOmHX7k969r1iNOVhtuefxULzgAmKYHZXh0bKfb9n4gDuPpQbMk-nF3FNHormtiiX7o0YEla50SPKjazB9FwGrpANny76vO0CPbAAKc61HratCbnkYmIQttqSaZ28xk1Efqcvcx2wiO-hcFXB9Zp3pAmwxigmSBkVoNZ_UF1bua91IeSrlABKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=TN1KUR4iO0UzAD_l5QNIfIUsjUCHfTxbJvUYYRtvdfug-rcjwZFAakXVve3VCSAwQ_pOVvNE_g624cRharRzOT0tJygc45-53viw5SErYACmDMdQOSNPRljoYKYetx462QpwscRJCp13AIeWgRqF49N_sVT8TfvySolrjDRnDCA1D1So5PJN2RqPnnfaxjiogpPBty_IMbKhgqcD8J2-PyluBLnplNboHBmT6j5u7nZ9nVeeQyD1RCiLRSPyzDuyXrN4IR5ZfSf4vZG8CSmITFeUTQ5M0TNpT99klC6PQUCDmdRqCZO9ZE_a_wAMazA9Ob9Wlve-RuWOnO-Ep0s06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=TN1KUR4iO0UzAD_l5QNIfIUsjUCHfTxbJvUYYRtvdfug-rcjwZFAakXVve3VCSAwQ_pOVvNE_g624cRharRzOT0tJygc45-53viw5SErYACmDMdQOSNPRljoYKYetx462QpwscRJCp13AIeWgRqF49N_sVT8TfvySolrjDRnDCA1D1So5PJN2RqPnnfaxjiogpPBty_IMbKhgqcD8J2-PyluBLnplNboHBmT6j5u7nZ9nVeeQyD1RCiLRSPyzDuyXrN4IR5ZfSf4vZG8CSmITFeUTQ5M0TNpT99klC6PQUCDmdRqCZO9ZE_a_wAMazA9Ob9Wlve-RuWOnO-Ep0s06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=TnNMvjJC7JlAvtyymyC_chYxfgIaU-sqXJ2SjMLYn2jAmyrWvIP03cyD-xwMdY3vtK9K8Cv6GIQ4FZJepZA-ypMmKUHtTLrw8j9WVQdzJZbb0hpdreBscGgo4WrZE1cbAMAYv1VR1NSeQR7A_tmrx0ClAUxE2suwyI_mBwGkXKl6u2KGoS19h-vC1_Tu3DIyppczXN3_nsZvTpolVTDgH1StvKCOayBaZLpNKb6xMzKnh_ex5MF62BKJJ_YHAKikKSM-PZPDbqaUKA-UC_nIsCv1uDW4laGv2vM4EXHrQZhkSgpFMDHXM8KRNXwBeXBeB5MBoZvIy_5XwkngwEdXEhHJQ8XBufqGwOebsHqRheMNZAnMwIoJw5tuyA9tIf8KDoOXKRHQOqfroCMfVBuWnPv0pdgM6CLDJ6Eqz4D_7aaJTiUFkgrBJ7VZe9lC7ut1yWvd9ldFarWYyfjLlifKPT6k2vqWBvSSnCDTC9Mu9twFQdQzoAEJ7p_qB5kBg_RHoW2lAclVpKMdIddQkA5x8RzBxHOHXayMSeqsmtSzrHHPGnACN0gm78fIA_SK3MUDHjGFO9QgOJ3l5IPXezB5Ov-c6SVl8eZXYoX4n9YsQE1PWnYLhWHnZbzBWWhewBHrV5y9sOvJXyLgHEBCe1OU6g2F2mR8l0e0vanE7nL5IgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=TnNMvjJC7JlAvtyymyC_chYxfgIaU-sqXJ2SjMLYn2jAmyrWvIP03cyD-xwMdY3vtK9K8Cv6GIQ4FZJepZA-ypMmKUHtTLrw8j9WVQdzJZbb0hpdreBscGgo4WrZE1cbAMAYv1VR1NSeQR7A_tmrx0ClAUxE2suwyI_mBwGkXKl6u2KGoS19h-vC1_Tu3DIyppczXN3_nsZvTpolVTDgH1StvKCOayBaZLpNKb6xMzKnh_ex5MF62BKJJ_YHAKikKSM-PZPDbqaUKA-UC_nIsCv1uDW4laGv2vM4EXHrQZhkSgpFMDHXM8KRNXwBeXBeB5MBoZvIy_5XwkngwEdXEhHJQ8XBufqGwOebsHqRheMNZAnMwIoJw5tuyA9tIf8KDoOXKRHQOqfroCMfVBuWnPv0pdgM6CLDJ6Eqz4D_7aaJTiUFkgrBJ7VZe9lC7ut1yWvd9ldFarWYyfjLlifKPT6k2vqWBvSSnCDTC9Mu9twFQdQzoAEJ7p_qB5kBg_RHoW2lAclVpKMdIddQkA5x8RzBxHOHXayMSeqsmtSzrHHPGnACN0gm78fIA_SK3MUDHjGFO9QgOJ3l5IPXezB5Ov-c6SVl8eZXYoX4n9YsQE1PWnYLhWHnZbzBWWhewBHrV5y9sOvJXyLgHEBCe1OU6g2F2mR8l0e0vanE7nL5IgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=o8U-tAOg_nDZl2F37OPjDWeQZxzeS3W2CNQMo174KRZLAZV96Aj0e9fonJXUNEd-k2_jJ1Yjt_sz-bSASKb_6jVmXm7I2tXQet8wcQFROE8v4_jSuOPtjOIfHsaPRG6XWMbO66msxO-RuN1aSSUHbV6FbJb5dBobvMnLbBD3rwR7w8FiD_lUGPmVr4mFT-ntkUle7KWuq9pe3Zz2K6IGtEAgv9fUEksH5dmZm0iqtHJoOvMUnFOKT7BzF8CGB1TaCFGZlbpVc6e1F2FlgOQJGnuLwDywrqxOY8lWGIJvuxzWluHrZSPkUAA5MMwO43RRkxliNEGZ6OuvT35cw0QaiX2OCA1jShy7UGZXKhNJpU9IfZjRyP1wO2FejR4jNBMjSi_ZHGgdVlvhyPApDLTi_L7d-OKgSj-ox8tPLa813lr3Si3hvI-W7kf_yhgdJLKhqlS3pXDkqwCDnU3cgIVEqmD7C4m9LSoaBq5dVTUprCXaMAUR9N5Wpf2GhgtZhnCXWS9_V-UoO3D50G9Tuo5y9dvt6MbtzMh5veZ4qPefXSPpVEp2BSbZrv_w6IXu2etjFpMmdGJ_Ok31BYGzmN3NNFCJUec4V-PJktZK1loIq98o9eV7yPF1ak-jaQZaaYC_yw0-HPRZqhFxOtFi3CDndCe_qQcDLbLOST4gpN7zWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=o8U-tAOg_nDZl2F37OPjDWeQZxzeS3W2CNQMo174KRZLAZV96Aj0e9fonJXUNEd-k2_jJ1Yjt_sz-bSASKb_6jVmXm7I2tXQet8wcQFROE8v4_jSuOPtjOIfHsaPRG6XWMbO66msxO-RuN1aSSUHbV6FbJb5dBobvMnLbBD3rwR7w8FiD_lUGPmVr4mFT-ntkUle7KWuq9pe3Zz2K6IGtEAgv9fUEksH5dmZm0iqtHJoOvMUnFOKT7BzF8CGB1TaCFGZlbpVc6e1F2FlgOQJGnuLwDywrqxOY8lWGIJvuxzWluHrZSPkUAA5MMwO43RRkxliNEGZ6OuvT35cw0QaiX2OCA1jShy7UGZXKhNJpU9IfZjRyP1wO2FejR4jNBMjSi_ZHGgdVlvhyPApDLTi_L7d-OKgSj-ox8tPLa813lr3Si3hvI-W7kf_yhgdJLKhqlS3pXDkqwCDnU3cgIVEqmD7C4m9LSoaBq5dVTUprCXaMAUR9N5Wpf2GhgtZhnCXWS9_V-UoO3D50G9Tuo5y9dvt6MbtzMh5veZ4qPefXSPpVEp2BSbZrv_w6IXu2etjFpMmdGJ_Ok31BYGzmN3NNFCJUec4V-PJktZK1loIq98o9eV7yPF1ak-jaQZaaYC_yw0-HPRZqhFxOtFi3CDndCe_qQcDLbLOST4gpN7zWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=jWZQNT9Olw_PRXVm__C3umL6e_TGHc5KLad-mbX-rEf-FnpXSZ7p7JOQUMSpliJtzWfcwZfcndcK5VuKnCrIFnNDBIzj0YWlLnpY8ZL0Dxhx1VcBUh7532KjvdERui7wRqvL4cRMT2jgOU1b5TJd3sHE5P81lZuEL4rzYs-wTi-o0h_4Kx8pG1ONFMgvCE6TQSUHFDVcSsKudqbKxdXVM_gjbsqO_3jUUrZaN5r3EreYauLcqC19B7HiYBj7kQb8Vnh-7Q2ptthobmTDk_JomGaJ-lXI99NAu1qOEii5VQGC56mObhT1I87-BJF59zSWY7M4flpxteWYR7GhlYfqlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=jWZQNT9Olw_PRXVm__C3umL6e_TGHc5KLad-mbX-rEf-FnpXSZ7p7JOQUMSpliJtzWfcwZfcndcK5VuKnCrIFnNDBIzj0YWlLnpY8ZL0Dxhx1VcBUh7532KjvdERui7wRqvL4cRMT2jgOU1b5TJd3sHE5P81lZuEL4rzYs-wTi-o0h_4Kx8pG1ONFMgvCE6TQSUHFDVcSsKudqbKxdXVM_gjbsqO_3jUUrZaN5r3EreYauLcqC19B7HiYBj7kQb8Vnh-7Q2ptthobmTDk_JomGaJ-lXI99NAu1qOEii5VQGC56mObhT1I87-BJF59zSWY7M4flpxteWYR7GhlYfqlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGsjlsOrOtOjmxj4VUS1qeojK38_kN0pKktV9hGeyZ-XioZaWk1E6xHb77EPO3Hw4yvgGaYYXSOkMi5DqIcdU1RU9lAzny__mastooioYHv7sjiXR5Uei3PnaNqdqHl-efmuS1qDAshEjwfeNu2tUQfnCvI75McSbLuQHXQKk-m35gnBAYRibKWwV4DSlOXS68W5-4gZXR3Uab1ii31vaDDWeCSeTqRq8PMZRArz4VmtwbRdPvozTqXHtvK269QXMwvYgKaEaKgSHSkxqsqEEAEyTVB3LSZZ3Tms6bwuMhgbxueirFehUSHHFkQenneXMPTKFtxG79kaMNI0PKXW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEvmrkkjcJ_tsEh-3XE2uL2gRpU9EM3lwqxR2S7aEMBY4F4mc1PciNx2fjhO5u4zW0NAHs1gHVcv1hG_AilP07mFVV571G-w1hZ-wSwPUfFGgpbse7uyA8m_L6kdD_ZCLImN47SCzwbIWX8HzYoUb-EzXR8YWiQ7X3JSgCRe1l5bHOLYIdEpDt1xSUbp--HoaXED7OFR7khIRUHHsnJIJ1jel0mIpgKfAEvBbNBCaZYL1PmK54Bj_vbgGCDoJfzZagn0rO6vX0_6xsXrcCzJqjWuESbRj4W8pep1K89yqv8eprscsuMGX8Ngn8XDjIDmCTNAuJb36_rvBh4uDpXLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=cEuvjMFCXyH5RfELOojQ4Vzy3GBsWZAKT1Ol8W7CtWVi3QAXImdmc9akg63ipphN0B3kmEDeRqQiQmxYjOcfm9kJSbLU-iP6sW7fohrXf94eahK87dbHLVdYZnKqUpcFzF9gvoQg5idOxbrAwt_ooPinxbfwS4Xn9WqpVYuUobe-jCVkkHQrJq5sD3OLFne1TluU-uD3X3pB2mCBy6_dqNNDlYs7rXKTfRJZMPW5jINFuBlIMmlD16YrqYQJWsjHF_enLk_uHU2cej6u7qxhbLiMthaRxj30581pnqieIkcNHRz25oFgcVvAdAsILmOCXof8afm6HC6P6cL_f3FJbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=cEuvjMFCXyH5RfELOojQ4Vzy3GBsWZAKT1Ol8W7CtWVi3QAXImdmc9akg63ipphN0B3kmEDeRqQiQmxYjOcfm9kJSbLU-iP6sW7fohrXf94eahK87dbHLVdYZnKqUpcFzF9gvoQg5idOxbrAwt_ooPinxbfwS4Xn9WqpVYuUobe-jCVkkHQrJq5sD3OLFne1TluU-uD3X3pB2mCBy6_dqNNDlYs7rXKTfRJZMPW5jINFuBlIMmlD16YrqYQJWsjHF_enLk_uHU2cej6u7qxhbLiMthaRxj30581pnqieIkcNHRz25oFgcVvAdAsILmOCXof8afm6HC6P6cL_f3FJbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhM2V2rwZpAuY88PtpGe8iqP0Xr-1h_67XT_JRbI0x2SXpD8hEl74d8hOZq28a6G27SHRiVmrNLEXpcL1VVTf7roKiNm7qSR1XQkVYKXDupqyXl9h0vrkBBb6lZMM0iOOhqFeiqraGJthx9vBZdpoNhvI5AbJwX4sOMATV_g_Ut7bdytb7SFDypLUBTlx_97YRwtTzCoAtd2r9kd9kNJeBqJI084X9MKfB7LntrmPsVB9zHND-2X34K9m5g1x53kYNqhC7wO1st8B_nRJvyEOUYRExHWed7HBFroDz3_Gfd_EOM84I_k7zqvPmCCqkoOtQ-zLoBjBwm_Yy_PtADNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xdvfs7K_zNR9AAl45Rnk5vYGbnyphZUR3AHWkEMywYSBjMaunBfJwqQj88xH3gRYgA-PdHI9_UnyNFYwiSLSfeu8PWX5wRk8-BD_tm8WZKn1ruke8_rt_NdxcI-u35YfxDmcLOWQLEZBR5HHEDarkWKirZ2_g9ZzBCNeMkL3nJjk2TXT6RSx4LHTAhtNKnOxJYWAEO-oAFMeT-24WMk6TRVJRfV-XVQpw9Jr1Cn8AfYLOB3gN6d0D044WaejANFs-N7WV55-PQyBRArFHhsCgoA8mF5ovadu3IYR-un8gPOCQo9YO4d61Q9ZD4Llv22fIsVH8D-krJhDlNbwU_JZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h85Mf4LrhPRDF4GIvDdJkmltcquKfvVIJYev8YXaQJUt3IEmZm45CHxPwppixwoZYhzPzguJo99c6bng_vDlQLAYkmOZp2DHH2UceaslJYIJ535Ad5FzASSWhU7VnLo4Fif5hwowREUW2WsZ95Hn-8FgV1cGxqG551KQ7GoaFhTQcld7674nWAXrcEsUD-sAkui6Iz7YqdKBpbhhjHrv1nQ2GxcmzyCgRVZqg_7AaRlc9SHVL-q3RuAyQwd6qtvtxg39U0LizupWPQt8Lr5UnKkBDYKDzKamooe0HIIfG-E1YpRQ8N1pt6S4fG81xFE9fZaBv7yfng83MB_TpT6w8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjNM--vKiQMCuX6IcMdGpZ24WFa2nBiuNXriqhJwEanKXRYBg67VG_PqX926dvz9u0UK3hEGAZrZynNM-ngfu1DgQjs8GgmZST3C-_-VVAUFeQUrvT4VvtO2f0__gknGbI-Qu_PlEXifiezYJsABnWThA_rFhwt9nAIgmcmfukVI9PNEo2RR1uWIthUZOG_Q3dDRQjG6B5xOgPwRHIxPru6rTzuFx7Ooa7MKoC8Pzu5wXwznk-ZFTgeVMyh5buwqn3iUgo6wSaSgFds1CwvbyxJDV7vS-sRUojzfiAplAFqYuvzqbWGKT6SMZsDGmLij2vC-mFhjIGNtc2I0Oqensw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q6bajyCTHXnwbZl2X1bsnSf3n3_9mO6nFzuznp1mHvh0hUURSLN4rkGtZsbCci9yaf3QG0NdUMfSgvyfZVIxAyEouKECHrlT_GGG9Eqo0AZfDQC2YrBnOVvBUUj_KCXG2sHy6rTE6zLsi3fYAK3q_4CGeEWmn83DhuExtCP39eFp-eicCq1t2qgFqqoH7FgnnuZtyZgd53I8WcLCV_O9jt8Igoe6fDRvcjty94Q6KS0pIR8fy0bm_d2G1-ZcFAUeu-9sTB57H4DZfhmBl6VIW9SEcBjYUjKYBwaokiugNiiGj-nchvd1aga3PbKkyqsL5sPeXKHt8z9X4_jy-Vr2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXNJ-pSBs0s3Lmcg-UujmcHtYqoa2X61NRtW5OGF49cUBt2gpH9jompE7Hq29fK1Q2aOSQDxMqc8PGyYHIfrfsA1PjV5lnaRTGWwthjbyTrDtSuniPiNyAGJYxccjmEAYRl8xba84zjTa5Fp6euZMu4tZsVcw3xp0oDEWMAA5nJqAtOEfydDADfwmFZqR37DfFxZRihmJA1OAUJ1aR0ieogRgmqnAfAtx-8ZsPVQXTVKjzT-8o2yxyyQE7d70orrygTV48o4pThNrMFLk7J1HpqvrSrP6MfYXzUFNkWdjnRf42cytDLHzQOt_asqwKK6cqoU9Jv1GCdCKYPbIiCr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBgltXwg40EKZbjl09hC47VtyOZLHozkUjV_c4RTBYWwF3mfT0D8kSFyVvuBNtlVl3_Jp6inIl5RiHVfUUhBfnL8VL0exv3E5w-qcVWzg5uYF-dLB-7SO8xvzdctmDJtgovg4if3QkFP3zdHX6AHpZzexOMAfhpzkthWC02Sv3X5qnYYJHJTM8YCt9ueTX_cDuc2fPlIkU85Q06TZHVrgHRujxecEsP-xvKMoo-V-XeMALAeCF2F2FWe6swMWIaXZVWzXNy8t2n103Vq0BVxrhDffGW2yiPeDOgPUyBP27F_72q9iikayTMyxitWDXoTSAtp8z4iDVxIxOYokobu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XF3T4wUdNetyU35HkN8X0gsDiZRsgF_UAc09Sh8lngWVV2ltwb2LrhxYrP-Riq6FeyfnURmaFKzQrKXIb8SWfn6oKqGfvV3JLNHRcREs8oZfpik4UVhe_ab1Ablj1sNuRmjA4rdgb0mECFoSOvRIdGMrtc1fGdAarTtRSOg2nY4kHSbnl7CoSIZGko8fdWDKctyN69CU7gxLUVmcApIfwwUpkgX2osQacA57s3Y9_svXPMX37JNdDk-n026nPDDjdn2lRZQohMlUjGQH0e0Or0Dy9XxgKZ5SKIsOAhgfaF7DTnlerOs_24b3P8vZCmJSluNhevdoYcAmHPjHT5p8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_PTgJ_Y8Wt5TvW3SUudeCz6eT4I9kLb5ZD5Kc8_oaH8vh7HdmGH7WjqYX8ZAP1M9ciSUfPwiKp8HYUruCeR3pdRFhu6wYUAbTlNnBZvlHsO130NVe_az69u85SlnG86ylVKAnD4hHFLL2Izv9E0943gy4wZ1BXvuyD6c5sBR7hsXjq5qPDINtrXonrm__ttyqSeoIBdH9NwZJPcoVbzRQqUjCdxgMUBEVMGy0_SsJy4135GQbfaQsbBI7ep0B3Srr31vHgiJQ1_SF9e6vr-r4N6OY-8aG6UARvIooKDUdL6b_QPHFAYbQ5B2Ew5rceiKiGG7wAsRNsKynfY7SFHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn9Eqm9XtlVcRnqbjbVXJREqJLrNMC56alIrJhYxYqAJuOeHqV-DsYWBlg_KKLcLFZNNrwcAtdr3pY9WPaRtFy9EmPIt-h7w_hioO38zGCXBc01ew3ndPzXJCYuOVRUwX_64cwMnbVXTjRwpmY6dtYI5zHkCYnQPg3nIWfNnuRlI_6nLpE_j-VQ_1lWaEQSPSnG8n1twrHAOndOTKIcUknHMY3g8zmDNOtIH2IkXPq5EotPIRgGuZWLyAdaaFefdPmwgP1uSSBA-IK7asN9sMCmIEqi7rOxvBFmpeoZKjZ_5DfPnA8phfGjPgEZ8X-jGtwWIqBZlEkBwp3fxXJJL1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOKaH9i_EuEfW7SfElGVT2uotHxku7Lsd4Ikpxu29Zv5i_H8cgRuiN8VejqG5677lX3PCaCrEv6gI4DA8RYyosx4fui4FFLFxduKNpSqR-eoHzt3FdbawdmJfvW3kEatYjLag1pfjWyjvhqxP_CGYkdG5ew2hpmmSkQ9vQq3tnKiBU4j2LuESO4Qkqp52SfzWtGyzLPDMyWXOMukEl9An9zaT_rfVRp-TpZznrN-DD3JfFBb7UKnD0djryTsSfDNCzxCe6fQveNha_bNmhd2lDOvBIyZ-dTvdDL8huD6WDNB3sm7MTpojbRwKxr88eJ0S9zTs6LOUN-66hBl1zoT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=raFjwMK-urpGr8DOZF1ua8EemuV4QbwTTMcjIp9DFyXj7jb6HiGmKGOl7Z4x5VQzswJ2fGSdqI94lMXfxTWPdRFrvw66VGQwzdZiZ_7a81-mxfj7moF-2J6BL-LPtgGwGpSkQD1qL9RhKImhy18ZI8E111Mae6-wUzydC30I-b-H7LmWXgo_WrdNJQymUZ08xZJcVBbHek30k1zJvpi6HTZpvmYstiofXPXD1Pz4CmauvOOD01orshCmwFru-1l3ckcdZ6y16WenVfkbMiNvkIsNFvnCZu0wajPEKHJZ95TUq4Ry_sZ7VdCSjNO5MAfBUImYG3JlhtYAIpt04Dia6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=raFjwMK-urpGr8DOZF1ua8EemuV4QbwTTMcjIp9DFyXj7jb6HiGmKGOl7Z4x5VQzswJ2fGSdqI94lMXfxTWPdRFrvw66VGQwzdZiZ_7a81-mxfj7moF-2J6BL-LPtgGwGpSkQD1qL9RhKImhy18ZI8E111Mae6-wUzydC30I-b-H7LmWXgo_WrdNJQymUZ08xZJcVBbHek30k1zJvpi6HTZpvmYstiofXPXD1Pz4CmauvOOD01orshCmwFru-1l3ckcdZ6y16WenVfkbMiNvkIsNFvnCZu0wajPEKHJZ95TUq4Ry_sZ7VdCSjNO5MAfBUImYG3JlhtYAIpt04Dia6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=uf2xtxfOxlg-Uf4EStcPQzzPGRdfs5svHvdEwLH3369eycbV2IecwiT3-_Kj1rhWGWsjl2ANYGLGhf0gBGshturr4pZgW32ZRs3ZIkNtHD6NHJC4ndwNaAtbTqTgYpY9M9gZnlyNxCog0xyxA1NLA_DdVsGEVzbrg_4iImmnDSjxyDD7bWygneqeZCaFiEfjTIPyzFAZY75IsCvzcaWAf9FH4gFNwBC8ipFpglZ1XTuVxDE6LM7jW7q3e3Q4rR0Xv0sBqe3cZxp8TIXu4ea8qeRZTaJpzPfAIHzaD7nlcmQB7EJ3EK7adTI3NRSEXRsBajT39jZrAEHzXPkIzu2smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=uf2xtxfOxlg-Uf4EStcPQzzPGRdfs5svHvdEwLH3369eycbV2IecwiT3-_Kj1rhWGWsjl2ANYGLGhf0gBGshturr4pZgW32ZRs3ZIkNtHD6NHJC4ndwNaAtbTqTgYpY9M9gZnlyNxCog0xyxA1NLA_DdVsGEVzbrg_4iImmnDSjxyDD7bWygneqeZCaFiEfjTIPyzFAZY75IsCvzcaWAf9FH4gFNwBC8ipFpglZ1XTuVxDE6LM7jW7q3e3Q4rR0Xv0sBqe3cZxp8TIXu4ea8qeRZTaJpzPfAIHzaD7nlcmQB7EJ3EK7adTI3NRSEXRsBajT39jZrAEHzXPkIzu2smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=Aa6CXFn2llWQLbBjEU3XejFxA97j3t-zrYVqHxFTqjN5oGB14NltjN37x7YEX5qs4PxegDHKHzfWHOkL8FtJmbU1emJATbTfCoUP8WeBbfl8g2s2tW138CrzS8gaeoPJwCx2mvBBN3PBZfhzrveZh5jDnwWU5ze_n2vL8HUkqzWF5y7I9_qsyfCCk3n8xOLrUjzWyJNXF4wPrPXzRD7Qui1BQAXHfy9l5uXuc-ll-edmAJi-eH4T2s99nD-qN3fnKwT2zw47Pl2MIu7QNXTPrThPwHYU_Ua_6AV6i2cWovXwiK8b6CccidWLwOPEd55fmipPJ2XLCFr8XQesVatdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=Aa6CXFn2llWQLbBjEU3XejFxA97j3t-zrYVqHxFTqjN5oGB14NltjN37x7YEX5qs4PxegDHKHzfWHOkL8FtJmbU1emJATbTfCoUP8WeBbfl8g2s2tW138CrzS8gaeoPJwCx2mvBBN3PBZfhzrveZh5jDnwWU5ze_n2vL8HUkqzWF5y7I9_qsyfCCk3n8xOLrUjzWyJNXF4wPrPXzRD7Qui1BQAXHfy9l5uXuc-ll-edmAJi-eH4T2s99nD-qN3fnKwT2zw47Pl2MIu7QNXTPrThPwHYU_Ua_6AV6i2cWovXwiK8b6CccidWLwOPEd55fmipPJ2XLCFr8XQesVatdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=UKcFQyY_RthcqL4Nk9kYaGeirOT9P5dHPQMrSHhfDNbdlsaE2bFkrOnALcMI5IovM1pl2Mhf1_B2hhcU5G6G8pwVYEhwB5gRvlS4_UfHtVv7nylrGj6UZUT-D2sOFoc9hSmMBOJ2nC9k0SzCH_Wp87sRTYtWRGEB486iCVa_x3xuBey9xPb56KEkjdgGknlXKNV8ZDiLZZ2uEs8-Y4NTcy2fN-OBHjRiOaVjYkv0eScltmGk1GFvut2--m87G-46hNjA7wwI2ydPG6hQ15q5rVwqaVGcVY7yk--48nr2B5ZCAqQwogdjAhGPNzFQQmmZFJshUTCYnyxprcl9HTGh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=UKcFQyY_RthcqL4Nk9kYaGeirOT9P5dHPQMrSHhfDNbdlsaE2bFkrOnALcMI5IovM1pl2Mhf1_B2hhcU5G6G8pwVYEhwB5gRvlS4_UfHtVv7nylrGj6UZUT-D2sOFoc9hSmMBOJ2nC9k0SzCH_Wp87sRTYtWRGEB486iCVa_x3xuBey9xPb56KEkjdgGknlXKNV8ZDiLZZ2uEs8-Y4NTcy2fN-OBHjRiOaVjYkv0eScltmGk1GFvut2--m87G-46hNjA7wwI2ydPG6hQ15q5rVwqaVGcVY7yk--48nr2B5ZCAqQwogdjAhGPNzFQQmmZFJshUTCYnyxprcl9HTGh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JmN1gM_j9_lTdfP64kzMSJ41j9VbUnbF3yuN-UrUcnMRo8Pf3a7u9E-Lp9Dmq_XW9bd8LpyWgmc6LD5aKE7pAj7sH_OhjGurlsbfG1yjquwo1sdb7WYHyVeIWn9o1LU8ZAEQ88lseZHaCcI2S9lSwB2u4AL_SEZ-z8_XWpLPFPWJyRhoee00EyW9DcDoobuyISp2Q7TeI3UU0B30Vy1rTJ6F6JjnZgDmYaKUxaWhgPi4O6y5WFwqOdFBqzwW2SCMA_j19XKubSorUeVZj0J9eA2CjNoxWgGhdVjKqhdUTjpLWyfJ1oK1_3S3IjzLVJwiSKrDxlUTN0M_5lAqrnm5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQpcdikVnyHY10ZWUHvjtF2g0abs0Uu5oRedCklOK0V5AGOyltXUrqKlLlgfIGYD8CMPoImQzMmyf7wCOqksNelKBgENVupQXmBZb2VykmZ3r-XTOZaAxWd2uJ0EIBthFW_jW4SNLDeTkBp3XFwdT3RWLTsskBEc5nvHk0MfejPz0wTttLax1lyHgshj_AHvLDzYG94HzL2b2zf4smlKCBvXOUdtjE52QcF5LoQlUeA0-Ew9fodoCf0d1aSH98TAuTEh0BjWEyNwVqR0LYpZQSHcwNtP4FkGqPhm5OqZrABgD9Xn6Z9WuUVqICFVz_zmiFvg886GGjpspX7pPhSppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vogOnL6vGvMQCFzQRFKEOfolTQ3wW2quOHtyyprG0k6QDy-2wskSXJIzrXo_aqim9Z9ciU8UmkwmdXMOnduwdIgSPOQAdP_ix61BEjcq0yApX2zzgArNRtRpAR3M5AM-noWZXs8rGPQ7ZXdLS54bTOhuwfdXlmrFgcj5btEdLfjd9K6hCv4PgovzzUTX4JqbybViDI8pYSFIv_64IYAfnH1X97ojE9p9Qyn6t7wV2tLpDaZ8frXTa_lDA4iwZU4TnVIdr-r4iHAD-3KxGTciIB9UFVAfJ-fQXRy2T02lwfZSC8hzviyG2AJEEqu7yfMmnpwHPtecb3j-FeEyRSt8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=GVLHoklCXcMZ5ovIWsv_HgGJZspGBqYJno7hQcsOuCXxIKQjC0eCGwED-0sNFvmeGPXLMlB3XQtqVC-NWcTisZbVq1TsuZ2rMbOUh7PxT-HA7g4zX-LYeMUfsrQDzEo_jp75bLfiSjTF7mSUPwG0CQzHK16zy3qJ99Xd9QqPb1Ze21wlnWZBR1gtvbg-_9LfAx_yUtMR2BDs2m_dRnMQK-p403ZJ1zEgLY75v-FY5bAmq1F3KgEAkEVR_Sjx54HGM8p9vjDWqjQ-_B9jRTCn85ORh2Tmyrd5ALR-_45EScXndtwieS0TvExhCno5F4g7drZbRclPxPe3KhUMzhEgxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=GVLHoklCXcMZ5ovIWsv_HgGJZspGBqYJno7hQcsOuCXxIKQjC0eCGwED-0sNFvmeGPXLMlB3XQtqVC-NWcTisZbVq1TsuZ2rMbOUh7PxT-HA7g4zX-LYeMUfsrQDzEo_jp75bLfiSjTF7mSUPwG0CQzHK16zy3qJ99Xd9QqPb1Ze21wlnWZBR1gtvbg-_9LfAx_yUtMR2BDs2m_dRnMQK-p403ZJ1zEgLY75v-FY5bAmq1F3KgEAkEVR_Sjx54HGM8p9vjDWqjQ-_B9jRTCn85ORh2Tmyrd5ALR-_45EScXndtwieS0TvExhCno5F4g7drZbRclPxPe3KhUMzhEgxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzeUU2RcbDZLg1BSr03A0DT9EnKXvFhr1EJuUqNMoILYlYJBySUeVb4vqmw0axRgYTwaMxvDzMgW5usa0Jk_kALs5lzxkRStXnhVJbQTwhBYlodbMiQaK-klxnfSe8taIeaSum7DjYBafPHHLr_1uMxQPDFBYAusAQ0cURL7UMnSVHsFSn1r8JVFCX1y4W711F1Hjzbf_2tfcsiQnftE2IjFhBdwTesv2XuYgFGB_JoXyBhWvXb50QhmOmu2Y5tDEj0Xt3UByAxfge2QNFeeb2YLAMMxYn5jFGTR2R6f0GapyQ-hDG8Rz7qxQGDaFBqdaETZvOW2TQHY4s75-hEatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=n89IoOqdV9otfA6bQS3Xdsu7Jk9swDEaSmSF6YJ2S7uouRWONb2-ZLjFfOSBfSzxwpwwuMSXO4MoQPq77YRT4gMeF5Bz-zgaT4uXboO_MNRa_tVt8zALdvv9OsC2pbNx2XfzP548bJOnhrAT1HwcOqL_LxRvVcQyBxarMfFEmBX1W75FkYI0dr1kxZLqo-F-_gT57SerjWljXMD7jiKZbVOIrdtXIqobA5pNrmbbiPSbUisz6A234K4sBq9Iir79XdA53Aml2kcoFOt3i75VUO54x_Rj9gGDVNtQ_63wZWlBEDML5t_t5DDaxLHnR2D1jrNkHsgr3dtvMsXkoFfW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=n89IoOqdV9otfA6bQS3Xdsu7Jk9swDEaSmSF6YJ2S7uouRWONb2-ZLjFfOSBfSzxwpwwuMSXO4MoQPq77YRT4gMeF5Bz-zgaT4uXboO_MNRa_tVt8zALdvv9OsC2pbNx2XfzP548bJOnhrAT1HwcOqL_LxRvVcQyBxarMfFEmBX1W75FkYI0dr1kxZLqo-F-_gT57SerjWljXMD7jiKZbVOIrdtXIqobA5pNrmbbiPSbUisz6A234K4sBq9Iir79XdA53Aml2kcoFOt3i75VUO54x_Rj9gGDVNtQ_63wZWlBEDML5t_t5DDaxLHnR2D1jrNkHsgr3dtvMsXkoFfW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=EH3nfcHh2-M47nrb9wTa94hnImDPp-0vbg93q97782QHqW_wP3sKkw2O9VTZ9vqQEsO9VAc2z16LHE8h1hZg0j82ywDWWqsYOR5NWjBBpmwMjmy50X5RqYzYfNd2Vbtk85_pjF1_-3kIyki5wVQq0o0F8x9zQX5f4Y6lG1pjjvr0LmHZhyYV2sbd52nSrESBVbS1tSS5BOHcG63CImiH36A4up2VPSW_Z0mHHSYn-hf9uUkVIJAMo6PLTZra6AmLmW-MDiHi1UM-_0ZALeWlS1-ANbXMYvobjFcuUpT1DYawsEpFW3amtFosrdulbPbQUMxWRZXBY4oiwAhWyobdhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=EH3nfcHh2-M47nrb9wTa94hnImDPp-0vbg93q97782QHqW_wP3sKkw2O9VTZ9vqQEsO9VAc2z16LHE8h1hZg0j82ywDWWqsYOR5NWjBBpmwMjmy50X5RqYzYfNd2Vbtk85_pjF1_-3kIyki5wVQq0o0F8x9zQX5f4Y6lG1pjjvr0LmHZhyYV2sbd52nSrESBVbS1tSS5BOHcG63CImiH36A4up2VPSW_Z0mHHSYn-hf9uUkVIJAMo6PLTZra6AmLmW-MDiHi1UM-_0ZALeWlS1-ANbXMYvobjFcuUpT1DYawsEpFW3amtFosrdulbPbQUMxWRZXBY4oiwAhWyobdhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=vdry0pVWOOckUvCwlrjKtrYMF2PpZyfiZi2Ez_Qju5m5TiEfP0NS0gFRvaIVs-2iMvgJEkjoMoR81lK2efq_5ujDKVKWYHHFCAQ9hOVUwyReuy8gcfSsmVxTvd2xv25rZn5Lf3l94AqvjG9xHXKtpf83KTMYeEZTkrVMIS-W0x99FJmN5voTNK8YJ2268d1nmh8eurRkfPQsG-C25lemGoZkKMKUzmU_Nm0h_8xkUCWoQznoEppLSXIVi4uSaRjKaZ_8kCvi-Qxee6sej_bmKlnqNKywwbyL6NfkPDEHiW8lvbUlHRozb9sX72jrlwcijSuh26cbXFqBujBK9auUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=vdry0pVWOOckUvCwlrjKtrYMF2PpZyfiZi2Ez_Qju5m5TiEfP0NS0gFRvaIVs-2iMvgJEkjoMoR81lK2efq_5ujDKVKWYHHFCAQ9hOVUwyReuy8gcfSsmVxTvd2xv25rZn5Lf3l94AqvjG9xHXKtpf83KTMYeEZTkrVMIS-W0x99FJmN5voTNK8YJ2268d1nmh8eurRkfPQsG-C25lemGoZkKMKUzmU_Nm0h_8xkUCWoQznoEppLSXIVi4uSaRjKaZ_8kCvi-Qxee6sej_bmKlnqNKywwbyL6NfkPDEHiW8lvbUlHRozb9sX72jrlwcijSuh26cbXFqBujBK9auUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soOBse3Z0yFzI5A5vlzH8qkBat5T5Sh8FHhgZ_f8cS8adb9YiDPg3nSOWDGRMCq71ap_RvNnJgA0J48kLVzmuvDlU4JZ50KSferFqdN_Pn07TeKNZCbIsfn5Q3rv4AP0TsJmM7MSSVLqPpYZVYJESxy9ft9noRTF686vrpiFNY0YXmgXfG5HAhiudK26eAh4hgROGTFiMFDLrX-Kz0J3Hs4XDbM2H-j-5ElJbOJCOn-rL4OOW045LDhJrEwhTAY5a3mYaYIC9g9nM9U4oGIyCtwLo4GTz5vDqRP-zjHPce-9LKM_l4EW49FgGO0ek03gX8WIa8V67LHgrkSGEcY6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=j8zNTdocte83tDhJCs0gaAprJawluntQOiHTjN87naGwTR1A_pjZVReGT3CFMk1lKf5KTALT1SrRyyJfOzfhJ1fFjdKdT1d4Csu4DmqT1sHrGKOrBdOK77EO9C1cQiOMWfIOa7utZbv3Eq1VTaT_PifFQzs8JiAduujKAyXV2YAHlWLxwGpqTOGeH50G5gjSRgCBoNHX6NSzF_o8qSxyaz1Dl7yrVZDxKycr6GIMGEfKFzCKQBtoh7NmkfxJkS7fSXBm-HhZ_4KJPO5yTf9864g7q3rdgm3bXvBY82SVGDgPno_Ogba9od8D0uetQsKvIq-8D7GItNkiT6VoVTySgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=j8zNTdocte83tDhJCs0gaAprJawluntQOiHTjN87naGwTR1A_pjZVReGT3CFMk1lKf5KTALT1SrRyyJfOzfhJ1fFjdKdT1d4Csu4DmqT1sHrGKOrBdOK77EO9C1cQiOMWfIOa7utZbv3Eq1VTaT_PifFQzs8JiAduujKAyXV2YAHlWLxwGpqTOGeH50G5gjSRgCBoNHX6NSzF_o8qSxyaz1Dl7yrVZDxKycr6GIMGEfKFzCKQBtoh7NmkfxJkS7fSXBm-HhZ_4KJPO5yTf9864g7q3rdgm3bXvBY82SVGDgPno_Ogba9od8D0uetQsKvIq-8D7GItNkiT6VoVTySgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSas_1wIcmhyaxLcvC9MvwEjTuMhbdgGpJt7mAZ6tub6CT8JSeEWy9iQ1tnDSZFtrA8iG0wTAR3YCy4Y1j7DCH0reyfFjMXs4lKy8V0GvYyvZs9fMun6YFOI5VclNetWsvpk2o625YU-GTXQmtR6tvQjsrpZRD2eki_sMq4wuBow4wl17l1sffUpV2Ttp6aF_GBQsl-O20fvlOmwcNPaucyeAfzezxBr6_f1bQvd4w5AFhr7JwISu32MiuQOAKzy0LjPZ2O9o-JLtsn5hKqiuyIXepP68UBRqwES4t5wxDSry94b9NQn-kpMxw3oIUnmRUVJlvp7RorHD9HQ0qPWwFzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSas_1wIcmhyaxLcvC9MvwEjTuMhbdgGpJt7mAZ6tub6CT8JSeEWy9iQ1tnDSZFtrA8iG0wTAR3YCy4Y1j7DCH0reyfFjMXs4lKy8V0GvYyvZs9fMun6YFOI5VclNetWsvpk2o625YU-GTXQmtR6tvQjsrpZRD2eki_sMq4wuBow4wl17l1sffUpV2Ttp6aF_GBQsl-O20fvlOmwcNPaucyeAfzezxBr6_f1bQvd4w5AFhr7JwISu32MiuQOAKzy0LjPZ2O9o-JLtsn5hKqiuyIXepP68UBRqwES4t5wxDSry94b9NQn-kpMxw3oIUnmRUVJlvp7RorHD9HQ0qPWwFzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm8WnsTrisiYkmRWZbh47oCN4b6HiBDO0BjJUkHxFTtAR94EuuM1lCluEyRzpbUuibbIldfMUUxwIaTDW4yf-B0oTL9b45k72dX4mT7BYvEtEYUrhsNlICfvEYmC4wCKlINaPmO2IoWjE-pTJ5gjVybpkHHYydGnHZMxFY5eDW6kUwr4rv7Dj-h7WQtwEW0D7CDd3va2_GHgniZWyhaWIq3hlJ_7A7z0wSC3qMF0OwgNirHGqrFaqv-hMb-3ImRDzNTUKrth8hrbDsb5dx_w-yHmTJFl72ia9TfuE-AQdsRodvXCPe8YfYMOF_SwK_Nfo1LSlH72TiE7S3FnYb8MAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=AMWAhXzpd1yLW6VTG_eS2N4-1TbL-sa3QqNBeOvyuwlLvbs9PLnK3DbqKQbOys4KKPTSTEtwptZjSUnNkWquqsQU_tZI5peKvZ1QO0iCMmPMllEs--x48ST2AxcmfdINQOQzBR4DU7f9VqN_zmQ3nTHj344MHqdegRmIXhnbwI5HWhyQP8Rs4Ui0k8W6PZWDXekps0VSvXXqpspe_wjcCLJdZB2NwdhFNALSTMSFL2J-0RsotFQrOMXhLXNVfLqkdOPZQL1nNkiXqnMxlLKLwDP9sp695O29HaSUjOvvmZYfIqrgq35JhabU-GriG9eG4evCJbgSJIBBHKS14lOMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=AMWAhXzpd1yLW6VTG_eS2N4-1TbL-sa3QqNBeOvyuwlLvbs9PLnK3DbqKQbOys4KKPTSTEtwptZjSUnNkWquqsQU_tZI5peKvZ1QO0iCMmPMllEs--x48ST2AxcmfdINQOQzBR4DU7f9VqN_zmQ3nTHj344MHqdegRmIXhnbwI5HWhyQP8Rs4Ui0k8W6PZWDXekps0VSvXXqpspe_wjcCLJdZB2NwdhFNALSTMSFL2J-0RsotFQrOMXhLXNVfLqkdOPZQL1nNkiXqnMxlLKLwDP9sp695O29HaSUjOvvmZYfIqrgq35JhabU-GriG9eG4evCJbgSJIBBHKS14lOMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6aD4E-ZakLy9vsoImSdwYf2LSXf_uwg9QnOkeWN6iWOesT8FqBL-G4mgU9EeeR2kY8NVkk1pnXxFz0pM8q-b1LdCnYI4JKjek_G8zjJZMgZfFLrR0wSXU8YApm6FtdV6u3e-jjLwOGDCeUj2bxyb7vZXIlB-ICv-cPAWiacyR1SYw0EfBhkCFFJmTgtDzDbIUImVMZAry_b2e8EyoowLWWXHY-AqWgP3kpaycQLK9m1ynBHh2zrkmmEk7tdmdBcL_LGSQoDij3A9FuXlT0GSSGmGgQ-F2DuNAGZEzuZ7IW9yZ4DsifJ2MSoe4q5BlcTYnoE4Djd0SAhhHoZYnc1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=gBMBsXH6CWDdATEfy9Nci-Z5VM_dmuAT74THTECrOH2YKWnOpArWwh58hiQ3z84JfjxXbjULMEbVKPtFPyAcu2Fukdb4XxRJbLRv_FRfNWWYCXe3y5C2jdilBei0Zbt7whipyKMl7pbnJfp9NT78dQb4KbgQvTgGSjzvyrVRzYGvgxMAt6ZZMssCb9iCN83u2vLjEPTM8aByl6_7_tQGm0XwYqsm5SqikoNQKWodUKaGbI_yBhVzSq8wS-mecdOArhWBqt0e_PlmaMpTnfIcT7UUcr9QDACQdfVvIP_RPCdR0T0wEPwloBqXj1NZLKepcJpIshN5UGN4Cu5OeKKVJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=gBMBsXH6CWDdATEfy9Nci-Z5VM_dmuAT74THTECrOH2YKWnOpArWwh58hiQ3z84JfjxXbjULMEbVKPtFPyAcu2Fukdb4XxRJbLRv_FRfNWWYCXe3y5C2jdilBei0Zbt7whipyKMl7pbnJfp9NT78dQb4KbgQvTgGSjzvyrVRzYGvgxMAt6ZZMssCb9iCN83u2vLjEPTM8aByl6_7_tQGm0XwYqsm5SqikoNQKWodUKaGbI_yBhVzSq8wS-mecdOArhWBqt0e_PlmaMpTnfIcT7UUcr9QDACQdfVvIP_RPCdR0T0wEPwloBqXj1NZLKepcJpIshN5UGN4Cu5OeKKVJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=VJ8Mt5A4gpWMh6cFrMJj3nUtesg8LDpiGvvi15EEOWKk-RIwogHQihAAEtWj74zNW3DlJO95J0HqWlK3z42hxUzA885_P-ldOJ0ZdAvoOe9LwDe-pXSSX_1HNOAwUPiNgZasfaunPNzmBnNN6eSi0X8RbyZxC6swQGGnRxbplcLbjfcHqw3yj31MVXovRTIrWOFhkZa5DgQVlvpMAljt48CK206nWfggkMa0pP4NehGfgGEAtXMz_1Ddu53qpTPTMLrQ-r8A7bVQjekYl0QMLF9hCSlicFWjiYwdMR4lb56H_QQbVpdJtKxT0kFYv8OaQutvDYDKXYhuCTf28XOVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=VJ8Mt5A4gpWMh6cFrMJj3nUtesg8LDpiGvvi15EEOWKk-RIwogHQihAAEtWj74zNW3DlJO95J0HqWlK3z42hxUzA885_P-ldOJ0ZdAvoOe9LwDe-pXSSX_1HNOAwUPiNgZasfaunPNzmBnNN6eSi0X8RbyZxC6swQGGnRxbplcLbjfcHqw3yj31MVXovRTIrWOFhkZa5DgQVlvpMAljt48CK206nWfggkMa0pP4NehGfgGEAtXMz_1Ddu53qpTPTMLrQ-r8A7bVQjekYl0QMLF9hCSlicFWjiYwdMR4lb56H_QQbVpdJtKxT0kFYv8OaQutvDYDKXYhuCTf28XOVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=TW-TT-iUokXdbTc0FBFn5ha__L0dh3L89be57F2YVHeC7N_XXWqjzEPJbeJoGUCBS4qBdZSd-mB7ygWikWJjQv6WfIqEIBV7NfBzYZlaSEQvrzVbVCOCaKaszTHHYFQBkx9s9kUFYL3V0ZvgOfnMV12-EA9hjmpotcI1sUVBpkbV8C8JB3YbchY9fsXt6DgjjBNVnIqEe21EWSTr1SqF65FhCNivi14aOKv1hhfiMGIOGwINRVyRkVLgyVZgmH8DqikOyI27HK23sLSgvmA3QnSQc04sQmXol2akCPPK1HjBbY74LT1VOi37lpaXp01EIKP9ecJkyDzu_LrganSNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=TW-TT-iUokXdbTc0FBFn5ha__L0dh3L89be57F2YVHeC7N_XXWqjzEPJbeJoGUCBS4qBdZSd-mB7ygWikWJjQv6WfIqEIBV7NfBzYZlaSEQvrzVbVCOCaKaszTHHYFQBkx9s9kUFYL3V0ZvgOfnMV12-EA9hjmpotcI1sUVBpkbV8C8JB3YbchY9fsXt6DgjjBNVnIqEe21EWSTr1SqF65FhCNivi14aOKv1hhfiMGIOGwINRVyRkVLgyVZgmH8DqikOyI27HK23sLSgvmA3QnSQc04sQmXol2akCPPK1HjBbY74LT1VOi37lpaXp01EIKP9ecJkyDzu_LrganSNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=VHOCS4k3CZqILioZRgtPqbKyNfvKRgTPt-9DYtvhjUrXXi4n_rDuKC_Ia0PA_YNnJZVKetLk25irJVUmUPCqhzftQezKvDgDYktgIYGRz_xUzgcgWIPGOJ5Ch9pyyb7pQxzPshIgxr4sXgNA7xfT4FH6a2VmvwZTR0n8kNfz608KrGdkAv3A7N5pjm4YQ-3mNyx34vnj31PWjabosGOEWU6rXRfzS2_l0qVX4WDdYAY1riJd-49NoHpbJwWLsBVBNbTc0fSgZQLph7AtpIcJZD1LuBEutUp5x-GWz4CloyRRikyeAlrBNo1sOEz2hSBu4m_OAl9TEbDfM2M9ROWLlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=VHOCS4k3CZqILioZRgtPqbKyNfvKRgTPt-9DYtvhjUrXXi4n_rDuKC_Ia0PA_YNnJZVKetLk25irJVUmUPCqhzftQezKvDgDYktgIYGRz_xUzgcgWIPGOJ5Ch9pyyb7pQxzPshIgxr4sXgNA7xfT4FH6a2VmvwZTR0n8kNfz608KrGdkAv3A7N5pjm4YQ-3mNyx34vnj31PWjabosGOEWU6rXRfzS2_l0qVX4WDdYAY1riJd-49NoHpbJwWLsBVBNbTc0fSgZQLph7AtpIcJZD1LuBEutUp5x-GWz4CloyRRikyeAlrBNo1sOEz2hSBu4m_OAl9TEbDfM2M9ROWLlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=JH_nmv06rU4RcnBTl5m2_9iQ9yIXGbs114fXgRPLIne9_Atywo5ExJVB0zSvYCtTtKVtndD2mkeqelltEfQcKHst0LTW4BXxR8ngROjHFsPt-mcJR9I8weIX-vcN6pczyHbnwTkWtW0TggRMan7sTKI9ROCMGaNVvZejiDYGagXhG9vdwkjnfEKK1Cu3rNOcPCU_Bg4qqsE-cZiqjzNRTziFwJ9PGvdQzOUAXIQLkfoIHz69gutzeXxFK7hsCuNCxRgRpaQa_zZhjFfSWKkstijvUEdea3A77fkmJnXWQwNyOpi6eqNuHWnZ9I_-4QleK-X_R2KkwKCGTTE1a3Fq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=JH_nmv06rU4RcnBTl5m2_9iQ9yIXGbs114fXgRPLIne9_Atywo5ExJVB0zSvYCtTtKVtndD2mkeqelltEfQcKHst0LTW4BXxR8ngROjHFsPt-mcJR9I8weIX-vcN6pczyHbnwTkWtW0TggRMan7sTKI9ROCMGaNVvZejiDYGagXhG9vdwkjnfEKK1Cu3rNOcPCU_Bg4qqsE-cZiqjzNRTziFwJ9PGvdQzOUAXIQLkfoIHz69gutzeXxFK7hsCuNCxRgRpaQa_zZhjFfSWKkstijvUEdea3A77fkmJnXWQwNyOpi6eqNuHWnZ9I_-4QleK-X_R2KkwKCGTTE1a3Fq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=gWhjua2KugLyuAdCEgbBskDADU-UWd_y27bCp02JtNnOz6_Voi8YakE3VqueTk58_MlBIl_xbL--PmnBODKVXGhdi-dSdJh3q9SyofhhZGzibrKNBAXPC7TuERi8r8oENGLbzPjaUcBTSUBhV_Xw2booy40lC-GC3uGZNz88a00mes_sIXPFAeYiJ7LecXRQA2vqSI-v2JQLtRs2vqoFnaIt6bJSZtAkjNcxXbgyhx5pZKmeMHfqMkfADqWNVIueW1K8JvU6TG7tDciUzfoQaUoQJ8vSYl-EAwOmRxQ1KhtfQF4loYmGOWRrM85byPf7C0uGQVSykkc2-C4yf6Jcww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=gWhjua2KugLyuAdCEgbBskDADU-UWd_y27bCp02JtNnOz6_Voi8YakE3VqueTk58_MlBIl_xbL--PmnBODKVXGhdi-dSdJh3q9SyofhhZGzibrKNBAXPC7TuERi8r8oENGLbzPjaUcBTSUBhV_Xw2booy40lC-GC3uGZNz88a00mes_sIXPFAeYiJ7LecXRQA2vqSI-v2JQLtRs2vqoFnaIt6bJSZtAkjNcxXbgyhx5pZKmeMHfqMkfADqWNVIueW1K8JvU6TG7tDciUzfoQaUoQJ8vSYl-EAwOmRxQ1KhtfQF4loYmGOWRrM85byPf7C0uGQVSykkc2-C4yf6Jcww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=G5IjOhh5cgJhFOGPb8UR7ROCoRyjKMZ71lKT_tIa7dkx-9zEQ5y1-Pmo6ln-sn4eIryPmqUR9c4pxGnzcn9JXp_u-r4c8274WwAW-H2afhLe-XkExvVPeFMbz2M1jul5N7SdztHgq0dW9hDnuLg-wHBsP5TGWMsDZXQpQYmysBtV4niPV_wdDX6pDpBRQBP4PjfkRBy6P1g4ZA3fpdbKz-hVBoyYs_bx-ID2u7QvC55MZN2fEgdxPuJPvZkodbOLkvRl3kZB5dYxTE_cabWWpWeO0vvWKDIW9t2EOxE92NlTpeNEmb8elESCJ7QJYgZO8fZzqsTTkanZjo6jEBWEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=G5IjOhh5cgJhFOGPb8UR7ROCoRyjKMZ71lKT_tIa7dkx-9zEQ5y1-Pmo6ln-sn4eIryPmqUR9c4pxGnzcn9JXp_u-r4c8274WwAW-H2afhLe-XkExvVPeFMbz2M1jul5N7SdztHgq0dW9hDnuLg-wHBsP5TGWMsDZXQpQYmysBtV4niPV_wdDX6pDpBRQBP4PjfkRBy6P1g4ZA3fpdbKz-hVBoyYs_bx-ID2u7QvC55MZN2fEgdxPuJPvZkodbOLkvRl3kZB5dYxTE_cabWWpWeO0vvWKDIW9t2EOxE92NlTpeNEmb8elESCJ7QJYgZO8fZzqsTTkanZjo6jEBWEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX6X5eRXYY3mkspdLQ9Nno18lkMLJ0RdDdwraLNXe8EYz4aiFYLVJTB7oNLbaJLZtMdSMh_LN-beJA6s9lpcijfTFZ4kbbZj7Cpj-qLSoGNkJhymfLugPnbg4Y-hIA4-Nbd7bpPTHAQlR9pvu-8ydd-tfEjLMQpaAeJzd8WfDG89YO5H6qBTFHrk6KhUkv7fJ6PLJii50gDsNCH2VjK7FQt5BQMtC3hF8F6cQ93WlJaAHY6A12Lx9CNLsy_e5UciEshxWGv5Ee3n_m-dencJg1AwPzGzWAyVt6zpVWQcTAH9ywn2TObLraBrvSTztCdh1uTegNwwHOxCAz_A0DFQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyxWhFwQ0hd8XQqbs8y87J8nlSBhzo_qH2u2bN0A0-XawcMNAfBPdTn_T9cCsTHs5V6TH70waH84c0alSJfAQm1g0EALJNb-8aEH6MaVVnzJOfMhPFzjhTMLBUoiZ2vj9e17ics_zjA108X51Q1hIAtYtJJNqMtc7ga2xsZH2XrPQnl1YYnJ4of4nIwofL07EHrmvAyHEx7y-V89MJ5tT2I3HYIMMCK2OEx7mSAZ-iBePViS3KtB3uQFDzdfVJjeBW6BkfEg51XNjdXiDsZQ7-X9H2Vvsshw00f58JqYxCCwoYhvuvMothEBT8MxaKkCj5gu1H4_ZS4RLiDmR0XKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsJE1rWzl8mIlXgDz8-nhCHK3ZCuOMtw8W_JhetpZsjMrUWNEudKH0bbfPFnBiBrIdDcd98F-GKVK0q9n7ivUdzwBbBHOArrAHZMvE69-6BlJp8mR48F9sbXuk_ZA27sid1vcPf6VtCabRk-TvvLgB0d3jcDVJeMUlO_DiUVgV97pWQmrXn2gg3jCpEjQ3TPMvp31tW9WLlv6ZAWLtPsZj42ksyG5fep9vH-njYr6z5ls-tg6JJCI7HchzTTTCzNMCp8yaqvS_rptUqkir2TeR6pGCm8X54fhl2M-GAHDRymxZaJb4HLQCUpyNe3xyKQ5pv-bgolNVMsI0r_QMGZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=QHAqU_Dz_0stXmEKpWez-1IYrHFyxYj0Jv4Yp7VeuOOk3EAyu6x7_1FXrdr3ai9u0iOcT9jj-mqVAWRYf79vwkhW4jyTW_gI8uIbBgOY6EHTumjYYzfLm9_T2MTbJoGcmc95DSjnCEugW2DZ56u-K-5-Ju7rbw7dULe36VgI4QsdOWMcCH5XP50fNOdIrzt-q4P_CGVBLhziFfnNBcx5kbi6k7v4jD7l9bNWMMZWKU0fri-u3iuKm8y2S3hlC6tMRHj66VqX_pld2dE9AXK-YXRYpKUunfkSqNqN1G6IsehGSdDXJ2sOJP4CREgGU4myRQ9S3d_Ee1PbKmjkK1DyTgAdTfvSZOW0UVRaME-0Dz2xs3KyohHnnsuOBxBjtg7y2oS3g9W27-u_JE4PNPvAQ4cUucZzaPK0tJ_v_g9dMbvRglOAMiKMcy0CYVlfCVJygLr4I7zRTgppFrR1Jj9be8CdEvGm2DV35JCITlRxBRRS0DE_y9X5KZUAAwtxwUg2nVuRMIrLL-APa_FNYAwnztVUHh6_HO7bPRqj_P0kQCpfF5wTxmBnZGaaJhDfr4pgS8Esrn9hUcl06GM4eCFg_o34E-tiiOHBVmVqb6BdjcxOJFDLAko4ZxI3WUbWE7uIhuz3zoQ_NFEkPVrP4frmbp62uxandQwNTo_QjwOH0N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=QHAqU_Dz_0stXmEKpWez-1IYrHFyxYj0Jv4Yp7VeuOOk3EAyu6x7_1FXrdr3ai9u0iOcT9jj-mqVAWRYf79vwkhW4jyTW_gI8uIbBgOY6EHTumjYYzfLm9_T2MTbJoGcmc95DSjnCEugW2DZ56u-K-5-Ju7rbw7dULe36VgI4QsdOWMcCH5XP50fNOdIrzt-q4P_CGVBLhziFfnNBcx5kbi6k7v4jD7l9bNWMMZWKU0fri-u3iuKm8y2S3hlC6tMRHj66VqX_pld2dE9AXK-YXRYpKUunfkSqNqN1G6IsehGSdDXJ2sOJP4CREgGU4myRQ9S3d_Ee1PbKmjkK1DyTgAdTfvSZOW0UVRaME-0Dz2xs3KyohHnnsuOBxBjtg7y2oS3g9W27-u_JE4PNPvAQ4cUucZzaPK0tJ_v_g9dMbvRglOAMiKMcy0CYVlfCVJygLr4I7zRTgppFrR1Jj9be8CdEvGm2DV35JCITlRxBRRS0DE_y9X5KZUAAwtxwUg2nVuRMIrLL-APa_FNYAwnztVUHh6_HO7bPRqj_P0kQCpfF5wTxmBnZGaaJhDfr4pgS8Esrn9hUcl06GM4eCFg_o34E-tiiOHBVmVqb6BdjcxOJFDLAko4ZxI3WUbWE7uIhuz3zoQ_NFEkPVrP4frmbp62uxandQwNTo_QjwOH0N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4V29guzpFKEUWFO1hihItQEmaWfusCEY23lIRxEBgHmB8U-vXvXNSfxj1PbJVupv6_R_Oiypsg--v-ItWb9Y2AgqAR0pzgDcp_mSNDfG7ftuPdMtaKVlOnYseSX9JlxjRcdrpesL_3HzFFiH1c1mQ_0fjvDIzbScFPAVOphowK9zP6NHk85DW730zWhYh4yXLe0sg0YQQSVAkFVhOjudPPojf1rr0nlkHR9idy66yK-MlfjBsqza7_TMOHnMxvOah_R4FLZe6wL4KwFbeVei6xgaM99oO0L0c7tBE1Z14YDja_hVM_jM1JuxavNPzQbN4qweLbSbgoVGxztOC7rjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
