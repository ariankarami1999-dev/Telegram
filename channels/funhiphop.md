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
<img src="https://cdn4.telesco.pe/file/L1tuLJfKpBwQjBwoQnAMDs_Wd_VONntmzu6aevS7cJv6M63wei3bkc5c0ObUFAQXSiHLDdxic2FzfTre-8-IZoOZBm5-h2cc33Dt0rVSAOros2HXUGHztN4GPhKhtEXkyW9s45OMBSabU87bC7YC6SP6nQ3PcnpbDdgQR5YccQVo35jc1Em-OGrGDLD7sYbRJft_hFsd0RNFKpdDRVb6YBPUWHZXRRKB2btinXRhKi3G1faYRK4F7DODSa1JL_Ho7uLULOEPivnow9GBHzY3Lhof2JDSDYxtKKX7HVNIlBlbkyR5luaDd9HzFfmiMSHs2UH8i8sLSS9slefJTKQjqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 194K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 04:27:25</div>
<hr>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO2wEec55I8UuKX7nO5iJYnbrwm1D-G2MvRmihbbaQMAFbDR-yPsoYEB3sbZVD6Wx0q3FGBfcS2mRtCBThExZqAMQuxYretCrJxmgKuQ66M_b3gQOmY-Zizzchz__uBR02WPpzonWhrDad8YZqyY3BaiLOOzvrTqj_47jQmWzUlcEWxwzfG6UVmQBAINvWwnoI0KVsP1VPPCPX2YNA4OxdU6DoAJ2FetosikvSsncEi5Qlarhi7k6gzxPswR7ViG_6ON7LzcWroLqDpWBamfh6eUwAgsQ2oILrk6wckySIwWfxu3kEEO1bk7Mooj3Vtec8FEzmzjxJDOZxw3g0RfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUWCrjs3BqwvEsNEYmlnwG7lXybbzyBp-WGUwnpac1pt8a9MQHuc5mmzB4L4uuJ6C0rikl89ed0qSBw651Oi0s_yslrqe8BZxAxNcSNwKjg62zqmbmE5Snyx685cYlTcxTNUl1L_gvJGy4i1hZBDpRRWEP2zyeqhZLU8s15sf7So_qtPAi2MXX9oeukw5GYBlbeM3caqutlM8_Y8Nw0sUAAofaL93J5VKCe2Id5v-uSnjdyAjPL41WlwktXcnqpvt-eAs421uS8KUCnUqwlaUrT7-XiqIJg7dlfMZ4bu6yy4LMnFJNjWdsroencK75iNJN7BMHh-EFhjYbZm8uJMHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متاسفانه فینال و رده‌بندی رسید به این دوتا کون بچه، فغانی هم کلا به دنیای داوری گودبای داد قراره کارشناسیو ادامه بده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/80556" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/80555" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنگه رو وا نکرده پس فرستاد</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/80554" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی رفت مذاکره</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/80553" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/80552" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا: ایران کنترل تنگه هرمز رو در اختیار نداره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/80551" target="_blank">📅 02:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186980592e.mp4?token=X8YVgXPOyYMwr2iIvBtUUrNwIP5F3cXK7skopJFxmyIaMe7Z3nP-1SKJAvrAxLMpfq6xLoym-Pb0tLTbbjrYOVKcOssO_10UPbDmjwNxRTXAYVer6SrsbcHcx2jUt_5CNsvLM3FRzCOSa8LiwZXTA35qzC5VaDCuW4tgS3j0GP7kx406IjuI2NveSZwsGbC2AYsMfFxvz-ZohD-SCOacBVaJlQCJw1OH9p3xqyhKXQzka3Xo8oSp381IQSYOFD2pVbTxN_f7ECl1scaZlfs5AaL_qiWZ2Z65xT5D48Ov6mgvVC0NS6M4jve_ndC8NND9xVc36hni7Gisrkk5VxmtAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186980592e.mp4?token=X8YVgXPOyYMwr2iIvBtUUrNwIP5F3cXK7skopJFxmyIaMe7Z3nP-1SKJAvrAxLMpfq6xLoym-Pb0tLTbbjrYOVKcOssO_10UPbDmjwNxRTXAYVer6SrsbcHcx2jUt_5CNsvLM3FRzCOSa8LiwZXTA35qzC5VaDCuW4tgS3j0GP7kx406IjuI2NveSZwsGbC2AYsMfFxvz-ZohD-SCOacBVaJlQCJw1OH9p3xqyhKXQzka3Xo8oSp381IQSYOFD2pVbTxN_f7ECl1scaZlfs5AaL_qiWZ2Z65xT5D48Ov6mgvVC0NS6M4jve_ndC8NND9xVc36hni7Gisrkk5VxmtAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات سپاه به کویت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/80550" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگه نتتون ضعیف شده وی پی ان عوض کنید توهمیا، فعلا خبری از قطعی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/80549" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/80548" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/80547" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به لرستان هم حمله شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/80546" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/80544" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80543" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سازمان ملل بخاطر اتفاقات عادی خاورمیانه ناراحت شد و گفت تا اطلاع ثانوی قهرم بای.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80542" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">راستی تا وصلیم بگم کیرم تو نت بلاکس، از این اسم دیگه متنفرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80541" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حقیقتا میترسوم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80540" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آمریکا یکی از نفتکش های ایرانو با هلی برن توقیف کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80539" target="_blank">📅 01:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80538" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80537" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سجاد پسر تا نتارو قطع نکردن پول ویناکو بزن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80536" target="_blank">📅 00:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خطرناک تر از ناو آن جنگیست که اینترنت ها را قطع نمیکنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80535" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بابک زنجانی میخواد بمب اتمایی که از پاکستان خریده رو کنه.
بابک زنجانی: تا غافلگیری دشمنان چیزی مونده، صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80534" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80533" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80532" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قرار بود زمستان سخت اروپا شروع بشه ولی تابستان کیری خاورمیانه شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80531" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یادش بخیر ی زمان چند نفر بودن میخواستن با ی سطل آب آمریکا و اسرائیلو نابود کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80529" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خط راه آهن بندر عباس مورد اصابت سنگین قرار گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80528" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه پل تو بندر عباس زدن که یکی از مسیرهای مهم ترانزیتی و لجستیکی جنوب کشور بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80527" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این عاقبت 47 سال مرگ بر آمریکا گفتن و ایدئولوژی خودتونه، بیخود گردن ما نندازید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80526" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آمریکا هیچ غلطی نمیتونه بکنه ولی همه غلطارم اون داره میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80525" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب سی میلیون جانفدا، الان وقتشه، برید جنوب از کشور دفاع کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80524" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80523" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فرودگاه ایرانشهر بلوچستان هم زدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80522" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جنوب رو بازم دارن میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80521" target="_blank">📅 23:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از اونجایی که دیشب تهرانو زدن، الان تو جنگیم یا آتش بسه همچنان؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80520" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raYOxM4nlctabvYEJNXC4Z-wDhdiYY8vRICf1mE6LuFPVNODe60h3yMAVYhWPb8HDqia5fmft2yyB8s-C9UsB_m07Dt5bCnVhpNBVTjmOf_5CfDhoBlsZamyVXcT_Jdy_osFK73YOviRXE-1_MGzDYUQM_1uZZOmJq1bjz6_B1l3JBDooZACjJJgKZfyU2TMw9_jkjh7lblFgrrLGEj8Jee0cesDhiRlC5gbnOlmXiInPrnd2sdaf5bfZdwE1Y22hUkQeaqxzJCNwpENQSrGjo8i5XCOfq-TrIimlZvMjHL6Dxyzeeg0iDoVTyU0nkTE3Kk3JjhbrUrbGLCMZBlk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80519" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اهواز
@FunHipHop
| Rea</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80518" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با اعلام سنتکام دور جدید حملات علیه ایران شروع شد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80517" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izIpDhQ3PyLVqYWWsCUC07Xiha0Ivm5jjOX6LFS_FnLDISnA-YXfX_idkh7codpXrSZN_it0hqoEoJsKkdxqlF-Az-W9Gzw_tfxeJJRcgn0ECwbPlDIWSgHjFNffW_kLeKwLho4sCgA6XIIG11XdfCUW3WKuZfOZFfUqS5bdo21fMaBAQcm_1VmiGRY2WCHR-uf1MUENSoVqO4wEZXggMk8ejT6qygEiOHWcBVhzysoSsT1FgjGr9Hb9aU8F3pOP5HfflfWaPLsDcYiDvP7QVZA1GGnmbn7DS87bMQgirrmSBKlU8XQxpPp7y6BziGvxUaR-cmFLH-DcD_ZG25vV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام کارام هیته منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80516" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">همان همیشگی (انفجار در بندرعباس)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80514" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=qYEAg5wtPOOcn7xgeqkNVBAHOqli-Ny5NBe6AbDemxklCH9OEskx56rQswekIOwpgbmsMAatqMeBVzBARJD7YbUBpyZpxR5d516Od-rsr6olTMNILN4XbTaWyY52JDt3SMyyFImrJ9VhkWQZdwVi11vcE2zFYj2HmYqYvACFvPdPLxZBeTK9AdvI22JXII882CxXpmjuBFR4EFUNXil6mhxWJBSS5jgZ3_UNS5AHvpPId_oNh31br0ib0R2LVtMhXYIghX41erag4_fTeb0bLfWnuUVn2nMgG5iF_ZfSVoqyP_6tlNnxbNy2470iqD767q4xSQrQpBet0SJRvtxp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=qYEAg5wtPOOcn7xgeqkNVBAHOqli-Ny5NBe6AbDemxklCH9OEskx56rQswekIOwpgbmsMAatqMeBVzBARJD7YbUBpyZpxR5d516Od-rsr6olTMNILN4XbTaWyY52JDt3SMyyFImrJ9VhkWQZdwVi11vcE2zFYj2HmYqYvACFvPdPLxZBeTK9AdvI22JXII882CxXpmjuBFR4EFUNXil6mhxWJBSS5jgZ3_UNS5AHvpPId_oNh31br0ib0R2LVtMhXYIghX41erag4_fTeb0bLfWnuUVn2nMgG5iF_ZfSVoqyP_6tlNnxbNy2470iqD767q4xSQrQpBet0SJRvtxp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80513" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2obLFr4HF28HT8ZNEWnP9rG8qUIhWFVwUEN7n0kkzByKDMiHyOpmUzWi4tZnG6RpbF9v5UnLmonhu3nlYR1doZU5uDuqvA2TYIrneUQOx_RPhMBiYzbHymUf2hs6oMQdsvi6OpBcVpFBnIJ8orhkdNeAH5VLjrjxOrgNoo3Oi0iEJWthFZ91mmjxhw1x86XpEAfcC3Ws16ROR0eHGgK0hbmuxa7VJH6VMw_E-8GMEtwmuxctuSj0SResSbWPQaIiCwshR7oMK2OLqRuFYPslv_yY6FnXQHuiuYELTSzdlLrH4bexnpjbd21KSh88Fxs8b57Uo0jnXf8ZmnA6R6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g25
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80512" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طرح استیضاح وزیر آموزش و پرورش رو یه نماینده ثبت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80511" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwvKTiizF6wB7p8JbEAZvy-faK6TZYqe-6-XRI6YhIgi1fTTpCG6SUKR2kul1uHFMKJPJ6bDkrwt5Plh6vkASZzvCJPrdXSLdxL_3FJQNlTKibljsyppZ1NTIsupb0uwjjK5lw1Kv_0yDh0Ixegqo0s3U074UdCuzu1ZzMjifrVsVz55s_dbliiVC72z_3tCTomJ452U8TkXX0-tBBQNgX3uWRub42gdqsf3ZqUjOejy2_npF_dBVf0ky-ZnWuIeYQ3GGRk7zVsGqOadA8Kgdvl8OuvUG7b69V-ACjlmJAr05N0W_6RAFPav6vIVtmWXcaXmcfAXz7045Kkzp8vb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل برد آرژانتین:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80510" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=rn0EbGE6fzouV1Jy6uiR66X3Ger0Dcd_ZTY3Erov_FMr8tzTF9GUZhosNUstoc2utUYMUBFnIJ6j-bhot78AiwwcrdtgrQ7O07rSztGTruPAjtQh_ZwrU34BCrFWL7qaBSabjN1EUmcDZ0ONIm6-YyWWF9huWHkRBybuyN32_XnwOUsV2uD8ZVbb_LYkSRU7z5Kq2KZ_YqRodzNckwVk4_3b81KxxbA3FyfeMKfsuWg4Y9c3N6z6jBTzphQY8Ioxt5aYzMCjGylrYTI7oA8OBQJqZFSEMQRtxvmIsRLnC_eHVZBoA9Q608gTHmi10EOl2X0SNXNYfzKG7dyMQxKD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=rn0EbGE6fzouV1Jy6uiR66X3Ger0Dcd_ZTY3Erov_FMr8tzTF9GUZhosNUstoc2utUYMUBFnIJ6j-bhot78AiwwcrdtgrQ7O07rSztGTruPAjtQh_ZwrU34BCrFWL7qaBSabjN1EUmcDZ0ONIm6-YyWWF9huWHkRBybuyN32_XnwOUsV2uD8ZVbb_LYkSRU7z5Kq2KZ_YqRodzNckwVk4_3b81KxxbA3FyfeMKfsuWg4Y9c3N6z6jBTzphQY8Ioxt5aYzMCjGylrYTI7oA8OBQJqZFSEMQRtxvmIsRLnC_eHVZBoA9Q608gTHmi10EOl2X0SNXNYfzKG7dyMQxKD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستار هدایت خواه نماینده مجلس، که توی تجمات شبانه کلاه خودشو در آورد گ گفت هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80509" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلام همون همیشگی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80508" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ویلسون دیشب عرق لندنی خورده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80507" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=Oio2oTG9VWwju00HNePY4PRhcjqD7e4Nqp82g5gVei6FCSVoWq2BzkiAPS6owYGXbyLinc-R9vxhGSc4f0-HzG-6D4ZWV_xgSk6DgxJg_fbXVwGeQBoUXY9GwSz8AJ7t6KOqV-aXgrlrjJKR6JwADXh-Y4iTOgJ4gVCb_4DjOT11OUeqWOTtmjBI_kOiOEF-O06JHAywOJ90lVspxBg6_U7LlwuQzTshS_Gg0_s1aVJYczOQvmcws9hdhW6p-Z8At0n-wcdF47WB_F8Ep8WBImaR8XbA41G_kqZDXgX4ab3ZsMmijMpe3twFOOtMHkB9LRloAIl2YsWZUjzJqlsXFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=Oio2oTG9VWwju00HNePY4PRhcjqD7e4Nqp82g5gVei6FCSVoWq2BzkiAPS6owYGXbyLinc-R9vxhGSc4f0-HzG-6D4ZWV_xgSk6DgxJg_fbXVwGeQBoUXY9GwSz8AJ7t6KOqV-aXgrlrjJKR6JwADXh-Y4iTOgJ4gVCb_4DjOT11OUeqWOTtmjBI_kOiOEF-O06JHAywOJ90lVspxBg6_U7LlwuQzTshS_Gg0_s1aVJYczOQvmcws9hdhW6p-Z8At0n-wcdF47WB_F8Ep8WBImaR8XbA41G_kqZDXgX4ab3ZsMmijMpe3twFOOtMHkB9LRloAIl2YsWZUjzJqlsXFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80506" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80505" target="_blank">📅 15:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ی زمانی غزه و لبنان و سوریه رو سر اینکه بی در و پیکرن و هر شب بهشون حمله میشد مسخره میکردیم و در مقابل کلی منت میذاشتن که عوضش امنیت داریم، اینم از امنیتتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80504" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نت شمام ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80503" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عجب امتحان بخوانیم و بنویسیم سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80502" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">لطفا فحش های جدید بکار ببرید
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80501" target="_blank">📅 12:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l27XI5Fhc7BQpG85NQBVSUSSHtFfz_oZqKwMhIHsIfgvdcRtab9UmmxrLaLqD7OLAtXgSwtSBNvrptfsEcVFwD0Z5aGso3g5mQNg0K-MiA5VBVyroqdW6AXCHdS_TZw6jn3ok9Y2dDbWBXHJ1Mcvpy56HCEyj3cSJ709agwFAmBP18yjcWY-IPH1c9pprIstPM1IVw-xwmMsUPAbbEvB5krEWnxYqwkOlaoqvWo8zI9xnokw5NSUP3AoLq-mhmdyr-QcPfVR-Aw1H-hMOjLf7zF7oLePD5rRXaQvGtw_RdSf_AjoQ2ocHVTosUc69CrLZLZbV6XT3Fso28vixPJkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم پول ویناکو ندی بدبختت میکنه خوددانی  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80500" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aturcY6dj1GYP434JQQfkF4smz00vO5yKYrgCR4MrSHvRa36asbd2SP-ZngDP_8ol5wev75D901FULBnucyoUbhggtxr81565nopiyNcLKtrhOXgkqvxefy8zBMN-hz7TCBeRN0DgL_QtEIRypfr87XSYkywMKIGxbpS4IKDxkoArOsCmjyv9awZf3Vf1GohmqoCwNNWezDUvlkJ5yKe71dNAbhZNYvmNg-JbfwElEja49j6V5FE8laGsbUVy6wcaTDL_wfoiXotFpkIoOjbyhnH2tewX8jcugClHO3whXyHl0C_tVbVxDprnNYOKgTPdlbVLFlitq3ou2SIzlWGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80499" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتکشم زدن تازه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80496" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsIJKyz3mkOEDfKdlFcAwlmJXiMbXfgcgFI9MR1s8J_ss2lQ0mcoOQglMX0PmcpPJjWJE00BouD7Z2PmMBLxubHZF_qtuu0QXGtPJPVpEcRvnuqBJ-KDLRClFp66YnzfdKirZWAGH3u2PelXgXYwUvfNKyTykQgudnNpyPC9oLx4B_bVOLI3cF8-GwXSE86vVH3aJgdg4yBPAumD6R9rCbSuY2UesuUQa_z8gtqg1JPpdXIaIKVzz1F7-Fe81yLMfBzpV0qXXBJP7uaVkcchuS0liEWkNwslLi0EVlebAXLIKVPXkaDm2DK8kNT4dfbzdWGbIUdZSFFDQ8anFflH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بخدا بلینگام بدبخت داشت خطایی که انزو روش انجام داده رو تعریف میکرد، گاییدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80495" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فکر کن خاورمیانه چقدر پیشرفت کرده که دیگه تا خودت صدای انفجار رو نشنوی حال نمیده و هنوز جنگ حساب نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80494" target="_blank">📅 04:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBGgktB1jphPOZKffhjOHVygkvnWmXwdGZvIwI-5Y33_uWz8l3TBcADqFH8CHUmdzCfxP0CLKtJNq_TjX-petXNFJR0gl5Oi0SR-RawgwLj6OWJzdk5qiiKClJ9Mj4Q8QoyNA66tdXXdMrfB9LvSvxLmEGtN-9t4VvaNsExRGKpfpNFYcAKDdy42dDoj0aZRxoYpwdexvm9gtaBv3rFmwTtp-ZaCJ2vNUvsEcwOxlmrOBpwNDtmma6M9cvOh2tOuc-BjddFWyoByBA_VjCfOYXX_-B6nnWCqcOxA3ulmm6TxARoBhXzsdkg2qEAmiBDrT1iGyJPBB1oZG2HMkyD9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1bM2zS5CPYmKz04UpTpJdGhtRBgqoy8bCG2-7Cs7jWoR8BmpzvEXX4XFIqOhMW7Z8RWaknWVnk2AKSX3qsfNxvUBGXHLbdDPreiRC45xIjdcMVPZaLfJvCUwwwOSYsH7JRfck1YWYgu32B9aggiqG3FOqcTOQsKgBEaejLQ4zsCEoafAyGKLiP1zQqcZAxe0OJdylALGUS7MPkk8L_Oo2DIRjr2vMmc0Q3JhL1Br8DqQmMpDzvDUTeuLi0IUtoPrmcOUS5W8ZGQWLFVigPX2-rboZov4PoyYMXPb8nYejQI8Kp0h-y_broY0U69-BtwxvC1MvV8v6Zx0hWNtFgxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtW06ic6xSjrjmN20CfHwT2o7XeIDjoc3CnVTeLL2tbibNBFJt7UQ_gjjVwYIFZ_wn-VEckwjJjY6cBkcjO0s7w76Ro7rufZmWhK0ISYrKin266cqbfinVhwx0nwV52bOWbdPTt-01qPEx6_nE2y0EZhX1JSRDmPnN-2Hqa5b1H6rIr_MxUwaR0kHcN_U0uYXEYIn2-XzF9gWdvbfVto6kW7nABYHKPW3Oc8gNNjekxq5QSBoe10a355Dx5Un1CysCEIxHLGg2bF57M0gDAjLw74FhYpSbAdhcUbDfx_QczSYMYRPQIxiuwUeuA8sJFyckUrX3I-3-hL2Y6jUuqtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLeuCN5-xJijm01ix4NTdsLJn-Rmup9DeE0P_9HhSMDek90CskKatRSg5PkukGdcXle_g5cPY0pbwzlrlSkfxLnyJk2TYOA9w7dJhzDM-0v9wIEbny0FG1-ltKQnzIml_f_gHYUEoOF4g3AAGZpG9M2fqHUYrrwM9ZlxplTMCUkHspde-2iuP6l8dqu5IhIdurDVmePIUjushcupObwO4gabwMeeXPCr4nVJiqryM4jakGbKJtWLUUOEQBNanEUA-tS0E4fwz0UiMm5ywOb9dXAa1PO2q5izxRbKbeUDHwlATldDoQZtKbHuaLsH_KtEUKOj3N6kImj4wmYm0Qf0Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یا عباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80476" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNZ-3ub2TWGHuH4b2Ir_dRsTKVJG0LrGKNiqtcxfNOI2u1ukNRDcP0UD3eVTrnTjmuqfqzXSRtOfMj6cOy53GRtCgfZ-ONuWEKvCVvozLCXT90MCdLvgOPPCq1Gg4k5zUV4PzMgaumqN9qWKSztPAG8F6RmFXh659pCdRnKg-VsYaGmifwIkRZG7ax-86w96YI3Qd1U9KWNsx7cT8I1h6V8A8NPmVcOkyeFRoDmBfW09HBEPPS1sJvONrTPu823Q6wZFasQ2rl-9phNAxJVBiQ7Ayy_EWX6N-hAXDMNwrpUFuETni7MAlE56dScDP2pckvqIssCM0pb8sgxcrd_6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزا جان ببخشید
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80474" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رونالدو فنای عزیز صحبت کوتاهی دارم،
جدای از اینکه جام رو یا یامال میبره بالای سرش یا مسی
باید خدمتتون عرض کنم که مسی اقای گل و پاس گل جام جهانی میشه و توپ طلای بعدی رو بهش میدن.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80473" target="_blank">📅 00:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ساکت شید شبهه علی دایی نواخته
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80472" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromvahid</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrsjAoihpwqIClSTNZ_YF1VU_rhGHY3irf18JIxylXUTyz8Spl-XZ3cz_xp6s5Z-NyIYvB3BEHRKLPQ60CTzX6Wada_SgiCRLO2PTH8lRgBFNMX-d_YC17xSUaQjaWOZqN7fwXHDQJ0PkFdGkeCCZi3M6q99gp5MDWUi8iqWlv-a5xnAs2V7hQN9hFMxcEtPXDK1xeN53t-VHnpr07JdsJlFbXjUOfjsUTGUpBzXGbkBCA49tEsXBl4NA35JQoTjC1zsXnTvysEq9q0gfLbgbtgpBr2n2Zid70kPbosG7zIjFCGAkC4gpYs0vfFzV0VSnCjc4uLPaYeXoSeqp0Rq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم ی سری جذاب و خوش چهره ، جلوی این گوژپشت اوتیستیک کم اوردن
😔</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80471" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تا ۲۰۱۸ رونالدو رقیب اصلی مسی بود
از ۲۰۱۸ تا ۲۰۲۵ امباپه
از ۲۰۲۶ به اینور هم یامال
تو دیگه کی هستی پروردگار فوتبال
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80470" target="_blank">📅 00:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان بخدا کلیدی ترین بازیکن اسپانیا رودریه، چرا انقدر عکس یامالی که تعداد خطاهایی که برای اسپانیا تو جام جهانی گرفته از گل و پاس گلاش بیشتره رو میزارید رو پوسترا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80459" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صداسیما: شدت انفجار ها در اهواز بالاست، در خانه ها بمانید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80458" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سجاد شاهی ویناک گفت پولو ازت بگیریم بدیم بهش واقعیت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80457" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انگلیس عزیز تو امشب به صورت استثنا فوتبالو از دست آرژانتین نجات بده ما فینال از اسپانیا درخواست میکنیم مجددا فوتبالو از دست شما نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80456" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3oz5pXvNuEslMvSyUmiX_IOF_h2SbhDWVVM-zQlBOa7QnqTdA6xLeWBn-xTtuPWPe5ot7VrjSambND4vpzl6vHhFstO1n1qVt6nBQmfklZ61RmBBly_XG_TiGBnQdUleBhAw7MGprR6Ttr0_-DkVBuuxdg8vlUqzJz-0O3Vw-Whf6-hgCBQP_ScRpAibYBNohJwXqoV_IqO_KPR1FmWiuXFCMCu_Re6StG20zuVvkF-PkMVhVB2YwDH_GdFJXbv9wQd7tFaAeqp7UBbCyOzyeHHcC5CTtw4LS8ElrPObPjkJGrYvvy9wmzsti6PAie1HViYiV1xB3hqMSwyvu5FyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام سلطان رو بگیر پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80455" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حالا از دکل کی میخوای بالا بری رئالی
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80454" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کوکوریا دکل بعدیه فک کنم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80453" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فینال بین بارساییاس محض اطلاع</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80452" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تموم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80450" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این مصدوم شدن بازیکنای تیمای بزرگ مشکوکه
رونالدو فنا پیگیری کنین بیکار نشینید
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80447" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاهی ویناک پولو نگرفت بزن برا من</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80446" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80445">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توپ طلا نهمو بیارید بابا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80445" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80444" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وای وای</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80443" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80442" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دومییییییی</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80441" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اکثر تیمای بزرگ مصدوم دادن حذف شدن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80440" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔥
تکل موفق از جود بلینگام</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80439" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYitIyq9SnDWL3ZoJuKAap1re3WcBSHhO4EWHnuO3srYNeidVnJP_n4ZlsPWsQOjPpNN6oqNYpFm-EDawC4qq_OGq6o5_nAtQur6-OXNHS4A6Dq6z9sXVVAiCWJFlEI-N1g8jKs7-dW_1yrII8mjPC9Sh5YmHWn6IKJAzAIiXCKXRhfOYy1XlsO1vQeF82OW81cNSD2-jXY_IFiwKcluHpCCOaYHODwg2N9SeJNngOQ-alOJjHh2bdY7Ix64oWSGO2loaYi7zbgRyOdcYsrHhnPDUNAH27jwXdLA72rNOmcFh9-7vb6wTo0qyAQu6zlRuPcIbYhMhv2EsUK_o07FPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مسجد برکت میام برات بمالم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80438" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80437">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خدایا کیرتم</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80437" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آرژانتین زد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80436" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80435" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80434" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
