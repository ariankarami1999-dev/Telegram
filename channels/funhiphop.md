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
<img src="https://cdn4.telesco.pe/file/ByBnrWlPIdFYs2I-n_8FFJMR9xe_x9krdBhK0WPv9X3YWt2RThVfjkwTMX5KPZg3gu-gFyH3mnRJxWSM0_kgDvAa7ydMiKrfFC0O0SQJXDCd4oySLlAR_YdsvZCY3Zd0gonI57STzowYgfs_k2-w14PFaSqycRVjQC39ZFlfr7XQuFwKZGv-53V7p119d_igJ6TheyF19oskJ16bqpMN-4-Ht9bueqwCPieSFcwFbUCt871umO9qeUZUxb5TyH57k4M75_sMrrp2-RjT3S6e83xrNAoa5ePzoSjoom4D5GCIolBvFgoV7RcflZuwc8ftcR133dskJ9yae5aR1nz8Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 212K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVYrDhrCCdmSILEjEu7H4lCs7jyM1BncH5nqILB3xTm2lVs5YeIPj_oqmR0UQnB3nHlWqyFZprFgeXlfqUzFzT_0BooHGThWU_-vq-a8XFLYK_qcBTJOqbG3jS_9qpAC37ueG43LoDXztUTwUj229XRi9dW30sGCL1pcXd0ANypyt9KByKIfk6xNhqAfKhcBvzCZJBX_Ykzs5XHr8x08J0KeDZYalwsqEhD2SSniUwOT_C_oWRWoUIDlH-kM7UeZzxC2zfrO_B01scOrOZLX4Af9w1j8ybr9qsgYg939h1YZKWQCRkYW-Ua53bq3ssJsjMHbxjzmP5idCNAeNirX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KL4kmO7Uf-pSc8BwuSH8xkrfeO6jL2S4XSLBaBdfkIO_ljUSrd4AyzzzbgZCWJeRuup9jS09j3qlEpqqdOOwT4_L6aP52BOLeu7oY07DKyXpTjAUWEWEthRoyiNCS2HHnRokKVVY8ok33TOld0f42BsFk5zSogHhtuyaRMgrPXb8CGsir84bLsAgrOWto1zgWiEqqC7QKmAMZu6Z4Q3XZupYjVPeTC7pKjmY3xSpiMkzprxThHv77zdqzyWm39UHwtjeAkF4gDf3rEvztqg64YnIYuvgnF5bVh8ZRUO9HlkkWTZvppmFVwSvrufla_SiUK_M_mxZzeaEgH6SGzyXNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3IX4DxErGJ9wlvpnEgF6gQM7WhfzgCI0Mo-9rAI7e31rcrGkjiG8aNxpFNWxmthld5RKX1gMWYZanO46U04E7Q61NXG3DJcGAHNC8ivdFmlS7wa7QVaqcg284sY7RHr-sY3LiSIQmwPPpMuidmYUEOGHUp323JuFclnrCbWSs6BHq2geYpX-bG879wrdkXLHabzHIRtXyJYtvFRvNL9q4EY9_4ruD1VxFOP-zM-GqOPVsJG263JP5klWb095OPfhwHjcGtLnDDPHE3gVb3EZ2UZFPjC1iEoWmW1RXu2BmFQqdpYLGcLxVflKTwo88d53S37qn5Ts7CfXYc13TOFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=kr6r5EVuTpDqvm170m5eJUvVVDbj3ygpe7nfqvfvngZumhl1qhfG4h8ligwFCd95v11yiAOGOyVNQVADFn6E_ZdvvBKkW4LAcgj3UtyJDXQHa3Sh_mFqBpIm5ODY_9AV1Kd0BE4nLm7_2kIZNnXJVPGtMuNSTnjmeRt7G2aDLu-jHTryu8awd-vtHdAF60rC3vadSPpoqrlyM4Ukb9kWE21Z30SRppoYMubJ7GIatSsnpBGwE6lkO2fLkC9AbsOnnf3dWJS6iezjzvxLF7jPTFmq5rLjxvU89Gx0Y0WA4vaT8tZuStzjJOuSgs7_xv9xr7S9tDSJqJHZKG_Ukx_SIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=kr6r5EVuTpDqvm170m5eJUvVVDbj3ygpe7nfqvfvngZumhl1qhfG4h8ligwFCd95v11yiAOGOyVNQVADFn6E_ZdvvBKkW4LAcgj3UtyJDXQHa3Sh_mFqBpIm5ODY_9AV1Kd0BE4nLm7_2kIZNnXJVPGtMuNSTnjmeRt7G2aDLu-jHTryu8awd-vtHdAF60rC3vadSPpoqrlyM4Ukb9kWE21Z30SRppoYMubJ7GIatSsnpBGwE6lkO2fLkC9AbsOnnf3dWJS6iezjzvxLF7jPTFmq5rLjxvU89Gx0Y0WA4vaT8tZuStzjJOuSgs7_xv9xr7S9tDSJqJHZKG_Ukx_SIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX5reO8WfpsQe489OemSYs772bJssRA6I5Y3q02pCiSZWoZ3h-273-gxU9xtRQMlmNkdAn8UlTb3ooQ2RDddV4B-bG2ZmLW_dBMk-5SMw64iY-ahBUC-QyexitLIjUPYNsBDamp-v6x_XPDNbnS3BfoMRXBm-toi-5-AOJynDoNzbf-ZYdZS_X0QFLjMbE-yU4epGAaAUO5bCo4vZAuVLKia4sQqzn_lO0F106rwqLkZEyosIQ_0ozQd-zkJ_D-DGqRxl9uGLycFIVPQ5fGhKQ4bP0BUpUPxMWgKO5WePS3xm5X_ytJgg6qpCL7QnpGyWX-e6cXMDdwagHeuZax_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=IbZdHD3nSvGef5TSrGwd-nJJoGINwDKHH-vuW03c_oJqZAg4RIdohpx0brnKNHzQu68l1v_jNeoyrssZN9PV0DAiLAiMdfXNFZ-8yv0jF2jUaA8XVQfI73TLtelCFcyGe4frjpYduAcWzNIkXcO7G17x78U9sqik4Bs6cMq8hH4_JRz9Acvppmi4cwF27ckRnN7duBABW33S3rplYtlsFRMTBMgxm7DcHCaY5T6ahKGAK57J37VSjn7v1UjbJFryG6DVz46H4AtTcb236QgCMHSCNnpfzwbxVneVLK3HOtsASjuUoMP8dpdkFcO9EvP0RZXYQO2NhtPyCMXggRYZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=IbZdHD3nSvGef5TSrGwd-nJJoGINwDKHH-vuW03c_oJqZAg4RIdohpx0brnKNHzQu68l1v_jNeoyrssZN9PV0DAiLAiMdfXNFZ-8yv0jF2jUaA8XVQfI73TLtelCFcyGe4frjpYduAcWzNIkXcO7G17x78U9sqik4Bs6cMq8hH4_JRz9Acvppmi4cwF27ckRnN7duBABW33S3rplYtlsFRMTBMgxm7DcHCaY5T6ahKGAK57J37VSjn7v1UjbJFryG6DVz46H4AtTcb236QgCMHSCNnpfzwbxVneVLK3HOtsASjuUoMP8dpdkFcO9EvP0RZXYQO2NhtPyCMXggRYZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6dMThSZSCdoKMk3TRKROrnMk8HzikDQOq9PkK19RcV-QP-WsNfW07bFqBcDu0dAHR45ImSQXOso4WroVtXwDmgoZA58PTOP-EJ519d7YmoqjtMjKi0TGQHxNUapGoiZaKzktmBqlQFyavkuMOnMzjjKtB5nZxl3_tykIZj4e18LHWVdNOpAx8cignseJmJjnOhFjk3UIuQOv2Z1Iex2mW3CnQ29xsKhyWWXrs-eZs3KVsDWE-MlBLSkidRrLHkg5IXIr1g4VxoYXnTWH4hatsosImc5mSZApFD4DgWspb2mYywMCOqBtffn3VjKnXSlXRptiByuN7J0CPmQKUOT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQChUheIBoBS-6oLcaQknkSrnWtItuDdHE6_GkOXQmtqDEY4MuTsHIvw2F6yJ-2p-Et64jRkRD8_Qo1fYUI6VbgRHWjCwBqhWYDZHtVbW3c79zzaknybhDI_hqX67zi-OB8H6kWWkFhQZfhEYXQXtl8tCKKqQvJ2oZj956X5T4WnghNTK0BSAabsc3R-V20t61pEtTpi67uzfm9WClinK5K_se2y569MoxTwRh_8WK9_ksmHp9yw1ZCnQdTXh1-3lGDmlMXiR2KfBufQb2oWWtAHh7a8LUTq3Z51Z_NW09ziN5vLMtMyODE6lxaSLxVn1WjnZxVixR-Vod74L0H4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmSRXyGvVNkjxglu-Z1ZQqXgcWpO4NoaD0yFsh7KbQRAKnzzRz2qcDQ1iC8aY8um0d9lJBhClhBS_AsLWnU79B9SS8G0cUW3wSYMLU0iJ50GJ-r1v1-4U3SvYIAvbCrGZsi1DV17yt1UdHQ9Tg3tSIS4wWtLt_KgfcW4mrJ5XQ23IavJXq450G9V-5GpmYPYpw5JgCQalvwabL3mU_EP_ZqkQja7K9bd5PtP27rMNBGCGwO4gvacZvr-WBvANTdA2MVXeVRhACrq_43Rpk8yuRUUVCelpfd58nbcYqk0r8Zj-BN3eLwd_DGkhYXNzPyVEKfuy7S0qyOD86M_af_vcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=Qtrvv9vzT14GcIyX-Tp2etepsSR1p_iGK4rXyZ7XwDbywPR0OjBaTsLdi4c-b6uK8T6LE3pGAN90Ht6RawnFs9QQmPqQ11LaHOI9w3M5MH224jGNEtF9OhPMAMnjr9-FnHbC_KcWgOxNlRS3ruL1rLHeX3SK5tYwGntlQeLT5E-P0QWwuPgJSeXWDpphEJqdIuuzIJIJeFjOgchQUz9ysbrPJKz-LYGA0RDm1GnAAVFkexqem19G_0iOs5sxx9pdnvt3ILSnjuWUvXsvEanFGlHKDZTsRbrtSFnRA7OJ0zTJ6pKTqg91UXnwnwYWcrF0P8AR1mLs58TjixEv0f3kSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=Qtrvv9vzT14GcIyX-Tp2etepsSR1p_iGK4rXyZ7XwDbywPR0OjBaTsLdi4c-b6uK8T6LE3pGAN90Ht6RawnFs9QQmPqQ11LaHOI9w3M5MH224jGNEtF9OhPMAMnjr9-FnHbC_KcWgOxNlRS3ruL1rLHeX3SK5tYwGntlQeLT5E-P0QWwuPgJSeXWDpphEJqdIuuzIJIJeFjOgchQUz9ysbrPJKz-LYGA0RDm1GnAAVFkexqem19G_0iOs5sxx9pdnvt3ILSnjuWUvXsvEanFGlHKDZTsRbrtSFnRA7OJ0zTJ6pKTqg91UXnwnwYWcrF0P8AR1mLs58TjixEv0f3kSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5PeCruKyVXv5uvnHfP7XNi78XXQG3ivmgwsqi3UcseBaX5XAk-4j6donn5NAyf8pl1MLGIpZxn4r9MMDJTSKnO2eW2NOvzVu9C-6FbhBz70fiSaM66UGCmRLIj_JH5VYmyj0IovRfEw42I34p_izEf21wHeCFGt1KGmkNr0Dp7Ao6RI7YGU_Hd1qYmT-jVMHyWw74BEZWXyTEy3rEcZprdmrqf5OcObBW3SCLm15Uly-p_IwImrc8qdWMmLkXAgeq8S7iwQW7_tqkVWT7jyhV-Lfr-F_ae8ZhGgeMF27gqLrYlKvt7dib6dHWM8EbUZ26ZlOn3BeJPUIgmQQuZnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1SNoDbktn05KN-JOe8FOyykdIWxbhRX2cwNgVzOeEH-CCulPXmBnpKHQrjM2Sqbxb4VoHv8b9YZFibJR5Orlq_dTaJ-4oh7DqCnNsdx4Lv1JiVS-rQNzuaV-5KIxSg9ibXI4EimaAxT5yFbxr1vXofcyBaV1nVLEUrHc6PvYfuIUYQD7z6SSaFHOk4t3GtMm9cYEA9ABKpREEtgWuPVhZ06m_rrmGRMxN0jzr5FmEtEQfoKn-szRE2fQa84ZIZyzUPCLgoWTgyEVeEEmdBdhtrJjW2gq4yjfHHWyZa-XVe9BuBagipxD4lnPWWj5yAe8O0HIDnqADS1ABrbIx1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVHbiiPwF3AWtJ4us7fQpsG7BFYVNcUTSvWFzlJud7B1LxOKRJl2WQKPIO2_V2RG_EnIfURlk-gGCW0WqpbB_-vYLurcWs8e2KLPkIrTwP_y4yYw2EjKxKojdTfNcPpfcel3hR6cctH6YYCE77-Pnd0ZhwRPAGJvTSooHgxvS41EMOTsLXtZoZre3YtZ46ZtlwgomtTrr_yp8S_thSbpkhNIlzEbRNzV90mZUFr9a313ZRX9LgubEczf3wxoFeDMI_Qqo7tjsmH40KM4npBp8XxIj4XhZgE6zP2eo8yB4TBSiZxWplAr3hHDFhxZP0nXoh_RXAXypOuYb5qFHe77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9PUjyqQuH0KsmVH8OPLj_L6UzW1rkyTHbEDKt5E5g0wRAshKSjKbzW8XFPtqNMFo9AZuT_3X-xYPpy6VSTA9wowu06Ht24xWxO9AzGFxjGKhc4PSe804vhrXfZOy601pUyyABOehtz4KoGI-i-MLNGfIjOPokyaKDseeSOZByhurqaOTFPsIEtF6c3LAPNVrgEiy0iws0aUNxx-3kCRGKOfqr5cs4YwneLQOM-kX7V6sh-yR-X31HL4RDL0Ghgf1LDcs4bZhfuebafU4o0Ax2YYP9R62UcA1FUEPk10arGhAcwPNCGlayJLHwN41_YsUywvWFE7hD_QxDMySOOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPizIAVoAnzw2t79xZkiz9vvP0n42rK7kVXbvrXYM-mEcQjtrlZQoAKGUyATPWVvPYpVUePJDq8BkcjR3DE4DvhhLCelp5jDtd8JhLUKgRCKbLhPyIkiDPlGWeFfxzt098CaDNsZEQgfW_aJGXb9xWPbpRBppfBwh1mAeJA1eLT5MVe6wsS4lLkt8TDH7wbmSrbq8Ajuha7p-t5qSlqG2VpzbPpjRzDMDkeCBLaDqjVtmZF41NnRJE9dIz4YRDPiGlIc-f11fyX3RDuYNJrAb0Li54fwDpSfDpMl6DXRsjm2eIandCBjAOoCm8nSOGxsB8cz1-m5VqUDbhRHe-fB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYk1-iA6PgIu7NL-lweGzs274WOU_B7hKO7KWOgO2-VJAqXJUmhn7LJqm8bWwgwq1Wv_zz-4-EcuSsNKx0PdCPvEfssYzCStvhdZJFkX4L4w-uWIPN5dXOBlIhLKj2jONpGy6FqUZ1JZkt8CcRdYRKzZyYgj__1dGSQ4ObB4sYjD5soPvo-fQ3kzsQwqwL1Bx65ns4trDus81AsYZT7d_bfw5_arf53SyhQGR1eEoRBfAEjYeooIUNdRN7BCr5WVr9Sc6clnV1wP7FYD18K0cg8KSmsqKFE0mt4WfIRDqN2797AQNt1erTHEd-dM-ymYgyopiWN6_h2Nr-kROwEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ENTDkBay4E6JNNLGMyiJI1w1MyIydgA0akWdgvwBIZyErQPUAEOv1J6AVqIMyo2uiDGNm27f7Zr7zerbMncU_MNWDDl0XK2ZVD3h_PoBgvxCMqvpE9gdATL3_niF1aa9778Dl3FYQXvfIJ8zDqn1o1dcg6C4OiW9sNFJC5rPWLD6hK0BeQLm--aT6o7MRWlabVVwtxIPHyr2Gcqpy8LwugzZepCYMn834cHbbZXW5P5uvUsqS6eQAD4rq-TwBwc4Coe9LkMJXAyKotiwJ5VaVWaxgWh5buzEGaaVd8kbOgiwpBWrI9lBM60p6XMrix3L6LKlxfNWbuRc7Zdl0jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2V5EkxuYfMZZ-bz7rAuy2CJwV2N6xGASwmXE8cs3D6FhwdaEb7kzAuHEnGqBkp0NIL7dYXUp99yP4rjLP_1DMEftT811fQumKEJ2alUjEHytBlLhlCkBMIhe03r7V4zfpuIt4Ei8ojh3Q953pcW9r9mkiCcDSiv3bKfvdth3wQPKNa2Wv3r6jMfQ7m2hpiAUNnikXmBmhxXQmOq5GT04taF5q0qr_GCyWjU5NeBcXJAbt72GBokB0t_I8ATEVFmsgojnpHBExlvnbpQpRkPdUAFY15Qx_x5oSwXjFT0XAgJ8wICp7FTdEyW1WKqfNFdisuHtyV8PN6dIE16oLhxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE1h01MtEAqF8Cfrh_8vODPwmmiBLcC8I_8Q7RFwE49xSY59-5X8loJroZumqGTKOJ1B3-UOs2seXmUOUlYdew0OX6SxhSefNFlAGRG8ff1CHMU0pCIxZDeNWE09kL6XyisTYG62BdZfyHoK4nLgOl0hTcMO_KSd4641P0wJzUnmyGOqHF3Dj3EYVfiaCds_5heLkT8Gha42Suagn9yJ2cOm68p00EKIETJgQSxtciHpHoctbfBgmCGCsKsPnRHX23NuoPrrmNgeXhInETviw-kzrsmbmiHQxmJYd6aqtlS-skxcJ4EyIpL_AHBT_bIbryXxOOI_xApIqdO-Eh8iuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ZdsZtCq4m3xmvrQuxsp9EuFtlKA6C4_ARCT0Nl-S7UPneNTOym86v3QHz7qz9k0ZmgxIxcxlcFlR91fjOMosDVmxmFRmX5Ssja39cs9yRadpEXxZcYiCBxcWJOLGh1hhAD-g9O5aKZDwQcVZHc7QEmbhXHSUXvV7IBJXnl2s5WLs1RfYgCBSct55EPzaK0pYcdbnDYuRmhaTzWZgm6EUYxJDdwIvhM3I-M9e1f1WwNtr7iMTaXpNANv5FLVgJGr_PimhYNaX-MI8vctA8f4xnf0EQExMlnoG1o2XghQMHXbItX48NTqjXL20RBhWcWGDoSoInV38EeRJxObNWgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5LBhAVjV3atjbtjDSWDRAJFr-KlmXTYMOZQ4aLrUpW0GAlj4erzTrq1HyIBjOBfJOcT1Q-vdd1jS8deAZzsiFiKSy0q-bPN-bc2kXF-mCwOLPXs5wNmdqqj6cnteQ7qOzNOT_xAuoGhze6opRrr7qtzOgQXBsWHdQN26YTDSm546RRFB4PkKvVAIN2dPXKO6xLn8QQj1-mYvcnd6V1eFbvpOgaR-kbHiCpSyC2B_QBymfQ4TZZ5-ZvS09tvFEJ7RohUyC-ZO0HYFh524Nh3CO0WUX-0wc9MLOsF4mxI9zljAqPeNiUT0t4SZYxPuNsGdLTFy0Y99VflFveEwvuGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWl2ydOqvsGxPofN9Kmm-qbsHdoIkJTIcbXbOoqWne2TB09WQ5AwaIQZhC0W4172-pbcsVRNdtZW5sNt1qEKQQuhCNFYZzQcBNBEtKGdDOIR8LbqFbICXKEgJMogDdZwg9MhjFL7q7ac149PUQGjSeH5SWPdoj92oNW8gTyBRZxEcGXqKFpU6A7oLIKeHsL04T7x6PohWEzr-UMM-PhvCc0afpZNDLsZRuUg6Oq4td97tuQi1tB-0I4gaCAzESfeJntvlCQ3GgUC_Z8N7h-bXLKPHfBzAY_53jyDJAHPkAHZ-VArg4a6g_HtpRC6kiJJG5xs9PDnuZmDjekV0dIHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3xbSxV9EEiyWnP9H_6HmYJLg7oYAF0wn__S-fqp3oqb0RNR2wq_bp2Dz2VB_N9qLIxq1_Ci1gG98HTTfiwD8aFIs8mFCymyntvt7N5XRQvmfagEAkCHKMQSc_aIrsCr2SplWGElw3OV7lHJcpjQqOCbUsWlOMsnxI2slTtBQVBX1wMLfuCbHwGBG2HuuFuNz7-ZwxGzgFDj7jIjrsnW99dm7h-9lwUJoyWXCZwrt8OJ7hNo_hzK7bHFkJSDXK2_U9UKXc5xygeyTeQhyw7fMwcbcrAQt8wMguqS9ae_4vjVgwMaCXxNDy5_57VCoMrUGUs9ZTVkhp3RonychZpz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9c5-iBXf2wp6s5-kZ_kA67WLRBkmegCZL6xDp-RqNbA2KeM8M9Rgl2A_MboFEeIT9HjTopD3aeysicxq_IKXA1LFSz8XYdGmKWjl3gNJPKAJvtUQtP1I47ECnd2W3y6VxxKgGx7bI4-PQlDqewBpqc6BtJ-D8jzHMlb-B46Lv7khSlEWWa5-IXauGecQicvzC69WvV5mKK_UC4OccN2ugJk96jdpYEp1urEFMZrJpMrWaOWW_sZYa_8J2MJU5JGvBLvd2d1BqDREnAESZ88e2JBNDyhli07Mue99c4ZZ6s0gWaJBBHjPd3DKCNFJJEpUJQ3DzEjAfumgSwazKMRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKuRMg9pxx1QLmEPSBgRqtDXzg96Guw9tXLpH_nV1mHKMmnWyCBP4JRM2EE9HchuKEhMo0j2DSc9XpmC9aCNq_lyagmQsAyDii_gMjPtMZOs7-ejEZg5mJh0eJd9aaW0APGQjObkPVjyHCK_mHEdVh4FA8uk_ms4_w-RzYrBLJJ5WSaViUmWZlWYrlalYTzu_YZMS7-LGxe4dAz_GmcTVU_XhwzIlZTzbNG57IdhrmHEBVAWZCaX2ktSCAvGJT82wvRohlwKqB8iadPK1jmB3IGZDJMBsMADC_5FubUzKUF87S8td1ONfdu95J7gvok2SGZ2iPL52XZabVtYnca1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoKOH4pWKS_dDEO-yD-804bntAKaH4PT9aZ0p_XyiVoM6HPi9A-yb9vZoUDHl4bsPZvk4aZvCUprLDJYSC0MHLS3Eml-1hPT8M7ORBVmYxF4-Vt8k8zi3VPXPzm5yJw9ejg99qBlucQVImsqMeb-75p-7DqUnZrOAjzv2SkknuZ52BcLu5x3bWk2Jb4Cm2k66XE4G6GtfG0VSCTn23l5uFxCKXLCU5i7vdJpdJIwSQuCMfLs5zZTc4zHj9YkTyQ_1Q40lvdXQOS-V_TCPvWfDu-i9HFDS8gyTKoeNHk5503vl1dLMXVXMnQX5B0JfO1QcCF-aaG-zr_-YSJNi9CFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqptJApeiCqv-K7TdVhm016RCjTuvfTp9APapjtSg-IEeePvcaw8seBP4YWT-y_AhYG8MvrHGtv3M8ZiYBpG6VoBoUv3pJ-7ahhER_HxhbQmBktxKepS78rsRJA_-6P0yK3OMgmIdSQgzr7dAYT3o2XGz44iYPV-X3oS7lvAFZsK92L0Q4bxOU4l0WqnY20z2Y6gMMFHyzotHXiUToMyLr5G_t250fZzN3xAFdbusUf4Zbp60t7D2vyGA8SLoBIaKfHzUVj6evAtc5Zsn2th2AVDGIxJ77JkWSg6a5vR7mRriD6wOa3pzXN-0K8qW9lCLYJ7XlWo-Qa29gdo7cOyBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULSaJz_di_4on6BMnvE3fMfAohPqeDAKUbM6zCNVaOnQbLE6Vazl3shD74EP3vXHmm4s1NA1cXlZa4jvJZOMNb980cL3LC_FN5RcoJOKIaMQoMmTxx2xwVMiE4IkHgPvPkTPEAI7sL-cO9dx_aMERXBdFKjSehKVrd5zNabPZ0Ow9gl9KQUNKJxFPeTTYsm495yd2VZWnsbqu0Tu2Ec4eqsZ_1AgKcNTRzMNv0WYzhuAro0C2ABe1yo8vlNIuAOPjWUt3pq2Ihh3nwUZXAlMsLjjwQiRZ4f3gLmFUXrPK3y_Qal8fWADh5b-RGHMeog9SNidM7n1FRdBjSbCGb02Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=Awk0nN0CqG3a5LEE2XIgZw8UOP9evacMdbycGYlu2a5JMINaAx2xDlyvhWFydRQTJQzr1GvU2S5G0OC_3m7zbiWdxFuWwdXKvg9yzeYzJMEryWfEk1t4wuDjHNQXNwG30oI2E_u48K7r8mHM4sRy_pZHCXDX8fYfY6wgC46ZDe3jU7gPfGJ7a5uhvSUxBvEP4IQpvKbn-KEAbdOrTlI3wwjSokZ-eMBOY8pM8WkeiRYyGJsB-31dBvcEBh1H47tsXEqpkepR2PSJ1UzXktlI4WtjS8tB4_K0XnVq8YTmKfyY8T1Ecd09i6ieY7x5eC0wW9SKB6OW5ppJLATf29rQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=Awk0nN0CqG3a5LEE2XIgZw8UOP9evacMdbycGYlu2a5JMINaAx2xDlyvhWFydRQTJQzr1GvU2S5G0OC_3m7zbiWdxFuWwdXKvg9yzeYzJMEryWfEk1t4wuDjHNQXNwG30oI2E_u48K7r8mHM4sRy_pZHCXDX8fYfY6wgC46ZDe3jU7gPfGJ7a5uhvSUxBvEP4IQpvKbn-KEAbdOrTlI3wwjSokZ-eMBOY8pM8WkeiRYyGJsB-31dBvcEBh1H47tsXEqpkepR2PSJ1UzXktlI4WtjS8tB4_K0XnVq8YTmKfyY8T1Ecd09i6ieY7x5eC0wW9SKB6OW5ppJLATf29rQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVxJ47TSocnupcazR8nfKhHkI8m7C0ct_jM0nRIZU6uTtYGg8Vq3VCZTbUjzh_C9LHbFdC4I1Mn577wjRInSfIqPlivRcmLdu8IeRt8lLjMbKDQR9KA3HncEYkT8SQcBWsqGUJiL9xnKhEbYQQN8FGKAuYlby_wDbRC_z9yjLcqlkoRgMQg3DzLYhyLIc3NeN1ouY2A60QRpS5W8SI06dseNO6OlTSxn00cnBnm7eLDf7EOU4SpsEhCMNn9QAEgkZhD_PEwYMggvjg_uS0M6JeWb6wSYN_6jGtU-asIIBMW0uu8xHd7NGMPEv5ste8voRMVysgHtE5RYw9SURVCuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiqbrAJr14w7a9Aes0ncA5kD4eoqkgjKFQ2mFWMfHmdymqUfrH-Z_TQObgnemdHm_ObTrpXYQ7dJEcejLLKITV-wZL1dzNDGM0547pakZKEHvpSjTctlxKi6R1ZbJG8xqRyDNdbSp9FNlGPrvbWjJaUkSez8_UFe1YFRfswIky9Abtby41pl_5aRmA6VBlHmSH2ukNySeWiBw9nhCg9i4mSZtegRcE23ExmdFnZLsU6h8bmuh7uJVIAhYcs308y43OGIPKX0w5SxGFxNoj4LFPyzkihv-W73WwQkSr22EJsgbSEQlawv7KCKe4Q_glrBfBrT70rh0bTn2uzbqH8s5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkcI015cynPKXEJpwck7DF65rMdW-ggRYxgw19huyG9ooq-IYvmfXH9x0-zQWSH4IBibkNR8bLgsfqS1e09jYHgMd7_RZEBp4-SfyTPDma8t68ugCTokMCFjOot8KSdaKUtxYEb9PFUPHKIXZhOg60lU43m6B5mW0dHHoq44FvRUw3Nt7bmuYl8aiUFtLkSHC9PWFsrdrYAip0tN4y-Z2VA-EoIayVvCB8YuiLwLZlSupRVVmInfEG1zDCGlcrvcOXZEX1v2MV1RR6jD6p6qTPxCKAnpWorSUkidr2Zfb-NYPbPesABiUAX6oDalJTXhpb6214of1zFSH3YjPfrMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmFX59p4no7gAw_AcN0kDomBR_LD3uqUGnI-cWI7iG9tXVmlkM8zFdYlLvvnTyPPDG5R-5ZRz9S90q5KukEbYIZd40mYaEi6MYGFunyjG6LTy56_j6XT73qGb5aHfRVwPDQiB1_kQ8GDb9Ad6SZpXzJBBKYIudGA1wT1SV2rIVVquRcFWlJAHmIGXyh5az_GYcY3nitoQvG0OAt9NaB1NvQS0aGs3_1NESuuTBRZizWEtj_z0K5MbwnYDfgkvqE_kZgV1lwVXbT94pDv9wxN0wgnL2hyE8S0PbgJ_6-whr00uedlArAwHgfudWdAIzCP30GVb1_HRIimVDNTl13dDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb5MWkiYOofMMjoN0mCIolRyX0gvHdjGI1qB8TKqD0hQSsidEs0hA1oO7likTMHQ8JZtL-DmUVTIq7oMf7Zp_3INxHgulykI736Va8WSl5nsZI6Lvwr4sc52p4jpc9YdKhpOuGijEPt7pjnLyGw5SUXCkf3OQejSwQ8fvY8YT8P5j06vhdV1DWseWHLG_qCrw-o1qJQ-O9HviaZ3Bf58TU1Vg6tG8OobW65EWElAt5cqnBDu39IF_cDI-6af8wA0EsTHQp_uAZmP5qK4zbV_tBHus2k9J5qfnvYFEntiWhTjbgXwLWrQ8ubm2bsZo9901sZyuMdN5FdWjaiBc2NKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coEBET4TSbJMqmN8cPfjZ3n8ligTv88ctnElpC97Qc8nwpe4UdOIebdE5EckqBL0DStJppUesWAt1aL_0p8OIFV0L41UTKYFfEVAY_kG7dPTtCW_LTSwyboz8QzhJkZUyU-OphVXS3L0Zs4_7IoLEExzPWpKE4Vt1a-hCYlb5I1BT1RX-ProFNJThtRHxzAHrv1MDq241QoCLRRY6XpiV8hG2IKlcQuZDR1rgHMjBdXbRoy6ULnPrQQ3qZOp4I7dfiy7KwtxCaPnK_E2KZK8xPYiES3W7BWG_HA2RxCmsOHkSWryl8TdQmwfpP5BK4pUEX6d3MI6Pv5knIT8alKHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZfBbtiAusoyjMNEg2DK5jYehne0ifuc1cTgwk7pMyhHVE8H8xCIrpnAc0WelsnzcEB9d9BQlbjKRLJcrbuIMRX3an0KAHdfZ-vIRUlUTRTOTCKLYwk6fYnSYO-plQQzvu8TvhtSh_OKaiVurdADIAYrz68OjHZU-zPF6i43nvBE568-ky8XvYieCgmo7xJs1WynM8niVjlsv-R7sxgMSi8BQN3rUQNtaGy2KUYUfz-VU5MSc6xlzCT5wPAJHdJqoSGU_0sFFMSqgqaS1MNaToNhPs1T7X75EfwH8IZ_sMjaXv3rDA702n8zTnNX7wpwq5d5eiCK4LNbFoFhxQrMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9U0OWdS5K9lcwUieZHxlh4PfSejs6-_J9NyFe8h7TSDKavkiPn9al8wZJ8fZsBZsm0jzKKBVSy6wClTbBiYZg6h1lLdcbcFiV9UQypTtnnZKzHAgZS_rEbhtbWm-07fZWOx8kTbXvDsv0buiPdmwjowQl1hl7S96xAMVncPHLCnxiK76mKCWlGfR5Cxui5bjiVbLryccRhXMu9UHcdEC0UnPCW2yk4CSJxEYaE4ODvsmQC12veeAXKZ4xif6zeHegDO8VG6rUgqgBZKGf87CORJvtbVVR71Znru5947RnUgvcEEPtBU8r_Ki5YozcKFQYjWkMoC9PkdRivVd3LBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSOM9MlRTjroftasrQzjSmBANae20rxXXiR-9XcAYQ39JdnRS2OLCxs7w9ZyrWPeyvfMhnb6M9i0v_vSfRweSqSG0Ame6F97hljZhUuUrTzwhDudQrB_Y3ONqPVnL9Hj4qUq4kLEJCkRDDnyCzzbKUuALVB3R3NNDasafLGLv77iapwESa3C_4ugpg7WmV4luCGwxFFwn_9_q6Qvt03Nl7z5szEPFEjp-XFmYTSq3t3pWAy1PKkySZ-EWIoxK-ZO5oO7lUXYpXPpY3tl9kaUZVyW5oN-iYb5yc4OHSv9vJgBYlPgyID1cQ_utse2qUNOfbw_eyhpA3myfOhoJ8GeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAeVtuv0V4J0HNj92EFhzoeMA42zFrsN5lOHMdx1OVG4z0reCudukgsoIrQiePIntn0gN5meQ96NiGtyvwV95Ueg8217uo4TXwGFKOo7mnHo9pkDQqZyJ3FP6riy0jKcASLST9dZHJnUiLfw5aA_qYJFyWPGXCt9QfRcvdawBiYqtoB6ngw0yYfwu8fBNdN8s8JXoJR6wBc2iUFTv4hSCXxKqRjCoOPBd-Jg1m3g5wXRXFfIpdhWWguUd3nMKBUnPEr-_lBC4_WU_hC-16K7fNu3WbGCUEdQq_teSyUeoUTy848vB1r99mEVKQYSHtE-3xeiZFZB1IbOQ8MOM-rIZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnASuUEbSixEqNR110D51jOO-lkCB3JAKITc3xo3ZpOVR-7DZdh5uAAAEvI6kOkcqyMuMw5rM-1TVHRPIrOTdROh6BjQ87lescXzRoDaUq-G6ncQ_FDoYCUIvku3Rq1M8dG0UxBQUnwmuDa0td-4gOGbxrzHlwOFt-P9fVmnpFia3Z0N0MGza7Tz6k_Ie8FWtDLHSjaksOK5VS49tuFYkP4vYJUjgBVe4D4OcFEbshzkdBkM6bWbPOJvd3nlbH-nKPXa012EeC4KukeTge5sUlX460i6EUyYS6zl5busmxPzO_wZUD_twvbDpBQ4shBvu4QysE8TTNMrr5o44XJq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLX_FRbrlAIi5DocB2_lxdqnI4nY7h0-YczS-4pGxfhxZ4FJD6ITf-QFNvaNCqcw1EFvayCuzEkcbjRaQTkveuZ9_l8ybiBKNLlniKY0mhLQcaiFcXe_Jgw-FdT7AjsUWH4-q8Z3uHMKxqetqxdqvZZp6lh3pjfQizBSND42DY0GYG-P5h5nyLBDQHRWUHkPgzEFYtz4EJ-m4URx05buXUms0SjtKJSy6rUrUi210schV7trhaB7Ed-1WyGXfP71HFkasojZRLxbtaOh32Qc-52qcKRZ6ipyBCmoh7sMqYTN6f7tNb3LO_LaIXM-wKtcDQId-xB3UYhDF8clOns4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US50Q78n1RL7k5Vy2-GYBve8yt407xM97O9f5XXGId6wWayA_1bLbZWiY77kE--5da7SJKO11OOOBZXqIEQFBZHVxnHHqmebduUbMtraPnp0SjTshhELFVEPdTzC7CooT8SK50QUYNk7iJejhCPAOEqnmi34evk13JB2Ynua1VvFlLt-EUVD5oqX67aA8rcJ0a8wSW3uVBUmrOKKS3OZttfVXJJMpo4nJhkFL4MlMJDSvCfNp7qjjUjPINBgyJ1xCs_Bh8SK-ATR_VknFZpd-pqAjdvPImVXXaTJfMV7JZ1WR8IAQewlTf_-6amxdt5ZkZcWDTXys7w8MvN5XdVgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_aaaWc_JCVCClODzDY8KEfdudKYJgbYVtKO1p-eqeqe-q-k_j5qJGqAfjV1aGnGQcJe_59nuOp9TmK9oj77us4pRckbNvqoslyvdmSBYp8JYCThbm5mNDKFJh3Ab3hg6jn59LD3D3GbHuk-aBuUrJu5m26fSMYakTB_osNeByDEzBchhW52FJuSvlrjuuqO-g1jv_68sxnp2ftClexjJgvZ4KhFujFUgYVVZB-mdW82991aRCFAdklpJnlj07KEfXTnnbQjwSjEZ9ES70Q5MCVUzKy3r_eVfkW469wlnTC7h0ABUS35Q9xucXZet-nc3Gdw-y1NVnKWxpguBVFObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmtZRe5At1F8LNKye9Q9NmQeDW1RcV50F2RRrMQpqoJOaMCt41nGbxjBCA8mWam3XvhRi-8grA0ILKfiZAzNgxYz0-7LW0LVblQpxKNnWo8ZTLB-cBWYpYF1AkpwJ9l3loLfcpW1BfUPF7Oaob9ta7CGIQl1P-TjE6mhVMziWrFa8rkS_dBLHemCDAMJROuEitlzyjwu-tY5FHIjsbB29jjaEWKNd8lBsgN-HlGuJud3aAwHeRHSnHmpS0s-KjogpbozFbGveSs28X1uiOtRVt3X513feZKJKu79IWMKzMx-IM29mk3QBakrSwAVTk22HR76oykfXGbdV8JIH4FcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLi0mBZSogIc5eApbt9jPEnqbhuAj7khsFUdl6MohJuAaS31MBizwal0y9e2e9CjswVeC-dVXgwwn0Tj8ngwTpCGTHO_yzLRzlZqumXe45XWmhf5XI-5tDQKXtJ_NXrxA_Dlih65qWZqkh5DgSxkAxY7Fnri5BfINIXRYK0Qk5MsLxwIwfrNFR73trgubUSX7_ZyFSIfMSoPADy5Ri2fMLFe5FxWHDyHyEJKY_pa2tZuEcbRbDxwQ7Eb598HgXyTzeTWBSwIPpQaTEeItSnPWLzJzDdsIzySSbxm1lzNPDyk5ZefHFvTABWj9gNfl__HwAzUE3LxymrEZewB8DQyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAeAKG74tVgsZ92k-U1YYoz8kJqWL4tw21bWzAEGJbB9WyZEPSLeE-17nvEviiFVgGOkaMfnVAEEcvi57HFXIrlElkjgCn_OLFaeljBbga0c_qLM3z-0ywe3sEShFKnJBS2uxp1hplPgVAV8eijpZGTY1NtkjqbYsz89yoSkfz3HdezMFoMfhFi8CZ5DguKFjauWoG6ItGajuNaW881IYO-yALYNc9_Gh_Zv3YOldYEgQGIW4jbqd1dBL_gLbiOkGd4XjZrOMzjnb5rvYij4DL9bF4umH2OMHT05DD9QgYwjdTz_3sjbjjMeKNYlkij-O3jnpsbgK9iULtJnLX99kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvHnCgDKgPrgt4eYBZOT-tWHR9pMRA-bq8iEsp7pTc9-tk3jmHfrhrvZ-BxDQZnPNL-0KE593jxBTTFa09z2Xp6KwC04bqlicdtOp_JpGeAZrqivn8Ty2rgRX1xlEPQRwjnZQvUwTbtVgmDVA4d6eNyZxgoqFSQRxTlVtkLkly3vkcHHOgbqS6UTXaP6zNK37iel67MbTznBdLLbHUWuqq1Z7Ioq-qnVKw95ijrpPN3O78CndqUohme2ahLW3gKUSC823G9I0K3I1Izbt5djMjJBq0cea42Fi9nxMAJXuk_UmViQijy-TlTa3LH-JaG3E8s4B4UIDGzQ3DUpOfJ18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEHoE09o3N4DGRHK6cjyxe02gZjvejR5e0NnP03rbNCDalYVled3hnl6BQh7tJOovnNg-BjJNXVcbFhULvsT2xsByFmw-QAmUSZrVcIdg87X1UjwtXOyrlq_AUYWLrRd_dOSwH6Jaz9CoNfov1dLG-658LaWwQMwqZ8mrY3JVJnRpIoHDavhFNlXemVndViHCto5XA3teRsdvdHW0G0tiSXlMJQzJGH-walHTtF0IAfNyE17fIkNK2hMV0_fDmE_Qi518rBYgG9bA9rU2kobAnkwLq9JgkPlpUISfTARazhu2PyQP4GjYrDK9uZG956GbtPMHPZwH9VD0tJn0h7npw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL4IiaeRbYMjZaCVXWyAydxgJFC0dBm_ed3kgpctBKUf3mnATFG_CPs3fb_e8Oj2LtVjKWw7a4JqurAnL4yMqRg7camq6Iy7UaNr0XOou5GT9Hdg1rOsvXe1WM_Y9sASshP8Mp62GBa2RoEflDvg8Fs5NoO3pa1iTX9QhPJcjUU6veBP0eOUcaSTMnezkUmn9LuOb8v3I7iVIHOn_E26A_UTc5SBMeewiN_S7tzy2vqS4bQEHJNilEceJNsz_xsQKtTrZvbxstIquQkYgNpODf6Uv6QsATwnTd-zqDCNP7g1LfERGFUTI96xvnAxOoOvcY4kZ0DSs9lXUNRCQQCa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-doFabujRjB5Q7j0LORblJ7tHmSOGyZxHxroSLvlB24jh9bGYEhDtp3vp1w3CJXbwtSCOxB9pLMCqOf-Z8NG9lV9D7ChT3EDde3Ep3nb2vwTuUCEXfFyGHWZaRcsboZRFfVGH8211KsALHH8QKyWMg06pqRcbFoG4CF48DFvcgL1DswHQH49CMEjVGbUK_CXSSCiZik0FYstltuS3ckknvJYaA33Te2OSv6dVWDUUaV2XV3K5zY1UsawtMSq1WGSLJaVhkjGxRxyEdiQbImSe629mOZbLg_MNwV1U2v3MNkfBDF8eoT-2MCN_qgzyK0qN27HHUWuD-iJ-RlWqq_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1GiVO9quncx_Uuaw337lse4clgVb-uhZCrY400JRgWczdx51TWr7QtYJUbWdeogwC3WgolByZ8UPoCoNwubzFwnsVC9y5zuFiG__JQ8GQQBYkPASQgrkdYKdZEpfdVJMbroTzs1T9Zxa4H_XCZgcnBSFMsYYS16GfQcifidraAJYV0y_MRc4P7ySukqyfBU040IxVMVHtW8KPD8cd0IH180m8_Bd6gp3DHpkClinXh54-bAdEPt5QnwfxqspHSUWcgCbRGU5nELNYn6E6dG7MYcCwEHj-aWYppBxCQBbDcCtQshIGOwJEy98vVuuZOkL-s-XVZgbKKuvMO0KioOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkabE96VmQ2nfFVZkfXDLWjSSP-MUkQy1XF-QCoPN4nq5Arin3I-zp_UsenqTllAEB4PyQORAsm_pmw8r5UJP3bxZ9C-YZfTdJ7MbLtGPwWBA0tMDBQOxqGDlHVmp7KYXmaZeO-bRO0XgavJiWXVs441xjplgpFQnvcvrzhlSETaCdpb0YH1w75X0ysygPzq7A6olMpPoVOQkDqHxOs9XIiKiLoZxxlPU_ghC0O87dktmlTB54wVAqzUGcAKFAz5GslhQYGoivZI9iFtX8oJBRXv-P7G9hzIAJoYofONYhL1evEFprYk9fEVXqibXGXvENP6JCps3rzGjlmioZYKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyqOeyMUOEOwa-r__hQyAh-KAhEFOSpIh67kNZ23Ip9-0z8-Nz66yNSLDE52Qh6OKBpDWOnXmGLURZSuTsqwEC3n-rzA3D3EIKY87DcTWQIuRhNJmbFPCnXyhoPu9EIyzKHpCqz0l1DWyS-hfdngMlMdngd0KDQlrcuhgoDrPBMS-FoaFRCsCq7rSYtK5Tzn73ZmNzPvrwx1TD4SoOzMJPphuJaGrFo_82Br4nRRfLgyN_4v26q59_tM3copiLBv2N6aWlkZa0plwyzU3hUwY5GPBnB57glB2VejuTkGoM7CDcG6RIejSEtCLPqEnHv0FVh-HmwMbqjPgFQBg4nwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzzDwRiJ28qDCrRv0J-tiCOsYePE5g9UB3ENYbNMAdDddHB-ZIAZkFsRmTdh2fGAOGRQGy1FDic4cyi2UD31TV_tWPaq3VURRGAF3fft7lwm3dOu1fyUBzQQ96zFthOGTYGZWhjzq8sBULRqxduPRlpHKq8sxRm_w6JxnrRIS_UQuLrJhivJm68_3-r2XypxBljg_9QYaynQEXcsMrqLOEL-34iZD3gE2hwNz2NCTGT_PtgZ3Wn5fRLhC5e3JbrOunK25rTUPZrAjiHOzxtmfSxWGxWQSRlzMbhWmqHof-c9RQ7adrVrwkIadwfs3IDrO9FGyWQb1Aya_2MREcYUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teKycE51YlwojVc22tSWfYah1gImth8aPGxiG0Vj3e9encgC4ZvDNBsqL8K2lhPSVD-nQrT-Ipbn7VyjAKqAe6BW5lggM-D7lNl4fSfji3tfMfjBulD-EZZ19Nq2NuqbofZtfj_QJ04v2KS_GXm_gPP8Ch8nmbw_wN3UuhbCbLRElHpAewhB9OileQi8pu7ItMrq3YjVSezr_JX9sgBHC3NdnEBz4se0RxjAeijclNOxKuJRsrYd1Pon_fPEmYypVFOrhlQlfOP5avmT-zbrqySq3Y44YRhwHegws7qB6YaBDxDbmco2g7a-gs19eraVtkx-bn2clG52oXAZ6lxjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbrWmSPj7PuKYO_10_2qjI8Ygi9NRzGH3MdrtjdTwL4zRYCpx0574__iKbIAIDk2Wcb-fu51g_fwB1qTnX5xDLfuBImMOqdc1dQmJeQjydStPPEw6mhZyXpn3-mTOhBORg0qDDa4UPMRYxnYYkEgaZFynKua9nWDGKNIRkVfRa7pb9fjUxbXTM6MHOKKRK8Dbt-TDELVnSuLU74HK5V2jPmQn31eo-FAkiv-0DO0sFgBgdd4ToI034LBExegs9vt7ESu3SN6I2C-2sXpqe6w4anIot3uDt0_T8ewNKsJvD4xc0CBxjaFQgNF_Db6wGUQp7PZBoZpccmGkzKrDffCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5tR3baxK8KdiCWnoMERJy6WK0EQn4iIoIt4xvwNWNgS-t4WrBFbA8Y2bYdgQI7PMlpXn4eajR5CCDWaNtgsV_S4jbPde4sB0_HfAJAmHj_rT97baGt23cX6gTpiaCkEA-_7bY4iG9BbtO-y16XoNlo70AZ0Bzcd8SWVUL3UGnOrpC7yxLEGx39swGcwv3Lr3X02cq8Vrq_fGpQIXyCXZtYn_1im4fOpTBbteqjDHfot1yyOh573E2rp3au4jHWI5ou5_RsZQHIpWEsPrLKIQmP3OESYPHmC02FFgnZ61waPz4foXR0p-trEBvFfncy_N3sJJ2z26VpNeQAla-Rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-Hqw4DWfpEs_Lhuyseep_rIA0uBz_nIavoLF5C_tUkroQFpyzdhx57JQ522GqCH_miM_-ZsseLs4elb-fCeLzdqFAe8ovFXjZEj10znBxeUzqmLeJ5MDVeE8s48BQas3HTSkI3pUTMZBP45cNZdmnFNG93Z6uXKvSxVnviRbfRIh3y6vUrlc8lWTxt6QKVVXUmWjqqelzKkJAhSKrNNGZO6GH77uiu_13eYE9o7z_pkqYYnvF8qlqoSVpwwhnMj6xoGwTWs70w5jwJVu50tIxP11WNNLpxSQy3sjR3hw2eGuRaAwVmE4ro0pWqiRxiWkBigPUfHDjrMUfY7x2O_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ7qlmI08iWM9Pyz9O-PDb55pNq84ek-TxEbiPfu1T8ugCKR5dGgBvfQT9OLvbft3FPlWPqpqZYdcztlnySyOj-I0ZtpjG1pQIcVohpsPmP71VH8AO6ZDvHGsyokeAyf_by4uwlv0q5oPzUVTzWhh7hCKREghv_Haes6Z1bbyeebPyJ3bqP08EuRN53SHrjQ_DCrMwrvdZA-JyyllqGQe2ZqiN6HYHx0-Onys_1SSsQPYMzxyRGfjeL3pyCPZvrCpZ75Evx90WVUs02DknKtrIHytD5u18_IzG4t8FabFAtB5VV25C7QpLK0Sd50hZFWDVeXb-B37LrS4sEniNbV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aghfunyGfYKdHs708wIxMNiHJMFqHVhZ9GFXoBKc5oCKN14CQ2jX9ol0LSdyKPxFL2tGIeKd7nWMI2d-4SIj7tfCDuETKM-7yLl4-7xVtbJNwmu2YmGkyNhdZxLIyo7OwZAO8JAQjzV8zcGy-m1CE-IDZeaFDi0p6dJFoVLF87XrNZnFwByqXZZlJMOtgOL70jUKNqUhJMScCgs-qUtHlAf9Gb7OrQ5MrEHMsCerMwPQqLQSqt-Atp8NP51Ed_bQ1_HAlBU-7BX3qRDzlRMMZ2upD9qvHSBSIyOGpvADGOB1PuWl4ob9B-6_SngtOwCPWL5NHLprR5htri-4-wh3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAtj63GFDL_iSIFOeVpX9a7gcXn74X9t8jKwdSMvSZLRoh1JPwb1SKftNxLTnk9ybrk9ZO4Uvmq3L9FDgdMAsIoAQGRKQLalbcvbtHDHkbgrgcNMBwpvA8jwMol15bkcbwHG73sSvPv5rlc0Cwfikzax7cQsRaOU-f0nd8QOfjKgXveA3izFRem_L-p0cR1gRS-pEAf1e_8M0DTcwHx6Q-ajVSlMjCAtg2YND-RcwZli_i7GkxrqvRYFgubCVUw3mzisvze8IuMeq43QaCq2aTWzOFHBgpe6xfkHig6uhgvD_IGedhswkNH9TTDRnRlkzh0Z-mWl3RxFqV_ngc9Nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIDWjHMbYBIjyUM2mZFNMPxtNeBXaqpJL2jX7FR_8esyWKo7EZWjmEhMGdqTsF_IHybh2jde_0t7hG4drGvXVklfnDAgG10bBCb97afNUuT5EO-9kkiwaQ_D1C0MTuI2lc1Vz0eCBmUdiYlWcdwrXWZE9UDjvF-18aT7uhI7p7qwxvy_Y3Lk2NNsSmn3LyOejsahQylZ_NkUG5QJqPm96UECMh7F5Soic_AE92F-J-vp1rVHpO0kjYQ1_9Ovhci7-yZUsE41iJm1QhH08TBBb0VG-TJCEY-LNIVE--Hdto87HVmoTuUdo2c7MrxWTwCYD0DEdINNVraHs0IVh8bjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzvwjhgs0jPsKsS69_wpbCkw5yLAAnCozu_KwKd07Gl8spHGnvU5LU4H1RniR_or8XkxLeqqC2Ch_S-VMthoArDVzzIXJYdWf_Hzw_Sm-IhOZIqvrlu1kpZA_ULJOPjuWD8_VvMzC6hl3T1ZCaUTIvKNZJiQtvWrN-4PBizNc0q5AAgYswxJfjvBnCR9p8MWUa_R-x-r2IsXTO9nEPiKj6acnB4Tow5UrXjEJQwBxTLBkpQPF4gcViyPp8J84TfZAQpDxQWzCX0mpX3HfZvxB9xzSGw8SkwAP2-v3k5oyu_cGIhbpGtcfzpU2U6YTukQex2czP7oZv_2q5bFX0_cYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pneJbrPsbxcQqvSEYc0MUKRQjWdNHKHaluACDSH303OG_Nnk0WVZ-TXjzjFOzMGAES1v1o9QQzihnZVB9gJ13RmoLVMovUaUNiYoKthKzj7GLfAOsM5MhShaUqJs9opFSlZdgviIvbz2NbKggIIIpVWU1Lxye-45sUMNAfajE5SR7gTiQO789kqb64SEcuov1c4Bm_ZwcOB_sxJ-yFYzhzlUJCkUwNuoiv3NxPBtT7mb3q71GfWKmGhAhQT5uwnDGWjop7OxpuUSxZ2rJrghfsiTMohPek63kJfCJheIoge0kUMqZ63qp5yThtJTBveNNN3H0AeWEyZDgryPbKFSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=MB-ZrqCh9O0B7ymsVKuJbr6co0TkDa-6egWNo4a2U5--WhWfvvLoamF4nbw34HYsUOlmx4QVFLayZBHLZtb7Jg-tW01K569HAdWAr5fQfnfY2-ya7Q68WAHc_0ZD38Quep9HZAU0H26O1FzN8QhSCZQRF0nH74NPb0ya16VKoEh42ThtihGR927NHrGJlNNe4HUeeQi3iCouhGgzQe9rN6Ekt5-uUnXHlPZDrMubyZxGB1fDLGJOcCqTFzsVIoLn7HPpuMUKkbsSMYUmS81jh86td0bpRVSFiRABo1nVVkUp4ShDwFnzN-DCfitbxASPGX-AEONXPFGI4Dbslr_IaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=MB-ZrqCh9O0B7ymsVKuJbr6co0TkDa-6egWNo4a2U5--WhWfvvLoamF4nbw34HYsUOlmx4QVFLayZBHLZtb7Jg-tW01K569HAdWAr5fQfnfY2-ya7Q68WAHc_0ZD38Quep9HZAU0H26O1FzN8QhSCZQRF0nH74NPb0ya16VKoEh42ThtihGR927NHrGJlNNe4HUeeQi3iCouhGgzQe9rN6Ekt5-uUnXHlPZDrMubyZxGB1fDLGJOcCqTFzsVIoLn7HPpuMUKkbsSMYUmS81jh86td0bpRVSFiRABo1nVVkUp4ShDwFnzN-DCfitbxASPGX-AEONXPFGI4Dbslr_IaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=TsZmbRrnfGl6cwf__tb49gbCT2zRVzgSj3h8xBZ6yz2pwyjMacs79G1I2cJ-D6-IaKPKvmOmhQGuLywcABZBJT-C1Hzmxd_f6ck06btuRmv0UqmhqFaiSJFxvRzO5k6WCaHzXeGd_6ZNx9xCP3QoNKCwPO6_cKKmgjw3ESfJfvQpEg6hc1Jw0dzsOg8v1u-M97CJcOnRUaWFZ2kpsMdNn0gkFuHiQZE3jQ1v0qFDMPe73ZOFxDDpeZVAEtM4tbLZqqkZJJJuSmzSvyzWY1yv_W6068_SCxBBxPHSzlp5lvRGzctBsypLPx2DOCo3b_IijLuoJTOfaF4Tvt2O4J3YIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=TsZmbRrnfGl6cwf__tb49gbCT2zRVzgSj3h8xBZ6yz2pwyjMacs79G1I2cJ-D6-IaKPKvmOmhQGuLywcABZBJT-C1Hzmxd_f6ck06btuRmv0UqmhqFaiSJFxvRzO5k6WCaHzXeGd_6ZNx9xCP3QoNKCwPO6_cKKmgjw3ESfJfvQpEg6hc1Jw0dzsOg8v1u-M97CJcOnRUaWFZ2kpsMdNn0gkFuHiQZE3jQ1v0qFDMPe73ZOFxDDpeZVAEtM4tbLZqqkZJJJuSmzSvyzWY1yv_W6068_SCxBBxPHSzlp5lvRGzctBsypLPx2DOCo3b_IijLuoJTOfaF4Tvt2O4J3YIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHY38XXUVtmW7tfUMIM1lGDDjW3AG06mMe3sfq6UQdkS27XsuVJvO5EYE__wbdY_sXLJ3WHaM9Nsb-p1w0cCcykNMAoxJ_V2Mlxh4EfZeuUwcJtETRhDjGx1QHOZO9MTEZjKSpx1VIqI7ARAVHI4hd7-m8Y1BBQoFyvtR1IfQQD8mrt460QPfrKbtEGJEHj9E5tjmO967bPNy5czPt9BTWlRYr8FvYF1ozjo65aylqDO9M_hTi2vBJ7oDMW-PNrxlJDgtiRm6vZxNfTDJg9wW-2btUa2zOivYZYFbIXZnPQ3-KBC3vumPqGleDCvVqFva6_eLRoTk92r67ro6BojJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Gc5lW4wpQeG9JhxrdCKyKo0NgEXcTmKTJjxNJzdEgTpx59V1M9XtSxfG02sLFsUKuyLdp03i5UGR6KkscttK5kY2yxkNL6DtbYx2JMi7r-yIQUT82T_BbJ_0ozi7Ev5H5sFCSzTE2rsbD5zhPd4H7NLRiMFWUcOX79mbvSh9Z-gD5fiwq_sVy1tQFSzSiagCoE4SunnZ6hHd33zOYej5RQMwUL70zEZe-5T_hvmXs5jHPAodVhGDgUeCUVxc6J8bza42n7du1gosYPMqSiVNiAg7Lx2UIwcZci73nHLMp7EsRIpg-qF99BrGmgqjJzM5Fu3a495N1HNd0U3zBCPIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Gc5lW4wpQeG9JhxrdCKyKo0NgEXcTmKTJjxNJzdEgTpx59V1M9XtSxfG02sLFsUKuyLdp03i5UGR6KkscttK5kY2yxkNL6DtbYx2JMi7r-yIQUT82T_BbJ_0ozi7Ev5H5sFCSzTE2rsbD5zhPd4H7NLRiMFWUcOX79mbvSh9Z-gD5fiwq_sVy1tQFSzSiagCoE4SunnZ6hHd33zOYej5RQMwUL70zEZe-5T_hvmXs5jHPAodVhGDgUeCUVxc6J8bza42n7du1gosYPMqSiVNiAg7Lx2UIwcZci73nHLMp7EsRIpg-qF99BrGmgqjJzM5Fu3a495N1HNd0U3zBCPIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APrwVzcSU9JLuD0BPKRzs35Q1QO1ImSMh1VgpVywKC5PlwkTqCGC6UCo5-mum7zLl5vYjouFbgKMxxkzJlsylCImW6XFGPvm0eWR2hhcyZ1eHK0IyFAbdOE6Eo222shx4YoK6SVEgZtqcOoMIX4zINrE1MUadHC6EooJnjVXxofz5ZDkQVN_tiM6SQuQj7FCc5a1QUzj6vM7lK-OOCVpFewYcPVLSoNlkQDVeGu0Lancs8-SNbzAXMZNoDJBKYjb6AYVgjBSKK3VLoVeaj3Zh8zxQS0EkP4xtwYurZci1pix81UFBDIjMbfQYoA-XpxFDoVTGK8JldeW_upBlj_tLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0PPMHTOm9hVTZ73qaPLqalwAhtVBv1Fon5lGvIf-4CoLueTlqL57uFShnCEuKDkz18KAHe-h77UtMHYNowoE4BITg1mmRvw-TEOH3GmNpX81SLodGwIbSuc-HNQZ1Qu_Xr58bKAqGhKFDoqG5yFmb5BhgW7TmC-hCQujRyX7VHSzZxBFc0kkORfM9w12Z-vRHA6dI705TrGMyTPoZfeHF0_dcEJHD2R-u7GzCBYUgN3gb5Xv8RKPa7mHFC6LRREVFV5-3Mf8hlHGIMd3uYR5d-BoHgWzX8cZRiLhSSnCVixXkR4QiK7FalLBZ7oHk4iBBnyLnj3a9T329UvSpfMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
