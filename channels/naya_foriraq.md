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
<img src="https://cdn4.telesco.pe/file/QMVulSDysSn5NG_2fcnDz8fthwrr1Ksg613eJxavvaiK6z97jfa0HuMH3gbkxSrtCYjuDEsrduQRTtCDNNtnlNXvxnwKV2i7DVM3_CE3CFEMHVp1-gRzmbfDvWzQ8_rmhwGbKsQDjD8OKY8RUy0iWvVNrZdQZcKh4KJFwb_L662vjLesXWeZ3S7WUtf0rXdppzOXNEtHPZYRbF3eeapvK1BBKimpURY6vXOqTDkj6OT2OzAtkZzW90UYuORjHjYD4Kh8ANiWLpNdG_YpeSdj2d7lQS44W3K9SWcpOHgp-Dj8mL4s_YrM1dtyH0QuRdNT_N8RvPDRTlXjo-InxQFj2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 08:36:54</div>
<hr>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av34mI9wSoWnf5qRORFOumbDo4LR1PysNsArZyGvfFOP0TCUQrY0jJs0GLFdMN-teVu7xaE9OyeOtIsaJlZi836r1jgbLQTDdhnrvmw600GzAXjS94GB2AcJZTN9nYq7GTBNBZzLuQ3CGt35kp2nZHymFemmZiScMyn1nLi350mi_V1JGhemDjAyLsAscH_tBMdFcsh6LqZiYj5xGYk5JoaQy0XIdPUp_ll7g1X9L1gtg5CKYDoKDfQ8cESYPBR-c_ubJ4SFvAS2UrGF4eoMtMhlEU4tGz8gFi7T1PyycQSEZr9EjbRErJEN9u-mm7qku_C5ynjAW-815--pJnNdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب
عندما أشار الرئيس شي بأناقة شديدة إلى الولايات المتحدة على أنها ربما تكون دولة متراجعة، كان يشير إلى الضرر الهائل الذي عانى منه بلدنا خلال السنوات الأربع لجو بايدن النائم وإدارة بايدن، وعلى هذا الصعيد، كان على حق 100٪. عانى بلدنا بشكل لا يُقاس من حدود مفتوحة، وضرائب مرتفعة، والجنسانية للجميع، والرجال في الرياضات النسائية، وDEI، وصفقات تجارية فظيعة، وجريمة متفشية، وأكثر من ذلك بكثير!
لم يكن يشير الرئيس شي إلى الارتفاع المذهل الذي أظهرته الولايات المتحدة للعالم خلال 16 شهرًا مذهلة من إدارة ترامب، والتي تشمل أسواق الأسهم والـ 401K في أعلى مستوياتها على الإطلاق، والانتصار العسكري في فنزويلا، والتدمير العسكري لإيران (سيستمر!) - أقوى جيش على الأرض إلى حد بعيد، وقوة اقتصادية كبيرة مرة أخرى، مع استثمار 18 تريليون دولارًا أمريكيًا في الولايات المتحدة من قبل الآخرين، وأفضل سوق عمل في التاريخ الأمريكي، مع عدد أكبر من الأشخاص الذين يعملون في الولايات المتحدة الآن من أي وقت مضى، وإنهاء DEI المدمر للبلاد، وأشياء أخرى كثيرة سيكون من المستحيل سردها بسهولة. في الواقع، هنأني الرئيس شي على العديد من النجاحات الهائلة في مثل هذه الفترة القصيرة.
قبل عامين، كنا في الواقع دولةً متراجعة. وعلى هذا، أنا أتفق تمامًا مع الرئيس شي! لكن الآن، الولايات المتحدة هي الدولة الأكثر سخونة في أي مكان في العالم، ونأمل أن تكون علاقتنا مع الصين أقوى وأفضل من أي وقت مضى!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75406" target="_blank">📅 01:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من داخل مقر رئاسة الوزراء في ليبيا، عقب اشتباكات عنيفة بين مشجعي أحد الأندية الرياضية امتدت إلى محيط المقر الحكومي.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75405" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75404" target="_blank">📅 00:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75403" target="_blank">📅 00:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75402" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY_1KfQFVnVPeLuKIBMepibmfyxwRL7Me81jwvwk7mYRLV-hBR9FD6VxVDTp-W_VI_8CXj3ta8H90U1RjKkpzyke74s7yuyIj3LVLpRzapz2jRHp0aBYY5mtpSuu2dZK8Iq3jYqAeQ4p42V0A7pfXxSvZOM9CKr1oCcA0AAapNW0ElM7xdKwGzHRQSj47OiGpiSLurCbE0PE5SJJ8xV0GVnM8bQ1dPAiKw6ijyz_E4gbSOBCIMWzDeGOt_5uGWQIrPyshxzZANOK-d4_JptjhyQm-dYIhDwFdwYJaLlAxVIs89cdfLHxpI0Txq0GyQ4rCZQUqa_DlbzrhF4wu08Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75401" target="_blank">📅 23:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75400" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROZfHazcKFWN90ZUdZBd47KyoKddor-REkiPdxbxviNS0W9w6HvsBXWcBsiO-GkPDd93kge6jf3g6LexglMiYTzvFV5bcCXxwrI3lIetq-78cS89kpyJ9XRWp1-tMw8a4pCRL51Yp3vCtR5rm8ygQGg0wGf-pSTZiEZhqqOwy5leUDZtcgVlkhgnNFwZ4j-UV4AYCImZt3732M0pYBBYscTarwqG0IarcIN7ED7hVWf1JXWQw26rbTmGhImn_40cAzipoDIW0WGXDbVcsKuZFHmzkpP74k2zbMzMpdKoalwYiY9gY_nURJyPoMRhccEtkmZ2UpB9xYmnuDSI6mczcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إذن أنت تمول هيغسيث مقدم البرامج التلفزيونية الفاشل، بمعدلات لم يسمع بها أحد منذ عام 2007، حتى يتمكن من تقمص دور وزير الحرب في فناء منزلنا الخلفي في هرمز؟
هل تعلم ما هو أكثر جنوناً من 39 تريليون دولار من الديون ؟ دفع علاوة ما قبل الأزمة المالية العالمية لتمويل لعبة تقمص أدوار حية، وكل ما ستحصل عليه هو أزمة مالية عالمية جديدة تماماً</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75399" target="_blank">📅 23:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#سمح_بالنشر
.. مشاهد من إستهداف أبطال المقاومة الإسلامية في العراق
#رجال_البأس_الشديد
أهداف حساسة في عمق
الكيان الصهيوني
الغاصب
بعدد من الطائرات المسيرة حيث حققت إصابات دقيقة ومباشرة .</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75398" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات صاروخية من لبنان نحو كريات شمونة ومحيطها في الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75396" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية على بلدة على الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75395" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصدر لنايا
يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75394" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "خضريان":
لا ينبغي للكويت أن تنسى أنها سقطت في يد صدام حسين في غضون 90 دقيقة فقط، وعليها أن تدرك حدودها اليوم، وأن الجمهورية الإسلامية قوية للغاية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75393" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
تم رصد تحركات لعنصر إرهابي خطر ضمن قاطع المسؤولية. و​بعد تحديد الهدف بدقة متناهية، نفذت قيادة طيران الجيش ضربة جوية ناجحة بواسطة الطائرة المسيرة المسلحة (CH5)، مستهدفةً الموقع المرصود في وادي الشاي ضمن قاطع قيادة عمليات كركوك ، إذ تم ​تدمير الوكر الإرهابي بالكامل وقتل العنصر الإرهابي المستهدف.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75392" target="_blank">📅 22:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">يسقط حمد
دعوة لنصرة الشعب البحريني المجاهد .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75391" target="_blank">📅 22:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سوالف الگهوة   العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75390" target="_blank">📅 21:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سوالف الگهوة
العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75389" target="_blank">📅 21:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر: إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75388" target="_blank">📅 21:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بولندا تعلن عن تسجيل أول زواج مثلي لها يوم الخميس، بعد أحكام المحاكم الأوروبية والبولندية التي تتطلب الاعتراف بالزواجات المثلية التي تتم في الخارج.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75387" target="_blank">📅 21:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
النتن ياهو: نقول للعالم أجمع إن القدس ستظل عاصمتنا الأبدية والتاريخية.
‏أبعدنا خطرا وجوديا يتمثل في القنابل النووية والصواريخ الباليستية الإيرانية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75386" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf0bEVNf6IFY1Zv6OUM0TUQvR96Hxz0l_y7p0Jxr8q8Sv-UHjzQyTuV-q-9j2GeaVFE_OquuudGCWv11bdiAdHzd3XhgrMDa9bpjV-p-9UH7qHY3Nujjruv2lSyEnFhhcJ1xlliIyEJpolQINW9r45CBIfJQrJi5Z9Idr8I705QPCNSwTJih1Ipt_m_L6x9J42joUG9n4g1fTthVhphJpyrLX5ULWwOTgsDcrMNyBmytN_nmgoIpvOX8JPm_vURtdRipE_mWIuektwMmPPlh3EqJGbuE3dUyd3Ct6UmWMF12doAKKFEIp6x0emtb8KX_bxZsb2DJJX76UJjN9-g3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75385" target="_blank">📅 21:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر:
إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75384" target="_blank">📅 20:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال:
إصابة 4 جنود في رأس الناقورة جراء استهدافهم بطائرة مسيرة إطلقت من لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75383" target="_blank">📅 20:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭐️
بعد عدم نيلهم ثقة مجلس النواب.. توثيق يظهر لحظة إندلاع توتر واشتباك بين عدد من نواب الكتل السياسية في البرلمان العراقي.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75382" target="_blank">📅 19:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b2948510.mp4?token=udSfF-CtgIhMRh_L_I9euqq7kkh7hWMOWELvbkuMQmqL8VfNUoFNxxnEbYttg9L_vZ7JyfFy3LMkAELAvLuzcj6AkumRgbCPKBq6heUXkqPB8VC9E5l9rwwsI-NAAoWv1zIG2UkgqsrEoIx-YGU6ABDmJaMB4PCa5pkWq8wn2cnJMG3zHQTvrjItkG4GinURK9PUdGoJiu2bywY8Ee09dxQJzUwGvA9xKhuW_afsDK7HxKqozLJZCKHCnA7bizHdw9csTb0bUG9S5zBmbDUBbzAyGE3XWtlYcQ6rW2KlNC1YftSTl7XyGVIj8DPHbx-QzViz7HmKwiKdL9NLXu-jFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b2948510.mp4?token=udSfF-CtgIhMRh_L_I9euqq7kkh7hWMOWELvbkuMQmqL8VfNUoFNxxnEbYttg9L_vZ7JyfFy3LMkAELAvLuzcj6AkumRgbCPKBq6heUXkqPB8VC9E5l9rwwsI-NAAoWv1zIG2UkgqsrEoIx-YGU6ABDmJaMB4PCa5pkWq8wn2cnJMG3zHQTvrjItkG4GinURK9PUdGoJiu2bywY8Ee09dxQJzUwGvA9xKhuW_afsDK7HxKqozLJZCKHCnA7bizHdw9csTb0bUG9S5zBmbDUBbzAyGE3XWtlYcQ6rW2KlNC1YftSTl7XyGVIj8DPHbx-QzViz7HmKwiKdL9NLXu-jFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75381" target="_blank">📅 19:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئيس مجلس النواب يدعو رئيس مجلس الوزراء علي فالح الزيدي والوزراء المصوت عليهم لأداء اليمين الدستورية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75380" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75379" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75378" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
خلافات داخل مجلس النواب العراقي خلال طرح اسم لأحدى الوزارت.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75377" target="_blank">📅 18:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75376" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75375" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75374" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">استهداف دبابة ميركافا من قبل حزب الله في بلدة الطيبة جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75373" target="_blank">📅 18:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مجلس النواب يُصوّت على المنهاج الوزاري لرئيس مجلس الوزراء المكلّف علي فالح الزيدي</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75372" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس الوزراء المكلّف "علي الزيدي" يبدأ قراءة المنهاج الوزاري للتصويت عليه.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75371" target="_blank">📅 18:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس النواب يعقد جلسته للتصويت على المنهاج الوزاري وحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75370" target="_blank">📅 18:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هل ناقشت دعم الصين لإيران مع الرئيس الصيني؟
‏ترامب: لقد ناقشنا الأمر. هممم. أعني، عندما تقول "دعم"، فهم لا يخوضون حربًا معنا أو أي شيء من هذا القبيل. قال إنه لن يقدم معدات عسكرية. هذا تصريحٌ كبير. لكن في الوقت نفسه قال إنهم يشترون الكثير من نفطهم من هناك، ويرغبون في الاستمرار في ذلك.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75369" target="_blank">📅 18:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامب: عرض الرئيس الصيني تقديم المساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75368" target="_blank">📅 18:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قيادات سياسية ورئاسات في مبنى البرلمان قبل انطلاق جلسة منح الثقة لحكومة الزيدي</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75367" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhrsk4YpLd8FYMwlG3N9sMuXlOgRkFX6ExYMJRVvY4X9sMmQ9cNGnD6LTkZXPaSQ0qnWJA0FZN50Gqgp39MqXeOe30HhXCratPF2w5Cp9Dc_qWMv5YxavpTzLw2VDYDyWeWyJ7ZCdK_2zVjiuzhyTVJovhILuSl60cLBwR00xC8VeukD1BBtTV1Wr1Zsr-IFD0mHu1KcGEos7lc3sLPY6C-m_ZkAHOzlHZNj765lDboYZXIH5fYcSHk339A5HUZC34I5k7VMtXJwyeFlioLJi-EVJWsratuvH8mzsRWUaOJKOxX6yl1f5rS4w-ZmotKyObZ-k3GMIwDlpOEF_jKXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرع جرس البرلمان إيذاناً ببدء جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75366" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piOZ88IsIQgAM7-rZcXSOXGLDAvi6w_mU1FOo0H6MjRJSFlhLHk_AJUew4lSp-NwwPoMXBXQ55ZrSzzh7r6W01GObnBxkHnf_1XO78b4OC_OUySrr85sxHRqfNG-owV5xjrAG6LaPvNpQbme34eGHAxy-ATqYXuH2JzLUl1T_vviEEsmOxg8x93URxupNYDpK425qak3XPdlCH4_mCtMlGse4uP7wrQYjUQ3f5IZeGEWxWZCqQ1MRbjdFow8gTFok_nS_VqQ8aWlEtd1EoVL45Ok0GMlAWt5yB8LpHzXZUAuynovsqynJs9RnWrGlGx7EGAElVcYA0sy5K6C1M8LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائد القيادة المركزية الأمريكية:
في الأشهر الثلاثين الماضية فقط قبل بدء عملية الغضب الملحمي، هاجمت جماعات إرهابية مدعومة من إيران القوات والدبلوماسيين الأمريكيين أكثر من 350 مرة - أي ما يعادل هجومًا كل ثلاثة أيام أو أكثر، مما أسفر عن مقتل أربعة من أفراد الخدمة الأمريكية وإصابة ما يقرب من 200 آخرين.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75365" target="_blank">📅 17:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">القيادات السياسية والرئاسات تتوافد لمجلس النواب العراقي للمشاركة في جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75364" target="_blank">📅 17:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فايننشال تايمز:
‏السعودية تطرح معاهدة عدم اعتداء في الشرق الأوسط مع إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75363" target="_blank">📅 17:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75362" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km6nyKSTo2weRytQCNoBrJWuVSZRODLA9aSguZaSnh7ti86Phwsw-1NJRgB5OUvILESJqPt-YtIUM6wP_zGp80x2GkLnK1OeIjeDPlPJBQ7yS91iAZtw6cENsx_89GNeG-W7PxYAY2WZ_F0gOaq95RveDVi47ySA34jYbEhL1JbwZfV5Cd5G4xtAuQe_afnmzic_UPTZ0RF9IkaIZ4EILbRHakp10xoWP5UOWPO-TWfcFutVRTr7qZwRNpShg42lt8cBrinuu5QrdxSeykp4ui1hJF_PtkiipZ03Ug8p1Y8y2-jQAvc8eFbNjdbGPY4EVETZLKut6FfWPn7hxl_XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية: ايقاف برنامج (الحق يقال) الذي يقدمه عدنان الطائي لمدة 45 يوم بسبب مخالفة الضوابط والمعايير الاعلامية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75361" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جنود من جيش العدو الإسرائيلي في محيط بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75360" target="_blank">📅 17:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تأجيل الجلسة نصف ساعة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75359" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الان - العراق   المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75358" target="_blank">📅 16:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان - العراق
المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75357" target="_blank">📅 16:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صندوق النقد الدولي:
العراق سعى للحصول على مساعدات مالية، محادثات جارية مع العراق حول حجم التمويل وهيكلة قرض محتمل.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75356" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i280HVuUSIv9Rhem0m3f_zMVnFWr1O8e9tyCc4GAI4AlP43sARsTDmssAFWscAfzTGq74G5xFz5FnIZfvANwFRT3dxAqsvu5vhdtPAyzXyEFKuzePpZDkh1mQOLZIsJjMfiroAkn8w67AmCb3J6jGoP6jbyYTCS-0TdAI7MWY2uTTkv2vNJ-LeqgfweZR3x6J5MFd7HX5wshRdZUTtruHgP1vHRLCXFztbd_ZW55JXVibH6TlX_TjjJHu64bpb0z895yYz4Iale7Hb3f9fNLNOtVYKvBvQT49fGFgLc63rpCsHwOT0GANfhyEiiwFoB9qv73t8U_apizdoYUG_lJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غضب جماهيري في مواقع التواصل الاجتماعي بعدما بثت قناة العربية السعودية تقرير خاطئ يتحدث عن العراقيات نقلا عن تقرير أمريكي وبعد البحث تبين انه غير صحيح وغير موجود</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75355" target="_blank">📅 16:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مكتب نتن ياهو:
توجيهات لوزير الخارجية لجدعون ساعر برفع دعوى ضد نيويورك تايمز على خلفية أحد المقالات حول اغتصاب أسرى فلسطينيين في السجون الإسرائيلية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75354" target="_blank">📅 15:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزيى الحرب الصهيوني:
مهمتنا في إيران لم تنتهِ، جاهزون لاحتمال أن نضطر للعمل قريبًا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75353" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvSBUDxvutNpcgXsAFM1tU3db1F7YnxbCN8JtcfY3dOVOhoYTFFaF7uu70w5KfFHGOCVwsSKFyfDPVtTucC7EOAhT3-JqTHDW1KFaCXgUnQzK1o_6vCBalYDya067bLMNKRNb2URyOxF4b1ywWKXnp7a8QCXBBHoZHprl6i8MI6AJxdb-lGId4vzCm0guEpYgX7lUSbK_U241Cx6toYM_kLZFpFOxJnH4IeM4CtqffvykDJLKLIy7xuee2gaGUGJHShwNbaZhDSiDNNn9pc-YcOoxTCgOzOV-9VECD5621YrpOjIHGBvjWMbl3z6Dz44hVHEBKEwnCBey39k8QxFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة / نايا   مصطفى جبار سند المرياني وزير مرشح بقوة في حكومة الزيدي …</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75352" target="_blank">📅 15:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CV حكومة علي الزيدي.pdf</div>
  <div class="tg-doc-extra">8 MB</div>
