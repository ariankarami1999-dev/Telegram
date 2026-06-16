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
<img src="https://cdn4.telesco.pe/file/Q8DLS9piyvS5KkRcN0ZOwf2xfmJ7_WOrPC1rTkPuH6KNVj-ggMWwXuf2LEVVMKzJBhKDdNQer-4T--stbuTY7UkvSI5qCbxwkE-dUt5UpmQ28Tz58IbkuhiOf_Qb5fgdPVCDSgGqO15TlBCEz5jmNBLGCtadCkw2inUHc0IoFNrJTGkZW--bJCFJkHwQrF4dm7XBzD0J_ziE1kCY92XLHEb_jB3zObGkgRNXqSD3t8zLibLER-lGb174SItnOVq4vV8PiiEGIQMBj5Anos57bjYzpzXWMouGYfGMC9zBZXjpoGNjarDbHId3X1ZpncV7BTmBJ-Pq4tElkM31d1vYhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-128482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک منبع ارشد حزب‌الله به تلویزیون العربی گفت که ایران به این گروه اطمینان داده است که یادداشت تفاهم را امضا نخواهد کرد مگر اینکه شامل خروج اسرائیل از لبنان باشد
🔴
این منبع گفت تهران خروج را شرط لازم برای نهایی کردن توافق می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/128482" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7a9z-MXWiDUtS_uWALrl8o_p23BhNPQCUQZXSB-t6THWocmLu-EXP3MmGWejAVGg3cL3oSMPD0560vvGPIBDNwImA_VnqB2zGMvX0sFa7hNuPR0BKtzEr75F73bqOO52StAXL62mruQ2tY_IKraZzh24fHwL5yW0Orz4x8daSwD9uZtGkxyNoaLrhd3ql6Xby8xVN33WyKZokhGd4yAxnw3Z8hclPn70zkzfiQkEDEGUu9moVmK3Dijpf0xQQOHLsOlJ-1JGf6P2hj9WEEu2VD3IfjtzDVzesgA0CchPP3OBKKLnApPx3fIJ_0SZC1i1ZYezcQl2ddflvQs43_h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/128481" target="_blank">📅 16:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران را داشت اما طبق گزارش کانال ۱۲ اسرائیل، این درخواست رد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/128480" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ در مورد توافق هسته‌ای با ایران:
این توافق در مورد یک چیز است: ایران هرگز سلاح اتمی نخواهد داشت. هرگز.
🔴
بقیه آن، صادقانه بگویم، بی‌اهمیت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128479" target="_blank">📅 16:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: توافق با ایران را برای بررسی به کنگره خواهم فرستاد
🔴
ممکن است به زودی تحریم‌ها بر نفت روسیه را دوباره اعمال کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128477" target="_blank">📅 16:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره گرد و غبار هسته‌ای ایران:
ما عجله‌ای نداریم، اما آن را به دست خواهیم آورد و نابودش خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128476" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره یک خبرنگار اماراتی: چه آدم خوش‌قیافه‌ای. آیا او از کشور شماست؟
🔴
محمد بن زاید امارات: قطعاً.
🔴
ترامپ: او رفتاری بسیار دلنشین دارد. مردم من خیلی بدجنس هستند.
🔴
محمد بن زاید امارات با خبرنگار شوخی می‌کند: حواست باشد حالا.
🔴
ترامپ: می‌توانم همین الان او را در یک فیلم بازی دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128475" target="_blank">📅 16:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: سناتور گراهام همچنین گفت که توافق نهایی با ایران باید برای بررسی به کنگره ارسال شود. آیا شما این کار را انجام می‌دهید؟
🔴
ترامپ: هرگز به آن فکر نکرده بودم، اما انجام می‌دهم. برایم مهم نیست. یعنی، می‌دانید، دموکرات‌ها — می‌دانید، ما به آن‌ها «دموکرات‌های احمق» می‌گوییم چون آدم‌های احمقی هستند.
🔴
خب، چیزی که دوست دارم انجام دهم این است که آن را به کنگره بفرستم و بگویم «نباید آن را تصویب کنید»، و من آن را تصویب خواهم کرد. هرچه من بگویم، آن‌ها می‌خواهند برعکسش را انجام دهند. به هر حال، برای او خیلی خوب پیش نمی‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128474" target="_blank">📅 16:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=s2kMPQsq997gkf5BxXCzEDRLYewAE6vkQzhatQuFVi9zVd4xD9gWaY4gWDD_CRpoI7BKye_nXCzhfNR9KERfACs2EcMk5R059S8AnkTnWUa0O4oOMuGFFQRlBu2n2goME7c76IKxYErkb4GU32HzPSDh5JKdtG03RUxabY7xGAZWBib9GhZvWMLEJZRDvphivoiS4xBxOL3rWfcvvPGczQzoL8Yw2MQA613KSxVfBJOf9skpmHUBhTKu7bu1QLud2O1g4Qf13jCy2z8KZGNRrSI31cfLr5uEtxUpHcq2qxJAXgYTJ7xqUGriCjm6BtmTIqhoq_Iv_8phWFcCjM19sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=s2kMPQsq997gkf5BxXCzEDRLYewAE6vkQzhatQuFVi9zVd4xD9gWaY4gWDD_CRpoI7BKye_nXCzhfNR9KERfACs2EcMk5R059S8AnkTnWUa0O4oOMuGFFQRlBu2n2goME7c76IKxYErkb4GU32HzPSDh5JKdtG03RUxabY7xGAZWBib9GhZvWMLEJZRDvphivoiS4xBxOL3rWfcvvPGczQzoL8Yw2MQA613KSxVfBJOf9skpmHUBhTKu7bu1QLud2O1g4Qf13jCy2z8KZGNRrSI31cfLr5uEtxUpHcq2qxJAXgYTJ7xqUGriCjm6BtmTIqhoq_Iv_8phWFcCjM19sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: تنگه هرمز باز خواهد بود و همیشه بدون عوارض خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/128473" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a17e9d5f.mp4?token=DvRioxnV0E7cEVDT1nN_eCuTqYEhMuyZfnoGYj4z6_NcBznoeCHLdskfF0B5J2yr8s_wxo5Siq4VQm0VwH274VQsN3d1hhy3ZbTgfu_2cOIeCsR-9AVU4T-diJtx7lsGBqKN_83P1qFXmQepwOcEmdTPe57g2z14u-RVlrzSYfXzEfLbaMtNgY7ljima7KZAwi4eG8KhhyIF3FJaKTe-3pqE2skWPraatJPBHAc-A5ZegSQplFYE_q0wmTX8Gm7QL7EPKdNgv2AZU69emgk1Rtu8a00xL62kgsBiP0nYR8Q3-SxnlEkuCsJItByywcbtN6px1_4ylHjDpI5Plq5QhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a17e9d5f.mp4?token=DvRioxnV0E7cEVDT1nN_eCuTqYEhMuyZfnoGYj4z6_NcBznoeCHLdskfF0B5J2yr8s_wxo5Siq4VQm0VwH274VQsN3d1hhy3ZbTgfu_2cOIeCsR-9AVU4T-diJtx7lsGBqKN_83P1qFXmQepwOcEmdTPe57g2z14u-RVlrzSYfXzEfLbaMtNgY7ljima7KZAwi4eG8KhhyIF3FJaKTe-3pqE2skWPraatJPBHAc-A5ZegSQplFYE_q0wmTX8Gm7QL7EPKdNgv2AZU69emgk1Rtu8a00xL62kgsBiP0nYR8Q3-SxnlEkuCsJItByywcbtN6px1_4ylHjDpI5Plq5QhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: لیندسی گراهام شکاک است؟ باید با او صحبت کنم. او در دردسر بزرگی خواهد بود.
🔴
لیندسی خوب است. او مشکلی ندارد. او شکاک نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128472" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9dd03f8e.mp4?token=Dpobbjmi1x-zvWhvnqMJQpAEyNkraXQEVZuGoFPhRX4_aYSQORbQWj-pgRlNr6m6xuMOe9F919exSk0sS8htIpwVEHrdWlz4XlQsV1RbTKn2wU6mqBKrwrP0OUwg_wh8FbWd_LHPXh5RYi38llgm_kI8D2PxQlDSwCSPS5tZkKQTsGZxaHHtOQ6Bg3PL4HX_bGuolx7d5131-_lTqv0uYZm9Z1Bl4-u6cvnp4vpjf3iQVmMr8WWRyrfBkuOVMFq4C7x-XpI8IIX1X7UhCMBulvGYqCHVoQm4hhcXvLVcZjzSieb32rRDW6jXabMYoeuCQnk8H7EOsxJ0Qy_juqwKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9dd03f8e.mp4?token=Dpobbjmi1x-zvWhvnqMJQpAEyNkraXQEVZuGoFPhRX4_aYSQORbQWj-pgRlNr6m6xuMOe9F919exSk0sS8htIpwVEHrdWlz4XlQsV1RbTKn2wU6mqBKrwrP0OUwg_wh8FbWd_LHPXh5RYi38llgm_kI8D2PxQlDSwCSPS5tZkKQTsGZxaHHtOQ6Bg3PL4HX_bGuolx7d5131-_lTqv0uYZm9Z1Bl4-u6cvnp4vpjf3iQVmMr8WWRyrfBkuOVMFq4C7x-XpI8IIX1X7UhCMBulvGYqCHVoQm4hhcXvLVcZjzSieb32rRDW6jXabMYoeuCQnk8H7EOsxJ0Qy_juqwKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: روابط اکنون عادی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128471" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e1926caa.mp4?token=dk8f2hG3eho1gem8cI-Qy6jsBrA3Pcd0tCLRfVyISHsxo4dqE0tJpjCTIAgmLp8gyi6OFELmWlH8UpVDf2lEM9SrdlF1_GwFblG2j-NY_MB9-hjwcvYJTOvKvSk_-kkuFFqWnd9iDWMs1AIc4u5PSayw7qa8jmTxn1cEZr6NZRaMBGUKZcz7kZjJi1fNS6lgbAFD2mDLmCxP2h7TL7dL4Dv_8JhNIGR3ZVblWRciL1TZtZOiMzchMdfIkb2aaEvyyjoz5SKtN3xKGx5VDPTKmwAvI1Iq9px_pnVLK4N12BKQ0YkAQLnpJfQVrSLRi3hz0b0YPy7ix95p6-W0nM1oBI2_6C5cg5sm-evgsy6Gunfd-x5qI-ShnmQdPF8THEhPtkUNjPFVxS3oljjq1Y8F1ZozQlnNr-zdOCLnYt3RViADbuRomUytF-Jus2mBq3TBvLXZ9Pw93HT-FQtmjqAzQa7C_FLgJeyjLf2d0krug5wS2iEDdypXmdaT_gCGP0gIHLE8WKXF8hVK4tPDIdQAXYZnAFFoOak1H-JDrBrVqBDSba0n5afAC2GXVEkldwCxMgwvoP0l8B2dxlc6rd6OtqJ7wl5OGizb_YXqOvA0ocATzXOpoMUKKOILN0JhhA4Nfj_lTbupaN7aJDNnfFcPSqV6OXXZuX10cwQGrQxWNFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e1926caa.mp4?token=dk8f2hG3eho1gem8cI-Qy6jsBrA3Pcd0tCLRfVyISHsxo4dqE0tJpjCTIAgmLp8gyi6OFELmWlH8UpVDf2lEM9SrdlF1_GwFblG2j-NY_MB9-hjwcvYJTOvKvSk_-kkuFFqWnd9iDWMs1AIc4u5PSayw7qa8jmTxn1cEZr6NZRaMBGUKZcz7kZjJi1fNS6lgbAFD2mDLmCxP2h7TL7dL4Dv_8JhNIGR3ZVblWRciL1TZtZOiMzchMdfIkb2aaEvyyjoz5SKtN3xKGx5VDPTKmwAvI1Iq9px_pnVLK4N12BKQ0YkAQLnpJfQVrSLRi3hz0b0YPy7ix95p6-W0nM1oBI2_6C5cg5sm-evgsy6Gunfd-x5qI-ShnmQdPF8THEhPtkUNjPFVxS3oljjq1Y8F1ZozQlnNr-zdOCLnYt3RViADbuRomUytF-Jus2mBq3TBvLXZ9Pw93HT-FQtmjqAzQa7C_FLgJeyjLf2d0krug5wS2iEDdypXmdaT_gCGP0gIHLE8WKXF8hVK4tPDIdQAXYZnAFFoOak1H-JDrBrVqBDSba0n5afAC2GXVEkldwCxMgwvoP0l8B2dxlc6rd6OtqJ7wl5OGizb_YXqOvA0ocATzXOpoMUKKOILN0JhhA4Nfj_lTbupaN7aJDNnfFcPSqV6OXXZuX10cwQGrQxWNFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور امارات، محمد بن زاید، به ترامپ:باعث افتخار من است، آقای رئیس‌جمهور، که اینجا با شما هستم. و می‌خواهم بگویم که ما بسیار سپاسگزاریم که شما اینجا هستید و به عنوان رئیس‌جمهور ایالات متحده.
🔴
تشکر ویژه‌ای برای حمایت شما در طول جنگ شش هفته‌ای. این برای ما بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128470" target="_blank">📅 16:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bd31af11.mp4?token=UdUKZd5_CeZJ5Y1dPskmpTOF8Jvgin3M5cKhQiEGiCgnghI2Gg0vcGxf_yt2Zp-v7TNHLQBsGMkylXlIOXIHsTWppqtg4apkxxPubVgVgsFc2Rl6zaYG-8HmjCB5w3TJhmMtKOBUiIHvcSmC5YOMbEGk8xFZ-Lio6oc74Z6n8ZgPnvioIFWhwvUUjDkPdpGBvybohBc2swm4hnAtl8V42pziJATTCOmdMvYzWi0I2Fsl5x_g9AFgDqtbFJxtJjP9LrVgkwauFfcKH-SLXDboFF1DS2Cz1Oc2Xi-UAH2xMRI05bB3mSK9ogAND5fxA5RpjTwr_LJX7un1Af8G7EZH6ZJgWLiPKqoCGyGcPC3c6i0GKCrUee51jwhByw7r7mCDi4UaRkZzEDK5J2N-4PP2s2VEFl0lK7nYuaXd3vAW_YVYhsotmhUaMnXCD5mDJkNvCzIKWuwaTqnlwt19r4r97tnpQoLEolHT-ntmovtIy-mHKrDlTsQqEX7r7u5cSfttjbLeEYEYamWsXALZe_2pHIWThgUiMd4xPjJB3tacm4QQa1Jx5e_TBeAVLONo0apDpcGhDWyoZAr6_6R4Ufv0pLNH4W3_nVXOJOTn9eQ0fdkcVH8mEqGZOk6nzER2KH-98svk4-RQazqP7xS2ETv3EO0nPNiMWPaozaOd5s4Mw7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bd31af11.mp4?token=UdUKZd5_CeZJ5Y1dPskmpTOF8Jvgin3M5cKhQiEGiCgnghI2Gg0vcGxf_yt2Zp-v7TNHLQBsGMkylXlIOXIHsTWppqtg4apkxxPubVgVgsFc2Rl6zaYG-8HmjCB5w3TJhmMtKOBUiIHvcSmC5YOMbEGk8xFZ-Lio6oc74Z6n8ZgPnvioIFWhwvUUjDkPdpGBvybohBc2swm4hnAtl8V42pziJATTCOmdMvYzWi0I2Fsl5x_g9AFgDqtbFJxtJjP9LrVgkwauFfcKH-SLXDboFF1DS2Cz1Oc2Xi-UAH2xMRI05bB3mSK9ogAND5fxA5RpjTwr_LJX7un1Af8G7EZH6ZJgWLiPKqoCGyGcPC3c6i0GKCrUee51jwhByw7r7mCDi4UaRkZzEDK5J2N-4PP2s2VEFl0lK7nYuaXd3vAW_YVYhsotmhUaMnXCD5mDJkNvCzIKWuwaTqnlwt19r4r97tnpQoLEolHT-ntmovtIy-mHKrDlTsQqEX7r7u5cSfttjbLeEYEYamWsXALZe_2pHIWThgUiMd4xPjJB3tacm4QQa1Jx5e_TBeAVLONo0apDpcGhDWyoZAr6_6R4Ufv0pLNH4W3_nVXOJOTn9eQ0fdkcVH8mEqGZOk6nzER2KH-98svk4-RQazqP7xS2ETv3EO0nPNiMWPaozaOd5s4Mw7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رئیس‌جمهور امارات MbZ:
حضرت ایشان یک جنگجو است. او در آنجا می‌جنگید و آنچه باید انجام شود را انجام می‌دهد. و به خاطر همین شناخته شده است. او مردی شجاع است
🔴
او کشوری عالی دارد. کشوری فوق‌العاده است. و آنها مدت‌هاست که با ایالات متحده همراه بوده‌اند. اما من می‌گویم از زمانی که من به کار آمدم، خیلی بیشتر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128469" target="_blank">📅 16:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اسرائیل هیوم: دونالد ترامپ داره گزینه برکناری مقاماتی که با توافق ایران مخالفن رو بررسی میکنه!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128468" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی ارتش: در جنگ، جلسه‌ای با حضور مسئولان عالی رتبه نظام در حال برگزاری بود که مشخص شد یک پهپاد دشمن بر فراز آن منطقه در حال پرواز است
🔴
از آن‌جا که پهپاد از نوع کم سرعت بود و جنگنده‌ها با سرعت بسیار بالاتری حرکت می‌کنند، پهپاد مورد اصابت قرار نمی‌گرفت
🔴
خلبانان ما با استفاده از برخورد فیزیکی، جنگنده را به پهپاد نزدیک کرده و با اصابت بال هواپیما به دم پهپاد، آن را منهدم کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128467" target="_blank">📅 15:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فون در لاین، عضو اتحادیه اروپا: من به ترامپ به خاطر توافق با ایران تبریک گفتم.
🔴
هر دو موافقیم که این توافق باید به معنای پایان قطعی برنامه هسته‌ای ایران باشد.
🔴
تنگه هرمز بازگشایی خواهد شد.
🔴
قیمت نفت در حال کاهش است.
و اینگونه است که دیپلماسی نتیجه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128466" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اکیپ: دونالد ترامپ دستور مستقیم ابطال ویزای برخی از اعضای ایران از جمله مهدی ترابی و مهدی طارمی رو صادر کرده و ویزای این بازیکنا ابطال شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128465" target="_blank">📅 15:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b287c6a06a.mp4?token=c_mUQpd0UhSLDU7Mjy6r95BWaK7WRdXSqg_9hVBUwAMyYjuQYhE5PxCvt-OeOvOX8w87AgBgs96aJ1pjR4P8bmI7l10Czy6LQ0XEqu9wqVNVXrkS-H5L3Vs7mpRnBCPXxN3Sjf6-uCIBtVXXbOFOMwIozD0MK9h9L_T56aMbe2xxkT7RK-XXeyF3UIS5CZLXczDyuExyMSoskI8DhNcXGXmIkTQO_gzt2e4OhQoBOPEefd3LGdyVgUVBZ-LEJPsIJ3mTn2_1-jIVXz37R7nNNf280niTJgEqc2W3W9jcDco-QFr82zfjsPxGO-o-Kcir9fbA_RxIqwzE6u7bOOo_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b287c6a06a.mp4?token=c_mUQpd0UhSLDU7Mjy6r95BWaK7WRdXSqg_9hVBUwAMyYjuQYhE5PxCvt-OeOvOX8w87AgBgs96aJ1pjR4P8bmI7l10Czy6LQ0XEqu9wqVNVXrkS-H5L3Vs7mpRnBCPXxN3Sjf6-uCIBtVXXbOFOMwIozD0MK9h9L_T56aMbe2xxkT7RK-XXeyF3UIS5CZLXczDyuExyMSoskI8DhNcXGXmIkTQO_gzt2e4OhQoBOPEefd3LGdyVgUVBZ-LEJPsIJ3mTn2_1-jIVXz37R7nNNf280niTJgEqc2W3W9jcDco-QFr82zfjsPxGO-o-Kcir9fbA_RxIqwzE6u7bOOo_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین حرفایی که عرزشیا به قالیباف میگن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128464" target="_blank">📅 15:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: مرحله بعدی مذاکرات ایران «آسان‌تر» از دور اول خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128463" target="_blank">📅 15:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXFCyXmNilwZm1GB_gUMzf9beuWcx6hr2_pkr8M_pK2gs5VZYexedpumHbQqQ_j00khsvYzQtmGue-1TpUN7UU0MYD08qJpPpOTyErYq5J84etIQU9xokyev5gtl0kUYx84PoJDut_Jk3MfXo89zddoep1144-4z3P1GCq5VOi8xDwVLI9j00EePrP7EMOmJHcwLzchsmd89ZwcNLEiuM6AxUO15i3rLkFCNw3Yof-RX6WlPCVtl-Q_c5bbfDaqKYJhpcfRb75VNS9Tvd9h3OCoZ0sodas9rGdDFHNPuFHWQ0eoatG8DslOKEAIr32fbiMp_sRIq7G7TuMf5EMHp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضعف فاحش شجاع خلیل زاده در بازی امروز صبح مقابل نیوزلند
🫶
بازیکنی که صرفا با خایه مالی به تیم ملی راه پیدا کرد نه مسائل فنی  @AloSport</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128462" target="_blank">📅 15:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: ما از توافقی که ترامپ با ایران منعقد کرد استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128461" target="_blank">📅 15:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قطر: تفاهم کنونی تهران و واشنگتن نخستین گام به‌سوی توافقی گسترده‌تر است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128460" target="_blank">📅 15:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293f42cae1.mp4?token=Kur9FGt3kNuUmp11WkHEb3ZLrgvtcvxVZlFCi6PPsc5PCspWk9p_PxNxSfc6V1caKFRjwWuqawP0fevL3Uy2rcs5j9ZtcMbv_Dmh8yta9K2nC3PJBR2qNH0gQQlwHCR5DPXi3xgrlMk-B2zbvxFLmmduj8pvOz9k73VPvgg52Nij2LJOz1k50_5bPLjokg3z1UMuZW594xBiTimXug63bmEEptv_GU88tJkE5Y-F0eBAZAaby9viAdEMVvRH94CF7uxZhep_pms3_RJSWqN68LxnLC_eYoegGF1RXQ9PCKxxmwGwDDkZw1jZQ0CURVAq9eohLdtlmxyuYZCcHlIhjUX-kI5ExJWLwHrJIDdEm0i_NZ-M6cmPSE0jNuq3CNItZiTQZkl5ltFhT0bGMdaLpsD7FVkNeQb-UjgAu-BL4BB91v8fhY9uE6Nj2YH86tOAoF1OkFBPnhD680CDYL_7xZ64Pfa3WN_-THC1_oGwRbtlYNgaJuc00cyU50ktbneBvO9KO-dSR6-aAK7jU35JDp2pg1sdC4NiA4aoehKiQQ_dkTfm3G4QLdw2ZCg7F1hn4NLA97E-5y0aHsVbvTh4wGaKl0HyBSU0t4omfxIPIQfY4v0LUfuBGO1RHK1vqF2A3vSE6ohcSOtQfENh7TEo9ubttXNO08xkNkrlsyP7kmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293f42cae1.mp4?token=Kur9FGt3kNuUmp11WkHEb3ZLrgvtcvxVZlFCi6PPsc5PCspWk9p_PxNxSfc6V1caKFRjwWuqawP0fevL3Uy2rcs5j9ZtcMbv_Dmh8yta9K2nC3PJBR2qNH0gQQlwHCR5DPXi3xgrlMk-B2zbvxFLmmduj8pvOz9k73VPvgg52Nij2LJOz1k50_5bPLjokg3z1UMuZW594xBiTimXug63bmEEptv_GU88tJkE5Y-F0eBAZAaby9viAdEMVvRH94CF7uxZhep_pms3_RJSWqN68LxnLC_eYoegGF1RXQ9PCKxxmwGwDDkZw1jZQ0CURVAq9eohLdtlmxyuYZCcHlIhjUX-kI5ExJWLwHrJIDdEm0i_NZ-M6cmPSE0jNuq3CNItZiTQZkl5ltFhT0bGMdaLpsD7FVkNeQb-UjgAu-BL4BB91v8fhY9uE6Nj2YH86tOAoF1OkFBPnhD680CDYL_7xZ64Pfa3WN_-THC1_oGwRbtlYNgaJuc00cyU50ktbneBvO9KO-dSR6-aAK7jU35JDp2pg1sdC4NiA4aoehKiQQ_dkTfm3G4QLdw2ZCg7F1hn4NLA97E-5y0aHsVbvTh4wGaKl0HyBSU0t4omfxIPIQfY4v0LUfuBGO1RHK1vqF2A3vSE6ohcSOtQfENh7TEo9ubttXNO08xkNkrlsyP7kmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضعف فاحش شجاع خلیل زاده در بازی امروز صبح مقابل نیوزلند
🫶
بازیکنی که صرفا با خایه مالی به تیم ملی راه پیدا کرد نه مسائل فنی
@AloSport</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128459" target="_blank">📅 15:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI5vd6DKpGIlqT96Itlqax2AIf-j5_JDMrEY0pxWBQ3tMaDkblel1Er-3-t__LuzFZMOg2A9QhUREPH5-mAJiXgOygRlBvaKZ6hv4fIzwbmVRZd-oCdxMNU3qcWq67-27RIWo1AdTuNcSmhqtRI-j3l1axOYm8Cq01R10dHFvzK1MtNCyUnVM7fPYaBrPYFmIGGNNabi9ml-Be-9MBzPbfQiULMmAViMrOcQewI0tIWXDqoBtMv1S5-ngTdFkk0Vqadfs18wfdmFBdi-L6Okw6NHb4-snrV8KO46xfwej_WxAEpD2rPysne5oQAJzPSOjGcYN8X7vCTBOTrj97Xllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpoIXg4Ts9UhK7e2xbf3E7j6rfk0Za7eTToyK-meeEmH70kUiAvIRCFrfl07Y02i5g_KnFFJvK2H5FYp1b0IEBC9yXo7YWeQOofLJ7ZMqoLhNeWUUSgwgDnJeF8SlXVS2c6ZK4xxESynCNigifBFoaOMvcIvTtLIDHUVj7BLd7W1wWoa56K3qkXH-joalN5chm-d-mjbL0QkrkPHAWULxaFyJue6HdA6VzypVq5N0Baf4XFMF8Wr3Fgn4dsRiyWNEfUz2xqL-GvR_-oK89UxSr2RRi6wItoSRqNWY22-hc5yUnESulUUo5NfzMzvbhufWzJDB4vxQlSB1voCHvBH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1-_iygcSAQKtU9aJRGzZdgdvRib6x63Fs2cqRS3UMDnJZfyqBs9tjADxkdiYDtnKi88Q9ThfcxCIV2ibl3RmWZGOdDhaDQX-0MBiD_JX4TOd_iDSAvgtH9tw7m3dhv219BiZunZAzcfrqbaaG1eUFTtxHvWthr9UikdUpbx6no8Fg_KaUc9iTM3-nesVoqM_gLHoQJzEBQFTRky27N_qHBDZLb54gSNotvYHz4yTr-6X6X4RpaxkOeMgKOL_2UkSF9KSJPoc-_MdxHTdLp6e7CdWT89HYqb74jeAQBTuI-wqJBKCevgOpjbixMgaQ1MvBTrOxUd2GHZ81-fEq1xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMtIZ9VXVM-lBhPXl__SJ7OYBamgpHwHVI7dakh54Xa6D_SAoSu5trLnbnEWWVuLud0TBh5YO-wh-oVNsKjw5i9dpFMYAH2AHzjSpKJeRgrOm8hcn1c5S-ewG2iSA-a8ouIu-789qp-vOgJYFZizyoCFyCqeTxzkVQ1MDd6EnEKj247ji9i8dHn_T5hEygGB4eyfrkA0PVTe2cL2s-j3mu6sp7ezr0EKdZQA4_93clKvwpGlg1O0hRanD_jfdSgheYkDe5l8ry6GIxx17UZIqIbtc113k7gDrz9JRJiKw_AxQDEJecqCCh6x8_uvTf8jZ9HO2tz-TXQs2ZdJ_CYnjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ و رئیس‌جمهور زلنسکی در اجلاس جی۷ به طور مختصر صحبت کردند.
🔴
آنها امروز بعداً در حاشیه اجلاس دیداری خواهند داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128455" target="_blank">📅 15:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اسرائیل هیوم: دونالد ترامپ داره گزینه برکناری مقاماتی که با توافق ایران مخالفن رو بررسی میکنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128454" target="_blank">📅 15:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قطر: تفاهم کنونی تهران و واشنگتن نخستین گام به‌سوی توافقی گسترده‌تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128453" target="_blank">📅 15:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فیدان : ترکیه همون‌طور که می‌دونید یه کشور مهم و قدرتمند تو منطقه‌ست ، برای همین هر موضعی که می‌گیره واقعاً می‌تونه اثرگذار باشه و فرق ایجاد کنه
🔴
سیاستی هم که رئیس‌جمهور ما با محوریت ثبات و اولویت دادن به صلح پیش گرفته، تو موضوع جنگ ایران تو منطقه هم خودش رو نشون داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128452" target="_blank">📅 15:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیدان : بعضیا به خاطر گذشته سکوت می‌کنن (اسرائیل)
🔴
بعضیا پشت پرده درگیر تجارت و توافق می‌شن یا حتی تو انتخابات با هم تعامل‌های پنهان دارن
🔴
نتیجه‌اش این می‌شه که این وضعیت ادامه پیدا می‌کنه و همه طرف‌ها در نهایت آسیب می‌بینن
🔴
برای همین هم تأکیدم اینه که کشورها باید جدی‌تر و هماهنگ‌تر عمل کنن، تا جلوی اقدام اسرائیل تو منطقه رو بگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128451" target="_blank">📅 15:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فیدان، وزیر امور خارجه ترکیه : اگه یه «درک و هماهنگی مشترک» بین کشورها شکل بگیره؛ و این به یک «اقدام دیپلماتیک جمعی» تبدیل بشه، اسرائیل عملاً دستش برای اقدام بسته می‌شه
🔴
به نظرم کشورها باید صریح و هماهنگ عمل کنن، اشتباهات رو هم سریع و مشترک پاسخ بدن
🔴
چون همین فشار و اجماع بین‌المللی می‌تونه جلوی اقدامات اسرائیل رو بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128450" target="_blank">📅 15:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128449">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بری و قالیباف در تماسی تلفنی: واشنگتن باید اسرائیل را به پایان دادن جنگش علیه لبنان ملزم کند.
🔴
اسرائیل باید مجبور شود تخریب روستاهای لبنانی را متوقف کند و از سرزمین‌های اشغالی عقب‌نشینی نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128449" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128448">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شورای هماهنگی بانک‌ها: سپرده‌ها و اطلاعات مالی مشتریان بانک‌های ملی، صادرات، تجارت و توسعه صادرات امن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128448" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d0fd899e.mp4?token=dCp0KW5trr-lJKOAcUKT-eYR0SYF0w_9nfKULIAwbU9Vf9xRGShBUiJ3Ha38HNXG24H92HTS4e3pri39KCQHDp-qZFijOCZeg8DU4sjpBoTG7X0pTp2PSLi1dAde2eCEPc4xsjrht9mNdeDg1Hm6ju9QzlcLF0m720oHjuB0Qf5ZAUwITN9ou9GxcgTbBPaSd0GV24fCoq9pEQfS5R8UkDaNdYcWWCml_ksKFAD1ekS7Uhcn4fDiDbn7CKxyiZdnQQeVjQ0xXmyg6aUpDa1ZQZXmF5in-iDyrKvTUrElHVujMT98YXK85TPgEWr5z2vc6_nM6Ddm9zWg_UHynI4W0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d0fd899e.mp4?token=dCp0KW5trr-lJKOAcUKT-eYR0SYF0w_9nfKULIAwbU9Vf9xRGShBUiJ3Ha38HNXG24H92HTS4e3pri39KCQHDp-qZFijOCZeg8DU4sjpBoTG7X0pTp2PSLi1dAde2eCEPc4xsjrht9mNdeDg1Hm6ju9QzlcLF0m720oHjuB0Qf5ZAUwITN9ou9GxcgTbBPaSd0GV24fCoq9pEQfS5R8UkDaNdYcWWCml_ksKFAD1ekS7Uhcn4fDiDbn7CKxyiZdnQQeVjQ0xXmyg6aUpDa1ZQZXmF5in-iDyrKvTUrElHVujMT98YXK85TPgEWr5z2vc6_nM6Ddm9zWg_UHynI4W0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صدا و سیما: عملیات رفع محاصره دریایی اجرایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128447" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">سایمون کوپر در کتاب «فوتبال علیه دشمن» اینجوری میگه فوتبال فقط یک بازی معمولی نیست. اگر یک تیم حمایت طرفداران و مردمِ خود را نداشته باشد، فرقی با یک مشت دلقک که بیهوده به دنبال یک توپ می‌دوند ندارند.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128446" target="_blank">📅 15:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBdyceVUbcxbIGuUWVUoTUQH7G1gPQvZD_prFzeaEg7HegE4CFH0ctb7AZE34A-KJ3BDQQU6IIjqNztB5ew7mX7Hxup_5hq_J0Og0SYBFQl_UaHsHwhJQi0UbINAtXsngkIvXe5b_JQ1bcpjhlaVmEJ9BI_ZOtNDG5dvYaK-TrYdrSACO4U3xjcyvA-QM2AmlIglrkdCCVdjshkaFRlljiI_sY3mZP6v8Q6K8bJ8TftEFZB5R4SSEbA-T9sjblOgCHXshhHc6kMPGUxbKPTYuDcQYbXcrUkJX9Kq3tGaETlaUeSsr9G7E_7rakS8ZaulKw-IGZkJeLCb-1-EK3SS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دراپ سایت:
ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128445" target="_blank">📅 15:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG6se2ZwtEYgJLN2GTTPCGu1nKQWNVp2Lfcby2lXkYdq-jlApIiLaJkta4vZRYipC09rLZQdCfEhMlINFfL9zKDp61HaPM22eD37zJBmfJdiuK4DZ83y7tc2FL5pEMvLTtCpUASjOqi4Fk7mbdZ4gSarIMgGzty_w8PFHuIXcM8z1cZK_u47PHBwLmhMhHDqdhWN2SlvlP59jWvkTdddxmoUiD14AXXem4ojh16FACTWds1NcbRkS9G_49QukWn70UXp1hwoSuJNfzAHREk6Y5pQuU8Kn5Y8KtMARiDqI3P0ZH2Bt6qugj1i6KGHHlIcFZkYZ9PQ9-9OKlaQlN8Jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش چشمگیر قیمت آیفون ۱۷ پرومکس در بازار ایران
🔴
یفون ۱۷ پرومکسِ بدون رجیستر که قیمت آن در بازار تا حدود ۲۵۰ میلیون تومان هم رسیده بود، حالا با کاهش بیش از ۳۰ میلیون تومانی به حدود ۲۱۶ میلیون تومان رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128444" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128443">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
عرزشی ها میدونم اعتراض دارید به نوکری کردن برای آمریکا.
🔴
47 سال به آمریکا شعار مرگ فرستاد سر آخر زانو زدید.
😅
ولی اغتشاش راهش نیست. بازیچه حکومتی ها شدین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128443" target="_blank">📅 15:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128442">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاریو: نتانیاهو تقریباً تنها مانده و مشاوران نزدیک خود را از دست داده
🔴
نهاد‌های امنیتی درباره تغییرات ناگهانی مواضع ترامپ، به نتانیاهو هشدار داده بودند، ولی او جدی نگرفته بود که نشان دهنده ضعف در ارزیابی ریسک‌های سیاسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128442" target="_blank">📅 15:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128441">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb659ad616.mp4?token=CqpivCB8LtgZnzesep61TeyRF_N0TFDj3elM19EeTunO-Fc1hDmelr8VPR4TbFFNyM05AH-LlX_xF65xhpzq4U4aGgfr6f-erfoQptjpR6gXYOBX2IdGkETJ9xakSsRygMxpro3i_tQr-I6-_LzvDNWFan3Boo4uxfeuGxz8dO7XNw82xyq46LgWA3fBW6SgUvSpk4TiwMgg767sx0WgnsUTqCP3YKNGqCJY9Ybmu4SH1aFwk34QxHt3Wr5TB8YsXh5J1tbjLMNNdiWmt87rigCDoIFjrB-_Sy-_HhXacZUIzMw66eLsxDgC-kFqVS16skdEKIfifucV04vLv9nIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb659ad616.mp4?token=CqpivCB8LtgZnzesep61TeyRF_N0TFDj3elM19EeTunO-Fc1hDmelr8VPR4TbFFNyM05AH-LlX_xF65xhpzq4U4aGgfr6f-erfoQptjpR6gXYOBX2IdGkETJ9xakSsRygMxpro3i_tQr-I6-_LzvDNWFan3Boo4uxfeuGxz8dO7XNw82xyq46LgWA3fBW6SgUvSpk4TiwMgg767sx0WgnsUTqCP3YKNGqCJY9Ybmu4SH1aFwk34QxHt3Wr5TB8YsXh5J1tbjLMNNdiWmt87rigCDoIFjrB-_Sy-_HhXacZUIzMw66eLsxDgC-kFqVS16skdEKIfifucV04vLv9nIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، فریدریش مرز، به رئیس‌جمهور ترامپ یک پیراهن سفارشی تیم ملی فوتبال آلمان با نام «TRUMP» با شماره ۴۷ هدیه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128441" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1153104f58.mp4?token=fvIWRpPJD6rp8Rkl3s31F3ZSzahvSZi8mQzvJQIuL_JldYxnAXS8L16_UjlH9-6o7gFDensP5n5_iowjXG7BJi1rkkOGstfFGIR_gE3iVJ9_yT4DpnePqXLH3-yaMUYULbAoB89iMchoAMOQKCgrmuUt6j9HaU_1hy2JRjCf0VHyZ3uMNdmgUMiO7tORcPPjib9ZkieWBWxK0J9KisqPKH6hEHmcERAW0bP5cKZsOPyFXphRBvKL8n_UFonOh1tRzunXsAGXsEQvbUor0VMvM0S41YwiEqfM-nB5hbaw5IDOhgz2udzY6SQaUAbpojErKUvL53i3d4v6A2S41DjIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1153104f58.mp4?token=fvIWRpPJD6rp8Rkl3s31F3ZSzahvSZi8mQzvJQIuL_JldYxnAXS8L16_UjlH9-6o7gFDensP5n5_iowjXG7BJi1rkkOGstfFGIR_gE3iVJ9_yT4DpnePqXLH3-yaMUYULbAoB89iMchoAMOQKCgrmuUt6j9HaU_1hy2JRjCf0VHyZ3uMNdmgUMiO7tORcPPjib9ZkieWBWxK0J9KisqPKH6hEHmcERAW0bP5cKZsOPyFXphRBvKL8n_UFonOh1tRzunXsAGXsEQvbUor0VMvM0S41YwiEqfM-nB5hbaw5IDOhgz2udzY6SQaUAbpojErKUvL53i3d4v6A2S41DjIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی منتشر شده از آسیب و نابودی تعدادی از  هواپیما های ترابری مستقر در فرودگاه شیراز در جنگ 39 روزه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128440" target="_blank">📅 14:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128439">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
خبرنگار الجزیره: محاصره دریایی آمریکا علیه ایران لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/128439" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128438">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOdFMas2KkmmmQbW5WoH83lFAfNF91de2iSl7Vn36jwz7Am55PfTtZkQxBnBsthA3-T2ajXp3n7APYJSa2Lc803LPttFIBBKLEJ9m2LGhbkrSDDbirL8rfvLsItQLqbljIXu0oqsiEtCbRukfyYTqTzEPh9b415_jKUfgGSaOKFd_DNlWYnm8r7W3DQdwuprOeAKKMYhuJMybI59oSpW5iT53tEjc7t6o4Xbiub6TpHZSUvIYng0LfxC7kZtaUPih-P2MsvYNiElK5qK18w36seWUUxXAnkzcG7H0LUzL6rtWn19o5MWVl1hZ5cpdNkiWK5FU_UgjxW7o8K5bIqT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128438" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: اوباما به اوکراین سلاح‌هایی به ارزش ۳۵۰ میلیارد دلار داد.
🔴
او داد، که دیوانه‌کننده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128437" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128436">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: این موضوع هیچ تأثیری بر ما ندارد جز اینکه ما سلاح می‌فروشیم.
🔴
ما هزاران مایل دورتر هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128436" target="_blank">📅 14:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گزارشگر: اگر رژیم ایران به کشتن مردم خودش ادامه دهد، آیا شما همچنان این معامله را پیش خواهید برد؟
🔴
ترامپ: ما با آنها در این باره صحبت کردیم. بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، بسیار بیشتر از الان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128435" target="_blank">📅 14:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ در مورد اوباما: اوباما اسرائیل را به خاطر ایران فروخت. او به ایران رفت.
🔴
هر کسی که می‌تواند به این شخص یا حزب - دموکرات‌ها، من آنها را می‌نامم - رأی دهد، چون آنها احمق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128434" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gt9cRqPfLghx10QfNZfdHYDHD3NcjVqyN_NhShBEgZQUrednnOhVKQl78dgVQ0QQBBeZ9V4Ku206jbf-oAdbtp_FH38238XV8RxrcE5BfxVC11Pyddb6mnYwCorIdO6sWfI4NjORtJYf9XplctGW0TGtqppKa-oVGYDs52Kh6dn2zemJS3agBdEmZZSsCXpUKJKz_211kxmuo2l7YqYCamQMeLucpDBo7n273YKs_NNluJTAQczUD1asnqZVEW-w9Rm1hreb85BDb-Zxoh5NDQNjYUNNMtEvv6fJ4XGwGDYFcCvM6P0W2hZHaDfXtubrQI1YaRVdBxL03AUuKJAPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OL-kMz0y6Fb147LkzGRxrHeqHx8mUDujqNeJ8KHb9-d9xrQ_vPYFR9R9kJoWxMo3ZcfIvUuf8paqNKeXidQ4_G6FseESxUKAtz4pIcWAUIMVi329A4s_ZIbopm6ZKVA4nZp_XMGmOq-mfHLH6UJXh1-DFisXVR_XXtnLj395PMFo_cpB9roMrirWCsZG8zxhR_mNNRdo4QkSOoUyOiUjSYsWu6PQOR4Q6Fp_h1rhmMtZajLcGQFf9O654l0YMk0Aua47698YO1ATbSMQNFW2ylIXFN31iWSf994IWbROYXcuY-HWTtZCxzhOK6UciYHsboLRS_65tBADY_VLIkhQZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برنامه جدید امتحانای نهایی اعلام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128432" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d53a579b.mp4?token=mjbPo5Vxx0BrqyM0vaAcW05yHDbdfevg8zluMuF6iN8A0Ih64Zi99A1WWCMuck5uVueJr-YfPhipLAncMy7WrYg7ffJ2Oh8aZgrrgdbIxaWVRuq-fercNbN3gj6WRK0CzxxeemxHqPC26Ur9icNhEIDMAxZpsZ-lXp9vwN_Bk7pseoNkJBh-pe64YkaFIah9BCq5wYg9vgAhcYoIj9uYkn6NKFDo2Vz4hveAbDlp2Gbd55_IgsKRh2Ti3Mt-9S3q3QNrN3-kLzkfqkzmc1qHevRwMnGiLT0emKBQryJ_FwTAFAbOhsGzuUvzMPyMRSRYLmoWHOcqKe3SeOEnGyv3RrBekMFJCyjqfdDG_P9I0sqfECAzAtmvRrn4Cz2_KthhgSAUvRgXcfmNwoe9MASHEFNU-XVx6hFU3lRfhjQfnnS3IrLajSAKcoS4tfOS-FWy4o7hSLZ5mPLNzdd640Yg3vqe-7hVpMn3k36bP8VzMRFREnyTLeNPhAlYhOiE7lrt_aV-AHuwh4gMrxbSbk1LPHisWw5-CpeEj9jN2LOhrYFexav7TqHK0r_VIoPkS4mhYTBl8INVsPKM94IVDLo6n1vKIIB4PclKdP2GtNn7MpbXXsv2P-8_ZDmNtrn6B7YbDsZaDgfkZw8RRS-ua_COl7zC9npKTLSpnSLZn8Rukkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d53a579b.mp4?token=mjbPo5Vxx0BrqyM0vaAcW05yHDbdfevg8zluMuF6iN8A0Ih64Zi99A1WWCMuck5uVueJr-YfPhipLAncMy7WrYg7ffJ2Oh8aZgrrgdbIxaWVRuq-fercNbN3gj6WRK0CzxxeemxHqPC26Ur9icNhEIDMAxZpsZ-lXp9vwN_Bk7pseoNkJBh-pe64YkaFIah9BCq5wYg9vgAhcYoIj9uYkn6NKFDo2Vz4hveAbDlp2Gbd55_IgsKRh2Ti3Mt-9S3q3QNrN3-kLzkfqkzmc1qHevRwMnGiLT0emKBQryJ_FwTAFAbOhsGzuUvzMPyMRSRYLmoWHOcqKe3SeOEnGyv3RrBekMFJCyjqfdDG_P9I0sqfECAzAtmvRrn4Cz2_KthhgSAUvRgXcfmNwoe9MASHEFNU-XVx6hFU3lRfhjQfnnS3IrLajSAKcoS4tfOS-FWy4o7hSLZ5mPLNzdd640Yg3vqe-7hVpMn3k36bP8VzMRFREnyTLeNPhAlYhOiE7lrt_aV-AHuwh4gMrxbSbk1LPHisWw5-CpeEj9jN2LOhrYFexav7TqHK0r_VIoPkS4mhYTBl8INVsPKM94IVDLo6n1vKIIB4PclKdP2GtNn7MpbXXsv2P-8_ZDmNtrn6B7YbDsZaDgfkZw8RRS-ua_COl7zC9npKTLSpnSLZn8Rukkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نتانیاهو به واشنگتن آمد و از اوباما التماس کرد که آن توافق با ایران را انجام ندهد
🔴
اوباما طرف ایران بود، نه اسرائیل و آن توافق را انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128431" target="_blank">📅 14:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ : رهران فعلی ایران آدم‌های کاملاً منطقی هستن
🔴
آدم‌های خوبی برای مذاکره‌ان؛ قوی و باهوشن
🔴
اونا افراطی و رادیکال نیستن و دنبال اینن که به کشورشون کمک کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128430" target="_blank">📅 14:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ پس از دیدار با زلنسکی: روسیه باید معامله‌ای انجام دهد. روسیه تعداد زیادی از مردم خود را از دست داده است؛ اوکراین نیز همینطور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128429" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: من از نتانیاهو ناامید نیستم. ما رابطه بسیار خوبی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128428" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128427">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / ترامپ : من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128427" target="_blank">📅 13:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
🔴
به اسرائیل گفتم که از حمله آنها به بیروت خوشم نیامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128426" target="_blank">📅 13:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: اگر من نبودم، اسرائیلی هم وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128425" target="_blank">📅 13:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: من به تغییر رژیم اعتقاد ندارم. سال‌هاست که تغییر رژیم‌ها را دیده‌ام و هیچ‌وقت نتیجه نمی‌دهند!
🔴
فکر می‌کنم توافق با ایران عادلانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128424" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ : اگر ما برنامه جامع اقدام مشترک (برجام) را که اوباما با ایران منعقد کرد، لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128423" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: ما می‌خواستیم برای دریافت اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128422" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128421">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e70655ce.mp4?token=aJv8_g9YA5Lw-JSWzMAnSdg5vYnCCbUHji6_lKZ-7EkM7Dfzbc7rLGNPIByb2tAtlwD-iNO6VSk3SCP_7laQ4EcgyxslmRBQfDUom04b8q4zjrlGZrdvSE7QqXcGxv6YMlpGwPaAultRRbS3lOJpMwBAo7CQNVr8XGwCOYpA3EUhbjYrKmgv0x12jklgCIL4rkKU7ht6iCQX18a0HPZOW7Veo3o7YhHl9eYAqECM5HjgSkHqmxKRjYQB5YC-FEpQQCPt2gHjrOG19x7TuYJkV9GPs5c3lIo5Z68Fgb6JpAil5v4p0RLG3ZLxaVjlitUczA9lH2v8LkpvXTsvyJjUvG_jNG8VSDVVq51-tEhQj4iRLCt4AV3ImKuZPhEC7T8QZwviIeD-5SXK3USGCGvnbdjjnYqk-Mzinl1UwvfFBAlYyvbygLp7MQiI5ibQyTrr2WNHAHMc13r1hlsjlTMmPREgGAkzbUqdi9cOfUz6BwaeLYIrn6mKBNmzTdT7i1T4fB76IkLB2Q7sfWS2BSU_37Nv_v0TziI91XOXOeDsajaoZSGqOE4_oRXA1B7OnRM1OZVGixSCkZpC1STv9q4fu0PgvPqJnj7vgwYG8rVUya1283D0ILipyl5G1K9y8gOjUas1DQ13AviXgWutx83YsRyA4U6NqZTGM6Yu4cvHp6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e70655ce.mp4?token=aJv8_g9YA5Lw-JSWzMAnSdg5vYnCCbUHji6_lKZ-7EkM7Dfzbc7rLGNPIByb2tAtlwD-iNO6VSk3SCP_7laQ4EcgyxslmRBQfDUom04b8q4zjrlGZrdvSE7QqXcGxv6YMlpGwPaAultRRbS3lOJpMwBAo7CQNVr8XGwCOYpA3EUhbjYrKmgv0x12jklgCIL4rkKU7ht6iCQX18a0HPZOW7Veo3o7YhHl9eYAqECM5HjgSkHqmxKRjYQB5YC-FEpQQCPt2gHjrOG19x7TuYJkV9GPs5c3lIo5Z68Fgb6JpAil5v4p0RLG3ZLxaVjlitUczA9lH2v8LkpvXTsvyJjUvG_jNG8VSDVVq51-tEhQj4iRLCt4AV3ImKuZPhEC7T8QZwviIeD-5SXK3USGCGvnbdjjnYqk-Mzinl1UwvfFBAlYyvbygLp7MQiI5ibQyTrr2WNHAHMc13r1hlsjlTMmPREgGAkzbUqdi9cOfUz6BwaeLYIrn6mKBNmzTdT7i1T4fB76IkLB2Q7sfWS2BSU_37Nv_v0TziI91XOXOeDsajaoZSGqOE4_oRXA1B7OnRM1OZVGixSCkZpC1STv9q4fu0PgvPqJnj7vgwYG8rVUya1283D0ILipyl5G1K9y8gOjUas1DQ13AviXgWutx83YsRyA4U6NqZTGM6Yu4cvHp6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به امیر قطر در مورد ایران:
شما جنگیدید و با شجاعت زیادی به ما کمک کردید.
🔴
شما همیشه دوست من خواهید بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128421" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128420">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: قطر و ایران مرز زمینی مشترک دارند و می‌توان پیاده از یکی به دیگری رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128420" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128419">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
🔴
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
🔴
ترامپ: ایران طبق توافق هسته‌ای به سلاح هسته‌ای دست نخواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128419" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128418">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ در مورد ایران
:
ضمناً ما هیچ پولی در ایران سرمایه‌گذاری نمی‌کنیم. دیروز شایعه‌ای پخش شد. مسخره بود.
🔴
ما حق داریم روزی وارد شویم و اگر بخواهم کاری انجام دهم یا کسی بخواهد کاری انجام دهد، انجام دهیم، اما ما هیچ پولی سرمایه‌گذاری نمی‌کنیم.
🔴
ما هیچ تعهدی برای سرمایه‌گذاری در ایران نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128418" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128417">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کرملین: اگر زلنسکی آماده است که به طور مسئولانه و جدی صحبت کند، همیشه می‌تواند به مسکو بیاید، جایی که از او استقبال خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128417" target="_blank">📅 13:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1QRU2veUAj9fpGlA0mLDsBpVt1EaaDPoH4mpMyp6F8fhCCE8uDEe3LXlxi-iY0ebcN9OLDts-ud4d8jRbTiJOl5ParhM7zUT--qUPedrChwwoz9UFbXo_EUt14j9B1HUyUcyby-XzxgiITT40I2XXJWr7oSxevyW-9ICqUrSRAxqh6LpKaNVv1j0Pk0UFls6anSzPDpi0usiOpAKMFto_6bvgjRemoI1K1pNpMKQMh8Lgu8KjPpytgIQFAD-YWUO6YI7xKaVDMTX8xxn0Kn9K5oILr1TACgYplo3hN-H192gvW-TNTkJV-hefEmbdiFqw1IvkMBz5klx4_V-svv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت آمریکا ۷۸ دلار
🔴
نفت برنت ۸۱ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128415" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۱۱۹ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۲۰۰ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128414" target="_blank">📅 12:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c187fdc80.mp4?token=nXLgwUop9c3vgsPLFTz8AjjeSdom0yrtn2oyeMZRobJpxeQc57GuHAqNv9JDwHR3tMomGdbORCQW1zBHu2Pgv9YE8ITbAkyJdbDdrwxkcWpEkfPujd3VGOI2z4qQRs1uMDQkeScY8-YsEQvqZ1zVLWXYfCKUtQrjp8dyljknxNuiFOHAQTFagWYX1JQeKII2AdA6v-jgX1f2dirBHZ_4xjN1jtL8j9lSzDayWs2aV0aFKsPBVn6BmSOdtQ3RG-zzNv-4nXjT-qHSdFpaxtCUJbqIoEu6cJoj_UVSKU99GN7MiOu-GcZ7Oz-eKkUnfOq-uuD1NRYTvSjAt_B0WYmIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c187fdc80.mp4?token=nXLgwUop9c3vgsPLFTz8AjjeSdom0yrtn2oyeMZRobJpxeQc57GuHAqNv9JDwHR3tMomGdbORCQW1zBHu2Pgv9YE8ITbAkyJdbDdrwxkcWpEkfPujd3VGOI2z4qQRs1uMDQkeScY8-YsEQvqZ1zVLWXYfCKUtQrjp8dyljknxNuiFOHAQTFagWYX1JQeKII2AdA6v-jgX1f2dirBHZ_4xjN1jtL8j9lSzDayWs2aV0aFKsPBVn6BmSOdtQ3RG-zzNv-4nXjT-qHSdFpaxtCUJbqIoEu6cJoj_UVSKU99GN7MiOu-GcZ7Oz-eKkUnfOq-uuD1NRYTvSjAt_B0WYmIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ ارتش اسرائیل به تپه‌های علی‌الطاهر تو لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128413" target="_blank">📅 12:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان‌: در سراسر صنعت کشتیرانی، اعتماد چندانی درباره بازگشایی تنگه هرمز وجود ندارد
🔴
مواردی مانند [احتمال] حملات موشکی و پهپادها همچنان مانع از تردد کشتی‌ها می‌شوند
🔴
حرکت قابل توجهی از ۲۲۰ تانکر و نزدیک به ۵۰۰ شناور که در خلیج فارس لنگر انداخته‌اند، صورت نگرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128412" target="_blank">📅 12:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e305acd2d.mp4?token=ay20zjvZc_7pOYTWpiQ5ZlLyRgLLY1W3zAOrp1kdS-ZpaztS7NUHULtmNRTKnIG7scPeDaqOtNOuT7lzQJzOI9W6wkD4cYwNpYnp7mcuEZjlhyWnI6pggWMTKnYhumI4dWRXPxlSJciBjA8BcLgAcVCyrqmtjnVPh5mmxivqXnpiF79kcEsqcX3BWJ_3nxhq7NTQKePfoVUeTATvoL8nh2j3FGXzhPP-0Kyz0_LE2ogr6c3jSX2H7pPl5Z5b-IFPg5_WJEFQ20vgN-xC8Q5VzfOobK_q7Mrx0DhIoFKdHyYSuYv8zvtTD9iJai1mEpRfx8gzjd1l-pY_JmMXB4TzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e305acd2d.mp4?token=ay20zjvZc_7pOYTWpiQ5ZlLyRgLLY1W3zAOrp1kdS-ZpaztS7NUHULtmNRTKnIG7scPeDaqOtNOuT7lzQJzOI9W6wkD4cYwNpYnp7mcuEZjlhyWnI6pggWMTKnYhumI4dWRXPxlSJciBjA8BcLgAcVCyrqmtjnVPh5mmxivqXnpiF79kcEsqcX3BWJ_3nxhq7NTQKePfoVUeTATvoL8nh2j3FGXzhPP-0Kyz0_LE2ogr6c3jSX2H7pPl5Z5b-IFPg5_WJEFQ20vgN-xC8Q5VzfOobK_q7Mrx0DhIoFKdHyYSuYv8zvtTD9iJai1mEpRfx8gzjd1l-pY_JmMXB4TzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیدیی از یک درگیری دیگر بین موافقان و مخالفان جمهوری اسلامی در ورزشگاه
🔴
پ.ن: ژاپنی‌ها بعد بازی آشغال جمع میکنن و کل دنیا میگن دمتون گرم. ایرانیا بعد بازی دعوا میکنن و همه میخندن بهمون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128411" target="_blank">📅 12:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt4SncGUqoPuTY5vAgmZn_9gPJ6iKWUlVXWJHXB7jX7R52rHQWVLG5yZT_wROovxKcChsjGuVOwEvOQ8Z31n8jIG6tXj-meW0CmUKXmZbXUm5bmR0KM9kiv4aO1zt8h0iH6U3bmURShFqLIWNFB6TTzh774_kH7JttNqQXUHl-YY8a_8Jp4EcWrG6piEaeAL5IhDgl0W4L9KEEOA__VUBG7FzG86LIVe4IY2KD11egZxQwZxmQ69PcMjwa-cbs2oS2d6feq-Bjn_xXWr4X7q6fMLwLcmwD2cF5mAJy-dv3dVr9O0QBlsAJq3-8-HpL_102Ftext4GLJuNVJrU9CDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جمعه قالیباف و ونس امضا خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128410" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
حزب‌الله: ایران الان یکی از ابرقدرت های دنیاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128409" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تخت روانچی: در سوییس پس از اینکه مسئله امضا ( تفاهمنامه پاکستان) انجام شد، مذاکرات شروع خواهد.
🔴
درباره جزئیاتی نظیر اینکه چه مدت در سوییس باشیم و چه مباحثی مطرح شوند، صحبتی نشده اما این مورد تایید دو طرف است که بعد از امضا، بحث‌ها (درباره توافق نهایی) شروع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128408" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e565b291e7.mp4?token=ne18efqZbLRX9FnfVP6wkUopVXt8aZYOTieO8NSyogi6cQbRWheM1CWrP7g7PQ73iyptl583DT_7RCLbji6ayg5Y3fQ_Qv9WpOdUtG6ZVvH9oIN5qCqVm5LKDunZ4QClyKRFsQh70a7LMSBSBS7SWnx68vRowt7zKS9-QewmXzjlKzC_C6c4pgQdjq1oJhVnteeU8QLNZUVrWt58HzueBXer8ayb481NaHiq-2zTVfX6sdJH71BWZYngih_78RZJHEn0P6OGonliDPgtocgJYDxbaWZrzEGAXCiDyQNS8D4ije77gaz54FISqPWpqm8n5ZyQ84gjs2MmYq8SLfVfQy0JtZcQAWlARPi2auQ2YtOpnk2UivfZGyTacId1ba-uwMwUe8tLtd688AbzoyL6SgAOsCB00HYX5xJ0loRVAfslDqO7b6pzPparKHV6FBfX1S5OO9ZObsL9KJf0cjSMPA5G8f8CNElSyokHZuXap4YUZx2gKs9JzWMGL-KgzbzNtIvIqOgfL-BGscN4H4QGt8uJhlQRivdMOZGze_JOD4uxTadtiiUc8ZvBUKpdOK6E0UTOqRYnLaACj4qGJDW_MB_MAdG8Xx5IXbdwTVP3f538R3JgTtDHbMe8JR_QC857nT9LnnlbXA2Tyur9ax1Drro5i9rf--5X8Pbe4koF9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e565b291e7.mp4?token=ne18efqZbLRX9FnfVP6wkUopVXt8aZYOTieO8NSyogi6cQbRWheM1CWrP7g7PQ73iyptl583DT_7RCLbji6ayg5Y3fQ_Qv9WpOdUtG6ZVvH9oIN5qCqVm5LKDunZ4QClyKRFsQh70a7LMSBSBS7SWnx68vRowt7zKS9-QewmXzjlKzC_C6c4pgQdjq1oJhVnteeU8QLNZUVrWt58HzueBXer8ayb481NaHiq-2zTVfX6sdJH71BWZYngih_78RZJHEn0P6OGonliDPgtocgJYDxbaWZrzEGAXCiDyQNS8D4ije77gaz54FISqPWpqm8n5ZyQ84gjs2MmYq8SLfVfQy0JtZcQAWlARPi2auQ2YtOpnk2UivfZGyTacId1ba-uwMwUe8tLtd688AbzoyL6SgAOsCB00HYX5xJ0loRVAfslDqO7b6pzPparKHV6FBfX1S5OO9ZObsL9KJf0cjSMPA5G8f8CNElSyokHZuXap4YUZx2gKs9JzWMGL-KgzbzNtIvIqOgfL-BGscN4H4QGt8uJhlQRivdMOZGze_JOD4uxTadtiiUc8ZvBUKpdOK6E0UTOqRYnLaACj4qGJDW_MB_MAdG8Xx5IXbdwTVP3f538R3JgTtDHbMe8JR_QC857nT9LnnlbXA2Tyur9ax1Drro5i9rf--5X8Pbe4koF9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، ترامپ و مکرون برای نشست گروه هفت رسیدن پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128407" target="_blank">📅 12:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تخت‌روانچی: قالیباف و ونس در روز امضا حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128406" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
در دیداری میان نخست‌وزیر عراق و فرستاده ویژه رئیس‌جمهور آمریکا، دو طرف بر اجرای طرح خلع سلاح گروه‌های مسلح خارج از چارچوب دولت و تقویت همکاری‌های اقتصادی و انرژی میان بغداد و واشنگتن تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128405" target="_blank">📅 11:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMxW2hJkFC-qviKJHpqDLEWawZbNKAE8VbjFAQpUcKi1kiJdan24LsD11dXsa2DjK2p8fNGYFUd6a7h4uLZyDhUleGPvWx_Blrow6fbkIua0hX7ZHnpxAfzA1KXVStZ4wqvIbo8Gb4k1S9HVNrmVJdBYgAr1dg08HiM2idS1LRun3DGf5en1NewAqI92rLjWdqVAH1QEa22s04xLxR3PSX1imdP0XakA5ju9KxoA-WAzAGgkysrp_UUrmCrbWmRvGZE0N75_tAPSEOnpU1UVXcA70urdy4_ohI8FDYraz0kuxdUf_bfD3ovcjCAWWT2elCiDHzUu1GuC7vHUgnoU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPUKDJyPLnMEadnG5UFDUJT5v4FTRSPRYW0DJVxh7z752Y5nP5xqOzCTuca7-7eua0_ttPZze5rtrzKl5X0-6n7-9O0F-n4gPnN979ZVqEd0-2fZiciSizVONczO_ROGXxbCRjBFcYUKeGyOFMjAdZc79vsYcJLdu30-ShWUI5CwcZxeycoM6aAAkKAB0idFgYTi-C5QP-KII_2RlW5NTsgNxrpv6ccJYNrBRpp7ERVZaB204-DSNq8_-kOMcv1LVYfgTm0TTaLyGN44WWCtfM8-68tFfAzTbU-cm3IdK1LXLs4-9CCW6zgwbnq14SarsCcAAW0buWDisV8cn-wJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyOkdb_z6-ePN8IMNtrgAXcQVxmm78K8rY_ChN7OVkWQ6j0q9kew4RaTSKzHK0IpJ2rLwvjd3_Y4N2HQb10W8_iaPi-aA2umwoCElGaOL5ogwoO9fasijefhG4n9gNlbal0UyhWgmACCIKHvYwn9WAziIvzGM0YMP_lXZh6qQbA-l6UOteveZI8s39BHEvqtR49L_1meP5SZqaCRpFaSed6WH7pDqxMoq8C8GkQl7TiQzY0brTO7uG67o_RAwpec4T55SZv39zWtZSqw5QF8zVy8jaRExl3CKpTKuqHjdc74klnHlwzE2MRyqFpoIU1Junq7alXrSgCgksuNjdNUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6necl5uwbnhOAXfjomCfLxXvOJkBbkiUoNbXS47jGwRmIVAX_DGZOok2Jb-VyQHyUSEi43zCSm_LZ-b0ZIOH6wJmszLlNO2Y_DP6mgYj72DKRcvlsmhZHvUjwQb9ZFHbWGIJvXM_jdhdTMKEomCljJ6o6z4_4Zud3fcr14SxyFqUabQ6s6RLG-ms2AUS5zTKhPMEd3WrocW96GeA5bMpaH4lSgCgUL5yZS5vPuQLdI8Pg4VD8LCznR2jtF4SzN1YlQaIQIRjtILdsJOaVzp-EN3I3SSPwPY2bhsnP_3o8k8KYEh_EW477DnlabNqFvIAPMi63JGuZuUqGXeVuvtvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صبح زود امروز، پهپادهای اوکراینی به پالایشگاه مسکو در کاپوتنیا، روسیه حمله کردند و باعث آتش‌سوزی عظیمی در این تأسیسات شدند.
🔴
در چند ساعت گذشته حداقل ۶۰ پهپاد در منطقه مسکو رهگیری شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128401" target="_blank">📅 11:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7kw9aXgMkAcclhybj_U_5RMc53Zigygo0JVsq3tfwm7ki6a6Ot1b0xRIpOhHmA9GU_EWh--qc66Kin_VWZYhGpzQswaj5UbIfz7VHG4-1JSr2_M7X8qWCHA2HFwL_XD4ztyzDQYaSjwHI3VkSZ91n92B-GBEKd2wwGApWZX1S-EfR9s9HKh__8oKN8UHr5T-U-mqZaiP6OoUMzN2FsJeSuTd9KrWMAmU1-lP5-203JsxkpWXzBKzTQ3M05vr_j9wadg_mZIDzsWgHZ2M6l3Ywd5fYme7uSE8-0zJ5QBpFJN3OxBqJmvYQDk1YF66sPhIyvIACRe-LdDy7dmOrBNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا برای تخلیه بخشی از هواپیماهای سوخت‌رسان مستقر در فرودگاه بن گوریون آماده می‌شود. احتمالا حدود ۲۰٪ از هواپیماهای مستقر در اسرائیل منتقل خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128400" target="_blank">📅 11:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
عراقچی: دو طرف این تفاهم‌نامه، یک طرف آمریکا و اسرائیل و طرف دیگر ایران و حزب‌الله هستند و خاتمه جنگ در لبنان، بخش جدایی‌ناپذیر از خاتمه کامل جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128399" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76adb99a74.mp4?token=ZaqdkiFbiYCw0iBDTni2f4IOnsBGFSUfXb-jyAjGQdlUM9HPNuBnO-OwHMz9ho7l5nmuK4yhbMRjn3-MTxdLAv1y6YG2lYBASn_wM_8jR_7smmcKiH2-37Z9sKpnKxO-_q3M0IjZI6zqhVU_9g0kTu9NwheAEWJhiD8gwQNru9mPM2YAgEMfA6kTwftqBk0NkcXBVTdpGWQy6HPIxY6AlVuooF4UvMajgdaeXtRlg-ef8wG0-8CqXtyEnAG31C6MYDJbSyNEyQh6MHtyDdB649szYUVyXLhIFRC_6gnFP1CSDvUPgR_UPbpK5L-JhtVQxeMwkalaPwpCZEVx7ia5plfJi6y28rcJGlEujM52WYfj5e_QZrCzXz7eKrQ_XrcaSw0KiUAWnyyBM1qrLQ2MtnUIkNbOuALUo_KokgSAJGTE9RzfiXRycp14IIlxT9eIu9kap3zEN_MMjkyCjyN66AJKXB6223IuCm4ZDVLEVzM0zu0opftC9Jr_ZfTMi9W45o75BzJ8hOYVCWkmlVstLx0mrgwHiSYhsFmkENN2CE4MwfKKJFr2lfpiBl0QEQS4SiEP6B8EKFpcKd3yv7eI8fVv15Xw3AQVfa0GOugM07Ii4SMP3Nxr5CmsZ3vd8h8uMI9ukSzO0wXXKMtunYbMYge9xTn2xXlwz7t7_pH4MFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76adb99a74.mp4?token=ZaqdkiFbiYCw0iBDTni2f4IOnsBGFSUfXb-jyAjGQdlUM9HPNuBnO-OwHMz9ho7l5nmuK4yhbMRjn3-MTxdLAv1y6YG2lYBASn_wM_8jR_7smmcKiH2-37Z9sKpnKxO-_q3M0IjZI6zqhVU_9g0kTu9NwheAEWJhiD8gwQNru9mPM2YAgEMfA6kTwftqBk0NkcXBVTdpGWQy6HPIxY6AlVuooF4UvMajgdaeXtRlg-ef8wG0-8CqXtyEnAG31C6MYDJbSyNEyQh6MHtyDdB649szYUVyXLhIFRC_6gnFP1CSDvUPgR_UPbpK5L-JhtVQxeMwkalaPwpCZEVx7ia5plfJi6y28rcJGlEujM52WYfj5e_QZrCzXz7eKrQ_XrcaSw0KiUAWnyyBM1qrLQ2MtnUIkNbOuALUo_KokgSAJGTE9RzfiXRycp14IIlxT9eIu9kap3zEN_MMjkyCjyN66AJKXB6223IuCm4ZDVLEVzM0zu0opftC9Jr_ZfTMi9W45o75BzJ8hOYVCWkmlVstLx0mrgwHiSYhsFmkENN2CE4MwfKKJFr2lfpiBl0QEQS4SiEP6B8EKFpcKd3yv7eI8fVv15Xw3AQVfa0GOugM07Ii4SMP3Nxr5CmsZ3vd8h8uMI9ukSzO0wXXKMtunYbMYge9xTn2xXlwz7t7_pH4MFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری موافقان و مخالفان ج.ا در ورزشگاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128398" target="_blank">📅 11:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/128397" target="_blank">📅 11:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d16e6d68.mp4?token=usSHYOzkfJz_0K7ZLG6qJknetiOTLGVXJ6ugXYljMpyjv9QlYVuwiW9iRICGMVWtkl1HKoFyTiglgin3TzsB2uLJ4DvRCQBVevbLWTIT0wvXYTygaVSnu2c75xz-SNheHMuDp_Y8p9YOibmMzOzqQnYdVzY5oaVfe3JqhzENhiRrGjD-xGFtlYUknYUzxDA82cWKWFK4UwAKmaYbYDHJQq9yrCQNwjBhqwS07a34lcqO34mPiu9IYT3-lJTrE1iPxUqu2-qxD07iZtDi8mFZbC1WuKk_a7RARc2xA4OAlOTHSD_EQFFXwDtxO7yQHy9Y8NTOQ3XiRve3efAuFJvVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d16e6d68.mp4?token=usSHYOzkfJz_0K7ZLG6qJknetiOTLGVXJ6ugXYljMpyjv9QlYVuwiW9iRICGMVWtkl1HKoFyTiglgin3TzsB2uLJ4DvRCQBVevbLWTIT0wvXYTygaVSnu2c75xz-SNheHMuDp_Y8p9YOibmMzOzqQnYdVzY5oaVfe3JqhzENhiRrGjD-xGFtlYUknYUzxDA82cWKWFK4UwAKmaYbYDHJQq9yrCQNwjBhqwS07a34lcqO34mPiu9IYT3-lJTrE1iPxUqu2-qxD07iZtDi8mFZbC1WuKk_a7RARc2xA4OAlOTHSD_EQFFXwDtxO7yQHy9Y8NTOQ3XiRve3efAuFJvVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ترافیک گیر کردی
اون زن چادری پرچم به دست:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128396" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عراقچی: روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود.
🔴
بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔴
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام خاتمه جنگ است و بنا به تصمیمی که گرفتیم از صبح روز دوشنبه به وقت تهران که این توافق نهایی شد، خاتمه جنگ هم اعلام شد. ولی شروع رسمی تفاهمنامه از روز جمعه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128395" target="_blank">📅 10:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اختلال ادامه‌دار در بانک ملی و صادرات
با وجود گذشت چند روز از شروع اختلال در خدمات بانک ملی و صادرات، سرویس‌های مختلف همچنان با اختلال همراه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128394" target="_blank">📅 10:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">از بین ۴۸ تیمی که در جام جهانی حضور دارند، رتبه‌ نیوزیلند در رنکینگ فیفا از همه پایینتر است؛ حتی از کیپ ورد، هائیتی و کوراسائو.
🇨🇻
کیپ ورد - ۶۷
🇨🇼
کوراسائو - ۸۲
🇭🇹
هائیتی - ۸۳
🇳🇿
نیوزیلند - ۸۵
@AloSport</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128393" target="_blank">📅 10:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128392">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128392" target="_blank">📅 10:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128391">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd2ad4863.mp4?token=Npg76kkg-DFAzZ8GU8Yk9zE1huPwmvFU_OkR9UdEOyxPfl4jp1XOjvQq4q6bB0AYuQHgNojg6udfJxhzMEuirkWdAubeZ07R18R5G14MFV80kr2Wr0dJA4V19aeF4gd6bRgBajqug5QS-2dEN1WtNfMVgqLc03UnpbBGemSowlH9PdtP2wXA7md3gew2SY_NvXfe4E79BFsCGU0_C_ifvfIdFOuO1A8tMTKAZF5dOK1XqVX9lWZV2Ldz2AbcYYFd18b0j_ImbvEU95rg0n7bLFFpq9AOa8QU5erhcMK04nwfPc93IoCX7avHb5AekXcu9AMf59qvZAqJEm1aGIXW_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd2ad4863.mp4?token=Npg76kkg-DFAzZ8GU8Yk9zE1huPwmvFU_OkR9UdEOyxPfl4jp1XOjvQq4q6bB0AYuQHgNojg6udfJxhzMEuirkWdAubeZ07R18R5G14MFV80kr2Wr0dJA4V19aeF4gd6bRgBajqug5QS-2dEN1WtNfMVgqLc03UnpbBGemSowlH9PdtP2wXA7md3gew2SY_NvXfe4E79BFsCGU0_C_ifvfIdFOuO1A8tMTKAZF5dOK1XqVX9lWZV2Ldz2AbcYYFd18b0j_ImbvEU95rg0n7bLFFpq9AOa8QU5erhcMK04nwfPc93IoCX7avHb5AekXcu9AMf59qvZAqJEm1aGIXW_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ایرانی ها خارج از کشور(تورنتو) در لحظه گل اول ایران
🔴
وی سپس در توئیتر می نویسد: دیگه دلمون با این تیم نیست، تیم ج.ا و ...
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128391" target="_blank">📅 10:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128390">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ویزای مهدی ترابی بعد از یکبار ورود به خاک آمریکا منقضی شد
🔴
فدراسیون فوتبال برای اخذ مجدد ویزای ترابی اقدام کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128390" target="_blank">📅 10:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128389">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی دولت طالبان: توافق ایران و آمریکا باعث چشم انداز و پیشرفت خوبی تو خاورمیانه میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128389" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128388">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1f670914.mp4?token=X6det2_sSzhbizGFJPVTGMkvs5yRSxpb7TUlQCIsT-BPMb2zXZjKY_EbMd4Gd2MRvYT-SI7TBSjzqDtiJq1CtajQpG9BaC5JBelSeQ6edy52wiINs1-kbM6GzBUhOBkr3JLtOk9igfUuM0grWru13zJskKw2bvRynjoPOKKEymhNpYx2WR8d51XYwkUTQs9V16XYfDkgmhmhBG0AsfhpRfRU0NVp-4uwCxB8Da36JA4R64eD6cbC2AWXdipaPb0TKHiR_dy8YotpRNGDT3fNnU1J1byT6oSQtmu_LAZnRc-spJEbvs2UQBHUiaPbBOflASSZKMLg6KlbWT-ar5B5njslYgx2myPYxcfbkxzIi3Imm95rSyjHR-UBBz1xroB4rykgNG1N_Iwp3g0CsKy42vUlAKHDt56PrrgrQMXFMT928GNGTaZGF0ahQ9bZ07XsqbYbhQIjw-6O7ihcguOhvMB6wef4N_OOTCnGXcN_iQLf1rPWi5JIMeByFq57I1V8DPve4yNFC6GmPxs1Ke1VQtWTGrBZPmb0YDNiI1n5ix-2m6VRq6RVGdYmzrjQqnz1l6v7LgchdpWb42NhCV1VsCqvJs310rPk6ayFRvhwOBOIuhw2xcyR3rTaaI1MEP1GsU6fjd87nKXN6hR-rzEec8sBHe4-QgvgPWcq80fH5Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1f670914.mp4?token=X6det2_sSzhbizGFJPVTGMkvs5yRSxpb7TUlQCIsT-BPMb2zXZjKY_EbMd4Gd2MRvYT-SI7TBSjzqDtiJq1CtajQpG9BaC5JBelSeQ6edy52wiINs1-kbM6GzBUhOBkr3JLtOk9igfUuM0grWru13zJskKw2bvRynjoPOKKEymhNpYx2WR8d51XYwkUTQs9V16XYfDkgmhmhBG0AsfhpRfRU0NVp-4uwCxB8Da36JA4R64eD6cbC2AWXdipaPb0TKHiR_dy8YotpRNGDT3fNnU1J1byT6oSQtmu_LAZnRc-spJEbvs2UQBHUiaPbBOflASSZKMLg6KlbWT-ar5B5njslYgx2myPYxcfbkxzIi3Imm95rSyjHR-UBBz1xroB4rykgNG1N_Iwp3g0CsKy42vUlAKHDt56PrrgrQMXFMT928GNGTaZGF0ahQ9bZ07XsqbYbhQIjw-6O7ihcguOhvMB6wef4N_OOTCnGXcN_iQLf1rPWi5JIMeByFq57I1V8DPve4yNFC6GmPxs1Ke1VQtWTGrBZPmb0YDNiI1n5ix-2m6VRq6RVGdYmzrjQqnz1l6v7LgchdpWb42NhCV1VsCqvJs310rPk6ayFRvhwOBOIuhw2xcyR3rTaaI1MEP1GsU6fjd87nKXN6hR-rzEec8sBHe4-QgvgPWcq80fH5Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میثاقی: پرچم شیر و خورشید، آشغاله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128388" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128387">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بیرانوند قبل بازی:
دروازه رو مثل تنگه هرمز میبندم
🔴
دوتا کشتی رد شد و یکیش هم زاویه بسته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128387" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4htw5N3TQHx5QwuZJb_wBYK_7XeEtSePa480A-QhZ2VIpvId23Z7vQMnwBi49fWwgvym3sV9OPJqKvBcaZcITdImZv5ehdv7Ac4NzlmYwdlrpwQ25JiWaK_B7mbcvpUFySsQsLyhHTlvmtvUUcmUi132ow-WMCj6XU_GbM4Mr6lbKobLeAfasdzzAJJ8xvGmobnpa6mw3EOk7ZW0LADcK-i-eFgWwmJYtOrG2nSuokunxp9G1TOKComwqGogxC4oUAToudEdch9rUFIaWhRPW4QaCKIYCqkW8vRR01IWsKG4y1Z8HF_u_YpFxNGG4hzmouFIfbnVsRJE6nZu08iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de38edfb2a.mp4?token=uknBgHt2I_OOYw9pQPa0uPmHEQiAL7i_kzOnUgkxqjB2wgqg4pUsNP8GlfnZRaWvYothJUr4wvlBY_TeyH5Qd6pijkV7STkXtsjCyGWY5mqDNb_bt1bubkuQc9yh-4ezOnmyI9KhOcZ2SDkHIppJZ_3Uzc_vEcG7QCsoTpfejO9P9zsJlzclAD78KwhOzRIPV_0sHthxOOiP5sQ6LxuBL2MIvxuWSIyrgldd8tuzCq19JgqOOYaSQiXiIMs9_jOQK9xHqtevHEeSTu_trhPqXqqjH9-5V6tYg5PTZFQwKYWxMJtwU4Hk-qYrhIL8I5K1caBs6YUvhLu0jKoV8SmwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de38edfb2a.mp4?token=uknBgHt2I_OOYw9pQPa0uPmHEQiAL7i_kzOnUgkxqjB2wgqg4pUsNP8GlfnZRaWvYothJUr4wvlBY_TeyH5Qd6pijkV7STkXtsjCyGWY5mqDNb_bt1bubkuQc9yh-4ezOnmyI9KhOcZ2SDkHIppJZ_3Uzc_vEcG7QCsoTpfejO9P9zsJlzclAD78KwhOzRIPV_0sHthxOOiP5sQ6LxuBL2MIvxuWSIyrgldd8tuzCq19JgqOOYaSQiXiIMs9_jOQK9xHqtevHEeSTu_trhPqXqqjH9-5V6tYg5PTZFQwKYWxMJtwU4Hk-qYrhIL8I5K1caBs6YUvhLu0jKoV8SmwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شادی گل بحث برانگیز «محمد محبی» که با اسلحه شلیک کرد سمت تماشاگرا.
خیلیا معتقدن به سمت کسایی که پرچم شیرو خورشید داشتن و عکس جانباختگان اعتراضات دی ماه رو داشتن شلیک کرده.
برخی هم معتقدن تو خاک آمریکا به آمریکایی ها تیراندازی کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128385" target="_blank">📅 10:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng4oz5sPa9VeTWQlx-oFbLPAn8TpZ_O115liQp6dG8-prY9JT_MUqCEK1857H8tUQJNK-MVNf8WnVNJDW-Rm0EcLTHh0xgAArwEW6Ql69863eeQRDqWcHNzboHgmwWNy5asDWkifquu2_26_Gor0c-Z1ETVSfGXGDi5v2IPO0TRHgtX0W2J1GKFz35aMMGbUlpr8PXYwwk6-0pYjXYS_OSheUPJK7g5-hP216rsEsXBd4F_cQGBeptYS97tViQOAsKz5tCg_QFa-pM2l-R8WkPtAKrX402YjUaxrlxB9tx-FIR7qfKsvDVimDYJAzH2Snil2K3dbr8ncw8QajPIeVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحقیر پشت تحقیر
‼️
🔴
تیم ملی ج.ا بعد بازی بدون ریکاوری درحال خروج از آمریکا است اما طارمی و الهویی درحال بازجویی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128384" target="_blank">📅 10:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60c66f257.mp4?token=IvDCVWk7C6yAS6mDN4VUl8OaJ553gul6X7NDHyehPomQQewshQnyFBIKN-NbLjFbgMHE4ZURxLy0Vg05niEEiFjH02pIZ8PgXAGROCs-KbQmQ5z0J-F-lLIu_ze5iAwbU12yoC2SZnkI2QbnaYxy5yi9TygcPlmCTpbUN76MQyPKefXKaPU7wZHLb7udZKTdycgIDv6GH1LkNqX4GQcr3yrG0zwjrLpmgQ2djsBt47PAJRXtPnHUw25GO0RZR0Xbwvx5zAr6VaTIITt9c__SaTqLahsOeJUEcFYb__DSPpaoKPphhuKiijHp0EJOt_gHHnZ2s2ZEfOKIv0Zd0A7eew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60c66f257.mp4?token=IvDCVWk7C6yAS6mDN4VUl8OaJ553gul6X7NDHyehPomQQewshQnyFBIKN-NbLjFbgMHE4ZURxLy0Vg05niEEiFjH02pIZ8PgXAGROCs-KbQmQ5z0J-F-lLIu_ze5iAwbU12yoC2SZnkI2QbnaYxy5yi9TygcPlmCTpbUN76MQyPKefXKaPU7wZHLb7udZKTdycgIDv6GH1LkNqX4GQcr3yrG0zwjrLpmgQ2djsBt47PAJRXtPnHUw25GO0RZR0Xbwvx5zAr6VaTIITt9c__SaTqLahsOeJUEcFYb__DSPpaoKPphhuKiijHp0EJOt_gHHnZ2s2ZEfOKIv0Zd0A7eew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از ابراز علاقه هواداران به بیرانوند
@AloSport</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128383" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgdNOTF1H0m1bFF2rWfzsCcMSpfhf6RFJX-iGegBq81cfkOfxyNlQYoU5yB6A8T0WpU5ky27Zmk6D8fHKQVDU9MDlQjPpnwpjyyY0tNKL0DaDBSSTCeUB84Y3F0Oo9gU6DSZmcV7FoFkLeDXAY_TbVxaxUmIvcyzYyHmSu30BcluvahFmDkuDbpPSScrCFWtfSZvWNAjKS0UclT3Hv1zLW6rN8ClMl_ZjNcs2N4rWXwjIyMSuCiInDusPMRySl5MZOwUd26WBO84uNRadsCQ4FuI_br9JHXc-O816SAGU7kzjZH0bOmnC0i8ehwW78ECCCwZcxGfYafwBn2AuJFLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیرو هوایی اسرائیل درباره جلوگیری ترامپ از حمله به ایران: تمام نیروی هوایی آماده شروع یک سورتی پرواز رزمی عظیم بود
🔴
عومر تیشلر: ساعت‌ها قبل از دستور پرواز، با کاهش زمان آمادگی، انعطاف‌پذیری استثنایی نشان داده شد و کل نیروی هوایی مسلح شد، برنامه‌ریزی، آماده‌سازی و آماده حمله به صدها هدف در قلب ایران شد.
🔴
حمله در حالی متوقف شد که ما فقط یک ساعت قبل از پرواز در حال توجیه اهداف به اسکادران‌ها (گردان هوایی) بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128382" target="_blank">📅 10:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ در ازای تعهد تهران به ازسرگیری مذاکرات هسته‌ای، با رفع محاصره موافقت کرده؛ این یک عقب‌نشینی راهبردی است
🔴
توافقی که رئیس‌جمهور آمریکا، دونالد ترامپ، با ایران به آن دست یافته است، بیش از آنکه یک پیروزی کامل راهبردی باشد، نشان‌دهنده عقب‌نشینی از اهداف اصلی واشنگتن در آغاز جنگ است؛ زیرا آمریکا در ازای تعهد ایران به ازسرگیری مذاکرات درباره برنامه هسته‌ای خود، با رفع محاصره موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128381" target="_blank">📅 10:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تسنیم : دقایقی پیش، ۳ نفتکش و ۲ کشتی حامل کالای اساسی ایران از محاصره دریایی عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128380" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
صدای انفجار در دزفول ناشی از امحای مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/128379" target="_blank">📅 10:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سپاه: احتمال شنیده شدن صدای انفجار کنترل‌شده در جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128378" target="_blank">📅 09:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
🔴
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128377" target="_blank">📅 09:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d96af772.mp4?token=szN4D8apIbBhi0FxFXnWnSWVLYqv6rN3pRS1Nvd0ZFKJO79730HjpN8XTVtpkWZDrU7mKoG6B2xyQjXP4C4LX4H8KjjPkAnD6X7GDaLOqr6gHXix8dMyOCu7rdk3nwiEY76XDpsz3Q3uC648q9U33AH5khAXBfPrcJpuP4ZBV9gVabpjzuh-sAPItShLpjV_aP5MTqHiv6QLYgGGQtRH7GKdOePb5hYvuTH3HclPN6HIrzR6fVm-hf9Q_do_nuA-cL6xnmFFSCE3Y2JJrtCB4UP7fEMgCk_h_h7cS6RC9Zhr9X1cMFNvqEIvM37Yjt-A0MtmcN0polZDhG2Bpeh6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d96af772.mp4?token=szN4D8apIbBhi0FxFXnWnSWVLYqv6rN3pRS1Nvd0ZFKJO79730HjpN8XTVtpkWZDrU7mKoG6B2xyQjXP4C4LX4H8KjjPkAnD6X7GDaLOqr6gHXix8dMyOCu7rdk3nwiEY76XDpsz3Q3uC648q9U33AH5khAXBfPrcJpuP4ZBV9gVabpjzuh-sAPItShLpjV_aP5MTqHiv6QLYgGGQtRH7GKdOePb5hYvuTH3HclPN6HIrzR6fVm-hf9Q_do_nuA-cL6xnmFFSCE3Y2JJrtCB4UP7fEMgCk_h_h7cS6RC9Zhr9X1cMFNvqEIvM37Yjt-A0MtmcN0polZDhG2Bpeh6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: ممکن است در این ایام با حملات سایبری مواجه شویم که نیاز به مدیریت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/128376" target="_blank">📅 09:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ اسبق اسرائیل: این توافق تضمین می‌کند که در نهایت کار به یک ایران هسته‌ای ختم شود.
🔴
من هیچ ادعایی علیه آمریکایی‌ها ندارم؛ برخی انتظار دارند که ایالات متحده بر اساس منافع اسرائیل عمل کند، اما واقعیت این‌گونه نیست.
🔴
این دولت ناتوان طی سه سال گذشته فقط مشغول حرف زدن، اظهارنظر کردن و پیش بردن دستورکار سیاسی خود بوده است.
و از سه سال پیش تاکنون هیچ نتیجه‌گیری و تعیین تکلیفی حاصل نشده است؛ بنابراین آن‌ها باید فقط خودشان را سرزنش کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/128375" target="_blank">📅 09:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: «نیروی هوایی آمریکا تأیید کرد که در پی سقوط یک بمب‌افکن B-52 در پایگاه هوایی ادواردز در ایالت کالیفرنیا، ۸ نفر جان باخته‌اند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128374" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZW6J6bhy8XVSva2akkKPryuBzBQ91yeMC376ULLa3qawONEE_JNIFP6s1oCo7LpLvFQuJXA3AW1Vh6sOfnoZFkXqsSme7LGuaFQnddoHf1KnlxMEVnrFnrrPYCkI1rk6Bmm_qetTYCF3zVIf0HSMyTuX2xhoLDuH3VLm2TDaXUgr7O2Fu_jNyQu_mPkJpoiDIX8QegCHErQxInJOLfCoh6XZpMMwuxz4q0FmUS99zIkXnx_MnFp5JpmoG6WGHtWvhmzsBLHJrkajVc8IGDYi4jLvYnd4mSQ-bW8Q6rTvGjawAf7djOfIclmE6eZtGeckPQ1hMVnFTP_V6F50bGHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس ۵ میلیونی شد
🔴
شاخص کل بورس ۱۱۶ هزار واحد رشد کرد و به تراز ۵ میلیون و ۹۷ هزار واحد صعود کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128373" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
