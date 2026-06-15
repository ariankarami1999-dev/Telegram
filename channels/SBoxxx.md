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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 649 · <a href="https://t.me/SBoxxx/17598" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لاپید از رهبران اپوزیسیون اسراییل:
هیچ شکست دیپلماتیکی بد‌تری از شکست نتانیاهو در جبهه ایران وجود نداشته است</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SBoxxx/17597" target="_blank">📅 18:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یاد فلیم اخراجی ها افتادم که امین حیایی آن پسره برادر کمند امیرسلیمانی را اسکل کرده بود!  یک تاس به او داده بود میگفت بریز اگر 1 تا 5 آمد بازنده ای و باید پول بدهی و اگر 6 آمد برنده ای. بعد امیرسلیمانی پرسید اگر برنده شدم چی؟!   امین حیایی گفت اگر برنده شدی…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/17596" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: این توافق به آمریکا قدرت نظارت بر برنامه هسته‌ای ایران را اعطا می‌کند</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17595" target="_blank">📅 16:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/17594" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: انتظار داریم تنگه هرمز در بلندمدت بدون عوارض باز باشد</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17593" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده. طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/17592" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا لازم است یکی دو فایل اپستین دیگر منتشر بشود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/17591" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwAvJKwLAjw0CvA_OJ7tKSSrM9KaUfQNArT_BDy6wxuBlEXY2uh1eBqFO2znhCwaNTPTsG9jCT840O95mec4t9xi5VnmZ96gCrRQ6lDKW2QdsXpMNmvPArI3JVvtnSoWWySQpAMDOejXFF6yAURMEG1qGReAKWjmTynHQo8P-InDRxxSTLNmVEb10m9T-gAKHxJbLQfr9OWckweC87j_yyWtutQy5AHZnsrylIwRKA8q63zy1WO52dAdWVx3hJcJefR5DcajvVYtQ9DfrTKYNgHwAEVBxFaEsSMlDyfc0ilCJPlcC2whbeHTiaNlLptBBiXHsUMkirRJKal6SupGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/17590" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تحلیل خانعلی زاده — از اعضای نزدیک به پایداری — از شرایط توافق  میگوید از 10 شرط رهبری 8 شرط رعایت نشده و 2 شرطی هم که هست به صورت مبهم آمده است.  در ضمن بند مربوط به لبنان (بند اول) هم شدیداً ابهام دارد و بعید است اساساً اجرایی بشود.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/17589" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حال حاضر تندروها هم در ایران و هم در اسرائیل با این توافق مخالف هستند.
با این تفاوت که در ایران میانه روها با این توافق همراه هستند اما در اسرائیل حتی میانه روها هم با این توافق سر ستیز دارند.
نتیجه:
دست نتانیاهو برای ادامه حملات در لبنان باز باز است و حتی می توان گفت که اساساً چاره ای به جز این نیز ندارد چرا که هم تندروها و هم میانه روها خواهان ادامه جنگ با حزب الله هستند.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17588" target="_blank">📅 12:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع ایالات متحده نیست و ما کشوری مستقل و دارای حاکمیت هستیم! ما شریک این توافق نیستیم که امنیت ما را تضمین نمی‌کند و به هیچ وجه ما را ملزم نمی‌سازد.  نباید در هیچ چیزی کمتر از انحلال…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17587" target="_blank">📅 12:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تقریباً با شما موافقم، فقط اینکه از دید من آمریکا به مراتب دستاورد کمتری نسبت به اسرائیل داشت (و بهتر است بگوییم اساساً دستاوردی نداشت).</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17586" target="_blank">📅 12:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر دفاع اسرائیل:  نخست‌وزیر نتانیاهو و من سیاستی روشن را پیش می‌بریم. ارتش اسرائیل در مناطق امنیتی لبنان، سوریه و غزه باقی می‌ماند. این مناطق از ساکنان محلی پاک‌سازی می‌شوند و تمام زیرساخت‌های «تروریستی»، از جمله خانه‌ها در روستاهای تماس، نابود خواهند شد.…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17585" target="_blank">📅 12:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 از دید شما پیروز جنگ:</h4>
<ul>
<li>✓ ایران</li>
<li>✓ آمریکا</li>
<li>✓ اسرائیل</li>
<li>✓ طرف پیروزی وجود نداشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17584" target="_blank">📅 12:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده.
طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات دریایی" یعنی تثبیت دریافت هزینه برای ایران توسط آمریکا خواهد بود. این اصل در جای دیگری از متن هم تکرار شده؛ به این شکل که ایران فقط برای ۶۰ روز عبور بدون هزینه کشتی‌ها را خواهد پذیرفت.  اما پس از این ۶۰ روز، جمهوری اسلامی ایران بنا دارد با ارائه خدمات ایمنی، دریانوردی، محیط‌زیست و بیمه از عواید مالی حاصل از تردد کشتی‌های تجاری در این تنگه بهره‌مند شود.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17583" target="_blank">📅 12:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رسانه لبنانی:   امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17582" target="_blank">📅 12:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه لبنانی:
امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17581" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=VxcsVso-Vnp9yXMs-cVqfnvfsGZRk-cmzAwZUxjVlgmpx0N-N3X0XuQyVwP6_N68Ly6VReTZTd4081loFFjAssLcS4kN-bJSWCO7MFp6joR_kjicjvM8Dcts2rWCAvLeuIq83_Dms1sWynozEYfmSouAWwuGTjDHzdr0xAM_tahYinKsIT4GgEoHbFWE_HmGdRnT_eDWraSSmMUddYn556kJIIK5HTf5bgXPkrpzJh6uT8REzhtf217bHrlFP42aWFo4O1Hd2BjA6GxU9GQpoRVYXyXsWJLTqtVtf7weqUkHMONJ5xL4EdufWlXIAdINbanKnCWeLSVAd9m0QCh4QV4Y83tkh-kd0JutD8bJnz2wFbdya8KOG0tSbx0t-bGbNv-0eY2xBryNd5K-nYlreU14oAV1DL7Lcd6oDrqmPLMwcLEcUGwekz237aDGX5_9ezAe9q_3rMPT7JsdOIW-1BGVemuCK7qIS00UXEDMA5GiKCfb9lP8b2eAjNyHAHXc2qmvu-7xp931ciDzlCVw5-k43Cjhcia47rlWGQxkXTEgLSFsNUstq2t1dvxLteLP9ln8ENnSrCHzpCRNlsOqpfj0D3X_QIGIXJ4fZwrEm4dOWiv5tySk5CRqNHjU7W4zAdj5YHdvnXeZETOrFlp4TkgC_qRiBEpqzMxa7Sppcy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=VxcsVso-Vnp9yXMs-cVqfnvfsGZRk-cmzAwZUxjVlgmpx0N-N3X0XuQyVwP6_N68Ly6VReTZTd4081loFFjAssLcS4kN-bJSWCO7MFp6joR_kjicjvM8Dcts2rWCAvLeuIq83_Dms1sWynozEYfmSouAWwuGTjDHzdr0xAM_tahYinKsIT4GgEoHbFWE_HmGdRnT_eDWraSSmMUddYn556kJIIK5HTf5bgXPkrpzJh6uT8REzhtf217bHrlFP42aWFo4O1Hd2BjA6GxU9GQpoRVYXyXsWJLTqtVtf7weqUkHMONJ5xL4EdufWlXIAdINbanKnCWeLSVAd9m0QCh4QV4Y83tkh-kd0JutD8bJnz2wFbdya8KOG0tSbx0t-bGbNv-0eY2xBryNd5K-nYlreU14oAV1DL7Lcd6oDrqmPLMwcLEcUGwekz237aDGX5_9ezAe9q_3rMPT7JsdOIW-1BGVemuCK7qIS00UXEDMA5GiKCfb9lP8b2eAjNyHAHXc2qmvu-7xp931ciDzlCVw5-k43Cjhcia47rlWGQxkXTEgLSFsNUstq2t1dvxLteLP9ln8ENnSrCHzpCRNlsOqpfj0D3X_QIGIXJ4fZwrEm4dOWiv5tySk5CRqNHjU7W4zAdj5YHdvnXeZETOrFlp4TkgC_qRiBEpqzMxa7Sppcy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:  توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟  امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17580" target="_blank">📅 12:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/17579" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4giRSS75m-8RVFvARvrmsvg7Hr-bK4spzwgiMqEub-4ANFJM0ut99ddky1kQx7FpD5GawDQv25-TP0b3iiNp7amrCk9Z3ebu6WU8hbe-I7CUV_YzecpTX_3fNzvITy2HV22-a4uEzQ15NfbWANG7LRRLZXfBvefUvWVspf-8UR5L5PpVkE_fN9mC9sm5CxXIfog9r3phBJ_I5dQlFNspTEd1zx0AnG2tZG_BzTLb_PZWwYXFsThDj3R56I7EQBZBBEjaxBpHQeNP0xhf4h_QUzvFe9nKZ6re2cnbDVxjqrWgJrzUbe9nLRergP2Q55qECoLkt67-mnbYTILnk7TrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17578" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هدف حمله، علی موسی دقدوق یکی از چهره‌های کلیدی و تأثیرگذار در حزب الله و مسئول پرونده جولان بوده که کشته شده</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17577" target="_blank">📅 10:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17576" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17575" target="_blank">📅 10:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17574" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر امنیت اسرائیل، بن گوییر:  توافق ترامپ ما را به هیچ وجه ملزم نمی‌کند.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17573" target="_blank">📅 10:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تحلیل همین است.
این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.
پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17572" target="_blank">📅 09:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">- به گزارش معاریو ، بنیامین نتانیاهو، نخست وزیر اسرائیل، به دونالد ترامپ اطلاع داده است که نیروهای اسرائیلی از لبنان خارج نخواهند شد و اسرائیل خود را ملزم به رعایت بند مربوط به لبنان در تفاهم‌نامه ایالات متحده و ایران نمی‌داند.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17571" target="_blank">📅 09:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17570" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:  معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17569" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaIRQYVKvFt4YYA4NnNe9ZTMlqY-bzvSiEQiR-nfkI0u1lA5lIINV1ngMwqxK2UbFP8X-2WMsJJbe9CRvj2j56gQpCRUree2YMgD-tVFQ0Q5_LLBYDyfEjFN5BlQQQMFHQBE75x89ppE1lhNZoOPidZb4_8pw_cflBC5snVuE33w-RYTyeHy52ghi2BhJ8FhmYypncrxMpyIktPvnNDMtreBmpbMx6LV20vp1qX1x5TL24vtzjY9pU8TUeGXSWfDD8P5xLfWJlBiTpmck_2_5zL9u2F5VH9H8vMfpxfy3uENRFOeh4YQkYalqaIkfpWacclT8SC1OYeh_vgrZSyB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه:
لغو تمام تحریم های ایالات متحده و قطعنامه های سازمان ملل جزو دستورکار مذاکرات ۶۰ روزه خواهد بود</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17568" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نایب رئیس وزارت خارجه ایران: پایان فوری و دائمی جنگ و اقدامات نظامی در جبهه‌های متعدد، از جمله لبنان، باید از امشب اعلام شود|</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17567" target="_blank">📅 01:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آخرش هم گفته بچرخ تا بچرخیم!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17566" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فعلا که خبری نیست. فکر کنم آقای دکتر لانچر خودشان را فقط آماده کرده اند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17565" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ
:
معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان نفت آغاز شود! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17564" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9TeIeIHS_W1bw_OcMXOD6dv_u-pXo50MDk3xGE1u4GXm8qGa8DT8dDPebGZAD780AG0R6AEmA_4nLbxUZmTCr5hYW6q60EmwtIhImqUObsMsuAXT9aA_gvdbiIzaEleqlb8Btoy9gebnO8K8VfNywTgcBt7ixUDFn0ePJg8myDAPoGbu2XgoHY576sSG3zZRkNRStYgJuetuvPvJr2_CrmnuNKChS93BvA9iZP90ynnoADmYXEZgV4ubpxglLNrkK5Dpea55gmhjLNDx5XMahVm-ZdaMPTEKqpC8W1CvUNmO7IV9c2r649q_22IqailOeYAWc2uRbIniOEpu-Q4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام نخست وزیر پاکستان، توافقنامه پایان جنگ جمعه ۱۹ ژوئن در ژنو امضا می شود</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17563" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ
:
بعد از ترور رهبران رده اول و دوم در ایران، رهبران رده سوم فعلی منطقی‌ترین افراد در برخورد با ما هستند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17562" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17561" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: ایران در توافق پولی دریافت نخواهد کرد، اما ممکن است تحریم‌ها تسهیل شوند - WS</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17560" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17559" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش روزنامه‌نگار اسرائیلی رونن برگمن از ی‌نت:
پس از حمله ارتش اسرائیل به ضاحیه و تهدیدهای ایران مبنی بر پاسخ موشکی، به نظر می‌رسد تهران در حال بررسی به تعویق انداختن پرتاب موشک است تا به ترامپ فرصت دهد که توافق‌نامه چارچوب را امشب نهایی کند.
به عنوان بخشی از مشوق‌های این توافق، به نظر می‌رسد ترامپ در حال بررسی لغو فوری — نه تدریجی — محاصره دریایی ایران و تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17558" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کله زرد :
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17557" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17556" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باز معلوم نیست این فاکستانی ها چه غلطی کرده اند !
احتمالا دوباره نسخه ای که به ایرانی ها داده اند با نسخه ای که به آمریکایی ها داده اند متفاوت است</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17555" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این فاکستانی ها چه موجوداتی هستند که نه آمریکایی ها به آنها اعتماد دارند نه ایرانی ها!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17554" target="_blank">📅 00:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfBUsOOETeYtm1OId_whowgqwyQBP0a7dprdgmhJbEqV4x9lRtc_aFHvVGTfCBvAfZKCQoJn72roIJZKf1cNfzOeaoL4cKlUkLUVIVnOCrNijWn8rZi03kGT2pVIkGCEK36R0wbUmhE_jeTmm9wiaJB-UzEBywDKR3hv6hrDNffiT30BG7KQvjsWRewvOEq5YizuwIZZmkmfVg6fTCPIKeZ_-PSMrdws_yzg6-iIDZLBZPosDS2Li3vhonrDLXFW0a_7nv7PD8gFOqhKaYWHUke0hpHX_Kgt2G8umkZ_L6KVru4EgXyz6xC8cZmQVD_NSfNtKw10Q2hPEjugOKxwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.
دو مورد که مدنظر من است:
— همون همیشگی (حمله به اربیل)
و|یا
— سپردن کار به بچه های نقطه زن یمن
در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه باشید.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17553" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17552" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علی اکبر ولایتی:
یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17551" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ونسِ ترنس در بحبوحه تنش‌های فزاینده با ایران به کاخ سفید شتافت!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17550" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:   هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.  نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17549" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:
هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17548" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ینت اسرائیل:
دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17547" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قالیباف:   آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17546" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قالیباف:
آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17545" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17544" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمیدانم که میزنیم یا نه اما میدانم اگر بزنیم آنها هم میزنند و بد هم میزنند</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17543" target="_blank">📅 22:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خداوکیلی از دیوار هم صدا درمیاید از رییس جمهور مملکت نه!
بلند شو یک چیزی بگو مرد!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17542" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فوری | محمد مخبر، مشاور رهبر ایران: به متجاوزان درسی خواهیم داد که پشیمان شوند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17541" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 امشب:</h4>
<ul>
<li>✓ میزنیم!</li>
<li>✓ نمیزنیم!</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17540" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17539" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17538" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این مقر موساد در اربیل مثل درهای بهشت است
هیچ وقت تمام نمی شود</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17537" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقر موساد در اربیل؟!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17536" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محمدباقر ذوالقدر: لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد
پاسخ رزمندگان اسلام در پیش است. وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17535" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsTCOKKSI_mu4-eECK1KaGToQAIZ-KTbMslUw0QU60sumspAQvH1_uTVh_3o54Y3j68dSEEZfYBACATdTD6c5MC-jwE8Lq6sqTv33X8HXG0Jrxezy2BtiYg1DpxAcSbmtUHQDHDdKyamuBLAA-cLw9aXe7cLpIFsWtGYfiq1lan64kTAHiXvGvl--53mD3YlP0dyu6kfdNWpklDwlmiMEHwjn1ynBGBR8HO5zKcqMS46rRusJtvFD69RGAT52rDDQgzbv8BtUowx5CyBlUSMT77dN7LJ6AiSuY7YWmj6ActaONBsPrAyJwckhdaBe_wiYfyIG-0IyToSjRSMjhGaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17534" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">«کانال ۱۳»: ترامپ با کلمات تند از جمله برخی ناسزاها به نتانیاهو حمله کرد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17533" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17532" target="_blank">📅 20:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):
«انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.
ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17531" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اصابت موشک حزب‌الله به شهرک کریات شمونه
منابع خبری متعلق به شهرک‌نشینان اسراییلی از اصابت حداقل یک فروند موشک به شهرک کریات شمونه در شمال اسراییل خبر دادند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17530" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17529" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17528" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.  ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.  — شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17527" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.
ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.
— شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17526" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آماده‌سازی حمله گسترده ایران به اسرائیل
اینتل واچ: یگان‌های هوافضا و دریایی جمهوری اسلامی ایران در حال آماده‌سازی یک حمله گسترده به اسرائیل هستند. بر اساس این اطلاعات، فرماندهان ایرانی از یک عملیات پنج‌مرحله‌ای با روندی تشدیدشونده سخن می‌گویند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17525" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:  «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود،…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17524" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:
«حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود، مجروح یا کشته نشده بود، و نباید این روند مهم را مختل کند.
ما بسیار به توافقی نزدیک هستیم که صلح را به منطقه از جمله لبنان خواهد آورد و همه طرف‌ها باید از اقدام خودداری کنند.
نباید حملات بیشتری از سوی اسرائیل در هیچ‌کجای لبنان انجام شود، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری از جمله حزب‌الله علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد، بیایید آن را خراب نکنیم</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17523" target="_blank">📅 18:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17516" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قالیباف :
تجاوز صهیونیستها به ضاحیه بار دیگر نشان داد که آمریکا یا اراده عمل به تعهدات خود را یا توانایی آن را ندارد
با چراغ سبز نشان دادن به رژیم، نمیتوانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب، دیگر کهنه شده است.
اگر اراده و توانایی عمل به تعهدات خود را ندارید، صحبت از ادامه این مسیر به سادگی ممکن نیست.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17515" target="_blank">📅 16:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=uq9_CxRoewrJSQ2L3k0id89-njOWY5SamgDnTA_SdQt_wjy06hknnql9lrshbBIZXocczfeLKl_5ZGTm8yMDIpRlUOENYx71SzMbnRx5-dqwNZ1lXOb8VFphlC7ZJFnbrib9Ln1GCMDozXHKXa4IFt43kIKm63h9UxC4M3wFzNzrJZuWl_bnI7kQBTc6Wj8f7sdfZdepmOscXwfDnKm0OXk4tioCbYgjbgcLU-rwHW7M6dnOQeXE0_82dJq__oaRwF22dcdKd7l8KEmztBjV4G358QlkzfEEhz5c6LuKkYvL2UCuue44YO9_RIMxguk5YFWVQb1jdrdl-wiqZQCqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=uq9_CxRoewrJSQ2L3k0id89-njOWY5SamgDnTA_SdQt_wjy06hknnql9lrshbBIZXocczfeLKl_5ZGTm8yMDIpRlUOENYx71SzMbnRx5-dqwNZ1lXOb8VFphlC7ZJFnbrib9Ln1GCMDozXHKXa4IFt43kIKm63h9UxC4M3wFzNzrJZuWl_bnI7kQBTc6Wj8f7sdfZdepmOscXwfDnKm0OXk4tioCbYgjbgcLU-rwHW7M6dnOQeXE0_82dJq__oaRwF22dcdKd7l8KEmztBjV4G358QlkzfEEhz5c6LuKkYvL2UCuue44YO9_RIMxguk5YFWVQb1jdrdl-wiqZQCqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=FNqWieCaaGTCeTzjbwruEIiRbA26aYnwMSSjcf7ixqZ2gGyB65AtvcFBHeuDGqCiv4iXYoVQkZIRIpQsqzZ9LCaWx2YpJxMrDTu8gaCRGDKP7bCiMWuR79kTZTHaZzGk91gXvuHL0D57V_X6VjeAyHtAOb-d5m2I7yaTQYX-5Ldoz4M2H6sUKMlg6M7pgDsHqE8XjXDzv1P_xcfL0Z7GxU9AA1eN2MtRzX83_X0LAeS85iP38oRti9FJD-9btuq6618vX1La47ADXeSoeiq5sZzcoFXeDiZpaaUW5cPdc0nrI6kcUuLaYkzlD7qWxMg3nLenkQpl4gPmoZ-aAsdp_wVFjIFjnj28dxrGiZKSG17hne_yNvFsEGO735zJj4084m9jhkTpSbAiliuby9BKzzC36N5Fbd-uQk_SBEYc1D6IZP8Dkgrshcz6wDaKr1b7NeURsvxcmFWmCfNScsTtm-lpEsd2TorguzERzti2IqXR-a8JAbohuy-GV3r4c2_kVW6mbka5OybZxPaFcPBkCT_bwCcwEU0dzlD4DNR_sUyoG1sc_hqor98AAxB929CYaadlBv01jAWtALtMfQwv0TU6LeJcDoDU4gpdQZwgV-O4nmM2SPXsFRKqN15_xUJM6W3Iyg1rVlt14wrkwi-Igd8Ek0nyjC7PweLblrRfVWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=FNqWieCaaGTCeTzjbwruEIiRbA26aYnwMSSjcf7ixqZ2gGyB65AtvcFBHeuDGqCiv4iXYoVQkZIRIpQsqzZ9LCaWx2YpJxMrDTu8gaCRGDKP7bCiMWuR79kTZTHaZzGk91gXvuHL0D57V_X6VjeAyHtAOb-d5m2I7yaTQYX-5Ldoz4M2H6sUKMlg6M7pgDsHqE8XjXDzv1P_xcfL0Z7GxU9AA1eN2MtRzX83_X0LAeS85iP38oRti9FJD-9btuq6618vX1La47ADXeSoeiq5sZzcoFXeDiZpaaUW5cPdc0nrI6kcUuLaYkzlD7qWxMg3nLenkQpl4gPmoZ-aAsdp_wVFjIFjnj28dxrGiZKSG17hne_yNvFsEGO735zJj4084m9jhkTpSbAiliuby9BKzzC36N5Fbd-uQk_SBEYc1D6IZP8Dkgrshcz6wDaKr1b7NeURsvxcmFWmCfNScsTtm-lpEsd2TorguzERzti2IqXR-a8JAbohuy-GV3r4c2_kVW6mbka5OybZxPaFcPBkCT_bwCcwEU0dzlD4DNR_sUyoG1sc_hqor98AAxB929CYaadlBv01jAWtALtMfQwv0TU6LeJcDoDU4gpdQZwgV-O4nmM2SPXsFRKqN15_xUJM6W3Iyg1rVlt14wrkwi-Igd8Ek0nyjC7PweLblrRfVWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO9rJL77FRi2F15QBEvpkK49ei24zhmQVCoC1gIfFldG5dnSROxR1lKiNMrXU8k5HW_SDKwVyxhmFyJi-jQVhE75x08v7Vqu-Q9vaiEkyyv7aPMZ5LCXCdKocu9EWj3481vCp6RS50cpk5k8-WePAP61wySkPTVozcfOA9zbTNXPNy-FggZ8IsOAzbeBL4M8avob1iofzwx9P97udIoz6QgYypmhlIGh6JtzY1yZANQpoSQ2h1n4r9JVU2jY-_iAAmR3QEhqJ6aEfNa9QsgzvEEhjaasCn837JRVl2OmScTRP-7Q8l6H18DF44DPi4nv1Xy-z-WAKAhRdq9ULQAhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=LnyzWoyw_8TC3uh2c8-8Ow441Hmekt26Dw9hdlSjDP5XttAjvGc3ftfXZTC9wtToLmpa1GQJa4FbekKfd5LzITz-mtezk4Q32O5iVQtWvxn7ykSLOc3n7v2Y3yY035_pr2k0ZDi5XvTC09764qs-SEd33bZGhW3iM3omKJwEdnsJJdHkChhhB3b-wCB4PWZCldO2Uju8HjxWcVXvGz9P4EQnkCLgsZb5ULOOFUd-8dwJJXD2CeTMmfYuCWu7rcbi4gnqQWEC2OE2uzHPuxGeZZCIxMTbL5A3-XPU3_kGihn34BT3mQtSkfJOPBGH2F5pWzSguXyndNnHW2hVCmingQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=LnyzWoyw_8TC3uh2c8-8Ow441Hmekt26Dw9hdlSjDP5XttAjvGc3ftfXZTC9wtToLmpa1GQJa4FbekKfd5LzITz-mtezk4Q32O5iVQtWvxn7ykSLOc3n7v2Y3yY035_pr2k0ZDi5XvTC09764qs-SEd33bZGhW3iM3omKJwEdnsJJdHkChhhB3b-wCB4PWZCldO2Uju8HjxWcVXvGz9P4EQnkCLgsZb5ULOOFUd-8dwJJXD2CeTMmfYuCWu7rcbi4gnqQWEC2OE2uzHPuxGeZZCIxMTbL5A3-XPU3_kGihn34BT3mQtSkfJOPBGH2F5pWzSguXyndNnHW2hVCmingQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7-J1hVzgMuAPAVR-SxbtYjrAk_F6owfR1qpwqAciamKeI8hDBqy0ShpuZ7Bmq-mZWHSo63e_rvE32NbiHBXVdWW8HaG5zLPd7gjcKxjMCI5FG4Ei7lnwzCSo1THL-lbSer8zAkeFqd4CLT-e7-HSnnrMLdZMWeOtPDwYMAUGK77I1S6kJRTqC1CkfDXiP_5rJD0uJPtoF-5deuUneqM58mxflG6404OkKtLjw0QUflQEWXf0SMLkuUb6t_Vcm6Sa_-EvMz_yK-A808oTWP4CXrJ-m3rg-4ix7zWRTNfsaixHT7kXFdqZhaGeC6dvR5KJa3dPfuuluY1akXVybmOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRdR0Q7zxBRnkS-u7U0da2xo8jjDAGARtM5HRx2hAEh1Uc5gRuTkcsFS1A_lK8gx2m7tMMxbxWkcI6GkvX6ajGnoSwSOZ1Nyp0P91jUQL8O0cnATuPD_NcdVVc3f9Cclw1oJ944Ud0vO5AUok5S8OzdT59PW8mZ87j2eQLGEk_gde1gW0kiUZr3D4mz_DP98EU_DJapDG_XYRS8DSXczpW9xavyF_G1ZI_tOe7GB7J4e_KBoZuL0zuBVWm2Yc4i0smt07LKkKSiNl8h4ytVU-47oDO8cmSQ-Ytok39rZGkh6uYhwuwoRd8tr81Ar-m8Lyfke_AQH_3Hv1lp4o6QMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
