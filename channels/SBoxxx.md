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
<img src="https://cdn4.telesco.pe/file/Cxwcb5h3xAUcTM3S3ZxSOXY_zDksSkslmAMShTJn8_MoJi6LrACJ5KgesmVPd1tZXy7MxtRrlcTtuLs0CZb5WTCr7G2-LUx87UnJk6lG7csZ_8ft9pR24cAcbEWPpAbwSMT82nGRFfBNzgnc33YJ2oFveBUKV8IXJOLQ-Re6DLgvy0yFFBgORy-L910On3sYG5oOLYdFzM2KkBQRu0aYwLqsgAJ1rgS65z43V5NVdKyJJbLeBTi6bfstVvsj476rJ-PBMUQhTuY6h2aVETq0lsAUV5ivXV98L4ySOikw8yUveEtZT8fCi08gHBK-x4Jh9-KE6lZrxY2dsFU_SoUFIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه لبنانی:   امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SBoxxx/17582" target="_blank">📅 12:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه لبنانی:
امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SBoxxx/17581" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=VxcsVso-Vnp9yXMs-cVqfnvfsGZRk-cmzAwZUxjVlgmpx0N-N3X0XuQyVwP6_N68Ly6VReTZTd4081loFFjAssLcS4kN-bJSWCO7MFp6joR_kjicjvM8Dcts2rWCAvLeuIq83_Dms1sWynozEYfmSouAWwuGTjDHzdr0xAM_tahYinKsIT4GgEoHbFWE_HmGdRnT_eDWraSSmMUddYn556kJIIK5HTf5bgXPkrpzJh6uT8REzhtf217bHrlFP42aWFo4O1Hd2BjA6GxU9GQpoRVYXyXsWJLTqtVtf7weqUkHMONJ5xL4EdufWlXIAdINbanKnCWeLSVAd9m0QCh4QV4Y83tkh-kd0JutD8bJnz2wFbdya8KOG0tSbx0t-bGbNv-0eY2xBryNd5K-nYlreU14oAV1DL7Lcd6oDrqmPLMwcLEcUGwekz237aDGX5_9ezAe9q_3rMPT7JsdOIW-1BGVemuCK7qIS00UXEDMA5GiKCfb9lP8b2eAjNyHAHXc2qmvu-7xp931ciDzlCVw5-k43Cjhcia47rlWGQxkXTEgLSFsNUstq2t1dvxLteLP9ln8ENnSrCHzpCRNlsOqpfj0D3X_QIGIXJ4fZwrEm4dOWiv5tySk5CRqNHjU7W4zAdj5YHdvnXeZETOrFlp4TkgC_qRiBEpqzMxa7Sppcy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=VxcsVso-Vnp9yXMs-cVqfnvfsGZRk-cmzAwZUxjVlgmpx0N-N3X0XuQyVwP6_N68Ly6VReTZTd4081loFFjAssLcS4kN-bJSWCO7MFp6joR_kjicjvM8Dcts2rWCAvLeuIq83_Dms1sWynozEYfmSouAWwuGTjDHzdr0xAM_tahYinKsIT4GgEoHbFWE_HmGdRnT_eDWraSSmMUddYn556kJIIK5HTf5bgXPkrpzJh6uT8REzhtf217bHrlFP42aWFo4O1Hd2BjA6GxU9GQpoRVYXyXsWJLTqtVtf7weqUkHMONJ5xL4EdufWlXIAdINbanKnCWeLSVAd9m0QCh4QV4Y83tkh-kd0JutD8bJnz2wFbdya8KOG0tSbx0t-bGbNv-0eY2xBryNd5K-nYlreU14oAV1DL7Lcd6oDrqmPLMwcLEcUGwekz237aDGX5_9ezAe9q_3rMPT7JsdOIW-1BGVemuCK7qIS00UXEDMA5GiKCfb9lP8b2eAjNyHAHXc2qmvu-7xp931ciDzlCVw5-k43Cjhcia47rlWGQxkXTEgLSFsNUstq2t1dvxLteLP9ln8ENnSrCHzpCRNlsOqpfj0D3X_QIGIXJ4fZwrEm4dOWiv5tySk5CRqNHjU7W4zAdj5YHdvnXeZETOrFlp4TkgC_qRiBEpqzMxa7Sppcy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:  توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟  امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های…</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/SBoxxx/17580" target="_blank">📅 12:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:
توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟
امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های دشمن محقق خواهد شد.
تمرکز برای برگزاری آرام جام جهانی نیز هدف دیگر امریکا از این توافق بود که به آن رسید و آنچه قطعی است، سناریوی دشمن برای ادامه ترورها و حملات غافلگیرکننده به ایران خواهد بود، ضمن آنکه رژیم صهیونیستی نه تنها جنگ در لبنان را تمام نکرده بلکه رسما گفته هیچ پایبندی به توقف جنگ ندارد.
در هر حال این توافق عجولانه و ضعیف که ناقض خطوط قرمز رهبرانقلاب است، بیش از هر چیز ریشه در همان موضوعی دارد که ایشان در آخرین پیام‌شان به ملت اعلام کردند؛ "خطای محاسباتی مسئولان". خطاهای محاسباتی عمیقی که پیش از این نیز راه جلوگیری از جنگ را مذاکره میدانست.
واقعیت این است که این توافق حاصل "برآیند توان و فهم مسئولان ارشد کشور" در شرایط فعلی بود نه ناشی از رضایت رهبرانقلاب. وقتی تاب آوری مسئولان از مردم مبعوث شده کمتر باشد، خروجی آن تکرار خطاهای محاسباتی قدیمی و دل بستن به توافق با امریکایی میشود که هدف آن نابودی ایران است.
و اما حرف آخر؛ این توافق نه گشایش اقتصادی خواهد آورد و نه امنیت کشور را تضمین می‌کند. روزهای بسیار پر فراز و نشیبی در راه است...
✍️
امیرحسین ثابتی
‌</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/17579" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4giRSS75m-8RVFvARvrmsvg7Hr-bK4spzwgiMqEub-4ANFJM0ut99ddky1kQx7FpD5GawDQv25-TP0b3iiNp7amrCk9Z3ebu6WU8hbe-I7CUV_YzecpTX_3fNzvITy2HV22-a4uEzQ15NfbWANG7LRRLZXfBvefUvWVspf-8UR5L5PpVkE_fN9mC9sm5CxXIfog9r3phBJ_I5dQlFNspTEd1zx0AnG2tZG_BzTLb_PZWwYXFsThDj3R56I7EQBZBBEjaxBpHQeNP0xhf4h_QUzvFe9nKZ6re2cnbDVxjqrWgJrzUbe9nLRergP2Q55qECoLkt67-mnbYTILnk7TrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/17578" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هدف حمله، علی موسی دقدوق یکی از چهره‌های کلیدی و تأثیرگذار در حزب الله و مسئول پرونده جولان بوده که کشته شده</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/17577" target="_blank">📅 10:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/17576" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/17575" target="_blank">📅 10:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/17574" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر امنیت اسرائیل، بن گوییر:  توافق ترامپ ما را به هیچ وجه ملزم نمی‌کند.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/17573" target="_blank">📅 10:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تحلیل همین است.
این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.
پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/17572" target="_blank">📅 09:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">- به گزارش معاریو ، بنیامین نتانیاهو، نخست وزیر اسرائیل، به دونالد ترامپ اطلاع داده است که نیروهای اسرائیلی از لبنان خارج نخواهند شد و اسرائیل خود را ملزم به رعایت بند مربوط به لبنان در تفاهم‌نامه ایالات متحده و ایران نمی‌داند.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17571" target="_blank">📅 09:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17570" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:  معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17569" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17568">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJfb2ISsVLVbwf5CbmK0JUXLiPjao8wpPC1kWzpwdv-WWmXv9Aqp3UeoApV-IiFwugTIXntGyMtRzWKoESweGqtLaI3nd3U65NT-QSIhjFhWTph23oQX4rMlWxrTXyr2SHl-Tm9abq0vwxhFegTC_0dca2QdsmY8XtCKa0QjGw5XAnZAw39Ropu4a0KSzV8lnOmm23EibmL-SgTNlElbPN5AzZ5egCxCVzH_K3fVJd5e4ihMNLhhF3C-Ip9sN8m1VFH9-I7Gsnw0nacWUk7MQlhxj8kdAiuwwXCinfaNslwguhO8YqeutLAZHBwz3GnjQRe7Swoi9AwVHP_jj5-P1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه:
لغو تمام تحریم های ایالات متحده و قطعنامه های سازمان ملل جزو دستورکار مذاکرات ۶۰ روزه خواهد بود</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17568" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نایب رئیس وزارت خارجه ایران: پایان فوری و دائمی جنگ و اقدامات نظامی در جبهه‌های متعدد، از جمله لبنان، باید از امشب اعلام شود|</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17567" target="_blank">📅 01:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آخرش هم گفته بچرخ تا بچرخیم!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17566" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فعلا که خبری نیست. فکر کنم آقای دکتر لانچر خودشان را فقط آماده کرده اند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17565" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ
:
معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان نفت آغاز شود! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17564" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alKG3NdNGIhJ2AB9KdgvT4vpN_39DgYHPj5Vf_O_5fdC17ak8p2DkkYL20ZnHXniZckjdhvyGe5d7Zcfq99R4ct5ffrhbVCfVtJuJPwEGPqbpTNYbSRQWJ7EKTBslc-y2bJJOHpkMo9uLQCSMVtQru5dEjo79RWS19vWiNOTaVDFnExyoks1zZ_qPgJmNm0TfwNot__b96T3rxZ-c-dg0bPZeDkjpDszRk4uIKZ1XVVdMdyU0fLYSRNP5LZC4gSDLXYrJDXBpswFYb71ChgVgz6SGeKgiQiDgAVJZ65RawylNv-EeiBvzBdcDldd8Mcy_ovacx1x3rwgVUSfr0rrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام نخست وزیر پاکستان، توافقنامه پایان جنگ جمعه ۱۹ ژوئن در ژنو امضا می شود</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17563" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ
:
بعد از ترور رهبران رده اول و دوم در ایران، رهبران رده سوم فعلی منطقی‌ترین افراد در برخورد با ما هستند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17562" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17561" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: ایران در توافق پولی دریافت نخواهد کرد، اما ممکن است تحریم‌ها تسهیل شوند - WS</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17560" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17559" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش روزنامه‌نگار اسرائیلی رونن برگمن از ی‌نت:
پس از حمله ارتش اسرائیل به ضاحیه و تهدیدهای ایران مبنی بر پاسخ موشکی، به نظر می‌رسد تهران در حال بررسی به تعویق انداختن پرتاب موشک است تا به ترامپ فرصت دهد که توافق‌نامه چارچوب را امشب نهایی کند.
به عنوان بخشی از مشوق‌های این توافق، به نظر می‌رسد ترامپ در حال بررسی لغو فوری — نه تدریجی — محاصره دریایی ایران و تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17558" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کله زرد :
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17557" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17556" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باز معلوم نیست این فاکستانی ها چه غلطی کرده اند !
احتمالا دوباره نسخه ای که به ایرانی ها داده اند با نسخه ای که به آمریکایی ها داده اند متفاوت است</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17555" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این فاکستانی ها چه موجوداتی هستند که نه آمریکایی ها به آنها اعتماد دارند نه ایرانی ها!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17554" target="_blank">📅 00:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFRhaQn3ZYu499C0eJU4091bkGb3XiiPDdO1K7OTkvUQ3-H5vfpvD8h5AcQ8xba1FsdPxSCnrIZlCdgDd13bsZpvXq29MFZb2tgrzd0Ne_6egSofB2D5EK2ZCp4H2sTLH6ah1J8rnls8b6A1OK_4Aa_5NciJ_mZWDgU0amtuauyuIx_0vmPq85BDFWVAWUOq1U8BMpNPzvx5Eg1ShnVQKY01gdZuf4GsdckNYM0d0i7Aa-b3tzENWtYNkOpBhsloLihoS62oj65pV3U7L1LfkKonc6neOUAjwa7u8bXHDuIH54HzzlSGDUfHJgeNleppEMk4dxjzC9icd0C1JlkVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.
دو مورد که مدنظر من است:
— همون همیشگی (حمله به اربیل)
و|یا
— سپردن کار به بچه های نقطه زن یمن
در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه باشید.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17553" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17552" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی اکبر ولایتی:
یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17551" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ونسِ ترنس در بحبوحه تنش‌های فزاینده با ایران به کاخ سفید شتافت!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17550" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:   هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.  نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17549" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:
هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17548" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ینت اسرائیل:
دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17547" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قالیباف:   آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17546" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قالیباف:
آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17545" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17544" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیدانم که میزنیم یا نه اما میدانم اگر بزنیم آنها هم میزنند و بد هم میزنند</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17543" target="_blank">📅 22:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خداوکیلی از دیوار هم صدا درمیاید از رییس جمهور مملکت نه!
بلند شو یک چیزی بگو مرد!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17542" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فوری | محمد مخبر، مشاور رهبر ایران: به متجاوزان درسی خواهیم داد که پشیمان شوند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17541" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-poll">
<h4>📊 امشب:</h4>
<ul>
<li>✓ میزنیم!</li>
<li>✓ نمیزنیم!</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17540" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17539" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17538" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این مقر موساد در اربیل مثل درهای بهشت است
هیچ وقت تمام نمی شود</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17537" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مقر موساد در اربیل؟!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17536" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محمدباقر ذوالقدر: لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد
پاسخ رزمندگان اسلام در پیش است. وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17535" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8AA7lULFgskDTvjF47EJoDGR8UkEqgLKZUvx1AY66C06xCULsgADh8bp1MpXP3zOCpQmbikQll3SpeFjisEDpTHBM8WD6fR96Eq66TWE3ZmzIISZPn4-qOfz-wUK3FbnLRN4LTgkrbJSu6-tdF5XC2ngX-9F8jIHX7EWny6n67Xm9zUNkeBUlSH5bgtn8Kf8raxhmvtTC-hysc3eAcr7h1LrSeDFS5DW7TxVHOwrMzyCTAgLWVTo9n1A3fBpLeQip3vRX3MVvIEhIMSa52N3Z0ytptrpSoetJNxqnTVy9xNVAjPrKuMgnSBiJpyPG2Ew5mxHRpfwV-Ok7UXGdc7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17534" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">«کانال ۱۳»: ترامپ با کلمات تند از جمله برخی ناسزاها به نتانیاهو حمله کرد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17533" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17532" target="_blank">📅 20:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):
«انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.
ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17531" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اصابت موشک حزب‌الله به شهرک کریات شمونه
منابع خبری متعلق به شهرک‌نشینان اسراییلی از اصابت حداقل یک فروند موشک به شهرک کریات شمونه در شمال اسراییل خبر دادند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17530" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17529" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17528" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.  ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.  — شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17527" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.
ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.
— شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17526" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آماده‌سازی حمله گسترده ایران به اسرائیل
اینتل واچ: یگان‌های هوافضا و دریایی جمهوری اسلامی ایران در حال آماده‌سازی یک حمله گسترده به اسرائیل هستند. بر اساس این اطلاعات، فرماندهان ایرانی از یک عملیات پنج‌مرحله‌ای با روندی تشدیدشونده سخن می‌گویند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17525" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:  «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود،…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17524" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
«حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود، مجروح یا کشته نشده بود، و نباید این روند مهم را مختل کند.
ما بسیار به توافقی نزدیک هستیم که صلح را به منطقه از جمله لبنان خواهد آورد و همه طرف‌ها باید از اقدام خودداری کنند.
نباید حملات بیشتری از سوی اسرائیل در هیچ‌کجای لبنان انجام شود، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری از جمله حزب‌الله علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد، بیایید آن را خراب نکنیم</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17523" target="_blank">📅 18:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17516" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قالیباف :
تجاوز صهیونیستها به ضاحیه بار دیگر نشان داد که آمریکا یا اراده عمل به تعهدات خود را یا توانایی آن را ندارد
با چراغ سبز نشان دادن به رژیم، نمیتوانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب، دیگر کهنه شده است.
اگر اراده و توانایی عمل به تعهدات خود را ندارید، صحبت از ادامه این مسیر به سادگی ممکن نیست.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17515" target="_blank">📅 16:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=OF8gUqavnKDN6cQ3YbFKibhXn6kEAZ6y1kwgPd6ojRR8PlRS2GMVlj02RfkRi9MmoBsl4rXuDGdUeEx3zQdsdfgvrM8bMFHAq3x0aYtieSgEEItxXOdzbQLHMtClGbH6vrcJpmPtmav15IOppwb6jea4v-AUdupdRl_L-M7Y7hXGR5Y0GHaun_hMIznRD1BPLeWozPIJ2eg7LooDFtzmQlMCL_O2A4dz3CxbQ6taN-oj3xVg2Rk2wUGNQAg0OVV6vpr_-PfQQD2R9aqL83n1aPBqX-Rk-d5fOBwWb_8Rl-CuuwZdvvpM5yYib0NcyM0A0dt4PnYmTN4Vf_q30WISIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=OF8gUqavnKDN6cQ3YbFKibhXn6kEAZ6y1kwgPd6ojRR8PlRS2GMVlj02RfkRi9MmoBsl4rXuDGdUeEx3zQdsdfgvrM8bMFHAq3x0aYtieSgEEItxXOdzbQLHMtClGbH6vrcJpmPtmav15IOppwb6jea4v-AUdupdRl_L-M7Y7hXGR5Y0GHaun_hMIznRD1BPLeWozPIJ2eg7LooDFtzmQlMCL_O2A4dz3CxbQ6taN-oj3xVg2Rk2wUGNQAg0OVV6vpr_-PfQQD2R9aqL83n1aPBqX-Rk-d5fOBwWb_8Rl-CuuwZdvvpM5yYib0NcyM0A0dt4PnYmTN4Vf_q30WISIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=L1VV7Ba4BWpbLUc_xbkGRk-NAeF2RDcj1jMNFA-XcvRvW2jyrzXuo-pZwhsIe8PGeoEi0qcweVu_OHdZgoXNyzQ3l8Cfdew7GOLoSsbXpajLvyUtGNTp2_9fx21L4kSgdS0784O32zu90lZyi8Sq0r_RIVSyjDhK1qlaTDZvumXFnFnzsclMGRyaWQRzaJDBSW09YAdj1TVJvD1DgJ-zj_eTNxG81IeavAXXc1NK21VEXUGB1oPQWFLZnMREv96OcDCs5O9k1plEM_54rJt-B84_QxAY3dABHHrmdQhkpsb9JfyDT3Wk7P3RKBhfGOvZDVFqltrYJGOmiTr1VAzpFC8P_9yAlwPV7doFhGZrJAgvhLtS9LSQvVjA4tYIYjWJzLie_zlbBy6pGVFfcj3FConmZfETI8ELdLi31IbPDq_3hKXwBAW26czXiTtuXcvjKX2pQ_5HMAT_XF3KFpuGWA_j0sfGA8GChy9ABK2KrQKmluK1AxoUQiOxGzoRr2qvnkG86EtKuqnB-wdICha8PUwO_yfS3BLVK46zKKcsdpMzDMhN0sidcm48GH25sNrlvVl0hxmHvyb1_UEmddDy69UkUdMmPMxbwNxxlkWUH9ZilwLLD89XBXiylRGaKPUJj4qPESa0tKHhVkBID7xug-4JMsHwgAxC6w4_maPV-vI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=L1VV7Ba4BWpbLUc_xbkGRk-NAeF2RDcj1jMNFA-XcvRvW2jyrzXuo-pZwhsIe8PGeoEi0qcweVu_OHdZgoXNyzQ3l8Cfdew7GOLoSsbXpajLvyUtGNTp2_9fx21L4kSgdS0784O32zu90lZyi8Sq0r_RIVSyjDhK1qlaTDZvumXFnFnzsclMGRyaWQRzaJDBSW09YAdj1TVJvD1DgJ-zj_eTNxG81IeavAXXc1NK21VEXUGB1oPQWFLZnMREv96OcDCs5O9k1plEM_54rJt-B84_QxAY3dABHHrmdQhkpsb9JfyDT3Wk7P3RKBhfGOvZDVFqltrYJGOmiTr1VAzpFC8P_9yAlwPV7doFhGZrJAgvhLtS9LSQvVjA4tYIYjWJzLie_zlbBy6pGVFfcj3FConmZfETI8ELdLi31IbPDq_3hKXwBAW26czXiTtuXcvjKX2pQ_5HMAT_XF3KFpuGWA_j0sfGA8GChy9ABK2KrQKmluK1AxoUQiOxGzoRr2qvnkG86EtKuqnB-wdICha8PUwO_yfS3BLVK46zKKcsdpMzDMhN0sidcm48GH25sNrlvVl0hxmHvyb1_UEmddDy69UkUdMmPMxbwNxxlkWUH9ZilwLLD89XBXiylRGaKPUJj4qPESa0tKHhVkBID7xug-4JMsHwgAxC6w4_maPV-vI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx_blkKpInwQbjiRMpH7V1NNKd8ABPiElF_-5Y9Fn2DsX5hlBMeNbwH41nE4TBLKLQmTL-7T5t4htyJBri1vDW8ZNwmw78BJZ7ml9ETUAO0En-KOtp38QnDOWVF72rJ3mgbHDLMN3EIYDE-3GM6Q9ZAd8nuGBdIcN0GyzckLghNCqCO0b3q1Vir0Crszt5jaI7yhxW8yw8NfcD-cnQZpAC1bT0iAsngl7jYtiZPNZQ6Xiti5u0SXDGv2cTJGW6ekMr3JhtkKTZErbkXEdJiGgvY-Z8XZJGEOPRVZSIDQcaM5Glp3b6Tkuxd6kwCagmtaUHIhRpm2Gdw0gIDxfWyyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=KO7WZhl1ns3c6jx0MJoPJ4Q6lSWVo2sfVauNBGOa4t5goqYdUiggzLxmZvI2zVNZKplvJ1xwEc23STShaC82hLDVMS10C_ueq2Uaug1xfyiCtTziKxw7K1eOcq2aPvypqkVxiQg_GO41i3mDBobVlZHTuzn6qPMniWrU5jlp1mwBKNMnTkz2xX5DOam5X-plJh1dvMqZTXd5y06ADiJJUjPIymFCfCXki2BotnJCa2kIZe6K4RUA1wIlccd3HSnfB7dFZmA97e6fvvms2bg0foVMjCY5ANRX8YpYMGjKVnTPAKu_8PwxBMY4YL34qS8xQ6OBpYuDo1nVWOyNK1bwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=KO7WZhl1ns3c6jx0MJoPJ4Q6lSWVo2sfVauNBGOa4t5goqYdUiggzLxmZvI2zVNZKplvJ1xwEc23STShaC82hLDVMS10C_ueq2Uaug1xfyiCtTziKxw7K1eOcq2aPvypqkVxiQg_GO41i3mDBobVlZHTuzn6qPMniWrU5jlp1mwBKNMnTkz2xX5DOam5X-plJh1dvMqZTXd5y06ADiJJUjPIymFCfCXki2BotnJCa2kIZe6K4RUA1wIlccd3HSnfB7dFZmA97e6fvvms2bg0foVMjCY5ANRX8YpYMGjKVnTPAKu_8PwxBMY4YL34qS8xQ6OBpYuDo1nVWOyNK1bwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3sX6BrMuM3vN1iYY6bSRhen2mVvKmkN-kr9bpI9mAyPJKNPef92WiysbZ0zaGXaxMvQvLpcehgM5xKozd40IgBABlMcvIdhHQrrPbdpxkWg2KGsNeP5LnbvyTj-lAU_7afVYkIS3E7lZA80z-JyG2-CMZOmee7OKDsOD5tft7bD_Ft3pwAotUPjlbTYurwWRA9v7GvdH3E7CWqw0bMsTyoqBHJ-My4Rdp41Y0bgxUz294BLQPtk1IibcEaJU8ANzctowHKmWbeYKxjMSEjJZmLhq7v6IuK10j5pG48bMg86csKIVw2hyaafHlGnpKOufTfZlNeMX7rnOG1ABRR6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBBEyFamB7tw5sXuoem7-4rESv7TinZMPK7E65q44JqxE4i33HR1HgDTvaKg-TSwt4U_ZoV5WSn1GraKsy3KfNnnGwg0r2V99xcia9m9SPlk-_sMm68jcjJAz_14qzG5HSj0JDNUfFVkoLI82ozZMlUfwuzA2cQxiN_4AxY1eAEK7VaviYIwTxKmZUk1SlO07_27ca7c1xTn339NQPjxu92IBsHyIPRu9gP0X9aXDK36iWNF9scqLwRWLqOwh4JEEum6Jza_q2MnaMTX-5ddlJytqEphy1XtD5vW6f6QZFydQBmx5gVyrgNb7bpczI-yR2A22WYoP9Rn3AoNE9VxRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b618Hmln6thZyJH6yjnWKbyccNc_WUsvWlP-nzbDjKSHbEp4iQtH4OMXsMwU5DDryM5QVnCXvT65KXYA_nICPdNgZHXnoTfzwli79v8OjuFr-6TPA3NYwj_kSn37P--_jl_scjEwQOOU4MlncBU8EhXBN0quSyIpbOevG9r32OrVgrJEGw2xVuMiuh5Azvk_T2TVSUkPQ9LTPD9QZPDxZLGfVu8PDd4Ucr2h-2D1OhEO5lZZXlyBR2DMFdV_Chj1S2JYJ-lEgDagNAi12-4E0uZyX7mUa51YXVKuOoYpnh9lc3vHIkxPQZjekhqm1A_oK-P-QMSBW-GVmMBsnMlZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RariktqsyNfQeHQzwjrD6kCe9IZBDcEGSPUJqSRuKJryyjmkB8Rno8gjZ7OPa-YOVFaekFoUb9i1mmquB6EAH6D_aO4ZBJIE7gLjzpgvWwcxUK4MKr26Rb3TdzkChm-2075LjPsKXJVw4ImMSpORN6b4wCLEaApm9vWCIGjBWLP8IyNMdbYuNOgMeKU_G4JSSgNlbuHPIOaESNokFPTF_OfidHamzEoGjehV1XmQHGE5mRlcpg-yeojNtj0XQTa-VrIZn6lGAlYK8MFlnUqve-xFWCCUOuxYQGAkVp09dKwBuaIxztUMJhH75wauAeuO1bHkDXFl8cRdUVP_FfE81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0bW7HXgI-Wp_DQ4OWdagxAL5cwRDLlFRZNT2pIatPwx7zkKgADSQgL8jAcTmT28QGYlOyFVoyZdBPeAY0gh_Epr9oYV79shci7R-IwtPPePkOBSdTJ0_iHwZrBUdnR2tosgPEsui6utpSfO93uJV6j6POmmDsR3k_Yit0ONlPWbHhuv9OCdxOzaO_JdBBbWy4TXRJhwasbQ-J1NGBTYIRGNEPAixGEKO4_AJzoHyWalpwy1YKm7n1nYqkIzNwfTWEzTcMWAdbSMzTXQx2nFJy3Mq2Q6l4t8oOY21WTL8z9POuaSP_TSMh_fzZ5Gom_qwnhgxSpKeO6nJHy0qf-5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
