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
<img src="https://cdn4.telesco.pe/file/KDIB-OpKxWbzcQ73by63KZ5p0-gH_QO0gOl7ZGP6KyJ0uR_TBdImavC3tN2lYUGtA1XqZZQljv8B3U-AAOSlN1ZtJvI2UXsMIasv737eGp6tlLaWyvDTj5gP5wbkv5qsAdeD9dYIRH3gfIR52qqaz0Uf6mv9Jdo9zwfFVfSIGkcQJBJx3Ss_ivQrEGbEPyaVhzU_pEHwvdKwWKeklafrEAlW1vTUZpX56HKBTRDwxAa7rLTWtoS2geui-QGlos9a242z_0xKvK95e6bChi_CdWgJBmPRYUTWIxdtfo4OnrmkPYZ6OLSzMxvkf2N_svoZ---czDlwOVSC4UKXHp0Kbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 01:20:48</div>
<hr>

<div class="tg-post" id="msg-90355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حكومة إقليم كردستان العراق:
بعد اشتباكات عنيفة ألقت القبض القوات الامنية على وحدتين مسلحتين و21 عنصراً سرياً من تنظيم داعش في محافظة حلبجة، وصادرت كمية كبيرة من الأسلحة الثقيلة والمتوسطة والخفيفة.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/naya_foriraq/90355" target="_blank">📅 01:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
رداً على استمرار العدو السعودي المجرم في عدوانه على بلدنا نفذت القوات المسلحة اليمنية عملية عسكرية نوعية استهدفت من خلالها مخازن الأسلحة  وغرف القيادة والسيطرة التى تدير العدوان على بلدنا وشعبنا في القاعدة العسكرية بمنطقة شرورة السعودية.
وقد نفذت العملية بدفعة كبيرة من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابة دقيقة ومباشرة بفضل الله وعونه.
نؤكد للعدو السعودي المجرم أن استمرار عدوانه على شعبنا سيقابل بعمليات أشد وأكبر فى عمق أراضيه وستكون عواقبها عليه وخيمة بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/naya_foriraq/90354" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇦
الاعلام الاجنبي:
‏أفادت تقارير بأن القوات المدعومة من السعودية في اليمن تضم بعض الكتائب التي تتألف من نحو 80% من "الجنود الوهميين"، وهم جنود مزيفون موجودون على الورق فقط لتحصيل رواتبهم.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/90353" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇷🇺
🇺🇦
الكرملين
: اجتماع بين فلاديمير بوتين و زيلينسكي في قمة مجموعة العشرين التي ستعقد في الولايات المتحدة أمر مستحيل.</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/90352" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/90351" target="_blank">📅 00:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق من الجانب العراقي للطريق المؤدي إلى منفذ الشلامجة، حيث يظهر خاليًا تمامًا من حركة الوافدين والمغادرين عقب إغلاق المنفذ.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/90350" target="_blank">📅 00:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">كمين محكم على قوة مكونة من عشر آليات أثناء محاولة فرارها
عملية "والله أشدُ بأساً وأشدُ تنكيلاً"</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/90349" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90348" target="_blank">📅 23:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90347" target="_blank">📅 23:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90346" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ضغط مكتب وزير الدفاع بيت هيغسيث من أجل ظهور اثنين من الطيارين الأمريكيين الذين تم إنقاذهم بعد إسقاط طائرتهم من طراز إف-15 فوق إيران في مقابلة مع برنامج "60 دقيقة" للحديث عن عملية الإنقاذ.
كان لدى الطيارين في البداية مخاوف بشأن المشاركة وكشف تفاصيل عسكرية حساسة. بعد التحدث مع هيغسيث، وافق أحدهما على إجراء المقابلة بينما رفض الآخر.
كما أعرب بعض المسؤولين العسكريين عن مخاوفهم من أن المقابلة قد تكشف معلومات سرية أو تستخدم لأغراض سياسية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90345" target="_blank">📅 22:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر
سقوط مباشر في جيزان بالسعودية</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90344" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
تعرض ارهابي على نقطة تابعة للجيش العراقي في محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90343" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90342" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90341" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية
: متأهبون لعدم تكرار مثل هذه الاعتداءات على السعودية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90340" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مشاهد أولية من عملية "والله أشدُ بأساً وأشدُ تنكيلاً" العسكرية النوعية الواسعة من عدة مسارات متزامنة - 12 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90339" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90338" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات قوية في خميس مشيط</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90336" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90335" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات في سعودية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90334" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90333" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اطلاق صاروخي نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90332" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=SsOcTTCvy3xrQLsYew0epdHKV4ZcD_Dc-P_OLj_ZeZZpQ_kzk-KEmaQu6JnvJxYnJJgCBNxFrnrkiB1o5erUju3bO-fPCsUhGmRp3-sY6u3uPScBy6QGW0JwULnl3F2OFCZ97cCy7I6HgYil4Q_BmD4G8OBHmqecXAOlD4_1gBiUx_3yqAb4uk1vrP9ifuJuwSsQjxYB-Botyre6uaYnl34nMIYfY0QP3JzcXRbFyWqF7G_SHoNIUdGS8YNxDWmJFjiO6I-N2LOIhZoWufVylUoG6du3ufw83Sp2290XIxQ5oyBbyiyzpE7lmM15OuvwRErEoF2-9B9GRKS7NCTZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=SsOcTTCvy3xrQLsYew0epdHKV4ZcD_Dc-P_OLj_ZeZZpQ_kzk-KEmaQu6JnvJxYnJJgCBNxFrnrkiB1o5erUju3bO-fPCsUhGmRp3-sY6u3uPScBy6QGW0JwULnl3F2OFCZ97cCy7I6HgYil4Q_BmD4G8OBHmqecXAOlD4_1gBiUx_3yqAb4uk1vrP9ifuJuwSsQjxYB-Botyre6uaYnl34nMIYfY0QP3JzcXRbFyWqF7G_SHoNIUdGS8YNxDWmJFjiO6I-N2LOIhZoWufVylUoG6du3ufw83Sp2290XIxQ5oyBbyiyzpE7lmM15OuvwRErEoF2-9B9GRKS7NCTZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
من الاضرار التي لحقت بمصفى جيزان التابع لشركة ارامكو السعودية اثر الضربات اليمنية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90331" target="_blank">📅 20:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وكالة تسنيم:
أشار المصدر المطلع إلى أن العراق سيحضر الاجتماع أيضاً، إلى جانب إيران وعمان والدول الأخرى المطلة على الخليج الفارسي. ومع ذلك، سيقتصر دور هذه الدول على الاطلاع على نتائج المفاوضات الإيرانية العمانية، حيث تم حسم القرارات المتعلقة بتفاصيل الاتفاق خلال جلسات فنية بين الجانبين الإيراني والعماني، مضيق هرمز لن يعاد فتحه بموجب التفاهم مع عمان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90330" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
شن طيران العدو السعودي خلال الـ48 ساعة الماضية 129 غارة جوية توزعت على محافظات تعز ومأرب والحديدة والجوف وصعدة وعمران وحجة.
تم تنفيذ هذه الغارات بواسطة طائرات F15 وتايفون وأقلعت من القواعد العسكرية للعدو السعودي في خميس مشيط والطائف.
إن هذه الاعتداءات على شعبنا لن تمر دون رد وعقاب بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90329" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=Qqzvgu7Akr9aEpX_n_aaGcCJWK4t6MNL4cv8KKMDgyGIPLwpjAocCx40lnyGp0dn8SW7yFM7XdQFEo0q6d4CeumU8SdMh3t0kGH0UlvZq3JJLrjUMI_CoSlmjg1JN-yqjW4mc8XGcbSeW6SbUFk_oK7PBeFAjKCjzJJY3rUUBVe-xY_TyJJCCPP5gDRZXKIwvZJyAvDFKzD1pZcy5at47gBaC8JtH2XFRYi1Yyh_yO8sX9X2ujCXeQ_J2XoArtGZs2g-wb2PxvteGavQxcRCQOJBWVFqfjhfIWIC-KYq4428xppuLYewEEnZ2f5ytkVRXr41wUP7RupXAyiDKDyfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=Qqzvgu7Akr9aEpX_n_aaGcCJWK4t6MNL4cv8KKMDgyGIPLwpjAocCx40lnyGp0dn8SW7yFM7XdQFEo0q6d4CeumU8SdMh3t0kGH0UlvZq3JJLrjUMI_CoSlmjg1JN-yqjW4mc8XGcbSeW6SbUFk_oK7PBeFAjKCjzJJY3rUUBVe-xY_TyJJCCPP5gDRZXKIwvZJyAvDFKzD1pZcy5at47gBaC8JtH2XFRYi1Yyh_yO8sX9X2ujCXeQ_J2XoArtGZs2g-wb2PxvteGavQxcRCQOJBWVFqfjhfIWIC-KYq4428xppuLYewEEnZ2f5ytkVRXr41wUP7RupXAyiDKDyfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90327" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM4yXNr3xrSxdu9gXCTmrgjamPaYessoBVERay2YMO2Udt--nUBcd8ut5Afhg2sv6fpBCVtZdKrC70OUknsy6U-eQKEcr--TZQtndYTpfy-hIQVlHLH_JfE8sNMH9T9cguoPFlAAS1NC9aUe03X1OqNuuzUJtjAYIDLGCefaNHlqJ4N1GJxdVQ9z9c3R4eWkjYrqNbFk1QGzWuzSUWpRF9isfP-rpCPC91xDIEboBU3vICxnX1aMrVn5g8j2HxKrQhpw818r1vEMQp4VsSDK5M0ci9Vzhd-6IM7bwa6dmWVcIP-4cdDCwkHNb3BNtGFqLeVwTA_7pgQo5IR0sqI-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90326" target="_blank">📅 19:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=D7qdEbQMH5ntUG3qDZar-9DgTLGhxpZqIoKg8TmI1p31G1dqitQMfGIzzIYDBTD59uH5tNnFRgrGo4EfFmUKTSekxWe0_SxmNPtydGM1KL_3mSLKsiJPRYsAltg85gZ1SjyOqnDUd6bUzpOcSDd25RGe_V29n1_FLbhIgPdkskx8vTAH6Fgvi6jt7eixZ5uq5oB74W2PsA1L6VvPoTDfMOhZIgcj_18XGrwf7aypYJsUCcFDYha4iSPRaZLctY33Pn8q944cSDHklzdyPRzYuhZ5Lmrh38G5_D84lZrrPrnTm16iAonrzb59ugfJUEkmRdwS4R6QNeqVRTCbLZQvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=D7qdEbQMH5ntUG3qDZar-9DgTLGhxpZqIoKg8TmI1p31G1dqitQMfGIzzIYDBTD59uH5tNnFRgrGo4EfFmUKTSekxWe0_SxmNPtydGM1KL_3mSLKsiJPRYsAltg85gZ1SjyOqnDUd6bUzpOcSDd25RGe_V29n1_FLbhIgPdkskx8vTAH6Fgvi6jt7eixZ5uq5oB74W2PsA1L6VvPoTDfMOhZIgcj_18XGrwf7aypYJsUCcFDYha4iSPRaZLctY33Pn8q944cSDHklzdyPRzYuhZ5Lmrh38G5_D84lZrrPrnTm16iAonrzb59ugfJUEkmRdwS4R6QNeqVRTCbLZQvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تدمير 6 خزانات نفط على الاقل في ابها</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90325" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=aMZ19wtOaIBLX_stzX_DJ9xv0lCQXTHR6Lde9LSty8nDJUqpoAw7EerlEhA5bNebGtdUszieBZeVsqFSJ6xUL_BVWVZoDAoKeMXWr1C2WCsmJmTVucMfz0RU3dcWqtgr_7GoRqF-XDgMLsRLBMKdD0znCw6HURF7wsNrDzdNL_mmMiMxW2u4vGtzDO4oO1hkNOEy1sc65dIvHxANGQc_L6MV-42ZNIbukzhmjIxRHOgVxVZ2_y69-ijIdXk2hx5KlByLouX76j1lkXEDWJs5VbD8CdYR2ElV-YurNk6T7vu4BCWR2dDBnp21vh1WoJGQmr9-hSEroj9rRme9JJPk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=aMZ19wtOaIBLX_stzX_DJ9xv0lCQXTHR6Lde9LSty8nDJUqpoAw7EerlEhA5bNebGtdUszieBZeVsqFSJ6xUL_BVWVZoDAoKeMXWr1C2WCsmJmTVucMfz0RU3dcWqtgr_7GoRqF-XDgMLsRLBMKdD0znCw6HURF7wsNrDzdNL_mmMiMxW2u4vGtzDO4oO1hkNOEy1sc65dIvHxANGQc_L6MV-42ZNIbukzhmjIxRHOgVxVZ2_y69-ijIdXk2hx5KlByLouX76j1lkXEDWJs5VbD8CdYR2ElV-YurNk6T7vu4BCWR2dDBnp21vh1WoJGQmr9-hSEroj9rRme9JJPk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90324" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXeSsTMQt_PiEVj99v2PwADfmHow_TdPQA-FQO8j2mTenLiKeET7pBO1XvMb4mibBGCr8LvOnMF44lR4DFTSOed8ZsuCMmJY8SKWPDSFspqpjRTgoTICzRKaMOfcSIm0lN9s8zM1c8cioz62dwFcsVMXUnmAu5FKGRcCXtFYYFv8IfSFfo7vEQ981xOWD2r_VcTMLmULjqSJHAK7Uhp8M2ZVJDI_VpmgsFNLWcZZyDg42JUdL0CBi6ywq_7tIUWyWwG7SH3stPbyoXoj6jRRFU2ZtzkHB1s6GCy6sbS5TN50jwCv5qhwIlenCBwO2FCiUJTBZ_jbae5Ot9uINiphug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90323" target="_blank">📅 19:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">العراق يعيد اغلاق منفذ الشيب مع ايران</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90322" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية: باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90321" target="_blank">📅 18:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تفاهمنا مع عمان بشأن ممرات العبور في مضيق هرمز لا يعني بالضرورة أن المضيق آمن للملاحة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90320" target="_blank">📅 17:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية:
باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90319" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وتسيطر على مواقع استراتيجية بعد اشتباكات مع مرتزقة السعودية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90318" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">القوات المسلحة اليمنية تعثر في باب المندب على احدى سفن العدو الامريكي والاسرائيلي التي دمرتها القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90317" target="_blank">📅 17:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات سمعت بوضوح بالجانب الشرقي من السعودية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90316" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90315" target="_blank">📅 17:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النقطة الاهم في العالم - مضيق باب المندب</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90314" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkRdcCEu-_jdvWfLHG-Jmjeh5Wb-4qtdhHms7GFW-SI32XI8rULAITYzYj-tyqeEAah2bmnBS7aLY9_-LUDXExRU9qtgpbkn1n6WBEFqzXYca4EZemgYU2130kjroIYs4qI6QlQ41po3vhKA3mVxKB3dJy_G54uvqf8MtlO7cLUZ6iXgIXfNK3zYcK029qEe0Nhi6oauTlf6COQAiSa1zB7TUFTOecjcWRR5V2nZE-QmQXreZgB-Tu6ltWocjPQhIsFCalFyKF7Ytcky6CT1rjgacKOSe48ppQ4xoFhSDCA0DkHGmZiD6i0jyolGGspVcmYtlKlFL8ez77kDFRKr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZD1q5hPu7tPOD9mytmJ4ztZdlTNdgL4U9uWCT5JYp-gD9C0PJyqx4uX-zRWoX_Mt-FhuLNfbGIszfe40Hz33CfYZc3jx5YTE2Z2R5J0AriZ2UQXh1tlAlSQCFxQ_kqSf_rshK0sAAeR7lqIcF7ECB3ori-83NTFbktoWbCzSL1fXnMgRLebR8Dr_wWS1kw077NbRlSUzaBm_kl-s-047FiaHtdrl-Z8GbLe0ZE6owMcedsHWh5XCrS7qd7NY0KSaedXjglQJm8vB4GmeXyq1sPfxgPus0vDNeDAN20VNJ9zGohKEg4mO2ON9eMk7vkwpq3IxYz20OUbBJOMxNyNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUsYoLM-72KswNoia4xwrJOzo8S2JRRrKqWER57hUdDN97aXBt-zggLR5hRHOfRq1AWOcig4i1N9JUofJ02UoAfoeV9Wufa7cVXU_YzOnN-K2J6ymazqPHEnpu3ibLKsmnJ9-qfllE8uHoyMDVdDrAMcM0unm3YLbFEwAaNTXONfjxEf2RwAmqUuorVJimu9xrsNxVHfMsxXt_VF3FhsEz0QnJSoM9dRIx2WMj3T7xV8p5WMfGZWmYhjkncZDkXilC_yOXjCYeWBeK5d0r0qUHOflnrVH5oDNnQlrMnYuTIGHFKcVhkujiIN6NhQ4tAQW-rbEnnDn5a0HflbifDafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BObLPwF21YqYyU-khCaRtXno5ZZMYsKeKsQgaPvk6Oxi-NMVoTxbTJV4kHmReuhrHSfAuiUk49OU4vpOOp0OW-3mQRxS60xDAXVmA6k7QQWj7kGDhFj_kSzxyXZyXYT2pIchOC96-YoY2Cni0QiFdnw2tPiPUST_-xWPv8yU-lpj-u_Ee1HDahUphZnY2TgxZBneToFs7gF-k4hM4q4TCKSRX3DZ8pov-N9vzB5gb77o30qtfIzQnuPXOV7tBHzy2hq-lyvjzgnEDJWTzocy0G9FT494EZdPrIWQKexwzLmXIqUoCkzgEB21pyDY3g4Zeq-S6n0X559OFHiPgbsR8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ادعاء المرتزقة يوم امس انها سقطت بيدهم.. محافظ البيضاء التابع لانصار الله يتفقد أحوال المرابطين في مديرية الزاهر.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90310" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
🇮🇷
مكتب رئيس الوزراء العراقي:
الموافقة على طلب الجانب الإيراني لإجراء تحقيق مشترك بشأن العثور على منصات إطلاق طائرات مسيّرة قرب الشريط الحدودي العراقي الإيراني.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90309" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">المدن اليمنية تواصل استقبال الاسرى المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90308" target="_blank">📅 16:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90307" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90306" target="_blank">📅 16:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
🇾🇪
نائب وزير الخارجية اليمني:
النظام السعودي يسعى لتخويف المجتمع الدولي وتضليله، ونؤكد التزام صنعاء بالحفاظ على سلامة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90305" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
السفير الروسي لدى اليمن:
نؤكد دعم بلادنا للجهود الرامية لخفض التصعيد وتحقيق السلام في اليمن والتخفيف من المعاناة الإنسانية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90304" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">التلفزيون العراقي يقول ان لجنة أمنية رفيعة المستوى وصلت إلى منفذ الشلامجة للمباشرة بـ"التحقيقات في الخروقات".</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90303" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90302" target="_blank">📅 15:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv-kuoiPT4GY5VqXPoUFb_TBkFOMDdWpRtNi5ZEv5Og9_qcRA5yuVSw6mehSBuuXvaLNsQHvMKkOKLxFdfm3Cblgh66p33hrru1EU8HNO5iMHSw5gOMDzd8g8S1iawdPbQ0NGxmnDdM56d24mMpRf4Y18OWfVykIfEBtZYFII8icf-vBSPDl1EuiWGCx-_HwHKUmRwMKA4Gl0k9iQU1mMgMLIBMfGzJaBZwy2soJnjiFtp44bAA2Ku_6xZAbTZaGVKcv599-IVUHBP0BcoCjwGdC05VywsVy7uVbG-gLKRHXq6T6iKJUUFpKrITLhA7D3UCZbZnSnK0EkK62APeq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90301" target="_blank">📅 14:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشاهد من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90300" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90299" target="_blank">📅 13:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90298" target="_blank">📅 13:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه بالسماح بدخول العالقين من المسافرين في الجانبين بمنفذي الشيب والشلامجة الحدوديين</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90297" target="_blank">📅 13:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90296" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=FiWFqMdsas9ZMMTbgPD6h2MNfeRcnVoj06hkzNyCFW11-o1EmfVLxlfso4-ArODtPXUOzIO1z1iySJXVTU5ioW4W3_m-ovsx1qKdvS4Xw_Y2o98xCPw8LJZ57ckaYznTh9_PQY-7bG9MqO2ScxSdEk-_0IU_0Fu3_G4anh3jvspXnw7fWYTZvoU7D7WM95qON-EQfwd6mnSQ5_CKb0rVsteTzqvo2Za1-Mg9Fxy6QqoD8JFiEP1MFg-RiFTWwje3hKOy8SOaBXIB6UCIHSx19Zj6MV4ur07H7c2GEM9E15R0SZcQHHRoX8SnA2TY671hIeM6Chi_76KuFIrERLOslBthkE-teyWrnG_tohjWzG_kyccC7XMQ1E7zgOqGplekNzaTewZhGnQzH1-Yv13ZMHNvJJqMtQ5YbLNCeJ5y0bVTaG8kDdAma3ycdrDAjRrJu7y-EQqgKPid4wVP3xUMhMuMU6F1X-EkxtBqxuvemR5-Ub-xcUDb9h_XnnSmBfPXigByAgW_dUiSX3RKInCK0JrLPVWbpIbziDeRnKIY_FwAUdNyV7Waqf9fQrC1vEM4SoTJB0Zy2BuYVwzA2h2n1k9akybVAu3LJVc5nsFZ-uoHiXyEx0xPxU2-T_JBFCrFgz1wFCjkE6xt_1gLq-Y6-9B8w-m9gwy0ryGdCb1e7U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=FiWFqMdsas9ZMMTbgPD6h2MNfeRcnVoj06hkzNyCFW11-o1EmfVLxlfso4-ArODtPXUOzIO1z1iySJXVTU5ioW4W3_m-ovsx1qKdvS4Xw_Y2o98xCPw8LJZ57ckaYznTh9_PQY-7bG9MqO2ScxSdEk-_0IU_0Fu3_G4anh3jvspXnw7fWYTZvoU7D7WM95qON-EQfwd6mnSQ5_CKb0rVsteTzqvo2Za1-Mg9Fxy6QqoD8JFiEP1MFg-RiFTWwje3hKOy8SOaBXIB6UCIHSx19Zj6MV4ur07H7c2GEM9E15R0SZcQHHRoX8SnA2TY671hIeM6Chi_76KuFIrERLOslBthkE-teyWrnG_tohjWzG_kyccC7XMQ1E7zgOqGplekNzaTewZhGnQzH1-Yv13ZMHNvJJqMtQ5YbLNCeJ5y0bVTaG8kDdAma3ycdrDAjRrJu7y-EQqgKPid4wVP3xUMhMuMU6F1X-EkxtBqxuvemR5-Ub-xcUDb9h_XnnSmBfPXigByAgW_dUiSX3RKInCK0JrLPVWbpIbziDeRnKIY_FwAUdNyV7Waqf9fQrC1vEM4SoTJB0Zy2BuYVwzA2h2n1k9akybVAu3LJVc5nsFZ-uoHiXyEx0xPxU2-T_JBFCrFgz1wFCjkE6xt_1gLq-Y6-9B8w-m9gwy0ryGdCb1e7U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90295" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlPIee51qYe7KoHMBT4itfUImadT3i-u4pjXKcKonrvO4QxLaqz82dsd3ItVJuT8oRiXs7X4cX7yX0UcBXn2KBYV0fI7xTWuP9FKybp4TqBVRs-KBnwY-WZS96Z7b5qutE-NLPDS-CidQe3IhqIU0Yt7JDeoAKxwsxMJJ5PZiRXNVMGXkqLNdHoFEHdspNoLVF8u_Br5jOsG7zwiW6Tv2abs6wZrbO8LYl8jZgsxOi6iuE3YFxtAWCmb7PJ-HXcou3JuiY72-RZyHvg_Xdw8XnkDaW66DNodrneh1GxcIadyYj4VY_CpmsfZKWV2Ztaod3pUcQ0hDyvcp8Vf-dNJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي لحركة النجباء مغردا:
نشعر بالفخر والاعتزاز ونحن نرى هامات اليمنيين مرفوعة بانتصاراتهم المؤزرة.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90294" target="_blank">📅 13:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38811a403c.mp4?token=eukRn69TQ2osOHJDXV3dz2IAGzaxcltHeSvYPRwOc8nfc3_6N2jXFLD-OsPeOaUgjgnOznoJXorG_yBCbolY2CBWv38pbLB9z0ilwe_irndmkkKxIxJfZA49nQ1bJMZPhBPfUyojJD2MJcwvuHQj6UOCCVtt3u2cSE0n1wPhyKghykCbJOQJdMa1qYt3GApvxeoqndxBZiWlphuVIGVx9dbRVNNwluJpP-Z7DOdJvMChyRK4agSUkk8Rg4wkjNhEcIbDXcpTClRJjjqp77k807iBiIW_lzF76cnYo7xVIwYSwlk66ujUAlRnPwPtETFIk5p4Fq5o0NBpM0IaGx9L4rKJtLZMQ2rqGPUZzbdc0jt5FyeXy1iOYy8ryTC_Lhd6dCo1qqgermHJrbnC6i-_M0OiUbWzR9VMrTl3HvcZ_pTd2NNf4bGUc_fhP7CmXTvPWdSHLvEw6NMNagQGbvAH_oLroejTGtAes50eovqugk8BOAyaG1xI_fJHBgpOgJAMg5PqwqIjidbDSKxixpc6Xnkugh0O7CL2IwNzJTn9vCFPBXahN0cpneBBT6hTOeSK2_tu_wTA2FCZDt68ghEC1Ld10irqroPyxYvzwNv7swuYr8jdwvf-05HQEv4YDig_0c9aoe_BzJPsOqHh_Btq0tIgD3G6hcJv_Yi_n0mq17U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38811a403c.mp4?token=eukRn69TQ2osOHJDXV3dz2IAGzaxcltHeSvYPRwOc8nfc3_6N2jXFLD-OsPeOaUgjgnOznoJXorG_yBCbolY2CBWv38pbLB9z0ilwe_irndmkkKxIxJfZA49nQ1bJMZPhBPfUyojJD2MJcwvuHQj6UOCCVtt3u2cSE0n1wPhyKghykCbJOQJdMa1qYt3GApvxeoqndxBZiWlphuVIGVx9dbRVNNwluJpP-Z7DOdJvMChyRK4agSUkk8Rg4wkjNhEcIbDXcpTClRJjjqp77k807iBiIW_lzF76cnYo7xVIwYSwlk66ujUAlRnPwPtETFIk5p4Fq5o0NBpM0IaGx9L4rKJtLZMQ2rqGPUZzbdc0jt5FyeXy1iOYy8ryTC_Lhd6dCo1qqgermHJrbnC6i-_M0OiUbWzR9VMrTl3HvcZ_pTd2NNf4bGUc_fhP7CmXTvPWdSHLvEw6NMNagQGbvAH_oLroejTGtAes50eovqugk8BOAyaG1xI_fJHBgpOgJAMg5PqwqIjidbDSKxixpc6Xnkugh0O7CL2IwNzJTn9vCFPBXahN0cpneBBT6hTOeSK2_tu_wTA2FCZDt68ghEC1Ld10irqroPyxYvzwNv7swuYr8jdwvf-05HQEv4YDig_0c9aoe_BzJPsOqHh_Btq0tIgD3G6hcJv_Yi_n0mq17U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لغنائم القوات المسلحة اليمنية من مرتزقة السعودية بعد فرارهم</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90293" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8TEKzsZ4j92gC73CsahLtydwFWN7qWYiXwb28vYigM_8JJOOrJcqJxZ_duY5Fx_Sy_B2UOBwMhIgU9LNNmwnBsqPVgNYIPC7u28tXHkGYwoca6vQy5nfgoTjbzn6FVXqOGXe1tMeaV1sw4Hvc0fE6W7ch2unAlpl3iokzyRIVd4VrnJBCsZ4MhOQSxk7eTTNwyeuHm91vs1GPq9loWw5QZzRUh3TL4Qc68YeFa-UUrmY1dlfd2-VI86myDdbI0hG3Y3_T725PIvBqn9f8r_U_bj_0eHMVjuwXoQ_N4DITq-nmpeBtBUDOjzomf2Dp1OcSl5CPUGHUzgl2iaQwxi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
​في الوقت الذي نبارك فيه للشعب اليمني الأبي انتصاراته الميدانية المتواصلة ضد القوات السعودية ومرتزقتها، نؤكد: أن الاتهامات الموجهة للمقاومة العراقية بشأن استهداف المنشآت الحيوية السعودية يوم الجمعة الماضي هي (شرفٌ لا ندّعيه)؛ ونُعرب في الوقت ذاته عن استغرابنا من تسرّع الحكومة العراقية في تبنّي هذه المزاعم دون الاستناد إلى أدلة موثوقة أو تحقيقات ملموسة.
​إن تكرار سياسة إلقاء التهم وصرف الأنظار لا يعدو كونه محاولة فاشلة للتغطية على الهزائم المتلاحقة التي تتكبدها القوات السعودية وأدواتها على أيدي أبناء اليمن الأباة.
​وإذ نجدّد تأكيدنا على الموقف الثابت للمقاومة العراقية في مساندة الشعب اليمني المظلوم والمحاصر من قبل النظام السعودي منذ أكثر من عقد، فإننا نحذّر من الانجرار خلف المخططات الصهيو-أمريكية الخبيثة التي تسعى لزجّ العراق في أزمات لا تخدم إلا أعداءه.
​وختاما، نُعلن استعدادنا  للمشاركة في أي لجنة تحقيق حكومية بقصد  الوقوف على الحقيقة، بدلاً من الانسياق وراء الروايات المشبوهة.
المقاومة الإسلامية في العراق
12 أيلول2026</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90292" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdEVYYtjZWoh_j7wUb9eWx3OOowm-emGOmdc01-vheeK03TdKqhWYGUhoeQIQ_CyijXtkq-0YmkXCiwwe20_FO8FBZulWzUncg0hZOiGxVBGVN-3VBcxmlOY08OGkPxQ53Z87fsmEuzF80FHIYXIjhuZdbV1m637jQv1Gg056mXDXdsQNjrWjJEuBRYSgv-hjlVfE2vUEd5r2zwO8r-P_Vih9qjIndzjZRa1tzXm0C-3qbw5C4AqH7Iwznw_S9BwbwvYvzGQXY6132tqcr2_StFbQrNOE4ejWFvHg7h4jdxuBfmMdqiea7CeJ9Jqnd3kP86_1BokyqAC1TLWQnIiko7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdEVYYtjZWoh_j7wUb9eWx3OOowm-emGOmdc01-vheeK03TdKqhWYGUhoeQIQ_CyijXtkq-0YmkXCiwwe20_FO8FBZulWzUncg0hZOiGxVBGVN-3VBcxmlOY08OGkPxQ53Z87fsmEuzF80FHIYXIjhuZdbV1m637jQv1Gg056mXDXdsQNjrWjJEuBRYSgv-hjlVfE2vUEd5r2zwO8r-P_Vih9qjIndzjZRa1tzXm0C-3qbw5C4AqH7Iwznw_S9BwbwvYvzGQXY6132tqcr2_StFbQrNOE4ejWFvHg7h4jdxuBfmMdqiea7CeJ9Jqnd3kP86_1BokyqAC1TLWQnIiko7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محافظة الانبار..
ازمة الوقود مستمرة في مختلف المحافظات العراقية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90291" target="_blank">📅 12:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني: «يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة. حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90290" target="_blank">📅 12:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9397297397.mp4?token=oHiS7oe3n00gd3lf61Qdjytm7SDvxMy1jD0IJ_GiNlUt9FyahBAnsGCh37WCy37K0N_cI27Y1D8zlIzInZus5Y-rub349aFWQuS9F0aKgpFyqshfqZ73AMRk2m9dgrknQD4l0O4Slamjt7FuoHFYTgZUWzYJf6qmL_-WNN7ltxZHlSzRRSYwYQA6g8UsZSxr0rQ55U5qDc26eT4Q1boPM4BloNLs1nVW2TzCxfEnfdarYitHvU9jq1GMseveK8D8xj0a86pVf-3LWqPNuiQc5kldmHiq-iiEbXCqGedMuYqSMuvuVP-it06ZahpB91XdjAAimD4TDIj6quk93ULcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9397297397.mp4?token=oHiS7oe3n00gd3lf61Qdjytm7SDvxMy1jD0IJ_GiNlUt9FyahBAnsGCh37WCy37K0N_cI27Y1D8zlIzInZus5Y-rub349aFWQuS9F0aKgpFyqshfqZ73AMRk2m9dgrknQD4l0O4Slamjt7FuoHFYTgZUWzYJf6qmL_-WNN7ltxZHlSzRRSYwYQA6g8UsZSxr0rQ55U5qDc26eT4Q1boPM4BloNLs1nVW2TzCxfEnfdarYitHvU9jq1GMseveK8D8xj0a86pVf-3LWqPNuiQc5kldmHiq-iiEbXCqGedMuYqSMuvuVP-it06ZahpB91XdjAAimD4TDIj6quk93ULcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني:
«يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة.
حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90289" target="_blank">📅 12:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
مديرية شؤون المخدرات العراقية تعلن ضبط 150 كغم من المواد المخدرة وضبط 3 متهمين بينهم أجنبي بعملية أمنية في مياه الخليج الفارسي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90288" target="_blank">📅 12:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق يعفي قائد عمليات ميسان من منصبه، على خلفية ثبوت انطلاق الاعتداءات التي طالت المملكة العربية السعودية من أحد المواقع داخل المحافظة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90287" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvCdISbTUmfGdcx6OXocSU4fqPT7CYNL2twyx4IZE3ulpCRWqI_kbi6mxuopCLf54FdPJiNqsSUvoHdhmJkITqGK0LSoiCKgVc9h_Snq-IUGq-8ERvCAyadAzsD1UCmrZnGndITPPvbdmgh3UVA37SlXyR-HOxQSvY7HeHovdo185WCESXQNUSqrHiK-kjZ5WJhAC4B60qw9sH7U0AdpTG45fFhxN-vat88qCjQGmkQPv1wlfkqdhmMEN9PeYdJXKaHc0KeNiPMGJ9fTrrNJHHt0LuptzX0z2a4FIuW_MBH8NhBNGTGY4zJQeHXLmYSKP0ncrEHet8SSl1Wc5KQZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
طائرات النقل العسكري الاميركية تتوالى في الهبوط بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90286" target="_blank">📅 11:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
مصدر ايراني...
انفجار مسيطر عليه في محافظة اصفهان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90285" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKd2MNWRdpqCc9IX9G340O5O3bWcsz-qo0M1IUXhzKj004GJQhDxrD04-T1rzOHdDH48SVAvMrc5_4fU1FZ3g2hX6K_GtznGFYpuAzlz7OlLl9emcPUfhuF3F1NO-E_eFLH2v-9xH8Oye-Ivd0KEJJpTssLb0lXmFMijEas6Gq9BEI6NReu8SKt1ArpZUq2H8FH4YHWi9D40FgksYHlGvwfzRrJjBzZ34xX607Qyu51QJeRtFDtgEjE9k2zQkYFiRKcbuC0wnauJfJKw3EdVFMowUydw84W_wScOhmso5bd3X9CyU466rLNSxkj89ZJPvSoHRrn2JNbDDEPkdxgN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpFULMh73AFxsE6y3DB-JbAcrXzFnV10wKCZkyaf55PgFX2XOgQ7B-Y0MWqZIbAPA87QCTpZ79uUgUSSXnOb1nZ6QQrWAA80jGZohj73tS8iRfYkXEsHcCcOuqkhBBbhYBvjc_-2ErGIJ93ECW21giSDZ7IrhN373YtYrHO7G5mWPHx48C8b9BKWlO_uS5wsS6VScjTfDk0_kRjMbpUyhWintlu-koIO2YKfrNIw3e-flGFIuMzTZfn2y7er21rUe1z9bcz-UTmApTRtSaPv89o217mty7M8ahNka1OvTCzaG996qvus0ZR9teGCFbrlR2txeQyubKKbFQhK_dF-Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
لليوم الثالث على التوالي...
استمرار اندلاع الحرائق في حقل خريص النفطي التابع لارامكو في السعودية بعد استهدافه من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90283" target="_blank">📅 11:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeOA8v5z5PJItNv3Ugrn_X7MRFVBzjc2YZlaL3tG30O2crqUCA9bvty-oppgLOxRlURLu-bX0o6nQQy_IjTQW4lLjvW7PJ3Kvvxu3VRzcO_l1BJphau5WwBjuPF31Q_Ei_NFR-ZKL_Z7VnnycDb5xrvzO7JJa5pbEXajRNQCWbBudArXBXP4mReLKJbJqr5ImLZA7HX9fexq0J3DqbYHCyZyx8L_Gb_H7c4t3nkPM9LsS2ogZEIVuf3bq5Vw13ciOUAIOsdNbWWSZgFsAvScCL31_0gPX8xFyn3YIzI5fRb_X1JO_0W0ZmUgHyMy916Kv9zAPNPY3FifgAMn-JR9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
بسمه تعالى
لا يستفزنكم القوم
فهم يريدون تغطية سوءتهم بفتنتكم
فلا تكونوا عوناً للفاسدين ولمن يريد النيل من سلامة العراق العظيم
وحافظوا على وحدتكم وعلى وطنكم.. واتركوهم في غيهم يعمهون.
نحن وانتم فوق ما يقولون والله فوقنا يحكم بالعدل والإحسان.. وهو يحكم بيننا وبينهم بالحق في الدين والدنيا والآخرة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90282" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYqVmmsCyo845_FK3CwEgSEkKqqmNcJ3OcG4RrQJ7X-hiFsEZTyeAzFciP8VjJOyAskLsIs5AYuHgtb-DjOwnuKhZo9Lck3SKGXbOnMexHs8dNZTIBKPu9hx0hFLgtRxvyiS104oFdxV9EtjqEj1KuOT4P1I2zmRomNh8t5zXHxWRMwfL5HgTey5TzOoRAGpKmkFTg2qTgrl8okzlF53qlHSs8e_VJLJ-LpGfRb7RREt4dE-dnxmJT5ceyhS4D9hNTQ7aM-t1UPJc_bpXEEuQ_-WBO6UAW2c3XOUuayPDNBFHt9v-HCwQW4X2rKz5Kz6Y96pvYZmNoCwKyXeJnO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأردن يدين استهداف الفصائل العراقية حسب ادعائهم للسعودية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90281" target="_blank">📅 11:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">طيران مسير أمريكي مكثف في بادية السماوة جنوبي العراق</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90280" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
اتخاذ سلسلة من الإجراءات القانونية اللازمة وتكثيف العمل الاستخباري والتحقيق والتدقيق لمعرفة ملابسات الخروقات والمخالفات التي حصلت في هذه المنافذ ووضع الحلول والمعالجات المناسبة لها.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90279" target="_blank">📅 10:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇷🇺
بوتين
: نشر قوات أوروبية في أوكرانيا سيعني دخول هذه الدول في حرب مع روسيا.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90278" target="_blank">📅 10:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار إستهداف العناصر الإرهابية التي تكمن في إحدى مناطق مدينة سراوان من قبل القوات الأمنية الإيرانية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90277" target="_blank">📅 09:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
معبر مهران مفتوح، والأنشطة المتعلقة بالسفر والجمارك مستمرة فيه، ولا يوجد أي إغلاق أو توقف في عمل المعبر مع العراق.
خلال الـ 24 ساعة الماضية، عبر هذا المنفذ 17 ألف شخص، مما يدل على استمرار عمل قسم السفر في منفذ مهران.
الجمارك في مهران تعمل كالمعتاد، ولا توجد أي مشاكل في عملية تصدير البضائع.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90276" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان الإيرانية: وفقًا لإعلان السلطات العراقية، تم إغلاق حدود الشلامچة والشيب في محافظة خوزستان اعتبارًا من صباح اليوم وحتى إشعار آخر، ولا يتم حاليًا أي حركة بضائع أو مسافرين عبر هذه الحدود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90275" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUNaUG-SjwhZFLafxEHAx_RrYHJW_cGayYRlte0hpF7Yl3ZV1fsJW3kyRBQdQaeLfK9bOugGAn-EPErd7D1ANtQStsc9-H8oErOrt7CVoPLUaJbyxHkEDmlESp0EFh3H0Vn-yNGQMFe_2_ECjSB10saMCFdVC4bGG3zH4LJecj1e3XCWbQa-7GeEx29prrZgNL22uKFFv7hxdHOKsXHrTGOgMD4xE0coSXr2jVBYoGY1pFpk0GepRIWWH-9ctmrumkRUiI00Lk5bITqMDxnmhesxLihvcvkpQ0D4icR_oN-q_9DRjh96b64fClK6emlIb2K3537KP3-l5cIwyY_FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ مهران الحدودي مازال مفتوحا أمام الجميع وحركة دخول وخروج المسافرين تسير بشكل طبيعي.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90273" target="_blank">📅 08:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان: إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90272" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90271">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان:
إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم وإلحاق ضربة قوية بهم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90271" target="_blank">📅 07:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90270">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90270" target="_blank">📅 07:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار الإشتباكات بين الأمن الإيراني ومجاميع إرهابية في سراوان بمحافظة بلوشستان.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90267" target="_blank">📅 07:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90265" target="_blank">📅 06:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90264" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الإشتباكات العنيفة التي تدور بين القوات الأمنية ومجاميع إرهابية في مدينة سراوان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90260" target="_blank">📅 06:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اندلاع اشتباكات مسلحة بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90257" target="_blank">📅 06:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
مسؤولين أميركيين:
إيران حصلت على صور أقمار صناعية من جهات صينية قبل قصفها قاعدة بالأردن في يوليو، حيث أسفر ذلك عن مقتل 3 جنود أميركيين.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/90256" target="_blank">📅 05:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇦
انفجارات عنيفة تهز محافظة شرورة جنوبي السعودية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/90255" target="_blank">📅 04:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مشاهد إضافية من إغلاق منفذ الشيب الحدودي مع الجمهورية الإسلامية الإيرانية من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/90254" target="_blank">📅 03:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عوائل عراقية تقف خلف أبواب منفذ الشيب بعد إغلاقه من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90253" target="_blank">📅 03:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90252" target="_blank">📅 03:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q46vqLFRRcjhDFSCttbgp0yiVv8-PwBWvoU3Btdl3cbG3ZlwMz3Z2hfIi80tnkMoDPMLrqOwLsOhKWDzUAT0vURdJfefl4pDT7c4c56uIP8zmfGFrxfik-PmCUJ6lgaVip_xzOmaTZMEnH7i1YX5IS9DJw7MTM_v9V_baRD0lTkV9mYAzxTmkUcTloEOTZFJU06tpG5i1zQDhaEzGpP--bV09MKSXKsuobuENO3u02WLlrh-ZZmrBPMiuZ1MPISv3hGXSbsZ7NDrZqgcNVugy8LOtjYcecG1gYsafXepqAq-pBYBFae39aAbT5EZ499ezWa60JdrvUQ6HSDW0Bt-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصدر أمني: إغلاق المنافذ الحدودية مع إيران شمل الشلامجة في البصرة والشيب في ميسان بشكل تام وقطعي، ومنع دخول وخروج الأفراد والبضائع من الليلة وحتى إشعار آخر، فيما لا يزال منفذا زرباطية في واسط والمنذرية في ديالى يعملان بشكل طبيعي.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/90251" target="_blank">📅 03:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/90250" target="_blank">📅 03:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/90249" target="_blank">📅 02:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/90248" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/90247" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/90246" target="_blank">📅 02:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/90245" target="_blank">📅 02:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
مصدر لنايا:
توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/90244" target="_blank">📅 02:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7o9rptkLYC_aK2gnmBwb8FTptK9itc4YUX_vXR26H5-fCXMv6mvIvTGwpG-ACNxXCfWDvpXJsvRi98Oyjg01fsfieO7v5lcuS4Fb58e72s3l2-LXERcrOqDLcm7Dx61Z54Tem3ez-iHUfMGXRxf7wDsxaOaybKItl-7MgG3Nn6ExpfalgsBDGruhIN3Ny6ajAAo2M4b-VUtZQiJwmgFF7fqWjz7gPxs0H3hZr7vUgKcZoIwmm1kSApZG3_v4kO18QCMJ4NsAdtzTHycpVJYZCtAPQMX2WhT_Z2XrOCvLwKk1bNx3FBbI7JN12hyyMNXfCOTc3hNLPsII6YJYWLh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
حريق كبير في مدينة ابها بالسعودية بعد استهداف عنيف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/90243" target="_blank">📅 02:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇾🇪
القوات اليمنية تسيطر على جبل جرداد الإستراتيجي في محافظة تعز.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/90242" target="_blank">📅 01:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سماع دوي انفجار مجهول في العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/90241" target="_blank">📅 01:34 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
