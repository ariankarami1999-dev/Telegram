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
<img src="https://cdn4.telesco.pe/file/MS3n1NHI-GyQR_WsTYIofikPRDEjahVNQL48pqvUZnZu25x7c7c__fzAPm9TNRLclQoyvHaejbTjMd_ZNfm8g4xnf3iiR-eckZm33Ig5rYZP0L2UVjw4BWBhNxUWD5vD135BpIfk5v8pzYNU8EZkp6gjzn9tJ5azYHNN5C84DiiKGvfM_TEI_mBFYoSCx2JRpM5nOhtpZJv8Fh_yVBLolIVqq2-cAMbee7uVlY2QaFMyMjornQ3Z2jPGWJC8K8NZryaJ9TkxWOK55B_DTUrQ8acK9ruQxvAiY5XNfBx2YYYkIiLjvGP2u9cjH_vWwk5iTrtDfQsVZd0Da8Jul86J5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546ca50588.mp4?token=VJF-QAVG97JLSqGDaSK9BOTN5NhckxR-GTYgJaOn8TzVnMS-0HUh9V7yNs2_29jENvLt3AQDpj2u7rIvQcdhMce5NU62eio2c6q85DmbpjFZSJFRN1mOvihWM2qgaMzzy3qWe_iCoFwfBzcnH9XJFwHr6X4O8PAFipMm9EdB647SGh7L21_Zh5HbO8OSSai9Vqok-TLIPp9iAhKyhgbfrZWojqLf07kMYfNAT-0uMPsabdW-nmzHpYz5x34WVpcNlZMTnrsvJematEpWrilnrjq23gMhw2q8pz4mScEyLsPlaOAo8RJso0F-iYxXOJNziHMKVgiZ3sk_7XIciMbSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546ca50588.mp4?token=VJF-QAVG97JLSqGDaSK9BOTN5NhckxR-GTYgJaOn8TzVnMS-0HUh9V7yNs2_29jENvLt3AQDpj2u7rIvQcdhMce5NU62eio2c6q85DmbpjFZSJFRN1mOvihWM2qgaMzzy3qWe_iCoFwfBzcnH9XJFwHr6X4O8PAFipMm9EdB647SGh7L21_Zh5HbO8OSSai9Vqok-TLIPp9iAhKyhgbfrZWojqLf07kMYfNAT-0uMPsabdW-nmzHpYz5x34WVpcNlZMTnrsvJematEpWrilnrjq23gMhw2q8pz4mScEyLsPlaOAo8RJso0F-iYxXOJNziHMKVgiZ3sk_7XIciMbSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🌟
🏴‍☠️
دبابات وآليات الجيش الإسرائيلي تحترق في بلدة يحمر بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/naya_foriraq/76386" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: لقد ودعنا لغة "ينبغي" منذ 47 عاماً؛ لا يمكن لأي من الأطراف الغربية أن تتحدث بلغة "ينبغي" عند الحديث عن الجمهورية الإسلامية الإيرانية.  يجب أن نرى مصداقية رفع الحصار البحري أهو حقيقي أم مجرد تصريحات إعلامية.  نركز في هذه المرحلة على إنهاء…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/naya_foriraq/76385" target="_blank">📅 20:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: الاتفاق مع إيران سيتضمن وقفا لإطلاق النار في لبنان.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/76384" target="_blank">📅 20:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=qaqpS3dZ6HdpXfJLFWUSNQhK6f__tvaMdJD5GyOWbosfQKp2R6odB9LOPmZH7HuNypXpCnQju2-Kbb-OPgnjIVie2okhB_5qbxRwzoS03su2S8_RrJqGYhRKFNp8fOcaEmiAYV60Umst-tCPf66OCzIpP8ouqXvV2ia6ViUvEuhBS_d4aATqrABNsZBSd8mitCnuMiu8SqO5UzUynMijvTF4O3ZvzW99TMeYA-1AvjU0Yty9-QHW7vWAyhoamJCZ8Z1NE2SXo6COCyP6CUaEaIN3YwdT7Yh4kU_HREHSOsJ6WHfeLTHt2OyfSPY6IcTwQ5Jvh3CcrQCWwNydAOhd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=qaqpS3dZ6HdpXfJLFWUSNQhK6f__tvaMdJD5GyOWbosfQKp2R6odB9LOPmZH7HuNypXpCnQju2-Kbb-OPgnjIVie2okhB_5qbxRwzoS03su2S8_RrJqGYhRKFNp8fOcaEmiAYV60Umst-tCPf66OCzIpP8ouqXvV2ia6ViUvEuhBS_d4aATqrABNsZBSd8mitCnuMiu8SqO5UzUynMijvTF4O3ZvzW99TMeYA-1AvjU0Yty9-QHW7vWAyhoamJCZ8Z1NE2SXo6COCyP6CUaEaIN3YwdT7Yh4kU_HREHSOsJ6WHfeLTHt2OyfSPY6IcTwQ5Jvh3CcrQCWwNydAOhd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا في بلدتي يحمر الشقيف وتبّين بجنوب لبنان بواسطة صواريخ موجه من قبل حزب الله.</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/76383" target="_blank">📅 20:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyhOHTuetpymWodLWwe-S1833nL-DMesgzuGtL0TPnAqDE1bpTIBgEZiFnShWmgt8QhGqJLyrCdvC6XjJzo_OpxBAkGbka67kRLxQNEhiEt1rAZQ-7I4L_z1zBNEhhgNRbLrqfx6d9J_bPZ_74aTx-iEPhHoteCiDjltOJw-XrvpO_YPCd1GeMh37n7am2aMK6ICVGpr0ufaKq4TIhrUDvfKLIZWCFd2MsU6_cgyiBBqT2pXXijpv24mF1avFZuW323LU_49-IlJ-lNrR6kwTpuPK-1KrMjr-Nc5cNTqwrb55_8bjTX9sNganAlkgXO7F4OGtbI_aJpGBAyiHV8UeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
بين مايتحدث ترامب عن الحصار الفولاذي..
تانكر تركرز:
شهدت الأيام الأخيرة قيام ناقلات النفط بتحميل النفط الخام ومختلف المنتجات المكررة على طول الساحل الإيراني وفي المنشآت البحرية. واليوم (29) مايو /أيار (2026) ، نشهد تحميل ناقلة نفط عملاقة (VLCC) مليوني برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/naya_foriraq/76382" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76381">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: حتى هذه اللحظة، لم يتم التوصل إلى تفاهم نهائي بين إيران والولايات المتحدة.  ينبغي النظر إلى تصريحات دونالد ترامب، رئيس الحكومة الأمريكية الإرهابية، بشأن رفع الحصار البحري عن إيران بعين الشك، وبالطبع، إذا تم تنفيذ ذلك فعلياً، فلن يعني ذلك…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/76381" target="_blank">📅 19:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76380">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/76380" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن تصريحات ترامب غير صحيحة.  يُعدّ أهمّ بنود الاتفاق هو الدفع الفوريّ لـ 12 مليار دولار من الأصول الإيرانية المُجمّدة، ووقف إطلاق النار الكامل في لبنان، وهو ما لم يذكره ترامب. وبحسب نصّ الاتفاق، يجب دفع هذا المبلغ فورًا، ولن تدخل إيران…</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/76379" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇷🇺
بوتين:
الوضع في ساحة المعركة مع أوكرانيا يُشير إلى أن الحرب تقترب من نهايتها.</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/76378" target="_blank">📅 19:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=rrWoKxIsE0o-qJbCm-H9fZG6nMrfcG9yLeGR35YEUyo06HHU5qF-uQuZzythugWruZ3ZTTCnI4zy72XwbZ1FM2ikwqGFHWbVWu3w3VWJl6NABn5sARo_zk2nB4xjOxWqAHTtmFB5PsJkri27ohyKeIfTYv7ZHsxinDRJmVPRjrhSNwcluzjhA3G7qkdKNN7yoHlqHJdLZmqZhk7DK6rXZkLTuSfNbvLujfyIWrgbZCS50p4n5eChNG9ResR_LzXiMIZVCl5wrS3qeumzT_CELXHk1jW8HFGgSELF6YmfBm_7-JoDSDsDtAMJneatYSSu9Swd2pU5nNKQnt7ndHqYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=rrWoKxIsE0o-qJbCm-H9fZG6nMrfcG9yLeGR35YEUyo06HHU5qF-uQuZzythugWruZ3ZTTCnI4zy72XwbZ1FM2ikwqGFHWbVWu3w3VWJl6NABn5sARo_zk2nB4xjOxWqAHTtmFB5PsJkri27ohyKeIfTYv7ZHsxinDRJmVPRjrhSNwcluzjhA3G7qkdKNN7yoHlqHJdLZmqZhk7DK6rXZkLTuSfNbvLujfyIWrgbZCS50p4n5eChNG9ResR_LzXiMIZVCl5wrS3qeumzT_CELXHk1jW8HFGgSELF6YmfBm_7-JoDSDsDtAMJneatYSSu9Swd2pU5nNKQnt7ndHqYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
وسط غضب شعبي في محافظة ديرالزور.. مواطن سوري يهاجم موكب الجولاني.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/76377" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/76376" target="_blank">📅 19:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76375">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400a10f551.mp4?token=ThI3DxJtGnwJf6Il9TyqsLBfyD3Xa8Un1Xz8W84GSRIRi13O-hoFBkY5Q9ft1JLbAgVPKx26Gwp9jzctr_MX_TqY6M30Dvp8aEwkHHUdrKGsSMsH16x-UvzAHd7zfvMFkeQcgoGhSsujvwQ8OXLlVUrOUmMWSKVDlMKF13F1jBRN3sJZUnhZgiOy-58y_J3zJ9UbJ-4pzKOhmuaZGlZ65kwCIPY5FBR9vEukSFMyz69oNE2c1ARNEtFxQ6FR08AuLhrswQSDBqG0udBY-XHdOmt4MCiauIOvhq-AjA2Pw7k_Yt1TLC5D39aH6RKsHa-ZVIC_Qd-rnbbVi7b7CLeWzFxWqb8kaj7uJ-Iq7lW1bAcOOom3zravBefcnsibZ1HZDTkwv9sV3b9I1HHQhJOuuvfKrAcDPmd6TUKgS0aMjf-3RGkjne93G1sq2kdileK03VZ6QSzxg6Q62SCCY6DQq1lazLWcHNaTDj0zPou6hLrbVL2e0-3lTID03K3AtR-zZRXHAw1sSLqoazVP8ASsI_dn_vT7WZfGRMyWzWJGFQeKvCSw6SW3JDXQquGFTxTy6SM9ht7Ajp4ImwBgHbICMUUYg5icbbtgtPuouGGmuk0Y6ZeIZXwykxyZGgRpat64v4TRgZT42mdl8mcKKrZCHFboJkugsO8efPNeu6yVUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400a10f551.mp4?token=ThI3DxJtGnwJf6Il9TyqsLBfyD3Xa8Un1Xz8W84GSRIRi13O-hoFBkY5Q9ft1JLbAgVPKx26Gwp9jzctr_MX_TqY6M30Dvp8aEwkHHUdrKGsSMsH16x-UvzAHd7zfvMFkeQcgoGhSsujvwQ8OXLlVUrOUmMWSKVDlMKF13F1jBRN3sJZUnhZgiOy-58y_J3zJ9UbJ-4pzKOhmuaZGlZ65kwCIPY5FBR9vEukSFMyz69oNE2c1ARNEtFxQ6FR08AuLhrswQSDBqG0udBY-XHdOmt4MCiauIOvhq-AjA2Pw7k_Yt1TLC5D39aH6RKsHa-ZVIC_Qd-rnbbVi7b7CLeWzFxWqb8kaj7uJ-Iq7lW1bAcOOom3zravBefcnsibZ1HZDTkwv9sV3b9I1HHQhJOuuvfKrAcDPmd6TUKgS0aMjf-3RGkjne93G1sq2kdileK03VZ6QSzxg6Q62SCCY6DQq1lazLWcHNaTDj0zPou6hLrbVL2e0-3lTID03K3AtR-zZRXHAw1sSLqoazVP8ASsI_dn_vT7WZfGRMyWzWJGFQeKvCSw6SW3JDXQquGFTxTy6SM9ht7Ajp4ImwBgHbICMUUYg5icbbtgtPuouGGmuk0Y6ZeIZXwykxyZGgRpat64v4TRgZT42mdl8mcKKrZCHFboJkugsO8efPNeu6yVUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
24-05-2026
آلية هامر قيادية تابعة لجيش العدو الإسرائيلي في في موقع المنارة على الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/76375" target="_blank">📅 19:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/76374" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇾
مظاهرات ضد الجولاني أمام المبنى المتواجد به في محافظة دير الزور وسط تهديد المتظاهرين بالقتل.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76373" target="_blank">📅 18:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/76372" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ4JoywnVu1gcZZRecR6m_yXB72C-UCIlkRve7XvZbhtCGd3wxquqF7bQ3kVnVoXzSv9D3hJ3Vvgtjiw-lkiCndYAlOkHJHUkkwDYKUUV2JrNop8CBArkIajLIxsaZjjXI72b-EGXW-bwFOvQhz1DPRybFBswE1vbEfC54d497tRaA7AV6hvcmgqoujgEht4P0d40lNbfGzZlaG2LdtF1Rf2T2LTaUpktmF9-Dy5pwRgfRYIWVCv3ziDAFouO6Euj2s-5mZeriIU7XCRl5EWPU8A8EwVoWe9MZ9ruO1NDBLtdevW_N-I-vt4V5OF0glYK6FdTRZS4LLgHa6ooc0oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد من هذه الألغام باستخدام كاسحات الألغام تحت الماء المتطورة لدينا. ستُكمل إيران الإزالة الفورية و/أو تفجير أي ألغام متبقية، والتي لن تكون كثيرة!). يمكن للسفن العالقة في المضيق بسبب حصارنا البحري المذهل وغير المسبوق، والذي سيتم رفعه الآن، أن تبدأ عملية "العودة إلى الوطن!". سلّموا على زوجاتكم وأزواجكم وآبائكم وعائلاتكم منّي، رئيسكم المفضل! سيتم استخراج المواد المخصبة، والتي يُشار إليها أحيانًا باسم "الغبار النووي"، والمدفونة في أعماق الأرض مع الجبال المنهارة تقريبًا، نتيجة لهجوم قاذفات بي-2 القوي قبل 11 شهرًا، من قِبل الولايات المتحدة بالتعاون مع الجمهورية الإسلامية الإيرانية، بالإضافة إلى الوكالة الدولية للطاقة الذرية، وتدميرها. لن يتم تبادل أي أموال حتى إشعار آخر. وقد تم الاتفاق على بنود أخرى أقل أهمية بكثير. سأجتمع الآن في غرفة العمليات لاتخاذ القرار النهائي. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76371" target="_blank">📅 18:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a1115ab.mp4?token=TVrbIstfI_OluDehRKnOFtnCvw4Ca_fZcrtVvUTwIR472tBimA-LWI9G_9F8ad3TOWj7mA2NlUx25e8BQ8-IgnC4XDgbgF0xs2VlRjJ_bu9MxzQiFAjx2dGZgozJ5yaoqAI_mzjjHp-8G-OG76PhBbYn5q0NAahsYuSs1STQs6fcrYYBSbKcLTXy9I3-PNgVrCDGUkqojxd1WUM7K2oGe_qVE4OcwOT7nbgt_W__IfZDarQi2BKjAHm2j99Y_8Lwn6c4dXFL8FoMAZ6tZ4YqJV9GMblkyHIlQHsALPxtVV1sKNSN91DrMC7cmw5PTZajNOWJOSWl-5KnDfEtK15WzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a1115ab.mp4?token=TVrbIstfI_OluDehRKnOFtnCvw4Ca_fZcrtVvUTwIR472tBimA-LWI9G_9F8ad3TOWj7mA2NlUx25e8BQ8-IgnC4XDgbgF0xs2VlRjJ_bu9MxzQiFAjx2dGZgozJ5yaoqAI_mzjjHp-8G-OG76PhBbYn5q0NAahsYuSs1STQs6fcrYYBSbKcLTXy9I3-PNgVrCDGUkqojxd1WUM7K2oGe_qVE4OcwOT7nbgt_W__IfZDarQi2BKjAHm2j99Y_8Lwn6c4dXFL8FoMAZ6tZ4YqJV9GMblkyHIlQHsALPxtVV1sKNSN91DrMC7cmw5PTZajNOWJOSWl-5KnDfEtK15WzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظاهرات ضد الجولاني أمام المبنى المتواجد به في محافظة دير الزور وسط تهديد المتظاهرين بالقتل.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76370" target="_blank">📅 18:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpShLycoxWtv1NiHzgX2xXVK0PhDoEF8dAIUcbzRoclT4RDC9YaHho-9qZALOe5gI2bOs6d45BrYUy6t-o96WYwJU01164YRiBWUfdsO7ZL-CHQ-6IjQiA0g-3mX5wKPVDOeQGUCGiWYRLPdLUwdJS3uKYaQY4_GFQmyJu0OoLLOUzIUvzxCzdTeBEBqc5SnIUgReT0Wn3ajasaoBWp2RYeVAej1Oru04iuwKuE47ufLigLfntjkhVKS8nYte2FFWkCPjXP7EaC66LAwqGFUGE5GPCUSduyZpHag2lV7pHIEYxEWAZB0Zkk04ai_gmpAMOtCqVMh-ilFuj7272lwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحفي تركي يدافع عن تركيا المظلومة من تصريحات الجولانيين حول فيضان سد الفرات في سوريا ويرجح السبب للشيوخ الجاهلين لعلوم الحياة في سوريا الجديدة.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/76369" target="_blank">📅 18:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd29d4c9c5.mp4?token=E1gNnKuOGzQIBJRpa0F21JkW-9Pn5wUbZ1A-9qFgZ6EDPK_F93bd-jk_AtZJlaIeLdCgWx4hHzS2rpXgVcXrjS659wW-ZXR5CuphamhNEaB839ZsVklnfEt9mBVauURRTvgJC7W23-XluDz0z4unYUKZ_QnvGJ2KUT90YLwVC7N1l_iOkF2Hc-a4ZRnYwitHTtpBRizS41iHApBdFgahIKwwpCE2REgcM-Paceio1I15mDk4YVSeVTHLzgoD4jiR6hX90eC5bFFsnMHx_t6KzqIgIlufFK8w8iv0YManRZiVqG3K1rlFXhL1X8cy2oFkmrg_dj3-p5BgZybvzITrdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd29d4c9c5.mp4?token=E1gNnKuOGzQIBJRpa0F21JkW-9Pn5wUbZ1A-9qFgZ6EDPK_F93bd-jk_AtZJlaIeLdCgWx4hHzS2rpXgVcXrjS659wW-ZXR5CuphamhNEaB839ZsVklnfEt9mBVauURRTvgJC7W23-XluDz0z4unYUKZ_QnvGJ2KUT90YLwVC7N1l_iOkF2Hc-a4ZRnYwitHTtpBRizS41iHApBdFgahIKwwpCE2REgcM-Paceio1I15mDk4YVSeVTHLzgoD4jiR6hX90eC5bFFsnMHx_t6KzqIgIlufFK8w8iv0YManRZiVqG3K1rlFXhL1X8cy2oFkmrg_dj3-p5BgZybvzITrdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
لا ترسلوهم الى لبنان...
אל תשלחו אותם ללבנון...</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76368" target="_blank">📅 17:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPhvsOPfBmNX3AsaGLY13tMCqPINPEA4InUntBAotrsFOL_dT3pRRTSjBC9Kxb1qA38SIe0rxnBOXDJPUAY4JxRsv0dpvHy2vpFG_vW034kymJAtFvBoiRovxM89WZObdOlZLLLm-f_D8IWZFXUix8tKRAZpONb2wwLEIK3WzrC7KsmhO7GtMgnDIb0Mbds8klchqkMOTsVUygAXUSMVwiQNopsRaJaDzV26VV8T6F2nwaLUMNQQVH7zMJTUul9onLdpvSmseGPaUziOdRBWqNnEoETqZvL3gKuCZEYz_4tu00IPU4Bj0HwIrrjYrHQ06UPPi5Db1nNgjGRLv92gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
‏
وزير الخارجية الإيراني عراقجي:
ناقشنا هرمز وإدارتها المستقبلية مع عمان بما يتماشى مع مسؤولياتنا السيادية والقانون الدولي.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76367" target="_blank">📅 17:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfLvPNZDJvTyEhim-z_sEdhBFolLGLO8Awlmxkj_8bS3HV4o4aD5XiQ6QG7tBKhtuHQu13BgwNFmuRfINxxOGCH7DeGv61XZwS25SqRw3lXfMn_VIzdKPuLVf8194uA2vP3U4O2VlqoWt-LHK6kqBxLP0gmpiaNnyKrj-GluJStYpJrnIIOVt8i1e-ciWS0luiU_ccmzV60ZusW94N8Ogr9YfEJzaypV8AiUnFE5KNnPg0hxs6ErET2Uya5zeswaKMcr5sZKRx1XM0cPRvr6b_Jgt_uqHDAnFVmtjQu6HY3fETwrEqUPfaLLKtINT9Lgydo89kLbRDjuLYzFYM8LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76366" target="_blank">📅 17:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
طيران العدو الصهيوني يغير على بلدة البيسارية جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76365" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
‏
شركة شيفرون الاميركية:
لدينا 6 سفن في مضيق هرمز ولن ندفع رسوم عبور.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76364" target="_blank">📅 16:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7bX3r-zeU6L1gvZAcNSaaGQ5Q3-jRAEps3g9R4te08XVtEBgFYHaPb55DAP7xdVZjuOyfQzcyweRfGrerWVXmJ3KLydqdW6AzaOKpNGNEd4quA1Iphls9ql9-IM1nYpDnGh8fSKeB87WHjdZHVQvD0NXDtsa9Sh4fZRE4XflVKsBUc4TTLywkad0C5hXE-JvQYVNRrar_Z8AMTiFRYcoDmnQ5pjfIfzJsV_m6A0CV5bBUMh_UQlzxWYUtAci04LLgpzvx4cxK1GAb1prrobHquFw_T_JTvedkZHDhHqYNxVOllavuVMo4VnOSOuIu4q4I68-etCvIuAI5HRg1m4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دمیتري میدفيديف: التزموا الصمت. هذه مجرد البداية تستخدم الطائرات المسيرة الأوروبية، وقطع غيارها، وأسلحتها الأخرى، فضلاً عن المعلومات الاستخباراتية، في هجمات على روسيا يومياً. وتؤدي عملياتها إلى إلحاق أضرار بالمباني السكنية، ومقتل مدنيين.  جميع أنواع الحثالة،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76363" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL1ReQSaPBQJ3EJ2FCW7V6d7nEmif4qncf-tqGYfeoljV4m8IGIK0uz3FZhn86WF4oAxyGAOa0_RDIBzv7fRDtaoY9mssjmRbi4gscke1UTP5aBTQA9sG_WPuddSisZk74frgoRzSfA_13c-NoyrfVp9npRSAawuFUmuZ2wGUD1UMAPbsq-4E88uInnn0jnFzlrGQxqhMjABxSh4SIy0bMHXIs11YFDJ80aD6P71S2GEVo3x7UDCDOM9-tJ6wntfVwj6Hgzjqx8U853BySBbO79zgY5eK7rUxuHeDZUU6aOY6V03jSssiBu2kxZZfsRObhdTQDemOTDylQVknAlgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
جيل بايدن تعترف الآن أخيرًا بأنها لم تكن تعلم ما الخطأ الذي حدث مع "سليبي جو" خلال مناظرتنا الرئاسية المذهلة ذات التقييم المرتفع لعام 2024، حيث لم يكن جو يقدم أداءً على أعلى مستوى من معايير المناظرة.
قالت إنها كانت تعتقد أنه كان يعاني من "سكتة دماغية"، وأشياء أخرى سيئة حقًا، ومع ذلك لم تهرع أبدًا إلى المسرح لمساعدة زوجها المضطرب، كما ستفعل أي زوجة جيدة. والشيء الوحيد الذي فشلت في ذكره هو مدى أدائي القوي قبل انهياره شبه التام.
بمعنى آخر، كما سأل الكثيرون، هل تسبب أدائي القوي في تلك المناظرة في أنه "اختنق" ببساطة، مما أدى إلى هزيمته المخزية، أم أن هناك أسبابًا أخرى؟ لا أحد غيري يعرف الإجابة على ذلك، لكنني أعرف ذلك!!!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76362" target="_blank">📅 16:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkKgxPJhfWUnjAJQqrKKIskLIHSP3GorDwkhfFOUiNUIbitBEHm3h8pT7ayfESKOOJ0KITpzjFoL7G4GPYFyWi60b4njQvT14HUMfINyXQKdyVUL_2VPn421haGCw-4UtUHEcEvU4NaMDq0qCv0mdDmGjb6aMdzbX2PVm-635zMVWpKtz5S0XvKNrH9jsBa-YixQa4LRZGyA_WRmNVixzZiBX4dV_IZsVtwNzOmnBaSKHNLm90friLws222hMLrho3i3Xz97XX8dW4qgjifA_4lJITnGFVaR0-e5jBEf0wiTrDdfuyH5e1AlFERl8WXinCjM8U628dxwF3tKHR4s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
- لا نحصل على تنازلات من خلال الحوار، بل من خلال الصواريخ. في المفاوضات، نكتفي بشرحها.
2- لا نثق بالضمانات والأقوال، فالمعيار الوحيد هو السلوك. ولن نتخذ أي إجراء قبل أن يتخذ الطرف الآخر إجراءً.
- الفائز في أي اتفاق هو من يكون أكثر استعداداً للحرب في اليوم التالي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76361" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76360" target="_blank">📅 16:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇺
‏الخارجية الروسية: سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76359" target="_blank">📅 15:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇷🇺
‏
الخارجية الروسية:
سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76358" target="_blank">📅 15:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض طائرة مسيرة اميركية من قبل انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76356" target="_blank">📅 14:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مضحك
‏
زيلينسكي
: مستعدون لدعم رومانيا في مواجهة مسيّرات روسيا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76355" target="_blank">📅 14:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76354" target="_blank">📅 13:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🐦
نيويورك تايمز:
أحد أحدث العناصر الأكثر إثارة للدهشة في اتفاق مشروع السلام الإيراني هو صندوق استثمار مقترح لإيران - يبلغ حجمه حسب التقارير 300 مليار دولار أمريكي.
قامت إيران في الأصل بتصنيف ذلك على أنه تعويضات عن أضرار الحرب (التي تقدرها بـ 300 مليار إلى 1 تريليون دولار أمريكي). الجانب الأمريكي يعيد تسميته على أنه "صندوق استثمار" دولي سيساعد في تسهيله - وهو إطار أكثر ليونة يتجنب كلمة التعويضات.
يبدو أن الفكرة نشأت مع ستيف ويتكوف وجاريد كوشنر، اللذين اقترحا تعزيز مشاريع العقارات في طهران وآلية استثمار أوسع كحوافز للصفقة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76353" target="_blank">📅 13:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏الصحة العالمية: نتحقق من 223 حالة وفاة مرتبطة بإيبولا في الكونغو الديمقراطية
ارتفاع عدد الإصابات بـ"إيبولا" في الكونغو الديمقراطية لـ 906</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76352" target="_blank">📅 12:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز محافظة حمص السورية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76351" target="_blank">📅 12:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
وزارة الموارد المائية العراقية: جاهزون لاستيعاب الموجة المائية القادمة من سوريا ولا توجد أي مخاوف على السكان القاطنين على ضفاف نهر الفرات</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76350" target="_blank">📅 12:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDzuAQ93SkMUmn8i0Ze8qPoVRE4KC2ZEWs8YxYM10ULWEdqz3R2BCZNDbwvcU5l8LnKEZkbSa74QrV-J7-8FYdFJcNjhkxyqg5SAz5RfPmh1wYy3YjgVqagBqb-YvB_b_Lo8CvD5DJdvIsm7FvBXyELVhUoGwpLPw3u3s2NrWwtrlT-oBLESZrRAEFqAtefbKneNJNBjP_n0HJtFLizfbOw-ys3NIyLSSIn9cM35WtDlKCbzPuPzwU29hWj4P4jZenFrVJj0xK-OG-8Qkr1WwE187SWCKobbAvFlAlIjuJFgmPS1nw3WGCCY-O-BJURE_29r8b1k0591q6PD_PT4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية الآن فوق الجليل الأعلى دون تفعيل صفارات الإنذار</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76349" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 دبابتي ميركافا تابعتين لجيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76348" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏الأمين العام للناتو: خرق مسيّرة روسية أجواء رومانيا يؤكد أننا جميعا في خطر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76347" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">إعلام إيراني: حركة الملاحة البحرية في مضيق هرمز الآن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76346" target="_blank">📅 11:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حدث أمني يتعرض له جنود الاحتلال جنوب لبنان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76345" target="_blank">📅 10:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📰
سي إن إن: تراجع مخزونات الولايات المتحدة من النفط الخام والبنزين والديزل بسرعة مع استمرار الحرب مع إيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76344" target="_blank">📅 10:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ول ستريت جورنال:
مقتل
7 من أصل 11 جندياً إسرائيلياً سقطوا منذ بدء وقف إطلاق النار في أبريل بسبب مسيرات الـ FPV
مع كل رحلة بالمسيرات يكتسب مقاتلو حزب الله خبرات اكثر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76343" target="_blank">📅 08:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">في خبر غير مهم
🌟
وزارة الخارجية العراقية تدين قصف قواعد الاحتلال الاميركي في الكويت التي انطلقت منها الصواريخ لضرب ايران.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76342" target="_blank">📅 02:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
فانس
: نقترب من نقطة تسمح لنا بالجلوس وحسم القضايا العالقة مع إيران لكن الأمر يتطلب إحراز تقدم إضافي.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/76341" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/76340" target="_blank">📅 01:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
وزارة العدل الأمريكية:
توجيه 8 تهم للعراقي محمد باقر السعدي بسبب أنشطته مع كتائب حزب_الله والحرس الثوري، السعدي ضالع في 20 هجوما ومخططا ضد مصالح أمريكية وإسرائيلية بعضها على الأراضي الأمريكية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/76339" target="_blank">📅 00:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/76338" target="_blank">📅 00:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARNOklx14RfnVu_4Em2tbnUmYgEKVIHqDtfbkOpPEkmXftMWQuE7dac61ydcD6VMx6QfUjQrzNKDC6E_BPemei7MNXctYZxxQKZlKbBLaqeOmRbm0w6aO3pPp8OvuGO2R9LCjwUHdei18TD7nNIAjX651KINlbqjpLiusANzNyg09cVH7dRB_gTaj9y0qaAJo_XjMpRLE1IILP0Ikh19OiCNaKDxMJNiHFdhxCH8GkYJaCR59hDpf9Z4b6k-HfX6-uQZf1782adi5s7Hmhozs5il6BDLXaq8OFHqFPWTeQ_Ui5rMCqFxarICFwFhJTasNVuKpQq0qZYjPmtyqjipAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/76337" target="_blank">📅 00:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76336" target="_blank">📅 00:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKikjtojkkMl9Rf0mmlYXrUIOLFt5iJNIkXATcVF8ivw-yAJGTSOAXrY0aCfeAPmsSfJQMsx2JXRU-HjFwx4v30nXRamuWab3k4iOky87Qipx4AXLXOex_1z2Gao8IYdjyP8lI54cYyG2iOtkoZSYg23T8-WEdLuHquI-YquKfJR_Bh4IXjBE3YmAYPN3B_irZF17tEsmiNIjZnUlHDVADnycbxcEybG7Jef-AcNDEe5l9IZ2dzaIPkOMjMVwDyUii2Lb5YGjg7ptbyqRMbtSq2VHCwmxEMYYnqHH2CjLlzdVrYewDTL0jJ6WYelkFV5pU7oUi_lOaZNFnZV5KM1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇬🇧
رصد نايا
تمارس القوات الجوية البريطانية نشاط لوجستي في سماء العراق حيث تم رصد طائرة شحن عملاقة " A400 “ بالتزامن مع وجود طائرة إرضاع جوي اخرى تؤمن الوقود للطيران الحربي ؛ يذكر ان السفير البريطاني في بغداد قد صرح لقناة عراقية ان العراق يتمتع بالسيادة ولا يوجد هناك احتلال</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76335" target="_blank">📅 00:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
‏وكالة مهر: الدفاعات الجوية حاولت التصدي لطائرات معادية في بوشهر.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76334" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
وكالة مهر: القوات المسلحة الإيرانية أطلقت نيراناً تحذيرية باتجاه 4 سفن مخالفة قرب مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76333" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صواريخ كروز من طراز ابو مهدي المهندس باتجاه سفن أمريكية في هرمز</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76332" target="_blank">📅 23:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76331" target="_blank">📅 23:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76330" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76329" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 26-05-2026 أجهزة اتصالات تابعة لجيش العدو الإسرائيلي في موقع العاصي على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76328" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76327" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محرم 1 00_٠٦٤٢٥١</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/76326" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شبه لهم يا حسين
#شاركها</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76326" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وَاللهِ لاَ أُعْطِيكُمْ بِيَدِي إِعْطَاءَ الذَّلِيلِ، وَلاَ أُقِرُّ إِقْرَارَ الْعَبِيدِ
وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة (والذّلّة، وهيهات منّا الذّلّة؛ يأبى الله لنا ذلك ورسوله والمؤمنون، وحجورٌ طابت وطهرت، وأُنوفٌ حميّة، ونفوسٌ أبيّة، من أن نؤثر طاعة اللئام على مصارع الكرام ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76325" target="_blank">📅 22:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9IhF_6AwK5Zwesgo4FhVFwsKFbL1xhi_33LDhqHfYpfpxJR_Yg-L5IwFAl3BNVcTufGrbaTb88vAC8Tn0v0cE7MCG4-voVYQbQgBEFeNAeky4MmtEIT_In1feA8_JWucDTnq0TQJXW2ENwzzpxU_hjyUekfLNAGc4njECj4e5bfEtHgGZxFHX-2d-BlMX9UcpW1r-DiW-7zlxxZBHDeB1JdcJ7BaokC5PuadluoLG8iouWFSPgG2pyajG491ZCEiI81J6FKmoXWE2w7mq8Vh0swftfAyY7aZ-v9L2wu-VhRCGeEnOk08tR8-Co6DhLb7N7YE-SccGXHflRunPmhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم "سرايا أولياء الدم" أبو مهدي الجعفري: لا تسليم للسلاح ولا حديث عن الطمأنينة قبل أن يرفع الظلم وينتهي الاحتلال عن العراق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76324" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZzVAlX97Td40-ypgTFsJNS_PjasRP69jy7Gm15Mn1Ix_-t052u-W-NUzZqperxu4tG0Y8vzCDD-Nc8Y8Zh-uHhbJHB2zE6_M341FDP9jN7SEtlmGpq9Y5dKVvI_SXH1DcBeKMojKOReNBotttFeFdHqt5mdUwx50-lNvDTKf1duIUoYgMvOvnUJo7oR8KjvErjLreKV7olPiicP6yrDTgTELh2CvUo1s8E5yYZKIT1saN9fdSO3WAyBJtYhjeQDhZntTwaCms02IcgDKn2qL2lktyb2MbHtEcOxq-F4HdIKwfQ_zuJHymWhlBtU3xNotNJkk5CwZM1XdxCo3WX9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كلُّ عامٍ والوطنُ بخير، ما دام فيه حُرّاسٌ ودماءُ شهداء ورجالٌ مستعدّون للتضحية.
لا تسليمَ للسلاح، ولا حديثَ عن الطمأنينة، قبل أن يُرفع الظلم وينتهي الاحتلال عن العراق.
في الحرب ينادوننا أبناءَ الأطايب، وفي السِّلم يتناسون أسماءَ الذين حموا الأرض.
فالأوطان لا يحرسها العابرون، وللمقاومة رجالٌ أوفياء يحمون العراق في كل ِّ المحن.
#موقفنا_ثايت
#قرارنا_مقاومة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76323" target="_blank">📅 22:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026
منصتيّ قبّة حديديّة تابعتين لجيش العدو الإسرائيلي في ثكنة راميم (هونين) بمحلّقتي
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76322" target="_blank">📅 22:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله ردًا على مزاعم العدو الإسرائيلي الكاذبة حول سدّ القرعون:
يواصل العدو الإسرائيلي سياسة الأكاذيب والتضليل لتبرير اعتداءاته المستمرة على لبنان وجرائمه بحق المدنيين والأطفال والمسعفين والإعلاميين، في انتهاك صارخ لكل القوانين والأعراف الدولية. واليوم يخرج علينا بمزاعم كاذبة واتهامات سخيفة لتبرير اعتدائه الخطير في محيط سدّ القرعون، الذي يُعد من أهم المنشآت والبنى التحتية المائية الحيوية والاستراتيجية في لبنان، ويشكّل مصدرًا أساسيًا للمياه والريّ والطاقة الكهربائية لعشرات المناطق اللبنانية، بما يمس مباشرة بأمن اللبنانيين.
إن ادعاء العدو حرصه على البنى التحتية اللبنانية وخيرات لبنان المائية والزراعية والكهربائية، وخوفه على الاقتصاد اللبناني، لن ينطلي على أحد. وإن سعيه لتحميل المقاومة مسؤولية الأزمات التي تسبب بها الاحتلال نفسه وعدوانه المستمر بدعم أميركي مفتوح ومباشر، ومحاولة تصوير المقاومة كأنها تعمل ضد المصلحة الوطنية اللبنانية، يندرجان في سياق التحريض الداخلي وإثارة الفتنة وبث الانقسامات بين اللبنانيين.
إن العدو الإسرائيلي، الذي دمّر خلال حروبه واعتداءاته المتكررة على لبنان الجسور والطرقات ومحطات الكهرباء والمياه والمرافئ والمنازل والمنشآت المدنية، ولا يزال يمارس يوميًا اعتداءاته بحق اللبنانيين وسيادة لبنان ومقدراته الوطنية، لا يمكن أن يدّعي حرصه عليها أو أن يكون حاميًا لها، بل يبقى التهديد الحقيقي والدائم لأمن لبنان واستقراره وبناه التحتية واقتصاده.
وإننا إذ نحذر من أن تكون هذه الادعاءات والذرائع المفبركة تمهيدًا لاعتداء إسرائيلي جديد يستهدف سد القرعون أو محيطه، أو يستهدف المنشآت المدنية والحيوية في لبنان، فإننا نضع هذه التهديدات برسم المجتمع الدولي والمؤسسات الحقوقية والإنسانية، التي باتت مطالبة بكسر صمتها إزاء الاعتداءات الإسرائيلية المتكررة على لبنان وبناه التحتية.
كما ندعو الدولة اللبنانية، بكل مؤسساتها، إلى دق جرس الإنذار وعدم الاكتفاء بالمشاهدة، والتحرك الفوري على المستويات الدبلوماسية والقانونية والإعلامية كافة، وتقديم شكوى عاجلة إلى الجهات الدولية المختصة، بما يضع المجتمع الدولي أمام مسؤوليته في لجم هذا العدو عن عدوانه وإجرامه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76321" target="_blank">📅 21:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
مصدر إيراني مُقرّب من فريق التفاوض: خلافًا لما تزعمه بعض المصادر الغربية من أن نص ما يُسمى "مذكرة التفاهم" بين إيران والولايات المتحدة قد تم الانتهاء منه، وأنه ينتظر فقط إعلان الطرفين، فهذا غير صحيح، ولم يتم الانتهاء من صياغة النص بعد. لم تُعلن إيران بعدُ…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76320" target="_blank">📅 21:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTyTvMetv0c7O3MbvLP0jIktyOQJLBiFfEbifChOjzZdlkAxlHCEvotfmw0cxIAZwrP-pdDa36QuNp7zWQx55HmM7Hr4jmk7tc6GkQbGy0K0ppqhakGzK-4EP41gNIiUsvxpc3N3AOl-GQbdj6tYsVlh1yXiBXct0BR3NlxUhhti-iQLx0sTNh2zG6rXJdDz2IIClpwHqB5SefIjdVOBQxNaFk54u7-XB57yc_x40t3ZokFdfDZVlNA-ZGLKfyDQvNMegkpN8a_xyaGCV4ySLgi4LpwITKtEzon1WUKQ6D4zQA4faNkExIpzBxY_Hodgn7-226jjQalsfJpVhRMFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76319" target="_blank">📅 21:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
سي إن إن: ترامب يسعى للحصول على المشورة قبل الموافقة على الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76318" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/76317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرايا أولياء الدم بالميدان
#شاركها</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76317" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بيان هام بعد قليل لا ابو مهدي الجعفري الناطق العسكري لسرايا اولياء الدم … لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76316" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
ذي أتلانتيك:
بدأ ترامب الحرب لأسباب شخصية، وليس استراتيجية واضحة، وهو الآن في طريقه للخسارة لتلك الأسباب الشخصية نفسها، حيث خدع نفسه فقط.
الرئيس الذي كان دائمًا ما يصف أسلافه بـ "الأغبياء" ويصف نفسه بـ "الذكي" تجاهل أن كل شخص من كارتر وريغان إلى بايدن كان حكيمًا بما يكفي لعدم بدء حرب كبيرة مع إيران.
ترامب طالب بـ "الاستسلام غير المشروط" لإيران، لكنه يتفاوض الآن على صفقة تلبي طلبات طهران أكثر من طلبات واشنطن.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76315" target="_blank">📅 21:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR0woLxSJ99URNS6-_A1s6H6SvIZDGqCg_NgC6SUuPySret4GgzZ8L7_0Ew8s1x18WGP3yWEJQqXk0YsL1boRXj7KtWXK_z4BYLoZtNCHM9rcTF_MYKG6XwjI7zkF2kGZiYVwrO9CZLn34H3B7_UV6QSN-K7G1yRfejDnpepMgMDEovkMGsWDayTwqq7uICVHVcOi5jVuF_l6LRpZ_ZT23FkuQMc_rNEFmlSH9hQcT4kX1nilqfP8TCSRJ-cKleXZgfogxdCR_ghayeNO4IYUSQJVQtZvrYxjPdpaKLf8hMOsZaU8tl8u3a4tqirsrrzaW46sRY3W_E2UFu1vxVhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة بدر تخرج عن المألوف
🌟
المكتب السياسي لفيلق بدر ينشر عن تحديات التي تعرقل مضي العراق في مشروع التنمية بتفاصيل اكثر
اضغط هنا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76314" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
مصادر أمريكية: نؤكد توصل الولايات المتحدة وإيران إلى مذكرة تفاهم بشأن مضيق هرمز والمفاوضات النووية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76313" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
آليتين تابعتين لجيش العدو الإسرائيلي عند موقع رأس الناقورة البحري على الحدود اللبنانية الجنوبية بمحلّقتي أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76312" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظاهر نحو 30 رئيس بلدية إسرائيلي أمام مبنى الأمم المتحدة احتجاجًا على القرار المشين بإدراج "إسرائيل" على القائمة السوداء بتهمة العنف الجنسي إلى جانب حركة حماس. وأوضح وفد من مركز بيريز الأكاديمي أن "هذا قرار معادٍ للسامية، ومنفصل عن الواقع، وغير أخلاقي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76311" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76310" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76309" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76308" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن لا نسعى لامتلاك أسلحة نووية، ولا نمارس الدبلوماسية بالإذلال؛ إن الاضطرابات في المنطقة سببها
إسرائيل
.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76307" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=ZtX56tybGtLRO9zR5NVo5e9a_Al6FOJToSUOZcK3RJoqHV0L738gwReeSWB55ctQeiespGKBveObYVYqk7CBfUqPM0FQwnvM2cf6aQmstYR3HF3eRY1SbhVlIHBPRd5TJ2s47Y_uVUojKM17tyz3aIdv_x3EOabwD40Uayden4LP_0arqHYGjaLqs07iU4KTctY35SWcW3gShWUZfFYXedVYHXU0OEIY8QQFs6cnUee1vA15wYxARizc7rI1zZUZOIxlUTWhEAFsQpzA94e4OYafGi5NYrN76LUHkjUGlsVttFsYwqg-uzwbNr3uPeiwIDm9RDKVEs0JcixxiZQsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=ZtX56tybGtLRO9zR5NVo5e9a_Al6FOJToSUOZcK3RJoqHV0L738gwReeSWB55ctQeiespGKBveObYVYqk7CBfUqPM0FQwnvM2cf6aQmstYR3HF3eRY1SbhVlIHBPRd5TJ2s47Y_uVUojKM17tyz3aIdv_x3EOabwD40Uayden4LP_0arqHYGjaLqs07iU4KTctY35SWcW3gShWUZfFYXedVYHXU0OEIY8QQFs6cnUee1vA15wYxARizc7rI1zZUZOIxlUTWhEAFsQpzA94e4OYafGi5NYrN76LUHkjUGlsVttFsYwqg-uzwbNr3uPeiwIDm9RDKVEs0JcixxiZQsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إعلام العدو:
انقطاع التيار الكهربائي في المطلة بعد إطلاق صواريخ من قبل حزب الله.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76306" target="_blank">📅 20:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني: لن نوقع على أي تفاهم لا ينسجم مع مصالحنا وسنرد على أي انتهاك لوقف إطلاق النار.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76305" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
‏أكسيوس عن مسؤولين: اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76304" target="_blank">📅 19:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
خيمة تموضع لجنود جيش العدو الإسرائيلي في موقع حدب البستان على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76303" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=uiOoRSwSWKyIU4XUeozD64xNbrUnpByRBWua7mD_XmfCELybKe-BDqlcvZ1u0JKzRgq4cefYY4sgZK3gA3CnnoXbHkLYpNxZkDWewXiz7naFhg1UC2AwPN-ij7JNdvGfRqG9SEzMEOy8GU8lga0kdAAfBDczSXmONudCWlH6nsMQY_4m4sGmaqyPHyCHERJZxGfz6mS5CbYqgrFM82484B-BbMMpQjJzBan3rFNIhJYBW80r7zhR9zzJFULQ7mQtyuh_0Vt90tTg5RqnhcqwaPeQ6CkQ-Z64QU4M9tOx1cOKZafTGADjNINr-DIAKDn1iffJKRVoRxMhf74I3q5icw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=uiOoRSwSWKyIU4XUeozD64xNbrUnpByRBWua7mD_XmfCELybKe-BDqlcvZ1u0JKzRgq4cefYY4sgZK3gA3CnnoXbHkLYpNxZkDWewXiz7naFhg1UC2AwPN-ij7JNdvGfRqG9SEzMEOy8GU8lga0kdAAfBDczSXmONudCWlH6nsMQY_4m4sGmaqyPHyCHERJZxGfz6mS5CbYqgrFM82484B-BbMMpQjJzBan3rFNIhJYBW80r7zhR9zzJFULQ7mQtyuh_0Vt90tTg5RqnhcqwaPeQ6CkQ-Z64QU4M9tOx1cOKZafTGADjNINr-DIAKDn1iffJKRVoRxMhf74I3q5icw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
متظاهر حريدي في محاولة إنتحار رفضاً للإنضمام إلى الخدمة العسكرية ومن تحت عجلة يهتف "نموت ولن ننضم للخدمة".
😭</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76302" target="_blank">📅 19:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421e16253.mp4?token=VBqvdmcTx_m9M8HmMHEztFBSIaQgiVjxbqNTXuo8yxYaf3A8puygab_1P86NiN8HESnSNQR3BlkkhDy9tL4mJgOg41u6JBKVHN5t27UzOcflp29mbGqdtEJemYAS_48tdF09fYGIj20qZZKHdcsgUd_iSWD3IOOiCQo6vIgbTcwuRKUoX5vY9rgFCBhpZTq_LYbfdofWRFHwAlag6WFlII_rsiNEloH3mUa4p1Lcml2_dej9DmCr0OgVibt71if-l0zNMwZQ8zwgnaIreRLssTpjnhNgo8eEULEHOR-cK0y6byCgb-gXYeC8YkyUsJe1dViSQXVjH0w-W8sit7DAwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421e16253.mp4?token=VBqvdmcTx_m9M8HmMHEztFBSIaQgiVjxbqNTXuo8yxYaf3A8puygab_1P86NiN8HESnSNQR3BlkkhDy9tL4mJgOg41u6JBKVHN5t27UzOcflp29mbGqdtEJemYAS_48tdF09fYGIj20qZZKHdcsgUd_iSWD3IOOiCQo6vIgbTcwuRKUoX5vY9rgFCBhpZTq_LYbfdofWRFHwAlag6WFlII_rsiNEloH3mUa4p1Lcml2_dej9DmCr0OgVibt71if-l0zNMwZQ8zwgnaIreRLssTpjnhNgo8eEULEHOR-cK0y6byCgb-gXYeC8YkyUsJe1dViSQXVjH0w-W8sit7DAwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76301" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=OjmSiHu39ap5qqLArnc2SFcM4BlIjtp_a5Y4EDoBwZdqt-ZEwnC_us_P5H1jxC1YdryA-5NX4ojpbI10LFJD4gY-wc1RGhDJyJh6PuPqjQ7ntmS52eN7dGAhYVhyshmkneeN_pcoKh9ovCz86SrcvZ5LWVvc8FbBVwLr_Ozd6v1A5UFL4a-i0BwI02h_uprKYLEgN469b5qy_q9nd_VTIEHXlpR9nstmj_dQTBwxOuT4voTD-fRoqyZ0uceH0qX1Zt7e_bP7rAxDvg0AmG3mSqRr9SCcJULjddudUzx75yuGowbgXhj8CkZKZl2eh-Pp-VQ0sX8Pbuam68R1dfCBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=OjmSiHu39ap5qqLArnc2SFcM4BlIjtp_a5Y4EDoBwZdqt-ZEwnC_us_P5H1jxC1YdryA-5NX4ojpbI10LFJD4gY-wc1RGhDJyJh6PuPqjQ7ntmS52eN7dGAhYVhyshmkneeN_pcoKh9ovCz86SrcvZ5LWVvc8FbBVwLr_Ozd6v1A5UFL4a-i0BwI02h_uprKYLEgN469b5qy_q9nd_VTIEHXlpR9nstmj_dQTBwxOuT4voTD-fRoqyZ0uceH0qX1Zt7e_bP7rAxDvg0AmG3mSqRr9SCcJULjddudUzx75yuGowbgXhj8CkZKZl2eh-Pp-VQ0sX8Pbuam68R1dfCBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76300" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭐️
إعلام العدو:
التقديرات هي أن المعركة القادمة مع إيران ستبدأ بمفاجأة تامة دون أي إنذار مسبق.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76299" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
حزب الله ينشر:
لِتَعلَم كلّ أمٍ عِبريّة...
תדע כל אם עברייה...</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76298" target="_blank">📅 18:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تهدد سلطنة عُمان:
‏لن تتسامح حكومة الولايات المتحدة مع أي محاولة لفرض رسوم عبور في مضيق هرمز. وعلى سلطنة عُمان، على وجه الخصوص، أن تعلم أن وزارة الخزانة الأمريكية ستستهدف بقوة أي جهة متورطة - بشكل مباشر أو غير مباشر - في تسهيل فرض رسوم العبور، وسيتم معاقبة أي شريك متواطئ. يجب على جميع الدول رفض أي محاولات من جانب إيران لعرقلة حرية التجارة رفضًا قاطعًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76297" target="_blank">📅 18:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a977370897.mp4?token=tgGXlOK8h8UNzboystuc5wAHgi2ZjLmqZlO_Znhpna2QPlGc-6d0ExJ_6jOCjoH84We4WYVr3MLd8nyqpl5wiCigJJJxfj5wAeqHYSXcJrD4Jk8vvnU8y2TwKUdIq3AJojPXELL4qwzIs7jtGJjeq8Z2t9skPaxSMECYsgW7JyE3g3o2Hv_J6Dw0T8j7e2iNtjMNeOdW3roJmzWGORQ-ronbnYu3c48nJTa49JX7hUA3ABPSz0eM8pmGqotAaYCXcgpM_K5lDNALOtt5_fT8_LkQJSci3rDGnGkuqj_jRhgb2H-9KXqC3CS9p4_zGcfB9kM4y2ZyxSucr4e8WodScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a977370897.mp4?token=tgGXlOK8h8UNzboystuc5wAHgi2ZjLmqZlO_Znhpna2QPlGc-6d0ExJ_6jOCjoH84We4WYVr3MLd8nyqpl5wiCigJJJxfj5wAeqHYSXcJrD4Jk8vvnU8y2TwKUdIq3AJojPXELL4qwzIs7jtGJjeq8Z2t9skPaxSMECYsgW7JyE3g3o2Hv_J6Dw0T8j7e2iNtjMNeOdW3roJmzWGORQ-ronbnYu3c48nJTa49JX7hUA3ABPSz0eM8pmGqotAaYCXcgpM_K5lDNALOtt5_fT8_LkQJSci3rDGnGkuqj_jRhgb2H-9KXqC3CS9p4_zGcfB9kM4y2ZyxSucr4e8WodScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إطلاق صواريخ إعتراضية شمال فلسطين المحتلة دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76296" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
‏
أكسيوس عن مسؤولين:
اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76295" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
🇺🇳
‏الكيان الصهيوني يعلن تعليق علاقاته مع الأمين العام للأمم المتحدة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76294" target="_blank">📅 17:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه الجيش الاسرائيلي برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76293" target="_blank">📅 17:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه
الجيش الاسرائيلي
برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76292" target="_blank">📅 17:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76291" target="_blank">📅 17:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تنظيم داعش الارهابي يتبنى الانفجار الذي طال جهاز مكافحة الارهاب العراقي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76290" target="_blank">📅 17:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
‏
التلفزيون الايراني:
بينما انتهكت أمريكا وقف إطلاق النار مرارًا وتكرارًا بمهاجمة الأراضي الايرانية خلال المفاوضات وفترة وقف إطلاق النار، يسعى جيش هذا البلد إلى إيجاد ذريعة لبدء حرب من خلال بناء رواية زائفة! سيكون رد إيران من خارج المنطقة. المفاوضات ما هي إلا خداع أمريكي جديد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76289" target="_blank">📅 16:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76288" target="_blank">📅 16:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3gwqXeA7HuUIWFtmxhNaTJ9IcBmjjQjLLoW7cTuHqIMckxmLgtEDcn2vmdVVCZPBfTj5YAQ3_tl4ZSnNSa4qKEyCGlDworZHhgrQ6OJkfm0qoHivotR29i5t7zkDglz2ypp4-fptS9gG-wKO8Xuj-J3tXxK7lbKyQ7ljXhomWItYhhbP7O2G455iGW6M4j9ykwi8X9rFqwI-qEefNGZLwzPucnnWsCB2fzWRQ6bpBZcHG1lYLLh42lhck-GpBWbZdYrtkVjSAdN-9nQz-TUqf7-Y6T8lzGiqxCCDocFisI6AdrF0GWVcc8p6BElMcPrShZFJQl0friqq34QAb0DUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخزانة الأمريكي:
سنمنع الطائرات الإيرانية من الهبوط في المطارات والتزود بالوقود وبيع التذاكر.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76287" target="_blank">📅 16:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وسائل اعلام تزعم:
إسلام أباد ستعرض يوم غد على واشنطن نقل اليورانيوم الإيراني إلى بكين تحت رقابة دولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76286" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
