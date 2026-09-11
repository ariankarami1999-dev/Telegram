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
<img src="https://cdn4.telesco.pe/file/L1wWB6kRB8LxsPNPvgswWKQVNorwrj6LNIs_dDMiGIG2dnmUSNHFj2gu2A-wMCgzY8M7A1Cs1uyQSFfiML8scUlTCakhdAjgW5d8qf0sVFrzElwYW5FaTeouzW1kzOW3x-G_rFqghye8J-iZIQ0CFK4xQN5GQ85RZ2Hi2UF53IiqlqsfhxZ37npqAtZgC06A9fwAlisq8UJ1rU5HuXytzdUFaeLcjKBnPJP3aBahXtKbcUTJ9_mkTgocH7QEe0T3Dds168KLIG5evINjPj0I7pVPtNYaCW3o3QcHufZ4WMGU4jGc_x3lr3yPWaET5JaHzi2-lLFLpKEY8Zc8sMD8mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 00:57:33</div>
<hr>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/naya_foriraq/90236" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/naya_foriraq/90235" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/naya_foriraq/90234" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmSH1OzhGbPvZcju5Q_ZP_y6s7hZLQoSHNdl9PASsNXwyzNTrSDBzU7Xs924YrS67qQ1QO7W-zHkykS04n7fnvyMt_O9n__bsIPdy4Ni2zDEE2OvYA8j8cIBJHZUqnFlSBxXiP78SR3bcQWXFUwbfo2l1SvSpXv4plShcEPh8Af0cXXp9PVp5zUpJHrXY29ctF2hOlavfvGZw4sc16sVBkvVglqnjEOKhFUtTiX6nLRnXsWhhrn00laAFFZUEIUhxvvUDzm5ceFRhBbONgLtPmT280LYe5tOBOuUtoLosmfwbGhmSu4nGmnZUYwz14rguhILED7JXQz6-KkXAgSi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇶
🇮🇷
🇺🇸
🇸🇦
بريت اركسون : إن تعرض خط أنابيب الشرق والغرب لهجوم من قبل الميليشيات العراقية يجب أن يعطي الجميع استنتاجاً واضحاً للغاية: إذا استطاعوا ضرب جوهرة التاج السعودي... فلا شك على الإطلاق في أن إيران قادرة على ضرب أي بنية تحتية تريدها في أي لحظة.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/90233" target="_blank">📅 00:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي: نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/90232" target="_blank">📅 00:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي:
نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/naya_foriraq/90231" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🏴
قطعاً بینی سعودی‌ها به خاک مالیده خواهد شد.
@Naya_Press</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/90229" target="_blank">📅 00:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6MvwFrT9CMcVD91ZFjw_Njrvm4KxUHjVB_qq8fKaLDyXq-j3HLePTl0diIPRnzxH2LfHJEW5GLDqLfO7kGgSAkHMmF4nnYsjBDLIq2PZj47_bpP3mJeTOqD52OlKhbmaVUShLMvES1PtOb4IL2Lypb2V1YJpVhAym31Xt4IHkBd5GbkjcTDYqf7PlV0uY9TXkMgreU47wBfmWX4fjQMr328rLbuxLB7c_bGSHbiRZOPOnmkXDhYEebKcegvqplEkl3JDZDytgsOahayz_TAqVoZ2dMbq-4y49NlUa9Ir3cVXNco3ic-SesJL232YG7XFi0r6DGyGnPPY4jvewy9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية رسميا تدعي تعرضها لهجوم بطائرات مسيرة اطلقت من العراق.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90228" target="_blank">📅 00:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇰🇵
أطلقت جمهورية كوريا الشعبية صاروخًا باليستيًا لجهة مجهولة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/90227" target="_blank">📅 00:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
هروب عناصر المليشيات الموالية للسعودية من ثكناتهم العسكرية وترك خلفهم كبسة بالدجاج من دون ان يأكلوها
😫</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90226" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/90225" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jip1hB-3r3jyC1vEwTcUP6o0F4CPmABha6vk1sYppMzPcNAMe3PCgpVporpu4KnQCnsEehNOwojx09aCEwrfOZWUHEzH0jZLRmoYZOWbOVhikHy6nN1XgOb97Cu4PIJ9tcq3JKKFSovNTsf4SBhJOGRHL6Hl0vAFXE15BOVteHfPtWmCONiV-MynbbuSfv12PAfnLtlA2a_ucJoM-ztRbPwUYKUXYMyRwj7yQm-WVPTtpOAGl3l4uVWOCcEalL8DexFKK_UJ5KC7xLuFXdNAw6m-kQeJx2lG2ND33s0kngQPi7LLGc0OJFe4L7C7uSvmVmdWPU9qO2Rr-K3b1neR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90224" target="_blank">📅 23:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇷🇺
بوتين
: أوروبا تدفع دولها نحو الحرب مع روسيا. روسيا لا تشكل تهديدًا، وليس لديها أي نية لتهديد الدول الأوروبية.تم حل كل شيء بناءً على نتائج الحرب العالمية الثانية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/90223" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
سماع دوي انفجار قوي في تعز</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90220" target="_blank">📅 23:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90219" target="_blank">📅 22:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90218" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
🇸🇦
حرائق لا تتوقف في خط انابيب السعودية بعد الاستهدافات اليمنية الاخيرة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90217" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
محاولة دهس لمجموعة من جنود الاسرائيليين في فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90216" target="_blank">📅 21:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تعرضت حاملة الطائرات جورج واشنطن، التي تحمل حوالي 5000 بحار ، لهجوم صاروخي باليستي إيراني في نهاية الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90215" target="_blank">📅 21:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqZeLCdaCdo3Ec4IvHs8KNM1lzSNPkoSu2ORUnrZj9DWh6ZFQfWKqFrOhGDkpiQOiVfFoMxkHcCNXiNX1TDsQWSdZ4HnqIVc1E2aaAZ2xZhsQYfk6hyLcCd0nnk4S-pTy-FxyH4dmsuKRhFxaP00CL_bCcit3EOm6zHc-CT1NueHrHNTuuyDh0HErWCZKvlQOSPx1N7fqTau3BZ2wOKqp4DTyvaPWUve8IHL0RD3HbPM8qeeL-OAOBNfSOxjcQK8BnHoCTgQ6wbyF3oOMLq0e58QgRxovzGceLV0ZvsMKCSgtFLDbqeqIIJIyDkViIkmjy_NkXuOaMBLeSnSJXaCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسريب ضخم يطال وزارة التعليم السعودية
🇸🇦
أحد المخترقين يعرض على منتدى إلكتروني قاعدة بيانات تضم نحو 600 ألف سجل، مقابل 300 دولار فقط.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90214" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POSqMi3y-lQfnm43y0l_7FCl3vTDLn16oelEJkV0edtlDXl8c8_joZI4-InWKvrrlfQ2jC_sWeaMDkFP5AWp3_ksVeDTNDS7VmS22_ZKG1fh5pgBocmh1TguY_l3x3KhtKDpge5zRahSAhs8Xh6Ppx58GGp9tCKsNZiAz2tJ4kbFdAB8fYK_2Vbpds7ceHMsFcE7Cfy-BqU48H6qju4FC1GBQj8zsJ92jCPWWQo3hVKwrUMWWhfFeZ2bYs4K-d8IdwJDeA2SnVBdQzG_xJrDlvr3EifNJlfNkZW9TBFKnFQoeXhEBDWFF_J2I-vTdPZv8Wb1v6hq2TEIqBiT10Jslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي في ندوة حوارية بمعرض الكتاب الدولي: الحكم في العراق ليس شيعي والنظام باقٍ، باقٍ، باقٍ
- نجحنا بشهادة دول العالم بإقامة نظام ديمقراطي تعددي، فيه حريات وتداول سلمي للسلطة، وحضور شعبي، لكننا اخفقنا في بناء دولة مؤسسات.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90213" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
سستى مكنيد و اندوهگين مباشيد، زيرا اگر ايمان آورده باشيد شما برترى خواهيد جست
So do not weaken and do not grieve, and you will be superior if you are [true] believers.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90212" target="_blank">📅 21:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
الشعب اليمني يجتمع في ميدان السبعين،
شكرًا لله على الانتصارات التي حققها الجيش اليمني ضد المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90211" target="_blank">📅 21:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90210" target="_blank">📅 21:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
رئاسة الوزراء العراقية:
فصائل مقاومة سنجار ستباشر تسليم سلاحها إلى الدولة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90209" target="_blank">📅 21:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
رويترز
:
يدرس البيت الأبيض استخدام "قانون الإنتاج الدفاعي" لتوسيع قدرات تكرير النفط في الولايات المتحدة، وذلك في ظل ارتفاع أسعار الوقود المدفوع بالتوترات المتعلقة بإيران.
ويناقش المسؤولون تقديم دعم فيدرالي لتوسيع أو تحسين المصافي القائمة بدلاً من إنشاء مصافٍ جديدة، وهي عملية قد تستغرق سنوات وتتطلب تكاليف أعلى بكثير.
يُذكر أن مصافي التكرير الأمريكية تعمل حالياً عند مستويات تقارب طاقتها القصوى، حيث تبلغ نسبة التشغيل 98%.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90208" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGELyE-wI89b7cE9TxxEv1Hr0cNdWMJ44h-H4PhvvHUpnJfjiWhAU9ktmAWF1ZZ-Fm6UhNduYzSTAXPSa-u0y34VErwcHUP_7U8tfKIg76gqCtx7jS6cVik2MflfOAwQIdeYzrsxFKVX21Lpd9WjY4dMK4HxKVen0hNYj_8J-zNs8ntm7qp3BnAOKHQlb6uuL65U5l3hTmVEXYTsaGbftgBcMttZ7YMaZ_WFYQL7vuK7M8ekrQGq2F26KQuvNCh05jKYB4ufqawxPqnGSmaX7gcbIVocavp_5f3XmSTmqv7BwhiJucs71zPMoMcA2Tra93wulSItZtKa0RPaJtcgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
ول ستريت جورنال : استخدم إيران نماذج الذكاء الاصطناعي التي طورتها الولايات المتحدة لمحاولة استهداف سفن البحرية الأمريكية في الشرق الأوسط، وفقًا لتقرير أنثروبيك الذي يحذر من مخاطر الأمن القومي الناشئة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90207" target="_blank">📅 20:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90206" target="_blank">📅 20:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmUgL6TIVFlWPAZWbiBuPh0oCiTIg61OilUg0r9J3KHBpw7l6EY8kg3QcyYmgQT04ZrtxqOAZsCwQm3MUR0ChGku9KfycsNBhJhWG1NFhnBvwP0Nbr4GNNVc-VRYMRkDBbDQLkpM4C7gVzyt2rqYM_qzm2hKIBdPBAdh-S0sUcCncFzQGvKOmZKjlkMcd5p3JutfZn7YpXAXf38OCJq25Ew0i8YL3_CQWmPYRxIm9ii4Y4CQziKQ3l0gwU2aaGnWHTA8wLghFs3Ti_rOIuSDKrSrUrR-4opt42MB1K68c7t5R9Am_FEH7AEiMcvLeUagZsrYr9MOwoGZ2q0axsoL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
عملية "والله أشدُّ بأساً وأشدُّ تنكيلاً" في الساحل الغربي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90205" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jglGmyIB_LVebKSqi13lIaCACSLUnOviuk-nw5TTUAWEYIoYLqZZmlhxeVI-gquf16OByORnagk-EKSIP19Ej0R2V1h4oyg8CKZkI5_blVXpJZGBju_BtoPb4siXyuafqZbJrRv1RxRtuR8qXPXngHPMVmiOhcQjxLb0UI6DRqwcRG1oPTEX4PWwq_kRnbc-faC5mJvoJlzYBKFhionIu2vGjCGmRqwPkc7XDafDzpOe5-07McxDyOSx3jIsU938dFUcWnwc4pR3U2DWtwdj0R80Xhnoju4qdnv1ultfcErK7r_4l2YOunEyOcHX8CvCPnvdF2aNUkq_Alxm0yvWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90204" target="_blank">📅 20:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم اعداد كبيرة من العتاد العسكري في مدينة المخا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90203" target="_blank">📅 20:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90202" target="_blank">📅 20:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇸🇦
العدو السعودي يشن غارات على مدينة ذو باب.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90201" target="_blank">📅 20:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQRGRshgQ6uPMawfTHLC2uZhAombLTSxsrdlaUUCQE217LEoo_TmmgSBUIrgI04blnCKnxuFfR9MFmjXov81BSjyeyv8kDeTouzux59WPSPUncihra61KbOuvjGcjRG53HrYfrDQqvqQUvKiyRCnSkmj_o6Tlfo8Z37mejuuPQbfyNs4IX4FlDg5QmSbZGKi2PcWlRr9NgyVzcYeC7ZMX3FiLIE-zRMxcl8TRMk0Wb3QnRMzh9w7OUK-r7UCWhO0nJnbun6nnh9bv-rgmlw1EyYGkl2vRIHUANC79j0ULagm1sgwVEMy4Yz7MHS5b1OCyNvQ4N5zJtV5iUTA-JmYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبارك لإخوتنا في أنصار الله انتصاراتهم المؤزرة، واستعادتهم مدن الساحل الغربي بالكامل، بعد هروب الميليشيات المدعومة سعوديًا وانهيار مواقعها.
ونؤكد دعمنا لحق الشعب اليمني في استعادة سيادته وبسط سلطته على كامل أراضيه، تحت قيادة زعيم اليمن ووجهه المشرق السيد عبد الملك بدر الدين الحوثي (دام عزه).
اليمن الذي أرادوا له أن يكون خنجرًا آخر في خاصرة الأمة، يستعيد اليوم عزه وكرامته، ويمضي نحو يمنٍ حرٍّ عزيز، قراره بيد أبنائه، وسيادته مصانة، وإرادته مستقلة عن كل وصاية أو إملاء خارجي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90200" target="_blank">📅 19:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DZwp22Qh4wRkEl-oe2n0nVj-uyXwujpm6Ju5hvmObNLvmK_LsQeroL5FNU8VO9bRlS3snu1B13JFNpxUkKZ4FmXyTDYlUwiQAP7Hpyq7B03tKqUKLL0yPvAABDxRRAIeUPFlJUvEX01TAG6O-czn_wRiEBUVh-Fw8ZoaRQiqj-CQhtuxM9xkcYbVBMKszpkz4yypU-vKU6giQTFC-IwFm_7pVwbgd9Z-qfSA7gIwUywOFrXpKAqA1_8GAg84sxp5BL_WozlK5UhzZmmh-_N6WVGEfIDUgZwakwRPgDQqUfLpeDNXRGp8_oVue7UNQ-IbJmkdZeGq263YTjwoJXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هزة ارضية في محافظة اربيل شمالي العراق تبلغ قوتها 3.1 درجة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90199" target="_blank">📅 19:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">القوات المسلحة اليمنية تستمع لكلمة العميد يحيى سريع من سواحل المخا المحررة</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90198" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">القوات المسلحة اليمنية تستمع لكلمة العميد يحيى سريع من سواحل المخا المحررة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90197" target="_blank">📅 18:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e367315034.mp4?token=bN7MXIRE8ihHFmwGoER3kTPPeivnp507LfSGn7jh41mTQc9scMDEwhR6ohRzfltCaLjf2CmwyYcu3Dy8HiMFlubIUs4Uz34eXxdxMCnKbpXhPn9UVRCYR_0A8bpgfly2gJ50Fhp_lzE35zPIdOgGUsseTw_F2pQK7bPqVgLMx84_VikV4tgrpKDSB3Vhh8aUDViZtI2GH5eOxA2Jg4uvNwhQ6Ye007mAljMj2soAwYL72Z9pSjxZQ3-TtNZUUXS_TnWkC4kePhi6u2aBFsnbOG1e4zKgeo3GKltZGG3hsgHCpZCqyX5Joq43ywPTXT6qBl6LHkHGsOCmKZEtr0HxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e367315034.mp4?token=bN7MXIRE8ihHFmwGoER3kTPPeivnp507LfSGn7jh41mTQc9scMDEwhR6ohRzfltCaLjf2CmwyYcu3Dy8HiMFlubIUs4Uz34eXxdxMCnKbpXhPn9UVRCYR_0A8bpgfly2gJ50Fhp_lzE35zPIdOgGUsseTw_F2pQK7bPqVgLMx84_VikV4tgrpKDSB3Vhh8aUDViZtI2GH5eOxA2Jg4uvNwhQ6Ye007mAljMj2soAwYL72Z9pSjxZQ3-TtNZUUXS_TnWkC4kePhi6u2aBFsnbOG1e4zKgeo3GKltZGG3hsgHCpZCqyX5Joq43ywPTXT6qBl6LHkHGsOCmKZEtr0HxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرعات المرتزقة بيد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90196" target="_blank">📅 17:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الجمهورية الإسلامية الإيرانية الراعي الأول للإرهاب في العالم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90195" target="_blank">📅 17:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694eec3d51.mp4?token=arMvm99TJf9M5scjlCqw_97QmHK4UcpscF1lI2OMKcbptvKWt7G0xwrUOlhUZ25fIhnKtMvHYYBYp-3HecRitKWXEinm-pdR_1ewCHm8ibhajzyG65wqE30zKriq3-C7RDTi8M1mjd7R5yiM-XoXJvN1HqKIK7I8lvndOyX2k_8yzAixKKXLZyTSzilThPkDowp4yxaYRwU6ZIlD0ESWBGK7lyGGCGcpYHDSelBcRnBpk5hkYddL5UA6xbabAUqTLrAX3KW2LuvTZ3jnb1fcRU_yVP0bGEy3d3FAGb_2J2lNFD4SFnkIF6qn_w3CMWFBKcIFVENBJbLpzLxYdUD4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694eec3d51.mp4?token=arMvm99TJf9M5scjlCqw_97QmHK4UcpscF1lI2OMKcbptvKWt7G0xwrUOlhUZ25fIhnKtMvHYYBYp-3HecRitKWXEinm-pdR_1ewCHm8ibhajzyG65wqE30zKriq3-C7RDTi8M1mjd7R5yiM-XoXJvN1HqKIK7I8lvndOyX2k_8yzAixKKXLZyTSzilThPkDowp4yxaYRwU6ZIlD0ESWBGK7lyGGCGcpYHDSelBcRnBpk5hkYddL5UA6xbabAUqTLrAX3KW2LuvTZ3jnb1fcRU_yVP0bGEy3d3FAGb_2J2lNFD4SFnkIF6qn_w3CMWFBKcIFVENBJbLpzLxYdUD4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرعات المرتزقة بيد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90194" target="_blank">📅 17:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dea1e354.mp4?token=a8kaCjt41B_1z2GEP16Rtel7OgVObapjgqw854cKmazPLtfO17vEkbrHTxh5OoaHVPqBlVP3WjrWLMrc7GXmAQ4fEBuWoaJmhEo7e-S7osKBaefOVvCQT0hGbQvZAVeYGkbTGclZXI8KU7d4-TrS6OnvDIdgxg-pwiuaU3W03Be7LkIwyRwgl4wY0XtKg5GiV9mgJzSojxAWtsk3S3iUXQbK8KwOxOCVsEOQihvwWzm_rkSrvYb_9ea2J91YazZnB7XVgg0G27K02YmViB0I-CtM67VRTSsozDwL7EgfsbI6Eadfyw0ytS8svvui2u31uPafR-9swWJiffeHsTXRrB3dkIQykQV6s1q2s0ztHPlEEOnvshwHEAaQ1u8YbdATVg6JNkVTs95U5t4n7xvvdd0Dtycv4-H-qmoDfm19Mew_8Ete04ABfNqRvgu82rDoNIIbYwuR1N9J04l6LdlGJXnf3Q4__xP05oMEtj9XIV3JrHywwUH2ZXT79NPqWoOragdliBLdWDo5vLzXjdre6435KIj_Lq3_wAKrKhiuiYE_r6JUD-JZ3SN_GeqwltNBb_FyK0EcX8ENHrARDbyrzY5v3fggp38svZilg2ZEEcZu4qhLQSCPTrkYKWk0UZo9Ea1jfsLZlayH5SOrkiSsz35BOF6ZCTrz1vIl-dnz8cM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dea1e354.mp4?token=a8kaCjt41B_1z2GEP16Rtel7OgVObapjgqw854cKmazPLtfO17vEkbrHTxh5OoaHVPqBlVP3WjrWLMrc7GXmAQ4fEBuWoaJmhEo7e-S7osKBaefOVvCQT0hGbQvZAVeYGkbTGclZXI8KU7d4-TrS6OnvDIdgxg-pwiuaU3W03Be7LkIwyRwgl4wY0XtKg5GiV9mgJzSojxAWtsk3S3iUXQbK8KwOxOCVsEOQihvwWzm_rkSrvYb_9ea2J91YazZnB7XVgg0G27K02YmViB0I-CtM67VRTSsozDwL7EgfsbI6Eadfyw0ytS8svvui2u31uPafR-9swWJiffeHsTXRrB3dkIQykQV6s1q2s0ztHPlEEOnvshwHEAaQ1u8YbdATVg6JNkVTs95U5t4n7xvvdd0Dtycv4-H-qmoDfm19Mew_8Ete04ABfNqRvgu82rDoNIIbYwuR1N9J04l6LdlGJXnf3Q4__xP05oMEtj9XIV3JrHywwUH2ZXT79NPqWoOragdliBLdWDo5vLzXjdre6435KIj_Lq3_wAKrKhiuiYE_r6JUD-JZ3SN_GeqwltNBb_FyK0EcX8ENHrARDbyrzY5v3fggp38svZilg2ZEEcZu4qhLQSCPTrkYKWk0UZo9Ea1jfsLZlayH5SOrkiSsz35BOF6ZCTrz1vIl-dnz8cM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من جزيرة ميون المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90193" target="_blank">📅 17:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90192" target="_blank">📅 17:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية:
خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90191" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان للقوات المسلحة اليمنية:
بسمِ اللهِ الرحمنِ الرحيم
قال تعالى: { وَٱللَّهُ أَشَدُّ بَأۡسࣰا وَأَشَدُّ تَنكِیلࣰا } صدق اللهُ العظيم
في إطارِ ضربِ تحشيداتِ العدوِّ السعوديِّ المجرمِ ومواجهةِ عدوانِهِ السافرِ وحصارهِ الظالمِ المستمرِّ على شعبِنا العزيزِ منذُ اثنَي عشرَ عاماً لثنيهِ عن مطالبهِ المحقةِ ومواقفهِ المشرفةِ في نُصرةِ الشعبِ الفلسطينيِّ المظلوم.
ومع استمرارِ الاعتداءاتِ من التحشيداتِ التابعةِ للعدوِّ السعوديِّ على أبناءِ وقُرى وعُزَلِ الساحلِ الغربيِّ طوالَ السنواتِ الماضيةِ وتصاعدِها في الأشهرِ الأخيرةِ، وفي ظلِّ النداءاتِ المتكررةِ لأبناءِ تلكَ المناطقِ لجيشِنا المجاهدِ بالتحركِ لإسنادِهم ورَفْعِ الظلمِ عنهم؛
أطلقتِ القواتُ المسلحةُ اليمنيةُ -بعونِ اللهِ تعالى وبمشاركةٍ كبيرةٍ من أبناءِ شعبِنا وقبائلِه الحرةِ، في الثالثِ من سبتمبرَ الجاري- عمليةَ "والله أشدُّ بأساً وأشدُّ تنكيلاً" العسكريةَ النوعيةَ الواسعةَ من عدةِ مساراتٍ؛ لطردِ التحشيداتِ السعوديةِ في بعضِ مديرياتِ الساحلِ الغربيِّ التي ترتكبُ أبشعَ الجرائمِ بحقِّ المواطنينَ، وتسعى لإخضاعِ الجغرافيا اليمنيةِ للاحتلالِ والسيطرةِ السعوديةِ.
وقد تكللتْ بالنجاحِ والتوفيقِ من اللهِ سبحانه وتعالى؛ رُغمَ الغطاءِ الجويِّ الكثيفِ من قِبَلِ العدوِّ السعوديِّ المساندِ لتحشيداتِه، إلا أنه فشلَ بفضلِ اللهِ في التأثيرِ على العمليةِ، وقد حققتِ العمليةُ النتائجَ التاليةَ:
أولاً: طردُ تحشيداتِ العدوِّ السعوديِّ من ستِّ مديرياتٍ من محافظتَي تعزَ والحديدةِ بمساحةٍ إجماليةٍ بلغتْ 5400 كيلومترٍ مربعٍ وأصبحتْ بفضلِ اللهِ آمنةً مستقرة.
ثانياً: ضربُ سبعِ فِرَقٍ عسكريةٍ من تحشيداتِ العدوِّ السعوديِّ بقوامِ 38 لواءً عسكرياً، وقَتْلُ وأَسْرُ وَجَرْحُ المئاتِ من منتسبيها.
* ثالثاً: تحريرُ عددٍ من أسرانا الأعزاءِ المتواجدين  لدى مرتزقةِ العدوِّ السعوديِّ منذُ سنواتٍ في الساحلِ الغربي.
رابعاً: تمكَّنتِ القواتُ المسلحةُ -بفضلِ اللهِ- من تنفيذِ (32) عمليةَ تصدٍ للطائراتِ الحربيةِ السعوديةِ، وإسقاطِ تسعِ طائراتٍ.
التحيةُ لجيشِنا المجاهدِ العظيمِ على جهادِه وعطائِه الكبيرِ في سبيلِ اللهِ دفاعاً عن شعبِنا وبلدِنا، والتحيةُ كُلُّ التحيةِ لشعبِنا العزيزِ المؤمنِ المجاهدِ وقبائلِه الحرةِ على ما تقدمُه من دعمٍ وإسنادٍ للقواتِ المسلحةِ في معركةِ التحررِ والاستقلالِ واستعادةِ السيادةِ الوطنيةِ، ولما يتمتعُ به من وعيٍ عالٍ في مواجهةِ الدعاياتِ والتضليلِ الإعلاميِّ الكاذبِ الذي مارسهُ العدوُّ طوالَ الأيامِ الماضية.
إنَّ القواتِ المسلحةَ اليمنيةَ تؤكدُ أنَّ الملاحةَ البحريةَ آمنةً لكلِّ الشركاتِ باستثناءِ السفنِ السعوديةِ التي سبقَ إعلانُ الحظرِ عليها، وأنَّها مستمرةٌ في تثبيتِ معادلةِ الحصارِ بالحصارِ وضربِ تحشيداتِ العدوِّ السعوديِّ والتصعيدِ بالتصعيدِ؛ حتى وَقْفِ العدوانِ ورَفْعِ الحصارِ عن شعبِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 29 ربيع الأول 1448هـ
الموافقُ 11 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90190" target="_blank">📅 16:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90189">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedecda38d.mp4?token=CdWP0aEY2LlUN-tXC2soFBZ8sfP14bu2_S0vIKQfTbyQAnmqW0O465S5FMkvxs67HS0YmW0CwkBlE6Dpiz6LhbYBbvvMLGjVRcY5SDjXYdyUas7-C26yZnuvdYTATiMSLS5Kv0LIKyv4dFS8Sv53-t8hW9iYzwja3Cp_RmX2mNaoVspvx7vY4pYnuDAxz9y6ki8YinrWadny59OlpjxSNiIN5fxnhmu_KFkHEllu9wnsIPMv0k_iPuCYeLP5HOL4QuAE9uKIRdUYUw4gyOSoEQuQLHSvVzbYRYyzGKiHjE83fTcFtWs_86_LtddbWkfDGfeU90SjOr7TcRoG841jqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedecda38d.mp4?token=CdWP0aEY2LlUN-tXC2soFBZ8sfP14bu2_S0vIKQfTbyQAnmqW0O465S5FMkvxs67HS0YmW0CwkBlE6Dpiz6LhbYBbvvMLGjVRcY5SDjXYdyUas7-C26yZnuvdYTATiMSLS5Kv0LIKyv4dFS8Sv53-t8hW9iYzwja3Cp_RmX2mNaoVspvx7vY4pYnuDAxz9y6ki8YinrWadny59OlpjxSNiIN5fxnhmu_KFkHEllu9wnsIPMv0k_iPuCYeLP5HOL4QuAE9uKIRdUYUw4gyOSoEQuQLHSvVzbYRYyzGKiHjE83fTcFtWs_86_LtddbWkfDGfeU90SjOr7TcRoG841jqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90189" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90188">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650f87549f.mp4?token=OR5nPVLvagqeadCR3-2IwSOkdFzU3oR-nHiJ1IfA4oSBoEfgp48MJGbXb1heDckGPiJ_coM_aYDEFzsUpFW496fmdnOlBdtpvqnLn04yr7c28PiW7S-1Jwe-gitn39IQbGwEyehOJ2XCI44gsXCUQiNiTvPRAepewUyDH3K45R9sEijqSVvN5XGPlDIHtfjL9_-nWAY6Q8SygJR6v9Xi40ZdGSfhyjJlCRs8Nr_oj0jzAQZeJu6RQdK1QJFUiX-5bqyCPkUKwzL-iyTbNiIznysUAQmRkdqlxguP2yw3gKlg3tsOIZvOKhGABNImfD_tBxDUNe7HioYFE-Ez51XVUlpasMk638g8rXGRNvQ36XhmaO4pEZlASzUexuiKBbLLjvI7RvonKKhWwjvH6A7ruFl8uS82lOCnDG1YyRVN81lkvg3tcmBt9dDmE7n-nZefJasQleBbqlLoCPz_UxPPl_dhbA3Ye4-k6UvPb4R1YoAKPNbrlhCI9yPHur7TdgsLvS8KxRCtscxzM0inyK7S7XSRy8uT0Ai0b8mFKGZY0_l-TJVFUm0qI2bGB6lrCY9dd4b7fHosoQUV7z16q_72vceASgsGCuJAiYlKezXl5EvIfboCL6XiE4k40rCs_5Aqs6JSVmcuCKPL-EpvCSpL72JvFpwNhAAGJrdwSLHwcic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650f87549f.mp4?token=OR5nPVLvagqeadCR3-2IwSOkdFzU3oR-nHiJ1IfA4oSBoEfgp48MJGbXb1heDckGPiJ_coM_aYDEFzsUpFW496fmdnOlBdtpvqnLn04yr7c28PiW7S-1Jwe-gitn39IQbGwEyehOJ2XCI44gsXCUQiNiTvPRAepewUyDH3K45R9sEijqSVvN5XGPlDIHtfjL9_-nWAY6Q8SygJR6v9Xi40ZdGSfhyjJlCRs8Nr_oj0jzAQZeJu6RQdK1QJFUiX-5bqyCPkUKwzL-iyTbNiIznysUAQmRkdqlxguP2yw3gKlg3tsOIZvOKhGABNImfD_tBxDUNe7HioYFE-Ez51XVUlpasMk638g8rXGRNvQ36XhmaO4pEZlASzUexuiKBbLLjvI7RvonKKhWwjvH6A7ruFl8uS82lOCnDG1YyRVN81lkvg3tcmBt9dDmE7n-nZefJasQleBbqlLoCPz_UxPPl_dhbA3Ye4-k6UvPb4R1YoAKPNbrlhCI9yPHur7TdgsLvS8KxRCtscxzM0inyK7S7XSRy8uT0Ai0b8mFKGZY0_l-TJVFUm0qI2bGB6lrCY9dd4b7fHosoQUV7z16q_72vceASgsGCuJAiYlKezXl5EvIfboCL6XiE4k40rCs_5Aqs6JSVmcuCKPL-EpvCSpL72JvFpwNhAAGJrdwSLHwcic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا والمخصصة لسكن المرتزقة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90188" target="_blank">📅 16:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70538256bd.mp4?token=Uyoa3LW3Y-VzNPMAdeWgbeo9WmIN4vfdOwyCwSDxSYLKKurJ3YXdI__-97yOIsSXyIhMF5wce0ZeZjdZGyM6PL8Jf7B5lyr0iKd8UeZnodVWuhXVrttiGCKr5WHAvaX7dgVjvWBlphwJGrrBfCqcMJURqSqiIq-qWdB8N7UQWCsDdv3GL4LmYyH2I4EldQJm-cmYHgGN1BvqMpPRJ7WzV3Y_PVdkx-Lu9-P8J_eze1WKmSDeK0HmzFWimKQ5_Fu52zaQnI3TkxrLgrGfaj-xFT12LTYMxKNEBnM_kyzJoYM9emyl9fP__gEx0fJkKKfkWb0NZz-kqd7Zkmp5h1o4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70538256bd.mp4?token=Uyoa3LW3Y-VzNPMAdeWgbeo9WmIN4vfdOwyCwSDxSYLKKurJ3YXdI__-97yOIsSXyIhMF5wce0ZeZjdZGyM6PL8Jf7B5lyr0iKd8UeZnodVWuhXVrttiGCKr5WHAvaX7dgVjvWBlphwJGrrBfCqcMJURqSqiIq-qWdB8N7UQWCsDdv3GL4LmYyH2I4EldQJm-cmYHgGN1BvqMpPRJ7WzV3Y_PVdkx-Lu9-P8J_eze1WKmSDeK0HmzFWimKQ5_Fu52zaQnI3TkxrLgrGfaj-xFT12LTYMxKNEBnM_kyzJoYM9emyl9fP__gEx0fJkKKfkWb0NZz-kqd7Zkmp5h1o4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عناصر القوات المسلحة اليمنية يجربون صوت احدى غنائمهم من مرتزقة السعودية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90187" target="_blank">📅 15:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا والمخصصة لسكن المرتزقة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90186" target="_blank">📅 15:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">القوات المسلحة اليمنية تردد شعار الصرخة من سواحل المخا وباب المندب</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90185" target="_blank">📅 15:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06ad01a85.mp4?token=rZxtVDlgMlwwzyZgc6E99WYw0PFGdSWz2tVuu_24R1K9cjslxuupbtElUxu7h9zYHIO8xpT3NZIVf1mLPzvPpk8VaZTf-WTIcj9H5rOuNd82IWCa1XFZqag19tYLIsFXrqSrTNlpMY7_Ig9UFQKyO5lULinpPww7kgrPCAVY1wed-kZOZT0BzdMkBDJq4THeY6UhLYJlW1L4IbIjXOi2wtLy21LchXbDPad9gO5iRfXZJM5sgbfk1r7DqQbOO24mXJJ3w565KYfu1RcrzUqrc-37wDxP9_5w58GQDMLgnSIrmIsWL9GqcBDkLSZdM8DDEawToKh0sVIcMYFUbzSKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06ad01a85.mp4?token=rZxtVDlgMlwwzyZgc6E99WYw0PFGdSWz2tVuu_24R1K9cjslxuupbtElUxu7h9zYHIO8xpT3NZIVf1mLPzvPpk8VaZTf-WTIcj9H5rOuNd82IWCa1XFZqag19tYLIsFXrqSrTNlpMY7_Ig9UFQKyO5lULinpPww7kgrPCAVY1wed-kZOZT0BzdMkBDJq4THeY6UhLYJlW1L4IbIjXOi2wtLy21LchXbDPad9gO5iRfXZJM5sgbfk1r7DqQbOO24mXJJ3w565KYfu1RcrzUqrc-37wDxP9_5w58GQDMLgnSIrmIsWL9GqcBDkLSZdM8DDEawToKh0sVIcMYFUbzSKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تردد شعار الصرخة من سواحل المخا وباب المندب</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90184" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">القوات المسلحة اليمنية تبيد ارتال مرتزقة السعودية الفارين</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90183" target="_blank">📅 15:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90182">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من غنائم القوات المسلحة اليمنية في ذو باب</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90182" target="_blank">📅 15:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم معدات واليات مرتزقة السعودية في ذو باب بعد فرارهم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90181" target="_blank">📅 15:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم معدات واليات مرتزقة السعودية في ذو باب بعد فرارهم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90180" target="_blank">📅 15:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">القوات المسلحة اليمنية تبيد ارتال مرتزقة السعودية على الساحل الغربي</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90179" target="_blank">📅 15:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyvl5Hor8OT0uVWjiBNVG_pZVG5DZPR-e6HDIubTcQ8Rjj-F2zsdCmJ5uBQM9_fNGf8sGWYs1VC9EaY4LneGjxOr-NaIPr5eWWDPr9gPKKcOApAyzOBi7UFTjyD1lSxLD1CM3SiLSObty3QrsNeyD3rjOtbEEDxN0ewZx_akD7qKBVSPGppkLzUAYudJRx_-N36KN-nNMjvgjsH3r7m5M0o0mn3quFX3ASy1s5h1rN7eDhaODeXEmX5w-Yc0iYx01J4kk7hbL7n7JXTDZDyUTJre19veKWAEfaDmRhCUuE3OwMxmTJVbBAmAYYtIfVsAqkZcCDNSs4CSOfKmm-yOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية من امام مركز مديرية ذو باب بعد السيطرة عليها</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90178" target="_blank">📅 15:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
تلغراف:
إسرائيل
تطرد جنودا بريطانيين كانوا يراقبون عنف المستوطنين في الضفة الغربية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90177" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇱
اعلام العدو:
المنظومة الدفاعية تتأهب بشكل استثنائي شمال ووسط البلاد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90176" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0d1DPQZP-26MQYOatDWUg7jJUSoKiQ3DXraWOs381l2eg2eHT3VtWNDsG5W_9jTKjbY_r3Ifh7KvoI_EsZDBChFmhvRMcBHxwfeszgsOFqhujU7usY3stCnSdV6FNF51HoH0_iIOQmFfqM8SprlelLmckQosegGgnZfbUGnxGDm2YWHlBSa_Ak3m9bxn9RoCzCVDJPNVCvrJZj9ogWeYKKinH5s4gHW5xmOZVBS-L0rXRzkE1T2NbeDdCrEdvRtZss2JEMpdYLV2cvmRaW5kn9EhRDiB3XfC86Am1X4shXrc5L-vcP-6meUVo3YsmQU-Ln1GHD8DebKIIqgCXbIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تنخفض قليلا وتصل الى 104 دولار للبرميل بعد تقرير امريكي عن مساع لاتفاق مؤقت مع إيران بشأن مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90175" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">القوات المسلحة اليمنية في باب المندب</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90174" target="_blank">📅 14:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انصار الله يقضون ساعات مميزة في ميناء المخا بعد طرد مرتزقة السعودية منه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90173" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJlllDHCkWovB6CBRoOb_4PYWViAalgUER49pmREJs4EwGed9A1o8Cxm0Ty_QUL6iaU4uH_HU52dwd0bOtTBaAU29EkYyxNuLy-bIT6wkWOguKuFbPHvdj--s6NJL96UVcsyC62UAgmV7ShWO265yE2Nxob8gabXl-EXgCYP2DDCkEwFuBEzeb-wgOTHrKjTv7ATGkUv-sJuPBZwf0h1320p5AMYO83tox7jrNB4XuxvF4PzExhBHXhW1JQBd36mO97lOJ9UY0wMdeKxiuhEOSd5bXRTRJHi9OYq87-l4s4Ox8nYCKYPLLDvzUAaH72PC7sbNSQrmzZPqVTWwE47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد:
في سياق معادلة «التصعيد بالتصعيد»، فإن أي استهدافٍ للبنية التحتية أو المطارات أو الموانئ في المخا وذوباب وميون وغيرها من المناطق اليمنية، من قِبل نظام العدو السعودي، سيُقابَل بالمثل.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90172" target="_blank">📅 13:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الاعلام الاجنبي: انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90171" target="_blank">📅 13:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90170" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
الرئيس التنفيذي لمطارات دبي بول غريفيث:
دبي تدرس نقل أجزاء من مطارها الجديد تحت الأرض، بما في ذلك تخزين الوقود، للحماية من الضربات المحتملة بالطائرات بدون طيار والصواريخ في أعقاب الحرب الإيرانية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90169" target="_blank">📅 13:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">القوات المسلحة اليمنية تستهدف تجمعات المرتزقة في رأس العارة بثلاث صواريخ باليستية</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90168" target="_blank">📅 13:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسؤول باكستاني لرويترز:
باكستان تحاول التزام الصمت في الصراع السعودي الحوثي الحالي لأن مصالح باكستان الخاصة كبيرة ولا تريد إفساد العلاقات مع إيران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90167" target="_blank">📅 12:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عدوان سعودي على ميناء المخا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90166" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90165" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/968111c504.mp4?token=ahYPnzxMx-ujhKJLdEpvBhU4VD6v37HyHGM9-iuavxv6Y5jSn_Xu3xeCviTLMGwJT_46hhPoHUFE-8oY9xzbsws4yH26Cl40meeGiBF1K2j5VCZmBoOx3ZmKAWx-YHS0SfCbsqSgkqpw9GG-cVKeWCvH_gqiahawYYZbflGDMwwd8G7BWh-kGSMsL8z8XFAPEZbvZk6OrvvDasMgkaT0onNHD_umijRxDVD2dq3l79BV9N4C8Lr-l4kW0-IHLdgB83FD4SSC_1o3MNzDwcGemZ8fADpM1d6VYJrKCN-O-s5OhSt39vDkYa5bNmJTs-gH9ZyuFWMl88_GZW6MTGsKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/968111c504.mp4?token=ahYPnzxMx-ujhKJLdEpvBhU4VD6v37HyHGM9-iuavxv6Y5jSn_Xu3xeCviTLMGwJT_46hhPoHUFE-8oY9xzbsws4yH26Cl40meeGiBF1K2j5VCZmBoOx3ZmKAWx-YHS0SfCbsqSgkqpw9GG-cVKeWCvH_gqiahawYYZbflGDMwwd8G7BWh-kGSMsL8z8XFAPEZbvZk6OrvvDasMgkaT0onNHD_umijRxDVD2dq3l79BV9N4C8Lr-l4kW0-IHLdgB83FD4SSC_1o3MNzDwcGemZ8fADpM1d6VYJrKCN-O-s5OhSt39vDkYa5bNmJTs-gH9ZyuFWMl88_GZW6MTGsKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الضربة الجوية التي استهدفت اوكار عصابات داعش الارهابية في وادي الشاي شمال غرب العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90164" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يشن غارتين على مطار المخا.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90163" target="_blank">📅 11:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFOoceImzIZditsDtqfyHeNJHoySS4Z_0dSpDuYrHXhykSym09JCApsP0bTFHUPBKxbvkYwU6yrOoB6cO_KT1JglYS2cLhoNfmTVhUVlLQFatcvcw7WYq4NkgRL77MrdL-ss6b90pFjyjvGX6UT4e3L3_0Az5EqXk38CJCTVCCDqdfw-8vAnIa_lkaY-0oV_gz6MOCHKeTecGskKCmdKwySCDbyRklfdwWTXHxwVNnTdPJBwt29Oa5VIAKZXyzKcPiswD5YZJPx5Vycbk1R11o43GuSy9NoONiEM6r5ZZMXyw8k8GHSk3vGjFLfqvpwI7MHzcS272PEJ6zDjHRTquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
رويترز: الحوثيون وصلوا إلى مدينة ذو باب الساحلية على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90162" target="_blank">📅 11:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الاعلام الاجنبي: انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90161" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90160" target="_blank">📅 11:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وكالة الطاقة الدولية:
من المتوقع أن يبلغ متوسط ​​إمدادات النفط العالمية 100.7 مليون برميل يوميًا في عام 2026، بانخفاض قدره 5.7 مليون برميل يوميًا عن عام 2025، وأقل بمقدار 1.3 مليون برميل يوميًا عن التوقعات السابقة، مخزونات النفط العالمية انخفضت 95 مليون برميل إضافية في أغسطس.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90159" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24fee932a6.mp4?token=lskUs5idFbT_PvsbsYWlnO9jA8c_9D_M-KFXzUybo4tngHAtN84kpdEOI2vWc1VVtwiAvsOcqKB4s-D04ED3LtYDQczB3vbmPK92aSSvEe4i6JWdLR6FlJ_mExu0f7CFXXOOwSznV6x45G_Q9Qnt6CWfqXQMdONBWsdjV3Fah9Yvq4jBl6dV4BGQ-gr2hxb8S9h261-zCF6pOVIdvMmyUsW0Qt00CIsfYW2gTdJKgIvMAT4Hpr6uEZw_wCUa5mky4I-huCVW67aL2qH-6p4ZlceguzVGTYLl2-lGARnaBUb_pSzVoDP0vkxcJ4VHD9sWfvPvcCRqLOrOUlpyyxa8tDmginZSSmJWax4ozJsh_K6LeqD03ZyhT4HrizOP5JP7TyDoWXkngtcniXRwf850iBNmEQfFVnq98sxGFEoK_cZh7guXiAX6okkWglx9_C4GVblOJ-lAm1lEIu-cPL8LKZw7rPRgLKj6W0hauFbxvdrZOWymlOnavOhR4nrQDYjUm4CNVwHxIyZQFGw-HRC1FdvyQw0-FatvpsbIxP5UzWnYdrjO44u--9PwexoCp2hGcZqvzY-LigFtBwkKDr5UmOafccF6WmvpLYbqSdq__UmCp9oPuGlKogFJsSPHWC4IbsBeru0UBvZfhPK_BUM3Epy8iNh6OaquTXpR8AyTMLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24fee932a6.mp4?token=lskUs5idFbT_PvsbsYWlnO9jA8c_9D_M-KFXzUybo4tngHAtN84kpdEOI2vWc1VVtwiAvsOcqKB4s-D04ED3LtYDQczB3vbmPK92aSSvEe4i6JWdLR6FlJ_mExu0f7CFXXOOwSznV6x45G_Q9Qnt6CWfqXQMdONBWsdjV3Fah9Yvq4jBl6dV4BGQ-gr2hxb8S9h261-zCF6pOVIdvMmyUsW0Qt00CIsfYW2gTdJKgIvMAT4Hpr6uEZw_wCUa5mky4I-huCVW67aL2qH-6p4ZlceguzVGTYLl2-lGARnaBUb_pSzVoDP0vkxcJ4VHD9sWfvPvcCRqLOrOUlpyyxa8tDmginZSSmJWax4ozJsh_K6LeqD03ZyhT4HrizOP5JP7TyDoWXkngtcniXRwf850iBNmEQfFVnq98sxGFEoK_cZh7guXiAX6okkWglx9_C4GVblOJ-lAm1lEIu-cPL8LKZw7rPRgLKj6W0hauFbxvdrZOWymlOnavOhR4nrQDYjUm4CNVwHxIyZQFGw-HRC1FdvyQw0-FatvpsbIxP5UzWnYdrjO44u--9PwexoCp2hGcZqvzY-LigFtBwkKDr5UmOafccF6WmvpLYbqSdq__UmCp9oPuGlKogFJsSPHWC4IbsBeru0UBvZfhPK_BUM3Epy8iNh6OaquTXpR8AyTMLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90158" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الاعلام الاجنبي:
انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90157" target="_blank">📅 11:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90156" target="_blank">📅 11:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAljRYBTqT9bKa6Iykzq67r2JK6QHw5X5nhpGS-wJE0hORib9I8nBO63NHHtpPEtrBdgGe5CZMCNisTSc8SZXODFTF2Kc-xpZNUN45ieHOvQL6HfNJdOjNFs97BCio1eSQO0O06Ssj_81ngkhhVKP25CQ3fPtKrHACkV-aYZeW7s_Bxrop8lddvZsnAlVqhT5PIUCDA2g2Iiz4TGWQM6A_X8JFlh3CgA7-4EAlqcd83yVlFRshYrOoXbUzu12MKvVH40ys5DsfPvWme2a09Pi0vUY-zm3syzSK-frysvlK2tjzj0ftVgCTrbyl5lFS6Ql4bPCBvXAXU4IYlg77lI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90155" target="_blank">📅 11:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324d248f2d.mp4?token=IjxuGE9qAj7GFmvnrW5XlD7rmga3mZTU77QiEnR8Q_MnQxqcUtPayu_9uINf9vJLouY0pw9nQ9NWWK3PQaBZYXvwtCyVZ85qrur9R_9J67znTG5kv2f0g7-g5fk6fB-aJOTu0bdIlpaBeczFmN5-0DXBftY7wODjA1RDF008bv_U5L3T92S2usWVCvhx-10Etmc9SotuM0mpFTWXgSg_IjF6GFEDu_ZtYKjwDa5jXku_dI8-ycAxd0LnbeWkBUWdmx4WmXFC-vRN3tspQPUQVhYH9mM3X01IQwm3n_8RAMLdbmiyG5YcEr1Xm-6QeRHpiaVV28JH1LwVvNtOBAGeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324d248f2d.mp4?token=IjxuGE9qAj7GFmvnrW5XlD7rmga3mZTU77QiEnR8Q_MnQxqcUtPayu_9uINf9vJLouY0pw9nQ9NWWK3PQaBZYXvwtCyVZ85qrur9R_9J67znTG5kv2f0g7-g5fk6fB-aJOTu0bdIlpaBeczFmN5-0DXBftY7wODjA1RDF008bv_U5L3T92S2usWVCvhx-10Etmc9SotuM0mpFTWXgSg_IjF6GFEDu_ZtYKjwDa5jXku_dI8-ycAxd0LnbeWkBUWdmx4WmXFC-vRN3tspQPUQVhYH9mM3X01IQwm3n_8RAMLdbmiyG5YcEr1Xm-6QeRHpiaVV28JH1LwVvNtOBAGeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90154" target="_blank">📅 11:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇶🇦
🇺🇸
الاعلام الاميركي:
قطر  أكبر مُصدِّر للغاز الطبيعي المسال في العالم قبل الحرب - تجري الآن محادثات لشراء الغاز الطبيعي المسال الأمريكي بموجب عقود طويلة الأجل.
هذا تحول مذهل.
أدت الحرب الإيرانية إلى تعطيل اثنين من أصل 14 وحدة من وحدات الغاز الطبيعي المسال القطرية في رأس لفان (مدة الإصلاح من 3 إلى 5 سنوات، وخسارة في الإيرادات تبلغ حوالي 20 مليار دولار سنوياً)، كما أن مضيق هرمز شديد الخطورة على حركة ناقلات النفط المنتظمة.
النتيجة: انخفاض بنسبة 96% في الصادرات - 18 شحنة فقط تم شحنها في ستة أشهر مقابل 509 شحنة في نفس الفترة من العام السابق، بتكلفة تقدر بنحو 24 مليار دولار.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90153" target="_blank">📅 09:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان: الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90152" target="_blank">📅 09:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
مصدر يمني:
تم أسر 2000 جندي من مرتزقة السعودية، مع عتادهم العسكري في جزيرة زقر وحنيش وميون على يد القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/90151" target="_blank">📅 05:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
عقب تحريرها من مرتزقة السعودية..
القوات اليمنية تقوم بتأمين الأحياء والمحلات التجارية في مدينة المخا.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/90150" target="_blank">📅 05:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إنهيار مبنى قيد الإنشاء قرب جسر الصرافية بالعاصمة بغداد، وأنباء عن مصرع 8 عمال كحصيلة اولية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/90149" target="_blank">📅 04:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
غنائم من مرتزقة السعودية في أيدي أبطال القوات اليمنية.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/90148" target="_blank">📅 03:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد مذلة لمرتزقة السعودية حيث مرتزقة الإمارات تمنعهم من دخول عدن عقب هروبهم من المناطق التي سيطرت عليها القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90147" target="_blank">📅 03:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
🇸🇦
‏الأرتال العسكرية المتبقية من مرتزقة السعودية تهرب من راس العارة بعد دكهم برشقات صاروخية من قبل القوات اليمنية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90146" target="_blank">📅 03:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  ستنتهي حرب إيران مباشرة بعد الانتخابات النصفية الأمريكية.  الإيرانيون يواصلون القتال بصعوبة وهم في مأزق عميق.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/90145" target="_blank">📅 03:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي للقوات اليمنية على تحشدات مرتزقة السعودية في منطقة رأس العارة غربي محافظة لحج، يجبرهم على الهروب والإنسحاب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90144" target="_blank">📅 03:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: لو لم نتناول ملف إيران، لكنتم ستفوزون بسهولة في انتخابات التجديد النصفي. هل لديكم أي ندم؟
🇺🇸
‏ترامب: لا، أنا لا أؤمن بكلمة "الندم". يمكنك دائماً أن تشكك في نفسك قليلاً.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90143" target="_blank">📅 02:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: كيف ستتمكن إيران من إطلاق الصواريخ إذا قمنا بتدميرها؟
🇺🇸
‏ترامب: بإمكانهم دائماً إطلاق الصواريخ. كان لديهم الكثير منها.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90142" target="_blank">📅 02:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90141" target="_blank">📅 02:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90140" target="_blank">📅 02:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7S9JXCLEVLGMdPvV9bZ7I2eX2U0m5s4czgr0Wt2yIOTm51ga-bkbvQ_iP_xzsDB97BJgUatcpX0sAd3s4-8Um0LxsJrX_tay95XwHCpgoC3MbFHq30IYJ8YSI9z-XiAbGqfVgY93MqgocvwSlyui_bNlPDTCKolm15eKc9yOBeM_KIwzFYQNYPjCjqbVo18vdum5f_giSW5RcC3nZcz15et81RAXGPCNaZvw-uLGwaV-3u0lSFb1kVvugbe4hR3m3cwoBwrMwSBezS3B4lNlZSetTfiuFhVofqBPazqqsmv7KfiG-E__0Ujc2bqjDTTrjUwFjMFPyqjxZyiVigUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تؤكد الجمهورية الإسلامية الإيرانية موقفها المبدئي والثابت بشأن ضرورة احترام استقلال اليمن وسيادته الوطنية ووحدة أراضيه، وإنهاء الحصار غير الشرعي واللاإنساني المفروض على هذا البلد. ولا شك أن الأمن والاستقرار في غرب آسيا ومنطقة البحر الأحمر لن يتحققا دون احترام حقوق وكرامة الشعب اليمني العظيم.
لا يمكن فصل ما يحدث حالياً في اليمن عن تطورات عقدٍ مضى. فالشعب اليمني العظيم والنبيل، بوصفه ورثة حضارةٍ عريقةٍ ومشرقةٍ لطالما لعبت دوراً حاسماً ومشرّفاً في تاريخ المنطقة والعالم، له الحق في أن يعيش حياةً كريمةً، متحرراً من الضغوط والترهيب والحصار الوحشي، وأن تُحترم سيادته الوطنية وسلامة أراضيه احتراماً كاملاً.
تؤكد الجمهورية الإسلامية الإيرانية، مع تأكيدها على ضرورة الاهتمام بمصالح الأمة الإسلامية - خاصة في ظل الوضع الذي تواجه فيه منطقة غرب آسيا الشر والقمع والتوسع غير المسبوق للكيان الصهيوني بالتواطؤ مع الولايات المتحدة - على أن حل القضايا المتعلقة باليمن غير ممكن من خلال الحصار المستمر والعدوان العسكري.
تؤكد الجمهورية الإسلامية الإيرانية على ضرورة استئناف الحوار فوراً استناداً إلى خارطة الطريق المتفق عليها وتنفيذ بنودها، وهي مستعدة لأي نوع من الجهود في هذا الاتجاه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90139" target="_blank">📅 02:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90138" target="_blank">📅 02:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90135" target="_blank">📅 02:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90134" target="_blank">📅 01:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gteO9ZACQU0XSoMAUTGdcryoz8UW_T3LGBPisVFIUr5j6ViB15VaQg9s48OFtu6aKRWxQx_w_wgvFuUPJruQ0h61eGD481Hc0vmcDwLlogha6LKQzsoRhVF6JA2s_F0aFa8RCbQ_Cnd2Jg4i7O1T8Ehb2NxUX-tuRecsE3y8ObSiLklHN6y5kvDDOWRpWI0HzsfNFRO8x5bvhX0juzhiS4MhsmmqKUA8_VFz7F8dlBtxplVLMeMcRpIcLKXSgzjlCulsiegigc7WOFUcYMK0bKQgotfpXJmfLRdR2ah2bliWwrkzOTpxL6-2XBVE2SKz3qPQ0r_cjaTfmBt5bSp1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النفط يلامس 110 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90133" target="_blank">📅 01:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇾🇪
الجيش اليمني يطلق عدة صواريخ نحو مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90132" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
