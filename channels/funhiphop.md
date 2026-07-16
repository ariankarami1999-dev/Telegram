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
<img src="https://cdn4.telesco.pe/file/lNsezOxA2BHXfY6tRgOFhECqXX5ssgKeCQ-EQwdmZv1AtCTmpoEASS4_0m4s7dY8Lo-txw1bSOIgvI9oTcj0j5lFWtD9fjbGmiBzwUBsxCFzqO5mCruOQr9LKjqjU4MK7J_bvEMy49XgLGxsYhlpPY5yl_0FiEN-MR0aABDFVWR2BPr3H4qicfQrCmDiepWsPiyBtPvmNBkmvmGY_7iLZbqhCalV_tXdogu7hF5ls57LG3NxaTPy1T6hJt1soh72eys9kSU-_MfCARxdiNgQFkpZSY4e3gfUz9bDSLBUy54n-dM-upj3ea1--iESkonEEi5ax-8YsHvZGSbuHFbwjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 194K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/80486" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شاهی علی الحساب یه‌مدت شماره ناشناس جواب نده
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE_ZRL1NjGhoBqaoL51E1BMT5Gmnq7g67cf_YApRwcMsjNmJNRgsV38GcpX--565Qxt_euNradT7Ui3zWP4SpbDFcQ7y6Nguwln9IWo-WEDAEmoLz8n26hJ1HI25GsqIUshZ851zPRlYp6EqnMOhHBWe8pAkALS6dIAQaykBDbOZ-3w7U-hQV5Qf1XRhyZWkqI948wiuAd2H45ogEL76xHaTgfH_ZfgW9dGdOdfxjGKVE5f3_ABssZOtkI8LdlHbkSgTmpjB58YEbVqO4TGLwlY4BWRkdzckhtrQQyesABQjG-UvY6k17EAnHw2q_Nk6oKw6wBhvnHyqgZDntizANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8jHPsqOdkxAcRzXuKft9ulNcPGCj2uiyAFNlXu0J1iFZE6BbA4B8rnFlvC-L2eTmzbWhZStPzuEvXEKvPb2LrR8IEfIkBFalH2EEYyWlp0Yq825hzqWkKLrtNS2N67lEwxED_bHbxpCguJLYfIwd3-cT0WkXjD-9X0DS3d8m5I8wQ3CzzIvF8i6fk-V5EyQXwGNVhXsj1GrWTouHTTUTAqEgMC4lelJexyb2shrFC3jGQxvk_r0mXY7utJKuZXHwnT7C4jZe66kvey2bsFOuU2LPLMvztm6_U2snpVd4RLSZY1eNhOZZiCYbxgp6Os5wsZ02ttrcjx-oIToT6TN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z008XXkEcBgl1m_AT_vHlp1W6_0OiuWjFKL4e0F2hQElDMtCL4_nURcTp05eZjx5zifrq0bOI4hVNYloPDrqVi2ol-EOkIFk229uvz_t0CLcpd-nlGRNd6TCDLOCHlb_gRcWNuEK821P5TykxOstOQpUbbQaMJkiAVzNxhyGG3uMxYph2y4gtHDqTBcsp5fMyKNvsTpFot7y45IF6TbxGHtp7uWIEQ_oZ42nyhlfRJAJZXKV5Lm-EY_piXG4pVdUvysBTDv7QTq_Difg5-Ta1L9quD18CaUcihBsFz9agQw8uhA9pCoLd5r7cFT7LUDJN3PKUivgoj3as7DLbn2GeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcIqo9bh6PUJQjzT9iTs0YfpAgMlUoNf89qIiuMW59V_4Ra6wWpC4m_ABhyUdXwDPVb6T6ytS-AAfPtIZnBFcEWFvCfakjoEduLtAB9RBt3bxvQVPCYIOFHNejuJcCuB81WT790BF-kCgnl_KGj6toukf6Q2dmZi2jLRrHZJwwhsMAlESjKCK8-mjPRdEtQ_u77uZh0hj9bXS6NlzwO0s2NLXFDpYos60g0h7D6O1D76gkSLrEVqgHlbrw6VAbTNC1GscJXQbC1RBn9MVmmpyjMn71tzkTRPt65U6l-vuTwd7PB-caxbS_WF3mjWLLc-C1jj4DTs7x23UTv2o_I_VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یا عباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80476" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqwlwjvR9qaCW7DGajd7friNbRV-f-3EQWLxYO8zeM0R_ouXASIIRN3QUwBnsAHnInhe68QTr5N7apHhErx5X_6vceYBENGqQuqFj3JMJGmklWtCPzba1vivOuWsZlsq0VwYXDAuFxEj20N978Iych0DvgcoUA_p-_hXvL84UDwqXlfMie7sHZ0qNr-YCxCnMhujXKMZcDn3ocyQfE_c8Kov0E1i_Mha4Y70VsvliQZAg7XgAYYsnwLbEOS2otrt_h3uIL5rH5uvgTpbG-GNTXfGXLyhO3QSqxL56dywXCeuubEmYsZbhPSLZxKGQrpXn0TT2pM1wkyovwEZqcX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزا جان ببخشید
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80474" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رونالدو فنای عزیز صحبت کوتاهی دارم،
جدای از اینکه جام رو یا یامال میبره بالای سرش یا مسی
باید خدمتتون عرض کنم که مسی اقای گل و پاس گل جام جهانی میشه و توپ طلای بعدی رو بهش میدن.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80473" target="_blank">📅 00:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ساکت شید شبهه علی دایی نواخته
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80472" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromvahid</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBGSePv1gJHNPmyb6-QUcCNXWJ0YR9tbh0d1FbYeor1oPXFLqPQkPSMmkEQF7zV0gXch_clOkytUBdf3uxGj7tUqtFw3iTSHDR7lztZ6QnHhZtYTFOh3XLKrRQu56j0CWTP8n_51_SGnzKu9-kzu4Sv36CHxBBxLRgXmk8HEFIMQfP5lO42_GHPRP2myc-iXxd_iXupiSRHmzNAMhC1h6_8AXLaii95iMVHNJjF7LEXhqLuFuBibiRdb4t42WgSMYmwyRNRQb2sjxL1cL-a1HP7qbEcm_7tt27fJsuWtgzY2yvtMYspJ0eB8eUYlI1AcrvBWY9JW1GIhUoUF7ccGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم ی سری جذاب و خوش چهره ، جلوی این گوژپشت اوتیستیک کم اوردن
😔</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80471" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تا ۲۰۱۸ رونالدو رقیب اصلی مسی بود
از ۲۰۱۸ تا ۲۰۲۵ امباپه
از ۲۰۲۶ به اینور هم یامال
تو دیگه کی هستی پروردگار فوتبال
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80470" target="_blank">📅 00:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان بخدا کلیدی ترین بازیکن اسپانیا رودریه، چرا انقدر عکس یامالی که تعداد خطاهایی که برای اسپانیا تو جام جهانی گرفته از گل و پاس گلاش بیشتره رو میزارید رو پوسترا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80459" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80458">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صداسیما: شدت انفجار ها در اهواز بالاست، در خانه ها بمانید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80458" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سجاد شاهی ویناک گفت پولو ازت بگیریم بدیم بهش واقعیت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80457" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انگلیس عزیز تو امشب به صورت استثنا فوتبالو از دست آرژانتین نجات بده ما فینال از اسپانیا درخواست میکنیم مجددا فوتبالو از دست شما نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80456" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5ZSFXjokCFeN5Y6syhR0_qD5TpPSh6uMBr8mSGSSpBuCYdOE3vROka7WjerTzYJSHOxeUU4mxChAzvvRB3a_wPCsx4PuVxGMnM3Uv45u-4LXuAIbXgqlzOIN6Y_QC0zvGoWgPdTDz_GitCcGaPLsWdZ4dlnN9WpG724szeXtXuoFOpXwFrnnuO4g4wpEIR-pbOErKnuepG_mWHdFaJ3P8DthiS-NPKVmNYeaTYw0U0NqIRTNQQFpsM55h0mfY57fiPo4em1GVppHjQ2hSz7JP1EDUBmK9DTBzHODJEk5e3zNfO3vECdUk04uDPZ7b5Ph76OhiceVOS8il0PFzkJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام سلطان رو بگیر پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80455" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حالا از دکل کی میخوای بالا بری رئالی
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80454" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کوکوریا دکل بعدیه فک کنم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80453" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فینال بین بارساییاس محض اطلاع</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80452" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تموم</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80450" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این مصدوم شدن بازیکنای تیمای بزرگ مشکوکه
رونالدو فنا پیگیری کنین بیکار نشینید
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80447" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهی ویناک پولو نگرفت بزن برا من</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80446" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توپ طلا نهمو بیارید بابا</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80445" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80444" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وای وای</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80443" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/80442" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دومییییییی</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/80441" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اکثر تیمای بزرگ مصدوم دادن حذف شدن</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80440" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
تکل موفق از جود بلینگام</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80439" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxOlrZ0RGZSEOqrQTwU4ajzDLklM9mykU8qSJrC5Erkt_QB8ZeNCPpcTwDxqBKtYNZtJQpkDYw681Ky0HDIpYhLmA9F2Q5PivSe-wkEdsrP3B9pWYGxpFx7u-KSWUuHMidco9oUb1Sm8GOrhqeWq7HPamZhkLMJeBsFad12po5oGf-aUXEwqj4YAfRScT6xeXWMkefRZvPRNfZdxHdfQDP6p3XJnj50vTuRaAY0j33AHFY0qdpt6xAS8MRBZLEp6OQ1nAsj5FoLul5bWPbMTslhg_pyPDvmvL1P--uYlfHtIFXJiier5R1sBSa7dhloKJFJwCIIvyRaWtI67-mjTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مسجد برکت میام برات بمالم</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80438" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خدایا کیرتم</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/80437" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آرژانتین زد</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/80436" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80435" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80434" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسی باید تو اوج خدافظی میکرد تا اینطوری یه بچه کون توپو از زیر پاش ورنداره بره</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80433" target="_blank">📅 00:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خدایا امتحانمون نکن</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80432" target="_blank">📅 00:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واااای کیر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80431" target="_blank">📅 00:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چی گرفت کسکش</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80430" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسی کیرتو بکن تو بکام کصکش از تیمش برو</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80429" target="_blank">📅 23:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گوردون برگرد نیوکاسل کصکش</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80428" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انگلیس زد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80427" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اهواز به طور متعدد و وحشتناک صدای انفجار میاد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80426" target="_blank">📅 23:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این بازی عجیب وایب بازی آرژانتین هلند ۲۰۲۲ رو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80425" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نروژ عزیز لطفا تو دیگه امشب فوتبال رو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80424" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اهوازو دارن میزنن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80423" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زلاتان ابراهیموویچ:  انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80422" target="_blank">📅 22:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زلاتان ابراهیموویچ:
انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80421" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پایگاه‌های آمریکا در اربیل عراق مورد هدف قرار گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80420" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHeSaM</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dghNp4piSxUP2cF8XQqOVHxEset825vfsWA_jP0cYub9MYJ0LcaAcDKbBLHq0RcQS90bguEg7ez9ASm5fXamkfnmWP1FDaaZ_1ebG5-Sufg7s5zNwI7Y6mwRUp45bsdc3X8aBz4nlfP-e-w4yiZ3x76_G4nbqsGs4A_By6njjFfM2CPKYUa5MCdwXskQaJsgU3vFYfwMoSo2Raj65ChS6MqXtnbl-evXQj7VKyaXpeN1gtl3oyK120ydf145YU3iDDw_bna9A27e9KvjDImuI-s7I3cBoBqABaNkyhjDdFk6JaHYDNHRqvpgKzM_JY5At3UhT_XhsBNcF5gazWXWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرتون وینه؟</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80419" target="_blank">📅 21:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJUj0EbtUUNYkW6mFQ6wpuXnSOFqcAJJyf6aNX1Ua-URoYe-sDfw3D4858pahGN3ht7SWhbif3MnKTuq0Em38tfZVoBqZItCFNz1VMPc1BzmUmQGQPbQuLRJ4gcuebHBFBxYf2pawLYaZcXd92w6Pq11DbgPEWy_22u2NkSI_DBic04XxwFzp1cMQ-ziG6W8k6aTsODkjj4y-Hd7b_268_vqx4UUPUmxS7dNsJPVNv9F4VFQYAIzvU3onJQoNdtTBO9_PzfAMOgn-pLBROi-owlsTKSOHeKMFeqZbrzOtuYw6FPCUmnqSM-fawqMm3nzh7r6BKKm2GNeyoBzYvCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80418" target="_blank">📅 21:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-FA</strong></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80417" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80416" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80415" target="_blank">📅 21:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIUKdk8dh2W4aDVZbVrgrzp9RXsBdqUcaYOeuUZw4ys5tCun6P6RpOMhZwBoyzx5J9ZqEIkdtRRoaJTX0jt3n2Vy85XI4gFyUht0ED1YqhwMzqeKQAkRgBnz_zhPL3AE3GI81MmHfFvBHp7GdwFFjD_mzSxErl8FnIZREBzCuD55KaWekMDUDNBoXi-kLQERnHIwysK2-8QkBVw63Rk8md7N-Sbl4A5MeF0Sl_4NyN9xzUEzHR3U-du0SQAZQ1q1ux04EPP8_BBnyutOYJXRfdKuvbA-_fC5tgb_9n6mHV3R7ohoFz_0MeYSDyQCUiauZo-py6rOD5dvyYA02PLcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80414" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیچاره فنای رونالدو اگه امشب آرژانتین ببره ناچارا طرفدار اسپانیایی میشن که پرتغال رو حذف کرده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80413" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5-OKBqub3enTRBwxCjCGhbA-2u_26uZ9Rc2PSyAq4VOfPbVCBXHLGKjkXHzLcnV1ZNMmFGtLG6PvW9WmjlXIkINDCw8yAXTwPYam9s9kfeFAXByAfjTD1IOeVZzBE_nITCgUQJ0ATAsFikJmOHIGf1k-Ni5JF0uvMMycYPbtWXDNe4bDxUhrxWWWzoFiw6OtHgf_T9VJ5OZCE7c8ioq2r2aGO_x5G5RsZvZy0C-FnpigEO-z6ljG_2F9xe1XXZN4UbvArPyyCzgRuVef98593dmNlP3IQk2StOYLXqiOaSL0l-uopsHj9uv2yRGYC-jSiteTtBPhRdtnJRlt5NNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب دومین فینالیست جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80412" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdLDalkPxm-CL88MLEOWHdCMhnQEHz3k29y-v7XlgzmWr-6-O9Z3wOW9kuLJro1M7tqAUylD8q55ZvrgbFiajR1XTA8yIApHTuMA-jxi5zB_yPwleM8AHuNzTaeLmhwivGHddbqDtgHyi5vDgcsh3gDkMmDq8dJPqibtHBdoJ5EyDYjNyPo32QnJmzH5SpZ-BjeUqpYUYRNHtRM7tlhcgdRy68SkI5VVC41LD_vRF3FpWCg9judYW_tiM1x30pilYjf0kW8A_muQqMUVVGL7Uhbsfw7DQzaDWSmPgNbOM9Od2jy6uuPeOdifLAy7I7IvKg4Tk1k8As6puAyZOAK0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ۵۰ بازیکن برتر جام جهانی از نگاه مجله اتلتیک
پ.ن: گشتم نبود، نگردید نیست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80411" target="_blank">📅 20:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اقا مثکه ویدیو قدیمیه ولی خبر اعتصابات واقعیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80410" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=B8rT4erehdDT3Ei_9Z3Reko6M0qwQ6pO9PJrIJY1UwgbNDTIUb0geZ9VGYwXgfny6t5RQqhq7nQfNf2W166GXo-6CbPHHqp6NLTVLW-DOqDMDkN7w7mYg4K6C4ZymRrzrR0AyEHencl4lWgD1DhEiJxIHTv061l6ixV9z8KjdrHXdJHDlIE5pYtjVKC4AKS9xvOhHnPVdjbgwagL1RAHIM7H4L5_whplwHSbYlkcDDH7TxIt9xyAN8UIcV2-phpJDfYogXzfNCGbcIKd8zWstlzE4BxU9ZJvIEacDqVWE5368yxl_hBpHwdVLY91-HJjyQn7d32uQBJ_z0MBDUYkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=B8rT4erehdDT3Ei_9Z3Reko6M0qwQ6pO9PJrIJY1UwgbNDTIUb0geZ9VGYwXgfny6t5RQqhq7nQfNf2W166GXo-6CbPHHqp6NLTVLW-DOqDMDkN7w7mYg4K6C4ZymRrzrR0AyEHencl4lWgD1DhEiJxIHTv061l6ixV9z8KjdrHXdJHDlIE5pYtjVKC4AKS9xvOhHnPVdjbgwagL1RAHIM7H4L5_whplwHSbYlkcDDH7TxIt9xyAN8UIcV2-phpJDfYogXzfNCGbcIKd8zWstlzE4BxU9ZJvIEacDqVWE5368yxl_hBpHwdVLY91-HJjyQn7d32uQBJ_z0MBDUYkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتصابات در بازار چارسو و علاالدین تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80408" target="_blank">📅 19:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hARyZirHJNV-n9VJpBgZHXOnG387Ax8c0SB5ywuQGk4MmdSEd4rb1tTfPDvsBT2aXRHOvaF9TPGYOkyGvJ7WlkDvtywaf0F41HZi-X8LBdl7kptnu6gQb8L0hNvkAE87wpi84TuNhIof0XtaKgLXi8P9BLpJC_rznAj_VVqhtdqURz97BCpYdRgJv5GrgGpJ9qFHNxg6Z3oGSjB5hMHcBjf_R3fxKdmRqhgYN60ZzF0jBIb8u2eQw4KtvAnyW_t9O5eLyvglWlkUc62Bt6QuEx2Gk8LbYNOs-XlynS_5p3Lc_o_bOdVvuk7jIt7sfSl1MMsVSPKL81DDBGFnakpotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا بخدا
چطوری روتون میشه با زنتون سکس کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80407" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6Oe8ExMt9ytt09MIssajddfd9nH34liNa7Un11Mnx3etGfnkFdeyO9Gb4V86NSnRZ_oGAqBe9tP4XipvGJDxGHtLTekGTx3k_0mlWcTFWowM6LGjnrq590XIiWzZYkKJbW0Eo6R5uwxpT8FfT2IAseU6jTSkYmRg5gLVj3Y1QNc9xOHbmzl8t0n52ZABiRNZXNiswOjkV31sotFP5ebxI_9opixqTYMfB1SB0HmXVNoeticxKE22ZuvLxMI8Kla3b0D4ETZWP7dSuIBNAS_mPUWQY5WMUKbBe18e3gOrGnaIgRtHS8-yGXyP5NaNY_qeu1gV3or4O5UDDV--zUZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g24
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80406" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK6_iLUn9t5Hp3xmd8zq3JYNCgG40mweKUUd4xT0MVUUxlUC4uqL2DKwrn2lYs6jRfuElQs05cW_vQCztCCGo9PooQt4nt3jYyMrxcqwTCOTCwZ3pzB04m9ZerPW3cLpFs2AU3rDkaXUGWkWGvsxTkdB8vULW5gLobPcy1iTV-xYTqwyC15v91-T6UN10pgrKGG1_DbNhXEnmntmd4Sd9pb1JYSjmhoqh--tfLMJ-ciXet2buVGKvUKDsxi6aTGRE5a5ZGamBndsZez8tIz6EBb4n6ntNcc0nWbi7NbZFDm_DY0htuQOYXG-VXgSJyGbsM6EQT19qvJrM5OLOWCIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاخارا بخاطر پسر خوشگله ببندید رو انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80405" target="_blank">📅 18:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به به به این خبر
عظیمی راد، نماینده مجلس:
به آقای کاظمی دقیقاً ۲۴ ساعت فرصت میدم تا امتحانات نهایی کل استان‌های کشور رو به تعویق بندازه وگرنه برخورد نظارتی شدیدی روش اعمال میکنم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80404" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کصکشا حداقل برق دکلای اینترنتو قطع نکنید</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80403" target="_blank">📅 17:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqg3lITGD4CF4poh0hsbN8-4Gvb2iX0BACLqFmkeYcpy_Iw6M8ZwMie0ON80JCm0ntuVg-GCGNlQvRfEL6nz-zcy9G5OJVqM-0TGtOK0C2lql6cVxuyb1EWnus55f9wOJR0_M3UylZGKi4_7c5LUyKx_K1WH0xC_GzirgBf4IA-jDikphiB4SF4ZpBF1009lo9G6rJoWfjy5Kb1dKjunTDMgO62N12F-5INI_hNg5cjtvLf2hWdmnjLUsesnhiGg4vMEoaHjMbzcHMtLci-mhAnBnngrx6y4GC9rlfoJnXhpxGlQqicF3tCYqJDFk9oolhBv8EjDlB9ZSI9EQwLzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیک علی تجزیه رو از صدای امریکا زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80402" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8TWVPknFP0idEzcD29vp3im4pSuE9leIq1lrt6b19vFh6nJWFV3K4gqi1UMDC2pxJdb9U1gX5XyePBZumI5YfK3UpfSlIZiBEReGgaY1ygszONyTDrHj1JQ9PFCXl4eN_YgQjzPzmRtupimzsER64jytNNdYIhoPgy9qgI6W01G2x72bha0QkDg6Wpjabo5h5-Ncg1AtgEylpPWe4XpGyj_PS3gr58LcNW_uDRA7i3BlTX5fIK9EN6rnLQvJP5MLmDkpms3dVI18zYVXPBEKoeCWFx7fNmhU-fhX_sU0mBkdLVshtb683zsUc8odTlglBVnQNslZDyZim_TTTXRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چی بود دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80401" target="_blank">📅 16:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام اشک ریلیز شد  Spotify  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80400" target="_blank">📅 16:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlfA_KT3Tt3cZWFBYiXKVkFBphNY2J5Vbwh6dQgDTJUopUuA5bsVaKf8gJjAtGOWsay_atkgBaSu33HPv_qXAe3SPwWDbBsr1-OpOx-rlHxdx0HboLnIQpNGYF-q87eSA13p0VTGHi3o4ds6S7bVyn-J6QOXPvEql0XMR8oAmv5OLNnGf8HwpMSheWV17nTi1iDk7w6fl4EaRWBgkPxfypWa_iFyXTLeb3KpCsRLmxDMQ5ibrs9OcWlnqe5YuzcizQS--lL3si0GlwD8ggLGQmYAFT5--Sc9CebZG9tjT3ZVVpQTFD6vFSKXYqkQT05v7zWpsVN1k6EA0dTL4_Lzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام
اشک
ریلیز شد
Spotify
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80399" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عجب ترکی دادن لنا و مهیاد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80398" target="_blank">📅 16:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTrL3-0lfhkxwJoLq8uL574VzwxlI0OMy76hSRMKLz4xsImHNzWGCQaukvNj2fP1eudmO73xMldo8qIi1Evvk9wPc7S9TK-mHFfzJbY3Fjf7qFJWo9xKRLeIaqAHWsjuY2VjknSVQ-59OCfXXC1L-AQF4R4jYCHL8Zl9P3BgdvRy3zQwHTrrtyev2dAOaZoK1PC6O3NCZqURyv3fuxc-yZn_Zp4jDS3YkC4L8mXYBzasDuKb_xY-8TWZA0IAoDswjWeDrPDhjl63sVvLMMwzCsnxLD_SHj5797k1uVc1MmpCd63hLhPEndgeQf_2X6PpcPNhD6-YeWJwbjc5oMKEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80397" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جدی مملکت هیچوقت اینقد رو هوا نبوده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80395" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80394" target="_blank">📅 14:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80393" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">که اولیسه و امباپه و دمبله قرار بود کوبارسیو جنده کنن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80392" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زمان جنگ میگفتن نیروگاه بزنن هم ما برق کم نمیاریم، حالا که نیروگاه هم نزدن روزی ۴ ساعت برق نداریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80390" target="_blank">📅 13:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تا کی باید تاوان جنگ طلب بودن چارتا پلشت مثل جلیلی و رسایی و امثالهم رو مردم بی‌گناه بدن؟ دیروز بچه های میناب امروز چارتا سرباز بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80389" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حقیقتا تصور خوبی از این که همزمان با محاصره سیلو گندم میزنن ندارم، خدا رحم کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80388" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">محمد امینی دهاقانی، از معترضین دی ماه، متاسفانه در بامداد امروز اعدام شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80387" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80386" target="_blank">📅 11:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر خزانه داری آمریکا اعلام کرد چند کیف پول دیجیتال مرتبط با بانک مرکزی ایران را تحریم و بیش از ۱۳۰ میلیون دلار فاند و بلاک کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80385" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMycaFqEqKacy73Jn3yRvwmtlYkbh1VhxclVB0hbatgXczb9s9v8ATk2St3TiTwUEmTuFTi6lAQrE-l336VnxHu2K1hw-DiA0C8Ofcl1yfX_Myw21YuG1eX7OJdFgn3mq88yV26TaJBQx0mSUz9vcgd2THng0hvvK7wngQ_QIrE3N5UqWN_EaXJx5EG1flBiO03xAOSgKHdzUqrPxvwsdElxoe5TJtD_5zyOK8nMMgn5u4d7_GRrvWTaHZyQFGUsHbNp_EI00diO_Cp4TDngnBuv9eNPQQSz6YfzrnE_Z5_EeNoz0ODQEAnUuxGlsbnq5iEroqcynFVgaPtLG48-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تا الان توی مرحله حذفی جام‌جهانی یدونه دریبل هم نخورده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80384" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMi2z4ClKSpIN3jQiGBgfb_xfqBuSGeqiDMY8UtD5lmy-ix_TWkDOffi6NqBPw-IFCA0xXuFDWmOTquaQQYRip6Jaz9_Lra3TC9y_tWs9j3C55hfYr8m6GllcZC4Z7lItNHHgZ5PQ1BxEQkHAfSNUwTv1SY0kR3OJfMwBee_mxIhOLPX7rdbR7tV_f38ud4AdmStDDUoBj9nc_ggZUDE6B6E1IOoLIBPntNWNFrG6yHluoJ-aKQAQ8WUptmHQCaiVd2P0qjoPnpNt8L3J0-8K2tNGZ8PBiRU8Md8aa7UP8VsjZegqzOyiMfqWL5OeM-c9uMC9oHFgGuZYpncUC0SFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید داداش یامال و طرفداراش :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80383" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5b33Kmknr7ZsM5ESzohBYHfeN2rtDUg9Ya2I8qfvV_iYPSSmJrGmb6e12to_P7gW5qxZdej_5UVombXnPXzije3zLway4TCZQIWCZ0oYv8eggFx9ezyX9AtDo0IhqlKUrnfJ_BAmNCzpc-oViQSfIopI8w8oItrQsH39INvS0vZgfu-86b8YziqVISEyurNNe65BxM3hc6IF5TdKW-YQH1WPO37wKHJ1mEqAfNwkhY3A3_Qm5Nwo_vdzIuxj2uImW5EBDIkO7gBKm6aSIeQ4ew0ZM2_dqCLNCsBCoQO1Feoifch26a6n9pdsztSh64-FiRAIJAiEWfygt19R6BeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80382" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جمهوری اسلامی ایران اعلام کرده زیر ساخت های استارلینک متعلق به شرکت اسپیس ایکس جزو اهداف مشروعش خواهد بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80381" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80380" target="_blank">📅 05:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80379" target="_blank">📅 04:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80377" target="_blank">📅 02:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">باز که شروع کردی تاجر
ترامپ: ما امشب، فردا و پس‌فردا به ایران با قدرت ضربه خواهیم زد و در مرحله نهایی، نیروگاه‌ها و پل‌ها رو هدف قرار خواهیم داد.
اگر اونا با بازگشت به میز مذاکره موافقت نکنن، تمامی پل‌هارو هدف قرار خواهیم داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/80376" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بهترین فرصته ویناک هم با یکی شرط ببنده سر پول جیگرای اونشبی که شاهی با دوس دخترش خورد و فرار کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80375" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینام میدونن ویناک نمیگیره هی دنده میدن به همدیگه
اگه خیلی پولدارید ویناک نگرفت 333 میلیون بدید خیریه با سندو مدرک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80374" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اقا رپفارسی درست شد
ادرویت و شاهی رو بازی فرداشب بستن
هرکی ببازه باید بدهی دکیو بده به ویناک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80373" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80372" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
