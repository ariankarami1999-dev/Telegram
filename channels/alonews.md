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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 15:44:21</div>
<hr>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16 · <a href="https://t.me/alonews/134726" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm4z7NTt7kQ03tQxqgnw_7wEKMmEhSKqbBkHsyhUybKghmnD_vu9JTVk_KmTPFuColomjZvk0VOkHYZYWGhOb2oANgp0ow_Y6f3h5eOUMrPbrIyuRHazEZsbapV-PHWFkqwFZk8-0b9r_D0OCv5hE2S5hSMBDA58aFObfj2RfQ0M-gGEdLVkMZsYkDv9pwds1yLtNBvYmkt3U0kwDfoKjp4nvdkC-HDn1u_UKaC4T2x_lyoKk68exvqNtx0Wr4L_FpXkKnBEbSGb5AMhNuW7-Qsc0ANPXUhQCrEij8B62MjOfFEDYWXx0A7fDtTauW9sXejNYAPy2pwlRtt33Ml8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریگوری برو: عرضه فراوان نفت در ایام منتهی شروع درگیری اخیر باعث شده قیمت نفت فعلا بالا نرود
🔴
قیمت فعلی نفت با وجود حملات زیر ۸۵ دلار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/134725" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
منابع عبری خبر از گفتگوی تلفنی بین وزیر دفاع آمریکا و وزیر امنیت اسرائیل در مورد جنگ با ایران میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/134724" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رویترز به نقل از منابع: حوثی‌ها اعلام کرده‌اند که در صورت هدف قرار گرفتن شبکه برق ایران، تنگه باب‌المندب را مسدود خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/134723" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کپلر: ۱۳ کشتی روز گذشته از تنگه هرمز عبور کردند و تنها یک مورد از مسیر عمانی استفاده کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/134722" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM916EH3FkwU1bHIbUvC31AvRnanVfuiTunRQVzCXAgvCmVVuTOhjUwa_jZreJMtHpfts9kmi-t_RyNzOjNTDF3Yh_SSkX4s-XLGmTz_nlCpxbnqhmtoLzm67wdIYA9mxNzH1Ba1zs22Bxj-DCIwVqfzQ0QZF-D4WW7o7BopQFD647yOVO-WFajpDlZ6WFXoIhVpi2WqKtjIDVFuxMfArBa1J9L_4E737_huF4jIfcvZi-RMaQ_XSbCijAcqrqJH1t413wP6TokdkSNKS-haZRI_TNyVQ6CUTJItkJyxwkNCWNyg94r6tE5slEXab7yluuii9MlkEhbeF8vj0g4JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/134721" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: در حالی که اسرائیل در حملات آمریکا به ایران شرکت نمی‌کند و به آتش‌بس در لبنان پایبند است، نوار غزه همچنان مهم‌ترین منطقه برای عملیات‌های ارتش اسرائیل است.
🔴
در غزه، ارتش اسرائیل دامنه عملیات خود را گسترش داده و در ماه‌های اخیر، حملات خود را با شدت بیشتری انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/134720" target="_blank">📅 15:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ثابتی و رسایی رو باید بست به سرجنگی موشک و زد به پایگاه ناوگان پنجم تو بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/134719" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_igszQqJR-US6nhPNImotEyklOemFV2XRx4WsZNyPUkWyo2ndT_1tJmStH7u_g7v9Y8b5xtE8b1nSAYExoAR5eE0WsvNxy8Lthsj847byuU8krPSmKmXLaVsBOt-3Hdvli2lnyIjpTlPJAt7ATN85TXxw_FyAPb6xsRWXukkW1uw_O1ChonV7ATsZMSzyDtTWfUsnFoj_a1CwXtg9q9zVscArnNdrGuVf_lK_Dfra2hBknwGlmG3BD1WWttg9lxol3sLdogynvR0B18hfbWM_73CsCDKjPV8JYO9nRSU6Ak6h5JDxrThMrf6wN2UpZi7VLyVh7U_2HvUrsHb58Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی منتقدان خودش رو ولگرد خوند و نوشت ۱۸ماه جبهه رفتم و الانم دوست دارم برم جنوب
🔴
بنده ادمین الونیوز جلوی 950هزار نفر اعلام میکنم، آقای رسایی ....... هستی اگه نری جنوب و زیر بمبارون ۱هفته زندگی نکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/134717" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F56Yy5vKRSntxztfhe8V9XZYg-dmNh1nQtopADEMEuH4wto2KE4GVcjteHxIWnJg-9ELWq7iJTXfubVySU-JgHxb9jKu7nfknG5pdG9ei4f6nRl25CmXYfGyptZxoQu-bGLub9SjVMqrZIu-vHP6LMQNdUSBQzpQyho3me-kX5-_aqZ1cErxZzMyO85H9yjt7P-Ls9xL4V7-poNZCp0tZQY7K7imbSyKRyMsC5mpkYoLLLlalpMQRj2dhtnl_7-BtD1XxdA9360lP8r851qUTIpqJE6Trn3KpN-56yZoObCbqjnFE3YjWFSuTqTo0ahyVfqY-fFsJj0WJRl_jDrXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
#بوتاکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134716" target="_blank">📅 15:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری اماراتی در آسمان جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/134715" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134713">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJBUT1JDmOHR0dQ-YXGtHBq9-aqb3ojQmV1nkyM1aK7nvgiOMAFLw9uVQosy51tzOJbALTUVlzZaJMrUMOYe206ZMQRKeyxLkKHgTFFIk7AZVbVU4hJf6VJk8pLTfXDe4nK8p0OiMTxa20XWboBQ7M8nl04fGAcofQ8B84M5528yJi1cr884qyu22BwOKNtHJscFEQssu8zxnaqDMMeUPMUWsj3nM8OXLhdNDpbicvZkJ8iw-PRM8avxC_XXCrfN2oLE8qIWqMEAAhYY6TCRsd_fvoF_P5_4GcRqNdrhSoPNA5gklyJn8UNnssAH5k8L04Uf2utUkoiTkt4wAARvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حملات جدید به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/134713" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134712">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم  #قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/134712" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFxI9UHkBTmpIaUOKKY3LLabv9zBorUwV7pX8nHC8dqNpUygFbBT0Yd3ctqTj6LBAV73LOou5vFIVEQ_iyAXcY78AfA1G39o6vH3MZIR6Ed3xV978j6XBVvzsk_3pdxqnO8ARP_Miy82LS_Ckyzct0rHodnOIMm7-TAwuaIeTffqHlUPrvexwfPz8VOFFmuWENBYS1wxpuZmLy-KbBHZHMN2WwR75a_Cn_UWgjxSZQcnCCg-KjzsfV3mwjC90ra86tIvUocXUW5E2Q_ATpHTbxrB8GlOBcdhCUOZQm_x_2_bRHwae7jt5KL1V49L-CKgc8uqg9H3wFT-2UesXIpbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZDh3d7yrz8NA6SCSYIm8CS4s-OFD1N9NJg25FHE_G_v5jOC_1TwZVDOUJk2ekZiRKHu2tAbAm53p7og1XCPYGiab5LVA27QxI1wkW6DXsyZwcBSkd5bZBhoBt1FaLtJEDByw6pjuO37yjF6w-iDLQOSuL2jBZ_vE3MqHZYdhdpJI0_1pHV1FMuB8l4maQc0PiQlAsrHt9cw-1ud6IRCIGLtLPd5wFfqHS92VBY-iERIumv6SuVEMT8TV2eQX6wvhgpvfbq6UMjq-SNK9zvUWEkBeAeZF_dneSC4wGSjpA4Qujk0cPDATt16wwaks5MsxZU_Geie_sid19g9nE71Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی کارخانه مینو در منطقه ۲۲ تهران!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134710" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ژیلا صادقی،مجری صدا و سیما: همه جای دنیا مشکل اقتصادی و قطعی برق هست،مردم بعضی کشورا تا روزی 6 ساعت برق ندارن، مردم ما ناشکرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134709" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بیت‌کوین امروز در محدوده ۶۴ هزار و ۲۸۵ دلار معامله شد و اتریوم نیز با رشد ۰.۶۸ درصدی به یک هزار و ۸۹۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134708" target="_blank">📅 14:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb22f7q9UP9f4G_shXzXwnoKHq1ewoAmGSfO8waJG-VLuA5A1MBBL9YWYxDuSUlxbd80DLWfS8psp1zH5Oy1VbabX1WKZ_N3t8NI1cUnAYZt0N_ISQhzMaR-7Q6KS-xJ-OR4O13f6uHZHhpenFqmKVLZCNmRVwxrH0TEp-S27G2ojdORQxepdAyvWZLaE_sbrx0UV1oDXlFza5gj96zJ3lp8NnjKLKc0vrzp92aGY6m-fEIKJXAJ5V2Q9CUBc2M-FKPyvFLzvHTWY1NZCrK4o6ragRkJDP9g_cKL-m6ePfMLjfXXmxKCzwPbTCSB-zphDr5HSNzBTf4lHQRJAfmqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم
#قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/134707" target="_blank">📅 14:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134706" target="_blank">📅 14:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqbuFWd0_nlF9L3tecbH05Hi84DggT3DyWVdfm_TsJ90tkoJKqG4knKRW0t7Z7kJd3neZxPnD6n4nWihteF-IY4cC-BWzcmCr1dXeKMse-x10vVioRxFQE8hg2VNSzfN2Ds18CudAzYkkIFJQzG7Y9KmezxUVQkDVofxMWhRF-sl6hZP1pqozsZdAr-je5lVsvHMcNj_PXYwEz9PM5LiLtqY6VmwsTb4ZC3VRJNMRA9-iuOTnJESFwKW6Wrnw4IaqqQd_olXJx4c8sqT_YDr9JPeg_eEvSr5hscalRDu19STdFiwtOPP9V7tvRrwkx6Cwv_Ljs34tQZ8ZyObf8ZtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هم اکنون حمله پهپادی به کویت
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134705" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که سفر فرمانده نیروی دریایی این کشور به بندر لاذقیه سوریه در روز دوشنبه گذشته به منظور تقویت همکاری نظامی میان دو کشور و تلاش برای بازسازی ساختار نیروهای مسلح سوریه انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134704" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134703">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
الجزیره: تردیدها درباره نقش پاکستان در میانجی‌گری میان ایران و آمریکا افزایش یافت
🔴
شبکه الجزیره در گزارشی به بررسی تشدید دوباره تنش‌ها میان ایران و آمریکا و آینده تلاش‌های دیپلماتیک برای مهار این بحران پرداخته و نوشته است که نقش پاکستان به‌عنوان میانجی میان دو کشور با چالش‌های جدی مواجه شده است.
🔴
بر اساس این گزارش، پاکستان که تنها چند هفته پیش توانسته بود زمینه تمدید آتش‌بس میان تهران و واشنگتن را فراهم کند، اکنون با فروپاشی تدریجی همان توافق روبه‌رو است. درگیری‌های اخیر نیز برای سومین بار آتش‌بسی را که در ۸ آوریل میان دو طرف برقرار شده بود، در معرض شکست قرار داده است.
🔴
الجزیره با اشاره به دیدگاه برخی کارشناسان می‌نویسد که پاکستان اگرچه توان ایجاد کانال‌های ارتباطی میان طرفین را دارد، اما از ابزارهای لازم برای تضمین اجرای توافق‌های حاصل از این میانجی‌گری برخوردار نیست.
🔴
در ادامه این گزارش تأکید شده است که سرنوشت بحران، بیش از آنکه به تلاش میانجی‌ها وابسته باشد، به تصمیم‌های ایران و آمریکا درباره تنگه هرمز گره خورده است؛ آبراهی راهبردی که همچنان در کانون یکی از حساس‌ترین و خطرناک‌ترین منازعات ژئوپلیتیکی سال ۲۰۲۶ قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134703" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134702">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoiG2hHi0yh30PrlFJ2aG1BK6M9tNl0NcUzA0kMXIO-csXHnOn0GDiAFM_HY36jkUy6Uo2b4ao27qVgIBuadSB92BhwOgBTKk3vY109s3rsfo1NvGEdJ9UY-DtwtlX6xmF1Xi8acXrckLB7vRpQWfyyAqtDD2uYlNMbYKxdm_6b_hx8lqRM5WKxtu73EH6y8dwf4INKB8rlGHpE7IfT_UK4i-wn1ZmtJCsvk7FfP0htyOX394jLlffoQJ2VfO6WiSCqxH9jUrk9nVtMM2vUbSJWDSw-iS3Fr0NKUMgofBAZFBjOi1LTU8fhEHRUi0ekLG5YClMPlwsMEedCavETEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار مرکز پژوهش‌های مجلس: نیمی از روستاها زیر خطر فقر می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134702" target="_blank">📅 14:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134701">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کاخ کرملین (روسیه): با ایران تو تماس هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134701" target="_blank">📅 14:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134700">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گزارش ها از اختلال در ایرانسل
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134700" target="_blank">📅 13:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHrYMRMsFsdXRKy1Wzw-OZ_PEv5Cy9b4cso46NHLXfcyK967VUVvZCZc5XKdXhMgGHnM0An_KJlPPBzuCVsWjGhG318JXUfQutirIvLYPENSwjqCyceJmBKQsatf5TpgWkQDZ8mBiNAlv8cVVM-SwEDrswwlVuiiSYS_VZ5CuHjGdVd37P3q6ATcUywcQjnaRsJtoslzUV8Z9KXR9ZT8Dr72oEk02AOfmJe_gogZdwkxQjGoOVqftC_xd5SaTcPYMqmRZVomjKc1YWq3kvMiIOTscV-WOGq5aZaicrWYePlfSvPNgQrMcXzgekh3T3nR7sL54sXLp0FOpPgiUf-AgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین دیوارنگاره میدان ولیعصر با اشاره به مرگ سناتور لیندسی گراهام: نفر بعدی کیه
🔴
حروف D و T در متن بزرگ نوشته شدند که اول اسم و فامیل دونالد ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134699" target="_blank">📅 13:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ6Rz-47Fenx6zinbKI5u3L0flnEDlvh5GV4edNaDqpxz5CM4tkWaize0Pn2DzC_55-icf7ThTaYvddWvnr2bMoRDbtt37Fl-oiU9ncGq89J7GHwWXAvs4V7MWKvzQ0VRb0PYILxHHkYt_sxLIB-o2w21qyBM_yEMHnWGsXSVUs699vRUGiu6703eUyc5jtQep0q0-47HBPUYve5qzQragCj195U1hoPj4L4CVvHC1M6WAE3Y0ihraCsDG-EtpET3Uie6zVQ4SoIAE1Dyk3DJiTO3rQTbGKHe001GwXp-2ndAX4eUnrevAgbkuxWZd3hkJ0UqsB5xmiMVELS4nkJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از احوالات روس ها در جنگ با اوکراین، نقشی سوخویی که برای فریب کشیده شده اما روی همان نقش هلیکوپتر میل گذاشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134698" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سفارت ایران در لبنان: تنگه هرمز جز با «شرایط ایران» باز نخواهد شد.
🔴
ایالات متحده باید این واقعیت را درک کند. یا از طریق گفتگو یا با استفاده از قدرت نظامی ایران که آن را مجبور به رعایت «شرایط ایران» کند، راه دیگری وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134697" target="_blank">📅 13:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کاظمی، وزیر آموزش و پرورش: برنامه آموزش و پرورش برای سال تحصیلی جدید، برگزاری حضوری و بازگشایی کامل مدارس است. به شایعات فضای مجازی دقت نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134696" target="_blank">📅 13:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu_Uk4SpOzu2xpZSt1oKmmpq_I3Z0X82e2LzpTDYecWRNG1ozP5CXRzzJVdDDJDQdzdpokhgv-ujxzDngeJcSBWJi7pKtORuU-AEgWtf2j8iDBYCzYfyL9S5CGYOasWAlrFSTEVOZU80jrij0cWaDH5VEgibm2P2LfJ35fE1rbhuHOzsYOQL-HKi8G1YVZRPfh1FyPpAbTlVOvbc5DMNIx30Y3QsRb-AOHObRwf4HUmWTdIsCSRb0KBhMKRqDEZZnklZuxb4H3bxON3P1J_bNzd5J0ACBau9FX7fqgJNPqY9yt8SXJNfkAuKAu0qJbj2pIHKKtfCSeeuzFzi0GVtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: از لبنان، سوریه و غزه خارج نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134695" target="_blank">📅 13:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الجزیره: پهپاد به نفتکش در آب‌های عراق اصابت کرد؛ صادرات نفت بصره موقتاً متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134694" target="_blank">📅 13:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی و نفتی عراق: یک نفتکش در بندر بصره مورد حمله پهپادی قرار گرفت، اما خسارتی به آن وارد نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134693" target="_blank">📅 13:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی ایران:  گفته می‌شود حدود ۸۰ میلیون بشکه نفت خام در این بازه زمانی(بعد از امضای تفاهم) به بازارهای جهانی تزریق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134692" target="_blank">📅 13:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIOYIc30wRSFuGomTqES322-LfuUCw5ppWRC5-AcshsLKgTTArDiSDCWTntGYiA70uLYL4vOMhaFYJpZey9n2oFEMFkRxgG9oivBzf4PXc83mjOTmSqL6Xl8xSIXshd14ofV2AjIBf_GG8PPL-tHojFr9fNfBKpsan2i0or6ECr015_crP6_hMuMImhZV5YfbleR4yeZe8xn1JOdfd_vWF00NUdtEKkkgI34Nfd6pRlS4wJBbbPKNHrzwgDyFOKrWxnSI9CrNYBvTYA2aJtyuEEQD3lxhzd3TguQq7jcU66VD7hG33a_OIIB8_UW7zFpuoi73_R6B3-lS9wHtUPBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افتخار ایرانی‌ها
❤️
انتخابت رو به عنوان داور فینال جام جهانی تبریک میگیم و ایشالا خار بشه بره تو چشم لبنانی‌ها و عراقی‌های مقیم ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134691" target="_blank">📅 13:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عربستان تعطیلی سه روزه فرودگاه بین‌المللی ابها را در پی حملات دوشنبه‌شب نیروهای مسلح یمن تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134690" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134689" target="_blank">📅 13:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=t7Fw0MdTc8P8zur4ULN9Furwe5yAcBDCeBGrkWNi3iMtdhk2g7AwOiPOkI42Gn4wgGHk8VNVouFuLYOeAWBG9s98lN2WIeh-dy9FmhGe_pPuPsXnNuMpHcjCkVAZT-xpDApEmfMz7A526N1-YqmoemB_dtI_hHvll7xoWvOvnHMJ3dyYE1-_9o_I8Pc_aN4h8PtppNd5h2E_bk89T-z-zxbWMbxDJnAs0aWXGSaq0nkVjXIFD8yTSGLouFc4MYwT_qXG8pUK0GhjdST2rYMWK1wXFWFsI4sVo_NSJYdtV73WM9wEQaIbE68n_coct05ycWwEp3CqKek5weTbJRXw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=t7Fw0MdTc8P8zur4ULN9Furwe5yAcBDCeBGrkWNi3iMtdhk2g7AwOiPOkI42Gn4wgGHk8VNVouFuLYOeAWBG9s98lN2WIeh-dy9FmhGe_pPuPsXnNuMpHcjCkVAZT-xpDApEmfMz7A526N1-YqmoemB_dtI_hHvll7xoWvOvnHMJ3dyYE1-_9o_I8Pc_aN4h8PtppNd5h2E_bk89T-z-zxbWMbxDJnAs0aWXGSaq0nkVjXIFD8yTSGLouFc4MYwT_qXG8pUK0GhjdST2rYMWK1wXFWFsI4sVo_NSJYdtV73WM9wEQaIbE68n_coct05ycWwEp3CqKek5weTbJRXw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا شب گذشته لایحه توقف کمک‌های سالانه ۳.۳ میلیارد دلاری آمریکا به اسرائیل را رد کرد.
🔴
نکته قابل توجه، رای مثبت 103 نماینده دموکرات به توقف کمک‌ها به اسرائیل بود. موضوعی که به هیچ وجه 10 سال قبل قابل تصور نبود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134688" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnLHKmPdMiKYL_7H3n684gq0T9wC33pygTko7grbilPn7IL1huZ4CMDt4e3nEy0hYibZ0g0pIzA-xnvxXy2SV4nEm5C_tsKTwD8h7yEbRyP4pZIrHyrZSnJrrANVhqoiuhyNUq7hWQD_6Q6icZTGsPlvCNu8hjVUsUcu5_KyE-O1CPR7te8NqIWCn0fRQqa5FhWjjGlSlqWhX6xgLryDK7QU-4mdwMHD6wldiUGSqW_RNE3xo0kIzY09bBvPZMHtJOHSaIhfwTib5oXJRYCTBq9fHpi8zeyydr6XIZ2fI1CEwgcHfdel4f61W97I-mxYTKJ3WeVjp3kgsfGNbHjddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده از سنتکام، از حمله دیشب به یک دکل ارتباطی در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134687" target="_blank">📅 12:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmf8mxgsDSctZA2RqN_eCDBdxfVoZHjt844UPT1knA2m0u_DAo3qbQVFao-2yj6pyDD1LbMP75ZUo_SRGOgrPoC5aYJsAOxlZFUbzoQPj-yQy711jFHcNJLSeLvLos11P7qC9RrfQ-ZsWhLDoZnDtcralAkiTn0QMBj7nNIIb1j7NUUBYNCF5TpXyHoej2VF9PZ4WOz-HVBch7Q7fQsMOusxODI7HZIugjxkweYPW4HB_jbeJy6gOkDEuKANCHw8f7Cj87FSobHpVQeGxjMEf1dbSbiCjKlxNOw_qMiMBCWYdLtMU_MQFKguqOqXeh9xGsuqume7VeWfgaENR38gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز گزارش می‌دهد که شرکت‌های کشتیرانی پس از حملات اخیر ایران به کشتی‌های تجاری، به طور فزاینده‌ای از مسیر ترانزیتی تحت هدایت ارتش ایالات متحده از طریق تنگه هرمز اجتناب می‌کنند.
🔴
یک منبع کشتیرانی با اشاره به ایمنی خدمه و بدتر شدن فضای امنیتی گفت: «به نظر نمی‌رسد ایالات متحده هیچ کنترلی بر اوضاع داشته باشد.»
🔴
در حالی که واشنگتن مدعی است که تنگه همچنان باز است و بسیاری از کشتی‌ها با هماهنگی ایالات متحده به عبور خود ادامه می‌دهند، شرکت‌های امنیت دریایی هشدار می‌دهند که هیچ تضمین قابل اعتمادی برای عبور ایمن وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134686" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / تلگراف: انصارالله یمن در حال آماده‌سازی برای بستن تنگه باب‌المندب است/حدود ۱۰ تا ۱۲ درصد از تجارت دریایی سالانه جهان از این تنگه عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134685" target="_blank">📅 12:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134684" target="_blank">📅 12:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4EURejxIjzOYaF7cpNK-Rnu1wkyk4qe_-aO7O7-NWoy4zemr2417HDLpi7y9LM0RhjvaB8rY9TDvoMpsnnUZlNLvpB4x91KuOTxFjhyhJpMlPwnzdklILCC8JZ-ILiUuP0-7ab7l1lN3-LFtTjJpvFxJjUqbDiStPaTyhrD1tabQysFhmTjujbgxb2sJ6iWgwMMzpRGgUJY31WGBKUcU7HK8pc7aUj42OqHyy8DtR1ldmbxjgLtzGB2lpIMuODIS_pRY_qJqzCHwewfR2DZBVd0cSE2ENdaEKO_V8wOHRZT_s_Rfxp4u__A_gt4tcEM8TO8Ud5nTFSGp8nh2hcATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رفع ممنوعیت صادرات سوسیس اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134683" target="_blank">📅 12:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سوریه، با رهبری جدید خود، اعلام کرده است که یک عملیات قاچاق سلاح‌های پیشرفته و موشک‌ها را از طریق مرز سوریه و عراق به سمت مقاومت اسلامی حزب‌الله در لبنان، خنثی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134682" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134681" target="_blank">📅 12:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cugIunwc7RRVX24lUYlf80ZY5_HmhACJsUcTpzadolKn4Xz9D89fY3ty4M3lcix0YjHuY0iz5PfDEZDw29EY9IoIIZS2wyerSd_MKewmKNFBjSLvbul3YEaWwxGYicLml5XZkbsdnh8I2gGjJcJg3sXVsghR3yZaZdJBqe-qjNeiDfNIOZuiwbn48qT8Rx47VILgY0sX_RBP5zqo5cwP5HHnVe3ygGZffJKaTu94VNH2s5MzagVgb7RzKrYbK8f8LkwGEJdnI_OajImmOmNyPL55QgtpdQgbasAK0peAYhzK80CzvkwESYHzcHUdx3YDkckccKRQ4zleJix5eVKxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJrfCZf0TTeZHc7zImiwp9t7enf6oOQmFL974S_yfWCFJJvmOG_WhJAk-n5ufrh9xE_GnR40_ZwQezzOer2oZG5RvTzdpI0xr2xhV1ivd0EgZ4uGuv9uoijpUkFg0vELFi9-OYnlfbLgWPIgdRkpvD46SCfHxJZAoxRoWs7EqFX2TRJPl61YclmH-dred35QQMvH0h_mbBOyTNFlIF9k0MYIAMwsdmqQEBazLB8kjAwJ4Gr_IpYL91JaQwzFxwAAezE66y7F4jXwDbqgMxfRNoBCF1FO7BRux3VClsrPmRdCxrjeLYwfGGehFCnRLk1wqmQG-qrsKFgEpgGGwDfJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-sorAwpArksghxLoKzm1hG5ENG1cf4Kaa_U2QyxYm8e-CHrqSiIoC7obBPZ9OQzMoW4qoujZPnTkamM7AsBQl-dNX7eknAQK9865WETrEHEAVjLQqHwm-6sqEhuillzxdDvLduSS9UaZa8iBt9URJM_tf7T3qUbgqnVdGYNrTO-abPwj5jSY6HAy4AGyV1NbCAIC3qyJx-8gbHZdcIZzDxFaL5qm0N6zbkYEhe22CA21JHs7nnpoWvASbt5Nkbr1AMIqHFh-vVaw0VwXVddE2w_uwxFiZaS67TfQSGAGS3Hvfpcx4GBX-Op-Eg03FuPPc2_5IECjKTI7vnx8kxGFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مشهد همین الان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134678" target="_blank">📅 12:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsUHlnvCv2m4YSlvpV7J5jWiDma2v6RR4K9TizBYABbu9ONWULPYzeSJxBIE8-zOi5jgmqFRw6l9i30YQz7hSNEDq6P3hskTDqg1xoUrtHgFt8nLjAWseMhniGbII8D-KdSaFTLmcK3tP5n1DtfWh1Z0MVMmcYPkjSnG5-AIShhmxuoGkHhPVKL5l0KaDFL22gNgjBYvb94gbnDZSphH2eOA7gS6inGcCeh8upJhnuwIvLZ4d-Ey-7jNY6CkQGhdrjpebjx4N5J4q-NeoU38nfVnd0pJhQjWAkznFnJ7iXj91WW5DsYGyExUBvZCK4GerviFNHiDV_qStB2NVxnevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/134677" target="_blank">📅 12:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
هاآرتص: ترامپ در حال بررسی عملیات زمینی آمریکا در ایران و حمله به سایت‌های انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134676" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / سفر نتانیاهو به آمریکا؛ به تعویق اوفتاد | مراسم سناتور گراهام هم به ماه بعد موکول شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134675" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYqay_nFHEQ8uhNei-GkeDjQV_CKXVgl2Zmwo0qAFbKzhyXcxvnOIVKYQ3IJDCemIaK3-Y9m0uuyG-dBHDt4ttaT_OS_8-xQXdJr2EpkyHCStklEUOxdJiGnitXcLYYgiSvnEDFa4I7D4yE2A7Ofexmbzxh0xPzxRNjwLhCJO5fT2iscU_fHNWmjbBbEZpyaI9UOOLaTaceMnOnFjI8sq-caAt2HB4ZmitQsSCE5jsBxN8dz3RrOtejfPOJ3mttiwn5RyowJxcGWmQNrseYVDCptILyLe_Kl2z2d1t6hgLLvoL7gJVc5VBUDkW7NcZaV9xaJsASju1r8fP1zUDFFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه سی‌بی‌اس، انتظار می‌رود که دونالد ترامپ، رئیس‌جمهور آمریکا، در سخنرانی خود که شب پنجشنبه پخش خواهد شد، به اتهامات پیشین و گزارش‌نشده‌ای درباره دخالت چین در انتخابات، اشاره کند.
🔴
این ادعاها شامل این است که چین در طول انتخابات سال ۲۰۲۰، به اطلاعات مربوط به رای‌دهندگان آمریکایی دسترسی پیدا کرده است و اینکه سازمان سیا از این فعالیت‌ها مطلع بوده، اما در طول دوره اول ریاست‌جمهوری ترامپ، او را در جریان این موضوع قرار نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134674" target="_blank">📅 12:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الحدث: حملات دیشب آمریکا به مکان هایی نزدیک پایتخت ایران نشون دهنده گسترش عملیات و تغییر عملیات به اهداف جدید در شمال ایرانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134673" target="_blank">📅 11:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134672">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری فرانسه: پاکستان از آمریکا و ایران خواسته است تا مذاکرات را از سر بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134672" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134671">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMozv39wZxVrDej9ztjL0zzEwLx5pZ-WnoT6SCnWZlZJsSBOCmd-IJZ6i6_jTZRvACferM9Z-OkB01_4M0Gy78IKEZhEh2oyJP0767LB3Q7xEU9zxjgCpyqjGknuOlTFknpi96S6FarCs7b7onGm2KRENgKTnMPuELz_9bx2Bv6pZ4qufkkZNbrGOph020sRYc3t3jVwKcgu5JjWkGMktLRNYjdHbnbx9grXK1Dr256WLHodyP__Y6E6faOZxgsC8GqaWd51WyuVpUGzd3ighYU8EKdIIHH0K4bKSAJdGI3L273bG_wyncigkFP91CQqfpzOU7lpkJ1hHczEF3ULNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد امضا کنندگان کارزار «درخواست حضور اعضای جبهه پایداری در مناطق جنگی در جنوب کشور» ۱۱۲ هزارتایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134671" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134670">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de798daa31.mp4?token=LEUekTjGrGYwJILX1z6bX87yGwdJmSj0Jcf8z0mitM4CE5psCdzxm5j6OY2S27Cv9BJoN5iOKJtp6f3lK2gfpaCEA4ByekOjylAy3ALAndynhjk0ohi9zoQRd883p155NDdbrGIpOngZcebrRudSfSaqorOODacX9m3ddWha6qeqnNWpotfoe9G_16xMTLHBhkp8eIk6gYjO9e9ecHy8pDFDeMNqBK0ms30qPrxE7ZtRXZb1khT5vjLwm71tCQWPLfvcRzvWH-rnFNBqkgRIPfxpZimMw8uXYj_Qzo86nnaDzdca3dwV_AJWNVEHm83jtn5g-36BYEI8G0pgJgtSxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de798daa31.mp4?token=LEUekTjGrGYwJILX1z6bX87yGwdJmSj0Jcf8z0mitM4CE5psCdzxm5j6OY2S27Cv9BJoN5iOKJtp6f3lK2gfpaCEA4ByekOjylAy3ALAndynhjk0ohi9zoQRd883p155NDdbrGIpOngZcebrRudSfSaqorOODacX9m3ddWha6qeqnNWpotfoe9G_16xMTLHBhkp8eIk6gYjO9e9ecHy8pDFDeMNqBK0ms30qPrxE7ZtRXZb1khT5vjLwm71tCQWPLfvcRzvWH-rnFNBqkgRIPfxpZimMw8uXYj_Qzo86nnaDzdca3dwV_AJWNVEHm83jtn5g-36BYEI8G0pgJgtSxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توقیف کامیون با رانندگیِ دختر ۱۰ ساله در هرمزگان!
🔴
رئیس پلیس راه استان هرمزگان:یک کامیون کشنده که توسط دختری ۱۰ ساله هدایت می‌شد، توقیف شد.
🔴
این اقدام، مصداق آشکار به خطر انداختن امنیت ترافیکی و جان کاربران جاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134670" target="_blank">📅 11:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134669">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=VLOgEjS4udOvJJrTrBNkJ3LP8hBvO554Gp9Mbnswo5jFUSaQYHtXyxb9rj9ifOYstLaEIcOkoN-8Ew939ZUEbUEbNlMneSOH4k45mfr87Vusby5vifzwEWyoXakxv1uGHzGlc5dwJJT3CjF06b2aEr4yNdrPwCkry5vc4KuOyVy1ZEDZRY-OGhK7yYSrRR4wy4CkGt1rTwmUK4tTItjk1Odm0dAG5pjNA-S5Y757dI1_XlZYhG06jIMQm-Jev2bFmEh5GKwhTrLINW83jV4rIAK-AsOOlwbmSzZbRpCavCxl4NWR6DFEg8paYdrLFenzNrM2-mk03P50dxFkGfbcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=VLOgEjS4udOvJJrTrBNkJ3LP8hBvO554Gp9Mbnswo5jFUSaQYHtXyxb9rj9ifOYstLaEIcOkoN-8Ew939ZUEbUEbNlMneSOH4k45mfr87Vusby5vifzwEWyoXakxv1uGHzGlc5dwJJT3CjF06b2aEr4yNdrPwCkry5vc4KuOyVy1ZEDZRY-OGhK7yYSrRR4wy4CkGt1rTwmUK4tTItjk1Odm0dAG5pjNA-S5Y757dI1_XlZYhG06jIMQm-Jev2bFmEh5GKwhTrLINW83jV4rIAK-AsOOlwbmSzZbRpCavCxl4NWR6DFEg8paYdrLFenzNrM2-mk03P50dxFkGfbcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های مهدی مطهرنیا در مورد احتمال حمله اتمی به ایران
🔴
باراک اوباما هم در آخرین سال ریاست جمهوری گفته بود پایتخت‌های ایران و کره شمالی در مقابل حمله با بمب‌های کنترل‌شده هسته‌ای استثنا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134669" target="_blank">📅 11:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134668">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
🔴
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134668" target="_blank">📅 11:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbRbYn9P5ZdLWb4LC2p2aD-xRfIpc3EY8-32DZrFEzOp-EukpmA03ux0UvGhA52Vc5mURR-Lmr3tzLJZyLqxgy47SdOYjUqkxMUrmtK9KdxH1VqcAI-6QPN7P3fdEJm1WiGu9D5_2fGJM3yyTDX0o_RK_hsa1M_yPWM73AO7IKctQoIweWrQ3f3j9vsKF2wuJcb-h3O4YdXIApMvvsJcVwJJGusVDztjjPnEdiLMsQ5YDn4NQKV_L4pthiEY9oufdPTVC1TVsSMVxmeXviL0kjdWuMbHGAx3iOsOjQKDjanRBo4kJxvytTJLGttXxfodwU1TMTILga-Y9uTLbnIMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرآنلاین: احضار برخی نمایندگان تندرو در پی ماجرای تحصن مقابل مجلس
🔴
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس، در گفت‌وگو با خبرآنلاین با انتقاد از عملکرد برخی جریان‌های سیاسی و رسانه‌ای در دوران جنگ، گفت بخش زیادی از تریبون‌های رسمی و رسانه‌ای در اختیار یک جریان خاص قرار داشت و انتشار برخی روایت‌ها و اظهارنظرهای هزینه‌ساز، زمینه شکل‌گیری شعارها و برخورد با مسئولان کشور را فراهم کرد.
🔴
وی با بیان اینکه برخی افراد با وجود مسئولیت و جایگاه خود نباید به اختلافات دامن بزنند، مدعی شد بر اساس شنیده‌هایش، تعدادی از چهره‌های مرتبط با تحصن مقابل مجلس از سوی مراجع مسئول احضار و به آنان تذکر جدی داده شده است.
🔴
نصیرپور همچنین تأکید کرد برخی جریان‌های سیاسی، بقای خود را در ایجاد دوقطبی و اختلاف‌افکنی می‌بینند و معتقدند با از بین رفتن این فضا، سرمایه و حیات سیاسی خود را از دست خواهند داد؛ موضوعی که به گفته او، در نهایت هزینه آن بر کشور و مردم تحمیل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134667" target="_blank">📅 11:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روسیه: جایگزینی برای حل‌ دیپلماتیک بحران تنگه هرمز وجود ندارد
🔴
متأسف هستیم که رویارویی‌ها پس از امضای یادداشت تفاهم، بار دیگر از سرگرفته شده
🔴
امیدواریم که مذاکرات ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134666" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز به ۱۸۸/۶۰۰ تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134665" target="_blank">📅 11:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روسیه: شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در اودسا انجام دادیم
🔴
وزارت دفاع روسیه سه‌شنبه ۲۳ تیر اعلام کرد نیرو‌های این کشور شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در استان اودسا انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134664" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nl4avOmbwqh1n-R8T4HZ4xODKDDV74TeyNh2AlzWcenMKUiyyX6QcOicJ_ebAM5JwJFQsUVFtAkP8aIQjjbKr84f2YKcv0ZgmMyn4ORdOzU6AsX8ekfvmrC8kOrgY7-cIgmTgqxutXVFYKQlfs9Uonj778Dwd0YPkeg3f9PqHSmGdHIC0bgNapVEDPP5m_IXXBfOoUzznOPJtSGwXfWn-GElEbz8bpqgidSgGgJ0-xRYxXq3ItqRs15rcYQhcn4TksYJwkDgEVQ0G_5I0pvH13J-vXNzh-Qm18QTt1NW8NVMvA6JQfRd6BVgcEsCecitWW7mB_YIi5--S4SkAYw-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRXrNdHk1ZgDvUbcECWrKy-gDLmRAFaSKV0p5mOjHaaGvHBKPlkRKbQD0UVCT4xlxy43s4lmJ92VAxpWwmPnZs_F1upxGiFviXvEYFGTRIEgafZU5KeLWS64GmGxmJOUKkcoPo1btlQCI7rUrY73Amc7U7G0gUuEzDRXkuFRHaq3iXOlqtlPncVybbmF5uaP4SIc3xuMmePrBqh91U1jjbvNzJ-nfyv1rgwXB9qcpEKMaEY9afr57OXwJ3_0AJ9J80cK1gi-nCeAklJyrkghYbEjEAXuFxTsKzILO6zOFwrRsFjPV_1OvzZHsgfGhcu5xOA3r3eyZT4YlTiqEd_rGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgYAP6aFCwz9T1rFYE3bHLc10IgUIp3Rb4XmWv5kr87hXS7Fl_I5JLBKlbn3qZo7q52NYLZ9thwCXv_d1dG0CA39Dgy9Gi3XjCX2TG86jMU2MeRf2J6aR-9fGmf7XKCAnkOVwN935O2SCYMKueJTvCSfZUF53YeSmOs9jbteFZTSdBYkGvxiztsDzuAqg06wCUEkzhsQFY23i7njFJSVMDHowXr1XiGhH-sHQWO8jjVF8WPXL3M3vfXILbY8LW0zlK8c0aI8tAwQGKQmEjCvAkzx_RsJJsUrs4j4LLDQXV7JkeL66ygjQ6ollwTXnHLcM6CH3eqOjRu8PHd68pExdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVMR6jeIAa_j90Irep-Rn3kwwF4nhl6hXUR-aa4EfPatcs4drFxth14NowIpulxQKDy-GLMzjFvu53m4R2PJEuvgLO9Z66U4DDtAUCOjk_-F7sdfkYAejVL0LkQwJZ848vPJ1WnOCqRN9dTrd5_HdVAcKZN5QM8-pjb7Krix8qkrLVAQOAcX3zhPtkwl-bWLwI0ihEUn5elL9UCI4hZYZsLpJjFfe-_B7uAH2sc-FwriMPKHX4nk6qvLl0_ea9FnIHx_BL-t1Nf3m49Fm5EEyVxRb9DSIAeuqlHFD6g0LJvJlSC2wo8Wf7QYq8AXlDCpVJoxQ4yDXMGIUyId8I32Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازیکنان آرژانتین بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ای که روش نوشته شده هر بازیکن پنالتی‌ به کدوم سمت میزنه.
خنده‌های انزو فرناندز که مقابل اسمش نوشته شده بود “وسط بایست” (یعنی پنالتی رو به وسط دروازه می‌زنه)
@AloSport</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134660" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=slmQJ4MbKetlw6x8wmTrzchpjfTeahOSVdfyRJAxoWIiiU564l5dxtLp7ldEG-nwVFCNZJmys2hPwQmCSTuq5UAWTWTpjNzo0y06X3QrbpyC-Gz15Ej3ofb08nF-sGUS1DJXs76soyA5-8wWF-4C9zg8NnPjXz4Cb8KN3-EW9kAHeQto-6gbpskze5GcQygkDEO92H3AkBudJkzwsfpvA7L5ZL3by3a6oRF5U_g32ZgzJ5jKhM_i0FUAB7YYvJQE6oHm0zdUmh_-ZLuhBnvB_069ucyho5j7NtlEeuSILRG67aUrBqlsl81QPqr5qxZoi5C8hdhl-Q_woMiu1lNjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=slmQJ4MbKetlw6x8wmTrzchpjfTeahOSVdfyRJAxoWIiiU564l5dxtLp7ldEG-nwVFCNZJmys2hPwQmCSTuq5UAWTWTpjNzo0y06X3QrbpyC-Gz15Ej3ofb08nF-sGUS1DJXs76soyA5-8wWF-4C9zg8NnPjXz4Cb8KN3-EW9kAHeQto-6gbpskze5GcQygkDEO92H3AkBudJkzwsfpvA7L5ZL3by3a6oRF5U_g32ZgzJ5jKhM_i0FUAB7YYvJQE6oHm0zdUmh_-ZLuhBnvB_069ucyho5j7NtlEeuSILRG67aUrBqlsl81QPqr5qxZoi5C8hdhl-Q_woMiu1lNjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از ماهواره های استارلینک ایلان ماسک در آسمان ایران، دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134659" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت خارجه آمریکا بامداد پنجشنبه از موافقت با فروش ۲ میلیارد دلار سامانه‌های موشکی نقطه‌زن به عربستان سعودی خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134658" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFwItLBuUFtN8h_qiprC9EyGZpcnvVCIFts_r5om1B6OFHj6J6FfHMfqCGhOni7PWTTm6J1PC4b3415Z6Wslilh_GNPx6l7GMLhLkWdRZyJd-JcLl1Wj_I5u7Q6nG-fjQMP5m2FXlbni3oLVKRiVVZk1H-E-jXeu7TlNYzO34tRs0XsN8MOs1oYgHkWeuLt97vUciCOh9Psy_Y_dlKmr9HloSX4AI9Fo2FgfNGHuZbZXi1FK8frqlYKLcBEFTXo3kILXkP8N5aZAIuvteCuxEC9SEhZoHcJsHA1T8l03un68FI-QABikjAAeSXs8LVf-8giSSXYPHzYcZIn9dmpJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفری، نماینده مجلس: پزشکیان و قالیباف حاضر نیستند اعلام کنند تفاهمنامه با آمریکا عملا نابود شده
🔴
شجاعت و صداقت عذرخواهی از مردم را هم ندارند. اسمش را جنگ بگذارند یا نگذارند "جنگ سوم" عملا شروع شده
🔴
ترامپ، ونس، روبیو، کوشنر، نتانیاهو باید قصاص شوند. نه تنها یک دلار در جریان تفاهم نامه را آزاد نکردند، بلکه آمریکا در حدود یک میلیارد دلار ارز دیجیتال ما را هم توقیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134657" target="_blank">📅 11:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای جنگ اسرائیل و آمریکا
🔴
هگست، همتای خود را از فعالیت‌های نظامی ایالات متحده در ایران مطلع کرد
🔴
کاتس بر اصرار تل‌آویو برای ماندن در مناطق امنیتی در سوریه، غزه و لبنان تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134656" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134655" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما به تعامل فعال با طرف‌های اصلی ادامه داده‌ایم تا از تلاش‌ها برای کاهش تنش‌ها و گفت‌وگوها حمایت کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134654" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی ارتش: در صورت تداوم حملات آمریکا، جنگ به عرصه‌های جدید کشیده خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134653" target="_blank">📅 10:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiRgSdkw0cFJQMpqohHsf7ajP45lcSuQHZmFh1buW84X9YgZCoNrV7FVxZXvEjiP51bva-9eE2OmVbb-Zn1tf_IItkarlwKAEhZTDRKk-RXaH4MFben2wrO2VEZEUvADTyw_3IIdtIxHAnxZ2a6-D0ZzHXCFCqahJOJCY996De4uYSwdP_pGTIo-52MYpfW3uCzevp_A0tk2dEmFUqMKOZnEkvNSqZZVNl92X0EwY7O5dIZxMQu7z1fYVUdxxP0hsFSGzFfil6eCB7Vo4KGSTEoLxah-CLTNbrUFoKxgR4DWdrcYiiVG3uNE83hva7hocdNVsTeLVkElJ6ZExckyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عقب نشینی نفت برنت به 84 دلار
🔴
قیمت این لحظه برنت: 84,69 دلار.
🔴
نفت آمریکا: 79,42 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134652" target="_blank">📅 10:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
شبکه آمریکایی سی‌بی‌اس فاش کرده است که رئیس‌جمهور آمریکا، دور از چشم دوربین‌ها، از رد پیشنهاد ایران برای توافق هسته‌ای ابراز پشیمانی کرده است.
🔴
طبق این گزارش، ترامپ بر این باور است که واشنگتن با رد پیشنهاد تهران برای محدود کردن برنامه هسته‌ای‌اش، فرصت جلوگیری از طولانی شدن درگیری را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134651" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=sZX4TlPgSDO6dbqFOKwl1WA-4kucwMlPUMasXzJ3tJOt3BmRY_kl8tQnzzl93mixIYxv-ntgATdEXt6p9N9cQOHRdS36F8m20JIppDK_6tZjGTo-QS6t0DfGIIw6L0AmhotN8M8_kK0pZE29eRT-RS5cLB315zv1uhJi4lppc-zj9mdVNpop8kCy_VOe7qyn5lxqi2gRS2g6R3uVc7441NeGxRWYjh_tA5-_K50aWhtUpVRBfx3i_pbj4wQGk68OyB-BwnyrnXjebgHsz_Djd8KEI5WnmYFowiS0YsCchaSUpAdWr0IU159lEdlBc_pXD5W9iKXzk3th8zY7xIhqtJ1NU3ZphuH5f2lUFiQdvVWhCcGINMRvYuf7vd-vbmHM_4MVeexzoAhwisCpNd_mQMs3eWASqnODxjpOGFNdO7ykGBP1hnvpaidne3XveR9CXP-BhVzd1U2KYXesNd2e4zDXc87tVEIsSWqT5KsH8T8QgaqDdGcwyYJ_rYXvkT5Fg4yASdLLC5-81Guq71TDcbK-N2_A7fKLhymAy5YMh97i6lVT3I9D4_RmKswZ_CDfiTgRiDNMSIQMquRxgT1rT6eqsFkNA7q0n-OUw0e9lPAg-9OCahuEdv6_UsKqciLqWJWbvyqGFayFS-bIGJunlMX7cTuDkEyV-WzLBvAuD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=sZX4TlPgSDO6dbqFOKwl1WA-4kucwMlPUMasXzJ3tJOt3BmRY_kl8tQnzzl93mixIYxv-ntgATdEXt6p9N9cQOHRdS36F8m20JIppDK_6tZjGTo-QS6t0DfGIIw6L0AmhotN8M8_kK0pZE29eRT-RS5cLB315zv1uhJi4lppc-zj9mdVNpop8kCy_VOe7qyn5lxqi2gRS2g6R3uVc7441NeGxRWYjh_tA5-_K50aWhtUpVRBfx3i_pbj4wQGk68OyB-BwnyrnXjebgHsz_Djd8KEI5WnmYFowiS0YsCchaSUpAdWr0IU159lEdlBc_pXD5W9iKXzk3th8zY7xIhqtJ1NU3ZphuH5f2lUFiQdvVWhCcGINMRvYuf7vd-vbmHM_4MVeexzoAhwisCpNd_mQMs3eWASqnODxjpOGFNdO7ykGBP1hnvpaidne3XveR9CXP-BhVzd1U2KYXesNd2e4zDXc87tVEIsSWqT5KsH8T8QgaqDdGcwyYJ_rYXvkT5Fg4yASdLLC5-81Guq71TDcbK-N2_A7fKLhymAy5YMh97i6lVT3I9D4_RmKswZ_CDfiTgRiDNMSIQMquRxgT1rT6eqsFkNA7q0n-OUw0e9lPAg-9OCahuEdv6_UsKqciLqWJWbvyqGFayFS-bIGJunlMX7cTuDkEyV-WzLBvAuD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر از یک کشتی مسافربری که ارتش آمریکا آن را منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134650" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVVHF7XH00T_RIicPsYNh1oO4vGDzVwvUhusiCh171mBuKZmfbr2lYSKKZfiPysVf9VSgc985d84QhDBHA6VAfyHhthdU_MJOM8-NlK1FrQmswuygoJjn8AEQprkP8NnrO88_GjV3Ik1SbIdZcWqjjgr20Q07rrb-IyCrjVe7PNbdVSt6rWaO7R8kcDGUwXOqVE9_QTb5Ajbu1W532TeKdhMcz3_nFGYX_syLNqlYhDucMvTyLVqV2EyJyzh8mwcFHMj3UD-T7SBEBnejI5LKXen33VfIGEfN6z3tY7N8bKOOjOphIHBh2lOztb3XNMwhHNZSU2Wq4AAAJUTBuYgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abBERpPVkT3WRHopEfhtvaiKqFL5n8Kfz4ZjvQLS4McfY7qBw5po2TMo5bexeM-ChvFg3r2Bx-5jQVoCwaoOjaGng7OqIC5hNcKDWdlX7a8Y8TyPqRChPleC2hoAuIY7VTUuaD0uCeC0pq8jKh2Ic_RpFwUXcChGhH7_Cy3LTlsFeoxv9B5RtLUuR4hAaVmUw-R1OyJ857fz3Q00VGHTdA9K3wKnzVx6S4qEkgyb3R7jqTuJTp0UnD2r1TbragTcOcaXDn9eGDg3_zaR8rbIxjdkJEcDTrFX9sMjo9YEL5NUB4aKe60rZtDJ5KSHYf4D10LVNuwUqEdHDxSDJB-0JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
ولی ما میدونیم چرا!</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134648" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه: بحران تنگه هرمز تنها از مسیر دیپلماسی قابل حل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134647" target="_blank">📅 10:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qxcfGw7F6jLOitI3T96ueDId2KaKCwde-M3vo1_Fp_EVUhhg-TMGtZf19iUQDMxZI644bHI79A9_7YnXW_M0N5x0m9aJhCqpD5ZfzHKIbUSHiwkE_z2bwKjnagxCemD3SKwsS2xzsZF-UrxHmVbtFfLmMcvalVrJ9oFhfq5pn4JOYKKSvJejth7xLNhOyE2y00oGbcuqjx9cYqhmE8NSYjqFYsEROgyqXxPCKgJzna6j4nlZNda0nNbc5hFT0W0gqFx1tCnKghytkgVS8E6ip2Scbg2sKXNvXTUfVnAEriQZNey5QzpJMts5daefNliOCWaTcPnfjJ_tZeFmWcja2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qxcfGw7F6jLOitI3T96ueDId2KaKCwde-M3vo1_Fp_EVUhhg-TMGtZf19iUQDMxZI644bHI79A9_7YnXW_M0N5x0m9aJhCqpD5ZfzHKIbUSHiwkE_z2bwKjnagxCemD3SKwsS2xzsZF-UrxHmVbtFfLmMcvalVrJ9oFhfq5pn4JOYKKSvJejth7xLNhOyE2y00oGbcuqjx9cYqhmE8NSYjqFYsEROgyqXxPCKgJzna6j4nlZNda0nNbc5hFT0W0gqFx1tCnKghytkgVS8E6ip2Scbg2sKXNvXTUfVnAEriQZNey5QzpJMts5daefNliOCWaTcPnfjJ_tZeFmWcja2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134646" target="_blank">📅 10:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8vn1Pnbo5w4twZwNmrH54nGSQ-qSBo7-Ydx1eWmNzEO4xazkjClTKC08Lbo3E5KLjCRllhbi4a1qAAvuFCueRtggREZ3C4zNbawswBh2TYoP2-3qabDWWR0Tohjq-3rE-t5oq2AOFOHLGRySAGuuIUVVfJgkAJVVRWCORPxKeS1fUHUe4vQl_0tE1pEisD13F8_kRMigkN6Yp6t3GXSPPTvxppk2bBhrBSKW0c_9tmFn-YVOjZSmNyaPXt0Ppn1p-NeovkSXcRDPLIH7lDZ57o8xMkem05o6kCSEmB15PmrMFnLuMGp2869mfCr44_M40vQ9taj36gubszuk795oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف جالب مسی و یارانش از گلر انگلیس
🔴
بازیکنان آرژانتین پس از پایان بازی با انگلیس به‌طور اتفاقی بطری آب جردن پیکفورد را پیدا کردند. او تمام عادات پنالتی زدن بازیکنان آرژانتین را روی این قمقمه یادداشت کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134645" target="_blank">📅 10:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری /  آمریکا برای حمله به کوبا آماده می‌شود
🔴
شبکه «سی‌بی‌اس» بامداد پنجشنبه به نقل از مقام‌های آمریکایی گزارش داد که پنتاگون در حال آماده‌سازی برای حمله نظامی و تجاوز زمینی به کوبا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134644" target="_blank">📅 09:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی قرارگاه خاتم‌ : اگر زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134643" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جی‌دی‌ونس در مصاحبه با پادکست «جو روگن اکسپرینس»
🔴
کسانی که از مذاکره با ایران امتناع می‌کنند، هیچ راه حل واقع‌بینانه‌ای ندارند و تنها پیشنهاد آنها بمباران بی‌پایان و بیهوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134642" target="_blank">📅 09:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سپاه: مرکز ارتباطات ماهواره‌ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134641" target="_blank">📅 09:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اکسیوس: نخست‌وزیر عراق، درخواست‌های ایران مبنی بر عدم سفر به واشنگتن را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134640" target="_blank">📅 09:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فارس: آمریکا در حملات بامدادی خود نقاطی در کبودرآهنگ، استان همدان را هم مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134639" target="_blank">📅 09:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ تعرفه 25 درصدی بر واردات از برزیل را وضع کرد
🔴
مارکو روبیو وزیر امور خارجه آمریکا در سخنانی اعلام کرد که ترامپ، به نماینده تجاری ایالات متحده دستور داده است تا تعرفه 25 درصدی بر اکثر واردات از برزیل را اعمال کند.
🔴
روبیو در صفحه شخصی خود در ایکس نوشت: لولا رئیس جمهور برزیل و دولتش با حسن نیت با ایالات متحده آمریکا مذاکره نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134638" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cd351ed4.mp4?token=VZCjGMN-Z4MTuemWfRJS3gVSaJ0zAe0Wh0v6aCdKRT6s1lsEtp9kNbV-Otx5jipkuMtU9gu4pzR2edN56DN9MYeGZbcIYZq-0xrmXDeNchndQFzwz3iIyEzKtAZuIaWmrCp4KMFgA0ndVn-a0pg_hPXZuBTcBJ1xazynsNWxnTpotvGtS-OwqH2rj1neR_pmdLlpBEvdQwDlh7Vw1AOIiQrZfZWcbYdzfUej56BUI9Z2RSg9rOZt0KfDmDPlNCjZkdwivN54SclZvon9qK5CQ26Hanv7OsRTolRapazALBtMOEumjfQP0IGY1E4qBpeeVzXTDHwd8cRg6gRy1kkQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cd351ed4.mp4?token=VZCjGMN-Z4MTuemWfRJS3gVSaJ0zAe0Wh0v6aCdKRT6s1lsEtp9kNbV-Otx5jipkuMtU9gu4pzR2edN56DN9MYeGZbcIYZq-0xrmXDeNchndQFzwz3iIyEzKtAZuIaWmrCp4KMFgA0ndVn-a0pg_hPXZuBTcBJ1xazynsNWxnTpotvGtS-OwqH2rj1neR_pmdLlpBEvdQwDlh7Vw1AOIiQrZfZWcbYdzfUej56BUI9Z2RSg9rOZt0KfDmDPlNCjZkdwivN54SclZvon9qK5CQ26Hanv7OsRTolRapazALBtMOEumjfQP0IGY1E4qBpeeVzXTDHwd8cRg6gRy1kkQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه وقوع یک انفجار بسیار مهیب و باورنکردنی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134637" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQe0_TFbmtMcdBKtJshicnKXVcCHrSJgv71hPlaE9eCLoD3xoVScVJ7LwvZo5MGVuT1wKWzss5u3qbp9hXG5FhDzQjnZDluJ9Tbg1D5H6wesyLTLRAUts1-a131TF_reLYM8cDRFtqrydQskb83K46SgiBSTMA1XdFqQsu3QArwSj0lNw-XSUYEtOuwJLTbbMhOOQENITQIjOcqSjzCxcLfJJepZjGSGx6XzFHuhOXPhzrEjha9B6oKYBplB6HElCySKa4lzQmQJERqwUcMyrMx0OaK7C7mTFnkrXdcXWscGPzF-lHu3WRyDvesESus7J5CFbu08AlySqPNi-WAZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: چرا ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی در ایران بوده است
🔴
به گزارش سی‌ان‌ان، دونالد ترامپ پس از فروپاشی آتش‌بس در ۱۰ ژوئیه، در حال بررسی گزینه‌هایی برای تشدید عملیات نظامی در ایران است.
🔴
این طرح‌ها که در نشستی در «اتاق وضعیت» مطرح شده، بر کاهش تسلط ایران بر تنگه هرمز متمرکز است.
🔴
آمریکا در پنج روز اخیر حملات روزانه‌ای به مواضعی از جمله «تنب بزرگ» انجام داده تا توانایی ایران برای مسدود کردن مسیر کشتی‌های تجاری را تضعیف کند.
🔴
ترامپ علاوه بر تهدید زیرساخت‌های غیرنظامی و انرژی، گزینه‌هایی نظیر تصرف جزیره خارگ و بمباران تأسیسات «کوه کلنگ‌گیر» که گمان می‌رود با برنامه هسته‌ای مرتبط باشد را در دست بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134636" target="_blank">📅 08:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ونس:  کارزاری با بودجه‌ کلان سعی دارد مذاکرات را از مسیر خارج و توافق را نابود کند
🔴
برای این کار، افرادی از یک مشاور سابق ترامپ حقوق گرفته‌اند
🔴
خود این فرد از عناصری در دولت اسرائیل دستمزد گرفته است.
🔴
این افراد به من حمله می‌کنند و می‌گویند نباید با ایران مذاکره کنیم بلکه باید کارزار نظامی را ادامه دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134635" target="_blank">📅 08:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حمله آمریکا به فرودگاه سمنان
🔴
بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی آمریکا قرار گرفت.
🔴
این حملات خسارت جانی در پی نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134634" target="_blank">📅 08:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کیهان: آمریکا از اینکه ایران به بحرین و کویت حمله کند دردش نمی‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134633" target="_blank">📅 08:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر علوم، تحقیقات و فناوری با تأکید بر فراهم بودن شرایط برگزاری آزمون‌ها اعلام کرد که کنکور سراسری مطابق برنامه زمان‌بندی اعلام‌شده برگزار خواهد شد و همه هماهنگی‌های امنیتی و اجرایی برای برگزاری ایمن آزمون‌ها انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134632" target="_blank">📅 08:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سنتکام: این موج از حملاتمان علیه ایران پایان یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134631" target="_blank">📅 05:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
انفجار در سمنان و همدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/134630" target="_blank">📅 04:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134629" target="_blank">📅 04:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط ماهواره‌های ایلان ماسک بصورت خطی دارن میرن و تو ایران هم قابل رویت هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/134628" target="_blank">📅 04:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دفاع‌های هوایی اردن فعال هستند و در حال تلاش برای رهگیری موشک‌های سپاه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/134627" target="_blank">📅 04:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند در شهر ری
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/134626" target="_blank">📅 04:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکدشت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/134625" target="_blank">📅 04:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فووووووووووری/صدای انفجار در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/134624" target="_blank">📅 04:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=UGqIegl5WWzyZ9_MAL2W83vwA2IpRzQBkUWzJCwxSIJYR3n9xnikBrFhlM1nbrU8LQd2EzbdvDNm5KUldvPiANKUDvaGjBTe_45onl8Q18KLD7Gj4SWf1vt6By--T-CSerroM1pPycCmUZkAyr6IrxSx5GbsCTE1NACQ3MbyvKa4RrhCLqCVqe-7G6bCO1Lv1HctteSXbAobxlUlWP6oKBjLWPziiancJ0PxaerPY8eRTd05j4_1dZHNoiU8NIFvdhxf918CcLSd6sAf5mgzZUXlsRj2XvOm7wTz6viucNcXjf91wjUHSYtIllBYQ17Qu01ljzbTbGFlBiZqIImK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=UGqIegl5WWzyZ9_MAL2W83vwA2IpRzQBkUWzJCwxSIJYR3n9xnikBrFhlM1nbrU8LQd2EzbdvDNm5KUldvPiANKUDvaGjBTe_45onl8Q18KLD7Gj4SWf1vt6By--T-CSerroM1pPycCmUZkAyr6IrxSx5GbsCTE1NACQ3MbyvKa4RrhCLqCVqe-7G6bCO1Lv1HctteSXbAobxlUlWP6oKBjLWPziiancJ0PxaerPY8eRTd05j4_1dZHNoiU8NIFvdhxf918CcLSd6sAf5mgzZUXlsRj2XvOm7wTz6viucNcXjf91wjUHSYtIllBYQ17Qu01ljzbTbGFlBiZqIImK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/فعالیت پدافند تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/134623" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/134622" target="_blank">📅 04:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/پدافند مرکز تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/134621" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/پدافند غرب تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/134620" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💢
فووووووووری/جنگنده در تهران  احتمالا خودی
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/134619" target="_blank">📅 03:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گزارش شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/134617" target="_blank">📅 03:55 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
