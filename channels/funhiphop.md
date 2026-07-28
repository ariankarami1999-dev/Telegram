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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-LJRWwGMsalhPE5bXPrhhWqwIL6ITvyu9Mwg1bddSNH-rvUO1_O5R3YhkFwkjt8cJOtcwUlpssD5Y_NO4EksndjmI11wPbi63mHywa9FJ85p3D7NtqqcjYzqxJtB3i5JuPkH8sjPoctPyGcStNeLUK0LKxX4R-mkPmr2mGVf3Sc5gZinclWzJwx9VMwukVrixobcogeOqbPaC1Gl2zbkarEJzhdCCSxhIXUdVDX_cze0OLTm36p8FHz-Tet5RpjZsiecy4KovaZMFKYgdeMMI4xyhKhnfDHQlwvGSq5068m_o-FElM592UbgAn6Lt-kbVjsus1f2Ry7TqkeMbHAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVYrDhrCCdmSILEjEu7H4lCs7jyM1BncH5nqILB3xTm2lVs5YeIPj_oqmR0UQnB3nHlWqyFZprFgeXlfqUzFzT_0BooHGThWU_-vq-a8XFLYK_qcBTJOqbG3jS_9qpAC37ueG43LoDXztUTwUj229XRi9dW30sGCL1pcXd0ANypyt9KByKIfk6xNhqAfKhcBvzCZJBX_Ykzs5XHr8x08J0KeDZYalwsqEhD2SSniUwOT_C_oWRWoUIDlH-kM7UeZzxC2zfrO_B01scOrOZLX4Af9w1j8ybr9qsgYg939h1YZKWQCRkYW-Ua53bq3ssJsjMHbxjzmP5idCNAeNirX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KL4kmO7Uf-pSc8BwuSH8xkrfeO6jL2S4XSLBaBdfkIO_ljUSrd4AyzzzbgZCWJeRuup9jS09j3qlEpqqdOOwT4_L6aP52BOLeu7oY07DKyXpTjAUWEWEthRoyiNCS2HHnRokKVVY8ok33TOld0f42BsFk5zSogHhtuyaRMgrPXb8CGsir84bLsAgrOWto1zgWiEqqC7QKmAMZu6Z4Q3XZupYjVPeTC7pKjmY3xSpiMkzprxThHv77zdqzyWm39UHwtjeAkF4gDf3rEvztqg64YnIYuvgnF5bVh8ZRUO9HlkkWTZvppmFVwSvrufla_SiUK_M_mxZzeaEgH6SGzyXNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6dMThSZSCdoKMk3TRKROrnMk8HzikDQOq9PkK19RcV-QP-WsNfW07bFqBcDu0dAHR45ImSQXOso4WroVtXwDmgoZA58PTOP-EJ519d7YmoqjtMjKi0TGQHxNUapGoiZaKzktmBqlQFyavkuMOnMzjjKtB5nZxl3_tykIZj4e18LHWVdNOpAx8cignseJmJjnOhFjk3UIuQOv2Z1Iex2mW3CnQ29xsKhyWWXrs-eZs3KVsDWE-MlBLSkidRrLHkg5IXIr1g4VxoYXnTWH4hatsosImc5mSZApFD4DgWspb2mYywMCOqBtffn3VjKnXSlXRptiByuN7J0CPmQKUOT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQChUheIBoBS-6oLcaQknkSrnWtItuDdHE6_GkOXQmtqDEY4MuTsHIvw2F6yJ-2p-Et64jRkRD8_Qo1fYUI6VbgRHWjCwBqhWYDZHtVbW3c79zzaknybhDI_hqX67zi-OB8H6kWWkFhQZfhEYXQXtl8tCKKqQvJ2oZj956X5T4WnghNTK0BSAabsc3R-V20t61pEtTpi67uzfm9WClinK5K_se2y569MoxTwRh_8WK9_ksmHp9yw1ZCnQdTXh1-3lGDmlMXiR2KfBufQb2oWWtAHh7a8LUTq3Z51Z_NW09ziN5vLMtMyODE6lxaSLxVn1WjnZxVixR-Vod74L0H4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmSRXyGvVNkjxglu-Z1ZQqXgcWpO4NoaD0yFsh7KbQRAKnzzRz2qcDQ1iC8aY8um0d9lJBhClhBS_AsLWnU79B9SS8G0cUW3wSYMLU0iJ50GJ-r1v1-4U3SvYIAvbCrGZsi1DV17yt1UdHQ9Tg3tSIS4wWtLt_KgfcW4mrJ5XQ23IavJXq450G9V-5GpmYPYpw5JgCQalvwabL3mU_EP_ZqkQja7K9bd5PtP27rMNBGCGwO4gvacZvr-WBvANTdA2MVXeVRhACrq_43Rpk8yuRUUVCelpfd58nbcYqk0r8Zj-BN3eLwd_DGkhYXNzPyVEKfuy7S0qyOD86M_af_vcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5PeCruKyVXv5uvnHfP7XNi78XXQG3ivmgwsqi3UcseBaX5XAk-4j6donn5NAyf8pl1MLGIpZxn4r9MMDJTSKnO2eW2NOvzVu9C-6FbhBz70fiSaM66UGCmRLIj_JH5VYmyj0IovRfEw42I34p_izEf21wHeCFGt1KGmkNr0Dp7Ao6RI7YGU_Hd1qYmT-jVMHyWw74BEZWXyTEy3rEcZprdmrqf5OcObBW3SCLm15Uly-p_IwImrc8qdWMmLkXAgeq8S7iwQW7_tqkVWT7jyhV-Lfr-F_ae8ZhGgeMF27gqLrYlKvt7dib6dHWM8EbUZ26ZlOn3BeJPUIgmQQuZnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1SNoDbktn05KN-JOe8FOyykdIWxbhRX2cwNgVzOeEH-CCulPXmBnpKHQrjM2Sqbxb4VoHv8b9YZFibJR5Orlq_dTaJ-4oh7DqCnNsdx4Lv1JiVS-rQNzuaV-5KIxSg9ibXI4EimaAxT5yFbxr1vXofcyBaV1nVLEUrHc6PvYfuIUYQD7z6SSaFHOk4t3GtMm9cYEA9ABKpREEtgWuPVhZ06m_rrmGRMxN0jzr5FmEtEQfoKn-szRE2fQa84ZIZyzUPCLgoWTgyEVeEEmdBdhtrJjW2gq4yjfHHWyZa-XVe9BuBagipxD4lnPWWj5yAe8O0HIDnqADS1ABrbIx1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVHbiiPwF3AWtJ4us7fQpsG7BFYVNcUTSvWFzlJud7B1LxOKRJl2WQKPIO2_V2RG_EnIfURlk-gGCW0WqpbB_-vYLurcWs8e2KLPkIrTwP_y4yYw2EjKxKojdTfNcPpfcel3hR6cctH6YYCE77-Pnd0ZhwRPAGJvTSooHgxvS41EMOTsLXtZoZre3YtZ46ZtlwgomtTrr_yp8S_thSbpkhNIlzEbRNzV90mZUFr9a313ZRX9LgubEczf3wxoFeDMI_Qqo7tjsmH40KM4npBp8XxIj4XhZgE6zP2eo8yB4TBSiZxWplAr3hHDFhxZP0nXoh_RXAXypOuYb5qFHe77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9PUjyqQuH0KsmVH8OPLj_L6UzW1rkyTHbEDKt5E5g0wRAshKSjKbzW8XFPtqNMFo9AZuT_3X-xYPpy6VSTA9wowu06Ht24xWxO9AzGFxjGKhc4PSe804vhrXfZOy601pUyyABOehtz4KoGI-i-MLNGfIjOPokyaKDseeSOZByhurqaOTFPsIEtF6c3LAPNVrgEiy0iws0aUNxx-3kCRGKOfqr5cs4YwneLQOM-kX7V6sh-yR-X31HL4RDL0Ghgf1LDcs4bZhfuebafU4o0Ax2YYP9R62UcA1FUEPk10arGhAcwPNCGlayJLHwN41_YsUywvWFE7hD_QxDMySOOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPizIAVoAnzw2t79xZkiz9vvP0n42rK7kVXbvrXYM-mEcQjtrlZQoAKGUyATPWVvPYpVUePJDq8BkcjR3DE4DvhhLCelp5jDtd8JhLUKgRCKbLhPyIkiDPlGWeFfxzt098CaDNsZEQgfW_aJGXb9xWPbpRBppfBwh1mAeJA1eLT5MVe6wsS4lLkt8TDH7wbmSrbq8Ajuha7p-t5qSlqG2VpzbPpjRzDMDkeCBLaDqjVtmZF41NnRJE9dIz4YRDPiGlIc-f11fyX3RDuYNJrAb0Li54fwDpSfDpMl6DXRsjm2eIandCBjAOoCm8nSOGxsB8cz1-m5VqUDbhRHe-fB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYk1-iA6PgIu7NL-lweGzs274WOU_B7hKO7KWOgO2-VJAqXJUmhn7LJqm8bWwgwq1Wv_zz-4-EcuSsNKx0PdCPvEfssYzCStvhdZJFkX4L4w-uWIPN5dXOBlIhLKj2jONpGy6FqUZ1JZkt8CcRdYRKzZyYgj__1dGSQ4ObB4sYjD5soPvo-fQ3kzsQwqwL1Bx65ns4trDus81AsYZT7d_bfw5_arf53SyhQGR1eEoRBfAEjYeooIUNdRN7BCr5WVr9Sc6clnV1wP7FYD18K0cg8KSmsqKFE0mt4WfIRDqN2797AQNt1erTHEd-dM-ymYgyopiWN6_h2Nr-kROwEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ENTDkBay4E6JNNLGMyiJI1w1MyIydgA0akWdgvwBIZyErQPUAEOv1J6AVqIMyo2uiDGNm27f7Zr7zerbMncU_MNWDDl0XK2ZVD3h_PoBgvxCMqvpE9gdATL3_niF1aa9778Dl3FYQXvfIJ8zDqn1o1dcg6C4OiW9sNFJC5rPWLD6hK0BeQLm--aT6o7MRWlabVVwtxIPHyr2Gcqpy8LwugzZepCYMn834cHbbZXW5P5uvUsqS6eQAD4rq-TwBwc4Coe9LkMJXAyKotiwJ5VaVWaxgWh5buzEGaaVd8kbOgiwpBWrI9lBM60p6XMrix3L6LKlxfNWbuRc7Zdl0jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2V5EkxuYfMZZ-bz7rAuy2CJwV2N6xGASwmXE8cs3D6FhwdaEb7kzAuHEnGqBkp0NIL7dYXUp99yP4rjLP_1DMEftT811fQumKEJ2alUjEHytBlLhlCkBMIhe03r7V4zfpuIt4Ei8ojh3Q953pcW9r9mkiCcDSiv3bKfvdth3wQPKNa2Wv3r6jMfQ7m2hpiAUNnikXmBmhxXQmOq5GT04taF5q0qr_GCyWjU5NeBcXJAbt72GBokB0t_I8ATEVFmsgojnpHBExlvnbpQpRkPdUAFY15Qx_x5oSwXjFT0XAgJ8wICp7FTdEyW1WKqfNFdisuHtyV8PN6dIE16oLhxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE1h01MtEAqF8Cfrh_8vODPwmmiBLcC8I_8Q7RFwE49xSY59-5X8loJroZumqGTKOJ1B3-UOs2seXmUOUlYdew0OX6SxhSefNFlAGRG8ff1CHMU0pCIxZDeNWE09kL6XyisTYG62BdZfyHoK4nLgOl0hTcMO_KSd4641P0wJzUnmyGOqHF3Dj3EYVfiaCds_5heLkT8Gha42Suagn9yJ2cOm68p00EKIETJgQSxtciHpHoctbfBgmCGCsKsPnRHX23NuoPrrmNgeXhInETviw-kzrsmbmiHQxmJYd6aqtlS-skxcJ4EyIpL_AHBT_bIbryXxOOI_xApIqdO-Eh8iuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ZdsZtCq4m3xmvrQuxsp9EuFtlKA6C4_ARCT0Nl-S7UPneNTOym86v3QHz7qz9k0ZmgxIxcxlcFlR91fjOMosDVmxmFRmX5Ssja39cs9yRadpEXxZcYiCBxcWJOLGh1hhAD-g9O5aKZDwQcVZHc7QEmbhXHSUXvV7IBJXnl2s5WLs1RfYgCBSct55EPzaK0pYcdbnDYuRmhaTzWZgm6EUYxJDdwIvhM3I-M9e1f1WwNtr7iMTaXpNANv5FLVgJGr_PimhYNaX-MI8vctA8f4xnf0EQExMlnoG1o2XghQMHXbItX48NTqjXL20RBhWcWGDoSoInV38EeRJxObNWgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5LBhAVjV3atjbtjDSWDRAJFr-KlmXTYMOZQ4aLrUpW0GAlj4erzTrq1HyIBjOBfJOcT1Q-vdd1jS8deAZzsiFiKSy0q-bPN-bc2kXF-mCwOLPXs5wNmdqqj6cnteQ7qOzNOT_xAuoGhze6opRrr7qtzOgQXBsWHdQN26YTDSm546RRFB4PkKvVAIN2dPXKO6xLn8QQj1-mYvcnd6V1eFbvpOgaR-kbHiCpSyC2B_QBymfQ4TZZ5-ZvS09tvFEJ7RohUyC-ZO0HYFh524Nh3CO0WUX-0wc9MLOsF4mxI9zljAqPeNiUT0t4SZYxPuNsGdLTFy0Y99VflFveEwvuGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rq038_YVPoaWGAYHgZxwFuDhFKxwpSZ6yIfoTEurKxREvNopLPSTLlpJOQbvN3hwnFfFtrqw7iPqk58j9zFWY_XrToQ98a6tip3U3TzC-wHVXqDVxV3Px8Q09T7EikJbxSlGC9DKqC0htyliBz3kCFyKHtEKh91GrDZXKaLsdqti5HmOt6PWaQbPFs9inUBtH0tmhO5Oidf3tJioCQFELCC6zQ174S3FHUTd4DgH4RoytRCrNCghveTbKrE8cZSg-chmLMeCDc3PNAMBaD7oc7zPq1DrnvYczjb68pS9OoGkuam-WZJrclJeh3nE5CAy42xirPKDoUojAbQr0LwI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeEVXELiY_D7Ixm_cOv7PhJl2WYZavKhbdJatf5oGqU_jQBG4AQF1ePbXsni1kg0vwatSMbdccQwuy84FlCWwkXAB_-PsOLJF-JmhOyGMgEr5mYw5UNgW55dtzbYxMVi_lJKzhRSQEuASwHv5pRwjZxmgObt97RYEQ0UjWRJ2KTnZyu91Th4RW1YiqMkCXA0Bq-4npxjwdIN2gs7G2k-7QEcXZuAQoY3mtN2Jsa57r_BnQEaQ3mYnMYCAG8pzvBYkDXqXs4KK_Zyd5KIx1pU1kBNtyKJlJmmZBiLgkib-GgKL5340dtmv8cJk7IKTfesNmphCpp-L8blclX2GdvCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeGmtzU0IsC9Cf9NkIHBs1To26tqWCN54tIoIsMgjLCon2g_H9CYGrZiad7iZqJfLQybqWsrUdCiXcqLyBxtZRpj3Qm56vQtdcaEw0t0Idls2nzMKsAlNnftGEAto6rKmB50iUuCyJYaT4sKviGrmae0Wg0Q1hbk2jGQUduDaBpX2sTp79sxFD3m_QDUaEuixKNTTlj8QoBW2UuN9YKckaFiwtGFp-2vihWrW0r0-TV42T3WuEAK1BFsNNRYBuxe_xmgp2APuDuvXDLdQMFwEkKmJRjFd_mP_1EDEgheKcgr_Yy7KS-VnPXZt8JcSF84oTrb6CKV2ex8AdITIX27Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR-NXLZ_YQlgAgMySLS5czYEhIVZ6oO9ro9htBof_ursJPxpsMoKB5eVHeJMS5RlNR0GrEltjpfHqRIid_8q9mpOFd9AMV0FXDGxpj479aaPHZMry9rYDSO0F7k53KFykIvKTRpu8rDMHLUiS4eOW5t6J0Blx-EK-QlRs_zZhGYRtLRRPI2oXqs4LE815Tx_VtHed14ss1ULh7Q4ulmvV6YpJZfiLWhWSkxXXQ1a6eQJJpFURyAm1giN5x73rFk3JgBSu9JXmm55UNPM3kyVmKGZ5Jzgu27r2IIY1-y0XruTSun9HpphFs2TIdnr6jXKGGLhMsCaP685H3jQ9BsZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBxcYzSebkt6lfnY-MnZSzQEZaLcBdlNBJUhcd5yl5wIVq30XmJcJcmtU_enJqrI_JblZh4h3Fztp9_ifg8zKBLVXGCF8nX0ViUdvvNBgeSUEEQvKF5XGcUGSEozMxfzmn_hB61pEj4SiMnqN4C7eHagQ83g9_zuJajdDcwT2QhOaNlVEZFIN1fgTlZY_DxKD_P5g4xCQ5zRhLbP9lCfUdOW2AjeX9pg_ZWxn9yBjKURQPPlcjNPAiO4n-4kzL0MIyS3KxjUP1RrOTPrNqjVd4wJOCFuNm3KskndHtIJmkLyZlDNrapRZUpAT8LGw8ugf4aoYZcwieFZ7Ki7b-_PVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q237KV_oFO6ZNdU5EfIpXU9nhhvg_p7BkM-_Sicdf6ulBy3zA5ZCahxbBWeqUQBcir0HolBY9mAokd_rgTDUonV9fok2jiaY8K8YRMLFFyl8Nx7oKBTu4bjQ0pQjhZ_tnGBRBZ-ssdVA_ByXtsov6ilamcT3Q6nBR4pfnCcs2vjhRgyYseZ3BVk8FMRAdHAYY7GEjYMlAnjVIrEEr4bG7YTz0py4ypqnPl38VUf5mGp5Kj0NCXyh0JHByMc4zA4V4F9bBs0ro2_g4QhWPeBxDFmBP5MYh09eNY2Ra6-QC8SyyiOgaEjwN-hbzRGHyl8TXenKbxG0W0-42CQVPd-n-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5p_c76mZmtlD4pyjUAaJIFCoVN_K65au52k38XDBmj5proh72E-SSyF9Kli1-9i5_Oy_bccVUNBtBq5p3loOO56GiJjDEAGblZXLAsCaifxWmsmcO09Yf7GLLARWVr2G45A9-qtO_RDQSXnLxEn0J9ZRabBn4lZBCJc_Ds40xnA8Rveb3d8kipj_EgOvIGMmzeah4_eGlWnX22dRkFNdBNHTyIEVOWIfqdmTnHCIdFJ_r9XijKX3FlXLQdZMKWr8NjW5dbosP32wFEu3UiHj9iANE7OvqIHWm90VtLa37Lq60pQ2KG0KCNVSD3CnSt-hiEoN703jAV-cq0NznC_Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=fietKVGRvGLYWNSHMmk42xwFpjtx2ooGGOszhQW-2x1XpkfjOpnaZbfh5DMzKe1suTS0N5J7dqdInC0WS0COXBDfQKg2gqlnrlcT5uYcS6KZW9vp_amJTkNs14OY1WeryZOCv_ZFKEyx_LMHvjkNH34-U2KCQDMI4yvOKtxyMJT_96UONY_t17HwFYC4G8-o00AoF1skGyqJsarxZXUupEzm8ZRRSYFV3XrdcBedbTUr2iOYQoX2usmZUUhEhZJ5NWLUD4WIS9drqxmH9BL9k8yuuEghMetWyZTgWSImzK9TMsYpNvWBLDoBOGtEoxgD-QfDDhCjEqp06CG6OZ3ObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=fietKVGRvGLYWNSHMmk42xwFpjtx2ooGGOszhQW-2x1XpkfjOpnaZbfh5DMzKe1suTS0N5J7dqdInC0WS0COXBDfQKg2gqlnrlcT5uYcS6KZW9vp_amJTkNs14OY1WeryZOCv_ZFKEyx_LMHvjkNH34-U2KCQDMI4yvOKtxyMJT_96UONY_t17HwFYC4G8-o00AoF1skGyqJsarxZXUupEzm8ZRRSYFV3XrdcBedbTUr2iOYQoX2usmZUUhEhZJ5NWLUD4WIS9drqxmH9BL9k8yuuEghMetWyZTgWSImzK9TMsYpNvWBLDoBOGtEoxgD-QfDDhCjEqp06CG6OZ3ObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2rpZ_3KE-Jjl7hAJxSDb3qAtRGMa4bZd_Y6mNaxgusLLc36puuzpq1ixmgGjZAWbXvntj79pnBnqMQiI81vTWm40Tm6vt3EyuYU7aGA6Eo5BrGxWqx7ZmxTR3MWtLxO-ziZi4KhNOnDk_5q8AMR49AjbiWjUBtblxSJTpkLEM2tTV0dg7S5ig9KWc8aGNnJ_HBX-wbUqSDggy0cGhZY8xvZtEUgrWSeGz12X5HxXfh-GATZ4GMsAiGMXfiKIR_Bp1tVrDgDg-RPrparkqUOe-4dyLCmVLkbI-JEyA8My3bc1AWAVPkhRruRPGXnxd9-z8aXWZN-K_G94RD__dMciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-Jh1N-MvTUuefb6NlHnTPfSd9Mg3kBaBYEtFdrMme3y0ruhrUPYfG2klGy2SZ-DnjnwgWPL76RVwZ3w6HapODjFk4f99Mgf5fTtTQW4aGhQYvNeGImh4gJt8SDAhMx-hmZZuysuBfX4nq0sV8Tacgy9sDgihWqjAb5PBshcV7Q2vm7JFgFNsH68hdTYITHcdg4bs3mrUrwu_kE6QQUpYWFCRv_oFSfpnPs3TzQYGjS5FnCjOI9YeQy2iqluenKiygRG6Ql3b1vnudYlKlRrYE60G81Lv42xH8dsuHhXStdhX3EM7nkPzYSSyEmivSsvXDE6GcrO_bh2pewEv8khdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO8Xk53EzK5I0XzepLpwg6ytIUFNZFvI4AXWav_IHa8vhtP2G9c0KxeERkU5i-XNpFrW7zRMjUdBj3pAMWC186bPzVKK_vxTZR8aNwujkEzGh6cq8zzrFUNhfHqi6eIGcFSeOwpOqU1W2HNiSLoiOOWWEVo0Zq0dsoFX_2ISRf2142LWar5TFLA5oUn9gxv2hUOeVlc4bCkbjKqXr0qmqkJKIcoKRNs3Y94tagqvbNC-WI9VEtUge3lXlYwgGkAfUUrRuYT8Fb2IBGA0GKrFcD7KJDqyaatM6MnRzBVJ36bGr2YoMNU0gA2b6akRRDMitgrwLn_WcQTks7-tGbENTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxmebIN5UfLyAhRPtOdwVOkf0pnsfdz0r5nBVPzuiJ0sFJD5ur0YHAwjHOL8nY1dlmqKLw0hBqF2ynrVqJs4QxkJVa_d1cczD1Qwytk3J056V0T_XZPktWpUrqqcuskjYMS_0_Rj0AsGlrnIC7qumF__bjgIudll8gMKYatU_NoFyH9vT8dwmUGQeHrA4xEpKB9jlgBzYkZ6Q99xAv9ovSDNWnivhwzWB1EhIwVoEdK_MP88b3NcMGF-A19fLwrRrNRSelGF4RAP-Cjl9KOxdsi3OiwwGfF9AxEILRcAMjfrTYay0PIE_q_Bppqjq4fqonHKv2cNJuT2XTrUKQMzmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueYU2U0ZZvGxrjg8imk1GQmKpfHxj_iWJVuUgrQxWQjuWNhc70i4jPFdSBuwt83HV9XHp6jB9cXfZo83YlXelfSY3r5Fbp_V5eE9jxWNHRKzDKjqaa9MyF4tAJlq3HJybirS7twRc7XbnLaykjaClIoPIO81vxxDVrjO5lnGbateFVSiD0rloQw3KlxFchDHM6t7EB_7PbEcWIcZyRdFsi3dwBBSd6D5RK0Ac3lRdafz-opez2uSjjTio3MTj95HRtAtyW2iNBXzLJTv43qBf3YIwkJFjgFCehazIIoTUnv-4PQKABHelxIVdEU29qDkLr7_6W4Tf7Zr4IWyu7y4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSrLiccRooyMZBRJ21G6D9FSXcpjncCUIR2r-FOu5fc6Jwxs9V8mONoBLCNnV__YBi1Fkaf5ZNKwATZF-uH1YcIwEUE-16Htn510U_FN7zHmHermZrNhTSGWqr7n8Ar-L2tXJK56KXIVe17ixw6yUaERS02X_KwdtTFiLGRbykcIEbLXefroheVulJbV0CYxqWbBKmOyf12_qc5gUWn-wWVNC4mtCMV3sbDw6HHVvpt4y98rDaxtBNjnI9Ivt313hQNUneojadmyyQy7wu8NOxQWrWQosQmlRWlAZKxtxU2ETCS9QJ_OwHP_iDqCf1GWz1W5V2KjOnuqnjmCzzq_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT4lzyf9LVDx6L3ssGWhNB47X6-9YZ3vLmOPy5BLqxwj8dtIn56RxxJKPVjhxkKUo4J2VwguWGHEvAMINLtvfjwXkuyaHtYlmrMyKXNCOOJqy07n2k5Pijstc1jtvsgFo4bGpyDLyrI7bSDtJw6YQA0Al5Xh_Ih-yy2R1MiZ_J2qmFGO4LQHNpGmRIFroWa6OjxxnWecm9s7okDBiQN8fM2WVlczWBVwrSxppbNllcfQ9XSyX7f_k24U3cxGFVwMZ61wSuUOatKd4jAKU5_y5x8eXspD-0Na7r4g4fG8VLIkM3e_VUeJhUkIMuFfEkWzTjuL1riib9zYlZhRqBAMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKL-Y12YHiX_VoC7XW-jjke5QbEQeMH3PLmKSROuba5u0MaS91Et6dRWHWnV45cFwtrsW1nzIDP0DYTTRz8G2ViqK2t_zywkb9aeavFPExCS3FbV6cLFp7BaPoV95wIRH6RyP589D7tVh4cc69bR4rGsl3fpknli56pmXG0w-Vzo_g8sVBN1U0GRGhYH53fq7Qk0KMsQ7R3yuvScFOE0QS5qVgX8j979ezUboHqxYI2uPzOtZ9LYuraos-0emYeLBBvZMie9PJyEUKlZNZbdBSZc0ZIALbx_E3NmPgKtobmRsUw-KyXVb1f-rILIk1QrJhYBy6ddOPLwjfIrLBcrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTQ38wMhJqgSFJ0YaMeFf_EUyZejIBf4Xj676xr4KYr3Pwt9FGoFAJ9jDqpAxBBelW5hRx1_SbkOI6gj9r6FKxHrO8dFjHspnpYm3ASDYLMjDdMdSL_gTr_woe2shwhSGS6QsFwA1TeSg5mGf-OE5A-ihYRZBb1CqnDbtsielZFJ-D2DPSkizbez3uvovrkQp3jQlCb0FGSDJVDUcgs9xTK-yFwbOMM0Kb7b8ZXqh-HmBA5Sv0X6xuf-ZdrUAF5cyi9qlM7-Y0iu5-NND3E6rv0Orv-HsvuKS5XjezZPy98oR0ljHUenPJGKXDjRjvvXOSOaftZnaSoz-4atwH0Jhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLQ2sQWxS32CD0NN4Jnw8uZMwhq9MiNKnmb6czxJUCS5AQQZj_hShYXOwLxwjOVXN3NDmbFX2XRYnhSyV2PvNAerBU1lcpFmphkEUfwlfSWpB3_f67IhbLCyddqYTeFLdhEsiEl8eFQsNZtaansHVp87keszs23No94is2crj6E4QuA4nkBhU26XAxb75flhHnffZnnqRCLn3uUMqMOn0WFonafYk6jSeaVgbmwYRGL_r9nnS1X4uN8iWGyj9YUvtxfRuLjcCAXilZVTm5C32_Ng3wJ4AF-M2a7apQNdN3bkrCWjh72oPqlmATuMfR3EA-w9xWM4sYOsm4nepnSC-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-YuqS4DrA_eUtEo77qBoykUfRWfEKTpj9fXs56-R8ccxfL4giVrMR0O2hFZf2fwOKO2Ef3MzzPvZrii7tp7lL9Vfg2CbSxPKHc-h0ikENjKds6QOszMG4cBCpOnU7YAqIEMs7B8yc8JiPQwOMNXpIq25MvJ97iCfuDSCouaE71qCP1kcMZwPDPhxoFCfGOfohKu2dJhUZ4LvXCfU6OrMj2CiG-I6v907tr4wT_-tDH0f_Zys8RPnvMmW2fwNwqahbTlPFHvbYXQJT0mduZJYqIblZhFN_tDXkeJU_IFhvRm52-1aXLKFC7U3EH99SxxG6VgxdpG-EfDXpSnHRXw8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLX_FRbrlAIi5DocB2_lxdqnI4nY7h0-YczS-4pGxfhxZ4FJD6ITf-QFNvaNCqcw1EFvayCuzEkcbjRaQTkveuZ9_l8ybiBKNLlniKY0mhLQcaiFcXe_Jgw-FdT7AjsUWH4-q8Z3uHMKxqetqxdqvZZp6lh3pjfQizBSND42DY0GYG-P5h5nyLBDQHRWUHkPgzEFYtz4EJ-m4URx05buXUms0SjtKJSy6rUrUi210schV7trhaB7Ed-1WyGXfP71HFkasojZRLxbtaOh32Qc-52qcKRZ6ipyBCmoh7sMqYTN6f7tNb3LO_LaIXM-wKtcDQId-xB3UYhDF8clOns4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcXX_V0aaPlFtGODV9xjpIdyU5C3o7f0IYkxI7Snb0xHq1oSEtYFzM3lY5aOaNou7l6rA1fcEi6VsKwvd9bco_1Bqyt971NqjTsxxywP2WmSVCcm2J9n1Ta7kAOL2XpiRqvbbcIuY18u8Bfsdlh7tEgStSmdI-DynifFA9Pml1Yxy7a9JwdLPQs7O41COjLnN7FRP2na25ggNUfwUeE5a1NfxluBsoWUoRfOz-vuPAyN7tRwpQ66-Oqmira3eoaYUeYaSPndZGdOtK0NlKzeiNl8COI96mTns3gBSrtf2hPQRUrmHPELrmT_zqVszPlv1YWGprFcHfGxZAn-xxTMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBqM0qHts0nbj9iZo8Otyhhc7VHad-TK2Ppif8XZuYcMlZA3SXLwTFGKmDC7NqzClANGjcnUOuRodIPCFsCw58VP0xKZ9jTApyTAjpflJrQT4-SUi9ZuQFLMwLIaaYRyt8F6eeHB7QMeV0uzHXzugCJu0ss2M7G62NYWLWkKjYTYt_KeOkXckHFoDwvlw-G8Sed3-djegGi0Dan_lByOMAEzmxkNOSGe2yTvsVxLVUnhC1dP7XQKmeTyk4bxCWxD4b639TkB37Bg8fFT-TatMj9xWGKnRLTbnB2pEAteb-5_GihpZun088KekaEV2ABQFpYrGRh93Ywxh-yRNP5UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL7BsmUCo0fpxeAeV-TY7plNuIO52j6IZn1SzBMl5Ch2FDpPztnx6c8Vwf43o9UvHy9KtSva6pHnIBlypfQYrHbS5LLmBokNKnC8ustmn_FdrAoYE8G2UDx7-RQmbtvo3xXRy6Ro65j72sdNurdbSVndSoSyOw9QUkwwr6P7hY2G7bS59KBzQK85hALoxXx65_n67Iil6SoIhzIpomF3M4K5jZCRwC_Wue4hMkxsOVPfkojcY-lhVjAzbRiO4XjKOEVQF51bKkACu4OAMdyBlm3D6FgqStaXTKxuIuj4VZrWFdtP852Uq3MMCU9nB9rM-L6YFNZijh2hMhKEJRza6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyQ9WXv0DWw6NBzgA2VY2cVkwCVmL_UnHXUJpKTcz7yECdnPNiXGiwHaRkBzucyQSxQ7wCm0tXE9L-Gnkn2ajeyETQs8Z9qCpCN_5CHnoGDXZsPvng1TDLYOZEi7PShyscPoF7C4Iu6uUqlZU4X86CBmGvwg93yZRKzGtEWMQ0UOZaRPd_IWmpYt1O9ALrOsZeNbnbrgZ1BZoM8gWXl-Ec65T1UeSl84y_449_4GmnPFdFNIktFv1NBXwIAAimm3D2v48Ckl9mnWmlVIvULguXmWyIHsZbYFd3ufDwCQsFrtsAdzMcT5wuR_xriz4-uEzhQLIbZLMea6BlGUjbIFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mx6DZRQEIKWRw8DZjD-95Fuzy5-zUwRrwA-QSzS4I5Wd4zA7eybz9kMW7GkcVBW_vmq-UnDQOVqBheeHlT6jy6fwfbh27mmCQI7MYc-mxeHl27WNjtCvZcCaQ-LTotTwhhkNAh207MKBBtbwe-wglSf9rWbP63m-HrX_EHL7lHiMYk1TwIe0Fs1P2OnJF515xiksu9N6KJSa0HiEHHrWFeUyy_msnD7m19na5Mutyid6XslE4yfL3skOoRHKyYfdDaPaKGgGYaZOMs2w3MJxBj1hs6UocGwk5j0QpKUVRpfkr__fFAntuHy_ofl2EtlyC3BJ5po5wF_sdMiG-fFySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRAWop5DvWRXl3miVEr2p7IvxziMOdYuoLJxbxKNaJ7PnRWNZxdHesV9FsDiZM2zMHUR-Ig1q3F8eI04Gb5Bj-ohxRm0loYJwzH-IOqQ5vqzAqvh34cYGuNwvpSg9zmrOIl3kBWm_arJacdAu9D66zTxRAl0M3LkCRknRftSuM_OWPHXBATBDtafg6Li_-xTwVnleqcR2kYSuoTo3Y33oWPthL4dh0U9ys0gSMpWyU9DEUKMMwpgy0f_3BpmftL6L1pnYgxxXG-LnZUPFeOjql4IqsPWx9z67cvG4OUMTrkNwwHoW4M60aoYBuJp5Uldn8ex1iKbQqseQfpvSPprQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bS9jE3utVmWnGamYjtqqN7fvrlp4gOU0JKrnol7euEXhZ0oPQa5LVEl0vu6FQ7FeZLTaJClUOadywKHmn927j4yHrCU8GWnRL6e-KtpR9dT6epAgUxIlt4Ce0D3fktU9bp7F4O1PHpD9-YHS9Z7e4imi7WVCCQRAqHvvBszR4M4j5YOWfq6OP6BRsUBRcs5fIqu5x5w5vURXBGuA10KlCWPEIBPwpebLnaoMPa6-Z21YYvSal-eMwyngWnvq0W4PS0xeUfDqLW2KQXhlOhxoeqPrZRLlT_i6ycDlZo3EdL3lUGutH7lNyllmI5uoUG_1zMz7MWvrLo_zzy1WItm04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxVL7RLNmaYkDbPWiMs5EuX2_L4bh9GhYDHFafeXxsWuMvR0TUqsDfAiP3mw89MHSATflqnVubHAhG2a2W_mkCW3yFmgkdHaNEVZamCORVzkZ0Ldxosalrq-R2lHSQaK2_klMVi1tAuhUiij0SqcSLTjUmHAmCUz9cQAzbWCtewDrcI-gj6D-15KyFfUUOJIoU4xGWFyaBkyKnVZxorkvVNPfKrBWCIENl2NgieOk9qvEFxi_j4J1VJg3ur_fh37c7MSyjv1BTsbtJJfBebZDNaAqYburFcsb6zT9dJOFoXIB-sTd3a0AffZYcvey7YDhF0v3rgLl1Mj_SAxz9CLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fslo8kEC5H0LJbECptnekXu_-YeFiijcbqXaf9r8lb8or8cj8xrDGNbnLPicShrDJOZ4zIYGwwAUiCtNHRPeSNIeey_85DN7WQwIJF7qNv-T7dyzvZREXfpEfPLnwXGoaDcH4z1Hy-dRE9I6io9k6DGssek-I7cMdm4i-YrsA3Rq7GNzUnFTZVJrmmVkqE7QDhNz7e3dO_ekwO9hMjBqdYZICVngygekakxXQ_QgzzCWFDCjJkZzekwacWOcHH1nggk0mCyNKaebeG-eYkoiXtRI4VaRR4vWtOHqoTmyKF4FqwEKtvoy_8x1HvYdes9eWrHshR-xwR3LQuuRe3A8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5YpiML4nKCIKZySgV6XOPheP9zZRbdsm5usSm3ySg41ycMDLyBgKX9IoxYcYIbcipZirZEV2jUxPE1oFskh2jWFumioVqJ_pd-yjBnUrJ2g7jW1QkMCYe3LcZPCk4VEyjvFrtiYrJMlhJRWXCt76XkLm08_ur24QPpOsaTnmI4eSaHg2b_vssY_qo3bI1L7zaA4ITYoG8AKIy2FoEPuRdHKa5AlP60WBrYzN0rxCdStHEWJ4XSUq8-oNl9XpCXDfiCzWhaco2D5rtQU896vsozvHhVabGcHHJeUNerPGA1eFwnRFOhI7lzv23t3HQzlxZbUFWLnxse190hJmdPzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_V_1rI6X_vFaOGL9wIr_reji-i1yVVQq7S7NppebhCl6WvPS52oyUnlTG67NTGy8LT_AhXsm9aoUohVNwDcftJb1v37dFlUVykHr4Ie8WPpunut0Y23I0xP1Tx3rOHipi2u1uhBOp2DXnkqkQ46JaGRb5CkWT-f-ertVNSYcwE4rnANqKVNxUugUHeuvRbbcN2XE06TPDtGxVDLoK8JJ8Woh4eisxPaxIEfbiSzloelDnYFAsxiiGP6Yr765a-uMjnGvunllFZimAsfKZ1d3M6LXciWi6eo1Otd1-Qgcui0CVTWNslw3rvvZTlu7FSYT_k02Pv3uV3vnR5tzoQJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPDK9qdDhytqPksgU78cjJVM2PaafXesV7L0fbyv70nxtxcWCVr6LzF4HhZdbAwyJvwgIzdb8VW5tVEB-dlwi1oWUk4GAkXBjwuNlyKlajEroIBGrTeYswLrCzb3CI5Ezk2Bl-a2w-PV5YgR94-meNZaaJATAnLwTHwT0-5vuFivS_NOyzF5SH5qFg9UOeim-hd_UmU7nNI6uHtjAzPYtE8e7zgWaVuq6YdQ9GgeZxisg2Rc-qBpTUDYclZ0E1LAU-4-_c9vrEv7YNILDW-eGk0zDL-Mxpoo5OqKWdgRa21VK4qHNvL8oi6Zt15CpFG9nol8Rbc-fu_wculnxypByg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toHEPAqqLKncVOtj-Uc8wPHrNiRPeKSrNJIXed3n-bE6k0vA5hOXPN2vIsLkKi7O4Qde3NVe392opqSOLwxVIjj4fr65UvIa1GocseXdETpZBic8GR-YD9DFEZvakoJfrSF-vQTRG_jdLcplVLbkLsbqFod941nrz_tGAwRCaDyU3AZBrkcn6QWBe5gBd6f5P9UDDW5b6fkC_Z7_fbZ9so97IK4B1XdYtH619pD5junfTtF9iYxCy3u2TaZKER66gG6Ud-lG0MN2B3qJrikvLcYaNfp8ib9kgrkBJj4Ekf0PUeKJgtzBMHUE7bXxyT6oUpiI6cp3dg_huj8jfB5ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3VP9ATt0BZf2djhJ15gOTj_1cwa-DYMIOsyjSvvXk6AtF-QJYSZKU1YF-9UyVt7iyMPWDfwOH3938S4ZeyY4AKvjvMJV3y9TG5vPJTyxKqlWvCQQa-dbFaJN36c4F1lu6ABO2Wkd0Y2MUvwxwxKyjpaXFoseCcKYgHs8SrHQS257miPbHnToTyZIeLqT7fqKMYwT6yrXBcJsVAD9c1VbPMJfBJf0Ld0Pk6ukpD3cOOpPwqBGppLEet7n_73-a84y3HwKtGAxy4g46iPX065QNYJUT5pOV7d8fMyBhiuuDZNOQDN_ngAkckryxf_QF9EQs8QXoiC74aH7Ln-U3L_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az-PJMtBQ2HArspM4eh2uwqQtoR0lj6NzSqK1F5sqARmUcj4YrHadXvs-yn-IYJYzC0M6lKrRflPSDmuXRnH1LhEMOXTZ1S75klGPWVtyUKGtrBNuQ8F_XBCef6ChHSI4DJ6Q7Bv7jbw4eUZydRwQz4UcA3BJPzgGVFQIr332tK-lozejxWe3RVm5-p6ndT-Z1l3JI-HokD4q6LW45xzSJtHKsvyxXeW0g7G4P-OXWsO_VJvp9Dp9AeEKBnHKJHRXSSJs4PdiNCJ7EyA9R71HpQjFFBdMNLJakQ1-0vKFW8KJuh_eEzulJQTy3B54JNNXEoTCd9jQrq97cue_5nPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5tR3baxK8KdiCWnoMERJy6WK0EQn4iIoIt4xvwNWNgS-t4WrBFbA8Y2bYdgQI7PMlpXn4eajR5CCDWaNtgsV_S4jbPde4sB0_HfAJAmHj_rT97baGt23cX6gTpiaCkEA-_7bY4iG9BbtO-y16XoNlo70AZ0Bzcd8SWVUL3UGnOrpC7yxLEGx39swGcwv3Lr3X02cq8Vrq_fGpQIXyCXZtYn_1im4fOpTBbteqjDHfot1yyOh573E2rp3au4jHWI5ou5_RsZQHIpWEsPrLKIQmP3OESYPHmC02FFgnZ61waPz4foXR0p-trEBvFfncy_N3sJJ2z26VpNeQAla-Rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-Hqw4DWfpEs_Lhuyseep_rIA0uBz_nIavoLF5C_tUkroQFpyzdhx57JQ522GqCH_miM_-ZsseLs4elb-fCeLzdqFAe8ovFXjZEj10znBxeUzqmLeJ5MDVeE8s48BQas3HTSkI3pUTMZBP45cNZdmnFNG93Z6uXKvSxVnviRbfRIh3y6vUrlc8lWTxt6QKVVXUmWjqqelzKkJAhSKrNNGZO6GH77uiu_13eYE9o7z_pkqYYnvF8qlqoSVpwwhnMj6xoGwTWs70w5jwJVu50tIxP11WNNLpxSQy3sjR3hw2eGuRaAwVmE4ro0pWqiRxiWkBigPUfHDjrMUfY7x2O_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kem8qWZF0x8GQRufNJbV9U6QmJK344HV1S5zBQqBzdCQlLTLMuMcbEKIZtiDgy__O54NMpOvGEBqTYVzUbBeLBhD4HeBbXFnsB-1HwmjlXlI89ej-MZmjm4sY46hWlWB8V-z6WQpaZVR-J51FJ3-I1Wpmnf9p8aollfX-hcjaNbAF0H5GFaoU5eN3e1t4XgfRzb8xxcOL_RpRDeO4X75_gXnYU-OZoW5rECnganNddBUpPnZBmvys1V2qhaLFo-B4UHyRzw4vJdWj7qdpGDjy4YP6UG0PPy09PT_KTKxNE5uOAS8N02apnODFfwfDX_CbnFaDuvtvEwpGtmF-eiPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU-IaxMflvBKIq1MixjHdUn-7l_QemHZpY5EpH7TFsbUwAUHU1_ZoPcOIUzALK3ZYkULdFZ3N9V-hBWcyj-_B_-4NHf6XY9iZ1ZzIyfh4q1SsYGonzker34JaA0yOcJUeZ6ATsm0CaQ27fyr1gshMVHRL-rgJZrBTiIzgjjRB_-0QxsWCwfwNlB1kkkN3TK6BgRBnlCEeo7mlDabvZiMdSswtVIlTkJqeWQXoEISvSEYLcyCfzZptNNqD3VJLZYdbEHnc0urp7T94zRNMGD8QVkLCC1cHIfjPYx2DZ807LrBdJcQFFhXim0WpvAfh4zzXKSQUn1-W9sej7y4PZTukQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzDOxng1S96YI4bGwF_JEVhsTRB9ZPdu0HH3EGncWLnxey-Krko3Dt6fpWEWNwWAJwld4mvkvMGar0nuC4Zo9hDLtkef0QsyZI8yPcufRvcxJfyeiZa7_MlnrYdig6b28X7PpGGojf-dmSJ21zHKxh-x6Ox2Su9G_jv4aa94rMnCSv6ZEiOsAK3Ewnrr-SL3nU_Jsew3IBqoT93PrB3O69f0zY3hPLFwNIK4P0q3R87nbQPjNMqYmnKnd0_jFQA6viUZfUIH4E68omyG3pFCDTz9JPWqVCt03P7uPyDjR_ljkoCGPagrTcmuWHVABaeG4Iyl1TgX4qV3T8E8_TrndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koZfyGYgPGO-p8KZyRAMhvZI7W9tP1bDlg6Y1BOukPLnQo5TKXSzXn7i8f7Gu-YK0Mf_ZpshT-YwjsQ3QZmHVcV7TGRWhr6A9v0653ibvSobMGHPgCUG62KKWOZqZ9g2U44jY-oYwgI2hwHwQ2VU9RGTXpmVn6XahR4pvtbxGQIQX_KjP8E94CUmrABmXspTclLfR7TS84B2YfGc4hKAlOPCSh1yeinalqK8BfF0whn770YWrUnLPgV2g4I5drkHQvXqcZSakWl9kNMMs3gzZ7bT0r2tfqb8ZYXrVxYpCMQOYId5xfT8MqmQwtUoy8hT2urGBBlEo52XRWBQSJXE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpZ1gmzlehT9wEKpI83NvYUJYpNA60qUg65klSMksMR0XI_xdpFOZBmXchh2ka8EsekF3_dwNnv-fTLHtALjiHJdgy-pHYK_TPhx4gzJvDg84kNNoN32j-no-HV1fCRcuwoj-lRYoXU7wgoWObBCHzU4LDlDXOSRpqD_DVpTbKGLwfMowgM_AaFOeI1ifz9w5yJcyRJe89-dujSzUzu-mffa2xWLsxcHmKTyWNdLGgD07g4Yd-1Us8rC26zjT1jUHVkXHpTlBAXpwiglk425kpNRlAZF3TW94WEalMoYdLDw0O82zYWlz9U9U_m3dCywqTl4GRVWiuE-dx7HnIiu1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pneJbrPsbxcQqvSEYc0MUKRQjWdNHKHaluACDSH303OG_Nnk0WVZ-TXjzjFOzMGAES1v1o9QQzihnZVB9gJ13RmoLVMovUaUNiYoKthKzj7GLfAOsM5MhShaUqJs9opFSlZdgviIvbz2NbKggIIIpVWU1Lxye-45sUMNAfajE5SR7gTiQO789kqb64SEcuov1c4Bm_ZwcOB_sxJ-yFYzhzlUJCkUwNuoiv3NxPBtT7mb3q71GfWKmGhAhQT5uwnDGWjop7OxpuUSxZ2rJrghfsiTMohPek63kJfCJheIoge0kUMqZ63qp5yThtJTBveNNN3H0AeWEyZDgryPbKFSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=UzLcxV3n-FSdZ_zBOnXmKO3x6YXCRkoDsZatl6dXgeZtigwDHMJraQtNaoS-U7YC2qZcOZ2i8rVgsfZQYmTz_eliwPexvENWi7FFmYCNGaQr3tTCvL8Qk8j746XAV-4jgnyQlxYZ2klV20F0sPS2D-pIGlOdjBpVo35DUEydCxj2eLu8NDlq_MmzbKZwtfOG0WKoYz_W-ePgEGvRla2tFK30K-SVjXP8qUj9N4z6mkpM4ihOryJp0zPh6L43nzhOzceAiXGfxeHl3a8PZKlmQYrD0eK1pg1cyOqnK51rECDJulw0ekRRGogTARw5xw87b3i_DRa80gO_lSLaqlZHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=UzLcxV3n-FSdZ_zBOnXmKO3x6YXCRkoDsZatl6dXgeZtigwDHMJraQtNaoS-U7YC2qZcOZ2i8rVgsfZQYmTz_eliwPexvENWi7FFmYCNGaQr3tTCvL8Qk8j746XAV-4jgnyQlxYZ2klV20F0sPS2D-pIGlOdjBpVo35DUEydCxj2eLu8NDlq_MmzbKZwtfOG0WKoYz_W-ePgEGvRla2tFK30K-SVjXP8qUj9N4z6mkpM4ihOryJp0zPh6L43nzhOzceAiXGfxeHl3a8PZKlmQYrD0eK1pg1cyOqnK51rECDJulw0ekRRGogTARw5xw87b3i_DRa80gO_lSLaqlZHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=i_MCp-x_RPXxF1hbMHsTfZyOrV4VrwuqO0o9UY8TM4Mdw-7BEf4nVBvQHP0i8Jclbmz_i5fZsZVbpOdhlr8ynS3L87xcaTzwhR83-0vwecIMNOvAHFvFnhochspr7B_Eo8sL6yfV72nrcD4zm3Y3iZid-wnArOkwZvP0Bszgfb65XCWdefzUAKJ64CQfGUAGiWBlzYF0-Zybmwwa4ONwt3KRzr3qhX07XrNbKnxRooA6sH_pqmA7NSrenbIJITAgtxfAuCD_-5GDphZPUSpBISESKVjTvrXi6y0VjHxPFCsf-dwhZdu4dvuVMBm_sAOJNzxS29qM2iqHtaluMlussA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=i_MCp-x_RPXxF1hbMHsTfZyOrV4VrwuqO0o9UY8TM4Mdw-7BEf4nVBvQHP0i8Jclbmz_i5fZsZVbpOdhlr8ynS3L87xcaTzwhR83-0vwecIMNOvAHFvFnhochspr7B_Eo8sL6yfV72nrcD4zm3Y3iZid-wnArOkwZvP0Bszgfb65XCWdefzUAKJ64CQfGUAGiWBlzYF0-Zybmwwa4ONwt3KRzr3qhX07XrNbKnxRooA6sH_pqmA7NSrenbIJITAgtxfAuCD_-5GDphZPUSpBISESKVjTvrXi6y0VjHxPFCsf-dwhZdu4dvuVMBm_sAOJNzxS29qM2iqHtaluMlussA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTW5RN3aoH0guWa1AsJOtNaVyp0yRWOeEJlp_ou6QuP8VFpBMmAITk2FiFzvrZ8gm7X4r0xVqHgA2NdnZHvCbomB1OM4R9zx8KY4Qt7Ex8TI0xmCH4mtpdb_1XHv7Qr5hWvor3AZHwB-PE4tPkX2ZsG7KH2ahYT74qoIEdAeEJuC7XvRsjA0vuHdFlod513ktHydJgukHvUG3v1Ewm8rctFKsdeKBqvfGmB8gmLDWGYw7UvrKn_nLQ4g3d2N5NdlTdVbfr3Kys5dFjDUTRYyqsC8ZisaAMKMG6mQ2Of1-UX6gcVQ_bkJVtrva9nFEd2cIV1K2SLRt1zNJVPuNG9kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=OsdxlgEX4Dn9YmGBfFdvVnWUoDZR4Zt6DrHC7dvLZUsB8oLQEEeoz82l6PL-sRc6KJ3Wd9tfyCFbKDlc27XDn4sUfV6ypQMIqLAk3qI7-FjZPheYxD-5mcg0tVGcJrQ26DMcugCUBKU5l0rx8meKdLBQwltLlwwf1CQWqQGLhD-wqhiqc_0TtIVUGHKSxOkh8lJEaY5rjUKMdxfXVVAIjxT1H-n7sxJJuLpKT_kvf6LwvXUNRP5dkSPHF1aeV1Yzb-mSWEDisYFtu9OHBRvNgOdZteoeYnUilZCDFOkkg5_DOMhhVr8MhexY245Vox_0WjdmV4ncx2VySOMEqhFH8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=OsdxlgEX4Dn9YmGBfFdvVnWUoDZR4Zt6DrHC7dvLZUsB8oLQEEeoz82l6PL-sRc6KJ3Wd9tfyCFbKDlc27XDn4sUfV6ypQMIqLAk3qI7-FjZPheYxD-5mcg0tVGcJrQ26DMcugCUBKU5l0rx8meKdLBQwltLlwwf1CQWqQGLhD-wqhiqc_0TtIVUGHKSxOkh8lJEaY5rjUKMdxfXVVAIjxT1H-n7sxJJuLpKT_kvf6LwvXUNRP5dkSPHF1aeV1Yzb-mSWEDisYFtu9OHBRvNgOdZteoeYnUilZCDFOkkg5_DOMhhVr8MhexY245Vox_0WjdmV4ncx2VySOMEqhFH8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGPNVHKsYvqVsB-gALyNxO6ZenmBXysYDb9896V4TufqnrK-8N024M6kjg3Ev6Ct1oD9gX2YxuZ7pcnwMerXgIs4bYap6u8zcnpJ49kHTHLPD2vlOjHc3lCGX9H3k1MyDHvtweIQBvMialjQepSE-CwbqOZF_hDCv7bEqcM784_MHfzOKQPP4P-AC7RvY-pCZDa6xgBMStbDVfovzs1KqPXP1fprTC77MdyM_-amArK_dRh1ieaTc5qYxSxwL5xqnZIjJCAbKFZgan-vJZkDkVJj4Wp-Of_PgMdD-Tu44ZKWaUPiyFLWLnsFYnmC_fXX4d_xe9MAjBdijHCbRoYABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
