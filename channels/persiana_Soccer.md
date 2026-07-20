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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 23:45:45</div>
<hr>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nij57szZSS_wfrN3GmkLbdDEdcCxJNtBN3Qsa0Dis5mAufuaNk0btVC0zvc51JlW84r1XHvgg46iAJhsVVaao46jPXGWQf0RU81buuxbf7KYX4U2ULM29VbIPZoBNldBInBaq3VebPOalPqkihxI_G_pXNdd9IhHiaC-mAasIDrMdYpVoR2DIg9kijLdmavWLA_b595P6IROkLapmJ4C5OiNzBLOsimvSfNbpBQcsxSAE5JJK429rNFFnvkf01pAPPXBS2nfYG-EkuVcAd4EwRh9eJsHlGF6rBuhMGLOWfHkDMXGfzWJNUXUEZroN5bBVfJNXPhidxx5wO6tW_-2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1L9CQqfd4KKVxWto8gwiunoFcCfoVIHwwor-_7Iw_yQNN4ogCuRyUOTM3dgY6YdYW0BlJGT4cDXNAxNgPceCAjkZuxAaFbb8cyCD0gnWVvPeoVxYNC-jA0N67n9VA9HbaiKES2o6h0_yblnL5QglRNKld7YPSwaVfwP0o5kzl9G36ClslXvAFAq3j6Uo9f32RMBjQVPlrCO5sOnljG5eX2O2EO6iXVV0MCQqAb9NCYTBx4jlZyj9sgMLq5ja3eEqLQatw2HlcrVr7QUc6iAExP0nImGnNLQvFgpMDxG0o3PsGuvCxTpby6CGacVKih7j9Rruo-PN3xY-vktLaugpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT5wport7fUSbDG9z7r2y8C4IJ50wYHv9zgcFj4ty2cgHjpPIdzi0ggNtxW8IMFXEqGz8oZ83IdVAYLR439dV4-lVpDzqholPZN-wQV0svh3bNhOgI_kDuCyWrL20BW8IWQ1u27GbJa9ymW7us_X_R9vJ0F9nU11eMSdrPBGeXDfeliVpbnTbGaj6uni70SGc9OPdazAAhr2S7mDKk4Hz1E2wfFUaDIQUwlgeg4zoJhidqF2NNkS8-olefTpJizkk6x8KKQ-_WjI49SU555kPwGYguG74EPdBPK_Bf0QhkDGSgIRq2v1EWqy4_SqQXPMrbcbYtfGJ_aLfyrFpMETHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4HeFeBtzhQBAWW2mfKv5TM3hhhN_keeUPeN-z_8DBci-6O8CuVBK6CZnEJ0WUt6QBatQFVUP2Lrby7QBAG7kgxXbNXU3WClEzpL1InDb_xvXTmHZ3hiFEGtU-V91w6VrerA_DbWnSK1s3nPsV_DZ8P3DoEHSBISw5-wvAwxPqhjIDke-NAN3pGYWa18syEPBAIUezn2FoSZMMbhm-z6rMscIxBwPq6l1iXpKAraaKk4vd_SyraJyx77aUNGTrvsaGmj1WqHUrroM1PA0abvrD1K7RGphdcUYlhYU3CC--6CY2z2F79bYMmqb_yG4GVtuaf7pOy1_l00WZt67Td2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0MSqsHGFLHU3HWnJxrlC8LzXq22zgqVqZ_mNLGIWwSg3fYVo6gPC8fLyIIbc1qXzSsOinwPTMM8eYlWsuR46OL9cFyYXxLWzccUoP2rRm4XVKExUSahWNSY3NDq5SjnT-uG2PwoZ5QGKZK58ApH4oRRlEPTBzQ0vhj4xOq1UxneVaWcodZzdbOm4Pgh0L95DGyChGM8-dVoxtwtmkHNuqpbRLnKjamUIyW8DBQQfSnD45ui-7FDGq01_NJKTY-IDQYJvig5_JHLHoRnO5EsHLiShqZBnx22sKAq462woeysKArNAabl6Pbz-fQrreEfWo45d0TZ5ODhEKjBz62Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT39W1SulUzaD2SjX5TC3A0-NjJr3tfeOBhR28fc_m3oqknWIKn0lv38yfCrpAZQTiKntU5d5eTweUCPZHgkc8WzkjwYpqpwmEEzegsfpjbHWvPwL0SM80d5KVNc3AZDv11e68PTVsV3oknZUr-VthkFU5ClcKLEqglAn8NRY9LPVvrPh9nz0mXK5rjU5i5-RI1KLvt9F0M3tfHFL1ihrwW7YEO3aV4RwbZT0A2arieOs3o0PodkHapVHzpOLUWTy53oUModDmWfYuhWGDTRwP1PKt7zPFZWrjSmZVVv4iMMFwv-z-bjU7jsw6myHLpk5-22GrKtaD3L2FjZUyJrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVWwYtqce66Up02mZbMO8WwkhqOZwSd_3dUYKSLFFziRNMcCfYWWYYbCa5TFKc68HO1K3rI4FJpB8O4nX_-1A6gFyqHpMqf_8OHVm1n563sKdbnQIIeOBZ_sVHxkU8GT3TVLuskOP0GW6baVTETkyPzyiKsFHfeR86QbM_vSviY0CbG3vO7t82bMH3VkyCvb4eOV53qE1aA6700LBWt7d3Ih4y1HyMruqXXn1uqW--z2zmGmpk9nTNhCkUN7OYXvfv3q4vyBRXTZf63x0ij_iTweIFKqbD4KV2RcoAcFfGjwm1uqwoz5SqzbpWus9aOfudNOYSh6yXPaLhYrXw60dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klDhOm5M3ETINZbSyi9rFhaL9B4Y57NC4DhyHkW28b_YPPDfn_ZD2boQKv0DbikH4FZn6UMOH0rX-IZMidyoxmaefTQQmoMLpf23xLCvzRqgeo3JiyfvZ1Rrlz-BvzAGQyU8gKJkqO7gr7PJZajB7V0Y9WeJvJ_v-W4eVSb_7oF8vdfZYA7wetkdUazl_F1exelhoBxXj5d8wJGvLXteA0dE42AwkrOMaEVekj63g9Pb6ceJejRaOI5VqHhgdzo8eMxzFWZWtAyCRvUQPQhFWn_n4ZbZuwiymtKMM2F2sPXzrky7VZWlJnaCRWBJDhvP4xHgxQ3bDsGjbt9O3NlCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVIFEYfP_L4GkAzb84kq73gvQrOoUVgJM590fWMg4eQqj_j_b7ZhD5sviXGz5x3BWrfbvm0-6dVWeuBHCANO4gaDTMdB_IfDiOT45P6PVzlvgcPDbBsOOF-FN9l2ewqXtLlS8nSQaRuKTv0lW8vSuLYX5dgK5CHMB-OPBpnHBHofss3HNvTWs_QA5xzSrZileV0aXB3FwtykBgWTV8AlNk6yfcB8xwgk7kIg3FrQ59NchLbhYzD_sRrIWaU3u3UZ1CzPaC9SnAvAyZj5Fa44Wpp4iXWgglu5ilrE4gdkMi1XBuoleoCiZYHzFWAWPtr5eDsDRSTRIdd1IB1Xh4RyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=iANKYQ-NrS79zhLj2rTaoebl5RHJCLrOQhu3n2T5WjkFZGXaI0ovbX1NRxEW65HfLY1LHo-_ZBtyuVgbly0Nz1VdCP01K2CEczzcXtp32RK6AAovLy6leRKTYOnNY5FH1ybzxhQm72u7v01z0751o_VjMEDmGsEviN9NqpLcDyD-JVwSM1tTo09GYqmStJuDSXL7XPC-RGw-A5RneBPx4cdPO30A_dkInF9-w71rTdDHopw2aEEIXZhcoRINVKW2HaCLsprVq0wOvzz_QgGgsk5yRjB4qaVMGM__0SKJxVfscmpz74DmHuVV-E7qVJ09pOS1wbhZzZRm3wM_uKPgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=iANKYQ-NrS79zhLj2rTaoebl5RHJCLrOQhu3n2T5WjkFZGXaI0ovbX1NRxEW65HfLY1LHo-_ZBtyuVgbly0Nz1VdCP01K2CEczzcXtp32RK6AAovLy6leRKTYOnNY5FH1ybzxhQm72u7v01z0751o_VjMEDmGsEviN9NqpLcDyD-JVwSM1tTo09GYqmStJuDSXL7XPC-RGw-A5RneBPx4cdPO30A_dkInF9-w71rTdDHopw2aEEIXZhcoRINVKW2HaCLsprVq0wOvzz_QgGgsk5yRjB4qaVMGM__0SKJxVfscmpz74DmHuVV-E7qVJ09pOS1wbhZzZRm3wM_uKPgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqTemamjNtuDoUBDjNyEeJypuksXWx7qNS2GbCpUGawVQoBhXN8FCc9zPwF_aQJIqg-QEi0Db0b5sPYecdnVNCs8Ykl8demX-5jsOYoWN0tcVBdY9EBi1xUHmHBfv4Al6SMwCfKciVX7BK4r0bw93aXXOtd6Jmh58axa21hFKLwnKvlWC4Dca5YxGvFHfzDMjCpCRoT9K5MfGqIxyfy7WI-ILsXm-WpduvOdPDDeXtTbDn1Z23-5v97JTpABbgKgj_QgHY8Yq_90TyhtY4m78JVgo4SjDeXD1dN99GwggZqGzWzPsFMBDBqKanclK35IhWo6gpWIpymQJ6QO4HdwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAsghDRFgcLrhP3IkDZvwRQ5BDRNLvhPd7nowyAKCItyNRTqzQnynjuAT2ELQ0VBZLym0GlfAD__Y6B1vZtp_NmLLU7JAwWRabMWy6b_irF0PSv8aerDXDTo5p_wrv_PqPcSTO0qQ7_i14yZz_TAbrn7QWP6gv13fe4GwhzzbMrIKL3cFcWV6CJD6ir9Z7E5O0XpP68pih1iS3WxMq_M7KrFeKz_JE9uYKijyqWiRVEcwUShPIXRB0Ci8vDalWhPHKIp_ac_A7hJ7Fa5zX2G1tZyX5jHoMfuZGT-6wI3QwM6wGPfW0IcmAlM0mLxoQ2NGN8WGgiI_nWarMp2si1PUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTjGHNqhWOeeI3A6b6i6FHhDVUkdk4ijHhtqI_wQIJKhE4ZVlcQhkcd-yVuYHH_NNE8lzGhiK-yEKFBh9wDHXz8cVHC6w0ECMdt6d4kLvH_tWoq_6FyLJwnMemZoGxbu12pfVSSmjaU6UKab-gjy5xdbcKe_UdFFCma3r6Jln0eDsBOvR-26aSFLiVxpbuM2tuVYLaUVkG5QODkK-KWnwMrgAzTRv68QRRAetbvCvlm5cir98ImR2Famh12m-BzQv_yFan6AKtv2AH4w4GTP1DqHBlvY_9SjH737Ao2sJ36Cpkt8d2TqZhUDydcEcJQrpBBGpET3MnhUNhq5aoQcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f51Mpxvj9bTeK1yvwiyS7Qi-C0qPlRza2YPC6U8o34KIyaWAFLW0bd00cnrycE-P0Ek_nIASrT5DGpuJeq_jXeLkmvTuHULzHiTePkUosca4tuuadNDRNr2Bji6YaWtBNx3gHUE0u4k4x8Ld8rK-EuUkNk4-S7DUwYBOpAJIAWA5xOc-CaG7luTMsgaqZUbfR2FOw9zJcDmwFwSTFIl7uWnpGzjzKOyZG2KSG1AO5fi6xHRLz7Je60emoevh1qBcbqm4vpNkNaQ-zk3n00j4SYPNvnARHrQdwPLPE0ccaiTaqcRAxizCwWRtLK5dHlQLIk3QWLVN3RNsI-781kZtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTj2dIaFGvHDVyfQo6AyeqT5EL3x7JryaoVHhpUdYfNmJJdw1esdfE35S4tuirIdRUtWBlBQJRBaijOZ9rFKS_RVv9-Exe1P3AmZAYuDYtVw9iK8rpNRZh_DlTjR6BcG8Lf7KQQvscK2AQFDTBDPBmtY8U2SA2TN9ojW18uTdj2pN_yyd7zcumOBP2wzcb8mbYXs9-mH9XvEyz7NcyeOZBHSYSKAPhaQ5zZUiQCQWWWed1X9SuHTgS_ekUPtNBXj_4a8KksBdXpiT7udP1bqri8NqYCQm2Tgc8VgifLLBhl-wB34Nl0XzGu2ojbl5P_9_5X7Oty24zks1W1dFXdYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0uTaeHKH0BBcQno-o1TsyjAV3vGQSJIduWSk3G3nyC3ddPdYhT5WJiQ8XOEfOrnWsq7tHCt0DPxndY1SUYCSXeJ7te1k4YdM_IdYz9vkIqxNKft6dSsQ5WJlxRy4vkN4VPR71iePAy23GUtffNcui5uykWaa_BZfekCwt6Zn4i12OZ48M_Bmzmx4LSpRcKtLIlk2LG7elGIl7NLs1Y8RIBh2wnyjs3TsELZmMFuiI1NSoqUTAhjBUvMzeCv9ZL-8jA5oOu2VqrNKHPiZ3TzvUaA6E8a4p32_ye1TE-KkE-jMzKA9thm0sPAqAPzyyvXBqz9OuufYKlm4dLzxAjfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDutMnTkhFW-Ir1aQPQBn9YX_dtLX_cNfVE-OvmCWhsogcfQakmuURxxzuwgsCIigX-MPSFHUVP6GHDto6Blk6CurAWiFhi4kXZoEO5w1xVDoQKUkJ5TIk2bIvT3cdG7Fv-YNtIzcZJDt3CJkrTFpIsQzs9lkfjunHWG8KjEHYg1zlFHraw5ikCwya3IS1bHlQqUyj-8E_Zmuy5ew8ARfXFMDQjTsmZ1lvYLjXJxCGraBkhXRCCwqlUEsn3TmOEfn-irH8Ks6EB27s1JYasd9VArdnV4-Mth_XoETAJqICr1ycAVhQc5H_8CGwhBfDZ7XJFOumjT50tUTHkhi6uNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM0hEZh76YYWQjhGDcRXqmxlyHJapGv0bEAOok-L0xBkFlblfWolCCzxU0LEmeV0SatzRLOY60-hEI6Gm62Nq2CwoSdne1dLuKqIETmY-Qx0DKCmhMb32_VnDKnx4s8M7ORr1XJaGFuvyu42Ce_wZJEKhKFXcadTCBrv41YlgMk8apnscNoI9LvmKZtqCXR1IHO-JXFNH6yz7Y_OSjgGSHdVBl_2CJhOSYeYVWFoKnX0Ch-DmoQ27aukqrIKqfddcKHB5oVtoaejq1IOmCpIT-a_U_H2-o7qnzLZyG9FvjgMYG3pVPJZ4NbTd0NitXm5GhnbWZR1AkSJRevTc6Tmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Pp_EeTHS62TfhjIRoMz2rkDAWtB9k7DzvLmBSe4XTfJgktmNctHiL04eEnnBUa_AUNKmSbPawMD0U0K-1IwzxXvvbJUk90sODtK8wMIEpSQ6EO1LcBXnW0sN6hT80_PLUWew1wubN3-Mk8VuZ-m0uJXpmVrZrVHREKoU3C6bti-X7bPaiCq6M5RwWTYz9qOAxt74DKhLTuxHGh0BbkOSiXhrYBzWay6WHQ3bVcvHwH_WLf_4SO2PA8uwdoGOSf6xXy2vplwtPDewerzoq8fCKTsJfbwWRPR79yFQy6ZsJTzwKanprXcX0YldjI5Gmjh3LmW-ozdZz0PzKtP-pAoA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Pp_EeTHS62TfhjIRoMz2rkDAWtB9k7DzvLmBSe4XTfJgktmNctHiL04eEnnBUa_AUNKmSbPawMD0U0K-1IwzxXvvbJUk90sODtK8wMIEpSQ6EO1LcBXnW0sN6hT80_PLUWew1wubN3-Mk8VuZ-m0uJXpmVrZrVHREKoU3C6bti-X7bPaiCq6M5RwWTYz9qOAxt74DKhLTuxHGh0BbkOSiXhrYBzWay6WHQ3bVcvHwH_WLf_4SO2PA8uwdoGOSf6xXy2vplwtPDewerzoq8fCKTsJfbwWRPR79yFQy6ZsJTzwKanprXcX0YldjI5Gmjh3LmW-ozdZz0PzKtP-pAoA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B21hl_CINZ0phQaKvGtD5TE7fTkJvsN60x77k34t6srPHLh60imL0mE2wI0_4jSAEZtLJyvJqQPRSdfomoVUBz5N25W7SU2K0KgnGkJMXE2UKcmuDXZ8DQecmzvSs_pyiIA72W3sIXIySfKkOtZolymJWzQGPvtCzmfm7_jM83czldLJHSMJubhLpKkhSVw39wTmuNTJVWwn-yI7LYu4D7k8jHXRb1bd42YF-AEM8FI3HiMkNBH0Wflu1fTggohcMmG_sJORfCyP4CMUbNxYJrzlTyUKfTc6dubOv36qskiLqaIX7kvlRXBfYmQk61ov2dRZUZHFurQZMgAySFSXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCwkE9o1RKfS6CpYeomCc4Zv3iaYykDzBXzHWvuUCbb3zcdT64tt4t1gOFFMr8HgnV74OYtp3B99ggrpJuvod46aKZsVJEOfE51BZCZlga_H_EyFu_x0fD_4gYn0a65XA3CZre003IwayNHv_2DjPdkmNSmDphvvgpKlu2_UOY-TX1-pZLM-p2t5QGAIDTfqF9jmMAxO9S4BOLfNkhOWc4nfRhK_ZdcbVHipPWg_hGHdVYQQ9jvDClT5wTs4mhh5AEBHMEx5BhxROHy6Rfch0NE0CkhGOzB1GSxZFMnGPSdlRyWaXeRz37NSSI4kxq8pRy-rQLawQDl-sESCCLFR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG3Hz6lVmz6TSXHGwtbKRo0zFdAFRAd-iMwS_iSPAq0fhDv1IjRtJeTyYcIzKS00DRLEwyb_SkbD-YP2fGfuO4JAgg4ZoYPENVxOkXFo2973xKd3E9H5crWEeDnpxGjmst3AImimvCeL2A7NvcemdlL-RqjNGc6Yw2b3yrRcB4Jtw1ssQo7JZIAoi6okZytuqi7Nt8HGs_q77KI9RGFKgAUYWKntRrp4Gb4XPfBqeTVLCAmN_-AznabnwIG7IO_aFDwo7fxU-6ic3A4_AxioqAaI2FbDOnML1FSjKAM-1vTSL95Yqt4a5dftB3uSIG2ew3BB5w8HUCdVnWwpOgz9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usr0iDXCAZj3erEgKcSydldopVs_yaRbB7srrghBWNeD3rWO6Z0iQkHlKr7bLT9ObLJ9gbQtPVwN3OsvihX2SqKAsAUP4PkpnxqB0zPphCJvI2mRouV1liFcZGNcmkqyXAwg8qU2Lz2C9Qg_7nWPPvwDR6MFORsa3jm5RvqKKawqiZuG6R5FhsQRug-D_NVV0ZLFE4f8IugGPtXdFEZH-uihWgjWsNtn2XOFo697tCWzxiXmN32LEQv8SXE2P5bvMButlyjlbmHsVgfGAPN_pkn7E8IQzeyw0hU_vRgsdcpuVAkrwyxqKyNyZUfRhWrhvDOyPIDQmCTfLV_vodHxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTcbQ4TUgguaqMMirVPLTOz2oa9NaDfjxzUEUdzOL_dvCpy7rWHtLWHNvmPpc6qalgNvIqOxbC3NSLPpYXRVcRQx7Bk643izIIqITUwg5GuZVgcVFWg0R_6PSbIklnvimCFS9CNAPw8LPNKYgxfnZLVPtRlBM4XTZ0bkEbt7M9_Q1x1dSBZR2eHyJOMaikx4qLlr4DL973b8YtkFf_1ZbUJVdXI-4YlW7vWkucSbV2-T7cOimzZy3kBASuHmfIQPPmr9tdKjCrY3gjOC_BaiIG84A_YQy3If4aNzUX0ea1EX9BA2dsxFdyYMXxAE65CERkMKixSaYnHlQPX7GdSlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir0WoZ_Nb2DLJdca3fhMZEgEPPN1KASqLaWMne_e398hvNe27m-mAEW3lk4v2xq5X9FPm4alO_4n9qEDN8JWoMlkk1L4oAOtOr7wzBmQAYNnKspP_sfprzweWtJFsHQ6x4rcCrhJb_cxLKUe4GeBs7YYBvN8hhO0Z_MDudbwml2LA1ULIrhwT2nyMZU-KaT6nVlye2AEn0X_WfIWVA5blnnYKRWy4jUZLIGiRdhGXe17vSqWMz7_vH89acIy8snXLoDYXXz78Xfvk4ICnPv6gam2_htiCbUvdIug7gLt7WIs4-mkF7s-OhT40tzBPQVI2XbKkT5uhyah0zQyfa9Drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJFgY1F8KZWcpXY9vxMjokYy3e4c8T_q7FCG3KjZyY_yH65PFcPEYFwWohSjdGhSUJGcnheFdmMmwGH-E-oBusWrI_BTquuWSw5gbPhPEyysBYWCJg0WHisjpj1ysURlnvmP5gEDw49dd0HBSKddbemcT0FMBFSZDg3zWG4KtxQa0OvDQS-mXjYM6cKen-PW5gZ8l5wzAd4Caq2yQ6JB4NFqxqGl_nGJQl5Jhhsl6Kacu1_Y9JFY4k3J-ozEpUo3jcWaPtWQuvzCDoSGdvloR9V6QuGIgzLv0L8S2Whsf4_YkJsPLHohmd7IqQE0IWHuhXEfRHrNdXSjNosuO2_fTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpL4dxfbSz7IUNU9h84iHXXHqQdV8Td54pqgY3LqPDUKkdhOLPv40tT_g6WwLPYSyPSYhPmsqjsbLqFiLzSd4MfkIpynuczzC2Q0YzHRMRgVZamXUT6M7vUkflaMKNfcP24cA_CadTTL4OBfunlxwqcvXDEbVlQvmqYQKvKY5Z_-AMUH2_-T5YUjGMRuESv2dkuq5iQL6NV16XLVGUQY8bTq6uTqGvkQ-eAvnhFauX2erSuoFh8zVe5MKrp3cvr9toMU-bfolCrNosdqU29WNyvl0X6ywWghgCQpR2GkO06XZTe1Sfe7uCvgCwWFzZYgo0VIJK7ALa0ROAbnNQ5s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBFv1GA72_7-qSEZwfwfjtA8Aep2IgMFAj0kSjpj9wUdPL2hZW80ue2S3c7DBUdynIMCGpl_nbKln6RPx3nKO1o1IyvHZt0P_w6ZW9YZiLZkpuinCY_JihFGk8wibRWM-XGXFNhOKm6d3sVP93IH6BIdOfAKlqZbuB2FxD5lei7ODVONdlryu7VZsDKZlLbDZrjqtdmjg3GAIL5xa4dDwg1PqAx3H3xWFP0u_4L-mFHcw3r7KMxvqT49UOAHgFEZaGFzKbMBVxg6doYli1RykKnqmEKNcwA4fs-hNCPQ6EGRUGxneVdhjx4SYipOCEZlna-9lf60VTuP5ce5pwPiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qtWB1KmIL1EtIFRaNfoc9keAe9ZXo5aYTmp1gtqic3L9xp7WxMrgpFZSDOh6TvCpAc-cu38lCE_a3RwJoj47wiYLKezBWicwlmL3lLImYUvfd3uDsXx9mPeeiJAd9B_3ikHIPaQpj4lNSOCKbdAPPNf0RWMr9_Y_qPHSD5-RRRLoMSTEj7QRU5RvG793a-jOg2NeJdE51ep2oCxyHLRlBni-jrI1oUbHN4XQZpzrL3MFfZzwhwwBoEyqq-NPcbySUcOsBpYKfLnIjCOizYDiLZ277tRp_1Aq72wOeTNguwgG12b39MZhPBrAFU_b5whjiWXF_L_KEt7eAJuihEBQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qtWB1KmIL1EtIFRaNfoc9keAe9ZXo5aYTmp1gtqic3L9xp7WxMrgpFZSDOh6TvCpAc-cu38lCE_a3RwJoj47wiYLKezBWicwlmL3lLImYUvfd3uDsXx9mPeeiJAd9B_3ikHIPaQpj4lNSOCKbdAPPNf0RWMr9_Y_qPHSD5-RRRLoMSTEj7QRU5RvG793a-jOg2NeJdE51ep2oCxyHLRlBni-jrI1oUbHN4XQZpzrL3MFfZzwhwwBoEyqq-NPcbySUcOsBpYKfLnIjCOizYDiLZ277tRp_1Aq72wOeTNguwgG12b39MZhPBrAFU_b5whjiWXF_L_KEt7eAJuihEBQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxkW5p2-fONZaJQILOh5gWwSkIdJ3yiV8UAC5-zEv6NKPPcuAuA-DBCHN10yNmW0c9GKZ9Wr6Ltzv4cNTaJF7-ICyTNGgJtuUOQMcQoiV3Tlvd1UVRiKAi_PAEugtipkbaLt-e90ChU__y5ejUkqus8Fj1K_hCGjD_Io7BHgN2KM0vsgdvJ5xv-LI5lNtBIdbkWEObnNPqqHpRb7X0trVeUrF5r4WaT446kK12YCRXFHlxzFkacgAb_AOuI8ymqCBPHIYedWS-n4UZwuJ1Hi021D99ly8KURObxcFkkEaBcyIamL3rFKM8kuss85mX4VW5L841lPKDG4hVxG-sQ9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=He95OwJ-rLGy4gg6soxxZp1sCGl2eMng0MkUrgv_ZOEGrccofx9TLyFT6POz5EeEpOxb8_QXWbe-MMt2pp8Ye_cAEcGMWS63BdyUtSYNdPB2vD4KvXwbKSuFMLgSx9rNTeHI8ULlBp3nbqEGpMsQ9vnL955XBqZ-EnfrLXeVVLjR6SWfPfJVmjaqAw9D0gctmMvs16_317gdZXNp9OvQ2zLoDqsXDA-TrmRlp4Dev4MfMJX4ZexjA0F1SAReIc1EPK3AItY0iFDkfFVU7mVN12MLVMNK5yspRG3-utWs29zI2Q6BD7i-m4Ez6hMekEgLDwbA_PbPzNjdoT_OKQdNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=He95OwJ-rLGy4gg6soxxZp1sCGl2eMng0MkUrgv_ZOEGrccofx9TLyFT6POz5EeEpOxb8_QXWbe-MMt2pp8Ye_cAEcGMWS63BdyUtSYNdPB2vD4KvXwbKSuFMLgSx9rNTeHI8ULlBp3nbqEGpMsQ9vnL955XBqZ-EnfrLXeVVLjR6SWfPfJVmjaqAw9D0gctmMvs16_317gdZXNp9OvQ2zLoDqsXDA-TrmRlp4Dev4MfMJX4ZexjA0F1SAReIc1EPK3AItY0iFDkfFVU7mVN12MLVMNK5yspRG3-utWs29zI2Q6BD7i-m4Ez6hMekEgLDwbA_PbPzNjdoT_OKQdNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwsp0mCtIF-EObEfN_Ap0edzc2ELUC_hIimIEgYgva478d3q6tnsASnpnjrt5PEW37p6lYHyg2TubjNLI2lAzuIeLjHZEAfs5kOrC35PiLOoljJMI7J9_CBakPxNdlnjcaVMMvguwggGlpZVxFfyCbK4NzGTCsyRKBOJJhH18cTx3FKaa7dzB1TB2xT_Sw8Kq7XpdVtT2dKuuDoYQidaY5Sm_OS9E51VY8MTQonPMlHYj2noxvvRZU8_B0Cn5euulPLd3P0uQethoL3GlkeaHvCjMvBDG8YWVZIaTLVjDozbzVGzzV46xWhhxNAFwyRXEUmF4z7SVIwAEAfFRJJmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-Ki7JeXNI0kTCiGj10025A5CeasWuactB_1PhNJH7z8uS5r8C4lZnBYqgstJ4VXe88hjuYc8z2uicpBnkjgFX-HUZjnyHZ_Ue13h_1swtcGO8HI-wruOyT2lPMTBmBKH9HiOlJ6-lYrYLIc9zyI_iIAwPm-nf1Lu-mLGqZHnjPmzM7lS-2bMYqriE7gxbW7cz4Sq8dacQPtemMvvFgoW74zhPm--7TN5srjUjoCyxQjmhiMek3QKyi9L6doXgfZ7sRU9Dg4dXnoetc7mtYcpHJGe6HSPrtraY1HH1WU0WWgy0W9-NffRhcIsXzEnGnJCTDLClko2A04q-LvUo1g4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=ZtBUXR6374UkNIk5dcRD-Qj7zjsqPpvoj51enOuZr_p38fz9BB6KjcjOMlCWepig4vT3FX3GcnNuUlJuI9CBTvyvZa7gzcreptzJfRU7D7GM1p4sIEoJnollgx2Vvpsc8oNwj8OTKjqh71ISFniHOq2Hw9DAxooc23uUCxUOTg9BETnTBB3yf5D9STF2VXMC0Qg7TQJz6fF_QGypH-UaClx1tskkwaN_vfT0sBi8-8enPeqGtj5jkSfahyZqgAElTQoC96vxoy141Xok_iuQPrfxR94DttkHEDcRYniltvsatgV-ewzakseILRcuK-v_0ylxFWOUcZPEKnURlRfhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=ZtBUXR6374UkNIk5dcRD-Qj7zjsqPpvoj51enOuZr_p38fz9BB6KjcjOMlCWepig4vT3FX3GcnNuUlJuI9CBTvyvZa7gzcreptzJfRU7D7GM1p4sIEoJnollgx2Vvpsc8oNwj8OTKjqh71ISFniHOq2Hw9DAxooc23uUCxUOTg9BETnTBB3yf5D9STF2VXMC0Qg7TQJz6fF_QGypH-UaClx1tskkwaN_vfT0sBi8-8enPeqGtj5jkSfahyZqgAElTQoC96vxoy141Xok_iuQPrfxR94DttkHEDcRYniltvsatgV-ewzakseILRcuK-v_0ylxFWOUcZPEKnURlRfhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=Knr8QcBDA5zhgo7ZXbsbwbyYGfaNag0ItHGGtjEJVNG45-VDQcH4Y-fM5hbiO_cnXHFbtr8ECzMQTji0XzLpPHtDuwxI2UpolsGifWVKS8XuQtjS-5__luruaMEbyaAVH8HAdHj_slta9WA-umgfeiQQksSWs-NqtbTHGOfhP8A5E1ZY2wCe1eO99DuEsc6DXG6rmxm9EjDU-zIQvZR3uI2hPU0WFzCYce3LTWDFU5gpvd92uWNC78SSGDQOjPwFlgrYDJxRzpAWmELAKUWEKXm2vA_ZFfnaQ6WZsu_JtckZcWMK1piWtVpNrebJ3a3VcdyoQFcIP0lRnDox-EY8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=Knr8QcBDA5zhgo7ZXbsbwbyYGfaNag0ItHGGtjEJVNG45-VDQcH4Y-fM5hbiO_cnXHFbtr8ECzMQTji0XzLpPHtDuwxI2UpolsGifWVKS8XuQtjS-5__luruaMEbyaAVH8HAdHj_slta9WA-umgfeiQQksSWs-NqtbTHGOfhP8A5E1ZY2wCe1eO99DuEsc6DXG6rmxm9EjDU-zIQvZR3uI2hPU0WFzCYce3LTWDFU5gpvd92uWNC78SSGDQOjPwFlgrYDJxRzpAWmELAKUWEKXm2vA_ZFfnaQ6WZsu_JtckZcWMK1piWtVpNrebJ3a3VcdyoQFcIP0lRnDox-EY8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=p8Hj8U84S0Ig3bkRnr33ieatrQ-SvN210aMBZKcaVSwJWeRT-9N2nFgV0phRMqIg2a9UVh3rUxh2AhYKs5G-iboOpC6YHKqH6Qh1hBY-4TfQqkUFOYhwffuQR8G5b-MmSfbmZvC6haQLz9E8fY4Jg2xgBeHvMGZ3xVOO3dVpNMkwdblpwL2LpFxmIukLSRFaNGguLnPhvWP_prsLzZCNSPvtRJ5hvwKLi4fTphHAhg6UXuO-5IpuqKVL8V7uotCqPyAi7TtUpqmJhUDhJCvgHPhIwAzSOdCoayCQPf41MRRoV-RK30AGRqaJAb6l0DDV9NyrsQvNKKOr8v2x1upHzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=p8Hj8U84S0Ig3bkRnr33ieatrQ-SvN210aMBZKcaVSwJWeRT-9N2nFgV0phRMqIg2a9UVh3rUxh2AhYKs5G-iboOpC6YHKqH6Qh1hBY-4TfQqkUFOYhwffuQR8G5b-MmSfbmZvC6haQLz9E8fY4Jg2xgBeHvMGZ3xVOO3dVpNMkwdblpwL2LpFxmIukLSRFaNGguLnPhvWP_prsLzZCNSPvtRJ5hvwKLi4fTphHAhg6UXuO-5IpuqKVL8V7uotCqPyAi7TtUpqmJhUDhJCvgHPhIwAzSOdCoayCQPf41MRRoV-RK30AGRqaJAb6l0DDV9NyrsQvNKKOr8v2x1upHzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CariLTgNnoCNbMW8mmGfky0gpvtVuS1vJvL7Ee59u33Wpa5nIo6HH2sa5lvieVwhiXLA1RGe4SUdnsZZSQZ4u9PHMqvfnOqjc6m3VWf6EdgUP7QlXg3wdn69GYceRwKTcQOxzP47xEe9XjDfWZV69VettVSOjOF-80P5ZFQyiGXv1f_CRxyCQoF5rW0nNpSkkByzz2p3DNy6sTMg7p-TQ--Q5IQnVqxb5voeTNBl0Pb_Gjfxu2imRzufVkViaviUAYRB3baDb-_MVlurojRIH8-mkrH7Gk2CaLEvta83h_wgX3eLi90lCMu_dOjZjeKCFDBsrpvkbiWSn5wSHGEt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CariLTgNnoCNbMW8mmGfky0gpvtVuS1vJvL7Ee59u33Wpa5nIo6HH2sa5lvieVwhiXLA1RGe4SUdnsZZSQZ4u9PHMqvfnOqjc6m3VWf6EdgUP7QlXg3wdn69GYceRwKTcQOxzP47xEe9XjDfWZV69VettVSOjOF-80P5ZFQyiGXv1f_CRxyCQoF5rW0nNpSkkByzz2p3DNy6sTMg7p-TQ--Q5IQnVqxb5voeTNBl0Pb_Gjfxu2imRzufVkViaviUAYRB3baDb-_MVlurojRIH8-mkrH7Gk2CaLEvta83h_wgX3eLi90lCMu_dOjZjeKCFDBsrpvkbiWSn5wSHGEt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=flAZ-QPEPDhg-PEnqmOvl02rYg2mJyNj9xw85RwYLEil13a6dbVVyFN9BTLWK22jpj3uQ_uPFS90CFOuAThXj2OTPM6hFijmOi2CahSXzoP_XjJJcOis2XbXryFlK4Ey3VA-ceq3gnQEvduuAVnbKbN9wWYE9IPU8ehAHMZ-Vf9bwCe5UWHb5yr6w3AW-g6NJFGMyOKvWNq-QOSXn7Nig1Sec7uE44zW7YM47WVfPb4J84-hefBLcVYab2WuVLeFVUxdSnmqHCPfxxqhaUx1w7yXQhKNqQ7uYOVN_PHcGZaLNXPF4O3U60BOsK_MoWc6R_PeT0n82oKtDY86EISgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=flAZ-QPEPDhg-PEnqmOvl02rYg2mJyNj9xw85RwYLEil13a6dbVVyFN9BTLWK22jpj3uQ_uPFS90CFOuAThXj2OTPM6hFijmOi2CahSXzoP_XjJJcOis2XbXryFlK4Ey3VA-ceq3gnQEvduuAVnbKbN9wWYE9IPU8ehAHMZ-Vf9bwCe5UWHb5yr6w3AW-g6NJFGMyOKvWNq-QOSXn7Nig1Sec7uE44zW7YM47WVfPb4J84-hefBLcVYab2WuVLeFVUxdSnmqHCPfxxqhaUx1w7yXQhKNqQ7uYOVN_PHcGZaLNXPF4O3U60BOsK_MoWc6R_PeT0n82oKtDY86EISgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBV-EtL-bmXCtdwbaDiTFKrWQIInCJMcfsMnWQM3cmy5TD17f6wEAUhiuIvTwq0EGTpbm9AldIo7fCz_h04SnYIFpcDdjmzNbZRKRwLHuUWeFeX5YF_Emif0sU3tQWgYzOhNVBogkbMgOXWmMk2dzvpgGRRaUUp1gn2JgCtIbkCuz_3Z8NavnNUtIHfOekUjZpZWBPTvmbBVFsDV4k-oQZsWuhbmUht2j9ZG0XwGunGsLqLN4M76np5v7807sboPlhGeUUm694ltNerfVnXy-uaJXzTUOlC2mN2CL5lgd_BlJ5LYmMxfM0LewXF-3sPujxoZDUN0nqQ4hARobeO3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7LVkaVDpy0MTo3mn4PRS0sxDUgQZpjePhTfViUJpAX5GZGryddkKIi2NJR53CsKQVczqP2s1ef-mwU6f4ycDSVtfcWjMNoM2C-ZGjfwuZET0LGhsoY0og3Jk0noeNpGW7E06TkJYbpFQwE736CIVS_qRoK8Q5AZ01nwpNBgPiE23m12E5GHkryG1Bj0KYV-YU62FP7GWg75Ch2euioIW_H7xePpubsVX8O1xhmoQioEn7lm9XgvZlGojfh0AvWk_vcDdT1yAFdtGep3Y-L4iGPesdJKsQaaWLQkajUKYaInm0ERv6gGruyZZMvJsoNEUgrfn0BMVv2gqCl-v5K8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hke_Ca-p8AM9u3Ape5qWTkKwsElndL832xekldYKlqnS_TlzjPxpq8imBgcXMNRD5x7nB4CvK1Vx3vMxwpzQ83W4LRU-J8Opm9kiTMZC8FisAGKtbAY4gotHpH5bX-m8ecP6N5_tO-N4E33DsILxyqAMvemlGBrpb26cbGOZKGHmhPc4c8j5L_5ttvLVSraTL22Tnlbhh6XB3_njmCHJwC9jBzCKz_mvn8oIrhJ9-YwD_h9NxDsCbQfwH50wqeks3qcF5wa-EDwy_cIP6ajHxLcQcW4lfrN53usvUu89Ij19KzKhGky9aGgJwuEEV1TnntLoMvqpH1NRjgAFsUb0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpcvyMrouXgoJVbR0npLSZP_THXAM5SXMmEqK3sTKmYLIZ3VYh5EMa48GzEdVaDOiM9nn4TvE5ZynfaVb3I6L8NIP8YOIHH5xryAv4NFlYsf3V7ggEJGG4GdGmq3l4HFj0WMktWrTPo2f9VjzVvlHL_A46jcke4cLrkbcJFxgrvIw2BJrKTdhh2S-Qr8XtjMUT9k2nnhqAQaus44Q2ohaTxV4a71inODXaZgbOKrrcis-iUtMojDhipZxuVm02ixFxmxXYmcTb993_kPZh1oa5V1_ti9e4gooET8NJJvMAl5cjml44jJv-2FKwE06bcLbn321bSQt8_sj6B1Cx5X4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbsKAQBWymgB-6InYQobIAn9A-Ba9gve9gt571x5FjM_GXhff96L5k59Fbojz8Seyt7iK2SKSZtaNUTV1fqdJML0ev6N__R7DPQZtKBGq0fSg67_Nu7McjfJLgKX6W-Oz_u13h19nY0qWaMbRClgAkVd9L4q_ILEKThnGD9rOrSVU9xf_uXdZ2tkZwXuT9YgSwW8L8TanhEw2p0MYCVyiDmncvfpewB1cg79sk1lHffTkJ9Cp15vzWwndf_O62DtznSiAAFG-jQV-TNK59kFmi-KkrX9btOmO4gdV1VCH_TzNEGIrm9VqINkHy1DPAAVgV9pIDrhB8FPhxQxUHF2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFi5lDJdtAU4eKHZfHJhwmuI1VbpvFyeycP61ZQB_qdjgnDXws6NCS0wuXRpIklheJIXz7Wsbt2mXW8JRORrYpUo_yYHuRVSaketnaBjntHL6wQoI7Sr6dsJ1XhtCJlN-gJeZunmwqRrWr__HrwEA6wcWwbvACz_S7_r3z4f1OOmVpYqtxxHJ3qN2iHPaXcdAQbEowfKRm0t8z3Lv8plRPN4Qg-idjdk9Jpib2f69TiRcg9Dx7ycTMbos9MoKcNavoAHHcloDtQI3ijUParEzYe-Tk0O0KClEY-UkNGrajxso0UkLarwhkP0BAMLrJTzqW5DxYhUFauWCKZu6JUw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMHYzYzPpKcePjAauU7DdJ02tqJuyMeBMsen8Rn7FZJj8JFq_Ff-Xt0ZuW4l-m2rRdC67S3TaR7py9L3lfvmokOI4ELj3_Qu6Gbiuq1Z9QcTSPCBfm6EwxOLYqDHwmm5KyNo7sqOyFXu863FgP6YzZzW4d4cTMmKiIBi4paOizUhPn75sQ6BUANEk4AvPABhT_nGFHLqcLNGYraNGKXgbl1KAifCEBbM-O1mah3kkvFYn8f4_q7W0iTNPYt1pHQgof06j8bLbjf0z5agNwf2TDjm-OLKgTagZa2jWdwUYseQUw30QO_QmypteOmJo4oAN0h0ZbVLydbIQlwf8Lugvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEhWDoLx9hPVujNtTkUpxMct8ej8DXKWZOB6-t8SxrsY85X_jC0UeFiHsVX9dCe9vIpwxmaUuyFKC3_ZIJ-k8d6VFToWLTliecnxVAJh2oMLJjrdzEzJBd3qMM1rgyRJifNHMPRPKiIuia4qfwX0_mo1NN8IIGUwMCf6iXjLWTD08q1pIjgFxWLc3vXbTLLKNy8-I1tu6CVOspDxoUkAnoqyxfDIspTVe8BzrJXFH4il3ez5qe2dNRWWWAft7VA2qre1i5xk5zgWYPC41ydn9xSc2dPhKzc8Sifu2AUEZ6YpSMsHIumdxuMPvCDGWj1yexZpS1uS-xMILpGh2zjsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu-re_RhjWl4paO-GGMz7pAlG2tZ6MWiJs9ijORw7kWlEgMLGC2XZQupswz5besFtNAiS0LExrpoZozWguC9Lhcqqu9-Z8aaObWvjSUC7wQMyTXdwdOtaYKyoKfaCRzr9hbK7YZB9dLiF0EXbUMAAcU8occQugWT9Spb-eAPPzmx0AdZFQdK2SrCjlrH0KNv8J-mm8S75n8GkPYn3bjBkclYKP3BPOqORmyXRBVPq-YPpE3Ev1AW6WyF0TAxPp50vAyY6MoGbWRKP1dEgp68oHDKTsDvo1CGKLve52AI5CZqKQUfR8APd1-h50jIP43ArFbvCmcGUmNVjOblftOAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJcZkh_pxFVH7cd_NS3QuNYRlv__-uu83ayzJWVhIKzcApSUYlxMJnWuZHq1EtdhgsIvopJDu8EMY74E32R86nzmeIazA-i-MLiXH563oncmH1kCksBHd6ypHU4itAJ169bgLxL3QSgPD4yQJSGnkgBeH3btUG0eMK9Eulsbv-WjWyhBTkFS2h5jkId9aFgcNZsf56PxOnrarPaj0jlSW01Yni_hZr5vYDGljp3oNLzmS4otKLlIhnfx1bECHnTorj-484-UwQgQwQlghGIXfKw7k5TEy2IGUbnlniiLDXXidcKtq8mvXRx4J2Z7YDfr5fCZ2xj-SbbIyNQV5sZtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=tPT3gflCkIlSD9efV1CRuZ8OKCYT0q5iDkBLPQAok8kN4gFtllnZWom9ZCTr-D6_4AfMvSih9PVjjc5QoqjNOXYQQbiHqJnYR6Cg0LlNI_JvurS2ETJDzzah2YtinfF_UNx4hLu5Ei8BZSWDwsOjBq57ZkV94UJoSWo0nQPb3h-dM5Visic5s-1BGxqNsskoZSPGbibqgVRYOXqyvlO9l7NitBbJWJjrw0bi4RtgvHO6M1q8AhgF3f2ji7rV3hFeYppeaZkJHoL2QFMrskkS3R76axNIvG-zPq5HNgbpwHpjaOwB5y9VZGaLm-67hAbPrWb9SQU2xyDyJLmpxu0jGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=tPT3gflCkIlSD9efV1CRuZ8OKCYT0q5iDkBLPQAok8kN4gFtllnZWom9ZCTr-D6_4AfMvSih9PVjjc5QoqjNOXYQQbiHqJnYR6Cg0LlNI_JvurS2ETJDzzah2YtinfF_UNx4hLu5Ei8BZSWDwsOjBq57ZkV94UJoSWo0nQPb3h-dM5Visic5s-1BGxqNsskoZSPGbibqgVRYOXqyvlO9l7NitBbJWJjrw0bi4RtgvHO6M1q8AhgF3f2ji7rV3hFeYppeaZkJHoL2QFMrskkS3R76axNIvG-zPq5HNgbpwHpjaOwB5y9VZGaLm-67hAbPrWb9SQU2xyDyJLmpxu0jGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONEIwCJhDXQk5CC_7NxfBSGqorSDq13A55q7Xe23JRBlA0R1RKQRtf0oXhcFKBGcEtJxzqtMpVvKsecgPkGQ30Xx9y28zfVYtpxPgidyLgC4tD3szDTW1DSPhXu_z5OHHVary-n7GOztk3NfKgkKF6uqV_S1Sm8rkZA_nt515ALdi93yfCXosFT1d2wUSqywlNUfLNTjZrbC1kKbOzaYi4bqsw8Wx6cTN6q8BnguUqpxlMTeJKti5VqZsq5HO1SWBL8kXxS9S6H_dK3jLFx6JMuGOH4gO7UBFI2NLtw2uAw7PbE22x8bs8RnD0WhHinyDtxtDoIZQkhyMrlfkkCZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJKKJGgdiFmGX-6gzQWDwnNQVYpCdD_wOX7zOglMHmejyOWybDW6obvQkT5nQlgE4ZbrqZX_I6omAWkEVC4fDntR5WJrkLU3kLOuPUj_BaqPRovDDbLWQb-bpk7yWipIbAoU25ApOnY7fmWSO-_dCEgtKydlMNxibLqpGVnG6ChbO0C1_aXmvaNYuXM5f5OkvDTTCS9XHBDtHiVBw7Z9EBI_xHbj1Epm8exNzhJxBc8_ryAyCOpBUCI5F0BHhnxFA4iM-haV1t-PNTkb5NRAd5FXK19Wq5cp0rGvebIwqlHGSI4arfdCbqzRb60ha5caSkY0WCSOPyLkiMmN5_Dpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8D70WsYMdsUwSHG4R4gNE-B5hBfZyGcTmuzyOIXbiPlIgDXeMIUrOecqc2JF4nqSFFHcJKkznQxufXZcv28gvi6470kudWzkAenKtmMhmqch8_xNieXyl20BZ1ojSVt2q2M-riJcxymAv_f0Vc6bCiw_qA0uAmQr8IdxguWWu44IIiXfIqrb-EfDyQIssx_xM97WOe2KW88biXTOjZJya3ydyb7YpcFVnK62tRnFu8T4B_lbrd1sBFvJbJvNCP_FZ5WuKyS6vIuops7YKXmIsQcRaeaDuh5WKuquNRoqc-Xg6-jkOKp4TxypQADonhTE_NaIm9dP9svAHPSUkdxng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHRjjYywUiupZGvcNARwzdPBD1l4003IWAXbXP9ie5yloBZYA3hnICIjHDCWG3Rz8_DyjNci2xmoPHzkDzETHpRjiojgE58FH-kumBzOCR2Pz1s4C81K5Bp9uRYBY5cJM-igB8HYm04UwCwlDvKTPMGosKw5vA-8Q5Y65hYtBDVjafEZJA-d-dIMjCMaXtzyI7O-LV4h8DHFuMbKlI1pOcITD_bRfjQ7IrhlQ-kJypbWxNJCs1jzkU44U0mnogpDLa-LEn3szYSLIinSzMNx2cU_Xai-V14ylN0TEcXpjBgZM_UYxIyiq-aBAPlr1OJskkFRiZIuUxi1_Ze7oCDeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1wWHiIuGek2XRFAlSOZD3msSRoYwj3de1k-9apG-Rv0IWlSPIKGQ0mJntFAx43jI5g_9tJxLUaB4ulf6AJFZdDblHRv7QSzFQucbqBmgzKQX9xnhj20DxCxH8DhBq-TgqaHaKpFzfeBqmd7IFzmLSSDc0Nv_MLLqiOB-T3gXflcrnItJgZTmzZXv_E7eCS9wr0n4KV6J6z71ljG0wORDZlrXCI_OQsamPtSvSdFAVvJ93oFBlcw_tuOJzlGYRdxoeahJXzpdjrUbq979-vnplJ5GZZMQnnFYdwhHAaX-gncdfOK439wWKiXaQwtQIHLux1Iglsm_tajH5Twr79-dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeAsWBTCwWIwdfD1sMWmPbMinfBwOtH2omchVsZdxVrRobmRR0d8PEsFF9Ac03gwJGFn4aVjZW4MeuRMQaIxeuvrK-RmFE3pVQsmyPj3vyizD4xiYPmp70uOfGiW1uUdBSGB0iF_8Vfd6gTBxbos_q-cFlxohsudjiWDGuDwW-8sOMU8NeZeV3l9ufZmzrsj_c9lWXQJlTWjuthOoiYuKZbk3HtcbXBh3rVIVPFyGVyvr8W3zokp8YheCZH0HvLYgowegx30JTBI4mu44-j5ke0Bgmfc9ch6OWC_p31K_a5xeiOX5whEo-XfN4wc3H-u-74bS2rbosfRfFzgklL7EEvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeAsWBTCwWIwdfD1sMWmPbMinfBwOtH2omchVsZdxVrRobmRR0d8PEsFF9Ac03gwJGFn4aVjZW4MeuRMQaIxeuvrK-RmFE3pVQsmyPj3vyizD4xiYPmp70uOfGiW1uUdBSGB0iF_8Vfd6gTBxbos_q-cFlxohsudjiWDGuDwW-8sOMU8NeZeV3l9ufZmzrsj_c9lWXQJlTWjuthOoiYuKZbk3HtcbXBh3rVIVPFyGVyvr8W3zokp8YheCZH0HvLYgowegx30JTBI4mu44-j5ke0Bgmfc9ch6OWC_p31K_a5xeiOX5whEo-XfN4wc3H-u-74bS2rbosfRfFzgklL7EEvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Vk_eMHbl3wEbOmgI6wRu5qJkxoJ3T8BDL1p3ZobIBK34V-lTXR5663zVuZTex3xlRLXhoLitTGCr1fXB02W0T3_mhePpZ8a4x-CSPevZSk_K9Mo4APM1FkfbeMeUfxRyBsGSsO6kjPa9RyUCuZYZC00eIPaTvFnKEu6WpiwgZ7kM_DDb5XTHMSlwCc6ZR6WU3ZBYSyo1mIEnGhFn7_I1t9RYzm2CGXhFH28uWL9JNaTUdH9s5-lKwva-t1SrFpsOJIKoK04EHvzpWLUQ4XH3iWbijC2ixzAOLb1easVCKDWqy5-swFhBSW5cJfeWxleWqfd86YD7Xqnw6wZ-UVBTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Vk_eMHbl3wEbOmgI6wRu5qJkxoJ3T8BDL1p3ZobIBK34V-lTXR5663zVuZTex3xlRLXhoLitTGCr1fXB02W0T3_mhePpZ8a4x-CSPevZSk_K9Mo4APM1FkfbeMeUfxRyBsGSsO6kjPa9RyUCuZYZC00eIPaTvFnKEu6WpiwgZ7kM_DDb5XTHMSlwCc6ZR6WU3ZBYSyo1mIEnGhFn7_I1t9RYzm2CGXhFH28uWL9JNaTUdH9s5-lKwva-t1SrFpsOJIKoK04EHvzpWLUQ4XH3iWbijC2ixzAOLb1easVCKDWqy5-swFhBSW5cJfeWxleWqfd86YD7Xqnw6wZ-UVBTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUd0nPbQqHxBidGtZuaMIng9QabROG7LScL7kOJMDtrLAaj5VZ2Cz4N0-xwlhjcfPR_UuA9dK_CJ18IjMvjzpoGLQALj7v56HB3cvpQ7KUeAFAyz8ptvNEJOflZoiPwP9oWwGxckKRp1LKmgzV-5y2krZ-skzohqfZ5VPf7cd-t7BHpI9CbOjvFWB7rcdIXy56o3baYRVfnyQXUtDy6mKtmfQqqnAf1NnxpgbTRT_HIOSjlsZr47q72vnC7QfetdKE_B4PcwzlN9FaULGQUxr4BP52KP_wh2rE5uj01Rk-v-VagqCWftysFOz-mpVR1KRxdNglqTUuqqnHRDDvr05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=qDk8yIRK4yBAQQqroXkcBq__5O0HUC6ZYaGvinisIB-_RObsfsR-ICVycdSSusyNs5VxdnxwZ0VIg-h457tJdQQKObv53jGdJRpODr4mRHabWuO_TYt0e1FLFM6WpqQKVCrMo8im7qapdlDxL2G6rkJExTHe_wHqrGr5HdHtexJv25qfpqPJ9HMCSVhlUDAzlWHsP-qrDREta-jqY935cVG1L4ZVnTLSmoXh1qP04L6MAjMSg2fqpJyKkT-7M9CIQVp7dhAQmMdZAFievgDjwo7s0maQqNISNcQIc_vC0TQuhaCXpwf20xClMsHfWHmNgy4ijkO8sUkjLWuaSSzEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=qDk8yIRK4yBAQQqroXkcBq__5O0HUC6ZYaGvinisIB-_RObsfsR-ICVycdSSusyNs5VxdnxwZ0VIg-h457tJdQQKObv53jGdJRpODr4mRHabWuO_TYt0e1FLFM6WpqQKVCrMo8im7qapdlDxL2G6rkJExTHe_wHqrGr5HdHtexJv25qfpqPJ9HMCSVhlUDAzlWHsP-qrDREta-jqY935cVG1L4ZVnTLSmoXh1qP04L6MAjMSg2fqpJyKkT-7M9CIQVp7dhAQmMdZAFievgDjwo7s0maQqNISNcQIc_vC0TQuhaCXpwf20xClMsHfWHmNgy4ijkO8sUkjLWuaSSzEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsf_BwpQejmzqazijac0CAHh-jpbNjHuybhTXGV0XKJXtBKLJPhDcDBWV-yFpMD2-2lxsl49OFkKJrZjF36jbwHvdLhCWi5ICdXrFv2LRpiM5BJF0y0eNx4iYsogQZi9a1s35WjV4EnEi4hgbp2Dl8uQ15B51mgNA7vd1t8EsbaTW1YW_WsIgEuVp4eZ5ImyevFl4vti9zkrONQ4PisoTLGCsQ71As6HcCCX8AreweCTEkMlxwhR5-8X59N5Y8PBMlwu5cmdICaaxxspPHIQ0H3MbecL1GLEnblDdHI5XAOZidG6LUn8YNQx6lwkNFw3IFg79RgbzdE4WweDeO4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofqJFGkCZ3Iq3icstNiPdr-ddeh4-FO2ZGmmGLCDFz6u3eTdgjbgwB8DEJpwQU-YYo-PW24f5Wq2SCsT7JXzlRqDsSa_KV74Oe9kmfVdGXZZk04KKCyjBUd-rpAlr7Gh12U4UU3ndye06aumSI_bENWmKwLaSvjb59vnNCj5XoRQ35MeXi95jnBXwABucsiibnIA-dl3_5vzKJ_mwmI9sMEP9rQB4cGDX5_fHhUTs4kDUwU0SAZrBOJBQFn_yw-UFiaJBcFrU-_2FZoev6xXJomzfeLh0JLRkznjWYt-CH5fQBUFlYp8mQmTOG4sAhW_H4JhrPr4CGbZ28w9FJsn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=LoS9hmYcrTqTw0LLINtvWv87ucA8IM4lXHV2T8L_E8brHJTBmaAh1yZbC_mc-8ACfY39IS3vMvFEBS5Rl1qmaH140Ez8zyHBVEpXkEpLdUNPfZ9x1TY9IdZ57oAWGs3RbmIwF6l7uIy_h694O4lxU4elebJD2uRYMRjup0cUF3LPkqv07zRFy0ge7a34Vlk9TN15Lv9CSoZTqccK3sQrHUpWaPrrvF7_ALWXdFS21QJEPoRinLXoBAREnhzwzXrWF7oajTcLQWEtuq9SxLc0BFUDVuya1X_x23Mh243hmgSuMBtljA5sIHJwTr79Kn3h05AE36Hs_9ZIWXatxNILyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=LoS9hmYcrTqTw0LLINtvWv87ucA8IM4lXHV2T8L_E8brHJTBmaAh1yZbC_mc-8ACfY39IS3vMvFEBS5Rl1qmaH140Ez8zyHBVEpXkEpLdUNPfZ9x1TY9IdZ57oAWGs3RbmIwF6l7uIy_h694O4lxU4elebJD2uRYMRjup0cUF3LPkqv07zRFy0ge7a34Vlk9TN15Lv9CSoZTqccK3sQrHUpWaPrrvF7_ALWXdFS21QJEPoRinLXoBAREnhzwzXrWF7oajTcLQWEtuq9SxLc0BFUDVuya1X_x23Mh243hmgSuMBtljA5sIHJwTr79Kn3h05AE36Hs_9ZIWXatxNILyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGS5Rnsjy6mt9uXyr9TPEktPCSmkrnbXT5aO3kDIFAar0AKj5kfuxLwJw5xY4JBLCyEfxlnIzHthjHo5fKGvyJUi3EyGWVrnMaxEbBPhXnnKbJGXcAMKp8tuAADMytY8GxxDAAHUWymSuJriK2iNX-qQNF0i2w2H5c1Ht7yEi7FKkI3fSI16pPLTshr85sLqmVQy6ygh5fF3liWgpPI1t6ZUiw0rUYwOD_7KliUUW8SK3IMFSVAaaO7RR_qOa15tZpHem_xh1X57_BqdGPus4XHiKyFQ58yTUQ0Ar2k4C5uEO3JvZnOXqQzZmYxc0qiMD_1AdDYtTSA5gukq4PH0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=CF6tlTQ2GagKPZudY1Szcm21SklgvmO25F87BQHXOOajI2sAk6fnqQCECzU1u0hDYopPkr5Ym8zA6W2G3uoIrhMmLDhiRjcNNHak4DkeJ5ASkxfGjsSKAG0pxqGKyn9a-xjTniFPeiaYdFgkuX4tfk5lFU5WsruOdfO0AbZPvyl8auULLs1yGye4zguXcelOS5b1wvmbtEIEcmqK7iEsHvo93_SKFCC_rTVr8cgmEhtjIcKH38uzlVEQuhw1mPDffi4ugTkjsr9FZWJKrfGeNg8CEzv-8jSToQYMiPMzoGaMkFzLBFKn3OvAw0hy3Se3iAL8biHqfIxBtWfCRCl2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=CF6tlTQ2GagKPZudY1Szcm21SklgvmO25F87BQHXOOajI2sAk6fnqQCECzU1u0hDYopPkr5Ym8zA6W2G3uoIrhMmLDhiRjcNNHak4DkeJ5ASkxfGjsSKAG0pxqGKyn9a-xjTniFPeiaYdFgkuX4tfk5lFU5WsruOdfO0AbZPvyl8auULLs1yGye4zguXcelOS5b1wvmbtEIEcmqK7iEsHvo93_SKFCC_rTVr8cgmEhtjIcKH38uzlVEQuhw1mPDffi4ugTkjsr9FZWJKrfGeNg8CEzv-8jSToQYMiPMzoGaMkFzLBFKn3OvAw0hy3Se3iAL8biHqfIxBtWfCRCl2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=Qk3tH0KRP4dUN_kidD9IQLJSTLp1xAYY22owUkiW-dlDc6frrRib8zKhPCgx-HXFMnsuL0NK1XSqIEyeuDOtGGtEsrYIlaKka7SW6pJfVfqF3PxNj-3S2S7I7lEzL065Rv3ZlmH9ChubZGDAlpdkpxDGJr1MiruRdar0dObxCPJoCIHrsnkhYXB7Sn5j9bxybYH-hSAqjC_u-LmZPf6WDjaohcNfSupg3f2DQwQ64fyjTsysKebT4safIn_dLy38fYMpsVtOkLSkwdltVSp8LfW1cKHJT7tW5Bpt1CfAk3oeqMQNS8MEnicce4ElNwdO5H9C32Ka2xyxP20ncNgkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=Qk3tH0KRP4dUN_kidD9IQLJSTLp1xAYY22owUkiW-dlDc6frrRib8zKhPCgx-HXFMnsuL0NK1XSqIEyeuDOtGGtEsrYIlaKka7SW6pJfVfqF3PxNj-3S2S7I7lEzL065Rv3ZlmH9ChubZGDAlpdkpxDGJr1MiruRdar0dObxCPJoCIHrsnkhYXB7Sn5j9bxybYH-hSAqjC_u-LmZPf6WDjaohcNfSupg3f2DQwQ64fyjTsysKebT4safIn_dLy38fYMpsVtOkLSkwdltVSp8LfW1cKHJT7tW5Bpt1CfAk3oeqMQNS8MEnicce4ElNwdO5H9C32Ka2xyxP20ncNgkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6_6NcZsDaxVD1IpBLEO11HavonOwE4unQCA9D4RU6RTpX0nVIB6i_8RA8Zm3u8B23rUrVtntwWsGQkIfTrXdVrwrRP_x05aNzLxtF1vBGebv4cMvZehg8oObe52GyHM1Cgm8B8wfwTWRjZONX4Dy8EJiYdXPUJseJ-VPteA4PZG3QbFzB1xdas3TncXFHsPhUacjqylEjaEqe7qa5Sl4wqeT0l4vNvXJDRtzKuHIqpIZCe_3-_HFWvsnlGDr3FAORSHzQObJVUCqg0fJz7R0KHGS6kEw68hPbmjV5yJHh1hl_uATIjLYPi_hpcvBvYjqdGKRsVcw2xXcuC1uywlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=QiwwCbELr9I17cHXkGW6E3X9d0sxA9B0d5zsR_yr5uuGtyPf4mxFHNbpvlaLXN5igVC4gWVElTEEiTBI0L4kEBRGbQgTvePYJtsC52KmuBKgn2Nr9vsOauH3PxoTqRTBDuFPtvb5cpStUpw6K5ftLqPbvu4gm7FvxYcMxXLOZksrkE_47IXxNI2imrxlO9QyYGmhN0hHIzo6LP9V5GEYE4Ja5njtbFhsi1-xr_R152nPZrXhwywAO0iA32nsPVN5_CxKqF50zTkFfZYSVoTmM-tidtjxaqhgrOQyIKeW-k-p_x5dLOakWx_X9bz72zR_1aHiNWgeRmNLDn72jhl6AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=QiwwCbELr9I17cHXkGW6E3X9d0sxA9B0d5zsR_yr5uuGtyPf4mxFHNbpvlaLXN5igVC4gWVElTEEiTBI0L4kEBRGbQgTvePYJtsC52KmuBKgn2Nr9vsOauH3PxoTqRTBDuFPtvb5cpStUpw6K5ftLqPbvu4gm7FvxYcMxXLOZksrkE_47IXxNI2imrxlO9QyYGmhN0hHIzo6LP9V5GEYE4Ja5njtbFhsi1-xr_R152nPZrXhwywAO0iA32nsPVN5_CxKqF50zTkFfZYSVoTmM-tidtjxaqhgrOQyIKeW-k-p_x5dLOakWx_X9bz72zR_1aHiNWgeRmNLDn72jhl6AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldIQ4QqBBFsZyRV-dcc-NC6zMVgkJK4zv-lBX0UfeSmzrIXsq_PrT5PnqsZGicQjrtu5HwT8dY-lYaArNq6vtX338w2tGI2TKbgW82njqfElFBvUueButQ3ix6LvFRp0pgZ3kNycjkseFaX9djLerL9mKlyYoBWDKlE5Dzg5l_ytDGaamvucG6-lvADmXKUCajdAXdOMQ76XinYGWWr1m1t25xoTLOAuBM3b_FxgcqBSSqpngHJx5hzw2M_SJ-FGjLLnRV4LB1j79N9tTCEE4NowFaUTYzvDm7AB1NBqNZ9eBOgB_TGjbFS1tJ51KHFffe9dYPcTL18AUm1CfRn41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHJX5EgqQIx5BEq2IrryZmcM-APSQpeBql4gtICvcGyaQNrbYc8oCDpLcTaGpuyNhsJRWSxVhQe7GFJvSiVZk8pnl0iMJdHYlNTMB8Q2XJPXKcVs4pHrBpqmVieaMcq_fSQLpLbW_06BCAW5CT-XsjPifhJkxrQ3ub-f4UPCRkEBd4dCKKROnibQz0BT3TY7scs94hlEWMgVdUSV-XPVK5H9GS-zam0Un9gbQiUY5HhBj0l50agO3sPaqir1gjk2-D4jPqH1DSOhreGjm-MUUmg_WGj8ibrlmwusDJjHvH25OSiqfmnRtGx8Pe0iuwEKWdI6KED_Ap5CPHZFpk2VOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qREbQdkWlzMXrpRlZG34QtlQHomMhaGP1VBmS7DR6iTRGqpelaR9G0qweGgKlMCfUhNAsrTpPoUR4j6WNcMh2MsN7Kfs61z8ZLx1jfhksdGUSArEjWpPSiDgot9kas9CttqiRGAsEHg4yUs2a48R41nmcVHTc9kJX0SRLACnSunqUuYd9SrumbfqSABnLOZJye0RtF4pYCrBx1N7vM3CnVnshUMCTgEDSMFTUsfKDbX6aDwE2I73EXPcgdrE1_CaspESoewc9yvyFxfeACSN64O6OMHQcAu0XXsTUcGItAMthe-HIyWgJ9y9PvaLIPQcmfI-I81y7CfTpIJauAm0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv3kUgs0oC13Ek03YKEUjfWLOw8sPnqrArJCe6jcuWhNTOY5HACXJMx5mOqlwqjrZxEycQnHl3PNKadYaQxuGp3GKrgFFiyExVOOuXFCmtRms3L1LIM05MIv6szH7FiiL1uUFueN2IbvSEhYTCdke1VTMoh_CasK_KlZA2BK65ivJi08ZofMELDVa6ujjP_ou-lLISFq7G3_RfLt5ANd-h0TOPC8eFawwYkwTdSqoX-TQi6ZpWAbsVv7VGfjtcUZHSDoYOFjDxCIxJx2g_KoQ9RN4cSC2iOM8BXMvoeN8q3O05AFcRtRp_rtVH1wFpIvKZ2Qz9fSKaJZRqtHvs6H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRHeuJCFEi2DXB7wjD7UgmV_p2op7MoJQYWHOJHzE37jXFRXZKwddNeCp0eTsu_0lGMmP0HJ1eii_F_E4m0-2Q0XKyqt9JkySYVivVrTC11wHnmaVmaQhlZ3rx2QSqiEXsYsFb5t8-dRvhOfwCA43-e5xPTtiDFJK1kqx_xh_DBZ7kuGume8q_yDuCwYoLV4o0rDYsg4J9KNWK44j73TiFM__yTTvfxgLPdD2C88RDqG1qp7i2kvP3IcnxUx-M52XPfT9wDSiy7MS0tiCYislA8hU5CtN7QbI1mwOhPsayJUU1LGcVgFJxmIyLkhHHrJYINrSsAEAVgkalXYixVWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d61IJQjZC0-cLPGihUpfveOhAyFnNrDL4g_wh9UUtZvX78xg-RPMo4iVkX7R66XdwF5FroX_TeJoP5VBj9KgdpsKbyOrafQppgS7mbNKw68EY-4WhOiPKFNc3Ru7AFpsTy5txHgiRiCN6cYBF7YTe3j5iLGs5mtchM31HHfK9wnZhtZnMmpuCD444L9lo3YJ0e6h8CigVYpGRaJiAwvJ0VHFre3hhGcDSqsj5AJy5EGdgP5bQ4NcU9IrJmK2eUGa3yCWkW4-oOVs1YX2xJ06pgjvVTd_ZEUj7Oy_MGyX6H5eARGYjnnX5Hg3pnyZ4LMhemqrRwwt9cap2BiFSu4s0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7_S-kF0_3VM3C5kRJtBq8IX0Vtr7cBUI7bPdNW9WD73QlNvC1asZixRVIRmjR8EQCJCmRTqXKow4bhNqZW5lmVA4Nd_tRVG9ZAL4nU_Gq7TZwfKeTTwDgu2b99JWBLdLm_CBDtbIqLBEr8ELE634iJY_t4JOdnjTHLcNbLTRBqicpoP1GaBFbbTAmudABheGMT3HkC4ipGgTtAnqNKpEXt1XtJ2PuLoeDnCIXPcrB5qDvvq6dOvxn3Wwjni3hKnv6KoGbFuPz90t43SjrKdXSiEpH86f4D3bCvTEg92FlcIrC110wzCM2OqKifO1ds2_-0_8o3UWTJacQhIVZTFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaI4rBMz7WLUWangKzAd73qfDghhQbiZB3IexGgayk8ZMVn6eOW-76KSYBf7JUyO12NMIMPMvqoMABmWYzo7pH7zEnkMPULstHWsDkRBa1U9Mm9g9oCJUYculJz8FAyGT9cH2D9-mSDNblnH05Ms__MIWi2d8Mg0369S9F4t-WN9Atn9ZOTTT1zG_INaYjiLovTX936xxsmoy-76eSy8u_s69K9JV023kMShNhxI4JBAadgBp-NvCJSq00zffSkajOeeh-PFilJjMa9fXXK9_TX0u7aIQf2FLJnOu86899xFI_qszVM2v-8kLiJizglY8iTL4k2JTizQVCDPstzIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKmqo9eWK6sYJlGNC4z_TjMPby2Z14Y2l9L6xqn-cYgQ32z9ma3GPtqYSIlL3fuFLIP8p5M2NhUGwUE1qfkGKVIO41mp9-vXBS6Nziova7kNWOyqI0o4qM5eIdrS1ZJzF0_c3GwsTT7Gr08L_BKyLvW0fAkQCoMZQwF9tSu87cNArAr7951Vh_C3PFewSMkMZlQ-bGAkFPrCygHIVLmnez_tK3ayc2UOIIiFBi6pGUieeE0zxV6HI7fL4gL9mrz76Snf-OeoxoFCwGMm6n1BY_3icCxMRxTmZ_xRJrajodLtSw-AA2p2Oxef4Oo4Ln1Dj-nkTA2zgOqfZ5ihk1DDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=Pr3DYIl6le_BEn7Kf7OTHyo5qv9gif9QaMK9IliC6EXSXxV53lXce8W12Xq8LvyOPq78ZSJOzsuaYXAVK9331u3kWAEpHtpr2ihvVTxNsuuivHdfKvPbbE10T-8PN_44mD1DJaMZPfx3jDC5b7nrVuiToAsdCQdiwrx0hUi9ZSq_3GZkQ-UrrjBbjzltS320TN06vW2FJsuX0QvQuXs100eiSNAjRCEri2qdpuiz5OO5q41nOncKu5rynMGbhn5_wgOsSM_exdgBuIqQ-RNWoQ-JM2oh-FQFdo9tBEyGqMRjYKt5Jgh0l-latKGIHFMdVAXsqZUsZfFr3O3R0bECDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=Pr3DYIl6le_BEn7Kf7OTHyo5qv9gif9QaMK9IliC6EXSXxV53lXce8W12Xq8LvyOPq78ZSJOzsuaYXAVK9331u3kWAEpHtpr2ihvVTxNsuuivHdfKvPbbE10T-8PN_44mD1DJaMZPfx3jDC5b7nrVuiToAsdCQdiwrx0hUi9ZSq_3GZkQ-UrrjBbjzltS320TN06vW2FJsuX0QvQuXs100eiSNAjRCEri2qdpuiz5OO5q41nOncKu5rynMGbhn5_wgOsSM_exdgBuIqQ-RNWoQ-JM2oh-FQFdo9tBEyGqMRjYKt5Jgh0l-latKGIHFMdVAXsqZUsZfFr3O3R0bECDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilzugj0OHgjnzr66WMn_HeCo9OlP-sP21naJeeSZpo2n8nrF1SLXmItJarCZjLUj9nMVEtFvSPjt0NT3aDSLIenld-tUdxdK2bQW3Elzsw_a7JDpvpvksOIMx610RGckrRRttQ74zt-76KXk1ZGVaKy6G_y66KoUDC_8N-67tRyqkBVCEuzl0kjRjLACrIp5ZGTM-d0EXMh8JCNzC9ViON3m7aQ3TSqXauIutIufDEHF9RmD-KsMkpB9L1h3LKxli66tV_cwPAjvEeFCxyOdlqoncCkSafRoYWEBYyZCDqma9_Xj8wMxHxlumKe3cbE6C68jorkLHCnwwNCIj0yODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rikiULis5lmOLpCzxAZHtN9yz8w5XS7KhUCmt9QDfGrOzy5uudIKGzHqKBJGC371ghmsdJdXrehWLYsdqNjo9unmkVfh4qmbQ91gKccw2GVJnc_cimpGVfDtlEZJVf9_w52nqRaTXRgEfv9ulCESTmXcBobuHJOv6r1Nae7NMYID0kIYRQ_1b1W8CW6tZyXfFqTkc-iWzyEZv8wYQdmP6RLLvXvXM7dOqG3YkAUw-X2MhF-wfJgXygkYT4ZnjEvgQ1MYMoXKS9xnJU7KQJ_-gcd4Bmi53eg7bYFbsYkqAV5inoinZDXW4BlenhPRcl_a_2rIy1jxHkq4OVJacU5x7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us6gG1HrKEqB9Xv-Zaf7nprpmHMAS6TtGasXZuHYJez_nE6Vzbb0pj9mgvuArQO-PFywZ897-CIK0m5YAYZWmiqynCNIJwGCRdwN3XZ7DMt9EqvCGneFXlxKpsw0gvVijXhh_mXGFsGHj6IeOrkuQh_Gh8-4vsQ2DO9PunAAcWUHcbEc8nFc16WGmq7XDaAgUMTCB9jWnuUPqtBuqnsk9Y4bVi4S_r34jNuZ4EF9V_7hRaHrSgKKXx6RWUmyBmzCFaE7u4z9-yDG36A3I31QiEnWd6gs0zT9k5u6xVDfDi81e6BGag1xxrcXoFULNej6RCN4MZ-a_4cWyA1_N-ow3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=asSfJKcS0ZMhmjHYvt0pHPvltCqur0ixXvQbh58pL4djRr9g43nXv5cswpjBj89Dc9X69evKJDVBM8_RvS1Be13lW3ybbugYXEm9pYcZPhnNklYgEaP--BtmvidHZum5--jst3Q5-Zxem57AgCB16TSedrXpzfrWCbGWM34_Vw2xU-fQrAvX6enwQos7lpChpbuh6PCWuAUaLJjufDN5OSEGjGZ4CzYH8R3lVCzfZM_uig5VMrRUC5uWvadILxWR7hHBufxEM6zry_vwfMssKKCIMAhcrQ7iluBzaN2Ny6ehfBoZH4MQYBh_XVd34meO4-8tG1WokHFzOltwvQcV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=asSfJKcS0ZMhmjHYvt0pHPvltCqur0ixXvQbh58pL4djRr9g43nXv5cswpjBj89Dc9X69evKJDVBM8_RvS1Be13lW3ybbugYXEm9pYcZPhnNklYgEaP--BtmvidHZum5--jst3Q5-Zxem57AgCB16TSedrXpzfrWCbGWM34_Vw2xU-fQrAvX6enwQos7lpChpbuh6PCWuAUaLJjufDN5OSEGjGZ4CzYH8R3lVCzfZM_uig5VMrRUC5uWvadILxWR7hHBufxEM6zry_vwfMssKKCIMAhcrQ7iluBzaN2Ny6ehfBoZH4MQYBh_XVd34meO4-8tG1WokHFzOltwvQcV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVrydwSIn3ALqCqEXn0wco3Mcd0vqbtfoAAd7ugO4f6qHym11rc2ejTjBqQGy_dx8DLKE4fUb-uF-fQzxrj7DUVTdAAIzJHhWbDoaHw4npRDgLL8FgTXXxPhQrqiX1lblkn8D6KmndAbcyCEiEaTo0so-VmfH__wvqTWL3sMHQlv0p1E62lkDMeXkC9ehCJ_qEQTJdDDEwsNUy026D3bjxcovLz5PulxSg6qTnrvExD7tBJ6fRwiLzClCzes8KaqRzXeD_Z4YlxG0w-a6YoMuDjy_S-nQsdtAXzbdEXBrHlSYAEss8jtqjKudACbJRCgrmcA1xrrj4OIawlbYydP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=Fb9YovSWu4NYrCKObuWmaCjTpAl73cIPMWqO0vAq_4v5bh-5NpJkiddJRm2uhcEzf8ocKa9UrO8RDenSY8TtcbsDdR-7rg2x0UQx9GMOtBJmslmkLxFc_8_uJBuYakxoRZMEsaTc2aEX7BEz8uXW6K0JJnuVGXzx9muBNnfFsLZu4wUxZy8tbRMbkcrxTZh9r5LTGFWJi86AlV6fZE7JHW_P7FRVRLZbRZBJscoW_fMhZV1b9rCspDvjxTomKgBNZ4TYK-m-01m9Jg5w0yGXlljb-BUdOL2DRcUN-bTiPorf-Rfzge5chd1S3Xze1zE90yf__vX6xOzP-YWXwvfXdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=Fb9YovSWu4NYrCKObuWmaCjTpAl73cIPMWqO0vAq_4v5bh-5NpJkiddJRm2uhcEzf8ocKa9UrO8RDenSY8TtcbsDdR-7rg2x0UQx9GMOtBJmslmkLxFc_8_uJBuYakxoRZMEsaTc2aEX7BEz8uXW6K0JJnuVGXzx9muBNnfFsLZu4wUxZy8tbRMbkcrxTZh9r5LTGFWJi86AlV6fZE7JHW_P7FRVRLZbRZBJscoW_fMhZV1b9rCspDvjxTomKgBNZ4TYK-m-01m9Jg5w0yGXlljb-BUdOL2DRcUN-bTiPorf-Rfzge5chd1S3Xze1zE90yf__vX6xOzP-YWXwvfXdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnoqpGV9w49z42QQMjelQIt_6fk9PXM6nWeLwSMURl4ftUQeyIhOIyj7LuClUuZJsXTc73bNZvcJUeC5u8wFSG85WSm3BbNBepOAHH4ChxqWly_ujFJ2oQCuQ-sTN_17YFz7kWa05sBQLyP6ZdHQOsAk2gGoI0b_jYNz0agE4tol3xeX3sIqgZH2-AXYro7Kl2QtXfVcBjzPgIsKM0xQ23wM8f1W9cOtlLbdN9C4Fw9m3gwbC9P0rq4W3pisqUVgMrHtAezcleP2qD-MpI4qwJgrMsKYK19Tizo-9ZjBUUk6i8Rqxz0BuFwdNu0xoLiWD4cVennr2NE_g0T9I0JeyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
