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
<p>@funhiphop • 👥 213K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-LJRWwGMsalhPE5bXPrhhWqwIL6ITvyu9Mwg1bddSNH-rvUO1_O5R3YhkFwkjt8cJOtcwUlpssD5Y_NO4EksndjmI11wPbi63mHywa9FJ85p3D7NtqqcjYzqxJtB3i5JuPkH8sjPoctPyGcStNeLUK0LKxX4R-mkPmr2mGVf3Sc5gZinclWzJwx9VMwukVrixobcogeOqbPaC1Gl2zbkarEJzhdCCSxhIXUdVDX_cze0OLTm36p8FHz-Tet5RpjZsiecy4KovaZMFKYgdeMMI4xyhKhnfDHQlwvGSq5068m_o-FElM592UbgAn6Lt-kbVjsus1f2Ry7TqkeMbHAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVYrDhrCCdmSILEjEu7H4lCs7jyM1BncH5nqILB3xTm2lVs5YeIPj_oqmR0UQnB3nHlWqyFZprFgeXlfqUzFzT_0BooHGThWU_-vq-a8XFLYK_qcBTJOqbG3jS_9qpAC37ueG43LoDXztUTwUj229XRi9dW30sGCL1pcXd0ANypyt9KByKIfk6xNhqAfKhcBvzCZJBX_Ykzs5XHr8x08J0KeDZYalwsqEhD2SSniUwOT_C_oWRWoUIDlH-kM7UeZzxC2zfrO_B01scOrOZLX4Af9w1j8ybr9qsgYg939h1YZKWQCRkYW-Ua53bq3ssJsjMHbxjzmP5idCNAeNirX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KL4kmO7Uf-pSc8BwuSH8xkrfeO6jL2S4XSLBaBdfkIO_ljUSrd4AyzzzbgZCWJeRuup9jS09j3qlEpqqdOOwT4_L6aP52BOLeu7oY07DKyXpTjAUWEWEthRoyiNCS2HHnRokKVVY8ok33TOld0f42BsFk5zSogHhtuyaRMgrPXb8CGsir84bLsAgrOWto1zgWiEqqC7QKmAMZu6Z4Q3XZupYjVPeTC7pKjmY3xSpiMkzprxThHv77zdqzyWm39UHwtjeAkF4gDf3rEvztqg64YnIYuvgnF5bVh8ZRUO9HlkkWTZvppmFVwSvrufla_SiUK_M_mxZzeaEgH6SGzyXNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6dMThSZSCdoKMk3TRKROrnMk8HzikDQOq9PkK19RcV-QP-WsNfW07bFqBcDu0dAHR45ImSQXOso4WroVtXwDmgoZA58PTOP-EJ519d7YmoqjtMjKi0TGQHxNUapGoiZaKzktmBqlQFyavkuMOnMzjjKtB5nZxl3_tykIZj4e18LHWVdNOpAx8cignseJmJjnOhFjk3UIuQOv2Z1Iex2mW3CnQ29xsKhyWWXrs-eZs3KVsDWE-MlBLSkidRrLHkg5IXIr1g4VxoYXnTWH4hatsosImc5mSZApFD4DgWspb2mYywMCOqBtffn3VjKnXSlXRptiByuN7J0CPmQKUOT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQChUheIBoBS-6oLcaQknkSrnWtItuDdHE6_GkOXQmtqDEY4MuTsHIvw2F6yJ-2p-Et64jRkRD8_Qo1fYUI6VbgRHWjCwBqhWYDZHtVbW3c79zzaknybhDI_hqX67zi-OB8H6kWWkFhQZfhEYXQXtl8tCKKqQvJ2oZj956X5T4WnghNTK0BSAabsc3R-V20t61pEtTpi67uzfm9WClinK5K_se2y569MoxTwRh_8WK9_ksmHp9yw1ZCnQdTXh1-3lGDmlMXiR2KfBufQb2oWWtAHh7a8LUTq3Z51Z_NW09ziN5vLMtMyODE6lxaSLxVn1WjnZxVixR-Vod74L0H4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmSRXyGvVNkjxglu-Z1ZQqXgcWpO4NoaD0yFsh7KbQRAKnzzRz2qcDQ1iC8aY8um0d9lJBhClhBS_AsLWnU79B9SS8G0cUW3wSYMLU0iJ50GJ-r1v1-4U3SvYIAvbCrGZsi1DV17yt1UdHQ9Tg3tSIS4wWtLt_KgfcW4mrJ5XQ23IavJXq450G9V-5GpmYPYpw5JgCQalvwabL3mU_EP_ZqkQja7K9bd5PtP27rMNBGCGwO4gvacZvr-WBvANTdA2MVXeVRhACrq_43Rpk8yuRUUVCelpfd58nbcYqk0r8Zj-BN3eLwd_DGkhYXNzPyVEKfuy7S0qyOD86M_af_vcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5PeCruKyVXv5uvnHfP7XNi78XXQG3ivmgwsqi3UcseBaX5XAk-4j6donn5NAyf8pl1MLGIpZxn4r9MMDJTSKnO2eW2NOvzVu9C-6FbhBz70fiSaM66UGCmRLIj_JH5VYmyj0IovRfEw42I34p_izEf21wHeCFGt1KGmkNr0Dp7Ao6RI7YGU_Hd1qYmT-jVMHyWw74BEZWXyTEy3rEcZprdmrqf5OcObBW3SCLm15Uly-p_IwImrc8qdWMmLkXAgeq8S7iwQW7_tqkVWT7jyhV-Lfr-F_ae8ZhGgeMF27gqLrYlKvt7dib6dHWM8EbUZ26ZlOn3BeJPUIgmQQuZnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1SNoDbktn05KN-JOe8FOyykdIWxbhRX2cwNgVzOeEH-CCulPXmBnpKHQrjM2Sqbxb4VoHv8b9YZFibJR5Orlq_dTaJ-4oh7DqCnNsdx4Lv1JiVS-rQNzuaV-5KIxSg9ibXI4EimaAxT5yFbxr1vXofcyBaV1nVLEUrHc6PvYfuIUYQD7z6SSaFHOk4t3GtMm9cYEA9ABKpREEtgWuPVhZ06m_rrmGRMxN0jzr5FmEtEQfoKn-szRE2fQa84ZIZyzUPCLgoWTgyEVeEEmdBdhtrJjW2gq4yjfHHWyZa-XVe9BuBagipxD4lnPWWj5yAe8O0HIDnqADS1ABrbIx1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVHbiiPwF3AWtJ4us7fQpsG7BFYVNcUTSvWFzlJud7B1LxOKRJl2WQKPIO2_V2RG_EnIfURlk-gGCW0WqpbB_-vYLurcWs8e2KLPkIrTwP_y4yYw2EjKxKojdTfNcPpfcel3hR6cctH6YYCE77-Pnd0ZhwRPAGJvTSooHgxvS41EMOTsLXtZoZre3YtZ46ZtlwgomtTrr_yp8S_thSbpkhNIlzEbRNzV90mZUFr9a313ZRX9LgubEczf3wxoFeDMI_Qqo7tjsmH40KM4npBp8XxIj4XhZgE6zP2eo8yB4TBSiZxWplAr3hHDFhxZP0nXoh_RXAXypOuYb5qFHe77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9PUjyqQuH0KsmVH8OPLj_L6UzW1rkyTHbEDKt5E5g0wRAshKSjKbzW8XFPtqNMFo9AZuT_3X-xYPpy6VSTA9wowu06Ht24xWxO9AzGFxjGKhc4PSe804vhrXfZOy601pUyyABOehtz4KoGI-i-MLNGfIjOPokyaKDseeSOZByhurqaOTFPsIEtF6c3LAPNVrgEiy0iws0aUNxx-3kCRGKOfqr5cs4YwneLQOM-kX7V6sh-yR-X31HL4RDL0Ghgf1LDcs4bZhfuebafU4o0Ax2YYP9R62UcA1FUEPk10arGhAcwPNCGlayJLHwN41_YsUywvWFE7hD_QxDMySOOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPizIAVoAnzw2t79xZkiz9vvP0n42rK7kVXbvrXYM-mEcQjtrlZQoAKGUyATPWVvPYpVUePJDq8BkcjR3DE4DvhhLCelp5jDtd8JhLUKgRCKbLhPyIkiDPlGWeFfxzt098CaDNsZEQgfW_aJGXb9xWPbpRBppfBwh1mAeJA1eLT5MVe6wsS4lLkt8TDH7wbmSrbq8Ajuha7p-t5qSlqG2VpzbPpjRzDMDkeCBLaDqjVtmZF41NnRJE9dIz4YRDPiGlIc-f11fyX3RDuYNJrAb0Li54fwDpSfDpMl6DXRsjm2eIandCBjAOoCm8nSOGxsB8cz1-m5VqUDbhRHe-fB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYk1-iA6PgIu7NL-lweGzs274WOU_B7hKO7KWOgO2-VJAqXJUmhn7LJqm8bWwgwq1Wv_zz-4-EcuSsNKx0PdCPvEfssYzCStvhdZJFkX4L4w-uWIPN5dXOBlIhLKj2jONpGy6FqUZ1JZkt8CcRdYRKzZyYgj__1dGSQ4ObB4sYjD5soPvo-fQ3kzsQwqwL1Bx65ns4trDus81AsYZT7d_bfw5_arf53SyhQGR1eEoRBfAEjYeooIUNdRN7BCr5WVr9Sc6clnV1wP7FYD18K0cg8KSmsqKFE0mt4WfIRDqN2797AQNt1erTHEd-dM-ymYgyopiWN6_h2Nr-kROwEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ENTDkBay4E6JNNLGMyiJI1w1MyIydgA0akWdgvwBIZyErQPUAEOv1J6AVqIMyo2uiDGNm27f7Zr7zerbMncU_MNWDDl0XK2ZVD3h_PoBgvxCMqvpE9gdATL3_niF1aa9778Dl3FYQXvfIJ8zDqn1o1dcg6C4OiW9sNFJC5rPWLD6hK0BeQLm--aT6o7MRWlabVVwtxIPHyr2Gcqpy8LwugzZepCYMn834cHbbZXW5P5uvUsqS6eQAD4rq-TwBwc4Coe9LkMJXAyKotiwJ5VaVWaxgWh5buzEGaaVd8kbOgiwpBWrI9lBM60p6XMrix3L6LKlxfNWbuRc7Zdl0jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2V5EkxuYfMZZ-bz7rAuy2CJwV2N6xGASwmXE8cs3D6FhwdaEb7kzAuHEnGqBkp0NIL7dYXUp99yP4rjLP_1DMEftT811fQumKEJ2alUjEHytBlLhlCkBMIhe03r7V4zfpuIt4Ei8ojh3Q953pcW9r9mkiCcDSiv3bKfvdth3wQPKNa2Wv3r6jMfQ7m2hpiAUNnikXmBmhxXQmOq5GT04taF5q0qr_GCyWjU5NeBcXJAbt72GBokB0t_I8ATEVFmsgojnpHBExlvnbpQpRkPdUAFY15Qx_x5oSwXjFT0XAgJ8wICp7FTdEyW1WKqfNFdisuHtyV8PN6dIE16oLhxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE1h01MtEAqF8Cfrh_8vODPwmmiBLcC8I_8Q7RFwE49xSY59-5X8loJroZumqGTKOJ1B3-UOs2seXmUOUlYdew0OX6SxhSefNFlAGRG8ff1CHMU0pCIxZDeNWE09kL6XyisTYG62BdZfyHoK4nLgOl0hTcMO_KSd4641P0wJzUnmyGOqHF3Dj3EYVfiaCds_5heLkT8Gha42Suagn9yJ2cOm68p00EKIETJgQSxtciHpHoctbfBgmCGCsKsPnRHX23NuoPrrmNgeXhInETviw-kzrsmbmiHQxmJYd6aqtlS-skxcJ4EyIpL_AHBT_bIbryXxOOI_xApIqdO-Eh8iuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC6pkVLNRzFLmFkUEcJzWQYuiqMW932Jb3ccitha3tupKBBXX2-afBd6voZ3IPQEYELMSSHKrwZkNdUjBYuisCXKa4wnxgJtgb2h-DqsAwZbeUnkNOGeu8QO1i_wdFrZIIligKrmF1kCNyHo_bXV_e3D4_RFATG35UryBFagPyr4Lwra2D74dNoqqy99t0o3Ki5aFnxIZpz5UNyIpztNPad--fKzZq6GjyfggfZEkKfKCgBnCCkrrUZZGOnLtwT9Y4n1QsHYlQV-O8hEDZmP2x13Y5JD5B9ij7VqwVy6pj-l-aw2tGEeZYc70ZPt1jKMlo9GpfBmaUjT069cOGkN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sls-q9NIXvHgcNmgNK8TYjU65UW-2rxNw6FtVINCtVElFy2LPNvFdcDfXXLeA_Vr5kvIInLMhRm9e070_CyBq3qW1PavDrjHB4osct0dnr_VN2KfKFnO_WhZl1pwMTF5RMlF2ZQOige6TeCzsFK96dms15e2y0WVLZZCICAs3a1OMnkktnfSmd2bO-IlwS76QftxFcAOpd2ADrBoDrIIbY3FIrB3c3QqkWKN7_1XBnxP_Mxp4bKAs1JIRCJGAEMhAKOS6se93bQzOpxVZSkpWjwC628YTehM9WDCPGrEKIlsQ4a9lfFm5UAVdusZuxY72Ok3qEW675qK4Wi5zx6Wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUyqYD4yLBwBGufiUSyNDPjBa0ibfHji0UGxSYRKIDgdLpqXhLIYJCWC4WD5TFyqKq-KzdvE_-9SdS8GGqNaBSMxFPpE5G9zzrsx_j3JnTcEDtd7isfOqV5qyuVqmmTq5dQTl15tcd8MO1kakMwU-adGazWa0j6b3kjgPAWiAcpBFixxSpxs7l7OIKQyhXi_lVmQ1LM9lf-l02ap_lEEhIdAVZAok0SmlPBFbCJqbMQ48AlK7Dtqeil0477LZliVC-EDcsdjvhQzyweYlzAPkNM8s0jKcMFOWXzAzxyAaejtctf66s_K01rlob0AWdRH87-u4KGGnzjIBkZY3RKUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk_YXzmRflcZJKphEf0bg3eHf8v2OCJi2oPMFx9GF4H4lPKsso0LFy3qCb5S7zc-xF32UQpiLGDhbWhphvrn9weWtt4-MwTxaocpbx-C3BVYnRw9U7wq4f0qbdpcUPyJ2XEQQJTpUp6OcpjXR3Zn2zCeqiRiF_34RW12Q02-gGN_pCbxVWvngzpoyu-AEbGQrFdM6iW4P-BgDaiUPcP0v3KnlrKh3qZ1a_DMRDFQAVAjPu4WLt08k_LYGZNfcktvRvOmuV0WIDfEL97DpryOpqHydDPejiVB7qFj6YnvhMPuikpsy18euI_tJtW4umQfQHolHEOELlWrT5CcFH4rOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-627xldECy1-bnvhbgDlBlZVHiJBXbcXyQi_XL-rd1CwJ7eNXLbRmwd1MmLumQOVhSQpAkmwDMoXy6w19MCzij8VCxbjiS5gsnAz1gQwqeBGJ1ad3RnDJ3vygMFL-jdpHONwgLmtEVlKsgxmgKzjKdLLqNEVu0-OumSKURgWmpD9zby_gb_zPmOtg_5gyua9vpcR0adycpAtgmWYl4tGp3i08J68J3sDgDoqdwYZ-UHY2_Jg-OQxXiRPCfWT8Jiu4cbi6Emu_MDBgNX9C0tV0yB4ABobvRnotjNTXweQNcFGXa01iIBDk7zrAMcWBBxT95_JF8SB_XH_3W7e14rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcRZEr-RTMkhJo93AAH_W9NRWvZV5TUQYCOM4nZlx2KrTnF9tEcquDIdb1i1DRnTFC9k_dJ-L2Oou_lP6Xt-3jDgDf8fHkCob1RRRylhUKJwvaUemfoPz_O5Qh-NmrQFS2tZ9T6AN783P8ZIWm62muJhKV117gCL8bIYBH3pJvCWgDZ1NeW7Ey2JKYJzS2OScx0RedBB3AauKzo3JN37YKoDigFAsr4J5Fv8rAq6gh4qdjNMUeAgZUAmA1i8ip9xwuRRBsmWX9NKxN4-56bxLO7pdteiE5TWqYa3I0LbhEmfj15rlKeNqfISHQ0ltKXq7VhiFiAo9nFpjRPv26HL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZiAjbr13SutGSATn33oN_NGFYnZSyAnGICp9sCJTiWggdebIz5_AXaavINksY-NoPwUoYHY-XcVANXNIWhgUMZMgcEbmSkgQ4wOGazsw3VJd6fhkXMWBjlqwDpNrFBm3i1pJsujV1FfDl7aahvfreE239SWwHws-q9Cnp4apOI-WE0fsdjNdV0UxhU2wp5w5XZLGaisMZ9h02dVKYD9ExNmg1t1ebpwJMQvdDYH85lU9Z1_hlrbZWvzzSWZ-3nVoYLH8L8VRyarkmdnvWqxX3KXuqM1MyHpRi7xG9eMrjwS1hTOnBUhdXskYX4STPjz4ssDEbdomOhYzoF9146VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-jdUOf-AoFaAl4QJ2xoiF9a_fT91679J1kmLAb4r3-LUHHY-FXNx1MXnoe22OqZ166MrRnGto9PKZgqoQZyTXzg64GLWieFnqvsaahUatRQxvvEa3wqDbnLAPMJ3zGcIDBAMvp-D8VbRrAHV_sC_DkKazNlx3yvTlyVg3NfzZBR46GoydHBDHJk4yOSrlsLnIIMQEuxCQwNnKTbM9w-QNdzTQ7iLdiiVE1HrXXiRAmS3SYpnWyk0bGMoyhVq6HpnD8LPiWx5QAw68a3RVUhsTv2hkic2HuxZSj45FTFSAenEi3_jK7Z5QhuY36n6-hA8BoJVXv_vVsxal9wkA5k6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGho0k08YIx8II-_7bQxc1eFJ0Q7fQ_UC7K1ECzJCzxbgmRn5TfYLrq500swZU-MXG_cBgQDs476LAnDTyhPS7p7v-0Ss8lvzKeVL1Bc4eZsDX6RUZMXMSc81VvX2v-OEIfOC4XymHDMWcmGiFS1q6_7HxYU3f4dDBM-dWnUc5DCb_LZksvPSZA1rHdQUYe8EoAdBk0D0Fh6morypMll7JjNAgTtz0d_j65trRAhFTa3uONaD9uhOq0k2tW3xy7bD2U-S6hNQrODKl26FA8-kd9bnnfzQSrWNQtdIa66ljY9dYMhSdwZn4CCWNDm47jpbkWAPUJyw3TtrLbqAzo6tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=ki6FkeJMCyBGmdz_5id3MIiOPGNaaDS0dVY8rrwEWFfLjUZg-g-8Gj2P8__JG7ov8Z9o_yEdWqikYiiLMN28m_k9Gu2Wk7dyUS14C72P_40mpyPPWOWDvXZe00jYCiSk7IT_vf97jOG4bK0nJMfxPAzscG5kCc6bVsTJR83TSdr6kqiSPKgmC6N0962ceST6Sc28y_rGdsEijKCPh7oFCCyY087AYow1_YbKUDCJOu4BRdhqMpWIILmjhxJcHAq4U9ANJKGOHKUMB9588-z4zXoRKt7AJMM1VFC1hqFqRXIv1OlPkNX9EoPkzocnM7W2dXZ73s2KtDVV1wD0YBnzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=ki6FkeJMCyBGmdz_5id3MIiOPGNaaDS0dVY8rrwEWFfLjUZg-g-8Gj2P8__JG7ov8Z9o_yEdWqikYiiLMN28m_k9Gu2Wk7dyUS14C72P_40mpyPPWOWDvXZe00jYCiSk7IT_vf97jOG4bK0nJMfxPAzscG5kCc6bVsTJR83TSdr6kqiSPKgmC6N0962ceST6Sc28y_rGdsEijKCPh7oFCCyY087AYow1_YbKUDCJOu4BRdhqMpWIILmjhxJcHAq4U9ANJKGOHKUMB9588-z4zXoRKt7AJMM1VFC1hqFqRXIv1OlPkNX9EoPkzocnM7W2dXZ73s2KtDVV1wD0YBnzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiR749Jd2qNaY4PFJyk4bQUO2EJTbeq4-CEdMrGG570wvb8FqEp9gveusEas8yIVO4w2YFqtKyglQzyrz5jzLNpaZx3WRnHkf6kSZLdNxW3N4peYULE7kUSb5nmyI3avHhAxoKq89BRx23Ct6DyMed6cyL3uLve563Ae3xpiMuQIYVQexRRYZjxQr3oHFOc-q7kOs3BbCbxRXSV_pfHJ0iXZW6_H6RdL-JGn-agL2BdvOBnuVE090P_6AiWZajztfXjzaR6tEHs8_Rl_J8KH_KQwbtARvSyJ0JxxsdeWNhD4AX5oGnivcaTXrhYmKE_X9yjyON6Bx2L1S4ECeun2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WklLd8Sgnu0YyVSydSGCg1dJ4nKUDNeAoqth_3xHHixEBaLA01-PER5SnN_0nuYkG8nYyDsWnhR6djIx0nvz15DcBQDGqx9p8GvQPNibTB8nVx7-MTIF8HFRPuByspSaSyXvyng4fQemQtf5X9npy0b3qmTWr2q218dADeevFrfiky9stW-wXQW_hLh_wSh2979c9JVtNnbuajTnv9eC2u9xjF4tMT3SMpfdU_C0FZeglK8LImqLVVUDHah9k_iZHczym8p2yUohriebM1tBkA17vvCJOLjQJvTO13wN270-10OidRYLOZ_vXH8sHkmGuLo5EPKwyiELqBolQwvl-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J09NFO4VmWIUJL2kRaeOqlVTPXG5xrylwM9lJUt6SM25HRtuIW2dQRzNQgjM1iL7Qn_UpD2g8XgVwypNqmiib3c0qjWoxnNnZTKHyvCDBNqXcSDzI8cnzemj7UQUiqouRGEZ44R0bgo6YTmc5W5EzYVzPLZxU2OFNTY9BN8DjqhKLblSjea0VmRfyFdNFfkigN5cmRvcyZ67RILFBCyYYqB2hoyReHp0jcIkt4F8DH-9RDTXnXlLEWFNi7Ya9RfplpNrR_B808KBsgzatSunjlo00TiR5HEa8mzQ3FYiUcMX27Eb5PYljxy6iZInf-ck5N69eqrHnCDhqM-tCtV6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIHPMyWI3jllOCqJQ6ylTWBkP15d3II-SF1WOPaAATEAGYUM2yZjNBhlR3odRoK9DsmBh0kOHvzwhJ-bPkhQ6Yty3RbZDDs4LBSBUSLtgHfhL_3L68YmUUilUzqNvc79K1xpaCrcMwN-EvWZIltOaD0M1tSqc39mlUMgGc8jcR29VXkgdE_EV3taZ89_B3jJ3X3-8HUywKZ8NyT_Rf68TsuFvluSwlttygCxhbsLEoI_1ipfHh6MFZSkIgedq-JEfJ5qxzIhA6BIshXm0Xqh_S7YSzyT6E1oWK-98ax50LYjZrBpZulsAi_Z8GalPbQkX3OVyzNTRfonFdOGrMrIEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDwIHiHAfN-dfIcXYLctltKZiqZ3XCbzPL8eYJJYrTwtMbaKXKjXnoA7L64DJyq9XIErRJGN0EMNW7AJaXiQWNfHGVzBU2MoVKxl37pdlZroZAuL5Cw2jej0AOQLSv1fpZ2_S_DDc8hg2upgDUaxf3Q1ATr-BO1A5u6Xjm5seExoWNDRjO7DtpsQJGFPw27ttO2vzbxTgV7-9hv0sg4XoIkocrDsjgrzis8CJ9rcpBEd47-a5DFU7_gU4wPni6HLyy6Br8l-SGpYqe2bInG82xUWabNoCTX34Y2sRxuhRTDGzgtXKca49uEw135N5i53LlxBiAYkyqzhnXz2dnL-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSVgIo5oHRwDsPg-PCDefiUJeKDxfcszo4jPat6EihhAgY__6fayvRHYWdEZsndbLWYo3jgVQnmcgLVCBWFA7X3fADOereNOmfJyco0G6msFa5UydZzlrqS0UcOR2DjrYAiJYay8OZHFpBrljI4-V3epG1BsVRH9AjBnPrfxuO-Ms_opoCWFBkpLDQ5Fy6V-GVe_ETcdBZ9H1nc3dFwRRVoYNUCO4dk1kz9zOXwcXG7jIBwF7HvGSrj54nLf0Zo5YgyLsBCkNcKjS1OrB6O_jBGH5hx7_8mk2OfE5HCdDR4xa8OUwaC2F8kYVzL64D5bgnNtc7SOrLJzqPG5AIhZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oibrGPtFHxZdMXOcr-rb-bCAPqVfbvkTkM0VosjUTTW9BLC17kEcThDH5x42sQA1fdBMkOvler00FzbVuM6worceNDMOf1n1Xgvums68zCWf_QGXRmMf8tFppUYuabxtAhHS3tOA1ZNB5SGox8oYJTLgXng4InoW_DkwIvI3c6BXEhRTAUqKp4AGsgDEhFy-mB4AVp-AOVQdtAbOH6UB-vxaZziV3fDXoPNSaCrkFNHCkDUVAK_Mc6y4hzJed53xW_Sh0ULkst_gSSGQ8OhgpB1U6LuHy4dAQzZs9VU8ZvDEn7xXAClaIzqTkj-0KyBtEuB4a73b7F9UDs6Tos0giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK99QfVv1BzEz3HH643KknD_iRM0ECMoNrb_Yjc40YgYWjIGmD0C97e4oMrueEfarnebasai1pFsMBsKcBl5AFWlH8AXe1WTkpXcxx4NZuFQw2gj0xwELprXBdERvTraJTypn9sPTyKrSkhuH_5h9M3_-HQavcZ4LJkHOfgWO72rA36TebPexk3FdTDP7Gq6MhaT1Thfjrcy7CNshVaKT3V4KnGQX323E9JveDZriXSrKfiyPxI1I2RF9MxWmQFWb-3503E8-OkfDO1YHKRS-qq9DjueO4viswFbsnIwngwOS6bLikR2ueTrjL1_D5WA2ImzfRWWSTaYQdE26BGltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoCjE4552Ka7w-d5A-gcWRh2VW1kwgTft20MbNlXR1X-_w628bl__pl9NLgHKTUZqvE3abWb7gqFC0t9S92j6A3iPGBTS5v0yZg9imCHlmoQjSvH8TTLLf5jnqmbdPCVXubHf1E3R7ELXrEa1AiaNSKF46uDRbcx2qigKf50IFY05xcCzny5uqxpmZTfb0JacxJR06vlC3mEwd8re2Nv97etS1vpJhOwL5hFRv9iXQwkcw_99SEDHgsi1tzJXhmTRtUPWKpYSWwQ0X0FfPTb7QGlECKi1KdOuCoLJ-r-I1s-iPh262lMI3FRygLUMzF6T1XVPSlCsIWfdxJ1YbNhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyCMdL74dgtsaYcaCfGD9_zneqLR_xWhyvrpqx7zxJLR-dE8EC010aZ7hISxpVH9tkpESgOdFDqE0_CgC4W3Wfou2FzeQ5Dhkw4FIMZ5bEruP--z-GPlWD_gtecA1aZtoMaORkvK9dAFDNSZC68cRJfdVZ31BJxequmgfqniCvVVcE6X4bysiD258RE8TSZA82Wr8tQ3Xxit7C322qA9iyFV9Dm5WlTaYIHn11l9MzXonHEq-_S8R3QFK_E9Wlo3rbLBVzJ_OHvPhQhVLLuQVmQX6y-mKdyDK03EHvnwSCxQ-Ux6m4450_8Mj-R_K1IgAUdqpNfVxxVrodP2aGNaEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGnlYcd59CKOFBpsH0RX4lLYhKRuknjYrOMlnGvTna_D14Kkmb6L9qg5LTkfJhvG6dASRsKLGxgX3Gk-G1P9VvZzBhey7jbxCf_zGGXneTl8nYqymxpuVGVM_IWkm6cALdNa1AYkOkCmwnU0LGm_hq1LjTEoCZcpa-sKjdOoQtPBl8ulHu-MKVnzMaZbw4MwYRT2Hh6uVqwlMvnYGVE3bKP3r7cRUJnIa8tmaTPpykYCgDghe4HsQFtvmHJNs9lzgrRomhjoqQMglW9vQvpBf-vmB9K02CKO21yBwqyfkEk124Y3IS1WxJAhLf2XhsxewKyqt7oGbiqTPexVrczGrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA2vNVkWddAtLAbQCAsEqwy0lky2SsOertrtKzc2ZH2iPU4XCx5U7pYGPnVgUbl4JMSJAY5V0_reKHh3ZBCC4b4m1g8V9c03bBggmBTs0dw5AKFa79ML4CARwdNseIyvlL9kpCODwb3K5v7u7CW9rHUWxbV2HuOUo5hAHIXD5M5PoTVeqwc_M4fbOal0WW36qAVli3804OHS-eH7_LPM3oBayPrGXA6Y09CBcKp_B4_xQfEqm_c6R2x1G1aQtvKpVTgl_Ahww_D6mLuQ4Ojh4Njjbp8tiiM83TPMIUUr-3EAtET31W3gZUDSLxF0Xyp7ucaEZ-FSnuPat4Q-WAst6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPUKM4Yu-3as1hPrdHHuJQ-OKUOtpJFvklwQOPNm_ETOkn6GMD4DHIZ3t8TLCchBGxvs7kOPyE_dLLMvXRK8jwXK_yuW-lSJC78qXJyLWW3QfCYATFJAfm7gdFVWuCNHrCst_Lnb-b-cesorNlQ4sgC3iiCFlAjvAlf7ZTjgubPqDPqPXJ1MvJVbIHh3TyAnVHY_A4f4u8L_clKhuleeMPEHs4K6heHBvkaeuDxujP6r-kA0M0z4mC5CX-8UFXp3Aurpa_d8GUmlPEIbB7SoS1ZfSdzsGGPwG_aroXyhWU5vBqFwNvEBfKZ3KAJ6zQvAo6Q6cOl3vnFy1Uo4pd6sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=W5AWL1hSMjaJDrsEQG07z733Ys_8fCPNtNFCDdrnUEt6Tite2LPohuab9QbPNiKPsXg5JwLulJRGBNAqSqrv4_IqCW3ILC3FUDDYQCD8BmJKiIsRyMHwAFaTvUC_ZZ64xX7JzWBXuV8eYZLKuYGkpqhdvF6Tt4UiUA-euRzEWOSp1HJe0WQXEghhZDZVnksjEdDXG63ryQmQjZWpTo7DzxTT5waCxjM5hHo1vcMzh8UfQhqJk3nNbIYHqVC7iOiWTkbwLwZ830GHMNNEOAhZA0BvFH56vHePSMg73KfXtw-EkCF8od55bcoD-1w2fTDP57-hkRmZECjiGSTC1QA2kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=W5AWL1hSMjaJDrsEQG07z733Ys_8fCPNtNFCDdrnUEt6Tite2LPohuab9QbPNiKPsXg5JwLulJRGBNAqSqrv4_IqCW3ILC3FUDDYQCD8BmJKiIsRyMHwAFaTvUC_ZZ64xX7JzWBXuV8eYZLKuYGkpqhdvF6Tt4UiUA-euRzEWOSp1HJe0WQXEghhZDZVnksjEdDXG63ryQmQjZWpTo7DzxTT5waCxjM5hHo1vcMzh8UfQhqJk3nNbIYHqVC7iOiWTkbwLwZ830GHMNNEOAhZA0BvFH56vHePSMg73KfXtw-EkCF8od55bcoD-1w2fTDP57-hkRmZECjiGSTC1QA2kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKwMEcKbzlPBgq_drceqw0GG-ZUYWskKLCU8Nm4hM-CQkVIsxBU-DBht1aaNdE_8PQm5vVPtlYO9wgGs9ShhiLyia2Ug1UfBfJ5P0TDpzuBH6wdbAVC_I874FCKTagbWzIyeAaR5J-Cw-nOZirITWht3waF4k5lXqFIpmMRrvvKppddBBpzEYoIuNDBMwhiDVsfmfLVGcWycT4iDeX2te0xG4ZBdLkrIDh79ATlq7RgGFmT2z0ymsdFrY9TVJc5M55XPxh-Zb6pA4O3AMlhxVD416vhqrC08eIAE8J24m7mwqPDr6JDOWCg5cYwBazK76TsvQyGapxanuWv4K6-ytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN_r9YuB_vWihsqAK28Kq5xZDeB3YEIwqEpwa4U0i0TW58f6WDpuD_PMybsBm-nMLvDLZkrvUOoon2R-bVYtU5VnzpzVgltHcWBeJxObYO0kF-XeMGKETkOwSTueuVl4ekyn3PMICvQXfuP3VhSupUEL-1995zhIg4zmT-lu54_JoqJgsm1UXkZyrsYd60fOrAUx2eua8aYzN7jeKUTKEDUMH7XdtVSayWz-ptXXvnWTmLo6WQw-mSLdp9fcJ03vNormRFvhXedNnoSGXYO2-XETOTsEoVVZZBPJz5nDeF4vGpghYxVTCiGkksVyDcU5RLhGuqrD2mE-XznNrIaCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heEyL4cc49iuMv1QQOQSX3g0b-htdUVLApGXcaF-j1xY1zcRUuOzWHQbb9U_nwp5gzTJ-6oqHKXH2h__ImRBZS2Te6cVSG_yDz8bWnXsGpVcoEkCIm1NJJpIL5XbK0Eq9b_y2VM-krDnyVXSdXDMSrtVKCV2YxCyNndr0g4G03g4Cg8-2oVP6N_SbLsUW7KlStVfxEwMYiWrt-gt_nbuw_BlgkID0wLBy9Mwz5BbadHSa3L4D_Oa5AUHQjZtzRdSzIhzkLO5TDAr9ZKXFHSNxVT6I5I3GVUcmC8sWL1IcKFDa9oOdelRzzoWxlyY9MifhI6ivWrw57PR3J9csVUJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NET5rbzfzzwDlinakK7r6CPuXSbkIzSt4LM96Vrll4xv3oohKlKZDXbLaGBIhTzCLCVW2DPGOIXlq6W8yWy1nFWtnp3B3bfnjznXOIYxIs6w46RtWtjfTnZ9JmLbViEMJyLb8pnAbEUN6pveowKTQxpj2__1MD9qvNv9k2F6InfBzOGgCWBol4smM7Hu05qi9d2FZv4mr5JJYe-1IDO37xa3x-iQQAtM7mnqKYn2bB-spywFdkmLAOFqIqItaiRC3w0KiUxDVVECojqVH2LOjpZiOWaq0ZtvdVa1cavR4KL0V03ddC8MLdJ9wRzuovhfTa4u9HCCLnYh-Z3-6NJmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLCqHOIPl1DFMDuH8LU58uHhEFvJrk2ouD0Fy-yN92V4HdDnWnL15hPAKiTsr-0_49zRqlxVrUjaIo1VCZvgdXl29WVDnxVMqGZHLo1FmpUSM80On6drl43ykO1_fLPbHuAtuM6VypGgdS3bgIJRNIlwrVT1xYc7gDiRS8B0YCMhHI0Y8Qvf7IfN_fs5NPTmsQe3wH-OXGwwv_WOhGCF8FdJZkk1gCQjPfFP00WYcHN3lVJmJGO5mS5Z5iXUy7jAY3_W42Z5-egHKmqXftC_HfaAGf8oT6f-m5xdeeujnWbllIIWpv9zjUq-begpRWz9rIkYsCEGgRplLGKZvLBIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/os175e20XEYhWLb3omg7HF4NcOz4p80W2L0UFqCjoKZ57-wEdBnHGieuAPeBXQJODv5-NJIoNzV8qsrd97vBcDwlf_aXz9435lKlOECA8IiVNAaarPwQF8VQGFl_M8-VWsrP9poPIQH1zbgSGXMW3ue2HDk8J73llmqucQVvhw0ZMSPIf2F-iM9mNriJKQyUBhS0RZrYKvGOFczEO8QcbYaEZJpv5cIKeljqFZQUwMe9GDaPDNjqYb7qurvmnB2dvIqEDvqrwdqoT1A_bXSVrXI6bHaNIDA2qUcQP42MNCyOKF_UcvZWgHOSbW26_dO-CP708hrjbAup0oo7HlTs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBN5I5SYKEfXCFlWkhK4IGdWb0_snEDNpoGD-swmV7f-TCAPtxx2qraVEUuPhCliBSrFezY2tT5pVRInirKg9Ft8d-wB1VPHsNi-hTBq_3aPxoIOKo6ausgT4ExjfA16r9PBfskdE8FXuRo4IZl5TrSCaS0juHt66V5EFQeed-V4dNiT-RDTF3BOk1j2tpUjR7Z0jElpfx9sY9C5ZKG3U56rSZtRKOCeCTWzFO50J1bywor65My31d8EDI_VPkc2m036UuCwowYUj8HxmeHZV561bayGYLUXbVYecObN94b1YHQQybqJuWE510ToHNSc_8nOA51VpITPvTb-NS5B3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qksgla3yqXhP4rcxaeycRAjTo9pm-D90sUHD7g_uNpCJATMyyXDjbnqn3iHjn0LETyDoVqbnwZBte2AziolmJbVt4IWpZwAFhMMycYo7wKP4SxJxJBAqtKURoraFX1SD-iFIpA6aznCr6ja9bCyz8MRMNHOg0zfe9r_edNB0XBY1uqEM262U2oKqhRuS9AsDXwWqKcqBTZJgwJVlyBDImu65ZGEZvnAjvrIBfSDYid9lXdPw95sNVNlg2tcdbK-NhIW2zlYTo6IfAV880Dl18zO5Olp7v-bLiyCkm5t7JM95g12KJQTLrYbA5ph9PCI04n6DteCFYEBX2a4OVbusVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJlQ9qhNdbZ2yO7On-Q7FMD8dWTiQbAQzHzuzjYztsKzrJoNiRl-dsTDy1jjfF0npQO-Sa0KudgH_nCqTEhLdmDe7yHHNBf8d9WDfTDCCTesu_ql58rEqj9ZxMNXF0LMsSjEMKd1w-6xW-FK-yudrcSTSXg1k_bjnEEv2lhlJE-T7YFUsxPm76ITYaFoD3gsNZlV3NaXCemyQ0ls4ht0kQ0ngr55AGwMAGfSDGcExE6lhniLtglZGsD1iaqlZo1Q7k8_pg3qNd0O1l61wlF4EuBAA0JvRnROyfYHXfVlbU1g9tMKRwwLGc4ruqPHhL67gFkDJogIVzdaXhMNAcoYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlEXIycpNIl4MzQ4ar61FFPJpinvBip6aBS42uXyERTqrjJgjD-CBZKACwnB1fV3v0h6K9X37TKJyviupikXDSVnhPpYu3nA52huIbHzPMqr0Shp6Fg1qobivJH2lA-cE63FcznZsynhrDTxzeW8kSvOY9lubtfocDihFREeUlYt2uxEUL-yxhdPFeva30UpHAaKvHDfjVnebDflVEoNxzG8OLCkjHpJLMqbtr72F0dpT87b_RfiwKYnuzUXCIugQIWPU3oKX-NkNElFulc2wmYgu7h6yFRZyxhEJn7XxDQ6NKhkP1xUxfBY_CTrLvCdCsVHoD_9Nwu-D3YhvykTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTU3TNwrLkWFV1faZTl9itxIwznlGVolzwVVzxCsFbPddV7HCUPVHOLdlddctXLLB8lOUpbDuJvGpa9kQ7SF-kVFrUTSMTccupzZJtuXV021YBzkk2Pq-IG599Kj3D53NYonGdJgI-lUArTcz55UAUOcZwepvJvMcF2_mXbmc_Dqhbt6UcreffqzcXG_BEL3UK_La7d7r7P-TYEAfKKvmt7DrZBmlRZbKIP2BojMAtlJUUKSfz3Q2V8_4YQ_yK5ML3j9Uv3YfeJN1WGCO7Yi-jvRVG9zeZOHeuY2V8VIEri1DEsTdNkz_8CAnKi3m3SoBLkcb0OxJ0RIFntqaWIncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbrSRS148NptQJoUlgLBFS6vATR_7nfCaJpHK8IsBmY53gQSjgCx6fBUJM_s5Aa_4fn58vhMXPwya-Ign_0A8klnKBEMPVPRW-s_VUf_7SB1kSZlgixVrAvn5tFuTiANAdVRVpWIbqNhU-8PTvBf8ZnNYqWHssRv9FBMF0_d1Q-GVlqESBo7Hmke77JPGTkGgoi0GA_kU7kImzezS6mxeJD6sNd1fjvaOvJe042mXoBtAsbbW89Dp4Ac8gjW7pssOkYttreH5NHYlyjQf9HxWIwhKTTeqOW2paIutnSeqsSX3oNWQZNTHDpaUp1Hdz1ds7EtGp85wnj5DMKVKf_byQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7EPIh7Ewq-q78lhnZ3m0b36GbE5rRD6xLzXmDmhet3fNh-4V_HUS8GEH7I1uTLoNHT-W0_pIDtYUV3wX1p5gXcyT22-2B0RV4M_O1eTQH_lbT5go8dH4EEFBm0B2oiEbP3d-UtQgJ_-rmcm157emxBcxvaBpsf8EJE6Enstl7RwwXBIW64o0d6mevimGITWTqwak0VbTnKGT0_ahbOe7rEV8wZa0gzXl7a14N-frKSgF4jhPEz_iiJeMgwVyKc9oWyfU-5RI95yekKQ7CjAMsxiSi6X-eGAIha_WB9Cpjk8tvUvDN17DybKfVU2vP2rJvyjqiaVOsLzzs2jy5OeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8IJIo8gj7_RBwPC25bgxQ0IWPr78avkHHxEy8L7lQcRviB-CnaYDq32yNQTi8nwQlEwEuM_p4rHunCa6oc1Q8hZ_MJbxY-VEAE1dA7LmeQVlAQWkZXlfCu5O13J1OQ29eE-zz1u1h0WJZhn8NB-AIaroO0oPmuCUwCTwtEQRXC0FIV_C4BNjgQvjhauyOivfNYAerEZF4B-E7-tuaOu9VJpxzRZQmt73DKlrqgHlXAu1MImAD3HkQ5RvfU5WgRRrw_QlJnMIQ4lF0REflNMjnTTyObLA_sai3nQVUicjU4Dz4p_q14ktWeeoJOtZ-8suzNevHXmUEsjPmcn0XNCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRnIO0AOgHN1-JBvSl1yAKs77IVxIBD6R6Z3x3gdFU-m9q_4MlzTJm7AGMKIhzxT_-vHtJLDZ_TRCv-WTH5pRvKQ-DuOzxCQxxl8AUH9YVF33bqce27jRTiM0B8cVFgZASN1E6l6s5WMcmkkpnoFsDswAWkcNs9t8Qg8MU33FxVBlWMmBGP6BnrDFs0KoUUxZTyrueKq2d-JE2603vDtp6ECDT9l31Wh4AG5OAh4wcjwimfNwKBNh9jt6YmJ1qF319FPjCqEE3wHVlsPg8LWLXVL-gZq-MuklhFcqdz868CqExdftMEB0K-gU0hdIZKVwHIjvmfYtcUmQifTG82_AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqzjzdulyYo0-bHn855CCQ0ebjmLuInUlDtzM3xE0lxrtNPyHGHNJEkzgvkdzmGwzaj-QIwvIp-G5P9B6I6Bkv6i_Ypx9reVoWsa_l5TmECjUeOXP2wVPjhJY-z09VyvfUagDut28SZO1QNcnxx0m53-5ilpap7mXyJY6vpKv4cPYc4C0PonzDaJ8wj7a8uNd_ncISb0T_uojRfrmu7J0H2SfqrgoGteL-3m_POxTFwsEj50JqB5DjArWOSrDShOCQTbiubvC-DPISsFDaiApVNIBkw1iZeI3OVsVZdG2NatP1tr0U5MhNagfarIjQQfE8P3ggm_4zfeyr1K23v6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG7fAfnNjOsn_Dj6jEYHReVD6TCoDhORzcZ7UfvOmgQA4c0fZ8GLaXuN4Jbx65h1TX5fZo5wNGhTYa75P6NfTvKHx8qQ0tUAldD-jt5fodzyaZFi8B5xohaPZmALxjKsZ1nV4LTBypF1dpDj5sNSXHouDq1ZvpMD1x34crEP3oiVBZTGvxxvDxT4dHJwA7Xc1zFnonhbd7lMzqxrcM3jaKIfUKw0iY2ge6MyaDyKEsr-NepSjnPUk8vs40g2JU827Mi1pplM3hIoV_RPzvouRWB7ZBnqZFxGSQ94pKP-DswJC4I5xELkzlguBOJNjwyGEU8zg7teTXv1MGHpb4NAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxOwEraJ5F2RAR6FavCzy1AMKVdivPyZI7Rp9T_fxswHWYD-OmxSek_WBzWVfUISaQGlxjkJ9UdSDjlkwPlxcbCi_x9E55n8QI-sXQ6KsRrDVRG25bCv7OCVDFiWV647YqqZwsVSQLPRWC-Dvi8vJb0StvxcHNcnDDAdeobhbOB-Bo289CNygPRMDmS-h_dcslkRbqlUyDDS461k0Gd81yCnAQJ1S1MtHSNkyPLpnx-YeO0HQsVKzPjuQFI5C7-cC3cJPMIoduvPL57f9I3jz4am8zYdWee3H9BfPDpA_AZX8WvKYbrunOwqkg1meNCSGjFRRid-gkPR3aD-lz-xpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5tR3baxK8KdiCWnoMERJy6WK0EQn4iIoIt4xvwNWNgS-t4WrBFbA8Y2bYdgQI7PMlpXn4eajR5CCDWaNtgsV_S4jbPde4sB0_HfAJAmHj_rT97baGt23cX6gTpiaCkEA-_7bY4iG9BbtO-y16XoNlo70AZ0Bzcd8SWVUL3UGnOrpC7yxLEGx39swGcwv3Lr3X02cq8Vrq_fGpQIXyCXZtYn_1im4fOpTBbteqjDHfot1yyOh573E2rp3au4jHWI5ou5_RsZQHIpWEsPrLKIQmP3OESYPHmC02FFgnZ61waPz4foXR0p-trEBvFfncy_N3sJJ2z26VpNeQAla-Rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9vuaDPtNm3p0E3tHqrFsD5R4XWqDP5hBtY5WADN-AIYJ7k_7glP06bQsVkT-bm_oO5ytOEVDyD1LC9kjRsdfwLwr0yK44j9qicOt-CHeOOe1QdaSuQU1VAB2bNs0f_KVfhUQbaCkPyJi5-x9yaSUOdh3DnA7IsIQWW_BKE8sYbCuY4jDKQPuaEt9jPXmzk-ZNl1hLAtxqMNQ0yXYieaEYD6QbRjQRGDzgVRLzFiiUhER7BzUnj_G8F0WWOaN11byHjLotCQKXyX2JkDZkp8ZHbKbMEFqfkdVSkUq9pv5MmUPHnA6vgv6FSXmu7x03GyUiTpInsNvtMksg2CxxKISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ezVVDvcR6y787jjroFOXUMpe_pGX9B9kxLWGapIHLsXlsidFzs8l8vX2p8-LYqx_1W-JSd_7Ed8GrxehsHC0z_4TaehghxVgpzM59Z-OuraB9SyoSr2HRJT429kUpHFXU01wm2iOsriD9R-zZr4X9dy1uT90v1XMbGCWtCAKIuQxau8Do5oZPtH_UeYFovojGkGgviWwfo27_9zmgFIdcd_uSF1Q1-DizDmVkF3RViSzblOENt0hl03dWtpl182KKPrmW9EqzhirHFLgQ0m1OLAJlz5_Uztysm_ULkFC6ThrL9Zk8wwAdOE4M82wxPlSBhNhUwycJYHY9Q_jO9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rax_D0nN-1DzElF1isJxKQoL3fFzgHmNdWAy0JzYCUQwH3gt8BOgVn9Vd0e1TyNqrPJcPurTusQOtPNqjInIdmY-_NVdrWrAJmUkoW_YJ8mtacX67jmpA-JX-yZIuCq-x0v4tsBEeossWS8JTLrhLm_yWeMPBZirj49hI5mDKmnf6ZEeppvDjRzsqnRPpw47tPKQcW3eT3Uj7zpBVR-vnzzYj6kAZhutrMNFf-gaR8mOgOrVrlz3x75HkJIZ2iJz9Ll1bLCL24BB-sAILcFwxvLdsZfLvLZlkCKhVP3aoGYGw5AtN0c8TjTYs1dTnLDp92RE7IQC6_ZifeUANu03Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbi9AJM6RL6Xr2c3SWAJFZH50xCoK7g4RwpLYcVRJeLJMm4NDriMBbKD6n8wp4Sww9GrV_s3zbIOT4TDK55JmkSAvEF6BF8JHNCU4kfTAISkJ80iIhJAt0SyWZCrCN-wB7ySIr5_jlfJmQKD_xlE6chDJCFFjqX2LEaeKQamLOZA2iwdt25hmmrov9a_WvHikgzrQzsf4NXahn9U94y08jjSiTp2mv_ykopYldmmSLwS-xznSrTG_cKhGUeuk2GGraLDjWlFKEVjbTiIFmieAbmsBzOrIQXqeq4fWyD8Pfyy4zItOPPU1QLNvIaggOYWxqsG2g0Oq9j77mzHEIwEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qc7MpRDZ9LkS-JORECrYmi3MEgkXVDAANNGpTyfgS60vYATJEAgJ3YywG-3VazMFyYt01l5ip8iioBKdw49gRtyF5Njxt2EC4rHLEhJQXS1F24_Bk82Z-91l92rWWRhwoM0VipAvj-rOVKpN9QD81g8ERhxKtHgWtml_WrMFp85BqOo_QXDnRtLLwOau9uiHnGXmfEqdKcHcCytJuWZ8x2J_Y1I23SeAI1Wbd9zjqwIJ64qzcXCu3sNmQRPv9ZTMqZJLqCi_7VQ_tmytRRTsGP37CDo5vX4oei8lkFPy3dh0kPhowMtssandr2fzKBpqrMwhbpZrk_m0YzX6KZ-nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTHJ81ucPeXvBt0aDaIfOS8_zEhcxXEvfKZCX0GubofpEZs2aOWhC5se74G-9hhKZwYJHTzLhPwcT8jrLJBjJkTsRzlXRbFSpuTa8ZUZhRXyd_0CnsJ2qQgilDg-kW1cEvhNE09SpjFaetDRDuBo0glX4CZ1gpBHeOeXzjkST-r6IyvboRNEL3MdjAy4nFZiaEBztSX2RX6-BqNc2BRSLgALM0kwSM_oVGulPzwhtYAQkNCLf83iv13p7qYjEVg0D86AUbMRK3xlCZEbBBvTm_TE_OMIx_-p2MKBbi91qgGV1SJYHt12dROfh23wAmAV-X3g44dzaPFGApk9tbzrYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecMRreU43piq8XrUzoXokrs6MC62ZVioLcw6PLFxJvKOPCKvb9km-Ce7t3xmOYoQciAwWUad_POBUIfIdSkWZWHkFUTl8W-0ddkJfNP-FIztnOrGImiuCF6gtDneR0km_G084N5G5-ZYfvhAVkoHo62brcU-z_cpP2-fymNctxicpVu2RkwzdG1afLZXWfq78hRkBwoFMQXwcuYWVveWlBkOk_tuCBNTEAYHdg5B81CrF_X82RIMl3D6FUUwl51IzSRQaAarVgJGyxKaHrwFRdk6aBp75Mgwlhb5uOBxKGPZXSxc1ZLByd5zI3WeTUDJ-lQGHmusqQljXXlEHfSwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=K6OXocNPhjVKk2ErNMQz49udDpmnS9Yn4cWlJW5v4WiAvJxwBebRW0fScm7jFnFkFCUh5z9n_YHIwtBPJjuHK9DD51fiMxiCfIir-PT4PC7PmQqTcObzzub-9lcfCUC_ZRyVnin_hBnsNg6yOO0fkwdxHvInxYpxVx1aINF7Y4RVw19VNFa-3KP2tEpKRv3b7xycXAL4yJZLn52V59Io456kLfrqWexZFwuBF-HU6-kMW4I-Pegetgx1HOPqKsgj07ZiQTE1DeC8B8b60RpYzAkYfXpSwafwmQ6ZXv5QGbRREgoOCVH2_OfY8o6-WmwmEhouZFhcIFQ_dxx2syWXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=K6OXocNPhjVKk2ErNMQz49udDpmnS9Yn4cWlJW5v4WiAvJxwBebRW0fScm7jFnFkFCUh5z9n_YHIwtBPJjuHK9DD51fiMxiCfIir-PT4PC7PmQqTcObzzub-9lcfCUC_ZRyVnin_hBnsNg6yOO0fkwdxHvInxYpxVx1aINF7Y4RVw19VNFa-3KP2tEpKRv3b7xycXAL4yJZLn52V59Io456kLfrqWexZFwuBF-HU6-kMW4I-Pegetgx1HOPqKsgj07ZiQTE1DeC8B8b60RpYzAkYfXpSwafwmQ6ZXv5QGbRREgoOCVH2_OfY8o6-WmwmEhouZFhcIFQ_dxx2syWXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=C_Xenq2_fSKJWCaqSsFgbIWikCVUmHKvbAp2Eogxjm3mNNGdK-Nd8fwBFhdDYYiF9EF11__9y4oi5KhI4Hy8uNZ1EDblDEQY4Pk81VzNGJO2Uxo5rO7x6kCkPvPOftMobSt2k5AZwRsc-Lkwtzou39BUAtXQLscg9f_pdYi3PsRnFKo5-dmM-VPPDVOJSmtcUa4lGx1K4W6RefKYkmP4lYBzBHOdYKmq2nS0YBN9nPTTNjMPhqx2Pz7fUHXRKb2mp6dtneQ7SerJz6mwzHAANshBDRLf97bGI_hkOzeEHEttdIrB6yjjvF1UU_Dz3aNosMYzn9_SJrC0W9dUq_1jiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=C_Xenq2_fSKJWCaqSsFgbIWikCVUmHKvbAp2Eogxjm3mNNGdK-Nd8fwBFhdDYYiF9EF11__9y4oi5KhI4Hy8uNZ1EDblDEQY4Pk81VzNGJO2Uxo5rO7x6kCkPvPOftMobSt2k5AZwRsc-Lkwtzou39BUAtXQLscg9f_pdYi3PsRnFKo5-dmM-VPPDVOJSmtcUa4lGx1K4W6RefKYkmP4lYBzBHOdYKmq2nS0YBN9nPTTNjMPhqx2Pz7fUHXRKb2mp6dtneQ7SerJz6mwzHAANshBDRLf97bGI_hkOzeEHEttdIrB6yjjvF1UU_Dz3aNosMYzn9_SJrC0W9dUq_1jiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZP3tyWk-ste9RsiKWinWC0-6vTS5T2y30WrIH3mb46AfRYEQ8XAEsYdpRpDXP4PzsdW3Qj1ImjO3qdvTtkiXGWMxJ2sN1bwe9y_El0qVux2sPDTuTLfiGKXLeg9wSdlJyd3btktE5DACNweMlNwXYKvTqwXWsBAJdRQSDi07rPWYIVHbtDfhcI2LcFUV2k5CmXcj5oOt4JuP5wkh5WNEFxXqfIvb5m4D-WA055kcDgukkEjQwjV-1L-pN56yRR-qYq8gonxfDYWp-nMyFWdqS-8vZ5T07h7yPc2eARpEURvREHLG1MHPSs0vtzpEiqNPP8snuKAitErX4dXbKSWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
