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
<img src="https://cdn4.telesco.pe/file/m_emIiSnpt_QHnG87jIJuXFqHwGWqReF0TRemOPxyGYbE3o3bOsuSQOtsS60UAfgSBgY3jFc73jR3sj8JzJ1dtHcOJ_OC5o3KsOp6u0YJNndYlxXkcduzMcsgfCXKJP04b3ULICt6t-hM2useMdyKNRjxguvleTLAr2rL9s3XCI4lZeiS2nd46XJITiE3UrtTdA-dWhw9sbAaxhiPG48Xw1v5xVQhnQv_y6x9CpnkQ7MvuleSWPuimTNyaKe3quTqyn0G-xMIS2WDNKzsyKty-WTYVlVX1ykGILNsxLU92nkaMS_sNPLh37r-XrQN_xIxcR4L7QfvSAgZw5Yybb_ZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-452379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg2QVyI6xoV-WgAC2wRlNWJsPD3NoeTEFQL3og_XA90p4apzRS3CZhYB7KD9Mj0aMs-RFq3DCPXhO3nLbT6aCxkHiTcbhCVCWZqE9hP6dYmmTq8F-k4bzcZAvOM7xRHfSIYS-M9Aa8ivNCIuggARZroglO8O0--fmB4KPhzZFvJKCIkWxQu8iV8ZLxeFdwVE62scLgj7vECjz3L7YcwbkXcZxon5YlNdwnVUyRFcCzA_Inp3LMnJgUsvPCo1aMoqoK0LwcLn9gLKUO1GPfxWN0Cvzbr8a9XFSPamBuHtSG7a0nk3uSqEQbVzwOKwfYFot_PM_Mbqroqgdaj1gjpeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومینگ ایرانی یا خرید سیم‌کارت عراقی؟
🔹
با نزدیک شدن به ایام راهپیمایی عظیم اربعین حسینی و آغاز حرکت میلیونی زائران از ایران به سمت عراق، یکی از مهم‌ترین دغدغه‌های زیرساختی و رفاهی زائران، چگونگی دسترسی به اینترنت و برقراری ارتباطات تلفنی است.
🔹
همواره یکی از سوالات پرتکرار زائرین این بوده است که آیا برای تامین نیازهای ارتباطی خود باید از داخل ایران اقدام کرده و بسته‌های رومینگ اپراتورهای داخلی را فعال کنند یا بهتر است پس از عبور از مرز، یک سیم‌کارت عراقی تهیه نمایند؟
🔗
فارس با بررسی تخصصی، مزایا و معایب هر روش را مقایسه کرده است؛
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/farsna/452379" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حملۀ ارتش تروریست آمریکا به یک کشتی
🔹
ارتش تروریستی ایالات متحده اعلام کرد یک کشتی تجاری دیگر را که مکرراً برای شکستن محاصرهٔ بنادر ایران تلاش می‌کرد، زمین‌گیر و از کار انداخته است.
🔹
طبق اعلام سازمان تروریستی سنتکام این دومین شناور تجاری است که از زمان برقراری مجدد این محاصره متوقف می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/452378" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.  @Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/452377" target="_blank">📅 01:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
منابع عربی: وقوع ۳ انفجار شدید پایگاه آمریکایی الجفیر در بحرین را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/452376" target="_blank">📅 01:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انصارالله یمن ویدئویی خطاب به عربستان سعودی با عنوان «تنش در برابر تنش» منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/452375" target="_blank">📅 01:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPX6RK93oWpjq7ZCoAUxtAPqw7ehgvrso2axvY-bMSXdP_FNtVrcgmSz0PMnS6zauugbws4gxQL6RrxpLjmcM45ZvrXHZyh6hXvUbWNhxCLN3I2iZChil1wKWh4la0myc26tX-2MOl88-PPiJpFTOhuyA7pajS5wzYL8QBymIamnE-6IVgFhOQ_xf-S8Oe_-aqLgMShSRO9uqgYlHx9T8TvjPGpdHQ3o-kVCFDVe_Zey7wuU4PR-OpZE7CR2J25QM58fOs3f6-XFJyo5fZlb2bnBiLYXE-dh5YM_zIsdQHMHvsXIfQG8V9LMkeh96lKorQkhW9-PS_akuA2gWpyeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین دستورکار صحن مجلس پس از جنگ تحمیلی سوم منتشر شد
🔹
نمایندگان در روزهای یکشنبه، دوشنبه و سه‌شنبه هفتۀ جاری، به بررسی لوایح و طرح‌هایی از جمله لایحۀ مقابله با جنایات بین‌المللی خواهند پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/452374" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/452373" target="_blank">📅 00:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_jmcs43YlAeBLI6-Pg2dCKYthbovUtI0mCTMoSf42AKHDD68h44BDOvFM7zOg2dldRTW1Xzv4WLisZqfAUG1XBRLfMF1UtYUt_sWMlNaJ20pKDORSytHHhgQFZ4lucDLJfF0vgxtXahk3tFrb1-Egsmgh_Z3eSNsCogN0MV96clerqxX_tf2BxJFa1GL_Gc34bn_ifH3NnNzVTO5_yPd0kYnTcGgJF7JqUdiq8xDjmeGlXt6tNtiPcL4UH0Mu3t6fkJX2FDfaRZHvWJoAKT7ES8F4w7m35IQVplhK23nBVy6OYWJzSQESZlImWS2cIfjDJOaPqHIZGeEyHZr3ArMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9iecZov4pFtyLn6q693P2y59XtCPscX_7cirQshR2JebXmtsIXR717kugNyVFUiE7mCWawXaT12AMMc3MFbdEgJJVFlaNWB7vhk51ciWTnlYUTAOFf7rdzHwFvtsbj3jNNQj2InPI0YodqXFkRsvAlgftkGkmg-dPXf42JenYlYbQg69NaQakolaVOQL78Ehp4fFiOSy2b0yYs1gko8cuscPRtD-DNel79Txb_2xA0Q2rl5Jf1n67BqwmfXOAiqW-nkmLTBd_2d9PF00hcr9xmCfqYjnxRQ3_FxFEwq-YATwwyo0BFQygwYexnLDW5BREetqfui7kuZR7DVV_o_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2_jFInNbGp2KPBZnl5lSomJfEBv6jjC5MhZfMgH-zQS5VpLZ_gc0i6Ro-jJGC0_ZpzksAd2gp1XIn_kBnWzNnUUSDhcpc5hf5k1h-W1Y-Cph_2CmGMXLQayNqLI9pkjdF8L7nqyXV8wIikahBY2tRtMWop1wCG-6Ph6zXp1H393q96hazljZpEroCdV-yg2ahawA_s3GErE1UXhOySWbI8QWUcQzxYE_RmhvGvxvzKXvQdiRWhO5Da6YBtgP0OQPVjokaGDywKMb0Phk1-Lt41vCdxxdoWCRJaiWv38BU6P2U0TiaEPogc8VT5ILjo4ke5dGjeCpFa6djU_RYPhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GylwRkX7HOqehhgnT7BvxoQeJhRfDJFUKDYz4EDZgj0_MKcBtE3K3f6iiTXZmwHJXlnOoi6qvfI_1y6rf2put_ORhe3pO65dA_9GGUFSzy7kdKPLvMAG-GIfW0bDzz9vqRjqku5HyJCkIItj7QEb7lD2ckyr42ltE2b1tDSQaypEwSxeAKSwd6r6ujH5SWhWXqw7VEZ5yrMyyFOarfJ89n8Lko4PgShGFXDj1eBxBwfUkfkPL47eyBZpdKM4p4uuD-1TVB3gxIhmetwIHSVTedJstyXYtupB6obVsSguoKpodwx_pJMJsUKrZgMd0d0il0rCfkEIwKn1zgeNLEFNaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/452369" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452359">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyjjcEvWOSuJGtOF32CgakZFrTJzW2R7IGtAl5NcV6IBHKxeHXuOl3ZOsuCSLBSUzXl9rmcdq_c6OalyjIlWBFaer7fAFEB5x08gegUSw5YisZbE1HXe-RJxLbFqVg1U7qJvvZIRVG2H684ABPAQjo05xqvYypMaq8ZYomQHVv306J_KGKbliEYl5QavWyw74k-M3rTGg1LNMnx9MKfA9DUDO0HpQSi3z-e8iqKzTyR9UBZz0ZkMpYN1V4iRgiv6FO8kPymlLB2mj35-8qj2QYxA_cKXqC__uzh_5ibUPVfWpaeZI1ZUgF_glYdMGisVv0C1j7vBBzUQC1y53paxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyDAgvceJ1VCl36FvZYyrbs_eSFzMRTfplcRtknQOOlG7leDJNUSr7gMRclOXQgT6bPWM-hDTU6LJl0tnEahs1AGiASwPFH4eLfv4taBvXhppjGKllU2Szq9Ljxhtm2zRDVDczpz2WsaIYKkeyHp8MM5MXzcwoR7FLCKMI64bLsGPMx8Q0sawdrqLjh0Pm-ousIhRcuoZkxptA0QDpLbJbu9wAW3Jr0Ej0rhMOHRy-ePI7gn_oGCcawDQXRuSnHSN9YyK34vI_FF_6rZrJ_2k_ne6VYKmCtxxrbaOIg1fDR3fzkbiB9rxumuQ6ngw8uU77nGi934WTpCsyCaU-ZDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYF_-s5oUWfPfs8w8_0Gn_vvnYwq7-HSs1VWL8zW6OGQL1pYKzBiCdQRxJq5vePwt_Skzbd9mI_zwHt8h0jOZu5igcC_55Xv_IflMXmcPg7r5_JOs5OPFduBrz2qiZaz1IJ4nqsmCxNwipuCgr8uVa6bKIXx4xRxCMnzi8Lh6Ndlq5T_H_GWT-hquTa690rGfKIpSTXXByL-lumI69w7b7Zn3nMT87OwuE-XEFtYZAdv3TbBJfoyH5_WbYlSmPel_hHTe6-f2TlsjlRTPtwDCQ1DfSrdZxdwYtikpunJaJ8_uCpTpFArk-1rdIwH-A5kCTLPh5vdZAwMLcosH_hx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB6T9LTl3_-9ynKQ8veylvrNjqTQr06K_y__DvUmIba8iDb7lpBufLoTAV3UlKtVLJsWAh_AczpbSpf_s3xvI3YxUWdVtzwTdmDGdNUAeNtZsHYZ8_Qi8ePHu9xRjjw7LtSjEZkjCXRSs0qMpxnXFPJoycVsefOE2aPZo7ezz2NUFWxofi7r0N6ezz0TmrJLQXlGllzE4vgicwrnrwyRiba8nwjqIUxo5OEYXrsV2-HnPxTMdCgPalWJ6qnrQ59wM3RSq_PG-F1khnCoLvsLPmFB0ZTy-AgRPSadQ6a8eQJOhqa6EtpMVw80MrHcjALlKtp9Bc7nyXcuQgmF2AKdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgNLCxkWUnevxxdWptP9GGyMeCStygPaBoVlH-0QeIrMisilkjZ1kFZBzHl1_utQN7bGx6EKGgEgzytni6ga6TqgLLYo50HAvmpNYUG9fZz6VbzKY5oUEZIGC6mAS4AB6p-tUXyDHVapnhk_NVMVQY_oi-P3hsRo0_ypF6EpwH9VW8MvjUvu72qvG7WW2PsI0THeP-qUYPjaxeTYGvvwjLYmhKQHPWMIb3BM--4ZlZIc_LGSslKr9w8-yWqkej9oDy0QG3snSn4gMqcgOcB9yLtTkaa9ExTumYpxiredt1EYqob226d9vDkr790XlPv673W4kMjyDJjiDyFBxmJNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aczMpzPGdTcEt3Psw_BNrKmyD0zH8KJYCxpu6gV_hsQTUdKFV4T3aPhyj9Nepituqk8xd9NoanPgTRarXeI9BaADmbPyg9C1190WSETNkxgVjvzply5IjGsPrBtKYDN0Yn_ZQ2SEmAPLJ3bbJn54Uyw9poHKCYn27tOx7PfHhINTfQfs4frApAHqZ0kwuuIQRuSkPQriw3q4Mj1lu1sjUomC5d7oWHxvOqcuuMFmjLZzXnf0mjXrfw5dspVW1rb7fysSpYAN5mjN02UtObTILkx9XX78jY693gNPxA0kS4FlPcxMmQCQxfuewwO5_yL-Yr3TpAHoG3Zvzaj-pmPoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYfUhBYBKcwq6fyzcd8I7Gkb8r55QOqXUIlxgOjK7uS9RsETKo-ZDMtFUNsb2fjuFILiZpLKko622eiRBWuH9ubS8xE9MCkAqg4unFkaiM_ZP-YckzX37LEc9zRI5X3aT6Qwr8-SaMgPx-epXKUHwFGNwoHfg_T0DqtY6vznUmeZCQbPCEpGjngX16ySoYcIQmPdUsAX15UOdnuu9d0svAwxznieRGb7yiuIKSUhXiHYBn8lu9BTcARy6QJq6JspS9A375CioXXAcM7gR3MJTuUYfd1sT6qbMOMSHg06vF-jR2TO8skWl4-K73XTXkojH2gpbmPdl_gm2Bj4FZlJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2zLbFED1-CadeGK-12zUoWX6UB3OkLW3IH6k3PbKd92X44QTes4SKVCakzNp3rQg8ZZ8UZXeL42Vjafq18A_mlpON1YIstKhveZ3fvVSo_vr1cYLg4ABZrYwTE1yncr5RZILGEXzIC8Ft4u8tDutN3aW7rQ0H2_tkVqtzvz6aCxx1O7XFTCw7c-FJCc7ZdkIFCH3a2HeT5dgPSYGet8OhBwX0IFgzNfzGyPbOqDotDbhQFTQ66rqv77kIcTv9ZqQn1BwdXqwL6ldKq-tRsh4RQkpFB1nLsFPnO2vu2VRymm_-UnrQtGD8mbu_gn-4fo0-ozg8PZvYkJYEoxQwtXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2ZVWecewPQf30BO4MSE4baTqG5UCMuoYpEzWqCVa4TeuNHsRmL4wTpteOFCvFNty0bUezOr0HhLdhb2YdrzBazNz0CfZ9KPuK_blrGaAYc-uTAa8j9la861bdNCZkubU6HIGor2F5f-kqCCJfZiC6JsdhkfH_c3nezdCtzQvYXp7AYGCkzBfE3zilYMFKiAFKcm6EaDxT9KheiqMIbTo4hSg28EypTzbIf-zOIs7CTkRjS2M4n-6BTaXpbOUFkLOEfLxGNL_2xPpqb-hz0LoJN_Bvzt45a77AjEbZ1SSZQLIkgx_kfYUxngs8RIImpmSN09UqC3obEB9DuFneMKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYoVdYqNYxzd3j49dXR9DQAEszA5GijVibAWCZHQRa0rMiYMZ9boMV6pMRgRdGCSspTlaj4HRn1U9S8QDW5MrOKvCYV6pjN1L1NzI-hu0mwE1cE1GvvXrd4W22o5-uKqaGGJqm8hqqx0_5MroOUwe1GbZT0_hzauwuaQpFFJDfDTBSjqNpfdYUcYEV2iTAfr_s6MCd_qN-aSA5xRHXSo-zun39EY6dCbTNDdSe0I-KAvQmM3_8V1ec__SX_Sha83CbPqn-bBIuCj9hjFH2XEIXi_Rd_3k1z54soGdflejOcP4RPIntizHcVItwyFpqRGzq6qX2QO2JScvUHqPqRVlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/452359" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و به‌صدادرآمدن آژیرهای هشدار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/452358" target="_blank">📅 00:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452357">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و به‌صدادرآمدن آژیرهای هشدار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/452357" target="_blank">📅 00:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0e33dbf.mp4?token=sistrlEs0l0yuMQLiLf9bvJ2KUE1ixNeH1R7GohAl6DzL3w7WKZBNkntCZerwdx-DW_agIW2F8Y-OfVAOT4Hy-NVx4__QQgcayC3UWjU6FEnVt4wYcYjcU3Zm9liz95pKWS4haCmiWGcEEXEwyq3LhuK28pccq6EIddtVSAbz8ocL3J-IWRTGy-7IymnDl8vIFOIvVq-4ardvtd0GJ-T84vTZznFIMPr9SNyInU_Blrm1vKzWRmUsSWCPlhj8XoiGifOHTw3MxHxFjHLUCiLkjCrGo0Otx2RI8lHzhjgFazRNlRi05PW_HVaqElNvlEx8-nopJHqEhfR0dDhVsyTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0e33dbf.mp4?token=sistrlEs0l0yuMQLiLf9bvJ2KUE1ixNeH1R7GohAl6DzL3w7WKZBNkntCZerwdx-DW_agIW2F8Y-OfVAOT4Hy-NVx4__QQgcayC3UWjU6FEnVt4wYcYjcU3Zm9liz95pKWS4haCmiWGcEEXEwyq3LhuK28pccq6EIddtVSAbz8ocL3J-IWRTGy-7IymnDl8vIFOIvVq-4ardvtd0GJ-T84vTZznFIMPr9SNyInU_Blrm1vKzWRmUsSWCPlhj8XoiGifOHTw3MxHxFjHLUCiLkjCrGo0Otx2RI8lHzhjgFazRNlRi05PW_HVaqElNvlEx8-nopJHqEhfR0dDhVsyTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
«شما از بمباران کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بخش زیادی از جهان متمدن، این اقدام را
جنایت جنگی
می‌داند. آیا شما هم آن را جنایت جنگی می‌دانید؟»
ترامپ:
«من به این سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟»
خبرنگار:
«نیویورک تایمز.»
ترامپ:
«حدس می‌زدم. نیویورک تایمزِ در حال ورشکستگی!»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452356" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فشار ترامپ به کردستان عراق برای جنگ با ایران
🔹
منابع رسانه‌ای خبر دادند رئیس‌جمهور تروریست آمریکا به‌شدت در حال اعمال فشار بر سران کردستان عراق است تا بتواند پای آنان را به جنگ با ایران باز کند.
🔹
به گزارش خبرنگار المیادین از سلیمانیه، دولت آمریکا به مسئولان کردستان عراق هشدار داده اگر با ایران وارد جنگ نشوند، نوع حکومت کنونی آنان (خودمختاری) را لغو کرده و تغییر خواهد داد.
🔹
درهمین رابطه، سرکردۀ گروهک تجزیه‌طلب «سازمان کردستان ایران» صراحتا اعلام کرده که آمریکایی‌ها از طریق واسطه‌هایی با این گروهک ارتباط برقرار کرده، و حالا این گروهک به دنبال حمایت تسلیحاتی، از جمله سلاح، مواد منفجره و تجهیزات پیشرفته از آمریکا است.
🔸
ایران که بارها به سران کردستان درباره آغاز چنین جنگی هشدار داده، حالا به صورت روزانه و با حملات پهپادی و موشکی، در حال کوبیدن مواضع تروریست‌های تجزیه‌طلب در منطقۀ کردستان است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452355" target="_blank">📅 00:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ عربستان هدف گرفته‌شدن کشتی‌اش را تایید کرد
🔹
خبرگزاری دولتی واس سعودی نوشت: یک فروند کشتی متعلق به عربستان در دریای سرخ هدف حمله قرار گرفت که منجر به وقوع آتش‌سوزی در بخش جلویی آن شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452354" target="_blank">📅 00:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مرز سومار از فردا آمادۀ میزبانی از زائران اربعین است
🔹
فرماندار گیلانغرب: زائران از فردا می‌توانند از مرز سومار راهی عتبات عالیات شوند؛ مرز مندلی عراق نیز آمادگی خود را برای ارائه خدمات گذرنامه، پذیرایی در مواکب و تأمین وسایل نقلیه اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452353" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUm1_bjhSLTTh-ONTnvMKXK7Xs_5NKv-x0nao_-1lV1tZ9B1RHxZzFQe92-ujxYZIRaLPSJHkd8Uip2qi4ww6IzkrcgQ4EZSHYa_kVnbhH1ctNKQydzdsYEh-PEjYzEP_xFZqmykb3zxqvYcY9TLhpWWvZUX0olinyrpuspwyYSr_AxxdaKyDT_jJhlRSZPWgUq4ZjQMoFp2MVWLy92pwtNdnNOaaicPCv2PXYfVqpqexuVWts0Vm7y81wBaJdbrKGLEI-e_MZ0ElkkKaiLoR4wKsO3R-3zvqResrU1AnmRRFLqrAMB7vOYxdF3KoUqC6BYYRvDVptYHJgFJWoV9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFQ3WSOyCYnIOpYmtNictDWHSaM7yEiVN3Jz5qxMfVw8VoRMLpn0tNaKZSLatQFK5YsiJOLIDusVYVTCovn5JAqb3kZHcvLB-2kE63uK-oxv4j_41hpcgYJ3MM2XtImatdRcEO_08S08KDQopiPBSGe7ZPhW_84ojI9k1IXp_TuJSqwUYOMSYMm4xpByDXc0nI9QrtdHNQplpiFhUx_2HxXFVlNV0QOsL0NmDFYLhcpraSOSA2WBYs1CLiqxC46oKRttTBgL7APxe_dSIyjoGne7uiZDzqm8Dw4nlKP8k5WIF-8H2Ve4OEX4FaD5BAcczO4X5Oejt8FEWvpG3Z1Pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_1iAkab0jh0V0_CaDC-sj-l9PknJRSYCO0bJTzCyd04pVzEYKD9_hFVjcSBL21PIHhB3lv_RW3QOltOCuMyBaqs6xOpvDr5ZG_v03fu5D4kpXbdNCIN8Jjseb7mTiBAM-QGK3M1yD2YfyUo_IoQ71VZZovAzvfMTLIRS1Za6WxTwBzTHqd02YbVFxxp9MOpUkOBkZUoHQGtJU7jUcvR7znAqmU7bu2cibYSXj1zHZE23eOMYsnfxWXoqK5nRHS-wXGTzS-eCK4K8-PJak6af6IY0_LZsNpxgtB5tm8WKgtwf_b6d4FcoNI8q9R9P9rnSA629eoCUDWp1nc9dVLnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKb4DJub7lRv5HzBp-IQlpVc1pexm1ynawgaYV3omtvmlAPKRNWAyEbJ-Vvd8mGGHI7QGtPYAEm2YExsX1u7f2sEw5C9djoXBWOSuDKdADT7Wfb5MVW4C2GHG9jRduo7vAcfXZlgGss0h2WuqzmdJri27UpU7EGlw2wdd01lrkY7obO0rC6pOGsf_axuzjueuu1BfoTJKt2gs9AxdKDFefXhKSXwI0KaMnyvnnbXN9Rp8XwX1dh7BdzXBZScTACVPG_Za8Kon9wsA5SmAQuLWBtX25vnxGmdFd2K_Rqh2RwlZaBgKSD10EOD6GX-C4r0WwabY8XH5_bQIL42POMLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWm4DaAYAPh-NeKpNrnBRif1M26ClL_f57VD81YXKruIrlhpCaZI4V2Kkr1gZCs_dAohuWrxfVb7US30_H6FXA8p4aebs7QTn0qffnE-eBsess5oXtXGUsBSgagXsJ2EXkXmuAjUI8fNCuy8_uPx307ggEgxvsjta7SqVkEXln1viMktBPXrSAe2eOI13BeVb58oNnUkWGMwHwAc5rk1H9Aevk6xOkUpyy4IeiEW_snnQ13M0jBsfZahuzuRO9GvggdQqudLd1dkEhz4dDtn6bpYMFfHA7ysl3bKOENEHyawvrYfVlAslvDh6wmoWHG9tVclPsry23Yepbr3oxHFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMIdAQ7iltbeYUdvJylDcG9DAK7yjcpAiBLS_CCrRZeQawzRbfQ0gVlHjPUoaOCmiQ7hfPms8Kn5v87pA1dVB61eF_g-5JuzOWPRfJJ6piJzUb3x4WdqQGI225AiW3uyZE6E36w6DUlFxhnt6_54ebBVTzFbBVPiYjk8cGEGAqoVpm51YirQC1Ua_SIHR3VyOXvqnbRGFfbb_PjZp0Hk_OSxVqKf9j8SCYZIRm0xE8wqpCBRvq7eLWHenHsBqTpJcSlnAdsskcA3MxTGASvYmHZS86ghUrx9EbtMLtb2loXx472qNhksmJi5xG4fKo_8lnvKma1VMnXh9B25y4CEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPS_qMy_qgE6YUdW7S6HAVYjl2Wvlu4Gg30ENJqdnuydyaLzTrdAsHnnKQ405BkoEEIgXaRTXTmAJ-64StS99iiKqT5BhG5GUFeUNegI6O5dOGe4HUjTc9EAZOjTRJM0lhCIjQe_BzaJKQZib2fa8WKDR1YWXigt-qlI4JdD4WUJPVOy09Fd1_6hCHzcQ8sNPsjGS021cm60Zu4rcxdXTUme4bHL3iDC4YCWgpOtfYM88pMVktQ3BdlzUK5Jp6_DYBCXx4dqBTXXq65lywdU1HH36-wjJGZrBlvbZZ7xXHg3UTeXoOuM732ulpTiE19OgKVXsZshkahjTOnvnxiJPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید امت در حرم عبدالعظیم الحسنی(ع)
عکس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452346" target="_blank">📅 23:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-text">چرا پرویز پرستویی از پهلوی‌چی‌ها عذرخواهی کرد؟
🔹
پرویز پرستویی که چندی پیش با یادی از جنایات علیه دانش آموزان میناب بر پهلوی و طرفدارانش لعنت فرستاده بود، حالا فضای به وجود آمده در مجازی، حمله گله‌ای پهلوی چی‌ها و ربات‌هایشان را مهم انگاشته و یا برای فرار از دست این حملات دعوت کنندگان ترامپ به حمله علیه ایران و توجیه کنندگان جنایت میناب را هم‌وطن دانسته و از استوری پیشین خود عذرخواهی کرد.
🔹
این استوری در واقع بازنشر یک فیلم بود، فیلمی که به اتفاق تلخ همان روز و پیدا شدن قطعه‌های پیکر شهدای کودک مدرسه میناب برمی‌گشت.
🔹
در همان فیلم نوشته شده بود بر پیروان پهلوی تا ابد لعنت باد، چون این جنگ از همان جایی شروع شد که این افراد از عمویشان خواستند به ایران حمله کند.
🔹
کافی‌ست کمی به عقب برگردیم و یادمان بیاید که همین حادثه میناب را همین افراد در همان زمان توجیه می‌کردند.اما اتفاقی که بعد از انتشار این استوری افتاد، خودش داستان جداگانه‌ای دارد. موج بزرگی از فحاشی در فضای مجازی راه افتاد و پرستویی هدف اصلی آن شد. این را باید گفت که فحاشی در این فضا چیز تازه‌ای نیست، همیشه بوده و سعی کرده تا دیکتاتورگونه نظرات مخالفش را خفه کنم.
🔹
همین فشار بود که باعث شد پرستویی در پستی دیگر عذرخواهی کند و بنویسد قصد توهین به هم‌وطنانش را نداشته است.
🔹
با این حال، پیش از آنکه این ماجرا همین‌جا تمام شود و با پذیرش این نکته که لشکر غیر واقعی و مجازی پهلوی ترسناک و دیکتاتور است چند نکته هست که باید با استدلال روشن شوند.
🔹
اول اینکه عامل جنایت و شهادت دانش‌آموزان میناب هرگز نمی‌تواند هم‌وطن قربانیانش به‌حساب بیاید. این حرف بی‌دلیل نیست. هم‌وطن‌بودن فقط یک رابطه جغرافیایی یا زبانی نیست، بلکه بر اشتراک در سرنوشت و منافع یک ملت شکل می‌گیرد. کسی که با دعوت عملی به حمله نظامی علیه کشورش، در کشته‌شدن کودکان همان سرزمین سهیم می‌شود، دیگر در این رابطه جایی ندارد. پس نمی‌شود صرفاً به خاطر تابعیت یا زبان مشترک، او را در همان دسته‌ای قرار داد که قربانیانش هستند.
🔹
نکته دوم به خود فضای مجازی برمی‌گردد. اینستاگرام، با همه شکل و شمایلی که دارد، بازتاب دقیقی از افکار عمومی جامعه نیست.
🔹
از اساس سلبریتی‌ها دچار این خطا شده و آن را بازتاب جامعه می‌دانند.
🔹
اما در این فضا الگوریتم انتشار محتوا، شکل‌گیری حباب‌های اجتماعی خاص و سهولت ساخت حساب‌های جعلی یا ناشناس باعث می‌شود صداهای پرسروصدا و سازمان‌یافته بیشتر از واقعیت به چشم بیایند.
🔹
اگر بخواهیم این ادعا را بسنجیم، کافی‌ست همان محتوا را در بستری داخلی مثل ایتا هم منتشر کنیم و واکنش‌ها را کنار هم بگذاریم تا به تفاوت نگاه حتی در دو فضای متفاوت در جهان مجازی نیز آگاه شویم.
🔹
اتفاقی که نشان می‌دهد آنچه در اینستاگرام دیده می‌شود، صدای همه جامعه نیست، بلکه بازتاب یک جریان خاص در همان پلتفرم است. در مقابل، همان مردمی که شب‌ها در خیابان‌های واقعی حضور دارند و از محکومیت عاملان جنایت میناب حمایت می‌کنند، تصویری دیگر و شاید صادقانه‌تر از افکار عمومی به دست می‌دهند.
🔹
پرویز پرستویی در پست آخرش نوشته است که به تمامی تفکرات احترام می‌گذارد؛ فقط سوال اینجا است که آیا تفکرات صهیونیستی در مقابله با فلسطین قابل احترام است و یا رقصنده‌های روی خون شهدای میناب هم نیازمند احترامند؟
🔹
به‌نظر جنگ اخیر باید ما را به سمتی ببرد که موضع مشخص داشته باشیم؛ افکار عمومی دیگر پذیرنده حد وسطی که سعی می‌کند هم نظرش را بگوید و هم رضایت طرفین را کسب کند، نیست.
🔹
بازتاب عمومی به این اتفاقات نیز خود گویای همین اصل است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452345" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
منابع عربی: مقر گروهک‌های ‌تجزیه‌طلب در اربیل عراق هدف چند حملۀ هوایی قرار گفت.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452344" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=mc_5P6ixoejHX1YqGbInLBvWNJjix1u58qNyM4FEmcZ-X_H0TyXeYUg1Rv7BPPhtgz2aYfFagQo-Yb36p832rhf8awQJlNrVYUHKcnUC8O93Wi4e62YZC1fFo0EAOQAzcMo3Gva0wxo7D23XaFEQW8s2xh1tTCDMrjjjix29EUDok_AP1CVt8eYqBLyMWuuhsXqt6AeWb1qswKPFEnsO53KStzgidjx7Vdg1j0OBB_ZcT0HgkVpjGcfqb9jKSyZb6dZKod6fGx16ZVRfeEzyXZ4J0NfyjrgNQyMANj__VXjHYK3J0M9lcnam9LvyK5qZ9Zx0SKndevZni7RnZG8Mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=mc_5P6ixoejHX1YqGbInLBvWNJjix1u58qNyM4FEmcZ-X_H0TyXeYUg1Rv7BPPhtgz2aYfFagQo-Yb36p832rhf8awQJlNrVYUHKcnUC8O93Wi4e62YZC1fFo0EAOQAzcMo3Gva0wxo7D23XaFEQW8s2xh1tTCDMrjjjix29EUDok_AP1CVt8eYqBLyMWuuhsXqt6AeWb1qswKPFEnsO53KStzgidjx7Vdg1j0OBB_ZcT0HgkVpjGcfqb9jKSyZb6dZKod6fGx16ZVRfeEzyXZ4J0NfyjrgNQyMANj__VXjHYK3J0M9lcnam9LvyK5qZ9Zx0SKndevZni7RnZG8Mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری شبکه سه: ۱۰۰ روز است که هر بار اسم بچه‌ می‌آید ناخودآگاه به میناب پرتاب می‌شوم
🔹
کسانی که دم از حقوق بشر می‌زنند، کودکان ایران را به خاک و خون کشیدند. ما از خون کودکان میناب نمی‌گذریم.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452343" target="_blank">📅 23:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5Mt9HID-llMbWglSdNts_JX8EjgpNgB3-stNPm0q8--c7louQkSxL2-_PgcPwnSbHdeQrkWSKfwbLssUgV8swtHboFN4MY4uvBhayr7QJ6lfI9mVJwaAxBBZV3zkvuRVnTIweBr_NUL6QPqR2VXYIGRNR9-KstFb_Fj8RRXf6OH3MdHDQENk4QcOEx24DCGMf_Rr8_yspMBntPqqs0WRALCrAn2i7iUrm63r0zIrx-e0DVZ9Lm0fC5N4vH7Vqicf6s54be9FboGydGBvuHF9hv6PlLcI2YJgHBCiQ8EAjYWzOMzCchnJO9nSuvnSU4OSk_MkhBrGYR98Ycd97VRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان: تاریخ هنر، نام و یاد اکبر عبدی را در زمرۀ سرمایه‌های به‌یادماندنی ایران‌زمین ثبت خواهد کرد
🔹
رئیس جمهور در پیام تسلیت درگذشت اکبر عبدی: بازیگر توانا، صاحب‌سبک و چهره بی‌بدیل عرصه تئاتر، سینما و تلویزیون کشور، طی چند دهه نقش‌آفرینی بی‌نظیر، بخشی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452342" target="_blank">📅 23:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e798b36b5b.mp4?token=C-vmTjOUH65V9iGmzf0GSnTidf-15uI8c5dl1GZ0HOiIq5Sfh3T1zSPXWqMeXgCVSSXogIfuOu7o3W_j934x27Te2DZ-EzJGsD7fOqsttTO8SO7T1kHV-xby8EFhvjLtJr9bPAKc_TrhL8ltT3CMxEnHlJOPB4yINn7kC6hEARZFmje0hyVty3XPK3bEolE0ferF2R7kYIAK1JI6FVu2bzb0DTmJWVM8LqcH70_OKsRfn7m33CjMwjshX6tgLP1ed7L7XNh9bBbqYsnwwBzJmlg4ssyGn-niGINomjLrvY5uY5VIXhuw0azmk1PpvR6gjV5gchDEJ1rMvMSAuH9S_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e798b36b5b.mp4?token=C-vmTjOUH65V9iGmzf0GSnTidf-15uI8c5dl1GZ0HOiIq5Sfh3T1zSPXWqMeXgCVSSXogIfuOu7o3W_j934x27Te2DZ-EzJGsD7fOqsttTO8SO7T1kHV-xby8EFhvjLtJr9bPAKc_TrhL8ltT3CMxEnHlJOPB4yINn7kC6hEARZFmje0hyVty3XPK3bEolE0ferF2R7kYIAK1JI6FVu2bzb0DTmJWVM8LqcH70_OKsRfn7m33CjMwjshX6tgLP1ed7L7XNh9bBbqYsnwwBzJmlg4ssyGn-niGINomjLrvY5uY5VIXhuw0azmk1PpvR6gjV5gchDEJ1rMvMSAuH9S_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران اربعین در مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452341" target="_blank">📅 23:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaVuw2lkHwhKgYaE2s700Rd-wE-aFSBGDanxRO5rdgXViiZ1iV-ttkf89kFakDr1r7RAipmwzbnfhjj_0tuOgn5zsOp-ZLt6Z1u0V5l8wVQVM4qcSqUwwleVgoAfKnfhdxWyNtpSxrgjwbhGM9eWs4kWYg_gPx0avgeNH0aOBGWY7cEI1LuJmlE0HnzbsR9gI3TUFSKNNiqOUd1C_uXH-tP1dRmAvHLJpguYBDNCLZPa1iXcKbj7IDShCIAhqNNJKHfMnMQwX2GG4PAncG24I3Hj8B4oK0CH6mOTw4TkeiB8zXii5uim5xCzJrOJYaoIRycjUAYqRkWAjJFZ5zhqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452340" target="_blank">📅 23:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6gidxlsLnFYZSl6nj8CqNn4ApGe87EQnvC9ssan2U0qdPEOgySxqe2sIb3AeQ7ePk6ty2o9q5CrW7Ufg332eFthLIsmItGiN8-9_JTRaXKJ264y8CFhFGvwWoDN04Wl_wTfCeH6dXxWrfkEJU8S-lHKe6tQL-Sq8h0dGSSZqdld9LkanIJa-0kt_dIcSFfVDByRVVnyad_yFHf0LC2x7nGTpV1LT8SS6j3a47XVUlTvL_gGuAWjMpLyt_v5-Y7CiUfSaOZGSnPcCRbSwFuUqDgWEWXOwTRalFOsF8FTltPdPR4zKqMFK9RbaF8N9NZl1f4wPp61WD8YuNCo0gOfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452339" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d22d398c.mp4?token=MGrX36ySayATmHju2FXEDPo4qvU6n-QXYGaGLvLOYzJm1JOocsa42KUj0vwljK1IzLCegdxWtYgLvwsFY7ViXaE-odm0NXquNikUsfpL9cBpWnVVuvDKHD-He2CL92j1VMQx6iYFpLr96M1pNJS7pQm2Z_OiFN2ZAs29xvSJuBE013jgMOF5aAwG0dpBGgNy42xYUuaNGNAXgl9zeymBBvEF4jA2fAR2IyUMyhrAmIZdBfp4YGd-dgZFJRJPOUmwg21DVntVCi-zQ6FmN02V6o9oN2wWGXJrmZ2owo76dCL47IK8FdXT82Goq3LHQ585wy-qCRcaJws22B3JDkr3nFN8_5n19V3eWbVmsjD5XpEt805mEWeE6_IOWxu9EAdIP0x949R8rTCWNcmHLYz3rpyPnnVfChbQOXAXavi3TlRifLXfqgNThXRx0mfVHOnoe8zTJGjZZ5c5McTCxpPGLOYbyr94wr7Wh8jwrowk7lNqccyzU89gMUmGFk0sounO6y06UVWjGYK_Cy8MbtQ2atrKoK1SgQoKu_RiKpO5p4P4ZEFOxfkya0cFDakYsaJG2XC-7dnO_HqU_VEmm5-CMfa13UOB2eVvBe_94gcoMrk2EYIQ1FEi8Cb7OVRB_nWp0u6t5HJ_T88omZGt6eSFtDG7xC4A0Bk1_xPM9tQDzJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d22d398c.mp4?token=MGrX36ySayATmHju2FXEDPo4qvU6n-QXYGaGLvLOYzJm1JOocsa42KUj0vwljK1IzLCegdxWtYgLvwsFY7ViXaE-odm0NXquNikUsfpL9cBpWnVVuvDKHD-He2CL92j1VMQx6iYFpLr96M1pNJS7pQm2Z_OiFN2ZAs29xvSJuBE013jgMOF5aAwG0dpBGgNy42xYUuaNGNAXgl9zeymBBvEF4jA2fAR2IyUMyhrAmIZdBfp4YGd-dgZFJRJPOUmwg21DVntVCi-zQ6FmN02V6o9oN2wWGXJrmZ2owo76dCL47IK8FdXT82Goq3LHQ585wy-qCRcaJws22B3JDkr3nFN8_5n19V3eWbVmsjD5XpEt805mEWeE6_IOWxu9EAdIP0x949R8rTCWNcmHLYz3rpyPnnVfChbQOXAXavi3TlRifLXfqgNThXRx0mfVHOnoe8zTJGjZZ5c5McTCxpPGLOYbyr94wr7Wh8jwrowk7lNqccyzU89gMUmGFk0sounO6y06UVWjGYK_Cy8MbtQ2atrKoK1SgQoKu_RiKpO5p4P4ZEFOxfkya0cFDakYsaJG2XC-7dnO_HqU_VEmm5-CMfa13UOB2eVvBe_94gcoMrk2EYIQ1FEi8Cb7OVRB_nWp0u6t5HJ_T88omZGt6eSFtDG7xC4A0Bk1_xPM9tQDzJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذکر یا اباصالح المهدی بروجردی‌ها در شب ۱۴۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452338" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
سنندجی‌ها در تجمع ۱۴۶: شمال و جنوب فرقی ندارد؛ همۀ این خاک، ایران است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452337" target="_blank">📅 22:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831aa2985d.mp4?token=oDSENnxKYiI5J7ZH0NOGGD2B07pA2vyErfXvF-q_P6yYTnM-exPfPQ0sPd3pOtf2PFGEznFkNbgcQHZ65-YmvgLRWmvHmhA-7aJspdGaFeZtT7O1KGoy30QYtpkU2yMjCo_3rMpftZrKM9cg5Lydtu7W61LFtzzuPTabwG-p6hvUpNPVpeNTj3kwGpwe8eWHWEVRvw7xQde_xVMTgsYLg2Z_GDFXGe3KlLHoPQuVwXm8Di_w9pz4RfHcZsfViEqYqUjj4StKX6hQC-a0eqZE357Igwg14GUJTidZb-yehAzjfYra0CVzRmBccYS2NYLv-E1Z79yarHsqwD0SBUjjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831aa2985d.mp4?token=oDSENnxKYiI5J7ZH0NOGGD2B07pA2vyErfXvF-q_P6yYTnM-exPfPQ0sPd3pOtf2PFGEznFkNbgcQHZ65-YmvgLRWmvHmhA-7aJspdGaFeZtT7O1KGoy30QYtpkU2yMjCo_3rMpftZrKM9cg5Lydtu7W61LFtzzuPTabwG-p6hvUpNPVpeNTj3kwGpwe8eWHWEVRvw7xQde_xVMTgsYLg2Z_GDFXGe3KlLHoPQuVwXm8Di_w9pz4RfHcZsfViEqYqUjj4StKX6hQC-a0eqZE357Igwg14GUJTidZb-yehAzjfYra0CVzRmBccYS2NYLv-E1Z79yarHsqwD0SBUjjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۶ شب حضور دشمن‌شکن و وحدت‌آفرین گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452336" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d6c3a191.mp4?token=kxj8dJk2EgwNvlHaP8VIwtj61iNgKcL9gf9wW7BNckeDmH88xSA3iv_qMJ0Sww54EEYl8luhhY8tcXky3vYXm4biOV88fR91yT8IvA5VLnJM8UsdjdVLDBHdQ8jRb0-1WWTxTkH_Orzg_eTG1M4MJ9VLBpPe-UPvoFRbkoD-PBczcU3GpZa5p7bQ1fHujTaxMP-Z0y4KcgyhtxQpr0WIlp21sI1qq3xIqAXwK2WXLviiMY_KK1WcfnaYmqQ-PtHMGS-Ssm44NDAy24RMEkhmOYHWJLnFm4Zac6NDTql1eVyxgZMfYRMitSHjqwsH5VkBF_HZAfBpDliwz-g7lttdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d6c3a191.mp4?token=kxj8dJk2EgwNvlHaP8VIwtj61iNgKcL9gf9wW7BNckeDmH88xSA3iv_qMJ0Sww54EEYl8luhhY8tcXky3vYXm4biOV88fR91yT8IvA5VLnJM8UsdjdVLDBHdQ8jRb0-1WWTxTkH_Orzg_eTG1M4MJ9VLBpPe-UPvoFRbkoD-PBczcU3GpZa5p7bQ1fHujTaxMP-Z0y4KcgyhtxQpr0WIlp21sI1qq3xIqAXwK2WXLviiMY_KK1WcfnaYmqQ-PtHMGS-Ssm44NDAy24RMEkhmOYHWJLnFm4Zac6NDTql1eVyxgZMfYRMitSHjqwsH5VkBF_HZAfBpDliwz-g7lttdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکبر عبدی درگذشت
🔹
اکبر عبدی بازیگر سینما تئاتر و تلویزیون بعد از تحمل یک دوره بیماری درگذشت و مسعود ده نمکی در گفتگو با فارس این خبر را تایید کرد.  @Farsnart</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452335" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=bHkiqkgVmmNzz8QDp0Z-aTqXnMLNF0Y4Y8Eqquajj1yM_1qD1PuDeIA-x6Dm4BjPmnev6E2EAxE5KAJI8mBxSh1LfsOU5dRCqGA8X21U0UVO_bNCT6fqDG1Z_dVN_DRKUoHyrwulV1-hGP8d0G13YtlO-wvW8GQXm2nSINE0oiASE9DWuKDTYPabcSkep6YpYBAXb0rcs577EZHBxcHd45OVU2MCdyqzvuibKKuH--ljauFd13zZ9CqCHpv_6bTKkMzpK74VAZ005Pc6HdVwUbCdurQOcbyzIGAFPWPgHfNOZkufFRIGWhmsylafawruliP9m4Keje3KM7KcvD6dXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=bHkiqkgVmmNzz8QDp0Z-aTqXnMLNF0Y4Y8Eqquajj1yM_1qD1PuDeIA-x6Dm4BjPmnev6E2EAxE5KAJI8mBxSh1LfsOU5dRCqGA8X21U0UVO_bNCT6fqDG1Z_dVN_DRKUoHyrwulV1-hGP8d0G13YtlO-wvW8GQXm2nSINE0oiASE9DWuKDTYPabcSkep6YpYBAXb0rcs577EZHBxcHd45OVU2MCdyqzvuibKKuH--ljauFd13zZ9CqCHpv_6bTKkMzpK74VAZ005Pc6HdVwUbCdurQOcbyzIGAFPWPgHfNOZkufFRIGWhmsylafawruliP9m4Keje3KM7KcvD6dXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
ماجرای احوالپرسی امام شهید از مرحوم اکبر عبدی
@rahbari_plus</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452334" target="_blank">📅 22:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام آگاه: عصر امروز ارتش آمریکا با پرتاب ۲ ‌موشک یک تانکر ال‌پی‌جی را هدف قرار داد
🔹
به گفتۀ این منبع، این کشتی از سمت دریای عمان قصد ورود به منطقه را داشت و نیروهای تروریستی آمریکا تانکر را به تصور آنکه قصد انتقال گاز ایران را داشته، مورد اصابت قرار دادند.
🔹
این منبع تشریح کرد ۲ تن از خدمه این تانکر ال‎پی‎جی در پی حمله نیروهای آمریکایی کشته شدند و کشتی بر اثر خسارت در موتورخانه آن متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452333" target="_blank">📅 22:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksidP7iDz5Um-SB7s3_4hyIJL4QiFBJrEWL35fjJYLgGhRaeXSnuIXjl_SNvg7c5NfAsCYta6UE73mzxw41dlf1XK5MymqEb1NC2K0Wlw_CSt4Hf034Not4IJCG9DBFKsHi_WS7zfm2fTYUNChyjsGfYr25Jy0fEcdRi2gqW2lf96p1IXFqtZyzKCVIfCG0Xkbkw8wH-wP-36ggkdwJmxpUqsq_UJE1I4saRMX9tXjVdP2fW927g39bOX0gL9uhKfwZnSzwQXKLofejWmLjoFCGO7LIzg8IMW8E5Ye_nAuUfjVIBjSnTo6egzyFCl5pqXaOWKFhNfIKiCBD4qMVlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیین یادبود شهید رهبر انقلاب ویژۀ اهالی رسانه
◾️
یکشنبه؛ ساعت ۱۷:۳۰ الی ۱۹
◾️
تهران؛ مجتمع فرهنگی هنری سرچشمه
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452332" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع عربی از وقوع چند انفجار در شمال کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452331" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220a7c89c3.mp4?token=uhavjfPrIQq_unwP-eFSvWdGfoOzpShTJkaoYyycY4DZ2yjyCN_WfwSJkJrrK-NgfqiPtIzG4nsLGEwPsAwDBmUJ4_uMX2e49y8pzOFepPvA2-WTxttzjmUY8jxZ7fKO5LuEtmkn6m67ChhnyG02NTS-kfpjKQGLVTCmJxa7L1VoJWb53Vd7fQW9M2bwSowXtSgOaTmjNeEB4L3UPqP5jEqd33_sv-qgzvXra1t9AxuYXBWLHQARceqZ2kFTC6lIhORDb4Zzy5CEH8WMTs4ke6kHw4PGac9zUwvJqvmZVf0MqWmwR6-umqVKRwsVBtszDj2zNuFfHDTuuJKUK-HQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220a7c89c3.mp4?token=uhavjfPrIQq_unwP-eFSvWdGfoOzpShTJkaoYyycY4DZ2yjyCN_WfwSJkJrrK-NgfqiPtIzG4nsLGEwPsAwDBmUJ4_uMX2e49y8pzOFepPvA2-WTxttzjmUY8jxZ7fKO5LuEtmkn6m67ChhnyG02NTS-kfpjKQGLVTCmJxa7L1VoJWb53Vd7fQW9M2bwSowXtSgOaTmjNeEB4L3UPqP5jEqd33_sv-qgzvXra1t9AxuYXBWLHQARceqZ2kFTC6lIhORDb4Zzy5CEH8WMTs4ke6kHw4PGac9zUwvJqvmZVf0MqWmwR6-umqVKRwsVBtszDj2zNuFfHDTuuJKUK-HQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون تجمعات شبانۀ مردمی امشب نیز در رگ‌های ایران جاری است
🔹
قابی از حضور پرشور مردم در شب ۱۴۶  تجمعات  مردمی.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452330" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452329">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4f191934.mp4?token=VByzh0sysFKfvE3zVWB7aRZckJQHN7UJqQCe1z5FRvgQla7H8TPwjzjNXXKKy8l_qYWBr0oKdiy9jy00AboNitCjZd3fPj6zq6S_tDLsoYAb6HN_SsVfCxBNOLgry0R3aFWj_D5QgPpHpZNiKhl6efIga_gcs1HmE5gQ6AohbB_a0sFCZzSitqdqh-OOYKKBUurq0r2kavsHFyFhXxKqxEo5xePdN3qwL4rxLIgXduIaWAbNiKY_DZzOKY4x21MgVRdOQlq8VWWntJRzwT5Xd6CJNp2TEkJvozIbckAgmqNssurWm1MzSqUQe_ftHfW1gyyLVzlK6Kn1y1QcskDCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4f191934.mp4?token=VByzh0sysFKfvE3zVWB7aRZckJQHN7UJqQCe1z5FRvgQla7H8TPwjzjNXXKKy8l_qYWBr0oKdiy9jy00AboNitCjZd3fPj6zq6S_tDLsoYAb6HN_SsVfCxBNOLgry0R3aFWj_D5QgPpHpZNiKhl6efIga_gcs1HmE5gQ6AohbB_a0sFCZzSitqdqh-OOYKKBUurq0r2kavsHFyFhXxKqxEo5xePdN3qwL4rxLIgXduIaWAbNiKY_DZzOKY4x21MgVRdOQlq8VWWntJRzwT5Xd6CJNp2TEkJvozIbckAgmqNssurWm1MzSqUQe_ftHfW1gyyLVzlK6Kn1y1QcskDCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ کرایه مسیرهای اربعین از مرزهای ایران تا عراق  مرز مهران تا نجف
🔹
سواری بین ۲۰ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۸ هزاردینار و اتوبوس ۱۰ تا ۱۳ هزار دینار  مرز مهران تا کربلا
🔹
سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۳ تا ۱۵ هزار دینار و اتوبوس ۸ تا ۱۲ هزار دینار  مرز شلمچه…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452329" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
دادگاه رسیدگی به اتهامات صادق ساعدی‌نیا برگزار شد
🔹
جلسه رسیدگی به اتهامات صادق ساعدی‌نیا مدیرعامل شرکت صنعت غذایی و کافه‌های زنجیره‌ای «ساعدی‌نیا» از متهمان کودتای آمریکایی-صهیونیستی دی‌ماه ۱۴۰۴ در دادگاه انقلاب قم با حضور رئیس و مستشاران دادگاه، نماینده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452328" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">✨
خدمت به زائر، افتخاری که با کلام نمی‌توان توصیف کرد...
⬅️
کارکنان بانک شهر با اعزام به مرز مهران، در موکب این بانک آماده خدمت‌رسانی شبانه روزی به زائران اربعین حسینی هستند.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452327" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RcBMmmKhG4g9d4n2kLB1SB_UhSLf4WNgluqmhKEESr_Hbf3i9L9wznXGDpiF9cUJhggVS-CRv7OL6GwSnXfeh-r6C8CCtYzZUiA7iYY-AhOb2FHeRnUOSaHM_HczpYWMbfyHFE4s9nhvB_QNQZTzyuwzOXYLcgnr8gfamf6CXkuf_SZFPzysBrEayU5MhMHq480q84oCg0xaBBrtpdmDxNMQMq5BkENPDsgi6FQWDbZ4GndqknMxEcMwkqvgCl79_4fmDcDiAWPmVCxhZDbD8QY3XxTkXZo3426EHmH85v2ag8OdKC438cPcpbpc8_gmLpdQb5ChjgZxB6ipxigF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
📌
جهش سودآوری، تقویت سرمایه و تثبیت جایگاه ارزی بانک تجارت در سال ۱۴۰۴
✅
مدیرعامل بانک تجارت در مجمع عمومی عادی سالیانه این بانک، با ارائه گزارش عملکرد سال ۱۴۰۴ از رشد قابل توجه سودآوری، توسعه فروش محصولات نو، تقویت توان سرمایه‌ای، گسترش فعالیت‌های ارزی، بهبود شاخص‌های مالی و پیشرفت برنامه‌های تحول دیجیتال خبر داد؛ عملکردی که بیانگر تداوم مسیر اصلاح ساختاری و تثبیت جایگاه این بانک در شبکه بانکی کشور است.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452326" target="_blank">📅 21:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452325">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452325" target="_blank">📅 21:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452324">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc6383dad.mp4?token=bJCvUM7mwz52s5v7brj053iI2-Y6ewPMgMLDGF483hLkjQVdHhGXQZvZgqRgUj14JjEN8LiuesihUiabJbmTuzeLr2aqi6q3ccfRVZKe5jumkGYfep3fcdAlMj5FbxXQqm8G3hpFeIKEo2ra8enuDiAHT_5PkY4zYfY-oOsAr7v3fZCggyNx7sTpA8ALqt0wUdq7vhVq2qRuEXNPpu0qDJ2LSQt8v3GZlo0RxynxEUBhkEL00GiJsJWYMJ-44RoeRJ2QSx4vtSQGgR3MtqefVYBLzW8pPS-6twHctokHXt5IRx3gIe-rZUy4yjwQQzhL7d1bbBVLMhC0OlkwFowXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc6383dad.mp4?token=bJCvUM7mwz52s5v7brj053iI2-Y6ewPMgMLDGF483hLkjQVdHhGXQZvZgqRgUj14JjEN8LiuesihUiabJbmTuzeLr2aqi6q3ccfRVZKe5jumkGYfep3fcdAlMj5FbxXQqm8G3hpFeIKEo2ra8enuDiAHT_5PkY4zYfY-oOsAr7v3fZCggyNx7sTpA8ALqt0wUdq7vhVq2qRuEXNPpu0qDJ2LSQt8v3GZlo0RxynxEUBhkEL00GiJsJWYMJ-44RoeRJ2QSx4vtSQGgR3MtqefVYBLzW8pPS-6twHctokHXt5IRx3gIe-rZUy4yjwQQzhL7d1bbBVLMhC0OlkwFowXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری امشب مردم بجنورد در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452324" target="_blank">📅 21:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452323">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0aR98aLeQc2IlKwkGg7gvyQRlh-KtOC9M5thnIuYZv_pGmo2lSPIGZ8zfWHDlaUipgat0rKf-8O1DzkTvqBvPY4PbTb_kqZx09sJoKEbhscRaIjyCehhsnqX_JF1lNx_eBpwtpp0hTQlqcypCPaQyRAgtd1rvRMEIQCSzIU12TzRStwzQT3nnVlqNFtgWtHSqNp7O-48CEzKOX6lH7rNE-yrAOqhLX1eB7tFRnazIJSQPeOOgCdoldDo2EXa1caGmcm8dthlHe7Plybv9qeHlva2ijfT7_Nh1HoN-hBTHCDRCkaRZR2dJfmsEJyoQaCbveve1qpdDTMb-FtnkKkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان برای عبور از باب‌المندب دست‎به‌دامن عمان شد
🔹
روزنامه الاخبار: پس از هدف قرارگرفتن دو نفتکش سعودی در دریای سرخ، عربستان بار دیگر به دنبال میانجی‌گری عمان است و یک هیأت را برای مهار تشدید تنش با صنعا به مسقط اعزام کرده است.
🔸
منابع وابسته به ناوبری…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452323" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e3acbc7.mp4?token=vfqTeYns2tYLL73WNoPWx0nh1-lfOKLRv3YNEG_A4aiAMtBokXGkWUNAxHhy0yZ7ChbCzekf_YOwj1qvAaVrWYo_l2YwgqOIE8sAE6n-niBMmGrpXeEfPYPzwwxxh17Sr2dzfw-pXSq8qb4bGMDxFvGrK2lS_699Xb2jcgFHGC6h4MCFHx3c08OSvaQaI6iO3VzNiiogS2uT1Z8lTxqv3cnobHVR0j4WYi1mpQ_J5Wpu72fMiVcxhoodjaLgOtTzkI-avEJz7AoPjJiZIWzFao1bevlUPTuZPY-tr9WYv8upM4PS1ufTzf0rhbdVcv8JHzj7A6rGRg7tMCB0lVCB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e3acbc7.mp4?token=vfqTeYns2tYLL73WNoPWx0nh1-lfOKLRv3YNEG_A4aiAMtBokXGkWUNAxHhy0yZ7ChbCzekf_YOwj1qvAaVrWYo_l2YwgqOIE8sAE6n-niBMmGrpXeEfPYPzwwxxh17Sr2dzfw-pXSq8qb4bGMDxFvGrK2lS_699Xb2jcgFHGC6h4MCFHx3c08OSvaQaI6iO3VzNiiogS2uT1Z8lTxqv3cnobHVR0j4WYi1mpQ_J5Wpu72fMiVcxhoodjaLgOtTzkI-avEJz7AoPjJiZIWzFao1bevlUPTuZPY-tr9WYv8upM4PS1ufTzf0rhbdVcv8JHzj7A6rGRg7tMCB0lVCB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارشی از کشتی‌های متوقف‌شده در تنگۀ هرمز با اعمال ارادۀ ایران در خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452322" target="_blank">📅 21:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452321">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx1_0pmUPP68vEAT4TwHooA5yngCbxmJtvY8i8UEhwNwRgtVDeoGR7DwXqOvjmuiIhCtGvFZZW-SZ4NcLXGO_HdlKO4UBYE4uhnftHICtgQBimH_3m40JZS1MJ6D1Na8IVxRtdjAz74zN69yzx2OXZCgo_ATG7jhEqrZTilAnkmD0SSruYX7-rl_ghm4GKGCK-seh1pV9RPhcftkDNm-Zb1G6RYkLE0kRVGgsME116vNgCor75RnqImOcn47OlK-sBIW0rBHIZBS0lkjhuCFw9ZP-jc7IrGQuEgmoDWIfnif3w5UyCUsX-2bIjCzSBo46vUCMeHTqU2TL3gBUdQNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به بلغارستان هشدار داد
🔹
سخنگوی وزارت خارجه در واکنش به گزارش‌ها دربارۀ بررسی درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» بلغارستان گفت: «هرگونه همکاری در حملات علیه ایران، از منظر حقوق بین‌الملل به‌منزلۀ همدستی در تجاوز…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452321" target="_blank">📅 21:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452320">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM27JgOHW1m7IyiBcSVVhNKpRlhdzHFYCUexfry6YuFbO-jHemhR6y7pByIzgwfeY26XiNwGil2Wo6eZQOMUGkdS5OT8BfRb0W_p-KYw3-HaKngThbdPnBk7GcDgyBjOUMadmsNxZ4uptNCkXXEq-GYRm9CulivhUnWpb0BQ4pzew-ei1C-kR32pnHUKgaD3r7Erw3cc4AMM-j35toYVIuS5COKToImJvO28hDaSqrqRIxwsTQYY_oc342VUADp6Dze4QNI-Rv5Ac85H_evhbgefgxovh5r2XHVatO6WzfMBmaW3BFbU8lSqp0vT1LtS6Je_nCyj7G1Jg1pY27bt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی درگذشت
🔹
اکبر عبدی بازیگر سینما تئاتر و تلویزیون بعد از تحمل یک دوره بیماری درگذشت و مسعود ده نمکی در گفتگو با فارس این خبر را تایید کرد.
@Farsnart</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452320" target="_blank">📅 20:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lr9vqlaGs1MT6UdR9OutX9WiS_Z2HMnZrrsv4CGZjzAOpYydeMmsSIcaCgG6nYB2LaKYlMZxysO-pTvGasIfmdk1-fXnrIY40jqkphG6jJfS4cklM6TQAsTCrvV9IjHm3AhXlBFvDFiPnor9r4fu0-ey2n5Fl00Jm-HtuJdfSIqmbUvN_sbztQPfd-wqQ0leiYKqJncDxOSPw3sJEM-VCIguR8PeGKeUhdn-srPH6bujKFCucoPR2DTpQCsEyuOiJ9n2VmOsDEV6QC88ofzaK6VNDXhw1STYtp9J9ZjGaofVFlhymAzSBAEX1CN2cvbj-0SHa8fm30FzXuIzCdNWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cepQP5POj5Z0T7V4pbNheqKDQqs_JtAglyS3qG9wWRVbeffaDWWekuWzs80uJw0UxSanLrmc92IhPMyjatilaTNIMWSpX3kXilObo1_t7SZRpaYH8QXDFwaRbxkrGKT_grfZvOCiu9vvop4wpnzGU9GJAH4bn6idxxdH-7pzVoIof_C2RU9AkuLV9Huc7YPIObUFia_t3Ld2kW4uC4YU-gexSz-kZUxxUr9M7BX4PGinXlSdx2MIkJSmwg91B4NZGQVRVzgCnXaDkkwix5tlRhtFuC6Tz8IwXH48VL3JKryz8bYJlTpQZcZ0DZlEeCoTKsUuQgwDdcQmYtATRVcnEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آمریکا همه هواپیماهای نظامی خود را از العدید تخلیه کرد
🔹
تصاویر ماهواره‌ای شرکت سنتینل-۲ که امروز منتشر شده است نشان می‌دهد که آمریکا پایگاه نظامی خود در العدید قطر را به طور کامل تخلیه کرده است.
🔹
براساس اطلاعات داده‌های منابع باز (OSINT)، در تاریخ ۱۷ جولای…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452318" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f83a96df7.mp4?token=HTPIDcAx1HnyhdWSPyEyU17Sbi_AsuN1uhV07xTpiPJTA5NjgjNuzD7Vi0faryR_Zn_dvxdrhNa2oTM-GGM0ojcbMLnYhO5CwDZVVGOM0sfGgJWO3AF1IcAYQJcgv0q6dhZXsD8QMx9JjZGsxK9dDym4z8irCSuYDMwuMAq0VUqDtiZOUs8XbBjUQKZSquL4A56qLyuP70C3SSXQaZigg2Kk-cug-__GXQUVLbSZH5tUDAveZWjkUpIJbfJRbpcGZDpiKKbaVUI8qQ8N8LUfN23O91EtGv2J6nPwjqa_Julw7ZDcBkr3CO6Fs86jMhV6c0roMe2Z7Vc7aLWj_FyQMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f83a96df7.mp4?token=HTPIDcAx1HnyhdWSPyEyU17Sbi_AsuN1uhV07xTpiPJTA5NjgjNuzD7Vi0faryR_Zn_dvxdrhNa2oTM-GGM0ojcbMLnYhO5CwDZVVGOM0sfGgJWO3AF1IcAYQJcgv0q6dhZXsD8QMx9JjZGsxK9dDym4z8irCSuYDMwuMAq0VUqDtiZOUs8XbBjUQKZSquL4A56qLyuP70C3SSXQaZigg2Kk-cug-__GXQUVLbSZH5tUDAveZWjkUpIJbfJRbpcGZDpiKKbaVUI8qQ8N8LUfN23O91EtGv2J6nPwjqa_Julw7ZDcBkr3CO6Fs86jMhV6c0roMe2Z7Vc7aLWj_FyQMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ستاد اربعین: حدود ۵۰ درصد مسیر نجف به کربلا مجهز به سایبان شده است
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452317" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUx30DchPSv225zJ8QmtyUr4pxpsMRb39PfahQ9ZAztN6xiZ5rTRjU44HxujTg5cebjXoFSioX3E5O5QWHT0wxQS729eu575WXEfqhrlrZlCT4SUKSlnCWsePl5MkNMElFO9X54DSr-vzSXT_QCE958_22wWKrmIv40dS56vXVjfjh8vQexg7EZVEwDYZ5lGHnMU1fRC4KMGGShia1dzk4gk4FpZHCo3Jal7tSnHcagfJI3PgAcvuGGl9Q-voEv6VCkFpgQA7RmJ-P3KhTJKstimA4Zastv8996iIjGbilLtjrclo7_l7OGU_7QPYeWyv2z-G-1-8kJ3syCdt2Uiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلگر انگلیسی: ایرانی‌ها همچنان می‌توانند تنگهٔ هرمز را برای آمریکا خطرناک نگه‌دارند
🔹
مایک کلارک: آمریکا در تلاش است تا توانایی ایران را برای شلیک موشک‌های بالستیک و کروز به سمت کشتی‌ها در تنگهٔ هرمز مهار کند، اما این کار «بسیار دشوار» است.
🔹
بیشتر پرتابگرهای موشک‌های بالستیک، متحرک و پرتابل هستند و علاوه بر آن، موقعیت جغرافیایی ایران نیز چالش دیگری بر سر راه حملات آمریکا ایجاد می‌کند.
🔹
یک خودرو از مخفیگاه خود بیرون می‌آید، پهپادهایش را شلیک می‌کند و دوباره حرکت کرده و دور می‌شود.
🔹
آمریکا می‌تواند به هدف‌قراردادن محل نگهداری مهمات ایران ادامه دهد، اما این اقدام معادلات بنیادی را تغییر نمی‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452316" target="_blank">📅 20:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درخواست متحدان منطقه‌ای آمریکا: حملات سنگین ایران، توقف جنگ را ضروری کرده است
🔹
نماینده یکی از کشورهای هم‌پیمان آمریکا در منطقه‌ طی گفت‌وگویی با شبکه «سی‌بی‌اس» تأکید کرد که توقف فوری درگیری‌ها به یک ضرورت تبدیل شده است؛ موضوعی که بیش از هر چیز تحت تأثیر شدت…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452315" target="_blank">📅 20:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452308">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVNklecA0hEfERSk9Tv-efaTUDP_6en3pKItB5hdF5IZnJV0102Vv8tG4UvQ4zYeKOLX-GC77qIdkg4iZCwb7OIBdh-WgbMfyJUhyj7v_PkopebLm6wTLsz16oVepB7OWiksK_u0enPhIm7F0FLtj7MdSoAfottay9ljVsvdkOe2DjFCDVjbrJHxClSZ6Ng-HDECxdTXTIgynMvT3slIp9EKovOHtAXi7PbqBfWtBXmku57rgKY2TiGEvs9oGzluNYjBNoErF4E5E2dgG_0X8fGjal7jAlshlgLGr-9LwrzNuXqdznRpwEox90JeWcRPJR--zb1zPzsrARlj3hQd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-zulgehuTAKHH5wcKeqbc_xiU8k7vYmF-8Tkodw6QVvZWpuS1rhL5YzcDZ6PO9cR1DnLvIBT0irMDtFDEjYevQLZMfwQF3UyQVIKx53pK-YkuEonVzf9UZ_3hdh6V-8G4vX0bDy_TWdxrMpRPOVZZmnC4lMr4s-9pxNX5C_T8dXEVfCdXcoc_lMAgVSnJC75z9L5rHYNNN0puwGVhcGtlYqxGADCk6H3o2GAyKljxNIrx1aXE8Tc7MUNayXAT-Rx79gl3P_WzIEVBUv_tcqd_CT5VEITqy8_d3BuQphwNyEmiixnLNecBSRFXBN3o7DfHVce8VHlFauqNM5MJm9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up9bouDXCE4alcGrnaZIZnE3V4RAECecPi6a2tNO36oC9BpyUonRcSRZr909HCUVSs7PWy0QyrRSGeUaU5Qj6nx14lWng01ucTdV68QR-c5c5O3tNACm0BAB8cSHV31xADuT-RDa7QrvF8YfTqjElCGIgJXfLC72WNBiIc24r8Zfi9flqxM7iWSQ6LgQX4-6t2bdDz5UtylcgshEd2Tqq9iVcLMXcwb7UAC9HLc8r8qf1K3fTrYnXYKWCYQCKTCio4RmfkCE08Fc4eXv0vJx3XlcwTcVZIvX2q1M2X75QfTFIuFauKUQoqNcoSQH277YhHQyO7U5xaLaGlvB_paz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYR6hP-MY_y1xIIGLTLTa0dVasGmTjf9UDNhn-n1JcIPzvWbITHFcCkes8JMrDdTYlxlNBE-KuH4sz6cZAe8cdazNY9XNCYLSsADEHUz4ivZ3-nvhp3W2cIN6mF0REOvE5aigLtyxca_neGn8A4snM58YxPrKLxQXjvpo55DpwfbsafZNKx0PrvmBxMZLnS99kDpkr7pBWQ3uKI_zMMYJLxYv7Fgx9WXQWnLq869PqiaApXfzYGWIig2nTTJ2oGoRqf5CeCCSom9lQmxSHV-k-iZ6OVqjt5D4fA6q1rGenbPpNHPgvoCqOTUmuixcPWKquB8igR3E5Rbx3z2uAaUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9wh_p63dasmjxw9QdtSATesgMSW2IopEIvr5sHgv5cskXl4QrvYkT4j2_QU74z38-LCjue_VKOGO5mFt5Ls32Rk-gU88Ih9b7gCl4xhWzjevVqha1Ds7XrEVy-bLuBCCU94QH1iO5vMMl8Q9STzdWQpfk6MC10IuU2ZZ0OXn7MKxc_d4ZsIjDqqbeIi5XkwZV-nShvlf8--_F0jcBe8ogpaZhLc_jFTOHjrlocrCsC6gQ1HIF6rjq-ZozVyXEG5kxmmhJAF8gma9YvPImkLqEJYE5nTY5yffqG7bPW8yynr9_H1IQqAU-jn7T_iqqj_1vMFd1ndP8x9oTjzYfB_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cugUFmygwvE1QYwugn3Q9PhP93Ao3NRLvExpKgfHeZRCc8Hh22230wTa-cYtlE5ghsTTbHwx0xejKijJplJFoqL7OXTwnpqC52b6ooCYBu5v10P9aXi_3YVjTinbYe8RvLtyHH1Okp37jWDblqK_EciLR5NMXUv3G3jANfhwAZiRAaYtxS645ppbUPa7K3pgd8PJfSxQ3bb3VUCD39WUd96e91K1cGo9oBtalIbIifssdbKK7p7K5Sk-bACJTVAKxlmIkJsUNcypVkgBZ6p5QRAsWtg7sGkgcAmNfFZX7JX7DRsC1bnow-OACeQTPxB4HwOb7SAB3yD8RP58yLbJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvSuyekwQqtvxRaQCUIfj705hphBHR_ja383DlkROJhtMTZlxqNu_MzHe6EMoKKU9dp9vMr9JEHKbiVz55jkYJ1F8ypVRkMEJLpwZUXxGV3xXU8EMkt14q2r5EhOHADodNELvIm_LF7kgCnOWl3h47Y17f2Vsbdpmov7C6qG-3aDwtYJAUj6xcJ5Q21oAcFSDQ78DN1BlPiLrgUdXZM1Kc94UV-BXzEZ6FzPcWO02nQWwNuFs3EgM00c98aG2f3vdauwlZ5lMLLR_B5CBmIWiMt0HDESkmINQ0theLC0qiYxVNA9gFQG7hs812rJ8bQDZPRe-azVDg4oxsB5jFlpJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت موکب‌ها در مرز شلمچۀ عراق به زائران
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452308" target="_blank">📅 20:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af77e674b3.mp4?token=d3o_FffAhW2INItzfBJUhTeagtfxVJ49bROfcqCmxhtvscGp0gIO16P8QRuEQQHqqCnMTH8hZYN6CE3X9achTLBWlJ-vM03N0V6Rik_brut-dCIaGGb3ldwizV-JFUVg33jnAy2Kfxs-Ig34jBpcLapL1ZCVLXqgeRpUCpofX2QRvAASxE-mujDFPT46pWFbt0QfhMP3LnNcbXzduNSfcmz6AsHPR77nAaddGPTL936PGpLUaD3euFlFAxeD89EyVsAwrazgl62omPZ3AwT3tx9U_FzwVT9EjInaRqsVNb5NxdSDeb9RQCd53FfvJ-ipj70DMeMSe5HR6_oxZfjuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af77e674b3.mp4?token=d3o_FffAhW2INItzfBJUhTeagtfxVJ49bROfcqCmxhtvscGp0gIO16P8QRuEQQHqqCnMTH8hZYN6CE3X9achTLBWlJ-vM03N0V6Rik_brut-dCIaGGb3ldwizV-JFUVg33jnAy2Kfxs-Ig34jBpcLapL1ZCVLXqgeRpUCpofX2QRvAASxE-mujDFPT46pWFbt0QfhMP3LnNcbXzduNSfcmz6AsHPR77nAaddGPTL936PGpLUaD3euFlFAxeD89EyVsAwrazgl62omPZ3AwT3tx9U_FzwVT9EjInaRqsVNb5NxdSDeb9RQCd53FfvJ-ipj70DMeMSe5HR6_oxZfjuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند
🔹️
فرزندان غیرتمند شما در نیروی هوافضای سپاه در ادامه عملیات تنبیهی خود، در موج ۲۷ عملیات نصر۲…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452307" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
منابع عربی: پایگاه آمریکایی علی السالم در کویت مورد اصابت یک پهپاد قرارگرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452306" target="_blank">📅 20:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452305">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
منابع عربی: مقر گروهک‌های ‌تجزیه‌طلب در اربیل عراق هدف چند حملۀ هوایی قرار گفت.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452305" target="_blank">📅 20:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJaKkpSKSUZpBiDyeknszgLyuPcm-xHknOJcQnq2Cj6VyK0pDK-oa402-lQ3L5EF4wpjHnZUHCGJ5iVEi0fWg-5fqbLT3SADt8qcibyGTq3AM5IfIOGCrCnmVsZ00hhYtzd3_74xm69OLMr_GV-mGZpFNdI8kc5zY3H78DCaaQTHnVajo9uln6r7Eeos0iDIHibi3Vf6at2Tr-6AHtBbsEfjRoxZ5fX153UeCk4uNqQkkoWRKeECxhHe7DgbyTx9M2yvPmAOhO40UXVlkoLQhKU_OBgtcW9zT4z7SvBN0cNZgsByMMyBRXgTvnsGakpgU-TBpNAls-bE8pIzgRAtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ کرایه مسیرهای اربعین از مرزهای ایران تا عراق
مرز مهران تا نجف
🔹
سواری بین ۲۰ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۸ هزاردینار و اتوبوس ۱۰ تا ۱۳ هزار دینار
مرز مهران تا کربلا
🔹
سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۳ تا ۱۵ هزار دینار و اتوبوس ۸ تا ۱۲ هزار دینار
مرز شلمچه تا نجف
🔸
سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۷ هزار دینار و اتوبوس ۱۰ تا ۱۳ هزار دینار
مرز شلمچه تا کربلا
🔸
سواری ۲۵ تا ۳۵ هزار دینار، ون ۲۲ تا ۲۵ هزار دینار و اتوبوس ۱۸ تا ۲۰ هزار دینار
مرز خسروی تا نجف
🔹
سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۵ تا ۲۰ هزار دینار و اتوبوس ۱۲ تا ۱۶ هزار دینار
مرز خسروی تا کربلا
🔹
سواری ۲۲ تا ۲۸ هزار دینار، ون ۱۵ تا ۱۸ هزار دینار و اتوبوس ۱۰ تا ۱۵ هزار دینار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452304" target="_blank">📅 20:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452303">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayZGGf2vW_qeKBpsBchhThFK2vBbHnLi-CkmhcK8CktMnsEumy8e8ik27bA3gKc5RPvHn0eY6RCYAu2zrnNYTa3-YrR9ECY8JisXYQp6hHz1KQgFwiR8hi4H9cBeZx-T292eaBf4s7Zsk8x9I92ymgPJZYK9KdhT73Nwcr7zl_YxztHXW9pYgxsLprgrf_jhWrurZkKej6vR5B2unG28ik3qAG7pNjjGImLuz3N0StDlSgY9kp-6AUEjJHklUQOC8uehqcCeGhhri5JFCS6iabK6PD_dNahoCqmAUklBy8kkC4hpZfIAJUi9dXrY-Uhwj0NPNoYlFMXEHtCs2AOwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیویورک‌تایمز: آمریکا هدف‌قرارگرفتن نظامیانش در اردن را پنهان کرده بود
🔹
چند مقام آمریکایی به شرط عدم افشای نام به‌ نیویورک‌تایمز گفتند پنتاگون خبر ۳ حملهٔ هفتهٔ گذشته ایران در اردن را که منجر به مجروح‌شدن ده‌ها نظامی آمریکایی و آسیب به چند فروند بالگرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452303" target="_blank">📅 19:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452302">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXQ9yT1GPlf_aAMXAZq1evzGaghJH1JgZ_aT9Wpl0QjbiX-e3U_ROtnBxvFM4JrATLuz3XeaAlxIv2cvB1RKOxk7nAfmAnpmnoPUhX-3Q0dNs2vnsnEQnXKq1gOl_wgKYuoPoDOTb87-jSSsDp5ZrHz7cq7tCqkBcbuq_HfO__mxD-YwxWfsw6VxHJO2Pc9Qxz4roDMu5kZtoO6OswaI5RDZL9ZbJ0SSAopTzcUoyj7E7eXxPJb6QPSrFQ_UNzFOR3eqHbzy3cjYIc9Y3_NqMwH4PbgtUDmeMMcM1p-r3Z7fwDqM6IPam-y7lfH7_oJgKpXO6UiGDQF2G4t_r6JrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه خاتم الانبیا: در ازای شهادت هر یک از شهروندان ایران یک نیروی آمریکایی به درک واصل خواهد شد
🔹
سرلشکر عبداللهی: قاعده‌ای را که پیش از این هم عملیاتی‌بودن آن را به دشمن ثابت کرده بودیم از این لحظهٔ معادله قطعی و ابلاغ‌شدهٔ میدان نبرد می‌دانیم: در ازای به شهادت رساندن هر یک از شهروندان سربلند ایران اسلامی، یک نیروی آمریکایی به درک واصل خواهد شد. بلیت‌‌های رایگان و مستقیم به جهنم برایتان تدارک دیده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452302" target="_blank">📅 19:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452301">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع عربی از فعال شدن آژیرهای خطر در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452301" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452300">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWxd12gxX76xfV0MDDWXVGhV9HYt2sbiWRQUniCYlgZ45JxT4Q5VNCYL5ohMn5pJebx7Hdoes2-gflRkvQY8XLbY3PwJEZqGYo5bCHcQ03Vzj9xoQt5JEmsVb5c37WZZ-LbDv0jjp0r9NmgUrPMS479mPV1cccBmJUccIQ6cbWP8z13ipnIlryMhx95Is0hwjLPo9j69M04ykNVCp2mJnaC7jqXcWjvYCwrhHWR-oJEgfJGw2XAojx_8eTK8ZwR-gMLlH3WiBJK42TQELUU9X4qZKuskJc8I9w5qp_KzeNdgkfwhET4Rz183y16599PTEz9MKF7T0FsOlWu-Sras1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ۹ کشتی از باب‌المندب پس از محاصرۀ یمن
🔹
خبرگزاری فرانسه: بعد از اعلام محاصرۀ عربستان سعودی توسط یمن، ۹ کشتی مسیر عبوری خود از تنگۀ باب‌المندب را تغییر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452300" target="_blank">📅 19:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq2cjQfojwAyHBA9_C2lz-PlNRLB-FBNGwqm5_9kSJE-nAbg4TPSnLqv9dxy_M5dT54CicFtB11VjkL2jzNhOaAvYq6qjELScgLfbly7A2QPx2w7fIqC8JKlpb0fxJukxgttSmKBuV0omCCFOmQkdAZQxKQzzRW94lqlFzR9FNKeYWkzajDKSfN2lamtZRmW1KUA35eDbfS7gslyJ1zINpia3hqivEA8gyK6EByq00nMiIUnUxqHrUedSXgpdkF-0HkTGDFBMZ6EmEjFgp9Cmgu3xHHiD-8aSo85wYeBbqEAwzd4NEvCIiBFwFuXUvMiDHta60Fr_c8gkW_c6hlJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست متحدان منطقه‌ای آمریکا: حملات سنگین ایران، توقف جنگ را ضروری کرده است
🔹
نماینده یکی از کشورهای هم‌پیمان آمریکا در منطقه‌ طی گفت‌وگویی با شبکه «سی‌بی‌اس» تأکید کرد که توقف فوری درگیری‌ها به یک ضرورت تبدیل شده است؛ موضوعی که بیش از هر چیز تحت تأثیر شدت و حجم سنگین حملات ایران قرار دارد که کشورهای کویت و بحرین را به شدت زیر ضربه برده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452298" target="_blank">📅 19:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c401c1206c.mp4?token=QC79xy3x4Zze03mOF_1JpXMdo4r4U3RvEBdzo-ka3F-hwOq_9FVZujx26IeOlajYYhrvkvxc-inhT0whG_WFXYw2bY84O9D07_x5nirZhBOVJIiy_6edPx-fPtkG_M-P-IxFU0TsWmKrgmi4FxaiUaTrDGbl-1nV6gUYZBWGRLgqKPuKsujuQ4mIHITTSPRGb-gZ1TN7smuHduzM2h40PAtHXiwBar84oQDPNARamD5MLAYDEUx9mLe1VkT19dmDXqknPyLGoOSwd3XksSDxqmKjsKZaFwJz-KBM5ONR8L2M278tr9SWeKH2TE5tJhOtOZX1kZWlNsRoLuoyOz2maA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c401c1206c.mp4?token=QC79xy3x4Zze03mOF_1JpXMdo4r4U3RvEBdzo-ka3F-hwOq_9FVZujx26IeOlajYYhrvkvxc-inhT0whG_WFXYw2bY84O9D07_x5nirZhBOVJIiy_6edPx-fPtkG_M-P-IxFU0TsWmKrgmi4FxaiUaTrDGbl-1nV6gUYZBWGRLgqKPuKsujuQ4mIHITTSPRGb-gZ1TN7smuHduzM2h40PAtHXiwBar84oQDPNARamD5MLAYDEUx9mLe1VkT19dmDXqknPyLGoOSwd3XksSDxqmKjsKZaFwJz-KBM5ONR8L2M278tr9SWeKH2TE5tJhOtOZX1kZWlNsRoLuoyOz2maA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور موشک‌های ایران در تجمع مردمی محرم شهر
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452297" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJymJG4wd6L6YsuVCea31d6Nkp2D4QC5CBQP4Orvdbv6XEJL_cQmAN7THih_9BJ-lNxb5R_ErSakPc0929aIAzpl6vdWPPjGaCMjLgJBTV-9D0ZTFiRiHR_QsTjsC2SUM4eiqj0xdwvYi9cj8ebY-s6Hm5SgdxoYSxYwQ_TZXfrwVSWStFpPnA_Hn83a87TQyBoV_2ruucZPsvwLpGbZfJM51WTUliqGAHlyD34qqf7aKkoEGHo1qgTDSK2BFIuJmFGJ1gMJPZbtSbwk0FQXETHDMVbaGL6pkM__6Z1ef4vIP5tMwmtfT7QV4JWJxYZ3E2BuoMMtvzM9HSEyl9hHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: ذخایر موشک‌های پیشرفتهٔ آمریکا در جنگ با ایران رو به اتمام است
🔹
وب‌سایت شبکهٔ سی‌بی‌اس نوشت: مقامات نظامی و اطلاعاتی آمریکا خبر می‌دهند که مصرف بی‌رویه و بسیار سریع موشک‌های پدافندی و تسلیحات پیشرفته نقطه‌زن در خاورمیانه، دولت ترامپ را دچار تنش و اختلاف داخلی شدیدی کرده است.
🔹
این بحران، فرماندهان ارشد آمریکا را بر سر یک دو راهی سخت قرار داده است: آیا باید تمام ذخایر را در جنگ با ایران بسوزانند، یا بخشی از آن‌ها را برای بازدارندگی در برابر قدرت‌هایی مثل چین نگه دارند؟
🔹
به‌گفتهٔ این مقامات، آمریکا اصلا نمی‌تواند با سرعت فعلی به شلیک موشک‌های گران‌قیمت ادامه دهد. کارخانه‌های اسلحه‌سازی آمریکا قدرت این را ندارند که با این سرعت موشک بسازند و جای خالی موشک‌های شلیک‌شده توسط سنتکام را پر کنند.
🔹
از سوی دیگر، مصرف موشک‌های پدافندی برای مقابله با پهپادها و موشک‌های ایرانی در پایگاه‌های آمریکا در خلیج فارس بسیار بالا رفته است.
🔹
وزیر جنگ آمریکا، بحران کمبود ذخایر را انکار کرده و مدعی شده انبارها پر است، اما رفتار ارتش چیز دیگری نشان می‌دهد. ارتش آمریکا برای صرفه‌جویی، شلیک موشک‌های دوربردِ گران‌قیمت مثل تاماهاک و JASSM را محدود کرده و بیشتر از بمب‌های معمولی هدایت‌شونده مثل JDAM استفاده می‌کند.
🔹
وضعیت در بخش پدافند هوایی بسیار بحرانی‌تر است. مصرف موشک‌های سامانه‌های پاتریوت و «تاد» به حدی بالاست که پنتاگون مجبور شده موشک‌های ذخیره‌شده در منطقه اقیانوس آرام (که برای مهار چین و دفاع از تایوان بود) را به خاورمیانه منتقل کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452296" target="_blank">📅 19:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c88cf02f.mp4?token=XpxU5EXzxlCUCbPnaEmyF42NkwvGyAOwClXayMHuSV4DJXodfeyM65Y2S8_mtMdU5O8zbyRgtwR8wOOZmAJUeUyUuvoMbAUjiDWs043Lps0nbnPuBah9jaM08GM5AcdmvIvZEN2OSWiVLe8DjKSdhIzjuKWQu-bPUwBCThgfx5GedOd_Uzxy8c5UCJu61FVC3JvxPw0RkR4xS-jCPhHcSRR5xUcbCzcRpb33_ZhyqbipUQYRVunluJmQSZ845LYzps3E5xPPXJlzYzA0xvGODtb53VDVmGMzuQL7amABLvFbIcIn1hf41ucLOZKOI02nMHwbepYhE1PtXSWK-_A6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c88cf02f.mp4?token=XpxU5EXzxlCUCbPnaEmyF42NkwvGyAOwClXayMHuSV4DJXodfeyM65Y2S8_mtMdU5O8zbyRgtwR8wOOZmAJUeUyUuvoMbAUjiDWs043Lps0nbnPuBah9jaM08GM5AcdmvIvZEN2OSWiVLe8DjKSdhIzjuKWQu-bPUwBCThgfx5GedOd_Uzxy8c5UCJu61FVC3JvxPw0RkR4xS-jCPhHcSRR5xUcbCzcRpb33_ZhyqbipUQYRVunluJmQSZ845LYzps3E5xPPXJlzYzA0xvGODtb53VDVmGMzuQL7amABLvFbIcIn1hf41ucLOZKOI02nMHwbepYhE1PtXSWK-_A6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۳ رزمنده در حملهٔ هوایی به آبادان
🔹
در پی حملهٔ هوایی دشمن به شهرستان آبادان در روز دوشنبه ۲۲ تیرماه، شهیدان ایرج سردارپور، اصغر سردارپور، علی تاجبخش برای دفاع از کیان نظام مقدس جمهوری اسلامی ایران به فیض عظمای شهادت نائل آمدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452295" target="_blank">📅 18:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
آمریکا ۴ فرد و ۹ نهاد مرتبط با ایران را تحریم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452294" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InIKJp3uqTg2-5Y1b_RSQubWcMsfINYXeaBFe0e8dRI70mxiVO_rJi0rw3qxinPmEzwXMS7qGoyqj-cCpE2IGYU2Sf8friSuOAFfP5ZNB2YxuYPXFUN1bq-SrIyP-Xesc4cdrf1zpLsGXn45jTPGQU3iexvwPBqYKHYI7MU2APL7T5Xp5M3-EZ5FajZvGmeyx7NuRUpngkyLijPZtwo9feNphVxBPS38W4i4q2HNkkXdfphOIBBaKD1w3H1FW-G-vs8W4ff5VzGxzsEqHawEYHhthtVFjIaPQdM97unSSPraHFx3vB1PnsdluFKqPtgomzAErRr74naNAotxG3A9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: بسته‌شدن تنگهٔ هرمز ارزش سهام هواپیمایی‌های آمریکایی را پایین آورد
🔹
سهام شرکت‌هایی که هزینه‌های سوخت سنگینی دارند، تحت‌تأثیر نگرانی‌ها از بالا رفتن مخارج، دچار افت شدیدی شد.
🔹
ارزش سهام «امریکان ایرلاینز» ۸.۴ درصد سقوط کرد؛ آن هم درحالی‌که سود این شرکت در فصل بهار به‌مراتب بیشتر از پیش‌بینی تحلیل‌گران بود، اتفاقی که معمولاً باعث رشد قیمت سهام می‌شود.
🔹
سهام «ساوت‌وست ایرلاینز» نیز ۶.۲ درصد افت کرد، با وجود اینکه سود و درآمد آن بهتر از انتظارات تحلیل‌گران برآورد شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452293" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انهدام مهمات جنگی عمل نکرده در بهمئی استان کهگیلویه‌وبویراحمد
🔹
سپاه ناحیه بهمئی: صدای انفجارها در ساعات آینده، ناشی از عملیات کنترل‌شده انهدام مهمات عمل‌نکرده به‌جامانده از جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452292" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
آمریکا ۴ فرد و ۹ نهاد مرتبط با ایران را تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452291" target="_blank">📅 18:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0871f83bb.mp4?token=FK600S-KXqetnamtSVQc1cbtMRkgtN2hqQSEyFg690S0gfTxIVAqJVfwQ79WBPcPRNJMYr6MvXFxDPcd9NCpLphTr3hsBNohSj36PSTKtR2huEsFSiPcoLMYXI4ttSBfKExcnoDl6mrZKf-G4lNNWlNcxFDkfnbKOljnA54HFaQKYiMkGhqkufM137xE0YZnihkegJiclf6NLCZxotMdtggwJRns-jHlfKzg7S2uWNKEnAmWSWGJFZo-pqz3HBL2-XiaTVL0GKFFL7Fxx8r8A7SQrGOVRJ4QOgyIc3-ZrCzHenPzgpuDgPlhKPBPD1xpNclLsmO94fGiHEucvDD4uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0871f83bb.mp4?token=FK600S-KXqetnamtSVQc1cbtMRkgtN2hqQSEyFg690S0gfTxIVAqJVfwQ79WBPcPRNJMYr6MvXFxDPcd9NCpLphTr3hsBNohSj36PSTKtR2huEsFSiPcoLMYXI4ttSBfKExcnoDl6mrZKf-G4lNNWlNcxFDkfnbKOljnA54HFaQKYiMkGhqkufM137xE0YZnihkegJiclf6NLCZxotMdtggwJRns-jHlfKzg7S2uWNKEnAmWSWGJFZo-pqz3HBL2-XiaTVL0GKFFL7Fxx8r8A7SQrGOVRJ4QOgyIc3-ZrCzHenPzgpuDgPlhKPBPD1xpNclLsmO94fGiHEucvDD4uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ایران زیر بار قُلدری آمریکا نخواهد رفت؛ حفظ حقوق ایران در تنگۀ هرمز جزو اصول ماست
.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452290" target="_blank">📅 18:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz9di9J24PBe328lLUXxCiBiQhZvG-LWGvf97pLPBInDvKp-xxwEyVujeJOUCWUFh7y4cWbHnuh3lctMHyycDprvWI6O7T6e0VrCphUM91qShR5QC8pxm7AamWIac1dVEYqf9mCGcLs4ELxTKCFw3SLgPP0QL_tsPuTpY8xujM1P4HNGtxwInNDIgdL8LjAuofCAyWA8efob41Rq8Qi75oqNqjMLW448tcSqwnRvxr_yXiZDr40zDBxhClgPjPk_vbVASnbDhxo0R-NFKq6maVKJPlldNzI_4nd8Dp9k9nfCvRvDE8HZZYeD4bbtuHGdGooteI21X2oDlorfOY2ZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: توانایی مسدودکردن تنگهٔ هرمز اهرم فشار فوق‌العاده‌ای برای ایران است
🔹
توانایی ایران در مسدودکردن موثر تنگهٔ هرمز و در نتیجه ایجاد آشفتگی اقتصادی در سطحی فراتر از خاورمیانه قدرت چانه‌زنی و اهرم فشار فوق‌العاده‌ای در هرگونه مذاکره به این کشور می‌دهد.
🔹
متحدان یمنی ایران نیز روز پنجشنبه با هدف‌قراردادن دو نفتکش عربستان در دریای سرخ، این اهرم فشار را قوی‌تر کردند؛ چون این اقدام مخاطرات کشتیرانی در یکی دیگر از مسیرهای حیاتی نفت خاورمیانه را افزایش داده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452289" target="_blank">📅 18:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
منابع عربی از فعال شدن آژیرهای خطر در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452288" target="_blank">📅 17:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
منابع عربی از فعال شدن آژیرهای خطر در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452287" target="_blank">📅 17:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny-u6-hdQZX32enn-w6u6KgHGeciKU9ZKMOuUi8XkEgJpy6rle81duqRiIpQKzcjRbMtag5J2Hu7WA_TFmBIMygJgOSm8v4k9FLJ4i__KCt96kCRNITEITwHxU1X01elT19WyFQSKADh7ey1guQmlM0MCNIqhXS-eewOwbVm9HyD7oXpJNNB8kLMl-dYDEJyuaD2Ib8_K3_wVB2WUWXb9Ybq5FzMtrajEoPSQK0Boq5ZGhDRnhYMPD5a9tpVClsHHhpQ7trF7eFkc912UAIg3aWtJRXkCGwqERAjlyRmuYsiMf2xJLf_bdJaMiMhTkHm6WyhObnn4aCxSTBcH_BUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسانی به‌راحتی فسخ کرد
🗣
یاسر آسانی قراردادش با استقلال را به طور یک‌طرفه فسخ کرد.
🗣
طبق پیگیری‌های خبرنگار فارس، وکیل ستاره آلبانیایی ساعتی قبل با ارسال نامه‌ای به باشگاه استقلال به دلیل آنچه عدم پرداخت بدهی معوق و شرایط منطقه خوانده، قرارداد را فسخ کرده.…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452286" target="_blank">📅 17:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNizYSMdIZZzwt0g5I-1K0kiPUpgZzMe-2Hc9xRsTVC3G2s8wrMgCTbU86JqosZKSpC6cSEQQq419CEmA9msgjh3HTfY7ApCji2MRM0Mev2w9oeaWA7y7AVuByTzHrngD0xe9Sr2-KQGabiFUuofb4Z_IrZXugtJomKMKZr94BVP-FtLJxIk8VaNc-rY8HH7L9dbiwFsNZ5YtrlQIGhD7zoGD0rVwe4XwbpTYKyJgR4pqK9B4Y-p_B4J34Kf4qLCmBBie5tm9suWNYMnTpPTbf-1p5Yq7d2v1X_AJlVZClx3M3t3iFf3OFKku678JE73wpggNU2KIrZCBIs-My6Qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون آمار نظامیان کشته‌شده در حملات ایران را کاهش داد
🔹
نیویورک‌تایمز: پنتاگون در سایتش آمار نظامیان آمریکایی کشته‌شده در جنگ با ایران را از ۱۸ به ۱۴ نفر کاهش داد.
🔹
۳ مقام آمریکایی گفته‌اند که دلیل این موضوع این بوده که مرگ این ۴ نفر پس از اعلام آتش‌بس توسط ترامپ در ماه آوریل رخ داده است!»
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452285" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کندوان یک‌طرفه شد
🔹
پلیس‌راه مازندران: از ساعت ۱۵ امروز تردد خودروها در مسیر جنوب به شمال این محور متوقف شده و از ساعت ۱۷:۳۰ نیز مسیر شمال به جنوب از خروجی مرزن‌آباد به‌صورت یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452284" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7956e331.mp4?token=nqewxp07tbeVf6RpNs1k7yiMv3ymRGtESJ3o2RQPZpQDc9JDfyVHaMBDbeK2PX52IWSLwtJcjdGqvpEOgsoeKbrW6dQM23w-u7yV7c0OT6ZjdVacIklfvrEx0__etXJO9adDTQnSmkAKfXaOKbCM7EGdKU7nqDfj46kgiYnTlLGDdCY_gl4ncGEO_rzE4jYwBarqqUSBJajrEFGKIp5T6DJ5NvAec4efb4_EVf4R1EwufIBnEGzrC8YNp6gNhdHQewBBio4YS7Pr0hHsAKLcMGh91OAcaEfwuZxrk0vUwFN29hnb_UZthTBHbb2tvAzCHp40yrc3CKMzLJq_kvR-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7956e331.mp4?token=nqewxp07tbeVf6RpNs1k7yiMv3ymRGtESJ3o2RQPZpQDc9JDfyVHaMBDbeK2PX52IWSLwtJcjdGqvpEOgsoeKbrW6dQM23w-u7yV7c0OT6ZjdVacIklfvrEx0__etXJO9adDTQnSmkAKfXaOKbCM7EGdKU7nqDfj46kgiYnTlLGDdCY_gl4ncGEO_rzE4jYwBarqqUSBJajrEFGKIp5T6DJ5NvAec4efb4_EVf4R1EwufIBnEGzrC8YNp6gNhdHQewBBio4YS7Pr0hHsAKLcMGh91OAcaEfwuZxrk0vUwFN29hnb_UZthTBHbb2tvAzCHp40yrc3CKMzLJq_kvR-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۳ سولهٔ نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد
🔹
سپاه: در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی"، رزمندگان با هدف قرار دادن ۳ سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452283" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتحادیه اروپا ۶ فرد را به فهرست تحریم‌ها علیه ایران افزود
🔹
شورای اتحادیه اروپا امروز با اعمال تحریم‌های جدید علیه ۶ فرد دیگر موافقت کرد؛ بر اساس بیانیۀ این شورا، ۵ قاضی دادگاه‌های انقلاب در استان‌های مختلف ایران در فهرست تحریم‌ها قرار گرفته‌اند.
🔹
اتحادیه اروپا همچنین یک مهندس رایانه ایرانی را نیز تحریم کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452282" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
این بر عهده رسانه‌های آمریکایی است که در مورد واقعیت‌های این جنگ و تلفات بالای ارتش آمریکا و خسارات سنگین آن و ارقام هزینه‌ها که همه از دید مردم پنهان نگاه داشته می‌شود، تحقیق کنند و آمار واقعی و شیوه‌های سانسور حکمرانان دروغگو را افشا کنند.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452281" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkSt9LpPyB7j4TMatqyRCZkECfDU2RwLe6VDRlMf7KFVgzUSR3DJvbsMBYRRktbpXvskDkh5f850Jl5QQlyIEktaS0sb-LyRXHMqvbidWjolvKTOMmxN712c1VkHkAg8OVLxhcjDyW70Pf96M1pSXwBvfPcLPoX3MTiDrGYd8GHQwU_49HQro-fzHKSIna3IrQsen8EupKA9WC5pi43n5YxvQ3UxiZqx-s37Z8jm6HCt0tqD1KPujyE9ED8LZ7og8rOPHmiYhxHgxeC-B7MJduOOxI1JrxlgIJOlgEP_7bl1M3GLZcJfJ6XtMcYmitiVnrCk4LJ2DkmbOTy_7kEGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر جدیدی از مزار نورانی رهبر شهید انقلاب در حرم مطهر رضوی  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452280" target="_blank">📅 17:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJb7074XPtr79E_5vber9ixHl9_F4OPJVuCOykipx3jaPH-Qa06Y7mUUXNMbnqVpOIzSVu_wVbCESvzq84-TJGvQumTakoN60gEswqLje4ziFM3keQCGvc4pctR7evKhDttm_DLsALcGQnRlcTDhJbm4qxoVRliv_yCl4X8CKe51BG868wTYcpFJIbo1BkAHoR--9EbXoHPUlv4Mu6WSclXV9Ixl728FBzOkCptOCVhI85xnMhVouiE71WOj7x6_zIhPiEWebrcsuVOBxOoCaC6Jx2yt9ObNrod1lz6jyGVA16OXCEyoGzcGbisDEz0EUUrbUJgemE-nON9Y1ktnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه پاسداران: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند
🔹️
فرزندان غیرتمند شما در نیروی هوافضای سپاه در ادامه عملیات تنبیهی خود، در موج ۲۷ عملیات نصر۲…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452278" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
انجمن انرژی آمریکا: اگر قیمت نفت روی ۱۰۰ دلار باقی بماند، میانگین هزینهٔ گرمایش هر خانوار آمریکایی می‌تواند در زمستان امسال به ۱,۷۰۰ دلار برسد؛ یعنی حدود ۶۰۰ دلار بیشتر از پارسال.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452277" target="_blank">📅 16:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH7b_iTueXFu1l9p5f8zPY7GiE9llXHvBiwhV-AMAQIfOdR--suK9mheZnlcpBR23kR9QhTFWFDQWTNUPvv7r0D4lmILzTaIKyrU8Xt2PuRIHEAu1CalapeDM0tmxYxJ7X5-5XovcazeWGm6boZj1XKobDq_NvvsIO-uEIqHjk0Y_mJyl3w1wLp_cVjSTOPQtlhB5LB_0i_RMh6y-RsBVlMH4SJ3GNgkQTN1vXfkcjm-TrfrMOizNGksw1kM3Ko5VQ2TxVbG-kDAJ85peep2TgqmhjDKMMkTz4o-aQkLRP9oBLO0-0siLEc7P58BF4_eEBytCyVDkzJcUrhVQEx1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا همه هواپیماهای نظامی خود را از العدید تخلیه کرد
🔹
تصاویر ماهواره‌ای شرکت سنتینل-۲ که امروز منتشر شده است نشان می‌دهد که آمریکا پایگاه نظامی خود در العدید قطر را به طور کامل تخلیه کرده است.
🔹
براساس اطلاعات داده‌های منابع باز (OSINT)، در تاریخ ۱۷ جولای (۲۶ تیر ماه) تعداد ۱۷ هواپیمای نظامی در این پایگاه مستقر بود که تا روز چهارشنبه (۳۱ تیر ماه) به ۳ فروند کاهش یافت. اما تصاویر منتشر شده در روز جمعه نشان می‌دهد که اکنون هیچ هواپیمایی در این پایگاه وجود ندارد و طبق گزارش‌ها ارتش آمریکا همه آنها را به اسرائیل منتقل کرده است.
🔹
منابع خبری می‌گویند که خروج تجهیزات نظامی ارتش آمریکا نشان می‌دهد که این پایگاه دیگر ایمنی لازم را در برابر حملات ایران ندارد. این منابع همچنین مدعی هستند که جابه‌جایی گسترده تجهیزات و هواپیماهای آمریکایی به اسرائیل می‌تواند نشانه‌ای از احتمال تشدید قریب‌الوقوع تنش‌ها و درگیری‌ها در منطقه باشد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452276" target="_blank">📅 16:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
وقوع انفجار در عربستان
🔹
منابع خبری می‌گویند بر اثر اصابت پهپاد به انبارهای لجستیک ارتش تروریست آمریکا، در عربستان صدای انفجار شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452275" target="_blank">📅 16:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43a0966d5.mp4?token=qT7nNFXNi8XNehpVx7tT_fMdk1hd0jyRHNVDJ2rRAugkRyjxlEubRGRkzaTblwEPOTmcI6qEgoIQJFUFPCQNbIFE8xU_Ai0TX4KLBPT_ZgabKSEt5ttHaCUgrmAk-U5_TWGG5nO6fmd7m5lkXJpE-InK1FRKZObP_WTL79HYQNMF0lTCTcdUcEZeqgPwJLaY5oDoTidxeA_s_Y3j5YA0xk67HsIlXEDH6gpjl57hbyFh7mkGQObQQXr8w-_VOiwTRXBf9euLSa1IfzT8OmJDDCu7bJm9j1ZrpuFZ5Nr-ED4OYXFys_vuMAMoS3uNvRthwiYrR8_3rW5pq8u9-HqnPbu4B0PFvjIcnN2aSDqCcWJzQoUiS8bBhIy4SBmY3fFk3Uv9WSzxhHf7ahhkD-ksq7TtlnsBGRBU9F__rRhOPKYmdkS7TZRtvfdRBspf0cHwZ1jFtJwVLAbYJRQVXYr7V0HXSw4Z5GtjqUJn5YTwMn4LNksAiR952XU5AyuZz0vzbfUuDYPAmkVDzLeNdkFCFRl9vJIge6oCFU2sg1bzmbdu484a62-smjjnMTM3tzm1aL0V2jpKJuI2jE4FeA08a6BjTcZB1yiz-ZzxTw3aTqgEeX_F6dSlgGHtD2Cg2Sd5_K1H2e276XGsauWHwsTo8lOEyKuglsZmZ3E-QAJz708" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43a0966d5.mp4?token=qT7nNFXNi8XNehpVx7tT_fMdk1hd0jyRHNVDJ2rRAugkRyjxlEubRGRkzaTblwEPOTmcI6qEgoIQJFUFPCQNbIFE8xU_Ai0TX4KLBPT_ZgabKSEt5ttHaCUgrmAk-U5_TWGG5nO6fmd7m5lkXJpE-InK1FRKZObP_WTL79HYQNMF0lTCTcdUcEZeqgPwJLaY5oDoTidxeA_s_Y3j5YA0xk67HsIlXEDH6gpjl57hbyFh7mkGQObQQXr8w-_VOiwTRXBf9euLSa1IfzT8OmJDDCu7bJm9j1ZrpuFZ5Nr-ED4OYXFys_vuMAMoS3uNvRthwiYrR8_3rW5pq8u9-HqnPbu4B0PFvjIcnN2aSDqCcWJzQoUiS8bBhIy4SBmY3fFk3Uv9WSzxhHf7ahhkD-ksq7TtlnsBGRBU9F__rRhOPKYmdkS7TZRtvfdRBspf0cHwZ1jFtJwVLAbYJRQVXYr7V0HXSw4Z5GtjqUJn5YTwMn4LNksAiR952XU5AyuZz0vzbfUuDYPAmkVDzLeNdkFCFRl9vJIge6oCFU2sg1bzmbdu484a62-smjjnMTM3tzm1aL0V2jpKJuI2jE4FeA08a6BjTcZB1yiz-ZzxTw3aTqgEeX_F6dSlgGHtD2Cg2Sd5_K1H2e276XGsauWHwsTo8lOEyKuglsZmZ3E-QAJz708" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرتون در مورد این ویدیو چیه؟
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452274" target="_blank">📅 16:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
لحظهٔ عملیات استشهادی یک فلسطینی علیه صهیونیست‌ها که منجر به هلاکت یک صهیونیست و زخمی‌شدن ۳ صهیونیست شد.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452273" target="_blank">📅 15:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
سپاه پاسداران: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند
🔹️
فرزندان غیرتمند شما در نیروی هوافضای سپاه در ادامه عملیات تنبیهی خود، در موج ۲۷ عملیات نصر۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" با یک حمله کوبنده دیگر به پایگاه آمریکا در الازرق اردن، به چند جنگنده خسارات اساسی وارد آوردند و با در هم کوبیدن یک اقامتگاه نظامیان آمریکایی تعدادی از آنها را کشته و مجروح کردند.
🔹️
رژیم آمریکای کودک‌کش، به ملت خود و دیگران در مورد تعداد کشته‌ها به وضوح دروغ می‌گوید، مراکز تحقیقاتی و رسانه‌ها را به تحقیق میدانی در این مورد دعوت می‌کنیم.
🔹
در عملیات غافلگیر کننده دیگر، رزمندگان اسلام یک سامانه پدافند هوایی پاتریوت و یک بالن جاسوسی رژیم کودک‌کش آمریکا در اربیل را منهدم و اقامتگاه تروریست‌های امریکایی را مورد هدف قرار دادند.
🔹
رژیم زورگو و غیرقانونی آمریکا در صورت ادامه شرارت با پاسخ های متفاوتی مواجه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452272" target="_blank">📅 15:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f63876a96f.mp4?token=WAH9Je03yephv4dDLmM29Hox9SPEVZ6OPMPNhe4LkMVeus4Wxegot3BGx95hruBBkhRiaK5lgoNaRPdDCpv5njkN45WiH7h2LQ22nFOepyXnkwtHFYAP4dhqneqtkeu-l3XDJm3wSYtku4e-Nop3AbY71FCam2zCWrrAOwyw5k1BXX2EL1vrG3PCUqtgmFUoLwzDKAZmRbZEZwV3npBKPKOXdCDXBy9g0_k1g_4pfZ_VC-F5D_VpIbWnbXdrw5_lw7RoONtV-hYd71eEb5eUXmMYQW0huaqXC96Z09GwX0ouvbx6CA9VG9udjy3gke5zdHSKvUNHveo_YzAaYdAZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f63876a96f.mp4?token=WAH9Je03yephv4dDLmM29Hox9SPEVZ6OPMPNhe4LkMVeus4Wxegot3BGx95hruBBkhRiaK5lgoNaRPdDCpv5njkN45WiH7h2LQ22nFOepyXnkwtHFYAP4dhqneqtkeu-l3XDJm3wSYtku4e-Nop3AbY71FCam2zCWrrAOwyw5k1BXX2EL1vrG3PCUqtgmFUoLwzDKAZmRbZEZwV3npBKPKOXdCDXBy9g0_k1g_4pfZ_VC-F5D_VpIbWnbXdrw5_lw7RoONtV-hYd71eEb5eUXmMYQW0huaqXC96Z09GwX0ouvbx6CA9VG9udjy3gke5zdHSKvUNHveo_YzAaYdAZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا بدون داشتن کارخانه اسباب‌بازی تولید می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452271" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=Gk6nl9XuA_BJDy7mpGOb8elfN_D_xAlsdgrW6mx5N15Dzfi09CTuJN3nxPpiUOLimFkiqVV_p8vA1iXOUlLGXLHrx92IxvKKfz5-cnjHHr5_AhJRxPys81pIqnc8ZvSAjjGo0AJy9X4RwlfshGfp1gIHTiQdEAOm-czXQvsD4HC1n6PMO_R30dPZOXDfOnLQ87wg-BtkVcScTtGqibbuJL9MXSD_de79AfiRv1qNW88p4-TvbjkOliPuD4tAHNIj8-kAAGYTRFVyP1GhKs2dBfRsCLDy3qy6kaef1hJFgJDehpoeL4gme5De7OiUOZmWiBO1vy3jKKyUa0F5kG1JdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=Gk6nl9XuA_BJDy7mpGOb8elfN_D_xAlsdgrW6mx5N15Dzfi09CTuJN3nxPpiUOLimFkiqVV_p8vA1iXOUlLGXLHrx92IxvKKfz5-cnjHHr5_AhJRxPys81pIqnc8ZvSAjjGo0AJy9X4RwlfshGfp1gIHTiQdEAOm-czXQvsD4HC1n6PMO_R30dPZOXDfOnLQ87wg-BtkVcScTtGqibbuJL9MXSD_de79AfiRv1qNW88p4-TvbjkOliPuD4tAHNIj8-kAAGYTRFVyP1GhKs2dBfRsCLDy3qy6kaef1hJFgJDehpoeL4gme5De7OiUOZmWiBO1vy3jKKyUa0F5kG1JdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی، کارشناس مسائل منطقه: ایران با حمله به مراکز تمرکز و دپوی دشمن، از یک برگ جدید نظامی رونمایی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/452270" target="_blank">📅 15:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e470892728.mp4?token=fMLETwWp-jy6LWmNctPmH36wpnstDrdOKgubdpyp2g74aTUnFQCJSnuBPbdZgCP_HDotTKkc3zFPdAB81BGXDSXshj1XmF5AaLEIaqVKbCbAmZzSkfjlTeqS2qJDntQz9Pg4lUaK_ltIWSEaICI5TqCYcmX47G4hoPapGh9jpQ0mhi71bnfLtLMUHvKqNlL03U8-tKx16ZgfWtCI-z9aBP1KtKmZUdwfWKa9OjmpddtHvag76zIfvv8MBHqDvUtpcmPhedvw37LK0ru0XuRAaHI8mxQhIXMfZ9tPrLsv_rceIKcR0sCNiQTAM6wAKs3jnuL3K4CFuSiOgMrFiPOdMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e470892728.mp4?token=fMLETwWp-jy6LWmNctPmH36wpnstDrdOKgubdpyp2g74aTUnFQCJSnuBPbdZgCP_HDotTKkc3zFPdAB81BGXDSXshj1XmF5AaLEIaqVKbCbAmZzSkfjlTeqS2qJDntQz9Pg4lUaK_ltIWSEaICI5TqCYcmX47G4hoPapGh9jpQ0mhi71bnfLtLMUHvKqNlL03U8-tKx16ZgfWtCI-z9aBP1KtKmZUdwfWKa9OjmpddtHvag76zIfvv8MBHqDvUtpcmPhedvw37LK0ru0XuRAaHI8mxQhIXMfZ9tPrLsv_rceIKcR0sCNiQTAM6wAKs3jnuL3K4CFuSiOgMrFiPOdMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت تردد زائران اربعین امام حسین(ع) در مرز خسروی
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452269" target="_blank">📅 15:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07644f999.mp4?token=DxOcBK8jPc3zfYvJ6bmSno4Q6E7dP_TvJOlDlB-xRPsQ6JRKQ4RfrZ92Lo7BYD2BvJk51aGBR8BVNadlSAYd58Io7dVUZSnsrSZngsLUhVGluMGKC1hTX3mPc7Mjr3-K2pwfZE7mkl-31UdioU5CNzmhZIwV1kvJydbBf4N9zIhwbynsykD0uHkyFGMLsCY9gofcBSFnHrRD_Y39fZnlSzlnrAoAQnm62ntfRo41tv6Q0cI66ou2ty78OdotE4yocJWmsbQ8zHNPquv-lOVzq_UV1W1B8e5H7M2zZMUGyKLlhCAw5UMoTZmKenBWYXxlk_w1S_OaQFkjg0Vw_F4KGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07644f999.mp4?token=DxOcBK8jPc3zfYvJ6bmSno4Q6E7dP_TvJOlDlB-xRPsQ6JRKQ4RfrZ92Lo7BYD2BvJk51aGBR8BVNadlSAYd58Io7dVUZSnsrSZngsLUhVGluMGKC1hTX3mPc7Mjr3-K2pwfZE7mkl-31UdioU5CNzmhZIwV1kvJydbBf4N9zIhwbynsykD0uHkyFGMLsCY9gofcBSFnHrRD_Y39fZnlSzlnrAoAQnm62ntfRo41tv6Q0cI66ou2ty78OdotE4yocJWmsbQ8zHNPquv-lOVzq_UV1W1B8e5H7M2zZMUGyKLlhCAw5UMoTZmKenBWYXxlk_w1S_OaQFkjg0Vw_F4KGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروگاهی که رویای هوای پاک دارد
🔹
درحالی‌که شهرهای صنعتی کشور زیر دود مازوت‌سوزی نیروگاه‌ها قرار دارند، شمارش معکوس برای آغاز فعالیت نخستین نیروگاه زمین‌گرمایی ایران آغاز شده است.
🔹
مجری طرح‌های نیروگاه بخار شرکت برق اعلام کرد: نیروگاه مشگین‌شهر اردبیل که…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452268" target="_blank">📅 15:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImQ9WOekVQOm_mzjDGRDmtlg2ibNTr0kWNJASehFPtQNiKGMZLKl4jlblzu-gSm7gSd4IzKnnolCOAzqT4gaOF2-GVbi2JV5h2-SYLiMyGKH4QbW7FY1qzApSllIhOY5wPwPXmhAbL6yfErvujMeFA5jbU_29W6LNnl2S62Y097JKe0yvKQ1enO_OIWwddRFvgqhRi3NsmCqTFhCTWsDecPmeCflX6xT6yF4vadr8AL0U0gJvAE33ssE2brHHi8qs61KsSXFqw-pKl_FWFDRImwK-MDmxF6R3JG2o-yWwsTpdOdQW2BqNb8ZFngat72FRrf6oycAHbtIrmK_5rH3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاتزا روی نیمکت ایران ماندنی شد
🎙
میلاد تقوی، رئیس فدراسیون والیبال:
🗣️
پس از پایان لیگ ملت‌ها جلسات کارشناسی با پیاتزا برگزار کرده‌ایم و این جلسات همچنان ادامه دارد. عملکرد تیم، نقاط ضعف و برنامه‌های آینده به‌صورت دقیق بررسی می‌شود.
🗣️
حدود ۵۰ روز تا این رقابت‌ها باقی مانده و تیم ملی اکنون بیش از هر چیز به آرامش نیاز دارد. با قاطعیت می‌گویم که ایران با پیاتزا در قهرمانی آسیا حاضر خواهد شد.
🗣️
باید عملکرد فصل گذشته پیاتزا را در کنار امسال ببینیم. نمی‌شود به خاطر یک دوره نوسان، سرمربی را عوض کرد. ایرادهایی وجود دارد و تذکرهای لازم هم داده شده است. پیاتزا ظرفیت شنیدن انتقادها را دارد و خودش هم معتقد است تیم در مقطعی با بحران و چالش مواجه بوده، اما باور دارد با همکاری همه مجموعه والیبال می‌توان شرایط را بهتر کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452267" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=j8bN9cHa2zcq1vDOEGrVQp3LrEGDIU4I7ZzsNRu-ygTPJ5b1lXNjoDRAFWdu1ndOjYtachHIeT-q_iNuVNhjhu2XR6Te5bU9E-EEQWRhlSb94aa6XQOjTtUPhthahRNnvFfNMaQZivNE8xVlsnKazbciXRH0ZVHs9FMkTyw_-lG20JN30hSBNf3A-v2ZT1N1JfoEEsh7cSGZ4MXOH_xkXIqPuco4t9C0Kf4fl0_WM813Jvfd38Jm7Vqcj5CyTJci3FV7zSMMeNULBJkg-dUDsOliW2U8u98tGWYOnWakPLSOb5rQMmQildcjed8gp59KvBND9Ghyb7KOvvDjCFp8UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=j8bN9cHa2zcq1vDOEGrVQp3LrEGDIU4I7ZzsNRu-ygTPJ5b1lXNjoDRAFWdu1ndOjYtachHIeT-q_iNuVNhjhu2XR6Te5bU9E-EEQWRhlSb94aa6XQOjTtUPhthahRNnvFfNMaQZivNE8xVlsnKazbciXRH0ZVHs9FMkTyw_-lG20JN30hSBNf3A-v2ZT1N1JfoEEsh7cSGZ4MXOH_xkXIqPuco4t9C0Kf4fl0_WM813Jvfd38Jm7Vqcj5CyTJci3FV7zSMMeNULBJkg-dUDsOliW2U8u98tGWYOnWakPLSOb5rQMmQildcjed8gp59KvBND9Ghyb7KOvvDjCFp8UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی، کارشناس مسائل منطقه: ایران با حمله به مراکز تمرکز و دپوی دشمن، از یک برگ جدید نظامی رونمایی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452266" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3497f04ac9.mp4?token=XeCw7wKZLMTKitHcXGP8iF9CR-D7NbB2My_fLCXO8ZB3cDKFMNhvlmpE76id1_GNKQLACwdqkeTpV903HPw3HMpFvp15bXTTATwMnvssB6-0YzISK3t8cQzcJYcvCq2mrYWtnkoQYqJSIyqbapq8nEwxfEX9NzuaZJfN_6PYlYjOV2aRHp7yi-t4bYLYyer0LKdAzYTWis3mZbxRgaRawIShcQZ4L-kppIZBzGcSAl3VaAxnddj-fUWKIqwWClEAA8gwkob8jraFrVvqGItT3gC1QBg_L8lgxgBlQNTBnYvofxouQExLj6LVzObOUWmSjO3R6bp9lztICsmk4zXI0i7gDP2HVrbpwd1HoeOcpiSK4BvA4N93Slww1E3Gz2m2ny0pk1RZ25wJH45RYtOxJezxpY8HMFVnKz8u7-zW3v0HMSn1XGvaajTzUsIQXJQ5OZhbWNvn156W8uXta4nLzCMmH_QiZDIuRos3qJ2ZQm4wRG7PezjegEWbYHFff2hwZYz9Jd3eT4yjfAWs6Fy6VCwM_iINmHjul9pioVf1Qtjg-JVYHoVZT15JyArmcMdYMlbkKeIA-IUtLZWEMWkQbGoVTx6xKmDQz5LIOZ16EbsG0DiJXt65EMnBSB-aSMNT6dAvwHnnIJvrH1AwYROYxSy0u4vLxo57Z6-JnvN7fpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3497f04ac9.mp4?token=XeCw7wKZLMTKitHcXGP8iF9CR-D7NbB2My_fLCXO8ZB3cDKFMNhvlmpE76id1_GNKQLACwdqkeTpV903HPw3HMpFvp15bXTTATwMnvssB6-0YzISK3t8cQzcJYcvCq2mrYWtnkoQYqJSIyqbapq8nEwxfEX9NzuaZJfN_6PYlYjOV2aRHp7yi-t4bYLYyer0LKdAzYTWis3mZbxRgaRawIShcQZ4L-kppIZBzGcSAl3VaAxnddj-fUWKIqwWClEAA8gwkob8jraFrVvqGItT3gC1QBg_L8lgxgBlQNTBnYvofxouQExLj6LVzObOUWmSjO3R6bp9lztICsmk4zXI0i7gDP2HVrbpwd1HoeOcpiSK4BvA4N93Slww1E3Gz2m2ny0pk1RZ25wJH45RYtOxJezxpY8HMFVnKz8u7-zW3v0HMSn1XGvaajTzUsIQXJQ5OZhbWNvn156W8uXta4nLzCMmH_QiZDIuRos3qJ2ZQm4wRG7PezjegEWbYHFff2hwZYz9Jd3eT4yjfAWs6Fy6VCwM_iINmHjul9pioVf1Qtjg-JVYHoVZT15JyArmcMdYMlbkKeIA-IUtLZWEMWkQbGoVTx6xKmDQz5LIOZ16EbsG0DiJXt65EMnBSB-aSMNT6dAvwHnnIJvrH1AwYROYxSy0u4vLxo57Z6-JnvN7fpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ دولت پیشین آمریکا: ترامپ نمی‌تواند از گرداب ایران خارج شود
🔹
بلینکن: به‌نظرم ترامپ می‌خواهد از گوشه‌ رینگ که در آن گرفتار شده، خارج شود. او به‌دنبال یک راه فرار است اما نمی‌تواند آن را پیدا کند. برخی آن را تلهٔ تشدید تنش نامیده‌اند.
🔹
او نمی‌تواند این گزاره را بپذیرد که خودش یک واقعیت کاملاً جدید ایجاد کرده که قبل از این جنگ وجود نداشت، و آن [کنترل ایران بر] تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452265" target="_blank">📅 14:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgcHcBJs-icaNbB5AifxWTyx36ULV1mAIjzRpPLJbHjW432hDuZcsivwIvTSZQK6iRkvjbQoNBTT67v1dysDcxPT3vLoDsyg-EMsdGVAEkd0Q8kv4b8pKO566sj79revagh7oURKnLUP4Uj5PEkVxGD1_sGhJX3130TPAqgvlQURCQCb8gNMSolGC-zzND6k_f1BFvsNbZ7-jd9vqMhAZlz2kp4648a6cw4Jznx4VDObSE-SYuaHMitpXNF7D0FLIZ-6z14bzhHs8mYoGrLo05v8azQ5b14n9wwg7TZ5WgA4g8xJ2rqnU6AXUx4kXOuyofB2nD4nGPKDxPmWPsqIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامهٔ آزمون‌های نهایی پایهٔ یازدهم ۴ استان جنوبی اعلام شد
🔹
براساس ابلاغیهٔ رسمی وزارت آموزش‌وپرورش، امتحانات نهایی برگزارنشدهٔ پایهٔ یازدهم در استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۷ مرداد، ۱۱ مرداد و ۱۴ مرداد برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452264" target="_blank">📅 14:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اجرای محدودیت تردد در جاده‌های منتهی به مرز مهران از ۱۱ مرداد
🔹
پلیس‌راه ایلام: به‌منظور مدیریت ترافیک زائران اربعین، تردد تمامی خودروهای سنگین شامل تریلر، کامیون و کامیونت در جادهٔ ایلام–مهران و بالعکس از ساعت ۷ صبح ۱۱ مرداد تا ۷ صبح ۱۶ مرداد ممنوع خواهد بود.
🔹
خودروهای حامل سوخت، مواد فاسدشدنی، امدادی و پشتیبانی مواکب از این محدودیت مستثنی هستند.
🔹
درصورت لزوم، محدودیت‌های دیگری نیز متناسب با شرایط ترافیکی برای سایر وسایل نقلیه اعمال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452263" target="_blank">📅 14:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa13ec7b3.mp4?token=Bctd3UE285VoXETsIj--SIpPagNoulHJ7-KHbN9Jmhcb6YPNtL9ORtNjqUau6lmCUkElzk6z_iqALFKzYWiwvP3j2I3GPY76Ta7YiwR0vf0D03N51qlvzE2hNluAwnBTKsTv748fJsFfH0EXTNFbhbmkckF9621wYsT0PGS3o33J8mRRJbXbEa_L6h4CMyUfW8DB5Bc6fKqlJQCRM_6nCeu595pBX6073Jv1BHQia6GHHccz55QjOrXD1K8WL0LGrYtg8h_zTZ1dnSB4wODLwMgJacNj601v-zSnWXipFgh64Fq2sgCg9Ck51G-sqCcaIFK-bxpP2xOfa5jUR8dChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa13ec7b3.mp4?token=Bctd3UE285VoXETsIj--SIpPagNoulHJ7-KHbN9Jmhcb6YPNtL9ORtNjqUau6lmCUkElzk6z_iqALFKzYWiwvP3j2I3GPY76Ta7YiwR0vf0D03N51qlvzE2hNluAwnBTKsTv748fJsFfH0EXTNFbhbmkckF9621wYsT0PGS3o33J8mRRJbXbEa_L6h4CMyUfW8DB5Bc6fKqlJQCRM_6nCeu595pBX6073Jv1BHQia6GHHccz55QjOrXD1K8WL0LGrYtg8h_zTZ1dnSB4wODLwMgJacNj601v-zSnWXipFgh64Fq2sgCg9Ck51G-sqCcaIFK-bxpP2xOfa5jUR8dChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا تنب بزرگ، تنب کوچک و جزیرهٔ بوموسی جزایر راهبردی ایران هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452262" target="_blank">📅 14:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9f2ioG9KuYVdpBg6JAx5n_IphJY9jnuqRV2sUqZn0FNZ5kAay-DLe7kPvSu6r1OCmL7E-YzBykBLcHji70yIlHcrovYTh3tOrtIdi6wqdyaM9KnO6Sjv7qcnw3py9pSsPaVuEliCQpbwD8HdUhDmIi06R5TAzkNytmPxF--8v3rfn5dZJLaGUBf-zG_YBAqEBsi0lfZlMCek6JJAOvYWlaNh7y6zriscg9qb2bkaFaIcLNiwxOQ6wTGGMLD8Yhx2tz_9A8VPkCuJbdveYKfPt6yAfE2cLJ1I6tKz3cQAbswTd9gTb-4os3JrnjfHfSWtIWNKOsJSVFZZd85FfaJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد بیش از ۸٠ هزار نفر از مرز مهران
🔹
راهداری ایلام: تردد ۸۰ هزار و ۹۶۷ نفر از مرز بین‌المللی مهران در ۲۴ ساعت گذشته ثبت شده است؛ بیش‌از ۷۴ هزار نفر از این تعداد از کشور خارج شده‌اند.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452261" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
۳ سولهٔ نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد
🔹
سپاه: در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی"، رزمندگان با هدف قرار دادن ۳ سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی واقع در العدیری کویت، این سوله‌ها را به آتش کشیده و از بین بردند.
🔹
رزمندگان همچنین به‌طور همزمان برج مراقبت ناوگان پنجم دریایی آمریکا را در بحرین هدف قرار داده و خسارات زیادی به آن وارد نمودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452260" target="_blank">📅 13:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8bfdf3f35.mp4?token=OBTgnrIiocg8NLv-umQUVM00LFp07YjP7jiwBx2ZL9UOD8aVbnwNJ2rkgddXKT4yFMu3ITBXaJTsHus6oYo62cTLhN2bZEVKh-1ibx7ev4zHUgIhNCbqR7kyBXtqGlbBNGgtZTqciI6Bva4OjnCmO60RCF0UjK254Ar3JaX6bg6SC-2STue5m7duuIzpfNra771GLJb8PDDdPjBcRXO_hj4T2DQv8UZbfOoffxKrjr7pNuxw-y8BoOy81uUR9SQmAxrPG8EtYGII6wgNUHYyDxxbvq1s29nNqbzpHqBSMeluTt9kNVbK3xbCke8Lo4X13f5uKn2CPQid2hK2SXVVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8bfdf3f35.mp4?token=OBTgnrIiocg8NLv-umQUVM00LFp07YjP7jiwBx2ZL9UOD8aVbnwNJ2rkgddXKT4yFMu3ITBXaJTsHus6oYo62cTLhN2bZEVKh-1ibx7ev4zHUgIhNCbqR7kyBXtqGlbBNGgtZTqciI6Bva4OjnCmO60RCF0UjK254Ar3JaX6bg6SC-2STue5m7duuIzpfNra771GLJb8PDDdPjBcRXO_hj4T2DQv8UZbfOoffxKrjr7pNuxw-y8BoOy81uUR9SQmAxrPG8EtYGII6wgNUHYyDxxbvq1s29nNqbzpHqBSMeluTt9kNVbK3xbCke8Lo4X13f5uKn2CPQid2hK2SXVVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رسانه‌های اسرائیلی: یک اسرائیلی در محل تیراندازی نزدیک حفات جلعاد کشته شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452259" target="_blank">📅 13:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpPzCzUF14z5sdInG9tcAUACs4ROoxX_n_I8uioxw_qeLwh9kFMBI0dXvWghGu5Si9gnsX_n15e8NAisjlmrNXVpeKx0qEnXcZHLALU4MxB4n1aYx4Xr1EMr48LQ1rUWTKXRnuqZIASyCBY3lhVMbQZJp5qYJq4WNADjeiqP9kddWS9nVMt4A92z6LG395xV1FYuGpkEFPmIS4i3QhTDL8mjvoM8Hc59AH8BLse4nEar2R2uWRwf-cowTHd4NWeiggsxYOz01kFzYR-YA_B7IuO_9QjNPuhiPY1KTdvUajVnXLx4hgT2GiCRGivzhyaqpwn7maAjmFNBWHn_lMiQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار عراقچی و لاوروف در قرقیزستان
🔹
وزرای خارجهٔ ایران و روسیه در حاشیهٔ نشست شورای وزیران سازمان همکاری شانگهای در قرقیزستان با یکدیگر دیدار کردند. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452258" target="_blank">📅 13:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCVst17KivDuvUgQZcucdgHmHXqR6mtypvxxRQ__HmejpDiw0dHFvqedVKn6LW7ZdiikeQz0b4IEaFIUiy4JE1ZfOq9wTXRhReiFlYap2suEUGTdTnL7VtNRrFirc3qXKECBUbWYGiOY5IMy5SaZA-MBpNlBq4QItLVZAnKj1b6o3GK8miUyAzXnsgTy1TwzDCa7DHqTWyG0XpvEwzJ7114PTjR2xVE_mp4ra5oPUIGE9A44MLUxm3J3aT2UGHCnaZPQ7YfkP85FN9nAlfyNlIszrvsOfVXaHX73pe-LKwjmlIe5dOeiLmgXHaeT57SbqkY5B8xXd1fFW_YvgjVvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاتمی: تنها راه دفاع شرافتمندانه است، نه تسلیم بی‌شرفانه
🔹
خطیب نماز جمعهٔ تهران: برخی از نهادهای حقوقی و بین‌المللی صحت سلب دارند؛ یعنی نه‌تنها از حقوق ملت‌ها دفاع نمی‌کنند، بلکه در برابر جنایات بزرگ سکوت کرده‌اند.
🔹
جنایتکاران در غزه دست به نسل‌کشی می‌زنند و مدعیان حقوق بشر سکوت کرده‌اند؛ در چنین شرایطی دیگر این نام را نباید بر خود بگذارند.
🔹
این چهارمین بار است که آمریکا در وسط مذاکره دست به حمله می‌زند. در چنین شرایطی راهی جز دفاع شرافتمندانه باقی نمانده است، نه تسلیم بی‌شرفانه.
🔹
خداوند در قرآن می‌فرماید «فَمَنِ اعْتَدَىٰ عَلَیْکُمْ فَاعْتَدُوا عَلَیْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَیْکُمْ» و همچنین می‌فرماید اگر مجازات کردید، به همان اندازه‌ای باشد که بر شما ستم شده است.
🔹
از زبان این مردم به رزمندگان عزیز می‌گویم دست شما درد نکند؛ پایگاه‌های دشمن آمریکایی را محکم بکوبید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452257" target="_blank">📅 13:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سپاه: با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرید
🔹
روابط عمومی سپاه پاسداران: مردم شریف کشورهای محل استقرار پایگاه‌های آمریکایی در منطقه؛ رژیم کودک‌کش آمریکا پنج ماه پیش بدون دلیل منطقی و توجیه قانونی با به شهادت رساندن برجسته‌ترین دانشمند دینی و رهبر سیاسی جهان و همزمان به شهادت رساندن ۱۶۸ کودک دانش آموز معصوم، جنگ تجاوزکارانه‌ای را علیه ما آغاز کرد.
🔹
ایران بعد از ۴۰ روز جنگ پیروزمندانه در حالی که می‌توانست جنگ را با قدرت ادامه دهد، برای بازگشت آرامش به منطقه حاضر شد با نهایت گذشت با چنین جنایتکارانی پشت میز مذاکره بنشیند و تفاهم‌نامه پایان جنگ را امضا کند.
🔹
اما ذات جنایتکار و درنده خویی ایالات متحده موجب شد از همان روزهای اول تفاهم، آمریکا درگیری‌ها را از سر گیرد و تعهدات را زیر پا بگذارد و نهایتاً از ۲۱ تیر ماه رسماً تفاهم را ملغی و جنگ را از سر گیرد.
🔹
با گذشت ۱۳ روز از ازسرگیری جنگ، آثار شکست مجدد آمریکا ظاهر شد و دشمن فهمید با عملیات جنگی نمی‌تواند بر نیروی مسلح ما غلبه کند. اما برای خروج از بن‌بست به جای عقب نشینی به ارتکاب جنایت جنگی متوسل شد و پل‌ها، اسکله‌های صیادی، قایق‌ها و لنج‌های مردم، خودروهای عبوری و راه آهن را هدف قرارداد و غیرنظامیان را به شهادت رساند تا جایی که در روز گذشته با کشته و مجروح کردن زائران اربعین حسینی در مرز عراق جنایت را به اوج رساند و ماهیت یزیدی خود را آشکارتر کرد.
🔹
از آنجا که در صورت استمرار چنین جنایاتی دستور کار ما قصاص جنایتکاران خواهد بود، بسیاری از افسران و نظامیان ارتش متجاوز آمریکا از ترس آتش رزمندگان اسلام پایگاه‌های خود را ترک کرده و ساختمان‌هایی در شهرها را محل هدایت جنایات خود قرار دادند، به عموم مردم کشورهایی که محل استقرار نظامیان آمریکایی هستند، هشدار می‌دهیم با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرند تا در امان باشند.
🔹
مردم همچنین می‌توانند محل‌های جدید جابجایی نظامیان اشغالگر آمریکایی را به حساب رسمی روابط عمومی سپاه پاسداران انقلاب اسلامی در تلگرام به نشانی
@sepahnewsiradmin
و یا بخش "تماس با ما" در پایگاه اطلاع رسانی
sepahnews.ir
اطلاع دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452256" target="_blank">📅 13:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
الجزیره: صدای انفجارهایی در اطراف فرودگاه اربیل و مناطق غربی شهر در اقلیم کردستان عراق شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452255" target="_blank">📅 12:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQbMv4BHBjdjftgy8077u-fcKGaz5nCRpnITTCSdOfur0_CdvySn3P0Ctc0Kmf7HzQqgpi4nRo55dDfUSobO8WWWNP7UqKW69fHiSrL1ZRRdzeeLfwd48_FSXvO2tjkl5_O4toA81lWWGWE_t1ksqDuocsj44n5smtmeh9JD51zOmTRjrQheF7SSD4eNl3zT-T8U0_s2BqTQ6F0fsoucQ_yP5YNJuwoByKsz1DxDrwl3nqlnyPkrnR9gfz6btu2yUqE8G6zUHWqa2YUZPK4aTzt_OOHTLFS8Pt728aCaN8IZIauaU_-et7yafMNCneitH6ZW4-TfYiF5yoOtn8uk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni3Ohn-Isbyf3RX0L2kS1oDaf79_d2FTtpuyib_d69P-O9iiVyK2EqXF10F8O_35ZSZGo-r5vFRQIx0aRhsFyBBINqknJz84hyQZFJqlUpIwRQ8Xzd2YkGkhRCScvpf9H4psE_w_l_SRGZTNRTTrd19Vj-Qo7miuNhqOY8HXHGDJlQpspsOZmKuFPKcyTjYBO8jQQJ8EEds8xt9NOsumF3vzgBkP_8UjNLujfZqq11rT5XfugjOXY51LnSsizqjJcKdFPqkI0QmC8XATrm8lmkd3b4yPbY5e8b_b2qm4x7oTJ2RBjz4KFcOA-MkvgiNPNosaR-qVzAXwDglyQUluwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲۵ سند در قالب ۹ تصمیم در پایان نشست وزیران خارجهٔ سازمان همکاری شانگهای به امضا رسید.   @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452253" target="_blank">📅 12:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRONw4fylMpQnTCx34Rsv6OcpP2EG74ezkn0-sdAk0edf95T0OIdSPc3O62xsfkjGoHnhrUCAno0tz_oYvHV3lwtghkSYEZbkdZ-Gpd7IxP40vYU7EDTKHyG3lFJRwLPRYSjgj9AG7LZPz5Xrb_TSIi2K5pzbDfT2L_W0oR54iYQxXRd2MK1SKjqvZPtAgNj1Q8XymWBcp2_eUsDStgjbfaCJPwYiEHDN_riRmglulaq78X2JHWKtcZgaVPOPQ6DWgM-Gi0uwioWyyUhk205bXHDRCu8eC5DggVqYeUFT7aZhOz4KUfZrTguJlmFIYiyc5X1WWyd82YHQrFzb09HLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد دلاری نفت ایران ۱.۵ برابر شد
🔹
اطلاعات رسیده به فارس از وزارت نفت مشخص کرد، درآمد نفتی ایران از فروردین تا تیرماه امسال نسبت به مدت مشابه سال قبل ۱.۵ برابر شد؛ این درآمد علی‌رغم شرایط جنگی حاکم بر کشور به دست آمده است.
🔹
در ۴ماههٔ ابتدای امسال درآمد نفتی ۷.۵ میلیارددلاری وصول شد؛ رقمی که در ۴ ماههٔ ابتدای پارسال کمتر از ۵ میلیارد دلار بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452252" target="_blank">📅 12:35 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
