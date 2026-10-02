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
<img src="https://cdn4.telesco.pe/file/mM_iCbSU3kev9xxpdCLSqktQrqH9MEaHz1s5fnTiewCoZ5v2ixrFWsS1bvaTI-_th3tQVtI12svRScHzpUyko1O2Jv36sgtZeS0-nWqOHVrkXQmug37LVc9DfHYBPoIWjFejhKVTu4nGpQbb8MY9Q8LtMyIrc8jAUZHGeosWqeOpDBGDS7EIK__qc7wKNGnCHos2vkYohaYshZ0ssJ6pxXD1-sTgqu-fjYYJGMU0jVQdghHq1aEpioRbw2CgqLJiaLhwE2tE1Pfh_4YSK_ttvw8nH_BPhkuUg-SkWUu3mjednWPmUpRaVp9L5n3GCA5ghGoHZfieeUrSpd04x9Kncw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 05:52:28</div>
<hr>

<div class="tg-post" id="msg-694708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KQde-m7QVmrBy1YAPTj2ZNKE6zVcmjhfZs6TYh_YsR55PgDKlvbvVCrtrfgDReT0bbcedZHwHL9o6-7uLUaAwqC1ZT6SSOu5HNXyQv7y4kHdEEnECCoVrtvPAbb4OAE8sheNEmLwFsn3sMPA6jDDKsydDAX3Alglm1I6qsalHM7-164m52EkRPMhvW59iMgYTpvqQTTaPwzGUzyosjKjiGmbobfnDmN9Z3xJqvc-wSFLJg6HB-GC-x5v1utTt90-hs2K372-s4v_oKqvFSe7sTM3j5xxDXJgdez6oppX3uAoaL0gLyjFJyWkyNvXRUjQZBtpZBepdPZu0HiqRJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧥
پافر کلاهدار زنانه و مردانه Zinox | دو رنگ خاص برای استایل پاییز و زمستون
🍂
❄️
سبک، گرم و ضدباد با پارچه مموری؛ مناسب برای روزهای سرد و بارونی
👌
🎨
رنگ‌بندی:
مشکی | سفید
📏
سایزبندی:
L | XL | 2XL
💰
خرید نقدی درب منزل:
۲,۱۸۰,۰۰۰ تومان
💳
خرید قسطی:
۴ قسط ۶۳۰,۰۰۰ تومانی
🔄
ضمانت تعویض ۳ روزه کالا
لینک خرید مشکی
https://memarket24.ir/product/fast/64809/180124/
لینک خرید سفید
https://memarket24.ir/product/fast/64808/180124/</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694708" target="_blank">📅 00:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694707">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac0ffdf15.mp4?token=v26gn1C2Vi1oTGq-dYVq8zmyVU_WATTMnvWaqUbmGTh25JXwUpJ2Xi2prpfp9uuLsuF1ip9TjZKLoJt3Jx1RYKHw4J5xpjys5TmvebgzeezoAa6kYnlCR-xjQYaen3FxF6GyHJtKejHtBuwov5DWpXcHw8nm6LhTa3yIF2xEw_JttcFp8bpb7yU6Rn513kxnIdEjsr40kSbxdZ_zbsujKXTh2Fu8I76yblzSzn57Duintd2EZ9YrMcPk88xPiOQcpIu8mTIZ2cvWPAr688Ka_FF-w94T26VQVsqUfkIwLY-xewhr2NRuHsItfNddsG5LaQ1C1ePeu7xf8Fx1dgkKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac0ffdf15.mp4?token=v26gn1C2Vi1oTGq-dYVq8zmyVU_WATTMnvWaqUbmGTh25JXwUpJ2Xi2prpfp9uuLsuF1ip9TjZKLoJt3Jx1RYKHw4J5xpjys5TmvebgzeezoAa6kYnlCR-xjQYaen3FxF6GyHJtKejHtBuwov5DWpXcHw8nm6LhTa3yIF2xEw_JttcFp8bpb7yU6Rn513kxnIdEjsr40kSbxdZ_zbsujKXTh2Fu8I76yblzSzn57Duintd2EZ9YrMcPk88xPiOQcpIu8mTIZ2cvWPAr688Ka_FF-w94T26VQVsqUfkIwLY-xewhr2NRuHsItfNddsG5LaQ1C1ePeu7xf8Fx1dgkKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ترفند کاربردی word که باید بلد باشی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/694707" target="_blank">📅 00:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694706">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سردار قاآنی: آمریکا با وجود همه امکاناتش از عراق اخراج شد و در برابر ایران شکست خفت‌باری خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/694706" target="_blank">📅 00:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694705">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd21e9719d.mp4?token=cHsHHZRxTP6BCwiV4ZAmCNeyru0LTYAMwRQPVbkZjSJq2gcaBL0PyPjgnfnYFEYIcIlfxDaY91JD4W32w7oRxgwAd9ta0CMhJ6esxpzS9zD6trA_zPrFd4V-yg7Xc_IUGoQVpRD4kwTwiCXIDTorucfMCX8XYyrtwyw-uPLWtAEy1rBk6Mi8RuT0sAOCz5PcD1VUaqOEaePfuSjTd2XtLVIX55npNXN13fAxwEiI4ED5CqpoIXy-YfMth5zMRu_dQVaJVx5PdmOqS_yE4AQ9UOGzvqFzqBICm-5OV-FE7FRoRcVlZwajvC-z-jzwlLMbaVf7kHnV-nyylpL7dwdziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd21e9719d.mp4?token=cHsHHZRxTP6BCwiV4ZAmCNeyru0LTYAMwRQPVbkZjSJq2gcaBL0PyPjgnfnYFEYIcIlfxDaY91JD4W32w7oRxgwAd9ta0CMhJ6esxpzS9zD6trA_zPrFd4V-yg7Xc_IUGoQVpRD4kwTwiCXIDTorucfMCX8XYyrtwyw-uPLWtAEy1rBk6Mi8RuT0sAOCz5PcD1VUaqOEaePfuSjTd2XtLVIX55npNXN13fAxwEiI4ED5CqpoIXy-YfMth5zMRu_dQVaJVx5PdmOqS_yE4AQ9UOGzvqFzqBICm-5OV-FE7FRoRcVlZwajvC-z-jzwlLMbaVf7kHnV-nyylpL7dwdziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رگبار شدید باران، دیشب در شهر رشت
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/694705" target="_blank">📅 00:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694704">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWyh0KrojDRSRhHXfTy5v3DUVlw1CnKzEmpJzr1934FLDGTlse1DJTslHtytydnta2s_Mq_HdBCJ_iJQnrDIP9CuHacj2OzLXzWz1u6TZ3JA1utBrC2lrwSHr5Vr3IchalEgud7imTcJwpucmoRFoqdbeb1733-3AxTRwPODmULIdXdn4ZY2auwHpOMe7MX4-OocgyEUaCln5de-VfgDKE9yBDvB-YWCOwA_8j0m2QBrKbWWdRTsp0T3Nt1so2-9_hpNeSy7iylRS6-Gtp1nvyVddyT0fElMGQXETK7pJUVWTvcTK3SPHLoRlA3CvtE1M7On4Nr8e8P6Ak1xhlTULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گیاهت چی داره بهت میگه‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/694704" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyppOTcSlQLbZawvnJVOgMlsRyuz892VaWC6Rrf2U8fxTNCi9TKBFM1g8x_RDrYCsnFcy_I5xaiRckWhkkohnxfSTRxbvLAP1bGkKFeUWmZcB_jR6K9Zq94RxoJeLW44qynXqVWwvs8C6czXKXPkD2QxpfBcwGvtYetfGK5pabboHMjPg9MRItNNfpts7qjtw5afQPe9jJUUun8FtooTfChyp5HEv9WaRxYEe37_qK-cz0HzQTLbQKfGGR21OZUY-TldfVcgQHneTK55bF_NqoYiv8Vo7bULUDiXRAWAIr1bcfthrgyD5LaXZ6vzgc37mIb6Y9OkYGdagh2l6FQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d9be492d.mp4?token=Y6NGrbL_i3Rp8thRfwzlHmf7z2EQxfxKQ3S4aPk85tJY6bnr2znLTunl-gnzhiWC2-QsH2mxO9EPb4_azYq_LwWiVJEddSXIf4gNurnmhUrkUB3STfn5zXcA1-4-WppHdHV6kLrAL8gWnrkjH00vUf0Da8RJP2EJNZT2FclEqq58n2Gf9ck8mGrb9leahxdBE-GpCOUoi3UHdE7MIucOIeAr9G8DkkLq8FPJYNJg5RyYfAKgbv4iBcYCPZvQPqxugHoeq0EvGRQs969YUDfj4Jz0hATzeOrOjAewCl7flkTMCsrNhHeTNljXzp74Yjljk5dNftrKFIR2U80gbpxlXrChZF5EqLlyQ0N34bqwuW7ijnX-_eqeNRHmMgY0wuMwLJnpZJTM-nuXyQ-RxrOxFxQcYbkNWNgj5DW6ToE0_ou8sbdpNqfnwuvwC56PLT3gQyeNfxx5noJlNNsVGnvyVj2REuXFrA01b8aro3PzKCXOW99xWPDmgdgxhh7Zx_bEhmc3M1UypKHBWyGF_sNJ-yid4dPSc9buATKD1jC6mjj46snuUbKhSwMLdwJdL_OVG60miG3eFEsShJ4WobWNSyoUXqhO4nYon8U9T2P0IZNiyqVjHsaAJQUjdUFVcbp0zIJu447gXHyeZ2b8ZwF23s8p5Ym72Mt4mmKQCrfW6OU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d9be492d.mp4?token=Y6NGrbL_i3Rp8thRfwzlHmf7z2EQxfxKQ3S4aPk85tJY6bnr2znLTunl-gnzhiWC2-QsH2mxO9EPb4_azYq_LwWiVJEddSXIf4gNurnmhUrkUB3STfn5zXcA1-4-WppHdHV6kLrAL8gWnrkjH00vUf0Da8RJP2EJNZT2FclEqq58n2Gf9ck8mGrb9leahxdBE-GpCOUoi3UHdE7MIucOIeAr9G8DkkLq8FPJYNJg5RyYfAKgbv4iBcYCPZvQPqxugHoeq0EvGRQs969YUDfj4Jz0hATzeOrOjAewCl7flkTMCsrNhHeTNljXzp74Yjljk5dNftrKFIR2U80gbpxlXrChZF5EqLlyQ0N34bqwuW7ijnX-_eqeNRHmMgY0wuMwLJnpZJTM-nuXyQ-RxrOxFxQcYbkNWNgj5DW6ToE0_ou8sbdpNqfnwuvwC56PLT3gQyeNfxx5noJlNNsVGnvyVj2REuXFrA01b8aro3PzKCXOW99xWPDmgdgxhh7Zx_bEhmc3M1UypKHBWyGF_sNJ-yid4dPSc9buATKD1jC6mjj46snuUbKhSwMLdwJdL_OVG60miG3eFEsShJ4WobWNSyoUXqhO4nYon8U9T2P0IZNiyqVjHsaAJQUjdUFVcbp0zIJu447gXHyeZ2b8ZwF23s8p5Ym72Mt4mmKQCrfW6OU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
دوربین ثبت وقایع مگنتی A9؛ مناسب خودرو و منزل
🔹
کیفیت تصویر 2 مگاپیکسل
🔹
دید در شب تا ۵ متر بدون نور قابل مشاهده
🔹
فیلمبرداری، عکسبرداری و ضبط صدا
🔹
اتصال به گوشی‌های اندروید، آیفون و iPad از طریق WiFi
🔹
نرم‌افزار موبایلی برای Android و iOS
🔹
زاویه دید ۱۵۰ درجه
💰
قیمت نقدی: ۱,۶۹۸,۰۰۰ تومان
💳
خرید قسطی در ۴ قسط، بدون چک، ضامن و سفته
هر قسط فقط ۴۸۰,۰۰۰ تومان
🚚
پرداخت درب منزل هم امکان‌پذیر است
؛ مبلغ هنگام تحویل کالا پرداخت می‌شود.
🔄
ضمانت تعویض ۳ روزه کالا
🛒
خرید از سایت با تضمین قیمت و کیفیت
https://memarket24.ir/product/fast/30028/180124/</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/694702" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: تهدید هسته‌ای ایران را در یک شب از بین بردم!  پست جدید ترامپ:
🔹
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694701" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw6SmbcS-s_E_1b190FHvNedprFUc27QOSnOvDPh6xuzaI90vg6DZ08sdZ29TWSDPNlEgMt3n8BFbRp1T4BwhLjA3dFlb54JdPLJR8PV-HnrwobOMhX4WVFtjqBT5BaW1lImOl9JqU0pa-L7qPWmISGBxnZk26FsrDIvtQSUdnYvnXmeg_yLDdqUn2P9k4n4hOkxaDBzLSxTkcqtvq_9VsxppqZ7oa-6IgOFC4NlAWt5Ni-7_ze3yIfJgg-cA26-09XuUyRKbT9lsQFSDTeyAr9Wgp_oKGa3fL4cXVQeqBXh3BRXHBVW-APifAp7CPF-EBSCt2AOxt0ApizSNJypbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/akhbarefori/694700" target="_blank">📅 00:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1003893947.mp4?token=VyJsFRJGGOBYnJ62Wf_YjlqIH3pVd3ut7Lsz6od4W_VJ1dDdaosH7ahqqPGdvnNIXcnjODbxC7kRArn4ZEYC8FBX6O93QQbHmIS3V_OeDzdp1kYeIfXSYkxoBWekjosC-iQs_K31Yg4qQCY71mGbA30BPiHfitt1GLnULQV8MGuOdtJK-NecwzULnUHcaWC5mA_qdg2uk-Ksmni90LB_E-UNgLr92aZBbKoStxNYU4Yw6AKqYt0g1Uet3HD3AndDNqoMU8WWeg8FLd3u-6VXWBQ7Ne_yIOqzldauc_1yyYVTvG5FsStAd9IDWUNU1kK60aaPlUxkV0kYJRbruHK8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1003893947.mp4?token=VyJsFRJGGOBYnJ62Wf_YjlqIH3pVd3ut7Lsz6od4W_VJ1dDdaosH7ahqqPGdvnNIXcnjODbxC7kRArn4ZEYC8FBX6O93QQbHmIS3V_OeDzdp1kYeIfXSYkxoBWekjosC-iQs_K31Yg4qQCY71mGbA30BPiHfitt1GLnULQV8MGuOdtJK-NecwzULnUHcaWC5mA_qdg2uk-Ksmni90LB_E-UNgLr92aZBbKoStxNYU4Yw6AKqYt0g1Uet3HD3AndDNqoMU8WWeg8FLd3u-6VXWBQ7Ne_yIOqzldauc_1yyYVTvG5FsStAd9IDWUNU1kK60aaPlUxkV0kYJRbruHK8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد جواد لاریجانی به مصاحبه‌های اخیر پزشکیان در آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/694699" target="_blank">📅 23:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3d734775.mp4?token=YaMPhFe3IfPDFYdEBYQ4ld1N1KnK1VrmW-WWD2z1iWjTyNLyHfnbZkcGDTniqvk6hP0vPldJIXcu-cr8t5rjxU5dsL2ukJdsSEglY-iYxU0er_97KAlNyUvD5QfFyN2AUEybytbX98vj6os-UVnvWp2oE0RYoOt9tr_XVJdt4VpWfgCyIS8AbS4wisIMzxy75sxEyn_sUISjMab7k7m3gsWmb1SK-oUgk_L1fPMaZ2Abf5O9HFo-evtQLVG8KVGvfV5Ex6I4-SO6f5ockbIYUPF2y43q-3CroOGnI5zjoB_aZ4f2OkPK2C1gJtuEbHj1W70HVS2R6nO0WjJJ9xZl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3d734775.mp4?token=YaMPhFe3IfPDFYdEBYQ4ld1N1KnK1VrmW-WWD2z1iWjTyNLyHfnbZkcGDTniqvk6hP0vPldJIXcu-cr8t5rjxU5dsL2ukJdsSEglY-iYxU0er_97KAlNyUvD5QfFyN2AUEybytbX98vj6os-UVnvWp2oE0RYoOt9tr_XVJdt4VpWfgCyIS8AbS4wisIMzxy75sxEyn_sUISjMab7k7m3gsWmb1SK-oUgk_L1fPMaZ2Abf5O9HFo-evtQLVG8KVGvfV5Ex6I4-SO6f5ockbIYUPF2y43q-3CroOGnI5zjoB_aZ4f2OkPK2C1gJtuEbHj1W70HVS2R6nO0WjJJ9xZl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن مرتضوی؛ مرد ویولن سفید میان شهرت، مهاجرت و حاشیه | او کی رفت و چه کرد و چرا بازگشت؟
🔹
کمتر خواننده‌ای در موسیقی پاپ ایرانی را می‌توان پیدا کرد که هویت هنری‌اش تا این اندازه با یک ساز گره خورده باشد. برای چند نسل از ایرانیان، نام بیژن مرتضوی پیش از آنکه…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694698" target="_blank">📅 23:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پرس‌تی‌وی به نقل از منابع آگاه: نتانیاهو در حال طراحی سناریوهای مضحک و جعلیِ «پرچم دروغین» مانند هواپیماربایی برای متهم کردن ایران است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/694696" target="_blank">📅 23:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrFOudZUs8DW9rkOum4Bj6j3Ly54Ot_dkSUNDw3LYicbWIQgs2A9pNwfDeEpKvNiIA32BJRek1jnboIE2MLnWaVkiXT5LbECujIE3iC2lrSlxXFbfR8u8ZiMulo17WamS6xaNMrz7Bop-GrhXiC-Wb3XQJf-cQ_dM1qZMXaGdN4LustP8vQwrF01RT6EccPiY5KEmzMkePtuQMvF7BxlgcSLf9ZcqpaqAzZCfUsM-po6xy2BqFQruKvbhkIWxCQAIOKrDgBRXT9Oz92cGSNuA4-9kfpS3SSfpDJTopZ5eYLehAdS1oUIDz-o1QqdKNAj3VzIQCsrN0dulQDrtao0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cv-d_t0TKqlR_P2WJvfhqc0NwgiKIkQWmYZMwL4i5M7USpbK9WdOcK8rDIOd7SRfoDKat2lV_U-HjVvPWx203tiV-iXPeKYeibJzCYJbwwZPziL816gps2GUb0Qc3Srtv2ukqueRvDAqG7OlIGkeTgBVoP9E6N0kI10LM1SpsNEDBT3cpiMGGF1AaZBSTZiFzSQ23RIlId8vGFGh5cvKBSPH2O6kh3ocoRetAX1e9230drjDxoTw4yxYIL_GB2fSEoZ5_cJIIvDgdpgTc4WN7gzCwSoM0dxVeIq1dYnxQJ27tFdi1U3-0UAkVlobhTFoY2XrEGRXVminW2YRalNmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TisKbd10BW_XxZMezPqfZvJMaqwNK2D-vOe1J-YcpGB_0_l2WQijZFBaA36D0d5Qr8NiyeRWI-P4OtkE7hffzEEp0MiVdMAdBUYfsss21RbdAVTGl9_HN1QCdE-QJ_w6-UIKT1bjgjGJ6nRX1yopOnZ8Ij2YLP4pFdNsHPn2GgAfz9vP-wYd1kX2fcOV4q3zke8vpHIzeda8guEzCGKrMED3IuRRh4UEf6aFmBTWDHPwI_1pQmR8cyfLFu3QcPG4WSIygEFxIKoj-ibr8oBJ1QYPwnnZDCrT0HnRcjFekDDpFzcv7gQipnAssD50nIIqcGi47zEbdaIXVSIBSTcGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ltis-1A3DnZ-eBs-HkabYItL4s2AR2wQ_QHWotxmTbsaaxNaoUQxi1j1icLe7R87VLDybhKl4k0bVxAfJw3oHRW0YrbIZO4Ddl66QTssj844S1_YhbfZZrDsQQ8-2HLgK0-8JcOoJm9vLwvEH5PzLQsDAd9nHZu9VvdLRw6HDd2XZ7I9T1WKlS4L2_XQK0PH40BNNwgVALKFeTtk1A46-S3KMUjLfYbYygiSrJRURyPidgB3WM9u8256JPu0CGqCbeIa6z2TKtaxW7rJlMI7kpIUO1zgVwJegmAEZ-LG0YWGiPbWW66--fHEpzAe8UqbMmYGPO8zUNBlPe7nWgwfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAQUsPn9RxKoGJz0QwLzhb2-DYMaicgd5E_OqZpE0lE8zULKDrDiX4NUk_nnlRkTmsMdh6tuBczzRP4Wco10j-oclRY-uBrLEKsSvsoNaWETzRaK0knTk_2ABaX2oK0CQQOTbhY4Nf7aKeND0rf0gZCDwnrt_CqbUmJ8snQLC17dwHxvwEJPE_dgX1Yl71xyT9vvWr9FIUv2t1zCYnjJqjX5Ey5iyB_dcssM8Hk-kzvXgqkdUsul3uSy75qTF7J6eiHEHrCLiNXGtwocR24HYX-1whxBdW58hUM7C4FnjOO_XVcIdxp6uvRE-pzx0y8DOys0SazeaxZp6FnvcE4hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pr7D1ai2tAqv8IOLkr3kfrDERBTSPNvzecEMtADYm7J0k78GTQwaNQm_o9IKfTQ3JK46qnso2DCbDEDMkPu84TmFXz0ksGm1LihrK5qKitAJw-2_x6i7QbpesTr82JhfrpSSyzsfAG5jxWZjRz5ix4wkxd9Pmpe_mC2TnT9c2Dr_Kp4jYo5p1A6P39SP3YyPwqU_ox1tn5gQGBYfDSlXvdFoGbfpgMix0QcdGxz5d7qGxEHNlVKpnQVsSFDh02V73Iaya2LI5hScCcOb-eSRzXG59IrciFv1mbibe1mAvQVt12951yRNytpt7u4iJu4_WfHcBCQ4pbPW93Xby3aIgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در ۱ دقیقه چند تا نکته کاربردی برای یادگیری اسم داروها یاد بگیر!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694690" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رئیس پلیس راهور فراجا: جرایم رانندگی مشمول دیرکرد به مدت یک هفته به مبلغ اولیه بازگشت/
ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/694689" target="_blank">📅 23:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رئیس جمهور: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد/ ما سه برابر انگلستان گاز مصرف می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/694688" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پرس‌تی‌وی به نقل از منابع آگاه: نتانیاهو در حال طراحی سناریوهای مضحک و جعلیِ «پرچم دروغین» مانند هواپیماربایی برای متهم کردن ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694687" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPVPAIig0GShSXrDkaJUebtUeKJzi1S_RfFI24q9qv-RyVkr-P_dUmo5y_X2fMvCxM6DuMyiRr5cKe5fFR-tBUAdABHFWMIc_kEygge-MHd2bHwDnLOGNwByTKM4XK_xX4-8cRMp4Ul1pwuaucd6TfnwxokuqBPggQX-c96lOnzAlg-yckYUOXB3EF2Fta4pizwhkKHD44xfPsTBloASCPEuuC4Hwfb_c4ZOnCq3OnQPC59uA172vhj909SHLiTpNAryisIEdFi7eisuGuDR1M8ebHu1x5Iz8VDw6vWYPxcQ6bLDOhw-eltzmCT9ZdhiErTFlyqxHDH7Gt8HQ0IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو در مورد حادثه هواپیمایی فلای‌دبی: این مثل فیلم‌های هالیوودی است، اما در سطح بسیار بالاتری. نمی‌توانید چنین اتفاقی را تصور کنید. نمی‌توانید باور کنید که چنین چیزی واقعاً در زندگی واقعی رخ می‌دهد، اما این اتفاق افتاد #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/694686" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f78ced2b93.mp4?token=J7Ge2zJ0SppkRg4VicPqlkl_q5xAVIuOnLz2HvM4agqKOpmSejwRIQ9mhRc4K3byAhGzxNNidd8pczu0lZ5B-Z8CjR3AaohOSOPZ67dnKGoxkJcOPVJyJuL9ChhXi64pI3qDmme0Rtmq72khHHJFkkPYZkfDeEEnLFY_yCUsSUacVkBFQm2EiEdN4DK8kAyTqePX8UlucraBEtBBxn04CcsdFG8OwwDrM0hiiCixcv7LwVbOnLfXWO--te3J4AZwnvfpiPcCnHqW40GcBRQ_a55vwjp4IzjW2oUAt_TbhZgeGAxHhYtrO2i_74URr0HIhgF6i6Tu3vR8W71QVV42Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f78ced2b93.mp4?token=J7Ge2zJ0SppkRg4VicPqlkl_q5xAVIuOnLz2HvM4agqKOpmSejwRIQ9mhRc4K3byAhGzxNNidd8pczu0lZ5B-Z8CjR3AaohOSOPZ67dnKGoxkJcOPVJyJuL9ChhXi64pI3qDmme0Rtmq72khHHJFkkPYZkfDeEEnLFY_yCUsSUacVkBFQm2EiEdN4DK8kAyTqePX8UlucraBEtBBxn04CcsdFG8OwwDrM0hiiCixcv7LwVbOnLfXWO--te3J4AZwnvfpiPcCnHqW40GcBRQ_a55vwjp4IzjW2oUAt_TbhZgeGAxHhYtrO2i_74URr0HIhgF6i6Tu3vR8W71QVV42Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد/ ما سه برابر انگلستان گاز مصرف می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/694685" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 3- میدان سوم، انابت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان سوم - انابت
🔹
انابت به معنای رویگردانی و بازگشت از همه‌چیز و همه‌کس و روی‌آوری به همه‌چیز و همه‌کس آفرین می‌باشد
🔹
در مقام و مرتبه‌ انابت، فرد هیچ‌چیز را از آن خود ندانسته و تنها در برابر الطافِ الهی سر تعظیم فرود خواهد آورد، شکرگزار خواهد بود و با تمام وجود به آفریننده‌ خود عشق میورزد
🔹
قانون توجه، قانونی بسیار تاثیرگذار و مهم در زندگی بشر است
انابت سه قسم می‌باشد:
🔹
انابت انبیأ: بیم و بشارت_آزادی و بندگی_استکانت با شرف پیغمبری و بار بلا کشیدن با دل‌ها شادی
🔹
انابت توحید: اقرار و اخلاص و بینایی وی را پذیرفتن_فرمان وی را گردن نهادن_نهی وی را حرمت داشتن
🔹
انابت عارفان: از معصيت دور بودن_از طاعت خجل بودن_در خلوت با حق انس داشتن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694684" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcseyrVp2ITT-tO6QVHhbLMTUrUkQp1oL8Qv9y3pQxFoLVv10AqmIMiPEQl_2pql-o1x5UeELN078P0bYIswQXy1ySoH3oWJK8c0ect9mn9raxw_GnxjCu2QbHEBYsW_A-cSsXjDOTcr6kCPlSL-Oz7a0qHFf-7Sv8r6LaixNmLkv8WYrD7ZM2_bbjlKAmE30wEyNCdLr88TKK0AXrcvzCo-j7C_RugLTh8MWGJ41Q20qCt1ZXkX91v4C8AXkTZvyPiA7bAjt-UOh5KWinK44VCBpSfn8MBw1-A9f0XWxtx_FMYqmoRCZcGoqj_cP0gGCIF8GaopC_kouaFdLFlwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹ عامل سرطان زا در خانه شما!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694683" target="_blank">📅 23:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSMw1xF9sNqDkfcTI5Iq_3eF5XCSgSiMDaW41erUOt7Q8GrvC-7DnNRbDPEaZtw5onj1k1zVlpl4YQ6w75MSYtLxOV0nIonwI2rM6JrkuLf8aYtplX7_CSrAxb-1gGE81XuMKvFqxtVR73ZdkvDZIGYFXAzMuOXDA8Pyvpkio-LupC-zG7352b6P4lyVmTfuoNj6DCY6Ew5qJnr8qHPVrR83qXy5xEbSC4ZMOqXNMe_q-bmdP0_ETx9h8oWax2V5dem2g2wW74riNIzDH91_lkTi3yIv_Pulvo809Gl0f69CJAZ0zzzhbhmrmLIqcG79hhZATfvS2qEQVMxU21q4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پولتان را پس نمی‌دهند؛ اما نمی‌دانید از کجا باید پیگیری کنید؟
موضوع را ساده برای آداد توضیح دهید تا مسیرهای حقوقی پیش‌رو را بهتر بشناسید و برای اقدام بعدی آماده شوید.
⚖️
آداد، هوش مصنوعی تخصصی حقوق ایران است؛ به شما کمک می‌کند پاسخ حقوقی بگیرید، مسیرهای پیگیری را بشناسید و اظهارنامه متناسب با موضوعتان را تنظیم و آنلاین ارسال کنید.
از سؤال حقوقی تا اقدام بعدی، همه‌چیز را یک‌جا در آداد پیش ببرید.
👇
رایگان شروع کنید:
https://go.adadai.ir/qhm3TX0</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694682" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40099ddb82.mp4?token=i5ytxKR79M1jAyKAxdaSciFalog-jpmA0eT3UfogNYV5CpM6RR99bT-SHFLewPuQZL9exZOd0UtFNHoA2ulaPvpq47Eh-55lC5Tvl9IoQ0yPMptkCctdiKy8e6w7-sNqmPOCJvacVzhjuF2cJeZgI04IiF8-Rb5VDmiVf5GMBIxzgzN8qYleABi4dy83W7JUKVhdhqrlnd28vewjarZOfRGpthona1mG2l7_7o-aHU8cZCZvWGBarIj6Zjwzt65oJE1fBqvRUMVEN_3hnbnm0HOAKzTdGJlPMwoLNeYKqAJwhNeIZYOKaUj4zHPwF3ZaVFXqyjv16Pxh8FlX_7I8iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40099ddb82.mp4?token=i5ytxKR79M1jAyKAxdaSciFalog-jpmA0eT3UfogNYV5CpM6RR99bT-SHFLewPuQZL9exZOd0UtFNHoA2ulaPvpq47Eh-55lC5Tvl9IoQ0yPMptkCctdiKy8e6w7-sNqmPOCJvacVzhjuF2cJeZgI04IiF8-Rb5VDmiVf5GMBIxzgzN8qYleABi4dy83W7JUKVhdhqrlnd28vewjarZOfRGpthona1mG2l7_7o-aHU8cZCZvWGBarIj6Zjwzt65oJE1fBqvRUMVEN_3hnbnm0HOAKzTdGJlPMwoLNeYKqAJwhNeIZYOKaUj4zHPwF3ZaVFXqyjv16Pxh8FlX_7I8iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این روزها اخبار طلا دوباره صدر رسانه‌هاست
🔹
از ماجرای خبرساز شمش‌های بابک زنجانی تا دلهره همیشگی مردم توی بازار سنتی و پلتفرم های آنلاین طلا.
🔹
اصل ماجرا چیه؟ تو این ویدئو ببینید.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/694681" target="_blank">📅 23:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=hj5nv3gMtTjzfBevUUUQ_6xqD9z3EhOCbetKB7XDXXxt8S3-bZYxq4ObG9jUIgGOVad8lrADfbh3axyznzxML4gaPrJBTyEWJ3O8zn9TW7xlJkhIOR7mcwo7VxZS4aSQA2A9AEZD4VEa1MWnTOvVaf6x9CeV4WELdKFw4_Km4DOfcaPPse6BFYdYcdOkyvQrqOyIpBB4IIvB7PJ4qU-nS3KGDMGsrrocebz5WuhY3BzORhbmY-Q9l_iVYdKjk3xG_PykqEgHxRAiH1plR0zFaM7Zs6vj_VJT61voYh51rTQ2g2Q-R5LgonTsAMT0cElQ5M3re4Mjpo1zJvbSjAEh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=hj5nv3gMtTjzfBevUUUQ_6xqD9z3EhOCbetKB7XDXXxt8S3-bZYxq4ObG9jUIgGOVad8lrADfbh3axyznzxML4gaPrJBTyEWJ3O8zn9TW7xlJkhIOR7mcwo7VxZS4aSQA2A9AEZD4VEa1MWnTOvVaf6x9CeV4WELdKFw4_Km4DOfcaPPse6BFYdYcdOkyvQrqOyIpBB4IIvB7PJ4qU-nS3KGDMGsrrocebz5WuhY3BzORhbmY-Q9l_iVYdKjk3xG_PykqEgHxRAiH1plR0zFaM7Zs6vj_VJT61voYh51rTQ2g2Q-R5LgonTsAMT0cElQ5M3re4Mjpo1zJvbSjAEh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا در شهر صور در جنوب لبنان: نگاه ما همان نگاه آقای شهید است؛ آمریکا از منطقه اخراج می‌شود و جوانان به‌زودی در بیت‌المقدس نماز می‌خوانند
🔹
آنچه امروز در جنوب لبنان می‌بینیم، روحیه پیروزی و مقاومت در میان مردم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694680" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff6deb449.mp4?token=pBhzeDWDvhQkVwvLbMqRlhnfESJ63Dw5G-JEbJvpMwUJiNUrlldu1jjnQCuNCxznRnc5qkfOVzV8WMkvSzK1g0KD0cW8as7DcYogPllMUcJos0DpetLWsH5liwIcG24PxhehF4jPz_ddJjt4krzEBxXhLwyYrT4kM8Mh1kGEivcVwTMrtr5yDVoqmMjUN-lFzdIEuAwUN25_0deZVTiqDrIiCbvzHjMecCzzpvbazj2YvGBs0-ev722Bl6zK9P8zvNnLCtp5hIoly5leF6rIoFWmNIJtu8y7mLRtjwII1wpFKPwW609XdYg1m9aztMSmdCNzQ0ijPhF9hAqcMatT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff6deb449.mp4?token=pBhzeDWDvhQkVwvLbMqRlhnfESJ63Dw5G-JEbJvpMwUJiNUrlldu1jjnQCuNCxznRnc5qkfOVzV8WMkvSzK1g0KD0cW8as7DcYogPllMUcJos0DpetLWsH5liwIcG24PxhehF4jPz_ddJjt4krzEBxXhLwyYrT4kM8Mh1kGEivcVwTMrtr5yDVoqmMjUN-lFzdIEuAwUN25_0deZVTiqDrIiCbvzHjMecCzzpvbazj2YvGBs0-ev722Bl6zK9P8zvNnLCtp5hIoly5leF6rIoFWmNIJtu8y7mLRtjwII1wpFKPwW609XdYg1m9aztMSmdCNzQ0ijPhF9hAqcMatT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: روسیه امیدوار است تنگه هرمز باز بماند و تحریم‌ها علیه ایران لغو شود  پوتین، رئیس‌جمهور روسیه:
🔹
حل‌وفصل بلندمدت مسئله فلسطین تنها با تشکیل یک کشور کامل و مستقل فلسطینی امکان‌پذیر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/694679" target="_blank">📅 22:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504076287c.mp4?token=mxqnqXw6_L7CNjwKNL7olp3ID8_YV3Q-0pZG_ABtKwmCu51FK6OzQyVUEH8UaDrseOAd3mzpi6jEfJyoW4JorKH-8d6suj7vgKIw16wGu6TavtWxSZ9Y9y5pSq2CjcjWrJuwxSabGiv2wfxAQfeuIcdp_Ru1GkgEUmbcb8D5olSJt5FkM-TML904coS75PBywxYf9-06dul-PElSpmvrrNZEZpou0PJqTj1CJQfVT3Xx3wtOUIhW-btW-mY8lon5tYeHnI_k8huJI7LPPWWzVOG_j9Dk_m_eycc6y8sL-ab2L1jggkGNIMXZPXwOQrGva3bpiskQ2GkWngTSvIN-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504076287c.mp4?token=mxqnqXw6_L7CNjwKNL7olp3ID8_YV3Q-0pZG_ABtKwmCu51FK6OzQyVUEH8UaDrseOAd3mzpi6jEfJyoW4JorKH-8d6suj7vgKIw16wGu6TavtWxSZ9Y9y5pSq2CjcjWrJuwxSabGiv2wfxAQfeuIcdp_Ru1GkgEUmbcb8D5olSJt5FkM-TML904coS75PBywxYf9-06dul-PElSpmvrrNZEZpou0PJqTj1CJQfVT3Xx3wtOUIhW-btW-mY8lon5tYeHnI_k8huJI7LPPWWzVOG_j9Dk_m_eycc6y8sL-ab2L1jggkGNIMXZPXwOQrGva3bpiskQ2GkWngTSvIN-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی تمرکزت بالاست، این تست رو انجام بده!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/694678" target="_blank">📅 22:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/694677" target="_blank">📅 22:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694676" target="_blank">📅 22:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سفیر اسبق ایران در عراق: آمریکا پس از اشغال عراق دنبال حاکمیت دلخواه، حضور نظامی دائمی، آمریکایی‌کردن ارتش و کنترل روابط خارجی برای رسیدن به ایران بود
🔹
ایران مانع توافق امنیتی آمریکا و عراق شد، مواد مخدر پس از خروج آمریکا از ۲۰۰ تن به ۱۰ هزار تن رسید.
🔹
هنوز پول نفت عراق دست آمریکا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/694675" target="_blank">📅 22:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd8265650.mp4?token=seFmsC7Dh82kI_YTtOX8DOnD8qHsWFlsHSeAPoQc6X70CgSgXLMvCbZ2HTTKWafexPC0XBWZr7_dh7lYu9yAYY0WMy8BtnwM4L_kxfUnV7wTn7tqZdd9Nv8BBNAAnyiXo7abXSN4CLIWLOFIv-2gV4ykm4go2pfhpZrIOpplhl1NLmYcBT2PReqqP8o4IbOUug-yQ9aSo68_qnov6bBcVC21UgA_vT7IxN8Ij6uZCwYx0atVVcxBdHel3XXYST14pVWw8hhKNr_R8TW_FvOV82TYQunif1aBTyOYKyTuCu5zKOcBJ01jPEnzo_Mb6AlyVSJuhfu6GnMPPx4r6Gbkcra2dmYwygQbpR7xhq3BJTI8rhMgHt469coMNFauF2i6nM34nVWLVnBwktR7iBNd_cqJEH1blZEECWy0_2UK70N87smUl4FC5ItFDCsJmfN30a0ikzIKhyFOVjrDr5viTpDEI5Qo7Tvly9UjBDVoZa1IruOYkXuBWRLOdXezbkkc02HkKIXZQ1zzVFWE0ApgNP7TN-a40uPajw-RnqPCjVDMAslDVWwjAogHW6gPUpD2-dQXKBiBpvmUCWy8XhWFaIs3Nm3nGUIODOq__TXpy0Ih7QDNTWjNMp-N0N5enkEhJ2w4ywU_J6hKNG5tV9YJ4HlkDfc4MjwXSVhc7HRbWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd8265650.mp4?token=seFmsC7Dh82kI_YTtOX8DOnD8qHsWFlsHSeAPoQc6X70CgSgXLMvCbZ2HTTKWafexPC0XBWZr7_dh7lYu9yAYY0WMy8BtnwM4L_kxfUnV7wTn7tqZdd9Nv8BBNAAnyiXo7abXSN4CLIWLOFIv-2gV4ykm4go2pfhpZrIOpplhl1NLmYcBT2PReqqP8o4IbOUug-yQ9aSo68_qnov6bBcVC21UgA_vT7IxN8Ij6uZCwYx0atVVcxBdHel3XXYST14pVWw8hhKNr_R8TW_FvOV82TYQunif1aBTyOYKyTuCu5zKOcBJ01jPEnzo_Mb6AlyVSJuhfu6GnMPPx4r6Gbkcra2dmYwygQbpR7xhq3BJTI8rhMgHt469coMNFauF2i6nM34nVWLVnBwktR7iBNd_cqJEH1blZEECWy0_2UK70N87smUl4FC5ItFDCsJmfN30a0ikzIKhyFOVjrDr5viTpDEI5Qo7Tvly9UjBDVoZa1IruOYkXuBWRLOdXezbkkc02HkKIXZQ1zzVFWE0ApgNP7TN-a40uPajw-RnqPCjVDMAslDVWwjAogHW6gPUpD2-dQXKBiBpvmUCWy8XhWFaIs3Nm3nGUIODOq__TXpy0Ih7QDNTWjNMp-N0N5enkEhJ2w4ywU_J6hKNG5tV9YJ4HlkDfc4MjwXSVhc7HRbWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در ارتفاعات علی‌الطاهر: خانواده‌های شهدا می‌گویند خود را مدیون انقلاب اسلامی و امام خمینی می‌دانند/ با وجود خانه‌های ویران‌شده، روحیه مردم و رزمندگان این منطقه همچنان بالاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/694674" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX3hhMji1k7qRjYvzaO36dOIFiT8Nmof0uyAmStQ93mfc9_WGdu629ycs-WVP-kECjMR1u6pykZV4qRw8YIy_WlZElSDS6U2c97pxMbFIl3S3J3_Fz9esuww0gMdUHAioq1CTj2NMQ-6brPcYifNR7gx5ri3VbB94YzsoAnTlaYt9XYqCL48F64lV_m65zq_HUL3F03PnB2fJbvZklBfSM_Tzt4NPmsuYyZpFmysnkNnEoObgH6qfBuzJoqBbYcQ8vM4np-vDBbUBdcZKXcYuUIOHr-8bp1B8hzAbpNFvddkdP8gw8icmhplze53aEKMljvcB3ddNQkWNddig9Cchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن سه نفتکش در تنگه هرمز در روز گذشته  سازمان عملیات تجارت دریایی انگلیس:
🔹
شمار نفتکش‌های هدف حمله در تنگه هرمز در روز ۲۹ سپتامبر به سه فروند رسیده است و هر سه نفتکش با پرتابه‌های ناشناس هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694673" target="_blank">📅 22:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/694672" target="_blank">📅 22:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
هم اکنون| عربستان اعلام کرد که خمیس مشیط و جازان هدف موشک‌های یمنی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/694671" target="_blank">📅 22:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج ماده غذایی که کمک بسیاری به مغز خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694670" target="_blank">📅 22:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694669" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/694668" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-hAMpsUkbiKqysMGTa2PWE12LlOBpW71-oev6KOXckfFaBfsJ7e_lTbrq-dn_giiEXBrYu7yrlBHFpwjx5tqRbCY84uuoz-i8Gi9tDacDuTeq__0QEIsisrB1pFP_GCePlg4F8mqCjkzwd4othspB6Px0lsOmpdG07sllLUsy2B-w0u40XSNyP3ggKgc_pPIiRxZ88UtEZMX1Uh6XUrGfJI1YVUc0aYu24e80jl3oyKujiWmo8N0XB2OpxQj0Il-jmiQKbWomwttr71M2PcauGpC2LT8JU7hqON-z0f-fYJO2Ywdxu6MGGVOPNFsHEN3ToGSes1hiX9ia-8-b6SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/694667" target="_blank">📅 22:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo72IsLZ4lwQbtLGi-voysbC4eTjemCT5jE_Spr8QGcoT4bq0mm4Z0vprXqvs0FPu66aqH88maSCXbSbvUlHq4F4TH7kqlpMQpRrZZZd1uxp6EV7a2vmaWoh2YyeqZhtYx_p7PoVvHzlTIMueaCcUa3K9bszveJuMEhxOmp6-4LlVSlUMsoOOyWqM9I1NOdKCog95BQK7RCjINDlm0v0WLAt2qpOv1EEtywlHWYjDNxvo5r2_8y-wyuf5kUmKMrLOot7wl6FKEhjtPPQN-ZFbwhNuZtcPhT-W3FN84ItWXrTjVT4sxUtEqdkgppYo2q1voSl0IacYjhNzITGmLXIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی یک باشگاه دیگر هم خرید؛
باشگاه الدنسه اسپانیا اعلام کرد که لیونل مسی، مالک جدید این باشگاه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/694666" target="_blank">📅 22:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtm0AgHYdkJti6FgN_PAGhM_TJUHytCdeeVaFxqa2Jr1He8WY7s0tlaQcKAro3hDkSoxVw2JkVOS9waDIFpq13xxrrj9_jmzDekXJrmy5iYsnsffYxxiySzAWqDBbhdQvjg3d4rqlstZgl9f6DK3eIXvbMAwDdwgiBmfBICFx_ALRx3JLzhnqd1yH5x4yi_qrw4WJc5dGyvmM5L08hCty6oyyJIFntNfgY7TLbb_b6-5Y0HpLVtvyEHLf-SYKcYXWR8TETWH_qLh9rOpGpfjnD8yZgxQUF0vrPcjOJ1ZXGevra0wdO1VgRtu_ITKjdic7zqW_yQO1rwVtDyQ2Huu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: جرد کوشنر در حالی مذاکره‌کننده کلیدی صلح خاورمیانه بود، شرکت سرمایه‌گذاری او بزرگ‌ترین سهم را در یکی از بزرگ‌ترین تولیدکنندگان تسلیحات اسرائیل داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/694665" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXaTCe10FGi5BGz1BkawHSsB0hWDWZqQkP4kmEm4WrvngTr5pOJypRuielZc1wlwCIn8y9j2E3kUSQMZIrmbPMBZ3LxXBRRnAT3xg23Zq_7HqQhUjjaeAx5zgSWooxz-6_lcPGKw8Udd0_DnTcWgZ2Kf03FPOezpCDvG0a4j268o3xDGs1R6En9k0OxdI80vS6oip8fHzlYmQO_8TgiCX_zkFbewny1JUTTm3eMorPRfdQN3KRWZWHzqqdbWJzYnECCZhape-qgJzQlwe_U-IaoxkyYk0p-N4KQvOT1Cf5tlaarPCID0_XbiW1tLqmpwLg8scfd7e1VqePWikDzk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDJD4GpFjHtMPkX798GD0N7FHAjWL-foEMa1Gamb4VWV21HVBaGekcTH2nR7S0A6or7xfJ_jLtKq1Mg3Zxg7mNSNGl7fg9aE02yKP9U2d3Bx3yNknkfCyO_nW3G3sGMRZuxA0FaZZ9GAXtxVk9Aq-rgn5RiJnWb4jMx1QsmpETe3V1diTBLAOxCfqnBtXzSEl8x_6qPOOhu2wob4cMwnq5aBpQ_uBrBAkMfqtIjY__EMEOZyLzQ_vK1sO431E9EFlqp7MDZYP-J0ZV2bChG8gc6CBrL3l3gDTmVCk3netKOd2t81OsGjU-j0P66FAgoNWAbAdKdE2nK32F3S7thQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند سبک برای طراحی پوستر با هوش مصنوعی
🎨
🔥
با اضافه‌کردن نام سبک‌های بصری به پرامپت، می‌توان ظاهر و حال‌وهوای پوستر را تغییر داد؛ از جمله: • Skeuomorphism: شبیه‌سازی ظاهر اشیای واقعی • Neumorphism: نرم، برجسته و سایه‌محور • Glassmorphism: شیشه‌ای و شفاف…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/694663" target="_blank">📅 22:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvT-Fmf0Qa5Vg1M6Z9Iy3yix7L-mkdPWEz9ywOoCuF4euKM97d4D9vwoAhiqupbCmjFgHLTVv1Stu8mF-0YlCxh7I3OgtMmWXpspudQe8Gh2TPw7tRCXaeVXydSvpZOwlXzDEEkCcfBqToElSIWnh2n2uEXxfa_oHUB1qn8njuffWjUINt2B9-dTJKtlNE33h3NZL_QnztkPAPyLP5j5E-aR4C_Wve9PPzJURzsInO4i2gjmvC9Sv9OA9N90r3GGXUX3yQ1D2hCWguXFFvboNFQOanIKUquN-2h7lY2i2TAchtXP3_GYJBNlyr7hI3bxr8z_Q9Txr1Q6dkszltCokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/694662" target="_blank">📅 22:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ترامپ اخیراً به دستیاران خود گفته انتظار دارد بمباران ایران در ماه نوامبر از سر گرفته شود
وال استریت ژورنال مدعی شد:
🔹
ترامپ در حال بررسی ازسرگیری حملات هوایی علیه ایران پس از انتخابات میان‌دوره‌ای است و اخیراً به دستیارانش گفته انتظار دارد بمباران ایران در ماه نوامبر از سر گرفته شود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/694661" target="_blank">📅 22:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694660">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290673400.mp4?token=VtKnn137WaAxrT5Ypb0HdYNIkDsCMTS26bPHi92fVzqqm2pLutrT1kECJQf8SM_Kd7f5l33-ECtDnRm_tjzCdr7yROTw3Zep--oomRApoV44VzpnKQbtgnUWFYQYVTDS0-bR3gyQLN9yz1tdgVDnH600UbqXEVbx4K6EeMbzgZ_9FPX4nMfIZfbQYxMpZ9TAKBRpZcgoWlFxGk0kSD1agExMXrjVPoHFFOH3FkwUObU8druDKQd9v3vdzizFL0STfyiKHmIaaLA9obfjB98UU0CQjnOPmKiQtFtEoes9G8rGwKjRy_UKKEPmLMU_MGdOoEPx1950-yVjDdSA7CgFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290673400.mp4?token=VtKnn137WaAxrT5Ypb0HdYNIkDsCMTS26bPHi92fVzqqm2pLutrT1kECJQf8SM_Kd7f5l33-ECtDnRm_tjzCdr7yROTw3Zep--oomRApoV44VzpnKQbtgnUWFYQYVTDS0-bR3gyQLN9yz1tdgVDnH600UbqXEVbx4K6EeMbzgZ_9FPX4nMfIZfbQYxMpZ9TAKBRpZcgoWlFxGk0kSD1agExMXrjVPoHFFOH3FkwUObU8druDKQd9v3vdzizFL0STfyiKHmIaaLA9obfjB98UU0CQjnOPmKiQtFtEoes9G8rGwKjRy_UKKEPmLMU_MGdOoEPx1950-yVjDdSA7CgFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با پیشرفت هوش‌‌مصنوعی، حضور و غیاب در مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694660" target="_blank">📅 21:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573d27db24.mp4?token=lHQ9CFtPgvV8Zlf5_piXLHa9-vcVTTuIjqeeE7xGuSyFR7TqLyJrExn2hbgUGWVEez-cKnc9Mi6tm4DA-Hjm6pC19RaCrwNRAjptDyHxDleggsf7KAqdxqU9stLygiJPmRjfLPQQkpuIiRrzMW5Njtf6qeb4vrdSM3pnpfV0wGhfMxFrw6FK4IeYqrUBq6d-HzpS8wL45j5R91hdy2Nx0vQj4JpyOLgeH3VE1vQOky8OLyDjnp45Ucbm9Sr7xpJ5UwmjFOeTCL7poCgCHQvRPcy8467MyQB9Ve06WL10wv9tNiPiHLg3AotRush00B8jxfCCxHrEh-gprJ0dZmaDFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573d27db24.mp4?token=lHQ9CFtPgvV8Zlf5_piXLHa9-vcVTTuIjqeeE7xGuSyFR7TqLyJrExn2hbgUGWVEez-cKnc9Mi6tm4DA-Hjm6pC19RaCrwNRAjptDyHxDleggsf7KAqdxqU9stLygiJPmRjfLPQQkpuIiRrzMW5Njtf6qeb4vrdSM3pnpfV0wGhfMxFrw6FK4IeYqrUBq6d-HzpS8wL45j5R91hdy2Nx0vQj4JpyOLgeH3VE1vQOky8OLyDjnp45Ucbm9Sr7xpJ5UwmjFOeTCL7poCgCHQvRPcy8467MyQB9Ve06WL10wv9tNiPiHLg3AotRush00B8jxfCCxHrEh-gprJ0dZmaDFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمرت درد می‌کنه؟ چند حرکت ساده‌ای که فشار روی عصب‌ها رو کم می‌کنه و کمک می‌کنه راحت‌تر راه بری  فقط روزی ۱۰ دقیقه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/694659" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694658">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_6sIUFxQfGYKMGw1c9ywuadDpPQ1lDuzyGuYZqc-TTuwWr-if4FEuJ5Kd9zZsux8y6QMaBuUC74z9jGvY2KacWMXyMRgpiuWKp7wOOAkVwHT9q3JI4Vv6PEvqKvYYC_4ZvkYW73i3Fx_rVmPQAx_ex29BNYqWMTAOffZfDWwOSFG963JC8twjVvRbK0v2LDXI9qkrBFvg_1_3byqy9_mah4y_kKR7mJWAcCST8fKBxr0UVRf7_X3TIh8P4fkOPuTPsDBqKEjqlUTnKZZCBVdguE4_TU5zgC8TVluHn6xPonWwi4cKAmtFGFV5WjPXsyj1Z9FtEsG6x9rmvzd6Ecvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نحوه دریافت فیزیکی طلا از طلاین
🔹
طلای خریداری‌شده در طلاین، علاوه بر نگهداری در حساب کاربری، امکان دریافت به‌صورت فیزیکی را نیز دارد.
🔹
برای دریافت فیزیکی، درخواست از طریق اپلیکیشن ثبت می‌شود و پس از آن هماهنگی‌های لازم با پشتیبانی طلاین انجام خواهد شد.
🔹
تحویل طلا در مراکز طلاین در ۱۸ استان و پس از احراز هویت و ارائه مدرک شناسایی انجام می‌شود.
🔹
جزئیات مراحل و مراکز تحویل را در اینفوگرافی ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694658" target="_blank">📅 21:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694657">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f9fe8f16.mp4?token=ZMD1SHa2UfWJQTSePWQCjhFdR7YRDUbnch31-VIdlgYeZtv3N_roeoOLPYtzl4BdF0Whvf5jcZ_gqmjoTxApkxqcWY2N1rzoltTjJ0ocwTcRrr1q7exxeiR1EV5q_Uh3Ohl0l1OJkyTLWteJaoF0j9rjECwl3Zvh1M5PGYNdn1Oj9xGjt4P_JlISWv6jFvYLewO5MHzTO5SqcB1QHcXnsA0iX-tTZwtDNeSpGS_KHIqSv6SDk6XVy5cuqL5Gor67pU27rmEq_4mpskA4TvAoT9NbWUGcWaPIxJIK-JkzpIHKzUpaRtZp1QbuCOV47jz82Xsqp-c8mlqSkwZ3FEJJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f9fe8f16.mp4?token=ZMD1SHa2UfWJQTSePWQCjhFdR7YRDUbnch31-VIdlgYeZtv3N_roeoOLPYtzl4BdF0Whvf5jcZ_gqmjoTxApkxqcWY2N1rzoltTjJ0ocwTcRrr1q7exxeiR1EV5q_Uh3Ohl0l1OJkyTLWteJaoF0j9rjECwl3Zvh1M5PGYNdn1Oj9xGjt4P_JlISWv6jFvYLewO5MHzTO5SqcB1QHcXnsA0iX-tTZwtDNeSpGS_KHIqSv6SDk6XVy5cuqL5Gor67pU27rmEq_4mpskA4TvAoT9NbWUGcWaPIxJIK-JkzpIHKzUpaRtZp1QbuCOV47jz82Xsqp-c8mlqSkwZ3FEJJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسر شریعتمداری خواننده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/694657" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OZnHcPhE0bd2e4-6UHhTvp_VnV1H6Zd6t9c-E1DJ1QFiHBudX8j2IcB66Vh1yi1iim6IHqREubPGxY1MNXCr3qoszoOwSz9N-kwVoo30oCE239q6J1iKKDluF8w28QcZfqW2DODBuJCNiEB_YL4_kGAbwP1iyM1fOwV_r2mFAftEw0ZYdd8jQ8RXUZhFuS8SgoCmK1HhlKejrOtnNMh-hVNzqcrOf-BV6QAB6jPTHl3dguXZM7ubSX4PnXXDUDcfOOHq4Hz2vWyLnU1L9kmiPY2DFQnOBiy4gMHRjfOeseH_sNMpOD-UDWY14EjNN15Uq2wg9YDbMAu7ZxdNg-Si2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: تهدید هسته‌ای ایران را در یک شب از بین بردم!
پست جدید ترامپ:
🔹
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/694656" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694655">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=rYdspV7qe12HotknqS8MAEJBqZiJKwcfCDDDEWnIKgEGsagR1UYoAr8Er8drBidIGLuf4Qn0oYT-bnfeYFhMXXqOD8ZXF0pMhAQYXNOAM2VpsqA8xy5QK-pYT-NdwkM3Njcs4rs8wsEFS9UonWmXKg1sLMdY2PIi8UaZaDTAKvp3BekthgGckDBuITU3pMMdhuPfSEHUe-pHSU9vM8pVrmgNCE-kMImt3tSSUQw24nW0f5_LypeHpR0p2ce5U1AIC0p7aqcoQ2SNNGjaeiqul_Zlu-bnS8gHeDe93k7xR05j0X8MhxYInzN7IgUU0rGvTZJCst_FCtgTINpaxGRaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=rYdspV7qe12HotknqS8MAEJBqZiJKwcfCDDDEWnIKgEGsagR1UYoAr8Er8drBidIGLuf4Qn0oYT-bnfeYFhMXXqOD8ZXF0pMhAQYXNOAM2VpsqA8xy5QK-pYT-NdwkM3Njcs4rs8wsEFS9UonWmXKg1sLMdY2PIi8UaZaDTAKvp3BekthgGckDBuITU3pMMdhuPfSEHUe-pHSU9vM8pVrmgNCE-kMImt3tSSUQw24nW0f5_LypeHpR0p2ce5U1AIC0p7aqcoQ2SNNGjaeiqul_Zlu-bnS8gHeDe93k7xR05j0X8MhxYInzN7IgUU0rGvTZJCst_FCtgTINpaxGRaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما خواستار محاکمه محسن نامجو و بیژن مرتضوی شد که به کشور برگشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/694655" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694654">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e05ef7c7fa.mp4?token=XoL2YtOG6r6dtbBbabDPFCQw-HZQO-Fdn7xHxWanY3-dsW_fPM_RqHUIBUZgbCVbA8KaCci7VLRKXlu30eEv6vuEILpYbu4r5cPraJgcnymx6SokDZ7hshTN-baVioHMfG8KywQWWTZX1BVUTc5aZBDTjz8IvYu7pxxZyMQrqpt3YARhdYBxcpaWR8C9qmNej55psG7HulBHJf5fC2ETKUQ9PBGJ0VN5im3Wdze3gC3f6PAQQZJ-u3R-m1HkudJjiqcatxSpMs1LsCt4b0qc2VSM6fvM7rQntFx1LIK2g-IiY_Qdru_8tkQxRmwRzcgYIsvKhsSt6WSm-TmTN3txfE9n1eC94UPQotljYc0RU9w1WqvJFv-WiWTsUQA4SFxUVstMXcKgoBUQQm-kBvm6yTuNpEbS53LRcl8h4UKXsywoIcWLfKZs69zrDskv888NqLv8e5ZbIz0hjd5zFXnS1vCMbBmdjSTgFbAI_WAWiaoPH7lkPYWo7hDK2TCx9UKaTCR0D8cKuC8x4qpQGStGHX0tB3yMMAH1lSDAZ4u_WtDP15qylaVCHY_4sXt1i-Nh8LQHBHk-Qw__kySFEcI_HcYiC735wCBfMRuloxI8-a2gc3RV2JhHBh6mM_Flb-ao_w2uqzt6HGyK8hASFGymiSsuhjih62DtlMqoCocKpdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e05ef7c7fa.mp4?token=XoL2YtOG6r6dtbBbabDPFCQw-HZQO-Fdn7xHxWanY3-dsW_fPM_RqHUIBUZgbCVbA8KaCci7VLRKXlu30eEv6vuEILpYbu4r5cPraJgcnymx6SokDZ7hshTN-baVioHMfG8KywQWWTZX1BVUTc5aZBDTjz8IvYu7pxxZyMQrqpt3YARhdYBxcpaWR8C9qmNej55psG7HulBHJf5fC2ETKUQ9PBGJ0VN5im3Wdze3gC3f6PAQQZJ-u3R-m1HkudJjiqcatxSpMs1LsCt4b0qc2VSM6fvM7rQntFx1LIK2g-IiY_Qdru_8tkQxRmwRzcgYIsvKhsSt6WSm-TmTN3txfE9n1eC94UPQotljYc0RU9w1WqvJFv-WiWTsUQA4SFxUVstMXcKgoBUQQm-kBvm6yTuNpEbS53LRcl8h4UKXsywoIcWLfKZs69zrDskv888NqLv8e5ZbIz0hjd5zFXnS1vCMbBmdjSTgFbAI_WAWiaoPH7lkPYWo7hDK2TCx9UKaTCR0D8cKuC8x4qpQGStGHX0tB3yMMAH1lSDAZ4u_WtDP15qylaVCHY_4sXt1i-Nh8LQHBHk-Qw__kySFEcI_HcYiC735wCBfMRuloxI8-a2gc3RV2JhHBh6mM_Flb-ao_w2uqzt6HGyK8hASFGymiSsuhjih62DtlMqoCocKpdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت Figure ربات‌های F.02 را در کوره‌ای با ۷۵ تن فولاد مذاب در فنلاند نابود کرد. آرنولد ستاره ترمیناتور، حمایت کرد و در ویدیو حاضر بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/694654" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694653">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c654b44b2b.mp4?token=OLp8DVr_EuEicbKFVchGbb9g30PcNOSQslcXTyBPoa_eow2KIcFoiNnU085JNTsyP__M3Gb1k_ILy_00US9wpM8HGbAFHmuxZEV7_ZUxJdgao0bB98QNVWDvXJCIKjkfABiWfEyZPZERArWP76t42kRM5s8M1zhO-Iccvstg0Hhm9K4YtVXH1Hj4ZlOfT_9ZZGe4dt5VW94Tt4wM3eghMXa6LuFtFK_RF4WXn1CkRrOuT7k-IJqpdT5zj22tCQZiv3vKsFQQinGKKQPtEATowRhatxHKSapvjdRbzhy5l_VM779FLLQDLbe9iOUwS7VSLNcQ_RYmBlBNSNHkH6LRTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c654b44b2b.mp4?token=OLp8DVr_EuEicbKFVchGbb9g30PcNOSQslcXTyBPoa_eow2KIcFoiNnU085JNTsyP__M3Gb1k_ILy_00US9wpM8HGbAFHmuxZEV7_ZUxJdgao0bB98QNVWDvXJCIKjkfABiWfEyZPZERArWP76t42kRM5s8M1zhO-Iccvstg0Hhm9K4YtVXH1Hj4ZlOfT_9ZZGe4dt5VW94Tt4wM3eghMXa6LuFtFK_RF4WXn1CkRrOuT7k-IJqpdT5zj22tCQZiv3vKsFQQinGKKQPtEATowRhatxHKSapvjdRbzhy5l_VM779FLLQDLbe9iOUwS7VSLNcQ_RYmBlBNSNHkH6LRTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه این ترفندهای کامپیوتر عالیه و حتماً خیلی زندگیتونو راحت می‌کنه، حتماً ببینین
💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/694653" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694652">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg2PTf5_cZKLaNWyJsds-TEPcvKSbalBRp8LIz5MwBHDzHQsDrS07metOxobBWIO0QEYe2QJmn3fZXnTG4S5n5CfdJY1ftlLqGmOh8PVGhwergEmZO-wClLGKZo51mBKjfR9hRwqJXGSbDrYyTPk6bsw6Hr9RZxkqCaZMceCO9iPHD1xLpQ42Er9q_2UqTIl_ia5nbxNlMtLHmcB19lbjSeDkt4tX2A7FtiSDOhHAMJOp_zZYbY_Nr1zHVK6mDbQV7pzRDfzpBVd4khAMOkMJFcMVaMUc7Pff0gI_DspD66X8x1airQug7fMYR23azPXV-vPCl3c7JvjHqEzMn4oTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
آغاز فروش ارز در ۶۰ شعبه منتخب بانک صادرات ایران از ۱۱ مهرماه
⚛
بر اساس دستورالعمل ابلاغی بانک مرکزی جمهوری اسلامی ایران، فروش ارز در چارچوب مدیریت بازار ارز در ۶۰ شعبه منتخب بانک صادرات ایران در سراسر کشور از روز شنبه یازدهم مهر ماه  آغاز می‌گردد.
💵
بر اساس این دستور العمل کلیه اشخاص بالای ۱۸ سال مجازند یک بار در سال تا سقف ۱۰،۰۰۰ دلار (ده هزار دلار) نسبت به خرید ارز اقدام نمایند.
⭕️
لازم به ذکر است بر اساس دستور العمل یادشده خرید ارز در قالب یادشده مانع از خرید ارز اشخاص در سایر سرفصل‌ها اعم از ارز مسافرتی، ارز نیازهای ضروری و... نمی‌گردد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#ارز
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/694652" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBsLA0jaD5axnjN1a1SuCF0hOFhbc9uP5D7cyDC0Op5YJcGb6oEDd_2srYEi1j33kxdRmp1b94Eeo14z8NL6tSz1tMUoFPX8w_Sc138I-PQfsG1QSYLgquO2vEkcdkLu4s7zMAhRvEV4a__b5VdSrcWntfSfwOiO_Jp4mAFtpcmK5t58Kq1sTDE6O6ox02Ul8NSRVjUtZsCzIP5XL7vQA5jn7SGqDHs-aJsD-z8T09JJA6zDFaXKgKUyujBltzVXs9rQCcKa_aV8n_ZYfqXZTi2mJBZJJ47xFdJOXOBReWPizYuGYSyHdj_pT8DlQs0a32frlAQuSjRXjwsfi3gIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پیشروی نیروهای یمنی در جنوب تعز
🔹
نیروهای مسلح یمن در جبهه‌های جنوبی تعز پیشروی کرده و نیروهای وابسته به عربستان از این مناطق گریخته‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/694651" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پوتین: کل جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/694650" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFjvgI8m3yfU_2ePTkSorqAN0HYT0ASerCRCP6ptbA_wIFRMer6owBhyvDk60b7ISGd8hRfXHJVX3EwCgPVOLlmusz79KQ0ZOKxQHg9-7PDFhWo-QojXAB9Ghc1u2xJ5Y123ZrqgXCXKAnEe_B0rurBZh1KD3kQ8-MXlIA-bzZz0Lb042zRoFpi1Xum2c0hjay_QJfymsRe0KqGqEh_J8ULKdjXa_aiYSs9GYGRvYvgpFg_rECa8l9o2z648zMNdzYf5_fsOaYjP47ZE2r0RL00plV4qmrmSDhZ-WYV7LcMfy_49WW5T6gMJxqUUWECpkE2GqLwwUaqh6_JUrUrzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های کمبود مواد معدنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/694649" target="_blank">📅 21:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=IUgVoS1cHEF8Em2Xkb_v2lgk4_dQRr442UhvnUTMVGRYtWg9qfJbTlbNZOpgNKeWn1LSiZ4bkvl-ZNGnM9dHzHvlh6Jndr7mM6_QTubriMl9PYO1JjhlpX7mMKMVn15fL23v7nJZInvtnpFjZLJjUouZE6_3DUoKXvix_BBQJyyJfTSP1yCZC7VTUOR3NtBvGPPHAXMC88nj7Y7Z8AZiNYbcCBJiGORKwIv3i7a_cEOEa_rps4dfzKkKh1w-Ijyhtr3URQr3fN9x4rrV86lmTvYhJBoyrJS-LZT3QhK0H7nCW00_saYZpFICGCU90wCXlgqbGqGj1913-vqKlCVhJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=IUgVoS1cHEF8Em2Xkb_v2lgk4_dQRr442UhvnUTMVGRYtWg9qfJbTlbNZOpgNKeWn1LSiZ4bkvl-ZNGnM9dHzHvlh6Jndr7mM6_QTubriMl9PYO1JjhlpX7mMKMVn15fL23v7nJZInvtnpFjZLJjUouZE6_3DUoKXvix_BBQJyyJfTSP1yCZC7VTUOR3NtBvGPPHAXMC88nj7Y7Z8AZiNYbcCBJiGORKwIv3i7a_cEOEa_rps4dfzKkKh1w-Ijyhtr3URQr3fN9x4rrV86lmTvYhJBoyrJS-LZT3QhK0H7nCW00_saYZpFICGCU90wCXlgqbGqGj1913-vqKlCVhJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلی برای اولین‌بار تصاویر بخشی از ذخایر طلای خود را منتشر کرد
🔹
صفحه رسمی پلتفرم میلی با انتشار این فیلم نوشت: این بخشی از طلای میلی است که از بانک کارگشایی تحویل گرفتیم و با دریافت آن، تسویه‌ها سرعت گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/694648" target="_blank">📅 21:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518f939343.mp4?token=qpjiYYQg9N_X-qngZi9k4-HunFCpjPl-TyG8axkIWF6x7UbUBgayO6pZqjrr-lBgbprcSkrcs0zmhGfzAkyb2sPPWPuaxMOPNvmwR5oRyksR5dKswu85ker5eEwPX8MlY_5f4A_a18knhJkfy0gWyBHOLxzFjXYVDzPUGvWB9HEATAJBmuVI5tGp12h8Y2_HVchXggMHxNlRdZ9sPTVS9BOQcDMstL4R0scaO11qMg2nuncdx9P-FhOJg4a7iIeEdRLzROhwp32HKGeJjG6Zb0UoOi0EwWImiQsBMEowAR64BZE-XB0R9mwpvKXkV4P1htc1x6vb57TcfuVlSQeeUAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518f939343.mp4?token=qpjiYYQg9N_X-qngZi9k4-HunFCpjPl-TyG8axkIWF6x7UbUBgayO6pZqjrr-lBgbprcSkrcs0zmhGfzAkyb2sPPWPuaxMOPNvmwR5oRyksR5dKswu85ker5eEwPX8MlY_5f4A_a18knhJkfy0gWyBHOLxzFjXYVDzPUGvWB9HEATAJBmuVI5tGp12h8Y2_HVchXggMHxNlRdZ9sPTVS9BOQcDMstL4R0scaO11qMg2nuncdx9P-FhOJg4a7iIeEdRLzROhwp32HKGeJjG6Zb0UoOi0EwWImiQsBMEowAR64BZE-XB0R9mwpvKXkV4P1htc1x6vb57TcfuVlSQeeUAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: کل جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/694647" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
خبرنگار: آیا رویداد مربوط به پایگاه نیروی هوایی سلطنتی بریتانیا در فیرفورد ارتباطی با ایران دارد؟
🔹
ادعای ترامپ: ممکن است داشته باشد، اما باید بگویم که از اینکه آن‌ها این موضوع را علنی کردند، تعجب کردم. من این کار را نمی‌کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/694646" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8yv3t0y6NCw3jZlNWupyvh_JKzg9bEcRIC6SYDubENnBcL0ah2wxOZ4jryDhw2TFzWeITOzotdbeRKkLVmYguRA-zoCkPSAdQBKS_uIk7eB0WV4nOCPV3gjMt9juOcLNbMItsEQaQVCKlTFIL1eOS2KejGcexD8W7FsjFe0be8emv5IC15wXs68nOTDw-uCjmkT7u3e84mOF-YSWj-srGqp1rSHrGXP7nAxDuExTkLkuSJ2K_Xe4cBrq7FrIPcOTAmLkIN3UanYRy5CpMxTaqQUHHxY1eZWBVsBwsOsdrf3t8BKanO3f4zHNwewEZPkac4CGrXoFb27f33QvmU4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ تورم مصرف‌کننده در شهریورماه ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/694645" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/694644" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbzkBflwwfiao4PnZuX5i3fHyjJ_K1zG4ubWdpGcHkknWGptH32Z-Pkee_IK1XI8hBdZKIfFcUZWdj_qDvBiMtGxn_BxqQnd5Z4Kguo0EHeNBUdVQUFnG1tBGYN9yA28RpROLr3BGVPUg9Bp5eaSiAWB6nkil8Ig1JBZZq3ixD5_MXJTESRCgFwVPtC2a8SRCIwI1YIrNLNuoSgNUjs_1kd3bNN9KdR74YyN5AyVDpFq4Y6MMjjYtp5JPoJzR8VFOEmsWe_56YeApuVq8nT3i7N84u5dCL-LaATXKRXpErtJ5ogKpsosXHagqscRs-m4XMYAT0fzrzjP2M0eH-efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ ترفند برای کم کردن کالری غذاها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/694643" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223c1228bc.mp4?token=kalAThkEG10LM7Ot6q001H99Sv0Un6kcaSaVQKLGRu3V4wkCTQ4-5jFdCr-jV-2J4uBqTfb_mWtN3O9OTZK0_542XLmmnQd5SXf6wDicKsT6fAwrOUPmL-ji27xW6hG9ac4ZdP4UsoJUxhajDvzZTr7KG6fBx6H6A1_gvrT6oL5fd73fRgtAx6aYrl9bRdWP5Ndc2VV2Pzb16d9YJPdw1AWYU0oelSJmuVyLRNEnyecOxEiAaR9oNp9T0F4wbD5AseSMW83KmsrCteg-w9XlcXbghDWtqGy9Uu-X64hS5Ju_9jvBmutMmjkbakmaevkaMDT4opC2FIX8N_DMnSoK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223c1228bc.mp4?token=kalAThkEG10LM7Ot6q001H99Sv0Un6kcaSaVQKLGRu3V4wkCTQ4-5jFdCr-jV-2J4uBqTfb_mWtN3O9OTZK0_542XLmmnQd5SXf6wDicKsT6fAwrOUPmL-ji27xW6hG9ac4ZdP4UsoJUxhajDvzZTr7KG6fBx6H6A1_gvrT6oL5fd73fRgtAx6aYrl9bRdWP5Ndc2VV2Pzb16d9YJPdw1AWYU0oelSJmuVyLRNEnyecOxEiAaR9oNp9T0F4wbD5AseSMW83KmsrCteg-w9XlcXbghDWtqGy9Uu-X64hS5Ju_9jvBmutMmjkbakmaevkaMDT4opC2FIX8N_DMnSoK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: آمریکا با ترور افراد باهوشی چون آقای لاریجانی، موجب سخت‌تر شدن موضع ایران نسبت به مذاکرات هسته‌ای شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/694642" target="_blank">📅 20:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694641">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ایران موافقت کرده که سلاح هسته‌ای نداشته باشد
🔹
موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/694641" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694640">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyN0czwS2AQM7alCa1OAPpZsfLaCNOx1fcc3lsrDWXtQj-jVgdfN16NxGLz16VbqWdGvP2-AEBBvgBIAKEAh0Ut7a-Xb0lH9IAaNBLS5IrSZjNEJhZN5wXFFitro79C2W-N_D1x66vrOISyAawt72cswHPqE3R1DRJW2BFlW59OZTVpw64rG2v_2j905mAJ2wzikWIXzntQwpEjUyQ0cIBilLkqKdiZY89orKVT16p59fPHvXVlMB9htoIxmIszapUr6eaXqID6cGlejogVYxbyaLcmZuq9xW4krbY8UWmD7DHL0aiaGtWTjcFYAuxWRJeM-DQlfiWq7I-KZR_JT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی رسمی از سامانه پیامکی هلدینگ رسانه‌ای خبرفوری
🔹
همزمان با یازدهمین سالگرد تاسیس هلدینگ خبرفوری، از "سامانه هوشمند پیامک خبری" به عنوان گامی نوین در مسیر اطلاع‌رسانی فراگیر رونمایی شد.
🔹
این خدمت راهبردی با هدف دسترسی بی‌وقفه مخاطبان به اخبار مهم…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/694640" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c71ebc28.mp4?token=eBFgjcFV05pe-EJFqOXXpBiX5k2uhkd3PlyDiJUPeJx4Tlbw1cufB0pF9xFnZG7-LkVlD8PORdfWDGSDjEqwT31Wr6vk-cmBNLxBAbn28vvV8L_Pvub_Fs1y4i_VPRWW7scZo4td9vfqoIDbgRaOQwI7522CxIbyfJseVnqjo2uQ5MUI427wZnb7lAZWiDwogxBNLrtKb-GW63Of4BA9hUxHmeonTnlf2N8yYFRVkwRavFquzL6r8DOk7S5BwLkNY_a3wsM04dabYfFu4cV2RoO1IcPITcnsYGLUhWzwlRh_yCaG4SzFEyqVx6addQtIt_W6606azcmd7KrUiBH2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c71ebc28.mp4?token=eBFgjcFV05pe-EJFqOXXpBiX5k2uhkd3PlyDiJUPeJx4Tlbw1cufB0pF9xFnZG7-LkVlD8PORdfWDGSDjEqwT31Wr6vk-cmBNLxBAbn28vvV8L_Pvub_Fs1y4i_VPRWW7scZo4td9vfqoIDbgRaOQwI7522CxIbyfJseVnqjo2uQ5MUI427wZnb7lAZWiDwogxBNLrtKb-GW63Of4BA9hUxHmeonTnlf2N8yYFRVkwRavFquzL6r8DOk7S5BwLkNY_a3wsM04dabYfFu4cV2RoO1IcPITcnsYGLUhWzwlRh_yCaG4SzFEyqVx6addQtIt_W6606azcmd7KrUiBH2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: پیشنهادهای روسیه مبنی بر انتقال اورانیوم غنی‌شده از ایران به روسیه همچنان معتبر هستند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/694639" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اعتراف ترامپ به کاهش ذخایر برخی مهمات زرادخانه پنتاگون   رئیس‌جمهور آمریکا:
🔹
ذخایر برخی انواع مهمات در زرادخانه‌های پنتاگون کاهش یافته است؛ واشنگتن تولید آنها را افزایش می‌دهد. ایالات متحده در حال ساخت چندین کارخانه برای تولید مهمات سامانه‌های «پاتریوت»…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/694638" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/694637" target="_blank">📅 20:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">21-1 Ane Manaee (1404-02-08)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/694636" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ویکم؛ بخش اول
حجت‌الاسلام امینی‌خواه
🔹
چله‌ آفاقی و انفسی کلیمیه، میعاد چهل‌ روزه خدا با موسیِ درون انسان و دعوت به میقات قرب الهی [02:30]
🔹
عبور از حس‌گرایی و دستور توبه سخت برای قوم بنی‌اسراییل در داستان فتنه سامری!  [12:57]
🔹
"أُشْرِبُوا فِي قُلُوبِهِمُ الْعِجْلَ"، مبیّن اصل حکمتی- عرفانی "اتحاد محب با محبوب" [21:05]
🔹
آثار توجهات مداوم به معشوق در مجاورت چهل روزه و تبدیل شدن به تجلی او [25:11]
🔹
تفاوت رهبانیت در اسلامِ "ذوالعین" با یهودیتِ ملک محور و مسیحیتِ ملکوت محور! [29:05]
🔹
فلسفه عزلت‌های مقدس در قرآن، عزلت‌هایی که نه انزوا، بلکه آمادگی برای هِبه‌های الهی‌اند [36:31]
🔹
تعلق به مادیات، همان مصداق گوساله‌پرستی‌ست در دنیای مدرن! [43:49]
🔹
اتصال معنوی حضرت معصومه سلام الله‌علیها و امام رضا علیه‌السلام و ثواب زیارت حضرت معصومه سلام‌الله‌علیها[46:31]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/694636" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad74d45df.mp4?token=sdw7l06ObgbpCohNT1Y8y6UPviVp2jWj8VMCTFLP0YLfhB96B0eDkPmrOjhbVkcgU0uxAW6uJm-4oymGjWhI-2o44iKbvAJ8jknreI54esOi6RA6Uc0ZSS3RKVTr_ZxywUleTa1BzXc6Arg9fLZfkvAAos6uXaqpYyNW7oIybvfNdkJepdsd0SL_Q-CMLW97wbkkB1p4jKjAf_Du-d_BAjPUv2bpZzg8J_rDkfJzlE8jjtTfS2H8qw48sBzn_qWfYLb-Wy-nkwqRR4kyO7Z9ii3Lx8rkp3z0IumCqY_Hku4hyYzzqPnHKzIYIo8LQgmNDe8UCSkaatPQ0G2e6xPjOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad74d45df.mp4?token=sdw7l06ObgbpCohNT1Y8y6UPviVp2jWj8VMCTFLP0YLfhB96B0eDkPmrOjhbVkcgU0uxAW6uJm-4oymGjWhI-2o44iKbvAJ8jknreI54esOi6RA6Uc0ZSS3RKVTr_ZxywUleTa1BzXc6Arg9fLZfkvAAos6uXaqpYyNW7oIybvfNdkJepdsd0SL_Q-CMLW97wbkkB1p4jKjAf_Du-d_BAjPUv2bpZzg8J_rDkfJzlE8jjtTfS2H8qw48sBzn_qWfYLb-Wy-nkwqRR4kyO7Z9ii3Lx8rkp3z0IumCqY_Hku4hyYzzqPnHKzIYIo8LQgmNDe8UCSkaatPQ0G2e6xPjOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: پیشنهادهای روسیه مبنی بر انتقال اورانیوم غنی‌شده از ایران به روسیه همچنان معتبر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/694635" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694633">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=OxHJjmMBf_QVJjCNJkPCuzFwqHd39hd8NnaCLMJtfiIU6zW-6Vi2klQNsIWtKgxZTmuhqPYM2QUoQu5DhgZ3un3ak5BYNcZFU9aueILqHe9xkgeY_sCTVJ0JnIgdD-zWqpSxHxn8j8Ml1A2n9oXR0coYBNm2WS1kshtzt49839NOF_ZS_OVvjlz678z-CM_tSx-jZnNPoQ4zE9AbixcL9AiyDVkp-T065mDKZaHAvM3alGtM7YCQTL72xZ8QDdebaghOcp0LYW0BlhOy-gKI7x_invV95DH-jyUAVEoixW2AvG5stY1bHIYJaaShHjsgdLnR5TOCwvyy7sfUTrSyqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=OxHJjmMBf_QVJjCNJkPCuzFwqHd39hd8NnaCLMJtfiIU6zW-6Vi2klQNsIWtKgxZTmuhqPYM2QUoQu5DhgZ3un3ak5BYNcZFU9aueILqHe9xkgeY_sCTVJ0JnIgdD-zWqpSxHxn8j8Ml1A2n9oXR0coYBNm2WS1kshtzt49839NOF_ZS_OVvjlz678z-CM_tSx-jZnNPoQ4zE9AbixcL9AiyDVkp-T065mDKZaHAvM3alGtM7YCQTL72xZ8QDdebaghOcp0LYW0BlhOy-gKI7x_invV95DH-jyUAVEoixW2AvG5stY1bHIYJaaShHjsgdLnR5TOCwvyy7sfUTrSyqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/694633" target="_blank">📅 20:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694632">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be03a96892.mp4?token=XP2MBkrhcCNmZ3oi4GwlLpsYUpItfAaaSUykkwiEOeuefzcgnG04qVJVpO0mb04G-UzPqupZ7Xgp8HwexJHiOwxaCtcadB6IgG79DR59AF05quIXAk_0mIFg3mujXzREAnK3w-03tvjJ1ybJj-AqEIGAuBbKbnmSuO1xk4XD3JKd7EkIE3e_mjAuwq4aLatu7AdUA5Atz0tVpC1SjtHabp5Vjx-G8ZmjzQkpFfXGS6j79jLnNRMf1unroN6jkbO6a3ApWI2oSxG60bqTDnNJofiymlN9jPgDvOmXOxAamCWIDW6VZN7PKWcxb8bFGabbsJqmAXRlv_UYKWavUw0zBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be03a96892.mp4?token=XP2MBkrhcCNmZ3oi4GwlLpsYUpItfAaaSUykkwiEOeuefzcgnG04qVJVpO0mb04G-UzPqupZ7Xgp8HwexJHiOwxaCtcadB6IgG79DR59AF05quIXAk_0mIFg3mujXzREAnK3w-03tvjJ1ybJj-AqEIGAuBbKbnmSuO1xk4XD3JKd7EkIE3e_mjAuwq4aLatu7AdUA5Atz0tVpC1SjtHabp5Vjx-G8ZmjzQkpFfXGS6j79jLnNRMf1unroN6jkbO6a3ApWI2oSxG60bqTDnNJofiymlN9jPgDvOmXOxAamCWIDW6VZN7PKWcxb8bFGabbsJqmAXRlv_UYKWavUw0zBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شمارش معکوس پایان جشنواره «چرم مَنطِـ»
𝟲𝟬% و %𝟳𝟬 تخفیف برای «تمامی محصولات»
➕
𝟭,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه
خرید حضوری و آنلاین با اسنپ‌پی
کد: 𝗣𝗔𝗬𝗖𝗪𝗚𝗭𝟱
👇
🌐
manteofficial.com
فقط تا جمعه شب
‼️</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694632" target="_blank">📅 20:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694631">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb078f63b2.mp4?token=b6g9IT94FHhjgfeGArrzPR1T1amRqnA2pNha20-scGhL4nCh_LKWzNG7yhQDSad8_BMRJF71k0tNarLtWptZh6zQDSA6nKJgwRyvU23ljb9K-Vga5VG6u1iNk4yk5HnBrWNRlGExJFjIERu2MRAKigqRZNOEJTVPq3TjD8QKZSQPjfNK9dOjF8NMgyikLnjKhsyyOYQR9JU_ISG9whsu79vOnFig_t3-Btv3Cb0XADmH_0CvzDXgd5dJqH7EtX5PCi2b2a1bJ3N6CBg-ckP8CJ_ogMMcK8NdHuQ_TdhkExYxX9KNmUuwegVZS_R50oDnskNi5MZl0PQZdxwARJY_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb078f63b2.mp4?token=b6g9IT94FHhjgfeGArrzPR1T1amRqnA2pNha20-scGhL4nCh_LKWzNG7yhQDSad8_BMRJF71k0tNarLtWptZh6zQDSA6nKJgwRyvU23ljb9K-Vga5VG6u1iNk4yk5HnBrWNRlGExJFjIERu2MRAKigqRZNOEJTVPq3TjD8QKZSQPjfNK9dOjF8NMgyikLnjKhsyyOYQR9JU_ISG9whsu79vOnFig_t3-Btv3Cb0XADmH_0CvzDXgd5dJqH7EtX5PCi2b2a1bJ3N6CBg-ckP8CJ_ogMMcK8NdHuQ_TdhkExYxX9KNmUuwegVZS_R50oDnskNi5MZl0PQZdxwARJY_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک رنگین‌کمانی ۳۶۰ درجه که در اطراف یک آبشار در چین ایجاد شده است
🌈
⛩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694631" target="_blank">📅 19:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694630">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون آموزش: حقوق پایین و تبعیض در پرداخت‌ها، موجب افزایش استعفای فرهنگیان شده است
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
علت افزایش استعفای فرهنگیان که در فضای مجازی مشاهده می‌شود، حقوق کم معلمان است و اکثریت قریب به اتفاق معلمان با وجود مشکلات معیشتی که دارند، رسالت معلمی خود را به‌خوبی انجام می‌دهند.
🔹
حقوق فرهنگیان واقعاً پایین است و تبعیض در پرداخت‌ها موجب نارضایتی شده و  بر اساس قانون رتبه‌بندی معلمان، هر معلم باید حداقل ۸۰ درصد حقوق هم‌تراز خود در دانشگاه را دریافت کند، اما این قانون متأسفانه اجرا نشده است.
🔹
از دولت خواسته‌ایم لایحه نظام عادلانه پرداخت حقوق و دستمزد را به مجلس ارائه دهد، اما تاکنون مقاومت کردند و پیشنهاد مشخص ما این است که صاحبان رتبه‌های یک تا چهار، ۸۰ درصد حقوق هم‌تراز دانشگاهی خود را دریافت کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694630" target="_blank">📅 19:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694629">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT_Gm5FiK7uqoCAT8cvYA_CnRMh06crGaD1bTctc2yEGOWMf3fTnLrz8ctvB0S9CkyA2IwriB1flXui10k2sD0PbB6PpPot8hBxz1GNfYAZwP2NBQNaeOv6kmuB4CrqgcyrISfsY7JAU6T7qsegyQTeQWz8vv2jEqHKr1lAtR0WfvBOd2eRiKBmrTJkYyHjS6zgfAaSnJ4i1HGuXLxAcqKey8xr3VAn0QYfg8RKM5pKPbFQW6G6tZqBliZGoeQe9iXk586fukSOhbiFIpy6IpesqKVBPLpNI9swHR2fKQu3QE-q7selBfzxuaEf-XQpSv-MwxyM0I_4Y_3ejUGpwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنگ روغن‌موتور خبر از حال و روز ماشینت می‌ده!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/694629" target="_blank">📅 19:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر_بورس(Reza Habibtamar)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1AmXmmMlnuv1pSyoutiG-30sujK6F-QJjKOsL_2TsS9B5WF9CAdcPJFqLPFOgkBlBu_T4JTAWr4yKQZK7ZdkbkWgMSFg2Cn60tnfKD7QSAjUNwUXSg3Fu8SWmzRPosMzF9xfF2E-xA1FekH63vNTp1Ao3mJOY23k3BSBjvXBUcdZ6-_PpbvqMVXMKuiLv3EVcd2KHz5Hse1S_agkJsOj10W7ZtcHE_J0cmsZifxp1Bf6mtnDThtU90ZGDwZo05C92XEBho4Y6czQeNbIo_p5k75LPC59lg8F0GFsDsSu8F2sSLE5M6RqHNQin3T_aSLsC0O27RkhnJLGTrO3tiF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRzEcgRRPn5deNz4c-kwP4GNp76wFR57rTidvCqLxVp6VO5aezxlYNcOibtONUAlJTlb_3wN6PiEUXWCFzrvZwI_2z8N7vbkHJY9LOH8pCYh46yUKxGClXPVPBZLBQ4GpbjjEt15qIgkwsyJlhqNJX5vOW7mITxrlSudyMgv3A-suCBmoBgIBz5lTPDJdjNeUnhdQUmTtEdrsh3367kCjYR0nn14exj6qxNQgKZyCqsG2irDIX84rw2KVkKDZ5yXrot0L7lndRSW-K_7ewwAJCNIMNaKmlQkuKKwJL9XAugs7NiRN-T09s1aGd3J8KTYuXSECzryxnZDyUhTeAxBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRoJXKzajWKCvU_MIT8CJhrEd7wJG8ai5qKyFRb_DK7yUip_O7nh27GzkzM6MgUOQdb13LNchNysUCcAYR1wF_valBuZy1DzF0ANUAD9wnh93rLGmPd1utC7-i_E5a9r9fY5VIp0hDDxX2_XgUvVbTpJW9OinHjwpvDD5dAIS7XBLRymi5UjTuBvCzeOIqC0Org1DSN6_FfR1QjwZ58QhcCt9dFqq_duKAnE536hIO5p90ZJjoCuzuWPfQjx5Kk7RkgHxHzAG2JcyVWBJhvfqI8oA4BbkPm-wQmU3jRWuqyzQOD6-dZYgiex6gfHbLzOL5VZp9EHspgsorqpdzDx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQL8_zRL3e-Of2yBoh4M34uzQA_IVB7Q6aD3-OI6lqEkl7Df8nyWDvI6k3vDlRcCEZMpytduB-L4oRB79f_PiYMq9rcT7yLH8bPe_oU-1RE4dnBDJj3kezh3IM9rPvPyt7WyDll1m_xiRonBUtEH9GcMy_iaTexgAliMTSjeyBX1zPjqtOcTSfSsdHvEK1WykvGVs46EyntcNSO9UB36CtR-HaCfII_tfQzacOlunh9O0G_cVjBnuOP89E2XuTIXqVjqqLonUZQwj0_keF3ZRPH8399JRsOZli50DxfGregwvx2a5cJVMZrcwKAnjFFTbv35QHCBnNIWRNOrqDJGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SS9BOdJTe8doITCjnXUvK1O_3S3E0YocTilb1RwCNmZJLER8RQm5WvJj35q2gCum5Ir7hV4hk0XP-bAD8CksyoNGiSiKSkMFzAJi8m6K3LUsa7OPLZ7NcbesIOQe2rmChwTMYjT11wXHcBh7MDIpR6F0Mg1tWVHi4WexvnwbKVRZm6Y9h_x4WdstvxsSeJR_1Cy-IGa0_gPcXn321uFD3aFdTIw7QYyoReF72XDVNwdsvtSpE2v-fImQwq-ohOLAjrmg1R0xqf5mCOSKCkxvGKdlRlM6OmA_z7gGnj15c9-CnkNJe1mbEdN6toooqVkG1F-u7u0AbapSsbNkdPMDFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
هر پلتفرم و ابزار جدیدی که وارد بازار می‌شه رو بررسی می‌کنم، دنبال دیتاهایی هستم که جای دیگه‌ای پیدا نمی‌شه یا اگر هست، خیلی کم بهش پرداخته شده.
🏹
امروز
کمان‌دار
رو کامل بررسی کردم. سه بخشش برام جذاب بود:
➕
رادار سهم
شرکت رو از چهار جهت بررسی می‌کنه و به هر کدوم از ۱ تا ۶ نمره می‌ده: رشد، سودآوری، سلامت مالی و جریان نقد. هر آیتم هم زیرمجموعه‌های فنی خودش رو داره. (خیلی گشتم ۶ از ۶ پیدا کنم، نبود.) علاوه بر این تا چهار سهم رو هم میشه با هم همزمان مقایسه کرد.
➕
پرتفوی صندوق‌ها
فقط وزن هر نماد در پرتفوی رو نشون نمی‌ده، سود و زیان اون نماد و درصدش رو هم میاره.
➕
شبکه اجتماعی
اکثر کانال‌های پربیننده‌ی بورسی یک‌جا جمع شدن و تو هر نماد می‌تونید علاوه بر نظرات افراد، دیدگاه‌ها و محتواها رو از چندین زاویه از نظر دیگران بخونید.
یه نکته‌ی‌ دیگه هم که به چشمم خورد: ارقام مالی فصلی در ایران تجمعی منتشر می‌شه و کمان‌دار تفکیکشون می‌کنه، چیزی که معمولاً دستی باید حسابش کنی.
کمان‌دار
رو از اینجا می‌تونین تست کنین:
https://kamandar.ir</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/694624" target="_blank">📅 19:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: کودکان غزه از طریق شیر مادر خود، نفرت را در خود جای می‌دهند
🔹
نفرت از یهودیان از نوزادی در غزه ریشه می‌گیرد، و اسرائیل را به عنوان داوود در جنگی علیه جالوت "فوندامنتالیسم اسلامی جهانی" معرفی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/694623" target="_blank">📅 19:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پوتین: رهبران شوروی در پی راضی نگه داشتن دنیا بودند؛ رهبران شوروی ساده‌لوح بودند و اعتماد زیادی به غرب داشتند که موجب فروپاشی اتحاد جماهیر شوروی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/694622" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYdu7bWIfZP3O4KVqDpeBkLsL8E6g_LdM48B4RB3-qvt31qnszaiYd2wCs1zQX8vMqXVS6Xx9T69HNIafFiEHrwpcSmHX_mqnPhr78Jlle2-z9335y2z8V74V0ler9L__gKpV8wv0m1TpneZe4fZcjYw0Jmngx18Qoe_za8v4agmNYvp5LD8V3JQ7VQT35Pk3jPONPqCdenonVUfBxrcRId2ooZgCCgUq4eIQod68fT_FIw-eYOBsVHoYdxif3DQWc8ajWKc_kHn3DNtYSbPpYrjUwWvuXKl5Rti70a5pg2WVtdb_HTWE_qjGMeHwQm5F-Cke-q5iotJ0T8kOSn6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین میزان مصرف بنزین در بخش‌های مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/694621" target="_blank">📅 19:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694620">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48ded5e2e.mp4?token=KhrhLqQ8Q5v4RO0xM0vbjR-TwqJEvtW52hhngG-CRAdNYVDFWT3NoYiqGP9Q8MdN0mrxMKnAwGXAulD-emhp6u16vngHLsyAS33fak2rF2TY4Nsoubt89RB7vQa0EIGb2lX9Cbnkf_y8pI03HFk5qOF5trkVHbAXfR0vV-gt9ryFBbU_rFzQ3Kmotquf5xUbTpoAJ6wbkOaaA9mMX6QaPWbv_deEqBpGHrukOFkmDEpjWv6hbhiA8m_befRWpVP66nHN3J3hCyjq0FJ5tubq6cHdj6FTullHfj3cmpyjNhY66ZTdsF53UTAFYnXkJdKc83CBp2ANuAxK9XDlJgg9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48ded5e2e.mp4?token=KhrhLqQ8Q5v4RO0xM0vbjR-TwqJEvtW52hhngG-CRAdNYVDFWT3NoYiqGP9Q8MdN0mrxMKnAwGXAulD-emhp6u16vngHLsyAS33fak2rF2TY4Nsoubt89RB7vQa0EIGb2lX9Cbnkf_y8pI03HFk5qOF5trkVHbAXfR0vV-gt9ryFBbU_rFzQ3Kmotquf5xUbTpoAJ6wbkOaaA9mMX6QaPWbv_deEqBpGHrukOFkmDEpjWv6hbhiA8m_befRWpVP66nHN3J3hCyjq0FJ5tubq6cHdj6FTullHfj3cmpyjNhY66ZTdsF53UTAFYnXkJdKc83CBp2ANuAxK9XDlJgg9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوندن عقد آریایی آرام جعفری و بابک انصاری، توسط مرجانه گلچین @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/694620" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694619">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قیمت نفت برنت با ۳.۷ درصد افزایش از ۱۰۱ دلار عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/694619" target="_blank">📅 19:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNz3ztAarYWdWCCQXT--7Xf9wJPHRC8fcO2NwpjRLpSVYzIcOf_wGIWTMHXAsiBKPbbL6M81cjrzhmyI5h2S77xPm3zzgq8PjMPjyubu0JBSRU9-ktr3Z7glPMNRAuCf-muHpo4ys_kcy3NWTLfLV5qfkzYiWlzYieP6xoUi5FN_-NWzwDWPZMnJA3yxAMeeo30c4PRTkLJl0KsOtRdQSkPqSYMf0GA5FoF1QHKONhquuxTwXiR8zbUc2SMcpA_Gaao4XIc83ktUVtdi98eJs21azGAR6c4Mc4krRXPAxo_sFAjp5lreuPAF5TA0g-BGB3DSwveHO7SLQKdINUnPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم ترین فیوزهای خودرو و کاربرد آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/694618" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694617">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS7HSLUSBVv8c3ows_HSp9tA0GPMd46xto_lTTab2heLr9Gy9MZwyEJTJTYmVWgAu5tEPEePWM2Vk9TMmzxO5lhTNHdDDkFZggne6mb50IFUt81TovJiA-ZwsBPBIvqOh7q8OsXvL3XptoNVvW0wLudn5poR22aZksiKQILwCbtxKuWiFwLhIHM8yX9UosH63gc5URO-9zHHIgEPEahdW23-XOdQSUC6nx6rGiAyXS7IgQEii_0LojmZS7Pj80ec35tJ1Vyc6YMMjAz3rzun7KciDMUCS4NQvud6p_WbDM1AfQ3jUntXj4__qFzAtWBORvPDxlL4hisN-I4n66WHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناریوی سوخته
🔹
نتانیاهو، ترامپ و غربی‌ها بار دیگر با تکرار یک الگوی نخ‌نما، فضاسازی رسانه‌ای و امنیتی علیه ایران را کلید زده‌اند، از ادعا درباره برنامه هسته‌ای تا نسبت دادن غیر مستقیم حوادثی مانند پرونده فلای‌دبی و حادثه فیرفورد به ایران. الگو اما آشناست اتهام‌زنی، ایجاد هراس، آماده‌سازی افکار عمومی و زمینه‌سازی برای تشدید فشار و اقدامات نظامی علیه ایران. سناریویی که بارها تکرار شده و حالا بیش از آنکه روایت یک واقعیت تازه باشد، به یک طراحی رسانه‌ای سوخته شبیه است. تلاش برای ساختن «تهدیدایران» در افکار عمومی و فراهم کردن زمینه سیاسی و رسانه‌ای برای اقدامات احتمالی‌نظامی ارزیابی می‌شود.
🔹
هشتصدوهفتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/694617" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694616">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6ee9dffe.mp4?token=j0cdB4ZUOnPUvLDpAC6WMIuILZYz_FYHMGdef7e4yc2DQTPE7_zGGkCL6v57Amp1u43DSIM0A0PrzwcfgZi2uVZ192dEdTn9qGBAxbw6zlZNAhQ3_z7orowkVU1bAm2p0fySV1g80apBHntEf_V5OCVM92qpAy3FbzBvLdke5OzIce8Ij013kcieqA_UhCZQmfJHarCe3fSS7arUKuae6F4WurrlVLgSEh2Fosz8XGlHRzHntsuEGvaWT9DN7uxw8t29KMr5MHUEant79ILmGm91yVeH5CECRmgMAB8pL2HdOh38Ljh0HUQf1PyUcdl_xIwkicU5BLhJwWVwUxAvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6ee9dffe.mp4?token=j0cdB4ZUOnPUvLDpAC6WMIuILZYz_FYHMGdef7e4yc2DQTPE7_zGGkCL6v57Amp1u43DSIM0A0PrzwcfgZi2uVZ192dEdTn9qGBAxbw6zlZNAhQ3_z7orowkVU1bAm2p0fySV1g80apBHntEf_V5OCVM92qpAy3FbzBvLdke5OzIce8Ij013kcieqA_UhCZQmfJHarCe3fSS7arUKuae6F4WurrlVLgSEh2Fosz8XGlHRzHntsuEGvaWT9DN7uxw8t29KMr5MHUEant79ILmGm91yVeH5CECRmgMAB8pL2HdOh38Ljh0HUQf1PyUcdl_xIwkicU5BLhJwWVwUxAvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌طوری از هر درختی نهال بگیرید
🌳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/694616" target="_blank">📅 18:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694615">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
یک منبع امنیتی اظهار نظر مبنی بر «ورود گروه‌های مسلح به کشور» را تکذیب کرد
🔹
در پی انتشار مطالبی در برخی رسانه‌ها و شبکه‌های اجتماعی مبنی بر «ورود گروه‌های مسلح آموزش دیده به کشور و استقرار در برخی محلات»، یک منبع امنیتی به تسنیم تاکید کرد: مطالب و ادعاهای مذکور، فاقد اعتبار بوده و صرفاً بیان دیدگاه‌های شخصی است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link
‌</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/694615" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
الجزیره: ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، پایگاه سن‌دیگو را به مقصد خاورمیانه ترک کردند
🔹
به این ترتیب تا پایان ماه نوامبر، ۳ ناو هواپیمابر و ۲ گروه عملیاتی آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/694614" target="_blank">📅 18:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvpoAar16nCp61STZVC82b4gSG4_9PgMEOBGTF9TG-nk9cBCF0Z5lfyyEzR3q3iRtyiLlQqvbc_NCv4EdEtJ17yFF8OtFHrwvlv8w8cgALLDEDDG9d2nAWSnUqlfhvdVm96Lg513kVZ6_EcJWqaumN5VDDgdTndkY5qbX6BEHI43b6Bh19WzO6Y51juXpLlry9FKkW4jEk3bBqHmXYn8NZgrM8hLi0oha2DuVZitq2qfa8f7RPTpQ8n_Zab9N8tDIrajrzlkgYeoznIffmy_EF6juNedIc_iqOuCVvcMYDah4cLc3jFp6XYlZ1tFwkXH5eNWIFmt6aRvsMSuxZVxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم و نشانه‌های کبد چرب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/694613" target="_blank">📅 18:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
معاون وزیر خارجه ایران در گفتگو با رسانه روس: جمهوری اسلامی ایران طرح خود برای حل بحران را از طریق میانجی‌گری قطر به آمریکا منتقل کرده و اکنون توپ در زمین واشنگتن قرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/694612" target="_blank">📅 18:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksKs87vGQpjoWFutekSBoAQgPkREltr7v6o2HGnGS07wP8VywkFS76FyfptjRssX9O1W8u_VbKOHoJ3OZm1hul1c3C1pV-vWVBzhpyvRieAD_3HNiQ-8UnE4y3-qYgKey0ux285GZKGlr7bF_O1HtZtNt4HADUF_m0lKypUtxYDkGxv02h1sp61om7xzqz5AhwTZAeXNWlG0t35Y8_gaM-9P8F50Qz5qo2xHuIkSyMgvxBlyt1GsDEBSpGwbWY2RUuIBd_va9t6eJTwR-dDpBL3kFtOUM409O7eb2MAbq4tNrZp-RBCk7niTQ5pGfu2-2R4y1eF-sbezpt4wa8Dfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا الان زمان مناسبی برای خرید دلار نیست
🔹
نرخ ارز حقیقی، قدرت خرید واقعی ارز است. که از تعدیل نرخ اسمی نسبت به «تفاوت تورم داخل و تورم خارج» به دست می‌آید. برای مقایسه، باید این عدد را نسبت به یک عدد ثابت در نظر گرفت، نرخ ارز حقیقی به قیمت‌های ثابت مهر ۱۴۰۵، در اکثر مواقع در محدوده‌ی ۱۵۰ تا ۲۰۰ هزار تومان در نوسان بوده است.
🔹
در زمان‌هایی مانند مهر ۱۳۹۷ و مهر ۱۳۹۹ که این نرخ به ترتیب به ارقام ۲۷۳ و ۲۷۴ هزار تومان رسیده بود، قیمت‌ها به سرعت پایین آمده و به همان محدوده‌ی یادشده بازگشته‌اند.
⚠️
با رسیدن نرخ ارز حقیقی به مرز ۲۶۰ هزار تومان، ارز دیگر دارایی ارزانی نیست. هرچند احتمال رشد آن همچنان وجود دارد، اما خطر ریزش، آن را به یک دارایی کاملاً پرریسک برای ورود تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/694611" target="_blank">📅 18:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll5wlXQMI4HWTSaMZYGQo6dUS_zleM-fwUJ4yG1OF-dZ0xUJE95lfdWfGPqSpx6aQC8gEKEMw-_pn-jXwqDUhqYKNrAqETbiD6MIfXNVLNl5SH9LTv9ANewwQLRmJef-0keu4ybkGjPaiioidOIPhgbd2vOaqTtLykER1ND4r7m0hyatNFnvj6f2Mw4Vgdwb7Q6_r4vB7SVJnl14YFCHDDHMOsRAYvkBLf6kusLlcdPUUVqsn2pfkY63npKKQSlktuUxJdIrxT3OTAO2TSGHdM4FTrf5zyWxc87h6ukV04hTrEDTz5Dz9-7anszJr4fx4CfKggECStC2hZrtfFblZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی؛ مرد ویولن سفید میان شهرت، مهاجرت و حاشیه | او کی رفت و چه کرد و چرا بازگشت؟
🔹
کمتر خواننده‌ای در موسیقی پاپ ایرانی را می‌توان پیدا کرد که هویت هنری‌اش تا این اندازه با یک ساز گره خورده باشد. برای چند نسل از ایرانیان، نام بیژن مرتضوی پیش از آنکه یادآور یک خواننده باشد، با تصویر ویولن و آرشه‌ای گره خورده که بخش مهمی از موسیقی پاپ ایرانی خارج از کشور را شکل داد. هنرمندی که از کودکی ویولن زد، در جوانی مهاجرت کرد، در آمریکا به شهرت رسید و بعدها به یکی از شناخته‌شده‌ترین نوازندگان ایرانی در جهان تبدیل شد.
گزارش خبرفوری درباره او را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249229</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/694610" target="_blank">📅 18:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اعزام نیروهای جدید آمریکایی به اطراف ایران
الجزیره به نقل از یک مقام آمریکایی:
🔹
بیش از ۲۰۰۰ تفنگدار دریایی با یک نیروی زمینی آبی-خاکی عازم خاورمیانه هستند.
🔹
تا پایان نوامبر، سه ناو هواپیمابر و دو گروه پیاده نظام در اطراف ایران مستقر خواهند شد.
🔹
با بسیج این همه نیرو در خاورمیانه، رهبران گزینه‌های زیادی برای مقابله با ایران خواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694609" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ارزهایی که در ایران از دلار جلو زدند!
🔹
در حالی که دلار این‌روزها محور بازار بوده اما ارزهایی هستند که بیشتر از دلار بازدهی داشته‌اند. در یک ماه گذشته یوآن چین با ۲۱.۵ درصد بیشترین بازدهی را ثبت کرد و دلار با ۲۰.۳ درصد در رتبه هفتم قرار گرفت.
🔹
در انتهای جدول هم دینار عراق با ۱۱.۳ درصد کمترین رشد را داشت. در بازه شش‌ماهه هم یوآن و روبل صدرنشین‌اند، دلار با ۴۶.۸ درصد هشتم است و لیر ترکیه و دینار عراق ضعیف‌ترین عملکرد را ثبت کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/694608" target="_blank">📅 18:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwHIAloGK9XbKsU7K1CuPfamyNpocBdzxEambfNQmutcRNzvCbUNlCRXiSiG8bFQBdfK8OcWD8bEvlrYmwSyFzieMbPccZ0fEi9qVaZibojy18rJfIUSlFNxcvX66afGmHTg3b8pQ1gNjQSVzd3nC12RYtUc1CboVBqbyQUyHyUR7KpKh9nvy1yISBfEMWI8uGEsku-nnnvCkDtrQMLujKgGb4SmBUZqIa6aLK0__Teqs44drYaa7DlvHfr8LK47b0M1Bv3eGbw3P-klv3FG-j2Jc-SMT_goVz0kF4fxQhnMeKSVBiUwWsCc44vAt6-AY1qc9M-8DyJ5d9zeHhkP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک ترند جالب در شبکه‌های اجتماعی؛ از ChatGPT بپرسید:
Based on your personal experience while talking to me, please name a movie/tv character who resembles me. Only give me a name.
🔹
سپس ChatGPT بر اساس گفت‌وگوهای قبلی، شخصیتی را که بیشترین شباهت را به شما دارد معرفی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/694607" target="_blank">📅 18:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3201b6bf83.mp4?token=Wt8ff6ZYTGzfBYjy8Oe8lw4oPCblGxSDopYa9C3056WH1lBQFM-YMNDtqKvBEClxwWfxGvdiRCquU4clHXoR46gsRGFcOp8WbX8gXb-EEZUBq3sv1cFWvymnI00knrrcBbryAWNlFD0PYEUr6Gw0w4XduNJyuO3fsOWxHJHzj2GTNUS6tOAjOYOUdicswctWpg3ZGmkJTq2FfHCgA4PMZ_4joiifM-qA1_wcX_mDdvN5oZM5hpI0SB9Rv8AI04jOi86bHpeZQ2Vf0WcPsq5zt265pMzc_wPdjSO2yKReOrf92MCMk6Y7RfdX9Eskyo7dQaNVEr99L5WyRpukv3XYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3201b6bf83.mp4?token=Wt8ff6ZYTGzfBYjy8Oe8lw4oPCblGxSDopYa9C3056WH1lBQFM-YMNDtqKvBEClxwWfxGvdiRCquU4clHXoR46gsRGFcOp8WbX8gXb-EEZUBq3sv1cFWvymnI00knrrcBbryAWNlFD0PYEUr6Gw0w4XduNJyuO3fsOWxHJHzj2GTNUS6tOAjOYOUdicswctWpg3ZGmkJTq2FfHCgA4PMZ_4joiifM-qA1_wcX_mDdvN5oZM5hpI0SB9Rv8AI04jOi86bHpeZQ2Vf0WcPsq5zt265pMzc_wPdjSO2yKReOrf92MCMk6Y7RfdX9Eskyo7dQaNVEr99L5WyRpukv3XYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اهدای هدایای متبرک حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به خانواده شهید حزب‌الله در روستایی نزدیک نقطه صفر درگیری
🔹
دیدار هیات ایرانی با خانواده این شهید حزب‌الله در روستایی در نزدیکی نقطه صفر درگیری با رژیم صهیونیستی انجام شد؛ جایی که خانواده‌های شهدا در خط مقدم مقاومت، همچنان در کنار رزمندگان حزب‌الله حضور دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/694606" target="_blank">📅 18:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d2aa4165.mp4?token=otgNh95FJxLVWApHSLlq5Vk-2v8E-bMsfWpxBaeIwUDuVjp4pkQZX5GyLvuMQzhNQEKiPfm-T_LNV3GagCs8W-TQ_djsbxjoBtEg5pJtAIelM8HJPAINk47M1yLdsuf_qi65U8r9dRxMn40F3JW-O3Ei8ogtvouCkpe_VIvvtix5GXmEPcFtv6Ncf0vKZTsw3gTfc1ljptbKDQPNxYA1kIoz5ThGRuLHbzJ3rW6fPo7vjUWJyD89W_-jyLunqP8kua65r8lm-hLdGe7aN_Msady8K0CHKXR7uwscZmhY7rIgKHpi0C5_8kmjnrhPG2rtxGDf1BUE-2EWNpFpOW0RVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d2aa4165.mp4?token=otgNh95FJxLVWApHSLlq5Vk-2v8E-bMsfWpxBaeIwUDuVjp4pkQZX5GyLvuMQzhNQEKiPfm-T_LNV3GagCs8W-TQ_djsbxjoBtEg5pJtAIelM8HJPAINk47M1yLdsuf_qi65U8r9dRxMn40F3JW-O3Ei8ogtvouCkpe_VIvvtix5GXmEPcFtv6Ncf0vKZTsw3gTfc1ljptbKDQPNxYA1kIoz5ThGRuLHbzJ3rW6fPo7vjUWJyD89W_-jyLunqP8kua65r8lm-hLdGe7aN_Msady8K0CHKXR7uwscZmhY7rIgKHpi0C5_8kmjnrhPG2rtxGDf1BUE-2EWNpFpOW0RVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلوار شیشه‌ای هم وارد بازار شد!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/694605" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فرانسوی‌ها هنوز در ایران می‌تازند!
🔹
با اینکه پژو و رنو سال‌هاست تولید مستقیم در ایران را متوقف کرده‌اند، اما برندهای فرانسوی هنوز ۱۸ درصد از تولید خودروهای سواری کشور را در اختیار دارند.
🔹
بر اساس آمار رسمی سال گذشته، ترکیب تولید خودرو در ایران به این شکل بوده که ۶۲ درصد خودروها برند ایرانی، ۲۰ درصد برندهای چینی و ۱۸ درصد برندهای فرانسوی بوده‌اند‌.
🔹
یعنی سهم فرانسوی‌ها فقط ۲ درصد کمتر از چینی‌هاست، آن هم بدون حضور مستقیم پژو و رنو در صنعت خودروی ایران./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/694604" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBW2Xd_p3Vk82Kn0GcmWAnEj_OhgkRvTg2GSfADxMP8lOCRqUf95vvb2l8nc3p5dhp8gyoHbETXqCVeVu0o83G5AK_jHpojTZtF3a3ADEB7N8f8jQNDIL4k1FWaLepeRLTeHJ9hx3uL53i7Rbvn7lHCk2FfmU0y45vMaT_BUC63w7v21cc8-Hh6hQ5P8CeMO198kfxRsY31okPQzeTFEvUqZC1vYkaU9ZyoynNm1aHdyJ4seK16oNJJ_WKy_1cJwXSJSlwxiknrCbyauVikk2oFyiyJtCFlW6Ehkb_eETRxEL8hHFAXN1aMQ0WS1b4GbioD6hH56dK2ao0ktkoaaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWZ_SikP8sgusaC29D1z-q3wUi1Ah8PXvSQz2IRMTy4wddT3kK05pqIl8nDf46A2NXSLw15AzJwgeYB9doOdg-9ugE01IK3zLVeTMQ-utT6uZcezNqVw75xAGVDdXrXA5Lfgr8bpKEjyZiqalq58bpea20cSUgfdf4B6tP9wMEiTvb42kai2qBjUjUlaylMtu8akt52m3NlQg6w2ItkYPLXfx2-CxcLH5lSAISxzIMb0H6EzCs3IaHpyRLj91Zwa31Cmj8R5irbe2U63Dl1PTKWUtnzlbu5FEiepMcu1QUBUWryr5jHcHnpilcJRe5TIXKbVUSlyQhGDZjwSwvwuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkF8--vLUhTBNIK5mwMDcE6TFJQjtcNw_hw_3eGS48EJGpejbS5aspucrJd-uT3ustQ25XNWyb4hGWmbwupV0JKCzL3Jj8qPAnUer4llvrw0NWGzpF8qei9yxLLf75ufpK2HEKGnyGpCENbQrvoXECRI7sPQGZV479j5TFq1G9t2QBtwSKi_3S9F_2rJwS4g8fuLmqRzCn1fZfG0gfakTeWXs2oV4sJQ4y0yRr1DGi7UyaKNYX2fXTo338yFg9yk59TUPBn4snEeAjMmUZ4YeLAzrujpS2QWBaMp0-710PVBkT5Haeu6t5YeZBbum3VWlH4Ua4wCTTUL6orc_2Gxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvYgFclc2aqGs5pCOfk2A1PihHuiO4roRpr5F1g_GCGiwOcVPB7cXOkTdg_0SOmty69QNL_aI06ys7nI34jMs8PdstSfIF64_1yFCNA-8htdVDKCbgCVzbLt3J1JpR2h00xt1LqFHAY_Iw58WTpCnewJJ6qMG-8pMlAXGAMyzYMwFO7V5EqJ2aDlu6chtJnFxyq3D7jxgEXIZZ6-t2hJfi94MxAA-EVNx8QGuUsJab4NNdqqDpbPGSat3lRT4LicAgTmwrdx7TOEL2YnEXxIWJ3DzJBY5j0Z5GjQRbS0K-pbPV1Ws-cwmvw0rQN7hhEr0sMLwl972IWMCpjgzCGkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMqU0tnctE4LBGl9lTAh26uep5dsJ2aLp7dkYQJHwyHdJGRLNx8wWLUw7yu2INIlTZFf2gyyPKuCNUKdtbM2Xj2oYS86JbQDTJbJs1eQZ2_KHoWOUY-JIcTzu587FgH1pbqVIMY4xIreBu3Z1Ei1dxb9VAQ2kYN-5g2m_e2QmlNiZXyV4VKmXvmkTAqwNRL031dUw_VXwjpIYafkVnPMQL35oVBjGKzwevNEfWrMjCUBA_B7gC08fxrP3meRIKyxJguDMv29VMHaQHIqdGLKBnMP8zp3mr--OM0WW_7JjN1n0AjIb8Ip0sFUphWvODOReBMkNhrH30n0bPCJQrLT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7kTAtIoKyNbQ0xjhXpAYEQHZrT8_yCC804gMnhJtAGvZSGyLrpYsmCLVCmxtI26j2EtjwHXjRqJU4IXYw6DVtuMFp6dYGjJ0TdjdydsSjo2dWwzs249VCUV5xFOHUgJlqIMqugqlaTCJPripbxA32-PcS4UofQmgBK0DQKdH_XI3Hg0-jSqDeATxz1_-gSbNWi5D8ifU8IUtMsEqZSFRHwEel9hvnsjlEJk0FMFRvgweC-erj2uGQ-2QOQACK2tnZJ-Xa9YTQGlrim8K3ycH5Q5nlgkOo1gLX4AaSMJKHWsqBenNVGDjX1_8hQqb7P788-aS0JlXfezpudlj4cgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر فراموش می‌کنید که هر کدام از حروف اضافه را کجا به‌کار ببرید، این راهنما برای شماست! #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/694598" target="_blank">📅 18:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=vbP5Gb6beZxiambdLs07lxbd-LQEgy-71_UtkSFCLBMlAiBJlvP9IzUJBMxxYUGY2U5yJxo_Xga6L5JEP44WEhqFRgflR3gaWNuBJFDxwZ_ynxESr8GunZMuxjDDXC6MFB1q24oSCcnP6R5Mu63zYsWh-wxVuMyeJ6jLwt84Bgr--Dwm_7ZRvSlvuoEEN94I7QyOPTkKabXQGPrUhUKhcojrDN1Eie2xXCAbJ9LwT7t8MsQq7VAgZsP8F1Po4XXfNaYip-oIZbAt4LnBXPMo0BBVng6w9c7ZOxW3GW_Sxw6YtGO7IOA4ZnxRGOdQH6wxRWMut6tM0xnxDtE3pUuwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=vbP5Gb6beZxiambdLs07lxbd-LQEgy-71_UtkSFCLBMlAiBJlvP9IzUJBMxxYUGY2U5yJxo_Xga6L5JEP44WEhqFRgflR3gaWNuBJFDxwZ_ynxESr8GunZMuxjDDXC6MFB1q24oSCcnP6R5Mu63zYsWh-wxVuMyeJ6jLwt84Bgr--Dwm_7ZRvSlvuoEEN94I7QyOPTkKabXQGPrUhUKhcojrDN1Eie2xXCAbJ9LwT7t8MsQq7VAgZsP8F1Po4XXfNaYip-oIZbAt4LnBXPMo0BBVng6w9c7ZOxW3GW_Sxw6YtGO7IOA4ZnxRGOdQH6wxRWMut6tM0xnxDtE3pUuwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2604
https://www.20landing.com/214/2604</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/694596" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990e9dda9.mp4?token=rbnR4AkieR7fsIHKMtjUdRoxvypBL66XfBSVU1wFk6_pxM-7YVzxdWGAeIZyhkFzcki66W7nS7SNw-KnFsl67oF5M7mAEx59mP70Phhwlgi3_zCawHPGXhNoAp6MgPYnbKiPxKZpg6yWAp8JvcWEVYwwks3iHhgF26Fab62wfpXZZg57XNb_RBVa1NhrftlhOqQf0uQVn6B8jwtyxkCcHDngU97S3Jw7v6beOXangT33Bkdw6A62wv-XXWFCTnNkkXLnO6b3iYzHbx0kAL6j0t35F2xNdplhZjuzh50KNFPYo5yDICTDMVXKRh7Z7r3FGDD4UrJZ9QTYNY-3BUATJrpqbAit4lUGl9w8gbrQyMrjfXam8KM_Q8eyvWv_x0D7kdVV3r0fJnK9la_e_W2mXpPqYl9-W6rDkX7MoM0lOura6SbRKBq2Ms8P8Nvspu0KqarhqDxy1hSUYUndOG6O2MnXGvVnGeLGSSGd2xDM50cEBU9YrgBFU3w1q2Uw3XXvS76g0qpm11DuQD2E7NdjaUwI1OTDc89ni7yz9AOAkGFPKoesG07N9WgoSB6gql0Ttmj4zw9e_ypyZLy7JD_gPnI9BpjuiiulWlxhyfIkaCn8at35bRMdppifdbGmGM9_peGyhj1pfzhrV7RPgPRShnRWSi0Fnx6GTDEk19MqGYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990e9dda9.mp4?token=rbnR4AkieR7fsIHKMtjUdRoxvypBL66XfBSVU1wFk6_pxM-7YVzxdWGAeIZyhkFzcki66W7nS7SNw-KnFsl67oF5M7mAEx59mP70Phhwlgi3_zCawHPGXhNoAp6MgPYnbKiPxKZpg6yWAp8JvcWEVYwwks3iHhgF26Fab62wfpXZZg57XNb_RBVa1NhrftlhOqQf0uQVn6B8jwtyxkCcHDngU97S3Jw7v6beOXangT33Bkdw6A62wv-XXWFCTnNkkXLnO6b3iYzHbx0kAL6j0t35F2xNdplhZjuzh50KNFPYo5yDICTDMVXKRh7Z7r3FGDD4UrJZ9QTYNY-3BUATJrpqbAit4lUGl9w8gbrQyMrjfXam8KM_Q8eyvWv_x0D7kdVV3r0fJnK9la_e_W2mXpPqYl9-W6rDkX7MoM0lOura6SbRKBq2Ms8P8Nvspu0KqarhqDxy1hSUYUndOG6O2MnXGvVnGeLGSSGd2xDM50cEBU9YrgBFU3w1q2Uw3XXvS76g0qpm11DuQD2E7NdjaUwI1OTDc89ni7yz9AOAkGFPKoesG07N9WgoSB6gql0Ttmj4zw9e_ypyZLy7JD_gPnI9BpjuiiulWlxhyfIkaCn8at35bRMdppifdbGmGM9_peGyhj1pfzhrV7RPgPRShnRWSi0Fnx6GTDEk19MqGYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای در تجمع مردم مبعوث در میدان شهدا تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/694595" target="_blank">📅 17:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شرکت ملی پخش فرآورده‌های نفتی: کارت اضطراری اختصاصی برای موتورسیکلت‌ها در جایگاه‌های سوخت تخصیص می‌یابد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/694594" target="_blank">📅 17:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کاربران ایرانی شبکه‌های اجتماعی خارجی را ترک نکرده‌اند
🔹
با وجود محدودیت‌ها و قطعی‌های طولانی، اینستاگرام هنوز ۴۲ میلیون و تلگرام ۳۳ میلیون کاربر فعال ایرانی دارد.
🔹
همزمان، پلتفرم‌های داخلی هم رشد کرده‌اند؛ روبیکا به ۴۲ میلیون، بله به ۴۱ میلیون و ایتا به ۳۴ میلیون کاربر فعال رسیده‌اند.
🔹
بنا بر گزارش دیتاک، همزمان با قطعی اینترنت کاربران روبیکا از ۲۸ میلیون به ۴۲ میلیون، ایتا از ۲۷ میلیون به ۳۴ میلیون و بله از ۱۱ میلیون به ۴۱ میلیون رسیده‌اند.
🔹
این داده می‌گوید که کاربران ایرانی شبکه‌های اجتماعی را عوض نکرده، اما سبدش را بزرگ‌تر کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/694593" target="_blank">📅 17:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b876bf4a18.mp4?token=u5ZDl5wYyhNsYm7Ik23WyHnKmLyNiZ1kcXCBFJ2MYxHZivCvBwpjK1A40e3M95BjXlL3Aq_h1e1lYAiH5Y9Tlr53DOosMFDPaK7uaMY7fBs1DiqeJO4EMLp4r-m6h3VZNfhO0sZbMWalbuBI8XziUZxPBClAoC_HOTNEvYVB5KIXsxTP8QbzH3Yze9PV_8r3GRUL7BSznVUfnMb3xTJzZEy9Ypl0EN6ACZk0GtuQipUAjpAGZraOFFt72LbpifFzwLGsRNGtICcTDnXHj_4DbzbD8xcQCCK55LZ-fBdZ_bsKoMEoM1TdTc2LJufYywAuR8_4n9wRs6CaXh9d56pMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b876bf4a18.mp4?token=u5ZDl5wYyhNsYm7Ik23WyHnKmLyNiZ1kcXCBFJ2MYxHZivCvBwpjK1A40e3M95BjXlL3Aq_h1e1lYAiH5Y9Tlr53DOosMFDPaK7uaMY7fBs1DiqeJO4EMLp4r-m6h3VZNfhO0sZbMWalbuBI8XziUZxPBClAoC_HOTNEvYVB5KIXsxTP8QbzH3Yze9PV_8r3GRUL7BSznVUfnMb3xTJzZEy9Ypl0EN6ACZk0GtuQipUAjpAGZraOFFt72LbpifFzwLGsRNGtICcTDnXHj_4DbzbD8xcQCCK55LZ-fBdZ_bsKoMEoM1TdTc2LJufYywAuR8_4n9wRs6CaXh9d56pMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجتماع بزرگ جانفدایان البرز
🔹
همین جمعه از ایران کوچک برمی‌خیزیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/694592" target="_blank">📅 17:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694590">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a880fc2bd5.mp4?token=hAvEto9C87WbIo-h1IjtsnF666W3Qd2aODMZ0zJqZrsZD7i0h0DOr-MSmqVRWEy3pO9rxpzcKZ368JjMG45zQrDnAmq0Hfj7d50KtbIuP_mZy3roy1-FEvckQwfTUn7xj5brX8Wc7E0d0vAUqyXkB07BIlcQCFD_3bwqhDNMuK2DPhWEYwRvlai_1RYbbJp63GDD6JmVNbBb2uYkHzNskzorFju_pUqMLeQi1_VG0Ap5ulosWW48UrOCD44uAjTKDALfK0Gryta9IM7FuwpGalOiILM1PdOsfONgYJHHUpVWZtpGKKBRKp8bePhYYYZurAen0wPnYJre0pb6ZUaLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a880fc2bd5.mp4?token=hAvEto9C87WbIo-h1IjtsnF666W3Qd2aODMZ0zJqZrsZD7i0h0DOr-MSmqVRWEy3pO9rxpzcKZ368JjMG45zQrDnAmq0Hfj7d50KtbIuP_mZy3roy1-FEvckQwfTUn7xj5brX8Wc7E0d0vAUqyXkB07BIlcQCFD_3bwqhDNMuK2DPhWEYwRvlai_1RYbbJp63GDD6JmVNbBb2uYkHzNskzorFju_pUqMLeQi1_VG0Ap5ulosWW48UrOCD44uAjTKDALfK0Gryta9IM7FuwpGalOiILM1PdOsfONgYJHHUpVWZtpGKKBRKp8bePhYYYZurAen0wPnYJre0pb6ZUaLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه‌ تشخیص کابل شارژر اصل از فیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/694590" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694589">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شرط جدید وزیر اقتصاد برای افزایش کالابرگ: نه خودرو داشته باشید نه ملک!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/694589" target="_blank">📅 17:35 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
