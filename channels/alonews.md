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
<img src="https://cdn4.telesco.pe/file/t_JGijPVxfoAic9UHVfeniCbkNjhuumzMhPmE6MZlNq-oMSvyaDOmQ2J12JlMXbCCRGlt4kvg2zVExm-5S5IHuS9bECXYXnP9wYT4cGFMsLpfj36KYMOCiPtontSKq8pmHc78wImwtFMY-JzzfW10gCB4NOm4SUmIEB95Zl9hWiUfU0SX9dJJwo6ehn8iAeN3FJU9zyTJWn05wq57Zb21VJpLFGF87pbS5DglFKgFestckVkC1KfcCkhyoSCNzKvD_a6NOz4eFgWQtvb6mfLIlJPWNiIOMx5L9BHBvRPRjdQDnSnTNWx2qEHnOliQZC2HPSS4x-0hs1l4ewDT9e2wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 05:29:52</div>
<hr>

<div class="tg-post" id="msg-128821">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNNUBrtXAQwVtpDt6K0eDr5Vtb0mvn_pdhwl4mjhWHJfAPhU2H8l2UCHDn5jFOdU9z3b-6RBHN0TjpFjL03ZtsNR7-ZOtzzVWYmj0NpK1sUv70NwM3GIYD0HIQAXBD9fDlmlglyM0-NpghtzpVNCtGxizYzVFsMxUgJvdEplzObUkcrxAcZvVccjtecG_HvaauxwH7iT3mTdbLIn0QUHTmb3P1yGhlH1xM9QZg2EAwoBD5hFY6cCQ5cY3JZN-pHV86ch3tLEzPO0t7jTuhYGXgb5NprYV1KRH-c9HEJrtt_kQWs8IZGvbA6E4Sz6Ll_zDLj_nFdSkmEns0EysLcqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/alonews/128821" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128820">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هم اکنون ریزش شدید تتر و طلا
تتر 152000
طلا 15میلیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/128820" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128819">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjuSe0Kt2Hy4VZppCpxooyT3NMV2jwoQdlxAPW6YVzHDLjCo2iMD2KL2h8vxKCFZ0TewQXtSCdzYn68sfn6s5Zby-vK0MWrGj46SaokWyTTskCmteXI7nXtvtFbEuPLxjiJFnAfIAskmAM-7sb6MuvdVnckUBMhoSm2lubyh5zepKnAts4-cgT-5mYg78DPssm7673DYvAugw_r2VWVUoiv-ASTwZP9PlhPn_aHGKO8_0Lap4o33phXy81IUQ4HO2-NsNAtUR2CO1JKZphs_3Dr2UDf8ddPipS1nSE4eKjLD3LdxQ-jjkEUPk6ZyPnhtD4QXfq45vLrQYTivlScHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاضی زاده، عضو تحریریه اینترنشنال: کجای راه را اشتباه رفتیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/128819" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128818">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQzWXWzBEJSAddepGlifTe23oI4vqx2biO8i44YI8hdsTnnSwcJvgynr28I9ShwiiQ6MushXLIMHiFJIqiubvOB76t41S0O6Tu2BxruXSIE4rELo7VuuigOQK5vOG5thhX1jztPhjnUZIm657-oYEzN1AUgno6IPULduvfnv8xyJaIsPE9Z_dUJvVHfMidHl6g_JwDRaXBpRkLVzuGCK5JSPRhyMkhmTC6zjcZZYvrt0OFx1QlmCuh1qGNAiIsvoqJUNWACSor5kFszkx5hNrbdEB6_SgyzNpM9XKqegf7L_XAxuEaSF_T7PjJy62U7st5xmQ6zpjmx2oqjzMuARAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: ترامپ شخصاً یه نسخه از توافق رو توی یه مهمونی شام با مکرون تو کاخ ورسای امضا کرد و عکسِ اون توافق امضا شده رو هم برای ایران و کشورهای میانجی فرستادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/128818" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128817">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heztpjVJzGjqiEg6mJPoig0rNG1UGbQ5rtOKHhsHcXbtjAkDTc_cl04QxitRzRr6hGUrfAQ8Vp-liJTZTlQLCzSH1vUD4PlKZr4Kq1jieY8czUss6w384Du3Pa9mEa3qPsXEEaILpsV0_vRhi5B9ZSaBgs3Ms01njgtC_3h117A7H8eqO5iO5jGcxv2HrpuA_nDULXmyTUcCNd9nY1UlAq_IcEUYon0awqAL-ED8megAhXUNmKmcZST_urjlTkjgSJxyDHNDpBl5pMs0QE0y_agjCPKggYLvq5jG81AbupLshyvvgtd_sWyL4BIYE9fGyDPUdI_2FFChh7tClYFPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: انتظار بسیار بالاتری از این توافق داشتم و فعلا نظری ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/128817" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128816">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t646BCiGZqNtXUCe-dRHWY8OfhcZw00CkZLtXFqBZSBDPh4PX8f67CZ9vDPjLeKSTEl3yUrhpzPCuxVIdp1ybW4-0WDHTV7Y25tI6Yda0ND8Su9YK4I20lGTXxeek4b0RAHwHxESZFhi67EFQ759WX4uxCrSlmWFtcYtMhGz3hG5nSeqMTGT1BNyipHre22sVN7rWGdxYE4-BgJ_BTJpmFp5ih69jOeiHNiVD8ORf29Ib9u0VXp0fW_k6_YN7YZ7BzGbmCFPSONN-Ap3O_uIOLSsauMMxQs2H5Fncl4GjTkKI8JMGg0nkJTvEmUjSVVWe2U4eaqxST69B_xLIts83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: فاجعه‌ای بدتر از برجام رخ داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/128816" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128815">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد.
🔴
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما ‍بس از امضای این سند شروع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128815" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128814">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/128814" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128813">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حسینی با یزیدی صلح یک ساعت نخواهد کرد
کسی مانند ما با مثل او بیعت نخواهد کرد</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/128813" target="_blank">📅 00:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128812">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در متن تفاهمنامه تاکید شده است که فقط منحصراً در موضوع هسته‌ای و رفع تحریم‌ها مذاکره می‌کنیم.
🔴
از زمان اجرای تفاهمنامه، که الان است، ظرف 60 روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد 60 روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/128812" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128811">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عرازش برید خونه‌هاتون</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/128811" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128810">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرنگار اکسیوس: دو مقام آمریکایی به من گفتند که ایالات متحده و ایران روز چهارشنبه تفاهم‌نامه پایان جنگ را به صورت الکترونیکی امضا کرده‌اند و اکنون لازم‌الاجرا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128810" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFO5HbXO4lgFmWuY1G8wNSDpkOz7M573joU1wKlp5MHS1BSbz9rDVby98fXsHohSpAEUwpUhrnAhXpCMvalHCp_PTAlA99AuEWCGcZgcQk4KnsXgwwxXTMtxqtLZxZjXWc0orCsuiSM7PXvihD-6fP8EvJT0aHTg1whwBCv40CVz_ZKai7nfMtqy_XSkG2ZMzFtjmJ4-b-8fBRMSMS5qG9xB_4QhipKFljhHn2Wp4dMlZHc7d3lpYhJn2_WzoW7Q8Pq5J9AObquVRi_NUsDFGvapTtlYIU6Ye_pwrOWg8nLFIq5yYpoaJtJtcB4NJll_qk9YaXqE-Rmj3r8KuIwhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/128809" target="_blank">📅 00:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128808">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/128808" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128807">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/بقایی:  الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/128807" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128806">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/بقایی:
الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/128806" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=p2kHAz_NjyATW3eNBWpUCboW1ZChAIurtNIHI5zy54NdIK-htp0s9esfzhiuZdmS12aBWE0CdN8rUvOsjYkyzOlp9Qx6_KPUvzR66r_ugiwTT__ccDyrpgnnlPHyNBd-zLHODQa8jMv2vZf-XqiWVGx0CY_C0E5pN-V9fuvYBKFVTjaKQB_dxqbU2n6wQaymheWlWTf9LhViJmhhsxQa6LoztiXvofZymNtsmf_tPrvgvsSdtGP-OO-0vBwWGBMKKpgJI3hHUFnIPboRRX2pKKC04mo21-IeV8wJ3NZsmE85JO7eG7RX96YidGMY9rImEUohPKfLuLF8ZJUzB5ahPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=p2kHAz_NjyATW3eNBWpUCboW1ZChAIurtNIHI5zy54NdIK-htp0s9esfzhiuZdmS12aBWE0CdN8rUvOsjYkyzOlp9Qx6_KPUvzR66r_ugiwTT__ccDyrpgnnlPHyNBd-zLHODQa8jMv2vZf-XqiWVGx0CY_C0E5pN-V9fuvYBKFVTjaKQB_dxqbU2n6wQaymheWlWTf9LhViJmhhsxQa6LoztiXvofZymNtsmf_tPrvgvsSdtGP-OO-0vBwWGBMKKpgJI3hHUFnIPboRRX2pKKC04mo21-IeV8wJ3NZsmE85JO7eG7RX96YidGMY9rImEUohPKfLuLF8ZJUzB5ahPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/128805" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سناتور جمهوری خواه بیل کسیدی در مورد تفاهم نامه ترامپ:
ریگان در قبر در حال لرزیدن به خود است....این بدترین سیاست خارجه آمریکا در چندین دهه اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/128804" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128803">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=b3HYtOzwwpzR4ZPBkIANU6HvacX-rzE9Yaj74ku89k4bXQoifwl5zFYPRUjQe0ZBl_UDq-sa_3ebwOeeEkU-8DEefmxZjlEcYtAkhEDWj0RUxAR2GdgM6FvkULXdfbyPp7aAxNkIPJKE8P8YjqpeBs-2rNzdCteqXSsNG6h_LCNRB1IjAeADVWCvW0zmNvoQ8AHNOk6R9YPdcdbpDJrj56ID7NYI9wkZjsLgRkNtRCKobDNVsnjRrkRlWTr15Z6D5WvaE4OV-DD0-Z-_a9--HhRTBpzTGQISLEbNA3JHus1FQqzblGDlIZrC7Eowr-gu3WQ0-nOI8eAcmn2YtxHJfIjXxKxZPMqFEf2ig-I3MrWU0BcibXyn6gsjq1vcfyhyyyuvuCaK9Jsqc7RAHvozrEq7KcSbVcKgnP2USm65_QHW9_dr2A51M13JZUV0togadV9B3ILP09zSrWZetoY8rpuj7BsFgUwvGK8NoGhNqSl4Kg0iQ7FTjIqqf-Y5FJWZ5tXXkXw7W_2m5YaMsK3443HluFuyQDC1XGalDpe794bvdBamc_n0KCmPcvw-UHNX2hXURvdp9XZJsee2pTrEsZExy3Xd91CJ2jCjSpibOycoiTN1-1jQZrmB77OkVJuk97dffRgCzxlIPEfDs_1CuNyN1mPvotc6utdHsiEGqso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=b3HYtOzwwpzR4ZPBkIANU6HvacX-rzE9Yaj74ku89k4bXQoifwl5zFYPRUjQe0ZBl_UDq-sa_3ebwOeeEkU-8DEefmxZjlEcYtAkhEDWj0RUxAR2GdgM6FvkULXdfbyPp7aAxNkIPJKE8P8YjqpeBs-2rNzdCteqXSsNG6h_LCNRB1IjAeADVWCvW0zmNvoQ8AHNOk6R9YPdcdbpDJrj56ID7NYI9wkZjsLgRkNtRCKobDNVsnjRrkRlWTr15Z6D5WvaE4OV-DD0-Z-_a9--HhRTBpzTGQISLEbNA3JHus1FQqzblGDlIZrC7Eowr-gu3WQ0-nOI8eAcmn2YtxHJfIjXxKxZPMqFEf2ig-I3MrWU0BcibXyn6gsjq1vcfyhyyyuvuCaK9Jsqc7RAHvozrEq7KcSbVcKgnP2USm65_QHW9_dr2A51M13JZUV0togadV9B3ILP09zSrWZetoY8rpuj7BsFgUwvGK8NoGhNqSl4Kg0iQ7FTjIqqf-Y5FJWZ5tXXkXw7W_2m5YaMsK3443HluFuyQDC1XGalDpe794bvdBamc_n0KCmPcvw-UHNX2hXURvdp9XZJsee2pTrEsZExy3Xd91CJ2jCjSpibOycoiTN1-1jQZrmB77OkVJuk97dffRgCzxlIPEfDs_1CuNyN1mPvotc6utdHsiEGqso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آسیب دیده جنگ: خونه ما موشک خورده و کامل تخریب شده اما مسئولان اصلا براشون مهم نیست و وقتی میریم پیششون نگاه هم نمیکنن مارو
🔴
الان ما آواره شدیم و چیزی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/128803" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128802">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=tV51KD3zO_MZ2p3gXSqWr82-VQee_gFmm3l9KF2Yk-u4hLNh2Pi3XmtcfidZbamiyvrpb7q8ExyqeDZXPd212l3mfKTBPwNdo5I8DTFHG5a4EsyF-6-yg4vCwrBESU1jZzCpGwnbtkZyJlBBPY98jOmG0ZTonBN5uv_N5t-3bIKT8hLCBM5gH1bb3GbFUHEqWCT2slQIP8UoMstS7ktqraN3KmWESCwPG6y_JSuOkGqtbBRJflUpruoXisr8sMBnzLDDwjwht4BZm-HUKRrTK8OBOxFckwbfh2MJueZnmB3WHbDdvLA33UXZ7iZnXpgdVjO1tmpkUBRycfxbQEqhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=tV51KD3zO_MZ2p3gXSqWr82-VQee_gFmm3l9KF2Yk-u4hLNh2Pi3XmtcfidZbamiyvrpb7q8ExyqeDZXPd212l3mfKTBPwNdo5I8DTFHG5a4EsyF-6-yg4vCwrBESU1jZzCpGwnbtkZyJlBBPY98jOmG0ZTonBN5uv_N5t-3bIKT8hLCBM5gH1bb3GbFUHEqWCT2slQIP8UoMstS7ktqraN3KmWESCwPG6y_JSuOkGqtbBRJflUpruoXisr8sMBnzLDDwjwht4BZm-HUKRrTK8OBOxFckwbfh2MJueZnmB3WHbDdvLA33UXZ7iZnXpgdVjO1tmpkUBRycfxbQEqhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
با بغض: برای من کار راحتی نبود با ترامپ قاتل سردار سلیمانی مذاکره کنم / نفر دومی جز من برای مذاکره نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/128802" target="_blank">📅 00:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128801">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL1G6Sp5fOoQ0_lFLmQPzKgN-D1u0cZDZfEF0NdN4uKnqCsSXtMcmTNO65z3zzjIZ6y8YpVmtZZDERcx1MN43SMuaAN115k27rGNAe8Icjyf88wcUUf-0nlFAFg5sTaXxtFxMsY0pNE3jW8r76dk4i5RZs-X1Rww56iS0skwdJcsD9XvAwVnA2BhZDmC54LfvYTRhdAtPwmtJ7kJXjTy3Fh33-1NIBFwAij6y8D1rP3UTWk-tgG1ymA1qCJlznlLKZwo9nxnXUNzzGq2BS8B8wjoaMIWwUx0A2y0pS51c5XN2AQaeUiJawDBE7dcGK0dpIMOeNF0xw4viIUXo7c-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری میا خلیفه بازیگر مشهور لبنانی برای مهدی طارمی:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/128801" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx_CigfYPXf32m3OFBX2-DC6h3x31WoJgXy370XSh1krUkd86oNJc0AAiJsbpuOam7A3PPhx-JZ-XGJN04995cAxF7bKQLjDxEZNeNF5xVMjerg4IjyV9ZpeLOEJP4mAoxYf9EFQuLNX_gA0l-jjMCnLLhlE4fnDykE1JFprUJpn8yHOHab9h5NzAcoikioQdpraGAfB6nfoCehDXMwgr1siBkSDS4NamwSl3WiYWKQ4mMHJUxEodTkL2VtwTv4LirYy6ZIYMs8BoW1VT0R3So1vdm6E5DdAMXnJ4SVytuwn0os3fvt8tZFwVwjNPMzjlBexj0MAa2LV3P9Kd21d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=iJSJN09OF0sD99-4ZHEBd78ota7ZIyBFEX9f6SEML-Chqu-mU0P35WvcabRk22jWsHNRUEF6bcw8cTVGNCzveJf8iqqKkR3zwIvJzOmCvNEgFqfkQ0yt_qIgk9wzf3JQIf5rzkm92mNyHbx3KDkjDTA2ES4iWxUbk88kHDq66NY0TjZ3IaJ4wYnzSD-IWV7gzGUB-_CgHq3yd6mfm6v-di24xgab_Sdrf543eyyv8hkv2o168g8Mwf6ZTTyxSRQcXFO0Vra6s-CPapA5edhEQ3qypP_5q41aY3qOt2SzPPXCTxjtnjgabTdl4cu9IsuOSS4IGst4y7paGAr3lETEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=iJSJN09OF0sD99-4ZHEBd78ota7ZIyBFEX9f6SEML-Chqu-mU0P35WvcabRk22jWsHNRUEF6bcw8cTVGNCzveJf8iqqKkR3zwIvJzOmCvNEgFqfkQ0yt_qIgk9wzf3JQIf5rzkm92mNyHbx3KDkjDTA2ES4iWxUbk88kHDq66NY0TjZ3IaJ4wYnzSD-IWV7gzGUB-_CgHq3yd6mfm6v-di24xgab_Sdrf543eyyv8hkv2o168g8Mwf6ZTTyxSRQcXFO0Vra6s-CPapA5edhEQ3qypP_5q41aY3qOt2SzPPXCTxjtnjgabTdl4cu9IsuOSS4IGst4y7paGAr3lETEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جرمی کلارکسون از مستندساز های ماشینی معروف که در ایران طرفدار زیادی دارد اعلام کرد به سرطان مبتلا شده است
جرمی کلارکسون:
سرطان پروستات دارم، ده درصد از پروستاتم را برداشته اند و اگر همه چیز طبق برنامه پیش برود، در فصل ششم «مزرعه کلارکسون» می‌بینمتان. اگر نه که مشخص است مرده ام. مراقب خودتان باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/128799" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/128798" target="_blank">📅 00:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXPkabK4ImFZyZSIRde24txlOnR36NP66Pk25c-q3U9QRsTKBtqdhEsFzfdU4burm4qSvnh9J1cJKj-oURurrdZwHn2k7yFrIO-IBoDysGP2iOHZm30n0E9XVKptNKJLpPJHHk57sZYydSYcpyddOFn1wk6lR_r-qoyQs3GnuYZory-0vgv7yznHL9xDL_CR0FfYUjH6SfIAIk6ZBYNSqNzm-u7X2p4bOrz1B3JobABOLHYB572LmwNOR66qFec7UZSS2XrMZfXXr6hQ5vbTLjtxoVSGb1BdXbGgGwD78IsuA1ZBwG64dxlXqxnGN-RbmW6zvfvyF7ITLm6V97vGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر کشور: ۶۰ درصد مردم ایران امیدی به بهبود آینده ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/128797" target="_blank">📅 00:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=GmO79kiLjlEPIA1cO16But3jhdm6iwQxG87x-NXQN-fFrFOk-fj7G1CLEhuN6U-vWU6NaxBxeXSET17KwBQyVty1eltwUE4FGEt85f5gP7kSE-VxY2knK2k-IlF186v-dE7nJBS_rF2ZkW18skW3sDzfMCDJgfoZYMO6VkTabhfqluBNyG68gikUMcFvC4Zt0ZZUI5eP59-q8KRptv9x2TJBDpPIqkHmQUypCmiHNPaZia97kEczRQopxi5iGbdUs0Uuimyqpm63DDTc9HKPx_yL4-TanUw5P1g_8Vh5veFQImXCYThh7ZVHpuJ0l0fu3vSNbZTwfmZ5g4wy5SLheQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=GmO79kiLjlEPIA1cO16But3jhdm6iwQxG87x-NXQN-fFrFOk-fj7G1CLEhuN6U-vWU6NaxBxeXSET17KwBQyVty1eltwUE4FGEt85f5gP7kSE-VxY2knK2k-IlF186v-dE7nJBS_rF2ZkW18skW3sDzfMCDJgfoZYMO6VkTabhfqluBNyG68gikUMcFvC4Zt0ZZUI5eP59-q8KRptv9x2TJBDpPIqkHmQUypCmiHNPaZia97kEczRQopxi5iGbdUs0Uuimyqpm63DDTc9HKPx_yL4-TanUw5P1g_8Vh5veFQImXCYThh7ZVHpuJ0l0fu3vSNbZTwfmZ5g4wy5SLheQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: ما میتونیم تنگه هرمز رو بر ضد آمریکا تبدیل کنیم. هیچ کس به کمک آمریکا نیومد. این موضوع که باید عوارض تردد در تنگه هرمز پرداخت بشه، تثبیت شده در تفاهم نامه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/128796" target="_blank">📅 00:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z6ycWIG2XCblRDq_YDX6rEZ7EvuA8D0YMnkRU6jR6lYPPma8jAET_q8ldIOk5-xY0MlIEmA14RANNhbpamM-BTtPjnvX1LDk7ilmlMv-zyCXmm-VW_RhhLBPIQlERJg9L0bj8LHG0FDkJsXzTm7EjR-yISyBKDunH0Pq5PlCEYt2FoXFlEDVITeITuVIhQwXIdujFRJ9vPZkH0Q5ucQnzq3oVyFakrZA38B6Y2jwserpKI_q9GCQZOuP9U3DUVAnqZ_faXu9K0YgKX0DpuXzA4Nr-4eH9TqNRmLpT4suHAPCZ2AEHLqRZy7j9aE3OmbvNBIJUwXhiqUhHCdcuul4CJg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z6ycWIG2XCblRDq_YDX6rEZ7EvuA8D0YMnkRU6jR6lYPPma8jAET_q8ldIOk5-xY0MlIEmA14RANNhbpamM-BTtPjnvX1LDk7ilmlMv-zyCXmm-VW_RhhLBPIQlERJg9L0bj8LHG0FDkJsXzTm7EjR-yISyBKDunH0Pq5PlCEYt2FoXFlEDVITeITuVIhQwXIdujFRJ9vPZkH0Q5ucQnzq3oVyFakrZA38B6Y2jwserpKI_q9GCQZOuP9U3DUVAnqZ_faXu9K0YgKX0DpuXzA4Nr-4eH9TqNRmLpT4suHAPCZ2AEHLqRZy7j9aE3OmbvNBIJUwXhiqUhHCdcuul4CJg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: بند 6 تفاهم‌نامه 300 میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده!
🔴
در این بند 300 میلیارد دلار تعیین شده تا در ایران سرمایه گذاری بشه که بخشی از آن صرف بازسازی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/128795" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0842a70573.mp4?token=ZgxckDtsal5UrYl85hpxY8kttE33FhGxGeU9bz796dMkewCWtzINY4TKRo9oFrLm6d16k5hx7vxMWLAmtz795HMMQbwuclQsBQfOl9aCWHuSwAVFuCEGOLX7EAE5m_Wf7F30zM7WMAt_vMC6uw8sZpgfVzX1MrdoNc3-pYzTVjfUC0IDjBGr4MqMY1EtX9ol7K1eAVKZaayjk8h0MS8ZZPZzwYiDGC3behpF1B1e-8wqMo9C6tc8XiJ8VmcfLU7lRGGqZ8ssGS8PfC5f7G6_KxgNHaCnLyr5g4O8EebrpWMAtSFQJZIOZYJokCzRWK14iu1mwAYqHA2vMD0Y5ZSUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0842a70573.mp4?token=ZgxckDtsal5UrYl85hpxY8kttE33FhGxGeU9bz796dMkewCWtzINY4TKRo9oFrLm6d16k5hx7vxMWLAmtz795HMMQbwuclQsBQfOl9aCWHuSwAVFuCEGOLX7EAE5m_Wf7F30zM7WMAt_vMC6uw8sZpgfVzX1MrdoNc3-pYzTVjfUC0IDjBGr4MqMY1EtX9ol7K1eAVKZaayjk8h0MS8ZZPZzwYiDGC3behpF1B1e-8wqMo9C6tc8XiJ8VmcfLU7lRGGqZ8ssGS8PfC5f7G6_KxgNHaCnLyr5g4O8EebrpWMAtSFQJZIOZYJokCzRWK14iu1mwAYqHA2vMD0Y5ZSUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، ژنرال 10 ستاره هم کماکان در حال گذراندن تمرینات آمادسازی برای قبل از مراسم برکناری خود در سمت وزارت جنگ مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/128794" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ برای شرکت در یک شام رسمی که توسط رئیس‌جمهور امانوئل مکرون و بانوی اول بریژیت مکرون برگزار شده است، به کاخ ورسای رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/128793" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف:
در قوانین ایران هیچ مانعی برای حضور و سرمایه‌گذاری شرکت‌های آمریکایی در داخل ایران وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/128792" target="_blank">📅 00:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/128791" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: وقتی اظهارات ونس را هنگام سوار شدن به هواپیما دیدم که درباره لبنان صحبت کرده بود، پیش از پرواز و در فرودگاه توئیت زدم که تا وضعیت لبنان روشن نشود، مذاکره را آغاز نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128790" target="_blank">📅 00:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قالیباف: برخی متون تفاهنمامه به خاطر حساسیت های حقوقی ساعات ها در موردش بحث شد.
🔴
برخی دوستان نگران بودند که آیا بعد از ۳۰ روز محاصره رفع خواهد شد؟ اما به لطف خدا طی سه روز محاصره لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/128789" target="_blank">📅 00:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قالیباف: سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی‌پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت خود، مسائل را دنبال کنیم.
🔴
البته در تفاهم نامه بند ۶ برای این موضوع آمده که در آن از لفظ بازسازی و توسعه اقتصادی استفاده شده است.
🔴
در این بند ۳۰۰ میلیارد دلار تعیین شده تا در ایران سرمایه گذاری شود که بخشی از آن صرف بازسازی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/128788" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قالیباف: کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداختند کنند.
🔴
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت بالقوه ایران در تنگه هرمز بالفعل شود.
🔴
ایران در تنگه هرمز حق حاکمیتی دارد و طبیعتا در قبال خدمات، هزینه دریافت خواهیم کرد.
🔴
پول‌های بلوکه شده ایران باید در حساب‌های ما و در اختیار بانک مرکزی قرار گیرد. خط اعتباری یعنی بانک مرکزی می‌تواند هر لحظه برای هر کس خواست، ال سی باز کند.
🔴
این را اطمینان می‌دهم که هر کجا دشمن به تعهداتش عمل نکند، سیاست ما بچرخ تا بچرخیم است اما اگر به تعهدات عمل کند ما هم عمل خواهیم کرد.
🔴
اگر دشمن بخواهد خیانت کند ما مردم میدان هستیم و فاصله من از میدان مبارزه دیپلماسی تا میدان مبارزه نظامی زیاد نیست و دست مان روی ماشه است.
🔴
به کسی که منطق را نفهمد با قدرت، منطق را تفهیم خواهیم کرد. من دیپلمات نیستم اما خوب می دانم چطور باید به آمریکا تفهیم کنم که باید چه اقدامی انجام دهد.
🔴
ایران پول‌های بلوکه شده را دریافت خواهد کرد؛ اما این به معنای این نیست که پلت پول بیاوریم. این پول اما باید در اختیار ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/128787" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
توضیحات قالیباف در مورد فرآیند مذاکرات اسلام آباد
🔴
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/128786" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
قالیباف: اگر می‌خواستیم محاصره دریایی را با موشک بشکنیم باید جنگی بزرگتر از جنگ ۴۰ روزه رقم میزدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/128785" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
🔴
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/128784" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/128783" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قالیباف: ما حتما باید با عقلانیت حرکت کنیم، شعار قدرت نیست، گرهی که با دست باز می‌شود را لازم نیست با دندان باز کنیم. اگر دوبار شعار بدهیم ولی قدرت نداشته باشیم یعنی بی اعتباری و کمک به دشمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128782" target="_blank">📅 23:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قالیباف: بدبینی و بی اعتمادی من به آمریکا از همه بیشتر است، حتی اگر توافق نهایی باشد و آن به تایید قطعنامه شورای امنیت برسد بازهم اصلا قابل اعتماد نیست، تضمین ما قدرت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/128781" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف: در مذاکرات به ونس گفتم ما کاملا به شما بی اعتمادیم
🔴
بند ۱۴ تفاهم نامه این است که باید به تصویب شورای امنیت برسد و تبدیل به قطعنامه شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/128780" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128779">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قالیباف: رئیس مجلس لبنان به من می‌گفت ایران مایهٔ افتخار جهان اسلام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/128779" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128778">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
قالیباف: تو مذاکره به ترامپ اولتیماتوم دادیم
🔴
آتش‌بس رو هم آمریکا درخواست کرد و دنبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/128778" target="_blank">📅 23:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128777">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است/ در مذاکره‌ به روش مبارزه وادادگی و شعارزدگی وجود ندارد
🔴
وقتی حرف از مذاکره و دیپلماسی می‌زنم، منظورم دیپلماسیِ اقتدار است.
🔴
زمان برجام هم گفتم که با مذاکره مخالف نیستم، اما تأکید کردم که با مذاکره‌ای موافقم که خودش یک شیوه مبارزه باشد.
🔴
فرق مذاکرات الان با دوره‌های قبل در این است که امروز این علمِ پیروزیِ میدان، که هم دشمنان و هم دوستان به آن اعتراف کرده‌اند، پشتوانه مذاکره است. نیروهای مسلح ما در مقابل این دشمنِ سراپا مجهز، پیروز شدند.
🔴
در مذاکره‌ای که یک روش مبارزه است، وادادگی وجود ندارد و در کنار آن، شعارزدگی هم جایی ندارد. اگر شعارها را مدام تکرار کنیم، دشمن می‌فهمد که تهدیدها توخالی است و این موضوع باعث می‌شود جسورتر و گستاخ‌تر شود.
🔴
همزمان با مذاکرات به تمام اقدامات دشمن در خلیج فارس پاسخ مناسب دادیم
🔴
در جنگ تحمیلی سوم، برای مثال اتفاقاتی که در خلیج فارس در دوران آتش‌بس رخ داد، قابل توجه است. در آن مقطع، این دشمن بود که پیگیر آتش‌بس بود و ما در ابتدا آن را نمی‌پذیرفتیم.
🔴
به هر حال، وقتی آتش‌بس اجرا شد، دیدید که دشمن اقداماتی را در خلیج فارس انجام داد و ما نیز بلافاصله واکنش نشان دادیم. آخرین نمونه آن، حادثه بالگرد آمریکایی‌ها بود. همچنین دو ناوچه دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند؛ موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
🔴
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن به پرواز درمی‌آمدند، مورد اصابت قرار گرفت. همه این اتفاقات در شرایطی رخ داد که ما همزمان در حال مذاکره نیز بودیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/128777" target="_blank">📅 23:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
🔟
ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
🔴
1️⃣
1️⃣
ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
🔴
2️⃣
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
🔴
3️⃣
1️⃣
پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
🔴
4️⃣
1️⃣
توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/128776" target="_blank">📅 23:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128775">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
🔴
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
🔴
2️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
🔴
3️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
🔴
4️⃣
بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
🔴
5 با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
🔴
6️⃣
ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار
اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
🔴
7️⃣
ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
8️⃣
جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
9️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128775" target="_blank">📅 23:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128774">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or4fwGU4BpkQJ0VdcG2WlopukN2haJHXmIIuHurwmeKgyEAB3HmdO-O1FgtyErqwos6OMPR0BunQ5Bl3JTjy-TBtSZAFRGMxz2qifNI8Wbeqabb3ZJsacYlenZvrbpPV7oM4rwA6QDKLSqEmnA8XQntw4uw2LMRPu7A-COX2Y6TTv4M6hQA5MkMkDOJKI3ymF22VqizQ62EjvbE3okeUCWN3oVzEDJR6517YBDjAtLZRzCbD2bPXs2yOSwxcYMb8VPhLxioDx-IABYktcbqPB9EDKoxe4OuHjLr04SQTR_SJppe9aYY1zypPbBDQ_GAmPcXoDtYWRuoDBq4UzcHb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا سیما : انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/128774" target="_blank">📅 22:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128773">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تعهد ما این است که در مدت مشخصی، ترافیک دریایی را تنگهٔ هرمز به حالت عادی برگردانیم
🔴
برای تدوین سازوکار مدیریت تنگهٔ هرمز و خدمات دریایی، ایران و عمان همکاری خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/128773" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128772">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا پس از تماس با عراقچی: توافق ایران و آمریکا گامی مهم برای ثبات منطقه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/128772" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128771">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مدیرعامل سایپا: ما قرار نیست ماشینامونو گرون کنیم بیاید از خودمون بخرید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/128771" target="_blank">📅 22:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128770">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=v9xoDVaJXHWtwnqvHL4f4Sz3TMesmQYqOdvqmuzeoNwGZzh-DF1fcOfj1uh4raizgkdcc2ZdmYeIzpDbXCqqMZeUXPY-L8UbkNSOUpnhOwDLmL5nT767vsPFXpqT3a26yS24FcgBiCXuTsfTatU-FRfmve9Xbfsk2S7GSUwqiapOJvgkgQjDH_sNlLmawwxp2rXXWXWwPmKo6SOwwWFi1cbZ9mynYixI7WpD5TULTKxMVJteeR18bT1DlwRfA4ZO_3wKLJKG7xPtIrh2K1YofONAQ4kbzADMnlnvosvXqvlSxecaTCTXroV0gZpuFLGM4F5XfD1VKBSvWwLVuf4KtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=v9xoDVaJXHWtwnqvHL4f4Sz3TMesmQYqOdvqmuzeoNwGZzh-DF1fcOfj1uh4raizgkdcc2ZdmYeIzpDbXCqqMZeUXPY-L8UbkNSOUpnhOwDLmL5nT767vsPFXpqT3a26yS24FcgBiCXuTsfTatU-FRfmve9Xbfsk2S7GSUwqiapOJvgkgQjDH_sNlLmawwxp2rXXWXWwPmKo6SOwwWFi1cbZ9mynYixI7WpD5TULTKxMVJteeR18bT1DlwRfA4ZO_3wKLJKG7xPtIrh2K1YofONAQ4kbzADMnlnvosvXqvlSxecaTCTXroV0gZpuFLGM4F5XfD1VKBSvWwLVuf4KtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون شام بخوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/128770" target="_blank">📅 22:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128769">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK-_8XTHxi_AFkiy3Mmcl1y9q8Gat4K70UKpI7nAIxGVI7WOquoGs_HruHisf33qMcbfmY8AOv4JPp8MSA0OxZE4WbSojiyYKThcfxULdtHX4R6wsVPgf0uvDA2T-mZkVwDe0iOqG335L_sp9QsUJI_DlXQLJ7gTA9uIJw3RoLlKCcOkFH21svcAOYbs1C4hOBwHwiNcRqPH_t3qEW-dphCBZNAqGYZnqF5Tol0zX14nReC10OyoPmEHoUkuXALasx8yk7ETUx0euUUnQ1-s_CV7OjkWFxqjVCFTFYWaJkdIg4_Z-_hndw2c6cPuGgFha-ouwxv5qImyNewRAinnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع ایالات متحده خواهد بود، زیرا تنگه هرمز شروع به بازگشایی می‌کند و درگیری‌ها با ایران متوقف می‌شود.
🔴
اینکه آیا آمریکا می‌تواند با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسد یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی را کم‌هزینه می‌بینم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/128769" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128768">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت خارجه ایران : ادامه اشغال جنوب لبنان توسط اسرائیل، یادداشت تفاهم را نقض می‌کند و ما اقدامات لازم را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/128768" target="_blank">📅 21:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128767">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منبع آگاه به فارس: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
🔴
تا این لحظه جمهوری اسلامی موافقت خود را با این پیشنهاد اعلام نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128767" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128766">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/128766" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128765">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره به نقل از مقام کاخ سفید: ایالات متحده متعهد است که بلافاصله پس از امضای یادداشت تفاهم، معافیت‌هایی برای صادرات نفت ایران صادر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/128765" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / بقایی: احتمال امضای تفاهمنامه توسط روسای جمهور ایران و آمریکا مطرح است
🔴
برنامه‌های ایران برای نشست ژنو تغییری نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/128764" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آکسیوس: طبق توافق تأیید شده، ایالات متحده و جمهوری اسلامی ایران بر موارد زیر توافق دارند:
🔴
آتش‌بس فوری و دائمی در تمام صحنه‌ها، از جمله لبنان، با تعهد به عدم انجام اقدامات نظامی یا تهدیدات بیشتر.
🔴
احترام متقابل به حاکمیت و عدم دخالت در امور داخلی.
🔴
مذاکره برای توافق نهایی ظرف ۶۰ روز (قابل تمدید با رضایت متقابل).
🔴
رفع تدریجی محاصره دریایی آمریکا ظرف ۳۰ روز و عقب‌نشینی نیروها از اطراف ایران پس از توافق نهایی.
🔴
بازسازی و حفاظت از مسیرهای حمل‌ونقل تجاری در منطقه خلیج فارس–خلیج عمان، با پاکسازی موانع و مین‌ها.
🔴
مشورت ایران با عمان و کشورهای منطقه درباره حاکمیت آینده و ترتیبات دریایی در تنگه هرمز.
🔴
تدوین طرح مشترک بازسازی اقتصادی برای ایران (حداقل ۳۰۰ میلیارد دلار).
🔴
رفع کامل تمامی تحریم‌ها (سازمان ملل، مرتبط با آژانس بین‌المللی انرژی اتمی، تحریم‌های اولیه و ثانویه آمریکا) طبق جدول زمانی توافق شده.
🔴
ایران تأکید می‌کند که سلاح هسته‌ای توسعه نخواهد داد؛ مسائل مربوط به مواد غنی‌شده و غنی‌سازی تحت نظارت آژانس بین‌المللی انرژی اتمی مدیریت خواهد شد.
🔴
حفظ وضعیت موجود تا توافق نهایی: عدم اعمال تحریم‌های جدید یا تشدید نظامی.
🔴
صدور مجوزهای آمریکا برای صادرات نفت ایران و خدمات مالی مرتبط.
🔴
آزادسازی و دسترسی کامل به دارایی‌های ایران، طبق رویه‌های توافق شده مشترک.
🔴
ایجاد مکانیزمی برای نظارت بر اجرای توافق.
🔴
توافق نهایی در چارچوب مراحل آتش‌بس مذاکره و سپس توسط شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/128763" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/128762" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کاخ سفید: توافق نهایی از طریق یک قطعنامه الزام‌آور از سوی شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/128761" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه : در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/128760" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام کاخ سفید: به همان اندازه که ایران به مسائل هسته‌ای پایبند باشد، تحریم‌ها علیه آن کاهش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/128759" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm_z8W0f_6N_4YLU9ExbjGAcfM2MR_PVhf4WGMt0jK2qmrYwN18P64d_9RYvlKBYWdzgsy20WJrZVaJmei7SU8CR91GUpCH7sPw6OhjglDHn4yhFrYyz0HBuwN1Qljj6oP_NLG21da4WGJPcuTr1KgvT4QHF7kRSuE_srPfDPxK2b_3wjB7QEQ9CfjZ7x8x4UOFi022FeP3kKxXqrDBrD8l4IP4xly5LH0HdP6dz_GDhj_9Q65C5YDo-7GI_IQworSs3gwjUiXlag80LGi3XjubWgqqdzzFmrW5oDSpO73Ty_CosxzPY3VG89YnwTqvq94Ywyza6rCN47vA5MiPmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا گزارش می‌دهد که یک کشتی در ۱۰۵ مایل دریایی شمال شرق عدن، یمن، امروز زودتر مورد حمله قرار گرفت پس از اینکه دو قایق کوچک حامل افراد مسلح تا فاصله چهار متری نزدیک شدند و آتش گشودند.
🔴
تیم امنیتی کشتی پاسخ آتش داد، که باعث شد مهاجمان حمله را متوقف کرده و از منطقه عقب‌نشینی کنند. خدمه در امان هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/128758" target="_blank">📅 20:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / تسنیم :گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/128757" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بخشی از این موضوع این است که معاون رئیس‌جمهور را می‌فرستید؟ اگر جواب داد، عالی است؛ شما به خاطر فرستادن او نابغه به نظر می‌رسید. و اگر جواب نداد، تقصیر معاون رئیس‌جمهور است.
🔴
ترامپ: این ایده را دوست دارم، حتماً. به این ترتیب، اگر جواب داد، من اعتبارش را می‌گیرم. اگر جواب نداد، تقصیر JD است. بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
🔴
بله، این ایده را دوست دارم. فکر می‌کنم ایده خوبی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/128756" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دووسی از فاکس: برای مراسم امضای توافق صلح ایران می مانید؟
🔴
ترامپ: شاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/128755" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: رئیس جمهور چین به دنبال کمک به حل و فصل اوضاع مربوط به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/128754" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128753" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: به محض اینکه ایران اقدامی انجام دهد، تحریم‌ها اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/128752" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره افغانستان: ممکن است تمام تجهیزات را پس بگیرم... افغانستان دارد به ما چاپلوسی می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/128751" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/128750" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ درباره ایران: آیا اجازه می‌دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/128749" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارشگر:  چرا اکنون برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
🔴
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از سایر کشورها دارند.
🔴
ما احتمالاً ۸۴-۸۵٪ از موشک‌هایشان را از کار انداختیم؛ بقیه زیر زمین هستند؛ حتی نمی‌توانند آنها را بیرون بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128748" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند، «سپاس خداوند را، دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است؛ ما کاملاً تسلیم می‌شویم؛ کاملاً دست می‌کشیم؛ این جنگ تمام شده است؛ ما شکست خورده‌ایم»، نیویورک تایمز و سی‌ان‌ان و چند رسانه دیگر خواهند گفت، «ایران پیروزی بزرگی کسب کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128747" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ : ما یه میلیارد دلار بمب روی ایران ریختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/128746" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: حادثه مربوط به حمله به مدرسه میناب در ایران هنوز در دست بررسی است و اشتباهات در جنگ اتفاق می‌افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/128745" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: مرد خردمندی یک بار در ژانویه ۲۰۲۰ گفت: «ایران هرگز در جنگی پیروز نشده، اما هرگز در مذاکره‌ای شکست نخورده است.»
🔴
پرزيدنت ترامپ: کی این رو گفته؟
🔴
پیتر دوسی از فاکس نیوز: دونالد ترامپ.
🔴
پرزيدنت ترامپ: آها، فکر می‌کردم می‌خواهی همین را بگویی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/128744" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ORuOTsSkXFChIMMdZ1q-EAj9KOCP6qiU-1z3JElKP-qbkZp9bX1V-GdWDfoojpTaAfXmj19AUjfhLBphqQlI0IZ71y-0c8_hhApK2GIZKBgEz6ig395bP3DanpCFltZaCa4-Pf7OBvji6uXorEBmHEhW5z29H947pRaJWhJqMEoFrvsgD-8d1ZdyLvTPqztqGDAoO_oLkPYcshNXcGgGJF5I8EC66gb5pnay-3zqeiyuBBTjyiqAwBe9SxESPc1jIg-geNBxMy7UU2XHcW4FDfZl1EL9U3Utd10v2BJRR2YD88wO1O6HzcDVPK2-uRVAayPsiYniMsObTs_pQ_YftLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ORuOTsSkXFChIMMdZ1q-EAj9KOCP6qiU-1z3JElKP-qbkZp9bX1V-GdWDfoojpTaAfXmj19AUjfhLBphqQlI0IZ71y-0c8_hhApK2GIZKBgEz6ig395bP3DanpCFltZaCa4-Pf7OBvji6uXorEBmHEhW5z29H947pRaJWhJqMEoFrvsgD-8d1ZdyLvTPqztqGDAoO_oLkPYcshNXcGgGJF5I8EC66gb5pnay-3zqeiyuBBTjyiqAwBe9SxESPc1jIg-geNBxMy7UU2XHcW4FDfZl1EL9U3Utd10v2BJRR2YD88wO1O6HzcDVPK2-uRVAayPsiYniMsObTs_pQ_YftLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خنثی بودن متحدان جمهوری اسلامی ایران: می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، با او بودم و او خنثی ماند، کاملاً خنثی، و من از آن قدردانی می‌کنم.
🔴
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار خنثی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/128743" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: حمله اخیر اسرائیل به بیروت خشونت‌آمیز و غیرضروری بود
🔴
محاصره دریایی ایران از بمباران مؤثرتر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/128742" target="_blank">📅 20:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: ما کارت‌هایی برای بازی داریم و ایران باید رفتار بهتری داشته باشد. درگیری بین اسرائیل و حزب‌الله باید پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128741" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر ایران درست رفتار کند، می‌تواند در بخش نفت سرمایه‌گذاری کند و ما هیچ پولی به آن پرداخت نخواهیم کرد.
🔴
ایران به صندوق ۳۰۰ میلیارد دلاری دسترسی نخواهد داشت مگر اینکه رفتار مناسبی داشته باشد.
🔴
آمریکا مقدار زیادی از پول ایران را توقیف کرده و در مقطعی مجبور به بازگرداندن آن خواهد شد.
🔴
این توافق به کشتی‌ها اجازه می‌دهد تا از تنگه هرمز عبور و مرور کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128740" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن سلمان:
من چندین بار با ولیعهد عربستان سعودی صحبت کردم — آنها خیلی خوشحال هستند که هنوز... شما هم باید آنها را خوشحال نگه دارید، می‌دانید؟
🔴
ما از فرودگاه‌های آنها استفاده می‌کنیم، نه اینکه اگر نمی‌خواستیم، آنها بتوانند ما را متوقف کنند.
🔴
رفتم آن کوچولو را بگیرم. اما خطا کردم. از خطا کردن متنفرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128739" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مکزیک: مکزیک کنترل کشور خود را از دست داده است. کارتل‌ها مکزیک را اداره می‌کنند؛ این ناراحت‌کننده است.
🔴
رئیس‌جمهور زنی بسیار خوب است، اما زنی بسیار ترسو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/128738" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه-اوکراین: هر دو تعداد زیادی سرباز از دست می‌دهند، روسیه بیشتر از دست می‌دهد، چون آن‌ها تهاجمی هستند و وقتی در جنگ تهاجمی هستید، بیشتر از دست می‌دهید، خیلی ساده است.
🔴
من فکر می‌کنم هر دو (زلنسکی و پوتین) می‌خواهند کاری انجام دهند، فقط نمی‌دانند چگونه آن را انجام دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/128737" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: اروپا با مشکلات زیادی روبرو است؛ در حوزه‌های انرژی و مهاجرت وضعیت خوبی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/128736" target="_blank">📅 20:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: به نتانیاهو گفتم که از طریق این توافق، چیزی را که بیش از همه می‌خواست، برایش محقق کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/alonews/128735" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ درباره سوریه: من مسئولیت زیادی در قبال آقایی در سوریه داشتم که اکنون رئیس‌جمهور آنجاست؛ او کار فوق‌العاده‌ای انجام داده است. او این کشور را در یک سال و نیم جمع و جور کرده، تقریباً مثل کشور ما، یک سال و نیم، اندازه‌ای تقریباً مشابه.
🔴
آنها گفتند، «لطفاً آنها را آنجا نگذار؛ او مردی بسیار خشن است، القاعده.»
🔴
من گفتم، «خب، من یک چیز می‌دانم، یک پیشاهنگ کارساز نخواهد بود.»
🔴
و او در واقع کار بسیار خوبی انجام داده است؛ او دوست دارد وارد شود. می‌دانید، حزب‌الله دشمن اوست، و او وارد می‌شود، اما هر بار که می‌شنود کسی هست، ساختمان‌ها را خراب نمی‌کند — فقط با دقت می‌رود و او را می‌گیرد، اما نمی‌دانم مردم این را می‌خواهند یا نه.
🔴
شاید نخواهند، شاید لبنان نخواهد — ما باید کمی توسط لبنان هدایت شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/128734" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=NO9d0sgC-oiXWf4XhxS81dDdiVFewbEIKBqnboSTAiaCFQ304AQFGToStMypUCQqdx6vA3Aknzjew_XKxB49OvaBX-R1adoax7_GonLBLopeJHNHvhlCUnn4QzTRIGDM92crVhZq7qLw1iaVqA9H8vo_cJ8YS_7HbuM8CIko_J9WlWT0UfGv2NmJPytaPcggb8eS2rfIvPRs_o7y1rzMcSOdl8y7L0rTW_my7xJkG3Te5q9EcpMI3QQy9AmHPEcHUhwKvPh_hG5RjOBfSwJbWjGfu_TTSSc1aUhG3GJORQbpByJ3OskcbAN_p1rDB2fZzq53lgRtJtexbLZd4_p8AKmrplzbV_1VE2JMTLWOYteYLQRZuWe8yIRMdePCEQ8Cp8XCGr-aVzpr7YA69FtaL9ZchC2BvJqeurVzX4kz0rAQFmW8hGw1dq2qEoRtqaEa1J-uvUr06D3VF9OxFU_uPLT_aygfo3HNOF97-ISBc0Tng5WkLxttob4sfgCzdIE6LiL6pl3xpqJ3re5P0_ED_5_rngDA_cEuoo8aeMKW1tdDYkT1AzvZHdLru9BTO7rR5sj3HW2Q857Q0lu89sU2C0PXthv55g6jR_7pCrKAPyyg3U12MECEyvIVx1rO8ZL1NZhjZf2V1jTbq7FHCnisHXRe3Lcx9rIw43UOSI3jH18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=NO9d0sgC-oiXWf4XhxS81dDdiVFewbEIKBqnboSTAiaCFQ304AQFGToStMypUCQqdx6vA3Aknzjew_XKxB49OvaBX-R1adoax7_GonLBLopeJHNHvhlCUnn4QzTRIGDM92crVhZq7qLw1iaVqA9H8vo_cJ8YS_7HbuM8CIko_J9WlWT0UfGv2NmJPytaPcggb8eS2rfIvPRs_o7y1rzMcSOdl8y7L0rTW_my7xJkG3Te5q9EcpMI3QQy9AmHPEcHUhwKvPh_hG5RjOBfSwJbWjGfu_TTSSc1aUhG3GJORQbpByJ3OskcbAN_p1rDB2fZzq53lgRtJtexbLZd4_p8AKmrplzbV_1VE2JMTLWOYteYLQRZuWe8yIRMdePCEQ8Cp8XCGr-aVzpr7YA69FtaL9ZchC2BvJqeurVzX4kz0rAQFmW8hGw1dq2qEoRtqaEa1J-uvUr06D3VF9OxFU_uPLT_aygfo3HNOF97-ISBc0Tng5WkLxttob4sfgCzdIE6LiL6pl3xpqJ3re5P0_ED_5_rngDA_cEuoo8aeMKW1tdDYkT1AzvZHdLru9BTO7rR5sj3HW2Q857Q0lu89sU2C0PXthv55g6jR_7pCrKAPyyg3U12MECEyvIVx1rO8ZL1NZhjZf2V1jTbq7FHCnisHXRe3Lcx9rIw43UOSI3jH18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حماس: وقتی به دنیا آمدند، با یک تفنگ ماشینی در دستشان بیرون آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128733" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: امیدوارم توافق‌نامه ابراهیم را گسترش دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/128732" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: ایران حزب‌الله را دارد و این مسئله باید به نحوی حل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/128731" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=PRcb9JSOa37Xjo9HpBwSv0qwqEUJZ00jIPInlLIJZCMN2lJAAcpTnysolzYNAwXww4BfT_26WBs-w400mP61GoeqSIts06khHvlEtAbJ_-nk5_yly2tFQVOSIDbTRUgFaGVINnCGLV-uVGestofpg_GtGQdvkozOGjZ2UxHkgp6T53pyXM4H7uC6iM9niVSR6PJBBAIXkhlgDuN2-gZqM370eHdAi4k30mfF4XwKwHL9NgOpXlczJ2HqtEWHV1bqetXZq3WnmQel0_1M26g5ZEMnVNiddIUgDNEnaBnTEZ7bujoemkByENXgPPVTrFAZ7hR4MZ238wLk1gp8OkiKHpT1-eLVvCcFo6bNuh95TgMojB-FSa5-jyy_byUl6pLV4TTlIElzmMVJHSx1hgb1ci-8jUgXAbbNUknY61AMW-Te_K4G-6QyqkTpMLvZsd_qs6Wdr-hPov74wzffUIzpVeOz162zPN2R9IS9IulUHeVAg2INiE1juN3NixKE7KyDKWYBwV6mACzotuoGarRwn0s4u_zUywMx3u9h9aVse-BGOnWb6nrpe_PAPerOHWJoP8YfI8jcerrUrD_OMyYUTAPo_jcPFRvTbNGN40_CihIezAhEaKYAcTZeZ0Tzwg2a5mnkh70VuYswA40vAO1OM56tbw9A-HW0VF9hFas3yHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=PRcb9JSOa37Xjo9HpBwSv0qwqEUJZ00jIPInlLIJZCMN2lJAAcpTnysolzYNAwXww4BfT_26WBs-w400mP61GoeqSIts06khHvlEtAbJ_-nk5_yly2tFQVOSIDbTRUgFaGVINnCGLV-uVGestofpg_GtGQdvkozOGjZ2UxHkgp6T53pyXM4H7uC6iM9niVSR6PJBBAIXkhlgDuN2-gZqM370eHdAi4k30mfF4XwKwHL9NgOpXlczJ2HqtEWHV1bqetXZq3WnmQel0_1M26g5ZEMnVNiddIUgDNEnaBnTEZ7bujoemkByENXgPPVTrFAZ7hR4MZ238wLk1gp8OkiKHpT1-eLVvCcFo6bNuh95TgMojB-FSa5-jyy_byUl6pLV4TTlIElzmMVJHSx1hgb1ci-8jUgXAbbNUknY61AMW-Te_K4G-6QyqkTpMLvZsd_qs6Wdr-hPov74wzffUIzpVeOz162zPN2R9IS9IulUHeVAg2INiE1juN3NixKE7KyDKWYBwV6mACzotuoGarRwn0s4u_zUywMx3u9h9aVse-BGOnWb6nrpe_PAPerOHWJoP8YfI8jcerrUrD_OMyYUTAPo_jcPFRvTbNGN40_CihIezAhEaKYAcTZeZ0Tzwg2a5mnkh70VuYswA40vAO1OM56tbw9A-HW0VF9hFas3yHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مردم می‌خواهند من پل‌ها را بمباران کنم.
🔴
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
🔴
اما ما آن پل را بمباران کردیم، شما دیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128730" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=PI_Y4sm02L9Ku-OQlzNZxokYwJhMgC-fGits94d-sXmiyWvyJkjpThqtAIl6Zd6O3mzvWOkl-1CjZdSLmaTkb0BTalMp3WK7AqHj-koL2MuSukkX45ZJzDTLRYKEgSP10nH8Khqgb-v05howFXqGCbVZTrln5KohdDaVlqd6lj4GapxKvgAvg5lL1sev7O28R7-O9Uiv05zelA-vRgZ3Vj0XAJ-4d-y_46zA5kPl0JcyCJR-ChODisib1TbL0ENQHUfUgFZIK3mWwkJes56XWcNE3W--RdCc4-ndyNyuQQOLoox3MliRS6D9bHaxwq_dqqhmyJLy2Q0ohIyxo2oGcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=PI_Y4sm02L9Ku-OQlzNZxokYwJhMgC-fGits94d-sXmiyWvyJkjpThqtAIl6Zd6O3mzvWOkl-1CjZdSLmaTkb0BTalMp3WK7AqHj-koL2MuSukkX45ZJzDTLRYKEgSP10nH8Khqgb-v05howFXqGCbVZTrln5KohdDaVlqd6lj4GapxKvgAvg5lL1sev7O28R7-O9Uiv05zelA-vRgZ3Vj0XAJ-4d-y_46zA5kPl0JcyCJR-ChODisib1TbL0ENQHUfUgFZIK3mWwkJes56XWcNE3W--RdCc4-ndyNyuQQOLoox3MliRS6D9bHaxwq_dqqhmyJLy2Q0ohIyxo2oGcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: توافق اوباما راهی به سوی سلاح هسته‌ای بود.
🔴
توافق ترامپ دیواری برای سلاح هسته‌ای است که سلاح هسته‌ای نمی‌تواند از آن عبور کند. هیچ‌کس نمی‌تواند از آن عبور کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/128729" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1993599568.mp4?token=uVgfhIhJ6-bK2yWmwNxvo9bSDfM8oPcS-tXee576RVjCwmdRtPLhivSg4elTjCn5s8eVWMElXekqB_QmacRN9DSBjAykIYuecuxyVvDnfO5Id1lWrL5zHyGEE21eS6x1KlaVqXh1-HhEYwQdAqB-QDgn0pRHAnmyFj_qZ4tUcAHtYamAI--_hZ0rQCFMq_zFxx8YPesMOid7g8CmUaPwUkkVf03QgZkwQJ_wldx72vZOORx3jqQxDsHRaLE9KfoVnySysFL_AQsETjUuzFW1VOTBTwQZTqPc0YwmP2zOfM6Eoy4iRHQbpUGNLztV3jwWjGXIr8AT2aj62EAqhw6FbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1993599568.mp4?token=uVgfhIhJ6-bK2yWmwNxvo9bSDfM8oPcS-tXee576RVjCwmdRtPLhivSg4elTjCn5s8eVWMElXekqB_QmacRN9DSBjAykIYuecuxyVvDnfO5Id1lWrL5zHyGEE21eS6x1KlaVqXh1-HhEYwQdAqB-QDgn0pRHAnmyFj_qZ4tUcAHtYamAI--_hZ0rQCFMq_zFxx8YPesMOid7g8CmUaPwUkkVf03QgZkwQJ_wldx72vZOORx3jqQxDsHRaLE9KfoVnySysFL_AQsETjUuzFW1VOTBTwQZTqPc0YwmP2zOfM6Eoy4iRHQbpUGNLztV3jwWjGXIr8AT2aj62EAqhw6FbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن زاید امارات:
محمد در امارات یک جنگجوی شگفت‌انگیز است. هفته گذشته بمب می‌انداخت، من گفتم، «چه کسی لعنتی این همه بمب می‌اندازد»، آن امارات بود.
🔴
او یک مبارز خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128728" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
🔴
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
🔴
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/128727" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق پایبند نباشد، احتمالاً بمباران آن را از سر می‌گیریم تا زمانی که به آن پایبند بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/128726" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: از شرکایمان در پاکستان و قطر تشکر می‌کنم؛ آنها تلاش‌های فوق‌العاده‌ای انجام داده‌اند
🔴
امیدوارم این توافق صلح آغاز یک توافق گسترده‌تر باشد که خاورمیانه را نیز شامل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/128725" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e52341e.mp4?token=C4XYSheZHYqFY7pk6kW2jF1AYmFAQIQAz1Xni1d54FWaY0bihJm0rvO470fS99vYwjb40q0xBu3E5remvaJZjTcS5gmmuhJf78VmIKndh55b79Jww3jtibCXCqD4iYINYe8_XN2jyt2w286bp2r3YT1V24s0pcqHZmT6eeBuUhH43X9OuTNLeSOXujaTwQAUfpO5UD-Zs8-yLtrbpu0mPdLuLDleyq2TZP2R9PH7hELft_k0Sa76CjawXlF-n-8YnvIN-sBeO4Xnnq89XXtPWoAyYWBsC4FSJCTg96z3OsReD_x3F68wl9lXWdgZG-0w8vVkKYggfWjjbeEheU-KXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e52341e.mp4?token=C4XYSheZHYqFY7pk6kW2jF1AYmFAQIQAz1Xni1d54FWaY0bihJm0rvO470fS99vYwjb40q0xBu3E5remvaJZjTcS5gmmuhJf78VmIKndh55b79Jww3jtibCXCqD4iYINYe8_XN2jyt2w286bp2r3YT1V24s0pcqHZmT6eeBuUhH43X9OuTNLeSOXujaTwQAUfpO5UD-Zs8-yLtrbpu0mPdLuLDleyq2TZP2R9PH7hELft_k0Sa76CjawXlF-n-8YnvIN-sBeO4Xnnq89XXtPWoAyYWBsC4FSJCTg96z3OsReD_x3F68wl9lXWdgZG-0w8vVkKYggfWjjbeEheU-KXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/128724" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128723" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: جلوگیری از دستیابی ایران به سلاح هسته‌ای، در کنار باز کردن تنگه هرمز، مهمترین نکته برای من است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128722" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: این دستاورد بدون فشار فوق‌العاده‌ای که ما طی یک سال و نیم گذشته بر ایران اعمال کرده‌ایم، امکان‌پذیر نبود
🔴
ما با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای مانند موشک‌های بالستیک همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128721" target="_blank">📅 19:59 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
