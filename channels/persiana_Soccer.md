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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 470K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX99Y_HuA4cO-xdaIKvjb9H26NnT54BJtfCd5AMwNrPTp1SlEqNlFUDU77UNJNd14hj5wC6-roCA-UZUONlr9lh4UmRuqxHR2vHtUek3EtT4UXefOk7iex-egi-dNU4o3SEu07WSE1UGXzHdw3M6c-Oy_XyKMgNfNAIfKaZ-riuUu9R0B_DeAzS58Gq-lpzjp15doMb2QguBHbqZq70c2FduWKBPP9reWV6wLDsWMTelVpfepYGBtlsg_ledm-HKG1uiOLusVL3SOgS3Ps3NdbiBM7_nVvUvvpH7wdc0Zl7inK5d9P3eZPEMpYCUwexV6pnla1r5Be-LOoVUjBfBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UciGm-K7cCiVReEYyecFcTGG3G0neNxpOihPJUw8bnfMULB9aN5H5Uf7OYWwNYiRtZtdst0SFhiRqfJO4HZGllzInUhetO23iizYW7xQhZNH-Lvn2_wOjxNlqER4lcgZ3dT5pt2yOG8hzgMhfNcudBFihfRq03lHNSQqpkcgU-_nx1Srb_locf3ZjgQm77VHyeTpAqTAw_ejSMZ-B9k1oLk-r0xxav_G3oslgKybmnJn3O0qFepo4ZgBUdNKs1Hj5sDuzM5HAsrBKVlIe6iCWtwPN2uZaA9h6_nibYlk6YjLc0kqrCmiAVtRrHW74G3AibSWPyBNo_H1t550Irb8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB-F3OfstbJwU9bsLg5qqqGRXX5FDUxj8zOci0e2wPtT35yTFv3NWev5jxIGxxfJyYM1A_d8QJUyrowp0ZCKQ4b5Buta7qhzPNWMAmef8bie2KaEjClD47h1-eqfzi4nEIBHe5Vhg2WI0UqSFX7jKbKoTtVxeLBnIDujEIYqGRy64jvqSA5tICw4kFxAgxc5wZeqo_14oI4EAm1ml7AzubcS8zZfXdK-d8dYaBIcKAjs2yJu8Lg0pIJkx21U_r1UWJNrxgS9ACvhNGUQAfnfAqfUvkmeTqfen09uj7n9ispQ2jo9BtEUZNXBX93tv_LXx96UU3MRi-vdWmVnPfs1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJVe8IUBdBNdawenDOcRf0Heh9krbxA2Kacs0jtV9VSZ0iOFMgUmKZHXG5I0gnNvAB7WgAcDo0tckKFDE2nUp1-2_t3SfJZ3VY-3QWb3VA8fRt67EaST1ZFsoFc9ii431D6lwk1WjaV75elybDlwnZpSE_Wn1XghQ63i4W5rOWN29sUWTJUn-7xguQCGNd9nAtFVEovCNAJMQJRxp83mXKXJHkH9PUTWPK5yDfScEE4HyTemRQaXtxlAMnXYnDT_z9lw_sy5ZHQBuRe4eQqzXnbRzfLWnQ5slTlBluRy5hpPaq-yOMpb6J061mFozMYPOSCGZ9qIAsGyodJh7HdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUNo-ttyVjLvGfVYFn1e0camMucDES_qLgOndyUqAfMCKJgl4aQEM2F68YjT0GAUoBqcqWRAj3ntkwK4lrV4UfUiDVn9wgWn9KR02DSydRXrujdgLmIIepC7Mqqgu4Zrh2AG4QPxSFQlL3OA94Si8feEHXXKYhCWaCni4NI4jktYxTDl2Jdqmn32tMLCmCp6UvRX1NKx0iYaXgzBMMJtX_pgJ6WT5sl6zAGd3zwiXb-mJxcYYYelE-XGd03gEF8RyfDNL2dXos0EkbcoCAA4TyBfB3lq_v8g_-inUymMCwEimyAd5lq_UjCCVZVpARDnxxlwoJ6tj_b2d6gQ-oOX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgzhJJ8U6P0klz_QtszAjNu_IF_p2I4q4UeZBj57u4gHRAGkSpywXgGKDBFmAOVpDVLO2zo5UpTC7SOzQksp4uJTj3WfQueAvStDSnXm_O7PmXcjrxE5mvlLEEhWixO9JLgFl50DNtx8bXRPKRTLPfn_qDTKq445r4uL4SfW1zeteJNVDsL0ErqS3Lc8DI-boxPQL6wkGPKk0dMYSjdw84vh5gbTXgH-xJzCRguaJY-IjeosPRaUn8FGU3h0sd-AnQ6Mop0tZaq7cKzCwDURjjfQyYJw7yy2zODrsN-_fFj0elWzA-Ln1QgU-rboWab-KQ8hEmFc7X5VAfLj4csTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz1VgjnzTYZlBd9ZVrWgWVShn7_w4gkTlXrpdCO-jYOhlvcGwRXLS9iIwLB2zP11jyihWbPINdATn7SX2PZ3cVRlMm7Cxmi2ABrTRUHmwAwi6yH0uCa2NAXkLgWQ9vVB7GJ_wkFd0SR0sfZox6R2AK4zW5V_WTizSV-5lt6mmyZm4QHCJXv4m30zOaKMPq2v0nFLRK9TRGpTsQT2tnZHBPfqxN4zpPHeg06og7QxGE7q9_hpdQt71yj7LXe-smMnTUNe50z85LhfLQ78IfANTXc3eN7LUpUZcPC6Vm7cHzBrIjvRnaYyExpxu2uU54ZyY5ldPOdDHFl9Czf4_tbBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_YEOQW4R6G8zz00w1FNI_ErnKY38hTodgz-Yji5g-ep3eIa6oerSlUSS4MYpa0PydOPrrlRTnrmoK8iqhVHo-P8aCStnf5d4kRXzzIFU_nLu3kryWFBRF97-URaGBcXUSR2bCaa6UgkU_wQ7Kso9m-L4Xp6BOWLKBxaCnt45o-BoMPEp4kyiasChPTJ2-DSaLM6b3GnEM5rSz-pT8k50VCKLhApt-tZIMamgzcMNjMhU8dZyeL7yrAHy7mG4PhEHGXiLweKyvSjD2akyrLSed0fHqYwKyMGy_Ys46uoupEmFwypyxhuxM0sv0xoWL33TnH8mOxBVVstHU3KHAKN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyABkFSmYETdEcqo32rAhYzS0a4Fw8nFwFu0EB0BTNCsvoM0jnUJXmScg-dqRODgd9jjeGEXThTuiak3aop8cQJTUworeJgbBzmsStyVZbRg2gM3jnkDQEkZ0ma7fO8ylIgSqNxF6hAtmVF_AMbc_WCRa2pl8EGaXU4pFyhmqXfTYdCCYd3YdNfYKJ93hZybWPpHDozgFy4Mk_cB4k-abndzM2PBuJXDZVYfwJio_u1D_ZBZ8BbsEQqVkpFbu6sbgSD7q9f7_BVjnR6uQrYd7c2dUWtxTlpyn3b7759sImFaESG-C6eMtYse35uBPDc1vWdBiaqxMDY7Mk-5HE50SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPNvx9gVJO3LVXfox5jfRbkewAttMPRrwJiQ4igENm6psWdHGSiY62azOkP68F1BjEmV_mJ3YcjutVKRRI63-HmPQ5PUfarto5JoDpR94qmQ-l88wbufPo8qLN661lBM4C4ue1VsTXG9Soxqgz2bxUImlb9qhkT4C_jpcv78QEziBANMEC86Tv2V9Spq1Uc-MaGzUrgU_xTyt7109oXzqRpulPCG0pD5Nko2gPnzb-thadD4GcfNmGzxZw4f0uZTYetxFLSAAG-vmovsjbjyPNPx2Xjy1hRFDroc2rb6j6kWqFc_WEghuwcJAeKTbD2kaX9QB-qTB0_ewnFsLgEcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKBUpOAwpKVlD7Kh48djiBej53eeuXWe1u7NJk2wRpzM5bmu8jcvlpPvXAIIjRcEEQvnUaRz2se2eJgD26ir4JHnSGmmFf9Nyph8a-nPZgzzp2nUy_n_fqvCWyEXsDTw4hdktadctLA0ARXDgXtAU23CX98y8xLITYYuTq9otixhdqbhDnjmuhzfy0tgZtKFPPalsi3ix1576cCx3pn_w-BIpks_7c4NnSB9DyU2CPGC3_sfVIACAskhaS-tF5KEqE1ys44V_ASkePNPgkLJmNGGZzhmkWrKMeN2-AadYQY0W1pW3NNwKLq9DKl-YiGzonftTXmNTodmYYG0uDTqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHituhyojUGvGyemVKVHj1hfRzcbAC1PZpjivOJhOIlqaS33fKtsrSF4QIHrpMYQoAInvatTp7KkqiLJgzgh9F03pt_NqVcQz7xjury2D8RiIXQnALN9Q1vy8ZIg1WTZ-ha1masoizHOLbBVgL319gUA7ckEMhlJZlvwfI1SOQGXlVz1cDSRvqvIX5odSrCWZKmvJa4BfAHyh2kloHQ-hLQt12eAkCtOrh0XyMbs4BaYEwuqSLe4ybbKgvlr9bN0D4bejtpiJ-8j5MyiTGbmDy2N2ZkTuz7kNkrtGRrHKoMh0WgnhcOQSoa3JpBiR-I0kqmF_WYtIPf8gu2TQOKzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCsSlCGhBmocdWts3RmbQBCTZXzbYCfasq7o64kI1euJrhC0KSIbPFovI0vmPpN3mdCP8Zo2uITU6Qqibu9_3y1mqNKU6LQ_LA9YI6OKp4EZBGTRXKHwcEIA_CrIqSuz7Ytkh1iBnha63IUkiwXqJ9fOgVKCh73TZFDMjoMH8LDrpHC9QBHxCc6LnOOr6-BGcVCe0JONmv8Nf6FpH_iQcBYe_I3WdyfameUd2RChQcLcvovuIkHYxrN8Byl7ONHuV8PccStCI1JkyvRR0DWf0Uo-eTMvsFQIxwiT7aua7gSo-oO1HT1y8SO-LYqooEg4DnlHRjgOEForRDKnOU8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TArVDF089jWJpqXTMjCpL7y0EnCGqL6cs02Wk7LEDSNIr_quO-6eLzGTq4CvYFytQFsWfAt68ZHYadxynKFHT2uKu0LgViororyuyy2_O7uv1Rybv23nE11cxxJhI-fMsfBi2MkMoCeCPggb1fTfjx24QM9Vtne3auSZhiUN_2FpA0Igq7d68_EX8z_5K8xe2RvLmka2zOWod4J35ugly1vZl9e_oc_1QcTJ5PMB_3dZrMIPbqFuvZE-PYeep4tgI3UEsuCI_wGlz9VrzCE-P5PdnmVLAVgsDakdsuNoXqW1JCf5D92CgRR0NwTcZQuhBmya8kd823cD95Te2nXWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpX4iCHqNSUOxix6XXQNelmd0hoEKjsR6naRPHpDPzbsg9Rn1xyJSBGp55BlNl3rl2lCI48FQLIZU-AYf7w48jNzKxk6oz9Hsx6sf6oWHIV57S4YLUA4TOVXgXrW-osX4yGkEYXWIrl4FbR_gNQwcxNgPGPomya9a7Bm9viuZlHBntjrLKnAO2ROabyjJ5McCq3zd7Xds3J0-KibYqGQ9Kk6jCmU_fhc1E01FmBPUtnoz4IcQa3WfMyL20zFqIolsmv3beKUmkxanSlVvoUl9okURNm9Hu5SzQe9IDFE9sDoTblClysHzP4wPy0TnZH4nPjuY25-XjEQ3lPMBOVG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr-c7cKrdsUY7C3G3wLByU264hwpgUXB5uRiaPb_ADSK-13RVet6xZM7LgbYRAz5FWTFyQ5we6k7DjXjrus88uFeK0Z9AKnRNsG9tP_YUoMhvXHt44SU6LX27b23tGIYJDfE3YDHs45e6cakCsRltgNSenwZ-dbNXCjTijlwVxc9DA8fgr9u1W4J6BqJLdDHErIIfGGOmBoy0T2w3_nBKNBlI5-0oO5uGF77Ykmp2EHUFE_WiwZxsh-_1jOFVqNGe-vV5ALfLyowxNE6xfM76ovInvAPCocqVXlDyNb8ZLqYuILlbzjEdCYcagQ_J3Q07MKQiUwdeQ7LkDz_VWB8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSxiDmUU14fzexx7FJwsNap48J9S23ExhiDuC7JLephYrW827OLRalK6GHxVSp4REtiegJIaEDjgrfchVZWwhsrmTzEvZeMOl0nwXAVksJAwzrPON0N6rG5LxW3kGz3H_LQlVtdCPH3OeaIC5lsD8Ly6DFddpUirh0ChUYBtKgrTVgmRSHoy9bc0v-gqxPmustoZYsvGuS2BL8y_h5795z81jLSHh_laxsIb3CtJeZ-ENDCc4k7aQzeX-0wGbnedKd0iB881LHoUtejakRh9FIh-vYzOCTf0wBan18Rq5qSA6Tplr3L1wny7Zaiy0TX95i-wIQgPbsCE8G4ubQPwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZX430xGFZSQM1ClqUkJGiWafk8rF1Rh4msCIaApAmWIL8mPcd6YYcmwOX8j0Qjyu_6Oiv11Gf6BP0AosnV4c9U73Zze8HZY3IdEa95K2bwcWnzhItrB_uAiWNcb-fDhX19WpdrVBkF714_hfOUpsCKsVDKf8JUJWhKxeQpHCRsGFq1aCRqhRBrkFkEGY8IvnInvnpwQw2e8Uw7OHwwHd-_YI3XXTbgngR5qUSghHvsoF_EGhtokldio90qYdDqp-wGZ-FdJUtgvuM765vgAEnZLrI8NUHnobBQA00gkz5Crg8bagkuizcwP9PVqiGH91hUvT53m0_OLfCALqo-E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHqCBlN9Ph6eH5GT-SSLesqecRC3UittkxMKQn_NN5XScE66zhfPzSm9wgknrVtA7uHVPspd-cnXfv-EeSRUQS3-lthjrjL47-QCivSQh_SUiloTQCWesU5Es3nCqOK41eA4pMBWv086MYCYMWm8zUP1o5qI4QEESrUETcUicEaGkKeP9q_IfjbjsZSoNoDawdt-_U6rqrJaBzGr6OH3Y8Vx3Ab4tMpK4UHYa6uTvI_5PuB6lEKz_p5jWoCFULoRGwTcxi7mG9sn0qkNyGoShp9a97YZSbk6b0NJDloToO0CNnHPGWUFM3RWC7YbseaghgBqBwjfZ1mVsrM0lDexOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOGMS-zZCvpBQu49hqVFchL9Uaww5gd-7lBmAINn1E1faM7XJDizyyEJ0EFcWFAez-SqKfiIhHQoAwvBuIU7KJV9M2sbsM2iC7CrLTxpWtMBw3STz5XwVu9bywOtfJ9WBfBtL6G_6U1YdrvnMNJdZsWTrdCIA3TIF_t4jH1b_yytwMcuIO0QaGcQ8Eu8HFbMN3lQcxnO4xF9TgOfDvN-TVX7nlYXmxbELHZSOcMn4rNxDcYRQnE_ZO6MqQd5aNIiZ71XgqAmCAX3uhLtH-CD0ZgrSo6fjw0qizwBc2L-gxfqY3KiJU14Cmj7fHEbUul6FlG430z4Yjqc7kmZ5qKWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec4JG9GNJ1s5-iXnjJfDioI0fANMJUPiaxEHDA-nmo2iUdFHhdOC6H7M64utl60olRcFu5Q6ggPfHtdvEriTwZ30cComM8Y1UVlTl4wfqj_SeuEwc0M2PsjsB_6BY2hg5-c4oxDxQdYDn8xe6hIfyjeJP6zddpottWhnhgecvfX0h3QzyIW2IIf85rCEmnhqARS74vPPoF4Sj8wCzSw_Det8z4lzjk8OUB4xIjH9oi9PEhkL0n3Q-z7OtVfIpgShbZwoNptMiUBc__08n2cPbcbLg_HxwyKiM70OdutQ3AvoW-_Bgl1f6vBH0l5zfev2lMIVrjiV0AzKQ3dhEzqakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKv05iRbg_w5qmDgUGZT-U9QsY1kIcHKl4V6bhbevT_rm0jOOOD-1IKAUt0khezXhVJMwBrRC-DAwBmvYnK8CDltc0Mee5uF3hMUgRe6jvvCFVKywIM6RYtdhHJVeMqNIfSsj5w0ILYnDTmT82QZH-2N80__8Ou3YCwtRCK0Tlxcx85CpIbrmgqFN61tykSd633LRtkLfLS0BgVg0mhLAASdn3uNhxGzoJgNx21lp9bU-Mg7BxZdNfjVTzth4EByGXLh2pPCtHq51WSmWkEScdyUxWQ-iNc5yw1eSA2jCucJgA1L3GiPEPxY2X94l6yhwOyuqvixkMmy6UpaBpwXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRP5ammiu8y8AcNi2fu15ogD9zUs8kT9t8DbieNsB7DphgoqkbL6jebcKhDn6CPEyV4zMraZk2Erg9LVygaMaOxcCYGrFDNkAtUiVV6oN7tb-hcabQIfsEBFQi7wLnhD11D_1gA0LwbvyvlVtZsY8fOZzXYPzUlcHmxQEV9L_rZXyP5tzd4RwCsglSEKl_vZAqcreUQQfNFDB1o7kqDpobefPj89vANRAP7hmr_EoXzzCCxLOb8awR9qwr0M6-9XWsOOkiUvqNjdqJmtsogOr-iLhF2ZDxxeNApBGqRlCG1y_xVyB9Pa30kYK3lSbJSixBS3YSFD_vMRp7V82T8fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWRl7JGFqhG07MHgWG-Oh-Zbm6R1qv07dVgmQyl7vEHG4sMrPCQxt-Rc-hMPH1AmbOyvLRFKqTkEztfevQvl23EHB1LnW9b68iER_mNV8ieDlOuyTs6ADnZl_UsBDAw-lO3be9k2yz6AuVoLDwcNBSHjtKuw-zOJeJPHewCB8mPGuk8QMK-PrClpa9xGyQe8o4FXXJkRHaUcn0CkrBatWX4ftoxzx3KfkL-kdVsE8R2WYdsOoiisoBOBfJPsaMXOZc5KR3fv6ZHw0TiyjOa2biR1PC1yYm2OqkLsvdIbWvawJMYEXV5810UrLA7BPVXSyQRe6kwFuoE3dp9f29BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwp-az-yU5-SQJe3gezLMywvBxvkqLEP-Zqcar38tP1tQiq5HDemCpC8YFearJw52Eku-4CbmRbU_aMa-vGoZeTMl8eXZ9gw6ivXB69Nwbv0Okik_hXUjRn8erFLcM641xWKX5NNdKBpgj1J9g2JwfLbctkRzPmWGYhYIjv7uQFmSgssXTJNuRJ7eq8Vf4n6ne10BCpekl61bAuP_P-aWKxcrD90l8tggVgq1uWQtOY2-F-Ub2I0GAZe2lOk64x0Afox9hdiDjzwCqBOTjcL7uMLRGPT9HghLZ0HS39T5dO2dPws8VTWEd-5MaqhhY8TGyrscPelH4W8Zgloll_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6J8Z8v22e68jgA8K_d2vFmKLN07YlB1w0VXSHUev8Aw2N3-ORX2j5_LcKSZmdeRs6WRCUKb-0Colq79JfmIsnqIUZlepDdZfJ5N0rryPxFYhfRXWgi1AM27giqMObJjOSUo1QrXnKtSOuSFYFbH3rZNBjwsm0lgxE_ZVaheI2BJ4e5LfjnpvM_4giBGITlljUWpJ79B-b5_RouC17xO2kqMrcpL8zcMVyiVQdKMdUFWejvzI8c7kNhVvwBrd3zPeL7Bod6KZXsfkttybr9Fe-Nc8qD5VuNrp9ighBhPgchnPj_kJXSTc7LZvJGRbUOjU0zQMfMDgFy6HVt5EoC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCinNNqw6Xl9mcnBDbGAzM52aUEgeud78nNvWZVTspjBpcoN5ZlaTfn0Bo3VZaiY88V4NsLyzhNyszYVYCjc-n5p8YZesXoRZL0kW3NjfYHklusI8S0KhCF77hzFDx838kXsarlIU0KMSLu4F0ECKXCnossS-qx7tZblYNNIXFpP3NXuiKw-3a8j2CIAso0V_XQWQTDm1qsKBaO3K9GXQjV1EDyiBHRPGRDnl-lWhAOq6ia0QVqx9agEb2V03896UhxdFq1ESbsIv4grBt1BKh92fkdQoTRuGo2DGVTaYkguG0DUWF-clwQMnWHpNdSS-k0Jbeiclxr3ZToMgAjJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9jf91FSqqEDKf0JlRmn03-OUum6axSXHjRvPJutVNjDvK1ZLxNp68a6jOVLGiNmCzUiaIhM7YZeGl-VUHGAH67R9ADrbW1gvX1hmaCAPr-Kd19UxerSWC5uGusrEowyYG84KSHxvug4_ipPpjpRHxlkUBaKAz9IiAHElO0kj2-R521Bzy7uE3dNzhTz1fZXlr4ryepYIzg6w_IQNNCulyI1dOPSMuN3czo6X8GtmlS6wpn1PPp_wrmRli0EGZb5uAtW5M6Czcxf5rHb8WPjzDXQRU6N6eqY48phkmJw8VDTR46ON_87Jjt71wpCPFdxOXjtDjGvo9lEeRGsZGLyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNtf-VoGrLGz_c-JzFXk9BuBDtnZiDHmJlKz3x9lqXCr84JA6hCk6gAJoEWa1m1zX1_NnIkqw0sCowV8s0PC-9huwfo6DH0h-lhSm8145QNke8csWpDv9cekpQh0zxGqWOMc2dnjfFCUTALIH-dmJF9_epJheiQYKrBy-NkIIBh3wXCAklbJVO8Ksfi4yA34TO6E_kn7D_8zKGJMgqlvRxEJ0Dhf8fVQ7ZMWd1mdWOyg00avZh1c29xM8L9IPLqtXGxq6XEl27QXOuugXca_z2fu-lCLlF8MBmkL1iKNzW_N0CSUSlBRdXf0QubixxgXqqp-t5PbNuMv_13a4Irm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsX7ok2KTBOAoUMV5G4GFVRUQDDbws26FGi15jVVwvbbvTykqcBY_rGSBvr-zjRAUVNjclstK2ugEEZd-EEa7kOnQQtP0fbM1i88Tx8LJRgmzr7vQHN1GNP1GPxdySwQ-APv-eOZTc8oIjc1e26sSw7Rew1zklNZgHFVAfxfXV9kbE2Hjxbd6weB257X-dNFUCjs4zIJ-AXq0XtnMExw4AwwEPFzU-SlGT-raTKeFbDq-b-ZLv5D4dBnWgFDT906yte88QqD_n9bA72nFLrNqQftEjenFdCurQ1-adE9FiNWu_qfQ7080kCj_is8A9Lg-tleAnez1eZCr_-Q7ad1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq_-qXFNY7DbnVO5ByxIOItaYulwNK4rpMrv3DpXLe4s5Id1K9VZIRv7THQXKdky4iW9v3BYDVMGVSPZSYqfY0evmzYrI97ohxa2Z6cGHSh4rqcUP0BrhI8x5wi24tvx1RqQhW56iQ6Uha3CTl0cFH5OxxnguoJa0tu1pIuo8hKRkkWWvIArnRtQwhTkMPMXnKmFL--nrQGk3swQJ2EY0fQ3gg6QkueBuwxNVvRqOdR6ZdufxHXSjDo0Rn3EKyNHSxF9R3io_C82lvgfeDd0tXl1CXwmRmLoaiohs2Qu6papIHvVCQPVRC4cuqNY8gqTwCT3wjf4UJ95yd-q4jI8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=d__iMM4fzTbCKUXdoD3ulxCoHkWtBpxyYgy6LZ22NfnND6mGqCfHoN0oHpRVHVa1OtdrECreDB-Pk3KRf4i64Gi4fNVQJ66skA7CyT8ysspxOIliGikMQaNXqMLbAJrG3UWf-P1va-88Icd2tCd1rkU8Ml7YRPgeermu_JhAND_nPbvZwNVJ6wlmcZzeXwqOOz6fEUJ2j6zLpxSihrSMsL3pQtQ_ij7WzKCNA0YR2rYzUaO4rD-_3baIzGW5duHuUNeLL7yaQpCMgqK6VSUu0LQmHFuvxKXq1XyYDkkO-OwM_clHitvmxhfEtP-2AzMnW-j3ULV0hpFKLYzNBuXL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=d__iMM4fzTbCKUXdoD3ulxCoHkWtBpxyYgy6LZ22NfnND6mGqCfHoN0oHpRVHVa1OtdrECreDB-Pk3KRf4i64Gi4fNVQJ66skA7CyT8ysspxOIliGikMQaNXqMLbAJrG3UWf-P1va-88Icd2tCd1rkU8Ml7YRPgeermu_JhAND_nPbvZwNVJ6wlmcZzeXwqOOz6fEUJ2j6zLpxSihrSMsL3pQtQ_ij7WzKCNA0YR2rYzUaO4rD-_3baIzGW5duHuUNeLL7yaQpCMgqK6VSUu0LQmHFuvxKXq1XyYDkkO-OwM_clHitvmxhfEtP-2AzMnW-j3ULV0hpFKLYzNBuXL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8nX_HKHEcdKotkA06W-22ZYw6OhmvMV6VxAAfCIOiH9BydBm0qrYNNxY9m2_ZTduKLBSU1UOQOcw5rAvSKqOC3N188b7VUOKOOYtHPJLInq5Fvxj5mF9ykkLsR8szkBKKU43DWBTjAol3ZT80g1MBCUJc2T4oZqn2UBPrqy6eXpWgLz2WggKlIJVFBGzxkqMDGaK49SgI9phcUfH9rPI_rTj0oiOFC7kxm3H1psYG0MMALtSUpF5arErUuZXKYdON9BAH6Gc2KpveMQ8Ou1VLZJQV-mptbJL8RON1Sfm2pUb83Jn6HySW0dzobZcDyEsjRtcMwYmermQxBxKsEp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=HJt_cUMcmSKlCFichdXCPVTtkJntXErJNDkupDIiVx7hpI-kT0pyGARItVEWEq0ZBPNVhaDBIppHLlPw-jRQcn2vU2QAp7yyqiGX7yBda3El8QSKqiqYhbM5JUXwdpeLCvB-y0m9MBtd0LfvqQ0N8BF9XQDvAUXFJGfhoWUH3veRxoq3TkwrWmyXdQkYHQGg8fhL7oA07ZVQz08-FFjuVC7RgsUOhXPBYL4Qm_Qx_pK3P5ICvcT_QRfTD0eRR68UnI5BwdpLkJwoz67qyr3PTuGtUimN5pvXcAXFPhl3xnIKjvnDkCqARc-QMmWVliMXf58fpiORf_V2EoG3C0A2Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=HJt_cUMcmSKlCFichdXCPVTtkJntXErJNDkupDIiVx7hpI-kT0pyGARItVEWEq0ZBPNVhaDBIppHLlPw-jRQcn2vU2QAp7yyqiGX7yBda3El8QSKqiqYhbM5JUXwdpeLCvB-y0m9MBtd0LfvqQ0N8BF9XQDvAUXFJGfhoWUH3veRxoq3TkwrWmyXdQkYHQGg8fhL7oA07ZVQz08-FFjuVC7RgsUOhXPBYL4Qm_Qx_pK3P5ICvcT_QRfTD0eRR68UnI5BwdpLkJwoz67qyr3PTuGtUimN5pvXcAXFPhl3xnIKjvnDkCqARc-QMmWVliMXf58fpiORf_V2EoG3C0A2Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOJhbGJMXWfFGqBdidY55TkJvRcm9kTpLiE83l4KprhTVqX28VT42J06cPjoaD01klv6fkPr8Ttd1nAlYq-FXsWd-5L4_aa6cgaFEMEJMUgRTJV4a5CQTs6ekByViaOjkYzUA1UdC1IeuHZE1tk0epCFMl4hHVfiZLQ-Eq7kcxk_3SpBaWOJ0mBf8Y-f4LQ6LuyavSccL-6yAV6GsU29CwVw4ARq1BpxjJVYDyrbEzjpRsSoLyi5BHHrK4vkfmPs5wh1LSuz2kz7PDzQrQOOHOz2GKwFExdZBuXHYZNokDQplUt-vdmt1IcXsEjMK7uJ4R4Lpody2lz51hrFEtC-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUMfzzKJHiIO0G3zX9iwZA10bqFzJ2iB78oCfuhXPT1eiO2r_P1l5OvXZA9WZ8wGlrmBwq7ruK6yjkTQOO0762XJ1lP2pJEiYHLO6X2W6J0D8oTMempDFi3Af3lvmhrr9J9anTEJKDRhXnW3Gag-YMLtZgiIywrltV6mHEgbbiFmp7-zkVwfefe7Zt1Tjl2WDqEWDWWykHmjNwMaBry8SmS1A8U-ZM7S7iRJ58V-t2IagWs8I5ufBK2fGEub_rbQNOregTVIgILL2hr-zU57iOILacPHBWrvemoGpVVjxX7KYl64ohqFMtk6pgIlHX_IZY_XecvJv0F8DiBMpGvN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=YRoudtYzidHcDYNxZY5_aVR3L7VqEVMpDOEzGE4Dqrgh71618399rujV8PPZb37tE44twEW0iw9oejKBmh9_Vxcv3OCHssf2N40BxPl67Ip-E8t_jj3u4_L9HFUwPZNJxYYQg1Q2u5uzpaUYRMYYrpbW6nedg2_X-Bgg_4TiIJ0YUSbw7etKUy3vI999hqiBtGPbPMd7EkmuxmgnOtvVOXwfPmNoQatbKAZweLYQB91HRKL1XSOymrI1joEm9YBKSO_Qxz87IZY6JGSjpP-WQN_vwXy4LaF-emc_OY6MZAUBboKhWb9T0-chk-YBnzRKJ3EZUM2mnaX9T6HaX0d65ZBOvvM4N2qSVv-2EcS48Tf_yFwXolmb8M-f0JYEtPPqobPh4_00OMYgbdw_IAJlZeH_zY_CNAzgV7qqy_5u1vhfMeYMaw0NCe_S2XVYl5KtbPslZ4MufbvIfDsitoqHyHHlPE-NoJvX5VgGHswq1YD3m_EUuPxGq5NCMsjToRlAgnUW2LI82nLNZ3fnoqEyuN-WPfaGnGGsH7yBJadw2UiTUMdxC3QucZWpxQi_eMHUoq9fAZIpjYT7aXtcOOIcw9UFx4QktcdidAlLRbfyTi8P5TNkw9pP8kx6cteIij4_iJ0QjqH15TFBOO8J6aa4zfitZR5UDndaLAYEEFPO62o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=YRoudtYzidHcDYNxZY5_aVR3L7VqEVMpDOEzGE4Dqrgh71618399rujV8PPZb37tE44twEW0iw9oejKBmh9_Vxcv3OCHssf2N40BxPl67Ip-E8t_jj3u4_L9HFUwPZNJxYYQg1Q2u5uzpaUYRMYYrpbW6nedg2_X-Bgg_4TiIJ0YUSbw7etKUy3vI999hqiBtGPbPMd7EkmuxmgnOtvVOXwfPmNoQatbKAZweLYQB91HRKL1XSOymrI1joEm9YBKSO_Qxz87IZY6JGSjpP-WQN_vwXy4LaF-emc_OY6MZAUBboKhWb9T0-chk-YBnzRKJ3EZUM2mnaX9T6HaX0d65ZBOvvM4N2qSVv-2EcS48Tf_yFwXolmb8M-f0JYEtPPqobPh4_00OMYgbdw_IAJlZeH_zY_CNAzgV7qqy_5u1vhfMeYMaw0NCe_S2XVYl5KtbPslZ4MufbvIfDsitoqHyHHlPE-NoJvX5VgGHswq1YD3m_EUuPxGq5NCMsjToRlAgnUW2LI82nLNZ3fnoqEyuN-WPfaGnGGsH7yBJadw2UiTUMdxC3QucZWpxQi_eMHUoq9fAZIpjYT7aXtcOOIcw9UFx4QktcdidAlLRbfyTi8P5TNkw9pP8kx6cteIij4_iJ0QjqH15TFBOO8J6aa4zfitZR5UDndaLAYEEFPO62o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8GmnEnCEOvk8cJI4yx5SXz9LJ36ikD0oG_md4mA46rrLj3ajSF0No1WQiZ1FsVUbcHbwae4x8SF9icIM7c2mSXzCg2lFQ9O8N9UwnZzQtrOqwGJVY1ndeiXGqUmpr6Kk8gF0SR4tXieuTYDA4tO08EK8U6Cov3UixDpH356PGWLs9sYjKR2bOqvsvVBYnOVXNwAzf5yNqw0YbuGU3bseuOU9DCvy46BcVyK_sCJZzfs9F7Yc9H_RCCmJ3sJs6XTKf5mZGPE7t0QlUuargqXByuu3-DAkwhhrL_RLbTWtHqANCeL96E_BGN7Wxhl2Lhid8_bpCfrEiignjCBP9-uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEFk0FYjqVIk7ATOMcUBu_yQqhjxySUp9IyjbN1cV7A6-1qMLU0mZ3UsBszopeT65teLvGXdRfVDhSgIrnF2J_aahUUOyhNh0zYB6cQCm1bYVrL-Yri06UQrOnwSVHHWKDGIowNKY5sID6Ez5kpRu8P7kWe1BodVaxXNhXobi6R83XRv7Z5r2Rs63ht2o8qk_0yVQ9otZ0hz4XIoS56C2-NlKUXYxmtS7iYsez_CbkDO2rPPq9k0VGWa86LoSwZDNrMAge1nBybTAxlVeHK7Q789zvs3V_IDgTg0Gz5pB-33BMbsKZslTbgT0V8WTLSdHaCk5l70Ch6dGCaSpt5qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6vA39Qsmx20M9i8d8vXAIlJe9-1RiacJuvVGsDmcH8PDsMDC6YvMzXtkf3yTDgzLs9VEKnOJG4DG7Nf4Evj6an2HqDj5wi8YpT7S45hJaxJbkCeP7Wb_6m0-XG09_AusV5o1EwFKuzRuEOp6jRjnIHfSfr-ht69d-_j7-qs768woDpRZGlNxNsvoJ5TE_6n5JTUTEUOsMdRc1papxddzxw_WLAHbi5p15XxilfKw5YCtGtaEpJnoKH9zopguZyiaJODNSxbJk_alkx4qdlxJQ8ozbm6Fx-9HVUGKStIbMi4ESp2pRUkFXgu_h-VpHlA39lPgosIMdVl2wNR5AxzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBjlzHOr4YfarBDe-FJpqnIIipVtktB_NWXClSYOw7RxefXz8_9ikbf9MeddmZjhif-Mka8p2lh9RQgCE5Mz5BN83PXmV2r98k4L6BwtCRCQzy9aRC2w7mQIQigkjQDRtNti4lH7sPgayY6IjIaPFkPdae_aEJSADuKUl3G4oV0g6Jm2TubeNzrSFdXADlPbQS77-rZ6_rhnkI6mwrPXslMWbHFDgihxEOuXGFLomtTBaldb9tPV62_i-TcqUxbrMgv1hYLaUpIB7UzO5v4PykjUH3NVo_GGzJHvZTyLqHJhH3zDUV7fdP-jcGkxlZMfqPD7jcM1nQVRe9F9eGv5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=DwIVK56xUvA2X-4uxqoVV1KCYYBx-JdzIydwK7P582vxd3bZWQtHx_KIcgrBxU0kR15jcR7HdLzh93SAd365kps-Wt77lkJ5-GDMi9kgxmUAE3FdA91cQnhIB97DvcvqXDwQX6altOoRzUIMNbmGs4eDtiO2OCCZ8KKF1SgL5zypkgFyDUG8X4XG55VcXEHDwP5Ufw4PUNymZtiUbk-6HmDn_h4MWaJyTIHCMG248QTPreyec3URakrSAm8DIJvT3i_um9cZ-XizGX0tIu2W8uYdi5AlxPNhyz8f9zv7aRu9tzQ8jr4or9uAUt5E5L-wXoXrXmv1g-V2Nllu7NfPQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=DwIVK56xUvA2X-4uxqoVV1KCYYBx-JdzIydwK7P582vxd3bZWQtHx_KIcgrBxU0kR15jcR7HdLzh93SAd365kps-Wt77lkJ5-GDMi9kgxmUAE3FdA91cQnhIB97DvcvqXDwQX6altOoRzUIMNbmGs4eDtiO2OCCZ8KKF1SgL5zypkgFyDUG8X4XG55VcXEHDwP5Ufw4PUNymZtiUbk-6HmDn_h4MWaJyTIHCMG248QTPreyec3URakrSAm8DIJvT3i_um9cZ-XizGX0tIu2W8uYdi5AlxPNhyz8f9zv7aRu9tzQ8jr4or9uAUt5E5L-wXoXrXmv1g-V2Nllu7NfPQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8RQeLtY_vpqr9ujvQ5ulzEv3W0BuF5BrnOkqq_fBq5_c7NNN5yLRslTeTUdELAC8Ot5UBFt4VydLQgClOxZHA9YuqJ0j4nlXOZnsQ-Fk1uEWIWDSzCaKak5lxQMBbKhuhVCCbMEgkTmS_nEJXHmmRVf23XX6SxCyGrKOgNk7dCzjhJQn1apl3v6KD4HYiyF5JJaYliLe7ObSl3D2EjqlF4K-CdwVe6odjFVIHkpNFgZcWtkD8pBrvpDhH9e0xwNrsOGpfKpiAWP3S0zZrgIqxAQMbYvQN6AzGOBB_w5Q80If8T-fbim8MqaWqveM6r0Q2dsY1olEbEfNpZ4TEkU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZoTUIHcu88M5g_eaZe4aCy21S6rbCI6Qc1o7uQJ53DPAl-yPZJoXWDV0atVevfT2vJsF8CgH2pvw3gMu9qaUtCumWIT656u1WX3wcG8gc_hv2UzAS8Zpb5mOfM0IyXOLRz_sEd6pL7-bVpVQUMM_06CwUod1Fek-8YmlFUIG_0JAYVQ1bXN87GCgcqfVesE6_z_QRBnQ3e6EC1xxbyheCnnimT9pvcayj0r5MWz9PITlAv716sXGlQZAGt5A2Flpba7gXc2Vy97RfhK_qyaX4Dw8MEb2sTRgZtwIMehaE0HpZaJAyoIGYQaQaHCzT6cQ4AAAwszZrolCL1wSUE7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0teB1j6lB0rpTXKKM7zzLY8ySpOuUSstu2qKp0wBXbv4EjuunSaOupwypSSMc3oMjmYm3z-l4kEoYiHJj-miN2J_BP84jZO10xDY4wygp1yEQFGBh5BpOds13jegSSXXPm0MrkXPXD2NEccCuJ9QfpixIZazdugvfV-05lRgT254lAsRATrZx3YkVAbqAoOaTwtFbuM0SbuIGBxeXJvKa7Nwc5MiR1EZeQzYgjloZBYy9x4UfJ-wUyXWylc_5bIDP4Da4gXmTUgVZlyPTX_ZR0dxUDai83lsCf5VOvJZtHFCADfNNIxL-npqKlHCWZEl7JF6OpJkAjZXO_3OsrlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rECQZv3f2kTOnCEup_5DeqFEOQjpoP9oLjyhv26i4mwQ1dCcDW_HUF05J-JgwpK67LW4jQZsUD3xQQ6Afv9yrGPQoCmAj0h4tII8MnTUbh_wuYDVgLGPClXwLAyH0aA_vnTuJP8aZc-IrnBPANoEIMiKNF_WJYpxntgoeJu4n1_0jp7Z8U4EJE82kFME5W_0Y-j6eLUAlnfMf9N3KtPwWhOtfuYCIh1tZIDzCdpY84PpTZbHhV3RYaekIQHGB97PDPKa_lkg4wp0W789Sgb4AUpVEMgtXmRgKL88P6opn4QF14dx9CHKvANcmQ2yqJSHyyuOi_16xeRgd5PxBiarsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxefTt5Hv9KkHs4M99gd7KrHAHhzgZoKTHpyWVkEWYUzegLguEOMk5xOsvgs0SfWGNmOuzukJL6HU7eWNf3iLx2CTDgvEUxFRHhh781D5XVEQ5BLbQErvLnwU4itbwwylop8i9AAlvyEXL8Qbt_o24oXm6SDsp2Ob7EzUvzi3S0LTkFr2NRo7fXDvg6-lfsmpLllG11ZoKxnMsSFop63ML_0O68GpzJFCx_3cLfjFtlpT2plgoxOFXgltOB0V_7wD-pjtodh8-XPEsasjQCYyhDnlDOVW5e9kUfAPgXX7--X4_XsdE7GU2Wsr31RHg4I3INqPu5cjTqxWU9S0eQ-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDSQUeWSFKOi2jyCyIrhkd83dX59EijKKt7zogDKb4TT5cdE87NIyAUyruoYSTa8oQ99_jzn6oE4umjIx13rZve1am_uAbSH0y56T-tgqGWCKt7IIlGc4viGbMGrkaaL8XSzGlBf_oxYhUJLy8wzTOP3Q18f_4aop0euvYdP2TF92jb4JmRDhmk8G3Nee5PZrrHn6hyO6ki0Vmw9cvKmPNwbVeVI7LYCkgbuq2-jIziUBrV83_8wvdWrtkzRSBamd0LXBEiBE2xermvmnAcDozv2VOZPJbpH5jP4zjFVOFojcaZhyaE2zYublKetaDEuB3AGTPlg91V31cc6-qLssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmKQem59cmatnspJACYAQcoFqkiHAGNKH3e6WkZswZDjobwEmsDBwg-2QvhD6I7NXe2mcwCG4BUN219Pppfl0UnjqlGvCdc2hjftGPIrHlSbPhUM_a8c2_VmM07lqzLpOC2jolPMBnLTcv7dCrI97f3ID0GsabWOExlEmPhHHpb0C3YyMlDGEmpJIqkWrgnkVd54bgTsFufHkNuyHo7NqY5ztB2p6tkuFrd2PE4IU-PhwNRq1Lmkv5WVZINXp5djuOK3R69357erB9Qz-jLrEDB_9tYIjMnV3MJU8xtz9iCL6u-7X_g0zjmQau7TNMfEhv8-g7nVmSkGBL57kXuVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRDATf2Mzzx1_AHUqHMXCt9vyp3NEDw6DADtp8W6feWxwOrFYmXRoCAkDLw5OrOJUz37fZbkQ2Lt2807jSEMmKCcAs3wja4q-z-jqG8aX7ILy_Ik4wYpOBAY32Abanwcxfw9SyFjPdRkm6b8YfDY-irEMCYPWirviYMSNu0IpK_4GOnlm65WVf4AY3Q0aWkQtsrwmE52ImGmiGsLxb7HAXf2EthjDkrp2KKdRoRf4dhGX9Xnvrltu0X1DlExBDhFWeWkPT88LyNBnSmoE6Jxnoixl5tkgQP2cQDZUG4WqJdguTZNqa78xL9klkx2qlV7n-pvOw_JP8AFBgfpOiinGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tY9JmNqHdKwq_1Wd2j_MLh_1EZWAy2AkJgSNLMLpPOI-L6r5sSjB81ezGo5tuJyAMhcTFuQIogs2WmV0S6uGdOPfW8fuieiAz8WOde3kUrNpM6tk_KgXQnwTHI_KeTVBaYTf7Td1WTGK6ZRL1N6bB7f4irV6tlLyOHVp5fycen8xfJWiOOEzXVusxJhQGtApqYSVxWQvmGJWiVsI31NTIixy3mJltXOi2YArkd9sxuuDp7GpHSEz3RGRcAmJD4qzJx8XbH1QVXxm-iF3ZiUc-gAU_3t-i1ijSrleR4QYtT5d0y8DQwhR8Atw5QeeRpxXki3cbI36BsReOeRKFuC9HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SESumywVR1Sjwj3eLrkyCbkm_jXqAI1cuQVFzcAr4UhPo7_3Nvxeuda0A-nN4a2dLo22U2Bc1b0c6BdHAinsBkLYi1I5gZTvnhm9coz4AQE0-etqI53jl_SqFqqb1GDteN6hEXHU182j5tK4XugvGVFzOctHrNA0hFg527k_EOZayf8dAkZjW4XooluP5FbvfM64OOLCrXV6rW_iZ5enm1TaC2YplbuDsuX9d7VEhYI7WSr0N4KNHyDWnxZHk7zXT65ExcGTNDU-f74lohYAARDDVvlCTqbCjm0WtECqsBJgYqc2f8NQRMvcvhqTX2HfWCtmpliLQmccWPQ1LIJHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNfjvRkLZp58c4furGlW9bj3fNr9oOtoi77jpcgrc3Nfkbt4ZiT8urgUBhJ7WK0dMceNVVKKYCTkGs6igZLMQxD_bFd57O7fCFHfObfJZAdYPw87985mJB5fpWs--VyUBuar_kTki1M-pI2WrZRLZzYDe4Mb--tgZULcS0hfU3vSfN6tyRjtdbzwfCZs2ldu3hCEMDVCZ9U3iKaEjZ7aJqjlvU4Fevmm0RoEAdn6HHAY5I_w3-H5AjWEyFm1kIJQQIINv190sBzU141jgMwJlvC2YtMJtdmnB5SRSNVHrQZrdqha4-biiqJaFnAAB2VMeUQTCLEF-esRN2r-zyIsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrlpbnCxjuZOvrclFVjSNXEMq3HRX8c22jHMdyuDD8NKQWL0VAiGFmpZB5E06ibWMy-Kjny2k-PZXO63NFCT13vT7lLmPyUq4pibvkQA90q8vyHd_gFx9eGDgoa7DL_hBorWXfR3yE-eI6PWX_6uCbhYufqpQF_YGf54abzQZTt2IQQC-SuclqTYb5C1PwPLQRlJYNN-JQpzDTfUSar2w3nuBED10vj97q9QkegwikNaVC0dOsZbWzsF6JQQWOa6Urumx-h02o3pTCdzN8uBQ1bpM03MKOWNT3OZQdhn_KgFS874k71KBJc26NyUqJ5TLGh5F2-GPryb2g7O7CMBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGshoVyZX7A7Yqh90XRtfuXUAI_ZwQtnzM7WBZ67wQNhnRh9_m6pbWp6CRiiESicgk8zgx2BEhm0msbrlMKDusebOsaVFyYJShlYMT1x45liY-XakdA5WkNMJRNO9VHuE7jxOsccq_pvBVGnd2djTIlv7qHsszEdfPkEps4znRkHya_ZhEAUswWMKkWdPr9oGtkljh7U3BYe5LrcVDlcMfQq4glZHlZzbHH8AtUUTYAw3o-Z6AGRNJTM24tiJ6mbochsdT9n7B3G3BhCLofj9ZhY7V45C1tNv1OJQ4fKuFjuiQG4v_n2z_uHxz2ZRHARM6x8rP_-xGVF2U3cSJFL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-znCv05i80bGlqBW2p5ty0okLCQUdinC1aOtD_z2VDL6rpAXD_K3bYBjjichG9JLkBcO79KhtzS4rb86XtLAZLL8DJNG2iA3GuejU-42SsTqn_aysWt3vXWQE2ulXWZoQe9Diny1Vw5REd5DzjCYjngPqqDlDqYtuy2WDXRSKCnfbxGOO_R1hNCUrdu5z-6UsZoHms6n9gTfTPMINE976br_KinP6iR__d-qA0PUv3ClK0zSHiHYGEi8zHhPwVQ3AbPADt2ohtmeBOOKVE2oKi5EFTuhyODjEKvT31YmfFN-WTYmZIkiZi8p2RTr2Xb--vhoBsVwKffmfT7hk6eQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MruyrdFi7_H-pxWDSLwy3WqHWhII7XFVLGoeLuvbRdDv7YHZ0vSmj5rXoBc8oZ0xZDFYJwTbFMdLDWi72WieMF8KXZSeBk2GHS3hjvd5PhQ9cGCecWAeS2HDrWmyRhqAbYMyeg9J8s9sXm8agxu7oPgIr0kwK1MSRbRU36-AxUZESoRo6vmfzp8_nJVw399vcemB8BNSXVQ--i8wtpTx3aFme-JUnacrNCzdB2eCuQbZ92fOkkBYpV0T8NIdFA4YhjBwk1uJJcGnpbVfXaBA4Fgil98fomEb5wqEjxoEduKjHMpfeSnn0EARR-2VyYlw9G62-WSfh90JuocNDdkN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGRRmunHoihxiKjXPx04abqQfO5i-lKjLJBEMVKkq3S8EQ_K9S1MFGc4KC41kj-w6N-ErZjYx5-EdkN-uLrdlafksM6TokmTVkQq2JqpiY7qXKLSWRfSDziqWEVsVJQBFkXmanFfl-slI1-_l9tsay0rvPro1cZvYfnK-zdKYeNn9fsRULsxIj6gRbUmU9_KL0pHaaX3yLKrACYU5cC6OFN0cFzyH8vVJut-A1bPsZcn_5tO85LtjBF5koerwLfkoSqM11Wqk_Hqktzt0b-q8qr0tQJE83E1Zgix3lpgPV1Q3M3Be-4pDw0hdD9fte0oIYIiIIjNMyF-8wrG5BU88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AL_NX7-20vWVMeMVIzDNmRHL7xOn59g83cFUTkvTU79qTSg6hAfanUV_P-l6XGtLoaJhgwcYRMh8x497-VjipdzUILHN40iAlMVfhFihFthHJ1wnXTyBmHaTPeCOlhfg7u_dK4xb7AK0E8EfH7KntanyevSe79QsY_mTrxIhAoPS0N0JB7-MU6fvwVnBY3KRA7tdBAY_kqXeBx03aE7VKNuYA2Here4-qrK7Di7MDrkyU2A_uMqw6XBfl4Q-dTK5POxjUBtJ_cpD9VEX4BmYUAVOtAiyQdwhdLZGqeOOY6IfHhnwqsLe1F-87hjOCnFt-_7q1Yx-Gvt37at8m3JRJW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AL_NX7-20vWVMeMVIzDNmRHL7xOn59g83cFUTkvTU79qTSg6hAfanUV_P-l6XGtLoaJhgwcYRMh8x497-VjipdzUILHN40iAlMVfhFihFthHJ1wnXTyBmHaTPeCOlhfg7u_dK4xb7AK0E8EfH7KntanyevSe79QsY_mTrxIhAoPS0N0JB7-MU6fvwVnBY3KRA7tdBAY_kqXeBx03aE7VKNuYA2Here4-qrK7Di7MDrkyU2A_uMqw6XBfl4Q-dTK5POxjUBtJ_cpD9VEX4BmYUAVOtAiyQdwhdLZGqeOOY6IfHhnwqsLe1F-87hjOCnFt-_7q1Yx-Gvt37at8m3JRJW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=dEWdBfXj-fMyIXrACK9QmVq5IZxhuM2mqPRS2KwLlMga6Q5cd-5giT0-ue7JSidY94GtEXLmiFIgY-kg_rC7T_FU05thbm9UES_er16c_Re1yH8nDmmsNOJI3E-JaiVIkE-pjXd1Rf9RcKsLlYwWAeYTz5Y0RcXuHKzkCLa5E9PZTt5c9iqjgce5Gt_xXwDJIgosBpODNjUgDcqekX-fXLPiuvpbcIB4I31WXhOR1bWubYwCMidN1JuPOTgruaElQfpDBDFamGZtxr_NJ5dLYdvWAutpJ14hHAK044qrClGiaOeSWdRGabmjRs21N7wkZY7JRavLf5OwndYpbQxlqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=dEWdBfXj-fMyIXrACK9QmVq5IZxhuM2mqPRS2KwLlMga6Q5cd-5giT0-ue7JSidY94GtEXLmiFIgY-kg_rC7T_FU05thbm9UES_er16c_Re1yH8nDmmsNOJI3E-JaiVIkE-pjXd1Rf9RcKsLlYwWAeYTz5Y0RcXuHKzkCLa5E9PZTt5c9iqjgce5Gt_xXwDJIgosBpODNjUgDcqekX-fXLPiuvpbcIB4I31WXhOR1bWubYwCMidN1JuPOTgruaElQfpDBDFamGZtxr_NJ5dLYdvWAutpJ14hHAK044qrClGiaOeSWdRGabmjRs21N7wkZY7JRavLf5OwndYpbQxlqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8lq_xdyg32PgHMcRoC6jtguTuC8wxTCjc-VNOphlknHw3H1UR_92cgdWvO_4D8_ZPVawk-HUlRjetgynH9ivXty-GtlP73z25qXzC1k6_UxzP5Sn_BKB6Y4jnAbp6W6_55BHTFEgI5vpO6rZUmMIDg61OQNhtC255xUJggdzy-zqDQ-IY0Ljd7BDUlva0QooLVQvkD-6B24kc7ANa8MRBOrm9sXatw7u0YvBIlTRq70ykaGaGhZDfKAOZ9oplKUScq1CsjM2rgUQzZCbdWq3aKFB-JbJgZx5Y_UfF2yz6063EDSablb-vQ9lk0hJgVxFlrvHIvnF2LJsIkRUUaXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLkoGtq9lie2iVOZ_de9sJcgb-GagxmLEGAiMfhM_4jgTqGx81UIJBVB6_sVSn_I-0vDBU9rB-_gWhEumamuvoE57nCM35aDH4A36mN5kfEOVfcw20cQGB0Kcy7lpuJbQV1ORaZ00AKMLtK_iYxsm5uZvKzWlulBrNB1LfMHWtr6niLPwBL9Qi036_jSXpuT1DQgsuBnyyJ-PSoiTTxawkNTNXxAGOhHRRp3LejHHJNBMgxymUnKrQE-CXPx8Thm7qlXxRAdQdZypQEEV9LucKkiLfG-eBthUNHPWiR2PJp9FpjEqN09IYFc1md76f12x_QNkpv3scWHEtURw8oS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSM2Sv2E2j4TGotRDWom4D_QcpSAAYvDv0Li6vtvmLOZF-2KfV1S0IbmaFk-SDyTihUmkvQWptFT3AZQw3p-a4YzAGCzot5fpnUk4l82aI7Px4Tv0vQH7N85FPZOCG-WTbERdGkFS-ZLfM09vDGy5blkFgPbI__iTsugBu6_-iDe5Ww8Gtd-QxNXFV5yX3kCZHXEFHhdl_dcdbHMVdY4iJbtbjT--CMlicNICPeuuxxBZ4rN2VG5k_LuNwXs5jSJOdRppJmN1VAAmhA5XeCnLbyonAPjCegDL3376QoYq704W2taW-leDSSPZS5OU3DP9yf08iZVyuCGPD2j0P8dcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZfpQKzZs8DrrBaGevN0w4V36aCACePTZTDfRhFYtfpdaftZbAukuQo6BzNt9jSBHPayLtMOH2BA8RjAmTxaaIFttFwq7NbDRdWR6GmBV3L1xWZi5qHKIx3U3bfiG763RRI63I5KvYvDLTOkkjtaSpkvyc9hAzeVOyQPJmJ7s22t-Rt0HI8sbCzFghqVWkQhAnMqeRDv5On9MBCsug9_0eIrJ586XKHJ_KdMVu9LFPSGkIp_wRgI6hfFFC44PFl7qTs0cW0DdUBu1CObdlAXlvWQ694uqMH9OKTjYtktBmOUVZoR5b-osxC1OxweyX6CCwJ_OxAy2_lVVezcYH3ZMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehc4iWvn-a3Koy37D1cRVpTV8H1oiqaqQyYVj1WXjbfouA5mfIrokDS3gkOaZ4aoJNJoX_iMDb-6c7Ilw00qSFgZjkxFB5vlFqjFW0YWrG7YVngl0BMWClqGBewp2mFXVNUOlYj6NDtgXfiMZ7lolWwQ_18Qa-ok0-qilT6l9Cpf7Vyv-RSjBgMdwGsNhn2pFthzWPrQpT6aAcrnI0N8H3RP_5GWOSoeFZ0rE4fuER-Hvrciphda2jL4mzYpHAEstQEsaNGxo11L1H09I7E6ZWCg7Lv6YxJwkQGM2bLeEQGx3NxiXlFA7RZziI5t-NlqCtBK7ORM5QQGQyHytv6dSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT0mk1IWETSyOM9BvrxyKk6z8OSYhN5oNARBc09mucpnNrB0rTwYjDbZ2FDJUU413GORg52pAI7Xhjye8qYOvnb-pxxueeoHXXzhtplrCb7-vMphQgJMH072mjizrc9Abbq4nGbstV16vxAby1vhTOkdwxsoEj4laNxx_lVFouWOx2fPbg4pPR2jkgsUixTT2-y0UwlYWmqRq_jhVlWm0cvOkFn4DRd9Kp91QQuMGFGbWEPFcgXVv_I-j3OV71J69mijt6Y5PZJFRvuYza0G8gOvy4OpszR9hrSmcEivCtN51ItdTeMdcHBwCrfAAaIWq2Oxk7dI60u-Vxgv2JfcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZBzUNnRJgaERRlAcQqNh8-8tnUgp5Wji1mGpSAIQ2_kVM-1wWqZR6blUNb7L5oPT_YmrOQIbqXgUBYkPXSy7cf3MF5EbnFQGoJY9cZ8w3acK5sePTh-4seZrP3cTVwud6J5kHOPPY01acTfhBG52iL_fmu3_CrNL-eMbclq2phBXdclFoV7I51K7Uz1VvOhq1brmhfy804t4N92daOE7GJm8fMNpjSRSivFM3OuzzxVdSiy_dg0Eq1FUstoAqL7U_0YsYeOkTHEIVwemw86AI_SizUvTlC66C1qhRGtfoXHNHAUPIN6VcBb84gFHPFT38uw4axM9Bp8B-APf5NQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4PvoVtcYhXHY33HlkuUSPkfzRSyE8oLxXx_SeNanX3YtTOYsAl8frmON8R17P09McYuM72viCO4pyb1jYREdS1AruXki9HuDM08qGghXnkIowEwmN8qAexnsKFaMn0TUUhiCp8fkPcpUIXzI05ofoI8oF9tkTajhj3Rc3PdEViFwhv6sSsO69KuAnkVgjRXjjpvFvHh6Ls5CJ5fDgPpFbhGZ-iUHzwE8q6WBxY5eGPb9pq04n83jXUUSyqJjy2a_NdSytQgUzEsBxVyTPk2POzZkYSrTq6UDH03O8HmO0ehX71-duVu3p4vcEAF9q5rH1DaeDWncNsqAl6RpsY6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk9_dtjJXCyAdgKAni8dDZRKvibW1m3wJh8y1hho74v6lvt7G2E69_QAkM3Rv6nIgXstJ6ziWSWOASDDDNY5kbca7V6DJSCX0aYt7FGOR-Cpk3z2KJ2yhIzz6BboaPPtnYlmco3KV-g6dj4jB6okVZyyqncXdHfGcInuTWcHzvgCIj01l2fk7oJEvyacVJATkZ-8cs67pFhH1Prx_u-XmMJfZb1a5-JTRoU8jtqm_vD5QHfhfUF_mt1o4yTrDYo-QKkmmsxXGGvyUhkhWECNDmWfCravquHuSScs21fvept4Y-ed29c2nLg9LA-k3yy1l9UK3SYrzz4lngPYOTwSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEJyIcmGpwKifeKJetnVQBx34M8jgwKnPU7hyVw-tZfAK4k0cFrekclPINy-pspCWcL0NYBvZ4SNF4cDzx7koH4u-aSozVY9kaKWCbvrfXxNxh5AhwJoO0B4OSP1tuFpGUupBXrVARNbzk924F_96ItSeC4zMCQ43pyiIMAWLvxqvUgppfDBpt5iQCc0vhVLHORLGNbs21yghtkuoZf5nfVkzraD4sPKzZSfn_03qmM1xwUwDqu3eoRzd2mhok6wL5Gvc363THc8NO4Zcni38q4XbQS_Vzo2rMHuzzwRQq3DvDC47hsjtpey8pCRLtCAZYu5-y1t6whxNYUUY7zF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=EhLkRO0OAstkTH5RdcbwKMyFPSDWMNRttLqhjvivIgFijtll5n7E6Y_vSBKNMCT4yYcz5xR0UwoBFkFUR0vs_5nOyFwllX7yQhXMLWBF7Ar4sgGPUstAOWvW_QKvGAdLMZ1ATNXexnxSTO8_hDKGqouDKI9FkaJ8b5-oQqryWNNTk9Yif3OGt_Wg-prdPZrB2guzcK4EhFttbzI-73PyrM9h6sUcI65jw9CiNM-QWevR7-R5FIYOrLWftlv4zR0xj7YBbu087Ej3OIG92DMQkv-Omo1kkUuX9CjHQfxjOoqMyT7peB0F9_dGAXjlp8u1iDIgExXN_3n0f1KD2OZZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=EhLkRO0OAstkTH5RdcbwKMyFPSDWMNRttLqhjvivIgFijtll5n7E6Y_vSBKNMCT4yYcz5xR0UwoBFkFUR0vs_5nOyFwllX7yQhXMLWBF7Ar4sgGPUstAOWvW_QKvGAdLMZ1ATNXexnxSTO8_hDKGqouDKI9FkaJ8b5-oQqryWNNTk9Yif3OGt_Wg-prdPZrB2guzcK4EhFttbzI-73PyrM9h6sUcI65jw9CiNM-QWevR7-R5FIYOrLWftlv4zR0xj7YBbu087Ej3OIG92DMQkv-Omo1kkUuX9CjHQfxjOoqMyT7peB0F9_dGAXjlp8u1iDIgExXN_3n0f1KD2OZZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmILDo5LY7oCGgiG5HY5ee6lDdIZQMWtCHMmO6-63wYIFY_JocGJB1fuDUG6Np_WLVGxUr2P-bTMMzrU4rgp-2xXR1MRoEie8534lp5mYtRp5Zl1edgtg_-i-_ed-FZSk_9EwZl-t8qo4Cq_DhM9a6RqstOd1jW4WKf6EaMnC7IYED6KoQsI9lXBh5vDllvmjZ2i-M8jRgvc0_0Jaq7TWHl7EqBMpIrgzP0OwBEEADvIhtc0ELEGC4s-HLqu-QGQ9wV5-7OjdCXoH7OFCrpSDeZKucHfVAuOXHNCeQ6pQp3Kz3lMLEOJ_0-kOZ-Q6ZnNWVKYKYlAvPbLcqDYcDGpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3l2ulTIvvwznYXgnra7hgOt41gwZQsdiQacfELfytsoinNI6yiOHM6ihUfj5i0VDAyb-Qfv29YTmCJ6XnjdmDDL0u-cH-jRrfNpDcJYpqMM1uHQXW3AcxOWXwVLK_C_Zc768rvaaHCPcW3U_eYzrzDq8YS9n8GqrneRasvWQnaVTU_M0b3EnA1bSDDc2JrkRvzFL-_TntKnTKAIJMl6McS7Iq_-ZMOhbRx9qh218r595uU-35SUzFdvKiDsdXtWtX0Mr0833e2m9Am3PscTCsuvX4uirXFoS0V_mPPm2UYnEq3mnRKIG-8Gs6Da-hs2s0jm9YFbg46syJNxNBq1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfvGgOKrxpfizpja290N45Jo81s1YLkJytes5mO2DIVoKoYGxwd2jRsLVfuwWkjZnKtjbld9ZHIBLoBoJRNeW1ugMiVqsOkIspW7C-UemjpPu8LAyt4_YkGagRa11THskg5Z4LIyPhMSdsckmYnp4xEmD8-y6z-care-hKmXM1wh7WeUpqo5WsuKd-2Z756cRqpQ4zqE6jn8OJ-9mbU1H-nP3MqfEHz4oswTqJqMixgnYtzMg88wIXzSoECLprRFh8IMauBaMhDKyaumU3ag3MYkAWJQzIJ5NUh4SY4Tin-fPbCv7XDY-jXTm_KVHweeI2ASD-ZeCxfg9l0N1bZVhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipG8mkaWyWyJpJhKzK1UDkDVI5AH-szU5IMDVNVZCUyV5BVz7GQnXZ1kx9-xn-vGuT3-JiJDeK0m5yjI4XB5UogCujCWM5aE1qT9RelDtKswimRXotM2ZxY9ZKtFt6NGDGrjbVehHAUKtzndWQ1_QjPayhv9FVlyM5Ht2SJ03p3tIob9kggLKzUxujICRKVymFAOckJU1vNJ65u4AForMZiSEygdg_XNfLoXx58U9NysH8QPlFuYDVJKLFypoLH6JNJHtlyCvqEa-NcLJqvHNNvZaFkqyVNOeLEgii5Jnopu6ThQCTkadKkaT6CCBHa7NbGpDW7x0T8P5pqNbiu8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt54FseSxgEk8wbEn6tVN_q7_BWF_qIkd_TS56DrkwZBUB3qumQYpexx38GfhkcVE3OrL40a2KNh3seD_MeMNd-JAPu29AyEh87BpcDPcpJNyOBshEwBPBXmfKjU6vnObEIDrCoxibmb2KUbdoDhU3nGEF_RwBedTQrKALbyDaTIn3KPY3M0E9g24tBL272TnmvJhLbsXvp3xYaxCABd3E4EZv8uT9DKQc33w0bM1mNK06_XcgpQJJ2OUe0VhguKfz_2lHCBZUB7ywiF9aXgb5in_26lOyzSYe2-AQDwfoGdooZH3VwlQFfVws3zvgpi8vph6frugq5ed-y4xzyXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_IADAwzv-a03iqssIjdTgTt9oDoUMpEWF_Qgym3POFxHLKHQoN7P8nywWjZfeaR_8RQCDF0Sud8zafXAiAgMgwqOYrKwgmBsnZMINh9JDn3fpH78OgL3rAS7xLXwZmV2fvRUk_r8kxaTSX_RzIbdknWIDPxRfg2izyGfcjN-owpnPacRWKKzMvMzqZhau6_lX1FY3WPvsBa2tukigZhJJTqKRBOFyeQRvZZzb1Xz1ye5CMPFxh-gUJ8lIlpWHhcBTj-qpRQt3k7Si9OGD6t5S5hYQJzFzAL7MdGaSfXvzcsUH-ZiLAhYn8SHziQ_N4XgTEXnz8I0aPwaDrC6FSEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI1mA4u_EoiUn0ttQib9r3E-JqoYQEVExG8yqe05KdJZl2VbDjEJGQW7ewknCFGngDHoY-BuTuIoOvgaOdb-dn-BMfmM5_fj0WnBN5aKe7yW7BZEWfcA82U5JH2McC13P-YareIP-MGYFBaQde6-UPkMyzE9Rn1KNLY0yR3lSYbvlGHwHCUGjPm7ehrx9MzCl5cGjX8V2wc8X5484AjY-ljypXKAT_1KWJ2ejVbE_icPgKIJy0JFqUiGOWMYGFPQyFrlQo0zruvhF1Mre_iMUuqnmD8H6nqRA2sMKOdh3T_Km7qIKF_vXjFVxGsw7vANtv2doCayi8XaK4gPdh72Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxwcWrgNykilfc0UO_QwO3zxV5KZNg_8wRqfhmkDEGHAo-9ysaVC40NsbW2cL4VbKxDtNNVgzM0VJgt3rqkBvmbxOa1dLwskdPUFkA8f7ytBAdUShcVkG3HYT3NZyRqq2J0cYzTy3l6atu-4eQuwmwn6SVIkW7KiH4ddOvcGT93B3PDK_OYgSkj8a03rpN7s3l2X7NJ4BlP25b_Q77jzFRwMyzhbH-8VKdFxcLX8Qhj2SV4P5L6MBoxeoV9ljkyKJ0YaUWpWPIM6Ym9zRnV9AT7C_krfwsnh2uLDQqPz2PIIYjeAbbz756JmOEgMNdYjyN3Qoh570J3bqqwZuQlTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7pKZFP-hENo7DHNXDSs9Seu6oIPsLJb77KJ7SM5jhkVTybSywshRyaQ4pjPT0-uZM-76Qf2BdVrizxsuca6sVl85vvtVzZLmaALyBlkd04xdY3l9jh9LnZgP-2rpQW04_SOZ2lhjUyYFGmOuAbiyQl0uXgtfsfTseSq86XTFToCqQ9G92UridPS-XAK0uOzEG8wtAr5QNI15zmDd2rksbwyqg9Qd5or3HxS6hOa6ZplgWsL4W1vPh99YmFrmDIwk7WGVYBXbdKmMWc2tlWFTRMtdCZiRLULTupUBIcCBltM6yCQnYg1_sI_ifIW-cQFLy5mp9HcaZeqMA65UVo8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6VcUZxQzYhiu-XraS7Un8SQLRHUEigyHt3eoXoyJu1ihcDz9zvb9dybfa3kF-RN9lPS16LM2V6nCe2KrGSEPEc_E23c1AYG_nLiFXZScihWHCgkExSXFzCd6BKnhlBa0rXo3a5SGN7dIAtUuigHj59hF3LgttC0IZmRUdpowNKTvvHOmknUiRQbGmpM1YrpQkvfqW-V1nhiBjbwW9rdrw4IVrYE4yDAfhnnvH5SMAHLuQmjVT0zvhXOJ0_felg1WI17hMfCklsL-aqh8lrQTr56CH6rxIsqpmkXqFYFWwVQj8WbePNX0JxDVIb1byMNGYtWOe7zOUXjDRbzhXliNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEnx3Oeu2vrK2LvLZmYDlzKdsL2uy3T8_L6BTcDbh7R66UNDnk_RAVhGBVLROoZuvMT5_P268ESNNwpLtgGiE5X6do42sB76fKBKMEq_zkWke5qTeyD70dxhWLGWGx13KQ5c11d2-ahQA5bX9tprxWwhBnsBbPZ3c4UU3bYLASNhRD_3BU-J3qDyHNF7PgnMsoa5YR9Yw3m9BD3sgFExkU8AXRAVWkkyAHcoxdbAlPGNzygND6CEAy7F9N0qK-56zBrinH0X5l4JaxkR3EhtBD8kBB2SaswQHQX5N5Rbma7O5i2VGB7pw-l_QMxXwHXUDMBe9l7axn7s8usa2dwxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlpvOLfJZZINtxNMVSBd-mr8BCehXak_3V4I86oTQnDzJ1Vr33HIjf1Wg_GS_ZbSuIDk72HLNDb1KwWWrZMYN3SLVZkVaX6V_zoiOTbSr7HQ3BlJ_-Hy78LUT-pBY77fGpcldkj50MlyIG56JZLs9JExC52VQRUtTQgYnx_yOfLPGCCp9xXg5HrGuoY_vpcUJTfPQpp2oQmEHlnnuam5uTzkOz8cQMjw0Hpo0LNOjYhzh44r3W3JN84UNd-zXNzE71IHEzIFFheOJbvdQbsf7x0AqCfIJ1hdGJGJh8N9bFeT7kcacF_ZtaWGqppctfDrp5HTny4L1812BIRGB7ytwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJfSyiUso4EL86YWDmYtkZhQGUnDpcOgEl1em831CoT8CRwRi9aZeciSRfeC81gZja3EmjLric4SVmrxYm35NLWw1aNee9kfou9apl30_V0xmWDkwwhspFGZzqvdfFAkY_5kRUXZAZiT0Xzkv3Rf7ENPJDnwRJSeL4U_41IAn2VUwEPcTD0DWGEE3P3FtIltk-bHSC4yeI-3ISkDVCXQaLLWoo4WGAzYEe0ZgMZoLoarBIgNSY7xabXIqrpKsFRuTst8TT5bDh56Y2PzBJmZSX7adZZHgPGprMMx9dp2Aih8BpnDCijNuKr_qbVGL466nphTbOPXObzaQ8eb93lZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQJXorZIJqdU5OJg0kF3pkesJfC5WFjQKBzqexbfRsx6Auzl86dhm1dRAVVyTASvF9H8rsoNbC7PT8s1Ce3Z6J6R9ClGPXClJV9gGNQIy0-sbbyO36U067M85_azYjSGN16K_akQ6ph_3IoU_GbxLjcHXBm4idz8baYqhbL4J_hOyS0KWj192tbhG860etRO3HYN6696ACw97PYgooiE12IuNiTEww8ikmgw4y0_r4JJf_B8tCQVVVEvfnfo7_J6RU8h5UoFAyPBRwkS6Ju8Uidsyi1vMV1CWeUvZc4RQp5JYfPYzilt2tOIuq6qOBlOtFxMfztcqtVTRtJtC4TCoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIe-ohX_GrDNftODzA-U-4ijLrK_pZF1zpbFtRdrodFlj3-3CUecU1SB8r8yUMcr3sntPJgbNvuDQchm-YBbOFWdCIS3KW76vIVtsn1Jd-6RiXKprIOW7aEV5MuHMTIX4Fjgnag328C2ZiRzRvqG0T8vwxDFaUDmzjzOv3KUxOAdMLfWVgyHySxukApNCK91KCf4Ts5C2c8BBzd7Jo4qIuhxL5qF9ktSpcmYCPaCjQhBGTUNDes5gEKH9wlfXQY9IqHQt-ZOGgPqVbte6BeJDPAg727IsEflgp_kP7jv9AWF3vUfQEWhhjqe5kJnBFRtsMV976K2n9Wbe9WyECWpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw2ONI4HXt9stj0HW1RECAHHKsj-nVpw8TaOsJGIoawCCq9DicK6RfS_hfW_ljCn3QbfWrWWNFlH98aByoYXC6eRDA26KqMGxONS32ob0Xl5NWoFE4uB5rqNrf7-dhVC1j1Ro_y_G5tfcvYek4d0xxVE-PNb1RQo3e2LjcRFe8dAycG7iqhgsBRAKYdJzOSNdjpmA761plNCubcGj8PyEXoj1Xwmkl2dnWBEvm5t-wgNay6njEr-tYqKoYiGTrDlAyxBvpfDWJS0l02-25dVR-_wgYfPd7ydZmsf0L5VQ4dUN38w5GeeuW-_X3gQ9zRB_Dwmes3fzsp5kcl_bhkJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtPCucEyqxULc3gOn-xV9TfJFrNs4l12rCckuj96QPXLIR93xVUGGmc9crKG-0v-lVCYHa3Njy6oa3cvliVx9S4vk_fnUBNTPuz93kyDWdxTNzjN1DNQdhX2byWx43xQwMLCHR_EnhtJFiR9RrotbcC08sfR2IO5SGpbzJYFJhQ4MkZaswE1vXLDgA8DhiRPgXAQfiRL9SZQPDRNdxiINQdBFLYDb7QxTyu5w4Rw3Z2ML5VgRn_jKd4wXxlYG9q3wHduwUL2NI4w36ozbxZuOxuEB5wYq-WaNJ3uGNGt2SyigWcGLEbrCQnq7gqKlltee57Svk6309kxZCq9j84N8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
