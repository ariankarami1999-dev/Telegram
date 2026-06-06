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
<img src="https://cdn4.telesco.pe/file/CJ_OdKKohqS8V1etGgC3YcFRRbann5prs7RKI6J7VT1sMsbVQnPkRH9Ob__jRK_7uhVoAabhTZNnYoZBNdwf2KAxspIdj1rCFNhLGTtrDZbE8Pud_VaP4Ey33LrRNesabaCnt90OQj98dat2xLxuamhPwVYJoZOCMRoFxqkRp9JnzxxslRYY4ks-UDniIcq17gfxx6JYygvjPw-bWzToLoLjcBRYFP5Znk1DgYmB1_QDUyeGBgqBnYkwJxK2ip6Hcmvbno9zNlKNUgrZyPDAUok_xgGtymdZHThiSf8Pi9uOMTnfpIc9TWqEAO5f884NCmmuJ0RKFytGatt0OVDc7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKx--9YNSbaVcUjA4jZmJJaKfCRnUmqzjxe-BfVclvLM0DcXPByQLtk6MY8MOB9k1SHTkykUEz95hCr046U7oLt-5Os3R3DOlCfWWvaV6jCt1uxLQYwVXC-Lq2c2wPSBPVcd5-snAb_kW3vlAvfygvmnkDpgLQbaCibLTWoZo2WFSsNQv3viRt2vKOA0-rE8AbPI5zFI_Dx8aJZHMTGM6MqPzCY1OdwYP3T-90JNDxdlDaeWpKQmxTaCiKysFQvHO-_LcOpDetjEbD6_g60IgE4-OV16pEs2MnSgPGPUtJogs_ebqtqQXwgHltRgmayN6yfq4PSm07Au27Mee7Bjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالكاتوغرافي
أهداف في دويلة الكويت قاعدة علي السالم الأمريكية تم دكها بصواريخ الحرس الثوري بهذا الأسبوع وجاءت الصور من المواقع المستهدفة لتبين حجم دمار شامل داخل القاعدة ..</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/naya_foriraq/77225" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇳🇿
الرئيس التنفيذي لشركة طيران نيوزيلندا:
يجب على شركة الطيران تحديد أولويات التكاليف والأسعار وتوحيد الرحلات الجوية إذا ظلت أسعار الوقود مرتفعة، قامت شركة الطيران بتعويض 25 ٪-40 ٪ فقط من تأثير تكلفة الوقود من خلال التحوط ورفع الأسعار</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/naya_foriraq/77224" target="_blank">📅 17:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏رئيس لجنة حصر السلاح في العراق: الحشد الشعبي سيتخذ قرارات بحق من يرفض تسليم السلاح</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/77223" target="_blank">📅 16:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق: كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/77222" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق:
كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/naya_foriraq/77221" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKIGFvO_RlAeTJObM5fhqlGfpyOm1URhh_hYFIlsVIhzphOpfBDOjUF7kggauswkJ6gZH4f6K-DKt_OW2o6LFQglcIpPnwgcZUtXtO9lF1chKeQtxmW-VkujtKz7ts8Pf5nMzGnZ3NIc_aG7WUPbVxzQmOMIvuPQkXJlZbqpfBGEjo9cT1iWmGu3TQ1NlyVLB_VItKElia9KLkql_i5BkMryx4udwrM_PPDNKFmtRexx5EL8QQaK16JpfGHEDb11HC_yhdohk2edC4wIZ3CCQCpXlgkhk8Y_a-BHI5wUuXsg9X8U3eBr4OSDEbv68HKI0M9PDyr8h23AEm9tQS3YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان لوزارة الخارجية للجمهورية الإسلامية الإيرانية بشأن الانتهاك المستمر لوقف إطلاق النار من قبل الولايات المتحدة
- تدين وزارة الخارجية للجمهورية الإسلامية الإيرانية بشدة الاعتداء العسكري من قبل الجيش الإرهابي الأمريكي في الساعات الأولى من صباح يوم السبت على منشآت الرادار والمراقبة الساحلية في منطقة سيريك وجزيرة قشم، والتي تكمن مهمتها في حماية أمن حدود البلاد وأمن الملاحة في الممرات المائية الدولية، باعتباره انتهاكًا واضحًا لوقف إطلاق النار واعتداءً عسكريًا على السيادة الوطنية والسلامة الإقليمية للجمهورية الإسلامية الإيرانية
- هذا الإجراء، الذي يأتي في سياق السلوك العدائي والاستفزازي المستمر من قبل النظام الأمريكي تجاه الجمهورية الإسلامية الإيرانية، يدل على تجاهل كامل من قبل السلطة الحاكمة في الولايات المتحدة للمبادئ الأساسية للقانون الدولي وميثاق الأمم المتحدة. وقد ردت القوات المسلحة القوية للجمهورية الإسلامية الإيرانية، في إطار الحق الطبيعي في الدفاع المشروع وبحذر وحزم وقوة كاملة، برد مناسب وفعال على هذا الاعتداء العدواني، ولم تسمح بتحقيق الأهداف الشريرة لمخططي هذا الاعتداء
-يثبت الانتهاك المتكرر لوقف إطلاق النار من قبل الولايات المتحدة مرة أخرى أن هذا البلد لا يملك فقط إرادة لتقليل التوتر والعودة إلى مسار الاستقرار، بل إن أفعاله المغامرة تعرض أمن المنطقة لمخاطر جدية، وتقع مسؤولية جميع الآثار والتبعات الناجمة عن هذه الأفعال غير القانونية وأي تصعيد محتمل للتوتر على عاتق الحكومة الأمريكية.
- تؤكد وزارة الخارجية للجمهورية الإسلامية الإيرانية، مع التشديد على الحق الطبيعي والمشروع للبلاد في الدفاع عن نفسها استنادًا إلى المادة 51 من ميثاق الأمم المتحدة، أن الجمهورية الإسلامية الإيرانية ستدافع بكل قوتها وباستخدام جميع إمكانياتها عن سيادتها وأمنها ومصالحها الوطنية. وعلى هذا الأساس، تدعو وزارة الخارجية الدول الإقليمية إلى احترام مبدأ حسن الجوار والالتزام بالمبدأ الأساسي في القانون الدولي القاضي بعدم السماح للأطراف المعتدية باستخدام أراضيها ومواردها لتصميم وتنفيذ أعمال عدوانية ضد الجمهورية الإسلامية الإيرانية.
- كما تطلب وزارة الخارجية من الأمين العام للأمم المتحدة ومجلس الأمن والهيئات الدولية المسؤولة الأخرى أن يتخذوا رد فعل فوري وفعال تجاه استمرار الانتهاك الواضح لوقف إطلاق النار والإجراء غير القانوني من قبل الولايات المتحدة، وأن يمنعوا تطبيع الانتهاكات المتزايدة لميثاق الأمم المتحدة والإجراءات التي تهدد السلام والأمن الإقليمي والدولي.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/naya_foriraq/77220" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إذاعة جيش العدو:
الجيش الإسرائيلي هاجم اليوم عن طريق الخطأ مركبة تابعة للجيش اللبناني - بعد أن ظن أنها مركبة لمقاتلي حزب الله - وقتل بالخطأ ضابطين وجندي من الجيش اللبناني.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77219" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
وزارة النفط العراقية تنفي إيقاف ناقلة نفط خام من قبل القوات الأمريكية قرب مضيق هرمز نتيجة دفع مبالغ لجمهورية ايران الاسلامية بالمقابل لاغراض العبور</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77218" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🐦
رئيس المجلس التنفيذي لحركة النجباء الشيخ ناظم السعيدي:
لا يصح استحضار موقف المرجعية بشأن حصر السلاح بيد الدولة بمعزل عن بقية مطالبها المتعلقة بمحاربة الفساد، واعتماد الكفاءة والنزاهة، ومنع التدخلات الخارجية، وترسيخ سلطة القانون وبناء المؤسسات الوطنية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77217" target="_blank">📅 14:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني: المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77216" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77215" target="_blank">📅 13:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77214" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 28-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77213" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
‏
نائب رئيس قيادة العمليات المشتركة العراقية:
أحبطنا عدة هجمات نحو دول الخليج واعتقلنا متورطين بالهجمات على دول المنطقة وتوصلنا لخيوط مهمة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77212" target="_blank">📅 13:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني:
المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77211" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
إعلام سعودي عن مصادر: ترمب أبلغ الوسطاء أنه لا مفاوضات أكثر من 60 يوما وأنه على إيران الرد سريعا</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77210" target="_blank">📅 12:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: سقوط طائرة أمس الجمعة في منطقة كفار باروخ في مرج بن عامر بسبب غير معروف قد يكون خللاً فنياً.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77209" target="_blank">📅 12:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGET8NulWCh43kl3tl6OPchrrDSZNsVg5BRRjV5sMGHy-Sef0RgHR2MDQM6QSFzhcRxI-sOsaGKuBUwLjpqfj-Kcrt4bSfqpUN2IY-awcAw7O8yI9ettQhrZIdjreEtwR-zKv8JRqC_z-HyzbKUEsHOfvqgrLr7QvAkRe8Oz5_ZPltIxYKVEfXvWrUO_ZaxibF91iuTo2ZZAwGzyFOAe9aCU8rIJhKHnoiw7zgvxRsjuVZbAe4tz5boCwvDj5j4ie43neigVsaQI56orRnAPaorf73F8zKI7wTAyL7fbhF_-i6-NCrrEBBrv3RNGxt6Mm29-lGo5tV5QWKVxhL2a9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«أَمَّا بَعْدُ، فَإِنَّ الْجِهَادَ بَابٌ مِنْ أَبْوَابِ الْجَنَّةِ، فَتَحَهُ اللَّهُ لِخَاصَّةِ أَوْلِيَائِهِ، وَهُوَ لِبَاسُ التَّقْوَى، وَدِرْعُ اللَّهِ الْحَصِينَةُ، وَجُنَّتُهُ الْوَثِيقَةُ. فَمَنْ تَرَكَهُ رَغْبَةً عَنْهُ، أَلْبَسَهُ اللَّهُ ثَوْبَ الذُّلِّ، وَشَمَلَهُ الْبَلَاءُ، وَدُيِّثَ بِالصَّغَارِ وَالْقَمَاءَةِ، وَضُرِبَ عَلَى قَلْبِهِ بِالْأَسْدَادِ، وَأُدِيلَ الْحَقُّ مِنْهُ بِتَضِيعِ الْجِهَادِ، وَسِيمَ الْخَسْفَ، وَمُنِعَ النَّصَفَ»من خطب امير المومنين ع</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77208" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#ترفيهي
‏الرئيس اللبناني جوزيف عون يهدد اسرائيل: لن نتهاون بحماية أرضنا وشعبنا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77207" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: احتلال "البوفور" (قلعة الشقيف) هذا الأسبوع استُخدم لإعلانات الغطرسة ومحاولة لإعادة تسويق المعركة العرجاء في الشمال</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77205" target="_blank">📅 11:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=WjnQKQe0MmdDm1HVJ4pZDH1iPlCybnEouZCnEo2Q-4y7TLaSzajHDxE7ZwanQU0b2m9z2IMuqCcF3iL-6CLITlQnWj8PTBkghx6JnY5PW0Wt6RwfNIuRaHrlKjO9BycDQtirtqSB4E1LLrr22KDOhQZtEPTZpk1xIP8gIzo2spK32TFrhpi4PDVPHiKnzVlBjxEPXbYv7TH8cD6uZbjlDA4U735I4m4oSIND5iH2Nv2l7PphTKAMX-nnd8rlXlFCiN845orWeoZ6ZK8tju_9enjpHQKLemeWI12NMTRLhFDwRAtSGp5fQbyrUxGbpeZi63XBVKMG9j83p9A8mSLoyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=WjnQKQe0MmdDm1HVJ4pZDH1iPlCybnEouZCnEo2Q-4y7TLaSzajHDxE7ZwanQU0b2m9z2IMuqCcF3iL-6CLITlQnWj8PTBkghx6JnY5PW0Wt6RwfNIuRaHrlKjO9BycDQtirtqSB4E1LLrr22KDOhQZtEPTZpk1xIP8gIzo2spK32TFrhpi4PDVPHiKnzVlBjxEPXbYv7TH8cD6uZbjlDA4U735I4m4oSIND5iH2Nv2l7PphTKAMX-nnd8rlXlFCiN845orWeoZ6ZK8tju_9enjpHQKLemeWI12NMTRLhFDwRAtSGp5fQbyrUxGbpeZi63XBVKMG9j83p9A8mSLoyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
عدوان صهيوني غاشم استهدف منزلاً مدنياً في بلدة السكسكية جنوب لبنان وإصابة عدد كبير من الأشخاص</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77204" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=mqplPwdUs-TfWAhm52tif_vkqoziR0lWI6nhYVy3WlGv-5YlDRYiJywuQZm7iCWD7uo5Xu-kRpL1hNNdjYzlnVJMb_hkJeb5DjDcJtgXYSJrKenedZo79FaxJf8a85Uql56aP3SgU7dj8i59L9PbYfSNa1_hOaErpGIk4LVXxJVA4eWgg7ai-pZb2d68kS5cYzG3Dx1RyiajgJBVoOCgsBI2aD1vDSibc-Cc7ohDnovueAbqNejJUbGjY3kWJXpJdnRjIhWqGlrFkNZ4bZ9QbmcyynXfEOUX6fBgVnMOWr6RxJBLbQ4G8gjfGgp6jiycoEmYAmzCeTWPwWQdAu-DmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=mqplPwdUs-TfWAhm52tif_vkqoziR0lWI6nhYVy3WlGv-5YlDRYiJywuQZm7iCWD7uo5Xu-kRpL1hNNdjYzlnVJMb_hkJeb5DjDcJtgXYSJrKenedZo79FaxJf8a85Uql56aP3SgU7dj8i59L9PbYfSNa1_hOaErpGIk4LVXxJVA4eWgg7ai-pZb2d68kS5cYzG3Dx1RyiajgJBVoOCgsBI2aD1vDSibc-Cc7ohDnovueAbqNejJUbGjY3kWJXpJdnRjIhWqGlrFkNZ4bZ9QbmcyynXfEOUX6fBgVnMOWr6RxJBLbQ4G8gjfGgp6jiycoEmYAmzCeTWPwWQdAu-DmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المُتحدث الرسمي بإسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي
: سـلاح المخازن للمخازن، السـلاح الحر للأحرار ونحن نتحدث عن سـلاح حر  يقاوم ويدافع ويشارك ولا نتحدث عن قطع صدأت من التخزين</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77203" target="_blank">📅 10:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
مشاهد من عملية اليوم التي نفذتها القوات الجوية التابعة للحرس الثوري الإيراني ضد قواعد أمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77202" target="_blank">📅 10:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇧🇭
الخارجية البحرينية: ندعو إيران لفتح مضيق هرمز كاملا وبلا قيود أو رسوم
ندعو إيران للكف الفوري عن الاعتداءات غير المبررة والجنوح للسلام
أوامر ثانية
😆</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77201" target="_blank">📅 10:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660122eaff.mp4?token=Tb-oGOqzlLKlgBOq60dblcwP470ERlDxxlXXqjWVXYYmm66zLTAmFOyxMeM561GQSDTxvModDVoH9wP0KHkgJeX2y1OvyB55wKYEJ1Dj3mZKiYQD7UrPaw5pfQ_fgOuUBXnBmxh-2mSEH5g6UiuM-29Hhr34XUOqV1qnKoVeLd-YmerT4o5PqXcnfDcQIj-wsGJkPhpB_fSNLf7w_fXm-YZpE1fSlf7YYyarK82yd77UnFNXS3adRcd2gbS-khM477rlHhRoZwBefhS2pM4UHB3WYH2xP8SVX0RPbNYvs4YEpJ6DeiAr9Jnqedkbe96teDv2stFHGpn9B1P2puliwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660122eaff.mp4?token=Tb-oGOqzlLKlgBOq60dblcwP470ERlDxxlXXqjWVXYYmm66zLTAmFOyxMeM561GQSDTxvModDVoH9wP0KHkgJeX2y1OvyB55wKYEJ1Dj3mZKiYQD7UrPaw5pfQ_fgOuUBXnBmxh-2mSEH5g6UiuM-29Hhr34XUOqV1qnKoVeLd-YmerT4o5PqXcnfDcQIj-wsGJkPhpB_fSNLf7w_fXm-YZpE1fSlf7YYyarK82yd77UnFNXS3adRcd2gbS-khM477rlHhRoZwBefhS2pM4UHB3WYH2xP8SVX0RPbNYvs4YEpJ6DeiAr9Jnqedkbe96teDv2stFHGpn9B1P2puliwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
قوات الاحتلال الإسرائيلي تقتحم مدينة القنيطرة السورية وتقوم بتفتيش المنازل واعتقال عدد من السوريين المدنيين.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77200" target="_blank">📅 10:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721967c09.mp4?token=jWxTe6yVUfiv4MpPtOJbls8q9TwPhtn6aPj5n7qtCXJcLO3WDEQfNaAO1Pn1MQn09a0iJWSFDNp8pSVetUPKkVhNLiQE8-mGKsyJR3jnTQUeVHE4vtbe2lJr8pNu4KZRy3o73dEQZTsQXRhyz8Nty4WSya81yZicAr8D6tTK3--5R33h_LQnnNCuFkv91TbHaS-U81yGja4B67NrDeMgIlVUWX_zRwu-qPVrDQBoC9XEq5TKHbxdOXYYYRu8bZLr082qXexKUIISOEYsfCo1aTXYSfb7Uq2HZm5PudHKXM1Di5ZCUdzoDhnMZxfxprVZRA1S5kX3V89a8KPuz5oOkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721967c09.mp4?token=jWxTe6yVUfiv4MpPtOJbls8q9TwPhtn6aPj5n7qtCXJcLO3WDEQfNaAO1Pn1MQn09a0iJWSFDNp8pSVetUPKkVhNLiQE8-mGKsyJR3jnTQUeVHE4vtbe2lJr8pNu4KZRy3o73dEQZTsQXRhyz8Nty4WSya81yZicAr8D6tTK3--5R33h_LQnnNCuFkv91TbHaS-U81yGja4B67NrDeMgIlVUWX_zRwu-qPVrDQBoC9XEq5TKHbxdOXYYYRu8bZLr082qXexKUIISOEYsfCo1aTXYSfb7Uq2HZm5PudHKXM1Di5ZCUdzoDhnMZxfxprVZRA1S5kX3V89a8KPuz5oOkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مقتل إرهابي من الجنسية الروسية يتبع للعصائب الحمراء اثر اشتباكات مسلحة داخلية بين عصابات الجولاني في مدينة إدلب.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77199" target="_blank">📅 10:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=uDssHspRtjV9zHDwZC2-VavnmV4ARUfe4l9RsHug0x_2DYQ-bLoBNUX0El7ep28kBHLZ-dzxnCTqhzUCJrDk0Lww_CAjlXu0CDg6y4P2b2xIKPNYWCSH-WLp8MnAIXMILGrq3Hn8jQBZUd30fdG8leFWLMM5zPwnFzIHYsOx_QYLmdaEUuO6CDyoPJf44mJ-ohM6UxsBdbCsgoUxVWQapu_YICpatWV-rp_rB5l0RLODl_B81UADXgGEUul0cFCzx4wKpEH06FlXqYEwxcubO-WUukOk9WnhZlhE8dmUPXI5rMo0IBccoMczyvRV5_nkeGNAS3i38qANmT_ZeNDq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=uDssHspRtjV9zHDwZC2-VavnmV4ARUfe4l9RsHug0x_2DYQ-bLoBNUX0El7ep28kBHLZ-dzxnCTqhzUCJrDk0Lww_CAjlXu0CDg6y4P2b2xIKPNYWCSH-WLp8MnAIXMILGrq3Hn8jQBZUd30fdG8leFWLMM5zPwnFzIHYsOx_QYLmdaEUuO6CDyoPJf44mJ-ohM6UxsBdbCsgoUxVWQapu_YICpatWV-rp_rB5l0RLODl_B81UADXgGEUul0cFCzx4wKpEH06FlXqYEwxcubO-WUukOk9WnhZlhE8dmUPXI5rMo0IBccoMczyvRV5_nkeGNAS3i38qANmT_ZeNDq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا   من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77198" target="_blank">📅 09:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=i_hJPCGxnPOBw_addej9DI3Cmcz8td86Pwsigrm8ycmy3a1I_cRYOAAMYMDRBcKxZ2XNJlZqVJujkV-2BkCkv7ZfDP_pTmxVRLu3gdJCvDnHMbtScyYEAcqZi3IEsQwvByytG0PGJb0WSIJV_k2b7x3ZTswaHimBT6j7DUcpXl7D9-aMPS02iNBuqSrL3XqS8-LDN1T9MLWZreSwmk-pqag2LGZ2VDof75ZPXkpULy6oqspaev5FAq881MTiEw06RxdjZbZXj3E9SjOkK16i2-hWDPVg7zKt599Jf7qp2wrO6D_VApImPacSkrxhDzy_HbAVvf0HHQD0nG96_oVnAqj8c11ESlHwm7Uv_tdMnhJroFgKIy4pNvFf2OHWIhOYqznVkMe10ftnZUWcVS0jDT3FoE9RpNRqeRdNnEHhrMCoBkXxzG2sRXAUqRsc2G5BTwdEEjBGhWhypoCNlTvoE2Fw5flray3eaOUGx4ghcZ_1uQ43vHBV76sdJYUl1xIwbdsrnjrJg_Y6q8o9I7_zKXh_95BBeAeQs5WguEkzVm0EcurW2U5Bupiu5Ler5lpxbyMb34pe-oaE6J2n6uMhVCHPQnhvU1r5qy_TZ90N-y9ZBSr0oj2jRt2g8Rimc4mRq_039zYOT17vLp6on50OjRfqtgvBvF9o-NkznONg5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=i_hJPCGxnPOBw_addej9DI3Cmcz8td86Pwsigrm8ycmy3a1I_cRYOAAMYMDRBcKxZ2XNJlZqVJujkV-2BkCkv7ZfDP_pTmxVRLu3gdJCvDnHMbtScyYEAcqZi3IEsQwvByytG0PGJb0WSIJV_k2b7x3ZTswaHimBT6j7DUcpXl7D9-aMPS02iNBuqSrL3XqS8-LDN1T9MLWZreSwmk-pqag2LGZ2VDof75ZPXkpULy6oqspaev5FAq881MTiEw06RxdjZbZXj3E9SjOkK16i2-hWDPVg7zKt599Jf7qp2wrO6D_VApImPacSkrxhDzy_HbAVvf0HHQD0nG96_oVnAqj8c11ESlHwm7Uv_tdMnhJroFgKIy4pNvFf2OHWIhOYqznVkMe10ftnZUWcVS0jDT3FoE9RpNRqeRdNnEHhrMCoBkXxzG2sRXAUqRsc2G5BTwdEEjBGhWhypoCNlTvoE2Fw5flray3eaOUGx4ghcZ_1uQ43vHBV76sdJYUl1xIwbdsrnjrJg_Y6q8o9I7_zKXh_95BBeAeQs5WguEkzVm0EcurW2U5Bupiu5Ler5lpxbyMb34pe-oaE6J2n6uMhVCHPQnhvU1r5qy_TZ90N-y9ZBSr0oj2jRt2g8Rimc4mRq_039zYOT17vLp6on50OjRfqtgvBvF9o-NkznONg5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا
من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77197" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📰
قناة NBC News: البنتاغون يشعر بقلق متزايد من أن إسرائيل تكثف نشاطها التجسسي ضد الولايات المتحدة، وقد تم رفع مستوى التهديد إلى أقصى درجة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77196" target="_blank">📅 09:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeIKoKAeILfs9VPLHbmQ7N5QJxOxlJCbw6jDie_DZVJ5GcgkG5LVSH_YRUcp9ec7YPxD7I5Hv7Y1LNQ6lHgC4qapdgIpRU7s8MTpaykuPLM-aIy4nUBGQOsejib30nHSOz5rbeHCx7sKuTqiRREyGnuOdxUKEBSKcm3sQyaf1q53Z_pM1d2M-k--htBcjH4JYytb2HmPdZXEGdnjnv3BmwByDVxrfii0qpo761L6St5g3jMPJdCsoCOHBvQ2eh69fpihIzjs0RjqqL5a3q_IBBAhSmZ8MVx0_UBOMJfYjr8i4srr-OPp592o3jFc0HjN0kCEKCtDoTOjwxaZ7AeKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWmlNOnqvv4mkpfDjn0gRntIquyv3JQnpIzp0HynM0jSrQgW9oJH479NwTcWhzTnxU_IHm9fgVIlP1yYA6jsayWFkNopZmax2vJApGRpYvwfB6ARIbmAg4W0kex0gvxyUGWzIHsEhuA6ZnJSeWf2VhPdl22c5lPuLlkigcJcI5c7HW7OQDlhhN2PILbgZVLP1gXlm4I-4obiaJ_hXw_-sZ1exzYwKgT-cFC32rivbmZZ78MT_U15xG2UmucCrGF-t8hVzGFtuOGjDpUOxj4bL78CQi8YmAZ-qJZ6SmOcECPCd2JOsA4wbPAdXcK6az8FRjF_dwp3TX9n45xCA1o8OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور للأقمار الاصطناعية توضح استئناف تحميل النفط في محطة جزيرة خرج البحرية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77194" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=vVT3fgqnX6d5cvjvXsTbA0qCgPjloAhpudDsq85ilqAJ2VIloMW3pWR6qihEz8lEwJJvp-zFVI0i5KBodkdVz32ZHoMuR2sT2lwUEalvXyp5C_j1X89iavaM3eOzbkPjaZGEXkR54gBBxS-u-xTRoUiZiRDzsLyz2SYgKeM6gqCPyoGvLsTEHoD-MPSeSEPznWjC3dLWAXIOi1ZvqaQMMMCV1DsIrBtfPee3AisN-WeRMF3WBMFfKZ7jJU8vd-3NJE1AEVIYURMDN-sV3Z_hhrm7yOFE_RpIr4n7Xb4qZahGTYT9430dCpT_mS_Dyg4_0OCK2fZTU2c_GQjdf7rttlbkh1StOltHt3Yw_nlYC-1N36QpN8nco67_u0tAYsgaadtgZO5OXhiQ4isPXKlma-AmjEH8glVPSMOwtSdpNXwdu2qG8fBSpzOz7UmBa3FMuKrgDicU2v2zeM5qs-WGfKeChSCxFWOgHL1Gb2g0ugFKVm4BNwr7lmjD6Y5na06cj0DxE3EE4M_wFJlHx5-lmRrJzY-PznDYW0hb-7t2yz0Haoj59ZLyaj8Wh9cf-oS2D47IIyxnbjtmzdB8NWYWtst4PGSStP4J8vUQM4HNqYNMgHRwLqLrOXexZFYWoe_rwxMTC66lskY0YKoU5lVUQTb09WWfGdBqOby8FErv90I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=vVT3fgqnX6d5cvjvXsTbA0qCgPjloAhpudDsq85ilqAJ2VIloMW3pWR6qihEz8lEwJJvp-zFVI0i5KBodkdVz32ZHoMuR2sT2lwUEalvXyp5C_j1X89iavaM3eOzbkPjaZGEXkR54gBBxS-u-xTRoUiZiRDzsLyz2SYgKeM6gqCPyoGvLsTEHoD-MPSeSEPznWjC3dLWAXIOi1ZvqaQMMMCV1DsIrBtfPee3AisN-WeRMF3WBMFfKZ7jJU8vd-3NJE1AEVIYURMDN-sV3Z_hhrm7yOFE_RpIr4n7Xb4qZahGTYT9430dCpT_mS_Dyg4_0OCK2fZTU2c_GQjdf7rttlbkh1StOltHt3Yw_nlYC-1N36QpN8nco67_u0tAYsgaadtgZO5OXhiQ4isPXKlma-AmjEH8glVPSMOwtSdpNXwdu2qG8fBSpzOz7UmBa3FMuKrgDicU2v2zeM5qs-WGfKeChSCxFWOgHL1Gb2g0ugFKVm4BNwr7lmjD6Y5na06cj0DxE3EE4M_wFJlHx5-lmRrJzY-PznDYW0hb-7t2yz0Haoj59ZLyaj8Wh9cf-oS2D47IIyxnbjtmzdB8NWYWtst4PGSStP4J8vUQM4HNqYNMgHRwLqLrOXexZFYWoe_rwxMTC66lskY0YKoU5lVUQTb09WWfGdBqOby8FErv90I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القيادة المركزية الأمريكية: اعترضت القوات الأمريكية عدة صواريخ باليستية وطائرات مسيرة إيرانية أطلقتها باتجاه مضيق هرمز ودول الخليج المجاورة.  أطلقت إيران سبعة صواريخ باليستية باتجاه الكويت والبحرين بعد ساعات من إسقاط القيادة المركزية الأمريكية (سنتكوم) أربع…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77193" target="_blank">📅 05:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني: بسم الله الرحمن الرحيم من اعتدى عليكم فاعتدوا عليه كما اعتدى المعتدون. في تمام الساعة الواحدة والنصف من صباح اليوم، قامت أربع ناقلات نفط معادية، بتحريض وتوجيه من الجيش الأمريكي المعتدي، ودون تنسيق أو مراعاة للتحذيرات الصادرة عن القوات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77192" target="_blank">📅 05:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني: في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77191" target="_blank">📅 05:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAaPuBv4K6NcbJOWbnapSviZrfvEiMlZ42pV65u4JVEAI3tpD1PMC8Ld0e-hl5nv9PFKNH3tc6kQeiERQil06LHtfZUyBUyz0nEBTEeTRwHUnarvY3iAXnT5BmXbJ4GetA53Dt9VSr4TTNHF2IW2-dXJ8980xHXGheDmgHvzK40Y-vXCM7UiGOkOx8oBrGcX4AWyXeXS9spOceijVi829BEdfrLsC-VorPtnuO02JTFrhRHR-qZORgiC8ZEAPv5_3IYTYikz0GayMz67mVrPtzYKR-RI3nY3zAbBTvazk-x0I_31yrAmCdqQJuaGO70YGDQQUqsEdfT3cgJE_hmbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77190" target="_blank">📅 05:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني:
في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77189" target="_blank">📅 05:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDUh3UlGa0hcTJ2kNiato1H963To9gpsmlRDCY4vDVr0f_-0K5gfV2FRFGRXv4G2bRA3S0I1H-GTvj70AAQg597M8up66Z7ZpwLmPJpVuVw-X47eGt21sRRZkZ0NAEA6aqQi3oMfZ9Ebty8qxeYoyq4Yq5xMxMyTrolf5PQrAYoQfb_-Zh-K7glPITIBsXGMV_CCUoSkaeYf7LvSSu_7x2hz2QL2e1jwjZUkZKl13wVcSddjXArCHfyo6tkRQrh5zB0_5uuYNR5PzLnWgyCwxqu1XFukiaJv6zlnyolf2qR9a-KCy3jKUzebi7GvxrrT1bWvVxd8mr6HtEvFpP-vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة
.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77188" target="_blank">📅 05:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMjYLwxGkvqSbOVLJlIXOCe2Yogd_NEHEd3I4V6fp0yFPQShtkm9Qa9sAvDDuHz9ZSbC4BOq-aRQV5o_7kp_ZhIxIflJCAiAU_ZboZH_hmVml-8oCM15ziGErJk1xqV2alTPweelaiOnWehX64PsdNBNKKOMwZxC8LLQ3xtoaDQwrCaYPpU31e92knnUi_HPPkAZfPGNmZ58qZ84j9yHo_JdcOifLvzdC88HQqRdN1HVMWvOr4yWpfcEfnikuB0g2Yn8UTP32zKtvo4Z07YT-cI5qr06OaswtaDwiG72RPsVOWOxOHfOcW_RVo0WYjlYmSkbqL7hwJdD0HI0npiifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جميع الطائرات التي تريد ان تهبط في الكويت تغير مسارها بأمر من الصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77187" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=MKzg7t0YDWqEGQVI7t_XH9bULSR81oQfb10sQuLJnBPEv95fEyZL2tg9xWasOVjAgqE1llaOcqXubG7MNpFsGJv2xn-F7PgNEK6jZBGsiI07p6nhcniJVdDzBbDoFGlRmvygdTMudXA6wXjPRoqbP9kU4EejbWxEpkZoFkKwGGYBatDqO_YtSuoqIjybPAbg97mt4Fw8W2VSODR0XheYiUaVegQjZdzb0zAKKaDrxW8KPs77Bac1M_wuELDHvN8Il3Dh72NEfaBV6p2mBC0G4n-iHUdgqJTJV2qbzkXbJqCXP31ROuwGqFkB37udLyF0wtzx7MHopaZkXAltmCoIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=MKzg7t0YDWqEGQVI7t_XH9bULSR81oQfb10sQuLJnBPEv95fEyZL2tg9xWasOVjAgqE1llaOcqXubG7MNpFsGJv2xn-F7PgNEK6jZBGsiI07p6nhcniJVdDzBbDoFGlRmvygdTMudXA6wXjPRoqbP9kU4EejbWxEpkZoFkKwGGYBatDqO_YtSuoqIjybPAbg97mt4Fw8W2VSODR0XheYiUaVegQjZdzb0zAKKaDrxW8KPs77Bac1M_wuELDHvN8Il3Dh72NEfaBV6p2mBC0G4n-iHUdgqJTJV2qbzkXbJqCXP31ROuwGqFkB37udLyF0wtzx7MHopaZkXAltmCoIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي إيراني عنيف ومنظومة الباتريوت الأمريكية تحاول الاعتراض في سماء البحرين</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77186" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=ZLP7ea_7dfO6ucE-4Yn5Ve6Av6GvX1TytQAQWhcsQ4temkA8hV9OXWQ5A8Jp6m2fDrSNF36GyrHRJzgBN8heKxnGY20Q1ZBw-8vTSw4zr6wYyozN1TBUtofHXDdf78rktpTTzQznaRG1Pifug3twlX0xYXSUpz4hFqmnisUfXTqsAI4a2uxf3cVpsUvmsMMnJr_T7ovuVbFRVT09QV6kHEW4sSebVgUKRcYQGXpkWYa06PRCwSZVszqtLw7NrIvP8MkdWiZWhAX66Z1YU1Ey46kbz1Z93Jur66R_2K8yhikn5DHyPwASDUqaaOoHovGpG40qi5ouzw_Z2WAOreJ4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=ZLP7ea_7dfO6ucE-4Yn5Ve6Av6GvX1TytQAQWhcsQ4temkA8hV9OXWQ5A8Jp6m2fDrSNF36GyrHRJzgBN8heKxnGY20Q1ZBw-8vTSw4zr6wYyozN1TBUtofHXDdf78rktpTTzQznaRG1Pifug3twlX0xYXSUpz4hFqmnisUfXTqsAI4a2uxf3cVpsUvmsMMnJr_T7ovuVbFRVT09QV6kHEW4sSebVgUKRcYQGXpkWYa06PRCwSZVszqtLw7NrIvP8MkdWiZWhAX66Z1YU1Ey46kbz1Z93Jur66R_2K8yhikn5DHyPwASDUqaaOoHovGpG40qi5ouzw_Z2WAOreJ4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشتعل بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77185" target="_blank">📅 04:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQF42_NzpgOC3fLZrFU8Y3QlaTHYzbRGYoWQrS9nBYTD7kYil7ALejxSvkIepm8L5MIkNHVEo1KrmZ6Aue8bXTKLZMvIP33qwmB8i9uh8MF8ChMnI86b8WyCDSnzggr-knC_rbx4FVSb_K7nCXRsJILCmRhGPO2MJGQ7h15HrpU2hz-GoeAtFFADqG1Vd_4qu5zx0iM8AZMrYYaOXYeMllbKnssVCmQ7hddyglUyuhMZJxjmo6CFOhWTISi6aQ4chsa4Nhsat6wNbFW_K7VniNlBaOk7P_lKl9oDnTf2Q3nXPFCDDkW_68-Tzy7kgpfM6hgzunTJ3LAol9oOC_V0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdO3Ql1WwSUsfsHg1b20ccr1QbB8Fnc-gL08Qcj6Y5viTFS9IeWkT8paAAzGZkmG2N79ZNLc3malVAqqrJuM-M8_cPS4ENIcPejas0zbFDjj6J1K42tDN-7dPnB-Cj_QiD-umjup4_Ifduz5dV_AJEyXsxH9_mqwSlnNFKG3QMTk6pAESaFw6bBAfi-zLbiQiZD06LhoALiH5K4YKvJgPT__nj-geUDwHhM0374Mvnsuxx88xXxKiW1SQIrd1dq-za4QoYW1b7RA6jRyLZ3g61kGJA8sR0Wpdh-W5cBBeYGtHYdyhgfnvxPp6axUuZkJHmXMI9fY_yxtbkHDZc2bZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تدك الاصول الامريكية في دويلة الكويت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77183" target="_blank">📅 04:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=Jpt3qU1-sYtCVzw4AJF3Fp0ZbjgfzmdmtfklKMDycZ7HTihsGSDlRmPF0-HGrrAGo61-GGuFJ5gatoV9j5B33eEFClo-7_jGDbmDPf1K9kRAhQbYyHF-wdpU046gD63hdOliCaAx1RRnKmJsSDJ2TeignpaWomH9K0tkZjfpQwX1KKZ3dEQ5kAzUpgOTs1mkSJObP9yq7O8DVf-TD0nzogdEAWFWfjZa_ANlYGAmLyrLPfvcM8hxCu8rsjwDkzVILM90OeCSY18wkl3TgcYujoxgweucFjY75Iu5njo4X2hZUXwWXAm_Nzrl33nnZDtiqcpozinDapy8SDj6XEW_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=Jpt3qU1-sYtCVzw4AJF3Fp0ZbjgfzmdmtfklKMDycZ7HTihsGSDlRmPF0-HGrrAGo61-GGuFJ5gatoV9j5B33eEFClo-7_jGDbmDPf1K9kRAhQbYyHF-wdpU046gD63hdOliCaAx1RRnKmJsSDJ2TeignpaWomH9K0tkZjfpQwX1KKZ3dEQ5kAzUpgOTs1mkSJObP9yq7O8DVf-TD0nzogdEAWFWfjZa_ANlYGAmLyrLPfvcM8hxCu8rsjwDkzVILM90OeCSY18wkl3TgcYujoxgweucFjY75Iu5njo4X2hZUXwWXAm_Nzrl33nnZDtiqcpozinDapy8SDj6XEW_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77182" target="_blank">📅 04:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXpPnYfcC2AP5mVb-Df4C-VPdbnA5iFGHD6Q1qgLvcn9iDE9IOK51WD77dbs1_pybCWjBmHTyF_HYa0fGUnhlQ_9XGN-5HdlIcRZmGSCCwaIcp7K7Surt3bdb_9Y7JbqyuBpFk5ccpoQy89DDeH3qWfm9o22GYnILqL_o0uAzWZEk3Eso8ishWdRu0I47oveVSPuOg1gwd9whhxVmibXOucgbxLag1r_s1wP3NBk22Rc83E5hBktsZV_LmeqY6zW1-1B1VNiotjnDwZbC-vJNlh2L-zsm5R5nb-2HHIhJ15YsdyQcnri97VxwwjG1YChlwdPXZVapN__S4ddbNv6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDhHb5ALSD5hyZr7k3tLpvLzpXwOQbFVYrhX0s0W3QFuh5WuElD8hzS7VVs71SVFMdM0AQ3YQgBoWR9Gca5Xk9zoFzglAxOEY0XX39YBCYU9MZW6o5ukHu7gG_g9Ce2EJs5s_dkWvYx_HqrIG1FZT5WvoPiDTANTLur1Pu_hUwid56U8jnEwqdVITcJzCOtyc_ChOjkFjsBFCFHnMzMK0l1j4S3mt_4DcJc5QeZ53F7q6c30lIRuGYwIhj_y2TTo6euGj5fLyJFLa1ZbyxF0o1-ykFWf3hqvZtJ1rJIcFKwLCTw3MAkVKPnHu34BRxuWd_Oisu_YbrxHs6Ab1X1W3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQMkPbqmxzFrj7hBsF042yTI2Wzfah-MsAjFVtMTQBB6PGE6XpAuXuYyu47YFW5b3huXOLLg1CZ9M7VHSCm-XbOuEB4FC1fiikqX9obsarR0BWaf3fCLB8tmkUJQQoyOiqJKFGaaCSlgyto5joxuDogLkEf_Lm37k7OOvSwkH260tQH3Jh7ukgr27j8rqWcQOCXH5T5spDP-3K1cM3J4ow3G6jXCaZTCxNFBnyFsL-pSwkeW5X_z5Hh_nAdEmgISK-6YBFKT7VpU1uMOwSIcgTnflW8KIhGTZJuDUqe3XczJVm_GEccKliDgt82-RWXdKd__4QOvPb6uWP-r6UJoIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مطار الكويت الدولي يستهدف بشكل مباشر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77179" target="_blank">📅 04:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مشاهد من تفعيل صافرات الانذار في دويلة الكويت نتيجة هجوم بالصواريخ والمسيرات من قبل ايران على قواعد الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77178" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=COw51bG8yGN8HgHBaPcL8kmUCL2v5fOV1uTtrYNMdp4A0QitCVrGb4A2s6KC48eP8x1cjcm3lpT2T2qrQaf-yZfaYyjd3fbgBoR0d42x9EcPn1gqkFa90zRvGUp-FqZ1KclM_86jGnJzfVw6_tmJkj8LT-x3weF6CUftuZek5aQHTaCLBXw7Tw6h0aSTJNtRhQWrU327T79sBUV-EVGcXZRhsm5aU9KyKxVyZxVQ2CWJxugL-bUOL738vIwq5C-usDob903BSHohFhChdrCZWPp0fIu2O_GbzSGaWOUCEKD_pMqno03VbaciKAw7wgiNsMAl2t_7jD5Us_0U_8O5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=COw51bG8yGN8HgHBaPcL8kmUCL2v5fOV1uTtrYNMdp4A0QitCVrGb4A2s6KC48eP8x1cjcm3lpT2T2qrQaf-yZfaYyjd3fbgBoR0d42x9EcPn1gqkFa90zRvGUp-FqZ1KclM_86jGnJzfVw6_tmJkj8LT-x3weF6CUftuZek5aQHTaCLBXw7Tw6h0aSTJNtRhQWrU327T79sBUV-EVGcXZRhsm5aU9KyKxVyZxVQ2CWJxugL-bUOL738vIwq5C-usDob903BSHohFhChdrCZWPp0fIu2O_GbzSGaWOUCEKD_pMqno03VbaciKAw7wgiNsMAl2t_7jD5Us_0U_8O5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77177" target="_blank">📅 04:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=OowpvVmXOWITXr1gQb5_rAr1tgqp2O7-ep_7HoaGMpIKT-76rfeKceFrlpHbUXPtINWjYf3K6yyIC1C1qGEVNyiWbbCE5V-PDw56skYuMJza3zYDH8s4STTWRWssjVSCa2s0KdPMHmcW9LHcnp77gvv9yzPxJvFU5DWk_YPuIihLCKSG3lMg5uqVXSV354FfCkesxUv4bBVaFM42J9DIqh_1F3k_WfcjZZt50Atl2HqhzBgfHvgwqRKQdLpfrz4AgNCclDMZfYHMeighwCqmWlCNQCKY8cyRgq9MTI_xZ6c5olbwi0elsMkU-BoDB3JmUP2lW9q6ycD3LVfgtO_VVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=OowpvVmXOWITXr1gQb5_rAr1tgqp2O7-ep_7HoaGMpIKT-76rfeKceFrlpHbUXPtINWjYf3K6yyIC1C1qGEVNyiWbbCE5V-PDw56skYuMJza3zYDH8s4STTWRWssjVSCa2s0KdPMHmcW9LHcnp77gvv9yzPxJvFU5DWk_YPuIihLCKSG3lMg5uqVXSV354FfCkesxUv4bBVaFM42J9DIqh_1F3k_WfcjZZt50Atl2HqhzBgfHvgwqRKQdLpfrz4AgNCclDMZfYHMeighwCqmWlCNQCKY8cyRgq9MTI_xZ6c5olbwi0elsMkU-BoDB3JmUP2lW9q6ycD3LVfgtO_VVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77176" target="_blank">📅 04:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77175" target="_blank">📅 04:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77174" target="_blank">📅 04:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH5Iyy00NMT-dFLCdCsv10McHqlUlBVNdozibh8ZgivKfOpTa8fO2hj29O-HjREkSrwavuTtHrK1fUPCWxGIx4DceLw5-KIMqA7FJh2ywGFFZWX5m0VbHWdST1jOEVST7DBc7eYKjJ4qRisCbdUH2C-goAp0lArytY0JOzwaeuu2MTMCIMCo2WxLcJFpeTylDTyxyrZUarGVmbxbka_Kxx8OihEv7zEAQ8Po1FjCEaMGHhuTPi6n0dNpOhv8cmadhq2V4UsksiDk2Z1OiMpHoPtfKJ9YD452ERNqsc06GtZPcGeYxZyUTGOvArErpra8ZAfqNhcE-sIosuMBRYyHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77172" target="_blank">📅 04:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77171" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هجوم جديد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77170" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هجوم صاروخي يدك دويلة الكويت وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77169" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17be2d7041.mp4?token=eQBDeztbILshlf9QzR6hHsSPvuerhmEFQjQc9bJX2EEcdNYb8MQfiX_49asqi0s3wtBVqZX8cXboaWIRjO9IumNJlCiJ2SRDA8ay7HafXYaF83Bor-mj2RC7DaTkW-2rrd0l2Q5sdL6M8HYazeX1CEmqLdy5RJqkbXhCXiItmw6q3DUwZA6kjLXQjrrLZU-4sXIPeBZyLrrO3CWS6TDG15HRgFkElRlf4OnLqYcaXcTIixTYwTfHfeJ8X10L0BoT7jngzLJ97ZidjPB-UTX2ogUsNdqyh4WAjFX4-S7WLLfca_zIyAg2-XHVnIoJ1_yexZG-x66ZyZCAA_S2I5AE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17be2d7041.mp4?token=eQBDeztbILshlf9QzR6hHsSPvuerhmEFQjQc9bJX2EEcdNYb8MQfiX_49asqi0s3wtBVqZX8cXboaWIRjO9IumNJlCiJ2SRDA8ay7HafXYaF83Bor-mj2RC7DaTkW-2rrd0l2Q5sdL6M8HYazeX1CEmqLdy5RJqkbXhCXiItmw6q3DUwZA6kjLXQjrrLZU-4sXIPeBZyLrrO3CWS6TDG15HRgFkElRlf4OnLqYcaXcTIixTYwTfHfeJ8X10L0BoT7jngzLJ97ZidjPB-UTX2ogUsNdqyh4WAjFX4-S7WLLfca_zIyAg2-XHVnIoJ1_yexZG-x66ZyZCAA_S2I5AE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77168" target="_blank">📅 04:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0024f3f1.mp4?token=gnS_UafaMpq82wjHo6eyNZSO-QhUoOLP9Wf5o_0fCnUJg3X2VNuw8nkTsbnrrDH_tFBOP557IGsUYmkPueWjWt-IBfRr20HdVg5I7aoPIdeS8oj8BdXRPf0eMeBNnxH0MimIoas8I5tuGAI8jY0q7mH9Cg98QvoQlUhRxVgGWn9KLBO3jlKdr0YF93wDuvZnzVqnmqq0lsXytgt_SBIrxxsH40YdKEynqZdxJ7NcfpBqY2ycW4SFwonKVml6ioARlVAO8IlRevKFBMdnGRd49Eob5Spqh8tc6vuIyWJ0LFbErIAAJeeK37fG4XViLukD0V1-YRBC79geqBpAhO3R_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0024f3f1.mp4?token=gnS_UafaMpq82wjHo6eyNZSO-QhUoOLP9Wf5o_0fCnUJg3X2VNuw8nkTsbnrrDH_tFBOP557IGsUYmkPueWjWt-IBfRr20HdVg5I7aoPIdeS8oj8BdXRPf0eMeBNnxH0MimIoas8I5tuGAI8jY0q7mH9Cg98QvoQlUhRxVgGWn9KLBO3jlKdr0YF93wDuvZnzVqnmqq0lsXytgt_SBIrxxsH40YdKEynqZdxJ7NcfpBqY2ycW4SFwonKVml6ioARlVAO8IlRevKFBMdnGRd49Eob5Spqh8tc6vuIyWJ0LFbErIAAJeeK37fG4XViLukD0V1-YRBC79geqBpAhO3R_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77167" target="_blank">📅 04:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77166" target="_blank">📅 04:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوي انفجارات عنيفة في دويلة الكويت  نتيجة لهجمات صاروخية وطيران مسير</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77165" target="_blank">📅 04:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوي انفجارات عنيفة في دويلة الكويت  نتيجة لهجمات صاروخية وطيران مسير</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77164" target="_blank">📅 04:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سماع دوي انفجارات في ميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77163" target="_blank">📅 03:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77161">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1795e9070.mp4?token=vWmqjAXKRCfPhfwZmZz6sAh2VN_0fRD76s0mofWt6CstJWNk7JVBxJVsvdVP_kuZOpwCOXiJocH7f25JcfbKvnk9NPbt9bkEXJ4a4UhTVm4QvsYEAJbnh0QJHsOKWP8Bd7FBHCYE0WCxZurIpcEUpn6xhF5XlB2mO6qmdpe_lNl1WBOTVdtkEa2iyZUt0ndibpw7qe7Aew8gKaT5OU7hS4oiA6doKkDOcNes0aS4RMDsqADF6BS9ce57MBXvcx2We5BQG0b5_c4iNKPf81gWcysddMd_PJdUnMV45IqCdLHkMPpEcPjOEmIo0HefpZxppDmWFshmU_oI29NIUvJs1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1795e9070.mp4?token=vWmqjAXKRCfPhfwZmZz6sAh2VN_0fRD76s0mofWt6CstJWNk7JVBxJVsvdVP_kuZOpwCOXiJocH7f25JcfbKvnk9NPbt9bkEXJ4a4UhTVm4QvsYEAJbnh0QJHsOKWP8Bd7FBHCYE0WCxZurIpcEUpn6xhF5XlB2mO6qmdpe_lNl1WBOTVdtkEa2iyZUt0ndibpw7qe7Aew8gKaT5OU7hS4oiA6doKkDOcNes0aS4RMDsqADF6BS9ce57MBXvcx2We5BQG0b5_c4iNKPf81gWcysddMd_PJdUnMV45IqCdLHkMPpEcPjOEmIo0HefpZxppDmWFshmU_oI29NIUvJs1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
مشاهد حصرية تحصل عليها نايا لسفينة شحن تابعة لشركة أميركية "أريستا" (Arista)، محتجزة في مضيق هرمز من قبل الحرس الثوري الإيراني، بسبب مخالفتها قوانين وتعليمات العبور في المضيق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77161" target="_blank">📅 03:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDffxcXW53P9m96WyGodBiMH_B5TXYnpFarn9zGAI8_iltTJ_oTT1_zhu5x_h6DBpT2S1H3bHZbNgtZ5lULc710EnhdWUlFMgZOJTXLm0aHPRtEtbwIaQNHkkwZ8g31yzWRfs40jF2UStO4fAtFBAt0EKyxYT3lZc8FbrLcagu1I8Dr5odLLDT0ZaXRo2MWZlDdx3uVucYn3leEwgEMgV--Agr3wSSST_J-LJLSbp2CwdRWfFfSJ846p0ZrJVogiloicb5McH2fYkLRr9qy-a6mNH7ICldjAJCvMPQ4tOslXdDoYxWEmowENCqjUpLGA7PnjeoXUeerrAqjC8K-Arg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
على الرغم من أفضل جهود الحزب الديمقراطي الكاره لأمريكا، والذي بذل قصارى جهده لتدمير الولايات المتحدة الأمريكية خلال السنوات الأربع الطويلة لإدارة ترامب، فقد وجد أكثر من 172,000 أمريكي وظائف في شهر مايو وحده! وكالعادة، قلل 100% من اقتصاديي بلومبيرغ (الذين يبدو أنهم يدخلون المراحل "النهائية" من متلازمة كراهية ترامب) من شأن اقتصادنا. على عكس نتائج انتخابات كاليفورنيا المزيفة، فإن هذه الأرقام لا تستغرق شهورًا وشهورًا "للظهور تدريجيًا" (مرروا قانون إنقاذ أمريكا!). يقولون دائمًا "أمطار أبريل تجلب أزهار مايو". حسنًا، هنا في "أكثر" دولة حرارة في العالم، في كل من أبريل ومايو، إنها تمطر وظائف!
الرئيس دونالد ج. ترامب
نمو الوظائف يضاعف توقعات السوق في مايو
التغير</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77160" target="_blank">📅 03:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=bFRzH5J8UD6UbdlJvqO-5zmeQ4zzLa18aQ1VMs9iDhTtJePMriXfeB0GV9epgN5UqlD7j7mrdlfWtksrSBHc4xDhIMq3eHorWZ60dOftNaEK3kXJctDYaOaCbT2sKq9sTNOyW2--mdRQKQGa4omgUND16MKC-mfbM9RaNtk3-7FJ4-peEWfY9aQBxGteB7zmlSwgojo8NPh39OKW_kvfQHF8Z-8S4zGzSey9ePUWMp0P2j0dS9eYfIEPGpfF6hlgvfLaEjltp7UsmA2rgtTRFZP5fB2-IdxPsjB9LVUIgA4h6l7WN1WowAs2Cq5V0nLt65WOVbxnDDHtmVaibQDTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=bFRzH5J8UD6UbdlJvqO-5zmeQ4zzLa18aQ1VMs9iDhTtJePMriXfeB0GV9epgN5UqlD7j7mrdlfWtksrSBHc4xDhIMq3eHorWZ60dOftNaEK3kXJctDYaOaCbT2sKq9sTNOyW2--mdRQKQGa4omgUND16MKC-mfbM9RaNtk3-7FJ4-peEWfY9aQBxGteB7zmlSwgojo8NPh39OKW_kvfQHF8Z-8S4zGzSey9ePUWMp0P2j0dS9eYfIEPGpfF6hlgvfLaEjltp7UsmA2rgtTRFZP5fB2-IdxPsjB9LVUIgA4h6l7WN1WowAs2Cq5V0nLt65WOVbxnDDHtmVaibQDTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
مشاهد حصرية تحصل عليها نايا لسفينة شحن تابعة لشركة أميركية "أريستا" (Arista)، محتجزة في مضيق هرمز من قبل الحرس الثوري الإيراني، بسبب مخالفتها قوانين وتعليمات العبور في المضيق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77159" target="_blank">📅 02:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77158" target="_blank">📅 02:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77157" target="_blank">📅 02:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77156" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=I_IC1frwk17a7ij6RIMak7gNERHDLHYCcgICnLKAKgM0DOt7ivf5fH9Vtaptqb_ZOYx59oD03igX1WnFTC7dGYnmRNGDsaaw1u3VT9we4jWu5Z-ssqZxDT-pnA-OC2ooX8wF7KwZil9YMPUo7h9OdhL26bLem30Akwrt40Rya50J4PVzHxmgiD4VZl30N2x1bQNVecMF90nEB6DyOK6aWNo8IgA4otJsLeDPXORtdHIAqxSpJgai7QmDwprSp2lzTs_fgS_SaXeT0sDONtY2scSsTVa1p6lAcP6n9EV6niPBXv9fPQBP5ZE-rEQAuWuwp-RUKT1fgUFEMh2YAV59BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=I_IC1frwk17a7ij6RIMak7gNERHDLHYCcgICnLKAKgM0DOt7ivf5fH9Vtaptqb_ZOYx59oD03igX1WnFTC7dGYnmRNGDsaaw1u3VT9we4jWu5Z-ssqZxDT-pnA-OC2ooX8wF7KwZil9YMPUo7h9OdhL26bLem30Akwrt40Rya50J4PVzHxmgiD4VZl30N2x1bQNVecMF90nEB6DyOK6aWNo8IgA4otJsLeDPXORtdHIAqxSpJgai7QmDwprSp2lzTs_fgS_SaXeT0sDONtY2scSsTVa1p6lAcP6n9EV6niPBXv9fPQBP5ZE-rEQAuWuwp-RUKT1fgUFEMh2YAV59BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا  معالجة طيران مسير مجهول كان يستطلع أهداف في مصفى بيجي بواسطة مدفع رشاش عيار ٢٣ ملم  .</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77155" target="_blank">📅 02:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77154" target="_blank">📅 02:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
‏
الخارجية الأميركية:
الموافقة على بيع الكويت أنظمة مضادة للمسيرات بقيمة 1.98 مليار دولار.
حتى تزيد سردية النيران الصديقة
😂</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77153" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">إعلام رسمي إيراني : الأوضاع في جزيرة خارك آمنة وهادئة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77152" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=KLFdRsPG0yLqi3PcMFmna-kXotP81wu5F2uJe_CFU6_FA2hoW-I6sDScHkMsdYZt9BgUxH8AOnnb87JnWLj5GxpClWuIhgxvTh9I6K8_0mQF1fT9kRnhUPMjzMxMfw6B9YaH29O_pyupI5j8fr3dmeT2VKfgR--3Cg788r6nZBCzX5W2F8JzbK6dErY1-ygoENLrIgxKa2oDnvFnOp83CPZXzEnzpLVZYLhVBt-DTGrKmhqANuY3pVuLiP4QMLDVCkt4bXTOn-syi7FcDPXPjftcacTuHDYWax7mDYIOcDxVQ6uqv5adL6bYXZWpBnLGQDlQPo834_JsHg3WupfqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=KLFdRsPG0yLqi3PcMFmna-kXotP81wu5F2uJe_CFU6_FA2hoW-I6sDScHkMsdYZt9BgUxH8AOnnb87JnWLj5GxpClWuIhgxvTh9I6K8_0mQF1fT9kRnhUPMjzMxMfw6B9YaH29O_pyupI5j8fr3dmeT2VKfgR--3Cg788r6nZBCzX5W2F8JzbK6dErY1-ygoENLrIgxKa2oDnvFnOp83CPZXzEnzpLVZYLhVBt-DTGrKmhqANuY3pVuLiP4QMLDVCkt4bXTOn-syi7FcDPXPjftcacTuHDYWax7mDYIOcDxVQ6uqv5adL6bYXZWpBnLGQDlQPo834_JsHg3WupfqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77151" target="_blank">📅 01:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77150" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77149" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🐦
سي ان ان:
إيران أطلقت طائرات مسيرة متعددة باتجاه مضيق هرمز؛ القوات الأمريكية اعترضت 3 على الأقل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77148" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77147" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPVeyV7WmJ59G-fnJuJOKjjeWJlRbRutIe4irCVlWZX2z_xH_zYKkCL5d_34YE0kqbJJexJyI8ouj1N076PkEq1Kkm0Up1NQToSakQVoV4KbOUHRdYweia6Caki7_na3bdcjQ6e0Z9wpLqiPqnEuogSMk4BMzPSBAND6qwQLAUChRb48lbGkY05JLnm1RP0WJhJch2S2pVDvgQ8GDG1HIYR9AAbIAKuKz2aE3XWEYHj9b6vjOxNjMJ22W3XsmVVgTv9zmuuDX28KD3pXOKQzEzjk3ya4LDxaLafomiQr1Iw58jfItE27v0WpT-fYOGxv7Edu2PQ6386tRp-A6BSOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبت يدا أبي لهب
📜
🔥
إعلام مقرب من الحزب الديمقراطي الأمريكي: بدأت يد ترامب متغيرة اللون ومتورمة اليوم على متن طائرة الرئاسة الأمريكية
✈️
🇺🇸
👀</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77146" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyQmZikOpMwUPVB3ulU00cyhC88ZZNx_w1g9It_JHmD2Ipdkx53BHr7j2Wpq4BuSpScbEtn4FHyOBqrLZq-rVkR0xFK-BYfo4ZVP0t8dX3osKRFc_kDL219b0mY3G11sUJI_PNeIgoJhWLC8HcLtFjFPNKRBoVrUHUH_DaV-Q0pLvpZ3zAt2ltYcodvwquamwB-i4O3mKa2gCW9Yywln61FSzr7HfdFGJwbfS8CsGBE0CKrZ16tB_UqqTmaol-zvhKO64ijk8bajxToXb5QnukKKxtqh3vMuXdHS2gWc0kwQeT9-6kg2053D_2Y2uk9b5U3R3XSpuNW9O01ynab5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: "مرّ إيلون بلحظة سيئة، لكنه الآن صديقي مجدداً. لقد مرّ بلحظة سيئة للغاية."</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77145" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778bb77285.mp4?token=pYn0dwVkLpfkndqg27XU-naT97WILe94ZmNU-xpimwIeuI8UzYgqoZm7vsBcPshHeI39Wca65iuqcviCFKElscOmoavoMOu75RzPn6vYDY8pOyJ0QgIf4Jpqt6o04OF22ttvijyKtrChmv_LGWy7YBjq2xObA24YCQhLb8SR7D0WodPCmhHhNI9gcCxSmLswhKytOa_7RNzIkqx81Bq41Kgv7EoQRzjXvvH3yroLefsVpSCrJGRDe1gnt6iAj4_boPArHBwZ4nm1rezdhN-189awI38ogsdv-gxS1m6j2fC7pMiP3AbhFx0Rk78fhQFDJb2ELMJ-Y0_yHMBVjdMZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778bb77285.mp4?token=pYn0dwVkLpfkndqg27XU-naT97WILe94ZmNU-xpimwIeuI8UzYgqoZm7vsBcPshHeI39Wca65iuqcviCFKElscOmoavoMOu75RzPn6vYDY8pOyJ0QgIf4Jpqt6o04OF22ttvijyKtrChmv_LGWy7YBjq2xObA24YCQhLb8SR7D0WodPCmhHhNI9gcCxSmLswhKytOa_7RNzIkqx81Bq41Kgv7EoQRzjXvvH3yroLefsVpSCrJGRDe1gnt6iAj4_boPArHBwZ4nm1rezdhN-189awI38ogsdv-gxS1m6j2fC7pMiP3AbhFx0Rk78fhQFDJb2ELMJ-Y0_yHMBVjdMZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سلطات آل خليفة في البحرين تعتقل عدداً من الأطفال من أبناء الطائفة الشيعية 1.سيد سجاد سيد فاضل الموسوي 2.سيد قاسم سيد ياسين الموسوي 3.سيد محمد سيد ياسين الموسوي 4.سيد حسن سيد ماجد سيد فاخر 5.سيد عباس سيد جعفر 6.سيد حسن سيد حيدر 7.سيد ماجد سيد هادي 8.سيد محمد…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77144" target="_blank">📅 01:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3d463c5c.mp4?token=XvfuVqF5B1eztb8UIO2vajydfYrV_if4A_2S4w307YqyR7tNq4SiigdtlxfIl0zB0nEmDdrCWddTVZHTHKE7-1t9tpqAhBZlgZXBUOh7N9ZyXyIm3UoxDkKObDMUyMSyCwX40sgUGN402hDGtjrgiiToefZ60RczZsfihW_ZHJm9G7xRPtETA_gnW28_OWVHeJhc9qVnpZQT7qc1ufcVXs-4QXUy5m7YyFjgqRNcPb8HNl31z4LIDknSQ7e9vaAo53UV503v5RrCHXFSjSj5DPrf5uOeXFpD8WEt6JOTuomf7NCT-wOBqL7nFcxHWcElsHqL_M5T8g5rU56dE-wxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3d463c5c.mp4?token=XvfuVqF5B1eztb8UIO2vajydfYrV_if4A_2S4w307YqyR7tNq4SiigdtlxfIl0zB0nEmDdrCWddTVZHTHKE7-1t9tpqAhBZlgZXBUOh7N9ZyXyIm3UoxDkKObDMUyMSyCwX40sgUGN402hDGtjrgiiToefZ60RczZsfihW_ZHJm9G7xRPtETA_gnW28_OWVHeJhc9qVnpZQT7qc1ufcVXs-4QXUy5m7YyFjgqRNcPb8HNl31z4LIDknSQ7e9vaAo53UV503v5RrCHXFSjSj5DPrf5uOeXFpD8WEt6JOTuomf7NCT-wOBqL7nFcxHWcElsHqL_M5T8g5rU56dE-wxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: "مرّ إيلون بلحظة سيئة، لكنه الآن صديقي مجدداً. لقد مرّ بلحظة سيئة للغاية."</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77143" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7a30PRV8U9utQJ6ejqd2iBMQLkTBKtjh7cyZe7SPOicttfoMtbQ18JJYZ-JWP2fYavTPXf2_yAYuj9H9S7Ooa-g2ZIXZQt4uXQQZVTpRA0po1z8cDNeyV7TfwU6arP0zike9MZ-EeuyM_c-lgKwrv8EN8XoqwaesrPOkVHX0XPm9Z5oNT94yts7i_AehSj6MD5naS_NClXbeJoFhwugJRiUM1lgxqSBf6fXDGbhU750XVxUCqk5ehRzb007MB4EGHowuMxu5Mf_GXN9-k5k9shkgXbaMzImyOptEloJPQfSw6FMpGEoHocS6VMbuR6MV5Cwp7QXJoaFTqjljlgigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77142" target="_blank">📅 01:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
‏
وزيرة الطاقة الأمريكية رايت:
إن تأمين تدفق كافٍ من النفط عبر مضيق هرمز لخفض أسعار البنزين والديزل يتطلب حلاً مع إيران.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77141" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77140" target="_blank">📅 00:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77139" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77138" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e62cbf2.mp4?token=SN2FIcidwQSHYM3Hq5ZtGCeplcPM2Y48kHrPFHGi3k1GRJ-_vqpOqYIAM7KinoCEyehiIYEMpk1B5UdYk_Cn4aK_kyyHIbV1h3n5PGfICVZcO6flG7-FFczSFGV3bJ1qGm3hjUTDOOBpw4TZtO5MZ-658TIYmxJyi1GGaqkQwYms7AP3RDkveXed5JvYGXp7s-DXUzBOYMDjW1TVoH0kScyCDdi9zzc3yI41eeiQ4R5tsnIMAM6j2u0WvGhhHH0g_oy8JwKrarzxCVExExn2B2gec9KTr-9jz932a30SZJ3FaU5nkqJAPlJxferIcK273-nFYbtM1bZjtQMmkzMFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e62cbf2.mp4?token=SN2FIcidwQSHYM3Hq5ZtGCeplcPM2Y48kHrPFHGi3k1GRJ-_vqpOqYIAM7KinoCEyehiIYEMpk1B5UdYk_Cn4aK_kyyHIbV1h3n5PGfICVZcO6flG7-FFczSFGV3bJ1qGm3hjUTDOOBpw4TZtO5MZ-658TIYmxJyi1GGaqkQwYms7AP3RDkveXed5JvYGXp7s-DXUzBOYMDjW1TVoH0kScyCDdi9zzc3yI41eeiQ4R5tsnIMAM6j2u0WvGhhHH0g_oy8JwKrarzxCVExExn2B2gec9KTr-9jz932a30SZJ3FaU5nkqJAPlJxferIcK273-nFYbtM1bZjtQMmkzMFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇮🇷
ترامب بشأن إيران: لقد أبطلنا مفعول سلاح نووي. كانت هذه الدولة ستصبح دولة قادرة على امتلاك سلاح نووي.
‏لقد انتهينا من ذلك إلى حد كبير. بطريقة أو بأخرى، فقد انتهى الأمر.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77137" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77136" target="_blank">📅 00:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77135" target="_blank">📅 00:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
مستشار الأمن القومي العراقي:
سبق وأن أعلنت إيران أن العراق مستثنى من إجراءات المرور بمضيق هرمز وأن الحديث عن دفع العراق لرسوم المرور ادعاء باطل وعارٍ من الصحة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77134" target="_blank">📅 00:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77133" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=kCMOPTc5jQRr4VKa9b8UOsQLQq7IgGbbMtdAGoNin92BzFvRCGvyE9pWD_2Nzknn6H02u811bOAvUt_jKKgFSSROT8khwywxHQqfmbbBoC_AV2By8RkjxoZw6UIrLYzNlcho9Q4C_wBFT1uo3kZI_AJXZkseB5n73G5Qbgl_jM1Dfq9onsCGroCxDsqWJ-hTpDew6d9C71TCoIWCXqXqwCWJdfkJLppmVDJxQsvlCkxvwnSXfiDcu8BNZ3GhKKNGp0xOspBSIyak-QvPMzfm07QUaSXnHZp4d7TMFBnLkT8l8_9makydPLHgd_zqxQnQdi3VLfcm_n8MqyRwp95G2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=kCMOPTc5jQRr4VKa9b8UOsQLQq7IgGbbMtdAGoNin92BzFvRCGvyE9pWD_2Nzknn6H02u811bOAvUt_jKKgFSSROT8khwywxHQqfmbbBoC_AV2By8RkjxoZw6UIrLYzNlcho9Q4C_wBFT1uo3kZI_AJXZkseB5n73G5Qbgl_jM1Dfq9onsCGroCxDsqWJ-hTpDew6d9C71TCoIWCXqXqwCWJdfkJLppmVDJxQsvlCkxvwnSXfiDcu8BNZ3GhKKNGp0xOspBSIyak-QvPMzfm07QUaSXnHZp4d7TMFBnLkT8l8_9makydPLHgd_zqxQnQdi3VLfcm_n8MqyRwp95G2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇨🇳
ناقلة نفط صينية عملاقة انتهت من تحميل 2 مليون برميل من موانئ البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77132" target="_blank">📅 00:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
🇨🇳
ناقلة نفط صينية عملاقة انتهت من تحميل 2 مليون برميل من موانئ البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77131" target="_blank">📅 23:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98fb36676.mp4?token=cwRTfjqXNUfnYTOCFgKF5I6qV07d19lOFmYDbTDXWorpj5ycDcgeIr4toE_yXgbtgjMw7-0mtkgeQCVzkopffZP5aep2V21nwU5qzy5uyL-336BSlAIYZzdwlkS_-hZvBj2gtoiyTPnd6u_lCcilPiqITFmO-__3id0WFTWYbV5YEhUVUOkZFxYPfCcW_Nje4PaUobv6qdftGe76FsdzS_XvSc8gakQBPEHIIT8hzzZGF_Fv9vt79-w8PWcU2HviYedNMoX1IENhGcy0tPumGAzj0-XUb8BeD34aGNl3mUezCQ1RstRLd9UrMPu142Km2a-1aG6h4OTaZTe2Bqcnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98fb36676.mp4?token=cwRTfjqXNUfnYTOCFgKF5I6qV07d19lOFmYDbTDXWorpj5ycDcgeIr4toE_yXgbtgjMw7-0mtkgeQCVzkopffZP5aep2V21nwU5qzy5uyL-336BSlAIYZzdwlkS_-hZvBj2gtoiyTPnd6u_lCcilPiqITFmO-__3id0WFTWYbV5YEhUVUOkZFxYPfCcW_Nje4PaUobv6qdftGe76FsdzS_XvSc8gakQBPEHIIT8hzzZGF_Fv9vt79-w8PWcU2HviYedNMoX1IENhGcy0tPumGAzj0-XUb8BeD34aGNl3mUezCQ1RstRLd9UrMPu142Km2a-1aG6h4OTaZTe2Bqcnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترمب: نبحث إمكانية إرسال أسلحة لتايوان، والحرب الايرانية ستنتهي بطريقة أو بأخرى وأسعار النفط ستنخفض إلى معدلات أقل مما كانت عليه، ونحن قريبون جدا من حل حرب روسيا وأوكرانيا وما كان ينبغي للحرب في أوكرانيا أن تندلع ولو كنت موجودا في السلطة حينها لما وقعت.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77130" target="_blank">📅 23:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
‏
ترمب
: نبحث إمكانية إرسال أسلحة لتايوان، والحرب الايرانية ستنتهي بطريقة أو بأخرى وأسعار النفط ستنخفض إلى معدلات أقل مما كانت عليه، ونحن قريبون جدا من حل حرب روسيا وأوكرانيا وما كان ينبغي للحرب في أوكرانيا أن تندلع ولو كنت موجودا في السلطة حينها لما وقعت.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77129" target="_blank">📅 23:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=oAU3cvvjcUUkEfUDiSoxCBuUz2mVUjSCLV16CwRgimimZo1JvhaLcvCdxExUFWrK3rsG6a-HtP5VcQcDEiRXxFdt0aOryg9mrxACpax9S0uAMYEuK19PGGgL9mgTr-HzwqNnvcG9ScRBIQ9MU3b4AAzBv_fwFn6bxn3QScJPKdWxB9cB-igCGrGDJ1-rJBpVX6BH32lHGUGrep1bBxMD3yE-NXJcu_UOI_7mCn4UK7ldrm-kjftl1wpnkS4Xsae6ug2fxYuyMqpWOmbTmWdbIb5dHteSR9ox4ZG3uOxhN3ByncIL5Y17boYUMax6Wj5SH_9xAOa9gdt4wN7-5pVUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=oAU3cvvjcUUkEfUDiSoxCBuUz2mVUjSCLV16CwRgimimZo1JvhaLcvCdxExUFWrK3rsG6a-HtP5VcQcDEiRXxFdt0aOryg9mrxACpax9S0uAMYEuK19PGGgL9mgTr-HzwqNnvcG9ScRBIQ9MU3b4AAzBv_fwFn6bxn3QScJPKdWxB9cB-igCGrGDJ1-rJBpVX6BH32lHGUGrep1bBxMD3yE-NXJcu_UOI_7mCn4UK7ldrm-kjftl1wpnkS4Xsae6ug2fxYuyMqpWOmbTmWdbIb5dHteSR9ox4ZG3uOxhN3ByncIL5Y17boYUMax6Wj5SH_9xAOa9gdt4wN7-5pVUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سماع دوي انفجار مجهول في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77128" target="_blank">📅 23:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
سماع دوي انفجار مجهول في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77127" target="_blank">📅 23:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
‏يغادر ترامب المكان بينما يسأله أحد الصحفيين عن آخر مرة أجرى فيها محادثات مع إيران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77126" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🌟
حزب الله أطلق صاروخ دفاع جوي تجاه مقاتلات حربية إسرائيلية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77125" target="_blank">📅 22:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
🌟
رشقة صاروخية كبيرة من حزب الله صوب الجليل الغربي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77124" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c85045ca.mp4?token=e2lXuzl5sK-zCrlryZhWbdJi892xWnVDbxZDVA7d4c6scyvYSaseGscS_1ZSj5mM6frF4T-lz-DfHeW8CRu0PnCU63btjLtJHsdP3ufu0iWB_QV7zxpTY_F8nYfRjVcUvvDh7_5mDcy4T4-hprqZbqyj5sZoySVG8iAp0ca6AQk-jfRnrDXuziHKcMK9JStpE3yUOxB8lAH6WywwiazHgrwhLKlEHcyOJfbB2ScVDKWwFtMoHtVPvhLfX5kH3q1ZidXnJtTVZnPX09hFcUGCBIEf6YIJw5rAT3a4_qVn99AxCbcO8U5n8sIEKVi7ixvjNfUZuQJl4kQFGvPmpYQJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c85045ca.mp4?token=e2lXuzl5sK-zCrlryZhWbdJi892xWnVDbxZDVA7d4c6scyvYSaseGscS_1ZSj5mM6frF4T-lz-DfHeW8CRu0PnCU63btjLtJHsdP3ufu0iWB_QV7zxpTY_F8nYfRjVcUvvDh7_5mDcy4T4-hprqZbqyj5sZoySVG8iAp0ca6AQk-jfRnrDXuziHKcMK9JStpE3yUOxB8lAH6WywwiazHgrwhLKlEHcyOJfbB2ScVDKWwFtMoHtVPvhLfX5kH3q1ZidXnJtTVZnPX09hFcUGCBIEf6YIJw5rAT3a4_qVn99AxCbcO8U5n8sIEKVi7ixvjNfUZuQJl4kQFGvPmpYQJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اندلاع اشتباكات في بيت شيمش بالأراضي المحتلة بين الحريديم والقوات الإسرائيلية، على خلفية اعتقال مطلوبين للخدمة العسكرية، ما دفع محتجين إلى اقتحام مركز الشرطة الذي يُحتجز فيه المعتقلون.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77123" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620f5f5b59.mp4?token=HEB5oUDDNVZ97zjNaJ9ZlBSelOf2xRLMeO4XO_NdfweHtw5PuB2syHfak8B-HBC0M-A4bZf-81S6P-abwEz56eWavO_KLlG2Z8sI5c4_vRzkPoC6mPpWXwI83Ex4pFPd2ud_xlS0mYPWyG9kmalFlUsV6jDLg0-xDgNdb1SlA2hVZFAE8_hB49y_eBT-yO0hkTf7SRXmnLoZTR_ZaRBJYJHxuQHVJ6PhUSGop9gyrjK9MJ1M5Ww5oldALayhWHMO2XOIg-1oPAMUAKHPMxOQsmX8RVzEXFmN1h27XmVvvmlvBDhzIPV_OS59U3QW74MbkFzZ7ceQ7N_lsitb9jCvfnWmjJIdKal0PkfUv7Yyh7Lz0OL1Qmxgo99V7LrKQ3Z0wtYX_DovOVG50ylrv4bzhflwVxDa94l7K_q1APr9Q9_SVnmEqE8uMBwHHzDanprr4A2ldBDTGJlwm3gJNpirTsOemOwUCK66Xm4INWqeyXgZ2CumVM8z5d8iuam-J0RKEEF909hnkpt55xRjY1rXLzsJWug7o3EoPvrua5mGjOks9upl15yTRWiTqrN6Wfzdny_Vw7PHPn306KbdJZgkazdoZoOLx3gyIk45zqEJBfvuWntFvHyO45zXQCOkTFZQbzMmsjFPGecqZWxcnA9sPw9KPRGviC_Tg-Jw4GVvS6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620f5f5b59.mp4?token=HEB5oUDDNVZ97zjNaJ9ZlBSelOf2xRLMeO4XO_NdfweHtw5PuB2syHfak8B-HBC0M-A4bZf-81S6P-abwEz56eWavO_KLlG2Z8sI5c4_vRzkPoC6mPpWXwI83Ex4pFPd2ud_xlS0mYPWyG9kmalFlUsV6jDLg0-xDgNdb1SlA2hVZFAE8_hB49y_eBT-yO0hkTf7SRXmnLoZTR_ZaRBJYJHxuQHVJ6PhUSGop9gyrjK9MJ1M5Ww5oldALayhWHMO2XOIg-1oPAMUAKHPMxOQsmX8RVzEXFmN1h27XmVvvmlvBDhzIPV_OS59U3QW74MbkFzZ7ceQ7N_lsitb9jCvfnWmjJIdKal0PkfUv7Yyh7Lz0OL1Qmxgo99V7LrKQ3Z0wtYX_DovOVG50ylrv4bzhflwVxDa94l7K_q1APr9Q9_SVnmEqE8uMBwHHzDanprr4A2ldBDTGJlwm3gJNpirTsOemOwUCK66Xm4INWqeyXgZ2CumVM8z5d8iuam-J0RKEEF909hnkpt55xRjY1rXLzsJWug7o3EoPvrua5mGjOks9upl15yTRWiTqrN6Wfzdny_Vw7PHPn306KbdJZgkazdoZoOLx3gyIk45zqEJBfvuWntFvHyO45zXQCOkTFZQbzMmsjFPGecqZWxcnA9sPw9KPRGviC_Tg-Jw4GVvS6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية
جرّافة (D9) تابعة لجيش العدو الإسرائيلي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77122" target="_blank">📅 22:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي: الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77121" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇹🇷
‏
خفر السواحل التركي:
مقتل شخص وإصابة 4 آخرين في هجوم على قارب صيد تركي في البحر الأسود.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77120" target="_blank">📅 22:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي:
الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77119" target="_blank">📅 22:01 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
