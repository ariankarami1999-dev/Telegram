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
<img src="https://cdn4.telesco.pe/file/YA7iM2qOnU-2eGdwMyjWK_4nIuiQYwK001xAQm0ZIRHtXdkO6oUv_qt2EhNRkiOMekuPqPJu5jFYNbYwNfuBhTHeOYXpYua263Fshp9bd1AULwLhZVHIuu-mlJF0vfDebVixZ5h0tQdka_TM5Z5HQM-jOKo7oem7p8_a2QtpjfZXhjLaEuBav9DhvmUr6Ovep2prKPxq9xn65J33ZU-w41bN5EZ3VdCKYCt32G9UBUmJ1mKUneRshvBAC6243iIY_KNSapY4wAt5gXg_0_qP69SatqktAvVPaewHUeNm69lJ0FjzxfUT9TJmWQ_0TKkcbK7ur6fXKiecl4Jw5mommQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 19:21:46</div>
<hr>

<div class="tg-post" id="msg-87568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyppLiRkldZYmPiI-N50mQAFByR06Qzx0L4fJwaLJ4vtXmmGgfKtj-HEkBs_EFNwTQvagz_Ltnrk2ZtgvavPZ8KxiHxcu_OJKDqZFR4Gy0VkLCG0Y3Se5S0r5J_-hQ27Yq3UqCVv6ghBnsEbn0GzY5JVPCYTJ17LM4ezvKL6vqVy0q9eutRRz-o8rK7rXpiCFLAWMXPnTY84503cuMyO50fdSfXPHnMyMgZ8faygJEcakzp3jFICn0-sk7sYuj-rrKYRUHJiVuafsIZQ8kfkzINYUOG8umalHju8xbGj3p5KzAVonlMzy3_jy9UlHImMYynlW6lYRKIv0iV2az9rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
تكلف ضريبة الشقق الصغيرة في مدينة نيويورك مدينة نيويورك وولايتها ثروة طائلة، حيث أن الأموال التي سيتم الحصول عليها في نهاية المطاف ضئيلة للغاية مقارنة بالضرائب التي يدفعها عشرات الآلاف من الأشخاص الذين يفرون من المدينة، ولن يعودوا أبدًا. فلوريدا وتكساس والعديد من الولايات الأخرى تجني ثروة طائلة! هذه "التجربة" السياسية الخطيرة في نيويورك ستدمر ما كان يومًا مدينة وولاية عظيمتين. إنها ساعة هواة بحتة، ومن الصعب، كرئيس للولايات المتحدة الأمريكية، أن أجلس مكتوف الأيدي وأشاهدها تحدث، خاصة في مكان أحببته يومًا ما. الخراب المالي، ثم الاجتماعي، أمر مؤكد بنسبة 100٪ - ثم يفرض الجهاديون اليساريون المتطرفون رسوم الازدحام فوق كل شيء آخر. هذا لا ينجح في أمريكا، ويجب إيقافه، الآن! أبحث لمعرفة ما إذا كان للحكومة الفيدرالية أي حق قانوني في تجنب هذه الكارثة، قبل فوات الأوان، من أجل ملايين الأشخاص الذين يعشقون نيويورك ويرغبون في رؤيتها مزدهرة، بدلاً من أن تصبح مكانًا قذرًا، مليئًا بالجريمة، ومتهالكًا، ومثارًا للسخرية والازدراء. لنجعل أمريكا عظيمة مرة أخرى! الرئيس.</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/naya_foriraq/87568" target="_blank">📅 19:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
انصار الله شنو اليوم هجمات متتالية بـ10 صواريخ و4 مسيرات على مواقع في الساحل الغربي بمواقع تمركز مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/87566" target="_blank">📅 18:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2stgpeY_Sh-5a5jc_V7Uly2DZtRT_Vv2C6r7OB4V6gZGAP6s8Or6h-fUcPfHBUbWM6OPZqkgCW6M33l9X9cv9C8om14eMRPd9ou1GZy7vzPsuJftVAeXx6yCVCUMntvhcunyF877atKnB0s6iEN0ujtG9IdLRqPr6teL0evQE4yofvf_kt8dADsxnpHgP_ybYzDo4Vmlp1lkBDMhC5COTuw7hfd_Q3dMUffk2DdJgmB__kmo41DWjzz-SYW43z8HgyIPJHuzKMs6JUmTZ1RL5KwaOTwJtlY38k2ED4pQgRrZVqFr_as7QqKOk-wYnxliqCMElONXTtuuihwDH5mQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: الجولان أرضنا وستظل دائما لإسرائيل.
🇸🇾
رد الجولاني: حكم على بشار الاسد بالاعدام
.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/87565" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
انفجار عبوة ناسفة بالدجيل جنوب صلاح الدين ؛ اثنان شهداء كحصيلة اولية</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/87564" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇷🇺
‏
دميتري ميدفيديف:
أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/87563" target="_blank">📅 18:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/87562" target="_blank">📅 17:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇷🇺
روسيا:
القواعد الروسية في سوريا سوف توفر مركزًا لتأمين العمليات في إفريقيا.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/87561" target="_blank">📅 17:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اصابة 14 راكب خلال رحلة قادمة من جزيرة فوكيت على متن رحلة الخطوط الجوية الهندية بسبب تعاطي قائد الطائرة للمخدرات مما ادى لانخفاض مفاجئ في ارتفاع الطائرة بمقدار 300 قدم</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87560" target="_blank">📅 17:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامب: يتحدثون عن نقص الذخائر. السبب في انخفاضها ليس حربي مع ايران بل هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا ‏عندما غادرت، كانت الخزائن ممتلئة. قام هو بإفراغها ولم يعيدها.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87559" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87558" target="_blank">📅 17:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296520615b.mp4?token=kxQRe_lIqumuPfeIoKy2kh1E5PeaGW73w7-fmNZ_IE7SvFeFTv9wGyzpZsut9hyv6gQ5woTaAoXGoHDAP2JoAIlgzHEMRetDlC3MfUbYovt-Xww_nd8L1kGbCWBPY8PSY9Ca9oiz0YYYMTZ6SP3xqSmvCmLErW3PJxztcYDbGl4K5pymd67Iy_qgif0NhTcTcTLO-o4lln4KqEsjA3A9T8FYnpsEMQAMiidlEViZNgx6170agv3rJUhuJosWZLwuVHrfuKu517W76_sCmNnazR42a_ND2d72Q3cLyekQygnKqH0hWtykDZ41nHCf9ubPdN-XvMS7LZDfuVM4pjDtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296520615b.mp4?token=kxQRe_lIqumuPfeIoKy2kh1E5PeaGW73w7-fmNZ_IE7SvFeFTv9wGyzpZsut9hyv6gQ5woTaAoXGoHDAP2JoAIlgzHEMRetDlC3MfUbYovt-Xww_nd8L1kGbCWBPY8PSY9Ca9oiz0YYYMTZ6SP3xqSmvCmLErW3PJxztcYDbGl4K5pymd67Iy_qgif0NhTcTcTLO-o4lln4KqEsjA3A9T8FYnpsEMQAMiidlEViZNgx6170agv3rJUhuJosWZLwuVHrfuKu517W76_sCmNnazR42a_ND2d72Q3cLyekQygnKqH0hWtykDZ41nHCf9ubPdN-XvMS7LZDfuVM4pjDtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/87557" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=DiwaEYLNAtWBYuEtkRRZpkzIWxl1ex-hm_JTUw14yUgXApY3jaY2lWgDDwcBQuXv9FehQ_VZQqY9JLbg2SZtoxNfw3v5fGkmWyQy__Ti3zcjB-n2Poo4cXutqGFYRXJwTds8XbRJYEYlJfgtO6LgFEHHYonOCADwnhlFdOIZxcUIpboLYgW8XTp5ImRQd6YZBlkJHlbv5TtZy4ieEirpf-oo5v2XX6iJKGePadAQBQQCylDFjmvWYZRtUGNiAgAfpeOrjICQXT2tb-kf58kwuZdzPxnKOSGPoKo_Wlkt70pBFBbyJDDFm4i8kKQadhHQ9cZWQpA2GOCXNMdf_aFXXBTHTYkRofpn9C826XbFn1emiLCRD19W1lrwgbb8tTIQ8iBLsFiaxwxTFMlFVr7OSHWkfix_V0s06-sKzmHbPbBml6uMq-wkR_0CiR8rOBLXugAArpjfHBj-YSH-hrezQsy1Y9vq9J-CDmOezZzzhgCb0LtX-Y9q1uATdRwsvDPTubQaK66QJgdODgtYV7SjHDcPf0M8vkY2j9c0hMvCTW-60X8bjh8DCBci-RbjJWBkD9gJinWDLRVgTHvgq6EKQYlq9aJz92kl38IzMJO_3GyU7v0EiWPv8QCffGxzxLoiZmTe5JgVCFDR4U2MQ3vrpocxMA2s825C71Lb8rOFgKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=DiwaEYLNAtWBYuEtkRRZpkzIWxl1ex-hm_JTUw14yUgXApY3jaY2lWgDDwcBQuXv9FehQ_VZQqY9JLbg2SZtoxNfw3v5fGkmWyQy__Ti3zcjB-n2Poo4cXutqGFYRXJwTds8XbRJYEYlJfgtO6LgFEHHYonOCADwnhlFdOIZxcUIpboLYgW8XTp5ImRQd6YZBlkJHlbv5TtZy4ieEirpf-oo5v2XX6iJKGePadAQBQQCylDFjmvWYZRtUGNiAgAfpeOrjICQXT2tb-kf58kwuZdzPxnKOSGPoKo_Wlkt70pBFBbyJDDFm4i8kKQadhHQ9cZWQpA2GOCXNMdf_aFXXBTHTYkRofpn9C826XbFn1emiLCRD19W1lrwgbb8tTIQ8iBLsFiaxwxTFMlFVr7OSHWkfix_V0s06-sKzmHbPbBml6uMq-wkR_0CiR8rOBLXugAArpjfHBj-YSH-hrezQsy1Y9vq9J-CDmOezZzzhgCb0LtX-Y9q1uATdRwsvDPTubQaK66QJgdODgtYV7SjHDcPf0M8vkY2j9c0hMvCTW-60X8bjh8DCBci-RbjJWBkD9gJinWDLRVgTHvgq6EKQYlq9aJz92kl38IzMJO_3GyU7v0EiWPv8QCffGxzxLoiZmTe5JgVCFDR4U2MQ3vrpocxMA2s825C71Lb8rOFgKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/87556" target="_blank">📅 17:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87553">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=TllfHuE95osmw6FE8XOJCeRY50sMIKP0xv7EwHDQIYHS8NDO1bgklMySaMs3QUoU7OsPAoE5QfoWu9sF8km2QWRsGXdVM8eFTv5cFIBt0iccyMh33NkP3sbYT7oFKdumvwNA1MmCBWCUirvl_aOlSbCarp8IrTwsppQzn89VYtkElbStgpsz9dL5uMHCa1F4nslWV8IV3omycDY07UbefnZtNO0q2hHGOW2ZG7UdL8kjjGNmz-Ed5WorcQ7-Fytpt70BbxKf1_IzJBesoVFaX4eQcN015lh2BfK4_B1air9E4uzoPs3OeOBUL91WCgn7g3xwBiNROMwFcWxJ_NrOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=TllfHuE95osmw6FE8XOJCeRY50sMIKP0xv7EwHDQIYHS8NDO1bgklMySaMs3QUoU7OsPAoE5QfoWu9sF8km2QWRsGXdVM8eFTv5cFIBt0iccyMh33NkP3sbYT7oFKdumvwNA1MmCBWCUirvl_aOlSbCarp8IrTwsppQzn89VYtkElbStgpsz9dL5uMHCa1F4nslWV8IV3omycDY07UbefnZtNO0q2hHGOW2ZG7UdL8kjjGNmz-Ed5WorcQ7-Fytpt70BbxKf1_IzJBesoVFaX4eQcN015lh2BfK4_B1air9E4uzoPs3OeOBUL91WCgn7g3xwBiNROMwFcWxJ_NrOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مناشدة انسانية عبر بوت نايا
بعد منعهم من الدخول بريا خلال زيارة الاربعين من قبل السلطات الايرانية لاتاحة الفرصة للزائرين الايرانيين.. مشاهد من محافظة ميسان لاعداد كبيرة من الزائرين الافغان والباكستانيين الذي بدأوا بالدخول الى العراق من الحدود الايرانية لزيارة العتبات المقدسة ويعانون من شحة وجود المياه والمواكب على الحدود بالتزامن مع ارتفاع درجات الحرارة.</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/87553" target="_blank">📅 17:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87552">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/87552" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87551">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
العثور على رفات 12 مقاتل عراقي في مدينة الفلوجة ضمن محافظة الانبار غربي العراق قتلوا على يد تنظيم داعش عام 2014 وفقدت جثثهم.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/87551" target="_blank">📅 16:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87550">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مرتزقة السعودية في اليمن:
مقتل 4 بحارة وإصابة 4 في هجوم لانصار الله استهدف سفينة في باب المندب.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87550" target="_blank">📅 16:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87549">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انباء عن سقوط طائرة MQ-9 أمريكية في جيبوتي ولم يتم تحديد سبب سقوط طائرة الى الان</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/87549" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قوات أمريكية أطلقت النار على السفينة "فيلا نوفا" التي تحمل العلم البنمي بواسطة طائرة هليكوبتر وتم الإبلاغ عن سلامة جميع أفراد الطاقم الـ 17</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/87548" target="_blank">📅 16:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الكويت تزعم احباط مخطط لتنظيم داعش لاستهداف احدى دور العبادة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/87547" target="_blank">📅 16:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb842a65a.mp4?token=mPWJbY4XmpvKF2m1V7KAKiNoj_ibjYPx4RkVepVoYHV5vpgu5iKKAyM8MqjSossuMSEvnNc64mJdw-F0qRGTMGkZkfLEjO3k4F8Tb76Qro9WvBHDpnpQsYywefWCkVKp7xfxdB7TC9zRQGwp4NFZXcQ2Y7thq7mT0DM-wXtuP5JieyOdU-YJ6piPI_QR9cyoBHKXGV_UDpuylk7BsLV7r9yyFbJZHlOfXh1iuDXfejO9UEk_yYwDr4OGedDEC8ScFXSlChEFw4ViMHqW65rGrYVz4jRYtb0rfH_T2AHxZssviIDpaUuSeh-OgdilCNEKzHqpyHoa_ELVY8_kxolBBWyudTmVzY1wOAd0k3xMPdvCMqGh5FSqTY6YTjhEGWygjZ940DZ3jv4a7Nzcqw8kerwW4RI6UAdsLrwN5zWJ1C75g78VWWPkLzinOIutOzVmDGGXll1zr3AD2BGAlhOXX_QRALk7q-6EQDge4idsqtb_0D2K3lI_dVv82XKOansSD-HjKgQMpu7hMHX-2b0VPBTXdj7QDPxBHcDr7nRZo32H0H4Qc_rKccTwZ-LZuJZPGU_R7XbZGeh0eCUGdrDnsPoqH_x7gxv3uNou0cMCwjHVyFOu49zJWB_0U_OZMBfmyQVGYbrxIMGXvV_fo5OPzzF0eQVQKkiZyQcNDOyZtu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb842a65a.mp4?token=mPWJbY4XmpvKF2m1V7KAKiNoj_ibjYPx4RkVepVoYHV5vpgu5iKKAyM8MqjSossuMSEvnNc64mJdw-F0qRGTMGkZkfLEjO3k4F8Tb76Qro9WvBHDpnpQsYywefWCkVKp7xfxdB7TC9zRQGwp4NFZXcQ2Y7thq7mT0DM-wXtuP5JieyOdU-YJ6piPI_QR9cyoBHKXGV_UDpuylk7BsLV7r9yyFbJZHlOfXh1iuDXfejO9UEk_yYwDr4OGedDEC8ScFXSlChEFw4ViMHqW65rGrYVz4jRYtb0rfH_T2AHxZssviIDpaUuSeh-OgdilCNEKzHqpyHoa_ELVY8_kxolBBWyudTmVzY1wOAd0k3xMPdvCMqGh5FSqTY6YTjhEGWygjZ940DZ3jv4a7Nzcqw8kerwW4RI6UAdsLrwN5zWJ1C75g78VWWPkLzinOIutOzVmDGGXll1zr3AD2BGAlhOXX_QRALk7q-6EQDge4idsqtb_0D2K3lI_dVv82XKOansSD-HjKgQMpu7hMHX-2b0VPBTXdj7QDPxBHcDr7nRZo32H0H4Qc_rKccTwZ-LZuJZPGU_R7XbZGeh0eCUGdrDnsPoqH_x7gxv3uNou0cMCwjHVyFOu49zJWB_0U_OZMBfmyQVGYbrxIMGXvV_fo5OPzzF0eQVQKkiZyQcNDOyZtu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حادث سير بين صهريج وعجلة في محافظة الانبار غربي العراق يسفر عن 4 وفيات كحصيلة اولية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87546" target="_blank">📅 16:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قوات العدو الأمريكي تطلق النار على سفينة ترفع علم بنما قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/87545" target="_blank">📅 15:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قوات العدو الأمريكي تطلق النار على سفينة ترفع علم بنما قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87544" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce4ade89d.mp4?token=vhFqBJdBUJXu5_b8C9PsKa5WLmByp5GRtr9lsRRqmCMHJ5-pxlUEEphoMws-FLLNkN5hu41Vi2K9uK9DL_IAJH3U6MXVRRaR7EudfAwkMhH_PxW0b-fFmaHC8yOBB3_guTxrH1oAklCYCWGf8Hd1xZ_tN2TywT69k7BpzI707YvqNtb9JiE70HROBxRIaxdNkBdASOY3n7zgt69rlxiqsO4NujguFGkl5qlLnxP70b2Y0Otrm02yj3K0NvJHJq8KP3e60CC_RRcKDK-IjbXWTi3Ji2EjN35y8uj2rXYg_PMCbeaoSf2TAgbaBO-2wlw_C6kWlSYmTrqLYhg9P3BUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce4ade89d.mp4?token=vhFqBJdBUJXu5_b8C9PsKa5WLmByp5GRtr9lsRRqmCMHJ5-pxlUEEphoMws-FLLNkN5hu41Vi2K9uK9DL_IAJH3U6MXVRRaR7EudfAwkMhH_PxW0b-fFmaHC8yOBB3_guTxrH1oAklCYCWGf8Hd1xZ_tN2TywT69k7BpzI707YvqNtb9JiE70HROBxRIaxdNkBdASOY3n7zgt69rlxiqsO4NujguFGkl5qlLnxP70b2Y0Otrm02yj3K0NvJHJq8KP3e60CC_RRcKDK-IjbXWTi3Ji2EjN35y8uj2rXYg_PMCbeaoSf2TAgbaBO-2wlw_C6kWlSYmTrqLYhg9P3BUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
15 حالة وفاة وإصابة 22 اخرين في حادث تصادم بمحافظة الإسماعيلية المصرية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87543" target="_blank">📅 15:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8aRT5rACc0ZND_47eGiPaBY-n5yyrhBRb7fTAFuMJuPqctmzjK-wwBVqaSkXc9sZKzJQu10fAvJrRdUZHLD27EKLP93YuKbVWcs3Pw67LMxeEl-Z8uUfznbkWcxWUnfJeW7agCVUzXPStTGgBWTCX-ZLSHGhSVoZd3p53EVQDjO6XdhqgRNPkuhz78oQHfO9yQCzwMwBuchrbqNuqRseczTeP8cP8cnrbmsa2XQzrpXIUEfjFSMnSZkmgmdk0-wswkbVGxpaDmDzTOckUr6PF-_fSLCnMJrsUbnyuf0dUZKBWtKXIt6QdIUWht9Gnwm87_YoLGxYmfnOYpfPIZsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWjUB42XBVtpDZ6iZTGoGn6-8R6aY7GQvZ-9zBTbyWtrABTLO5eiFZuv8vewZAE4Ryddj4iEIzU0c_NSGOj0M3QPRK3lfaotoFCwN2tVFutdcVaKSWrUzySqGcfGkCcVgbVX4q-MRwNLKtXndO6zWy_b-MI16mEN3hDg7tAqtDij5rwi7x0BYlncXqjghNa5Jhes22uS2cYMBBJx9DhPBctHyll6raQrauMXWqqCZKrCVPm2GWWdwyZiWO0Bg8UxTfOhXW_HKKuSbbMbl_L3znohj7U8MfvnGjnQyizdfzT5ColRO7Q-oPBt4G5qZIMiaiHVSStHJ1qNrR7r5IgrCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">العراق يبدأ العمل على تشريع قانون يمنح موظفيه اجازات طويلة لا تقل عن 5 سنوات لمن يريد مقابل منحهم 50% من الراتب بسبب تصاعد الازمة المالية وكثرة الموظفين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87541" target="_blank">📅 15:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr8zedwsLpW-vgAF237u3pK2PGYYPOKwuZRHNTkFdNXzcnmU5oiy0K1Hwb5Y4hon4dN_cPqQf-me0pswwxN41TfHq0RmnInOoVxbtqltcFq0_e9mBxRhUahBxQpLK6IFVYd969O4X-Hl64wr1Gud4eQsvVgNwhBjJjtB-tsAsCZjDRErI0gVDz47S57hOuyTaZ79S1V7iAKgEREnhJAbAYsGBvkUKRglT80WiyDtxeeQiy8kt_y2Ke4vtVHAcWKHmJIUOzBlVv3eA75wf2qUbkjwlT2Rlg091Cpw6Y88txgjgzHO0Vb_55-iD2qyRjpLC8EyYQ821iiYKgAGeJqHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة من طراز بوينغ 737 تابعة للأسطول الملكي الإماراتي A6-RJA تحلق من أبو ظبي إلى طهران
‏هل ستتجه المزيد من الجزية الإماراتية إلى إيران، أم أن مسؤولاً إماراتياً رفيع المستوى يقوم بزيارة؟</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/87540" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">استهداف محطة كهرباء الزاوية في ليبيا بمسيرة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87539" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87535">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrkE7-2eZtQjxciH7OnCL5BzLnR9xqsGLsHxdNHD0OVh0p9765lgTD3c4-CnQbBff3CavmIsIdFDx6fQnEIJLOpigdCJS7vVe2lMKRWz6jzPKv-zQy6SAnrHwEq0bXWfD97F_29C21MsrLyyo0UfRVKg5rGDeg4uZhktp1JcyIUvo-8KBHGQsMFg2I2IbOFOdXUpRU3B5YNQP_iJZQXNLhUi1OVB8JZygz1q1xhkxBUhwce1W0sSrpAFbgbapmTqAdzUtbqUlafO7-lzsNLeXOZC4I-0gaQnhSXpbfgqOrwkTmv-fwKd54mzsV06Thjx8jA8709R-jN2-QUhcqrLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIeNSvC4YY7fhS6flINDCM-iStJfyyOcqdJ52Rw2iutSe_Q_5EfDv9NAeL1qWtJX88PfgtRUN2ccoh66DCKZ3PU1OIkL7vXj04hmjIKJCB3HpUHlHrQZstP9tlZQ4CNcbMveM-MA6pRLKkdfu8H_0GsoooT5NJyCA0lLG0qMxLhIlEWCdr-6I6Qhjxm4KYk-K_UpRK1mvLgA0Hi43BC7quXa8kHBw3eIYGWfS7m8-paYnFlR5AdNm8Km12hvl0bcgcx7O03REfJz6gjdsi5s06uLTmxjR6ds4tck5Eq9LszmNIj5ouDY7AtDIfzun9nhGJkJTtNMftU2y6MuALzYNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5979332c5d.mp4?token=PuiTFYSRK_BcB2fmT3f_bSsV-sAiV81i4H82lzg6s9cA_Y8DSFRxDMawdjI86cldVfxWsTvBqgPqK6cte4CIAALuMJBS77TEYByKUcc9n-Z2uyOmYvyJxlrrnfZBnQhYAE5AVHAhyFb3fojBg3DLjudb7KbkXEtnk_JImn7SEwW8QYAU_8vU1ZcJaiYck3FcOXJbtmUAEolMPGultE86c_1S5XUemgXvXdVmNi6hkIo8QCFDhFKsivEV5fI1rh487g0WMajO_BCV7G3_nLxyaiiKogRIROJ9j5AwGO2XEl-XaTvPvdpM80LNhfuOkMUAD6YlEZFouF1QuCrgge3tlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5979332c5d.mp4?token=PuiTFYSRK_BcB2fmT3f_bSsV-sAiV81i4H82lzg6s9cA_Y8DSFRxDMawdjI86cldVfxWsTvBqgPqK6cte4CIAALuMJBS77TEYByKUcc9n-Z2uyOmYvyJxlrrnfZBnQhYAE5AVHAhyFb3fojBg3DLjudb7KbkXEtnk_JImn7SEwW8QYAU_8vU1ZcJaiYck3FcOXJbtmUAEolMPGultE86c_1S5XUemgXvXdVmNi6hkIo8QCFDhFKsivEV5fI1rh487g0WMajO_BCV7G3_nLxyaiiKogRIROJ9j5AwGO2XEl-XaTvPvdpM80LNhfuOkMUAD6YlEZFouF1QuCrgge3tlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اضرار جسيمة في مقرات المعارضة الايرانية الكردية في محافظة اربيل بعد هجوم صاروخي ايراني</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87535" target="_blank">📅 14:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87534">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW71N86s6xDeW8Fk8inHjxMKtdxfaW970Nz0CEXi8ZPUpFpzEV7rN21Z8H76HN6fPk4CcyKhdtpIUh65Tpkpv7ACOCgkMLIoJSd1OEUa7fuh8YZBIc2YBuY7Deo-x-yymcj4JQx3wFoSOS8_ygIqbrKQ1R-RRhLTK7-LCZrVh2W-e-ztnerDHDtWTDdHDZskoT2V47h8nk-3xfuFzYTgEf__W6Z5yiGVZjnHNmZNpgthrDag_UCMWJV3ryhQ6HwJg5jHc_P0k89V4mx7PlQGvUEagr84RRBFsIGGwckKX-2fX10NV2DZPvzG3t3D4Aza2rs-mSLXIp1CD6L_bCkdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أصبح الآن بالإمكان رؤية أضرار جديدة في مصفاة جازان النفطية جنوب السعودية عقب هجوم بطائرة مسيّرة شنه انصار الله في 5 أغسطس. وتُظهر صور الأقمار الصناعية الجديدة من Sentinel-2L أن خزانًا كبيرًا آخر لتخزين النفط تعرّض للإصابة، ما أدى إلى اشتعال النيران فيه خلال…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87534" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87533">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dfaf180ac.mp4?token=Nf-I2qvrHPF1H1PR87Iq8StrpHqSob39THIgb4yKXlEd10Y992UyPbCfLAQu1Seb8d3efFhfbhCkb9qQFcRhS_wTZnkzoupuIP_hypay5-ZqavF_RFObXzST9FWFQ_muViHHuzSViNgHuTSjFK2qZRlTEDvtOZIxxlAc_puDx_1LRqQJUhioF50ShW01fmugMvnrivt2CEkLBU5CZmmFm4kbSthB4MIzIsLItCpbv4G9N-12aPoLeJ4Qp_QC2j8H-1bdpGk8spWnZtRPmljSP9iRpRSn82jJrsbcjFcmri-lFVgBnja_K7asYKg1Vu4UQjy1RQLPXO-hDv0J5Yb9sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dfaf180ac.mp4?token=Nf-I2qvrHPF1H1PR87Iq8StrpHqSob39THIgb4yKXlEd10Y992UyPbCfLAQu1Seb8d3efFhfbhCkb9qQFcRhS_wTZnkzoupuIP_hypay5-ZqavF_RFObXzST9FWFQ_muViHHuzSViNgHuTSjFK2qZRlTEDvtOZIxxlAc_puDx_1LRqQJUhioF50ShW01fmugMvnrivt2CEkLBU5CZmmFm4kbSthB4MIzIsLItCpbv4G9N-12aPoLeJ4Qp_QC2j8H-1bdpGk8spWnZtRPmljSP9iRpRSn82jJrsbcjFcmri-lFVgBnja_K7asYKg1Vu4UQjy1RQLPXO-hDv0J5Yb9sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أصبح الآن بالإمكان رؤية أضرار جديدة في مصفاة جازان النفطية جنوب السعودية عقب هجوم بطائرة مسيّرة شنه انصار الله في 5 أغسطس. وتُظهر صور الأقمار الصناعية الجديدة من Sentinel-2L أن خزانًا كبيرًا آخر لتخزين النفط تعرّض للإصابة، ما أدى إلى اشتعال النيران فيه خلال الهجوم الأخير.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/87533" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87532">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حادث بحري قبالة سواحل المخا، اليمن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87532" target="_blank">📅 14:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87531">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxfarQ_IrzqKpdjVOWbnMiRADVeFS4uvFCav30kSKuu0gnyMUKsjSboiFu4kI48JqYijHdeULvsVbySpoLYseTHEys9aujL2fJGzwu38KX35yCIFfB_SDj8mOBAsjPNUF8N2fAr73Uz2UQW3jZSS4pefq8zni1O0oXVacheSQY_JgTnUDM-tcIWKHYkII_HewPCucgT305vcmqQhzM40jSa1iOrYI8S7vWObb-mdwc-C29GbmZBrXNQNIpQgH_7zILqVWYc3yhe4fTWEe6BDtQ75T3WXfdfSoLpjQNXthQp-coSXAvYxoILJOfh8uRYRqZvCo9DM86lyatvqSCxhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري جديد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87531" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87530">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87530" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87529">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87529" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87528">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزير الشؤون اليهودية في الشتات الإسرائيل: الضفة الغربية هي قلب الوطن اليهودي. هذا هو ميراث أسلافنا. السكان الفلسطينيون هم سكان معادون.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87528" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owBfXjiV70sMQEmKMpnHudOEIH1nOnaFWshSV7ZwVfFBStL-8dSRK_ml_SjtQobNjqBmGtOe1pUxrZVJnrx3zx2-Kpp3maqGCH5AeD265K-FJKUclNdz3F7wlbpxxH59zaKvRkKVThpbNFVKQk4y9OwUK7wbe79Xsqs8fAzetIMPWKFlP9P4oZNRh1rnHaf3yf-Q46muiwTMBWemLFg8YcbZGVKW4LEdxXI4nJmTyn1DDKLuLjgVyROoJ1nCBhIXB0gTYKdr05PfUKt86pN7sErCyTG5G4ydz0-HZOwpygxEVbCMzlGvDUhYKXT8elpDq9agQuuDymuVd376rcLnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMmsCojjfVs6JT7linLxsBi1KNoIT-j113CsDVnJrf1bdggTLxCpCXlyU-DOEs65Vt4MP-05tCKRhr-2Y5o11n6wKq99i1Vbt_Xb_9WiOh9y0NoW7iVX5b968NYRnH3Taadkg3-U3GIYbhD7J_PgF02NxNehYV7ljIc4sf4wvQy4BCCYOwIjcny9j7cufN-nzrnMU2JdbFKJaftThkTn18UbAYaIkNz2_nkg1P60SUPYAjABr9DrLgNN_AWbOFX2HTt5QGjXDULQtgvrOiIkatUMBeWBL5SPnZDhJiFVgq7322oCfxrhS91KNR9hlxjVUZqBNCu1b05qcWUlxZDZIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87526" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87525" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87524" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2SYH1oTL0nJSe5uEsCttE_ZaIBOlhcG_UGNkUCrFSl-V-8AeUC5UOr6K9DgPj7l79S2k5vcv9s9ZBqcdt0Hl5CvG4DsvevHHPS5oOV6YvvwyLdq4VKpeq7y-z2kX9OFmDmIWmnXprP4WowM7IdomHfDwZOFbeWSK4fSVf1d5UuUPKDGs2Zi_lxXI4mUOr2iDkUXS5QYnmI4dAhRqhBc_xnvulkjuaNCYkigXYUKTuOFU48dw2Hoq_yO0Sw4u55kAL-W3OAFhYtTl_eat_gq1_kML2M-hr64EullB__PzpHUU2p5cxEgS6IgO2z4Y-ot3FJ2122-jalJYlMGSfF06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87523" target="_blank">📅 11:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-AlkHa6xF1mzXPf4WZZ2tIvwjACEtPiDK21rgeKzvY7nsMuHim2hXKKUfAPnZTw_kgJI7tzpcxIlNxHN16Mfwl1OjnGhA20FnCJtsEp2HFde0aMIhXUApUdDrlue1el0JU2f6P8tX1EJvorUoUI6DfpwAW099o5nDDoadVOXbZPpHMGPyUSyBw7pxA0yrXM683rT_roTLf4xSEYD5dSUwa31B3qpPEcCSFUaskKTvG3SgCcnfNM_F3OqLuMnf4b-aa_Jlql8_sZ4t-38uCf9cOkjeHCq48Zss3fDIvXY9zaAs644d4lRfZVD6MnvwZmDrM-9R6q0vpkFLPrYF2vRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87522" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87521" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87520" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87519" target="_blank">📅 11:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87518" target="_blank">📅 11:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.  إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.  بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87517" target="_blank">📅 11:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.
إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.
بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة للاتحاد الأوروبي. لديهم أموال، وهم يدفعون المبلغ الكامل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87516" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIjZJnjnLBKo_7jTEIXXf6T3JZiRK4CwqmnocK4sxA-PXi7pGvL4iFd_Do3BKBWEsptDX0igxP3ytRvqhKy1fHfeic0iMi4hXSELdXPdWgLdgQPM4cE1xBKu4kKy0_mlBny4MjPFA1VRKalWRn55j0gx4n12ghYKwWll4vDE8KM-NUWNRu_pqNWnXBMxm0eLgHQznPK3aQanBZ243OtUC_VO4N7xVwYgF5_UHBAAtK1lBj5QVQGfcVoeXcVwVZMHTNiHvPL30TBmk7cPGh_FQb3I3IVj5GIPEhbj7IDeqwgVOn7XHdlrr23i0pbzF2nO-aCmQ600VAqBSW-hqSsm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط وسط تصاعد التوترات في المنطقة حيث وصل سعر برميل النفط الواحد إلى ما يقارب 90 دولار والارتفاع مستمر.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87515" target="_blank">📅 10:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87514" target="_blank">📅 09:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87513" target="_blank">📅 09:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسرب نفطي واسع النطاق بمساحة كبيرة جداً كشفت عنه صور الأقمار الصناعية قرب مضيق هرمز ؛ تشير التقارير إلى أن مصدر التسرب هو ناقلات نفط كانت تنوي العبور دون الالتزام بالإجراءات التي أعلنت عنها الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87512" target="_blank">📅 09:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترمب لريل أمريكا فويس:
نتحكم في قدر كبير من أموال الإيرانيين وأصولهم وهي تحت سيطرتنا التام
لدينا 3 استراتيجيات للتعامل مع إيران أولاها مراقبة مدى سوء وضعها والثانية ضربها بشدة الاستراتيجية الثالثة هي الضغط الاقتصادي ونحن نفعل ذلك على أي حال
أكبر تغيير رأيته خلال ربع قرن ما حدث لإسرائيل فقد كان لديها أقوى لوبي في واشنطن
إذا سمحنا للطرف الآخر بالفوز في الانتخابات النصفية فستصبح البلاد تحت حكم الجهاديين</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87511" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0JhEH97kVKdldeBFvmndmi5vjZHhEnDVllDeQ5i99kx1NXlEoKNJNtxSOd0V2YUs8UAK9esIvWkzkb8MfO2OUREmd6bQP3uXLeBgDikdVBVEpOYAmVVsrjAq-FTWVMA8cZKGW59pN3Pt_Uk5P7mZy-dgocsd6-1B7divCXVUZb9t-pkFo9PXhWcNmKb5pBXGDo4zRjwoDuJeTalKNd65wMrLIdtqCfa9dbhvCJgmbJ5sEIrLvlfzNNA25LZAMI7hsRfcX7D4hXTBFrriIj5gVevCW-2PN51uzLm2WQdD5u4UdlQFrO6lilUlnzrfseT3Q_FdIHXawknPwWiscPLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سيرتكب الاتحاد الدولي لكرة القدم (فيفا) خطأً فادحًا إذا فكر، لأي سبب من الأسباب، في استبدال الرئيس جياني إنفانتينو. إنه رائع، فقد ترأس للتو أنجح كأس عالم على الإطلاق، بأربع مرات. إذا رحل، فلن يكون ناجحًا أو مربحًا مرة أخرى! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87510" target="_blank">📅 05:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvQwA1n1G8r5Wb5LIm2xmG1r9YSBBptnum-kgC1fCDdVR83iSh7BcjKonAsYnueXC_ZKdQI7T_FyLElMMnL9JTdVPJ7Hzod3jsH48o-_94oxnUIGVSzwxYIB43SUHD464YbeNQg6VK-BmIH6QxDQejayv7cNYD97Zi7i7OQ-vbMnmzRIbMsP1tM77BlT1FNnMxWuLc8yz_b5MPmD8fQwC_cLfzfHlKVRkoHp1jVp0nN3T3sPOAXxWUEY8Yy81ziTKJYUoSoJ9NYy0RDQqclcG3pDALGzJuFzAyUZ6EeRyK1pACri4NGrMxT4GzJWD0vfpCc7prj1Em-PisoEBlrotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق موجة صواريخ نحو معسكرات مرتزقة السعودية في مدينة المخا.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87509" target="_blank">📅 05:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=Pj4ZX8XVHHyeRrkWzy9Gle8kV4i6Hpankj5Vqi9G7n2MJQfOi3qerA7bKE-TLTOvZFT_3jWlFQ8XkMpn82AhSeSBxjHX9Uuw0Lpxt1QwCzEYmIjRjm0C2wFFXbSQs2aN2JHo81npVepbHwRCuaxb7FAVF6bliN7UsrFGAMHmN8HR7kDhYwKo00ZSfNUVG_6Vcz2TCP0diB1eqNdRsAELvYGPJtE9GCTvCegLPnpY-xIGR5Drx_jN8MbcBubOHo0xOLaKkzfk7_4ScfmKq6mf_4B5_ZlypbNGPHYynO4EOZxwjv-rFubg_mW-VasTxuGpM5SJ-3xKqR6yiWj36YSOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=Pj4ZX8XVHHyeRrkWzy9Gle8kV4i6Hpankj5Vqi9G7n2MJQfOi3qerA7bKE-TLTOvZFT_3jWlFQ8XkMpn82AhSeSBxjHX9Uuw0Lpxt1QwCzEYmIjRjm0C2wFFXbSQs2aN2JHo81npVepbHwRCuaxb7FAVF6bliN7UsrFGAMHmN8HR7kDhYwKo00ZSfNUVG_6Vcz2TCP0diB1eqNdRsAELvYGPJtE9GCTvCegLPnpY-xIGR5Drx_jN8MbcBubOHo0xOLaKkzfk7_4ScfmKq6mf_4B5_ZlypbNGPHYynO4EOZxwjv-rFubg_mW-VasTxuGpM5SJ-3xKqR6yiWj36YSOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع حريق كبير في مصنع خلط وتعبئة الزيوت بمدينة الزاوية الليبية إثر استهداف بمسيرة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87508" target="_blank">📅 03:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=SbSWsUREiaHL5SPZUDTGPgnj_qcDTJtMjLNLvXK4MVgPzwXMY7zQLxYwR15k0KJ4pAKjIu9cYjHDZHLf7vQWzDdEkgCgt_sW8v_Bpl1nr1AEUj9CpIBS4gGyMw43Fc3PSVX3HzKDQi9MnBMpQP1pzfCjoz2BAEuX0ZWEqdqPoh2UA4C2B9tRA_vW5pwnMVQvdNs0JKlp5r24hSKeYml-fVmOagF-WVeh-fbamnZIbY8lwZ7tB1nJb-QeXnBq-pgmetTzGbr1PrPTVpYJuGaPy5t3FwelJCjrNO5W4z1mPD17LukpMob9DsOw1jACLo-Nz_tUf7YE9m0M4Qx-e93SSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=SbSWsUREiaHL5SPZUDTGPgnj_qcDTJtMjLNLvXK4MVgPzwXMY7zQLxYwR15k0KJ4pAKjIu9cYjHDZHLf7vQWzDdEkgCgt_sW8v_Bpl1nr1AEUj9CpIBS4gGyMw43Fc3PSVX3HzKDQi9MnBMpQP1pzfCjoz2BAEuX0ZWEqdqPoh2UA4C2B9tRA_vW5pwnMVQvdNs0JKlp5r24hSKeYml-fVmOagF-WVeh-fbamnZIbY8lwZ7tB1nJb-QeXnBq-pgmetTzGbr1PrPTVpYJuGaPy5t3FwelJCjrNO5W4z1mPD17LukpMob9DsOw1jACLo-Nz_tUf7YE9m0M4Qx-e93SSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق أسراب من المسيرات نحو معسكرات ومعاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87507" target="_blank">📅 02:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
واشنطن بوست:
تم نقل الرئيس ترامب سرًا من أنقرة، تركيا، على متن طائرة من طراز C-32A تابعة للقوات الجوية الأمريكية الشهر الماضي، بعد قمة الناتو، وذلك بسبب تهديد إيراني باغتياله، بينما أصر البيت الأبيض علنًا على أنه كان مسافرًا على متن الطائرة الرئاسية "Air Force One" التقليدية.
في البداية، صعد ترامب إلى متن طائرة بوينج 747 أمام الكاميرات في مطار إسنبوغا في أنقرة، قبل أن يتم نقله سرًا إلى الطائرة الأصغر C-32A باستخدام شاحنة طعام تابعة للمطار. ثم أقلعت طائرة 747، وعلى متنها صحفيون وموظفو البيت الأبيض، بهدف تضليل المراقبين، بينما سافر ترامب ووزير الحرب هيغسيث بشكل منفصل إلى بريطانيا.
حلقت طائرة C-32A التابعة لترامب تحت رمز الاستدعاء العسكري غير المحدد "RCH18"، مع إيقاف تشغيل الأنظمة التي تسمح بتتبع الطائرة علنًا. وفي الوقت نفسه، استخدمت طائرة 747 المستخدمة كطعم في النهاية رمز الاستدعاء "AF1" على الرغم من عدم وجود ترامب على متنها.
بعد الوصول إلى قاعدة سلاح الجو الملكي في ميلنهال في بريطانيا، عاد ترامب إلى الطائرة الرئاسية "Air Force One" التقليدية قبل أن يظهر أمام الكاميرات، مما حافظ على الانطباع بأنه سافر على متنها من تركيا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87506" target="_blank">📅 02:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87504">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=alQUoBWMmL9ki7IZaHvn9-PeDgaGe6f7ShwYIE-1Vc8QPoGP98x3_XXafUJ4nkoNRdbVwNImTK_9qFfY9_TqyFQu-eZQ4R69vPPiN40PhdDwEU5PCK_xNDdacd89lpq6YOSV2uquOLhIsLkaR8NWk5UCyxY3nEVIr3c9iJIkRGScLf3aG8ZQS2rROmUItOd5624jBNR9p8Ar_fp-G5SO4VpdSm3vz3Ds1vxdUlGpLbTxdz7yEWcfqkEsv6ExPbo4aXIulR6XlD8kCQwVZ3CTC7toLhJmhIi2Wv6GNRmiXhlAZgpgDiEOuXDZKvJcW5Yc8iXwu3xd3OJbPtgaPPXdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=alQUoBWMmL9ki7IZaHvn9-PeDgaGe6f7ShwYIE-1Vc8QPoGP98x3_XXafUJ4nkoNRdbVwNImTK_9qFfY9_TqyFQu-eZQ4R69vPPiN40PhdDwEU5PCK_xNDdacd89lpq6YOSV2uquOLhIsLkaR8NWk5UCyxY3nEVIr3c9iJIkRGScLf3aG8ZQS2rROmUItOd5624jBNR9p8Ar_fp-G5SO4VpdSm3vz3Ds1vxdUlGpLbTxdz7yEWcfqkEsv6ExPbo4aXIulR6XlD8kCQwVZ3CTC7toLhJmhIi2Wv6GNRmiXhlAZgpgDiEOuXDZKvJcW5Yc8iXwu3xd3OJbPtgaPPXdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي مكثف يحلق في سماء مدينة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87504" target="_blank">📅 02:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87503">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=YaXvGyCRyXfteFnhtJ7aXfavrFX8vrhYuZqUmcj_4LMsbbOzAvvlefs68WtQsHVhcnT8YBtO_CwLqhj1cvjJhd40zxI_FsTR6p6v1BUzspAPmmO3vxz87kPuxb6nlKvkQloNa8nj5cCzvzx-dU78Al8iuiUopCV6UKsPwm39tkq9BtHZsauYH95IiH0xmeND7-Cp-TnlIEZfkRRC0Hr9GNb2SlpBiDOFdtjf0VufRN8EMGdOE-F0qN6A7Cc8PlO97OsWXaV6GWjD0jHuKQYbfHpv4dCuoQhI_92gh-2tE_mpxqdR035Gv-j6NKsAN_aRgPy-KI1ztIbfisoOU8RIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=YaXvGyCRyXfteFnhtJ7aXfavrFX8vrhYuZqUmcj_4LMsbbOzAvvlefs68WtQsHVhcnT8YBtO_CwLqhj1cvjJhd40zxI_FsTR6p6v1BUzspAPmmO3vxz87kPuxb6nlKvkQloNa8nj5cCzvzx-dU78Al8iuiUopCV6UKsPwm39tkq9BtHZsauYH95IiH0xmeND7-Cp-TnlIEZfkRRC0Hr9GNb2SlpBiDOFdtjf0VufRN8EMGdOE-F0qN6A7Cc8PlO97OsWXaV6GWjD0jHuKQYbfHpv4dCuoQhI_92gh-2tE_mpxqdR035Gv-j6NKsAN_aRgPy-KI1ztIbfisoOU8RIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هجوم جديد بطائرات مسيرة يستهدف مصانع مدينة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87503" target="_blank">📅 01:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87502">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87502" target="_blank">📅 01:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87501">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87501" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey3kYypzikks_YWvCkXTCcajkcPfi4g7imGbkMty3k9JJiOUcvK79NExJkZGL2ExSDkgHoBEwFKHedeS3vM1cU5sMb-DzoDlXaHiUoWCdH10wlaSDlyz3FRftoBzyDIZBGanz3qCtQ-d6Pj9q2VJEywQ4721RdWPy1vgKWqH9u4wKd3dkNU5y7ETldH1VprR3xD5mWvGIPOQbF86eEZ3lb3ITkL6Aq74j4_Y8GcTMNDWJFOf6Q4k0k5wQr7NBXzaqS8D15IxxWkFHCDLPWnXNE4XCnuAH1D8qSoN6S4_d-wXML2RVRsuhUR8_--knqe6hLtWZ4fN49F92Cu-aTvfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
به نیابت از گروه‌های بسیج مردمی در عراق، انتصاب "شیخ ابوزینب" به سمت فرماندهی بسیج در جمهوری اسلامی ایران را تبریک عرض می‌نماییم، و تعهد می‌دهیم که بر مسیر رهبر شهید انقلاب، آیت‌الله سید علی خامنه‌ای، استوار بمانیم و پشت پرچم سید مجتبی خامنه‌ای باشیم تا زمانی که دشمن آمریکایی را در این منطقه به زانو درآوریم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87500" target="_blank">📅 00:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFLomdahIBVn-DFDrzMhPUU6YtoD0nxSeYNDlvNhW94G3EpIX39OlRg6vKTfvqiFBtag_xmF_VHKJKNCELRmKD28YTWgET-Fwm-RsuFwTqAkfkuqGmWJF5MpGgSMMU2qdtvg4hgI5Ba2wvVuzNmCcdxYdBwFB9-EiMvDCkj5fA5PDWb2aNMNW_dUhji3G13EZT-pwSYCBFr2PlUfXzOFxc-n3-7F9bpGXxFWq6f09cqaUZK4CDYDWv7RBaPeml8AuVXn1xQ2MOW2MclzDg7sozNCVzuez4ay-kY0gv0gZZil7GymtVmf5sVcdjbILAcgM0v5FnYV5V1T9suQLsQZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=kQAMGZh2LMbwK1FzROLv6UtsYD4wmUR6rcc-IIX76_C21y2Q7zwgmlm1124FzCOAkwfJFN7q0jJGKT_pAFP83OiHt98G_SzrNd-w9BKfqtjxoGpm-hIJbRlC3EWrcbDRWA9o8JYNzmk9U_xnAKTotaXbijFlwCn5CLERYvs8BKmH8owuk4bT4s5neWbdNYfiLeUuDB5UVUgjK-deovRLJ83Vm1GIaM1dZ1NHx5C7MueTAanYXVjMI_w04gbWbvwNbnv4LiuQca_fu_f4stMdVr-icK9Q-vnjO65EwiChjFLCEbtb_6zOxz_Fc7yAwjEHFPjre7AcoleGiZNI7UHTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=kQAMGZh2LMbwK1FzROLv6UtsYD4wmUR6rcc-IIX76_C21y2Q7zwgmlm1124FzCOAkwfJFN7q0jJGKT_pAFP83OiHt98G_SzrNd-w9BKfqtjxoGpm-hIJbRlC3EWrcbDRWA9o8JYNzmk9U_xnAKTotaXbijFlwCn5CLERYvs8BKmH8owuk4bT4s5neWbdNYfiLeUuDB5UVUgjK-deovRLJ83Vm1GIaM1dZ1NHx5C7MueTAanYXVjMI_w04gbWbvwNbnv4LiuQca_fu_f4stMdVr-icK9Q-vnjO65EwiChjFLCEbtb_6zOxz_Fc7yAwjEHFPjre7AcoleGiZNI7UHTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
احتجاجات واسعة وغلق عدة طرق من قبل المتظاهرين في محافظة واسط العراقية بخصوص تردي الكهرباء وخدمات اخرى.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87497" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الاعلام السعودي:
قائد فيلق القدس إسماعيل قاآني يصل بغداد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87496" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=Ep2IbXW6zFdiEkW_x1U0zTQ5e1BKh6cMnX0LEdx_sPNSRVYck07cG6vuHYp8jajPB9FFdaWmyfdg57Elb-gnYFjA8Ur21Cs2CevCwnM5myPlaBeGemLoLgR1c2ej7WAL5Ch9KlF8mWtZN_ExokfRlfuOS84yO6GtEaQ0xbzVc_RwFrygs2mG3yyIIOwApzvpK_b2yxdhreO7KqM5mnJfeFFnmmJdyCOT_SrY73axN3rIGVflSgsx9dr2Ma9nwMDqVP-CzsOPYU5VaHVDBg6iWZtfrIaytyrtZW-PLk9uLpJNCD-meSdColQC4pvfQA7ST2tulthMgjS34bVjgVjRA3xKPLDVOS81JeSF5q5IdHQjYsbCYwgttkK3r2XU9ozRG38-xn4lArjH8FjQURrwrxq-R2j1ttsfc6Guf-R85jB6kKb4otgiX5J9M3-3mfc8M4tasNzLJEs5y6dmnT1zKVnvIyt0YcTvSYxhQ43JwXetuE-_BasxjE5eQKHfu93ZDJ2Nwg_v6GsRaSE1NCZAEMErpYUr5ps1wmAUABIFZfHJ-JTdSAXCfvO5Nto-S2uHMAp7hqW4hlVTrHeip7BIE7qhjP13N7-zILAWQpA5eRiTYiNGNnsTFee-qhSRbvfQ1mYnmw5lrMAfgFbltfSaz0kSLxsFff9LaPkyRYYAlZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=Ep2IbXW6zFdiEkW_x1U0zTQ5e1BKh6cMnX0LEdx_sPNSRVYck07cG6vuHYp8jajPB9FFdaWmyfdg57Elb-gnYFjA8Ur21Cs2CevCwnM5myPlaBeGemLoLgR1c2ej7WAL5Ch9KlF8mWtZN_ExokfRlfuOS84yO6GtEaQ0xbzVc_RwFrygs2mG3yyIIOwApzvpK_b2yxdhreO7KqM5mnJfeFFnmmJdyCOT_SrY73axN3rIGVflSgsx9dr2Ma9nwMDqVP-CzsOPYU5VaHVDBg6iWZtfrIaytyrtZW-PLk9uLpJNCD-meSdColQC4pvfQA7ST2tulthMgjS34bVjgVjRA3xKPLDVOS81JeSF5q5IdHQjYsbCYwgttkK3r2XU9ozRG38-xn4lArjH8FjQURrwrxq-R2j1ttsfc6Guf-R85jB6kKb4otgiX5J9M3-3mfc8M4tasNzLJEs5y6dmnT1zKVnvIyt0YcTvSYxhQ43JwXetuE-_BasxjE5eQKHfu93ZDJ2Nwg_v6GsRaSE1NCZAEMErpYUr5ps1wmAUABIFZfHJ-JTdSAXCfvO5Nto-S2uHMAp7hqW4hlVTrHeip7BIE7qhjP13N7-zILAWQpA5eRiTYiNGNnsTFee-qhSRbvfQ1mYnmw5lrMAfgFbltfSaz0kSLxsFff9LaPkyRYYAlZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87495" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
🇸🇾
‏
الاعلام الاميركي
الوكالة الدولية ستزيل قريبا مواد نووية مخزنة في موقع سري بسوريا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87494" target="_blank">📅 23:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af84017206.mp4?token=P5mflu4ypQ9u8KUb3LTqZYsqlQQklxY8Qyxq7IOjxJbQIp2zLL-VSBQwMFeeAvHb7SHb5p6KfAzpO4KRPJ4q5pqqHfyR9BMPtQpr3EDiXK7VToc60mPTSCTZY6eH2RRXkedzOCRW5SLELwxTm06i3WP3Nu05OimkR15UcqVxb6Kl6fqCsTLpdNI5uRIf4dY7QlpfycQuglI0HXrc-DqlzBO9piNY6ngNDXurBwmBnbhDZ9A2A9O6t7sfubuXE3L44QJQ02FH6lJy3lIWcGsJN-nBjxV-aD8kmqe2qsmJ0DqAvnBxz5GH8E2LfhNTtNMEe4Q8-yv50PxGFHsO2Og-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af84017206.mp4?token=P5mflu4ypQ9u8KUb3LTqZYsqlQQklxY8Qyxq7IOjxJbQIp2zLL-VSBQwMFeeAvHb7SHb5p6KfAzpO4KRPJ4q5pqqHfyR9BMPtQpr3EDiXK7VToc60mPTSCTZY6eH2RRXkedzOCRW5SLELwxTm06i3WP3Nu05OimkR15UcqVxb6Kl6fqCsTLpdNI5uRIf4dY7QlpfycQuglI0HXrc-DqlzBO9piNY6ngNDXurBwmBnbhDZ9A2A9O6t7sfubuXE3L44QJQ02FH6lJy3lIWcGsJN-nBjxV-aD8kmqe2qsmJ0DqAvnBxz5GH8E2LfhNTtNMEe4Q8-yv50PxGFHsO2Og-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن إيران:
ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87493" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=JVjKOAgpmnrG3qPfohdfyhRH4Sk2q2bCfEN88rglKVLOBwJBswHJNUeSsMn_QlBPC7SK_k4TUoJmH9koS3jBuLn3ZkDDsQ7ew5TkMWzAe0mwvIhaq1lG7PiBxBpFT4vi9EQN0vSOzIPYW1cvjLj_10lhm75i5AJQhRXJwq2Mcnc84QE_HfF9sUETj3rNYbmXtXlKQ6K1XmtPJLufMsRkeRysPaFQixeW14HBbKCD2GfZYUCICBXBYfmNZxig4WwKkfVu_Sh3s64VcBv8ZxTGoMGAOTw9yI1XPqtmQeCVmuCdWUT_ah2w82_I5DglUUyKSFr-6cCKDiYuzQMpfktxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=JVjKOAgpmnrG3qPfohdfyhRH4Sk2q2bCfEN88rglKVLOBwJBswHJNUeSsMn_QlBPC7SK_k4TUoJmH9koS3jBuLn3ZkDDsQ7ew5TkMWzAe0mwvIhaq1lG7PiBxBpFT4vi9EQN0vSOzIPYW1cvjLj_10lhm75i5AJQhRXJwq2Mcnc84QE_HfF9sUETj3rNYbmXtXlKQ6K1XmtPJLufMsRkeRysPaFQixeW14HBbKCD2GfZYUCICBXBYfmNZxig4WwKkfVu_Sh3s64VcBv8ZxTGoMGAOTw9yI1XPqtmQeCVmuCdWUT_ah2w82_I5DglUUyKSFr-6cCKDiYuzQMpfktxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الضربات الجوية التي دمرت 8 مضافات لعصابات داعش الارهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87492" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea061f9pNXoSrobayE28Bxe0mNVUQxZAq5UooTWxza2eYp8xODcPiCvbo96yKunLikswYRKnZ8gc4zfbsp2UcF9aUrI1b2jLFB8XhzsoCvne-Fmzl7ChWDJwr_ndB1WCXK4MqI7TEt1MUUkwmuMb9yp6teZ5Wz-ADUU0zGQoE78kwKm3r_4pYp62eFwnEi5zFNo1hc4xT-pyh_8E7ugeCSxFMjv_-Y9xF-xLDxxFs-j8Pj4zZXeFf43XfpR_6FoOh4KvxXR8YM4kBNRunROd-lUt2LBFw14m6hRWEOYQ-GnSY8D0uqjO0NCodzb2wlY2gnYja91Z_wuopEc2WO_lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحيدي من جديد...</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87491" target="_blank">📅 22:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87490">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=b2dxpjjySwVP-rZyfR29tPiP7Zm3olgYJBHmHOh5LlEa5ncGXHi8zCZRla9YFDNhOJAGLGhNuiyGsKBbiH_tvhSDDEnEilmqd1BGgxi6SqiRHuTrxboF1z2_NjzKDiH5vdDwprDVqGh4CrFF_woHDycpPJDIZFmhEQyNk_uQjEMJd2x5f2nJquKCPBPZ-LVrp16tX8_UXkJG9Hdo8cgOQrsWBHtUwbkQn4hbv7h5cnFhDXJcHTe5oPbp1LLWUI98yNe3faPMDZO4aXkwXxoXKNkm8uAmP_3p6ZDIjZC6HFs_x_6KivkjGfmf8P4NObRAOR3_lQSEaSgH3ZmoTyF2ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=b2dxpjjySwVP-rZyfR29tPiP7Zm3olgYJBHmHOh5LlEa5ncGXHi8zCZRla9YFDNhOJAGLGhNuiyGsKBbiH_tvhSDDEnEilmqd1BGgxi6SqiRHuTrxboF1z2_NjzKDiH5vdDwprDVqGh4CrFF_woHDycpPJDIZFmhEQyNk_uQjEMJd2x5f2nJquKCPBPZ-LVrp16tX8_UXkJG9Hdo8cgOQrsWBHtUwbkQn4hbv7h5cnFhDXJcHTe5oPbp1LLWUI98yNe3faPMDZO4aXkwXxoXKNkm8uAmP_3p6ZDIjZC6HFs_x_6KivkjGfmf8P4NObRAOR3_lQSEaSgH3ZmoTyF2ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ثاني حادثة في مصفاة الزاوية حرائق واسعة تطال المصفى عقب انفجارات مجهولة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87490" target="_blank">📅 21:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=B2JVcZp0xSjxK6NUbqSkJJHtE9uLC_QOL48STyN8vhJuvuzJfU_YyeD1OY5z-8mJ6LGCuTu7GYy-m0piEWkP4K7SQ43UeYYDd5C9j5LgzvRT_0JJwPCYdFbvQOQiufkGEv-QKtOZc5GVxJ4m1QMeixeF8lTxxBec7vZF_mVnq2J_XtfmZJLxwnZjGr6QFf_4UjeysC71a4GbT3HC4LpiKkDDOAAxhsOyangAQOfpAH3IPciVSv9pCQthbIMDIM8r32Cz_HDJCYBtNZPxkLy1VXrTkZdzbjI01OBzGVBQHEtcHa2UeaeLQzcp0BhlrU97TlhqLTTOtJ3mIFH6U1NcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=B2JVcZp0xSjxK6NUbqSkJJHtE9uLC_QOL48STyN8vhJuvuzJfU_YyeD1OY5z-8mJ6LGCuTu7GYy-m0piEWkP4K7SQ43UeYYDd5C9j5LgzvRT_0JJwPCYdFbvQOQiufkGEv-QKtOZc5GVxJ4m1QMeixeF8lTxxBec7vZF_mVnq2J_XtfmZJLxwnZjGr6QFf_4UjeysC71a4GbT3HC4LpiKkDDOAAxhsOyangAQOfpAH3IPciVSv9pCQthbIMDIM8r32Cz_HDJCYBtNZPxkLy1VXrTkZdzbjI01OBzGVBQHEtcHa2UeaeLQzcp0BhlrU97TlhqLTTOtJ3mIFH6U1NcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87489" target="_blank">📅 21:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87488">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87488" target="_blank">📅 21:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87487">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=MF4vEcYQ2OaFPye-ZygINgIPx4rAWMhXVWc28ifuCmUOl-9mNfT9jyNyI3k8R5D2J5evvWnUzZ-gwlHPCGHiQmTdyuyH8p-jjdpiaHkUgQNebIymL6evJKZScCqx2Gvhi_HZ2sMAuYPr5PG2r5M6tUK3UaDGlKxTLiUEJX-cr6pzvBvDsGLIC63ZjFPkKLOe7OPQRBCyVocM9LefJ9h4SZjKEMoJSQDbdFPkK2iRoNCsz0AVtJz2kQDeAqDYqXLEH3gymTtkw5J6RygKmjbSoDhyvBIhpGDXdtBAnT0PO2c-_LSIJsvVdI7C0rvHXVV6nAWYfThzMdS8lTvdgbau2oFAzxijjbo9_iSsK-SJRkRcgUeQFOuUjMRCZ62x-_WAt0nyFarFDikvaGqnhjqTr7748gzuod5rRXXdXNFFBeGYpatr8QeMEF-aeQmv-kpJ_uWmFJR5U2Wa3hM_Y2nk0_edt5c39_31G3E-WF3JagsxwefCc_GtyBFsk12FeX5Rcrur3nfLaIwFyQu0_1QEcKzn8OIPXewoAQuH4UvXNEyxxIMnEBVQe_lThw1y-l0TiD_TPgzyqyHFglAYwa2Q6H8IK1YFLOBWLnJfDFxRZ0QSqUh3fywlWdidEekZS9Acm9pmKQxX7je1emVOm438DnpnnGFkZqsEBtxBdmqwS88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=MF4vEcYQ2OaFPye-ZygINgIPx4rAWMhXVWc28ifuCmUOl-9mNfT9jyNyI3k8R5D2J5evvWnUzZ-gwlHPCGHiQmTdyuyH8p-jjdpiaHkUgQNebIymL6evJKZScCqx2Gvhi_HZ2sMAuYPr5PG2r5M6tUK3UaDGlKxTLiUEJX-cr6pzvBvDsGLIC63ZjFPkKLOe7OPQRBCyVocM9LefJ9h4SZjKEMoJSQDbdFPkK2iRoNCsz0AVtJz2kQDeAqDYqXLEH3gymTtkw5J6RygKmjbSoDhyvBIhpGDXdtBAnT0PO2c-_LSIJsvVdI7C0rvHXVV6nAWYfThzMdS8lTvdgbau2oFAzxijjbo9_iSsK-SJRkRcgUeQFOuUjMRCZ62x-_WAt0nyFarFDikvaGqnhjqTr7748gzuod5rRXXdXNFFBeGYpatr8QeMEF-aeQmv-kpJ_uWmFJR5U2Wa3hM_Y2nk0_edt5c39_31G3E-WF3JagsxwefCc_GtyBFsk12FeX5Rcrur3nfLaIwFyQu0_1QEcKzn8OIPXewoAQuH4UvXNEyxxIMnEBVQe_lThw1y-l0TiD_TPgzyqyHFglAYwa2Q6H8IK1YFLOBWLnJfDFxRZ0QSqUh3fywlWdidEekZS9Acm9pmKQxX7je1emVOm438DnpnnGFkZqsEBtxBdmqwS88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
إيران جعلت ترامب يشعر بالخوف والقلق الشديدين، لدرجة أنه بات يحتاج إلى نظام دفاع جوي قصير المدى من طراز AN/TWQ-1، مزوّد برادار AN/MPQ-64 Sentinel، لمرافقته أثناء ممارسة رياضة الغولف.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87487" target="_blank">📅 21:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87486">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=fnA53eRPDKTSS4t_27m2usqTiBldLsSJRuJJi5Maxxcij5YVN1jNBlaCV8leccyHiZuUvOQxWipmP-Ru3XV7lfO438EIDDfPBmq-8MS5C-UJWZ1INatCO7uJ4vQqLK-qmUXcpvz65AT-nOfJRmGm5pURAVWerlDlNiI0YhFqKiT8oBH8KrU7KaRAugGtcLuOcD9GaUmQFJ2351Hd8xYgwpfUwBD1dHjxLB5pPm2k2o0_SZo1OZ8Hpjrfxkuye0lbKVOfdOXtujkUbb1QIiOLspn4BS5T1w0Sezb9F6UeEm2HX5vmbV1gEqvOj7JhIZvNDEElvnXiFQtSWJ-Kg5HKVDlqjQG9P1z_3AvS5zY2TC3sNSrzCd5ADLUoQfCgX1nbKyiSTzv3UHlHDd8TEOaVGVKlr1vZprvcl-q0jWiyEjHyEOR2fXcjmrUK_GeRzCZ8CmtC83zDY4mtK8ifHQCFNih3u0ijdP-qeExW_KwbJciHmqrxPlPnvqRdLRPwPG19cJhFQFLjB-3PktBFD93dpM1pEnEYCoIERjFSrctXwCthpgCpcdiOpylabafYIfH9nurldAbIQsSulxrpu95geOf5pM9f_nhIj9yThk4HhwMiHLU4lHFBe5Z2WOIo-dk8b28YkJ9B2tud4lrhbne0J-owKqMl40SH_Tb8RDsknCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=fnA53eRPDKTSS4t_27m2usqTiBldLsSJRuJJi5Maxxcij5YVN1jNBlaCV8leccyHiZuUvOQxWipmP-Ru3XV7lfO438EIDDfPBmq-8MS5C-UJWZ1INatCO7uJ4vQqLK-qmUXcpvz65AT-nOfJRmGm5pURAVWerlDlNiI0YhFqKiT8oBH8KrU7KaRAugGtcLuOcD9GaUmQFJ2351Hd8xYgwpfUwBD1dHjxLB5pPm2k2o0_SZo1OZ8Hpjrfxkuye0lbKVOfdOXtujkUbb1QIiOLspn4BS5T1w0Sezb9F6UeEm2HX5vmbV1gEqvOj7JhIZvNDEElvnXiFQtSWJ-Kg5HKVDlqjQG9P1z_3AvS5zY2TC3sNSrzCd5ADLUoQfCgX1nbKyiSTzv3UHlHDd8TEOaVGVKlr1vZprvcl-q0jWiyEjHyEOR2fXcjmrUK_GeRzCZ8CmtC83zDY4mtK8ifHQCFNih3u0ijdP-qeExW_KwbJciHmqrxPlPnvqRdLRPwPG19cJhFQFLjB-3PktBFD93dpM1pEnEYCoIERjFSrctXwCthpgCpcdiOpylabafYIfH9nurldAbIQsSulxrpu95geOf5pM9f_nhIj9yThk4HhwMiHLU4lHFBe5Z2WOIo-dk8b28YkJ9B2tud4lrhbne0J-owKqMl40SH_Tb8RDsknCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تُعرض للمرة الأولى توثق اللحظات الأولى لانتشال جثامين شهداء العـ ـدوان السعودي–الأمريكي على قطعات الحشد الشعبي، وتحديدًا في قاطع عمليات ديالى.
وقد صُوِّرت هذه اللقطات قبل وصول فرق الإنقاذ، علمًا أن مصوّر المشهد كان جريحًا لحظة توثيقها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87486" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87485">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhgbQQJw550fAF3ppXjtaGAk1Nof0OXpo5OoUwqiTKaBgW5M-lbHBtkqMylZPAEh2vn8qLb-q6be7A0un15wt4joWooVxfv_g-6obAcv45PFENGJ0TGOoQMGVSBIca2CYW7RvsDoA3jvaMof57sjcA8pKBkh8nTvgfUOjAcYQaHgI2G6uUTyp-jPl-ixQUUT7lIOgqENKA_GQVrDEn3UfOrpsQE5Gi7nISkpUeniqITGKCI13DLUq2HRgojkXTQHNtMaxo0R6rnLWlVk5XgAZn6rQc-uzW_-mRw7MCuqzthGiadMd0f4IlAUe_I2s7eqrWSl-xSYblQ0ALR8WaO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87485" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87484">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
تجميع لضربات انصار الله في اليمن وهم يدكون تجمعات ال سعود على غرار لحن اغنية Believer.
مشاهدة ممتعة...</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87484" target="_blank">📅 20:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=qPX9UnUAE9HUtYL_q7m-b2DsWbE2Z7GMLFf79O9Uv-DdciqS0-sh3hR7ZBmw47hgwmwDwmbwX4OiETxJ3TfWC2pi2JJHa-PbR7ESvx3N4pgsPpLKWiW7i2SpYCD_cF8b5Gka-YpKiFEXaT5DTjAoUztSry75t4Ct9qALMTbcs4tf8QLo5TV--fe4Qim9HqHyGsASfdPD85mOaPDAeWOTrI_20qSTWT5E7QYtQxSG7mqi4KFRR9tcZm6QVGfgtaQ2BkCqfab0-ZJIowWbLLe2I2slY3Iho96EhLAb-F8ML70dT-Oxm0Gm1IoUKvpMQNbEOOeW3t9rFnXXyniyk2gadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=qPX9UnUAE9HUtYL_q7m-b2DsWbE2Z7GMLFf79O9Uv-DdciqS0-sh3hR7ZBmw47hgwmwDwmbwX4OiETxJ3TfWC2pi2JJHa-PbR7ESvx3N4pgsPpLKWiW7i2SpYCD_cF8b5Gka-YpKiFEXaT5DTjAoUztSry75t4Ct9qALMTbcs4tf8QLo5TV--fe4Qim9HqHyGsASfdPD85mOaPDAeWOTrI_20qSTWT5E7QYtQxSG7mqi4KFRR9tcZm6QVGfgtaQ2BkCqfab0-ZJIowWbLLe2I2slY3Iho96EhLAb-F8ML70dT-Oxm0Gm1IoUKvpMQNbEOOeW3t9rFnXXyniyk2gadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87483" target="_blank">📅 20:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbmWn2Q2kHxMU_T88kis6rOoAv1IFjKk4upNNeThtIvp1MIX1qQZfQxSN3qnr1zViidpjrKI2mFa9IBHWobVaWVaE2ceWYy8Tt20wwCLgII00-jJbEo5H75TpSjIJfYsEpiOQHZgUX7Dgp9HjmyX_qGztUgXwxp_RqUzq9brBGmSeAHtM71XLhRfDtoEim5NBZpMQ4DYzSIZU17tINW9XKuLfDnS5ARiMD2w7uXwSbpHkNnNkOBq5P6kRDQ-gOgGjvML-kI6ta7ImOkQsjMUl75-iqvlHnjpI5rmgTzaPtQllOusC76poVtsmpWK7nusWKSE06GeM3wd8jGU6R8iwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها فكرة مثيرة للاهتمام، لأنني أطالب الآن بدوري بتعويضات من إيران عن جميع القتلى والجرحى الذين سقطوا جراء قنابلها المزروعة على جوانب الطرق وفي العديد من الصراعات التي اشتهرت بها، والتي قادها في البداية الجنرال سليماني، بما في ذلك عائلات ضحايا المدمرة الأمريكية كول، وآلاف آخرين سقطوا في المعارك. إضافةً إلى ذلك، يجب دفع تعويضات لعائلات مئات الآلاف من المتظاهرين الأبرياء الذين قتلتهم إيران على مدى الخمسين عامًا الماضية، ناهيك عن 52 ألف قتيل سقطوا في الأشهر الخمسة الماضية. لقد وجهت ممثليّ بوضع هذا الأمر بشكل حاسم في جميع المفاوضات المستقبلية. شكرًا لاهتمامكم بهذا الموضوع! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87482" target="_blank">📅 20:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87479">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7cf11d6c.mp4?token=Xguy1BQSrT5Qnv-WOESrr0XSHdqfMLrx4i8x58MqhljbCHD8l1uyzpg1vqcv3cDmrBoseiMJETMuIksbfrBqG3t2gRE9f_7-qH3LtLyjSwRxjh_vSH7RHxkfPRaKV-Gi4inm-HAVAXNsTIWyH8dFMb_F0I2wIyIYIVOzE0PrJySM7rMVfKcaVCkDHCvRoNeDbYxkgWA_Vb40LvHrQ33ifPsLG7f2qNl_tj-IuTsHB-ky6CebKAJU5OWvSfZYL5nIhXjxWOLd-iyUxR647g35ed0NICG7Ks5C5ibfuA0fDOYOlNOfCy-iaxCjk-nsvwj2wbi459PJ7l7uyq1MVzvGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7cf11d6c.mp4?token=Xguy1BQSrT5Qnv-WOESrr0XSHdqfMLrx4i8x58MqhljbCHD8l1uyzpg1vqcv3cDmrBoseiMJETMuIksbfrBqG3t2gRE9f_7-qH3LtLyjSwRxjh_vSH7RHxkfPRaKV-Gi4inm-HAVAXNsTIWyH8dFMb_F0I2wIyIYIVOzE0PrJySM7rMVfKcaVCkDHCvRoNeDbYxkgWA_Vb40LvHrQ33ifPsLG7f2qNl_tj-IuTsHB-ky6CebKAJU5OWvSfZYL5nIhXjxWOLd-iyUxR647g35ed0NICG7Ks5C5ibfuA0fDOYOlNOfCy-iaxCjk-nsvwj2wbi459PJ7l7uyq1MVzvGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تحضيرات من سكان الكورد لقطع الطرق احتجاجا على الاجرائات التعسفية التي تتخذها عصابات الجولاني بحق القومية الكوردية في سوريا.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87479" target="_blank">📅 19:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87478">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2SdlO6PhY-C1hHlk7Ov-_9IAqHwlXR208QkKxzjKbS_pK0Wtz2_FMUhYLhSsUMOrRRRW63PHdvx8fFMJgQjAHtC2eKz9GcOthrc59JLz8vQDmDNoNCJfhaQmpL2I6z2lxzALQ0wD2cGv_IseRyaQQhmU24Pf-Lqox_x_t-P9itpzjdHE5n6VZmlQB1Mtbo05GiY6iQSzpFNn_S5bWeFyXdWwCTrspx-M2HYVLOwUinXTRliVkWGNtFhzoYPGnyXW_DUcIMN47hxNyaqog1lrOhqONRX9GIn9DQdL-_rcdH7L6Cmcn1xC4IVHJr0UU4RcGmDZwAx8LqDuDkK0kGyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
السيد القائد في إيران السيد مجتبي الخامنئي يصدر حكماً بتعيين اللواء علي عبداللهي رئيساً لهيئة الأركان للقوات المسلحة وتعيين اللواء أحمد وحيدي قائداً للحرس الثوري واللواء مصطفى إيزادي نائباً له وتعيين العميد علي عظمائي قائداً لبحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87478" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvR_yiULm5DwBpeVHMfVh44W8bkk-SSYU03H2yjf96xjCJPU1wnmtlUDXmDSMPF9OK7CXKBTuL42QgpRHStqWRvS5MNQO0kZ7vOn6YUj3qVcrIvkO2YCMi7dhUkRkNTP2W9Bl4MBdV_IhLdg8LrmLZRm-btjpp7-CsXPQRZpySG0k9WK_PPe4YuZFpQvTaIqcb8QIW8ImF9BM5kpR8zspfri7TN-4PBosVH8OIEy4r1Hh8jiseBpKVplICVDWkfXeaO608OwJRlxuDyifRdINitTnEf6VYRo2quzqByiDkalrxCv8f6N6ah-Z1WVGFvzf-zA21xRmSOoqf0ckleojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة: أوامر بتعيين عدد من كبار القادة العسكريين في الجمهورية الإسلامية الإيرانية سيتم نشرها خلال ساعة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87477" target="_blank">📅 19:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=P2G6IFV2YQvdMhDLsx0edQO-e0pxVbKM5GrUV5_92nYoY75ocY0LxCpcKKaPoIrXE1hJtyT-8caX4M6OdkDUolnZ8WH7udiUx5zqMhuUnI2vrCc2ZFp1UaLHkbsXJ-OlNLcJXr_OPQFe4LgVxZ0gWbOvrB7hKa1-C1aSdgIntiz-k-gplVtQ6tYsi4duZ-r_DKwe3JTF_O8m1ZTrMqcQBmxOX5pvu_K6CEKm1fGW1IvY3VXih-IfXTtSSY_Z3lKsi2jMAznBBZqkj6i9GuYKOL_0P0XEB3zLakSt0hoeiMbjxDARiz3iq_grGCCpYkC8amoEAhrK9n3Cs4K38pjwzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=P2G6IFV2YQvdMhDLsx0edQO-e0pxVbKM5GrUV5_92nYoY75ocY0LxCpcKKaPoIrXE1hJtyT-8caX4M6OdkDUolnZ8WH7udiUx5zqMhuUnI2vrCc2ZFp1UaLHkbsXJ-OlNLcJXr_OPQFe4LgVxZ0gWbOvrB7hKa1-C1aSdgIntiz-k-gplVtQ6tYsi4duZ-r_DKwe3JTF_O8m1ZTrMqcQBmxOX5pvu_K6CEKm1fGW1IvY3VXih-IfXTtSSY_Z3lKsi2jMAznBBZqkj6i9GuYKOL_0P0XEB3zLakSt0hoeiMbjxDARiz3iq_grGCCpYkC8amoEAhrK9n3Cs4K38pjwzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87476" target="_blank">📅 18:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87475">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87475" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87474">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة:
أوامر بتعيين عدد من كبار القادة العسكريين في الجمهورية الإسلامية الإيرانية سيتم نشرها خلال ساعة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87474" target="_blank">📅 18:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87473">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
🇮🇱
اعلام العدو:
أميركا تواصل تقليص عدد طائرات التزوّد بالوقود في مطار بن غوريون، عدد طائرات التزوّد بالوقود الأميركية في مطار بن غوريون تقترب من مستويات وقف إطلاق النار.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87473" target="_blank">📅 18:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87472">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87472" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87471">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87471" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87470">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:  توضح هيئة الحشد الشعبي أن المقرات الوهمية التي أعلنت عنها وزارة الداخلية، والتي ادّعى القائمون عليها انتسابها إلى هيئة الحشد الشعبي، لا تمت إلى الهيئة بأي صلة.  وتؤكد الهيئة أن إجراءات إغلاق هذه المقرات ومتابعتها نُفذت ضمن عملية نفذتها…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87470" target="_blank">📅 18:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87469">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🇸🇪
جهاز المخابرات السويدي يزعم إحباط عملية استخباراتية روسية في السويد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87469" target="_blank">📅 17:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يشنون هجوم مسير على مرتزقة السعودية في المخا.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87468" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87467">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الايراني محمد باقر قاليباف يزور العاصمة بغداد الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87467" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkMxRuVnYE6R0EOWWuSuNt708ryaXibiBhZlHEQV06MVghR6sC5wV044pn0txo9xYPokN0UizcFZbsInL3KR8XZTwoXwEMwRIy8d8Ku-vIYYoBMRm7gLFK7B64H7BoG6oG7Sy2DGGTkqwVJWw2XONMomLB5evI7-5jpE9LEF1Liq1mS1rupg1bnz_RVPGQ2GCUNpCT3V9sxSoxA0xo653OEB5NQfAq9jGku_oWiu6eSuVj8bP2zfKcJWAvY76gXiI6ZX2-F5gMpGup_IDT9aWjxFzkdieL11fy-2C6wROg_LJeYfGZMjKrxx3yHE2TE8DnXgd1JvgfdeTkrEAoKhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع حريق قرب مرقد سيد محمد (عليه السلام) في قضاء بلد شمالي العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87466" target="_blank">📅 17:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d385f60930.mp4?token=KABYIiFZ2YdZdlHghN4AKP9TZpxW1sKTSJ0tku1_NDLRj-ULbTg_3asrN5JtrhluP6qrFoFjtobJdIU7NoRZNdjgf2bjcvUFiA9DI76YE9tQaqYN3voPfAAv43h8kEk-GPNa2WeFYe4xvGvWNgaxfcn4ddLirkCJZmfY-t6eitj-rWAsdT9yoCluiI-deryWFwMOwZvFqMkZx-lFIH38v66_7Lf7c8DIYG-Czl087elTMCOczMWxHY2J3VDLm3tGyOC6ogkufJCqb1c3Ysrts4D582Z4zLRsQW-Wtr1XdAxtlCSO07QFeRkWu4LTObXeUb59C6yom7ttWZpRPCSoAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d385f60930.mp4?token=KABYIiFZ2YdZdlHghN4AKP9TZpxW1sKTSJ0tku1_NDLRj-ULbTg_3asrN5JtrhluP6qrFoFjtobJdIU7NoRZNdjgf2bjcvUFiA9DI76YE9tQaqYN3voPfAAv43h8kEk-GPNa2WeFYe4xvGvWNgaxfcn4ddLirkCJZmfY-t6eitj-rWAsdT9yoCluiI-deryWFwMOwZvFqMkZx-lFIH38v66_7Lf7c8DIYG-Czl087elTMCOczMWxHY2J3VDLm3tGyOC6ogkufJCqb1c3Ysrts4D582Z4zLRsQW-Wtr1XdAxtlCSO07QFeRkWu4LTObXeUb59C6yom7ttWZpRPCSoAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87464" target="_blank">📅 16:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87463" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=i5hWrL-ks0smgt5dwnUYlwsFiadx-hJeBdVjQOZkHwSXKmlgnerjgpyrnYP9ptgdMAIDtpS0XYSz-b-SKQ4umwDAjj9oGikI2sH93RGIDL7nbtE4Z7d_oBBi7voMTY3rGASlw3R9t9MNSOHyEv7QtyNVXf6TTwxl70uYF-yWuVjSvy6qSJJhLFBSsd9seEnpn5HRtUlDaXmhoA0xkr35LOIabvWxHgwLgyv9KrNNTsfe4O8F6xMzdx1RvgeINFaGfr2IkbdxvFG1q6qqT0K8fS0g79h214Nj2C8IOg9wjEeBFvbuzSO70nnnDcXiaso8qQS4XCmUBbdna0Y_qcGTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=i5hWrL-ks0smgt5dwnUYlwsFiadx-hJeBdVjQOZkHwSXKmlgnerjgpyrnYP9ptgdMAIDtpS0XYSz-b-SKQ4umwDAjj9oGikI2sH93RGIDL7nbtE4Z7d_oBBi7voMTY3rGASlw3R9t9MNSOHyEv7QtyNVXf6TTwxl70uYF-yWuVjSvy6qSJJhLFBSsd9seEnpn5HRtUlDaXmhoA0xkr35LOIabvWxHgwLgyv9KrNNTsfe4O8F6xMzdx1RvgeINFaGfr2IkbdxvFG1q6qqT0K8fS0g79h214Nj2C8IOg9wjEeBFvbuzSO70nnnDcXiaso8qQS4XCmUBbdna0Y_qcGTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية تعتدي بالضرب على المتظاهرين المحتجين على تردي واقع الكهرباء في محافظة ذي قار جنوبي العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87462" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87461" target="_blank">📅 15:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
المتحدث باسم حرس الثورة الإسلامية:
صواريخنا لديها القدرة على التوجيه، وحتى بعض الصواريخ يمكنها تغيير مسارها في مواجهة منظومات الدفاع الجوي للعدو. حتى إذا تم تحديد هدف لصاروخ ما، يمكننا تغيير ذلك الهدف في منتصف المسار وتحديد هدف ثانوي له.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87460" target="_blank">📅 15:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch-tmTXsmthJIv6WmKIV4RUWmRXU9OdBC64jXTcTsc5OKmil_I9dbvgYwET2oNYk7d3pgQXJ46JJsRdgLlcYF_6TdmsTnBJFl3nhdrDGMxM6QzEKpGYDJirdjxswpHIbpga5datYqE0COKqW_5v0OHmrHvzwsnC7vkNBWOhSX3QiFMhMJodVwB3vdo5H4zNXn5jrZmy5jW05Jw6EQHF9JrRmmLOcElHsZv-y0tx8xN2IuhCGABDakBM04Ihlfzpt1HSYce97ZuaKZoZHcLWvxngJ26AwliZuR47o-Lm3YgPiHPE28PeJpxvU1k5d5lOR6r3gC3JvX15Q_-_gLpHOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انه زمن الديكة الشرسة اذ ولى زمن الدجاج الابيض … بحر الما يغرك ينعبر كل يوم
؛ والديج ضربته توجع</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87458" target="_blank">📅 15:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
مواطن من بغداد يتعرض لصدمة بسبب الارتفاع الكبير في أسعار الوقود في إقليم كردستان شمالي العراق وسط اتهامات لعصابات مرتبطة بعائلة البرزاني بتهريب كميات النفط ومشتقاته المخصصة للإقليم إلى تركيا ما أدى إلى شح الوقود وارتفاع أسعاره بشكل كبير على المواطنين.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87457" target="_blank">📅 14:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=te-LxHGPAbavgULMMD81DiNAa6K1JZbtzd5DJ3zBVoZdVgSufSopGANsdQEIP-iIMHv0sDQTKyuAWs17TqvdLgtx8mP6SX4FIQgMu_45CEvA6nXf8PpaTzLqhryhH2GJAhCZ0SKTxpY5hjs1Bzrbd1_ZkL3V5tPHTtjs9WzVsy-830ubq7gaHp1wPs4CeDseeOEsFl-P3LvCJ5JJ521di37t0KCCTV79GWX5FFKQc2lWr-JKLiNDjgv41wDFUZN6tUV8hTD1AM0i-w9itQQH_WELrVsJhMZasGqvoxoaAsSl5tOueqPTp3hVYBk1kLO2kVmnsOhDfyGdxsBYY4PnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=te-LxHGPAbavgULMMD81DiNAa6K1JZbtzd5DJ3zBVoZdVgSufSopGANsdQEIP-iIMHv0sDQTKyuAWs17TqvdLgtx8mP6SX4FIQgMu_45CEvA6nXf8PpaTzLqhryhH2GJAhCZ0SKTxpY5hjs1Bzrbd1_ZkL3V5tPHTtjs9WzVsy-830ubq7gaHp1wPs4CeDseeOEsFl-P3LvCJ5JJ521di37t0KCCTV79GWX5FFKQc2lWr-JKLiNDjgv41wDFUZN6tUV8hTD1AM0i-w9itQQH_WELrVsJhMZasGqvoxoaAsSl5tOueqPTp3hVYBk1kLO2kVmnsOhDfyGdxsBYY4PnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعض الديون لا تنسى .. الحرب السعودية المفروضة على العراق</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87456" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87455">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صفارات الإنذار تدوي في العاصمة الأوكرانية كييف وتحذير من هجمات باليستية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87455" target="_blank">📅 14:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
الحكومة العراقية:
هناك تنسيق أمني وعسكري منتظم لتسلم المواقع التي تشغلها قوات التحالف الدولي في حلول 30 أيلول المقبل.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87454" target="_blank">📅 14:01 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