</div>
<a href="https://t.me/naya_foriraq/75351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">السّير الذاتية لمرشحي الكابينة الوزارية لحكومة رئيس الوزراء المكلف علي الزيدي</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75351" target="_blank">📅 15:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئيس حزب
إسرائيل بيتنا
ليبرمان:
أنا قلق جداً ولدي كل الأسباب للقلق، أن رئيس وزراء السابع من أكتوبر (يقصد نتن ياهو) مع تقديم قانون حل الكنيست، سيبدأ عملية عسكرية تهدف فقط لأغراض الانتخابات</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75350" target="_blank">📅 14:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-05-2026 قاعدة شراغا التابعة لجيش العدو الإسرائيلي جنوب مستوطنة نهاريا بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75349" target="_blank">📅 14:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
قائد سلاح الجو الإسرائيلي السابق اللواء عميكام نوركين:
أنا أشعر بالخجل والعار مما حدث لنا في السابع من أكتوبر 2023. من دون الولايات المتحدة، لما كانت إسرائيل قادرة على الصمود خلال الحرب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75348" target="_blank">📅 14:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75347" target="_blank">📅 13:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وفاة ضابط برتبة مقدم وجرح ثلاثة مراتب آخرين من جهاز المخابرات العراقي بحادث سير على الطريق الدولي .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75345" target="_blank">📅 13:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK4WHMmlr-clJb9sPmfcujQSIrDQAFPfi5ChAaZOBFka5G1w2WV0vjrDUORPMMjLWvg-usv3nz87Cohb217pi99BA7c5n6vSTgk8MQg4U4NZMprpbJ18Js35A6FqE2x1xfWKvVgtZODbeOmEQWJnOZZOzdz7KRgL-kDlhKwaZP5_4HJGVb7uFGIWXoRmiVCWXxUmeYA7HMrllX_w-RFggBDgNLQyoUASfhPy8dM9A8QV7PE0mxOx54z8PUt_cWHsocX4txHnEb-5WITDzE6cvsjXy4YZpLhTZ4DxXBT6Tl182rx3bRYj6JRYzyXoS_vQ1l6nYu4ASJAbw90qmkPe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة بحق طفلة شيعية في سوريا..
بعد 45 يوماً من اختطاف الطفلة الشيعية زينب صدام ذات ال 15 عام في قرية الغور الغربية بمدينة حمص، عثر عليها مرمية على جانب الطريق بعد دفع ديتها متعرضة للاغتصاب الوحشي وفاقدة للذاكرة بسبب حقنها بجرعات مكثفة من المخدرات وبعد ذلك قامت حكومة الجولاني الإرهابية بزجها في السجن وترك مرتكبي هذه الجريمة من عصاباتهم دون حساب.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75344" target="_blank">📅 12:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عدد كبير من القتلى والجرحى في صفوف جنود الاحتلال الإسرائيلي بعد كمين من قبل حزب الله في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75343" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بلومبرغ عن بيانات ملاحية:
9 سفن محملة بالنفط والغاز عبرت مضيق هرمز منذ يوم الأحد
لا تزال بعض السفن الـ9 داخل خط الحصار الأمريكي في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75342" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75341" target="_blank">📅 11:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75340" target="_blank">📅 10:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75339" target="_blank">📅 10:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75338" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: مضيق هرمز مفتوح أمام جميع السفن التجارية من وجهة نظرنا لكن يتعين عليها التعاون مع قواتنا البحرية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75337" target="_blank">📅 10:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏وزارة خارجية كوريا الجنوبية: 24 من أفراد الطاقم على متن السفينة الكورية في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75336" target="_blank">📅 06:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=KspYQOiCRahr6gOErBDRvpsAfJ1UbSbzvdU3k0vXvWyZ_M6nr4OjkxVFX1Zwhbw_Air3iWkjS3kBk0tzE4PX_0lbdgI6Qmhc0y4oH6fVVk-rEJ61JMywtZFJA0EnygccTjhOpXtchjYRtG4fdin3IYrsDsD7FJDhHxpKJgvgpKrM4rGGOt9EW4EBPQkw3vj4N666HIU3L-nuA1Sp57OvFu4Qet2KUsKUmEtOrq5fHTBJnk1PClgxoGtvW-mkzpDkwyoYlo3VxGR4tn30O3uC0t0xul-38YAEi0r_WHOnx0moRTmBVfe3k-bIvWYMttk4VEkw8_uvI0Hcmo0HoWmPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=KspYQOiCRahr6gOErBDRvpsAfJ1UbSbzvdU3k0vXvWyZ_M6nr4OjkxVFX1Zwhbw_Air3iWkjS3kBk0tzE4PX_0lbdgI6Qmhc0y4oH6fVVk-rEJ61JMywtZFJA0EnygccTjhOpXtchjYRtG4fdin3IYrsDsD7FJDhHxpKJgvgpKrM4rGGOt9EW4EBPQkw3vj4N666HIU3L-nuA1Sp57OvFu4Qet2KUsKUmEtOrq5fHTBJnk1PClgxoGtvW-mkzpDkwyoYlo3VxGR4tn30O3uC0t0xul-38YAEi0r_WHOnx0moRTmBVfe3k-bIvWYMttk4VEkw8_uvI0Hcmo0HoWmPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75335" target="_blank">📅 06:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=cCzg5KrJ4s7KK7dRaYBzAkUliJtxyXAYU6tllUdw-069cQRwl3ZtRR3d2lb5JsjxhgSAsyN7G2mNsIi-7LeGMG-sbvguI_ysRJdb09VPTSk1DTsLOjg0ogHZBu8uFTsmGjanfPqXVBSn6R0LtNII31tU1HNuXlSOZGsl1h2QzqXDV3ZPz0qdhp5leP4-NZDTutPPGo7PGSGUrgD0xlcG2ELzllsB1O5oVsFg4iMlgovxtrwAKfRCSZ1eo3FzuUV8N9mNUyCQTU1gC7a_xnF8a4sq0aWsK5_YLpXhU1H6ygQHtcXSWuNlqQ0WoflkUD89FyhVusWDEUnkSUj2hVlvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=cCzg5KrJ4s7KK7dRaYBzAkUliJtxyXAYU6tllUdw-069cQRwl3ZtRR3d2lb5JsjxhgSAsyN7G2mNsIi-7LeGMG-sbvguI_ysRJdb09VPTSk1DTsLOjg0ogHZBu8uFTsmGjanfPqXVBSn6R0LtNII31tU1HNuXlSOZGsl1h2QzqXDV3ZPz0qdhp5leP4-NZDTutPPGo7PGSGUrgD0xlcG2ELzllsB1O5oVsFg4iMlgovxtrwAKfRCSZ1eo3FzuUV8N9mNUyCQTU1gC7a_xnF8a4sq0aWsK5_YLpXhU1H6ygQHtcXSWuNlqQ0WoflkUD89FyhVusWDEUnkSUj2hVlvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75334" target="_blank">📅 05:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo-k3Yux20Wa0OpVEWmADTSvKr6G-qcHlBj-P6psbqopKI3eNafd-cxi5VosoHV_XXdZi7bSLjK_ZB4rBEscyUGhM5WtSw55Pr4t--17PY89fzUp-aVyvez-9iOjXczV0bIFsCXnOPvJF0OTaKmLYttG0i5rYbeqBN1iZwXa9ajSs5pgH_bPE4Etp1GqHA2L4yQxvuxdkAElqBPcjqhA5wZr6raM9NJLkrqhnwBL3qXegxcBSmDhfnuWmhj5inxSs4-CLX6TnwBeOwk2dYjqrvKYNX81AgT4h-auVX7gqzb0QCXouBW6WB9sX-P462p_zK7Z2Wt-aOFOXK-7UQWwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نواب اسعد العيداني ينسحبون من تحالف تصميم " الشيخية " وينضمون لتحالف الاساس في مجلس النواب !!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75333" target="_blank">📅 02:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWf_9fhnU05l2KV6N2leSxd1ZrVmC0QvaLxRiycrXbnPywxU6e4knJKqYnbUhVqk-xz0uhahv-59nkuTccJ7rDaeT1QvPwXi5de5EtJPyBcHDVUY4XiYx0QKXhG8aAlQhmRZXGF1pTzS92Lvpk-oQzompytvEoO9pvz9NHL4biGaupIMLLKaNDNskxLxaK3hn8MbzIY3HreA_WWqLiTF3yTe1AewXlalMZ7X9QK5XJCg6gAEgr_wJVzQRSz3iMnWdlHmx9vpA0aGT2hFRhra7Xt2_YdspoqPzQGFCPQdHA1hPZrtNsk2wXtzmwNWSNa6Og1OQAb3-hLOi6cpjAE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
القوات المسلحة المغربية تعلن العثور على جثة جندي أميركي ثان كان مفقودا في كاب درعة اثناء مناورة في أفريقيا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75332" target="_blank">📅 02:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">واشنطن بوست
:
وفقا لتقرير استخباراتي أمريكي سري، تكتسب الصين مزايا استراتيجية من حرب إيران. يشير التقييم إلى أن بكين تستفيد دبلوماسيًا واقتصاديًا وعسكريًا، بينما تنفق الولايات المتحدة مواردها في الصراع.
وتشمل النتائج الرئيسية ما يلي:
باعت الصين أسلحة لدول الخليج خلال الهجمات الإيرانية.
ساعدت بكين الدول على إدارة نقص الطاقة بعد أن أغلقت إيران مضيق هرمز.
استنفذت الحرب مخزونات الصواريخ والدفاع الأمريكية، مما أثار مخاوف بشأن استعدادها لصراع مع تايوان.
تدرس الصين العمليات العسكرية الأمريكية وتستخدم رسائل مناهضة للحرب لتصوير أمريكا على أنها مزعزعة للاستقرار.
يقول المحللون إن الصراع يحسن نفوذ الصين العالمي ويضعف مكانة الولايات المتحدة مع حلفائها.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75331" target="_blank">📅 01:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
روبيو
: آمل أن تلعب الصين دورا أكثر فاعلية لإقناع إيران بالتراجع عن سلوكها بالمنطقة، نريد أن تدير أميركا استراتيجيا علاقتها المعقدة مع الصين، والصين هي التحدي السياسي الأكبر الذي نواجهه جيوسياسيا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75330" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترفيهي
‏الإمارات تنفي زيارة نتن ياهو أو استقبال وفد عسكري إسرائيلي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75329" target="_blank">📅 00:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnd8cz1T-KFB3AkNijUy07_gAfCAmr1N6GOlEh0MCQRDLhfdfSYQVkQVWHoEiXyeC0BwZGr0pUbBYi1jzHsh1bduMGGFUI5u2HL4iJSVw6dc99yft9peA_2unLDce2jR56DxvQRshwzI6CeESRN2aGeUMhSvWD73hRKrKXl1aGDgNAitbrEPXk4GKMtJjC1ZeVd60j5XB6tWRw_PpTfCBrKYj_cZMRy84nRXO7lYlHRfGm3qudT7mz8QG3DoCamHJ-7h380yq9N5MdiZDLkXLXU5dTxfLHxVaJS_UhqjRTdI1EKJkv3k44xhvcGMDvFTCIi6SfFRPuRaBEL2F6nRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس ‏عراقجي يعلق على لقاء نتن ياهو ومحمد بن زايد:
لقد كشف نتنياهو الآن علنًا ما نقلته أجهزة الأمن الإيرانية إلى قيادتنا منذ زمن بعيد. ‏إن العداء مع الشعب الإيراني العظيم مقامرة طائشة. أما التواطؤ مع إسرائيل في ذلك فهو أمر لا يُغتفر. ‏سيُحاسب أولئك الذين يتآمرون مع إسرائيل لبث الفرقة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75328" target="_blank">📅 23:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سيد وهب الحسني حصة بدر تقترب من حقيبة وزارة النقل العراقية ..</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75327" target="_blank">📅 23:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75326" target="_blank">📅 23:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">طائرات مسيرة تستهدف مقرات المعارضة الايرانية الكردية في قضاء بحركة ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75325" target="_blank">📅 23:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75324" target="_blank">📅 23:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75322" target="_blank">📅 23:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75321" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تيار الحكمة يعلن ترشيح:
- فالح الساري وزيراً للمالية
صفاء الكناني وزيراً للشباب والرياضة</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75320" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">كتلة تقدم النيابية تعلن ترشيح:
- محمد نوري الكربولي وزيراً للصناعة
- عبدالكريم عبطان وزيراً للتربية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75319" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجلس الشيوخ الأمريكي يرفض مشروع قرار وقف الأعمال العدائية ضد إيران دون تفويض الكونغرس</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75318" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شركة هاباغ لويد للحاويات:
نتكبد تكاليف إضافية بين 50 و60 مليون دولار أسبوعيا بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75317" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية لوجستية (هيمت) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75316" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmnupHrjKSI8VopJJdv3cvh5IgfTHAdBmr7hC6sh0jj01IFNmCq4Ww8pygtBAhCnx7ML03PwQiVXNr05ZE6tEMMiABHlJNfsKokgUiF7pwl5ic389INQwtzTq3e7u6BHS0LKKOHXV0-07MpJwNdcqkhHeVG0EYR_YaLFtR9RmdETdlSgV6s-2CuRle7KdQU7cRyxbcDc78HGtdhed1NAo0ITi_YRztM7G8vhGAxqb9mqj9rhLlfOpRVOVy3xzZ2epbz3ZuFqT0DK0hvYsN473tdIjCm45w7qFoyZypm6-8LskZo4lv24jdntarHvp86mJG9usjaaVSI30B4o2CLsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصابات تابعة لحزب البارتي في اقليم كردستان العراق تختطف المعارض السياسي (اسلام زيباري) وتنقله الى جهة غير معلومة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75315" target="_blank">📅 21:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مكتب نتن ياهو: زيارة نتنياهو أفضت إلى تحسن تاريخي في العلاقات بين إسرائيل والإمارات</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75314" target="_blank">📅 21:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📰
‏
NBC:
عدة سفن وناقلات مرتبطة بالصين عبرت مضيق هرمز خلال آخر 24 ساعة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75313" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75312" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اعلام العدو: نتن ياهو اجرى زيارة للامارات</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75311" target="_blank">📅 20:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العراق يصدر اول شحنة كبريت بأسعار قاربت 800 دولار للطن للاستفادة من ارتفاع اسعاره عالميا حيث قفزت أسعار الكبريت بنسبة 15% خلال الأسابيع الأخيرة لتقترب من مستوى 800 دولار للطن وهو أعلى مستوى تاريخي تقريبًا.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75310" target="_blank">📅 20:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اعلام العدو: ‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75309" target="_blank">📅 20:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اعلام العدو:
‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75308" target="_blank">📅 20:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75307" target="_blank">📅 20:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75306" target="_blank">📅 20:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTgdcKfZ22uMEDOtPoYipfRjAKzM0q2hImlv9POklA2IeZ0yvoCMx8l0d2Qybg2ZdXt9Xp14dm1wc_PPOtvgooGuAAD8yu5drLv7QS9WMZroHRvFiSR7jRRFtYBxG8q0xNJMyeefYvVUaX0iShwYM2inD401YKlufnB5A4SGUQB6_8QyTn8Trq0HFFhyEo8lO6PthfHUp-GaNJM8WGy2rRN_T-pdbCBvzGvHnFpZZ-hivujC_v3bCC4xvfmzBVCt0VrE746NzrwLCitZ7TnlOzILq9Ac8ZFVqnns90sO60Z2pFqYX0L88VjpFY67L2ye0NTax6s-uXapxC2KrC-ynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
وزير الخارجية الإيراني عباس عراقجي:
‏في محاولة واضحة لبثّ الفتنة، هاجمت الكويت بشكل غير قانوني زورقاً إيرانياً واحتجزت أربعة من مواطنيها في الخليج الفارسي. وقد وقع هذا العمل غير القانوني بالقرب من جزيرة تستخدمها الولايات المتحدة لمهاجمة إيران. ‏نطالب بالإفراج الفوري عن مواطنينا ونحتفظ بحقنا في الرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75305" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقرر الإطار التنسيقي عباس العامري: نحن لا نريد علاقة مؤقتة، بل نريد علاقة متينة مع الولايات المتحدة، وليس مع إدارة واحدة فقط، ونريد دخول كل الشركات الامريكية الاستثمارية للعراق"</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75304" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
