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
<img src="https://cdn4.telesco.pe/file/jHvm9JOuobx8kcvHRrhlbzP0AbKrq46aRIinnbffTOa_mwjtlCIwGbIT6NfHA1qWRQGbEws7swxngNQATAVpdkzEaC2-oEf9Xzv3ppXZdjhNCF7cESbnN4v-7SLVHyEOQVFfZBR6yHvFK4DPPME2M5RMWRHC6wdVdnz9PPJsQdGRGpaFHnfFjsKoW5i3V-cK3xjnu8jSdHAf8et0F8oImaguUJt9ahCFfOACEYKtuEEdZc2cYY9X5naQNbfnm_TeFZELkeL8te6OzyfL5-Zy1OQFiySsP9k5usj--BgrVPMS4x4ECd2vPsM0fX5JUlg-3ISmStXpGTccYClFS1ZUvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 04:59:13</div>
<hr>

<div class="tg-post" id="msg-450072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هشدار حزب‌الله عراق دربارۀ جنگ‌افروزی علیه ایران
🔹
مسئول امنیتی «کتائب حزب‌الله» به آمریکا و رژیم صهیونیستی هشدار داد که آغاز جنگ جدید علیه جمهوری اسلامی ایران، واکنش فوری مقاومت عراق را همراه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farsna/450072" target="_blank">📅 04:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=ANL0XuwN8nKXXGr22T4pu6ngGdWFZYvvT8-YJwG0p06FGAe2bT9YK2OWq-cRwgaiJcTMoyg4z0G88vG79lmSaY3saP5FDWe-bCfpqHqoutb3MPojTx9AGGLws9MeWcAEp_DepDZH-8pAlqZw8g4wWvqLRWfbQ3sTwOxKhuWryWocj5DTnUYd8EAcwF9UR36OXnlXsCifrgnUR8yqJQlLCKfWiINQH-tYYzbhEnSTmyay8pDYqHm8xqep2DPog49fueTzscLvbZq0NEIX44sqep1tpiJdxGzE0eSslvjMnwr72Zf_APZuh_tTKGC3rie41e-ZeVzjs-lLkAITWLBEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=ANL0XuwN8nKXXGr22T4pu6ngGdWFZYvvT8-YJwG0p06FGAe2bT9YK2OWq-cRwgaiJcTMoyg4z0G88vG79lmSaY3saP5FDWe-bCfpqHqoutb3MPojTx9AGGLws9MeWcAEp_DepDZH-8pAlqZw8g4wWvqLRWfbQ3sTwOxKhuWryWocj5DTnUYd8EAcwF9UR36OXnlXsCifrgnUR8yqJQlLCKfWiINQH-tYYzbhEnSTmyay8pDYqHm8xqep2DPog49fueTzscLvbZq0NEIX44sqep1tpiJdxGzE0eSslvjMnwr72Zf_APZuh_tTKGC3rie41e-ZeVzjs-lLkAITWLBEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت موشک‌های ایرانی به اهداف آمریکایی در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/450071" target="_blank">📅 03:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb04d40e12.mp4?token=DkxXzl4phPkCRN-khw62EtEt1JtSUmrf0dfoW_g58II_kCy1U0nCC101SkQA31KTob2gyjbk_inOr4Z9uJ5M_DiW4NK4FlDNkgHqX22PdJ31E4NxFgsv3YdP794l2TBY2U-fc9W3D_pvzlWjxhNhx-ELJvAEdsgqRBQnHBzStSKnbsVqQb5afs7vYMsXInmqzkxNgbzyOBnNY0CxSkQgyXHpBTU5uQHe61GctNvABZryu_31PyC_ZwWJEaAECitcePmh4lMkIbS-ITZDzL0fUG-1cmTxqL-5bN9p_dbNpnIxShQrNW2zHzCxqihWskEzk-Iyd_xPINdz5zd6HxXlLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb04d40e12.mp4?token=DkxXzl4phPkCRN-khw62EtEt1JtSUmrf0dfoW_g58II_kCy1U0nCC101SkQA31KTob2gyjbk_inOr4Z9uJ5M_DiW4NK4FlDNkgHqX22PdJ31E4NxFgsv3YdP794l2TBY2U-fc9W3D_pvzlWjxhNhx-ELJvAEdsgqRBQnHBzStSKnbsVqQb5afs7vYMsXInmqzkxNgbzyOBnNY0CxSkQgyXHpBTU5uQHe61GctNvABZryu_31PyC_ZwWJEaAECitcePmh4lMkIbS-ITZDzL0fUG-1cmTxqL-5bN9p_dbNpnIxShQrNW2zHzCxqihWskEzk-Iyd_xPINdz5zd6HxXlLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهادت اعضای خانوادهٔ یک محیط‌بان هرمزگان در حملهٔ کور آمریکا
🔹
در جریان حملهٔ بامداد امروز ارتش تروریستی آمریکا به هرمزگان، یک پست محیط‌زیست و انبار علوفه هدف قرار گرفته شد که درپی آن خانوادهٔ یک محیط‌بان شامل ۲ پسر و عروس او به‌شهادت رسیدند؛ این محیط‌بان…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/450070" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
🔹
گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/450069" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f0126dd0.mp4?token=QNxQpwcQ-V4K6qaJfKMU-lNbBeDO7q9EzudLFifFrOgypO10d7q2KecpgXz3lidLeA19H_xO6kwaj02Mo4bt3VHFy_5vUHw9yXe7sqAgl58NMVarNXlQ-7VATXjInM-DQ4UM1EVtWqFHowZCAIwL8LRKjPyp78uhg6RfyxGTdz4DMXDzBlyScpHMcsGIHDNoPhYCRAprXjvVC2dOcBo_MGIOdYJaCVAqFYqmU7iZ-kbnkQVnsjHA5rDplhuhjL4g5UEuss0XenexSY3_dvHs1Cc-w6hibHwp7AmLutpoLMVbZ8zi5gL_Xg8NoyqKV-MH_qxUSzt9_tFMsxYY7SIKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f0126dd0.mp4?token=QNxQpwcQ-V4K6qaJfKMU-lNbBeDO7q9EzudLFifFrOgypO10d7q2KecpgXz3lidLeA19H_xO6kwaj02Mo4bt3VHFy_5vUHw9yXe7sqAgl58NMVarNXlQ-7VATXjInM-DQ4UM1EVtWqFHowZCAIwL8LRKjPyp78uhg6RfyxGTdz4DMXDzBlyScpHMcsGIHDNoPhYCRAprXjvVC2dOcBo_MGIOdYJaCVAqFYqmU7iZ-kbnkQVnsjHA5rDplhuhjL4g5UEuss0XenexSY3_dvHs1Cc-w6hibHwp7AmLutpoLMVbZ8zi5gL_Xg8NoyqKV-MH_qxUSzt9_tFMsxYY7SIKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کویت
🔹
رسانه‌های عربی از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/450068" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت.
🔹
هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست.
📝
اطلاعات تکمیلی منتشر می شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/450067" target="_blank">📅 03:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2J_rUv3wcvUyfA_8PafnbuhyNjMfObOilMWyphsrWhRkNRQkc7sdqXAHEv0fDBT5ItLipi964Tfjd8oqG087bdeCjSwxfRWZkcg3quiEZCowgPVPYLFUHmKZkgUd4XsAwZzrXRu9mI-KYcPOz8IOUIFveg-WSgfGbTYPn0e-JYGeRo43cs4b18aiVfHnUja3m1kwTrhSIr6RX5jMAlc40AJuus_cgfrM7gI4Ge2INS6PtnDCGH-i_xpcRtQupXswOxkk7GeZLCnRFn5i2z1oUl7YybWZwI1G601yj9ouKeaIz0x2U0WSHnPbj-JUi5t8WQXrR1Lp_TqbcKPLSvQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/450066" target="_blank">📅 02:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت.
🔹
هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست.
📝
اطلاعات تکمیلی منتشر می شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/450065" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450064">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450064" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450063">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa94abe270.mp4?token=KDBNcK2C_En2u4K2bG7AzPgkiVjWp1utklmSx7FB1VUPvEw0iYTr541rYbLZCCFu5YUVw2ZvhHUnUxcMSKPoEa7ZwFM9uN9yyfpzo85hOAfplfG8SvcCO6A_nlD9WUgAIO_5aeMlgig42zFrQbXLeM3D2UbFg1Pmetj2sCLuz3M0NvXTDaqfP7W3jjyycOmxxgsoSRz6HiHqDTmXMsFM5ozAlQQ0pp8VPGBvs8t3jQVRNAyintyrSJ5QJ1ZX5w_xfKE_LmwjRrzENOcYrhOIoUZm5U-mCJJIeRa9aa_qe8uls2BUOUcJjzZ2999TVrNU-xW8L0zFsmoYwQa6B8cZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa94abe270.mp4?token=KDBNcK2C_En2u4K2bG7AzPgkiVjWp1utklmSx7FB1VUPvEw0iYTr541rYbLZCCFu5YUVw2ZvhHUnUxcMSKPoEa7ZwFM9uN9yyfpzo85hOAfplfG8SvcCO6A_nlD9WUgAIO_5aeMlgig42zFrQbXLeM3D2UbFg1Pmetj2sCLuz3M0NvXTDaqfP7W3jjyycOmxxgsoSRz6HiHqDTmXMsFM5ozAlQQ0pp8VPGBvs8t3jQVRNAyintyrSJ5QJ1ZX5w_xfKE_LmwjRrzENOcYrhOIoUZm5U-mCJJIeRa9aa_qe8uls2BUOUcJjzZ2999TVrNU-xW8L0zFsmoYwQa6B8cZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیلی/
ترامپ: کوه کلنگ را زیر نظر داریم
🔹
رئیس جمهور آمریکا به شبکه «فاکس نیوز» گفت: «ما پس از دریافت اطلاعات مربوط به فعالیت در کوه کلنگ، آن را زیر نظر داریم. اگر ایران اقدامی انجام دهد، فوراً پاسخ خواهیم داد. ما سلاح‌هایی داریم که می‌توانند به اعماق زیاد برسند».
🔹
ترامپ در پاسخ به این سوال که «آیا احتمال عملیات زمینی محدود را رد می‌کند؟»، مدعی شد:‌ «نه. بعضی وقت‌ها به یک عملیات زمینی نیاز هست».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450063" target="_blank">📅 02:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450062">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کویت
🔹
رسانه‌های عربی از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450062" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450061">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای ترامپ: ایران باید توافق را بپذیرد
🔹
رئیس جمهور تروریست آمریکا بامداد چهارشنبه بار دیگر تهدیدها دربارۀ حمله به زیرساخت‌ها و تأسیسات غیرنظامی در ایران را تکرار کرد.
🔹
ترامپ ادعا کرد: ما به‌شدت به ایران ضربه می‌زنیم. حملات به ایران تا زمانی که من بگویم دیگر بس است، ادامه خواهد داشت‌.
🔹
ما امشب، فردا و پس‌فردا به‌شدت به ایران حمله خواهیم کرد. در مرحلۀ آخر، نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد.
🔹
ما تمام پل‌های آنها را هدف قرار خواهیم داد، مگر اینکه آنها موافقت کنند به میز مذاکره برگردند.
🔹
ترامپ با ادعای اینکه آمریکا روز سه‌شنبه با ایران مذاکره کرد، اظهار داشت:‌ ما به ایرانی‌ها گفتیم که باید به توافق برسند، در غیر این صورت چیزی برایشان باقی نخواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450061" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
استانداری هرمزگان: اصابتی در بندرعباس، سیریک و جاسک در دقایق اخیر صورت نگرفته و صداهایی که گاهی شنیده می‌شود، از سمت دریاست.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450060" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010cb43dec.mp4?token=iPuWhxU3TGLn4uY_kABYjzCH9KiKwLjPY0SfgJf9aeUJyOpP9fRdPeq5TG-w0uABDN6gYAGi1LU1_Ee_CLvbcbxva2JC_5kzAOvnyC4YQgbFzqBmpr78lAMbcPTtR6ONoJPP-GFfIDTz4qUanxeBJ9eTthfr9990WSgmWXT5C0Me3I8KvtfT_Sfwb1cyBO29IwQTEO4VtrC3QEVy_jRZUKoQfEdpG1yUG5QZTzBg8vEeb19EJYzNvCH742Kxd5Fuq45bXmQDrEnGYH4qKbl38SfVxXGuT_6P3npDb-rX2TaLnHkHZi2Z7tXGZWSOWZifSk0egyGFIqnBgonjKwxqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010cb43dec.mp4?token=iPuWhxU3TGLn4uY_kABYjzCH9KiKwLjPY0SfgJf9aeUJyOpP9fRdPeq5TG-w0uABDN6gYAGi1LU1_Ee_CLvbcbxva2JC_5kzAOvnyC4YQgbFzqBmpr78lAMbcPTtR6ONoJPP-GFfIDTz4qUanxeBJ9eTthfr9990WSgmWXT5C0Me3I8KvtfT_Sfwb1cyBO29IwQTEO4VtrC3QEVy_jRZUKoQfEdpG1yUG5QZTzBg8vEeb19EJYzNvCH742Kxd5Fuq45bXmQDrEnGYH4qKbl38SfVxXGuT_6P3npDb-rX2TaLnHkHZi2Z7tXGZWSOWZifSk0egyGFIqnBgonjKwxqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل استقرار جنگنده‌های اف۱۸ در پایگاه الازرق اردن هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در مرحلۀ هفتم عملیات صاعقه و در ادامۀ حملات کوبندۀ پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده‌های اف ۱۸، ساختمان اسکان و سولۀ بزرگ تجهیزات ارتش تروریستی آمریکا در پایگاه الازرق اردن،  هدف حملات پهپادهای انهدامی قرار گرفت.
🔹
سربازان ملت در ارتش جمهوری اسلامی ایران قطعا درس بزرگ و پیام راهبردی رهبر شهید انقلاب برای دشمن را تثبیت خواهند کرد که «دوران بزن در رو» تمام شده و هر اقدامی علیه خاک و آب و آسمان این کشور تاریخی، بدون پاسخ و هزینه متناسب نخواهد ماند.
🔹
ارتش جمهوری اسلامی ایران، از آغاز  نقض‌عهد و آتش‌بس توسط آمریکا و حملات وحشیانه علیه مناطقی از کشورمان، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه ها و مراکز ارتش تروریستی آمریکا در منطقه انجام داده و این عملیات تا رسیدن به پیروزی نهایی استمرار خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450059" target="_blank">📅 01:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=BzmhLQlbzYwf_E9iOS4de4GBn5kQBOPDsJ5N-UxM2o8UeJDsKkzHc3YbTgzaFCbdWj2elNANrcdX87_GoVDPlf0rHmZgNqCuQXPSZD5VL4SOQGCTInY5C1p6UQbmgJOS5Kc-GOp2-dWoXwZBYxt2ajnh-AagYrvoPNtInpphGNwPh8DgH_zqOwUtsQP9sKG4tMcg6NnOH8GAlFMO3TkmEr_o62OhX5RhmkxKzgtHe3XXQW02u04-V1QNbY-0urul7bHhZILZm5Bhu1x-zRuO4SizrAn_iv0JNyLnHzQVQeMu1PqxopX2Lnc-hcF-E_4PKGxpapPWEXF7ZieCCLqdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=BzmhLQlbzYwf_E9iOS4de4GBn5kQBOPDsJ5N-UxM2o8UeJDsKkzHc3YbTgzaFCbdWj2elNANrcdX87_GoVDPlf0rHmZgNqCuQXPSZD5VL4SOQGCTInY5C1p6UQbmgJOS5Kc-GOp2-dWoXwZBYxt2ajnh-AagYrvoPNtInpphGNwPh8DgH_zqOwUtsQP9sKG4tMcg6NnOH8GAlFMO3TkmEr_o62OhX5RhmkxKzgtHe3XXQW02u04-V1QNbY-0urul7bHhZILZm5Bhu1x-zRuO4SizrAn_iv0JNyLnHzQVQeMu1PqxopX2Lnc-hcF-E_4PKGxpapPWEXF7ZieCCLqdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناوبان جانباز کنارک: موشک دشمن را دیدیم اما لحظه‌ای عقب نرفتیم
🔹
ناوبان جانباز تهاجم آمریکا به کنارک، در روایت خود از دقایق پیش از اصابت موشک تا آخرین لحظه مأموریت می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450058" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOu4UrEyY9bvigNrW3yiZSpW871EEI5Z33tRUOHERXevAEDCPz0LMgEbtBF7FPmZY-Wj_GffE-vet4p3GkGmBzS6LIPwSi5CaQxmEwkU9T41CQkPTUp-yKUYRHGu5xZW2qoa0DCRU_lpyW3FMT5Dg5ZV3yCeSGUXOFAjhH2895IDsQnH36_dFVCdTti_1OPS5ALVmfVDWOAjMuVwxlE4Y_pq0KKsrUWoU7TTHd7PCPlJBXKOxskXABKxsxIOTb6XT8ZMMZV2KhtsdWkQ3tcJpz8uSdmf9dEpqXNqf3cpcJIVaqGiirVV4XzANpSkroptOFG3RFPoSN3C_QBMfTBlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNsJT0JWdlOtV4Q6Zam9cupkTw5uWJ3uWrH-x_YUO2DOeR2gHww0DRrTRw1mY5sj_w5kdWYLV8gO5P4UYliJdSukWiO1pVjW82LLi7exAk3MSa8FktBjVDebjxOi-odvCGIMSAf5HNo5cVZNyc6LR87YAsNv7d1dThcMSbsonr3E4W7rCeBdfhEzJZbBqnNXmF8AYRispBmjZbtgrDRSlzcQxZgJ-IzKRl5HDL0r2t3jnXfJmQPTCUIrkUEa0ivjruceR4VOFtPuQy6He7xKY5ElP0i_3zaUOOYSeRmDfcZRnprEkAjdN43DR21oQGwOxQe1rinJxd9uzYIpVgkxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGg3M27je3jyyQRj2kMcbFFD3Rey7NhZxuVhRw1qpthLXLVLW2fSU3yfAaDgscd7l2YEkh_wE0pUT6G3PgVM2dkMyZ41dccMwab1NV-HUzkFebnHHRj6ZFaKTso9s9NE-KRdv_knvazWBF666CzDIraQ3wur6u3Q-PcNV9sngBJnQzbKUdF4bVt-1yy8RsHDrWWd0e0vshEZ7RyPPNo1oEtyYq6U2tYZlGtFu23nhSDcYrvpnbytpxgLUFcV0BCRpfPLbbllaQY-Azw6UIfLfWnhMMPnoKRDcuHYykjRcN7p_OUxzUfe_5CW1zV8JSE1MvwdmOc54CLIUeDpF7_EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpY5ZfUHZVwOvrRjF79mOR-BCUt65NLTyTmC_igX_i8Wy2PJcV07SodU4tG7WM6sShmW_bc9i1XSKonm5I47pMoat_44SjbYiz9lav6lGAWXY0ji9taw4nnPm4P7OeApT__n5tIDTVcNeBDOKmzOrSnjpimn4uI2hrAsaGa58wVijYGVhT-1X3bXAxfNrPr_KYttC39nUcSBey41YGMVL2M4uqalFQmcqYNSNcVse1icJodW10iN-HsBRvBYYEUmnandwmnxzyza7HleOQi-Bupvvi1b3EuebXkuSIz7pQ3P635RGBbifvSLsVhu8cMHJc1r2GUrH9aVLgERQtNJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۴ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450054" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez12576lrcAnXJ5uw8pTe035LGbLOhDmW9FAwAs6ezwowCknK4Pi3VhZSKIZGyYfK7_SEMmt32exq7cn_dIFa83lycNqDDwA-vmZjlvmGaN8vbw_oDNZmloCsG6XFvtpkafyYXsS4x_L9wPiBj-UtHjGrG03eqT1fMNLZi_Ug--ovmVtr9c8gheSGoCKwuVSelbATm1hdUf6YVe19w_kIx5sVyGfkXWV-xda_d6YhPQpzqeUR3z8Wf2bPSyXw5yDTrWfyjCuEjouzUJd_trwaMTi6WxPfVfglX_8E6MA9tpjwCO9kY_vaHpNY94now4xilP93xOX_WuL3dQF-7H3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDj7L50z93qR_u3TvBNkynh6wu-vnKNUXabuQQzBXtM11cTAjnHJpQQxWLXpBzVraWmY6MF0Y1A_Vb4MvAS7UXEX2YtJ_i-k6Dgofq-At46c2bCZ2Kvx2yt9qatr2Zhbnsc2CsA_kuKYVzxS9I5lnYzygVl4TBulO9E2oXsgmM-VJ46Cl6hdBvXTxyZVCAaqBB-E9tqotA5F3OqjrCCEBgsYRdkvkNTwHd5injY7LY4afH_gZ7y4DleW6UZFnsZ4w3Zgyy3RCMph5UvSN3dWFeiW_q1xWg6DpCTHrFsVeWGt9BnU1e18S1QQxdmfgDo3F1dyTJBFOTa4urfdLDnlfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipnKODn1QbGNzJhEdyQMNgVJLyfrJQ2pkhKqZ1IuSSuSsnFCLeyFK9nKrFoMRZu0y_CBJurl_g31VyaojahnZPnCndv0VrQuw9TEPfwtqVk-AOyKdAOPXqbS5W_zZxOiTsXT0kxkpyRj9EgraZcg6y4jQdjJEb7v7cepnMCu1NJnvvEkVMsYEmpiRrtjs4o2OpwKQQyvsPuCx-zmnm38Vj3DZJB-HKeUDtDXoN6wgKWAvEgiaMFqJiH5ctOX8OO4IA8WghqVazJn96wuzbuWM79jSQqQivetJsayv8DMMg9Ca107K2TfkjwtgzyazuiHmJD42b3j5Fb75t0U34tdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su-W6xUc-1_OuTeBbuuCirSmNsNoSoniNzr2FW-vlGUQDS8zPKvzntb5jjTBkjt0tFINXej5QNE5_uzydfr08A8RozLGh6dcjESCsma5U_cUk0bWVEh1lSGaJPBOTgAv2-QVP6VodOpsaNbCMHmslWhn8Doccq3y0E5TQQ4OupJKr27vMm8p9_1vk-EYnZZef2YNsPrdQkBdnRp5XU8-Ju-lszqOedWu5iD9S0KpL4EFsc8JzwCUo3odHslLsU8uKVcH36iW7_BfqcdtOUUyEOCkLJSSh2P1fh9GzC39daFGf6zbAkVdlH42aguuRQae8POT1DYfVdqxFTG1nObWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMPR1MC-xxAZ8KQMZrvpEu5j5fp8RBk9mE4yL2WtW8kcayc0ziZF3QnOOhSooQgZrXmuGi4P1ZH3WB8k4LM7MXAslmXIaALcQu1a-kiM_KnP-RNZRX6QPFPNvLTIfGR2X2tgBYgMbJxySlgJ8DJaURS6NjI2_gb1zej7-3ZJBtGuHtWaIfYq8BWBojdET1rQWS009JUaHcpS_pAhWQwZ9R20LosCh59_lnzjyEAkqozigITKKeBAEH8Bp7s_zxYAN1itORFLji37KMdEZLZz0-aABZZgXGClmU1ggW5ah2bOgrS2WZbOlBDpHy6kAJBN6I8gKp2hf6smvc0PnrtB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AI9zKWNS77jc3dVp0aVoEwmqaB7sL7lb26wt5Nf-uSm7VZHbbJpT5nROjl_TbucSkD2MBrLfTQ5l7kTW6dJzLlL7nQFFKmWgT0UBs3qiN6ThOQKWf83fDT7HSnYD_G1Nr56pFemd9ClTEmzUR1K6iHf6g40Wc2tov23zuAI9-koMrWiW12npJ_Xg6LxpOKhg9TBQ_pCaPX4YJbrCEvTmEuaF3XPE72ODQR80X0YLp9fPRD4Ud05m0LiLq5TMrN73SXIukzt3xZIByISlNVZgrKgEzidTm1CtuQQlWfpkIfO0IjNcHh3y7RWfwMjqdCqD6Fn4SorLTlGKd8NdEKdH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5qF3fY2YiroVPPqjDGge8YqIGFQoYV72SPtWdqUV2R-XBZxIZund3XA8G7SIVnhi3KOzYtk2LE2GDKDolmPxZSM7_p99rGF6a_-VCEogsWi2zE3otctP0g82GG55jWK-vOj26r65M-TbJ3kvr2PQk576l1DhM8YMiiMsdt7cV6YpRlYiOxXY4Scrk7KDbQOf-vDWoBKEyeHcswGHBreAEInjP-54hiUI5BPrqe4mCAp9dokX9J2gFD-PKKeensml8aSqSyLTy7eCuxQyM41eEAF5NhUFjc3DKFThqtDYUE5oy4778ZOgzmX43LutEiclxdCLRZ1Q7EqHZuBHKyMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWpNp2kFCon30TBwDXFji8fzsRHC3St1xgrEFDzzYnSTS02u_SgqVCVpGPow_XKCKZ7M6x4xJa4z67JLIP_fooQQhxqzgcVsPWMOSY2uBFRY_lY9ICKbw4It078UqjFFw0sYuoIbxiYnpkIuZTIDs_3YaoUTBqrJ5yml58dEzhlfA0Fq9hthLjuphk32c4nn6MAx6BHvrXC2h3qQm33p9HxIlaBtlAJsWq-2uHiwcejs5zYWFj09nbD_HkjfiDd8mjNhTuPoMB78ZzwUGXIbrC1C_acfOpBIf5WYJxryZfP5FGjlVSRAAM8_q6suNid-uDeIC9FUt8LIvdMQ3sPgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPXYAQ11ZSxKtN0ATxJ9zc-uRzsu1T6ThD202q532unWN_lIB9qjZ2cpqQPxesipRCRG-jHF14bowov2lN01ZiplBHyGm3xHPUAYLt_OPUj2p-G1qYDxyc8BZ5U83cjn7pIB4brUxmn69pijz9BFt81G0WJfiBrtPXq_YggqIINhEy63El0mhxJnHdZ_72yjFcjD1ANyDdL0LlW0TwsIEY_IJUlEGnfsqd1SsF02ONJ0Tw_s8rGJ03X5XkSi3k2Kbu8PIJ8aGz8grfXRsHa16U_fulhYPMkm9f7UK4Ct1nz5EW0MzuAoDXKcQkuXWYyinzwNbfFeMyrSQCH7EQVO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqMuSOlIB56v7Ym0Ludic2ufpApvn4vLGMNUNg2Fx5mO2LtkrBUOwiaix3O76JdMz7yEsPKuxVwQ0AVztwQ14QE4UHnMgJY_jyNw0NhxYVttdrpfVU9fti_bEJz5lyb_opagMnKeSJf5NfdGWOM1Y30h5-KF8thrXVcfRZ4A9VR6Yv_VnC7_GO_e7Z1NMQFvVlO4RVkQtXKfb8IjOw8jVpjf-rOnDJCUZ533NBQaveF100jKaeHK1y28MNZC1ex2ecDLmTNCs7t1eOhHg3AFO0Sjx2uQrA5r839vennqO-e8hPKBtjKpm34tr_mKFj73TMjRaY4ox0QiFOaZyfk2Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450044" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT13v3W_ALlnq2CTF2pks7iVn5K9HvN4fifw2zuzla8GF6s4D0oJUbNcy_x5bOc7rWK4_QE2szFzQyfLk4_yHRcX2TDsnoelWLl50yi9mF83vIw4ojM4BExDjXgkJQgBiL1Sbk38yjMP5-pdX5DO6AKwlos3adMntzd9Zu64s-mMRoPuIZekP0utSD2shwPRMS5qJ7ExyToa0Xha-wYRWjqK_WFRR2qsWCZ3qXh1pJ310Ie8m30WY6b8M_Y6N1X4sWVb0DjhTfr_YLKHwekU9IuxX1ybn8G1c4k-E1W8mIALEb41QnP95tqyh4vN2n8sul8IN-Zxe0dmSY1gyMBApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج نظامیان آمریکایی از عراق تا پایان ماه سپتامبر
🔹
وزیر جنگ آمریکا در دیدار با نخست‌وزیر عراق که به واشنگتن سفر کرده، گفت که نظامیان آمریکایی تا پایان ماه سپتامبر از این کشور خارج خواهند شد.
🔹
پیش از این نیز الزیدی، نخست‌وزیر عراق طی نشست خبری بعد از دیدار با رئیس جمهور آمریکا گفته بود که از تاریخ ۳۰ سپتامبر، هیچ نظامی این کشور در عراق نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450043" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=vfWgyJogCNfEBdVY0l8FFvPZSkJk0lu--3n7bC9bsmvHss-abwz7YFLKDyr_fisDJ43tszap2t0iigTNHEMev8OBIAMy3PuAc-SVUwicm-ad8w-4h_FgcV-Bo7i_E3L8eTg2dYSk6uu-rdwWPeKhrc9-ZtYQCIyLnAooZ11GFHu4gexop3SMuWU-eWwFDKs6jIstEKRjSzKS-JKv9fJ9jObYNZvYMAE4GZesAULBvPljlOI8d55630cF_RxoINpnX3RwdWZ8MqlYz17KqKpdfYvWgkegUUthuToZNLsoxDAAkH2q_Mhbz2KJoa-5JFCRi-257_IoayEs3I3YWdtwPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=vfWgyJogCNfEBdVY0l8FFvPZSkJk0lu--3n7bC9bsmvHss-abwz7YFLKDyr_fisDJ43tszap2t0iigTNHEMev8OBIAMy3PuAc-SVUwicm-ad8w-4h_FgcV-Bo7i_E3L8eTg2dYSk6uu-rdwWPeKhrc9-ZtYQCIyLnAooZ11GFHu4gexop3SMuWU-eWwFDKs6jIstEKRjSzKS-JKv9fJ9jObYNZvYMAE4GZesAULBvPljlOI8d55630cF_RxoINpnX3RwdWZ8MqlYz17KqKpdfYvWgkegUUthuToZNLsoxDAAkH2q_Mhbz2KJoa-5JFCRi-257_IoayEs3I3YWdtwPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: خون‌خواهی رهبر شهید به فراموشی سپرده نخواهد شد
🔹
انتقام از قاتلان و آمران تروریست امام خامنه‌ای شهید، در سطح ایران و جهان فراموش نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450042" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ستاد استهلال دفتر رهبر انقلاب: چهارشنبه آخرین روز محرم است و پنجشنبه اولین روز ماه صفر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450041" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450040" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e320839ea.mp4?token=aKRqcAzyL6MXZJcsn3lUBeROvN6MgVI8Rl6m0hrj9ftCdJ-Xg8Vhddn86N2UpEdLBFRULz771Yn27s2SEtDYCLDnfnqtpsRSLUHBwOZhDdE7QQrfMUwp6D8TLTto1EiksWZtKyvL7YJjSZkWdrbZ0yVldVxYg_6lk80pgRxTMevd3a9Km-jTMQPHmGoYzucb3J43HjcvNX1UhJUyq3MO3ItB-g91t8Io67tctP-_own841eVsVemydZ2HfFKMiRxlxKB-80FVKz_20mrU_H3B1yMf8s5mOo1BUcOlc8fiNsWF7yqlLLOhNZ5D6Z3EsQnjfd3AahlI6IRemiwkyZgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e320839ea.mp4?token=aKRqcAzyL6MXZJcsn3lUBeROvN6MgVI8Rl6m0hrj9ftCdJ-Xg8Vhddn86N2UpEdLBFRULz771Yn27s2SEtDYCLDnfnqtpsRSLUHBwOZhDdE7QQrfMUwp6D8TLTto1EiksWZtKyvL7YJjSZkWdrbZ0yVldVxYg_6lk80pgRxTMevd3a9Km-jTMQPHmGoYzucb3J43HjcvNX1UhJUyq3MO3ItB-g91t8Io67tctP-_own841eVsVemydZ2HfFKMiRxlxKB-80FVKz_20mrU_H3B1yMf8s5mOo1BUcOlc8fiNsWF7yqlLLOhNZ5D6Z3EsQnjfd3AahlI6IRemiwkyZgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان اسپانیا، فرانسوی‌ها را ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450038" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450037">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzqHFwC3eqDKbEIwntDj9vPx-xZMfTcVqbV8rP-xU-7TRmT_dgDyFSlY8NtR5ACqUtxjTuQqje9TbPBNpEmHmx_L9m-QEiTrMmm1jskK0X_2lJ4C8WE8FvTLy217dwq17AYk-YamiKlSo73Ey6EbbK1zUHN4q0jPUfAx7UUHICVB1Omk2cVFWdsQORr0gDSeR-d-oUmgZMr_auYnEMHDX-xFl4FzikuE0_jmux2WVU_k93TfFNHrTwoYiKEJJisBOHyfSyEpyOpzmTH3qEf7G1_LYJ1LZVAT0N1v0bKdsRs0ljq0SQSjY-EXoilddJi_4gyZuUxbvb_XdjRNIgHs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: حمله به پست سرمحیط‌بانی در استان هرمزگان، جدیدترین نمونه از جنایت جنگی آمريکا علیه کیان ایران
🔹
سخنگوی وزارت خارجه: فهرست جنایات آمریکا علیه ایرانیان هر روز طولانی‌تر می‌شود و هر روز که می‌گذرد، آمریکا پردۀ جدیدی از کینه‌توزی خود علیه ایران را نشان می‌دهد.
🔹
بامداد سه‌شنبه، ارتش تروریستی آمریکا به یک پست سرمحیط بانی در روستای سیدجوذر شهرستان حاجی‌آباد در شمال هرمزگان حمله کرد و ۳ عضو خانواده آقای جواد حسن‌زاده، محیط‌بان زحمتکش، را به شهادت رساند.
🔹
این تنها جدیدترین نمونه از جنایات جنگی شنیع آمریکا طی چهار ماه و نیم اخیر است که با ترور رهبران و کودکان و زنان و مردان ایرانی در تهران و میناب و لامرد  و... در ۹ اسفند ۱۴۰۴ شروع شد.
🔹
هر جنایت جدید، عزم ایرانیان را برای پیگیری اجرای عدالت و محاکمه و مجازات عاملان و آمران این جنایات مصمم‌تر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450037" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450036">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2edcc47a.mp4?token=QJtEtSiSsu7JqzfyPLNHVYB61vYkou9ClKADFK2h9rV7RS_3NqsRQm3hKtZppz_JUa3p87wTBP8Paz6vyyrJC72XsfSeAoxyKaaBfWUCzOT8ejkm-Qi8zb9Sd0rBaJ0FmCeIqFzZMWh_n6q0eWSkqSrrUwOrUblv8_wFH5hP1d5FowGVpT9KvVHMhXHDD2eF_k4fNXCq4tOZe7trItkbZ1Hf1Q_doiwjMohMucY_i0cO19E8SUTPcxpgQva01ADZeIGtcuPIA7hmGJD7kSH4HT6fnIbojZwLmguWP55_TT5Iro5v6vw4AU8UuUQ1jcVUSlENBbCzzQ1ToVb1FiPKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2edcc47a.mp4?token=QJtEtSiSsu7JqzfyPLNHVYB61vYkou9ClKADFK2h9rV7RS_3NqsRQm3hKtZppz_JUa3p87wTBP8Paz6vyyrJC72XsfSeAoxyKaaBfWUCzOT8ejkm-Qi8zb9Sd0rBaJ0FmCeIqFzZMWh_n6q0eWSkqSrrUwOrUblv8_wFH5hP1d5FowGVpT9KvVHMhXHDD2eF_k4fNXCq4tOZe7trItkbZ1Hf1Q_doiwjMohMucY_i0cO19E8SUTPcxpgQva01ADZeIGtcuPIA7hmGJD7kSH4HT6fnIbojZwLmguWP55_TT5Iro5v6vw4AU8UuUQ1jcVUSlENBbCzzQ1ToVb1FiPKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت امباپه از کنار دروازه اسپانیا بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450036" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450035">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da428073cf.mp4?token=QksE3KNb5QO6gPiwhmhPhm_v4oFmeRuEx8uhQfW2Aiv15-aGrfAipE_3XXD2QeiatPiy-J-T8IU1oks16DFII_qo5UgL6fRUhNYDyluZONS38lrdgc9m_BRWYqScUVIYVuduPxVIPB18FZbrwftVrBVseqZ6y3FMxqvIxWJusj2vgMok1kjKzx1DX_6vlliApM0KNeF401Y8i9FCLboJHH7QQ3jF6Z2k18PA5RbcvX4IGJ_Mlu97MbmsN2FPkTMxius8y07sIgeudDI3Ng2l86WxDekGQzpGl9yl2vlvfZ8wyHO8zfz60F8I0GfOCvu8jwdjKUlyoCTb5RgeJIx2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da428073cf.mp4?token=QksE3KNb5QO6gPiwhmhPhm_v4oFmeRuEx8uhQfW2Aiv15-aGrfAipE_3XXD2QeiatPiy-J-T8IU1oks16DFII_qo5UgL6fRUhNYDyluZONS38lrdgc9m_BRWYqScUVIYVuduPxVIPB18FZbrwftVrBVseqZ6y3FMxqvIxWJusj2vgMok1kjKzx1DX_6vlliApM0KNeF401Y8i9FCLboJHH7QQ3jF6Z2k18PA5RbcvX4IGJ_Mlu97MbmsN2FPkTMxius8y07sIgeudDI3Ng2l86WxDekGQzpGl9yl2vlvfZ8wyHO8zfz60F8I0GfOCvu8jwdjKUlyoCTb5RgeJIx2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوسی‌وششمین شب از اجتماعات شبانه در قلعه‌گنج کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450035" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450034">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دریای خزر تا جمعه مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌بادهای شدید و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را تا ظهر جمعه ۲۶ تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450034" target="_blank">📅 00:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450033">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de9f1865e.mp4?token=CthWrEyKz0A6yqtt4hjZWWPa5fBmCEYhiHAtK2Ktuisa5qABycR_YZjVQfkJ2qtnLtAQJkb82oftt2aYHMdqA2_C84e6f5WrJjIiMqcSEbg-pfN7LIdPEq8g2c3ic8GAB6XyFwNQf1KX7Ow13scf2sZ1FTk33KB3X1ynVMX1u5PCrwoiXNRc3whZCNuVluhvd-qo_RO6uk-zx5AIQHN0XWDsgw2O5iissrmNhbbEnn3FysxYQ-vgHDFK3DHh1x07MKNL56NTon3QBQCi3bKw_LTTYaEgwV5yJ0MX4bJKWGI7nBbyzNNbqWCRidpsLmBKL_NwEZljZTHaKckR71XrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de9f1865e.mp4?token=CthWrEyKz0A6yqtt4hjZWWPa5fBmCEYhiHAtK2Ktuisa5qABycR_YZjVQfkJ2qtnLtAQJkb82oftt2aYHMdqA2_C84e6f5WrJjIiMqcSEbg-pfN7LIdPEq8g2c3ic8GAB6XyFwNQf1KX7Ow13scf2sZ1FTk33KB3X1ynVMX1u5PCrwoiXNRc3whZCNuVluhvd-qo_RO6uk-zx5AIQHN0XWDsgw2O5iissrmNhbbEnn3FysxYQ-vgHDFK3DHh1x07MKNL56NTon3QBQCi3bKw_LTTYaEgwV5yJ0MX4bJKWGI7nBbyzNNbqWCRidpsLmBKL_NwEZljZTHaKckR71XrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم اسپانیا آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450033" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dce3529d.mp4?token=pUNmnGwU4C8i3dI-kvVJHQs5UbPEuapXeWGawyeTtLzpBOvOeMNAYV-j7KR2C0PxY6Jp-gc3bP6KkCO8G3BYypm4nGXegGEkKu7vI2fhKNDcobeph67nmYWGJM6OTvhc7sM5s5Dn8_mT8h-1m645rq21em7UjldlAzJJUp5eq88mF--wXybYddFeCIiE2kLfSJbIXDm3AJQw9zVDOKPEmd2wnuCJmgdh231kTwr8Xja-qAic79r2dMBp8LgBZJQMuxbHKZnGrLinSuzJwFPfMFvk3I3D89XOJ50CNZficaKkGkQrkgAsQlKrs_mMcwIjI9qD_RLardqn97CfIqA3QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dce3529d.mp4?token=pUNmnGwU4C8i3dI-kvVJHQs5UbPEuapXeWGawyeTtLzpBOvOeMNAYV-j7KR2C0PxY6Jp-gc3bP6KkCO8G3BYypm4nGXegGEkKu7vI2fhKNDcobeph67nmYWGJM6OTvhc7sM5s5Dn8_mT8h-1m645rq21em7UjldlAzJJUp5eq88mF--wXybYddFeCIiE2kLfSJbIXDm3AJQw9zVDOKPEmd2wnuCJmgdh231kTwr8Xja-qAic79r2dMBp8LgBZJQMuxbHKZnGrLinSuzJwFPfMFvk3I3D89XOJ50CNZficaKkGkQrkgAsQlKrs_mMcwIjI9qD_RLardqn97CfIqA3QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا به فرانسه توسط پورو در دقیقه ۵۸
⚽️
اسپانیا ۲ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450031" target="_blank">📅 23:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e50082f6.mp4?token=cPYpV5gPNXeOFL97bGzfqJT_YNwBAorToGljswonBnoZ83ypL_rrkUddD3ZXZW0I50DNEg-wJY6qYxX0mi4FAXaNU5_qurZyuYRryyJlQR-um4Xte-rbEvqPaFGmwSLiuFD28Jl7n_v1X_S4CXSD5jm8j51FMk1_B6gl4xHwu2FTXPMheDH1qPRoFVgXKHEvN9byctAh1MND8Al1Dn83uJf2Ujpoy9W0hnpEEgayvt--pToaKt7zm6Nt_ZZT2_iYPSSrBjTkseJ3el7VM2TZHHTtIGxjbNc0ShMImOm_2LDUxEQJaiImK6tYbNkagst9ai6OHCmM5qdZa5_c4jmN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e50082f6.mp4?token=cPYpV5gPNXeOFL97bGzfqJT_YNwBAorToGljswonBnoZ83ypL_rrkUddD3ZXZW0I50DNEg-wJY6qYxX0mi4FAXaNU5_qurZyuYRryyJlQR-um4Xte-rbEvqPaFGmwSLiuFD28Jl7n_v1X_S4CXSD5jm8j51FMk1_B6gl4xHwu2FTXPMheDH1qPRoFVgXKHEvN9byctAh1MND8Al1Dn83uJf2Ujpoy9W0hnpEEgayvt--pToaKt7zm6Nt_ZZT2_iYPSSrBjTkseJ3el7VM2TZHHTtIGxjbNc0ShMImOm_2LDUxEQJaiImK6tYbNkagst9ai6OHCmM5qdZa5_c4jmN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450030" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450029" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c80bdd581.mp4?token=BSg33H6LhaH4JACDJrwNl1N9nt-IhB837s-0JdiCkBe15mGY0f_HcUFcxWrhMMtaJxJ6aam1KBoRHnEzrwEdDiIRGYE-ZN5Qz2JG7qWguNeoFDJpt5WfncVGq2Pbj6H5ZUp0-LARWU-FED-ksFCXWM5pYeIlGQl9Wzl6oXyNgKYYog_976-95XfYiu-j5u7b5t_vAJzA8GFrl2YF-X3QOoIbl_45qyCvZHqvrLJdg7VVh7ihTXO79GJGglJe9mPoWiSQFAGdS63mWfTyP1TlYT4xgkyNiTot54TEPGfiwZEBqcbQ7HyNLhKpSI8mWGa1ORqpxH9epdsPpqnlBEaV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c80bdd581.mp4?token=BSg33H6LhaH4JACDJrwNl1N9nt-IhB837s-0JdiCkBe15mGY0f_HcUFcxWrhMMtaJxJ6aam1KBoRHnEzrwEdDiIRGYE-ZN5Qz2JG7qWguNeoFDJpt5WfncVGq2Pbj6H5ZUp0-LARWU-FED-ksFCXWM5pYeIlGQl9Wzl6oXyNgKYYog_976-95XfYiu-j5u7b5t_vAJzA8GFrl2YF-X3QOoIbl_45qyCvZHqvrLJdg7VVh7ihTXO79GJGglJe9mPoWiSQFAGdS63mWfTyP1TlYT4xgkyNiTot54TEPGfiwZEBqcbQ7HyNLhKpSI8mWGa1ORqpxH9epdsPpqnlBEaV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار خون‌خواهی و ایستادگی مردم کاشمر به ایستگاه ۱۳۶ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/450028" target="_blank">📅 23:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بیانیه سنتکام درباره آغاز محاصره دریایی در تنگه هرمز
🔹
سنتکام با انتشار پیامی در شبکه اجتماعی ایکس مسئولیت دور جدید حملات علیه ایران را برعهده گرفت.
🔹
در این بیانیه آمده است: ساعت ۳ بعدازظهر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف قابلیت‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شوند، ادامه دهند.
🔹
ارتش آمریکا افزود: این حملات در حالی انجام می‌شود که نیروهای آمریکایی برای از سرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌شوند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا (۱۱:۳۰ به وقت تهران) آغاز می‌شود.
🔸
آمریکا پس از شکست در بازگشایی تنگه هرمز بار دیگر تلاش‌های خود برای محاصره دریایی ایران را از سرگرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450027" target="_blank">📅 23:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17ecbe176.mp4?token=hJduuEWsNTTqO5rvFhV_W04xf7gKt5C4hN-Zed_uDAxVpACu6nHIsa7fuCcxaORZDBoDDto1uEfJTeXx9pBslJJiUX7TFtT6brB_GFJZfV7YIfvP5TL8OBq_hOebKCOZDvdLDxFExR6FBQVJay6ng-gem2Rhnhs9QRQ2itZXNnv8aigVczmY2_eur0ec7sb82ZGRq7Lv021wnBiF9VGBQPfgiLLqoZqubyn7cY6et1xyu-ISb65syBaTrlF6nY6Bsy8cIX0hmS43N4Hh0YoxpDiFdbdhMEAZvlXjDYSvBUqz4beismbUcGiYR6qAzt5gNYlhjOPuggtvkz7BWB7B9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17ecbe176.mp4?token=hJduuEWsNTTqO5rvFhV_W04xf7gKt5C4hN-Zed_uDAxVpACu6nHIsa7fuCcxaORZDBoDDto1uEfJTeXx9pBslJJiUX7TFtT6brB_GFJZfV7YIfvP5TL8OBq_hOebKCOZDvdLDxFExR6FBQVJay6ng-gem2Rhnhs9QRQ2itZXNnv8aigVczmY2_eur0ec7sb82ZGRq7Lv021wnBiF9VGBQPfgiLLqoZqubyn7cY6et1xyu-ISb65syBaTrlF6nY6Bsy8cIX0hmS43N4Hh0YoxpDiFdbdhMEAZvlXjDYSvBUqz4beismbUcGiYR6qAzt5gNYlhjOPuggtvkz7BWB7B9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی نیروی دریایی سپاه در موج سوم عملیات نصر ۲  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450026" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450025" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a35ad7e2.mp4?token=N1k9jJdQg2eR8k_zpesgV7HHGcKwBtm-xi7X8mKG4Fi8mp104BaytQZKF-8W8bxUmI7IEEbMxJtPLZIWMZucBhYLcEdnk0eTil82Ggz8fvO2NwskUZqGvWYwZ6WX79_uREOCDuCh3HicPGnewt-elpGJ8tZWj9ZaXi4PnugcnjX50olzFKSchgJFdWqJPs-7YSDgQcTLbfe9iBzQKwrme9LOW97Vs1vyKAmexU1VdJDVPd0S-CfMXHP-9eS_ZQ4ej3fU4K3sWPuASCjMhyqdD70kxtBaPX_ZQ_Z0ZZPw4HqIPMKEA-ChW7PX1xYtZxJcbHu9TfQaj7nzX5boDyVnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a35ad7e2.mp4?token=N1k9jJdQg2eR8k_zpesgV7HHGcKwBtm-xi7X8mKG4Fi8mp104BaytQZKF-8W8bxUmI7IEEbMxJtPLZIWMZucBhYLcEdnk0eTil82Ggz8fvO2NwskUZqGvWYwZ6WX79_uREOCDuCh3HicPGnewt-elpGJ8tZWj9ZaXi4PnugcnjX50olzFKSchgJFdWqJPs-7YSDgQcTLbfe9iBzQKwrme9LOW97Vs1vyKAmexU1VdJDVPd0S-CfMXHP-9eS_ZQ4ej3fU4K3sWPuASCjMhyqdD70kxtBaPX_ZQ_Z0ZZPw4HqIPMKEA-ChW7PX1xYtZxJcbHu9TfQaj7nzX5boDyVnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی نیروی دریایی سپاه در موج سوم عملیات نصر ۲
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450024" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اصابت پرتابه دشمن آمریکایی در حوالی بندرعباس و سیریک
🔹
بین ساعت ۲۲ تا ۲۳ امشب چند انفجار در شرق بندرعباس و نیز در سیریک گزارش شد.
🔹
همچنین حوالی ساعت ۲۳:۰۸ نیز چند انفجار در بندرعباس شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450023" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c2501449.mp4?token=HYGZbgPHVxYMFo24lqyaTsX0coXeYi4V4P_mfMp4kMQgBoQXkvgxx2-3tI6HqH7JLYY174na9TEi0-fgaXkpaGoNrOURpe9R-tJUi9zq1IRtMZwH6gHpmDvb8CbGAMwGLb26iF5KdKKItPuYoMl2NLogZ_SJlUyyP6XCCre9oRwf6KexkwyhQSGIhUBRcmuoIXbOD22xHOu5j_SfRVgz8e3WhUiGpLo8tY8dO_gWyhthjZDx5CsCKTbd89SjDHxin9Aq7HjexhrkK2C2LeI2mA-8hWJ3WONu-8L4CttrlMmRYUxV_RmRCCmCMEADMesD-DMJEDhKJXl97ej58wowFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c2501449.mp4?token=HYGZbgPHVxYMFo24lqyaTsX0coXeYi4V4P_mfMp4kMQgBoQXkvgxx2-3tI6HqH7JLYY174na9TEi0-fgaXkpaGoNrOURpe9R-tJUi9zq1IRtMZwH6gHpmDvb8CbGAMwGLb26iF5KdKKItPuYoMl2NLogZ_SJlUyyP6XCCre9oRwf6KexkwyhQSGIhUBRcmuoIXbOD22xHOu5j_SfRVgz8e3WhUiGpLo8tY8dO_gWyhthjZDx5CsCKTbd89SjDHxin9Aq7HjexhrkK2C2LeI2mA-8hWJ3WONu-8L4CttrlMmRYUxV_RmRCCmCMEADMesD-DMJEDhKJXl97ej58wowFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های مجری پرچمدار با مردمی که این روزها در خط مقدم در جنگ قرار دارند
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450022" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff6bcc325.mp4?token=XA2dlpJQ_ZD5js466MKrvyCK6OPsS257H_IavtvCapJzFyAWnWDzsbJOimHsKg_PqiucGiVvrQXf3qybN-_R15wxd8VI51BB59RxUmnJKSWZsstejIM8ozckbmxSfsrIFxjeDrcRSA5Z-dJjNNJUOwxfR8nKAKSLq3ZZnlSgaRUtGyiOZ7GJ4etuEaarJUi6HGCaaL_zsFlmwbxWLrKaQmWKDNsMY87_bx0bIiB4rML02M6ljOdyMq8g-jDn1p1SDr501AM_CQiXp9tRnOW1OY7oXd-Iz01nFGQmX3ZAQ8qokc-d6y3HCMVX7DvdERFcZuTKu4A7VbVI3rng4ycs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff6bcc325.mp4?token=XA2dlpJQ_ZD5js466MKrvyCK6OPsS257H_IavtvCapJzFyAWnWDzsbJOimHsKg_PqiucGiVvrQXf3qybN-_R15wxd8VI51BB59RxUmnJKSWZsstejIM8ozckbmxSfsrIFxjeDrcRSA5Z-dJjNNJUOwxfR8nKAKSLq3ZZnlSgaRUtGyiOZ7GJ4etuEaarJUi6HGCaaL_zsFlmwbxWLrKaQmWKDNsMY87_bx0bIiB4rML02M6ljOdyMq8g-jDn1p1SDr501AM_CQiXp9tRnOW1OY7oXd-Iz01nFGQmX3ZAQ8qokc-d6y3HCMVX7DvdERFcZuTKu4A7VbVI3rng4ycs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها با پرچم یالثارات برای خونخواهی امام شهید به‌پاخاستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450021" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08WghAyLkEf5KjkbAzcw56b6Df6uW2HyXNHcofMoo64NUemnqG6Ie6RX1WZx-p4cx4k8RJBcmkSFABqrFknPbsN8i4GLo_6cSd86l0rw2Es7gn3uaWHWhAvEcoWzg1MYzopsvYKb-ys0VfO_3WyzqgcGJS6K_-OHVb0uZk628DE2m6OGGgGyGX_V0tMzz1ZuN5w7h6pLlr6fyD8Vt6NEqhvxYd7COxKotwciR0Dhuy5-WsJmN7MRPN5y8Vwc6Nc6wQC0sZe11W9PBSoLg3TUo0r0Wk8KjqLvRAB8IojdIxsp_FwoPU8atQF0bchunnlY-gW7REt5AjYxYwCrVLFKsA-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08WghAyLkEf5KjkbAzcw56b6Df6uW2HyXNHcofMoo64NUemnqG6Ie6RX1WZx-p4cx4k8RJBcmkSFABqrFknPbsN8i4GLo_6cSd86l0rw2Es7gn3uaWHWhAvEcoWzg1MYzopsvYKb-ys0VfO_3WyzqgcGJS6K_-OHVb0uZk628DE2m6OGGgGyGX_V0tMzz1ZuN5w7h6pLlr6fyD8Vt6NEqhvxYd7COxKotwciR0Dhuy5-WsJmN7MRPN5y8Vwc6Nc6wQC0sZe11W9PBSoLg3TUo0r0Wk8KjqLvRAB8IojdIxsp_FwoPU8atQF0bchunnlY-gW7REt5AjYxYwCrVLFKsA-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راننده‌ای که کامیونش را وقف برپایی موکب رهبر شهید کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450020" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc44b8bf30.mp4?token=c6aQK9ieoZh0FaFx6AEtyowoat3_eiDnehFZZ8WajcliUYQgwVc2Vn4gCz96sI1d3tArrbP_54b5X2YeCjGCkGSPlrMWPDk7TthzP6JEXaKgTg80ACOY5jHlcp0bAhWazKjpIaumTp39rFfre0TdIlwuODED2Do-XkFC77V15r2wwrECHxUC9JXrWr-j3J6L3nmyNSv0lFgmwiqN3RGvuS13w1MMSZkvchnUgIlwakftw3o1j9ITDo7cU8iA6ofeZDN1O8gPL9U83QG8BEIzD5PB2FgFEk12BqxHlHGTmGc_ZvjApPvqEfcT_c8oc_c6ZRl9e7Ev0WI4WHwRxN9STQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc44b8bf30.mp4?token=c6aQK9ieoZh0FaFx6AEtyowoat3_eiDnehFZZ8WajcliUYQgwVc2Vn4gCz96sI1d3tArrbP_54b5X2YeCjGCkGSPlrMWPDk7TthzP6JEXaKgTg80ACOY5jHlcp0bAhWazKjpIaumTp39rFfre0TdIlwuODED2Do-XkFC77V15r2wwrECHxUC9JXrWr-j3J6L3nmyNSv0lFgmwiqN3RGvuS13w1MMSZkvchnUgIlwakftw3o1j9ITDo7cU8iA6ofeZDN1O8gPL9U83QG8BEIzD5PB2FgFEk12BqxHlHGTmGc_ZvjApPvqEfcT_c8oc_c6ZRl9e7Ev0WI4WHwRxN9STQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450019" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a32f2aaf.mp4?token=QsTJWW3xU0Pk_6vqXbHNWxLmkrZfSQzC5BgKLv26mtnRXPht48K0z15UdG-bVfXS9t7EZhMIcjhaxRStloiCxXfqL4ciDjnPbomQSkPOiZNQik89O-hOwWMnAQa3T8yAfb0CsHCUPrEhZ-lpYjzXl17QP-wguW7PB0fiSrWQQK06mMNxCBvP4bEx3Yx9VhiEetbxaZ4uQkNS9tsdabwIuphxHeaZ7nOEaJg85CU8DUhR_ZlAl2588igMi_7vpucxsOr-vghv4qomNoOFDUXb-LDnwGvaZ-P_h1eV43VhC18h50AsNGuJg73Cf38YPW2YVN0e9miulW4TT_Ngt3xHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a32f2aaf.mp4?token=QsTJWW3xU0Pk_6vqXbHNWxLmkrZfSQzC5BgKLv26mtnRXPht48K0z15UdG-bVfXS9t7EZhMIcjhaxRStloiCxXfqL4ciDjnPbomQSkPOiZNQik89O-hOwWMnAQa3T8yAfb0CsHCUPrEhZ-lpYjzXl17QP-wguW7PB0fiSrWQQK06mMNxCBvP4bEx3Yx9VhiEetbxaZ4uQkNS9tsdabwIuphxHeaZ7nOEaJg85CU8DUhR_ZlAl2588igMi_7vpucxsOr-vghv4qomNoOFDUXb-LDnwGvaZ-P_h1eV43VhC18h50AsNGuJg73Cf38YPW2YVN0e9miulW4TT_Ngt3xHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۳۵ مردم اسفراین خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450018" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
دوباره صدای انفجارها در کویت بلند شد
🔹
منابع عربی اعلام کردند برای چندمین‌بار طی ساعات گذشته مواضع نظامیان آمریکایی در کویت آماج حملات موشکی و پهپادی قرار گرفته است و صدای انفجارها به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450017" target="_blank">📅 23:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فردا صدای انفجارهای کنترل‌شده در برخی نقاط استان همدان شنیده می‌شود
🔹
سپاه استان همدان: به منظور انهدام کنترل‌شده مهمات به‌جامانده از جنگ رمضان، فردا حوالی ساعت ۵ صبح در محدوده‌های صالح‌آباد، روستای زاغه و آبرومند بهار صدای انفجار شنیده خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450016" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a1a193cd.mp4?token=IWVEMwLLP0tjx36rLYyTsu1frlM_45Xd4cYSBEHdb625uZOMC1CFXLbYzjmqZhh1rv52h83Q6yQhOh9AwISuwMpO1UI8jVng7yrJAWjbp_HIoWDwezlotJF7jYPi7J0F-AtGJ0lPAcbO1kdWQGYXMMmhl6G0TQwEdIqFV1v9hsD5x0xDXcF12Hzmzf6q5niWZxMWijhTraY6VCxwYVzg9-wKYNKzqykW9Z4JQ5MtDzwvB4Yr3uqamQAhd84a_M7MAY3vHAyRcdW7lX94HRJe4mARZ5B3nPRM74mxUGeo26z9tn2-h3sE98ooZF_yY6RGmAqgO3OtgSlhoUZ4eIQFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a1a193cd.mp4?token=IWVEMwLLP0tjx36rLYyTsu1frlM_45Xd4cYSBEHdb625uZOMC1CFXLbYzjmqZhh1rv52h83Q6yQhOh9AwISuwMpO1UI8jVng7yrJAWjbp_HIoWDwezlotJF7jYPi7J0F-AtGJ0lPAcbO1kdWQGYXMMmhl6G0TQwEdIqFV1v9hsD5x0xDXcF12Hzmzf6q5niWZxMWijhTraY6VCxwYVzg9-wKYNKzqykW9Z4JQ5MtDzwvB4Yr3uqamQAhd84a_M7MAY3vHAyRcdW7lX94HRJe4mARZ5B3nPRM74mxUGeo26z9tn2-h3sE98ooZF_yY6RGmAqgO3OtgSlhoUZ4eIQFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: نمی‌شود که آمریکا هربار بیاید تجاوزاتی انجام دهد و دوباره ما را دعوت به مذاکره کند
🔹
آمریکایی‌ها در هر اقدام علیه ایران باید به این نکات فکر کنند؛ این مسیر شکستی مجدد برای آمریکا رقم خواهد زد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450015" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a1c41c78.mp4?token=PB1sd9uAysJ6nMv3WLA4nnd5GDfzW10Fz-rUzpCXYk0NvGqLLPiYJyFvCBdYeasBOHru4vZzz0sI31sNj39TwZiH2DqtLBYDcgC4YQLz0xtxHPir_baGNsk3RtKSMukGdmxb0hmb42Dsiz4i_Ld8z2To22oz_vXacE_qmUE1hB_6y6hf7_dJ4uitP8LBrGxZYue1O4Glo77SxJ_6pUBiNKJsVfJWzluvsTzsSfsdQXVCTUYFNMpnFM8kWnMZWynpFSZ6p2oyJaNsLCXTOTWlnHK9xZ3QD7_wgQsTTaKrttA068aBmEio9P9Y8y5fkoVOdjg-Y2LEQp_HjIzmTKlbew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a1c41c78.mp4?token=PB1sd9uAysJ6nMv3WLA4nnd5GDfzW10Fz-rUzpCXYk0NvGqLLPiYJyFvCBdYeasBOHru4vZzz0sI31sNj39TwZiH2DqtLBYDcgC4YQLz0xtxHPir_baGNsk3RtKSMukGdmxb0hmb42Dsiz4i_Ld8z2To22oz_vXacE_qmUE1hB_6y6hf7_dJ4uitP8LBrGxZYue1O4Glo77SxJ_6pUBiNKJsVfJWzluvsTzsSfsdQXVCTUYFNMpnFM8kWnMZWynpFSZ6p2oyJaNsLCXTOTWlnHK9xZ3QD7_wgQsTTaKrttA068aBmEio9P9Y8y5fkoVOdjg-Y2LEQp_HjIzmTKlbew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیوند عاشورا و انقلاب در شب پایانی محرم گناباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450014" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ac0fafe5.mp4?token=RZJvxl1e0IcLh-l2DaISXW6018Dv7ZnoWUDl27qkB4OdjkghmkVsHtzOZrTTym4OiLvk1Ker0rZS_6Pxgw7mBA3uYXtwpvENTLhAQHYHoMjc67Nd1mv2qwP6LaEIiR7Lb4-WHF40XX2ADaN9RiACAu7EBLjP4_FyvS9zWtWE5NBMqG-Atz1xVILgNjMyj87oB59UZexSFGDPFc8tYGDMT8YbbbybuIOq2rOv7j7opGjdTFTVFSb6mZ2T8bfwDHf8RZktnrliEW1iqlpAXy9hbvtvGs4bjZCzF8MLYb9yuUPrOTNRJG3LNfG3ZZsyJCma_jwfuJecDImOrCTDIKn0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ac0fafe5.mp4?token=RZJvxl1e0IcLh-l2DaISXW6018Dv7ZnoWUDl27qkB4OdjkghmkVsHtzOZrTTym4OiLvk1Ker0rZS_6Pxgw7mBA3uYXtwpvENTLhAQHYHoMjc67Nd1mv2qwP6LaEIiR7Lb4-WHF40XX2ADaN9RiACAu7EBLjP4_FyvS9zWtWE5NBMqG-Atz1xVILgNjMyj87oB59UZexSFGDPFc8tYGDMT8YbbbybuIOq2rOv7j7opGjdTFTVFSb6mZ2T8bfwDHf8RZktnrliEW1iqlpAXy9hbvtvGs4bjZCzF8MLYb9yuUPrOTNRJG3LNfG3ZZsyJCma_jwfuJecDImOrCTDIKn0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های یک کودک فرانسوی پس از گل اول اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450013" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8547bb3b0b.mp4?token=IxgQ8MFLbmir3dsPGOh9ZN-Pgm-SYyx0Pml3Xy2ZCzW5BkMEDqxgS5NDqaDrWbHtRNbXvCt0kX2E-iOunH4INCHgCn6hcUijC5sYwib5-Ajmd5l0uPk4qtqBEFQQXmWrESahrekT13DZ5pWMP9asx2EaOBurBDoNH0FRlOm6Ciur-dSR3dH-GvWYU_Tc3r8qHYnWT_m8B2Gup5O8EOVbINZElCWxdnAKxShrbVV5_7-sU6Ci0FtKJpS790bXzx4yhgCM8uvZNc85FaLpwishidQkGfL9sX9CLFSIyetGaZHdX794wRuHa8fB0Ufwm88omBfT3AqIAAMtzFxIjsrqLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8547bb3b0b.mp4?token=IxgQ8MFLbmir3dsPGOh9ZN-Pgm-SYyx0Pml3Xy2ZCzW5BkMEDqxgS5NDqaDrWbHtRNbXvCt0kX2E-iOunH4INCHgCn6hcUijC5sYwib5-Ajmd5l0uPk4qtqBEFQQXmWrESahrekT13DZ5pWMP9asx2EaOBurBDoNH0FRlOm6Ciur-dSR3dH-GvWYU_Tc3r8qHYnWT_m8B2Gup5O8EOVbINZElCWxdnAKxShrbVV5_7-sU6Ci0FtKJpS790bXzx4yhgCM8uvZNc85FaLpwishidQkGfL9sX9CLFSIyetGaZHdX794wRuHa8fB0Ufwm88omBfT3AqIAAMtzFxIjsrqLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450012" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd391abf5.mp4?token=jxIklc71zTqZhFAWMemXscJSr1ThSdoukdozKsm0oCjnnXtWO0s0K0uMgTn7X6Op1GN8jYC8d2vzzQBaVlHKPfczl6tB8DiVjhFaJ4OMH_vmADtgmUyhIMB83BjsWLJc8QVPk7gfhHQ_qj9o7s58NBndHe2a8hdRTHAkl6kTjo5wt4iOO6-g1a0OW_RmkGgLWClGtpZaZlBAWTQLNDPw45Y650GNddDPqRXeXKhoP0crh6XJnVcWCp379UMyQjwcJKP88RzBdv72c5WT9M79k2YEU2bSmDJKSfhc2uKhq6g9GBL6qKMlFJBl2LBHckei4ymvVaq6Bh91dc8gsNYJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd391abf5.mp4?token=jxIklc71zTqZhFAWMemXscJSr1ThSdoukdozKsm0oCjnnXtWO0s0K0uMgTn7X6Op1GN8jYC8d2vzzQBaVlHKPfczl6tB8DiVjhFaJ4OMH_vmADtgmUyhIMB83BjsWLJc8QVPk7gfhHQ_qj9o7s58NBndHe2a8hdRTHAkl6kTjo5wt4iOO6-g1a0OW_RmkGgLWClGtpZaZlBAWTQLNDPw45Y650GNddDPqRXeXKhoP0crh6XJnVcWCp379UMyQjwcJKP88RzBdv72c5WT9M79k2YEU2bSmDJKSfhc2uKhq6g9GBL6qKMlFJBl2LBHckei4ymvVaq6Bh91dc8gsNYJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر آمریکایی‌ها فکر می‌کنند با انجام محاصره می‌توانند کاری کنند که ما درخواست مذاکره کنیم اشتباه می‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450011" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c11b6dc.mp4?token=lqe7SvjFVgHgJ8u5S6UHV9s588f7N9ULWaiOXbKBpSJRfDctg6sG_FXxRRtGmLCSzATVMVL9aqpJtxTYDi4QIGOTs5tihEsAnoW4Sfst54DYmMd73paHLrQpyqcBlHwmUhMfhFact3lLg5IFTNx_jedremj6RroZiU_cAhQiIMuzGpFklNJv8xuL5R_wk4ZQpMScX-i90Dfnr2CGGNr7lQwzXErPBbbX76iSnKfGJw97wMhv2hrEO9rGDkv14egoBWrGgAFxTylZMoWxuzeRjWB30A6IPmrSAXE7jSyAcjOyaIrjR_tzsflb6e0WGsMUHzhpdGktHXNyD-U5VUVGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c11b6dc.mp4?token=lqe7SvjFVgHgJ8u5S6UHV9s588f7N9ULWaiOXbKBpSJRfDctg6sG_FXxRRtGmLCSzATVMVL9aqpJtxTYDi4QIGOTs5tihEsAnoW4Sfst54DYmMd73paHLrQpyqcBlHwmUhMfhFact3lLg5IFTNx_jedremj6RroZiU_cAhQiIMuzGpFklNJv8xuL5R_wk4ZQpMScX-i90Dfnr2CGGNr7lQwzXErPBbbX76iSnKfGJw97wMhv2hrEO9rGDkv14egoBWrGgAFxTylZMoWxuzeRjWB30A6IPmrSAXE7jSyAcjOyaIrjR_tzsflb6e0WGsMUHzhpdGktHXNyD-U5VUVGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: پاسخ‌های ما به تجاوزارت آمریکا نباید متناسب باشد؛ باید چندین‌برابر و پشیمان‌کننده باشد  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450010" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14731ed869.mp4?token=KKQNa4WDSwX-ILXHj6xzhhB8-OieX3ouhEkzGgJPxLxURvDor1ANIGnZa4UgdcGaC5GEcH-qTKvpfkUvt3U6KhMGe0vhVfQKubaMKQfdeBaXmHRpwS7vZO021OJMVh2r-C5bQhhI_TYvErEzu1w51b-_c0bdfxWBCvir9Xoi62RIjWJoLG5nIvBLCR_1RXpVJKO5HOU0PMFwqu_JLESYYUgE1cr9v9ih2-xf6Y5CsD2y1S8Djhocuo5PMOPKkqQt4b4BxuQ6ewg33rjmDZw1tQ_UOX_ilIOwuYD-Ki3sg5d4_RrX5TCF4_XOjOnxQKHx_qtN1hIPojMhan-C7yVYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14731ed869.mp4?token=KKQNa4WDSwX-ILXHj6xzhhB8-OieX3ouhEkzGgJPxLxURvDor1ANIGnZa4UgdcGaC5GEcH-qTKvpfkUvt3U6KhMGe0vhVfQKubaMKQfdeBaXmHRpwS7vZO021OJMVh2r-C5bQhhI_TYvErEzu1w51b-_c0bdfxWBCvir9Xoi62RIjWJoLG5nIvBLCR_1RXpVJKO5HOU0PMFwqu_JLESYYUgE1cr9v9ih2-xf6Y5CsD2y1S8Djhocuo5PMOPKkqQt4b4BxuQ6ewg33rjmDZw1tQ_UOX_ilIOwuYD-Ki3sg5d4_RrX5TCF4_XOjOnxQKHx_qtN1hIPojMhan-C7yVYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: نیروی دریایی سپاه طبق تفاهم‌نامه در شمال تنگه هرمز مین‌روبی را انجام داد اما مسیر قدیمی تنگه هرمز دارای مین بود
🔹
بعد از این یک مسیر جنوبی جدید در نزدیکی خاک عمان باز شد که باعث شد حاکمیت ما در تنگه هرمز نقض شود. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450009" target="_blank">📅 22:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450008">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450008" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450007">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47e784745.mp4?token=ANiSoMYEj_eMOSrrQbzlo_fJgWcCY9Hy81V7t3iNhmKXdtVxJVACFNBA2OIl4YKof5RLjhCzhf6UUm8Ekxjv-ckZSduP53TpGBrphRwgbT03n-y0juogS2d1JTCQKaOhAhn-U2dHF1t5qKi2wW9E7s2vLYJ0DcF92zLSDFUZOJT3RwemxPt1sNrl6gUHXZh4mTEn1gP_qE53018QXpz2h2nwJX7A9Y9iu2hUsIijHaDgrlAzHAObqngCf384L0_DZmyPOaXYWs4TyP05NRI2twS-OwnxJ-BW_b_ss54WgVHhuUcPsqztuqF8xz9F1jVASBLIHPY4f-vV5F4vKry_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47e784745.mp4?token=ANiSoMYEj_eMOSrrQbzlo_fJgWcCY9Hy81V7t3iNhmKXdtVxJVACFNBA2OIl4YKof5RLjhCzhf6UUm8Ekxjv-ckZSduP53TpGBrphRwgbT03n-y0juogS2d1JTCQKaOhAhn-U2dHF1t5qKi2wW9E7s2vLYJ0DcF92zLSDFUZOJT3RwemxPt1sNrl6gUHXZh4mTEn1gP_qE53018QXpz2h2nwJX7A9Y9iu2hUsIijHaDgrlAzHAObqngCf384L0_DZmyPOaXYWs4TyP05NRI2twS-OwnxJ-BW_b_ss54WgVHhuUcPsqztuqF8xz9F1jVASBLIHPY4f-vV5F4vKry_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: در یک ماه گذشته هیچ مذاکره‌ای با آمریکا نداشتیم  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450007" target="_blank">📅 22:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450006">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18feac6532.mp4?token=dq9Rg-YDL-6_2d3TWwCTQU2iOokTSGSFEll-ISB2bOIMhj_LHxdnurIe1SpMnNJXGGomxTcq8uF7f7dDESWysqkW_EPKyYXRqCbrOgxqbKAI_ic9PbZhkXMFhiWDPddn5xmRO3AeASkwDL0DGQUnab-9nPhPNbjxKXl-glv0pyq4tE-43QjCQ9jp_sMqbfKOhBUYcFoKXwWEMlRaFh1k37VGJafrNfsuK64T2naKqJndn65BP4Pd5gSAkQqDgqaCHswbPyVmq7_AGlUJRYKeQHgUpvUJ5R-CUKtBTjdAFjHEExiCzDaxSsYuFV5MO-OBM9ajwetTZ5LAjlq3yeHNqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18feac6532.mp4?token=dq9Rg-YDL-6_2d3TWwCTQU2iOokTSGSFEll-ISB2bOIMhj_LHxdnurIe1SpMnNJXGGomxTcq8uF7f7dDESWysqkW_EPKyYXRqCbrOgxqbKAI_ic9PbZhkXMFhiWDPddn5xmRO3AeASkwDL0DGQUnab-9nPhPNbjxKXl-glv0pyq4tE-43QjCQ9jp_sMqbfKOhBUYcFoKXwWEMlRaFh1k37VGJafrNfsuK64T2naKqJndn65BP4Pd5gSAkQqDgqaCHswbPyVmq7_AGlUJRYKeQHgUpvUJ5R-CUKtBTjdAFjHEExiCzDaxSsYuFV5MO-OBM9ajwetTZ5LAjlq3yeHNqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: درحال حاضر ما هیچ تعهدی از جمله دربارۀ تنگه هرمز نداریم
🔹
هرکس از ایران درخواست می‌کند که جریان عبور از تنگه هرمز را به حالت عادی برگردانیم درخواست نابه‌جایی دارد.
🔹
شاکلۀ اصلی تفاهم پایان جنگ علیه ایران و دیگر جبهه‌ها بود که هم در خاک ایران…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450006" target="_blank">📅 22:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: آمریکا در صورت تکرار تعرضات با پاسخ‌های غافلگیرکننده مواجه خواهد شد.
🔹
مقابله‌به‌مثل و تنبیه متجاوز تا وقتی جنایت آمریکا ادامه دارد استمرار خواهد یافت. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450005" target="_blank">📅 22:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450004">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سوله‌های نگهداری تسلیحات، قطعات شناورها و هواگردهای دشمن و رمپ استقرار پهپادهای MQ9 هدف موج سوم قرار گرفتند
🔹
روابط عمومی سپاه پاسداران: رزمندگان غیور نیروی دریایی و هوافضای سپاه در موج سوم عملیات نصر۲ با رمز مبارک یا زین‌العابدین(ع)، طی عملیاتی همزمان موشکی…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450004" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوله‌های نگهداری تسلیحات، قطعات شناورها و هواگردهای دشمن و رمپ استقرار پهپادهای MQ9 هدف موج سوم قرار گرفتند
🔹
روابط عمومی سپاه پاسداران: رزمندگان غیور نیروی دریایی و هوافضای سپاه در موج سوم عملیات نصر۲ با رمز مبارک یا زین‌العابدین(ع)، طی عملیاتی همزمان موشکی و پهپادی در ساعاتی قبل چندین سوله نگهداری تسلیحات و قطعات شناورها و هواگردهای دشمن در پایگاه شیخ عیسی بحرین را منهدم کردند.
🔹
همچنین با حمله به رمپ استقرار پهپادهای MQ9 دشمن در پایگاه علی‌السالم کویت تعدادی پهپاد را منهدم و یا به آنها خسارت وارد کردند.
🔸
این حملات در پاسخ تجاوزات بعد از ظهر امروز ارتش کودک‌کش آمریکا در حمله به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح ما بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450003" target="_blank">📅 22:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450001">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMuE0fZEgOoYmPsD8HTvVw6ZPgwXr56XwehkKrwcQEDrmfeFBtjWYS9DjgB5pKng2SbBxuJz7Bqaj2XzV8rcyfy09erAwfp0pNn8iCH90WkoecJcr-3HIz_v09_e5JjgQ-ExuCXV0Svl2hj5yD6ph0JNLw8D_nbpVZVZ8sNXOCW6AsZbNfFtu6gxCA4WZuin_7LhdpbaOAv_6DMJmkBotKiUq335HeP34yD0cdm3HIGRqRXGBVuY3B6xM5t_Eok6mvVunKlzlugW91i5HvGHL930rzBjGx20hbyAjEJaP7BSc0ALIRk-ZxyamIotHaFq5R3ok8I-Bkegs296WaIH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مجلس یادبود رهبر شهید انقلاب از طرف رئيس دفتر ایشان
🔹
این مراسم ازطرف رئیس دفتر رهبر شهید، آیت‌الله محمدی گلپایگانی در روز پنجشنبه از ساعت ۱۷ تا ۱۹ در آستان امام‌زاده علی‌اکبر(ع) چیذر تهران برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450001" target="_blank">📅 22:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450000">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebab1bac8.mp4?token=qTrMeqi3GUIrvT-D8EJnZ8VaI7BHyO9tsPTw8Vv3E_s-9VaROwjTUUtQo1IpJ2QBs2Fx4R9EFERlshT7uFNAm2Y4OqRjpdQ_2ooMVbxsR_5ZPplODaCPwSHcg-dEgWDlHGtnRlQEA0LGnDsPDCC0VVfYNjP7I7LWS-bzlcVnDWPkEFttgdVH-FDGBiyq9nXhdMQTUaWOcMA93xyycULLxrVS1quM-HJyHrXt5JzPWyEmlpI27_0LwWeU1-pEGbXY5D_JuH4atuWqtkpSzI-WBOURsqv1zctTLtLE4s2w4rB6ibwToc4f1Nzek7zfOLdDfuyd23gmQZf8BemW0CpFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebab1bac8.mp4?token=qTrMeqi3GUIrvT-D8EJnZ8VaI7BHyO9tsPTw8Vv3E_s-9VaROwjTUUtQo1IpJ2QBs2Fx4R9EFERlshT7uFNAm2Y4OqRjpdQ_2ooMVbxsR_5ZPplODaCPwSHcg-dEgWDlHGtnRlQEA0LGnDsPDCC0VVfYNjP7I7LWS-bzlcVnDWPkEFttgdVH-FDGBiyq9nXhdMQTUaWOcMA93xyycULLxrVS1quM-HJyHrXt5JzPWyEmlpI27_0LwWeU1-pEGbXY5D_JuH4atuWqtkpSzI-WBOURsqv1zctTLtLE4s2w4rB6ibwToc4f1Nzek7zfOLdDfuyd23gmQZf8BemW0CpFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/450000" target="_blank">📅 22:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449999">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرهایی درباره وقوع چند انفجار مهیب در ریف دمشق
🔹
منابع سوری گزارش دادند این انفجارها در شهر «صحنایا» رخ داده و هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449999" target="_blank">📅 22:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449998">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9898241c.mp4?token=pw01MEszqo6Nxu6-Sbn6tKyZba3FxHntPfp6_CzjLPk5sU9nkXLJFeFkHopbXy9XjSxvc97N7B1ZgRNCOXLrz_08cwp0c0utsAxKx0MSR1GbQ8fSo2qRMEiNaAYEuxgMzg-mB0KoMc38XgeL0ERI5E9AIWxpkGoMxhkawYO3TfSVIYXf7tAC-tGkX1TOAz5HLf3bieg5wdbPnFERcIVBHduKIs_gGHyLG0YQ5aGsz_WhHlmT2rCZPJzbMQyyU798Y-WJ2qr40TSvfFWRxH_xq-wq-LWC54TlnRxPyOBERQF6LG1How2zSydgllKoZ_IlUn85DId32eo0CQ85lenG1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9898241c.mp4?token=pw01MEszqo6Nxu6-Sbn6tKyZba3FxHntPfp6_CzjLPk5sU9nkXLJFeFkHopbXy9XjSxvc97N7B1ZgRNCOXLrz_08cwp0c0utsAxKx0MSR1GbQ8fSo2qRMEiNaAYEuxgMzg-mB0KoMc38XgeL0ERI5E9AIWxpkGoMxhkawYO3TfSVIYXf7tAC-tGkX1TOAz5HLf3bieg5wdbPnFERcIVBHduKIs_gGHyLG0YQ5aGsz_WhHlmT2rCZPJzbMQyyU798Y-WJ2qr40TSvfFWRxH_xq-wq-LWC54TlnRxPyOBERQF6LG1How2zSydgllKoZ_IlUn85DId32eo0CQ85lenG1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449998" target="_blank">📅 22:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449997">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoFKsWuFtvoSGBLMsfiUUlD7GRfaEgxvbuqCmnYu0vc-zB4qAOockB9X_vCJTCTBHacxSfXgIQAzxTjfi8ojvuPQq3i6Fb_H_Kj-DN5TZsAjYNYS2qxD4HN264DfO7AW-cXavllZoeq02U3F96Ijjt1HFSXvfOr3EKokdZ7wVsCJelYcPZQR38PgJPwMhEPz5fxk8xn4QiJxEd8V7lPmIEC1HncPnwegqXyfq4kbkD8S-bZerJPIGD8-yRx9GB6I0vXBsFdqIW76BtuiBJDtpyvf4UNWr6jOP2d71K7Zo3zHiESkzdJoTUFZKC_HPy4NjktOKVGhgddHdEFMeznNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسخیر فهرست گرم‌ترین شهرهای جهان توسط شهرهای خوزستان
🔹
بررسی جدیدترین داده‌های پایگاه بین‌المللی پایش هواشناسی نشان می‌دهد که در ۲۴ ساعت گذشته، از میان ۱۰ شهر گرم جهان، ۶ شهر متعلق به استان خوزستان بوده‌اند.
🔸
بستان: با ثبت دمای ۵۱.۶ درجه سانتی‌گراد (رتبه دوم جهان و گرم‌ترین شهر خوزستان)
🔸
اهواز: با ثبت دمای ۵۰.۸ درجه سانتی‌گراد (رتبه سوم جهان)
🔸
امیدیه: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه پنجم جهان)
🔸
صفی‌آباد دزفول: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه ششم جهان)
🔸
آبادان: با ثبت دمای ۵۰.۲ درجه سانتی‌گراد (رتبه هفتم جهان)
🔸
بندر ماهشهر: با ثبت دمای ۴۹.۴ درجه سانتی‌گراد (رتبه نهم جهان)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449997" target="_blank">📅 22:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cace50a0b8.mp4?token=Ai0yPzpghmKpTkcebMZDzsVGZk0NdgKMfQ4lL0sQJZwhXgMzgmu7H_B50QyZ9RaJvhFb9q6ES05pkYjRNt2x41c9xrW0rWPTkjFIk7RlnjtXhBFedxFQ7LBwdK7R_hvxCNfPyT7s_9RsXSXsY7h8rPlpHeYXLe4QaF8DLyZH-4ZW8Fb42JXVDA9vnUT1Kb8rUzz0nSKC_5qDCmwT5XCFuDYrRSD43S6i7hUEtxdPLVn2iIxhQ7ie6m6pgHor5FW6XzrdFmuIXQgMzdR-UKgTVdSXSXuCEJJ5XuDp0kybpKBo26geFnW2nfea8MDLVK6CR_zqRx5f8nYZCqVP2qoOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cace50a0b8.mp4?token=Ai0yPzpghmKpTkcebMZDzsVGZk0NdgKMfQ4lL0sQJZwhXgMzgmu7H_B50QyZ9RaJvhFb9q6ES05pkYjRNt2x41c9xrW0rWPTkjFIk7RlnjtXhBFedxFQ7LBwdK7R_hvxCNfPyT7s_9RsXSXsY7h8rPlpHeYXLe4QaF8DLyZH-4ZW8Fb42JXVDA9vnUT1Kb8rUzz0nSKC_5qDCmwT5XCFuDYrRSD43S6i7hUEtxdPLVn2iIxhQ7ie6m6pgHor5FW6XzrdFmuIXQgMzdR-UKgTVdSXSXuCEJJ5XuDp0kybpKBo26geFnW2nfea8MDLVK6CR_zqRx5f8nYZCqVP2qoOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: انتقام باید به‌شکلی باشد که مردم از آن راضی باشند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449995" target="_blank">📅 22:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449994">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287e492c12.mp4?token=BQOmIenlRlys1nfLofWOrPdvqefxFUD9iMqj7pYZe9_xea3df8EpZEMv9ey-GBs3h09Osu14Gv0ts9GIYU35I63uDPqqcl-quXq1c6Os3Tot1PQszr7A_n8cDPDhhlO44PT4FhKsEZQQ3QPgAOehZ9s0onXtfLoh5hJIdiNgxrmePUUOlWSS8ea1gLNazay2RNrye54tlZ6a_Lw3Eyaw4fwOFl9g8LPA63yYrRWizdzD-fJyjm2Kr9IvyFpSQCLN6GsL8HcCtVasZL7FaLfUoHuEAKFZPxkpNMRDTJir4mciY34Hy6BaCke69-0-Y8CjpChx2HAyjgdiUyH70G6-qqok4lP9Ylj2Ge9WjW0vl3Wto8_yxDnus-8P97LHyodx0-zkjues6vGUCh3-B1VuCL0ivSIwbRF1en7pMJfnuIx_JLvEyZbV0ZjRGUVtox6DOPNpGIhdU6Bwbi_QmQUTaAn2b8kA9evmmpc8_nAbi1s8NaYWmPQN2eaeXsArX_YcuUqC8hODkRTv5DpD2zJ2-SSwBcIIXprKjl9SaQcx2ZFy8B3POe_4LsTp_W8NBYt6DCIZZR4TkNLa-m72kDkeDeqIUc1UfyIzeBS0oNmehL8150vh8elrMXQhUEmzcgACrW6N6m2NdgeQ44vL1SK9KjJuB6FnHfZTtXwIbAPwNr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287e492c12.mp4?token=BQOmIenlRlys1nfLofWOrPdvqefxFUD9iMqj7pYZe9_xea3df8EpZEMv9ey-GBs3h09Osu14Gv0ts9GIYU35I63uDPqqcl-quXq1c6Os3Tot1PQszr7A_n8cDPDhhlO44PT4FhKsEZQQ3QPgAOehZ9s0onXtfLoh5hJIdiNgxrmePUUOlWSS8ea1gLNazay2RNrye54tlZ6a_Lw3Eyaw4fwOFl9g8LPA63yYrRWizdzD-fJyjm2Kr9IvyFpSQCLN6GsL8HcCtVasZL7FaLfUoHuEAKFZPxkpNMRDTJir4mciY34Hy6BaCke69-0-Y8CjpChx2HAyjgdiUyH70G6-qqok4lP9Ylj2Ge9WjW0vl3Wto8_yxDnus-8P97LHyodx0-zkjues6vGUCh3-B1VuCL0ivSIwbRF1en7pMJfnuIx_JLvEyZbV0ZjRGUVtox6DOPNpGIhdU6Bwbi_QmQUTaAn2b8kA9evmmpc8_nAbi1s8NaYWmPQN2eaeXsArX_YcuUqC8hODkRTv5DpD2zJ2-SSwBcIIXprKjl9SaQcx2ZFy8B3POe_4LsTp_W8NBYt6DCIZZR4TkNLa-m72kDkeDeqIUc1UfyIzeBS0oNmehL8150vh8elrMXQhUEmzcgACrW6N6m2NdgeQ44vL1SK9KjJuB6FnHfZTtXwIbAPwNr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار آمریکایی: از منظر عینی، هیچ تردیدی وجود ندارد که این آمریکا بوده که  توافق‌نامه تنگۀ هرمز را نقض کرده‌است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449994" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449993">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_TSwgiiG8GoL3LSHqh8VoTd8ecw0EYPPWIcX_2geu1xDhSfXpXiTAfg2t3xXP9z5VTPj39hkJP8QABACeaitLm6kgdl-k_V3Qs_DWuoEFhkFq9SAvLUfSwVBBzREXEe2wAo6CTcTAxCxUVm3LPJoiv5wiHmc95nJIQHVdEAUESDChZasfj2vJjwPZzdGJA4Hl8gdZfhfjKVP8XSELnbTBi5BUW5L3VLPKRzpjN_Bzxwfj61pSqbuz3pKV0YZ3NoLTNzCSAlY4pHTbwptnkFFEJJ3ZjbN1L_mgEGjUgSP8nq_3y6KBmTLGJRvqXQEsqYUM0PR3Uflk19jgSvtNTQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خون در برابر خون؛ جدیدترین دیوارنگاره میدان فلسطین اکران شد
🔹
دیوارنگاره جدید میدان فلسطین تهران با تصویری از ترامپ، نتانیاهو و خانواده‌هایشان رونمایی شد. این اثر با تأکید بر خون‌خواهی امام شهید و شهدای مظلوم جنگ اخیر، پیامی صریح درباره پاسخ به آمران و عاملان این جنایت‌ها ارائه می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449993" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEWJK6g-o2I9owDcMajrSbYKwoUr9ugTuITw6qQrz14d3Mmwv8A4aO_RGWjC33vDxvPE65o6y7AamCK4y0i4ZYDsJaPPLiHAnsBm-_WIOf89vI_koHcsTx30MC8vYUrKJUHKHvhUre13zChVFTLSiuXP5OCFc8hXxR-rI06OyPI9_OOufMEOPOmsUogFtaaW1ujKHEl4dzHFDsbIt9ERpK4V43AAEGaqeJ6KWIJaMkjTG7BL2eJV2qjZegDbJVeWD614PMEcGUF7UgYr1VbBzD3lzhskCX-zJkAqP_wUzeohbG_t-3FOoCbr0hex8Pc2VLCWrp0ZA7bQ3gcednurOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«خپارس» از شاخص صنعت خودرو پیشی گرفت؛ بازدهی ۵۹ درصدی سهام پارس‌خودرو
سهام شرکت پارس‌خودرو پس از بازگشایی نماد، با ثبت بازدهی ۵۹ درصدی، عملکردی فراتر از شاخص صنعت خودرو در بازار سرمایه به نمایش گذاشت و توجه فعالان بازار را به خود جلب کرد.
نماد «خپارس» از زمان بازگشایی تاکنون با رشد ۵۹ درصدی همراه بوده است. این در حالی است که شاخص صنعت خودرو در همین بازه زمانی حدود ۲۱ درصد افزایش یافته و سهام پارس‌خودرو با اختلافی قابل توجه، بازدهی بالاتری نسبت به میانگین صنعت خودرو به ثبت رسانده است.
این عملکرد، بیانگر اقبال سرمایه‌گذاران به سهام پارس‌خودرو و تقویت نگاه مثبت بازار به روند فعالیت‌های این شرکت است. هم‌زمان با اجرای برنامه‌های توسعه‌ای، افزایش تولید و بهبود شاخص‌های عملیاتی، «خپارس» توانسته جایگاه خود را در میان نمادهای صنعت خودرو تقویت کند.
تداوم روند مثبت معاملات این نماد، در کنار عملکرد عملیاتی شرکت، می‌تواند نشان‌دهنده افزایش اعتماد بازار سرمایه به چشم‌انداز پیش‌روی پارس‌خودرو و برنامه‌های آتی این خودروساز باشد.
@parskhodro_pk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449992" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/449991" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpXTIq1t2Vx4pJ5oHJH2-I0gB9rCAxME3Dwl-R39Xwi0n9H1i2rgX8DwVY29MSQ20mZWAO9adJVQ8kLyvU3i-lUCk2hkp3-G3hZY5iT0me8iCKcPJmM3S6Hm3q0cJfJvf-j31amNj9fE1PZOZHd_l6YN1OVX5xq0O_t7xcEyRO50_cEU3pxgek9KtyL6hsu2ExEh2LyTg9urgc8B5Nhx8y-_KMhLr5pEQrLwRM97pVTpjiy1fZNEnbtoYuyphiuLMUut2JgnfsryAJ5-nLKlZWFaCAB9rEjBKneWbv6bn3cHrw6GaXWzmxOb3b_a7z3LDSHTIdSAHScwUrvOXvMXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دبیر شورای‌عالی امنیت ملی: مقابل آمریکا هیچ نرمشی نباید نشان دهیم
🔹
باقری‌کنی: مسیر پیش‌روی ایران براساس  شاخص‌هایی که ازسوی مقام معظم رهبری ترسیم شده، روشن است.
🔹
دستاوردهای هسته‌ای و موضوع تنگه هرمز را همواره باید حفظ کنیم.
🔹
خون‌خواهی رهبر شهید، ایستادگی در برابر زورگویی و زیاده‌خواهی آمریکا و همچنین حفظ و تثبیت دستاوردهای کشور در صدر سیاست‌های ما قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449990" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d871bc1b91.mp4?token=lnzs2hoM_YZsy3icvITv88P_6D7Rqv1vcjDSaW0Yb6EGuAX2uUiInQRgjJHQ3z7mqVeaR1Ij8wK0EjhoVWNeDaYoYpQ-ZM_HyEoJIbRAIu3dVwbcYrdhi8Q4HVy8OJZggdAGU3Xvah0wQ3TJ-RdT08H-eh-Zr1lBx1qqX9cSBjDoYGPfcGJKyddIWJNX0oDwt5plJ4XURyFT6bo_GaeHR9bARhkM0wvbRbmnTBVmL_UfzN1U4jRylHDKnvGb9ye3_bBuYc2IvS93tB5FpFNIbbpULYTrVZS8BX5a63ezjU6uHIVHkTsaO2xzQP_ZT35FTx-nlZSZB9XLhcXHX8xTuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d871bc1b91.mp4?token=lnzs2hoM_YZsy3icvITv88P_6D7Rqv1vcjDSaW0Yb6EGuAX2uUiInQRgjJHQ3z7mqVeaR1Ij8wK0EjhoVWNeDaYoYpQ-ZM_HyEoJIbRAIu3dVwbcYrdhi8Q4HVy8OJZggdAGU3Xvah0wQ3TJ-RdT08H-eh-Zr1lBx1qqX9cSBjDoYGPfcGJKyddIWJNX0oDwt5plJ4XURyFT6bo_GaeHR9bARhkM0wvbRbmnTBVmL_UfzN1U4jRylHDKnvGb9ye3_bBuYc2IvS93tB5FpFNIbbpULYTrVZS8BX5a63ezjU6uHIVHkTsaO2xzQP_ZT35FTx-nlZSZB9XLhcXHX8xTuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دو روی سکۀ خوشحالی و ناراحتی وطن‌فروشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449989" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=EMv0ECL9zd1K5xWh4XSb5X_GkfFeG1s8V2Xe4XCq2gOYruy3pQ71DwVPeQ3QRUOj5PbgaCB4Va5FlcnQnFjujcvJL745xpfNelYYdCfZ8mVajqsjsVGpQIdxr3ikyqWS5Cdiaa54U35lD8xVe7q7aeUbv8HvV3K5pY45bJUA5UKAXDQ4be8ybtUU3qYtOuvaXvbr3eTuFqoVZvLJiTNhnN-N2ZzXTLCzTWoXH7jusa_zc3Y-lPDkCPM3O4aLCzu7yYv0NZwo9jNahY_pPp-N93B4Sv-sGTziSRtWYl5xzGb_VCUR9cpun67EktAYxNgJqJbca3Rdz1g7CuCbjruUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=EMv0ECL9zd1K5xWh4XSb5X_GkfFeG1s8V2Xe4XCq2gOYruy3pQ71DwVPeQ3QRUOj5PbgaCB4Va5FlcnQnFjujcvJL745xpfNelYYdCfZ8mVajqsjsVGpQIdxr3ikyqWS5Cdiaa54U35lD8xVe7q7aeUbv8HvV3K5pY45bJUA5UKAXDQ4be8ybtUU3qYtOuvaXvbr3eTuFqoVZvLJiTNhnN-N2ZzXTLCzTWoXH7jusa_zc3Y-lPDkCPM3O4aLCzu7yYv0NZwo9jNahY_pPp-N93B4Sv-sGTziSRtWYl5xzGb_VCUR9cpun67EktAYxNgJqJbca3Rdz1g7CuCbjruUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، تحلیلگر حوزهٔ مقاومت: نباید بگذاریم بمباران هیچ نقطه‌ای از ایران برای دشمن عادی شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449987" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌ ‌
🔴
برخی منابع عربی گزارش دادند پایگاه «شیخ عیسی» و ناوگان پنجم آمریکا در بحرین، هدف شدیدترین حملات موشکی قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449986" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است  @Farsna.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449985" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۲.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/449983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۹۰.pdf</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449983" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=fYoKj43h3-tgoL4apJIK5o_1E0k1c3RDclau8DnURF5Wva_EV4ryITVh1YBaGnY_txWUg63KC-Yt8eJYkF6blIS-l_UeKP_-5VbMKWzTQ5hyzk5Q9mB_D5SCrAPIkpns4WpXDT7-BcQerrxpqP9c1Ip0MmiXdRkd1l69ot261fAyjysWzo3R6W1mZ4dZCsu0f41PM9NUtHHv4EcmqhMGxxwPYdLqBOwGeTxzOp8o05wtOxxl7Cnh_Zu-CelCIgiaq9YqmcIGxSN83uwIxCraO_xF0dFTA6E2ieljVXAa65hW4lfaPevG_o8X4__qFHIME4eOcDEp0n1P7A9WW6wCyodqjfXWco169QMOk7bx7HEduQXsQKDHUo3qXq_T0lGhqosRHaaBv4pYb9J8NKoEtmIAguR7vrm51hhL7ufBGQWWyIMwk_mov5J_nwLus1ipDTqXr7VyGwnFRwM5CHOCBoRPmndlDb5liCdA5u21sgY_sdh2_sBjs9UZm1WyLgMCf5Mpsuzj_etSIc2uVlyKZEnZnxjksTU-hCd78f3GlExHL68xpgB76tTlw0b8JLjqO_nvfxzG5jKKcWWjIHyxVtHv_usaH_-qFUE2eHta2dnPu-BSVeXPDZFBoKIheWEiYcexqvsKbv6MkCp9EVRXRC3nksaGGOr9kOPG7ykkZWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=fYoKj43h3-tgoL4apJIK5o_1E0k1c3RDclau8DnURF5Wva_EV4ryITVh1YBaGnY_txWUg63KC-Yt8eJYkF6blIS-l_UeKP_-5VbMKWzTQ5hyzk5Q9mB_D5SCrAPIkpns4WpXDT7-BcQerrxpqP9c1Ip0MmiXdRkd1l69ot261fAyjysWzo3R6W1mZ4dZCsu0f41PM9NUtHHv4EcmqhMGxxwPYdLqBOwGeTxzOp8o05wtOxxl7Cnh_Zu-CelCIgiaq9YqmcIGxSN83uwIxCraO_xF0dFTA6E2ieljVXAa65hW4lfaPevG_o8X4__qFHIME4eOcDEp0n1P7A9WW6wCyodqjfXWco169QMOk7bx7HEduQXsQKDHUo3qXq_T0lGhqosRHaaBv4pYb9J8NKoEtmIAguR7vrm51hhL7ufBGQWWyIMwk_mov5J_nwLus1ipDTqXr7VyGwnFRwM5CHOCBoRPmndlDb5liCdA5u21sgY_sdh2_sBjs9UZm1WyLgMCf5Mpsuzj_etSIc2uVlyKZEnZnxjksTU-hCd78f3GlExHL68xpgB76tTlw0b8JLjqO_nvfxzG5jKKcWWjIHyxVtHv_usaH_-qFUE2eHta2dnPu-BSVeXPDZFBoKIheWEiYcexqvsKbv6MkCp9EVRXRC3nksaGGOr9kOPG7ykkZWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، تحلیلگر حوزۀ مقاومت: استراتژی چشم در برابر چشم دشمن را متوقف نخواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449982" target="_blank">📅 21:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl8nsvq5-cXOz5nIb1uikxkIDI3Xf2UjDAyQgvzumNkNqEG_4uFlCyL8pMt5HezryRZEpMQbN0tW7LeUeBenGAyRHY-5V6o_OWnmFH3-88Q-IjGGPTQEsEacIB0TYZNf4HRscDDNCwORYSn3EL_L2cSUlB99OeT-i9a0d7wZtrgeNWMo5xN02Gvc-skkzB85TFiQ7_o10JF1917G7qXLf_IHqn8H7l1i_vXchBf51F28KS-Vn47oCyyKCjC67ZBU-59h508kogB048r92CwvEo-XYt4jxXYn1QaRHkLctEVQHeTLyWDmYFxeqOR6J_OKKGgiT4reyc92XHChERJX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدایی منیر از استقلال قطعی شد
🔹
جوردی پاسکال، وکیل اسپانیایی منیر الحدادی در گفت‌وگو با فارس اعلام کرد باشگاه استقلال و این بازیکن برای قطع همکاری به دلیل مسائل خانوادگی و شرایط منطقه به توافق رسیده‌اند.
🔸
این درحالی است که ساعتی قبل یاسر آسانی، بهترین گلزن فصل استقلال نیز قراردادش با این تیم را فسخ کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449981" target="_blank">📅 21:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419ffd0214.mp4?token=P59_Q56ShB-N7UcQZqKWclpoq1Rd-tBLEKXjb2VCSmJf_FTT5w0Wzei7ZOohC_3SxS0RwVREyycLgXp2wz506FZSYW8ARnA44ziW4q1xOXxriH67azVBsVq6fDJ6RYjl38PbWGrNE20iaIXxfSD5LaPBmbKdQl8OCrsZcvuyqU4E7XHXq-ZRV99wz55ieBQJcKtd9fg-XZn1sP28vk41N_Aowm306xe96tG0IoYIOxbos3cFYBSgrlLZUQqPMahXP6ENKZv4OCWTVRHMD6mqf2ruCtIKtOha59aePxp7Bsq4s8O2mi5ue2YCENcmzusKHKgg4WBqQECrXHYB1hhueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419ffd0214.mp4?token=P59_Q56ShB-N7UcQZqKWclpoq1Rd-tBLEKXjb2VCSmJf_FTT5w0Wzei7ZOohC_3SxS0RwVREyycLgXp2wz506FZSYW8ARnA44ziW4q1xOXxriH67azVBsVq6fDJ6RYjl38PbWGrNE20iaIXxfSD5LaPBmbKdQl8OCrsZcvuyqU4E7XHXq-ZRV99wz55ieBQJcKtd9fg-XZn1sP28vk41N_Aowm306xe96tG0IoYIOxbos3cFYBSgrlLZUQqPMahXP6ENKZv4OCWTVRHMD6mqf2ruCtIKtOha59aePxp7Bsq4s8O2mi5ue2YCENcmzusKHKgg4WBqQECrXHYB1hhueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر عالی حرم رضوی: بابت برآورده نشدن انتظارات مردم در تشییع رهبر شهید عذرخواهی می‌کنیم
🔹
برنامۀ ابتدایی این بود که پیکر مطهر  به روی دستان مردم تا ابتدای بست شیخ بهایی بدرقه شود اما باتوجه به فشردگی زمانی این امکان فراهم نشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449980" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHTRGChpo_mBAKMZTOKhK3H2H-7VU6eRAIMSJNC-9RvA5KzsoMyVu_Z35tMf8nrykdIaxxwV6m44fx7q-CacbQ1IBrO4HA0s7NZnRokh4fKRE9Rxw_m0wh_K6x2cKZznWyGpebfU2TmV9mKScPH7RDBzmZCJFBItlzyvrkeT42zJA1FLtA0XbhwUiJZ4zs4c9CRslu0IM3alYUPSbeb67JYvitBx2utsx-ReexBp4x594XVCmw3Lo21PoUE0TpQRaQi0GiDcxYlI5AGonkawKAiuY1_FAt9fIAwUontI6Mf-1TPEzpNNhmU-DSYwwJHWneXBQ4-7oyolvagb0QfDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gvcnf9qDXYQtnWDCpxKB2aLyYknRnoCaomr2LyPPxkl7Y-cIFT0_0oAaZPXMiXBi5VmjmyXaj22I0OLqxCFXm-xnhvTjEqZVDRiaq8rTK5-yOFR0TZeqEJHJiXHOwmxHdnod1RQVRn34EHGEAEYfdWu_HqT76Kj9v5PVkXJanQR9loEFrsKLz5q3bwINrObi028dHsqZ0Cuksxzlo-PV5M1F0FKTgeWSEe6OezZMwXI6Oo5dxGJfFkgaSJbusID6Q4y_SuqvUe_yg5YUiV7eEilUBLSzykriOnMfuPovvalYrAYCUqexgA-UDffeBhT8lh4ROLtyVRpDHtnvvpXNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_lhL1LOalMjCCOnzbMpJytWGMxrHDduLjOWAUtTcd3wy9O8wJbWUXZj4L2myBmRKvWO0MNeQZZs3Q5ap1gJNJd0YHrfCzKro7pxPRcFUsSqLeHh_PGS68GqO1CAjaPmmoR1dYpDZXkLtcNrAbM-zc3TRHMhYAtfg2OWpOnVDcJhHEOOxlk0NipRCuDbIrkXL6709YuyRco2vNUNsfcOdX4lCR3odTm2XkU5dKEtmhBlaZOUd9EUPnwJWW-l4X8ndYCWw7GxAKxbbfSISGKzn8gxdtQHiLHYugPy5aT8gf8qytA7jCUGxYceLyeCUnH2U50zFFe22oYPNWTHcCFEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O92vNakSEGJqZRnf2IdLZoNIFJ0AQqzKZl8rvcDHWiHyClAyNsVqY_fXk1W-zUaCoKYmzbbsi7WJYM6j32scnO2HYxAPnS2Txx4yRlcJKUouptbjH_sQiOrch3yTqbwXN3SauLcXN5BsisF6CGVHHHSmpWS7341pdPQPS4sCZb-60wCQrug11VVYY6Wxdi_giGVbY5ej-fOjdbnB17Ff9I9GFDHKE-VCc4JQWfyG_I3v3K_QR5TiYxHqTqSuXWph_TAYY9MQ79hyXiyKL0zcgvnCESEHwmwi53CmuVki8gWApZ67OF0UgEGC5481F3cnnVgzYrLkuHRItiteQ341fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdFiMbiSpMy5DP0D9FDWN2GaC1Gf-APMlHTakbT0piT-zpUzt_u1FS43wK_19HinM4Ik0wUfTULp6KYkGCn-dBB3coCqggF85xaz4j9onZEmCYepklXdaFU8Y7ABkLTvWph5y9rNB2u3PWL8gwZqTaaHstos-t2Iy07sYkx9kd2OLozIk8-txsAR_WpHzNJkOceNb84bFgcIo09bJrU_Udze73KoOvSPWY24eD59t4MUMeiFAQmr5rtMH-KhFMfi3EY5Q5AG0nETHZySLpE0fbLULQp5zwB_qrCJ0l0YQqocGilwJTvZx81wsLqRdMT8k0A7R2XkU_5n2-n0m1hQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsuETFTk8g8CFBR91EZm-eVhx0q3cBtIVjQg0OGhO5Y3xThx70wE3ludnY5bNd_hqQ_ROdMzOPKvmdhpLX1mND9V9v0IlA7zCC2O1OfaTnLyhixS-1SsR2NWTB82BPVs_gAtlY8nIbm2CDTm17bIDOu2ShP_w2iySAYakc-HwiYPdpkc7I1843p8nY0LooNrkMeSKYAxdiNvB6Ef0J5noBG6TtG6TvWUP8eMERIdoT00yqjDBTO-1-zKoZKkMczKNK6Al1SCtGBo71sRvPKW2CX256QfsjCzR2FP2OaDlnILjifL13KV4-ipy0BwXdmJAELBKjrJp8AI6yVSZqa6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aM1sV7X8taiogSbEVRBjmPRL9bzKm-xd2as1SB1TsPKNsWx1um8blvNBPJO5NS0m3YDtCR-hOWLqKncagbLrbc9qsI7WezYsEBe1IgbIud1Git4Fj5U3s_HSKEfnBLN6MpPCtnssv46PRczOENDIRDlzqL_FH_SUslrr6TvuqPkMyDbnsR88t4mi-d9dkfVOP2Dvd5CkgMXxqF3XYpQ8Ekm7y-aoLJM-3GN2Wf2yzgLyggk8HsGWgdeMFVqVxLdpvjglN2J4OQcUm0CgykryB3lVrcsey5lZhRycr4paLNC54t1bNkGJtzAE11ac4ZjvYNMrCjWTIkRl23ckHD8_4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب در مصلای امام خمینی(ره)
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449973" target="_blank">📅 21:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادارات هرمزگان سه‌شنبه و چهارشنبه تعطیل شد
🔹
استانداری هرمزگان از تعطیلی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی این استان در روز سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه به‌علت مدیریت انرژی و افزایش دمای هوا خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449972" target="_blank">📅 21:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d977dee9b.mp4?token=VtQQXw_E2xc0EZ_Qlwau8HUSJtuMX7jzHQTdl9FuoH_zWhOyRmpqBY4UGVp5mcL2Kd9pBcriD4pH540xC9yr58bTOl7RHRBofpSpXkumLHRI6YLPau3eTT6pWx5AnQsyDOa7J0xrJFPuq5vXevfW0PTSBmL1cefoyr7-C5z28I-aMOOaVBCO-gjaMqtBVCevjeIDhSixTnuH-Ixbx3P1pQPOLMnYhdl5jWCt3s3jtawTd2y63pFm9x3-c3zKcfDqX8FOb2ySlKYfbX5TKTrcRnsDy_6Oj7nTJivoSaszQBT7gbqv88hGZ2rXSmZnx1Ls680gtQpYjgI5v6N1-2yFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d977dee9b.mp4?token=VtQQXw_E2xc0EZ_Qlwau8HUSJtuMX7jzHQTdl9FuoH_zWhOyRmpqBY4UGVp5mcL2Kd9pBcriD4pH540xC9yr58bTOl7RHRBofpSpXkumLHRI6YLPau3eTT6pWx5AnQsyDOa7J0xrJFPuq5vXevfW0PTSBmL1cefoyr7-C5z28I-aMOOaVBCO-gjaMqtBVCevjeIDhSixTnuH-Ixbx3P1pQPOLMnYhdl5jWCt3s3jtawTd2y63pFm9x3-c3zKcfDqX8FOb2ySlKYfbX5TKTrcRnsDy_6Oj7nTJivoSaszQBT7gbqv88hGZ2rXSmZnx1Ls680gtQpYjgI5v6N1-2yFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: مهم‌ترین اولویت دولت در شرایط فعلی توجه جدی‌تر به منویات رهبر انقلاب و امام شهید است
🔹
بدعهدی آمریکا برای ما قابل پیش‌بینی بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449971" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266e0d442.mp4?token=XA3z7F5UsHgTqvonm8hCRNkQiqja7rP16tnvY5IyBhReVqUtSZWT7s76xtBG498SgaVPU31OB5BNH5dRk5BTDYpsq-FU5l3t2oi9XiEosJlXpSn9ebAcY9li626ZwcMf7NF7UqT5lT_dWJ9NZ7t_jsqDvCqN4aJVx32fvyg07ChUAHwlJkLn8O7jixvw8UvqWb9W25nDPULmUal3N8_fnOFhbokRu2gsLDcn-n84GeY5IZIMOWUpJlyENlTNkozv2-fDffGCOYHHZSTnv5uWxj2SXYEZOC0EU0RmtBMRltKg72TQOHc-W2cP43uVK2-Jq4apiDIFukyqe5XrnSsCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266e0d442.mp4?token=XA3z7F5UsHgTqvonm8hCRNkQiqja7rP16tnvY5IyBhReVqUtSZWT7s76xtBG498SgaVPU31OB5BNH5dRk5BTDYpsq-FU5l3t2oi9XiEosJlXpSn9ebAcY9li626ZwcMf7NF7UqT5lT_dWJ9NZ7t_jsqDvCqN4aJVx32fvyg07ChUAHwlJkLn8O7jixvw8UvqWb9W25nDPULmUal3N8_fnOFhbokRu2gsLDcn-n84GeY5IZIMOWUpJlyENlTNkozv2-fDffGCOYHHZSTnv5uWxj2SXYEZOC0EU0RmtBMRltKg72TQOHc-W2cP43uVK2-Jq4apiDIFukyqe5XrnSsCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: فروش نفت در چارچوب‌های قبلی ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449970" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=Q7NyXiqGR-dcCjNPZV_4wZKBrfq9a3WKUJCHSVYWpFYEkQHbqyQHIlMwuOpDX_3oX-eIvgGw3bW4K5VoC9EOJ41igCb7MfunuRwb_2WY8RZ_sPPJdRmkxszBybajRf-mo8laMBZxk4h8IFBv43F0DFcsXriPpdX1BLP8ZanxWrwwBaTnxWOWdrEKiCSf5Wr76wFQEUl8MdJMsvOtn2yXX0eZ8C1keJKQs3NA9wKOIzcGvkc0wXO0qOb4Xur_QUPBWEplTtG_aNsHoHUTasS1rD6yUqFLG6e5aALc4Twa1B0fHwoZ3VclQras9WsaP_IWKIOh3aqMPLLS_qUOTmhv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=Q7NyXiqGR-dcCjNPZV_4wZKBrfq9a3WKUJCHSVYWpFYEkQHbqyQHIlMwuOpDX_3oX-eIvgGw3bW4K5VoC9EOJ41igCb7MfunuRwb_2WY8RZ_sPPJdRmkxszBybajRf-mo8laMBZxk4h8IFBv43F0DFcsXriPpdX1BLP8ZanxWrwwBaTnxWOWdrEKiCSf5Wr76wFQEUl8MdJMsvOtn2yXX0eZ8C1keJKQs3NA9wKOIzcGvkc0wXO0qOb4Xur_QUPBWEplTtG_aNsHoHUTasS1rD6yUqFLG6e5aALc4Twa1B0fHwoZ3VclQras9WsaP_IWKIOh3aqMPLLS_qUOTmhv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند؛ گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449969" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542073129e.mp4?token=Hr53gQ--sUQaSClyQnPeNaNKQPbLfP1Qz8XkOS10tJ3GOmpYLhq4K0Q_xO4e0KyFKbqttIxF6iQt_AuNAeOk18OVwccronIJ4PyN2cw12rXhxKlMRmV1sVR1JxzVgFt-ldSXMieFcaQJG0pB-bnCheZCiOJN9fO0SXh3GT78IcbG3ZERHpAsCY68g4P7a029ygZGqMDDkd7J3JHBvnWZgdMRzyRHxCCe37P0oErVdiUv1zbHZYPbB1uafO5YNNXziHOLjBdQ7PhoVdZIU_XXM_E7NyegDPVRUuB3owadIDGysQOr6mb3pHLMFnKLu4dZqDzTCI2RL5oGELz7iQmGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542073129e.mp4?token=Hr53gQ--sUQaSClyQnPeNaNKQPbLfP1Qz8XkOS10tJ3GOmpYLhq4K0Q_xO4e0KyFKbqttIxF6iQt_AuNAeOk18OVwccronIJ4PyN2cw12rXhxKlMRmV1sVR1JxzVgFt-ldSXMieFcaQJG0pB-bnCheZCiOJN9fO0SXh3GT78IcbG3ZERHpAsCY68g4P7a029ygZGqMDDkd7J3JHBvnWZgdMRzyRHxCCe37P0oErVdiUv1zbHZYPbB1uafO5YNNXziHOLjBdQ7PhoVdZIU_XXM_E7NyegDPVRUuB3owadIDGysQOr6mb3pHLMFnKLu4dZqDzTCI2RL5oGELz7iQmGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضاب، کارشناس صداوسیما: آقای خاتمی گفته توافق نباید مخدوش شود؛ حرف ما هم همین است اما کسی که این توافق را مخدوش کرده آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449968" target="_blank">📅 20:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
دوباره صدای انفجارها در کویت بلند شد
🔹
منابع عربی اعلام کردند برای چندمین‌بار طی ساعات گذشته مواضع نظامیان آمریکایی در کویت آماج حملات موشکی و پهپادی قرار گرفته است و صدای انفجارها به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449967" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d1312506.mp4?token=GOR225kx19kYDfzLQ_jcwmx-ac3MmCohnVL6hqIm1XKDTWegQWpR2Z0gvi3jGKKEp4r73L253qrbuI68Vj2GZoHMyy5GZ5i_m7XOYsljfDUmnpAl45L2W8y24Gz6teuQXlW-ll4HuOK_m8v2lZrfg9KAHAiyECyloKYno2b3sdLkC4lAlTi4c0Vd1nPHktD6Q0f4jVl6O9OSlAa62t_ZHvDlNEbVaCxXZPFjDBWkm_RFvlr-NMh5uqCG9jOQoqoTKF3CeTchExh_-JZBvgLK5cPAZQJGTQHSOncJx1WAr7QbrM7cJMrleDqdaQTX1SIGGWijugaa13fV0daFlBg3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d1312506.mp4?token=GOR225kx19kYDfzLQ_jcwmx-ac3MmCohnVL6hqIm1XKDTWegQWpR2Z0gvi3jGKKEp4r73L253qrbuI68Vj2GZoHMyy5GZ5i_m7XOYsljfDUmnpAl45L2W8y24Gz6teuQXlW-ll4HuOK_m8v2lZrfg9KAHAiyECyloKYno2b3sdLkC4lAlTi4c0Vd1nPHktD6Q0f4jVl6O9OSlAa62t_ZHvDlNEbVaCxXZPFjDBWkm_RFvlr-NMh5uqCG9jOQoqoTKF3CeTchExh_-JZBvgLK5cPAZQJGTQHSOncJx1WAr7QbrM7cJMrleDqdaQTX1SIGGWijugaa13fV0daFlBg3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔹
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449966" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=AlzwUC6zEgzm6LnwkRfHHLcOyHbIfoBM9-FWpnfvCSefufPbMk24C1ATeNyksp1W3nTQaj_oNO0ulsbOMFrie6LyjRBmuD9bbV4Wem58GetuXZCyT2d90h8hLJS_XOu0hcDONyJ7-b8SVj9hkFxznRY0zEcQjCpH5f0emAmdz-PXyVDiui9g_yGnJtjFYvKQSIQrOTSv-ol9u_qimeHHa4NFxiJ4xZC-ajxw-_eCe0ZujIbsnZHa7YxEVqIZJGp6dFZejVJkxxDJ3IqIA4vWnMNLXldlGS_1NjmEXN-flgSsP_PWX68GCjrFC_nkQ2x25kdtklUJo9BDQPOCqu_oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=AlzwUC6zEgzm6LnwkRfHHLcOyHbIfoBM9-FWpnfvCSefufPbMk24C1ATeNyksp1W3nTQaj_oNO0ulsbOMFrie6LyjRBmuD9bbV4Wem58GetuXZCyT2d90h8hLJS_XOu0hcDONyJ7-b8SVj9hkFxznRY0zEcQjCpH5f0emAmdz-PXyVDiui9g_yGnJtjFYvKQSIQrOTSv-ol9u_qimeHHa4NFxiJ4xZC-ajxw-_eCe0ZujIbsnZHa7YxEVqIZJGp6dFZejVJkxxDJ3IqIA4vWnMNLXldlGS_1NjmEXN-flgSsP_PWX68GCjrFC_nkQ2x25kdtklUJo9BDQPOCqu_oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
🔹
بی‌ادبی‌های ترامپ شایستۀ خود آمریکایی‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449965" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucGyMrBLiM6ol1ssPPXvD_woms0STAPoOkDYqwlSk33mZES2dJq8E6icEQuUaGuCfGdZKN6_HmgQizuxu2DbcyJOVPzrzto-N_UxI63ixH5AcJDlXoZyY1yzsM0SxFWk1bCxUl5QhmQeQuQsVlHWXoHsi9lL4liJRQEntUMYivFKH5zhResomeYEyEULsL_O0y2EqnGsxM1TRfpe5A_9GyFPndSRKkowkFwF0Iub3pFMlphApv_MkXPY0TOcl7AQR363pvCROE2xeuRM7vh67x6B_USMKTtOPyv-WLeqJCd5aTEkTJxhJmcFpUjJjd-SJ-FGCyUKGK_QkH3Yhio3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرقت آب از سهم دریاچهٔ ارومیه
🔹
دریاچهٔ ارومیه امسال بهترین وضعیت آبی ۶ سال اخیر را تجربه می‌کند، اما برداشت‌های غیرمجاز از آب رهاسازی‌شده سدها، روند احیای این پهنه آبی را تهدید می‌کند.
🔹
با وجود اینکه هیچ تخصیصی از سامانهٔ سد کانی‌سیب و تونل زاب برای بخش کشاورزی صادر نشده، برخی کشاورزان به‌صورت غیرمجاز از این آب برداشت می‌کنند.
🔹
رهاسازی آب از سدها یکی از مهم‌ترین ابزارهای احیای دریاچهٔ ارومیه است. این آب باید بدون مانع و برداشت اضافی از مسیر رودخانه‌ها عبور کرده و به‌ بستر دریاچه برسد.
🔹
کارشناسان منابع آب هشدار می‌دهند مجموع برداشت‌های غیرمجاز، با وجود محدود بودن سهم هر بهره‌بردار، می‌تواند حقابه ورودی به دریاچهٔ ارومیه را به‌ویژه در شرایط خشکسالی و تغییرات اقلیمی، به‌طور قابل توجهی کاهش دهد.
عکس: حامد حق‌دوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449964" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
اعلام آمادگی مقاومت عراق برای مشارکت فوری در حمایت از ایران
🔹
مسئول امنیتی حزب‌الله عراق: در صورت آغاز جنگ علیه ایران، گروه‌های مقاومت به‌صورت فوری و قاطع در حمایت از ایران وارد میدان خواهند شد.
🔹
از اقدامات یمن برای شکستن محاصرۀ اعمال‌شده از سوی عربستان حمایت می‌کنیم. یا باید همه امنیت داشته باشند یا همه از آن محروم خواهند شد.
🔹
سرکوب پیروان اهل‌بیت(ع) در کشورهای حوزه خلیج فارس و باندهای وابسته به الجولانی بی‌پاسخ نخواهد ماند. این حساب باز است و اشرار بی‌شک تاوان آن را خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449963" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
آژیرهای هشدار بار دیگر در کویت به صدا درآمد @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449962" target="_blank">📅 20:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نخست‌وزیر عراق: ائتلاف آمریکایی ۳ ماه دیگر کاملا از عراق خارج می‌شود
🔹
علی الزیدی در دیدار با برخی سفرای کشورهای اتحادیۀ اروپا: نیروهای ائتلاف موسوم به ضد داعش به رهبری آمریکا تا پایان سپتامبر آینده (هشتم مهرماه)  به صورت کامل از عراق خارج خواهند شد.  @Farsna…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449961" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">آسانی به‌راحتی فسخ کرد
🗣
یاسر آسانی قراردادش با استقلال را به طور یک‌طرفه فسخ کرد.
🗣
طبق پیگیری‌های خبرنگار فارس، وکیل ستاره آلبانیایی ساعتی قبل با ارسال نامه‌ای به باشگاه استقلال به دلیل آنچه عدم پرداخت بدهی معوق و شرایط منطقه خوانده، قرارداد را فسخ کرده.
🗣
این در حالی است که روز گذشته باشگاه استقلال اعلام کرده بود که آسانی به دلیل دیدار با خانواده‌اش ایران را ترک کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449960" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af162478.mp4?token=tg9aQGNzJOx5a5WVvFZKFa0U3W4q4Mr51koHNugZpi29Hgz3Gd-OgSnfxq9P4_CJmOl7mGBdqEphRGfqFsS_PWZhZU5JZYND-F9i3lcrL13seHV4H_Wfm2ypiZERoc313auvnt5aEFOtA_4IOxfYbEydCRTohF3m0JFMwHxSukPdE9R9DZy1WJ1PWd9LD694_dVJZJiuuYpqgmXaachahOVCyrat6UC0zZqAVH2R86UshsJn5lUVuiAmhyORDpgDIjXeaA5gmV6TJCiILOxFCox3T0urOmKvEVi2zIWjSNOxGGzKvj6_KRNCIrOBarp_7Mx4I9tsNEJvmqkvpgeu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af162478.mp4?token=tg9aQGNzJOx5a5WVvFZKFa0U3W4q4Mr51koHNugZpi29Hgz3Gd-OgSnfxq9P4_CJmOl7mGBdqEphRGfqFsS_PWZhZU5JZYND-F9i3lcrL13seHV4H_Wfm2ypiZERoc313auvnt5aEFOtA_4IOxfYbEydCRTohF3m0JFMwHxSukPdE9R9DZy1WJ1PWd9LD694_dVJZJiuuYpqgmXaachahOVCyrat6UC0zZqAVH2R86UshsJn5lUVuiAmhyORDpgDIjXeaA5gmV6TJCiILOxFCox3T0urOmKvEVi2zIWjSNOxGGzKvj6_KRNCIrOBarp_7Mx4I9tsNEJvmqkvpgeu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران سرنشینان یک برخورد دریایی در تنگه هرمز را نجات داد
🔹
بامداد امروز برخورد کشتی فله‌بر با یک شناور دیگر منجر به آب‌گرفتگی و دستور تخلیهٔ اضطراری یکی از کشتی‌ها شد که تمام ۲۳ خدمهٔ این کشتی با اقدام موفقیت‌آمیز ایران نجات یافتند و به قشم منتقل شدند. @Farsna…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449959" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMR-vStCJB6NOzWgXjKQYnf1NxB9KPLB0fTgv8YD3kUMoECzTqM6cHInSBgtLr84UDmwhlLwWhrBcor7wKmqJ_7acI9pOn8Ee0gOP_Lv5RBYs17mQ_AfDzGlQxExgD2PXsoIKJ4lfgfAw5KdUQtirarZXY24L40tWaSXnSKv1CLaYo-TdrMt1mhx3vfCOczR2tQpqpaNSqtNrv-TPUfxnZSJ44Rc4uqncC6ug96zfP45GxjgCLgKwtYkwwhIA79xOIZsPAWFX2anqURcSAlWpdUD8dJ5SdDberouIBLI8kSf1TI6AB7RyThrw8nVkVi4ChIT371mUBX8yI16GWkpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوهای ایران و عمان برای ترتیبات بلندمدت در تنگهٔ هرمز
🔹
روزنامه فرانسوی لوموند به‌نقل از وزیر خارجه عمان نوشت گفت‌وگوهای پیچیده‌ای برای دستیابی به ترتیبات بلندمدت با هدف تضمین آزادی کشتیرانی در تنگهٔ هرمز در جریان است.
🔹
این درحالی است که آمریکا برخلاف مفاد تفاهم اسلام‌آباد، با فشار بر عمان مسیر عبور کشتی‌ها در کرانه جنوبی تنگه را ایجاد کرد که در‌پی آن، ایران ۳ روز پیش تنگه را بست و بر کنترل مشترک آن با عمان تأکید کرد..
🔹
وزیر خارجهٔ عمان تأکید کرد این کشور مسئولیت ویژه‌ای بر عهده دارد تا همراه با ایران و جامعه بین‌المللی، برای دستیابی به سازوکارهایی عملی، پایدار و مبتنی بر حقوق بین‌الملل، در راستای تضمین آزادی کشتیرانی در تنگهٔ هرمز همکاری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449958" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در کیش
🔹
دقایقی پیش صدای چندین انفجار در جزیره کیش به گوش رسید.
🔹
طبق بررسی‌ها این حملات به حوالی اسکله مسافری این جزیره صورت گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449957" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bICzEXJYlY6GhAK2tNmx340frjLKGSpjb13Qw9kdmTearw8gX4ZLQaUrBuT3Cw2XlhDZV7khH5oK5ka2g-TDXMTPToSUg6_6gYE3s3HthwafQ962Y3HXojLor62HB5P0984WqED6B8HzplcVGaltsCugPeXr-f_5RKxm-Df-ygXVLgIyyJdiWyjPK0fzqLroQ0HvVVGbLaeO_4G73--WWwITu8pasb1m4oArTO9iankQt_j0I61MzH16EMx1q0qvEDea8ik2TC7I7sTqzdOiC5ntVSniDdSX_dl_1OqFX4I7gN_AcALF3VOK9vh26bRJOhR3xNLgge9bYQ5wmNwz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن یک پهپاد شناسایی متعلق به عربستان را سرنگون کرد
🔹
سخنگوی نیروهای مسلح یمن: موفق شدیم پهپاد شناسایی (Wing Loong 2)  را که در حال انجام مأموریت در آسمان استان «البیضا» بود را سرنگون کنیم.
🔹
نیروهای مسلح یمن برای مقابله با نقض حریم هوایی و حاکمیت کشورمان در کمین است و در برابر هیچ تجاوزی، دست بسته نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449956" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl5eu82MkQfg1OqThHlP7d5raQnBq7_gt7EF8xY-T3ZFkm4BqwGSVwklubnxctjmmMR_z95xt_MroCRDiHlYZcyMzakYsucLOghS8woLR00z39Z7OA7bRsHduqpQ80ZFGwK8ScXJgSHZfWICW_rwzxUHrO04g1regtyK8U_Py_Odjt_FUyzSsmSGA69y1W-stuMGbsa6nptms2oAg38n5dUl1hhM-KQARTYEdCFM2SoXhnKgEzqN91n0ZcEHvn0caWI9CgrPNjwevh0SRhg4kPzSB3qwz_lDA5f8TahXIteZoFTGATnokX_8yvrPrptJFiRnAzW0OD5T9_cUyEJogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلوگاهی که بازار نفت را می‌لرزاند
🔹
مؤسسه تحقیقاتی «اچ‌اف‌آر» اعلام کرده است که اگر دامنه درگیری‌ها از تنگه هرمز به بندر فجیره کشیده شود، امارات ناچار خواهد شد حدود ۳.۵ میلیون بشکه از تولید روزانه نفت خام خود را متوقف کند.
🔹
۲ سوپرنفتکش اماراتی که شب گذشته هدف موشک‌های ایران قرار گرفتند، از بندر فجیره حرکت کرده بودند.
🔹
این مؤسسه، فجیره را مهم‌ترین قطب انتقال کشتی‌به‌کشتی نفت امارات توصیف کرده و می‌گوید از کار افتادن این بندر، از نظر تأثیر بر بازار جهانی نفت، هم‌تراز با بسته‌شدن تنگه باب‌المندب خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449955" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فراجا: نیروی انتظامی در جنگ رمضان ۳۶۱ شهید تقدیم نظام مقدس جمهوری اسلامی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449954" target="_blank">📅 19:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyR8fQpv2omlotiwf2Pn1ADq5Pm4Uo8lIZQiP1neH-4LkIYRj094C_O-1S1iyZhKyFHGoreUA9DOaU6guiDtHLQiaiPy9M7u6Bya62GPH7_INnxM-__noKVxUO89A3k2R6JXx852tNlM7eEQfTkayeDtHoYdcOhmkuiRmYxkqm8Iz7tC81Z5rWH7uB9mBAyV6Stb33FA6mYGtJuPjkjio3AbjdAXKqxHW2K-QSNzZ-5dMBXYaI2wgrG_4fL72KwepJY5Xyf9pRKGC3WbELCX-tatG6UyF3FJRl_r2HTjnQSV1EQbV8AI3ja_Q53YlrexkAlaYoUqyLeVnhjqHnStRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ بانکی که مجموعا ۵۰۳۵ ملک مسکونی در اختیار دارند
🔹
طبق آمار بانک مرکزی بانک‌ها بیش از ۶۷۰۰ ملک مسکونی در اختیار دارند که برخی از آن‌ها به عنوان منزل سازمانی در حال استفاده است؛ این رقم به‌غیراز ساختمان‌های اداری، تجاری، باغ و زمین‌هایی است که در اختیار بانک‌ها است.
🔹
در این میان، بانک‌های سپه، تجارت، رفاه، ملی و اقتصادنوین ۵ بانکی هستند که بیشترین املاک مسکونی و در مجموع ۵۰۳۵ ملک را در اختیار دارند.
🔸
رئیس سازمان امور مالیاتی روز گذشته در نامه‌ای به بانک‌ها اعلام کرد که همه املاک مازاد آن‌ها بدون توجه به زمان تملک، مشمول مالیات هستند و بانک‌ها فقط تا پایان سال ۱۴۰۵ برای واگذاری این دارایی‌ها فرصت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449953" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607893a909.mp4?token=JBuV19gR4a3L-t1YMOTENhzAZu5koBX52Xb8ndgOqLm8nBF9UEJhPDAFW4JGoforvyctf_VWxCErYt7dUhD12VvRfr-o6poRR9o2NksVFuc88pgkPJOiYhnUjLO4ODHCTsExAUGrynOe5Xz9wqD2XNWvLlETuVynOCgvoHg1QvXbNF-Fc762qLsZBOaX5UAewfa3b-pcZADgtq7XF-z3sykFyTFoSZ2UQ-XAgMBOIfjSdIj2HhtpHeAmwrBQ5u29n1qcNodVGkxnSENTcc20YBn6SN5X4ZtjD1vvnhVbpekdkXHwQKWeFeChP9v_cD_lzr0XXCvDJGrEqf0-F2tABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607893a909.mp4?token=JBuV19gR4a3L-t1YMOTENhzAZu5koBX52Xb8ndgOqLm8nBF9UEJhPDAFW4JGoforvyctf_VWxCErYt7dUhD12VvRfr-o6poRR9o2NksVFuc88pgkPJOiYhnUjLO4ODHCTsExAUGrynOe5Xz9wqD2XNWvLlETuVynOCgvoHg1QvXbNF-Fc762qLsZBOaX5UAewfa3b-pcZADgtq7XF-z3sykFyTFoSZ2UQ-XAgMBOIfjSdIj2HhtpHeAmwrBQ5u29n1qcNodVGkxnSENTcc20YBn6SN5X4ZtjD1vvnhVbpekdkXHwQKWeFeChP9v_cD_lzr0XXCvDJGrEqf0-F2tABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۲۴ ساعت گذشته در اطراف تنگه چه‌خبر بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449952" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
منابع عراقی: شدت انفجارها در کویت به‌حدی است که صدای آن از داخل اراضی عراق به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449951" target="_blank">📅 19:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffed4eebde.mp4?token=NIsJGIwLgcPBWkBCIQH4dOd1fYmaPZPR-kGOQTE4veep3luXqWtvmyMAQB4X1qw8crlf606KjY96up7jllzWgSQGZT7wjGyG0q7-o4ER-BwVqRDpMt4n6LESYvBe-Wpf3Cm1oJDqm6OYJUT4yA1s1CqAk4deOxQLZr71Sw2AKl00B9nUWro_B5XZFk-FY9XzqNqmgjRgn4OuzTjCSndNresTvfIALPUuVw7p4xq1qlxSbVtUJaOUdQtigmLEPcISgwJkLqmO9E8VxUKyNqfkGiDB-dRFCKyJnHDMLuMs01BpMWPkSE2Z_NIr-HArsp7MSTuWN7-osCbvOb7MPluDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffed4eebde.mp4?token=NIsJGIwLgcPBWkBCIQH4dOd1fYmaPZPR-kGOQTE4veep3luXqWtvmyMAQB4X1qw8crlf606KjY96up7jllzWgSQGZT7wjGyG0q7-o4ER-BwVqRDpMt4n6LESYvBe-Wpf3Cm1oJDqm6OYJUT4yA1s1CqAk4deOxQLZr71Sw2AKl00B9nUWro_B5XZFk-FY9XzqNqmgjRgn4OuzTjCSndNresTvfIALPUuVw7p4xq1qlxSbVtUJaOUdQtigmLEPcISgwJkLqmO9E8VxUKyNqfkGiDB-dRFCKyJnHDMLuMs01BpMWPkSE2Z_NIr-HArsp7MSTuWN7-osCbvOb7MPluDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورزشگاه آزادی را شخم زدند
🔹
طبق تصاویری که سه‌شنبه منتشر شده چمن ورزشگاه آزادی به طور کامل جمع شده. قرار است لایه‌های زیرین چمن سابق تا عمق حدود ۴۰ سانتی‌متر برداشته تا زمین برای اجرای استانداردهای جدید آماده شود.
🔹
در صورت آغاز به کار برای تعویض چمن حداقل ۴ ماه زمان نیاز است تا چمن جدید مورداستفاده قرار بگیرد. مسئولان ورزشگاه دلیل این کار را ویروسی‌شدن چمن عنوان کردند اما میثاقی، مجری فوتبال برتر ۲۹ اردیبهشت امسال گفته بود: «کاری به چمن ورزشگاه آزادی نداشته باشید. چمن در ایران مافیا دارد. الان وقت کاسبی نیست».
🔹
پیش‌تر مدیرعامل شرکت توسعه اول تیرماه وعده داده بود: «سعی داریم در اوایل لیگ قطعاً به بهره‌برداری برسیم. شاید یکی دو بازی اینور آنور شود».
🔹
سازمان لیگ زمان آغاز لیگ ۲۶ را ۱۶ مرداد اعلام کرده اما به نظر می‌رسد این مسابقات با یکی دو هفته تأخیر شروع می‌شود. با فرض این تأخیر هم اما بعید است که ورزشگاه آزادی حداقل تا ۵ ماه دیگر قابل‌استفاده باشد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449949" target="_blank">📅 19:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=g4vOOw9XPemaZ1Abl98JfbCx-_5cx_lEA_P7WS1cz3E_i0De53hX4QL6XjQL_noeGGdnBbs3TPzMIV1NVtFQBB2BX1_dV3T9rVvRupLe8kkBgJH8x4hC1ct15L_xwWuiGJRZFuT1r94pnAIdBfc29KMRG-DQooE7qP_LLP6j0msM4HdgXoci3VLnOIm0AMJQ6pcxAj4V4CAn0fMPEfP4cxVb-xijjyyj02M1nxq0ISkEaSVZ0_eYIuyaRZEfY24TI0vE_0eKjzmsEv6xfhnz_r0hGJq_PcuyR9zeXRHaMVL8Cw2JYe0crBDL216wQ-4Er5ttQoREwnA8bSJuJ2F3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=g4vOOw9XPemaZ1Abl98JfbCx-_5cx_lEA_P7WS1cz3E_i0De53hX4QL6XjQL_noeGGdnBbs3TPzMIV1NVtFQBB2BX1_dV3T9rVvRupLe8kkBgJH8x4hC1ct15L_xwWuiGJRZFuT1r94pnAIdBfc29KMRG-DQooE7qP_LLP6j0msM4HdgXoci3VLnOIm0AMJQ6pcxAj4V4CAn0fMPEfP4cxVb-xijjyyj02M1nxq0ISkEaSVZ0_eYIuyaRZEfY24TI0vE_0eKjzmsEv6xfhnz_r0hGJq_PcuyR9zeXRHaMVL8Cw2JYe0crBDL216wQ-4Er5ttQoREwnA8bSJuJ2F3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور قالیباف در مراسم بزرگداشت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449948" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
