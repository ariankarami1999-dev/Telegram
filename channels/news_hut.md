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
<img src="https://cdn4.telesco.pe/file/H0gSLo44wN019_qRbcYjQXGb3S61J7h90V2Gve4JngBdf785ZasJnWzh4aIhGrUOT8pN-OakIurkl4dC18katcpjSix4_3GMvqmquuZ8WkM1C32ckKjfr-PyYEdKSM5piFDc_9lQFSwuBu6kv9TXaqy2ZEiCMOFAMzByknotIZ_gEGwIYQE_GjYA2GcJ2HiHz_XqwdNQhK77a4_9KOXNSOaqYhUNJWETGWreX0T6MrHkXjd-P9iptwe2hQa_bDJzsD-kD6fISQQfyQszgmWi_jCWx6L9AD1sYLRA8ml78tv-HhmrPMs8ZBlTd7gP_sI7QyIkC-R_t7cqx8rjLvG4nQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 01:09:45</div>
<hr>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6_xHKagLvFPOKEGDz12oOssnPDZjs7pPpqk5K5ecDx0KaJnSkmyP7HgL73TgtSpadIHvrgsbHmkoiMC_YSpvNknxcyVhRtp16XlebWZm9sD7QBoKSQSnFzCcwqLxG46D4u-naobjrZUmcMPI1JWGOtguW2mXfitdFBC5n5Xv_5SlxzgFBCVeKSPaMT4bAGdErnTPNV4y2HrFeXrXKTJ8wqfOHXhRiV1H-fQrZSyddTqNWwb5wDeagIqX-tflvSWbCmtUDsvN8qL-oPXL6v6WnC5MMbrvWjF528Oq0FglnA3aoyY0dRRZrAXDuicao7_B3sf2BwETfCqcrkertpWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2l2xuEpPSxHk8uAvuKWLgj8GaZB_yTnQJ5t3baifRjnO1yi5clCek0-48281aXzFaFhRd9Vj9ecpcZmODnqDUzAXKbvv1Z9hp0dOKIBFUsp5nLyvT7qD6mb-o-_FY272v8Heg7MWRL1-NZgvGYkPaBPYfacYdmunVi--5BB6K-KVtSO0Z_CIt4tzohQwv4ZfYWEuEEgSlpHdMi1pHTgLnW3-kks3pvGI1go2RL_m85xoRpBvelZY0uiGWmQPYTEmOXheZkcLC_aOOaVrO-9oyJdaeQ_V2VW7XAlDkXMtlI-CIw0ItrJpPPN517DfU83Vv9d_va_NxCGZY2GVhzdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=OL9ewmibu8NUNi8sQJR5giBYR2nOCkQs5JE8gva5G-32IQEzATJK0kU-je493G4anTUIf0d1XgOfIdwLKNEdO3pBT9p9fr3LC5uF1lNsjIqqYbuRq8BEYP3spYrf3mbiKsb7XeovAwugNWqeIFI8ZT7iTpqvhLCFfCSFfiRMMBtmdcMhlKEOBMEfFOt_E325MrrkJqOOFEEdk23BWbYanm7ArlW5Y5kmb8nLq93SmN4IPu50j0SCROww6psXN7j-UIGVDFazit97FawAUQ4DuUu3gtsBzFRzjZ_3cHPGMN1b-2DdX6cpb97PSEkFRB3Ewe-4X14k_dwa-W3oGBJ85w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=OL9ewmibu8NUNi8sQJR5giBYR2nOCkQs5JE8gva5G-32IQEzATJK0kU-je493G4anTUIf0d1XgOfIdwLKNEdO3pBT9p9fr3LC5uF1lNsjIqqYbuRq8BEYP3spYrf3mbiKsb7XeovAwugNWqeIFI8ZT7iTpqvhLCFfCSFfiRMMBtmdcMhlKEOBMEfFOt_E325MrrkJqOOFEEdk23BWbYanm7ArlW5Y5kmb8nLq93SmN4IPu50j0SCROww6psXN7j-UIGVDFazit97FawAUQ4DuUu3gtsBzFRzjZ_3cHPGMN1b-2DdX6cpb97PSEkFRB3Ewe-4X14k_dwa-W3oGBJ85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WdCKC5NcuZWLZ6N-8y003ZxYwVnl2x2QSms5qnkA-WIqmLTi-ttOqgghkA-odzVikLaIs8SmNr-dgsn3FgBBaRxMaREC5Fq1zGbhKbXz_eX0pJjN_7BC-LO1WpSqNjOR4B7Q_6RnSbUYxL4WkRAxHQ8H0rGBvyIWn4n14ziR_qLkgFqh1S6wBvfKnwA4P72kgxIlcj3q5EhnoUelcoIhsHLxuqZkN3UL_VJqzaxO1_RnsA6DSeQ7An72egUT73Xt-7rXJuV3gYWYPSWxYgUCAcnvyWNr_-QNSM1rJfeLE6C0-sU4bCxAAboAnh5PNwZzGlR_DlxlDXzej-q5fZzWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WdCKC5NcuZWLZ6N-8y003ZxYwVnl2x2QSms5qnkA-WIqmLTi-ttOqgghkA-odzVikLaIs8SmNr-dgsn3FgBBaRxMaREC5Fq1zGbhKbXz_eX0pJjN_7BC-LO1WpSqNjOR4B7Q_6RnSbUYxL4WkRAxHQ8H0rGBvyIWn4n14ziR_qLkgFqh1S6wBvfKnwA4P72kgxIlcj3q5EhnoUelcoIhsHLxuqZkN3UL_VJqzaxO1_RnsA6DSeQ7An72egUT73Xt-7rXJuV3gYWYPSWxYgUCAcnvyWNr_-QNSM1rJfeLE6C0-sU4bCxAAboAnh5PNwZzGlR_DlxlDXzej-q5fZzWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVcAyzgbFI9HTWSxmJf3Y1MntbWW4q4OV6sqLgowf-4wTBUsspRuQ31sc-EaM51jWsGD9k2iLJV8MXZkZoXvYKYbeB9o8i1krcBO37_MVWk2CxLKcX9ehH6PHtrbkLcrkHk-fY2-VPp5p-uq63q1VzCbyjeLCIl8RFP_WS8joWbOT5oEU-zeGTo_S_t1zx2cXmUIp_fcvh-UOgnrRhQtD_KuQkVJhkbYJL2QdCEbNl_1_y9tkyEbb1ZLlSt8N2dvA9dcWHv_QrE3wssrhFPLfjScoc2iN09xy3GGppfRelZbGijmjC0ezoD4yTYaSyGom4-MF_04GfkquAVTDQPUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i04yPwixFGYkYl4RhPKBWKLX_jmo1_CnktoAnqh0yEfFGhsSVC88NiO0k7D03Jygal5dnl2zkuaB8IdGWe_l3-50aDLVmexNxC6W9ox6yf8aOtd1tRiln08xkCfC00Ru2WBu6Soc4ah-WxqjBwGae1o841UVQsqZd3zsdpCehNOsYZVOwYrJdWv_-3UUIcQ0hyoGf5aSoGHaepwPb0_EmTBBRFLEMbPvBzzrMmmrpngwGKBS_SKbCmqwbylfA7JRtdOZ238WiROcY06Ai5i0fA7vc96SBPIpiEjDBrYRtyqQjV723X0HTygzAhxqn2Xhta-1r4dorp0ROpC986TE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB1xxNrUN5VsrM968vwb9TVKAazN82jkEdXG2bZptj3dbzWSeksX4e6A9Ou_j-KNNPE85ehEWf60F5XGDLFmPJnxGDj04putwF3PQrJUL1aw2nl-Tn1TlcSNB3t9-mZHKLam93zsZjNVeYQVo_4pUfN895_zKf6Cgy9U26sRWZs1yaVV01ApdieW1E_vkXB9laNf7foIuRxoH-BaS1fZyrKMETmaBo4ZUKi6n3DwXjkkJClRIK3lEj-pK32CJTN-2D8EwrFGJmw3ctD5mvfX05iqxBInHQ5f6N9gmXy0Pa7ZMSdEtfuuXDGYO6XfeAvhRqzMeTXV1vl4ultNciigNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxdc773lpC7wg_z4heSJt30WTbi0ah8I0khPTuTBEGVfhvh5NfDAU0fCgc79DQovo3BZiKz4hev5cWd-I1kEbIIQY0kAZ0eyEHL9pJv35KCWiuRoQd7h138i_KgJdjBtwCXwBnmgubh3X9wzf2p5xTtOaBwn9zd2DN_-lg4bdTQdX7g1RpVmS7kUv8XThyPP6ybE-lGbUW49k_htTW-JL_wdY_yWcc7MDv6GXqcMeUy-5IvihSHSb10yP49IMIbfokfckFzaxOLG3rD08sxXeWaIncS666B40Tk5dBiqDBWN5QpRv1Ri7JLwgcaJqkqo1aq2d_t3RMWajeGivsN0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJQSl6F0femEvrDlXtJaohoRVWnb6URBeMn999A02yRbdEB8NfPg9rXaFZcCqVbXidTIsKAjT8Zfx-BW-dC1nBDmWnLErpJQBHZmn4rhJpAB-nWo8jd7ruzIT_UrfhyXi5NhSXzzupT3XLVzSL4SxxK81z7PDmk14VxjY14JZQUGBv4gn7EbQdzJWuPaMlI1gWlpte4wrgyysNBoVQYlP4GTaR4CT7XKsb11Q96W5oI__7-AeJRXNvsl1fWhWo5xFZZDpNAF4fUPwYROebzKABYNjZUSqFy-ufwl9f61rhIzXvxefjbbAPgcsoDxinA6w2zLXfSFL-21Ek_MZC9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lMsJOVyY_Z5BhsJqGbODVcKj-WVVb2Fk5Qecf4SmbyPGzaiDbw_e7EQWSBFfkxPD67Ys6IDcPsZgUUkmK87LS7IHbiqRewH17T2WcrAzGfDc8-WT-yY2UZKVA04jycQLQiNvf-lGLLOqSjIjdnD6pLfQL9Pqwelv6SFdF8PQP9w2q6Q36nbu3QN5WSV6tzQCiH5b949aqyAY-Jwz3yrn8oirHg8qUNr_5UcDAhWl5xreBhJX5b-n5fjQKc9KDgzCAkoGXZgyz2XFVLLY6ZiBJztsUNzbr_S4VZpiwTjJ8ffoH7CuVzf9MMu_o94NL4o62DoCWjtJy2vEg5dH7Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duIp-Hypr9lSLHS8Nj_uk7UxckHAllc1mN9G399UlQU1jJYcul0Fk5ze5csWyS1KtjiS0o0ToCoA2STYBG0lowf-NtRiI2LdvW1UmpeXOisflOeykGMhsg82k8fZyVRI9Jh1eoPlsFIzgz4eNnm0byubxjQBAeaFNVVIjh928pQc8kce9WnF4kW0mZmv-ENbU98jFAE4DGYB5EhFkwem3cYHAVMKR0ADw63_GnA8X5EjXJVfEDJDRti4M90OB9gdZbTfogCV-hAFHPw92ZPFDxWojcHqGnEA0Y99NZmy8uwYX1xIeotj9PxgMUUjkVB7BlGc2qcgYCwfuJudTOthOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlJG3Km_6GHbHJ7eVSfn2NJTbrb5iJBmEmwmXmjajqLgbi9xR-7ZRYEPECWnEWitE_dV0Edi8NE-D0TorNOTxqILkGsrnvjwybAQI5TbMlT7tChVH_d6xjmxn9r_IwIZBYhMT5NfWj3quA2sNvzMv2FCb_hI2f36Iic0-62sf8uDmBJXxUTZ9Wh92vKroaTwYbvfZzaGIRR_xfIqdESmlvNDIMN3GXK8_u30l8A3ftyN8cCbLJtza9Kk3nZj4ptYDR_IFprgTjO8teh4uzy_WpDk0CYz8pZ0efg787LMhJhhb4t6Gx6AA620_Tx05CfNqoggQj1MYg-tE4MkrX3Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-J_eahDvELSVHzYwmT1MY4_ZZUtwV_hHPN4F3E323RyD4x3BToW7zYgqpxUMYB8WJHtb3Ti5wA-1z42nAzQUwThTl9TwyyQoy9MTOl1D4oVCHAUphGusFVfWq4Y8_2IjXC4NegabyJ6g2-bBILt7_7bUBjwsYoppV7Wtl4HLj6tzktl4UJamqdE3btW3JXPMjVslztA1ViXnwdWh9Jwdw1PWY3JywUFGLuz1e8sYk7WFmZq7GYkqnbbNswG6CfxpoNiYR_kQi3sd8ieokDDzGaEXN7xX6lb60sdcAUQ8AbrLSYJPF_7sBrpcD_qQlW8v2-adYFPVrViRRStCFM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=ekwWdV20EKIgKBdtSqE03WfItYz_AIe581LlKfxoVADtcwyR3zksVmU0lJVmHgrXmBs41gUdcq1ZvrHKPGbFPS6YIIxR-K66O0GrNpSYm8gr4XM-Ry132u3VO_KOmxgjMPACMqHkeHYqiPYtyZVV-tXPc-uLR-W-lQebkOY7C4uqxlRq1U1lI-H95BlVGsQM_rGm_sbAR-eqWc_zJbj9tLlXkVuFSQP6UNWE9JgCvCWbw4SizV-qNZKgZ7ER2hUPkGSC-wekkY6QAJqa7LHWO7A92zDguPc2qBWfZes6fH5_poLD_avvFwa83Stq-T2r04vFHvwqP8CHoMmwXfslqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=ekwWdV20EKIgKBdtSqE03WfItYz_AIe581LlKfxoVADtcwyR3zksVmU0lJVmHgrXmBs41gUdcq1ZvrHKPGbFPS6YIIxR-K66O0GrNpSYm8gr4XM-Ry132u3VO_KOmxgjMPACMqHkeHYqiPYtyZVV-tXPc-uLR-W-lQebkOY7C4uqxlRq1U1lI-H95BlVGsQM_rGm_sbAR-eqWc_zJbj9tLlXkVuFSQP6UNWE9JgCvCWbw4SizV-qNZKgZ7ER2hUPkGSC-wekkY6QAJqa7LHWO7A92zDguPc2qBWfZes6fH5_poLD_avvFwa83Stq-T2r04vFHvwqP8CHoMmwXfslqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=AanLWQAERL9Wmd-uN5X2l2jlGfk_A_xJw915acy34kACkJpwa23rpdjBl9CfJyEjR0Pwre5HU7pQhO3IGUi532TeQ4O0Wco3ieLyNYb1gP9zG6v7as0n1zrhCkc7q1As66k57q8aUEuaqUL0OoU4pldOQU6UQCPHVotlE6aV9ah9K095ecNvtbdr2_7yfIgoQe4vuwc5rg7srjbiQZ2DTkFBYEC-3szlmnOd6Thvx8_0I0EsN0fwSK-xWs2yoti8CUVkDRilwcOQSPV1eFCQxOzsCNBFgSHKEyokIoxuaEuWqVGecXJn4FYtSfpAqupgs7nVr9wv2PT7VItNKbiQ6E9BSuUG6XLul2Nrg6CiKFOZMl1uwNLPwdxUDUS3T9oljNeSjCIPvjKmfodLtZhOMqflGTMYdn7Ey25Zj8vCmJlJuLTJLiSFkW51vfjC2oWtxKydpgz6C_wG7ZIZ5wJXjKv0n1yd6oWWFSm09gOuxi6jD2BeRo2bHLB0cJkX-ND_k_kJ_OMvl7FhAgm-UN1637SYbzJ32Vk9g8aAAmAvd5usAS1ZUj_067w3JP31R_3641JS1Ndx6gBulAEHM-rBzlsa34GajGeR3LxJU9CDZKeVUe7tMfCs5N18sQ1kSfA3gkP9TMCjduKfJPxqkJBWulCGbCpMxQ5mPwG1JNfFB0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=AanLWQAERL9Wmd-uN5X2l2jlGfk_A_xJw915acy34kACkJpwa23rpdjBl9CfJyEjR0Pwre5HU7pQhO3IGUi532TeQ4O0Wco3ieLyNYb1gP9zG6v7as0n1zrhCkc7q1As66k57q8aUEuaqUL0OoU4pldOQU6UQCPHVotlE6aV9ah9K095ecNvtbdr2_7yfIgoQe4vuwc5rg7srjbiQZ2DTkFBYEC-3szlmnOd6Thvx8_0I0EsN0fwSK-xWs2yoti8CUVkDRilwcOQSPV1eFCQxOzsCNBFgSHKEyokIoxuaEuWqVGecXJn4FYtSfpAqupgs7nVr9wv2PT7VItNKbiQ6E9BSuUG6XLul2Nrg6CiKFOZMl1uwNLPwdxUDUS3T9oljNeSjCIPvjKmfodLtZhOMqflGTMYdn7Ey25Zj8vCmJlJuLTJLiSFkW51vfjC2oWtxKydpgz6C_wG7ZIZ5wJXjKv0n1yd6oWWFSm09gOuxi6jD2BeRo2bHLB0cJkX-ND_k_kJ_OMvl7FhAgm-UN1637SYbzJ32Vk9g8aAAmAvd5usAS1ZUj_067w3JP31R_3641JS1Ndx6gBulAEHM-rBzlsa34GajGeR3LxJU9CDZKeVUe7tMfCs5N18sQ1kSfA3gkP9TMCjduKfJPxqkJBWulCGbCpMxQ5mPwG1JNfFB0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgvoXrtLN9T9_1oHHP3zzbwVsS8oHEu-T1aXpY4ugMBDPr2UxD-m2Geq95tHeN84mP8ZvxYdPZNGtzWkZa-UA7Ew1frvndK876aeY8XlhVF0O6qK0d-c5_S7le5f8_xle7NYbuG5DVy49T9JUdAOmEpQry5oY-0_jbPpAkz3I7JElBL4dTlQkyI-YZ8CAmcC3GQEExLSrvWJGj3P-idC3FR5NFDFklCvSDqZqC14i6fqhncDThp2cMAuts5_amVabCyJGlPASvpYkt-IRfkPe2lHNp7Nr7ynmD2SdF5yVdkXgsUHawS6VuIKCPBlFgHDtgDBNfQSuEFof0Kf5XTwe1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgvoXrtLN9T9_1oHHP3zzbwVsS8oHEu-T1aXpY4ugMBDPr2UxD-m2Geq95tHeN84mP8ZvxYdPZNGtzWkZa-UA7Ew1frvndK876aeY8XlhVF0O6qK0d-c5_S7le5f8_xle7NYbuG5DVy49T9JUdAOmEpQry5oY-0_jbPpAkz3I7JElBL4dTlQkyI-YZ8CAmcC3GQEExLSrvWJGj3P-idC3FR5NFDFklCvSDqZqC14i6fqhncDThp2cMAuts5_amVabCyJGlPASvpYkt-IRfkPe2lHNp7Nr7ynmD2SdF5yVdkXgsUHawS6VuIKCPBlFgHDtgDBNfQSuEFof0Kf5XTwe1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIOH9XK9yWa0Lwh-xk2P1EqpTWVetX5Odkzm_KEMnI97rpAOO0YpLD4SYkh6WqimrWzp2IOxEsqufOebDDHO0hfdjTP2YTiH-yEqpcBbD7smHeIGmppyKar_ykNys8Ww5veb5WHzqqdFVTNBC8dhQbMQALCTJby6g0TCZzcI6Pq7sMiz8Oz-oRyCUuN1Lt-W4Eo8jaCmKBCT3EhjsuBynjSyjqmhNpH_j3J06o2ZgRfJXhn4rAXMvR_QqyxDX7_SKuAYggKvh9raUCQ_lcGbVnc0Buhx-xlrE7FeM9QhpTyvLJJFmnpJ84U4_r5xb3zcbIYHwLEn5JOUYJS14nHn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-Ryh82qAZ6Rz6e6olpvsmrmwrc4fro8mctfb1kkW3PwUznA71rxPbZ38ny_fIY7xJ7bDoumsah2YuviobARGFB7gvfz7Q-dYsD-PbFcSkQDsPNGqQlKzJcyvyVW14juGN_5oZCmedavxw9YcLkDPmUkTlKni13iuNlLB0a1euI7RzSyVtCPh6UwOwppRH3VPl9u1fpVuMOle66l4-wZBG8Iil3tmpQNKNhqktYolAZD3JGr-T6yOX-_sZ8-zHxozQAPfENnPsqxjXQ0tdwR-ZZwAjpMwohmtn85RxoXpmaBEVEnM4oYeO9Pew8MObo4ynZB5Mhyrs2xQf6bGmJY5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=mlh1e929flykAqb5IPQ3MqiB6bDOBGXyqvOh02A7Ozqtm4748ZFqNGnrP0yXAcHatZC6rphqwUoVB_1_G-yaX-Ehyg5RyP1ZM-qFjL30CukZJSITgoWF6OWSQBmEz7I4iiNHh-1rQEZmOyw1MwHuzPq2Fy7wKhyU5VpF105EhFaKVS9NP07lEuVd8E14o4dPw1uJFjUzf4ubX-7yEjORyz1AIr1alEuryTobZ5BXshQ6w8qtUasygcQAliI34xihtHI01gA0eUZYfQY9FNic5miUaPmIGBWCDd6UdAq8-YU6-8bkj3kMc83HLnc-ZhC9O9BVTZaWuCdhges2iu7jUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=mlh1e929flykAqb5IPQ3MqiB6bDOBGXyqvOh02A7Ozqtm4748ZFqNGnrP0yXAcHatZC6rphqwUoVB_1_G-yaX-Ehyg5RyP1ZM-qFjL30CukZJSITgoWF6OWSQBmEz7I4iiNHh-1rQEZmOyw1MwHuzPq2Fy7wKhyU5VpF105EhFaKVS9NP07lEuVd8E14o4dPw1uJFjUzf4ubX-7yEjORyz1AIr1alEuryTobZ5BXshQ6w8qtUasygcQAliI34xihtHI01gA0eUZYfQY9FNic5miUaPmIGBWCDd6UdAq8-YU6-8bkj3kMc83HLnc-ZhC9O9BVTZaWuCdhges2iu7jUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=IePq4QLiCxaXMDrP2ls5xMw_KGVefTLd0K5rpxe-noeX6HfVCPXEdWkJH-Pf2r7XOkarR9RXCNX9Oz5Q0BmNLOs5IeoO9qsOau-IAzZiUCebrF7lacS2Nr2fOSbzIb-7DuQR4rVARUu3L683r2AmI361IkwfOI_lTbAjBD6LGHmtNOyqawsAsW-FUNPysu2FszHg5MVzaJKukz65ykJOYoOGLsaMKf9n_lniLyEhfGRjUkuDg7Z6DXd3HYocniViT4cihh6j5b4-RsBSZJaRogf81NtUOyWiQoY6MqZEgj8sabreMU1O6kENEA_8NaOgfMpaiO9P36oS9heZtwi4kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=IePq4QLiCxaXMDrP2ls5xMw_KGVefTLd0K5rpxe-noeX6HfVCPXEdWkJH-Pf2r7XOkarR9RXCNX9Oz5Q0BmNLOs5IeoO9qsOau-IAzZiUCebrF7lacS2Nr2fOSbzIb-7DuQR4rVARUu3L683r2AmI361IkwfOI_lTbAjBD6LGHmtNOyqawsAsW-FUNPysu2FszHg5MVzaJKukz65ykJOYoOGLsaMKf9n_lniLyEhfGRjUkuDg7Z6DXd3HYocniViT4cihh6j5b4-RsBSZJaRogf81NtUOyWiQoY6MqZEgj8sabreMU1O6kENEA_8NaOgfMpaiO9P36oS9heZtwi4kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu26lsYLgDq97BNJG4tWateCa2NkTQNQtp3tvzyWMP8Td-1EOU7Zh7PZSa53-rfsNzoFhqkkxDFmtSQD6UTF4jzCgk7TE20x_a5jkBJYv5_ee4SIX1y9hu0phzWwhY2v-yGtimwfc_j1c3Af9hy_1m81y5vTuiuMzzybvjOXGTznAX_pDBcdwiKCt4PlmZGOqFvNszQtqhnBZsFjvMUl234jTer4nYZ3lnrpSNGPEc6PpS9NU3ORlP0YpaqfuO-evaHUuW0rr2hJFdCxN5oEZtP08fST4InhgLZok_nXteO_840mIAhKolv4XLlu1BwbtvzAMqw0x8MjSZ4ccyL6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=JKwwGOrfK603wOP1ii3MoCbbs60SfDbVEuy08RfXA7obg6N-FLPcau9ClAv3UaoQPi1JASG7_tf992E3gOnXXN9jXKAB-o3yRbCOPb5Ojnifa8XtOYlFDJZ79J5nbNArln_Q5txSdR0kbB3b_hPJ2RTICUtdFwk4hLGkTOXzBATX-8As9AVPHMTQj58tz4b1hjeC8hK9zabSj6Y9EzLpjOafDrsyS3qTOqewyfCVcfbxzhvZsTwfRAvKgGeE8ZOk7gJ4GkJU5cV4TEaYWJcQ1wI1pI7XO_55V7-wymNsl61hxd_V952d9GkXMsmL7pepPQc233SeetFo5jiFfZQb3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=JKwwGOrfK603wOP1ii3MoCbbs60SfDbVEuy08RfXA7obg6N-FLPcau9ClAv3UaoQPi1JASG7_tf992E3gOnXXN9jXKAB-o3yRbCOPb5Ojnifa8XtOYlFDJZ79J5nbNArln_Q5txSdR0kbB3b_hPJ2RTICUtdFwk4hLGkTOXzBATX-8As9AVPHMTQj58tz4b1hjeC8hK9zabSj6Y9EzLpjOafDrsyS3qTOqewyfCVcfbxzhvZsTwfRAvKgGeE8ZOk7gJ4GkJU5cV4TEaYWJcQ1wI1pI7XO_55V7-wymNsl61hxd_V952d9GkXMsmL7pepPQc233SeetFo5jiFfZQb3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=F70Nl43QSyE4kFKrk6SrYbIP-6esuLgt9Ix7ktVnLMRHEil445Mz2iCwQmq6lpRTzB4-KtXffTVtp9utxOSkLrB_nRNTSh35f5ywfGDQhS9yHcGnYyyXf0g937HOdkeo-IIV7BXWbAUalxypR6PI9hmrq2l6k8rWiS9zk7i6pNUeX40V0vCi2W_1KbxPxnAr5obLgWuHvu5A1je6qriYQGW_aKGLJrC6zfjKh08gCwoC_ETzYlJCmEoL04jFlNKbrMooztkRUz16qQiZtwqetmmPc3CFzCkvOXvHA57h8slcQ9SMV1boa_1aO4Xm0Tpd6MHEemhciIyxp8JaJSMoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=F70Nl43QSyE4kFKrk6SrYbIP-6esuLgt9Ix7ktVnLMRHEil445Mz2iCwQmq6lpRTzB4-KtXffTVtp9utxOSkLrB_nRNTSh35f5ywfGDQhS9yHcGnYyyXf0g937HOdkeo-IIV7BXWbAUalxypR6PI9hmrq2l6k8rWiS9zk7i6pNUeX40V0vCi2W_1KbxPxnAr5obLgWuHvu5A1je6qriYQGW_aKGLJrC6zfjKh08gCwoC_ETzYlJCmEoL04jFlNKbrMooztkRUz16qQiZtwqetmmPc3CFzCkvOXvHA57h8slcQ9SMV1boa_1aO4Xm0Tpd6MHEemhciIyxp8JaJSMoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=mPuA9Hclt99FBI6qM3YjdSGQ0BbeaREv-En1FUXHbIVCKm2P2Zh7Nzkza_nVVHvVBSgcXE-n8WBIkVkossk0VGVuwRhH_Pw3jaChwuy9FrQg3Lz_n5cfPXMwd4cAuSO4FdsfENn_OVRJc0vktbA2MXzmW7uDOsLOzQVCzL4rrz69u-H4hfi3gG7uUe1Nq2vWDdWHhZPiM_lwRpZMzTof884vMku7D_3WCWH6ukmCymJzvd6CDCRKpxANBSyFfV-bO_Aav5qM8rd5eH5X3SM5SHpTSq1YiDnYZGbS9GvNhzB5uKPWC96DKJZPAt1rLGMXF9T6baoConxQSbpmE70rFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=mPuA9Hclt99FBI6qM3YjdSGQ0BbeaREv-En1FUXHbIVCKm2P2Zh7Nzkza_nVVHvVBSgcXE-n8WBIkVkossk0VGVuwRhH_Pw3jaChwuy9FrQg3Lz_n5cfPXMwd4cAuSO4FdsfENn_OVRJc0vktbA2MXzmW7uDOsLOzQVCzL4rrz69u-H4hfi3gG7uUe1Nq2vWDdWHhZPiM_lwRpZMzTof884vMku7D_3WCWH6ukmCymJzvd6CDCRKpxANBSyFfV-bO_Aav5qM8rd5eH5X3SM5SHpTSq1YiDnYZGbS9GvNhzB5uKPWC96DKJZPAt1rLGMXF9T6baoConxQSbpmE70rFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=QV-Xe6AdCwHU3CPhD5BqYgo636CpnfSL--MhQWv-Rhd_Jf5y9ZqvQNBP54ctmBHS9gITAQPArXprLRmPz1EeWa15aGZh4l7G3jBfW-BJMaG0BjRsMVzL4lfuA9NO_C124D8f8wPek3YPddV3D_1lQuVjYs_jzuX1gEC5tC_RvOVbgb7fZnxPfPXa1D9WK0D5Q4vTd-2-4APIL2b6Xqe4FR-SaZlujBkY0Iu-_TAqEL4FGl5fFt6u6IvCNJZO7J9mXBcyWj8xW0AavNOzLhOpf6f-qJJFY7y-LO0PR-Zs3TAhlkjWIcZ5KvJpibqXofJSvHEipUBFbw8nwfK3azM3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=QV-Xe6AdCwHU3CPhD5BqYgo636CpnfSL--MhQWv-Rhd_Jf5y9ZqvQNBP54ctmBHS9gITAQPArXprLRmPz1EeWa15aGZh4l7G3jBfW-BJMaG0BjRsMVzL4lfuA9NO_C124D8f8wPek3YPddV3D_1lQuVjYs_jzuX1gEC5tC_RvOVbgb7fZnxPfPXa1D9WK0D5Q4vTd-2-4APIL2b6Xqe4FR-SaZlujBkY0Iu-_TAqEL4FGl5fFt6u6IvCNJZO7J9mXBcyWj8xW0AavNOzLhOpf6f-qJJFY7y-LO0PR-Zs3TAhlkjWIcZ5KvJpibqXofJSvHEipUBFbw8nwfK3azM3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=X2P1fUSZYpoUT2yS84udlOeiKMTXAzxLYBCWqtZgnzgstnyiiCFGmSWujRI6BENxIttUvxmVTx1K9FsZ4Oo0j6RyhKg2YPD0R-JgvVoJvfv_1tD0c5BFoc2zxuwwmpT2E02lwSUJ1tlp_anJdcJ84HwmJRi2Y9LrcsCyVx_Z_tNmwSAVX98F5SK1et8lJtYtWfxaDE3XJVX6TDGg9wXK663eHT8Td7QQHPedSCEY539AGjd7joaHXCvFoTxjp05J4HMdZbCO6-8ERilRWJrqdLzTvKcyLNMk1q3wMp1sTENhVylXumCmqyYaVkZANhHFW3-3uSzmEEWOOEk1xEbajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=X2P1fUSZYpoUT2yS84udlOeiKMTXAzxLYBCWqtZgnzgstnyiiCFGmSWujRI6BENxIttUvxmVTx1K9FsZ4Oo0j6RyhKg2YPD0R-JgvVoJvfv_1tD0c5BFoc2zxuwwmpT2E02lwSUJ1tlp_anJdcJ84HwmJRi2Y9LrcsCyVx_Z_tNmwSAVX98F5SK1et8lJtYtWfxaDE3XJVX6TDGg9wXK663eHT8Td7QQHPedSCEY539AGjd7joaHXCvFoTxjp05J4HMdZbCO6-8ERilRWJrqdLzTvKcyLNMk1q3wMp1sTENhVylXumCmqyYaVkZANhHFW3-3uSzmEEWOOEk1xEbajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=Up7bz2RLFbLuyzm5uJHZf697dqbGCdFePGGer-rcM5FuONXcTMYrEvFMpVDbs0ihlQvTgSiW_fg4tgkCPuIOCYT132oI_sy8jN7EJ7HSQ_3l9jCGRmzRQCP8B1glaAiQ7GV3fjEVOce5Vbld3mwtKULcTiTomFBZNpg9MiYIRFixPlcUz7yGTGAT4eGTWKnrDPaPBiJE55hp4sMA25b66RZWatLHHsptsMRwf49crChiPUA-Y7Ij_nV1ot4Hin-ryJr4Wv-WRopAARKkC7Y-h0bS085xhWHVCm_2al0mrEIz3RmI5IPiHcLBdgbX9wp4pvxB-ND-G35cZ8ekzVozQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=Up7bz2RLFbLuyzm5uJHZf697dqbGCdFePGGer-rcM5FuONXcTMYrEvFMpVDbs0ihlQvTgSiW_fg4tgkCPuIOCYT132oI_sy8jN7EJ7HSQ_3l9jCGRmzRQCP8B1glaAiQ7GV3fjEVOce5Vbld3mwtKULcTiTomFBZNpg9MiYIRFixPlcUz7yGTGAT4eGTWKnrDPaPBiJE55hp4sMA25b66RZWatLHHsptsMRwf49crChiPUA-Y7Ij_nV1ot4Hin-ryJr4Wv-WRopAARKkC7Y-h0bS085xhWHVCm_2al0mrEIz3RmI5IPiHcLBdgbX9wp4pvxB-ND-G35cZ8ekzVozQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=nlMdLRVHg40mUKexPpQ87q4d6m9Q787qTKm89nSI7P_KsULoFhXPLGw6N_yFim0KJzXnxDOsg5dkU4GAvF8Ivvi2zuqAacXmJWSRjDMMn4W5h2wqAmHsT2CZTe0jK4vzsBIEJ0uHux216NuhDq5h4y6zSqRR8Yn-b9StYNsYJtLRS_IoS6t7vLbw8mIdPvdwavt4rv5l0Uk31QNcO0-3as_eB5yZ3szkbIfi3C_lcfOKVZfVGaMYyWPTP2KVYXGaU3ElGClDdz3tk-ltoBv-p2VPdjbQ7ztSDrd_TX3SIkCjCe9PBQHRkplxnhnxJKc_um4CvLO6dzqrwXR9_KbKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=nlMdLRVHg40mUKexPpQ87q4d6m9Q787qTKm89nSI7P_KsULoFhXPLGw6N_yFim0KJzXnxDOsg5dkU4GAvF8Ivvi2zuqAacXmJWSRjDMMn4W5h2wqAmHsT2CZTe0jK4vzsBIEJ0uHux216NuhDq5h4y6zSqRR8Yn-b9StYNsYJtLRS_IoS6t7vLbw8mIdPvdwavt4rv5l0Uk31QNcO0-3as_eB5yZ3szkbIfi3C_lcfOKVZfVGaMYyWPTP2KVYXGaU3ElGClDdz3tk-ltoBv-p2VPdjbQ7ztSDrd_TX3SIkCjCe9PBQHRkplxnhnxJKc_um4CvLO6dzqrwXR9_KbKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Oqh3f8I7OC4jZtw4HKA8DVdfP5eHUtrc3F5YjhFCgSMgrt8lUqpV9CfzQDSq9YvzZzPvlUDApClSIG8NpGwneUUVJqGuBfQMgafYRkoBaI0-vd7nEbFeOB60ldTnnMZQdowJacSxc7_hLWzSi7F5U3JWIbSvtbubab9JRcn_1DZ3sUyojXmmQvBlNnQi6ux0L9QQSxoVnigsMlL8kLmCgu1o-ZqlGMiIkUExvvoAYc_sr2OA0A_XYh67Pkh3kkVM1yxtdRmERPLsLI1Nmv7IS68Z_JzF9Tdc3SCfb0rntacrwIfkyMJ3PqSKRk4UXywVZzoFEsSot45FQlkHJ4eacQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Oqh3f8I7OC4jZtw4HKA8DVdfP5eHUtrc3F5YjhFCgSMgrt8lUqpV9CfzQDSq9YvzZzPvlUDApClSIG8NpGwneUUVJqGuBfQMgafYRkoBaI0-vd7nEbFeOB60ldTnnMZQdowJacSxc7_hLWzSi7F5U3JWIbSvtbubab9JRcn_1DZ3sUyojXmmQvBlNnQi6ux0L9QQSxoVnigsMlL8kLmCgu1o-ZqlGMiIkUExvvoAYc_sr2OA0A_XYh67Pkh3kkVM1yxtdRmERPLsLI1Nmv7IS68Z_JzF9Tdc3SCfb0rntacrwIfkyMJ3PqSKRk4UXywVZzoFEsSot45FQlkHJ4eacQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=cvD1j4VX1vU5O0IcenTyIAq06LtCHRLOnsAveDAhHD8HuOmvH_m_yPszkv2T-mOJEPDgz6Gdz6TudpUkPIFLFAUZjLoc-nOsmKyG55uTMkjR_qExhv6RJpw2ckppAdmyKhsGCF5YD0p5StFG2NXx9pPyJpaefxVVbabAB8AhHbhkqQ1sz93qpVx6GphfbDJuaoMK7zWcCcPjDsyStCUorOda8q5RRKuzOf-n6pwKP29tpRzh4319axxMzRmJ1djW3hX-L-8upJR7Qiv00cLcTm10J5X0JrRJJcKgO2-zPtAOYmRwFKu6FKUf2RBazsTOhO7vFabxfKt5KqDo-5eE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=cvD1j4VX1vU5O0IcenTyIAq06LtCHRLOnsAveDAhHD8HuOmvH_m_yPszkv2T-mOJEPDgz6Gdz6TudpUkPIFLFAUZjLoc-nOsmKyG55uTMkjR_qExhv6RJpw2ckppAdmyKhsGCF5YD0p5StFG2NXx9pPyJpaefxVVbabAB8AhHbhkqQ1sz93qpVx6GphfbDJuaoMK7zWcCcPjDsyStCUorOda8q5RRKuzOf-n6pwKP29tpRzh4319axxMzRmJ1djW3hX-L-8upJR7Qiv00cLcTm10J5X0JrRJJcKgO2-zPtAOYmRwFKu6FKUf2RBazsTOhO7vFabxfKt5KqDo-5eE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ret_xANNkP4mNWA5Fb8-2VYhA3GQndBi1MDQzjL9gfbB86BG3CN_vLnk731uovjRqFckE-bZLDJw3VDA8jFnorvo68pmo3BgkXTfjoFRa4c_pBlTDsgAZ4hM6THTQSv_9aVn4qdLtgOEJmnqZW0e1g2RbFxBt3lMrvNSiiSnSSMozC7ydeXklmsKqiJshx2D_twk11oZD8T7IM8oid19xZL14ddKOl5ErqNiygOJskpSCiWKA12YnJlDRyeJcxCRJJ6J594sLeE8oySfksbpKqTWrwJ4_jvIXtU8GGvu44y5E1NDGCVOhX3kwn_0JG-Ic7_oDGw2XF0D-TQ6i4q-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=h8fyBQbd7o7wHlFcp61XgCP8xzK67p5Q4C0pvdBFqCbJAPSoYPNBDBwN8Iz5FOpIothWqr3XEtPefp9Anr-VGPgqQhMkzR1vp4nZxjLwRJoXh1wtkwEH-QK918PbXKkD71q3wyt2sH4RhDCJ_eMO0yxuLjDvc8IZbfxbxtAq2HgTlSX0v-UQeoWIk11OEAfPviN1_BBfEk1ck9yfm9VNw7ktR_fOZTqtsop59iQoXG6gCVlvSyeJbiQ0Tl38qXG2MlTuNoB4tJ5CEDngJQtyAOBqR3RO8OZiRoneC136KOL3oeWwQSWDom8dlPX9WbbK_XedRjEFHbfgE2NH_mu01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=h8fyBQbd7o7wHlFcp61XgCP8xzK67p5Q4C0pvdBFqCbJAPSoYPNBDBwN8Iz5FOpIothWqr3XEtPefp9Anr-VGPgqQhMkzR1vp4nZxjLwRJoXh1wtkwEH-QK918PbXKkD71q3wyt2sH4RhDCJ_eMO0yxuLjDvc8IZbfxbxtAq2HgTlSX0v-UQeoWIk11OEAfPviN1_BBfEk1ck9yfm9VNw7ktR_fOZTqtsop59iQoXG6gCVlvSyeJbiQ0Tl38qXG2MlTuNoB4tJ5CEDngJQtyAOBqR3RO8OZiRoneC136KOL3oeWwQSWDom8dlPX9WbbK_XedRjEFHbfgE2NH_mu01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=oLFkBkHg-Pip8Y5IzDdMLzcR7Ssqc9lldPuq86THKcj-tLjIMplDqSo0V67_pTsNGdc5gI4XGF6qK8sEHTKlD_P7ro5Qk-Zh3O2HQrVRyj17kqSltEG--r9Ab_aYM3tpdMK8LVXjM1kWR6s-YUy212-RDLoP36mxLEbDl6eCT9ONPGsOsUudPD4Movcg8iPXXNurUoAim3ae6qfCZxhFmXhKCl-qn9egCXKQr1k1_Fc1Hbut2at9JJTjEhXnlLT0dlogASBYZOIqoKtkAyB5CY5bBjwOZehddxwITB2TNqFHRjKCXlLsmYjq-b_jxruJG3INbT8u2aiplpBSQshdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=oLFkBkHg-Pip8Y5IzDdMLzcR7Ssqc9lldPuq86THKcj-tLjIMplDqSo0V67_pTsNGdc5gI4XGF6qK8sEHTKlD_P7ro5Qk-Zh3O2HQrVRyj17kqSltEG--r9Ab_aYM3tpdMK8LVXjM1kWR6s-YUy212-RDLoP36mxLEbDl6eCT9ONPGsOsUudPD4Movcg8iPXXNurUoAim3ae6qfCZxhFmXhKCl-qn9egCXKQr1k1_Fc1Hbut2at9JJTjEhXnlLT0dlogASBYZOIqoKtkAyB5CY5bBjwOZehddxwITB2TNqFHRjKCXlLsmYjq-b_jxruJG3INbT8u2aiplpBSQshdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a41Oci9k0WsI_zTUXA6TBCvpIZWerI23Te6vnIQK4sMEfjC9je59B2beJMWeU0chXHKFj1CJzqg4A_hnbBSdMkepqlc1-7scGIyg3UdeSBS-m_e2kkWvmem_R92ZYwRAihQfgn8xURMHu4Fxrw8zJoPrIILyEZG1BPQU5X9jRVLZ5YPoK-0p-FB9pbvX4T1mOETXkUIwG8EkTriwRCE0eBKUuKFQO5adW2YwcFjgrHwv38C2atuL-waWyawVaPqg1vnxLS7Vv9fuMIe6OarKp2gMeSh5x7z17VG3VNegQUVPDWf8QBi2xWnxwLaegH37MXPV9H4NEXB5YVj8y4syrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=LqExaS-wH6IsLK4DKAbEgcVR1kSIX7A1Hhk1B1inLozA1PCu1ShakY8_Rn55Jdwk6bOiE11L2eMBfzbtakk-bdL9ZIEZnjoX9UmD1JbDDthU6fD7ZVNBW8lByi375cCMJGI1jsnv4koTkzmhQxtkxhcLxkK2BpXV9M6PPTBFp9J8bX5BrCHqM4fIkTkgKrme9Il-QE2XmTPKAR8sY-Jom0J9qFtbURHlNJlCiZSrujf7pQBgYWKAwCDg82J7yM8tVmsx7DgL-iecz1RMGYyXiuIsOw6NWdW0k-PfhpZckPTOzzTouDHkkIs4y9wcMr5ZaD1x09f66dYHm94iBJ65FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=LqExaS-wH6IsLK4DKAbEgcVR1kSIX7A1Hhk1B1inLozA1PCu1ShakY8_Rn55Jdwk6bOiE11L2eMBfzbtakk-bdL9ZIEZnjoX9UmD1JbDDthU6fD7ZVNBW8lByi375cCMJGI1jsnv4koTkzmhQxtkxhcLxkK2BpXV9M6PPTBFp9J8bX5BrCHqM4fIkTkgKrme9Il-QE2XmTPKAR8sY-Jom0J9qFtbURHlNJlCiZSrujf7pQBgYWKAwCDg82J7yM8tVmsx7DgL-iecz1RMGYyXiuIsOw6NWdW0k-PfhpZckPTOzzTouDHkkIs4y9wcMr5ZaD1x09f66dYHm94iBJ65FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=R_eKqlcqK0trdaZ8tFrx5a1O0Fwqadv0WPcTrG-2JBYL3ZCUtoMF05b612IqynO-qC0NaV3_b84vlso1RLfN_zpk6FCPStxNQbLnVQ5ezIbS7dJU3pm17pDeU0JAB0zvKmx3iFu8ymkMkA-utJQ2rSkHoLyTgXpJKao3UuFYrStFEaUeIfjtAYH6MWoIDLqYlU4OA-q_M_2tvG6Y-P4cB1SBr0Yf5fdeYCObokF0Bb5nhIXUihwM6fkqHr3PqhtmxGF1dd48s4kQg7a8PAsqjD75M1UqjQHT72SGu7EnF4OydUFtenl7I4YKLO2i8nNS62osqr3c03FqxAWkxBLGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=R_eKqlcqK0trdaZ8tFrx5a1O0Fwqadv0WPcTrG-2JBYL3ZCUtoMF05b612IqynO-qC0NaV3_b84vlso1RLfN_zpk6FCPStxNQbLnVQ5ezIbS7dJU3pm17pDeU0JAB0zvKmx3iFu8ymkMkA-utJQ2rSkHoLyTgXpJKao3UuFYrStFEaUeIfjtAYH6MWoIDLqYlU4OA-q_M_2tvG6Y-P4cB1SBr0Yf5fdeYCObokF0Bb5nhIXUihwM6fkqHr3PqhtmxGF1dd48s4kQg7a8PAsqjD75M1UqjQHT72SGu7EnF4OydUFtenl7I4YKLO2i8nNS62osqr3c03FqxAWkxBLGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=d0gnQSe7x8fnDNfemLnG6NW71ByvLT8eScKnWQ6K-5cY_KaGnflnZruPxiP4x0Z84SNC2SghUgFqXfDQhHLbC-s5VSi_zwKFU3wNdJBKEF4HG3rVYOYhHeaTQKskr2EPQyPWINO2soM26MIaeXzoTpSe15ImgjWu1V0z4elaaxaTsN55iukTXjBdmgONH5a5TdY7CtZKlGFDRrbxUFkeHAW8C0PHjmUbi8PTVm6lySS4jidIK6hW3Csf9CYxKjHynhCXOfUgVxG4rC9QlO6CD-vPKgwrrAS2ce3HBJ6NoeDF-0hD5XyLRIBptHiZ7PpLg-QjNvsGZ7HdYJF0LFPv9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=d0gnQSe7x8fnDNfemLnG6NW71ByvLT8eScKnWQ6K-5cY_KaGnflnZruPxiP4x0Z84SNC2SghUgFqXfDQhHLbC-s5VSi_zwKFU3wNdJBKEF4HG3rVYOYhHeaTQKskr2EPQyPWINO2soM26MIaeXzoTpSe15ImgjWu1V0z4elaaxaTsN55iukTXjBdmgONH5a5TdY7CtZKlGFDRrbxUFkeHAW8C0PHjmUbi8PTVm6lySS4jidIK6hW3Csf9CYxKjHynhCXOfUgVxG4rC9QlO6CD-vPKgwrrAS2ce3HBJ6NoeDF-0hD5XyLRIBptHiZ7PpLg-QjNvsGZ7HdYJF0LFPv9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=ND0GKcQer3nYe8XQRFnvin-lYgKFHNu2GBZ35aUS0mzi79SirAZGhWc4BV-sO9mo0QyLL1ObbYQC3P61YSTLaCZ43x-l8XJ_f6Bz3lt-xx3fubDiC3W_vRV6KaEblB5NimWl9hykEOx33-IUEiVFx5ZY3b2fCuWaybZ0mKgJVYSMpOOG0QXubGW5lMs6UwwRhn7XJp7Vk-iXnCLa6ygFmaYhVHzWmag5g-x-e1WxSrPBNHboSCnn35VmfHbZNdfYtBziZkh4jlEN0BVZb_t5WCyq_IR4cHuie2IvK0g023eQjj0D1wX_nyaxZQ-Cv2cy5Wj5oQEwIwlwR-c3oMN-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=ND0GKcQer3nYe8XQRFnvin-lYgKFHNu2GBZ35aUS0mzi79SirAZGhWc4BV-sO9mo0QyLL1ObbYQC3P61YSTLaCZ43x-l8XJ_f6Bz3lt-xx3fubDiC3W_vRV6KaEblB5NimWl9hykEOx33-IUEiVFx5ZY3b2fCuWaybZ0mKgJVYSMpOOG0QXubGW5lMs6UwwRhn7XJp7Vk-iXnCLa6ygFmaYhVHzWmag5g-x-e1WxSrPBNHboSCnn35VmfHbZNdfYtBziZkh4jlEN0BVZb_t5WCyq_IR4cHuie2IvK0g023eQjj0D1wX_nyaxZQ-Cv2cy5Wj5oQEwIwlwR-c3oMN-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQ76DLw4AKiXZ-3R0s6YrF0eEg7m5Plh-x-PLSm-2NrMv-3fJ9HDknnDEDG1RoqmRF9P6Y-bzIWPC_sfLGhSjn_OAuba6p9CrYX_1TX_W-Q47-zOk4K1yxGWTm_jqqvHmIlEuZHUgOo5QeOdrMWU9SKYgxMWPz--1MiG2aXL2f4ESDQzr9aiSutcPnZUsSgds2e4nXCBvlX9rlGkI2FBVdXui8uhWC2dz9mKckzL5Cb8PW9sPBYrH0Ge1SMhcV-SqxrZUYk99_PYouFQz4BFqCJtStdLQBpGbio6ytZ1zk5ZkvWC6YGucgzkR6jJBdQEqQSCU3R-oEHBJ2o7WPiCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJL3F6mKx5D-58p4mF-Ma1LTD6B_totGy1BGyPkCtImkyXeCcxK8yd6SyouhlmmTYhCY7q0OW9cxKRmT8V05Z_IJJIxHGfI0nDWAkT_bDJmYxJSiZLit7ipE04RhziQW8PelsfWIklcY0nQlY7LluBAv0I-atOG7hMbtugKbG_6Z7vIvsM0Ul_Gcc5uqMFvMQ7EdQ5w6kPMvgWGPh7Z_aolZWnmu4IUEmFBAwl915BRfcuSqcqApJpoJ-CBf9d2UU-Aknbx2FHuu6cxCGa274bRDOUmsZ1oPEEBYKpq2Mhmk_Zoyvy-ddj2pVCBCR5msz5KGEbptPPH74_5Eg4SXnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=IW9JP9GAz5JdUnwSdATc860orlVtNBk35TZhOUi8D268gWoRSZDxmY2tO61o-3k8oA2EPE_qMeVKiThmGxQRnucV_2MJhnAqOH3DTXYYG2B9XiaduVP0yzOGe8IkvWhcmpxJX0yJN7J0gmF7DPGVEsEFJVgHCtJBs8UWeGUvTr055AR9pdOmhoBlUwLStpejnSx2zfglq53zKJWvOTq7ojXIccvHJ_ckPp-1dFd-rIuHD64gCoXu77ZS3mm1IDLKozOMAMRwoz3BRw--tBoEjlfgSzBXSm7XtNSerjV8WOCNG4mh0cYWNYy7ZS-bACNcWB4H5nh1l9FhMlREaPL5dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=IW9JP9GAz5JdUnwSdATc860orlVtNBk35TZhOUi8D268gWoRSZDxmY2tO61o-3k8oA2EPE_qMeVKiThmGxQRnucV_2MJhnAqOH3DTXYYG2B9XiaduVP0yzOGe8IkvWhcmpxJX0yJN7J0gmF7DPGVEsEFJVgHCtJBs8UWeGUvTr055AR9pdOmhoBlUwLStpejnSx2zfglq53zKJWvOTq7ojXIccvHJ_ckPp-1dFd-rIuHD64gCoXu77ZS3mm1IDLKozOMAMRwoz3BRw--tBoEjlfgSzBXSm7XtNSerjV8WOCNG4mh0cYWNYy7ZS-bACNcWB4H5nh1l9FhMlREaPL5dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-wKT159MQ_6-sQyu_CFDkkqkgvmgutrYuI58IeYWAt7cnsXyQlzPTM0K1U9VSzJBhoR_CvTfa8iLjCFzn-WVBhEp1EjNdRPsV0EYkmU8X7WdEZeLc8H0Wv6dofC_625P4eBH-U6wdcd-EhxCTEk8NZWPuT0HAdFORhbPGYIFu01ZraU1mPeaHzDQFB0Y9S3ZBrHyirVuvIQwhBJCsjNhnrd7nwFnrm5GmSXOhUFYfuvGvyS6A8hwJ0QFvGsfsZFHnKDIUDi9QxpOPQYV0PcwUaLTLYlWiBcfVC1qZiliMbolPs31cl2v59W00XNZCz8jWNhah_jZRoJCgPj2mKXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=PBkyfLe6nlfSEumBHShSCk4vXmFtdPo6TH17dFVDej93E4AVz39dMhib6GQRJOR3Rmf-nQw3jJmU4Cvpsp4nRPCIYg5APKskYMIQCouFHe3gWpIIMntTamazxQQxaAtvkGoJEFCEkBLjAL__2xbSJ0-yXzxpOVaoXVUOlgoYTkGZz218rzkO53dlog_0xdQqFotTaobYH3cvWrSN18eY0xtFKaRPv86HLTQltQdkEqHRb_JlqzmHp9oJaFdBjdZ-PswCB1WA0OYhJ8lWAnLVLC43hbsmC9l4qDEMgSmb0pA3dycjYpKDiWlr6P5lOGl9UZbOJWZ2K7RQr68XwVtFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=PBkyfLe6nlfSEumBHShSCk4vXmFtdPo6TH17dFVDej93E4AVz39dMhib6GQRJOR3Rmf-nQw3jJmU4Cvpsp4nRPCIYg5APKskYMIQCouFHe3gWpIIMntTamazxQQxaAtvkGoJEFCEkBLjAL__2xbSJ0-yXzxpOVaoXVUOlgoYTkGZz218rzkO53dlog_0xdQqFotTaobYH3cvWrSN18eY0xtFKaRPv86HLTQltQdkEqHRb_JlqzmHp9oJaFdBjdZ-PswCB1WA0OYhJ8lWAnLVLC43hbsmC9l4qDEMgSmb0pA3dycjYpKDiWlr6P5lOGl9UZbOJWZ2K7RQr68XwVtFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=gQzusq4TUxT2rvhQIF-rmHHFPJ5CuVYl8hG46nE76Wo-h1KpLPr9bdCwGWfi7tZEv17ZZ-zCNWXp6cBNvoNtwQ1oO8_HsCiIfqp3QJfqzQqZVDHCHMHoQdN47xMRfKG_S9M8BcsaLZ3Ox2iOuAUwymnrokcqRqb8hTmG8WHqPqXx95-ihFzw19rI1z5EDNlOu9J9xxtpI_fUtn0t2pwGpY-jcBmoRDnilm0XP6s4vFf2qXJlzQ4y5pdf4In8B_wzkHe0S6Nlbtrz_G7J6I1sIAE3ueIBYXRlZbBeuBEm0-mEhueeMyG8DN_xUzIdjOdoZZWOzXURA1DPcv-YeeBdnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=gQzusq4TUxT2rvhQIF-rmHHFPJ5CuVYl8hG46nE76Wo-h1KpLPr9bdCwGWfi7tZEv17ZZ-zCNWXp6cBNvoNtwQ1oO8_HsCiIfqp3QJfqzQqZVDHCHMHoQdN47xMRfKG_S9M8BcsaLZ3Ox2iOuAUwymnrokcqRqb8hTmG8WHqPqXx95-ihFzw19rI1z5EDNlOu9J9xxtpI_fUtn0t2pwGpY-jcBmoRDnilm0XP6s4vFf2qXJlzQ4y5pdf4In8B_wzkHe0S6Nlbtrz_G7J6I1sIAE3ueIBYXRlZbBeuBEm0-mEhueeMyG8DN_xUzIdjOdoZZWOzXURA1DPcv-YeeBdnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=kjKNo8WQ4x9Kt-3I9tGcwh4NPo2AFFVNj1HT9pAnK5ntUEYSk8vHdG8EYLL718xPklllY-0tSfI_LfpaVhvUNaNnQiiZ46Iw0702c7XsRfWiIM1U0Z6GjrMUveDjiitFajW_xtN2eAx5TpQAl4Yk4j2bSInqFRjKjyQa_FDDIXPDQdja6lSRZleLqavMUBrY_993pfHMA6y6D4IPfrUAl0m_NFhyR4FRqoj1r1KwwGhExPQPRRKWxHpLAP1ps2lCtC1USBR7LXhXRflTKipvrzhaxFfWBnZumowogi6XghcjR0QVl8_EENjvge4FcHxZcVxFwsKAizwm_PaxACXVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=kjKNo8WQ4x9Kt-3I9tGcwh4NPo2AFFVNj1HT9pAnK5ntUEYSk8vHdG8EYLL718xPklllY-0tSfI_LfpaVhvUNaNnQiiZ46Iw0702c7XsRfWiIM1U0Z6GjrMUveDjiitFajW_xtN2eAx5TpQAl4Yk4j2bSInqFRjKjyQa_FDDIXPDQdja6lSRZleLqavMUBrY_993pfHMA6y6D4IPfrUAl0m_NFhyR4FRqoj1r1KwwGhExPQPRRKWxHpLAP1ps2lCtC1USBR7LXhXRflTKipvrzhaxFfWBnZumowogi6XghcjR0QVl8_EENjvge4FcHxZcVxFwsKAizwm_PaxACXVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=rM_DcWFW3GYeD1HVDxKFbhce8LrEAtrsCgh0Xj8mpSiiZ_hmeMkXlLeRVGdhpB0EuvfmDC53FJkXNTB2wlwIFrQJxZdavR8YWSprN8Vi4NmrsyFiuYh9-jYZXs55vLZcBPbgYLHt1Zs4Iw0GPVEx5RrhmdWtTao-4fECKA0URSp_rLXxG8-Z6TwkzX0qmXCY-XlnI2-MfLI4Q4eTW2bqqlIb8Pyt6-t3uoHpydTdUoiY9dGD4KA2zlqH0GugFRSrrXdrktnGqlDOZaK4uWKdDh40Yvkr0T5VeHQi_MlsvgbMDu221ezZA7Pcd5mB9JHPNohIxiAmy6mojhmFnG6aVDcU_lQIQNXgzwxqojAtO2F-zVHpjX-T-Lqz4N0aAOG-3wJrJD7bYCKgXiUflQlbCr-pk2b_zitgUJKna5sKFQEa4M9d7D_Pt4OIhrMZRU3j9v0T0ecYZrHtVk6z8gR6XJql5YPgatHuCmS-zfJCdtHsXkEV15K-xMC3eq5oqO-eaiyViTvtm_SfbujJD82StvMU6MZWh2vsWxT7IWyNYT8DSBwemVWEeSD5u3Gbqdn04JoIsbFrq5my3IkwA3_AQx_v-1Ju46QsYsY_SmM_tCQ8yDT3h0wzHWwC4al7D3_wDUoeLV-lSYCHERSNxSv8lnfktdMrMJtWchazvCP_PxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=rM_DcWFW3GYeD1HVDxKFbhce8LrEAtrsCgh0Xj8mpSiiZ_hmeMkXlLeRVGdhpB0EuvfmDC53FJkXNTB2wlwIFrQJxZdavR8YWSprN8Vi4NmrsyFiuYh9-jYZXs55vLZcBPbgYLHt1Zs4Iw0GPVEx5RrhmdWtTao-4fECKA0URSp_rLXxG8-Z6TwkzX0qmXCY-XlnI2-MfLI4Q4eTW2bqqlIb8Pyt6-t3uoHpydTdUoiY9dGD4KA2zlqH0GugFRSrrXdrktnGqlDOZaK4uWKdDh40Yvkr0T5VeHQi_MlsvgbMDu221ezZA7Pcd5mB9JHPNohIxiAmy6mojhmFnG6aVDcU_lQIQNXgzwxqojAtO2F-zVHpjX-T-Lqz4N0aAOG-3wJrJD7bYCKgXiUflQlbCr-pk2b_zitgUJKna5sKFQEa4M9d7D_Pt4OIhrMZRU3j9v0T0ecYZrHtVk6z8gR6XJql5YPgatHuCmS-zfJCdtHsXkEV15K-xMC3eq5oqO-eaiyViTvtm_SfbujJD82StvMU6MZWh2vsWxT7IWyNYT8DSBwemVWEeSD5u3Gbqdn04JoIsbFrq5my3IkwA3_AQx_v-1Ju46QsYsY_SmM_tCQ8yDT3h0wzHWwC4al7D3_wDUoeLV-lSYCHERSNxSv8lnfktdMrMJtWchazvCP_PxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ3UPSl0BIYozINJpDq4OOIz9UrzdHf5ADrxfFR5za3wkNcrdE_Uhh9XTJF96Aeb8lcRLfeCKZNaSD8Wtq7JDN7dki-bitWBpANeg0r00ZCuW7sEHMT2J2dixL-Rs1DzPr_uarX3DJhpAAqJp3CcwBMPkoyY8GOJXruepqhhMG0Kz7n6sJzya5nKlo4NoZNRLVfpRNIer7AZccIABi8e-3rBy4bM4t58lYRQzA8ccdx2tjd6kasdRJcu2njXIntpPPM33lNTq8rPUjDHRUgIUH5CDf2k-dlf_AE1XJfBA498cy6871nX7qBdW7sBkwH8loHiwZ87nSDdmC0lMuAMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUwWtVl677pUzCFlqQGDgD_0UgwYnzeVxgpDOQiSdRZxOQ_792JVyqF4d9y9i_NwCx_NMCN_9FXPJi9St1RtmQJjg2QAByfnmxLfKSNayOCFZnMrvsbL_OVcbHsPWLxIVawWO4pYA7co5YVC6OpCGvRFidM0x56F5rg3UBJ6IJgzbmv7ORchStTi9vyr5UL0rw5mQ93wbqTe18eGowKmdVfvASB4r1RY8xT1MeIlGsuJvgPXVfAjhs7zHqX6hHlVNheMcTyPiIdyVN7zkKAV2XHNVtVWB7u7DHSSce-4VnUTIfBMD6Kd8uKUVrKeEbbl658rD6yaxFgGGDvu2-DbvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=lNNeV3aRXdf6z8pyAAhVwIh1NHN3GwntlpnF295f2zgMwrKaQ0Vi-1EzjfckPGJYzBD5BEhMUJYQdv4Y-uqA0B7x4XsK3RSQcRiIaX6Fn-6Mp38fZGAcuAxHYA93kYXPRmW_n8WKrQRmhCJzdTEYVt8T2ZLEhIYROx6Ool3OkYizHBcdilJ4OBvNai-Qc6zGNsX0fJ89K8JNyiamt7TJDJoRgvv1Y1PL5LHo_SEtQmTproM2VC6bhl-KLGP1BNImWlitIHfO0UZexy68c_TKuLqTKSWU6dSXDjzvf99nlBaMBjtJQ_tDWhU14y-xgWqOorkMW_GBnlbU-dzUsr39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=lNNeV3aRXdf6z8pyAAhVwIh1NHN3GwntlpnF295f2zgMwrKaQ0Vi-1EzjfckPGJYzBD5BEhMUJYQdv4Y-uqA0B7x4XsK3RSQcRiIaX6Fn-6Mp38fZGAcuAxHYA93kYXPRmW_n8WKrQRmhCJzdTEYVt8T2ZLEhIYROx6Ool3OkYizHBcdilJ4OBvNai-Qc6zGNsX0fJ89K8JNyiamt7TJDJoRgvv1Y1PL5LHo_SEtQmTproM2VC6bhl-KLGP1BNImWlitIHfO0UZexy68c_TKuLqTKSWU6dSXDjzvf99nlBaMBjtJQ_tDWhU14y-xgWqOorkMW_GBnlbU-dzUsr39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=CktKBZJJBrzrweJAmAv4KjmHZz7w6xDg5VQwfbUcxiGkGY6qRFTiszDJJrnrc-YFlvuGGik5FQctkK_os2mMqRH68nVFClGaNTAK2VCuu3v6buek_UDjcb7raCt8pRa9qa85ionk_W3FhajLVNex1K3hS8BGlkt4OArSQPIKVQWrJNsg9yc_f1z2w8DN4Tv0pyvoUcZ6uDUebtxzftNyOIpuilQz24yLfLG3eTTkikNCKc44wvltANJmH4MTHcORYqR8DateZahV-omDIZorxt5TE16VfRhabBpt1_KUuY9tr0RfaKI1koJpkOl5bqqUC-QgCAfeN5m7rByvinE0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=CktKBZJJBrzrweJAmAv4KjmHZz7w6xDg5VQwfbUcxiGkGY6qRFTiszDJJrnrc-YFlvuGGik5FQctkK_os2mMqRH68nVFClGaNTAK2VCuu3v6buek_UDjcb7raCt8pRa9qa85ionk_W3FhajLVNex1K3hS8BGlkt4OArSQPIKVQWrJNsg9yc_f1z2w8DN4Tv0pyvoUcZ6uDUebtxzftNyOIpuilQz24yLfLG3eTTkikNCKc44wvltANJmH4MTHcORYqR8DateZahV-omDIZorxt5TE16VfRhabBpt1_KUuY9tr0RfaKI1koJpkOl5bqqUC-QgCAfeN5m7rByvinE0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCzEkWXIgHJDhLtqf5pBJZti0TPjTBF9oiseh2vwDG1WeiVttjIiajiZrjlw88nqTIJD4oNWfwSbYHRqesoKemdxEkaGEo9YmpFb_OUBk6TdbET6btln9t4t07o7Yufbmp88zC9_W-6Nlx7XKk5L3Z5RchlSp75gB3devM7Ba5Ub9aufr15aX8Y9B7v3VW2uBOmORGD8t5ulexeu5VmF0pQkwivgQpQTu98vmSL01IN6IipSFYEQLNvY8lRdWgOXfkRbTUk--5q_IjTGWgqWCYqedjSrUN1x1f_NdAMDpUvfO89XO37GuXFYXdPW6ly7Pdq5U2Dwh-dAmNy9NGGsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=d-gdMmxcdaRm3wGELDN43kUxUwWOT5W6CQlNR_-OxapKF4H9uqRGeBkIh3Om-__8MefFel5WO0bHri9qiNdGiN1TOSCItB-bzMWuu8mhjfGRlT8H6zp2G1stke0wkxRWV7qt2CTlwrunrW7eqDN7voNNdh5jCASev-X5rZneNHmpfmT75Ix2yzebfJq4GnWaCz1UfmgMSHekgGcAj4OgH7NTisaoSjXS9bee070w_6rAOUcigsxTZ33EQRnRGBBzMzOawAvOCV7UWRjc84NFeVGyLKDEwG2FsquJWUy5YiD9UIG418rYF8AKbowNb8NkrE_H9le65UUjV2pBB_zy8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=d-gdMmxcdaRm3wGELDN43kUxUwWOT5W6CQlNR_-OxapKF4H9uqRGeBkIh3Om-__8MefFel5WO0bHri9qiNdGiN1TOSCItB-bzMWuu8mhjfGRlT8H6zp2G1stke0wkxRWV7qt2CTlwrunrW7eqDN7voNNdh5jCASev-X5rZneNHmpfmT75Ix2yzebfJq4GnWaCz1UfmgMSHekgGcAj4OgH7NTisaoSjXS9bee070w_6rAOUcigsxTZ33EQRnRGBBzMzOawAvOCV7UWRjc84NFeVGyLKDEwG2FsquJWUy5YiD9UIG418rYF8AKbowNb8NkrE_H9le65UUjV2pBB_zy8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=Q27yTU4yj3oucv4ARYI6YlBXikNKeJvXzdU3iHs3B5qjBEjHFavIgtSA0dYYmszkUSi97hTRAP7CB1gCTQbtsAZk4VZDYCH3p8c8IDJ2zlyy7pBwE0lfTbhOuUImWCriukX4j-HpmCyqW6hSHl6xmcFd0Y8vE-IZjzsdc76PWQeAtdaYHxuSAUeEyDMQ578CmX8N59wtJvN7Jz6NUsIczYFG7na4xuaxqEvV5heukyyyM8Kfx_5nSfXzOwOsWL-C6haa-MadW78USbUoOWSG2yjYuce0LuI1oYwPgY_K1MpSJ1JB6Bd9hhOXeBqTRxjp_wTlgdqRhTk5VLrvwZQD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=Q27yTU4yj3oucv4ARYI6YlBXikNKeJvXzdU3iHs3B5qjBEjHFavIgtSA0dYYmszkUSi97hTRAP7CB1gCTQbtsAZk4VZDYCH3p8c8IDJ2zlyy7pBwE0lfTbhOuUImWCriukX4j-HpmCyqW6hSHl6xmcFd0Y8vE-IZjzsdc76PWQeAtdaYHxuSAUeEyDMQ578CmX8N59wtJvN7Jz6NUsIczYFG7na4xuaxqEvV5heukyyyM8Kfx_5nSfXzOwOsWL-C6haa-MadW78USbUoOWSG2yjYuce0LuI1oYwPgY_K1MpSJ1JB6Bd9hhOXeBqTRxjp_wTlgdqRhTk5VLrvwZQD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=ARDleDj4QWrpwjkHnsU1fvP-wIiiXQQPe0ILfPqUXu-_sWLMDm5it99J8RtBmiPNiUREOiEdd73H79Tn0Ey6lhtppKEYnQ8Ihaj9HOjlDpnF85XLzAnEfhlmNxWyHydiO0v_86IYbobZQf-M47ed-reFvY7i8u9a-XcJXXmkypzKrJO5QwNZ91HgTaVMJEVtxkRE5N25rIJiem0dJjI6-Gu9zbwa75zBEF8fd4J1zbHdQKaKuDvsjHlGQZfSkkJHc_Krm_s8G6QXt41crbhniVSEJqW0e0DNHkttIQHLBECWb8aZBCDYBZlBeSyCJQ6kv4CSfLm8KzwxCLb7wEFV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=ARDleDj4QWrpwjkHnsU1fvP-wIiiXQQPe0ILfPqUXu-_sWLMDm5it99J8RtBmiPNiUREOiEdd73H79Tn0Ey6lhtppKEYnQ8Ihaj9HOjlDpnF85XLzAnEfhlmNxWyHydiO0v_86IYbobZQf-M47ed-reFvY7i8u9a-XcJXXmkypzKrJO5QwNZ91HgTaVMJEVtxkRE5N25rIJiem0dJjI6-Gu9zbwa75zBEF8fd4J1zbHdQKaKuDvsjHlGQZfSkkJHc_Krm_s8G6QXt41crbhniVSEJqW0e0DNHkttIQHLBECWb8aZBCDYBZlBeSyCJQ6kv4CSfLm8KzwxCLb7wEFV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=ewjtkmdnx8aEHJkIHS0giUqCCimTX-3HtRn4sSBHWC1wZ_fX6wl3IpqeoIaoHwAhxKm-g1bZVfRXz6sl3IMerw95m-DQS1tSf_aM12J8MwN-VHi0mVKhi_2rdE_PpoRzzRn4lZ-BHQmFhknTS6dRF7Z71FuCo8iC3nyq5YzHBhNA9xWi3C-TMYvbBH7Qm3LcvINc3LzuTlN10LTpLEriavSM7vKIxe2XEmvpv_s_U3HszwszQMHg2yGKpWm2bBELEF7KjrA7ndwgw4TVpllW09T0W7d6XofrHNFFZ4q_PBieEhc5_j_MhB1IxmbD06Z1VvVvL-oOQ9PoTNZsxQEp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=ewjtkmdnx8aEHJkIHS0giUqCCimTX-3HtRn4sSBHWC1wZ_fX6wl3IpqeoIaoHwAhxKm-g1bZVfRXz6sl3IMerw95m-DQS1tSf_aM12J8MwN-VHi0mVKhi_2rdE_PpoRzzRn4lZ-BHQmFhknTS6dRF7Z71FuCo8iC3nyq5YzHBhNA9xWi3C-TMYvbBH7Qm3LcvINc3LzuTlN10LTpLEriavSM7vKIxe2XEmvpv_s_U3HszwszQMHg2yGKpWm2bBELEF7KjrA7ndwgw4TVpllW09T0W7d6XofrHNFFZ4q_PBieEhc5_j_MhB1IxmbD06Z1VvVvL-oOQ9PoTNZsxQEp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=cSFjHY0Fo0SlxdadVBWfJcGtKgOgOZRoTuABSgqh086-F9dqzx0NaeV2xmhOSecyDy3-EBSTjbSriX8Nj6em-Ga1_h92Fu5VVlyHKYJH2LNdEH1AuNWWVTvm5VhUECe26p6BdZVD3-AdrGDlHn4cTEMRgNSEyS2cZCnJgu-exLbvWMhecPJu6muSP8DvNcaJPIex3fj_FmqB-DRBQXoQTvWWo4LsVyIiRt2WIe-LZ-i6cn-L89J-mkzvlMN8md7zQaPDvt1OueevxNBydFuvzpOaA4rnRYA3xhrVE7iz_7a3SZ1qwJKkDGJu6flhfSgQpErEmtFOe_thhWdR9XIIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=cSFjHY0Fo0SlxdadVBWfJcGtKgOgOZRoTuABSgqh086-F9dqzx0NaeV2xmhOSecyDy3-EBSTjbSriX8Nj6em-Ga1_h92Fu5VVlyHKYJH2LNdEH1AuNWWVTvm5VhUECe26p6BdZVD3-AdrGDlHn4cTEMRgNSEyS2cZCnJgu-exLbvWMhecPJu6muSP8DvNcaJPIex3fj_FmqB-DRBQXoQTvWWo4LsVyIiRt2WIe-LZ-i6cn-L89J-mkzvlMN8md7zQaPDvt1OueevxNBydFuvzpOaA4rnRYA3xhrVE7iz_7a3SZ1qwJKkDGJu6flhfSgQpErEmtFOe_thhWdR9XIIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FMdMRJxwRzJywDq-RSPWrgKUv0sgzaGrwdn3Nkbyni9g1HVg3jLbmXII9S-z3zZcRjrijR3NdNcwML4TRz4sUvypu1nCj1NRntR9PlmLgiZpxIawKIyuDUQ20OzCNfu_cs8xbzqTpS27PCG204gciVkgznCWMV5GE8ehhfhkKGu9q5No-iGpj7GJyYi5v7RYUUZx1Dg05u8efDEhsZrmnp1zuL68_i5-5hIA1MT09ELcXcwk38EjUS9wysibV0NB-PxEbLDRGB1zdt8awFjluCzVAB2JQtb_6aXuU55PVWKc73qpG9poMd3l7KEsp9lSBlADeIQw2FnjdGEknm1ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1bTFoUD7u9ka8MKxA0o7puyj9RONaSb_qh6_UekrhRIlIcvhvRl77emLDxV_SgUclbFzY1IFBovacXyKsZtUIjKVF4l7cCE4EXM2k5Z0W2mrKUVL2F69IGSXyyIEgd1vvtbk-EuAbUpP0D0oTE920c7UwgYZXhuQSfzNwzGsQVFP0e52yKMqFdL-osvoVYEpDZwQ_a5NMXNiAnxtkvRWrPs0YfFJ5JtCM7-XZxlTI8QEJJWqXVovYFokADTW0hn5lkMTsUwYJwjxrJ1oHBRh6-J-23-ozFFq2U4yAPHJWvOX7TPmQnBZ2Cu0Lo1gCCJJBo7MeZe8ND8im1v4OFzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Cq82zlJQ6JQpKrOFHLkLedFGTSfyZhOB4Jde0Gvs4k_Wwv7Aqpw2F8LE5OSPXPnEIGPl3wAhFeNtwwf_pcGdihBOB0Bb9yLQuEIj3-NISWJamPiRt8KZmHijMiqlEZLbN_S-XZlRsvmRxo9FzFDIzs_u_zxcpHimpSoXAJlvE4qJj7BcRCALwqXWS4R5rAS9oKOOxTV11ktisXH8YHJvWesQWs-RUVH_J-bVDWXClZoOcp8DRRcQ8wPXoISNsw2dxrVtGLfT154TK-DMWhSZBorACmwOVseJq9oTNyw4lTlcbXPV6kYqrudCDaqMideMV4wjqX89GgKVu5g7jQUb3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Cq82zlJQ6JQpKrOFHLkLedFGTSfyZhOB4Jde0Gvs4k_Wwv7Aqpw2F8LE5OSPXPnEIGPl3wAhFeNtwwf_pcGdihBOB0Bb9yLQuEIj3-NISWJamPiRt8KZmHijMiqlEZLbN_S-XZlRsvmRxo9FzFDIzs_u_zxcpHimpSoXAJlvE4qJj7BcRCALwqXWS4R5rAS9oKOOxTV11ktisXH8YHJvWesQWs-RUVH_J-bVDWXClZoOcp8DRRcQ8wPXoISNsw2dxrVtGLfT154TK-DMWhSZBorACmwOVseJq9oTNyw4lTlcbXPV6kYqrudCDaqMideMV4wjqX89GgKVu5g7jQUb3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=BztgYZvQaUC73PKrROR3mCyem-WfBT7UqWFQWTUudTujoMxyBjhmlRHzRxEQ8AQdP7NhJBb-J9JgSVwlcn2_ZPC8dIL5jscri26RSRnWDFKezebEQOEjyodh5IsTznj57Yxurv5voq6J2JWawLOUFBgGS7UuNR0hLe8ugFFUWlDKDFuvsQk5zlhcGvxOCfJOpj9pGIdJzgZtZwhRiuXZ2aw2AIlZz5Mz5wRxy9VyknutqNWGb26Nykre2rusfExbHqTB3qgDMDJfE7b3MqgDWRmN_WU2d5i8DYUE0SJX07L4bznbMgwgYuTzzPNUEOX-PoLxvr4seHRaSWqw78BfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=BztgYZvQaUC73PKrROR3mCyem-WfBT7UqWFQWTUudTujoMxyBjhmlRHzRxEQ8AQdP7NhJBb-J9JgSVwlcn2_ZPC8dIL5jscri26RSRnWDFKezebEQOEjyodh5IsTznj57Yxurv5voq6J2JWawLOUFBgGS7UuNR0hLe8ugFFUWlDKDFuvsQk5zlhcGvxOCfJOpj9pGIdJzgZtZwhRiuXZ2aw2AIlZz5Mz5wRxy9VyknutqNWGb26Nykre2rusfExbHqTB3qgDMDJfE7b3MqgDWRmN_WU2d5i8DYUE0SJX07L4bznbMgwgYuTzzPNUEOX-PoLxvr4seHRaSWqw78BfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gEQLTLs3bbHyzw8dxt2D6PKeMIMLu_ia5-PnOjJiDkuVEo1o0QhXwSKqz0_nrqk8u1oKvkz5PgsP7-oCPFpmDi2_Ei0WfBhISQKvW15VbppfcJ_pGI-LQNSBA0kej_y1t8c1u8ZsSLvCVuLoNyu7SF_2MC-Os2vOoBvU1HsJb1zic96ajrhrcMQXNnLKVfYRsGWsEDdSJNCJ9oUnH4pVFmmGYPfbxIRfBgFvErcG2jpA1cI9wxrPaLrRzHLSr_u2GX_d4lESO2OJR6qQmZgt4prQQH1gz-2Dv3irk0XPcXcQgJCRorWBmXE8sUNSpRaywVR8hCy8kmEI2tTURDtJRlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gEQLTLs3bbHyzw8dxt2D6PKeMIMLu_ia5-PnOjJiDkuVEo1o0QhXwSKqz0_nrqk8u1oKvkz5PgsP7-oCPFpmDi2_Ei0WfBhISQKvW15VbppfcJ_pGI-LQNSBA0kej_y1t8c1u8ZsSLvCVuLoNyu7SF_2MC-Os2vOoBvU1HsJb1zic96ajrhrcMQXNnLKVfYRsGWsEDdSJNCJ9oUnH4pVFmmGYPfbxIRfBgFvErcG2jpA1cI9wxrPaLrRzHLSr_u2GX_d4lESO2OJR6qQmZgt4prQQH1gz-2Dv3irk0XPcXcQgJCRorWBmXE8sUNSpRaywVR8hCy8kmEI2tTURDtJRlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6730L8M5IrV5SMwzAJ8tm4cvP95qDwM9WlCg9NLM_ZXgIbAxmMqYX4YudePAm4Q-xaSoM5M1pp4msPk-fQpQgTeXBuGtEMSSD7nvvGXI8QdGMVpARn8ftHsmOwyiC8hqBoLs9doeLZ5ZSeQ89DOPiiFcMBVvU_yarQqmj2aPcywGISfChkTk0rSFQ5tIxyPsvyngyQahd0C-vq9UopLuKTb8WD69WkMTKT0ko-nJ86wg9O7pL3Xq9tapqcXWijaaLwwWAGHNusw00F5tTKW2u6PWFeynBQNG8vezI8vIkhXvEHHbW1Cv766TSAA8PlIJQ9XqFQ6c5jbhGl9CmZapjKU6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6730L8M5IrV5SMwzAJ8tm4cvP95qDwM9WlCg9NLM_ZXgIbAxmMqYX4YudePAm4Q-xaSoM5M1pp4msPk-fQpQgTeXBuGtEMSSD7nvvGXI8QdGMVpARn8ftHsmOwyiC8hqBoLs9doeLZ5ZSeQ89DOPiiFcMBVvU_yarQqmj2aPcywGISfChkTk0rSFQ5tIxyPsvyngyQahd0C-vq9UopLuKTb8WD69WkMTKT0ko-nJ86wg9O7pL3Xq9tapqcXWijaaLwwWAGHNusw00F5tTKW2u6PWFeynBQNG8vezI8vIkhXvEHHbW1Cv766TSAA8PlIJQ9XqFQ6c5jbhGl9CmZapjKU6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=vSnkuQngT1-OdDC_Oj9k62MbvNwCrIuCDXkogpPq8nuGGexDBHOz7chAeNtb-o6KQAy16ZyzTd5I18lmLaPqeuF0oEpvFU2P_dwoJazbjiYaVkcyrjvYf8wme8icLHd9VueqN75vUwBlCOIi_gX5jmWuCQsrUHVz2ovJWfxnFVym-MBNawFx-erCHbBUI-gNaEWh0onkAVJRybTnM2Rx6RCEnpVuTJSvUIZIWigutN0koWx7T4UEwSmaJDBzw2LvpL2MBff6jW6DkuEg_05DxY0yyt69PhCrE9bzXwGN5TMS2kbN9UkeEe5AQLS9475k8IqqSvtDbwO5pZGPcBWLelRY-ATFg0OjEfUTYHn-34Gp-Pe2pfsDV7QoJ2wLV-qC3iCsdVfiZYK7sP374Uvpfy-B8GB3IgRqwegTPCzXcQ1U6kyjslMVfTbt2XfIJ9qN3tk2DC2fPYhscbkO2N5fCQPj08V7UsCdTT8JanT8Y9bbMyxYuiliBuWsZ7dMFLYqRnBBE5-62eT044fv3bkbI09yaKrXXSF_9EyXjjlT-6tBbVWJQzGDPqA0nZQ5k_M3LfgYoxTWZQF_Y8q0abzYirocYQ4cYNZFP_b_gttAdoYtfdWZz_yngOthx4x-FnQRBUfhEaYQeWvB4Tb-OzhcF8H1UeZTVvdKq-QjCaJPrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=vSnkuQngT1-OdDC_Oj9k62MbvNwCrIuCDXkogpPq8nuGGexDBHOz7chAeNtb-o6KQAy16ZyzTd5I18lmLaPqeuF0oEpvFU2P_dwoJazbjiYaVkcyrjvYf8wme8icLHd9VueqN75vUwBlCOIi_gX5jmWuCQsrUHVz2ovJWfxnFVym-MBNawFx-erCHbBUI-gNaEWh0onkAVJRybTnM2Rx6RCEnpVuTJSvUIZIWigutN0koWx7T4UEwSmaJDBzw2LvpL2MBff6jW6DkuEg_05DxY0yyt69PhCrE9bzXwGN5TMS2kbN9UkeEe5AQLS9475k8IqqSvtDbwO5pZGPcBWLelRY-ATFg0OjEfUTYHn-34Gp-Pe2pfsDV7QoJ2wLV-qC3iCsdVfiZYK7sP374Uvpfy-B8GB3IgRqwegTPCzXcQ1U6kyjslMVfTbt2XfIJ9qN3tk2DC2fPYhscbkO2N5fCQPj08V7UsCdTT8JanT8Y9bbMyxYuiliBuWsZ7dMFLYqRnBBE5-62eT044fv3bkbI09yaKrXXSF_9EyXjjlT-6tBbVWJQzGDPqA0nZQ5k_M3LfgYoxTWZQF_Y8q0abzYirocYQ4cYNZFP_b_gttAdoYtfdWZz_yngOthx4x-FnQRBUfhEaYQeWvB4Tb-OzhcF8H1UeZTVvdKq-QjCaJPrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=buHj4w5JdKdgp6pdFai1iXuRSVAmxpb8GzVA2ZXUoQPFbAC4t-mJT3uNV7u-nqLQQd5-DvjdTtZ0KqHkmzHPb1zddDFpxAoIfhfNCA-cSemegAarqZYhZSIIn698zNyPdruMvxMFH1-Sj6KSaZ3H2zTBF70IOyofgPe91XYu6TEaHSgERYU6hAYaJL8yLBFjrTKzhLH_ku_bAXCIDz2UCkcDT3KoYNyQb3wXjC8-DKsH5WmlaC0yxcpyxL6UFp4GHITu8hm4M2xval7bIzj6xYF573o5nBr1jwOAyEvj4TL7N_t7pbOeSSobkxDoB9KMxZk3vo6Tu3OfiHwRund4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=buHj4w5JdKdgp6pdFai1iXuRSVAmxpb8GzVA2ZXUoQPFbAC4t-mJT3uNV7u-nqLQQd5-DvjdTtZ0KqHkmzHPb1zddDFpxAoIfhfNCA-cSemegAarqZYhZSIIn698zNyPdruMvxMFH1-Sj6KSaZ3H2zTBF70IOyofgPe91XYu6TEaHSgERYU6hAYaJL8yLBFjrTKzhLH_ku_bAXCIDz2UCkcDT3KoYNyQb3wXjC8-DKsH5WmlaC0yxcpyxL6UFp4GHITu8hm4M2xval7bIzj6xYF573o5nBr1jwOAyEvj4TL7N_t7pbOeSSobkxDoB9KMxZk3vo6Tu3OfiHwRund4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=QSL34rJm7v4AEZ9zT494aqbVb3Vvi7O58iWibsro_5LbDS6ewuyIvJ9Q44iYevsO1cPlEy5ZlZwafUqcuVkMEzdy8YhZeCoQbrZKP2UsCk6piccN3O1dHJg5fu3japHYKEQSE_2i8-76RcpEFIpuqRCEBsvS5l8RXG7MmTW7SKJbKfQCfUw4EWabHvvWmefCFudcmG7s9HnXOxr1thgz5Mw4h3oraQY_gpTMxlQyKgaOkaXNjRSRXXvh3CZYjDC8JclSvTUBLFN2v1l9_9reXDWyWKLNlma4DMzU9W81LOe8nQDa039GcELP12FWOplqRkTu42SNoignHjKZDzS4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=QSL34rJm7v4AEZ9zT494aqbVb3Vvi7O58iWibsro_5LbDS6ewuyIvJ9Q44iYevsO1cPlEy5ZlZwafUqcuVkMEzdy8YhZeCoQbrZKP2UsCk6piccN3O1dHJg5fu3japHYKEQSE_2i8-76RcpEFIpuqRCEBsvS5l8RXG7MmTW7SKJbKfQCfUw4EWabHvvWmefCFudcmG7s9HnXOxr1thgz5Mw4h3oraQY_gpTMxlQyKgaOkaXNjRSRXXvh3CZYjDC8JclSvTUBLFN2v1l9_9reXDWyWKLNlma4DMzU9W81LOe8nQDa039GcELP12FWOplqRkTu42SNoignHjKZDzS4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=mjM72jZvXGrqoLri9CCU_TOzrO8YawHA2d_wTINu_M_Vl4QYaZo9YGIYbomhm87IalDgo9RhUGihUw7nbj-CXCDyhMgZhYiipnZRv2NpP2Vd1ML4ipnqhJ23IXPG9iC8qPq9o2lt3VSZu9m1GHtrdN_Mwdgve_btcuL_J-o9KSQ6tWd4NnAeGkYB359AXdrLsCAFTUIjttnYL8L8Dw4lbLDhHJUlOe9MEl3jA20mGc6wkc9qULetS7yiND_ANX8lg_9QBdiqq7uq0aniAM7sk5mc8Bj_ME6pb22VFXp73YBiJWmj2qlOx3-e-m3UN3RScnxe-GIhzVGmUFy9DaebXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=mjM72jZvXGrqoLri9CCU_TOzrO8YawHA2d_wTINu_M_Vl4QYaZo9YGIYbomhm87IalDgo9RhUGihUw7nbj-CXCDyhMgZhYiipnZRv2NpP2Vd1ML4ipnqhJ23IXPG9iC8qPq9o2lt3VSZu9m1GHtrdN_Mwdgve_btcuL_J-o9KSQ6tWd4NnAeGkYB359AXdrLsCAFTUIjttnYL8L8Dw4lbLDhHJUlOe9MEl3jA20mGc6wkc9qULetS7yiND_ANX8lg_9QBdiqq7uq0aniAM7sk5mc8Bj_ME6pb22VFXp73YBiJWmj2qlOx3-e-m3UN3RScnxe-GIhzVGmUFy9DaebXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
