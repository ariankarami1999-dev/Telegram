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
<img src="https://cdn4.telesco.pe/file/JQQwhzS45mHFYcY1yBYyo4r6Xx8Jg2JFhM3LjBAfpD61k2bkoblETF_xYOf4xaKFI0jWHsmeqGqlwU2NB9-YwPyD1ldmuTBcMK7FCB9RT77TlHibCOIhhUFJ7SAn343nsDvacdiIzqnrqa-qaLBxu-5gOXv6MQxT1GJ67cyFaLhx0xdQc_F2xyoeu32gLg2VVCfi_vdt0t5jqrOuDliwrX_iO2yWum5plHuxXbQQe0SmWtbXUqTI-bjNI4FBXzpyCVCro9qvwACwVXVzoeTtvrK7djWZIFn070H0qmCOEIoYepdG35BTPkMwmGyyxyss5-1OmAjd2hFZ6ov5blwORg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 04:31:00</div>
<hr>

<div class="tg-post" id="msg-87257">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e351fb75c.mp4?token=oTwsut4ppa8MdLG3rwudz9GYeRGcoV__cuo5W2ANZTbjI4pQZt3dCyGSbY1nNIMgTKOCYPuNb-9BK4r4ywmQlbLY3dM67tGPbUIaU6Rjxwg2cFH89Phs4g9ql_cGPrfPaQOcFaLmyltVtoZq3-3GJjwezmq1_nhEaJHcJE-rh0tf6zCcR9n_zDJbKRXvgmCaY8qJBH48YTpmB6nqq1LuXJOzy_l3uA7CrSvWLp46KvCRdrJJMXuYzY9rMn2V8KVca-IsoAUbvfdM8e07xRZUPA4e9xi3wUiNLbNr5BEVU6fDIDCTMiAbUINLTN1HN0i383a6osjaNRivTZJLrE-tJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e351fb75c.mp4?token=oTwsut4ppa8MdLG3rwudz9GYeRGcoV__cuo5W2ANZTbjI4pQZt3dCyGSbY1nNIMgTKOCYPuNb-9BK4r4ywmQlbLY3dM67tGPbUIaU6Rjxwg2cFH89Phs4g9ql_cGPrfPaQOcFaLmyltVtoZq3-3GJjwezmq1_nhEaJHcJE-rh0tf6zCcR9n_zDJbKRXvgmCaY8qJBH48YTpmB6nqq1LuXJOzy_l3uA7CrSvWLp46KvCRdrJJMXuYzY9rMn2V8KVca-IsoAUbvfdM8e07xRZUPA4e9xi3wUiNLbNr5BEVU6fDIDCTMiAbUINLTN1HN0i383a6osjaNRivTZJLrE-tJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إشتعال النيران داخل سفينة بالقرب من الساحل العماني في مضيق هرمز بعد إستهدافها أثناء المرور من الممر الجنوبي للمضيق.  "وترامب يؤكد أن المضيق مفتوح
😆
"</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/naya_foriraq/87257" target="_blank">📅 04:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مداهمة منزل في منطقة الكاظمية شمال بغداد من قبل هيئة النزاهة يعود لأخ شخصية سياسية معروفة</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/87256" target="_blank">📅 04:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مداهمة منزل في منطقة الكاظمية شمال بغداد من قبل هيئة النزاهة يعود لأخ شخصية سياسية معروفة</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/naya_foriraq/87255" target="_blank">📅 03:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAwOk54PKQKm0mt-7q6MrQMNQDKkCE_4kFg9pwiHINXP-n9-HLBwhdjIFfqjOdJt4ZOxpsx8M-Vxtsy_RzDgkZVwAVcD3qeWNN3qJTyYj9fw-Ene_GptrpsMgy5iaEP1P1iKWmcI2y9QOxkSLUxQaDH97wZZ8x206jwJUfTAc8CbnxNNjNJ9qZMrQNFtWhGoJpuppxYjxzcZ29Mwl9ERAwaAo01zQ51D8_10aIdeKFH9_jwyxox4DXbRSt3qsYOiNA-ZJxELZRh4OFV_qSWvNMQ9a_SXfANdHA0k-AX2wqtXVPDd-GuIOnoBzlKd6nN3wjfH_YK79Ye2FVjpmdZpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إشتعال النيران داخل سفينة بالقرب من الساحل العماني في مضيق هرمز بعد إستهدافها أثناء المرور من الممر الجنوبي للمضيق.
"وترامب يؤكد أن المضيق مفتوح
😆
"</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/87254" target="_blank">📅 03:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce4bbf82a.mp4?token=TKB394r_eUP8iUFFSnjJIxMqPI4trVczJSQXGXLlJHWlAKOf87ehMhzHBJxwI1pOu7IL0hOFwIs6mlajt3R2bqI5oFTz1ew7hj4rU1tIgVMPC1qruu_GLutx5WSuJfKnKKpzZOpTB_kRHu72DBEsPuDDguQOd3YAQ5exTeVFAG-ISvdXKseekSr3xssU33wnFY9hxe_6J_qQIVGqTFrowCF6WPLJyi4Z2FqUbc21eIp6D1rOt2UD_JP_8dTZDTvoC35vn8_pKo96v45EuD41iJjmqS0_hqDBd9YimM8KE82Xa1GZR8tlzRpASCQlVL6LKfUwztYJ_S4xgbDlamKF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce4bbf82a.mp4?token=TKB394r_eUP8iUFFSnjJIxMqPI4trVczJSQXGXLlJHWlAKOf87ehMhzHBJxwI1pOu7IL0hOFwIs6mlajt3R2bqI5oFTz1ew7hj4rU1tIgVMPC1qruu_GLutx5WSuJfKnKKpzZOpTB_kRHu72DBEsPuDDguQOd3YAQ5exTeVFAG-ISvdXKseekSr3xssU33wnFY9hxe_6J_qQIVGqTFrowCF6WPLJyi4Z2FqUbc21eIp6D1rOt2UD_JP_8dTZDTvoC35vn8_pKo96v45EuD41iJjmqS0_hqDBd9YimM8KE82Xa1GZR8tlzRpASCQlVL6LKfUwztYJ_S4xgbDlamKF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحن لا نشجّع على الحرب،
ولا نحبّ الحرب،
لكن في كل حادثةٍ أو اعتداءٍ،
نواجهها بكل صلابةٍ وشدّة.
وقد أثبتت التجربة ذلك
🫡
الشهيد الأستاذ والمعلم
قاسم سليماني</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/87253" target="_blank">📅 02:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d93912779.mp4?token=GRL6DnqIU8L4-q08eeKW_1OBEk6YA8h3-g8ErjCXpf7AYSnpQ7aWHTIQA4oaANanX05qVLcogLmSnpzLvjG9s_NXIx8-OZbDQPOcRsxixLAb7DOI12W7XAhGykszBz2OR8KeANx8xFMwX4mWKkgqqxYKUgyXn55CmbMSedzb6SO7qbuz0k0kOQWeZ8ybVDRdfxaaQVl3oTCzpI_csUn2GrE6JuWcPzUmR9zp5XrU-uYhYb7ZbBXJBnauNPBkaZFTeaMNmudN6Hz7ds6aydSMC1tfZbi2kAJAwFNrJjR2fpobNcPMi2jimLxM5maaOZthDDlK4YxL4I0O2k3qu2xYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d93912779.mp4?token=GRL6DnqIU8L4-q08eeKW_1OBEk6YA8h3-g8ErjCXpf7AYSnpQ7aWHTIQA4oaANanX05qVLcogLmSnpzLvjG9s_NXIx8-OZbDQPOcRsxixLAb7DOI12W7XAhGykszBz2OR8KeANx8xFMwX4mWKkgqqxYKUgyXn55CmbMSedzb6SO7qbuz0k0kOQWeZ8ybVDRdfxaaQVl3oTCzpI_csUn2GrE6JuWcPzUmR9zp5XrU-uYhYb7ZbBXJBnauNPBkaZFTeaMNmudN6Hz7ds6aydSMC1tfZbi2kAJAwFNrJjR2fpobNcPMi2jimLxM5maaOZthDDlK4YxL4I0O2k3qu2xYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إشتباكات عنيفة بين القوات اليمنية ومرتزقة السعودية شمال " الخوخة" غربي اليمن؛ سقوط عشرات القتلى والجرحى في صفوف المرتزقة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/87252" target="_blank">📅 02:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULyKo4XfgumEcMoyjvFbi4fXatjSJeue6vXbbCmPZpollX0G7SPl6zh3AfRkLSA-dbcoB3FdXCA1tsGzozstFKGTe-SJpAnfUulFoXJ5l21QODkPpUdgI-V--1FATy-W6zn5h1VPUDuZyVz0fiX-f9hmSEr-g3HkXboJwJo6l6LOsI-nsqXMI72gwgtYI5mJCewcfEVvDO4SKc3ni3xd5xU8oRmHRRdkXA_zM7ASUbR63IGI3bbzh19TPGzqpEgWd7b65OhFdENo4ZgtDzBY_t6WSieNZ7C_Zp12raM2VdukkD5d9m4IHNDG6CypgoBVa8oHKwfEjk5lFoi4hw01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
"قال قاضيان، أحدهما عينه باراك حسين أوباما والآخر جو بايدن النعسان، في حكم بشأن مجمع قاعة الرقص/المجمع العسكري الذي تشتد الحاجة إليه، بما في ذلك مهبط طائرات بدون طيار رئيسي على السطح، إن "كل رئيس هو مستأجر مؤقت ... للبيت الأبيض". لسنا مستأجرين ندفع الإيجار ونقوم بكل ما يفعله المستأجر، بل نحن رؤساء منتخبون من شعب الولايات المتحدة الأمريكية، ولنا حقوق عديدة، منها الحق في إصلاح وتجديد وتأمين وحماية وتجميل أراضي البيت الأبيض، الذي بُني وأُعيد بناؤه، وجُدد مرارًا، ورُمم، وببساطة، أصبح أفضل مرات عديدة منذ عام ١٧٩٢، دون الحاجة إلى إذن من الكونغرس أو أي جهة أخرى. هذا القرار، الذي اتُخذ بعد إنجاز جزء كبير من العمل ودفع تكاليفه، يُشكل تهديدًا للأمن القومي على أعلى مستوى. إنه أيضًا عار وطني. لنجعل أمريكا عظيمة مجددًا!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87251" target="_blank">📅 02:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OshOAFwx1KIbvr2FqDhGIZW_uMVdW5GAL_mR-sATdTbnH1lAqG_50ihpuqeJSom6tpRAOa-mNOopEX4ypb9wJkDAKEGJtEoAek1ifO2Mmfk2SAyRS9rhM4GlQKwruDSOp5J62mkoVimXHh8HAD8tAGGfRpwEs8y9TTbw9YwKD7sia_KeA6QKeHDY9Dhqb8hoVPcLUZ4rsHD9KNi7X9QAChnVjLK8soo_b5fCmXtldjNkwhUG9c_LHlujtGjdEyat1eCTD_KmsBExRe0e3kj9XNbcCXCa0b3YT7CDx9exbtZKqDoDyspEnWGsLxP7oa2aCk2powazMC7h_2AInjfsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ليست دوريات روتينية
يستمر الجيش الاميريكي في عمليات الاستطلاع والدعم اللوجستي في سماء خليج فارس بتصرفات لا توحي بان هناك مفاوضات وحالة هدوء …</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87250" target="_blank">📅 02:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c84570fd5.mp4?token=nEu-Zcg0kzbA_Y2wik2eY9Rmw3Gc8M66deJ6D8jBzzFA_2YSnjEWidqZwud8RQm2WzbmWRkeclVl3jpBohl8mWph0aHCkqUMIATBscHV960nXcZmiuOXjzUbT5iExO65lToeNzMP4oXexM0tU87iENQZDV4O5QHpcCDOvyoxbIEZJpain9RU7TzwqZNS510Iflk3gdmMsqV96glXSGZX2oQ_Wl9MN2KtFnppDFpHsYA610hOWgRgg0x1tOBFhXb_szC1Q5aaHns7b_nKaVGU2HM8VLE8npaNP6oLEdx4BXqu_kIpx6244Y_CTZV-GyL6gLGsqe3wS5BM6Tw9TMCOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c84570fd5.mp4?token=nEu-Zcg0kzbA_Y2wik2eY9Rmw3Gc8M66deJ6D8jBzzFA_2YSnjEWidqZwud8RQm2WzbmWRkeclVl3jpBohl8mWph0aHCkqUMIATBscHV960nXcZmiuOXjzUbT5iExO65lToeNzMP4oXexM0tU87iENQZDV4O5QHpcCDOvyoxbIEZJpain9RU7TzwqZNS510Iflk3gdmMsqV96glXSGZX2oQ_Wl9MN2KtFnppDFpHsYA610hOWgRgg0x1tOBFhXb_szC1Q5aaHns7b_nKaVGU2HM8VLE8npaNP6oLEdx4BXqu_kIpx6244Y_CTZV-GyL6gLGsqe3wS5BM6Tw9TMCOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
تم الإبلاغ عن فتحة ظهرت في السياج الأمني في زيكيم، الواقعة بالقرب من قطاع غزة. تم توجيه السكان إلى البقاء داخل منازلهم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87249" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
أي بي سي:
عزل الجنرال شارلز كوستانزا، قائد الفرقة الخامسة المشاة التابعة للجيش الأمريكي في أوروبا، بشكل مفاجئ من منصبه قبل حوالي شهرين من الموعد المحدد لمغادرته.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87248" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
سي إن إن:
الجنرال دان كاين، رئيس هيئة الأركان المشتركة، أوضح بشكل خاص لمسؤولين كبار في إدارة ترامب أن الولايات المتحدة بحاجة إلى "إيجاد مخرج" من الحرب مع إيران، معتقدًا أن الخيارات العسكرية المتاحة لتصعيد الصراع قد تنعكس سلبًا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87247" target="_blank">📅 01:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-ua8icTeG8akzkUH2Asv9eYad93KS0gfWnh_HQoYW2PEK3aV908r71gbHmOB41Cen5edkONeX8wwLVoIw1HNuabk6A73wCq5dMyBGCJQ7BXBA2v-mhyYACu7IHNjCAYN__g_UBU1QLpPNEKB07hFuhNLjNZVL_a50Jv8lTjmairl6qYnIb2E5tsbZyZq07KMGdzAJ5SX9XC34Mpz9QLkpjy2W4ZMFoKVRto1pSkXf_tdCXe2QaAiRYhTgacrs8-7e9xIQtaAtBv-kYt6wATB27a5q2Y0In6x948Vdmg2DWlN8jYYa8gqMgS6aEdt01YI0ARdZ2A3QreUo6bibhhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
الولائي: إن قرار المقاومة الاسلامية في العراق بالتريث جاء استجابةً لطلبات الإخوة قادة الإطار التنسيقي، وبمقدمتهم الاخ المجاهد ابو حسن العامري والشرفاء من السياسيين المستقلين.
⭕️
الولائي: إن إعادة النظر في توقيتات الرد وحجمه ونوعه لازالت قائمة، وهو واجب عقائدي ووطني يتلهف له المجاهدون وذوو الشهداء والجرحى وغيارى الشعب العراقي.
⭕️
الولائي: على المعنيين استثمار هذه الفسحة لإستعادة حق العراق بما يتناسب مع حجم الضرر الذي لحق بوطننا وشعبنا جراء العدوان الغاشم.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87246" target="_blank">📅 01:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تدعي:
تحييد عنصرين من تنظيم داعش الارهابي كانا يحاولان زرع عبوة ناسفة في السيدة زينب بريف دمشق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87244" target="_blank">📅 23:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⁩ ⁩
وليس تكليفنا أن نُجمّل الأخطاء أو نبرّرها. فإن دافع الإنسان عن الموقف الفلاني لمجرّد أنّه صدر من الجهة الّتي ينتمي إليها فهذا يعني أنّه يدافع عن نفسه أكثر ممّا يدافع عن الحقيقة. وهذا ليس عملًا يُبتغى به وجه الله، لأن العمل لله يقتضي أن يكون الحق هو المعيار لا الأشخاص.
يجب أن نُخضع أنفسنا للحق،
لا أن نُخضع الحقَّ لأنفسنا.
⁩ ⁩
زهراء " دامت بركاتها "</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87243" target="_blank">📅 23:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3147050c.mp4?token=pMVhhwazMq__F3v3FZYv0KiLlJFGLGXThFi2H9W9q_sz0AO_pF2yPtygg4SyP2kZCaeTnxItFTIOLw8Q_Q2N2guL_POmNTsqHwXk515JDn-3YCC0CwsdnWVETA7i9OetSjaE2MUOb-ds5jwX8QWLcv0jvSbnJmlr7bgnbSxp3NUUKF3D18uQEkSnYgBLoc5v1H6Hn-feU760onH5aHGjZjmcaapE5eDrLARQFYphPcq4Ufjtc_Pb1rxCS2DPoU24s-BRPVfKqzYxqb0ONCWJuyM4XOsVgGvlCIO14F5AMFoPM2hYxwfDymWPbfU2TNP2RCsey8BGnhEwXQWWdgaIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3147050c.mp4?token=pMVhhwazMq__F3v3FZYv0KiLlJFGLGXThFi2H9W9q_sz0AO_pF2yPtygg4SyP2kZCaeTnxItFTIOLw8Q_Q2N2guL_POmNTsqHwXk515JDn-3YCC0CwsdnWVETA7i9OetSjaE2MUOb-ds5jwX8QWLcv0jvSbnJmlr7bgnbSxp3NUUKF3D18uQEkSnYgBLoc5v1H6Hn-feU760onH5aHGjZjmcaapE5eDrLARQFYphPcq4Ufjtc_Pb1rxCS2DPoU24s-BRPVfKqzYxqb0ONCWJuyM4XOsVgGvlCIO14F5AMFoPM2hYxwfDymWPbfU2TNP2RCsey8BGnhEwXQWWdgaIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب يلغي مؤتمره الصحفي:
لو أمكنكم المغادرة سريعاً سأكون ممتناً، لأن لدينا حرباً يجب خوضها. هذا عذري للمغادرة مبكراً قليلاً.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87242" target="_blank">📅 22:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏هناك تقدم بين سلطنة عمان وإيران بشأن مضيق هرمز، ونتوقع التوصل إلى اتفاق قريباً.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87241" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏هناك تقدم بين سلطنة عمان وإيران بشأن مضيق هرمز، ونتوقع التوصل إلى اتفاق قريباً.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87240" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
التصعيد بالتصعيد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87239" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
‏
الاعلام الاميركي:
الجيش الأميركي يعتزم شراء أجهزة ليزر مضادة للمسيّرات بقيمة 400 مليون دولار.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87238" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRSZZQvDK1FeKm0b4pQVjrMMTTTAaKq75UFhadwAJQjoJq3KLlRhzFIqU2PsW5RxcR7TWrczEBKf2O_ARQn1-wxI_1n0U13RluhorD490Njnj_26B1c0UEo1QxTE8lia-cVwVkP_fUnMGxe8JAAXXh16oM0UedLssdW7Is6nXVSk9n8gSMY6gog8I7txzg9SyhTI6a2DQA6lT670bMWzskORlMFAAdLShPO87cImpPL5lIsvh1AWL2m8klo55TTlH9ocIniLQIghVblkZt-Gj3LjcYYMRKYdh2WYSioow3ozbVYsCg-p9CdgUUi6LeCkds83vIENBM9CCFESJoer9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
أظهرت القوات المسلحة الإيرانية القوية جاهزيتها وقدرتها وقوتها في مواجهة أغلى جيش في العالم.
‏عندما يتحد المسلمون، نستطيع مواجهة كل تحدٍّ من قبل الغرباء الحاقدين وجهاً لوجه.
‏حان الوقت للاعتماد على أنفسنا فقط واحتضان الأخوة الحقيقية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87237" target="_blank">📅 21:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052f59ac5e.mp4?token=j-QA0kzQTkqZAJPoXYdqzNIa6CEsLwvUirzjzIXsgQHs83hqpqSwVs-GbRoc1UoaS1RtLPJ-XJo6s8c20tQE6TejSEPfv5XPoAZwwcNowSnFst6mZvFEYKWMHQ25xmYToct_6hE6IYRY9VKjBMp8yXNCSHFdoiSobgnuj9PEAxRljN8GALE5PHmbaQ7GjE0MZWMFNYrrisj1b8QUco61Z41N6PJPM_VPfLOLOHfgQ0dGwHGRWfiicMwdVdnE9VysEH5lw2ld3HSPK6jvze0CcCDZK27TrEBgkXM6cEdkvYkhv8sNDHBvbasU0BDAH3OoWaFZjos6cSDbWoySUNh-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052f59ac5e.mp4?token=j-QA0kzQTkqZAJPoXYdqzNIa6CEsLwvUirzjzIXsgQHs83hqpqSwVs-GbRoc1UoaS1RtLPJ-XJo6s8c20tQE6TejSEPfv5XPoAZwwcNowSnFst6mZvFEYKWMHQ25xmYToct_6hE6IYRY9VKjBMp8yXNCSHFdoiSobgnuj9PEAxRljN8GALE5PHmbaQ7GjE0MZWMFNYrrisj1b8QUco61Z41N6PJPM_VPfLOLOHfgQ0dGwHGRWfiicMwdVdnE9VysEH5lw2ld3HSPK6jvze0CcCDZK27TrEBgkXM6cEdkvYkhv8sNDHBvbasU0BDAH3OoWaFZjos6cSDbWoySUNh-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
إغلاق مطارات أبها الدولي والملك عبدالله بمدينة جازان ومطار نجران الدولي في السعودية وخلو أجوائها من الطيران المدني.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87236" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87235" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">يا ابو جبريل جيب الثار</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87234" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تجدد القصف الصاروخي لانصار الله على معسكر صحن الجن في مأرب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87233" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87232" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
‏
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ
‏بسمِ اللهِ الرحمنِ الرحيم
‏قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم
‏إصراراً على مواصلةِ حصارِ شعبِنا، وتصعيداً في العدوانِ على بلدِنا، يواصلُ العدوُّ السعوديُّ تحشيدَ قواتِهِ وتحريضَها ودفعَها إلى أتونِ حربٍ عدوانيةٍ باطلةٍ وخاسرةٍ.
‏وعليهِ.. وبعدَ رصدٍ دقيقٍ لتحركاتِ قواتِهِ ومرتزقتِهِ،فقد تم ضربُ هذه الحشودَ بما معها من المخازنِ والآلياتِ والمعداتِ العسكريةِ في معسكرِ "صحنِ الجنِّ"، وكانت —بفضلِ اللهِ— ضرباتٍ نوعيةً ودقيقةً بعددٍ كبيرٍ من الصواريخِ والطائراتِ المسيرةِ.
‏إنَّ القواتِ المسلحةَ اليمنيةَ ماضيةٌ في مواجهةِ التصعيدِ بالتصعيدِ، وتؤكدُ أنها ستضربُ بشدةٍ أيَّ تحشيدٍ أو قوةٍ يأتي بها العدوُّ السعوديُّ لإبقاءِ الحصارِ مفروضاً على بلدِنا، وتؤكدُ القواتُ المسلحةُ استمرارَها في تثبيتِ معادلتي: "الحصارُ بالحصارِ" و"استهدافُ التحشيداتِ السعوديةِ العدوانيةِ أينما كانت"، ولن تسمحَ بأن تمرَّ المخططاتُ العدوانيةُ على بلدِنا دونَ ردٍّ فوريٍّ وشديدٍ.
‏نجددُ نصيحتَنا للمغررِ بهم والمخدوعينَ من أبناءِ بلدِنا بمغادرةِ معسكراتِ العدوِّ السعوديِّ والعودةِ إلى مناطقِهم قبلَ فواتِ الأوانِ، وندعوهم للمسارعةِ للنجاةِ بأنفسِهم وألا يكونوا وقوداً لجهاتٍ خائنةٍ رهنتْ مصيرَها للخارجِ وهي تتاجرُ بهم وبدمائِهم في سبيلِ مشاريعَ أجنبيةٍ احتلاليةٍ توسعيةٍ على حسابِ أمنِ وسيادةِ واستقلالِ الجمهوريةِ اليمنيةِ.
‏نحيي بإعزازٍ قبائلَ مأربَ الأبيةَ والشرفاءَ الأحرارَ لوقوفِهم إلى جانبِ شعبِهم ضدَّ الاحتلالِ والوصايةِ، ونؤكدُ لهم ولكلِّ قبائلِ اليمنِ أننا إلى جانبِهم ومعَهم لانتزاعِ حقوقِ شعبِنا المحقةِ ورفعِ الحصارِ عنه.
‏واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
‏عاشَ اليمنُ حراً عزيزاً مستقلاً،
‏والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
‏صنعاءُ، 24 صفر 1448هـ
‏الموافقُ 7 أغسطس 2026م.
‏صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87231" target="_blank">📅 20:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بسم الله الرحمن الرحيم (وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)  تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87230" target="_blank">📅 20:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">علي فالح الزيدي يستقبل رئيس جهاز الاستخبارات العامة السعودي</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87229" target="_blank">📅 20:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87228">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c00-QP1qzYDSDdSJYgAciMa68T46g3XwKINroJy93y9OqYcT1I_NAwt9OZ1MPZ_hJSS9waK5cD2ceyTnN1ag13v82N9fdh04FyDReAHIR7qBQdPDgQbpxzsX6VjG-6DNh4IcA7aJ_hKLUYtgnE1K4SReOCgcm7fST1gMVFxdXAFX3diDrp0ybvKoefoPg010JRZ0C1emaQ7PPe9mj_VICP9Vi9Wue134nMaCs5FjoJcK0bpvXhT0vN3lI40tgW0PAwk-ZtpFk5X1UxSDiypBh9W_ZqINSio36JUQSasBe6SmqWxK3W8-BT_bCHgx9UYTPBfaeSpnWxYVxNMjoKU3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم (وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)  تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87228" target="_blank">📅 20:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87227">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">" التأجيل سيد الموقف "</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87227" target="_blank">📅 19:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA5xsiOoMdSYhi5jKOndvd25gXZhCtfeGkhPk9-B4fP16OQygDlxhYG5FpuXXJnI5AMSHIuJZPmfOPrZdng2hNeaqXDsUzHgiqeaY3hJJt4nfJSt6qjKBfaGZxvTZBqFaO1skmVrBtcsjxoy2Nqw4njsV_2rZmnDitRyYA3tv8qJlZAnYskHoVymiRHoo0NwP7v2PDeU5QeKdKOPnAHfZwr9nHoqq-eoNElIrYm_RUtkHgHRDnwS1_eAdayUjD6Rrk_gl3a8GZ8mJGcbMNE3HhPhgynFxTByU0hYFL6wmSGxrdqgICcG6jpQrUVBfaqwgUJ0H6czU_1Rl2u_cC08Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)
تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث والعشرين من شهر صفر الخير.
وإذ نؤكد أن دماء الشهداء الزكية ما كانت ولن تكون سلعة في سوق الموازنات السياسية، فإننا ندعو من أعماهم الكرسي عن صون الدماء والسيادة المنتهكة إلى مراجعة أنفسهم والرجوع لرشدهم.
وليعلم العدو الأمريكي وحلفاؤه في المنطقة أن دماء شهدائنا وجرحانا هي وقود صمودنا، وأن السيادة لن تُسترد بالبيانات الخجولة، بل بقبضات الأوفياء الذين لا يساومون على حرمة الأرض ولا كرامة الشهداء.
المقاومة الإسلامية في العراق
7 آب 2026 ميلادية الموافق لـ
23 صفر 1448 هجرية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87225" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87224" target="_blank">📅 19:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87223" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87222" target="_blank">📅 19:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انصار الله رجال ابو جبريل يهاجمون بالصواريخ مرتزقة السعودية بمدينة المخأ الساحلية في تعز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87221" target="_blank">📅 19:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
-
أي تكتل إقليمي أو عالمي لن يتمكن من مصادرة حقوق الشعب اليمني المشروعة
-
بدلا من تخبط النظام السعودي بحثا عن حلول للمأزق الذي أوقع نفسه فيه، عليه أن يتجه لإنهاء الحصار وكل الأنشطة العدائية في اليمن
- الأحرى بالنظام السعودي أن يبحث عن تحالفات لإنقاذ الشعب الفلسطيني المظلوم وحماية المسجد الأقصى من العدو الصهيوني
- أي تكتل إسلامي لا يجعل من القضية الفلسطينية ومواجهة العدو الإسرائيلي عنوانه الأبرز فهو يخدم أعداء الأمة، ومحكوم عليه بالفشل
- شراء الولاءات وبعثرة أموال بلاد الحرمين لن يمنح النظام السعودي الحصانة لكل الجرائم التي ارتكبها في اليمن
- الجمهورية اليمنية حسمت أمرها واتخذت قرارها في المضي قداما لانتزاع حقوقها المشروعة كاملة مهما كان حجم التحديات ومستوى تطورات الأحداث
- ما دون الحقوق المشروعة هو الذل والخزي والهوان، وهذا ما لا يقبله اليمنيون على أنفسهم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87220" target="_blank">📅 18:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8XIHq66WSAe5Z5M4Or2_N01kVmPvhU6WgLbArlj3ojGZuqVdeLgU9vx8Ft14f_q5IQCRlM7gBqO75JtxbTqrgFmnwu5ris5qaGpX1sIEfPD-KyekgdDpIGyoYa2LtVVOB-D59KRml5jh2eQw6GcM-jIR3AdoxyiuUvo327070h949QtMJKy_AQKGEy-iJXEd3Gy1u-eEsN6H14_lBYwQbw00W_SIUawsP2F1jkzBkXuq3y6HGLCdvKd-Rv20hOFKxpeUNQVPM2kYco3TtkFP6vFL5bGmIu0XhDPa2lN6OxsB3n-rQSNsoJGykITgvco9vvSB_aA0ftpEkDECWKVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milk him , MBS loves milking</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87219" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط: الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87218" target="_blank">📅 18:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87217">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انصار الله رجال ابو جبريل يهاجمون بالصواريخ مرتزقة السعودية بمدينة المخأ الساحلية في تعز</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87217" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87216">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط: الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87216" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط:
الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87215" target="_blank">📅 18:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/87214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/87214" target="_blank">📅 18:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhfTTc15GAvWTzFUTR0tStP9_yweBkFG3c93AjNxVvVjnfomO2Rha3XLi3pTN8Ppc6oERsqGA-fJaIMOLkrXhYfMGMQff7yDl0EEbR5K6fKil94iwWt8Mukv-JO2f8gklRwBgi4t0biIStu8jteN0K_oW0pZ5UQrRkivp9BqQILlCIJjvB6O7Q7joxRAVsW66g4XLk8PLbRWotbjRVMVR384f6UoNvZw_gfsiImcwW2TnwWGwQ4eGYExMyypw73UZ152dw31ywqsPhSbRcskqij-XpxV1NOB8xTzSIjv3XhoTNuyPsuGOXaiMlNSoEL4OE60g8glAG_P7RX0WdXFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بين عطوة الكلداني وفديو عطوة العامري
قصة عن أمة يراد لها ان تكون مسلوبة الإرادة ، فلا تتعجب بان تتجرا الكويت بقتل صياد عراقي ولا تتفاجئ ان يتجرأ الجولاني عليك بقادم الأيام ؛ ايران لم ثبت معادلة الردع بتهديدات الشهيد سلامي الشفوية رضوان الله عليه ، فمن ثبت معادلتها امام العالم ودويلات عرب الخليج هو الخيبر شكن وفتاح ١١٠ هذا وليعلم من يريد ان يستسلم للحرب المفروضة من ال سعود على العراق ان تكلفة الاستسلام اعلى من تكلفة المواجهة ..
يالثارات العراق
🇮🇶</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87213" target="_blank">📅 18:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg5aO1o8p49ijSR7y1eR-nN-rNo77j6LDhhZzAdM-KjBBBEELsM5iU4epCOOrex48g5dt-fG9fWB0o54dZoxu34Y0T4lkxBu8su3NUvO1nF5fJ4JvvUUI_8yQBBxgF196JX0cJ2KOLNUw_5uVIFBAz2aMgaCshOrRdyZWTzTtQhRCpoMnRBnUzFpDQKW9DVXapZG4ffta-xonHCXVRMgpUodB4lc5-tw5j8GXr4tNrmnLD_n7NepJZIi3_TbNi0lEdgYNWbpAUAq4NXYkJmToI_iKcEfAOAfHK166A_zxAgzSYzaTVcmP1go6q2OGdMZ2rrGXO8HKbOBGzB5-ECIDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعودية والكويت تقدمان مذكرة احتجاج جديدة لدى الامم المتحدة ضد خارطة المجالات البحرية العراقية وطالبوا بسحب الخارطة و قوائم الاحداثيات و تؤكد السعودية والكويت بان هذه الخارطة تسبب تداعيات جسيمة بالعلاقة مع العراق ، والسبب هو للاستحواذ على حقول النفط والغاز…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87212" target="_blank">📅 17:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
🇺🇸
‏محكمة الاستئناف الأمريكية تقرر ايقاف مشروع ترامب لانشاء قاعة الرقص في البيت الأبيض بكلفة 400 مليون دولار</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87211" target="_blank">📅 17:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇦🇪
شركة أدنوك الاماراتية:
تعرضت 15 سفينة تابعة لنا للهجوم منذ بداية النزاع.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87210" target="_blank">📅 17:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
وزير الخزانة الامريكي:
أعتقد أنه قريبًا، ربما حتى اليوم أو غدًا، سنشهد اتفاقًا، ووقف إطلاق نار لمدة تتراوح بين 30 و 60 يومًا، وستُفتح الممرات المائية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87209" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3686bd868d.mp4?token=Zs-aPeHHjcFjgrEmVrCHC9Vs1JDANEImfUYkXCBZlQ63J1lS4jUgSt4e5fMwySoQutsxLh_3xWFs4Sq9qqk36AKBacqb-qp1pSI6M_JeRQz1GbqiqbTgobaUNHSLLmHIWaonNQyQiT36zOi8UbsLcOGPD1o0qnA54yOPrr6ffEBM9NSAuzGCy7xUto4uF45-urgIqHK9YF8-s4RscKkJdH94kDgP5uqCQnkjlDZlJYs2Lu0vFp3Ljv5fuG-g12KBcx16v_p-Pzlx1Br_QnKw2iZo1t9Rb7Z36I2y8yA7qC9-9V4AVQEkCc-9rNvBhRZfgABelecYaqoycfKSH4IGfC9X19FUWzD9Vm34zXo48tmR1Z8K3SaJB6MaojcqzXq0ukm0knWtK0T3h7f1IYHN5yHwVPbM3HSr4KV2p66n_HbxOKmlyg483ORoT5U_HhmpvbYP2cP1bugWT6B3FR-_o7z8sl2rOGV56OZDQ3wI4mW5nVC-8jssnohr_xo3YxxzElfJCLqN03fvnoKmcHZq61GwxySMFAcz0Coevueumy7qgjEgAMIBilHf8myAY7fpBejNHLjqY-lSQ96QB_7BYIrMkHjJkqqqFuOmWPFog97tu01hN4P7RQ3kVpdbwMo5CAenjK3wSYouC2wKMQ5G0Z2e3h2gjzcW86arUFF-PJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3686bd868d.mp4?token=Zs-aPeHHjcFjgrEmVrCHC9Vs1JDANEImfUYkXCBZlQ63J1lS4jUgSt4e5fMwySoQutsxLh_3xWFs4Sq9qqk36AKBacqb-qp1pSI6M_JeRQz1GbqiqbTgobaUNHSLLmHIWaonNQyQiT36zOi8UbsLcOGPD1o0qnA54yOPrr6ffEBM9NSAuzGCy7xUto4uF45-urgIqHK9YF8-s4RscKkJdH94kDgP5uqCQnkjlDZlJYs2Lu0vFp3Ljv5fuG-g12KBcx16v_p-Pzlx1Br_QnKw2iZo1t9Rb7Z36I2y8yA7qC9-9V4AVQEkCc-9rNvBhRZfgABelecYaqoycfKSH4IGfC9X19FUWzD9Vm34zXo48tmR1Z8K3SaJB6MaojcqzXq0ukm0knWtK0T3h7f1IYHN5yHwVPbM3HSr4KV2p66n_HbxOKmlyg483ORoT5U_HhmpvbYP2cP1bugWT6B3FR-_o7z8sl2rOGV56OZDQ3wI4mW5nVC-8jssnohr_xo3YxxzElfJCLqN03fvnoKmcHZq61GwxySMFAcz0Coevueumy7qgjEgAMIBilHf8myAY7fpBejNHLjqY-lSQ96QB_7BYIrMkHjJkqqqFuOmWPFog97tu01hN4P7RQ3kVpdbwMo5CAenjK3wSYouC2wKMQ5G0Z2e3h2gjzcW86arUFF-PJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇰
انفجارات تهز عاصمة سلوفاكيا وتصاعد لاعمدة الدخان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87208" target="_blank">📅 17:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇳
🌟
وكالة رويترز:
شركة ريلاينس إندستريز الهندية حجزت ناقلة عملاقة لنقل مليوني برميل من خام البصرة.. الشركة دفعت ما بين 23 و25 مليون دولار لاستئجار الناقلة أي نحو 12 ضعف السعر المعتاد قبل الحرب مقارنة بنحو مليوني دولار فقط عندما كانت أسعار الشحن تتراوح بين 0.8 و0.9 من السعر القياسي. الناقلة ستوفرها شركة "سينوكور" الكورية الجنوبية وهي واحدة من عدد محدود من شركات الشحن التي لا تزال ترسل ناقلاتها عبر المضيق، رغم تزايد المخاطر التي تواجه السفن التجارية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87207" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
الأجهزة المختصة رصدت خلال الفترة الأخيرة ارتفاعاً في معدل الشائعات والعمليات النفسية التي تستهدف إثارة الرعب والقلق بين المواطنين، الجهات التي تقف وراء هذه الحملات تعتمد على نشر الأخبار المفبركة والمقاطع القديمة والمعلومات المضللة عبر مواقع التواصل الاجتماعي، في محاولة للتأثير على الأمن المجتمعي وإرباك الرأي العام، أن هذه المحاولات لن تنجح في ظل الوعي المتزايد لدى المواطنين وسرعة تعامل المؤسسات الأمنية والإعلامية مع ما يتم تداوله.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87206" target="_blank">📅 15:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ewAyKkqoSpUrVKUOiVqHr9s2sUnN6prp7giDUpomcTAvRtPWvq0a8MORpd8MNV9-0uL_GnmBnEGxYur-3mHg3ipNqzC8Efmdf8IjpMa6slHpBwHXy_smOcZlzPxQn0yNyqM-dmpTwXLpQhEmzNObtAXz4lQMePKX1gHgQf50dwsdnFpqXF5ksFvSqUHPTK7xd7wpLhwJtJsFP4yhbhB-_UMfj22MwUwodyt7aQsEsUuqGuIXk3mqQ0bmaKIUE8tnXoJ3cA33RystFfR_yxWKDjjke42CWUCqC-6KQvC9Tsqp_xFuJrTqZfp8rtt81kuk7bSyEtqNw7_q-QcMsVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو لجنة الأمن القومي في البرلمان الإيراني إبراهيم رضائي:
ينبغي للسعوديين أن يدركوا أن اتفاقية ورقية مع تركيا وباكستان لن تجلب لهم الأمن، تماماً كما أن سنوات من الاستغلال الامريكي الأحادي الجانب لم تجلب لكم الأمن. أصلحوا الأمر حتى لا تضطروا إلى التوسل للحصول على الحماية من الآخرين.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87205" target="_blank">📅 15:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية:
لا وكيل رسمي لستارلنك في العراق وكل من يدّعي ذلك يواجه المساءلة القانونية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87204" target="_blank">📅 15:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
🇾🇪
‏بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية نوعية.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87203" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ignou_JYHQob3-lXMfIUaq0jK1PH1IPdvkvO8rRlN4YG5f9P-8r2iqxlbszk6edQ85VAcm_gApw31VWdVViHCMCRJqrNsgM-4aF3fF6detwwTFdZMlEhJfv6E2gz_mJ0DtLffyyxbv911bDHKiaYWN-zQq7roWMdiyq29ui2RIoXmMNgCYJfAEjxt-eFBBxkOCcNaGmgqK2-1USnn0VpCgKovebgXnPEKv-E565BLm1GPLirCjEWb93Dku124RA92u28aQpy4_1K-hoYazkJuS-evDHPKPcOgR4z-o47JZ-ckQeGweW9dSuQlGnB2W4N_ORkEbco15vGIF0o44v58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">للبيع – F-15 Eagle
🔥
تشغيل وقيادة ممتازة (إذا عندك مدرج).
عداد الكيلومترات غير متوفر… لأنها تطير.
مكيف شغال، والمحركات بحالة ممتازة.
البيع كما هي (AS IS)، بدون ضمان.
السعر: لا تبخس… أعرف اللي عندي.
😎</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87202" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزارة الخارجية الباكستانية: تركيا والسعودية وباكستان توقع اتفاقية دفاع مشترك.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87201" target="_blank">📅 14:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارة الخارجية الباكستانية: تركيا والسعودية وباكستان توقع اتفاقية دفاع مشترك.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87200" target="_blank">📅 14:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
اندلاع اشتباكات مسلحة بمنطقة المنصور غربي العاصمة العراقية بغداد  ؛ ضابط في جهاز مكافحة الارهاب يطلق النار على موظف في مجلس محافظة بغداد و القوات الأمنية تفرض طوق امني حول مكان الحادث .</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87199" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
🇮🇱
وسائل اعلام خليجية:
واشنطن أبلغت إسرائيل عبر اتصالات مكثفة ضرورة خفض التصعيد في لبنان.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87198" target="_blank">📅 13:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660bec9997.mp4?token=VEFpSpEY4RwMDRSPXBhPnnLGbT3W7NJd4n-BpRwk1sW1WAtoVT_37hhyCv0M3z-lAtf_mhUNdZci5CuPIB4J1SgF5mF0GLZ29AlepEyG7YVX4qmwkgrTilBNNZw5xSBbN5N1AmXX5nXSmBXPzgeBA5X8Zjlm2NCwv7i6_gFSa1jPyOC0GgGx1IDpv1ZQOOq8ewn6uz1TeTRueFDUDvveB2tJnj9qr33EDp4twvcZIqs1fHmtUZz3gLLq8VUMymYeUSSlq4dUdRYBIsyfJjaJe9hyVxc_1-8ksxvuOO-L_kMKHR-LGsDRZk4KYH2ADwmvHC_MZby3TZ3zS4wCbaQgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660bec9997.mp4?token=VEFpSpEY4RwMDRSPXBhPnnLGbT3W7NJd4n-BpRwk1sW1WAtoVT_37hhyCv0M3z-lAtf_mhUNdZci5CuPIB4J1SgF5mF0GLZ29AlepEyG7YVX4qmwkgrTilBNNZw5xSBbN5N1AmXX5nXSmBXPzgeBA5X8Zjlm2NCwv7i6_gFSa1jPyOC0GgGx1IDpv1ZQOOq8ewn6uz1TeTRueFDUDvveB2tJnj9qr33EDp4twvcZIqs1fHmtUZz3gLLq8VUMymYeUSSlq4dUdRYBIsyfJjaJe9hyVxc_1-8ksxvuOO-L_kMKHR-LGsDRZk4KYH2ADwmvHC_MZby3TZ3zS4wCbaQgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة الوقود في إقليم كردستان مستمرة..
مواطن يفترش الرصيف منذ ساعات طويلة بانتظار دوره لتعبئة الوقود لسيارته في مشهد يعكس استمرار معاناة الأهالي مع شح الوقود وطول طوابير الانتظار.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87197" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae7cba1e7.mp4?token=qokxOAvPAeWUHW9k6iRxZ9XaiZLdJtR_7JbrhTGi0hun3gLbcwzspY9kqhvkd6pMEcF4m3nhw6RhykIKpFd5Zpl3CflhUmKFlvRZ0MgWzzY2vbNnhKoM03EmDnfovEjFyjGt2erqQd8rhqgssCQ0xs8sStlWRi_NK7Bk97y1SwLw8HHGVCgO5b82wc17BFhNsCxLB9zLRAyv6BiBicEd3n1m0-j2sd1vriX8NfWWMxCVqY_tw6nzqN8NLK_X3i8wUfqyPi8MQQMp7BmyeyEDX_1AnsK9Nt84qigYNrCboxHHV1zMqfRu9TrsSB_8XNuolwcydoUU3kOEaLdisvGJQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae7cba1e7.mp4?token=qokxOAvPAeWUHW9k6iRxZ9XaiZLdJtR_7JbrhTGi0hun3gLbcwzspY9kqhvkd6pMEcF4m3nhw6RhykIKpFd5Zpl3CflhUmKFlvRZ0MgWzzY2vbNnhKoM03EmDnfovEjFyjGt2erqQd8rhqgssCQ0xs8sStlWRi_NK7Bk97y1SwLw8HHGVCgO5b82wc17BFhNsCxLB9zLRAyv6BiBicEd3n1m0-j2sd1vriX8NfWWMxCVqY_tw6nzqN8NLK_X3i8wUfqyPi8MQQMp7BmyeyEDX_1AnsK9Nt84qigYNrCboxHHV1zMqfRu9TrsSB_8XNuolwcydoUU3kOEaLdisvGJQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇶
🔻
القناة الروسية الأولى:
بسبب عدوان الولايات المتحدة الأمريكية وحلفائها على ايران اصبح الوضع في الشرق الأوسط متوترا من جديد وتهز الانفجارات بما فيها في بغداد إعادة بناء العراق في هذه الظروف بما في ذلك على عاتق هؤلاء الذين أنقذوا البلاد قبل 12 سنة عندما بعد السنوات العديدة من عدم الاستقرار الناتج عن الغزو الأميركي للبلاد اقتربوا ارهابيو داعش تقريبا من بغداد نفسها
بعد فتوى المرجعية الشيعية العليا اخذ الآلاف من المتطوعين سلاحا بايديهم وتم تشكيل الحشد الشعبي
اليوم الحشد هو ما زال احد اكثر القوى نفوذا في البلد ولا يحبه للغاية الأمريكان وحلفاؤهم
لانه بالإضافة إلى المسائل الأمنية والأنشطة الانسانية يُحدَّث هنا عن العلاقات الحميمة الحسنة مع روسيا وحتى يزيّنون شوارع بغداد بصور بوتين ويسفر هذا عن عدم الرضاء القوي من قبل السفارة الأمريكية
مهند العقابي، المدير العام لمديرية الاعلامي لهيئة الحشد الشعبي:
"اننا نعتبر روسيا صديقنا. في العلاقات معنا الروس أمناء ومخلصون خلافا لممثلي بعض الدول الأخرى</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87196" target="_blank">📅 13:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_X60oTXbFMn6cb2M4hO8wM_1y30d7_wxW0CQaqdDDt7pG4oFwwg5ZFBKN1O1hF8vKtj2sNSz08lZGg6wqPSSwGfI7BXDhZjYcXDrNOD_y9CWQeDyLtsnNSP9xNPXwl3DhGqe8oaEXNwWU6kjG-3g685KByGLOGdoRb1qiZk9a_EpMqI6VfXIxK8nAkz6PC-dv39jEPu9FZzLY-EEwx9n4ZoBh815Co14Jx88b3bquxy_vskOCDi-OFYKNGwnEGRe2qvfkSyMlSuLXfUQhA7IvSRAUV1RZq72kSpA6ssBPplkGNH5i38J828Z95Gs7fy1thA1NR1NyfumfBFKuCBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلية الإعلام الأمني في العراق: الحكومة ماضية في حصر السلاح بيد الدولة دون رجعة</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87195" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mM293fKBZNMTuFHl7jvwtDvLD0O99rsn69akt5MskREkDppCzNW3BbYhFZsqliMYDxKanW9WvW7OWyAirkWhwUGMGbtZLiis2XJ6CidV0UU8yok_Xt3-nn4c8gbV0un3ZbHsQlflu7vaAtCMi7GUwA5gZ5jURTgh9GRxpXUFu6cpCsbw2BYNZbBbr0MmTfX2HvEDvipLOQwV5AmJIHHZbC5Na1kw4hmXDLJhKRbljZj1bFj_wUnFF9-E0oJXlZisf9DDr_o-tIYFHgm7ShgO2QFzzV-uchu3a-mIom3n9HwUua9IPYucloW4xC6XxaaPTktLdCBkuaKd2mmaAe_vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzBsdT8fqSEcs6RQYavbv6llv8m1TnuQe14p_dqHreb79toXINgQZTdiebdBkA_mc14dBj4zG1Ov4N-UitsYN9Q7MhASpkIulOgT2iEaeMkWnz3k4Tmo9TX7lmwk77E_fyqK4c1jtfMigCSfVxbbfEIgdKwYH0F9rgTsaVRcQ6kOYai_0IquvLjQkWao8nx6R70IZCkIL-GMrYV44ETdbLyzo-daRfE87hS6wzqUrxeRxGTcJWkK-BKT1C2utJDswTNLk_79LjF63DcdrCTpOMQAy1W-ELrUP2O-D-ZfurbYPkNyWeaaD2ymGHh0GX3IKLI8v1_kiuRFvTcLA9XGpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الانفجارات في صنعاء نتيجة إطلاق صواريخ أنصار الله باتجاه مواقع المرتزقة السعوديين في مأرب</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87193" target="_blank">📅 12:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/87192" target="_blank">📅 12:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blz0ctEkzDxSl88eh2t5EYOl-9PZ_j1KkoAJsUqrYqQER9LFEa6lEKsQ6aIFRlyWKC78eZc183VU4H-F1UfvOhlgdcfVeDlJEOLt-5aFZlnbn55dAhr9yVPHsqpnwPYIAr33Hilx2F1OsX7hN-2OKKFfmZrdiym1YAVVBOl952v3SdtPezYWOdgDUILZbeWUes6gMfHX9zH3RuRES5JxS_qSstzRz9DsTo1LAjaQB9QCfzR9hJZOCB3z7tVFBUtTWq5Me2yHbZs5xSfDxJIFGpFROQSnlQRvag5wnBN-mUn0MMuIZ2jW2f-V_KAW37NaGVoRr5E6vvmkMyp5FrfDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد خيار ستراتيجي ، والرد هو نتيجة
الحرب المفروضة
على الشعب العراق من قبل ال سعود  وعلى الجميع ان يعلم ان زمن الصبر و قواعد الاشتباك انتهت منذ رمضان ..
المقاومة لا تعمل بنظام الدكة العشائرية ولا على ردود الأفعال والمشاعر ؛ نتفهم جيدا غضبكم يا ابناء الرافدين فالعراق بريء بشهادة الحكومة العراقية من اي استهداف على السعودية وان ال سعود الذين عجزوا الرد على ايران راحوا يفرغون هرموناتهم المضطربة على ابناء الشعب العراقي … ومن حق الشعب والحكومة العراقية وفصائل المقاومة ان تدافع عن ابناؤها حسب قرار ٥١ من ميثاق الأمم المتحدة . لا يهمكم نعيق مغردي حوالات الرياض</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87191" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKR8Ss-OLGnyttvJeiqUBJ-lk59QZkUZ-AcU_s3R-oRsg7J8pYlaK0Y5G-tzN6kq8d8afQp_Y5Ohovo3wosWOw8kO0oadiFVTfMMYRVO0Xi9zEPwrVXVEkzmZGMIRdV9O5N4BjBFTVXw_Ua9CfkT5Bv3qISupdSHS64ysyvKNg4q8ouICikSC-GhBI_2_X5Z8StdomnJrPGQTuC0OQqXZgpYjBsQFnwkYMN2Q6YUON51mN2cTWIw9iYUYrfVw2S2kAIgWGrxXKmNzv62FnJ4fEJwsw13D_1EpI5wbfCZpDpv2HkojAh7DqcpfkI4HXAXUXTJNnHSyc4oF04LEXoyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNPLscoQ_RCPGABE7lNypjEZ5Gu9I5qIRFZPPbTwdFwSNpa0kjG6Xn_AaMoNyJzYY852YEhc5lXnox6hfphRT-DFEusyarxsxqg1YxZJcLPBGoD8NkiUu3dS2giZkmXlXtd6OfPgBHe-Hacess1xOWm6Peif0sAtl6Av8DgWntRuEILEpBUB8CXKcg-mjoS7eRLb62XAo10awUzubSSObtwDfhw9gAj32Tc8XI7HsDu-SNMBip7gKww1vfxhu-S7q_XVVbaeDzYE6f1CJz_kb3zKRB1p0mq1HVh6hU2c55ZQHGRRdobgRtmkv8i3br55JNKZy29KzVfTFCKM633ghA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87189" target="_blank">📅 12:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/87188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87188" target="_blank">📅 12:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87187" target="_blank">📅 11:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9K6PUCldtAWPM9raSBPCbU6EjogNRt-BHlKj-7O4I-5Sb4JPh0ZmexVpi5kHT14nHGoEkOpktuXf_wGULSBSIDdiGyM1dZQk6iEszopM4GjRrBbznGBqYJ7lT83OhyIJLY31DBt8QSXeA6kYOZiVkdpVLychwJM9cCGy-Rb1RN0m8GopkbfXTxRgd6pWW4ZOfDk5Bf3jQuenPMbjDoKk7zbu6aqtJgkKKrlS1nnOVuAuk_VRBbay39COCFloZtEnb95gDMYx4IZC89WenBFa8PjgU_kM2n6Jnk2m6FGwtkkVoFD-QK8_xrXIs5rQXkkiov-2fUG8waG8pEyZL_uEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات جديدة تهز معسكر صحن الجن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87186" target="_blank">📅 11:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87185" target="_blank">📅 11:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVI44UVhzNVk-0LjFZIbL2GDtwDfWXUhDDHRssohs-dhkL4h4vfsECazn8-P4PN6iyeW3ddCQgAhvzrxypxK5fEKGx5O3s1PPzdh0kr2pmrnyPoAeV9hsVUV5BbVshQXVWXvkXLsOMHmCCRyROg-wXCNjFrmUYl1C9ZqE3FMgI1dxUknZgBwr3GT-BUKFzuxNl_tXBQUkJKCIm3kBdoSWre7ZYyk4TaVbIa5d-rpuNoj0q0pjX_rjlTpCzQTqYmBUa14Bfv5rZvItehkMYi0XC21hPI7pSEw0KUADbNR3tcAlyBsxXskvaQzs_FzL5c_LhFWlChXw89duDKCwZ42sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو حركة أنصار الله حزام الأسد: من يُدِن عملياتنا فليفتح بلاده وأراضيه لإقامة معسكرات سعودية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87184" target="_blank">📅 11:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
🇺🇸
إعلام عبري عن مصدر صهيوني: واشنطن أرسلت رسالة لـ"إسرائيل" تؤكد عدم وجود خرق من حزب الله جنوب لبنان، وطالبت بتجنب أي رد عسكري عقب مقتل الجنديين.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87183" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87182" target="_blank">📅 10:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmQaa8cnSJ6NaLnV2TVz8uj4IDMboqeUQgCjja_7l36XJq_tJgcOP_EY3_PlvENOlHqo5LZjJBQLFCSgM7lCVglvd4dI4rKQp9uB_oMgctJy_EQnaMKfQxsDSyRy8W29oraDtkPE3chZbbHWyP6JdYohF_4nQAl5NhU_RlrwmDdj-DIPkXxEAYt23oLXoWvS72eVLUQS000nsawLM5dY0hdudP1_ag8-LIbhOZVPMaw5cAA_kfkyQJR17tBZeoq4EScz4xAR15QXfG7Qh890zUFBp2PBq0npuOk5dfEyETkHPlYTT2gQFO9GdPckrzJ3t2x2OwiG9vpGFYhpP0mlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87181" target="_blank">📅 10:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بورصة لندن: أسعار الغاز الأوروبية واصلت ارتفاعها بنسبة 3% لتصل إلى 686 دولارا لكل ألف متر مكعب.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87180" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شركة كيبلر لتتبع السفن: 6 ناقلات نفط غادرت مضيق هرمز و21 سفينة دخلت المضيق هذا الأسبوع</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87179" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVtd6tmFNvWYpKvlgKj2K_AyFW_2UFGwvJedeR3IuRamVLFjdwwJm8zGQ9W4_Hjtlkm_1Knt0NQ8sLAfkP74yi5n0liI06VS9LbRUCfr3LL7axgsrWlDVT-HIug2jvyD4cd23rs63QqpmsKzLN3Lof566DWh3wl5bQKwjsDTBurMV1COlGGrT5p_CgFtiAyEGdaMyMJDiODMPDqFleAuAuHtouQMsuZHKfM4dzGVlj-HfAU8LWRNV8lLZt-OCEZqfi1YUUZfjv0-RbK-rLi7FzEEKRvG9npIX8ac10wgLaiVZ77VphvPliroGgNEAOr-CtjTGy-FWnbyCfZX-HEbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/87178" target="_blank">📅 09:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
حادثة إطلاق نار داخل مدرسة في بانغ كرواي بتايلاند مقتل وإصابة أكثر من 20 شخص.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/87177" target="_blank">📅 07:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المروحيات تحلق بكثافة أيضاً في سماء محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/87176" target="_blank">📅 06:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من تحليق الطيران المروحي في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/87174" target="_blank">📅 06:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjO9ZhgLf5bm8r0C8ZMk_fNf-vO8VzTdFcGeXroZpUtJuoI65V_tINZoXKcJluCXhtJUuOcgNc9WFRs4pk0_4Ra3Hnr6H-gA8VPmZoQr4kxWX_OvLwLseLMnP5QA3l7Ao0Y0xjcFeCc_VzFAmbnfOUKulWa98tBwtEPlr1_BrqdW7HVNazMbHNDmo2b56X--PUJY5NhpuTzqesVWhXdcsgLEN0yipd6YlCM-RnaGsf2RmsDK0c_6hSTKKOFF5gKQNGboBOWT5LfdhbSv3YAlA_UmBXBXpJrvWO5kPur0NhPO3qgpLaEr1KoeCIUG9OLLowWswXPywvuYZOe25nBYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/87173" target="_blank">📅 05:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/87172" target="_blank">📅 05:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/87171" target="_blank">📅 05:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/87170" target="_blank">📅 05:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/naya_foriraq/87169" target="_blank">📅 04:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=QRL_rTc1PdIgnHUqzq2bQ5FA3-0ETw8yrOV74B8xRyO4IisJbsdpWKd_85tgDhbavZXcYDbubfOKTQQs5QQBXS0F3XA-V_VbxQcbn4b09SrzD8kRyg3jU6ZRfe-OuWVPcBdhdRhcWtxAjTJ-fVBsluJcgfZevTajfBdhm2sWvu9LgIe4R3iCNacwbVXmO1KweGg1kB2QJuYycbNXVoCN0zHlAo-oVX4CMFkr_civUim_tTRWLUFI2UQWmSV8evyKsAMO_lfuP532RO66w5VlZUHZSH06ueNQogfNBqTl_RDJL9haoVXrG3igMVvTs7Fbv4aa6afP4vGKMpdO8z2grBUkFa-93RDTxi7ws1jfEVxSyUaIm2FwmOh5MnVZFeEOcLO6VBgGqFFb_5Qr0ITZ4npCvuzhQiLcGsNxj-MB_K-w5HNMezLJBz-_0vmbgol_g9IPgS07kxWMRZzPrjqcvmFZw5k39AL0YMTHI4pq0scwYeQdSdr0NhInyK1XY_MgQcy4Sz7WnEz-5mz6Hd9PN5uUueOphV_fcjY8i5rllS5j1Hg2VoB1_cYYgy16-Tm52tWE7HpMH_IpradLWvpaMgGGNNkODzvbcY66A85Zz-By6bTmj5EC10SnYMmb2ODpG2TwLxr-XjYCSmnpVj4tIotTcsaIwxO4FCwHUetpHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=QRL_rTc1PdIgnHUqzq2bQ5FA3-0ETw8yrOV74B8xRyO4IisJbsdpWKd_85tgDhbavZXcYDbubfOKTQQs5QQBXS0F3XA-V_VbxQcbn4b09SrzD8kRyg3jU6ZRfe-OuWVPcBdhdRhcWtxAjTJ-fVBsluJcgfZevTajfBdhm2sWvu9LgIe4R3iCNacwbVXmO1KweGg1kB2QJuYycbNXVoCN0zHlAo-oVX4CMFkr_civUim_tTRWLUFI2UQWmSV8evyKsAMO_lfuP532RO66w5VlZUHZSH06ueNQogfNBqTl_RDJL9haoVXrG3igMVvTs7Fbv4aa6afP4vGKMpdO8z2grBUkFa-93RDTxi7ws1jfEVxSyUaIm2FwmOh5MnVZFeEOcLO6VBgGqFFb_5Qr0ITZ4npCvuzhQiLcGsNxj-MB_K-w5HNMezLJBz-_0vmbgol_g9IPgS07kxWMRZzPrjqcvmFZw5k39AL0YMTHI4pq0scwYeQdSdr0NhInyK1XY_MgQcy4Sz7WnEz-5mz6Hd9PN5uUueOphV_fcjY8i5rllS5j1Hg2VoB1_cYYgy16-Tm52tWE7HpMH_IpradLWvpaMgGGNNkODzvbcY66A85Zz-By6bTmj5EC10SnYMmb2ODpG2TwLxr-XjYCSmnpVj4tIotTcsaIwxO4FCwHUetpHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير يحلق بإستمرار في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/naya_foriraq/87168" target="_blank">📅 03:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJZnyB2iQIJNBNyZIhUTP_-txyt-vdqeETq7IC2US2HYn5QlbvEu7AWl-5N74wK_qBoSnYXTiAXd24MM3k4mG7HU3atDjikptPBNrBHrAwEQoGwaWPiflzM_VvR-EfaTN9okGq6WnKgFW-I81FuSorKJC8_eHLS-Ff9bgpMHpcW52Y1mz6Ldm8vPt7Ga4P_7WjJ-ko_P8cIuB9vSvLLhoizmwQhZeLcHgAkPdC7Sw7gG0R3Og_waTzhXhJ9TAUBCUm7YVYxxWkz9ReB4AwuzHyeWYftdrbJBZqCvtiWJUWfDIqWYPJqy9iLI29aS-iQwvLWMR28fareffyqSZF7NHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إغلاق مطارات أبها الدولي والملك عبدالله بمدينة جازان ومطار نجران الدولي في السعودية وخلو أجوائها من الطيران المدني.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/naya_foriraq/87167" target="_blank">📅 02:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
عصابات السعودية في اليمن:
مقتل 17 جنديا وضابطا وإصابة آخرين في هجوم المليشيات الحوثية بصواريخ باليستية ومسيرات انتحارية.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/naya_foriraq/87166" target="_blank">📅 02:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
ترامب اشتكى سرا في الأيام الأخيرة من أن الكشف عن انخفاض مخزون الذخائر الأميركية يجعل واشنطن تبدو ضعيفة.
ترامب كان على دراية تامة بأي مشاكل محتملة تتعلق بالذخيرة منذ أشهر ولم تكن التقارير مفاجئة له.
ترامب كلف وزارة العدل بالعثور على ما وصفه بالأفراد "الخونة" داخل الإدارة الذين يكشفون المعلومات.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/naya_foriraq/87165" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW0pKP8Q5lpxGBYxnbI0COjDu27GgDZfql6-ifDVy-xnqQHGEBc_GPNPiYzLf9lXq5iwelebNPIWx7uo87ahi7LPzxvcEJYp6-pNKRDy5nhpfG_L3OygL5rEVHx1vPbbd1D5CmQ0jgBKAp8ZP2P5tJZ5P4Mzz_IdIpypdXgH-a8nYGVx8Hk5Gk18PSYtT7kWANzo_Sy41H2ws2I8VabQVvXsSZw2Km73j7eszVgaqTSIsAckQRAHivI_tTJMr3ZA6rAEyKRTxCUHaK24KVseqqIpo2NytJQ0XNKag5XaE-MbxFcilZAzaLfEPzbJFOhwUdubbkqaYsNqIL554IXzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/naya_foriraq/87164" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/naya_foriraq/87163" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
مصدر يمني لنايا: مقتل عدد من الضباط السعوديين واصابة اخرين في المعسكرات التي استهدفها انصار الله.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/naya_foriraq/87162" target="_blank">📅 00:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8949db271c.mp4?token=e5fYMz3UlcoFIdIWkS9ppHSVXEejejWYY-YON4NqXB5JdOAW8TcUH_WgrEIQkVgIRQ7qi3eXP8I61Akw1IQf6TQVZrMSQFACNK71mDUns3O1W_515xAw2xy1TUQQkerhXqi1_aWOm8o4Nt9uwxShpogQsPaJe3VRx-VT-z8MJvQ698jk0xveWfwGhWbfjOk7_1pxEXyY-TG7dFgDztsKrGRFSrO7uOELMRdRzqxee0DuvuE4DeOVMwPx8RjFJk55bvgoOwNMSfhhPWNb6krUDEzsRE0g7MUywiKg3o-eC3EG1o8odSRn7T8Wo3yj-ZPDWnfbbQuCDHQ05iWlTBsNwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8949db271c.mp4?token=e5fYMz3UlcoFIdIWkS9ppHSVXEejejWYY-YON4NqXB5JdOAW8TcUH_WgrEIQkVgIRQ7qi3eXP8I61Akw1IQf6TQVZrMSQFACNK71mDUns3O1W_515xAw2xy1TUQQkerhXqi1_aWOm8o4Nt9uwxShpogQsPaJe3VRx-VT-z8MJvQ698jk0xveWfwGhWbfjOk7_1pxEXyY-TG7dFgDztsKrGRFSrO7uOELMRdRzqxee0DuvuE4DeOVMwPx8RjFJk55bvgoOwNMSfhhPWNb6krUDEzsRE0g7MUywiKg3o-eC3EG1o8odSRn7T8Wo3yj-ZPDWnfbbQuCDHQ05iWlTBsNwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: لقد نشرتم ليلة أمس أن الولايات المتحدة تمتلك مخزوناً هائلاً من الذخائر، ونفيتم وجود أي نقص. هناك طلب إضافي بقيمة 21 مليار دولار لإعادة التموين، فلماذا هذا ضروري؟  ‏ترامب: لأننا نحتاج إلى المزيد باستمرار. لقد قدمنا ​​دعماً هائلاً لأوكرانيا. هذا ما قاله…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/naya_foriraq/87161" target="_blank">📅 00:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=MUt2unMtMj-jYdVtGW2Jfa7RogBeBDQMs8c7vIBNuYfAPwlzl996OGA63dBaEeQfyfKvnZDYnuE9QqI0M0ivyDimzdMp_l4zei4fyF6XJnxt2DQVs0Pm9p56nhAMmAvY0NuTKyVo2eaAZTy5EJCTcp2CMisWwcgSdqnzmjd159VPGR2kaVoGu7-u5JJb9baTWbLDIdl_XewMB1B9NUj-782kG4NOyzs8q9uCBq5tYWSIeWN0jJFDZd_bYcn1dwQX2_GWnC-Ojk3Fl6p3I8K2kFHvJRYHL7VCk5X1doYsRevXjCOojEqq4T15nVzK25CF8BrZ-89WUEzpZHXaaLo-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=MUt2unMtMj-jYdVtGW2Jfa7RogBeBDQMs8c7vIBNuYfAPwlzl996OGA63dBaEeQfyfKvnZDYnuE9QqI0M0ivyDimzdMp_l4zei4fyF6XJnxt2DQVs0Pm9p56nhAMmAvY0NuTKyVo2eaAZTy5EJCTcp2CMisWwcgSdqnzmjd159VPGR2kaVoGu7-u5JJb9baTWbLDIdl_XewMB1B9NUj-782kG4NOyzs8q9uCBq5tYWSIeWN0jJFDZd_bYcn1dwQX2_GWnC-Ojk3Fl6p3I8K2kFHvJRYHL7VCk5X1doYsRevXjCOojEqq4T15nVzK25CF8BrZ-89WUEzpZHXaaLo-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:  يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.  ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث -…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/naya_foriraq/87160" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=h0EzZLuv8Y8f9dSVfL1r7OfYezepRYcoL4rBPttBO1DfZ-wtIqgGfP8ePZ8MfNQ-s5MS_p1Q8xVH6H10aXa53VPNw6WU5o2o3Pk2shWwjCRxmkJV7rJOq4UefX3DafH-LSABw8Lt9p04wCmRbaT6mPaXCy2QFfPyUdMywG7ssU9N2I_5YoelvNgLmNSvNJEbGoj4eCVZcr8uhJ5nMkzvaLOa36T7yrOZLXIl5bsyw3-gjSPn3o6--Rqke2fYsg12va9Xvo1l2KTdyW7wNR3AUKNxLAG-XxJljPMtgJ9jOQlQ1cmsD8B1hKPsFnhnk8q83bvjdiWyM50Ar64YyDur7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=h0EzZLuv8Y8f9dSVfL1r7OfYezepRYcoL4rBPttBO1DfZ-wtIqgGfP8ePZ8MfNQ-s5MS_p1Q8xVH6H10aXa53VPNw6WU5o2o3Pk2shWwjCRxmkJV7rJOq4UefX3DafH-LSABw8Lt9p04wCmRbaT6mPaXCy2QFfPyUdMywG7ssU9N2I_5YoelvNgLmNSvNJEbGoj4eCVZcr8uhJ5nMkzvaLOa36T7yrOZLXIl5bsyw3-gjSPn3o6--Rqke2fYsg12va9Xvo1l2KTdyW7wNR3AUKNxLAG-XxJljPMtgJ9jOQlQ1cmsD8B1hKPsFnhnk8q83bvjdiWyM50Ar64YyDur7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اطفأء ابار النفط الكويتية علئ الحدود العراقية تحسبا لاحتمال هجوم قادم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/87159" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامب بشأن إيران: أعتقد أن الحرب ستنتهي قريبا جدا.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/87158" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/naya_foriraq/87157" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/87156" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قنوات العربية ؛ الحدث حاليا</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/naya_foriraq/87155" target="_blank">📅 23:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3DeVa-Uk-FEhfhUs7__cULfgr0nsJAINKzLfig86v6BiDM2So3WtBtZ2agbbx0vX2sDRrQ2iiswKFNnOTkU0ulN3vRyQYbmgOsE-rGdgYXFDp6D3OFR1S-meJ-13p_CL0CNPngY7M3SvOwfD0wON0SYPMy9TIC2cClrFKw9okqDtSu7BfoGvlHhkJz6B3PYgT38rWWqZCdCmXujEzizxdMmsQsGBuI9AeVE6uyY9jiRJhdjyvLe8DtM8-y8T7T2DL9Emnm9THM4akGwWfMkIlNHtzCuQArdDr8GQszPSYav-9O6LIjl4Qe_oIdN9iv_UJz-EFWzGTEVlw7CMdHQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إلى أعزائي، أعضاء مجلس الشيوخ الجمهوريين، أصدقائي "جميعًا"، يرجى العلم أن المرشح الشيوعي الديمقراطي لمجلس الشيوخ من ولاية ميشيغان، عبد الرحمن محمد السيد، يروج، ربما باعتباره أهم نقطة لديه، إلى إلغاء نظام "الاعتراض" (Filibuster).
لقد شاهدت ذلك بالأمس، وهو يتحدث بحماس شديد عن هذا الموضوع.
إذا نجح، سيكسب الديمقراطيون 4 مقاعد في مجلس الشيوخ، و8 مقاعد في الكونجرس، والعديد من الأصوات الانتخابية والشعبية، وسيكون لديهم محكمة عليا تضم 23 قاضيًا، وسأكون، ويا للأسف، على الرغم من العمل الرائع الذي نقوم به، آخر رئيس جمهوري.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/87154" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK85-Fjol-1GNypF-w6sQJsbgXU-Az9bfADfJIQAEZeOodTm9hat8u3JsZpwr5k7F84KSUzYLvoHJb5JGZKGjh556fIAP0H38LgHJtk2200eKQz5vV7TDza2fwpjYZdyOSWlDn4NsUHzqv99UK1PxXjjQPhajMqnZrESdm7XN2bD_-KYVjayBvePgX8zPoLPRaJeCAAtYxr_Kgcko2YRY6RCeHnC7VtCStX7tDbrJTjkmjxIVHO5zUyXxyuM8HK_k-a1dKmCYlj2OVSkI7WaXvPhWoAA7ulOJmV9Rsu-LhKtiASciZ-h_LGmaLe2wbozPLebBYDLyqYjkHEO_iPJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
من جديد تعاود اسعار النفط العالمية بالارتفاع مع استمرار غلق مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/87153" target="_blank">📅 23:27 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
