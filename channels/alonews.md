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
<img src="https://cdn4.telesco.pe/file/KpebWi3jpUVCimGycKlS_HxOxJKDa8hBP1YHkL9Jfol61RhAAff9XI3AQ1RgSg4_ctR2S--424UtHzSjKOalZxVdKMCmWro5iDkjlG4ScG-MumznVo99Dl1mJZcDp47GS5Dp-5PvKkOGNmzR_84vqAUPxN7hG7GtJZdCNZ0wc8YW5gPkM9KFxl4E0H9Eou0nixA-eBu9bmKBdZDIw-h_4rPCbDNiqKoRJkqOH3Z08nLw8PhIc3YNawXnE6ia3Xz44Sq9MbpHh_fiZNBSnMmgHy5CIqbl-dN4kq9S7fMZFlvTKyEGnfuFz0Rg2BZe_Cm8TGOEWGT4JAfKgXqBW_ukxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 964K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 12:21:37</div>
<hr>

<div class="tg-post" id="msg-141790">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPccfOWKlehrcDOB8OOutZZy4jolaGmSbBTwyxYnywWU7TQdkDpx1ULCcQwDHqRX60xLu_P8oKdyZ_3RdXpj8FQDB0yTTjOHk4wHhCzStmChD0WfAPvXQlWRfEQd_gwtb4l09l7JR9MRSCs4IJ_r0dimLszwIp8h5kM8p5pZElRYyN9LMDhbMN0DmtxaqVnQVFaMpliC8aI1PFEPaY9M8-IvxIT8Y2lL1sVeTpsZhylsuOLiAgSaAkwuZbItzojOC5FDLPASkzgtWlq4VlD5ojelCuH5H0O4DrYtkALcFzitSyTeainM2zBYk4MnWxiE2eyLIow9MPokAYEBr5uG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه جدید کارواش خودرو در ۱۴۰۵ / روشویی تا ۶۰۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23 · <a href="https://t.me/alonews/141790" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZd0qnF8Flv_KApoDm8OpP0eKe4FuMsoTs29gWEwBatL_77rx4xIzS5gddWk42YSC17uOnwS8YDO20--DQMKWE8wd72PN8vIPFN_nJ1zGaySoSsszgxNsseHsfKbPhcXtL3WSsG_q1qrELkFRJUZAXfP5oR507g2Z-4VCveeym10slGHRYa6amp7CF-sF8x2RbV627UxsLREyZaubQm_HKRE56flwukOrFF37ANRQljzMCm1bzrfYi1zeuZNqBtnATAmD8fYwNgiW5U1rZQc8CDoZNNAHXEKsq2d_qn7xZ1fHT5pmlTf1-b6j4K8V9S3vT2zcB1z9zSnuWZVUHtkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMTgnENhkkF1wgssoti5toK8SJ6TZYE8yqhiNe5oZUZSjssdXPubP4eHGy5NT9jFOkna34Ex0iLm707hPmEFqSwjppph3Imq7gQUJ4KYeHiIwUrDjGjQD4izW2_fYRGC3MrIp8BdQjFC2IjPThtBQI7jgIaq-V1XZkprDcggSQIcmiXPSvbcIZfxhreAALLjCa_5EK7UAmIc6ZXSggdn6T6EqlcFuJQ8ZWJVW4QyUMOGjtW_7uhZ7pPObbhpfcoqIgogD9kkPj6DyFtJE9n5ISxIcMdtrxg8KfNM3mDskdmQ6ci8X3ZXZEQFl9DCDilxEHYX5bXJu_DiMtUax2pkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKFJ5EvopFIe5AZ2Yr2CDOCUnQ07gOviv6MPq0Cn7SekdkaAOmKkPgpBetcPljj1cymk_9o00GU42OrNuufpdWc8D9IHIpbFSsJBVlZb-thTqzoEZhxyOvlfY4rkp2svl3wolLS436Fh45fbcOSZEQaElJDocWC8Mvv8OD4Nu9fsdwjIrm3ECBR_fx7H6I2MKgPrWTMXpzcRLh7cMRvq0b79H_U9_GzrJqCG_CpC6A9jlCoysm1p6OKy1FHeX7G03wz2nbCXn2zkpdIwcVmPgd9UVO__EV_kY0jbhAaqA7ydoBO442lYVXE4ti8J3b0bcWoDg0ycFiK_HF-G_Qtt1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ، چند عکس تولیدشده توسط هوش مصنوعی از خود و جورج واشنگتن را در سالن جدید کاخ سفید منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/141787" target="_blank">📅 12:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czSa-dsVNCcHenJS-zuQj27cyu4KMxrYa320g6z5RhPONyMDSfVBsKfdBPxJcTJg640q0iBfAUTzN1NRi2pGa5pCifwL3Ob7srE2voBXOtwUt9YDjwMfhefykb7gvNRRmqCHk0ZrDxV6wutPnZxn9uBzYBAMawYKYq2kV5vhTuz7ldIJPGGWw0i_TDqpI4bBCfFNIl63BSBGtllcDGpiTzzUKUzcX1IYgNXX_EyMdWnrJqp8mB6kQI6Dr98KoMHIqXy-U6go9MvYJG32n-kMmGX8smeOr_5McoD6GhL31XeX_qSPzCk8s2L5YLMmPila-fjk7waVt4zcVEvI525R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفظل اقبالی از نزدیکان جلیلی: انقدر وضع حجاب خرابه همه مردها تحریک میشن حتی خود من
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/141786" target="_blank">📅 12:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/141785" target="_blank">📅 12:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سلمانی» معاون سرمایه انسانی سازمان اداری و استخدامی کشور: بر اساس اعلام وزارت نیرو تا ۱۵ شهریور امسال ساعت کاری ادارات از ۷ صبح تا ۱۳ بعدازظهر تعیین شده است و بعد از آن در صورت درخواست دستگاه‌ها، تغییر ساعت اعمال خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141784" target="_blank">📅 12:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ارتش اسرائیل: به حزب الله اجازه نخواهیم داد که به نیروها و شهروندان ما حمله کند و به از بین بردن تهدیدها ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141783" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953b386e17.mp4?token=T_OO4UQbnWRNlNs93bzva5grFR3HqmjnnPQHRMHlxIxCuBaPbeVblLStto5F0i26mLUR06x2ZKj1EPzMDcnJGD6vAvFrD5z5zRFO0LruFvQeCHruX0sgcoQbtrRMeGwI-2sTUlJup7xzNO8O-5YGtuHgc8F_65AUmPmQIuazjVDUxbjPCstNzoUtOfyyavmR-t4qporMkc9Yb7y_pAUvL7eYKhk5zSizsp3BYps1X4GSls-0NuA2F6g7IQLlmA9FmBdW_zjrA6exCL1JNvAIKz7YfC-pUDCdjaPWwt7W1GckTEgTo7tI--J_-SwU3136J5eY6iI3loHs8U72l7h1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953b386e17.mp4?token=T_OO4UQbnWRNlNs93bzva5grFR3HqmjnnPQHRMHlxIxCuBaPbeVblLStto5F0i26mLUR06x2ZKj1EPzMDcnJGD6vAvFrD5z5zRFO0LruFvQeCHruX0sgcoQbtrRMeGwI-2sTUlJup7xzNO8O-5YGtuHgc8F_65AUmPmQIuazjVDUxbjPCstNzoUtOfyyavmR-t4qporMkc9Yb7y_pAUvL7eYKhk5zSizsp3BYps1X4GSls-0NuA2F6g7IQLlmA9FmBdW_zjrA6exCL1JNvAIKz7YfC-pUDCdjaPWwt7W1GckTEgTo7tI--J_-SwU3136J5eY6iI3loHs8U72l7h1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
تو آخرین حمله به ضاحیه، مذاکرات رو متوقف کردم و گفتم اگه اسرائیل جواب بده
🔴
کل منطقه رو می‌زنیم، همون شب محاصره رو برداشتند
🔴
وقتی ترامپ هم درباره باز شدن همزمان محاصره و تنگه توییت زد
🔴
تهدید کردیم اگه حرفش رو اصلاح نکنه حمله می‌کنیم؛ ترامپ هم پستش رو اصلاح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/141782" target="_blank">📅 11:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c188240e7e.mp4?token=Ut4gugewPmvgK04EUOuxQoiFOsvp-is1O1zV6L3kLYFN7bQw-g2Z21XsaNM0y3oCuN7EI-FMcytS1B8gb-J68MOo25fEv4eLT_QVyGJdWiHFcHfdPOZytjg0yz3BUvk4geKakO96L0QiBB_hHutWN2E6n6qUmniQUIe3xumvdpkSBlgNiUIC0ckmVmL7uYqb4ridFvA2AlKCQDlBnKGy4dtii4LxGpVhVwjvcz9tNvM0wZtJw_PTwEEpqcT3hHMRV0IcklHa9kB7PPGHgkM-D6KrQP2UtY_s5qY21TaAxU1QMXzr5I9OlK3cBmOpRjKsUpPF2e8V_vNhmAVeDoNJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c188240e7e.mp4?token=Ut4gugewPmvgK04EUOuxQoiFOsvp-is1O1zV6L3kLYFN7bQw-g2Z21XsaNM0y3oCuN7EI-FMcytS1B8gb-J68MOo25fEv4eLT_QVyGJdWiHFcHfdPOZytjg0yz3BUvk4geKakO96L0QiBB_hHutWN2E6n6qUmniQUIe3xumvdpkSBlgNiUIC0ckmVmL7uYqb4ridFvA2AlKCQDlBnKGy4dtii4LxGpVhVwjvcz9tNvM0wZtJw_PTwEEpqcT3hHMRV0IcklHa9kB7PPGHgkM-D6KrQP2UtY_s5qY21TaAxU1QMXzr5I9OlK3cBmOpRjKsUpPF2e8V_vNhmAVeDoNJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
در تفاهم نامه، آمریکا می‌خواست ایران از موضوع موشکی، هسته‌ای جبهه مقاومت و تنگه کوتاه بیاد
🔴
اما ترامپ در نهایت به‌رسمیت‌شناختن جبهه مقاومت رو امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141781" target="_blank">📅 11:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
‏
🔴
همزمان حملات راکتی از سوی خاک عربستان به سمت منطقه «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141780" target="_blank">📅 11:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrG2PAWGhBKk16k0VserA684I7YQiCwK6RozE2URqTn8Y9iNfFbiDL6g81BAt6DyOw9tEywWzvMVDOt78UWxCUispk6BKN6Y6-IipZDmix4IBPt9xiLRmAgWQDw1-ySjPqWceVz43qk1pqJaWbpb-6Iew-A9JYwHAP3vi0GCv1Im8lo65v_Q5L8u3YwzMypOQQXaCbwRtre-isOL_-grVS8YzTbo4Uspk74-EF1hVeotuMGNm-_pp4C2bJiruC0hIQtHI5ZPZ7sniADnzUPouvmufekWaWGhvkQz5tPJvDK2gQD3IuWUDprdTo7ciEmbOyNrgI31ZZD9WpIlRi3GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از اپل می‌خواهد که از خرید تراشه‌های حافظه از چین خودداری کند، زیرا افزایش تقاضا از مراکز داده هوش مصنوعی باعث کمبود جهانی و افزایش قیمت‌ها شده است، بر اساس گزارش وال‌استریت ژورنال.
🔴
اپل در حال آزمایش تراشه‌های تولید شده توسط شرکت‌های چینی CXMT و YMTC است، اما اعلام کرده است که باید "تمام گزینه‌ها" را در نظر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141779" target="_blank">📅 11:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2JGP2vrnpzCY0z1B2UjG1EbGOL6h0-uma_ClddT4DikfqBSYpwhXGmty53gE4bknnVkC_5bNTryI5CgLDCxdU9e-RKJ6BTwEZdjWbABx978eB5xs3knAqRB5OvIieW30zdA8LML5GqIydMkBEMw768YDlyT9fB-DrMIh156EOD2KEaN64JUb_Y_SbIgw_qtEXMub03DDIdllr26K9ZOvM8kax4Yx9mwTA9uA1XIkAWVMTm679ClYd_laTSh41p3ug6kssyzh9t_0qgcWRoL2nJR0XBKIxFJMduquCtiTv0e_J_aJ7pe1QkbPcAAkCeCxVRjDo3UA2fjL8QWxyH1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141778" target="_blank">📅 11:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNOffuOJc8UK1C7mJO-nMMGPx3RZTYrrwTQ0fIzJo09ztD87-09tWqLntVZCZqUnjw-ot3uEXYA1k6ubh34b1FEsTgP57HDMvLCZH8aOqhHGs4NO6b-twhkX-NdHBNSms73oZ_8lSRPj9U9ixAPrqu43ENhhBJI4dWv5zasn_Dk4iuS8-fAAH6rbs7zNeTXf42-y_iToPLr2ivrBNFmvRhlfvA3Vd7D7sLHZN_7SbKCk6j_j-sHml7aWBN202jaZ9oKSlx7o6r5WU4iRTOAtt73M4A3k2a-6xNO3RpEb9Hal8peggz213eAAfiCqvzP4VJYLAQExV0h_mqXz2xvi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه NYT : حمله ایران تو روزهای ابتدایی جنگ به پایگاه دریایی آمریکا تو بحرین
🔴
این مرکز مهم لجستیکی رو از کار انداخت و نیروی دریایی آمریکا مجبور شد، تدارکاتش رو از جزیره دیه‌گو گارسیا تأمین کنه
🔴
مسیری حدود ۲۲۰۰ مایل دورتر از ناوهای آمریکایی نزدیک ایران
🔴
این مسیر طولانی‌تر باعث کمبود و فشار بیشتر روی ناو هواپیمابر آبراهام لینکلن شده
🔴
۵ هزار ملوان این ناو تقریباً ۹ ماهه در دریا هستن و هنوز وارد بندر آزادی نشدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/141777" target="_blank">📅 11:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ملیکا همت‌زاده، دختر ۱۳ساله از روستای دسکِ بنت استان سیستان و بلوچستان، پنجشنبه دچار عقرب‌گزیدگی شد
🔴
به گفته اهالی: به‌دلیل نبود امکانات درمانی کافی در روستا،با خودروی شخصی به نیک‌شهر برده شد
🔴
تأخیر پزشک در نیکشهر و سپس اعلام نبود امکانات کافی و لزوم انتقال به مرکز دیگر،روند درمان را طولانی و ملیکا جان باخت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141776" target="_blank">📅 11:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کپلر: روز جمعه تنها دو کشتی از تنگه هرمز عبور کرد؛ هیچ محموله نفت خامی نیز مشاهده نشد
🔴
کپلر، بر اساس تحلیلی که انجام داده است اعلام کرد روز جمعه تنها دو کشتی از تنگه هرمز عبور کردند و هیچ محموله نفت خامی نیز مشاهده نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141775" target="_blank">📅 11:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
حاجی‌بابایی: مجلس می‌تواند با رعایت پروتکل‌ها حضوری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141774" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=m5bxirfv7FAiPB1Auw43-JZocQlrSD_PpGDiroeAoaeEE4Gr_cotVCrx0G4RwteXgWo6qQ2IlR9dlYTGHe9ozNCrdwuG33D3W-eNwCXq13EfBO1GGSce8GoDVVxtfokZFZtmXatBTdZunyG3-JnwKF6Xk0WXaQGpHFdKmpy-tGcSEayynkdjWz38Q2EiUzYaq58z7nqFh7PejGxlxiSEkcdOhje5WZz01SP1Z1bY1iwvCs-f47mSj3uH3TScsWaHSc73yc-FVyUBuDokR8zMYnqf8PfORvjH4ntX-Fxk1HnaMhzjcpldmKuUTlqMYL86AEPiTs_WbnWbd1AOO8XdDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=m5bxirfv7FAiPB1Auw43-JZocQlrSD_PpGDiroeAoaeEE4Gr_cotVCrx0G4RwteXgWo6qQ2IlR9dlYTGHe9ozNCrdwuG33D3W-eNwCXq13EfBO1GGSce8GoDVVxtfokZFZtmXatBTdZunyG3-JnwKF6Xk0WXaQGpHFdKmpy-tGcSEayynkdjWz38Q2EiUzYaq58z7nqFh7PejGxlxiSEkcdOhje5WZz01SP1Z1bY1iwvCs-f47mSj3uH3TScsWaHSc73yc-FVyUBuDokR8zMYnqf8PfORvjH4ntX-Fxk1HnaMhzjcpldmKuUTlqMYL86AEPiTs_WbnWbd1AOO8XdDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یه نوزاد شیر خواره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141773" target="_blank">📅 11:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وال استریت ژورنال: جنگ ترامپ علیه ایران به مسابقه تاب آوری اقتصادی رسیده
🔴
ترامپ تحریم‌ها و محاصره علیه ایران را تشدید کرده در حالی که تهران روی این حساب باز کرده که قیمت بالای نفت، واشنگتن را مجبور به کوتاه آمدن خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141772" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE1kL1hMGM4jOlcLxY9slFlx8fWfeRO53eQKPom708C1Tn4FF9MqzumZWppBryjfvwvWcsutuKpY1sZU9vfgCVjlRT3OSWxD2mkqnQLUsbZ_mIFrKfdCFjGN4Vp8L3ZaqjMixzc7hTEdPHJFD8vxPmXI5A352EcubNB950MkQ1ZMe5U-RSnlYzgRaicBqLYEHOkc20GpPHMfTR4hWo8-juowriuweSebAKlNVz_nKxDLfuclrCBYBnjPb3WgF3AuNyETm1k1vM78fK6Ipg2K04ZlHcHmP5VIY0zumzRip9C5IjtaMrJI6Bz7NNp7_efAhqqmRuZuyWcRXl04PNEg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141771" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0azIXMuNwyBe01MywSivaY7MCBlJe9nTS6-vz_ep2Nx5nsCON2sT7syRkUDxGVfRhCi37huBGFJiRT6Ftt91qeJ_dpW81jExbsvv3Ed1YHwkxl4L4lZVo2NzaOpjlzt3EC6GnmAT51rlXy9buOxAyUwAYbYdFDLC0OEDG7iYKgBstVPWYNFpPq3uee2Az7PieCjiyTPfvB5u81JE4L9RzMqpyf8zTs6CHzZAS0NZctoQQhMcd7l8s4rYQEt0KgQPAjJtdVMcZmZr6ieiN_vNHA__pnPCJ95jK6IG57SDq-EklHdJcI2ulDCkxQry9meAT9B1OhguUrk_9RFQXn7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسماعیل بقائی، سخنگوی وزارت امور خارجه: این فراز از رمان برادران کاراموزوف نوشته داستایوسکی به درستی وضعیتی که سامانه حکمرانی و سیاست خارجی آمریکا در ارتباط با منطقه و ایران به دلیل اتکای افراطی بر دروغ به آن دچار شده است را توضیح می‌دهد:
🔴
کسی که به خویشتن دروغ می‌گوید و دروغ خود را باور می‌کند، سرانجام به جایی می‌رسد که دیگر حقیقت را، چه در وجود خویش و چه در جهان پیرامونش، از دروغ تشخیص نمی‌دهد و آنگاه هرگونه احترام به خود و دیگران را از دست می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141770" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq-Mbo0XA7hlI8Xu69RBvmiIzmfwrvTE8CQ5Sb50jJjIRymoBKQiDcv7vfSgpHVjKNfstCc8GI4_8EWKxrAV0uXgOt6oDUsZDA7mL3ip65OHcKUQYlnuk5VeJk4R9HLTm-b1xhhbRrQ1u39E2skfNNVDbXIExHYpQtNVAYIBcFYb5qHvaSbPWRA-hhVSvpisi1C8-RJS_5NkrjC27T4ZMDDNCdiQ6HyjoZQfOXRxcQ8iAT3hT-KyAFSvPoIXdRfISeQRQCL1z3FM_97lF44R7bNoHQUIS_XrtVXXknuRAgz-lWGb2P5V_fKGUcUq9bRj3Vm-hh4ayV-exTHoJpyGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد اسرائیلی یک وسیله انفجاری را در ارتفاعات علی الطاهر در جنوب لبنان رها کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141769" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
احمد وحیدی، فرمانده کل سپاه پاسداران : رزمندگان ایرانی در شرایط بسیار سخت، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردند. انشالله به زودی با پایان دادن به درد‌ها و رنج‌های مردم منطقه، جهان برای طلوع خورشید عظمای ولایت، از همیشه آماده‌تر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141768" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روسیه: انبار حاوی سوخت نیروهای مسلح اوکراین در بندر یوژنی را هدف قرار دادیم
🔴
وزارت دفاع روسیه: نیروهای مسلح روسیه انبار حاوی سوخت و روان‌کننده‌های مورد نیاز نیروهای مسلح اوکراین در بندر یوژنی را مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/141767" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قیمت نفت صعودی شد
🔴
قیمت نفت خام در معاملات روز جمعه بازار جهانی، به دلیل حملات به نفتکش‌ها و عدم پیشرفت در توافق صلح میان ایران و آمریکا، بیش از یک دلار در هر بشکه افزایش یافت و رشد هفتگی چشمگیری را ثبت کرد.
🔴
قیمت نفت برنت با یک دلار و ۴۵ سنت یا ۱.۶۷ درصد افزایش، در ۸۸ دلار و ۵۲ سنت در هر بشکه بسته شد. قیمت نفت خام وست تگزاس اینترمدیت آمریکا با یک دلار و ۱۵ سنت یا ۱.۴۲ درصد افزایش، در ۸۲ دلار و ۴۰ سنت در هر بشکه بسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141766" target="_blank">📅 10:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/141765" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
👈
اهواز ۵۱ درجه‌ای می‌شود!
‏
🔴
رئیس مرکز ملی پیش‌بینی وضع هوا: اهواز با دمای ۵۱ درجه سانتیگراد طی دو روز آینده گرم‌ترین مرکز استان کشور خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141764" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-46Bu1ZIBOCa9ptv5yasMJlaQ0jQMEYEEIRzw5VhjfXtD3oxIksA2wgSirnNw4WUKRvd06AfNj5DwzKOApCW5gA5C7WbLHepMnMwKukcxDCwl4jUeBm0A_vCXA8rCJZJKUZMzJMcAPZ0ktVAZK6fWUqyRv7xH_ahKO8XtmEjnm2Qsu3mU-iJNT4yHIAmjPoZrcHQFvCS5zAb5u2-UZ41YnjQdiudv_5i7YVpdBqQYDdmQsuG4dr3tZImwcsiKquW-xxSvitigsINlSgRSEwPwmKfz0l9EqNEoeahJ07J979o6dpYx2dqxSd-GewVVXh6BzHhbXiEc9lKY-Tzy01Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فرمانده نیروی عملیات ویژه سنتکام در خاورمیانه تغییر کرد
‏
🔴
فرماندهی مرکزی آمریکا، سنتکام، اعلام کرده است فرمانده نیروی عملیات ویژه این نهاد تغییر کرده و دریادار توماس دانوان جایگزین سرلشکر جاسپر جفرز شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141763" target="_blank">📅 10:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141762">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
حمله به نفتکش شرکت «ادنوک» امارات در تنگه هرمز
🔴
شرکت ادنوک امارات تأیید کرد که یکی از کشتی‌های این شرکت هنگام عبور از تنگه هرمز هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/141762" target="_blank">📅 09:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
حادثه دریایی در نزدیکی تنگه هرمز
🔴
گزارش‌های رسانه‌ای از وقوع حادثه دریایی در نزدیکی تنگه هرمز خبر می‌دهند.
🔴
سازمان تجارت دریایی بریتانیا: گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی باربری در تنگه هرمز دریافت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141761" target="_blank">📅 09:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bb640dd0.mp4?token=J_diY08OlLyvM866L7XZT19uOyny12lmrQb_brunHdA0CZudYJ5GDb9118ZY7mTJfD7veOgkfo9fn42JsKPtPX5Egft8L08nuC564JQgXctdYS06ML4wKkvNWFymHK3T-9JLi_njiulMr6_IKMcmm2aR5hlfktSzN1Vvuokqci7ryTVrZKMpJOA13D3mKGK0ZrY46ATQzRQ9szul0emC20wUXu2Ffi8mqW7c-ggHEngM67EoAKSljCVVDrnD8hbyq5pIzuBkVwTPh70njylxhHJbq0g4-nHpzta13nHz5fMMOFxTcKOzv0Pg8YVtzwb3in59O_t23mu2Xz5ceCWrAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bb640dd0.mp4?token=J_diY08OlLyvM866L7XZT19uOyny12lmrQb_brunHdA0CZudYJ5GDb9118ZY7mTJfD7veOgkfo9fn42JsKPtPX5Egft8L08nuC564JQgXctdYS06ML4wKkvNWFymHK3T-9JLi_njiulMr6_IKMcmm2aR5hlfktSzN1Vvuokqci7ryTVrZKMpJOA13D3mKGK0ZrY46ATQzRQ9szul0emC20wUXu2Ffi8mqW7c-ggHEngM67EoAKSljCVVDrnD8hbyq5pIzuBkVwTPh70njylxhHJbq0g4-nHpzta13nHz5fMMOFxTcKOzv0Pg8YVtzwb3in59O_t23mu2Xz5ceCWrAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلزله‌ای به قدرت 7.7 ریشتر سواحل اندونزی را لرزاند! ساختمان‌های آسیب‌دیده در جزیره فلورس، اندونزی. گزارش‌های محلی حاکی از تخریب چندین ساختمان در این جزیره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141760" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/449d6fd03a.mp4?token=I753F18c-joQT9jnfWmRmBjMY8JG_9CC9IxeAKmgVXOCmyN49KKm-78cWDRNnlWeyu0tYTM7Y3fXlfkT34lS8MjyFxP0FA_nVhu_ib2tTxQ-d9Md-KJACY66zjhhpWKRPGmAc3KXDRtd2Stq3e43q7PHwyF86QC2DiFacj4VcwD7etWFSeEE94hJ9fl8kgIUZCrlrjF2JiU-FJQCTP9bUkvnCbsLvNAEf7lOmr6K19iIHsSTxdGwGcdCosbzGQN6Qo10arSRZVe1huRMZTgoWQhoAuBtQqHXI7o3dJ-cMQjwYyfz6QGm8pmX617clMJLmUumzMBd1xNdpSWVziirMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/449d6fd03a.mp4?token=I753F18c-joQT9jnfWmRmBjMY8JG_9CC9IxeAKmgVXOCmyN49KKm-78cWDRNnlWeyu0tYTM7Y3fXlfkT34lS8MjyFxP0FA_nVhu_ib2tTxQ-d9Md-KJACY66zjhhpWKRPGmAc3KXDRtd2Stq3e43q7PHwyF86QC2DiFacj4VcwD7etWFSeEE94hJ9fl8kgIUZCrlrjF2JiU-FJQCTP9bUkvnCbsLvNAEf7lOmr6K19iIHsSTxdGwGcdCosbzGQN6Qo10arSRZVe1huRMZTgoWQhoAuBtQqHXI7o3dJ-cMQjwYyfz6QGm8pmX617clMJLmUumzMBd1xNdpSWVziirMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از ویرانی در پی حمله هوایی نیروی هوایی اسرائیل به عینسار در جنوب لبنان.
🔴
فیلم‌ها همچنین نشان می‌دهند که گروه‌های داوطلب نجات انجمن راهنمایان ریسالا اسلامی جنبش أمل، حزب سیاسی شیعه لبنان، در حال تلاش برای یافتن لبنانی‌های احتمالی زیر آوار هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/141759" target="_blank">📅 09:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAEKMONJQwngzEVRU8sIlud3XPAim6XtvHmrqKa7v0_SBzUOgJ9Zg8QGpCHMRapn7g8CvnxfTXRTl-vlAW6jFB3IVDwO0G1HIB7qknHev46GvtpM7vehTcl4cDrXcELXOz_B2eKDdSAuYQJMSbGkGa7OdrWcEj8jgwpOtbs19Lp4rwFQazk3wtYdTKBpAcSBcbd88i7DJfWpD21JmzLfuUWRnEbdD_8Hj6J1zlbRhIJqdvMWcjFHM4K-K_zTYYe47x1gfd3QPHmElN-zZh3RDmlycyGbe1z7C_kV2DGrYYJyaVH4xcChpbL3Ikxo-OXJWzsL7LC-5-ELmPMciylFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس از حمله اسرائیل در نزدیکی قلعه قلعه معس
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141758" target="_blank">📅 09:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141757">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e6980068.mp4?token=d9vnGhyINUsSydm4BegJ-4KwQrX3SA91EHbCznq-czAuJXVrakyi93rZAOdiPr2Ox3i8Z_JOln-Ml2VesFMeEbsFIPMGmIZBemfa6H-4g4ax37sB5C0knolP33CzWiDoUFJsthimJaMIwQfDFC6DEBoEB520411bmlINpcroTa2MKzVI5sgQJQv6bEEkgOKib5rF9m_GyZYOheqxN26lGatCZuBFYQv5iymrBSLwBbGMqaOip8HEkiiIbqsNISHcvA7qW5P0Z3tkwWzJZb0HZtiISJTNXhpQTp-YBP46Jqs2a52IhBFgVeOtRlBSsAoZ8DSLX-i2m_qCIFkj_KYUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e6980068.mp4?token=d9vnGhyINUsSydm4BegJ-4KwQrX3SA91EHbCznq-czAuJXVrakyi93rZAOdiPr2Ox3i8Z_JOln-Ml2VesFMeEbsFIPMGmIZBemfa6H-4g4ax37sB5C0knolP33CzWiDoUFJsthimJaMIwQfDFC6DEBoEB520411bmlINpcroTa2MKzVI5sgQJQv6bEEkgOKib5rF9m_GyZYOheqxN26lGatCZuBFYQv5iymrBSLwBbGMqaOip8HEkiiIbqsNISHcvA7qW5P0Z3tkwWzJZb0HZtiISJTNXhpQTp-YBP46Jqs2a52IhBFgVeOtRlBSsAoZ8DSLX-i2m_qCIFkj_KYUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در منطقه علی الطاهر در جنوب لبنان درگیری‌هایی گزارش شده است.
🔴
به نظر می‌رسد عملیات نفوذی اسرائیلی در حال انجام است. این اقدامی است که اسرائیلی‌ها مدت‌هاست به دنبال انجام آن بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141757" target="_blank">📅 09:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141756">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رئیس پلیس امنیت اقتصادی تهران بزرگ:بیش از ۶۸ هزار لیتر فرآورده نفتی خارج از شبکه توزیع در یک کارگاه غیرمجاز کشف شد.
‏
🔴
ارزش سوخت کشف‌شده بیش از ۴۶ میلیارد ریال برآورد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141756" target="_blank">📅 09:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141755">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های هرمزگان: پروازهای فرودگاه بین‌المللی بندرعباس از امروز  در مسیرهای تهران، مشهد و اصفهان از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141755" target="_blank">📅 08:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141754">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دولت انگلیس در پی خشکسالی شدید و افزایش خطر آتش‌سوزی، برای میلیون‌ها شهروند در سراسر این کشور هشدار اضطراری ارسال کرد؛ اقدامی که در تاریخ انگلیس بی‌سابقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/141754" target="_blank">📅 08:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141753">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2I3vNHXKWHcAdvGv6Ms5htD64kP7fyczbhUyc-zfRql7fDV3sRLeaLzcWSjUA6ZdK0mi2LYZzhp__k04QJs5k3eEr3W66QtVIGfG1gTMGwCsij1C0G3lvWrBDObTyoo9ys_vn2DwuLCmkfwR_N_Uk3QQRGglPsgE12rbFGBG7p5z1zohjwaL-yokvwUT47-F7PwYwKJbsiYT8mMNTNnpHTmTB3O20b-t98pfya55FOiCfTemeTb14hzQ7BRLtBnoRSFn37RKOZBQNRgiu3wFoHGnxnWNKPsM1Gr_7z_CGHNaBZanD4216_VwQ-am6kWYXBocPG6vL5Cn5CLQsuLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه یدیوت آحرونوت گزارش داد که اسرائیل همچنان منتظر مجوز نهایی از ترامپ برای تصرف تپه علی الطاهر است، این پایگاه زیرزمینی استراتژیک حزب‌الله که گفته می‌شود ده‌ها جنگجو در آن محاصره شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141753" target="_blank">📅 08:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام ارشد کاخ سفید: ترامپ در سخنرانی خود در مورد اعلام تنگه هرمز به عنوان بخشی از خاک آمریکا شوخی می‌کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141752" target="_blank">📅 08:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / زمین‌لرزه‌ای به بزرگی ۷.۴ درجه در مقیاس ریشتر اندونزی را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/141751" target="_blank">📅 08:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
🔴
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
🔴
این طولانی‌تر شدن مسیر، به مشکلات لجستیکی ناو‌های هواپیمابر دامن زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/141750" target="_blank">📅 08:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141749">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e3beeae8.mp4?token=MhNAa9gcQb1jHjVa2lhw71CfDfDP-p3v3CVCAQ0pK978ZHqkNqfuNn3Vqb863lNyk183wTzhan-ObxVu3QrKqQxDCiv1ppSUEgAnU-FkGn-KdTUIA48jJhJPsmoCt8V_zx7kBOWb2DyxTLx6ZK2rYjoZG9G5m51WiE8xgkoHLNZMAPsTNLfSb6zi9c4c5-NnIaeHSl8uT2hHwIUXii4j-syAPRZFd0BcYBgoa9A7RuDDJviBNx79uldYtcWtmaIaSRIWwPIvPkvaBpfQK7Guv99Wa9UIagKBWMjD685afbRLaNHrJrHmV8-h-UfEMDo040U51Ep3xhSKlkYlLMRv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e3beeae8.mp4?token=MhNAa9gcQb1jHjVa2lhw71CfDfDP-p3v3CVCAQ0pK978ZHqkNqfuNn3Vqb863lNyk183wTzhan-ObxVu3QrKqQxDCiv1ppSUEgAnU-FkGn-KdTUIA48jJhJPsmoCt8V_zx7kBOWb2DyxTLx6ZK2rYjoZG9G5m51WiE8xgkoHLNZMAPsTNLfSb6zi9c4c5-NnIaeHSl8uT2hHwIUXii4j-syAPRZFd0BcYBgoa9A7RuDDJviBNx79uldYtcWtmaIaSRIWwPIvPkvaBpfQK7Guv99Wa9UIagKBWMjD685afbRLaNHrJrHmV8-h-UfEMDo040U51Ep3xhSKlkYlLMRv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر ایرانی‌ها توسط یک عراقی
‼️
🔴
یه عراقی با ماشینش اومده ایران، و همه با حسرت بهش نگاه میکنن و فیلم میگیرن.
اونم می‌خنده و این ویدیو رو منتشر کرده و حالا در سطح جهان همه میگن ایرانیا ماشین ندیده‌ان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/141749" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141748">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW7Ruw01sZO8JKmFd1kXtLFgkMx3wTe0N2cW0tkm4J-BzAqILjNAN_aEiSB98hSoDQaONlHZNxHXZ98mEQ_7nWIhTihfL6KbPK7Se1OvIY2nEJYcJz8lCEH2jhfyMi-xwScoBJw2J2_VFMBFfnh14meppkh5otsj3HlLroRfJFfA0fFbKw8nAjLnnsiQqWmCfmFr8b4rTcz4KJ_IZ8uWcWaqH2DLjxPihGICFH6zenA--z7fqJPSEnuCp-GQF99Y2EDF8qfMS4mLCWR7lvL9HfAS9i6yaQwpwi8Q3K4ihk-yt0pkJ-25BLQtDvwMHsjWmsPayxtyw6g0FDY1M1wPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان: به لطف مسئولین عزیز و زحمتکشمون یه بلوار به نامم شد و آرزوی من محقق شد
🔴
دست مسئولین رو میبوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/141748" target="_blank">📅 01:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141747">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: میتونیم تو ۱روز ایران رو نابود کنیم اما این کار رو نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/141747" target="_blank">📅 01:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141746">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGa0bxktUELrd2AI-5tfVwdbyxyerG9CysG6prD_hOiQL9RYIHguAZ7YJ3d0bVUbEXA7tdKTDE6xCYmi_gpuSGyiApBUhYxqrzfa66PYicnIi12lIojo8-GuJ3jLA4gf76XGME31ctEnliASfQmEtdoY9MhhzbJNeBbY_i_BfIZjBo8HvzLR3vz1NvdZru0uBkpm5-mPcMlHfjCOvWyjkShMs5dykmLcrBHfJ2jHsl83c-em6_0y8kZUNv3pPQ0aCcVoA1tMyAD_OBwvSXQn9HS6Tk9cU8jfViQ5Ije22V6Au2YnmlkrCdx4eWPjQ4rm6SFPFrxZhkw33MjrRfGoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ:
دولت ترامپ در حال آماده‌سازی "اقدامات اقتصادی بی‌سابقه" علیه ایران است، به منظور وادار کردن این کشور به توافق قبل از انتخابات میان‌دوره‌ای نوامبر!
🔴
این اقدام همچنین نشان می‌دهد که ترامپ به جای بازگشت به حملات نظامی در ایران، به فشار اقتصادی و دیپلماسی اولویت می‌دهد، با وجود فشارهایی از سوی برخی مقامات ارشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141746" target="_blank">📅 01:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کاخ سفید:
تمدید آتش‌بس با ایران هنوز قطعی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/141745" target="_blank">📅 01:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3081852fbc.mp4?token=j5Ty0DVGVqFZe5w54BB86UONeuqCFneLPn0qpWUwtn-0lU-xrQEUgaJlYbHs3GC4imXdGcfXbOyG_lag0NqpSA_6o9GYkIkVzssGUiqhuaSWrUjsqKOeWXm8vJEi-NUm51tr9NvoNBK9zWOccZ2fD1ntrbD_H_TnnETcPWyxoPR40U9mjvFwflLdS1e7DjeqyAuFluQl4KK1jrDeajEYOyOvJ1F4Ck6hHF7rUZOUKpeGgYO5jZygJpZmpAkEi0DLNJ58Nyike9G0NycrS-LshCsVbGyNp3er56KC7QSPLkbc5FqJ1m6plAz-DDWDgnszRF_0jntHNLFd9Robv2T8MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3081852fbc.mp4?token=j5Ty0DVGVqFZe5w54BB86UONeuqCFneLPn0qpWUwtn-0lU-xrQEUgaJlYbHs3GC4imXdGcfXbOyG_lag0NqpSA_6o9GYkIkVzssGUiqhuaSWrUjsqKOeWXm8vJEi-NUm51tr9NvoNBK9zWOccZ2fD1ntrbD_H_TnnETcPWyxoPR40U9mjvFwflLdS1e7DjeqyAuFluQl4KK1jrDeajEYOyOvJ1F4Ck6hHF7rUZOUKpeGgYO5jZygJpZmpAkEi0DLNJ58Nyike9G0NycrS-LshCsVbGyNp3er56KC7QSPLkbc5FqJ1m6plAz-DDWDgnszRF_0jntHNLFd9Robv2T8MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شرح
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/141743" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری بریزید اینجا
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/141742" target="_blank">📅 00:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
عراقچی:
آنچه در یادداشت تفاهم اسلام‌آباد آمده «خاتمه جنگ» بوده و نه آتش‌بس
🔴
آمریکا این یادداشت تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شد
🔴
بنایراین چیزی به عنوان آتش‌بس ۶۰ روزه که نیازمند تمدید باشد وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141741" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrlHHXDPgFqu-W7nzjfAAdMaYRM3sEmEd7U877gPi3JoU5odCTHJ14iPLHBeQAzBX3qNTOIEUwwzrHo-58DZy6pnMxtwhJZd1pHpMMCRNbAUMJ_GsAxRcFjziavg5ROYo5IEMyaHfdbXyYuVLbIBW88JxPubSbMVNYrH5f4NEwhxmyAOXTbwZ1IaOqL79bXTVPTCLbB2sRlqK0og6MIRARjiDlNNUUsiYZ_QGf3rI92_G12h-d4r0MFQvVcSwhvsPwn7ZeSZp9sGYywz4Zdo3p5NW0JCAbs_CXlyQtgu0MjkaA7H2P7TJmo-0NL6r07GrLEXK-MfsFNfnkGu2F-2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: پول نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/141740" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0wDAnWsRF9HhOWchoNsrVhsKqsPvynbPpdwQb0GCYf0Ul4uWBZZ4Afq9qpxVeZkaccmXEmsg11OsY_BJVs2DETdM53WoxfCabNvvlFoyGdc1Si9fZPvp6Qwxv4sFxFpyU48HDPm-jFOYKoJ8k-3BWphX7r_him5e2Qpm-hF2CBfc2hTwqRjANAF30psma3xH4HiPd8qdEGvQKdn1A9Heze-KTMQZ00t4He6hvA-y6p9vWyK18-CUchBYNAAiHZkNzs_gKamwEoqCpSk5_jvX_5O1QVzAvg1gSuM1-3W-gNZSA6wdQofIZfCJb5AhcG2-jCFvbSMev0lgm1DpqbY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احسان حسینی، خبرنگار حوزه انرژی: اصلا بنزینی نیست که بتوانیم وارد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/141739" target="_blank">📅 00:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38c6a0d4c.mp4?token=BSXWTt7u7wlgji48gZZ9O3bN_hQ9MR67pAHWvE3WuSaEE6O0X99rOMd7epumq31z6vCirSYWR9C91eyCMkgksDvJNeMzBX27NaUoch07oOjOoQ7dwcW6Af549dXXd0mCpZtpY3SZ6NZp7GsuRRKDaRHEJrG8LYfigMWva7H7ITX7XTJBawKCLLQZsvKQr7sbg6MTuHNd8cSyKQ_bx-1c_rOwzHDgS8Blu4cGwneXPLxfG_7bkJWlfOq8Rl2PhkPf9xffnWwgh70ouY_bUEIJWvfW4LpX6DZ7a9st1T9Gvm8sm1VPXw9kA7od7xHHjFy9VrZsR2g_eb-96W4oqPfJcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38c6a0d4c.mp4?token=BSXWTt7u7wlgji48gZZ9O3bN_hQ9MR67pAHWvE3WuSaEE6O0X99rOMd7epumq31z6vCirSYWR9C91eyCMkgksDvJNeMzBX27NaUoch07oOjOoQ7dwcW6Af549dXXd0mCpZtpY3SZ6NZp7GsuRRKDaRHEJrG8LYfigMWva7H7ITX7XTJBawKCLLQZsvKQr7sbg6MTuHNd8cSyKQ_bx-1c_rOwzHDgS8Blu4cGwneXPLxfG_7bkJWlfOq8Rl2PhkPf9xffnWwgh70ouY_bUEIJWvfW4LpX6DZ7a9st1T9Gvm8sm1VPXw9kA7od7xHHjFy9VrZsR2g_eb-96W4oqPfJcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : آمریکا بازگشته است، و بزرگ‌ترین پیروزی‌های ما هنوز در راه هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/141738" target="_blank">📅 00:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141737">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e572186d.mp4?token=PS_3bLpXGYYvIc2-jkr4_OIvFjIm971xZwHVkvel17KJpoyQNeVyQ_xuRTi-Wzl9efsLUDv0hIXiegmaiLgjAs0KPDxOdhv7k6FkRmWrQe-c8Vh3MA4FyGtY86uL_Eh61vkgzpn03CRxOos0eMTg03E8njd1YCxC3ucr7JDEIK9a6XaAsOlztXrXhUTwiB_y7hml1Gjz6zpLsDfnPHQYCFBkEolr3DarHsrGmwSa5cZAUdKhksz5TMOPtCl9e_e2EY0eZaUH--x2ApivGs8Jkk_yMWjdBRffRa9A63iSW5kPMWq-XhNaziJbHMn7jb731U4mng1GmPUMAnkWax3G2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e572186d.mp4?token=PS_3bLpXGYYvIc2-jkr4_OIvFjIm971xZwHVkvel17KJpoyQNeVyQ_xuRTi-Wzl9efsLUDv0hIXiegmaiLgjAs0KPDxOdhv7k6FkRmWrQe-c8Vh3MA4FyGtY86uL_Eh61vkgzpn03CRxOos0eMTg03E8njd1YCxC3ucr7JDEIK9a6XaAsOlztXrXhUTwiB_y7hml1Gjz6zpLsDfnPHQYCFBkEolr3DarHsrGmwSa5cZAUdKhksz5TMOPtCl9e_e2EY0eZaUH--x2ApivGs8Jkk_yMWjdBRffRa9A63iSW5kPMWq-XhNaziJbHMn7jb731U4mng1GmPUMAnkWax3G2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «یکی از مشکلات در ایران این است که کسی وجود ندارد که بتوان با او مذاکره کرد؛ این یک مشکل است.»
🔴
او در ادامه گفت: «ایران تنها کشور جهان است که در آن هیچ‌کس نمی‌خواهد رئیس‌جمهور شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/141737" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: ایران ۲۱۲ هواپیما داشت؛ همه آن‌ها از بین رفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/141736" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d715d521d6.mp4?token=MxM7et8q22wwwDhe8dbyRX0eEyWyrpb2TvHHgbLQz56GJKWyc36yubXPSlOpv1zEyAD-gWjKKXoSi4kgBa_YKDbiYMMCk3qkusV5yiUDwSwkfAM8IOtnKCGfDaPHodHFuthtY4Z0UlECU5td9VEMSB3RyUc9sU-lR40sjDUphgItOcL3o3lRShvJxVDa61lJH2D9905VGLkWKIAbl0rZsJgd17U0Zv1hJjRwol6jVQbiMeWflDgglRO8tByDji4OC1SuMvYGWFSWjR4nYXvEgIA1YVC6Diu1IN6LdvYGAUHtqFJ_4bpjO8hgwcw8EsmL_VHap2wvUtV-YnlLwIaCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d715d521d6.mp4?token=MxM7et8q22wwwDhe8dbyRX0eEyWyrpb2TvHHgbLQz56GJKWyc36yubXPSlOpv1zEyAD-gWjKKXoSi4kgBa_YKDbiYMMCk3qkusV5yiUDwSwkfAM8IOtnKCGfDaPHodHFuthtY4Z0UlECU5td9VEMSB3RyUc9sU-lR40sjDUphgItOcL3o3lRShvJxVDa61lJH2D9905VGLkWKIAbl0rZsJgd17U0Zv1hJjRwol6jVQbiMeWflDgglRO8tByDji4OC1SuMvYGWFSWjR4nYXvEgIA1YVC6Diu1IN6LdvYGAUHtqFJ_4bpjO8hgwcw8EsmL_VHap2wvUtV-YnlLwIaCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هیچ‌کس نمی‌داند چقدر در ایران موفق بوده‌ایم؛ خود ایران می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/141735" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ : وقتی کشورها به کمک نیاز دارن، با آمریکا تماس می‌گیرند
🔴
من همیشه بهشون کمک نمی‌کنم، چون بعضی وقت‌ها رفتار خوبی با ما نداشتند
🔴
البته ناتو هم همیشه کنار ما نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/141734" target="_blank">📅 23:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8265299e.mp4?token=PVmIZEMT4FHLkztehfttypcqwRpqMXnzC8r9wJymgRFWFMXDtgRPI939h313zUmRtGcqEOzgMv_N-2SDUC_9rJEP4YlW_n0mrq5z0bzdgTWRwFIcuNafWYrF8_nFPw03DNtqtdF_EQEXJLlUH8PVSfwhbW_qAIEj8_nRp4ekElzl6AIfqLzRimwBJJgkSuXIDGc7vgGhqxgNRhw_BHN6-6LvSqAKsFelKxcGxjpZKNEy8OfD9L-ROiu7WR287gJVuUoJ5TDfdz0LODEI06vW0AAEfD87TrQ95aRkJgyHHz6P0rJAVIqALXFRFvpBCs5Q3QUJoK00HWIX6qijc-jDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8265299e.mp4?token=PVmIZEMT4FHLkztehfttypcqwRpqMXnzC8r9wJymgRFWFMXDtgRPI939h313zUmRtGcqEOzgMv_N-2SDUC_9rJEP4YlW_n0mrq5z0bzdgTWRwFIcuNafWYrF8_nFPw03DNtqtdF_EQEXJLlUH8PVSfwhbW_qAIEj8_nRp4ekElzl6AIfqLzRimwBJJgkSuXIDGc7vgGhqxgNRhw_BHN6-6LvSqAKsFelKxcGxjpZKNEy8OfD9L-ROiu7WR287gJVuUoJ5TDfdz0LODEI06vW0AAEfD87TrQ95aRkJgyHHz6P0rJAVIqALXFRFvpBCs5Q3QUJoK00HWIX6qijc-jDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد درگیری قبلی با ونزوئلا:
«ونزوئلا یک جنگ یک روزه بود. و اکنون ما با آن‌ها عالی کار می‌کنیم. ما میلیون‌ها و میلیون‌ها بشکه نفت گرفته‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/141733" target="_blank">📅 23:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بر اساس گزارش نشریه پولیتیکو، به نقل از یک مقام کاخ سفید؛ هنوز هیچ تمدید قریب‌الوقوعی برای آتش‌بس بین آمریکا و ایران وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/141732" target="_blank">📅 23:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ
:
چاک شومر کاملاً فلسطینی شده
🔴
دنبال لباس فلسطینی می‌گردم که براش بفرستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/141731" target="_blank">📅 23:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: اقدامات ما در قبال ایران خدمت بزرگی به جهان است
🔴
دونالد ترامپ درباره اقدامات آمریکا در قبال ایران گفت: «کاری که ما انجام می‌دهیم، خدمت بزرگی به جهان است؛ نه فقط به خودمان، بلکه به تمام جهان.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/141730" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ درباره ایران: «وقتی مجبور می‌شوید کمی بیشتر برای بنزین‌تان پول بپردازید، من هرگز عذرخواهی نخواهم کرد. من کار درست را انجام دادم.
🔴
[ایران] نباید سلاح هسته‌ای داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/141729" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / ترامپ: در صورت هرگونه حمله از سوی ایران، با قدرتی صد برابر بیشتر پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141728" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: گرونیا طبیعیه، درآمد نداریم، نفت هم نمیتونیم بفروشیم.
🔴
اما عرزشی معتقده پیروزه جنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/141727" target="_blank">📅 23:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما ۱۹.۲ تریلیون دلار برای سرمایه‌گذاری در کشورمان داریم. می‌دانید دلیلش چیست؟ تعرفه‌ها.
🔴
ما با تعرفه‌ها، ثروت زیادی به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141726" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141725" target="_blank">📅 23:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: در عرض ۲.۵ سال، فردی انتخاب خواهد شد.
🔴
لطفاً یک چیز را به خاطر داشته باشید: ترامپ کسی بود که این کار را انجام داد.
🔴
این کارخانه‌ها همگی دوباره راه‌اندازی خواهند شد و آن‌ها خواهند گفت که چقدر باهوش هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141724" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوخی ترامپ: فکر می‌کنم باید دوباره کامالا هریس را نامزد کنند؛ او نامزد فوق‌العاده‌ای بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141723" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141722" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد نخواستن اینکه نیویورک به دلیل جرم ها سقوط کند: «ما اجازه نمی‌دهیم این اتفاق برای نیویورک، ایالت نیویورک بیفتد. و به همین دلیل است که باید بروس را به سمت بیاوریم.
باید او را آنجا بیاوریم. هیچ‌جا حمله کمونیستی به جامعه آمریکایی واضح‌تر از اینجا در ایالت نیویورک نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141721" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
تا این هفته، نه نفر از ده نفر از لیست متهمان فراری اف‌بی‌آی دستگیر شده‌اند.
🔴
این یک رکورد تقریبی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/141720" target="_blank">📅 23:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان
:
بارها گفتم و باز هم می‌گم؛ من هیچ‌وقت در برابر رهبر نمی‌ایستم
🔴
این حرف رو فقط برای شعار نمی‌زنم
🔴
چون برای من اتحاد از خیلی چیزهای دیگه مهم‌تره. اگه اتحاد از بین بره، قدرت هم فرو می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/141719" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : ما نماینده کل جهان هستیم، هیچ کشوری مثل ایالات متحده وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141718" target="_blank">📅 23:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ
:
کسی اینجا هست که طرفدار قطع بودجه پلیس باشه؟ اگه هم باشه، جرئت نمی‌کنه بگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/141717" target="_blank">📅 23:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141716" target="_blank">📅 23:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره وضعیت فعالیت‌های مجرمانه در ایالات متحده پیش از ریاست‌جمهوری خود: «و در چهار سال گذشته قبل از اینکه من کشور را ترک کنم، کشور ما توسط مجرمان خشونت‌پیشه غرق شده بود. منظورم این است که به یاد دارید چند سال پیش چقدر وضعیت بد بود؟ درست است؟ واقعاً بد بود. باند‌های خارجی، اراذل وحشی همراه با بایدن.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141715" target="_blank">📅 23:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/141714" target="_blank">📅 22:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع نظامی یمن: حوثی ها با ۴۴ پهپاد و ۶ قایق بمب گذاری شده، بندر المخا را مورد حمله قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/141713" target="_blank">📅 22:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صحنه‌های ویدیویی شامگاه جمعه 23 مرداد حریق در بندر المخا یمن ناشی از حملات موشکی بالستیک شبه‌نظامی حوثی‌ به زیرساخت‌های این بندرگاه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141712" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری /  آکسیوس: کاخ سفید بدون اطلاع نتانیاهو در حال برقراری ارتباط با اپوزیسیون اسرائیل است
🔴
آکسیوس به نقل از منابع آگاه گزارش داد، در بحبوحه کاهش محبوبیت نتانیاهو، دولت ترامپ برای جلوگیری از به خطر افتادن ابتکارات خاورمیانه‎ای خود، شروع به برقراری تماس‌های مخفیانه با رهبران اپوزیسیون اسرائیلی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141711" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
در دومین حادثه ریلی از نوع خود ظرف شبانه‌روز گذشته در بریتانیا، جمعه 23 مرداد، یک قطار مسافربری در نزدیکی «ویکفورد» در «اسکس» از ریل خارج شد. روز قبل از آن بر اثر واژگون شدن قطار در «لویس» 20 نفر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/141710" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds9u1-HE5SCjK1FOayCwHLuyYvBIO18TiZjVA7FA1swOw5fFnlC-u_RG-qweLJmEZ2Q_D5t5FVxzXlwUCykmWf6IGvhB59A-rmX_AUdd0gWAirc3miINsPwNOwhaSRGVn4LFcoXozZAqBwJArEl_cpSzPxVUBJfUJajif6r1Op9FVsPv8Wcn6j7M4nDgyKj5PFP4Dc-sQjB0fwkPQvTxgtVN4ejGeDAbhsLxxOoLsDxzKNtAbg3yz9VL5izI0032iaBy9jngqyx50tJSjkr9nX1Ua67532-t_gn4KdBc6054Ni1uEdJng9FSnITP3Hn_rXo0VGvftmwTE62CChfXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با پول یه ماست پرچربِ امروز،
۱۰ سال پیش میشد خرج خورد و خوراک خونواده رو برای یه ماه داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141709" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0SgEH4Bj4t7PZO7mkxQUyX8cvt5GTSze8Y2HufKxCimsgKP0h5iAzBS19eP4gT_h3dGsu4Q2_WcSfRLLjc5-u_X5GWt5tT5iTf0s9bRL5EqWHyx6YYvHR_G9cX-Vfv_wC8hE1X7SY0eSWX3u4BV18zskjDxGPrv4qs_DSufSi0naenkdWKSEDNsnZrZi11QQYPMPuYql8aJS4Y7nSKmqxzwh2SRQk_yopa3l-6H9cuEB3CorYzoI0D-shJ2Sq2r8QDrMYdfHZTOLe1na9AxqY01icXMhlb_dVK9pMJCKDzRAZj3U1ARIdF4ELxIEZ1FSc-rCA2RSCZkovs8uhGUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد دفعاتی که مناطق مختلف تهران توی جنگ ۴۰ روزه، مورد حمله و اصابت قرار گرفتن
🔴
بیشترین: منطقه ۴، ۲۹۸ بار! که شامل: تهرانپارس، حکیمیه، پاسداران، لویزان، مجیدیه، شمیران نو، هروی، نارمک شمالی و شمس آباد میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/141708" target="_blank">📅 22:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbuyVZFucBgPhMSV1dqfA2bln5w4gJ-sZwrHd5_ELd8agHk6EAmWZrFgGzz4EFN6yx3IVhSjrzyXwKdVZp8HP0eOAnpTEFV98kx5TD1HZXcB3zkyNgJPeS5lLIDpBn3kVIcWXJplGtVRzrSeOH-0vD76iZFoWz7yv7HUHI_-TLEM91MQmiG8n8XJgrg6_K4w1dY1eNJBpak7f4NLuZwKnXh57XxYpbr9SBgacHy89xMyWNdwKwfXYLd8volfkxiOXO3ApgwwjNZ0OOhKwwC_aOBu2ulP_qkNec3WaW5BzbDHRwg_ElaJR3XwP9xbf-fTIMGm9r7vrhq6ZZjA0BiwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
افزایش خطر آتش‌سوزی در سراسر بریتانیا
‏
🔴
مقامات بریتانیا درباره افزایش خطر وقوع آتش‌سوزی‌های طبیعی در سراسر کشور هشدار داده‌اند و از شهروندان خواسته‌اند از هرگونه فعالیتی که می‌تواند باعث شروع آتش‌سوزی شود، خودداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141707" target="_blank">📅 22:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
کانال ۱۳: اسرائیل قصد داشت حمله‌ای دیگر را در سوریه انجام دهد، اما ترامپ مداخله کرد و این اقدام را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/141706" target="_blank">📅 21:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxREali0h3gTWpGaGOvqZ5fH9eFrrlOYMLsyn_WJT5fFu8ErVEGyJ81Vmgv2esNV-UR41pUHICX61ZUqpeYs-6zNdjvxecD_qtOP9UTizm5dPuE3eD9_9Pm1flSHnqEsMsnrr0yfz3nuMz2G5MLkaJNP69Xbe7QzsPBpN3Ro8WBvtcq3jWUimyRs3qgjo1zF0_ias9w233Lx7Rn7GNi-KjQm0HvOrbAWnff8InoqzPwCcpXQVuq5EtJGcqLtvvKQCun6kyvtEmubnTilAbi8V0HZ2WwB6G8LGWN1VTRj7ouvpnHYKXiCjLPI1eNJmSPVgtFtLh-GJvj7y7cLvcQdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیل محبی معاون حقوقی مجلس:
تو مصرف بنزین صرفه جویی کنید تا گرون نشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/141705" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویت : آمریکا همچنان می‌تونه ایران رو تحت فشار بذاره و اقتصادش رو فلج کنه
🔴
ابزارهای بیشتری هم برای افزایش فشار در اختیار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141704" target="_blank">📅 21:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یک منبع نظامی انصارالله: شرکت آرامکو در جنوب عربستان را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/141703" target="_blank">📅 21:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTLD9tfWOJrJxjfl0PYb-UHSWHTWsaFfkqJUB8MbvakCy6U6_LUgJt5w7uhV4cowbzzrDmZxWILxu6E7bJ91otKJypSThc28p0D6eOAii5uT7L3625J4st9fAY8vBb6PfvoZjJjo_HYWXi4MBJS-lkQ4VKLGJ8klWzOMXtePsrOgnMfvNkixrAmQnJvqTOQ-udwZRrCH638x0yHAnulyfAYJiTg80voOn34X83IZl4M7yH34wNXaC6HQKgHdfE7ILConY2HTfsPCN_9oawSEVni6vMM8O_ntE6llYdOH7bfhjhvGn1sUFzJnNLhJg2tNkvWWRmvrXxanNvXaXAFhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داعش اسپانیا رو تهدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/141702" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
دولت کانادا امروز جمعه اعلام کرد ۵ مقام ارشد نظامی ایران را به دلیل اختلال در تردد دریایی در تنگه هرمز در فهرست تحریم قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141701" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ : از نظر وال استریت، وضعیت اقتصادی به طرز شگفت‌انگیزی خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/141700" target="_blank">📅 21:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb239496d.mp4?token=YQsUZst93C-8A3c_bZHzGFs5Qtt_UyFbmn0iK5NgMD0WohENtGz3HQjhPH-fQTzldVrhnHM5V7Wb0IlN7tNpiYfyjLWqMM-8uMdPd_ceQV6MHujf9hKaTUx3-eiJ4L8KNRQTrAWwuooL5-jI7i0ek3GTFdcTnVxFovC36zSPFuVb-wNmTZIY1dUWEs_YS8hmMe1bjnJ-a7TLPOvrydqSCxXb0kqWob7H1xc3xSxIV6aauGrZrUkS4D-SS2SMP7VVz1l0_4TtOrgogcQUKx6jfX95cSgj6N_b1dvkGAD5KqDJuSzVVMX50WBvSDWVpJ9I3pylGq50nSdQamIlpQxwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb239496d.mp4?token=YQsUZst93C-8A3c_bZHzGFs5Qtt_UyFbmn0iK5NgMD0WohENtGz3HQjhPH-fQTzldVrhnHM5V7Wb0IlN7tNpiYfyjLWqMM-8uMdPd_ceQV6MHujf9hKaTUx3-eiJ4L8KNRQTrAWwuooL5-jI7i0ek3GTFdcTnVxFovC36zSPFuVb-wNmTZIY1dUWEs_YS8hmMe1bjnJ-a7TLPOvrydqSCxXb0kqWob7H1xc3xSxIV6aauGrZrUkS4D-SS2SMP7VVz1l0_4TtOrgogcQUKx6jfX95cSgj6N_b1dvkGAD5KqDJuSzVVMX50WBvSDWVpJ9I3pylGq50nSdQamIlpQxwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: مأموریت نیروهای مستقر در ناو «آبراهام لینکلن» بیش از حد طولانی نشده است
🔴
خبرنگاری از دونالد ترامپ درباره نگرانی خانواده‌های نظامیان از شرایط نیروهای مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» پرسید که ترامپ پاسخ داد: «نه، آن‌ها نگران نیستند.»
🔴
در ادامه خبرنگار پرسید آیا این استقرار نظامی بیش از حد طولانی شده است؟ ترامپ پاسخ داد: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/141699" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مجتبی یوسفی، عضو هیات رئیسه مجلس: وزارت خارجه وسط جنگ به ما نامه دادند قانون تنگه هرمز را در مجلس تصویب نکنید تا ما با طرف عمانی تفاهم‌نامه بنویسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141698" target="_blank">📅 20:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141697" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f84d0c51a.mp4?token=CZWjGGvaBKjnq8E_T9J8alUyre54_0Eh6dFlfdBhvVyDS-0RY9Ly3nY240i4w8t1JWXagijOVi3mQQq3YJidwsPMO9aPREUNCojbmANOvOfy0CrrfWtOe1EtShhl7hodHGS7pQOTUWCSidpIpaI31hYmOV5O8eQWvfmiLs-O_njZXISkgA8OJH0tI4PYAwDpitKw0umNnMAt5u27zv85KSX-WHko-_Q4KTSqNleefhNrgp_utozA16nKIwgFJDARpl3yryod0YYprRzg_tvIwgSjnDFf0m61AkHHtpIkGz992Ly2LhmtTX9Bhpo4-BQ1PDbx5gm2Z0p_-_G_qOxA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f84d0c51a.mp4?token=CZWjGGvaBKjnq8E_T9J8alUyre54_0Eh6dFlfdBhvVyDS-0RY9Ly3nY240i4w8t1JWXagijOVi3mQQq3YJidwsPMO9aPREUNCojbmANOvOfy0CrrfWtOe1EtShhl7hodHGS7pQOTUWCSidpIpaI31hYmOV5O8eQWvfmiLs-O_njZXISkgA8OJH0tI4PYAwDpitKw0umNnMAt5u27zv85KSX-WHko-_Q4KTSqNleefhNrgp_utozA16nKIwgFJDARpl3yryod0YYprRzg_tvIwgSjnDFf0m61AkHHtpIkGz992Ly2LhmtTX9Bhpo4-BQ1PDbx5gm2Z0p_-_G_qOxA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلوسوف، وزیر دفاع روسیه
:
جنگجویان شجاع کره شمالی که کنار نیروهای روسیه می‌جنگن
🔴
منطقه کورسک رو از «گروه‌های نئونازی کی‌یف» آزاد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141696" target="_blank">📅 20:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a627737cf1.mp4?token=uCLmpjHTBbbHZwt_mLCMjmKfRa5uGv-yoiRRcrZNc1DyXKlNvQqmXG9Fv8ZWCQmWYBsCP1qjL4m9xwXIOXTwDC1jRGOVEvsFEY_jXTxfjotYwGC6upBy3GfckfOV9fO04cD7AZGvNKoRPQeHkoxY4MmocTzDTB5yGcLPLI1KWagB0rVHcBj3GIguiVHj3bydmSp8pSKTDKPl-X5Lf4ShWmihbQXhZJsPOOJdTHSpY4bOZyXkl_qH-aX4iZCX2kx1ZPAt-zeAyyMvwXX7FQ806dXYfUnz1_BRguEmjlznjLnPyPIZIaENgdu42jpEPnQ5d8u56zEHi81kS22zHmfKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a627737cf1.mp4?token=uCLmpjHTBbbHZwt_mLCMjmKfRa5uGv-yoiRRcrZNc1DyXKlNvQqmXG9Fv8ZWCQmWYBsCP1qjL4m9xwXIOXTwDC1jRGOVEvsFEY_jXTxfjotYwGC6upBy3GfckfOV9fO04cD7AZGvNKoRPQeHkoxY4MmocTzDTB5yGcLPLI1KWagB0rVHcBj3GIguiVHj3bydmSp8pSKTDKPl-X5Lf4ShWmihbQXhZJsPOOJdTHSpY4bOZyXkl_qH-aX4iZCX2kx1ZPAt-zeAyyMvwXX7FQ806dXYfUnz1_BRguEmjlznjLnPyPIZIaENgdu42jpEPnQ5d8u56zEHi81kS22zHmfKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ویدیو وایرال شده از یه مسلمون در آلمان درحال تخریب شیشه های مشروب یک فروشگاه!
‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141695" target="_blank">📅 20:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfCUUD4UC_GHWJxSbLYSbPlIEPYCaGX7p65xpbGTsASHSOtpj3Y6NdtGvAGdwCtEwhKmayTcTHBZGBHcBYRDprbjndqMxlwajGN5dwBJDZRs1xCvvBKfR6mQV7n8T-ioN1ifOI6wvlKu1LQ-SbjerJ0QbyT_kex8iKErqtcjO2BYiXyN_Rwge9pNXi-QjyPzUI_p0AsMcVhihKfE-MK2cJ3lZ93TU_0sn4UCzPu2645z9xmAHqt4zqkUebc6DOOjwdyWSM1B9O5QpGmEaY8CanLny63HJhFpBhZx7bRUjX5BiirWeyOz7bpzBRx-1VtANU9LY621pa5k4LErcdB_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ در شبکه اجتماعی خودش تروث سوشال مصاحبه بسنت وزیر خزانه داری با نیوزمکس را بازنشر کرده که وعده فشار اقتصادی شدید علیه ایران را داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/141694" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8cda1283e.mp4?token=FtS0eI_vVcdRe3cmDXnAOedfq1vso9-RSZQwM3b7t6au92MYx0dzZpv_NtGQzwDO1Cer7UIS8c9SyhNgn7Di5jbaYWbuA-GOCqPD37aF8EaNs_ra93dz2Yo34y91ocUd-rP4ORK-l4M_6khDK2JlM8gLTc0jvRT71CuMzmrinGWF9pw1Xe67LnCCpSEb-yg9K42d1eBLCcrEoRTW8jd3w6Mn5ATK8IUvGf2RFxd4jLwL0HwL-wTzJbzJ4Cni-l7sDM0RyGke-cJD8vCqInvzcFBlOtUqSepBHPDM1o09mpsJayKkoDywruuHbGapU_HSMyq5D8evr6yzgWVLmj7Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8cda1283e.mp4?token=FtS0eI_vVcdRe3cmDXnAOedfq1vso9-RSZQwM3b7t6au92MYx0dzZpv_NtGQzwDO1Cer7UIS8c9SyhNgn7Di5jbaYWbuA-GOCqPD37aF8EaNs_ra93dz2Yo34y91ocUd-rP4ORK-l4M_6khDK2JlM8gLTc0jvRT71CuMzmrinGWF9pw1Xe67LnCCpSEb-yg9K42d1eBLCcrEoRTW8jd3w6Mn5ATK8IUvGf2RFxd4jLwL0HwL-wTzJbzJ4Cni-l7sDM0RyGke-cJD8vCqInvzcFBlOtUqSepBHPDM1o09mpsJayKkoDywruuHbGapU_HSMyq5D8evr6yzgWVLmj7Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها همچنان المخا رو با موشک بالستیک و پهپاد هدف می‌گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/141693" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تسنیم: دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141692" target="_blank">📅 20:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رکنا: تو تهران دو تا پسر جوون تو فضای مجازی سر دختر دعواشون میشه باهم قرار دعوا میذارن و دیشب تو یکی از خیابونای تهران یکیشون اون یکی رو با ضربات مکرر چاقو به قتل میرسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141691" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIuE-X1ZVfGyzp1cB6VPyv7EkCtl-Msd8anpfm-_emiFvOjJyEHm92siE2YZGOCxmoyWoDKX_6IoK88TXIlEZ08B9dmebygx5Xf7n1AW_l1Qmebl2Dz7PA7xRBVe8P-yLHSrtOoUyClXI5-I56VI3rQXp56ogZWvEcUk_bFadac6EwQBsmmujxyLOHiw1xDO4mcUvtJ0QVHHe0TYU6qwmHA8Wd5-GkuYhQ0IFKeXVoqfpjHaf8OxyFKx32IRISCDwEznMguwswzqezxdS2hiek_6Sn5ufvk2gGuBSgqufrXxqhFt7XpJLjMxiwzFl0e4kti-n6_vAuxfE2VhLCiRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
من با افتخار اعلام می‌کنم که کوین رایدوت، یک مبلغ مسیحی عالی، به بازداشت ایالات متحده بازگشته است.
🔴
کوین توسط تروریست‌های جهادی در آفریقای غربی — کانون اصلی تروریسم اسلامی، جایی که در سال گذشته حملات مرگبار بیشتری نسبت به هر جای دیگر روی زمین رخ داده است — ربوده شده بود.
🔴
کوین، ایالات متحده آمریکا مشتاقانه منتظر خوش‌آمدگویی به شما در خانه است. خوشحالم که کمک کرده‌ام! پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141690" target="_blank">📅 20:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شیخ نعیم قاسم: اینکه ایران نخستین بند در توافق‌نامه اسلام‌آباد را عدم تجاوز به لبنان گذاشت حمله دشمن را مهار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141689" target="_blank">📅 20:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز گزارش داد پس از حمله به دو کشتی متعلق به امارات، عبور و مرور دریایی در تنگه هرمز به‌شدت کاهش یافته و این آبراه راهبردی به مرز توقف کامل تردد رسیده است.
🔴
براساس این گزارش، تشدید تنش ایران و آمریکا و بن‌بست سیاسی بر سر بازگشایی تنگه، شرکت‌های کشتیرانی را بیش از پیش محتاط کرده است.
🔴
ادامه این وضعیت می‌تواند فشار بر بازار انرژی و نگرانی درباره گسترش بحران منطقه‌ای را افزایش دهد؛ هرمز حالا مستقیماً به یکی از اهرم‌های اصلی تقابل تهران و واشنگتن تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141688" target="_blank">📅 19:56 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
