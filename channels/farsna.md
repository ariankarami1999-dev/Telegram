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
<img src="https://cdn4.telesco.pe/file/odtcdlrOfbkelo_Vj87Q4oy_rman3GbbIdsQfEU1oSJPRjPR4lZDCqJE-nT00AyG5R1m27JjYntj7KD4hzUFxOHYUY-e4ndGfWS1smBdevnyEth941pom78-X17nLHCC_QILDblKxkQ1fD-ivgwVH3hS6h17F01-tBrZfGlo0TPQGmHOf3SBTPUmmalzoT9NGUyrxRy0rrmpLxy0GuAj3YTzbAElF9hpRLZyhfLUcojdqoHCS29ABCxg_i8yL_IE-mivZoqgXE4QW3shrVX0qbSgMq21uTtgKIrBY3jKGh_gJcWxgrZe_As4VcuI_5OCJYHkS-0_K2LcF3qjGkuDng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 14:14:35</div>
<hr>

<div class="tg-post" id="msg-443396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUxS7Wr1Am4FbtfuGlqHwLkU0Vxq8cR1hZZtqBi3h4S6lKgibk6-JmMRGfqvMO8Wk6f7twjZChEo4Tz6CEaRj-dn8vjkNDpjeivHs-csN0dzYAkanh2Y8c05H4xOOGU_oqO7cydyN92PWvz6mtwq8JWdX1ez47kxNZymXWKGBaTaovagtyonaPIDHQIsAov5B4LGU9L9BSJsSG7qs7D9ezIptvcHXbW88x2WHDcRTiUFE90-e-whZ70wesber4Rgf9kkw9MGU8VCRskKNeb9lvrW_vLNTRLdo64zBmuKDOB9jg_XWQpOJgRczkajDpJAzJxbiHjLauNky_vAocWh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7Xfl6PtMG3FTRK36wGZb83tKJtYLlSf81D_nIV_iD6cwAZ4yIlKXEfBtrHGcmX03N6rKKDxGYXuKGav2sCNFQSJKmRJfv58rAAT31Fgyx79WTSIO3r--IpkbBIqNprOWPMnQ1Nb5iO4bmZCfUHpT7z0VR5ujkxyI7qOl2dAtHeB0fGh75G53xg_KVfl7qQtQY1nf-uhpl5fQ1iWJKaC57ZOlRNfLUGsiITV1i3qTtdN5iKdcXPaIjDH_W9nYNjEHZtt28ehWj5mNuZAHiHBxHVA4OlnFwA7qspBP3rI6ZWG1DZIRXQEjE_7MiIMp-vDd6yDCK9jEuCeCkxfmqNP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWHKwVs3W6blTtIOrphvTyWzlyvk9iqctjtx6MqwHRFVTCz5QYs9QTuQ-JjdrxFIQsOTsy_5b98NzgFJiIsquvIK9wqj0jhINdvHBYpMRH0D8VjirR-QUhszDJNrwFdFNgPYt3mEkkHB3smtffABb5XmK2mR4iwXsFP9NbUpoLq2z-6Z5lPyipjvuVi7MN6Ya_ifIy2nLBDMbRr8oLcU-v8S6nkuT9p6-U7mA2XxM46_aC99MtIxB7cRkreurRNoWRLpdxHcLburLleogAS-Ek7uttJ_3RMANyK1ArPEEbqODaciI9jKsEsi7q9vXkzPICcAllgbry1XOB6y1iK-1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بلوار علوم و فنون به نام سردار شهید امیرعلی حاجی‌زاده</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/443396" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKs1Krbp50502Bzaoh5dqJzfROHda0G0ht2r11sqBbgSzqcA-iqzC_vixscroZemSvzSVSHnFffJxj6fQVvD_HWDkYae4XaifR_p4eA8oK-EWurSkUcGIfsOgpy1bWYNvhPIzYVQbsP5f0pvQR2hdaVEruYXCQVGAL4vVrkpGvMREv6YMk5qKgM_gCG1bKlzi7sjvzCegm1GOGgR52v3Ua6UvgFnmZ5fSA3zXYaQta3RFqIklJc-UYcuBp68S1THwwCTJ60w-qd9BJfKqPYX0VruAWKyFt4z_pmsGbC21bw1-Edf_0PCyfQyj39k7oNDOeI8XMF3dEjTK16M3i6Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سگ هار آمریکا
🔹
کاریکاتور کمال شرف، کاریکاتوریست یمنی، در واکنش به حملات رژیم صهیونیستی به لبنان
@Farsna</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/443395" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4h3F521GeScM19G-bguUVQbLRvUYYGZRsiwA5qkLLCW9ojhYzjhQbpZHNgnsTQ6RjN6oBbNpNv9t7TNWrIFIpAcjFzMq8TYxma7gK3YF5SdDqMYYQbyc0Ny48u4IdMoBg9w9JMw22jB8QpwfrWQpFy0MrEqIel-IAzKZlNlhsRMfZpjLugRNXcwM1tEVNCA_2h64Q3_TJOZEhb9k5_1nqlfM_FBuMTsPa-2ICHqsWQXJdOtS3b9KhyB-iJo9gouLcl-sdoRwczVQmoo8jEAzCoZ7znZ-ZJp-Le8VC7A87RomUaQJdhEMpoRMQEauZ4prMZbcJJgZKOn1BeQEgQeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
همزمان با پرداخت یارانه اقشار کم‌درآمد انجام شد
✅
واریز پیش از موعد حقوق بازنشستگان کشوری توسط بانک صادرات ایران
🔹
بانک صادرات ایران همزمان با رفع حداکثری محدودیت‌ها در استفاده از برخی سامانه‌های بانکی، رفع نگرانی‌های مالی اقشار مختلف جامعه را در اولویت قرار داد و در گام نخست، نسبت به واریز بدون تاخیر حقوق بازنشستگان و پرداخت یارانه خانوارهای کم‌درآمد اقدام کرد.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، طی روزهای اخیر و همزمان با بروز برخی اختلال‌ها در شبکه بانکی، اقدامات تخصصی جهت بازگشت فوری خدمات به وضعیت عادی انجام شد و عمده سامانه‌ها در کوتاه‌ترین زمان ممکن در دسترس عموم قرار گرفت.
🔹
از جمله مهم‌ترین اولویت‌های بانک صادرات ایران همزمان با برطرف‌کردن محدودیت‌ها، رفع نگرانی‌‌های مالی اقشار بازنشسته و همچنین دهک‌های کم‌درآمد جامعه بود به نحوی که با وجود اختلال فنی، حقوق بازنشستگان کشوری بدون تاخیر و‌ پیش از موعد پرداخت و یارانه خانوار‌های واجد شرایط نیز واریز شد.
🔹
قربان اسکندری، سرپرست بانک صادرات ایران پیش از این در مراسم امضای تفاهم‌نامه با صندوق بازنشستگی کشوری، بازنشستگان محترم را ارزشمندترین نعمت برای جامعه توصیف و بر رفع دغدغه‌های معیشتی آنها با هدف ارتقای رفاه اجتماعی تاکید کرده بود.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/443394" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPJoasMIt_UyXwlxtMiJ0y428ESxYPIah9l7MYxZamny5DNU5ZGW88PpsC_EH4LrQ_k5mGNlrrZXwAzqgoADzuYZtM4kLrsRpMktc7dVF3oGvo29z8EN6_4dQiNBwAGjCTEkl22Su5kAYeNZLX8qu-S2H8XFPFjkzCA1KOCGIdmIt_jUg686SVx3izBj15RId1TMp5uhWquPFoAk9UP0dtTIJYK9uAn8YtWJIcOQwjRSF_84DmPrySOa0sAUeHUoSEEbFJZWGQU0MT_PkcNdmEeAzvg32DyHsasG34JW_47mt1ja9fgwxWGLqEKj_a3_fe53UbV_L0pWbnQ-QZ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/443393" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/443392" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAVnYVfAp9tdOS_WNzrCKhfgW8JqxpwsPLKbzpcm2_y0lDhG7bG2np_07EkBTipSukbck5RP8LAO-s2wuH2QTUGajIqRa-rNGzwgnPUZDFy9PSvYJYVtIoKbMOPj5Rn4MT-BiW1QMjWIDkmF1iMZ3fGQ0G0t1cLoatPT4HZRSx9gMM07QOl87I6odlxHdVh9EBVDCEeweQDzIFwyMPyrsodtsQVU1Z7u_Af5amNNS8jKtzsRKcVuZpXXJYPKBXwQLaVZVWLPGj8CoTKD9oRk6q7ySDT4pEa9aRuCd8WGoH2gg19veokxnuu2YT2jTFhmnpRTCxIFUeeiBPFj0wlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم آب دریاچهٔ ارومیه ۱۸ برابر شد
🔹
مدیرکل حفاظت محیط‌زیست آذربایجان‌غربی: در آبان سال گذشته، ۲۴۰ میلیون مترمکعب حجم دریاچه و وسعت آن ۴۵۶ کیلومتر مربع بود که مقایسهٔ این آمار با شرایط فعلی، بیانگر افزایش ۱۸ برابری حجم آب و بهبود محسوس وضعیت دریاچه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/443391" target="_blank">📅 13:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت ۳ لیدر میدانی و ۱۴ مزدور شبکهٔ خرابکاری دشمن در ایلام
🔹
وزارت اطلاعات: ۳ لیدر به نام‌های «مراد-ع»، «مهدی-ک» و «رضا-ف» از اراذل و اوباش سابقه‌دار شهرهای ایلام، ملکشاهی و سرابله که در کودتای دی‌ماه ۱۴۰۴ با تخریب و آتش‌زدن اموال و اماکن عمومی و تیراندازی، تصویربرداری و نمادسازی امنیت را از مردم گرفته بودند توسط سربازان گمنام امام زمان(عج) بازداشت شدند.
🔹
از لیدرهای بازداشت‌شده ۳ قالب TNT، یک کلاشنیکف و شمار زیادی سلاح سرد کشف و ضبط شد‌.
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/443390" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ توله یوز هلیا پس از مدتی ناپدیدبودن امروز رخ‌نمایی کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/443389" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWL15VcPl-8p-MsQFy5heSwbkni_4yH2j1u1q3kCTJtNd3ilTkBZuYRFy7b9hyhNpMRPfqXnYP62WKC8NzK6iJPmr-ancuRkxDWusCNJnkBHUA3Dqu64C_2wPFzUy9tH4ITYR6HG3UwUyra-Ng7jXZqr8TZsRyTmIxF--zULh-vJgaQE8j3pa5xMCTVHsde3_Yo0PqBShKAx8niAWQ6fY2V5gafrIa9FX-02PkohEqFnJszQMLQyHh4ia0Pu9FZID-L5cpVnrTS_U95yrL-OVr4j1_QaVnsB1A4eiVEwOvvcD1uuhJ9BpNEcHwaIPlHa8L_xCxFtDGkjqkNJs4fPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل جدید دریاچۀ ارومیه آغاز شد
🔹
دریاچۀ ارومیه که امسال با افزایش ورودی آب پس از ماه‌ها خشکی، بستر از دست‌رفته خود را پس گرفته بود، اکنون فصل تبخیر آن آغاز شده است.
🔹
عیسی‌پور، مدیر دفتر برنامه‌ریزی و تلفیق ستاد ملی احیای دریاچۀ ارومیه، به فارس گفت که آخرین…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/443388" target="_blank">📅 12:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم سوم این مسابقات نیز از طریق دیدار پلی‌آف برای کسب سهمیه صعود تلاش خواهد کرد.
🔹
طبق این مصوبه قعرنشین فعلی لیگ برتر یعنی مس رفسنجان باید در بازی پلی‌آف بقا به مصاف تیم سوم لیگ یک برود.
🔹
نقل‌وانتقالات تابستانی لیگ از ۳۱ خرداد آغاز می شود و تا ۴ شهریور ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/443387" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRs4UqFYOw1tsdeIAhF8aHXFqYl352jNPOmJ0Rc0y_nxzzp-tSN7oXN3_YUcYIXarSlyvVrhiliGAirsnRsy-z9076keRTmTNc1HbNjzwwvV1dvcOteuPeH96HDBsAlZoxyKFX0toAL7mIHIQxz-AZYZ3bUWNUKI68W62PJ08lTUp0Fmxc1NvAuU-VIkH21ZaPQv3pYht_7LKlgnv9HeO1Pm8fvfgdrE_HQB_d9ANHTVVYyOxyVFOhsiD_4v1H-dTHbVZG0487R1BgnpFpszwYixYbg_igG0RYq2NGyA1siDUtmu_Vkk56qgIjH0kyMW8F2USih-ZW1DcOp8En1Auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۹ هزار واحدی به ۵ میلیون و ۱۶۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/443386" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyAIdypnnRXXdCRnLv-VdBN69s_tm-yKhyWF5POYBXbDZiw4Qlw6JA1LLFhZRhAZrDeBCdhGySGE3oWmaUIEZzGHD0MmN3Y-GynBelXvkZIYGVTWHTRhDVGE_AOCvhtf8XP-YVyMgLP31EuJfEF5tBMA7D0_wvnI1oPuw4w5r2CQZyYNGfCsQiS6qYxcfemYSd8NDL2J5w90PQ9Qb7Xb4X7oGvG003l_ZV-c3hit79dOmPzstabpR3QkzP6k6IxURzJGmGZPj_SP_vdgWbw_hcgTkfJMdYl4Yb6xBEIwdEFmzPbccALqEROokMB2-hBM3I5tJM3DtGlirnFBo0BnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای گفت‌وگو در مورد مذاکرات ایران و آمریکا برای چندمین بار در هفته‌های گذشته راهی تهران شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/443385" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4PsPE8HBUheRqdkSKMOl0QnbT_zq-MygUsil5Zvdh0vA96rdxu8vA1ynm6hfA8Tmkun0yKmIpI7dTwkgERpjwT1uLaWL2f3mk5jMYEjKnE4M83bqKk-U4H3-wGUzfb_FYLoryfK_-8O1iDG-vkopgR4fWmwcVYSC3PuH5bYxSeN82T4_1jXeh3plLatQwtzHIFZvtRwMJcuP-VS8ytrUzkbjaiJDn8vF8jB09CRU4PsFPUTBLC3iLc8OJZzd2PBsJDbv4gmDsR9TxFCWDhecWPbT4yf8UaHpA0uniypii-ZTW_-8EhI6RYN3LQYyRfPezM4bpYLuQeMXEszzDteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/443384" target="_blank">📅 12:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443382">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kynJdSzi6CI8Kv3BWgAlVAb4rR-0cc92CXx0bDy19Rpuykpzrqh5FmzZMZuAxBkdX9il60IBa-BIYieYOMASVCoz6_sDtV4JztgPJhKvAEvT8V-I1BGUbMcN0E4J_npDjGqgyhFxCciLjPcUBn-JFMTVLXPbDl-YZAAavTuQbtsBkVTZ-n7uMLeLKlCCO5R2fAq8zxFPf0xikQUFcn-6lHKxJNnFJNXRkaBIy1zKv84vaqpX4h_zpnn9rVBE9-Q8VnlUZKS9Vb-J3PTlAKxskQVUerqX0nG38wrx6ypmBPO_xS_z1MsoWMh6cjDC-MoL9sshrr9-aRFixPxqgtJ7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anq_0joBi53N231kH_ukqTKal6qJBs2MEhyOJ3z3vFZsxo2aE4HpoOKBGzWS_KAJjxaC3D5VTzNTZcBb2ZDTHvFgBT2Dwv9M0wtBUxaYHx2KNERCo1y9OUhxLJl8yEK_-_-mE-Upn-akcAHqoSHz1a5NLI_cB4bqYkdEBbx6_MtIYY579MaaIp3pVHkIBWIGxUeY1DSifHvnCk25noaC_VV_vblmKi_wAUQA_AKJuHk6IxWsScVbA2ymlacp5BaHulXRDvrR2dWaSOLwu9XeFaPnOD3aA6_eL80y4SDFmNCam1mc8ZuMumTfKE9fmWbcWDogv7Mnt3eyZaTUehnKCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی:‌ تنگه هرمز همچنان برگ‌ برنده ایران است
🔹
رئیس جمهور ایالات متحده،‌ دونالد ترامپ ادعا می کند که جنگ، ایران را تضعیف کرده است؛ موضوعی که بسیاری از کاربران در ایکس با آن مخالفت کردند.
🔹
کاربران شبکه های اجتماعی بر قدرت مردمی ایران و تسلط این کشور بر تنگه هرمز به عنوان دو عنصر مهم در پیروزی ایران در برابر آمریکا تاکید می کنند.
🔹
برخی از کاربران آمریکایی با اشاره بر مقاومت مردمی و نظامی ایرانی ها در جنگ با آمریکا تاکید کردند جنگ ترامپ نتوانست کنترل ایرانی ها بر تنگه هرمز را به چالش بکشد و بندهای تفاهم نامه نشان دهنده شکست بزرگ آمریکا در برابر ایران است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/443382" target="_blank">📅 12:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWecX2YqgN5YGLaGckJXvD-VauEi9KDM9JO3RJnCjlF9RESjR4yLQqUPCZY0MkKIcFB6mIdC3-EYuvcm44DfFtFcMKpuezRaqBOPBgR5CO0KV8mqHrRydvvn9Jdqc_FLjyL5cf8g0AiMxPcUmF48a3jKOvQEzJmwCefD37l6haIUSqg8J42Ebn8sa63lprLHR7B_fdtk4DVvDtSmD74n227RzUr7jk0RTNJTLCrG_FDCZLWw_gPShVATNMHix2nb0f2iGzWB04jMgqoCcpVU6SYsG8X0-9o3-HZDkYe8ezLoTQaWrspLE1RosJxb0tySbohphiKahgzRkKpNEii5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در نشست همکاری پایدار اقتصادی ایران و چین مطرح شد
🔰
سه پیشنهاد مدیرعامل مس ایران برای توسعه همکاری‌های راهبردی با چین
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست هم‌اندیشی فعالان اقتصادی با رئیس مجلس، با تأکید بر ضرورت ارتقای همکاری‌های ایران و چین از سطح تجارت به سرمایه‌گذاری مشترک و انتقال فناوری، سه پیشنهاد راهبردی برای توسعه همکاری‌های دو کشور در صنعت مس ارائه کرد.
🔹
نشست «همکاری پایدار اقتصادی ایران و چین» امروز چهارشنبه ۲۷خردادماه با حضور دکتر محمدباقر قالیباف، رئیس مجلس شورای اسلامی و نماینده ویژه در امور چین، سیدمحمد اتابک، وزیر صنعت، معدن و تجارت و جمعی از فعالان اقتصادی برگزار شد.
🔹
در این نشست، دکتر مصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با اشاره به جایگاه چین به‌عنوان بزرگ‌ترین مصرف‌کننده مس جهان و نقش این کشور در توسعه صنایع پیشرفته، بر ظرفیت‌های گسترده همکاری میان دو کشور در زنجیره ارزش مس تأکید کرد.
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6R9
@mespress_ir</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/443380" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKEOzfXW0ah6URqX_dXLRV0SMQTaeRSIi9kzaPK3Ziaj5uCFsYE95oNlbr9Q-81-rU_WRcLKawOjGCqZAGE5PPtQKtr93ulNkQH9NEQ3hxYQeW1E3bBswogwfs9JUTuzbXPcTvnofr4ahaQCBJrnqOfr4OqN7SMTZCWC7fcyZUenePuq80XMv_gyLbd4jPWl2I6OZC-7grEUH4OpETX7XkGxjjBONZ1K7ecL5jSXNlVafGmlON41SgumFsw2El3UcByMsfoR2pHvq_GdKtJ4VMrc0EBeD7UtkmfMS4I8g7gyuCPyBHtcqiaogjEd1ZUrS5DtmK2t8knwor11hqjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
نمایشگاه پوشاک ایرانی-اسلامی در مشهد
◾️
به مناسبت ماه محرم سدن پوش با همکاری بانوان آلا برگزار می‌کند
📆
تاریخ ۱۹ خرداد تا ۹ تیر
(در روزهای چهارشنبه و پنجشنبه ۳ و ۴ تیرماه به دلیل ایام تاسوعا و عاشورا نمایشگاه تعطیل می‌باشد)
🕙
ساعت:
۱۰ صبح الی ۲۰ شب
📍
آدرس
: مشهد کوهسنگی ۲۸ پلاک ۲۲
◾️
پوشاک زنانه مناسب ماه محرم و اربعین
◾️
پوشاک کودک و نوجوان
◾️
پوشاک مردانه
◾️
محصولات سبک زندگی سالم
📣
تمام سود حاصل از فروش صرف امور فرهنگی و مهدوی می‌شود.
✅
ایران‌تن | رویدادهای پوشاک سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/443379" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/443378" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انهدام کنترل‌شدهٔ مهمات در بندرعباس
🔹
نفیسی، معاون استاندار هرمزگان: در راستای پاک‌سازی و ایمن‌سازی مناطق شهری از پرتابه‌های عمل‌نکردهٔ دشمن، عملیات انفجار کنترل‌شده امروز در مناطقی از بندرعباس انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/443377" target="_blank">📅 11:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مصوبۀ دولت، رقابت برای ساختمان بهشت را داغ‌تر کرد
🔹
درحالی‌که زمان برگزاری انتخابات شوراها ۲ ماه پس از پایان قطعی جنگ تعیین شده، دولت با اصلاح آیین‌نامۀ انتخاب شهرداران، دایرۀ گزینه‌های شهرداری تهران را افزایش داد.
🔹
با ابلاغ معاون اول رئیس‌جمهور، در اصلاحیۀ جدید، مدیران ارشد دارای مدرک تحصیلی در رشته‌های مهندسی برق، مهندسی مکانیک و پزشکی هم می‌توانند شهردار شوند.
🔸
در مصوبۀ قبلی و با توجه به غیبت این ۳ رشته تحصیلی، افرادی همچون مسعود پزشکیان (رئیس جمهور)، محمدرضا عارف (معاون اول رئیس‌جمهور) و علیرضا زاکانی (شهرداری فعلی تهران) نمی‌توانستند به‌عنوان شهردار تهران فعالیت کنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/443376" target="_blank">📅 11:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443373">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg4T0wbBen20x7HRqnUzvi9-wilAnngL68JA5gIdB_FaOL9XSMO4IYpzWoYCCj19M_16kNH9SbLsiuTdjgBsBYsHYjbCHWeanp2CpJhemURFghcgXFfOiv0dR-XdUs2Zge8JggLlSjBOjNzT9bFCabg91A5eTUx7NtaQrlMa7slgB1KyBA8Gb9DqMsyeLDCXe0LoAxJvaJWKrsg0Gt_Nz3jii5-8XenjBAGjBG8VNVtI6ArFhm-IU9A_6K2oU-3qu87IIflpqInGrTKLwX9txF6aFZNKJRAO27nzsuBUN0SfO5Yuhp92GY8EAJN9gjcZhWB59fmbam7gg165-OaNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcrmJyHDNZ14-sE_9TIES6bwIsGcpB1axo95XM3fk02sAiRy18FY9fBSl7pyjkLE2TYXyVvZ2QdjKVhYrftu94JMiEbp2HblUPFqOeDHaZPyV_SBsfCvu9odoWnVfgQ-AQchCKX-zBIyWTb9BfYsMqjCLUmf52b4O-GRNWTPZIvdTkPF3QTxrircTmROGCloSPpNtlblDVmVsgbn1Rzmepw-IF4Mc79LXmJL7GYIYZm18LtVl9Zj1x3QUFkxSKxYlSkLUz4NS9V8_VucUqOV1BXR7Y29nYHWJnQeSPuenZJB4B1xDFEQ-fPh2bYZjjnimH7VZZpg0sI1lo2Qd8EWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dngral8lRnURsP35IsgHkinSqPYGMUxteVjQtimSIAGZ8ny8RLD8nDy-YOX4eAl77olyG3OBj-b8lnrzqws0Xs-BkUrhjbgcNkewbqXujJzvT8ef_Ul3fVH2XrtWIoijreqsoQixOUAXYeoHzgZnSoQiF9zWHPsDBbYxYRJUlKInlN_lB7caUSlpZyK2xDLqxK9ZZE8w-nkUleoezZqGBOk54XLQFuqZeyAEPNGES5k5ZaAUs3CjMdwcQCIhiAymL82wvynvcQyxkdiHRV_EHC4tyDSrOIwhp9C5YTlQ61X5V9bdQp7Q4rbjGKH5FTYnOLOZWcDsXflYMJtcmvwKWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا: شهید پاکپور مرد میدان، معمار تحولات عملیاتی و الگوی مدیریت جهادی بود
🔹
سرلشکر خلبان علی عبداللهی در دیدار با خانواده شهید پاکپور، فرمانده فقید کل سپاه: این شهید در بنیان‌گذاری یگان‌های زرهی سپاه، تحول‌آفرینی در نیروی زمینی سپاه، ایجاد امنیت پایدار در شمال‌غرب و جنوب‌شرق نقش بی‌نظیری داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/443373" target="_blank">📅 11:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OioQASMh_M1KKCbjupngSkR2IUFNLcPsOJxXfJ3CVaPd7GHCLAhV6dgtqVsJ2t7I7XcgnUnOMkGTknBoDpeqGmnWcplWPrEHETncHSkiSz34FJyzQpPMry3-9jSxWrO6wXqm7I_RZJ_h56Sp9ZPaTjfVOvdXV8YUi6XEhMQKaKxtVIse9_y42lzvV5H3Ik51y4p0ISayBMragO7RH00ygM4xw1DOv28GASM4gn4kO2vVQP4b69VD4MGD1Tmg2Bze84MsK9fpTLrXW1QnllH3aZmDUeMQwQtx6-7OSpmrjT0JR-VMmWLRab2BbGYolakTQ6wx8hvlrrF4omh0qATd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۲ مدیر اختلاسگر در سیستان‌وبلوچستان
🔹
دادستان عمومی زاهدان: ۲ مدیر متخلف به‌اتهام اختلاس و رشوه دستگیر شده و از یکی از متهمان ۵۰۰ میلیارد تومان طلا و وجه نقد توقیف شده است؛ به‌محض قطعیت دادنامه، رای صادرشده منتشر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/443372" target="_blank">📅 11:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/443371" target="_blank">📅 11:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT8ATh_Ky_MqZOqFp6XP4pOYa0yBE0Zr2dXPVCKjTK1PFDQqcPh8mi1axz_3kTGWMTooZ7JMsR3j-3FgHdLjcI6PLfcDMQIeeDUrTN08DOM24hoJPA-u3PAipy1OYd0JVNw7p6_nlAd6LPjyORoEid3jfnAqwKpZR_2OXXH4ftc3pR3GYplGfBVFkgMrt4GkN9M2nyicLUMPl6okNEWQBnsMwNxPe5mkHfqf2GUpkDs_aPjs76HcFx3YeMDJ1SgwakDpUIHR0bPc-eeNOd6wLvkFwTUgOwjLwva8DYgtkiVS5886sY7OA1ZJ1s9f8DhoAaGN3zanbYkcS3TdWTWzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی عکاس ایرانی موفق شد در رقابتی بین‌المللی و در میان صدها اثر از عکاسان سراسر جهان، مقام نخست بخش «عکاسی خبری» مسابقه Golden Shot Photography Awards 2026 را از آن خود کند؛ آن هم با عکسی از مراسم تشییع و تدفین شهدای دانش‌آموز میناب.
🔹
این موفقیت با ثبت و ارائۀ تصویری هوایی از مراسم تشییع و خاکسپاری ۱۶۸ دانش‌آموز شهید میناب رقم خورد؛ عکسی که توجه داوران و مخاطبان جهانی را به خود جلب کرد و بازتاب گسترده‌ای در محافل رسانه‌ای و هنری جهان داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/443370" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bea1b4a2.mp4?token=Ud3Z7oFD-ff_y8PQsyftCGLPqlj8JhsbqcZYisRhohAC5nxV3E7qSfB28gvwR2aRhFqjv11xwVc0GF4N29C8ji6jQUcrUottzDIKN-y18ESy9B2tNYYuqxltvCNHgwzU_vGo2Ce_ot21IrctzxSt7_zmdGLST_eO2sHLX_qm_PfhKwusaHTIYAk10tBzAj0UyfNNXO7gBwTC3fyKE3iHsFQc6gXU8r5E8uSYPp12Qo8wB88mhfWwoHyvfC6n3Bp38pa72JrTYfSCCwcC-5g_Pb2zqy9t3N9BgezlFalNcZOiNlBwDMCqrwnO2UVckA6krTaSCzXFfrSI152pZsYHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bea1b4a2.mp4?token=Ud3Z7oFD-ff_y8PQsyftCGLPqlj8JhsbqcZYisRhohAC5nxV3E7qSfB28gvwR2aRhFqjv11xwVc0GF4N29C8ji6jQUcrUottzDIKN-y18ESy9B2tNYYuqxltvCNHgwzU_vGo2Ce_ot21IrctzxSt7_zmdGLST_eO2sHLX_qm_PfhKwusaHTIYAk10tBzAj0UyfNNXO7gBwTC3fyKE3iHsFQc6gXU8r5E8uSYPp12Qo8wB88mhfWwoHyvfC6n3Bp38pa72JrTYfSCCwcC-5g_Pb2zqy9t3N9BgezlFalNcZOiNlBwDMCqrwnO2UVckA6krTaSCzXFfrSI152pZsYHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: همزمانی انتخابات شورا با مجلس ممکن نیست
🔹
قاعدتا چون مجلس ناظر انتخابات شوراهاست، باید مجلس مستقر باشد تا بتواند بر انتخابات نظارت کند. به‌لحاظ حقوقی، همزمانی انتخابات شورا با مجلس ممکن نیست.
🔹
انتخابات مجلس اواخر سال ۱۴۰۶ و انتخابات ریاست جمهوری اوایل سال ۱۴۰۷ برگزار می‌شود.
🔹
تلاش می‌کنیم تا سازوکارهای قانونی آن را فراهم کنیم و موانع قانونی را برطرف کنیم تا امکان تجمیع انتخابات مجلس با ریاست جمهوری وجود داشته باشد.
🔹
البته این موانع قانونی باید رفع شوند، اما بنا داریم انتخابات شوراها را در همین سال برگزار کنیم تا تداخلی با انتخابات مجلس نداشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/443369" target="_blank">📅 11:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر کشور پاکستان برای گفت‌وگو در مورد مذاکرات ایران و آمریکا برای چندمین بار در هفته‌های گذشته راهی تهران شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/443368" target="_blank">📅 10:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDV6zvk1nSjuqRi7kOgwRIgtZ4Jc8aJfmWR0mI5Lnjdfhr1PLHwaNndsAyScNMV2gdBWgRNhbfnPB8KI9xSkED7gs4fnjlzW-8-i1bgCkYDicmIzYE_uJon4ITuQGw5UbSuaY9RmwMQ9FazyHYBktXf3iABQUu0BkDP0nn_5yk19oD2Oe-DUZwZ6EfqmOASWTHey6a_q79QwUcsXhL8Q37z9XJg_tZdDynfodOC-0xpo2iXPZMJYePgv9GpXNiHw1rBKe7K8ISrKmXnSLfP6dPPLtqHMPdKnSzl3acIPJrGwzPmiDWXFcfWT5wKSja7e0_qzuB86OZ8i8IlFKDEhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MddVEKD3C_ICoAJx0qk_-L5Dbm2vzxzCLjJh60F9z5GL5Me4FcMysijMsaN_ahtSLdlVejIg23KUH8tzHfAvjpyycE_3dEoSd5nE_bQRZbJRrcEW0F7wdkFrogySRrk_CqsWq4PasDSkXoIFjk-9_6-lzm56Fa81PLxsHz5X43Nr7EmicETmAbAOQmVx-Bu-8dlH5Fv-f1UESndc3hJu6gKpAmec_jFYrvcpSLMJuJi3sI3T1HAZWS9TC-TnpumPZygB6LMSPDGF1hmXIYPjlnYEglPWwfzwcAXZonHXd4TZRo53Ot6rnue6hsgUR-0XL_dLi61bYwyRMl9X_drmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2cDim3w5NwHsDPe2FodfUZRmxD9X70sdAHZvK3nadftOcxbb1hhPuJMsaQUcEBDz6g5g7ktR9-dFksTGiviXCXoEdxADM31mUxcEcrucU3nwxdY4sMwTk5lmRvxf9aVzu_FQNnVSAFTsxFm9mYuhNAYBR3Ru2FDHj_1p_5CAJMj-qPOrcufZ7mqR2uLqiITttkdkaGtkU4tJmhrN7ppPEkf9TYnVfKaUWNWIjNHTEHqMEzebivvzaSmQ5887MFnKirH_N5YuHXbUsVGsyHSyR_PQRCPsgEwAoOX4g9H26JSBLPtNqiWccNhXcfEVHG-Rm09wikgsGesGGqmzqiv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ap5Am2JiQlk3B-qCRtJSnYnAXBbNQCDY-UON9-S-W34lEwxa9lAJ_uypbf2XEoHJMgJEJ1oELhspHDhnneVbDYIsEEx8qOMjnVgL8Jlpac0c63eY2TeR8STjw_NPWLncWaz8o4QCfStlubHmQW-egC6Ah95P2Q3XunnxX0kC24gS3pJXPlhygO3YtJHUIEQi5w3DgI4InG8U11gdIhd3upgHey32nCCSoH7uVa5sJM466Hpol98JdQW7rRE1shLqLaYKnF1TJinvOSPNHHczP53xMoa-sSMFTW9p76GDtwa6e5rOAzxEldor34KwxTolbjT_n_dm3DFm_QbnS5Sa7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: حل مسائل مردم مهم‌ترین راهبرد پیشگیری از آسیب‌های اجتماعی است
🔹
در نشست هماهنگی ظرفیت‌های مردمی و مدیریت شهری در الگوی حکمرانی محله محور، سازوکارهای هم‌افزایی میان مدیریت شهری، نهادهای مردمی و شبکه‌های اجتماعی محلی به‌منظور شناسایی دقیق مسائل و نیازهای محلات، احصای ظرفیت‌های موجود، اولویت‌بندی چالش‌ها و طراحی راهکارهای اجرایی برای رفع مشکلات مورد بررسی قرار گرفت.
🔹
رئیس‌جمهور: پس از استقرار و موفقیت این مدل در تهران و برخی مناطق آزمایشی، نتایج و تجربیات آن در نشست‌های استانداران، فرمانداران و سایر مدیران اجرایی کشور ارائه و زمینۀ تعمیم آن به سراسر کشور فراهم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/443364" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در در محدودهٔ صف، بهارستان و اطراف آن تا ساعت ۱۴ امروز، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/443363" target="_blank">📅 10:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa5c80958.mp4?token=A3qn0aFG5pE7tRktP6eZp1Emo7abkpniN-FQYMYkHfoaQ63BQYqQ900m8ypKDQr0Hb7aXMBCV4ap_0VJnr-vw30AdphotkR07GEkgND4QrQcIKnzxkmRqs1AI6NLrlSlsxyB11tR215nIKQ8B4pE0Wnfi_LeTugxBCS8O3ibVp3FRHeIGpuieUvKuq_a7pT0gd4EaNBO-fmAVYUFg5KkfcfzFFqgxoG4tbpiKKy04SvjjHiHDSojCLzXKJ7ZHIHVLdSVbv2wPFvlVx-rBuYlbDSRu_eFi9w71JNuKlIQ7OsxsCshAsA39VmOuG1mLuoH7I-dtzQIHfqp_fWop3Mhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa5c80958.mp4?token=A3qn0aFG5pE7tRktP6eZp1Emo7abkpniN-FQYMYkHfoaQ63BQYqQ900m8ypKDQr0Hb7aXMBCV4ap_0VJnr-vw30AdphotkR07GEkgND4QrQcIKnzxkmRqs1AI6NLrlSlsxyB11tR215nIKQ8B4pE0Wnfi_LeTugxBCS8O3ibVp3FRHeIGpuieUvKuq_a7pT0gd4EaNBO-fmAVYUFg5KkfcfzFFqgxoG4tbpiKKy04SvjjHiHDSojCLzXKJ7ZHIHVLdSVbv2wPFvlVx-rBuYlbDSRu_eFi9w71JNuKlIQ7OsxsCshAsA39VmOuG1mLuoH7I-dtzQIHfqp_fWop3Mhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب‌هایی از بمباران‌های وحشیانه در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/443361" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTO9Ul6wva9LgRnDKKnGAXQHArcUogaWkDkAcwjaB_M8iPvCSpuv9slBijLKufncVN3lR8GZtrA_We0Ct0AWpbktTxo1Alh62Ay-AtR0KnM0NUcCQIhwgcDUlhuVYCyRBrprGeVOUo7mbW0G8taAabizUR4_gfnXBrTKYWlMlX8rHJ0OlK05GRSf73EvyFCks86Sb5BJxCBAg5CNB2Z-zVoyui8rLqQEj9SBFFs1CiSxeOmFLMSgag3yOiOAabGDz8jNeuvhLPclqzOsKNHIY5LrzXaHQ1p48DFjmwgMQEsBxPtewY94VmGKs6car3JP1ozDtCV13b9AVSiYHsOtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از بمباران‌های وحشیانه و پیاپی رژیم صهیونیستی در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/443360" target="_blank">📅 10:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZcp1CsQoWvkXmWjfWxW_9wIVZSU5GbYqd59JkA29XDWS-Lzgck6m5NX4xia_2fgHHvRdMyTaRNn9vjT4wwQgvpzUdXBAqVqJqR1gdClmobcnaMnY3t4fC7ciweF6d92cvl2EJw9b94htZQ8Ssyqr2FjCXKbtDpQuMhVUu4PQKj9iarmZP0I3XrqpaglLm5hwFantDwKFoYAq2NcanxLpcOkECkSfoQKxRZhGkfcKOW8L5KJSPaH8ON-LZV4CtE4SdPUHjzd5NSKHPt_AFunH6dfcoDqCUMJLd7ZipeFgqIjnDSiRFaUE5BiC3r9-2uwlf3xtGbK2ygrZz-ldxkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر صمت مهمان جلسۀ وبیناری مجلس با محوریت خودرو
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: وزیر صمت فردا مهمان جلسۀ وبیناری صحن علنی مجلس خواهد بود.
🔹
محور اصلی گفت‌وگو پیرامون مسائل حوزه تولید خودرو، ارتقای کیفیت محصولات داخلی و نحوه حمایت از کارخانه‌هایی است که در این بخش متحمل آسیب شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/443359" target="_blank">📅 10:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443356">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDRsKWLylwSokEDAze0hrwnvH268KYpOn3pzijTENpACm2pWZtyPXF2x4lbsLvfBvhA68awgwvM9XlUzGGD8uieNMXc2sKj9CQIq4o9m3cV8tTksDABAn7yqQrVVzln2uzpqTNz09fYrda91hbTm_zTIcVrbLAtVlQKo8cfpsmnPV2Wrnie-XKaOJcnOQpMmRq8OMTf5FsZNSt-_F8sYLH1U90Is58OopYCbvM2tVoIUY48BfxgXo2OIo7pF9HzUAWuThFnxXmwwmRLppRwpzNuHeFbnQZDJDnq4Dg5zJTXf8LX12vUP0xqrJCm6UojRbst4RdNBvK3_MFI4h4er-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRlBbmnYD4VdB5CPHTq0Adaexv7uWxaKQUNdT-SOoiKzrZoTbqWwW3LnW1kq8wDk7a8dogNiIWEnhvfx9LQTOAvRCyRNpydZiMl_SPgXQSLCD55KTIy4st-LFD-GkozVl9NyFqtRW8IScH0pdEIRarEH7FYlW8cZ2UvU-y1fDQmk83dreqv1WuRltvDrWs8eLFwWlXHGI7AuczchrSGqYSrjl_qTvpocP2eFspY-UzqgvjxeXkNnxq6owZ_7jCJaruqo9ngzFIo7yAzGknLCX3jDradHYiNI25CwBjZ4E-jk5X5LK72ZwA1GEaa27H6geiDRR9tulljjJQBiiAszfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZjNqAg9GImBTqrdZ-GX1JPZ_xVZkxQDoar_-NmH8e8kQo5VtIAShOY_l0A5oTw_8ItrBSx8UFAbJXtgjKKM9_0bHx0S-owS9on7-rd5fR0rzWHaGWaXF84d5Z4P7eCeQJmAqJFPJ19nOIcWJSTJsU-pCQhFH9v6OgpJpNwuFmHWcpgTAkmWpivP0qMn9GIDvEyOgfhqglgmhokEndOtR3LvxovlmGTr3O1JCFGXO8tBqIoC1tzY1VSgJ5HvXDWiNuWlElZwwtHuXR50XuVfjmAfg-4dGEDp9sJEC9QrE4pBid5gvx7Rcv2FNOBz_-RCXatmwZnT5plSYJ_AQD92uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/443356" target="_blank">📅 09:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443355">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJObbCqeSFgNWp2rmvs9DqT2bitBlPJlEi6yjTM6fwNKhF2Sn3AYU7DjaidcipIA-RPongAQwHO-B-88cweEEX-rSSOnAiDaFeet6Nz-AUcbeWx7FsPVxFWkesplIqr7MEPWn4s4qk2nu9Ep8r6KPpkhS1mFzBCObto3Sqhq8lKVZJ8c2dOPV72WK859PQsV9zaCnJGy5e6X_B82iUo1my-P4BFnX0kAlXZMitLbsgxnbOjlhNckyVukVKM3Fi00UoW5uXFPGCubsvcgCxLDr0t_olsyOxo-wQf9Z5PD4MIhFuGS4LZb635aVzOTLE6TVgm3v4ZaQJDPxE8lpx4mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
الجزیره از ۴ حملهٔ هوایی رژیم صهیونیستی به شهر النبطیه و شهرک النبطیه الفوقه در جنوب لبنان خبر داد.
🔹
المیادین هم از حملهٔ هوایی اسرائیل به شهرستان صور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/443355" target="_blank">📅 09:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443354">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BovpOjxoj2sgWQCmxSZ5mZs8lqGyc-2d7mKNI8JrnQLPv8gsb1h7CNaa-X5JBxZaC9GPJrVnGg-cLK2jXEsO16UbW37lZV9BdAtW71K8DZOODVnIRwzwVgtbedqBGIifxhgH_dx8youM5fyw0VX1cB-HKTU4Avodx1aC8GsdRpDQT5H62m_GeNh6mURmcXkffpDpOx1c4aYjIJRGb2h21JHUsn-FIw9bqKTxPYRirCB0BtzUIkYJcWpzNaL8Uw_zIrMiXTLlFLDWmwOp2mS99gE426M9dUSXvsqDvsXiWepF9pyju3VFS71FgWAt995iIuqRMSR6sCu3jb0IJww78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور اینفانتینو در رختکن ایران و تمجید از عملکرد بازیکنان
🔹
قلعه‌نویی: به‌خاطر شرایطی که برای ما درست کردند، ما مظلوم‌ترین تیم جام جهانی هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/443354" target="_blank">📅 09:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443353">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad273a0bf.mp4?token=szaNjj_FnED6LnZSdhbabD3SItuC1ZKbZshB4foT3ob8SYuFd-xP9Hh_mURQHP6t8pRxHiMa11UYRV1AQ0wC_7rEx4RoKVX4I-Yqd8MOWWSe_0Ie0iZD0HixFxzQShI6EppNgA5rWokd3GRBiCDZzrm1bJ7Swv3cgPiD05QebIXbPOqNt48C0lGe94gmHcKQndu9c_WvovbX_mwSvv2kamzu9_MjNxfBSN6ZXu9Jk8PH1RCVoWq9cLF7uH_0NIVcMtROL4MU_LlTKVxuffcNrt7aHDJYtdbwrpLg-Ty7yIm39Sk5ymGpqbpcHn7DqISfGV29BPrvHT5Xk9pZ4Cd5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad273a0bf.mp4?token=szaNjj_FnED6LnZSdhbabD3SItuC1ZKbZshB4foT3ob8SYuFd-xP9Hh_mURQHP6t8pRxHiMa11UYRV1AQ0wC_7rEx4RoKVX4I-Yqd8MOWWSe_0Ie0iZD0HixFxzQShI6EppNgA5rWokd3GRBiCDZzrm1bJ7Swv3cgPiD05QebIXbPOqNt48C0lGe94gmHcKQndu9c_WvovbX_mwSvv2kamzu9_MjNxfBSN6ZXu9Jk8PH1RCVoWq9cLF7uH_0NIVcMtROL4MU_LlTKVxuffcNrt7aHDJYtdbwrpLg-Ty7yIm39Sk5ymGpqbpcHn7DqISfGV29BPrvHT5Xk9pZ4Cd5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آزادراه شهید شوشتری چطور شرق تهران را از ترافیک نجات می‌دهد؟
🔹
رئیس کمیته عمران شورای شهر تهران: آزادراه شهید شوشتری که به بزرگراه شهید یاسینی منتهی می‌شود، می‌تواند حدود ۳۰ درصد از ترافیک بزرگراه بسیج و بخشی از بار ترافیکی شرق تهران را کاهش دهد.
🔹
پس‌از…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/443353" target="_blank">📅 09:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f8e3c743.mp4?token=J0QHPteLCG44xpT3QmdfOHFY-_MDTZEO4AdQMYDMV_Msn94SWaOlMPw4YYok-oNO07EuQLzfDVunG645tkkaIxvwP3tfzNPnNbTkJPrgA7hGfUqfAkDOHOZ-xaTg3eS2dJl6mF-9J0Wba_1JKuHh5Z06hi5eCfBr3L0VTrgtNoSxc79IqpXzIinIb8VSfkkYN21gtHGqEqPnBrTW5gsMUWGvyeoP2hVDaw4UoBxlF1-0Fv454hbk3zoclXDLk6E6AfxaaNXPRBVx7wq6OpgpSXUBRQ9_msd-rfcZ8WXUgntu3_tTkOPuzCg16ZGtuIZkvvbJ8xgg72Hj3e3H69PNPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f8e3c743.mp4?token=J0QHPteLCG44xpT3QmdfOHFY-_MDTZEO4AdQMYDMV_Msn94SWaOlMPw4YYok-oNO07EuQLzfDVunG645tkkaIxvwP3tfzNPnNbTkJPrgA7hGfUqfAkDOHOZ-xaTg3eS2dJl6mF-9J0Wba_1JKuHh5Z06hi5eCfBr3L0VTrgtNoSxc79IqpXzIinIb8VSfkkYN21gtHGqEqPnBrTW5gsMUWGvyeoP2hVDaw4UoBxlF1-0Fv454hbk3zoclXDLk6E6AfxaaNXPRBVx7wq6OpgpSXUBRQ9_msd-rfcZ8WXUgntu3_tTkOPuzCg16ZGtuIZkvvbJ8xgg72Hj3e3H69PNPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز گل‌های زودهنگام؛ پاراگوئه در دقیقۀ یک به گل رسید
⚽️
پاراگوئه ۱ - ۰ ترکیه @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443352" target="_blank">📅 08:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqxaShaEA1ALKm3fAyZ6qKvArwNYTuqS2b8w0NUph-BgTauZDOMT2nODBEfbg0c07TvheMVjEC9wLu8Z2fGLQsdtIB9Uf7eTooc0XwNzA9zWMn6DHnO9a_YPXSlAOuh44LRf2qU6Gn60pkuj4iZM2cu0p9wu9xZF8u3hZy_Ml1TSmPYHHOQK-wfjqG1-2b9Beu0rfIQyfzlM38EH6nZa4fULVIPpiOUimB4CBj_iUyQi7IWMAcesColLC4c3tJ-d7gprhyuVXXML6U_w1cOAxA0FIy7oSqosH0MMkXD99AITEyu59fF_eFbIKfwB8vKGzGtP2vq0hrp509u02mQdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سارقان مسلح تانکرهای سوخت دستگیر شدند
🔹
دادستانی سیستان‌وبلوچستان از دستگیری ۴ عامل سرقت مسلحانه از تانکرهای سوخت در این استان خبر داد‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443351" target="_blank">📅 08:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJQkXV1JHPWOZ7eAeIy6aY31C1pgddM8AYJZ95IzeSRjvRx8NUvOE2KwCIm_nW8-UeoEaBeZr-lLiA2Oj3RXAboC8boh-poungLJox4UXs0fb-Aqd82-uSeVp1E05Tz1amYmq9kpAG1YQxm355Oskbq9hoTCZR-2IEzciM2QN13OFxxhAJtGmxSEAACqh-l-VrkAQBMsfnlc-A1evYGObci4clDQ20uHCyfYg06orGfEt9uw_ndDVu0KV_hIWoyEqK6fKawygNDtUsAijWvP4oZnMjZpF7yvlY7y1UCvcjUYt8vIYomPKHagEj0V-Rk1nI6GyBYJi0McBTUHwyVWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روستایی‌ها تولیدکنندۀ برق شدند
🔹
با تسهیلات بسیج سازندگی، سال گذشته ۱۸ هزار و ۵۰۰ پنل خورشیدی در مناطق روستایی نصب شد تا هم برق خانوار و بخشی از شبکۀ کشور تأمین شود، هم از محل فروش برق تولیدی، درآمدی برای خانوارها ایجاد گردد.
🔹
بازپرداخت این تسهیلات ۵ ساله و از محل فروش برق تولیدی تأمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443350" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEu6rIpnbEY02NYsYycdsvUq1s_kKSxZ1llDw1C66Ss87H95MaifP_MEyd3VP2gVst43hHnjO_1EBFwZ-_i3d3N6x7k-EErRE4FxL2fUcCPWZR49MlHlOjnQdxCpAx4hJSs8Bxfmy-mPCysY_YEu84bz1muMw-2P7BrglqCKqthWgP9LGV2-gbVuTwaza2V85CLZzvh_Gg3iCM2XZ-6DcwkCESeghr3-4DAnGDDijW_ZryygbWd7QziWk1tATszlKt1d_j0_j5cs5DaYTl4XWxqTTFJ4NyPVXlX7rJkWIptvTSP_0CRsZDvxhfNlem8oN5GfrHTGmg2xhdy7m8VyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج آزمون سمپاد کی اعلام می‌شود؟
🔹
به گفتۀ مسئولان برگزار کننده، نتایج آزمون ورودی مدارس سمپاد اوایل مردادماه اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/443349" target="_blank">📅 07:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f07b3fe1.mp4?token=MB66qQgN74kKzAgzTRynl2tbZ6sUgtj5jvh5rdeePEqKGvvrr7vb--9M9Sppdql2BVrusSJ8X4wlUKEHyAqN4lsPOxCJaS3zw5iYms0Hn24YxfBYRwwFRtlySK1e3qHhuZSCK-ghJq1rYy0HdYi52Usy8Hb9C8oXYglnHfTEpcy86rCGfkFlo-blN9g3kzPvvLQ-tOMtYAKwEuwjwzsAAe9ur6ZpiWoqvrSeCPz7BWzB-B7-vRDnwvJdNxRkcW2gx00JBRwNnQM4-2ewmGGzyZHIbH1Pv9m0MqG_MVtQJIiBzXqlxxxtZ8nGIT-A7uTS076k5aOUjJVlUKuK5sGBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f07b3fe1.mp4?token=MB66qQgN74kKzAgzTRynl2tbZ6sUgtj5jvh5rdeePEqKGvvrr7vb--9M9Sppdql2BVrusSJ8X4wlUKEHyAqN4lsPOxCJaS3zw5iYms0Hn24YxfBYRwwFRtlySK1e3qHhuZSCK-ghJq1rYy0HdYi52Usy8Hb9C8oXYglnHfTEpcy86rCGfkFlo-blN9g3kzPvvLQ-tOMtYAKwEuwjwzsAAe9ur6ZpiWoqvrSeCPz7BWzB-B7-vRDnwvJdNxRkcW2gx00JBRwNnQM4-2ewmGGzyZHIbH1Pv9m0MqG_MVtQJIiBzXqlxxxtZ8nGIT-A7uTS076k5aOUjJVlUKuK5sGBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون وینیسیوس قربانی گرفت؛ پاراگوئه قربانی قانون جدید فیفا
⚽️
میگل آلمیرون، بازیکن پاراگوئه به‌دلیل مخفی‌کردن دهان خود هنگام صحبت با حریف، از زمین مسابقه اخراج شد. داور پس از بازبینی با VAR این تصمیم را گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/443348" target="_blank">📅 07:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیش‌بینی بارش باران در استان‌های ساحلی خزر، و آسمان صاف برای سایر مناطق کشور
🔹
هواشناسی: در پنج روز آینده در ارتفاعات استان‌های ساحلی خزر بارش پراکنده پیش‌بینی می‌شود. در سایر نقاط کشور در طی این مدت پدیدۀ بارشی نخواهیم داشت.
🔹
همچنین در پنج روز آینده در شمال‌شرق و شرق کشور و دامنه‌های جنوبی البرز شرقی، در برخی ساعات وزش‌باد شدید و گاهی گردوخاک پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/443347" target="_blank">📅 07:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljLvDZ6m1xTel2HlkPUMHfKSEkvGIWH4t-JR4Wb5i8_eCdqC-MSs6YE12mLAwa5m_ij2U-K2cUIN3pyUEolLoq8N_cqp9MsLpnCD7aUzPefQjMkK72BYf3IfhIb2uzPgmxjKwpY_3Aoqhum-cq_AXyL0FYP59IXxkE_leeEK4V0VSb7MaP9MzS8C9d9vypHT02QXjUeNYKMNhDJqtGrATJNmn_CtMOhP8TdC6Rn85fbzVr7HrtxkWNjCrMWgf5iw4inVn9vC1yEX-211LIAb8cQ73fhNU40gl84KHM4PvzvfIJtDyEgZeTMa5SPWvaOI3nyS9tru-M8ZdP-wmrSpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لشکری که هر روز بزرگ‌تر می‌شد
🔹
چهارمین روز محرم فرا رسید. ۲ روز از ورود کاروان امام حسین(ع) به کربلا می‌گذشت و حالا نشانه‌های یک محاصرهٔ بزرگ آشکارتر از همیشه بود.
🔹
در اردوگاه کوفه، عمر بن سعد مشغول سازمان‌دهی نیروهای تازه‌وارد بود. از کوفه پیوسته گروه‌های…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443346" target="_blank">📅 07:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71790d2667.mp4?token=ujiuYHZgRLq-BC6PLLjWPgS1qCSNOVG4ebRq3_8DtvP6a7_cQOVCLMFpndgkA_DfHWFyIKW89ssEym3pbfOSa-t-5NO7x693yWgL48KExuyu1sn5-qM7fIjfSoQijhsmhxf75N318BzamwU6gBWO5I9cgmT8gEDZS9OsqqpdiWOhIRErIzEFUdlpwBXFoADEVr1bUFvyE-B8WorgxH6XNTVjq3Y7_68IbNCEt8r5SbLvq3-qqoc4CSic8eVL4scNoDMVWKOEb29NnKFMy4TDnbtt5veOwB_94DQTFUAteIBvvqKupn2_n2eBE1kbRUqefmLolCn4_7FdqaMnLLhtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71790d2667.mp4?token=ujiuYHZgRLq-BC6PLLjWPgS1qCSNOVG4ebRq3_8DtvP6a7_cQOVCLMFpndgkA_DfHWFyIKW89ssEym3pbfOSa-t-5NO7x693yWgL48KExuyu1sn5-qM7fIjfSoQijhsmhxf75N318BzamwU6gBWO5I9cgmT8gEDZS9OsqqpdiWOhIRErIzEFUdlpwBXFoADEVr1bUFvyE-B8WorgxH6XNTVjq3Y7_68IbNCEt8r5SbLvq3-qqoc4CSic8eVL4scNoDMVWKOEb29NnKFMy4TDnbtt5veOwB_94DQTFUAteIBvvqKupn2_n2eBE1kbRUqefmLolCn4_7FdqaMnLLhtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز گل‌های زودهنگام؛ پاراگوئه در دقیقۀ یک به گل رسید
⚽️
پاراگوئه ۱ - ۰ ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/443345" target="_blank">📅 06:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-_bRxWfF98pQHJK1lP3W0vbx3hu2bDcZCOTLrSdElGFHAOc8kpYboiuZ4lICK7oYgrWyH1i0hZwBMRjczL8LpxyoLEVUoUssmUr8hL-PQYFPhnFiT8y_JVcKqbQbl8Y4SkLR-kQ1sbCBSGjVbIS6uHLwDBJIQ5oN8WWooLZ9VhrXTr9xstVbv9f6rojB4zOMz9bT-pY5LILvBMY4oF7PyRiKjXkL9ZuoO_lhNQ11V9MWCWCTbjg5S_NRdOtLHkl52T8KAALgh3MreFHha52StK1-jr8aVDo6ZFbuaHVROOtHfsmCUfngqN4qzJrJmOth1Db0g_QfuscMj_Hx0eR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای تازه نفس در راه حفاظت از جنگل‌های شمال
🔹
فرماندۀ یگان حفاظت منابع طبیعی مازندران-ساری، از صدور مجوز جذب نیروهای بومی متخصص و کارآمد به‌منظور تقویت بدنۀ حفاظتی جنگل‌های هیرکانی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/443344" target="_blank">📅 06:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkg4ZikELVxmsSMjH8G0dzLQR9cirLayI634kEBSpFElLXgJBGo3_xJ4kaeIg3yZxWG9uczuVZXSLbib9ro6YEUyeFeWdUs_1CDjSWZHudnY6oPuHP28ieCsglStaietLow1VjjQ5i5OECCf8N9UtG2i9nnXjNzifoP48DMrLM19s4lFQ_uq0X4c05a8YSIhhnrq35zMjPvAe6AceGPnMLez3500tyIgqa5M0QahMnBMqbELlqDYN38-yJ_aCVDuQ8p-B3LfcLHWK6mCUbR6rjP3MOBZRV4jHGjPzYiT2BB709XDXY7aOOFpw9eEB0NpH2_ZJEwV1a8pyMYS8KOveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزیل‌ و مراکش در صدر
❌
هائیتی اولین حذف‌شدۀ جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/443343" target="_blank">📅 06:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1y6a7DdGyBxrl_LaLEWtZ7cP1yFZwM78gUDXE4ncjIOjNz3dNvyEPTw5mClIlzAAmYes4hTkMXRjquxjQ_nJJ0JeUbCGKBJlTXF6X6kLeuQYyNGiI14DVOfb2fQ_4fxkPhy_0Ygx28HYjjOSIMgHmvd9BuefBpb32YNDot8rdRUfL0aAnXgYeKzk0A6b7qZy3M_SV2IZQgINyCdH3V1sake22j_Tnn_Un9tIelhhQvw8SgCwmeu16bq48hUPAhdST7v6o3a6huu7JvGUbLaSP_rqVkPt9PtpU-G1D40ua_Md_ahqgShxukMuXUKaeyQEXX6QMz8YbeVnB2B84sILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل، ۳ بر صفر هائیتی را شکست داد
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/443342" target="_blank">📅 06:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c6faf471.mp4?token=YXbjz6n0bWa0nojHii7yiYlQsIWK64SyyqDB0RaJp0NFy3TBlHBn1s3z4vW3lelOl1ONy6djO8KJYj6JfPHjf73HD1RZ4JAgXDQSVgrQcsrPOEnWq-5wnCYvdUz4OgzdHHMHHis2XKbHN6TtBSFV3Rx6c8hd8Df5Oopgx-01pyNMhbnRG6q81403aU1UNiXOU3VY-G2V1Jf322HahWEPxd3dU8FvbNXPvTGUrz2ysufGWk2F7ILVQkYYw79BRdhRrA9AD0dnE94a8W3U4CGaTHU35NS6W6N2plNX13YIHcvnSr3oiPuIad5Gx8Xz72xRgrh0B-lUzTymDfk2N7SJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c6faf471.mp4?token=YXbjz6n0bWa0nojHii7yiYlQsIWK64SyyqDB0RaJp0NFy3TBlHBn1s3z4vW3lelOl1ONy6djO8KJYj6JfPHjf73HD1RZ4JAgXDQSVgrQcsrPOEnWq-5wnCYvdUz4OgzdHHMHHis2XKbHN6TtBSFV3Rx6c8hd8Df5Oopgx-01pyNMhbnRG6q81403aU1UNiXOU3VY-G2V1Jf322HahWEPxd3dU8FvbNXPvTGUrz2ysufGWk2F7ILVQkYYw79BRdhRrA9AD0dnE94a8W3U4CGaTHU35NS6W6N2plNX13YIHcvnSr3oiPuIad5Gx8Xz72xRgrh0B-lUzTymDfk2N7SJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در دقیقۀ ۷۸ بازی، گل چهارم برزیل به هائیتی آفساید اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/443341" target="_blank">📅 05:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfUMTYz7zkY26QuUfkbeq0Pp7GAp5hkNJfv5kwwF8aDk22cJD_rlN1nH-nLTQ-ipFZC0WCTzsWajxE4s6MVFFV83NoFLSGFOBg-xLKtMcBHqukqXXsRyXhTAV4gteqrI6x0Ii5kruApA3XXF5VdjmQBpnB4B2m2gnuh6_qJkOxT_uJUrMVBjJndJRQFnvaEkkFeyx_682bfAtK-Wg-DBfc-9bYF2Pwqp64PHnZizcnTuuBoWRrRA4HWsYu2EZc2FsiQmVKl3OMWvJ2uFtcPKXIA8WJgBSYUFTbOpuzHkqFygSZ-92EEZZGP01S30YSN9L_AIm2mZwjq-EJHKR2d6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکثیر یوز آسیایی در محیط محصور؛ آیا راه را اشتباه رفتیم؟
🔹
از آغاز پروژۀ تکثیر یوزپلنگ در اسارت یا همان جدا کردن یوزها از طبیعت و انتقالشان به محوطه‌هایی محصور حدود ۱۰ سال می‌گذرد، اما در تمام این مدت تنها سه توله یوز در سال ۱۴۰۱ متولد شدند که در نهایت هر سه تلف شدند.
🔹
معاون سازمان حفاظت محیط زیست، دربارۀ علت این ناکامی می‌گوید که در آن زمان تجربه و آمادگی کافی برای مدیریت چنین فرایندی وجود نداشت. از سوی دیگر، روند زایمان نیز به‌طور کامل و مطلوب پیش نرفت و مجموعه‌ای از عوامل، از جمله کمبود امکانات و تجهیزات و برخی مشکلات دیگر، باعث شد نتیجۀ مورد انتظار حاصل نشود.
🔹
این اظهارات در حالی مطرح می‌شود که طرح تکثیر یوزپلنگ ایرانی در اسارت با هدف نجات یکی از نادرترین گونه‌های حیات‌وحش کشور، در سال ۱۳۹۴ و با انتقال «کوشکی» و «دلبر» به پارک پردیسان آغاز شد، اما به اهداف اولیۀ خود دست نیافت.
🔗
ادامۀ این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443340" target="_blank">📅 05:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
المیادین: رژیم صهیونیستی شهرک‌های کفرجوز و نبطیه الفوقا را نیز هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443339" target="_blank">📅 04:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443337">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXnNKOsHShSnmcqKXeXcE1N3J8LY0O3peq41SuiRFOin80-2_tup5cDX72dsbyn2jttPKO-GTcHxo-6-9P0zLWhnN9e0naKtrP7Icr7ot6lTWq_ra_hQMXKxwWVHJxhznL0L8j0sfrbJ2lVdpe6_tO8jwKTVaCpw5Rupfg8Zt9V6qUIIeHENCDuYVY3N4mgMaglcI_-5yRNEORRRuTskHm7n1vdGqZ_nXQ3UD8tCaoZ_avYgouGVq_fMgmSbazJAsjKgKC78r1y2UVDGgZ_YWYlwA5fVPaYqWwsPFWYizNhL4qmOLgEGtGxs95Y7pl3Z_kldoXy79Qa1Dtawbbqrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqAoINhwZGoG5KA9yfkVhzlyactXHcc1pgZlNqUJMiKGkVuwasmUx3iX1VmLHQz2v7fb9b5CGaCvrRlfC7h7AI4aeOYmeurtR-QheF0U-LvrK45pcnoVE5qw8wX73tUgf43oCt89wa7enayaxjaf94R8u_bzVyzDh8LPIzuW8u3C2IW3KFBRFJ6iwM-n9dPfBTWDS5wF_qF8eds65Tsh-u8Jj_qcrBfPruHvJyh51EdEtrY1r4XV5qBn3kkTzSWJKuMscane5QClZwooemzIYDDhNwxwOP-e_HPY_LqvxHpoA3GEKTYqRhKtmARBDNtSyxEfmmDPG-NysdvDPJ-JsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سنگ قبر، جان‌ده‌ها نفر و عمر سازنده‌اش را گرفت
🔹
ناصرالدین‌شاه قاجار نه‌تنها در دوران سلطنت خود برای مردم دردسرهای فراوانی به همراه داشت، بلکه پس از مرگ نیز ماجرایی پرحاشیه از خود برجای گذاشت.
🔹
سنگ قبر ناصرالدین‌شاه، از شاهکارهای حجاری دورۀ قاجار، به دست استاد حسین حجارباشی یزدی ساخته شد که چهار سال از عمرش را صرف تراش مرمر آن کرد.
🔹
انتقال این سنگ عظیم از یزد به تهران در نبود امکانات حمل‌ونقل مدرن بسیار دشوار بود و به‌صورت مرحله‌به‌مرحله با کمک مردم روستاها انجام شد.
🔹
در هر آبادی از مردم خواسته می‌شد با چوب، طناب و الوار سنگ را میلی‌متر به میلی‌متر جلو ببرند. گفته شده در این مسیر ۳۰ تا ۵۰ نفر جان باخته‌اند.
🔹
اما با وجود این همه سختی، مظفرالدین‌شاه تنها ۱۰۰ تومان به هنرمند سازندۀ پرداخت کرد؛ رقمی که تناسبی باارزش اثر و سختی کار نداشت و بنابر روایت‌ها، این بی‌مهری موجب بیماری و مرگ او شد.
🔸
قبر ناصرالدین‌شاه در حرم حضرت عبدالعظیم حسنی قرار دارد و سنگ قبر او نیز در گوشه‌ای از کاخ گلستان که با نام «خلوت کریم‌خانی» شناخته می‌شود، به نمایش گذاشته شده است.
🔗
گزارش کامل را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443337" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443335">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXwbWrkfbv2ikGtKxE0arVoPafPD4A9vDkYjabnIvfqi68RVvckvbQ5xYpLq1oA7fm_-6c1ReRjwq7klUkkWIxL3IbfNUVIljvdj1VLDjWbzl8ICvIbXh2kOfJQpYVpKhEOs2Zoi4sXsbJurIWTSFGtYsKnp5twvObu4xylYc2exZitcJ7qaDgb4Dcc9-ICD4lkSFG8Ud9KBopkWMDu2rYuVRfJpou-vynOG4SA-DxDFZ0TRuqP_3xNiGhAzdGRTEAUA7VM6K7OObYPKcroDQZb71wMoA93WOVRcQ1g4Zn-Ileg38Fyil1Y8172qe7PsOrC83u4GdUOzavX47Whv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع پرسپولیس در لیست خروج
🔹
حسین ابرقویی که فصل گذشته از خیبر خرم‌آباد به پرسپولیس پیوست، در نخستین سال حضورش در جمع سرخ‌پوشان نتوانست عملکردی در حد انتظار کادر فنی ارائه دهد.
🔹
بر همین اساس، به‌احتمال زیاد این مدافع فصل آینده جایی در ترکیب پرسپولیس نخواهد داشت و باید فوتبالش را در تیم دیگری دنبال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443335" target="_blank">📅 03:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مجتهدی: به‌دنبال روضه بگردید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443334" target="_blank">📅 02:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443333" target="_blank">📅 02:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443332" target="_blank">📅 02:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7rI5jpJEoLc_1OvB7SdP_InoEBFkDSgFaGARFN4SqLdWKKkbAQafqpuYlVKiqJOhc50-U5U5KZoTiSIgX4_28K3s82IsYx5jGtF_znZxOrt9mqhzl9IZrfgM1pCDwOXXqZvbL9pnYpHoXEnSF97j0RQWXl_M7_aN2Jt5U-_imxVeRw-ub_nEhqdrfSc79vJ71vYBIhOzE_v5bS0BUygKxxG6sF460bcU20MxkjbkaDpu9qiUsR_QpCQgg9x194h2ZsAdLRKHkVofVy-e6baW1JOKGAXp5d6zITm0DGXEU2wLKsoAEWxT3BeJUyIWHZpz83wy-XsTjeseh878V46Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقاومت مسلحانۀ ماینردار بزرگ دربرابر پلیس
🔹
سفیدمو، مجری نظارت بر استخراج رمزدارایی توانیر: در جریان شناسایی و جمع‌آوری یک مزرعۀ ماینر در یکی از شهرک‌های صنعتی کشور، عوامل حاضر اقدام به درگیری فیزیکی و تیراندازی به سمت مأموران کردند.
🔹
در این عملیات، نزدیک به ۶۰۰ دستگاه ماینر غیرمجاز کشف و توقیف شد؛ اما پس از بررسی بار مصرفی شهرک صنعتی مشخص شد این کشفیات تنها نیمی از واقعیت موجود بوده و بخش قابل توجهی از دستگاه‌ها پیش از شناسایی خاموش، و همچنان از دسترس بازرسی‌ها دور مانده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/443331" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شروع طوفانی مراکش؛ گل اول در دقیقۀ ۲
⚽️
مراکش ۱ - ۰ اسکاتلند
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443330" target="_blank">📅 01:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«علی‌الاصول» مسیر حسین و شمر جداست
که شمر بندۀ شیطان، حسین عبد خداست
🔸
مداحی مهدی رسولی در شب پنجم محرم
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/443329" target="_blank">📅 01:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPWr2WQgQh0J4_aCbkuRASSsfRG3Lg_czhElI47U2KySYppMefrobbWwk3Cf7O7xFomwiEHzcUV4aAXvE_zwkFn5_lJR5KSNDCMu4OZ8iJQUOwoyV6dIDVolp6CacM91z9DaiwD69MkW_BbeePSIaRVB8gLxyJPrndn3wJaYUC8qjD2B-dQD1d9JthO0uCmTSK3DMd9OeDcIPLqef1XqlEUCBso8LEsjQACQJqNZTKshrSNUSOBOoXVyH5B6uVkrYCL6e32stEMXEAuObrY1q8tkbhWMYmFZ1MeIfzGL-f7HzG4b60ALLTpLJEnW_FrY-H4Comd9IZ5k-yXYFgegXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدشانسی مهاجم استقلال برای بازی برزیل
🔹
داکنز نازون، مهاجم استقلال برترین گلزن ملی هائیتی، همچنان در شرایط نامشخصی برای حضور در دیدار کشورش برابر برزیل دارد و احتمال غیبت او در این مسابقه بسیار بالاست.
🔹
نازون از زمان دیدار مقابل اسکاتلند در هیچ‌یک از چهار جلسۀ تمرینی گروهی هائیتی شرکت نکرده و وضعیت او تغییری نسبت به روزهای گذشته نداشته است. بنابراین کادر فنی این تیم امید چندانی به حضور او در مصاف با برزیل در جام‌جهانی ندارد.
🔹
غیبت احتمالی نازون می‌تواند ضربۀ بزرگی به هائیتی وارد کند؛ بازیکنی که نه‌تنها مهاجم اصلی تیم به‌شمار می‌رود، بلکه یکی از مهره‌های تأثیرگذار و رهبران این تیم نیز محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/443328" target="_blank">📅 01:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqwYXG_wliGvgQcyrYrY7NsacHYppb528hNOWwnmhzSeMsZAcpKn4R-5l7oZRkop2ECUjIdVK9C5B9UChm9TGc1rqeS7PH-hGBvGK_rDm4d6bkipzaIk59FX9nu7TOzgepY2x3V3HsDrNkbH_t9mvGJi6HAa63tLvoPYKLdDsiJZnBgu2s55SJj7z4j13YF5Ar9YTMvKfhILUuenIKHeIqamNfLCcvjJb4_VlAy2nzr1xGUEE5iR79BRTl9eeAGoRGp203tldpFVAKrO36vV8mHvjgoEqIzxkeKQ1X22zAE9lzg-fD6HUufb0AHWG3rAltshMNsO-5WH025thk8odQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8w_DZnpd3MiJWnVRPJiF4ifRfk7Qdzi-Vwkq4V8wfBkQdCFdAFu-WFVG2czIZmcx-f0t4zpL9nUAREpVvt-iKP48C597JSMIoF0eU1ouqb0ATdF-IXtkLzIIuAS5YzH16UqqOm2wAYB6WHnYzHq_bJu7eO0xtgll-umwWJE45sdxTxDHjI-p2grYVScedn5TW8vrHBTDUVsj4Ks3dbkzEoMmRdzIP5hsIST1p8aFeXfOfh3mRKMtXDWrk2tkkUaR6xDdmmszj4mnzmyNmUt2DpmZ7qc68r1PRJ49Q5g4c4RnFZLVHCjLHtefbeOKOF4BKNCKngi63tzPw6w0i9FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlUQzk7jh9_nL_g4Q0LaLVtmUzCGyKA4htIz9ZXhlwKDVpnXadpMkM5pGwhhXXhSxurgWw_aUlxrhOE7jzxCFBRyEKgBHj6sSEH-0MLJt56QGW-4f7dvugSEb-6djrd71wdzW3wOXFqztHbbUaVpwHufOEf5_iMXNtPYWsxkFiEVD8onuwIoKjijNPPPh3wPkktXgSJz5mT4Ylq0e27iBiL-uAx4GU_Igvgw_bo47oE47jGl6hKO--D06kQew4grw2AJLcDfmEtcwyD9Z_c7NssOAXCIIDdc-OfPx18g5I3bixxt9HEqf_uY4YHUcZAki-3YwcH9tGsqOKa_CRJthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7246T4eHpkrkQJEKs9tr_QwBRp5vdfgj_HRiMw-wfi-8CwOKUy7TnmvG_jXq37rG_0vUeBl_HsRE_X_ZHfxPSQeYowIOh-teRoP-xOy13-txKGtf_HeeUAsxnqHCLKSFEIbw2QBp_33mgyYYkNDHEWaFa4q6ZlKD6FBf82Kioy8woS29BV8_oG04HkBeM_BhFKAM931pu9Bg20C3RyCSJisIqciLxQSb-a9x7m0jlQV_WpKkmmIGzvlADxbsq_8UFDRyf0JQ9dIRMiqcYDLrKKOPJ81EVUas0LcmpYJQHFgGN2XtkoQrNOAb52y4MgdVyeMrxKKXVulGvi5XWRv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbloe16hbGC0Ag_GRCXXDX40fcdPlMxlF2p4_LAZ3mp5ufSk0s9nKTG17Zx6GR8ai2SS56pltlKlVwm95p5IhWSuZY64SJN_nvEiYQ8txj7Q8_zJksqx-GMeHvZtwLBJwZuVu0Awc9GFjeYkUaNBdFIjTSm_6qaqZqN4fw1YMW1tRzNXaLgrXaGCx3GOIzg3-dKKn4Twq_DySD8KTGamKX5jrLcFrQmCBMjXbs8QcIzKVjX8L0oIWZIFsbT4d-mcF8ct80E-NNlpVFeGwBIjw52H3UQ1_LuKGA-m30eI0ptcB7AEQUN3hm8mTvOJ_volcgtrFazmJGwir6_p-3Brbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQ4LvXLrMYxNHpJ-JlXYzZD4z-5cTosIwaLuEJIa9Yi-ue1nj0w-FuMng3qZc5fSM5Vg77uvD4HicB01XociN7TIJrhRaRxf69T1l3IlA3vz8RoeIHI9h81QtE0Q16-OOZxs2DhF7IJDv_je4cPTZfpzea2vgbXfLVvF5uKtS6nkrgzfqWa6imJApqFcfaVhLEQaDC0opdDg-hCVjP3JCgcSLc6kLxfNqiArJZomcv7_tPW7PUJvrNn7Lw1Ly_ftVHFjE5RO96ZB3Xw-Tw-xCjAi1FvHcP_QsEUaOU5S24DKnf-mt0qMQhtLvHyDj6hP71kwJV5UwyNVH3-zQH3ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443322" target="_blank">📅 01:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwgB6ZfyBhg7W58xlYQdCiwGt_pT5nsiuVz6-4Ibe97ABFXtzjuc8HVYiLeubxPuPUygTsVrkzP4fTOIufhZkkfBFjN_Z5nfln9piL-1ugn9uUcFs8yadbL3Dl-G4hl4OXWuuVjQ4_9Gq18WcVkqPsr9GPcxtgA41OphHAMPkI_Tk_sLiie9rjQHfrbYMcRxOOIuAY6VQVJPpRVYdBzbpBUKbEf07BkOL8NzU5BKnZ6XyqvxplVbyBupEVStPfaQ9__1xcJsmYAqnIHX7_5dCqRpMRa2CyWZJTkcADC8w8i-DLiHAQvHI4gyoF723qZLb9eNWwU4LKiGTI4m84j0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIXJvMWX_U4I1AHpANipyJ4nG9HhFzrK35OxAcq5cL6pyC3vXskgsOwcDOAF28ry3ouSglWH8W1l4JSWWPZSfgJ2EQQqxZzfX3ewlhpB7cg_lbeS51FT4MDwsQ3fM7u7GTIuWa3tslhijrnhHnS-FQBA8uSv_-qLKnJ3PdTrT6nBHK0ZDZEINj6U4MTywvANtyBuTHnve9Pi4jX9OQIu7GV2xyFvYV9Brcjez15bQPUyvuQ3hgJxNGsN7N3TrqkcLjR6yXd-pqDGG7LgClsUMaet71VOQ0J-6rp0_KbTqU0m3ifABUTL6z-g7HdCMx0S72l8FxDe7KVPk6-n0Yu2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra6QSjXU5T5h9bjzj7qwrqzSAGlkSmSZFD2gmZbUUBfzO3V6vmFgchDVIIDtFGWKwFKo-fQlQ6ZbWMe7i3GqrrBnEqaXmDhN4C4v4yudct54yG4PgSsLhIoSB2y37ReasUdVd0inULQMdojiKZkAaTC2xjNKCBjsxSNteQuuQ3_6vzxGjPkn7xwP83cGHIkbcf7FTPqiDkeYkoiX32oZoS3eIiph9pH14oW7huuf9MYmhMMJh4OpNe-QcqKIyNIqw2fpf6iTGe5AyRvxKJQP72gBRcfse5piNPBLy4Q6Uy-KnreEMmoi8wokG4ROpMulYZ58LfS6kX3agvarQErEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WotG6vA_R5wDzSH2eqSh7tEyPesNT1rhtCfXXB1P5pZxJVAznrPw5wKvWYOr8liHCAxtypvPLaY03WQxUzn6KccE22UQ6kbitBp545vnXaxE6-rMvqCIfjaohR-4bfLFa57bhRWYfznj3K_SfzmPuAfLtUS8oE5YsyHr1r81Eu-iX16CvTwNHu-AC3iwvxSpnfNhOT22Y_zezsW4v3u9Ea1kuqhO_1vMbYFrKdZM_NEoX1tmLk0RBV4HDNrwG7rctOZ85RFpXw8uaIyban18bMUSHCf9BdD9Zl1AnJkdtgaRVShm2t_gm0w0UZBDITvcY6NrG0b6YRZNTSB-TvqXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjiTDimk2oSF19hzb16kbDhFxcurm_1mzpficQRNlCPqYTdJXtp_dsz0rj-leYLAPpe8pTWn_JG1FjTHi1jq9GymzcvM6Bff1nKzaIySQ_aXKBmVPdUr_TQpDgmTgXP-XrvZ7d8lZ4GSUxGa7gf4G1uD2vvjwsgFhWpk_J2gR1EKAVsVHV6H7cRgyZFpWIHKm6oLiZ459bRmvPXp2mLtudfsH1IFbsGgVlsvXuBLMLt52e9FDUyJRQTMsOWXob9OiHvSLkjjR575qZ3vxtCmb3oSIiI02mYxUDe9GK0Ejy_k0yfwfVfOyIgwzDUdGmf2_YEiRPXhers2k6Hwzmar1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6nWKj_7YIU8C-aU9t4idX4nGZHTfbbfoDyrzSMSbDBtjPaM99VvSHBnUw0lDa1L3_JY_YJGwnBtqcWtTtAcGD6Om_f7iOqPzsWQg7s33Ltd69swUANrxKs9bVvyfTPFF1-OrbcNTtsTTSFi1VhBVb3JV73smtauu-ILUx9DLFIRJyG24xybRBbkzxa_kNdn4aLbfh1tvoMUf5Ch0J4fClCYmUfxX9z3xD6EjlecCHX4Jxeeq8YOnNZ7meboQFIIP-yBtdKUfeTOYlGWINpmr07iRU6RXcKUsYwZr7fB-tycS4bY3SIoJX334_0sWkHVIOKiEl8xqWAz1qIBMsiTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REDiDoRI-QmmHrYlxTnOQSen0c3yAVpPwc0KQzlaV_PmzXz1TG0DBoKeZ1IO6uoBkWDH8nJ93M5N8IQE2--SQw6K6GCvRJEinIhigi6yp43Wtjjbo4jHn7xsm6gtsvbL6kbcnq1VkFYgXgga6QirX_YM2RifUlNQER06PLIo3iYG4sZkVhj6yNs9TdkckXVOPXAf4yxrN-nyPtNaSVizZmXX6qF54KfvzImMWvRoniOlcSb9V6xP9aZ_6KByy63y8HQvlyN0CgQlx-71HtFRghUslHfh5RFZJd7GfrVr6GhEJs5ApMWaKDF4fHoj39C4v0Tpbe_y6frOPvsGzWTyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKcOM9ltkZqfzU0aCigFkUfa1lzZsNJWW3VnoWF-TFNAeTAl9zoDLoMnczSFbV8kkaTfD3hWuAIS109h0tf3Ugi-hbUS_mMw53oB9dSoNaUhBNr9mXiQjffZlezHcJj9hgLBXObneCKBoaLFQi2W1I7Ug1HJ7UMGKBKJKdO0Ok8qwT4Ewqp--KTftge7waWjtT4mFF0Cojbwakb9GGdjyxw11IoPeh4oyJzsVIx28qspKDMZ5uo_hElen9VpiRkM6DGmcGIHazK56E1bTPvadqqq01pwUvCeWAJsLyUwB4rdGPqyjiKkGzDVnbY3kC9D4CJAN9kODcitYC8hIl67Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDQ3NphGGu6uZfodrKEpWFyCVLCPEE23PT6d7OFTHLsaW49aVKyvLh9StHF-rcUHWxHIMWXfotI68bFU0x5DDhP3aDFmg_FVL20YQKDYUFgjtv53Ls3hvuzB4Z1AjCcpOYKe6QAjE3v1BR3N4UGazXWaQALaNTbaTeY9xdsefMaI3oSaKTYl66wgW1e2F52k3SbmLd8cra46O72DBOYbVQe1ew-hMVT5fZJ1snYo-vUjbFEdH2mCk6njqqINgzxV7gNOE0S5BXPHt-efIWPLPda7PzwW3sGJqpFrWecUOXvWU-zZuyTWwou9VsFr30zZxgQQ_FEje6fGbr-PkOO9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s82PlS0Cd3w-rr5Gc5nYeCPRGFeyfV3x77RghL6gNZYcn64cLhTmckSij0Glaax-x3VlSgur9iFjrAANiq-N8mrDy61QDtUOyx_JC07gj1kHK3aqk0lqRH2Wu0I3cFsVyHKPUthXujtrP8tANcfP4A9G5QzD7M5AnetbGC0Yf_YPCYFJ-QGZP9zhSA_bmh0F_J3NKSDFLqW86n4757OWOskjpwKjWn2suXmlaOHnmfVOBPAu3sa2iHFgsd6rj0wqTGZPLhgkECcm1ZCqwi-Xmpt3JehgLKew1SeSKQBNr3f6jcXj25knBF2qGJeveqMTOSRpf0CUlrfVLOWG_d-wNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443312" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توپخانۀ اسرائیل با بمباران شدید جنوب لبنان، آسمان در بحبوحۀ «آتش‌بس» روشن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443311" target="_blank">📅 00:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
رسانه‌های عبری از هلاکت سرهنگ دوم «دور بن سمحون»، فرمانده گردان ۵۲، در حادثه امنیتی که روز گذشته در جنوب لبنان رخ داد، خبر دادند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443310" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvCJ_Ac9i3nJ48EtdbRvsdDHxVx5FMp-4k19xBCxDRchchuZu6jYBLCHFqc6vJimygPoZFSTLhSNj5eKJ6odVhulS5rqs7WDRocPtGMuDGonQuUb9BJg7afWFG67CmgVudqC4_Bdm0D45gGTID_i05RMRupzW1RKYuyr0r9uQwf1RWTcH7QO2O3rcZ9VZtf7RDWJP1BtjPIcoCGjpzoeqW-L_ieJIsFUTB9R01BPW5M_AxHodzCL4WGlvLqj_3Ct3vszydX6bjWMbXV5zu3vJ2779cwbj-RTfVvjkaZHlm1Jz_grVP_S_GtC0csG2MbT21_oAXE8NpD6xZCLCscbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فعلاً گل‌به‌خودی آقای گل است!
🔸
جدول گل‌زنان جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443309" target="_blank">📅 00:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۵</div>
</div>
<a href="https://t.me/farsna/443308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۴ – کتاب آه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443308" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmDpUlMInzCtfotMJsexwH6FBrTbwY_1GmVmW1ODHWmhyANMghYO94UDTr3BQwU2O6GyRsWInOMiXdMVJilWxEb36wSHmC5br8gY4gLjc81zMiZDmX7P-q2zEOQBhadNxWjZ8alk7asiwdpY52DuJVpe2D7LtNJi2QwSV4qGCFFCKcZb71FnZ-kkjg_G5dWXz73x8M3RItwQjJnLLN9X4UwRXMvMpJU5-WtxTWp0RFwvZMRx5Xu8A4FwWJ3ry3j1nPmDH9tVTOF5CmkIVerLCVXpCMnjQOlKKJLsFPEuiSn0xOtEunjO8rnwAsT-XtUseazuKHwNvgnJqCKrtgjdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اظهارات وزیر خارجۀ فرانسه دربارۀ مردم ایران، اوج نفاق و ریاکاری است
🔹
سخنگوی وزارت خارجه در واکنش به اظهارات وزیر خارجۀ فرانسه نوشت: آقای وزیر، ظاهرا ریاکاری و نفاق تا به امروز از ویژگی‌های بارز فرهنگ سیاسی فرانسه باقی‌مانده است.
🔹
همان رذیلتی که مولیر در نمایشنامۀ «تارتوف یا ریاکار» در سال ۱۶۶۴ به‌درستی درباره‌اش گفت: «ریاکاری به مد روز تبدیل شده است.»
🔹
شما در زمانی که شهرهای ایران با قساوت بمباران می‌شدند و ایرانیان بی‌گناه در میناب، تهران، لامرد، اصفهان و جاهای دیگر به طرز وحشیانه‌ای قتل عام می‌شدند، سکوت کردید و در واقع با متجاوزان همدستی نمودید؛ و امروز در راستای مصالح سیاسی رژیمتان، به ناگاه وجدانتان به‌صورت گزینشی بیدار شده و شما با وقاحت در مورد حقوق بشر ایرانیان موعظه می‌کنید! عجب نفاق و ریاکاری!
🔸
وزیر خارجۀ فرانسه روز گذشته در اظهاراتی عنوان کرد کشورش تا زمانی که مذاکرات هسته‌ای ایران به انتظارات خود نرسد و به موضوع موشک‌های بالستیک و نیروهای نیابتی ایران نپردازد، با لغو تحریم‌های شورای امنیت سازمان ملل علیه ایران مخالفت خواهد کرد. این دیپلمات ارشد فرانسوی همچنین در اظهاراتی به مداخله در امور داخلی ایران پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443307" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEzoG3fhihryBvQFy7azo-Z-L4OK9IODclBvs3Pb0J5jI4MFonXSHkndiSI_gi1UeN-QrmRufJCTc81Qvu1LV_madiwjpUVTP4ASo3y4-VCqYuYBK9fy2rPNMAYQADYM717YRN3grUJuI-txd2cIkOEq3eM5JPhyqxXCScRBV2KApjjiwZuoLb-2eYKmesZ8CpeHSk7b6NsC-Mtx0VGt3yNcx6oHaY_tLWelWggL5ZkGHDI4Aggnq9Ie_eIz02PSYdJUkJAB6tp6v9K-RCSC5ffp9cf87MExGMKQdBG4VeXIaQag51tFja32m9hh0ULAEhOEdNZykLYEtThArGpp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان فضایی: مهم‌ترین پروژه‌هایی که در آیندهٔ نزدیک برنامهٔ پرتابش را داریم، ماهوارهٔ «پارس ۲» است.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443306" target="_blank">📅 00:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=kR1_DA3vprpMlWk_aZc90WZARNhTA83dGqhuQSj-c-XJqYqO03PWXYGEb0G795P7xsIOtQhLjXWaBL4WjTwETzrgqkfZrFhbIDq8Ecrp_2K9y-rMZOswA5jF9GWKOno2Ly8S2CgaKMC7YKwKjcdErhtDhUYG-ZYWICvSR_DqXrE_8xizcgpbLbJdfKeQpi45j9i_7TYs99ty1EsZG6oUiHI0SqiuJSWGYgZu1Kx92R81a-vrqLVv7ae6pZPddbRVcLeT4O9pmirKr-4I5pHPYg2fB_f-n7MQc-Wbf139-mp9gek4uz6aN02Bh8ki4oBISYTrjHL2HyVrzsYPxCGCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=kR1_DA3vprpMlWk_aZc90WZARNhTA83dGqhuQSj-c-XJqYqO03PWXYGEb0G795P7xsIOtQhLjXWaBL4WjTwETzrgqkfZrFhbIDq8Ecrp_2K9y-rMZOswA5jF9GWKOno2Ly8S2CgaKMC7YKwKjcdErhtDhUYG-ZYWICvSR_DqXrE_8xizcgpbLbJdfKeQpi45j9i_7TYs99ty1EsZG6oUiHI0SqiuJSWGYgZu1Kx92R81a-vrqLVv7ae6pZPddbRVcLeT4O9pmirKr-4I5pHPYg2fB_f-n7MQc-Wbf139-mp9gek4uz6aN02Bh8ki4oBISYTrjHL2HyVrzsYPxCGCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔹
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعاً کارش را انجام داد. ما واقعاً در کنار اسرائیل به سختی مبارزه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443305" target="_blank">📅 00:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2fd01ab5.mp4?token=SkFo-5KCchTXq6dt8r5D7-0jidoJbWll2pclvByadoeHDpV8WLnvE5NZUEuWvS0tJz6xad4u5JeoX2Utyh9AUAuDaf2KZCdBmy3wpB8HxPZMQ9_MnPvfPACTKOPIYyV3tGhyjjJFH7U1CCyz1Tn1O06mQautenFpzi_ZVrrKtHehqa3c8nhDPOPT708M706OWl0D0AoJ-REVPryKX6y9_a5afw4PINiMnZdqpwlCtX059BdHUe2hrWql7tWjnN441LLjNqlg1IqLuflL1kVe8txlTJjz9oP1O9HKq4YftoCs0YhIJ7OHMveEXnZWOistAyadgV40iUa7ZQO2piltnQvkFdTRCIC5d1JQgCSiJZarjkgljhlzToUW_psHp8QirOc0a_ltdgjHfcBUMZr0z1s0ph27Vsvg219KN0ZpmlH44pHJDPrbSBtXfPxXYjJfk75H-KBAaSjbZG1TUtWquDoRNXqiTzWegbW7iF99jSzdvWfDT455Yg8mUkuAFtLNSSWSJsjpvXtzimzGu7JAXkYKYhP5dposQhHSVVbVJalMltc_MhT19w0JKCL9OEhbdasrh16RCetEWezMiIEiJbIjK4mTDyTRprldu59Mg1mwb45TA9pamg0MNUXN6lTBT944LYeUb4DOIOxMNyuJYQAh74syNry1ul3hZHDKKwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2fd01ab5.mp4?token=SkFo-5KCchTXq6dt8r5D7-0jidoJbWll2pclvByadoeHDpV8WLnvE5NZUEuWvS0tJz6xad4u5JeoX2Utyh9AUAuDaf2KZCdBmy3wpB8HxPZMQ9_MnPvfPACTKOPIYyV3tGhyjjJFH7U1CCyz1Tn1O06mQautenFpzi_ZVrrKtHehqa3c8nhDPOPT708M706OWl0D0AoJ-REVPryKX6y9_a5afw4PINiMnZdqpwlCtX059BdHUe2hrWql7tWjnN441LLjNqlg1IqLuflL1kVe8txlTJjz9oP1O9HKq4YftoCs0YhIJ7OHMveEXnZWOistAyadgV40iUa7ZQO2piltnQvkFdTRCIC5d1JQgCSiJZarjkgljhlzToUW_psHp8QirOc0a_ltdgjHfcBUMZr0z1s0ph27Vsvg219KN0ZpmlH44pHJDPrbSBtXfPxXYjJfk75H-KBAaSjbZG1TUtWquDoRNXqiTzWegbW7iF99jSzdvWfDT455Yg8mUkuAFtLNSSWSJsjpvXtzimzGu7JAXkYKYhP5dposQhHSVVbVJalMltc_MhT19w0JKCL9OEhbdasrh16RCetEWezMiIEiJbIjK4mTDyTRprldu59Mg1mwb45TA9pamg0MNUXN6lTBT944LYeUb4DOIOxMNyuJYQAh74syNry1ul3hZHDKKwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم اراک: فداییان رهبریم، از شروط نمی‌گذریم
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443304" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33b806bb2.mp4?token=t3Un_a57vDSdFMKRkeiuqjAUCwhON7dBl7K4hM-4gl7i6ij2c4-RqfWeOzDJm4ABE9-QNI97KFvFHEE6xUNA8UUgau3t6hnqdL_hVeTvtNBG1UK9RD_4sgkKErsKMjFziQ_EqmHOHLFeutqw1JcjRIjyPaVzR28E_bW9LMDktsTS1G2H2E98Px1R8_vmQx2d6PEf6FYyVqEh6sBCRzF4mRPeuqVYVYyOL4AX62vaI6D2VV_dlCgAzWkHa9txSkqhOrEEceiFjxpg9O3fZ4G4Tg6gRgTc0niUL4k8BZHPSsBfQKTcFE9cq9cHrNMG2IVmyJQsIy0GmnlJLFlx8v5LVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33b806bb2.mp4?token=t3Un_a57vDSdFMKRkeiuqjAUCwhON7dBl7K4hM-4gl7i6ij2c4-RqfWeOzDJm4ABE9-QNI97KFvFHEE6xUNA8UUgau3t6hnqdL_hVeTvtNBG1UK9RD_4sgkKErsKMjFziQ_EqmHOHLFeutqw1JcjRIjyPaVzR28E_bW9LMDktsTS1G2H2E98Px1R8_vmQx2d6PEf6FYyVqEh6sBCRzF4mRPeuqVYVYyOL4AX62vaI6D2VV_dlCgAzWkHa9txSkqhOrEEceiFjxpg9O3fZ4G4Tg6gRgTc0niUL4k8BZHPSsBfQKTcFE9cq9cHrNMG2IVmyJQsIy0GmnlJLFlx8v5LVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد زنجانی‌ها: حزب‌الله دلاور کنارتیم تا آخر
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443303" target="_blank">📅 23:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891b77b63.mp4?token=bAnzMD_q12SkQXk3qFoR-DgvBxlqOKHrUONslhkicYv5J45UlMdoLvWEvygSv4gly4hgUCUHv6ukSghVe6LqqFqlV5VzylsbGkVra74HN81XYXoL1xC3RvbAwlGEOBpy4Wv9QTM_twHecn514GCBY5RPEhOspDQRZkP4ZLR55yJ0vR4ZLqw4D2M6SySWipVqe48ICtK8ORPf0fHA_z9aIonTZEBFDUua9qTNEzB1CqHykawIsmGqE2T9JZrEWbAm2G28Rpqdg0VZwq3apzfibceFKxtGAXGUQKV0u6alg9_1KroPBvipiVLoxkM8QoPqwk_yggybHYTe8usAOIamig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891b77b63.mp4?token=bAnzMD_q12SkQXk3qFoR-DgvBxlqOKHrUONslhkicYv5J45UlMdoLvWEvygSv4gly4hgUCUHv6ukSghVe6LqqFqlV5VzylsbGkVra74HN81XYXoL1xC3RvbAwlGEOBpy4Wv9QTM_twHecn514GCBY5RPEhOspDQRZkP4ZLR55yJ0vR4ZLqw4D2M6SySWipVqe48ICtK8ORPf0fHA_z9aIonTZEBFDUua9qTNEzB1CqHykawIsmGqE2T9JZrEWbAm2G28Rpqdg0VZwq3apzfibceFKxtGAXGUQKV0u6alg9_1KroPBvipiVLoxkM8QoPqwk_yggybHYTe8usAOIamig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔹
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعاً کارش را انجام داد. ما واقعاً در کنار اسرائیل به سختی مبارزه کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443302" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=og6jppPg9AMWFKOo35lkJNSa83IhVQcNeLSqNfEjZX6-Yg6_QVWAoo3CCucvRL8uFUDJCEfknNsvBK_9Y80cbo3jItxp52T2H8bBr7oGXl1rvxS87FxXLhXQ-Wx3u32Od7pr14YOrZzmYTrrjDuDdQwDoYDNpTXJ8YZ4ySkL9mys06BU7OlpBhyQD0Gh6CvcLH4TffqgwsFs0yZLsq58zzRocgPVMORenMHTTC5ECcnu77AzdE-fb9GlH6lDn4jjW98vfI59rjRToycXLdRra2eR50-wmr4KNGHQkoxQy-QjHYMN0S6SQk5Tj3IYHnnCzBTlVk-h5RUBkd-Qh99VH5mLpl8HADqdTCo5C8wGCWpK01GrTcn17GrYqansQQTV86asRq4pezbSFSzaAmF6vA7XQ6xI_NeesC1HmK3fOXwuDg6F-SQz2c8nBRoaaw5WwSNcpJ1dngsASAwIlz_ORoE2tsKPMp511fWk2kqFyXvA2vORjj8Ck_lCtZm0vIQAbCCyaJQHo9Cb61pjZWWCubVK-hMTlHmlHk7-aPe_s3OZCUpHGLY_g4dajWejKI-NHwH8U0SWRQfvVXcJ8kcZQE6a3fT4-cTfyxcsteVlaq6a-9jQDcEC_e4bVMHovg_AbjfVQPMbkXhSluY38iOf37ahGmB6UCkUArDcN2QNSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=og6jppPg9AMWFKOo35lkJNSa83IhVQcNeLSqNfEjZX6-Yg6_QVWAoo3CCucvRL8uFUDJCEfknNsvBK_9Y80cbo3jItxp52T2H8bBr7oGXl1rvxS87FxXLhXQ-Wx3u32Od7pr14YOrZzmYTrrjDuDdQwDoYDNpTXJ8YZ4ySkL9mys06BU7OlpBhyQD0Gh6CvcLH4TffqgwsFs0yZLsq58zzRocgPVMORenMHTTC5ECcnu77AzdE-fb9GlH6lDn4jjW98vfI59rjRToycXLdRra2eR50-wmr4KNGHQkoxQy-QjHYMN0S6SQk5Tj3IYHnnCzBTlVk-h5RUBkd-Qh99VH5mLpl8HADqdTCo5C8wGCWpK01GrTcn17GrYqansQQTV86asRq4pezbSFSzaAmF6vA7XQ6xI_NeesC1HmK3fOXwuDg6F-SQz2c8nBRoaaw5WwSNcpJ1dngsASAwIlz_ORoE2tsKPMp511fWk2kqFyXvA2vORjj8Ck_lCtZm0vIQAbCCyaJQHo9Cb61pjZWWCubVK-hMTlHmlHk7-aPe_s3OZCUpHGLY_g4dajWejKI-NHwH8U0SWRQfvVXcJ8kcZQE6a3fT4-cTfyxcsteVlaq6a-9jQDcEC_e4bVMHovg_AbjfVQPMbkXhSluY38iOf37ahGmB6UCkUArDcN2QNSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر با ایران سرسختانه‌تر رفتار می‌کردیم تنگه هرمز باز نمی‌شد
🔹
می‌گویند چرا سختگیرتر عمل نمی‌کنی؟ اجازه بدهید توضیح بدهم؛ تنها راهی که می‌توانستم سختگیرتر باشم این بود که دو یا سه هفته دیگر وارد عمل می‌شدم و به بمباران شدید آن‌ها ادامه می‌دادم، درست…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443301" target="_blank">📅 23:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81dafdbf72.mp4?token=e9xcMv9qMNWU29L_pNAVzoXsyQbFYv02_VVuboq2g19ftQaVn-KoV-_GW1t9HsiOExviPOr8WcpQq-KJlnQ8fNIeKnOcA9j4O5zWHAI6gCKBlysgrOjdBxfYX5-Cwr-s3gjNegBBoa0hhJICLsGLQWLmGJTN7qMnd2Nnb7CQubCzzsyPpVJofa4qVdHAppfJbr-cvgA1feMxo_d1qAPuBWCvZ8hfRvzQda9KWZyJ90rhP3IrNPQbUQ4qk4FOza2_bkhgeppPsm8GQVz1tHUVRedAJpIu50i-snzn5hV0h2zFTObDdW2aDJDdhvcT3Ol81MSJsgkhwv3sKPJKNgEp_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81dafdbf72.mp4?token=e9xcMv9qMNWU29L_pNAVzoXsyQbFYv02_VVuboq2g19ftQaVn-KoV-_GW1t9HsiOExviPOr8WcpQq-KJlnQ8fNIeKnOcA9j4O5zWHAI6gCKBlysgrOjdBxfYX5-Cwr-s3gjNegBBoa0hhJICLsGLQWLmGJTN7qMnd2Nnb7CQubCzzsyPpVJofa4qVdHAppfJbr-cvgA1feMxo_d1qAPuBWCvZ8hfRvzQda9KWZyJ90rhP3IrNPQbUQ4qk4FOza2_bkhgeppPsm8GQVz1tHUVRedAJpIu50i-snzn5hV0h2zFTObDdW2aDJDdhvcT3Ol81MSJsgkhwv3sKPJKNgEp_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۱۱ قیام لشگر حسینی مدافعان ایران در الوند
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443300" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2583bd5c.mp4?token=Rq2cx1CNAft9QdwqBLEE0_E-Fu80DlwDN25azFrwhodB9leaLaR0cSjpG8ycM7Ckf-0vVF3h9FA_6EmjKyOCz1z0t5N9B8mno2Drtd7bFNusZDberItcCxIVMlYx6SDjmzHHtJv-P0556KquyzMz8IdFeFQ5wK-Ofr0fGJnCjFjerGZ0Mo4VIITGkbOuJ4WZIg5dzE6vf2l-S9kor1xZG-V7q42xHwImwuYzX1RhMCPuLv8pIVrMUE3onwAgDSEliYr7K-1gy7wH4SGDAVvGFdXzCwWXF8t6GVlGBphrp0N31Yvmn2naKzu5v1sie26Pbd2d8pLqiaDTUHb6-134mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2583bd5c.mp4?token=Rq2cx1CNAft9QdwqBLEE0_E-Fu80DlwDN25azFrwhodB9leaLaR0cSjpG8ycM7Ckf-0vVF3h9FA_6EmjKyOCz1z0t5N9B8mno2Drtd7bFNusZDberItcCxIVMlYx6SDjmzHHtJv-P0556KquyzMz8IdFeFQ5wK-Ofr0fGJnCjFjerGZ0Mo4VIITGkbOuJ4WZIg5dzE6vf2l-S9kor1xZG-V7q42xHwImwuYzX1RhMCPuLv8pIVrMUE3onwAgDSEliYr7K-1gy7wH4SGDAVvGFdXzCwWXF8t6GVlGBphrp0N31Yvmn2naKzu5v1sie26Pbd2d8pLqiaDTUHb6-134mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام تجمع امشب مردم شهرکرد لبیک به رهبر معظم انقلاب بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443299" target="_blank">📅 23:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-WqirGETrWB67xynh0F0AOnKfB97eseJjitQzhc2bPM_VEvoPSdNGOC3cQwOI6IJst2RQ6qf7_5eIYXz-diNSDltBccY-OPjQ4UGCpDecHvNCZAm1mz-enioQvIClWydL03d_-ICHKRamt27XaBASjSC3Cfu-HBS5pTdf2D3LJ5vUGuHXszOryD945wrDl-7ZRTyfgxqLAIR3RdCdGbcyytvSzEe_lu7q0E7leJUps4zCkS5g4TFvVF5IuR5_ghmWLk59ab8098AMvXNRxmckiIQWS3TqneLa2eek1qzylw6XSxzY8XpZuJsljWTcemZ77s2f__saFm6YYSs6toog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله گروهی از نظامیان اسرائیلی را هدف قرار داد
🔹
به گفته منابع لبنانی، رزمندگان حزب‌الله یک بمب را در مسیر تعدادی از نظامیان اسرائیلی که در حال عبور از منطقه علی الطاهر بودند، منفجر کردند.
🔹
در این حمله چند خودروی نظامی آتش گرفت و تعدادی از نظامیان اشغالگر نیز زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443298" target="_blank">📅 23:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df838b83ae.mp4?token=lofmiVBHFsT1xSYurlbb9KxxVIZIvSSzVoO5ztoNI5hrYsDMWELe5fksF58Lojbh9NuS8OK3ZTTHfc0Rb63cDndh6_NwGnrX-YR4bQbZq8V4-JTGf5shEx3kqLg-3B9eiq9Rnbs6nnmY0vBIQFMTfy9SU8QStkPMyiZCTpuCV1S12eRVU8shLCMEYCg5ACBNbIos6qmVmSyJR5q7tpRkLfQPuuSVo-SzVebocsnGyjIFqZC5IX7407F5TJkzDySiGY5Rq8j-3Ws6hexExbeWpYkn7owJsA6wYE98kQA2Mc9CYU4ryXibQC3SWEk9U5rg-latKXwGs54BBEFy3FJ9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df838b83ae.mp4?token=lofmiVBHFsT1xSYurlbb9KxxVIZIvSSzVoO5ztoNI5hrYsDMWELe5fksF58Lojbh9NuS8OK3ZTTHfc0Rb63cDndh6_NwGnrX-YR4bQbZq8V4-JTGf5shEx3kqLg-3B9eiq9Rnbs6nnmY0vBIQFMTfy9SU8QStkPMyiZCTpuCV1S12eRVU8shLCMEYCg5ACBNbIos6qmVmSyJR5q7tpRkLfQPuuSVo-SzVebocsnGyjIFqZC5IX7407F5TJkzDySiGY5Rq8j-3Ws6hexExbeWpYkn7owJsA6wYE98kQA2Mc9CYU4ryXibQC3SWEk9U5rg-latKXwGs54BBEFy3FJ9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بجنورد در تجمع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443297" target="_blank">📅 23:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cea19557.mp4?token=UhIch277zyOvxSgTzCJaCxqx-JQ09WZB-KBpFxCHTw-5X8bPgplMGwhkV1MONAiIPFEWEfPiAdG-ujw5GIn3UMTM2QBiLbXTrE8hBXg1DDA6QMraehzywa0_rZkjU3-wHD-3nnetkiY7AU0Cy86xSqnURltRW6ZRQTpjgwZUoeA66ddsr4y668NAm8YE2BfJM0G_8SA2X9NpTmMYTSkfVjywNNB7xOFb_5FgXrYoQ1DozWnt7W64lMpoDqnPZIlCxnAI4xHBDl52ZoL2c3XQdpm17bSTnlDD1QiPhjtK2Mzqpymb75qSvAxA5UgQWmtWr4GWks157o1A2UUhEYnpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cea19557.mp4?token=UhIch277zyOvxSgTzCJaCxqx-JQ09WZB-KBpFxCHTw-5X8bPgplMGwhkV1MONAiIPFEWEfPiAdG-ujw5GIn3UMTM2QBiLbXTrE8hBXg1DDA6QMraehzywa0_rZkjU3-wHD-3nnetkiY7AU0Cy86xSqnURltRW6ZRQTpjgwZUoeA66ddsr4y668NAm8YE2BfJM0G_8SA2X9NpTmMYTSkfVjywNNB7xOFb_5FgXrYoQ1DozWnt7W64lMpoDqnPZIlCxnAI4xHBDl52ZoL2c3XQdpm17bSTnlDD1QiPhjtK2Mzqpymb75qSvAxA5UgQWmtWr4GWks157o1A2UUhEYnpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ماکرون زمان زیادی رئیس‌جمهور فرانسه نخواهد بود
🔹
امانوئل ماکرون، رئیس‌جمهور فرانسه که البته دیگر زمان زیادی در این سمت نخواهد بود، در میزبانی اجلاس جی۷ عملکرد فوق‌العاده‌ای داشت.
🔹
او حدود یک هفته قبل از مراسم از من دعوت کرد و گفت: «می‌شود لطفا لطفی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443296" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86872fd21b.mp4?token=FiEuLVoXDCE42i4fjmffkklmxkW0-cSo3Twlid0q5gTwewQJGQalnnc8u4kOWgDxZAsFfZRQsRk9DXY8umCvPCRc5G1Sik9RlAtCvEW8A56Yj-9om2rIVEUnWPmDB2jl4RGgJFTZ5JkcfaqaZtjJXj4nEFMu9t8ygIl-37wNgILy_QWaN_fUlVFE1HS6XEUREeyPjEtOMtMqx7X_t_lJy9cUvr79hche7RWARwhvDgESqGPKzIWTutGtsHSF8MsSV0cp7IGrH1w0KxcwRnubLMAAMmnlcap-qwUIU4C9MYuIwWDik0ToI28fCroJ-JhE95pdrhdKsOxJimliKz8f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86872fd21b.mp4?token=FiEuLVoXDCE42i4fjmffkklmxkW0-cSo3Twlid0q5gTwewQJGQalnnc8u4kOWgDxZAsFfZRQsRk9DXY8umCvPCRc5G1Sik9RlAtCvEW8A56Yj-9om2rIVEUnWPmDB2jl4RGgJFTZ5JkcfaqaZtjJXj4nEFMu9t8ygIl-37wNgILy_QWaN_fUlVFE1HS6XEUREeyPjEtOMtMqx7X_t_lJy9cUvr79hche7RWARwhvDgESqGPKzIWTutGtsHSF8MsSV0cp7IGrH1w0KxcwRnubLMAAMmnlcap-qwUIU4C9MYuIwWDik0ToI28fCroJ-JhE95pdrhdKsOxJimliKz8f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین مرگ بر آمریکا در تجمع مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443295" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfDfXfd0BizKcbbw43Vj_GIKOyyIVsSqN1P8PDSrzXChis8iYxp2KvAQt26JAWQLtUh-lTIQ7D0ENpkKi8eTfb24hcX7hc2kGElTPv2mIxH-kZoFZguxDgNkCVFXsf6SW0TxgTFhWLvg6QVfbeCcXPLJt6MxK2SAieFvHOp23Mlz51uV9GORJzgNky9hQKwWE3P42AcmqxepS8KJEImwm0_p3a-b-GVMAx8slb2kv90L8yYUqJ_w4DTmBAQHA9KKRy6F8Jw9ThzKvyh_kGsPei3o2ZZ14BHQBYlDfBLz0JkvKF7KFv4imyjcpaP41smVnMAVNZP2bAQfUafBwNGT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: حکمرانی بر تنگۀ هرمز و اقتدار منطقه‌ای ایران نباید تضعیف شود
🔹
متنی که برای توافق تهیه می‌شود باید از نظر فنی و حقوقی کاملاً دقیق و متناسب با خواسته‌های ما باشد؛ در مورد رفع تحریم‌ها، باید کلمات به دقت تنظیم شوند. در مورد رفع محاصره نیز باید به طور مشخص بیان شود.
🔹
مثلاً ما در این ۱۴ بند خواسته‌ایم که نیروهای آمریکا ۳۰ روز پس از توافق نهایی از پیرامون ایران خارج شوند. اما ممکن است آن‌ها بگویند که «پیرامون شما» شامل ۱۲ مایل ساحلی آب‌های شماست که این برای ما قابل قبول نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443294" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de95f3d4c.mp4?token=E8lxso9plZtil2HvVe84QNS8PD2xieynyzTYPv-oyt-GWjG3zEev6n-l9QCIiRK6ynLvMNhc_lK4zkxHCaERATM3o61EryA57SkDHUDssEfDg6hsUxQ9ucJnAeSU1Z8UKi2D_zVEwIF_NgkIsleY08z0aWXGQBx85D9fKA8SubEmsCI815ck_Sx6ClwVwRszmtvfneobQ5UBSHkawJvVMqK0r8j-03mUBtJmtVM4v9UCYm5LEeI2e5nMNx62V3H88KU2u2eIg5ISZxPfnsM9rFD2r0dIve3BQRE6tdPLU7lBgtvnA9IpDviQ0DTWZs37tbVCyfNW_vx9LQhBRuPWWYgUdRd6DrAE5drnlSnZ_74-ND4Z9gMxArtfqphH5tyyymA02SoCxjsQ9D_nkQXLsFrMFQoxu10q_0HkSFKk_CayToLCCZ6TPOA2Hycq9qNZJNyPtziAWOj4M4VRgpgFfFoHuRI53z0_R-mfJ8o_PYVfMN9eiHBiII74lUNhVkFwaoO0oKws_XAvC64pjgdYCE937c4fyfSo8-Q5yINfVsqWBD7Eb37ocTSJ39SJdORzQ_LTj4NI1o0Gr_JM-zCNbDyL-m2Tad9z2-El-q0mZO6fWYuTqkFaa3l-dRdNLxGtE5XK5IgKDZ6S-RUgQpXlqJeNAPmHDUASfnwcgy7k_kE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de95f3d4c.mp4?token=E8lxso9plZtil2HvVe84QNS8PD2xieynyzTYPv-oyt-GWjG3zEev6n-l9QCIiRK6ynLvMNhc_lK4zkxHCaERATM3o61EryA57SkDHUDssEfDg6hsUxQ9ucJnAeSU1Z8UKi2D_zVEwIF_NgkIsleY08z0aWXGQBx85D9fKA8SubEmsCI815ck_Sx6ClwVwRszmtvfneobQ5UBSHkawJvVMqK0r8j-03mUBtJmtVM4v9UCYm5LEeI2e5nMNx62V3H88KU2u2eIg5ISZxPfnsM9rFD2r0dIve3BQRE6tdPLU7lBgtvnA9IpDviQ0DTWZs37tbVCyfNW_vx9LQhBRuPWWYgUdRd6DrAE5drnlSnZ_74-ND4Z9gMxArtfqphH5tyyymA02SoCxjsQ9D_nkQXLsFrMFQoxu10q_0HkSFKk_CayToLCCZ6TPOA2Hycq9qNZJNyPtziAWOj4M4VRgpgFfFoHuRI53z0_R-mfJ8o_PYVfMN9eiHBiII74lUNhVkFwaoO0oKws_XAvC64pjgdYCE937c4fyfSo8-Q5yINfVsqWBD7Eb37ocTSJ39SJdORzQ_LTj4NI1o0Gr_JM-zCNbDyL-m2Tad9z2-El-q0mZO6fWYuTqkFaa3l-dRdNLxGtE5XK5IgKDZ6S-RUgQpXlqJeNAPmHDUASfnwcgy7k_kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری شیرخوارگان بروجردی در حماسۀ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443293" target="_blank">📅 22:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f337e5e65.mp4?token=D7lfpFjwqbTHh0g3gf_EM0siAffLJy8U6xDfpj_4autA0kblmDG8qLAmwgA5N4Uq0YzsZuXVvqiV8_pJ8thuF7FxJSqn9gQZC0Z6sSaMF1jfgLDZUsXetr4lwPLQAenQZDr2uZwYF5hq9DIZgY8vVxGYDcOMngOmrkz30Qz_xOxRl_1hCUKCLpdr-usEISeL5CINWxksLGTBkmJVDkXFwfpBpF_iFAo6Cc_LA2BHEUXEqw-FUHmdrRJk1pLFd49E-UbgexdiYks5VlpCeI2yWOjkp_eThKkgvPLdIPwT9ADx0PCXgxHjrm-aSF0hm00xCkF5pEEidBFByLe5NT4aTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f337e5e65.mp4?token=D7lfpFjwqbTHh0g3gf_EM0siAffLJy8U6xDfpj_4autA0kblmDG8qLAmwgA5N4Uq0YzsZuXVvqiV8_pJ8thuF7FxJSqn9gQZC0Z6sSaMF1jfgLDZUsXetr4lwPLQAenQZDr2uZwYF5hq9DIZgY8vVxGYDcOMngOmrkz30Qz_xOxRl_1hCUKCLpdr-usEISeL5CINWxksLGTBkmJVDkXFwfpBpF_iFAo6Cc_LA2BHEUXEqw-FUHmdrRJk1pLFd49E-UbgexdiYks5VlpCeI2yWOjkp_eThKkgvPLdIPwT9ADx0PCXgxHjrm-aSF0hm00xCkF5pEEidBFByLe5NT4aTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من بزرگ‌ترین پل ایران را به این دلیل که آن‌ها دیر به یک جلسه رسیدند، از بین بردم
🔹
آن پل، در واقع حکم پل جرج واشنگتنِ آن‌ها را داشت. من آن را ظرف ۳ دقیقه با خاک یکسان کردم. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443292" target="_blank">📅 22:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8222fb9f5a.mp4?token=svSUSGHP1U8Xyj2g_lcxQHlkyC-eb6jXuadxKRv9-MgS3ArRBOLjpJpTC_Ff9LUmCINzqB7IrUot6t-UzJpl0-1q2sfJZq6mGLfuPgEhFAu72jzz2VoaO4kAzpIjMVOV9Sjm90N7G06j5etFleRrJMNwuMTa3xZeLjltrueHwOJVimyIALabPqMZJELLB9dIhrzVR5Xhccv02zckAU16Dyi1UGFaUQlogJkkzzzjwOLR8ScLb84CRub4oYLMIbYF-wMz9cBx-1mNP0xtRDyKSziXTBsTKXw4fVN7stBS5KGtahTW5BAQctDbT3i9iCuCp6GQbhm_kLP4Y3rJcBrwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8222fb9f5a.mp4?token=svSUSGHP1U8Xyj2g_lcxQHlkyC-eb6jXuadxKRv9-MgS3ArRBOLjpJpTC_Ff9LUmCINzqB7IrUot6t-UzJpl0-1q2sfJZq6mGLfuPgEhFAu72jzz2VoaO4kAzpIjMVOV9Sjm90N7G06j5etFleRrJMNwuMTa3xZeLjltrueHwOJVimyIALabPqMZJELLB9dIhrzVR5Xhccv02zckAU16Dyi1UGFaUQlogJkkzzzjwOLR8ScLb84CRub4oYLMIbYF-wMz9cBx-1mNP0xtRDyKSziXTBsTKXw4fVN7stBS5KGtahTW5BAQctDbT3i9iCuCp6GQbhm_kLP4Y3rJcBrwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: بدون تغییر رفتار ایرانی‌ها هیچ‌ سرمایه‌گذاری‌ای در ایران انجام نخواهد شد
🔹
بزرگ‌ترین سوءتفاهم این است که تصور می‌شود سرمایه‌گذاری در ایران بدون هیچ‌گونه تغییری در رفتار [ایران] انجام خواهد شد.
🔹
این ایده که اماراتی‌ها یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، بدون اینکه ایرانی‌ها رفتار خود را تغییر داده باشند، کاملاً مضحک است.
🔹
آن‌ها چنین کاری نخواهند کرد و ما نیز اجازه این کار را نخواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443291" target="_blank">📅 22:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c612bc2d1.mp4?token=AG4JKL8C9j3TqzNRMaQdHQA9JBHHb_OdbSd45OVbwwjO3OjcXaKCe8pao_Py3lx0Vb9Eg9Hrvw9gTscbsmocN3I3oKRgSqmAINKrij2nvJKBFqmiu1i_GCE0lzS-2xt1E6n6zfsPp6fPDRGgmFtPepCNvMoTKZsDmyyXkPualltdflb-QFTYC8TAWS2ojby6gPKtutBGnYdn6tIKyAhFu2gWMt6aQduMosGwJkBabtdFV-jbQJxDgsK2MnbohRYC-BVcosK0Fv6nAaWHH0rLG1qySfNs79NDY2KU_2gpfoU7JSKclFaZgL4WXxbIHnK0uGfjX8DfyWGAfcLks0yxGpCVMF8Roagxe6BrDVlL6hek6IKJTOEp_BUGZsUJUX0rgjxuJX-BhuFi7jnW0sB2dWdJ9rOBmfK2BTMf3KP9AKYYLX-LyGSS4iKxiL7H1wOEneu-rAeBNqFX8Vn7sD_l6xeQkJvhVB1rEY-Ou_NiFuc6M6Hx69-M1ZV5zEVFwUXPIlrVBunQ0_r8uGM6OOt9mo3-BRmauHNDqhJ7u4UsxZTuVfXk9_qfcJV4lARv9cPYlh-kDuS8NIyMVHYEVhUFvXZGJqd21cLxSY48Fsv1Q78JVKPcPFvJ70A0o9wN7pI99rY7s4MeCspiADrBEEXNd884LMRB3i4E5UkXBeMP4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c612bc2d1.mp4?token=AG4JKL8C9j3TqzNRMaQdHQA9JBHHb_OdbSd45OVbwwjO3OjcXaKCe8pao_Py3lx0Vb9Eg9Hrvw9gTscbsmocN3I3oKRgSqmAINKrij2nvJKBFqmiu1i_GCE0lzS-2xt1E6n6zfsPp6fPDRGgmFtPepCNvMoTKZsDmyyXkPualltdflb-QFTYC8TAWS2ojby6gPKtutBGnYdn6tIKyAhFu2gWMt6aQduMosGwJkBabtdFV-jbQJxDgsK2MnbohRYC-BVcosK0Fv6nAaWHH0rLG1qySfNs79NDY2KU_2gpfoU7JSKclFaZgL4WXxbIHnK0uGfjX8DfyWGAfcLks0yxGpCVMF8Roagxe6BrDVlL6hek6IKJTOEp_BUGZsUJUX0rgjxuJX-BhuFi7jnW0sB2dWdJ9rOBmfK2BTMf3KP9AKYYLX-LyGSS4iKxiL7H1wOEneu-rAeBNqFX8Vn7sD_l6xeQkJvhVB1rEY-Ou_NiFuc6M6Hx69-M1ZV5zEVFwUXPIlrVBunQ0_r8uGM6OOt9mo3-BRmauHNDqhJ7u4UsxZTuVfXk9_qfcJV4lARv9cPYlh-kDuS8NIyMVHYEVhUFvXZGJqd21cLxSY48Fsv1Q78JVKPcPFvJ70A0o9wN7pI99rY7s4MeCspiADrBEEXNd884LMRB3i4E5UkXBeMP4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بجنگ پهلوان بجنگ
نماهنگ جدید مهدی رسولی در آستانه دیدار تیم ملی فوتبال ایران با بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443290" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e3f93872f.mp4?token=BrbQmg_yw0w-3u_ZZsYplMxHJX-9V1pYbTfmOJLlOoj9X9R9Got_9Hv7iiDF3r50qU2TAxlKqVMA_QZgysYBWkyCTFKgGzYC99e61xdCDP9_df5qWZXVU53NEvFF6-R939_h_ZCL3ei8cmhIn2nXKaq4l6KiTtZjZWPR27cxah7vRI8Tkzwzkhz1embUMBkh_DWtbT9_7qMeYzdq-6SUHOKDE9zDrtIvW1dXop7spA_-9dH0_auW4xT5zyLqtLRGD7owZv586DJHblZdqUPAEEUz8OrYdZ6TpNJ_nsjOsvNQXeMnkPrt189cSoZqxysxz97PNshjq1faqIxXrPUWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e3f93872f.mp4?token=BrbQmg_yw0w-3u_ZZsYplMxHJX-9V1pYbTfmOJLlOoj9X9R9Got_9Hv7iiDF3r50qU2TAxlKqVMA_QZgysYBWkyCTFKgGzYC99e61xdCDP9_df5qWZXVU53NEvFF6-R939_h_ZCL3ei8cmhIn2nXKaq4l6KiTtZjZWPR27cxah7vRI8Tkzwzkhz1embUMBkh_DWtbT9_7qMeYzdq-6SUHOKDE9zDrtIvW1dXop7spA_-9dH0_auW4xT5zyLqtLRGD7owZv586DJHblZdqUPAEEUz8OrYdZ6TpNJ_nsjOsvNQXeMnkPrt189cSoZqxysxz97PNshjq1faqIxXrPUWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران گرگان امشب در خیابان نماز استغاثه خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443289" target="_blank">📅 22:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64596567.mp4?token=XtiTlVkgTE-iIskFON0Hw4G4r-ZyK49kvwTHplO1NQaNtqXmukkqQDAGNzmGRJUkNGoQv3DyQOqzO5ZTGRaTus_A6_vyO6Y6I7RD-F40wo3WS8rmbCpOqSjKCCQtfo50y8dmGMdDZkKJv6BQ94Ie5qlawHjtH0-sSlN0uITwvnDBBVtj10zCdqqKTTK2ozRnv4Q5zlwCrNyhRu8lmXqgJQY8h_ftpnrTpppz7z9BGdAJamll7Z9x2sAERglGa5-d7PCJgwupRBUIFCVi8Qgu3Hgu_fIurEJycaE0JEJvHKpTjS0vM8MTs2qgksFdbsni_-MCRPu5sSjMio2ZEbVcFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64596567.mp4?token=XtiTlVkgTE-iIskFON0Hw4G4r-ZyK49kvwTHplO1NQaNtqXmukkqQDAGNzmGRJUkNGoQv3DyQOqzO5ZTGRaTus_A6_vyO6Y6I7RD-F40wo3WS8rmbCpOqSjKCCQtfo50y8dmGMdDZkKJv6BQ94Ie5qlawHjtH0-sSlN0uITwvnDBBVtj10zCdqqKTTK2ozRnv4Q5zlwCrNyhRu8lmXqgJQY8h_ftpnrTpppz7z9BGdAJamll7Z9x2sAERglGa5-d7PCJgwupRBUIFCVi8Qgu3Hgu_fIurEJycaE0JEJvHKpTjS0vM8MTs2qgksFdbsni_-MCRPu5sSjMio2ZEbVcFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها مردم بسیار باهوشی هستند
🔹
من باید آن‌ها را متوقف می‌کردم، زیرا اگر به سلاح هسته‌ای دست پیدا می‌کردند، از آن علیه اسرائیل استفاده می‌کردند.
🔹
من به توافق باراک حسین اوباما، یعنی برجام، پایان دادم؛ توافقی که مسیری برای دستیابی ایران به سلاح…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443288" target="_blank">📅 22:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf812ba81f.mp4?token=nT7CV0oPeI4S-3R7uxhOp_G0Kd4oroEs4HZmA2kBVUtfH3_drvksA-mfHuwS3mGBJIs6xCJ3y3zdVtwiGdOv3SLc0oRm-elETnXbBopsiFcz683rftCN8rhomV5eVkKgzN-z1hZMMEmVGUCc3w9G_DPDM8PWGB8mM0eos_-OrBkYDg_8MFZ1Z6X5HTvt4Epu0QFDPb7ZpzL_xCUJQ7crVwc0ANYW8yUx77Ko27YCwiOaZR2-2wbyvc4Xbvn1qAJ0ZMOPyFgjs2vf7eJwkLHyfteMz9CXr9h0JTkZX3QVtwUVOvGQsTlsGB1lNrsQ07CZ9UTD8bKffPAzwPlvD_K7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf812ba81f.mp4?token=nT7CV0oPeI4S-3R7uxhOp_G0Kd4oroEs4HZmA2kBVUtfH3_drvksA-mfHuwS3mGBJIs6xCJ3y3zdVtwiGdOv3SLc0oRm-elETnXbBopsiFcz683rftCN8rhomV5eVkKgzN-z1hZMMEmVGUCc3w9G_DPDM8PWGB8mM0eos_-OrBkYDg_8MFZ1Z6X5HTvt4Epu0QFDPb7ZpzL_xCUJQ7crVwc0ANYW8yUx77Ko27YCwiOaZR2-2wbyvc4Xbvn1qAJ0ZMOPyFgjs2vf7eJwkLHyfteMz9CXr9h0JTkZX3QVtwUVOvGQsTlsGB1lNrsQ07CZ9UTD8bKffPAzwPlvD_K7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند
🔹
گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند.
🔹
پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443287" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=e_UTvQxjclVgnqmopjQqXWJ-s3afOaLCGDBbBl4KXZt058rbJSOcf0VN3huwWDXm17YEpw17S7wiEyR2uuhzOrWUCTDGxHPmfYgYNmnYESoj9datJjZdx4SgxsW4qc3JVX-ITWGVVG-Or8byBxF_f_KAQaVboqQcCkZu9sAOTjsABFWqHO2UM7Z7eQSJx6D5UQuAg9gJJQ2Yer9y6xFeXxHttf_DHSt1YvUeWGKyFrnnDqaCns62Sams-DIb_xx_U52uBjkELASCxYXWSeok4gZZzC1F9H9CnkXUiKPgQqqZsEe9M7bzQKvCEFnXCF41_XtzH4xZU7CLyO6CYA14mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=e_UTvQxjclVgnqmopjQqXWJ-s3afOaLCGDBbBl4KXZt058rbJSOcf0VN3huwWDXm17YEpw17S7wiEyR2uuhzOrWUCTDGxHPmfYgYNmnYESoj9datJjZdx4SgxsW4qc3JVX-ITWGVVG-Or8byBxF_f_KAQaVboqQcCkZu9sAOTjsABFWqHO2UM7Z7eQSJx6D5UQuAg9gJJQ2Yer9y6xFeXxHttf_DHSt1YvUeWGKyFrnnDqaCns62Sams-DIb_xx_U52uBjkELASCxYXWSeok4gZZzC1F9H9CnkXUiKPgQqqZsEe9M7bzQKvCEFnXCF41_XtzH4xZU7CLyO6CYA14mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود
🔹
پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443286" target="_blank">📅 22:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=SekhbbJ1DUUZHNoaabYFDE0BiwJNk9eGEnGgpRSxjnFN4g2KongDtqLizWNgITsDBf7AEc8o01KydvsqhV0KomtU5-PMkIkjnzVaYhTOVZg0Bi7oEhQm71_9VrVYzKQhBaNfM2Lota6o3ELlptTxF2eGF5u-MUNmO-pSk_Z8uVGLhS2UTl1fOVNoQz07Qjdc4nkEogMAlAZg4mx3zvBMgQNFJC8BooMSXB8Y4k2-6Zy4xeMCkQGBYSzLVhYIHqaYTGzrLodx_UcdebgOerlYWSAItDlpDkHXT8QICHVh0YJhwvHHnBMriuQsCUB5ggqzVFskxqRYuR8VY9-FNOBc9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=SekhbbJ1DUUZHNoaabYFDE0BiwJNk9eGEnGgpRSxjnFN4g2KongDtqLizWNgITsDBf7AEc8o01KydvsqhV0KomtU5-PMkIkjnzVaYhTOVZg0Bi7oEhQm71_9VrVYzKQhBaNfM2Lota6o3ELlptTxF2eGF5u-MUNmO-pSk_Z8uVGLhS2UTl1fOVNoQz07Qjdc4nkEogMAlAZg4mx3zvBMgQNFJC8BooMSXB8Y4k2-6Zy4xeMCkQGBYSzLVhYIHqaYTGzrLodx_UcdebgOerlYWSAItDlpDkHXT8QICHVh0YJhwvHHnBMriuQsCUB5ggqzVFskxqRYuR8VY9-FNOBc9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود
🔹
پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443285" target="_blank">📅 22:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cbc790f95.mp4?token=c1uue161fhTpWgcadC9KSSj1_EfacljbOc76Rng5BZnsJ5wvwHS6LcJQ_SAi-kiRZpbSxovC0w-mnvSAVgPPkeeCMujd4e1Kkb6vHQhJCaQYDvcxo1XlYj5_HvtoiELjeB8TY_4qC3AQdrtA7qd2z8LRqdRxzzbkY6q7ddYxmsnmPvKq5dmcVbVQrOcCji3vLSzUXTEzFTQOXPTmquN4SoGdxbQPTg8KkIWIUXdTwmUC09H3hENksnueCPSoC9Kg14Txftt3P2HxIM-OpoAZBWp2O7P_xz2pjEO63fFWPwZrUNVpQQldJZJYDu-7z3ahin1kfVYo3Sk-dL3U504TsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cbc790f95.mp4?token=c1uue161fhTpWgcadC9KSSj1_EfacljbOc76Rng5BZnsJ5wvwHS6LcJQ_SAi-kiRZpbSxovC0w-mnvSAVgPPkeeCMujd4e1Kkb6vHQhJCaQYDvcxo1XlYj5_HvtoiELjeB8TY_4qC3AQdrtA7qd2z8LRqdRxzzbkY6q7ddYxmsnmPvKq5dmcVbVQrOcCji3vLSzUXTEzFTQOXPTmquN4SoGdxbQPTg8KkIWIUXdTwmUC09H3hENksnueCPSoC9Kg14Txftt3P2HxIM-OpoAZBWp2O7P_xz2pjEO63fFWPwZrUNVpQQldJZJYDu-7z3ahin1kfVYo3Sk-dL3U504TsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من از رئیس‌جمهور چین خواهش کردم و گفتم واقعاً ممنون می‌شوم خودتان را درگیر ماجرای ایران نکنید
🔹
او می‌توانست وارد این موضوع شود. او می‌توانست یک نفت‌کش بزرگ را به همراه دوازده ناوشکن به منطقه بفرستد تا ببیند آیا می‌تواند با درگیری، راه خود را از میان…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443284" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار و تیراندازی در شهر مهران
🔹
فرمانداری مهران: به دلیل تمرینات رزمی یکی از یگان‌های نظامی در حاشیه شهر، فردا از ساعت ۶ صبح تا پیش از ظهر احتمال شنیده‌شدن صدای انفجار و یا تیراندازی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443283" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=fXJpoxKEtSQk0tApyVv71N3zZMFoCgbwtJSLO12WPhqetKYvAepmfldD8QTbgAJbuA4rrUfs3JU9ZysPVbuGCi1O3wMQxl5MgS9dDR-HP6y8seFYTQFUxXjONv1NThJbSJSjOEe_-cvT4-sfNG4e1aldc8xpS5MSKIx338t2DLrR4JE37tSwvl60N2BD07mxmXwc1gHj8OOrZrG1a3hfFSMfpcToKinmjIIPrH60mDRBcLB0duub0j9ahVI253xykikF9lpqkGnVuMIfHKTv82Sz-G9JnYX2fy1crVbNOVr0zcW26W3JCyz3h8wfz3akIHpXQXt-7NSBFoneiAfAtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=fXJpoxKEtSQk0tApyVv71N3zZMFoCgbwtJSLO12WPhqetKYvAepmfldD8QTbgAJbuA4rrUfs3JU9ZysPVbuGCi1O3wMQxl5MgS9dDR-HP6y8seFYTQFUxXjONv1NThJbSJSjOEe_-cvT4-sfNG4e1aldc8xpS5MSKIx338t2DLrR4JE37tSwvl60N2BD07mxmXwc1gHj8OOrZrG1a3hfFSMfpcToKinmjIIPrH60mDRBcLB0duub0j9ahVI253xykikF9lpqkGnVuMIfHKTv82Sz-G9JnYX2fy1crVbNOVr0zcW26W3JCyz3h8wfz3akIHpXQXt-7NSBFoneiAfAtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی جنگ شروع شد، فکر می‌کنم بزرگ‌ترین غافلگیری برای من این بود که تقریباً بلافاصله، موشک‌های ایران به‌سمت قطر، عربستان، امارات، کویت و بحرین دیگر شلیک شدند
🔹
آن ۵ کشور مستقیماً به‌سمت من آمدند و با من همراه شدند. آن‌ها فوق‌العاده بودند. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443282" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3679be7cc8.mp4?token=vwQRqKJvpUX0o5a_WQi3dhEWi9t2D7ktGfzwk9i4CwsiepQlXFCVHM3cWQgi6lOf7DzOz0_3Q68NqwzsMbLEvbuHdEyqrJMmd9-WpYvSyqOez2RMLbXf3WLR5YgBGBKmdRCCr5IZgCu6evfIeB7G5FWUjR3_-aayfRz2rlyXPmlfnffxpWq2DcL38iQl83BgKGmLBy5Cj7gBDNeEFZ0ICr92TTX6ZoL339nyjsZB3WmxWtbvMP5J4pryP1wCcP38_8Y0sOiMqD34HywlzpOwWDhRs5u0mPJs5mlvKHA5hgbsl_OadWFrarXPt_Hs-Y0-RGNJuwyzTv_RuA-50fvhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3679be7cc8.mp4?token=vwQRqKJvpUX0o5a_WQi3dhEWi9t2D7ktGfzwk9i4CwsiepQlXFCVHM3cWQgi6lOf7DzOz0_3Q68NqwzsMbLEvbuHdEyqrJMmd9-WpYvSyqOez2RMLbXf3WLR5YgBGBKmdRCCr5IZgCu6evfIeB7G5FWUjR3_-aayfRz2rlyXPmlfnffxpWq2DcL38iQl83BgKGmLBy5Cj7gBDNeEFZ0ICr92TTX6ZoL339nyjsZB3WmxWtbvMP5J4pryP1wCcP38_8Y0sOiMqD34HywlzpOwWDhRs5u0mPJs5mlvKHA5hgbsl_OadWFrarXPt_Hs-Y0-RGNJuwyzTv_RuA-50fvhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم اسرائیل نابود و تارومار شده بود
🔹
نتانیاهو همکاری خوبی با من دارد، اما خودش به شما خواهد گفت که تسلیحات اصلی در دست ماست، تمام توافق در اختیار ماست و بمب‌افکن‌های بی-۲ و دیگر تجهیزات متعلق به ما هستند.
🔸
مجری: آیا می‌توانید مانع حملهٔ…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443281" target="_blank">📅 21:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df62eb34e.mp4?token=jVlc_zXKkB0TPvMSNTONfUHOZskSvlawGpbUPTKnv6XStQ1WIrzX2-SC0tVThr2q88X-dQuUBuN79G5HNd_N0hpxxh6ttgJ1Uik6GCYcE17NtUyjkWMAZipbg3_iCFQQmUoyGQ22GkbM0IbyRn26UcwWeh9jN7scvst7EbDdzJDFMa9esPhUc6QGGCdSJFJhCgliVEvQBjBLab7DI04fahjGlAaBc2C6FcUQK9Qu3ADFOH7qyn2kSl24_I4tkA8DCnl8zujanzae6f_0_zrhFGuIhm8sHX6xj-GXWoN9wigwI9QW0Ah5hiKkSELB8S6TyB5hk-NIMk6OYmpEt7nOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df62eb34e.mp4?token=jVlc_zXKkB0TPvMSNTONfUHOZskSvlawGpbUPTKnv6XStQ1WIrzX2-SC0tVThr2q88X-dQuUBuN79G5HNd_N0hpxxh6ttgJ1Uik6GCYcE17NtUyjkWMAZipbg3_iCFQQmUoyGQ22GkbM0IbyRn26UcwWeh9jN7scvst7EbDdzJDFMa9esPhUc6QGGCdSJFJhCgliVEvQBjBLab7DI04fahjGlAaBc2C6FcUQK9Qu3ADFOH7qyn2kSl24_I4tkA8DCnl8zujanzae6f_0_zrhFGuIhm8sHX6xj-GXWoN9wigwI9QW0Ah5hiKkSELB8S6TyB5hk-NIMk6OYmpEt7nOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تماس تلفنی ترامپ و مقام صهیونیست درباره لبنان
🔹
رئیس‌جمهور آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی از تماس تلفنی با مقام‌های اسرائیلی درباره تحولات لبنان خبر داد و مدعی شد که از تل‌آویو خواسته است توافق آتش‌بس با حزب‌الله را بپذیرد.
🔹
رژیم صهیونیستی امروز نیز…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/443280" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7f57be1d.mp4?token=YokmVCFkLdIE7swSUp6XunpkGJHmhFgKGE45UwD2nJ7KeQw4fq_rFD5NYdusGvKjBuTbhmH14WDdVpuYmowrFk9E0fd9UbImXU7Fwq3TMp1svQOT4AACIpFDm41IrAbBPtqfll1d-g55WWsshT9ul1AJwl1GUVGyr48FGT_VLsTZ1aFtauydaBavxn3_3ywGaAHdTTJmUbvsyxTr0Uu6L_7QClInVh2F66BQRowzCPFJwFN5eDWXGtVmTzG-aRFWPMTrl2M6tlKt7nhTALTyw6Jp1QDQZYSvHCnSCZSZ2IVds83HxawA3AxjLpskdSpc0K4-R8meHXnaIopkrNXnpIPm-rP7P7TfmEgUKM3sLMAeNSpBuWQ3D-2hpOdYQ8onri4ZpBN0T5pwM5s7jsCvbRnaMqz0FsfBDvWSKoZpqYJvEY6ZLSU6TabcobEepC6L6RUtpL3CHz4oZ40kBsvAM93XoN9nRQRAPUTdMCh6PA3PrRk44RPBB3NxbEZLHxC599EHUoxP3n9h30rcSgVDMIeZmJ3bbtQ4hHI-dYkK7Xhg31z2mrbe3JFFinnF1c0xgzldNEiTIQjqn7ELheqgM5Q-I8jXeJY2Pb_54thSm3Bwr1AeDD-r5X4IG78T4PbXToAbF_Qc1XYFnR7QaHtQ7CN1_Kbld_QiJb2KfHplgek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7f57be1d.mp4?token=YokmVCFkLdIE7swSUp6XunpkGJHmhFgKGE45UwD2nJ7KeQw4fq_rFD5NYdusGvKjBuTbhmH14WDdVpuYmowrFk9E0fd9UbImXU7Fwq3TMp1svQOT4AACIpFDm41IrAbBPtqfll1d-g55WWsshT9ul1AJwl1GUVGyr48FGT_VLsTZ1aFtauydaBavxn3_3ywGaAHdTTJmUbvsyxTr0Uu6L_7QClInVh2F66BQRowzCPFJwFN5eDWXGtVmTzG-aRFWPMTrl2M6tlKt7nhTALTyw6Jp1QDQZYSvHCnSCZSZ2IVds83HxawA3AxjLpskdSpc0K4-R8meHXnaIopkrNXnpIPm-rP7P7TfmEgUKM3sLMAeNSpBuWQ3D-2hpOdYQ8onri4ZpBN0T5pwM5s7jsCvbRnaMqz0FsfBDvWSKoZpqYJvEY6ZLSU6TabcobEepC6L6RUtpL3CHz4oZ40kBsvAM93XoN9nRQRAPUTdMCh6PA3PrRk44RPBB3NxbEZLHxC599EHUoxP3n9h30rcSgVDMIeZmJ3bbtQ4hHI-dYkK7Xhg31z2mrbe3JFFinnF1c0xgzldNEiTIQjqn7ELheqgM5Q-I8jXeJY2Pb_54thSm3Bwr1AeDD-r5X4IG78T4PbXToAbF_Qc1XYFnR7QaHtQ7CN1_Kbld_QiJb2KfHplgek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در میادین همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443279" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI2L3QqAxIQNTXzofu77PxPuN7arn-P_qelkZC8tUGs2nSFWlqIFQFm2RfVNKhPc2uEOmx4dwiYOpVNU1bBr3gr3o_1CpGdCyRKHrIJWHxYGiE-gTgg5MUwveghirJddyO11m1fncxKhhnQneHs9FvPVF69-TEzzjDiyLWzyl48SOIICu-hAzvASvcjFM4-erT1wHLpgu8_4wsbVS7zCWvLka3E7N35CYoJsQWQ81qnBeLvEvBHBrKlalDFgvuKynCekEeD_7f8_d6IjNgVUp1uTnbUCJJjMMAF7ZBkzywGgWAIr_rQQrM2ynHVtWuStTsTxwafdhZXwKvDxyZp1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: غزه هم طوفان دارد، اگر به خواست سیاستمدارانتان حرکت کنید گرفتار طوفان می‌شوید
🔹
وقتی گفتیم حزب‌الله مرصاد دارد توجه نکردید گرفتار شدید؛ یکصد نفر تلفات را چه کسی جواب می‌دهد؟
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/443278" target="_blank">📅 21:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80924e16e5.mp4?token=R8OuaqKVIYxqeO8PAbtMIeTnbZB7sQzzqqO2SmvfYFKDyBUaTG0-CHWTOdZVp0C5A1VRpx5ha2EEiBUpC_nEvvWQjhF6KvEin7W1Y99yLLqTtKW8Kta8D4ZVR5S-_GGszk_rXRXbqOxfNzkRWwelzndposa7TKzmDqh9R9W19rLvVnLseQxb28vUUNeCKtCSk_enlbe66wBk0D3Qrb4-P4_57VVGu5K3tO7xYiDT_m7Fk8mEk2bzIzFFIWc2xLIOlmQYh7UhqnabuLXIQNRiq9zQ93fxRgu-8oIUE2j396QdQNnFhKMj39560U8U2hwUAQHBirAR2S7I1nVoDBriZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80924e16e5.mp4?token=R8OuaqKVIYxqeO8PAbtMIeTnbZB7sQzzqqO2SmvfYFKDyBUaTG0-CHWTOdZVp0C5A1VRpx5ha2EEiBUpC_nEvvWQjhF6KvEin7W1Y99yLLqTtKW8Kta8D4ZVR5S-_GGszk_rXRXbqOxfNzkRWwelzndposa7TKzmDqh9R9W19rLvVnLseQxb28vUUNeCKtCSk_enlbe66wBk0D3Qrb4-P4_57VVGu5K3tO7xYiDT_m7Fk8mEk2bzIzFFIWc2xLIOlmQYh7UhqnabuLXIQNRiq9zQ93fxRgu-8oIUE2j396QdQNnFhKMj39560U8U2hwUAQHBirAR2S7I1nVoDBriZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام یک تانک مرکاوا توسط پهپاد حزب‌الله
در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443277" target="_blank">📅 21:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584dd0151a.mp4?token=Q-fdk5A9XMvwu8E0Xmna8nrqUiIyjL-ZUHRgXjdC3xTkX1n02rqOzdjwbIJZDHyQYiY-KtNqaYB4oBG1WMi14Am_J6PGdnZNFJGHBvZIWFvJDmpuL8F5HiWh9GbNlBlg2-1NafcXGdZKBuL7zaVOKcg2dDCIHOt_6CWOiKLRBFZQadLcMW0gb5n-0PVPY2EvMKrfbHtJbGALNIbnbwA_17beTAA2X1pruex3bBtGjQO5BDb6oHnvRtWlhLUfAjFtl8-BVDyXhrug6K1NPtjAnQpxw2CLMLSa33Pbiicswq-bncvGe3rcJk9uR2zITvZ2Ri2uOuNpTEZuFvcuAZXRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584dd0151a.mp4?token=Q-fdk5A9XMvwu8E0Xmna8nrqUiIyjL-ZUHRgXjdC3xTkX1n02rqOzdjwbIJZDHyQYiY-KtNqaYB4oBG1WMi14Am_J6PGdnZNFJGHBvZIWFvJDmpuL8F5HiWh9GbNlBlg2-1NafcXGdZKBuL7zaVOKcg2dDCIHOt_6CWOiKLRBFZQadLcMW0gb5n-0PVPY2EvMKrfbHtJbGALNIbnbwA_17beTAA2X1pruex3bBtGjQO5BDb6oHnvRtWlhLUfAjFtl8-BVDyXhrug6K1NPtjAnQpxw2CLMLSa33Pbiicswq-bncvGe3rcJk9uR2zITvZ2Ri2uOuNpTEZuFvcuAZXRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این صدای تپش قلب کیه؟
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443276" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANn8ynGfQmSTnQyBx8H_F6xkpso4VAq1OxudbV67kA257oJepZs8pY0tB3YXCGzBa6Yop1H1VxFrfVIHBnT6lIGSQTTE3DylWSx06Ex5-FxovXZTenYY6s2uIvrAB0BZDNfkhsOlQtiYFYZKw4zM1jbvFW18TtGoGw0WFhyecLLT1Ich-f0FT61UVa8SC0LTvqCdvKivMDvlL46rYgFevwnufC68WbOoLYRWFmxGHvMMdZJPuUzQYTEYx8RMs6Ph22tZAY6bXqL6rSxEgbV_Nt2TNux5gZyaVaTDiTdcp3sOYKZRbGlz78sqwDw6Rcvd1pDe4fXi6YJNVUn9JmwWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نتانیاهو همچنان از حمله به لبنان سخن می‌گوید
🔹
نخست‌وزیر رژیم صهیونیستی در شبکه ایکس می‌گوید طبق دستورات او ارتش اسرائیل ۱۵۰ هدف در لبنان را بمباران کرده است.
🔸
این پیام در حالی منتشر شده که رسانه‌ها ساعتی پیش مدعی شدند که رژیم صهیونیستی آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443275" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063415f27.mp4?token=ij4JNWY9dDifGEn18kdJAYJBa4VVShShE4R4yB7QM4tgOZD-t3pZ3XB062XVxttSxqllPzgNKvBSivIpDPQz7c5ZHwuNHfglRUHDrCZsyEdkh_pze1nFZBPiDb-YKyQL7dtFn_k82xhlXOdveT1MJM-PsooxjGvcd45kv2x1I0FQuype9XRw8ZnWS4YRPKH5tgkUYr2Zqw_itHPhJdIzvvcyCHH8AHbwVg-a4_KfNknIwk0MknBHYYE9M3_RjIHFEeGE-dyy7K6MbaCLEwxgTg7-QrQ4VK2l9aBCSlk65qzIV9bU8lDlbByKhUC019y1HmQSgw_p9bgmVqW4VmSALYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063415f27.mp4?token=ij4JNWY9dDifGEn18kdJAYJBa4VVShShE4R4yB7QM4tgOZD-t3pZ3XB062XVxttSxqllPzgNKvBSivIpDPQz7c5ZHwuNHfglRUHDrCZsyEdkh_pze1nFZBPiDb-YKyQL7dtFn_k82xhlXOdveT1MJM-PsooxjGvcd45kv2x1I0FQuype9XRw8ZnWS4YRPKH5tgkUYr2Zqw_itHPhJdIzvvcyCHH8AHbwVg-a4_KfNknIwk0MknBHYYE9M3_RjIHFEeGE-dyy7K6MbaCLEwxgTg7-QrQ4VK2l9aBCSlk65qzIV9bU8lDlbByKhUC019y1HmQSgw_p9bgmVqW4VmSALYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظم بی‌نظیر و شورانگیز عزاداری یزدی‌ها در حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443274" target="_blank">📅 21:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/443269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب پنجم محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443269" target="_blank">📅 21:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443268" target="_blank">📅 21:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e161982.mp4?token=aC7g0BKkDMOQX2NmiKqpI7iXoOs1T8o86miy2IzyX2_WNoVO4wTxuVSTEqefPvVhFE1W3Tutm2RFsADEM5ntCaNyVzvkHRYFewYwnHo4jt1d14tUR1o1oArZIGFLiQKWQQr9TR697PAWBaC2Zl6-SShm4XI-h6pXkAqwEGzVxt3cL46GpHDvO-DS0akjL1UkBu3Q0lvT1l3L5t_AjnuCliQbOlGb9HKej-1My39_jxMvL1js1nTJgv1U7_0ql_RXCUrL9KqfVjCcN_OEx7Tm7a7O8IMNPYqWyJLz9ZRNz2OlhYIgfdjXolaUXuqa3UoQ22VxLlHB8nTz4f8lm7K7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e161982.mp4?token=aC7g0BKkDMOQX2NmiKqpI7iXoOs1T8o86miy2IzyX2_WNoVO4wTxuVSTEqefPvVhFE1W3Tutm2RFsADEM5ntCaNyVzvkHRYFewYwnHo4jt1d14tUR1o1oArZIGFLiQKWQQr9TR697PAWBaC2Zl6-SShm4XI-h6pXkAqwEGzVxt3cL46GpHDvO-DS0akjL1UkBu3Q0lvT1l3L5t_AjnuCliQbOlGb9HKej-1My39_jxMvL1js1nTJgv1U7_0ql_RXCUrL9KqfVjCcN_OEx7Tm7a7O8IMNPYqWyJLz9ZRNz2OlhYIgfdjXolaUXuqa3UoQ22VxLlHB8nTz4f8lm7K7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان راهداری: مالکان ناوگان حمل‌ونقل کالا و مسافر می‌توانند تا سقف ۲۰۰ میلیون تومان وام خرید لاستیک بگیرند
🔹
همچنین ناوگان فعال در حمل‌ونقل کالاهای اساسی روغن موتور رایگان می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443267" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
