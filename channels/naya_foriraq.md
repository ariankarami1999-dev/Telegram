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
<img src="https://cdn4.telesco.pe/file/SMgBparfMb7SGRHNJe_3E8Ld31Z1GQ1cVxfWQUxgfgOAhkn147-WKKcPDZ0Sp2vHCpj9CLmtuFzX7ltYja5N6kU1W9_AAGAqd_DN_fu-UfwtfkH8FEEJ45-0TlUWxo464AXf7i5WMl-54kig-ubrU9HyHgguHhmTDmbDTI3_GxooAJRq1BaN66ScV_QonZrFRyGv89LnGJxxd0Cv44WSdbqA4C95TsH7mHN1GlolcNcPS32BGwWCxUtzhQBliPIIp1G_cUtXaDqIcMloMVAyc-tMHMNspWuQn_k4An2pDM9DxSzODYqF8neVt8NmWcKxMsOYnZ3vSgBuar05qWpEEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-89361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/naya_foriraq/89361" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
سنقوم بعمليات استباقية في أي مكان نشعر فيه بالتهديد.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/naya_foriraq/89360" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
ازمة وقود تضرب العاصمة العراقية بغداد وعدة محافظات اخرى.</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/89359" target="_blank">📅 15:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=h-NvMDoSGIkwLStjGm59uAe8uH3mgrQBCbn6953YyHFWlOj6drW7dBsWuQsDBwdYxUI4KQNNE4Z4mQxk5HnXtZTEYZi74CoFHymXWrZ3fdmSicEYmIeP_4MNJZV2ag5QW3hX9SCw5wjDkcj5K8bvZE4F89ipPdSi4_ZMIkk6zZb8W_pzwTdjqmQkEhH4nEJn5kgLuyTp9gQOwX4tuNWlLnBPDmD9DsLrPtyN1oDFnZ4hd5__L0Ld5vmUu1UeIYFnBAMSVxhcrzmtnU2ey2URANSUBTnjms9hqJfT3DF2wZUerFDx-S9Gj35ckUG62o5C7YMfTbgWPAkC38028EI94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=h-NvMDoSGIkwLStjGm59uAe8uH3mgrQBCbn6953YyHFWlOj6drW7dBsWuQsDBwdYxUI4KQNNE4Z4mQxk5HnXtZTEYZi74CoFHymXWrZ3fdmSicEYmIeP_4MNJZV2ag5QW3hX9SCw5wjDkcj5K8bvZE4F89ipPdSi4_ZMIkk6zZb8W_pzwTdjqmQkEhH4nEJn5kgLuyTp9gQOwX4tuNWlLnBPDmD9DsLrPtyN1oDFnZ4hd5__L0Ld5vmUu1UeIYFnBAMSVxhcrzmtnU2ey2URANSUBTnjms9hqJfT3DF2wZUerFDx-S9Gj35ckUG62o5C7YMfTbgWPAkC38028EI94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرحة كبيرة في صفوف الارهابيين التكفيريين داخل سجن رومية اللبناني بعد إقرار العفو العام داخل مجلس النواب اللبناني</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/89358" target="_blank">📅 15:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=luhLxdxb1WHmx5TTBmAVUxWAzmWjw9toWqqojtTwilq6B9gpFOHg4SPpI6c5KdNxJlGT7dkDWu2hK0YzNK-jx-v5-RWp6kGgtF2eOaDSpzqgUL6VkyleYY3TuAlxoiJePffjg9zn-8e4C0CmMJzHZXBjnhn2ggGkbJSkwuGsUAk98xbaKCxhLoO2yXqsyucLxVBYh66Ih8dxD1JCXrpc9sAHxblCTLBfGL0nzUfxsRQ1hDqXPhXHDuZt3WzXzRjKIFPETPZDtGB6c7pdQyOwyuvnxWudjQtWr8QnkwkG3dpiRTXJztuUwLVWUBGexZrj_4naXo-NFep0gy_QrWyLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=luhLxdxb1WHmx5TTBmAVUxWAzmWjw9toWqqojtTwilq6B9gpFOHg4SPpI6c5KdNxJlGT7dkDWu2hK0YzNK-jx-v5-RWp6kGgtF2eOaDSpzqgUL6VkyleYY3TuAlxoiJePffjg9zn-8e4C0CmMJzHZXBjnhn2ggGkbJSkwuGsUAk98xbaKCxhLoO2yXqsyucLxVBYh66Ih8dxD1JCXrpc9sAHxblCTLBfGL0nzUfxsRQ1hDqXPhXHDuZt3WzXzRjKIFPETPZDtGB6c7pdQyOwyuvnxWudjQtWr8QnkwkG3dpiRTXJztuUwLVWUBGexZrj_4naXo-NFep0gy_QrWyLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
سرقة صندوق تبرعات احدى جوامع مدينة الموصل شمالي العراق اثناء صلاة الجمعة وامام الجامع يناشد لارجاع الصندوق.</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/89357" target="_blank">📅 15:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=amjB0zx0mz-iNgqX3v66lTpJ9BkkIXO4B5y_fVZ5tVahHCQVXeslJDB3DPJ08q4Bj8S1AvGXnyhhe4eyS52qbTj58lUtZeT_RaDdUd0j7YuIAnfm0eLUmhwfp8Fvv-T_5emz2eeVmjWhpRflZcv1psM2u3RcSkJvJTmyj5rPYX1vwwWAS2mnzM_gm2TYsQWbN5NO1V9a2BXxP6JiglDCNX9epW45RqaVrTnaNz5IHbMrmh8hAqiQ0wJjjt5HDqFxOgkX65F6jdR06XLJmYtFbok-onbvg_ire4W5BN6ydvE_O9Zz2fSzUwHv3FHmMXcrPynugJkHX45UkXGma1NOKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=amjB0zx0mz-iNgqX3v66lTpJ9BkkIXO4B5y_fVZ5tVahHCQVXeslJDB3DPJ08q4Bj8S1AvGXnyhhe4eyS52qbTj58lUtZeT_RaDdUd0j7YuIAnfm0eLUmhwfp8Fvv-T_5emz2eeVmjWhpRflZcv1psM2u3RcSkJvJTmyj5rPYX1vwwWAS2mnzM_gm2TYsQWbN5NO1V9a2BXxP6JiglDCNX9epW45RqaVrTnaNz5IHbMrmh8hAqiQ0wJjjt5HDqFxOgkX65F6jdR06XLJmYtFbok-onbvg_ire4W5BN6ydvE_O9Zz2fSzUwHv3FHmMXcrPynugJkHX45UkXGma1NOKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد... ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/89356" target="_blank">📅 14:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
تطورات تسليم حزب العمال الكردستاني لسلاحه ومغادرته الاراضي العراقية:
جهاز الاستخبارات التركي سيتولى الإشراف على تسليم حزب العمال الكردستاني لأسلحته في العراق
المخابرات التركية ستشرف ميدانياً على إخلاء 72 موقعاً ومخبأ تابعاً لحزب العمال الكردستاني
سيتم تحديد 5 نقاط لتسليم السلاح على الحدود بين أربيل والسليمانية
بعد إخلاء المناطق من حزب العمال الكردستاني ستنتشر قوات حرس الحدود العراقية مع البيشمركة</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/89355" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
اعلام العدو:
أُوقف مواطن إسرائيلي للتحقيق لدى الشاباك والشرطة على خلفية الاشتباه بارتكاب مخالفات أمنية. وتبيّن خلال التحقيق أنه جرى تشغيل المذكور من قبل جهات استخبارات أجنبية، وأنه كان ضالعًا في نشاط تأثير أجنبي. ومع انتهاء التحقيق معه، قُدّمت بحقه لائحة اتهام وطلب لتمديد توقيفه حتى انتهاء الإجراءات القانونية، على خلفية مخالفات أمنية نُسبت إليه بسبب تشغيله من قبل جهات استخبارات أجنبية ضد "إسرائيل".
وبقية تفاصيل القضية ممنوعة حاليًا من النشر.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89354" target="_blank">📅 12:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
🇺🇸
فايننشال تايمز:
- مسؤولون أميركيون أبلغوا الوسطاء بأن واشنطن تريد فتح مضيق هرمز بالكامل بغض النظر عما تتفق عليه طهران ومسقط
- واشنطن غيرت شروطها بعدما أُبلغت بأن إيران وعُمان تحرزان تقدماً في محادثاتهما بشأن المضيق
- طهران تصر على أنها لن تعيد فتح المضيق إلا بعد رفع الحصار الأميركي وإعادة العمل بإعفاء يسمح لها ببيع النفط والسماح لها بالوصول إلى بعض أصولها المجمدة في الخارج</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/89353" target="_blank">📅 12:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwkNBqGt-BN1Br-2dYPFjduQF256ozog334xxrp0kA9zlwS7u361B-HLHwMWE7wYTwG0yysOUwcXMRY2855bewr04bEoJ_BUHgnVtUv_YbG0HgViUCdqDguChZRkmRLpagbXERzA_RtjshomWtexvZ2Cabc5p7axPXvE9ittPoB6TGQ57SGnljrvkWGmpyRM56z2GSn0St6O0wdiEReqxSy2tWJYLGkHQD8BVkf_LOXmtcWf8_Iqv-xIxmo0oLL0qbkS6mOUXNmyZt8cZrt8BkQmy-ijSWShkFhKuYBZxSndnq5bB42l5-Q-74autvE4NmNMsk8xmXGutmJNhdaVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89352" target="_blank">📅 12:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89351" target="_blank">📅 12:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
🇺🇦
بعد تهديد زلينسكي باستهداف الطيران المدني
طيران تنزانيا توقف رحلاتها لموسكو</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89350" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6J7B4sawGSsdO5NQon6KwisJx27yYitFI8u8I0ug5y6ZCan3GDrobga4lXyfgfLWfshM23Cb3U75Ptm0g-oVT0k2efckqxrqyOaBw0Z8Y9ffuB2Oy6yhsuwt022lD2fvTKVGyupujCxtc9eeEgzlp6R5M5tq2zonHrN8Ujmw72sA2lytOa5QVM-hcNjWI0AS-rdfoMPP3Mawqm-_eLlMU0WQodRsCvQs7V9a3i4CrQDrz7Gfee9fSfwCBo61ZvZcw_n0t_reuD_Y50ZHBUvM-VSiSIvZLOloAkKs4jhWhwHo9hkY-x8bwfr_XhjM6j1sj-Z_Esmb5Ls140rCo1YGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
عراقجي
يرد على وزير الخارجية الاردني:
كم من الوقت يرى وزير الخارجية الأردني أنه يتعين على إيران أن تنتظر قبل أن ترد على معتد لا يحترم سيادة العرب
وهل هو حقا غير مدرك أن المجال الجوي والأراضي والمياه العربية استخدمت في الهجمات الأمريكية الأولى التي أسفرت عن مقتل إيرانيين أبرياء ؟</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89349" target="_blank">📅 11:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=C2iS0i_51zknrZy3wLzMR5u73wDFNh5zvWWTAeP2-aoyem69S6iSvEw4JXX81713tOBeActdyGoxLKTgXBK8CsY1pZ5fPnsSFG4J5VNGgnx1ZnGMKjZb0c9QMxV6whr-ANT5_Hp36jwTEr_PuC0CUmhogrsLZYmzYnf6Cg4JS-WSfQBmUagGsPa59u7GrUyI6H6i98EDyYE36qtYj6yUCsMfd6IbY_IH7DjEp7xc9wvCLt-0NKyY1PJMJsJG-PwyTCIQPaS3nfeEYnYZOpIiBkFMEbzzfwdDMkm2gAC7fFDHjsQkA_iDkDbZs08xnA-sROe4uy3OecV3RNfD_rBEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=C2iS0i_51zknrZy3wLzMR5u73wDFNh5zvWWTAeP2-aoyem69S6iSvEw4JXX81713tOBeActdyGoxLKTgXBK8CsY1pZ5fPnsSFG4J5VNGgnx1ZnGMKjZb0c9QMxV6whr-ANT5_Hp36jwTEr_PuC0CUmhogrsLZYmzYnf6Cg4JS-WSfQBmUagGsPa59u7GrUyI6H6i98EDyYE36qtYj6yUCsMfd6IbY_IH7DjEp7xc9wvCLt-0NKyY1PJMJsJG-PwyTCIQPaS3nfeEYnYZOpIiBkFMEbzzfwdDMkm2gAC7fFDHjsQkA_iDkDbZs08xnA-sROe4uy3OecV3RNfD_rBEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد...
ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89348" target="_blank">📅 10:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
الاتحاد الأوروبي انضم رسميا لعملية المنبوذ الاقتصادي ضد إيران ونقدر موقفه القوي والمبكر.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89347" target="_blank">📅 03:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5rvLvYQNiao7RTT_Z4sQOQwL7W0ZPS3eGwf0BrBy0clI35FMiKYYcQjt5kB27KH7AGrYfKwHJH06zmV2YBJtqq3S9eAmfM5XqoucnauDesUq9ZFuDRhuZUOlA9K9Gngvc8xT01A8QJZx1GAU4SjdPhRaKYGZ13tmL_wy2JrXBtf8ojRiFo2byH3WLTy-02--t6tVvK6AOEr8Av1v_f-RZVJ8PYZM-dxaSNEgUcSiu_Sf1qyxvvUx7yolecRExOixjg7dFKvDSR8oRqZD5iMfmyvzaNJtSavdZR7-eDYUn2S5TO2AGhucPL6dCWZOZVtSbn-Q9e67cjkVdvdckC9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
لقد أصدرت المحكمة العليا في ميزوري حكمًا سخيفًا لصالح إعادة الخرائط إلى ما كانت عليه منذ زمن بعيد. هذا ما يُسمى بالتاريخ القديم! المشكلة، بحسب فقهاء القانون، ليست فقط أن الحكم كان فظيعًا وسخيفًا وغير دستوري، بل لن يكون هناك وقت كافٍ لإعادة الخريطة مع اقتراب الانتخابات في فترة وجيزة جدًا. العملية الانتخابية، كالعادة، تتعرض للتشويش في أمريكا! يجب أن تتمكن ميزوري من استخدام الخريطة التي كانت سارية قبل شهرين فقط، في الانتخابات التمهيدية.
‏هذا يوم أسود للعدالة في ميسوري! شكرًا لاهتمامكم بهذه المسألة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89346" target="_blank">📅 02:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
رصد إطلاق نار باتجاه قوات الجيش الإسرائيلي التي تعمل شرق الخط الأصفر في شمال قطاع غزة. مسلحون في غزة يخططون لتنفيذ أعمال معادية ضد قواتنا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89345" target="_blank">📅 02:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
الاطلاقات نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89344" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
اصوات طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89343" target="_blank">📅 01:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144436e58e.mp4?token=DjmdHODhEodM0Pjr6Ik6PcdY_s8UkwfGPzZqi7DvW5jJYBHv-5ZVmk8qaSQ5tJLpVCD9UGGRUDa9m9Fjm35doV-KmzjzYyekRG58XLoboxZ4tMAC72O3Stu1Ibz3Y6JXl6wZj-b3D62Og3fo97aS0DFvS_ocTurcO87GLVgpdI7-7o9W9x9_4mIwFDbNYhFK1NYL5hfLf9D3TAkIk57U-RT2krF45kKt8-mKjBxoCoho1nMUFULsfuU4szHWN3l3rtC5-Jt5shTrkc9H6K8nwX6q4OiS5Wed8SgTsD62RjKF7fSuVvOlUJN4RmXklKV9OkPyI07cg2znyVXWJFZxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144436e58e.mp4?token=DjmdHODhEodM0Pjr6Ik6PcdY_s8UkwfGPzZqi7DvW5jJYBHv-5ZVmk8qaSQ5tJLpVCD9UGGRUDa9m9Fjm35doV-KmzjzYyekRG58XLoboxZ4tMAC72O3Stu1Ibz3Y6JXl6wZj-b3D62Og3fo97aS0DFvS_ocTurcO87GLVgpdI7-7o9W9x9_4mIwFDbNYhFK1NYL5hfLf9D3TAkIk57U-RT2krF45kKt8-mKjBxoCoho1nMUFULsfuU4szHWN3l3rtC5-Jt5shTrkc9H6K8nwX6q4OiS5Wed8SgTsD62RjKF7fSuVvOlUJN4RmXklKV9OkPyI07cg2znyVXWJFZxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
اشتباكات عنيفة بين القوات اليمنية والمليشيات الموالية للسعودية في اليمن عندة جبهات محافظة الحديدة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89342" target="_blank">📅 01:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89341" target="_blank">📅 00:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/89340" target="_blank">📅 00:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89339" target="_blank">📅 00:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=p1KuHQg0ec17ct2IXRmz9rdveDvnCfMeg3VNsn51NChyLMR8qKfoP2jM_BSkmWNdUenSu7CP7uKDHWvWdFDqu4rbsR8H8VCexskxZ-pn0mLdq6uuMSeHG_9e79rp_qWIXoQArPRbQLJSdVT2ezJRz5Jj5uU0nGiFFgy11QVHkqcWXiW07Tvn1G338icp250KEsOnHYEUY0VfQhZ5jDr3g5QgqRHgvj7a4ac_4wOlMxwYG35cFEn73PqwBD_5VjVOMXFa689L5T-GC1EFmeF26HL_50wzXPJT86xKBNYv019I_C-oF_ybdnH_xOGiidk97obh4THcmzhwqRGuaQ0iLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=p1KuHQg0ec17ct2IXRmz9rdveDvnCfMeg3VNsn51NChyLMR8qKfoP2jM_BSkmWNdUenSu7CP7uKDHWvWdFDqu4rbsR8H8VCexskxZ-pn0mLdq6uuMSeHG_9e79rp_qWIXoQArPRbQLJSdVT2ezJRz5Jj5uU0nGiFFgy11QVHkqcWXiW07Tvn1G338icp250KEsOnHYEUY0VfQhZ5jDr3g5QgqRHgvj7a4ac_4wOlMxwYG35cFEn73PqwBD_5VjVOMXFa689L5T-GC1EFmeF26HL_50wzXPJT86xKBNYv019I_C-oF_ybdnH_xOGiidk97obh4THcmzhwqRGuaQ0iLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اشتباكات مسلحة مع عنصر من تنظيم داعش الارهابي في مدينة اسطنبول التركية واصابة شخص واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/89338" target="_blank">📅 00:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
الخارجية الايراني:
‏
أكدت الحكومة القطرية، في وثيقة رسمية قدمت إلى الاتحاد الدولي للاتصالات، أن الضربات الدفاعية الإيرانية ضد القوات الأمريكية المتمركزة على الأراضي القطرية "كانت موجهة نحو المنشآت العسكرية الأمريكية. [...] ولم يتم استهداف أي مناطق مدنية".
‏الاستثناء الوحيد الذي ادّعته قطر هو الهجوم على منشأة غاز في 18 مارس/آذار. لكن تجدر الإشارة إلى أن المنشآت التي استُهدفت في ذلك اليوم كانت تخدم العدوان العسكري الأمريكي على إيران.
‏يتناقض هذا بشكل صارخ مع سجل الولايات المتحدة الطويل في شن هجمات متعمدة على أهداف مدنية - المدارس والمستشفيات والأحياء السكنية وحفلات الزفاف والجسور وغيرها.
‏هناك فرق شاسع بين أمة متحضرة تعلمت أهمية الالتزام بالمبادئ الأخلاقية والإنسانية حتى في ظل الظروف الأكثر إيلاماً، وبين الحكام المتعطشين للحرب الذين لا يلتزمون بسيادة القانون أو الأخلاق في ممارسة سلطتهم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89337" target="_blank">📅 23:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامب:
كان لديهم ثلاثة مواقع، والآن ربما يكون لديهم جبل الفأس. لقد تم تدمير المواقع الثلاثة... لدينا كاميرات في كل منطقة رئيسية من المواقع الثلاثة الأولى، ولدينا أيضًا كاميرات على جبل الفأس. نحن نعرف كل من يدخل ويخرج.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89336" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامب
: لقد فعلت الصواب بشأن إيران، أريد فقط إنهاء الحرب في أوكرانيا، لم تكن المملكة المتحدة موجودة لمساعدتي.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89334" target="_blank">📅 21:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89333" target="_blank">📅 21:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857088ab20.mp4?token=STG9DNcLhr1YZYLeR36xfRowyigXGBiN1lZsjapbkondG7q6dZEPeeQ3fhmRjZws9nrzlGGKKA99MV6SzhsJg5-kyvuaTP4OiD_7OITqzthgJPd7TU9sAzErvnILivJJEvWaeSTBTldxFy8Kp6cHuCx1nTdHd_PyHUTpBG1vbZGDmxQY4ALQi3fmYH3B20Y1CJl4Bal49ZzYoBgEre8vGfK7A1KcEWjAxiVA6yTyJsbnE3MCorQlG0nSui85mYv_EPSZX_lMAbt2JHgC8Dnvtxq_aaALqsYI668cXjk5vpA6EBELIQEx505KZRuVIbwXSfIyRm5wTEAwg7GNDNuTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857088ab20.mp4?token=STG9DNcLhr1YZYLeR36xfRowyigXGBiN1lZsjapbkondG7q6dZEPeeQ3fhmRjZws9nrzlGGKKA99MV6SzhsJg5-kyvuaTP4OiD_7OITqzthgJPd7TU9sAzErvnILivJJEvWaeSTBTldxFy8Kp6cHuCx1nTdHd_PyHUTpBG1vbZGDmxQY4ALQi3fmYH3B20Y1CJl4Bal49ZzYoBgEre8vGfK7A1KcEWjAxiVA6yTyJsbnE3MCorQlG0nSui85mYv_EPSZX_lMAbt2JHgC8Dnvtxq_aaALqsYI668cXjk5vpA6EBELIQEx505KZRuVIbwXSfIyRm5wTEAwg7GNDNuTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89332" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
وكالة فارس: ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89331" target="_blank">📅 21:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNGj4YwbuDcG1oa_D3Raj49DwHk-ShhJAPdOvztiYsXvzt2EscP88pNrpP57jhVMfbAp-yD1HjtS_ezlxqMmvTEw1NEVdHtb9q-evHJ0PCTQaz_h5Vxg_GAs0EgJ9iH_gCafTqv6Qpz7SkOP3v2nt4lS9TL1UuRBoa9ad5VkiKNYVpN8-vp2GLjf_NL-DbGcvJATFpWUDHQCsKCGfFYMBXuIc4DGuKrDhsQJqEPqRoc35eb3bYOf5cIXMZ0V2HA-bO4Db7sF5dEezuBBPXre3leqhc-gL-tTYnZdXJJxk8TmKULX7yhJcdbB61UE0OveDLiMneHdHSckxLvGTj00bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
طائرة مسيرة مجهولة المصدر تحلق قبالة سواحل الجمهورية الإسلامية في إيران وبسبب التشويش تظهر كانّها داخل اجواء ايران .</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89330" target="_blank">📅 21:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
انباء متداولة عن إطلاقات من ايران نحو المصالح الاميركية في المنطقة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89329" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
قال ترامب إنه سيطلب من الدول الأوروبية تعويض الولايات المتحدة عن المساعدات العسكرية والذخائر التي سبق إرسالها إلى أوكرانيا، في حين بدا أنه يشير إلى وقف المزيد من المبيعات للدول الحليفة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89328" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇦
زيلينسكي
: روسيا أحرقت مصنعًا لشركة "كوكا كولا" - وهي إشارة واضحة إلى أمريكا
😫</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89327" target="_blank">📅 20:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki6xr_0KOfEZ2Qx9WdavOVDK9_8cIe9OM6Pe8m6sHE734Aev5Dg5AK2szLg9vjep3ix-sClLS87tkFOpKC981K3JVmg2TSHe1Vy3TXrSYWCRPhKX3bCA0OL7dOGmkVLOF3HyNXmSXXIAwTr9OnebFOePy8DVS7AdyGO9Ge21hKn08RDKOYwpYaZLeDhUdwJAAYSNzyPj2R2P7boyvLPnIs84VLW2lBjXni6LsjjOgxYm3zUj1-YpKFcpSwsGPUvr3ZGmcaBvcfrkPhPAqj_ouljo-yTXlw-ibvCDtGZrfHsjRSGwR5bbb_Pt_15XQheAvmdZ8FphtpIKK0fCIps0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
قاليباف
: ابذل جهدًا أكبر يا بطل. كأن مستقبلك المهني يعتمد على ذلك (لأنه كذلك بالفعل). أو استنزف مواردك إلى ما دون مستوى الخطر وشاهد كهوفك تنهار (مع مستقبلك المهني). أو صلِّ لآلهة الملح في برايان ماوند.
‏العالم لديه بالفعل ما يكفيه من الفشار</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89325" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية:
وجهنا بتخفيض أسعار الإنترنت المزود لدوائر الدولة كافة بنسبة تخفيض 40% (السعات ثابتة والسعر منخفض -40%).
كما وجهنا بزيادة سرعات إنترنت الأبراج المزود للمواطنين في المناطق التي لم تُغطَّ بخدمة الكيبل الضوئي وبنسبة زيادة قدرها 40% (السعر ثابت والسعات مرتفعة +40%)، وتلتزم الشركات المزودة للإنترنت بسياسة الوزارة المتضمنة باقتين فقط (باقتين لاشتراكات الأبراج واربع باقات لاشتراكات الكيبل).</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89324" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADOrXP_CBzOxWCNEsuTK7jkyhZyAgovpcvbPZh3Y80yc5AU4xdDqkZ2bgiBRxeKgwZq-G38Ig9YCPkKDsvOuAx-YzkYA51Bctp9uamuVZpAHofElYe1Zdm3Uj0wIJIFwjqmBW_S66Vg30ZRmEmmWX_Glm_uAeIk54lmqnM8tELsrg9mn5Iij97FepgIkPmeEUX73Xg5wk4Xo68_yN6Xj1ENHw6WKXCVWP5pU_V1IUFSGbogt9LE139rXXbEp_LSNN_HWJ4TZ1LCScDLWi9BiLbsKuuH_eWC109PI2uZFF21bXNzPQikMUKr4CNg_xwAbWCM0yO4utzC8US3n-mPLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
الولايلت المتحدة تضع مكافأة لمن يدلي بالمعلومات عن قائد قيادة العمليات السيبرانية التابعة للحرس الثوري الإسلامي، لاستهدافه البنية التحتية الحيوية للولايات المتحدة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89323" target="_blank">📅 20:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=rKgfavcr6NRKlxbn83Kgjg89Xxx_fHYWEFPGDUmb5zPaww9HVG-RKWrrTJ5YfgsiTOLWZGcS8ziJZ_ENHJn7EafCgq7acjiBk7wZlStWXuYC_Eax6m7SCYSHIYE7-uFAW5koab2Z6K8bGyXlm-DTC9fDhsDa9whYQPoQKZVC4dxrEOfrKzOUJfqWjCraAoi3i0_uaLCdvilmb4Bf_AB7CotGugiZLxqdB2o5HYGNGxopP9vWzGHQV7kgQ1cJlSzlLiU6RQhxYGEAqurnCV551n92XchdOqetub7-DKfe4oeVWwZYBlHazAKzlqOLx7_h0vE4Rs64nLy03lAo0xKodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=rKgfavcr6NRKlxbn83Kgjg89Xxx_fHYWEFPGDUmb5zPaww9HVG-RKWrrTJ5YfgsiTOLWZGcS8ziJZ_ENHJn7EafCgq7acjiBk7wZlStWXuYC_Eax6m7SCYSHIYE7-uFAW5koab2Z6K8bGyXlm-DTC9fDhsDa9whYQPoQKZVC4dxrEOfrKzOUJfqWjCraAoi3i0_uaLCdvilmb4Bf_AB7CotGugiZLxqdB2o5HYGNGxopP9vWzGHQV7kgQ1cJlSzlLiU6RQhxYGEAqurnCV551n92XchdOqetub7-DKfe4oeVWwZYBlHazAKzlqOLx7_h0vE4Rs64nLy03lAo0xKodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
في خبر معتاد...
الاحتلال الصهيوني يشن غارة جوية على العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89322" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
‏
نتن ياهو للمرة المليار:
نحن على ثقة بقدرتنا على إسقاط النظام الإيراني. هذه هي المهمة الأساسية، وهي وشيكة التنفيذ.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89321" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89320" target="_blank">📅 19:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq7_CMZJQO3uxdAP5Z0wgpTVb4S9mM6v4MuOljxWWRI83X4ccvTc_mnaRbYE4qlrMCdBhwvNFu2ZG8d3m5HLzxrC5aRVotSW3uBmIXMVybeov_T2fyzkD6phReS105HKSDi1nGCYkz5CLQFspJ8tUR-SE1XYjozD9Cn8vCHo2ANTlkq6NFjqU9CVaiZ6sGmbVcNlWPtqWbACIeyHCSHm3hh-XhRo1mb3PJRBI2Zbpfdy2K6YgjkdHS7HB1HQv9y22TktV0BIdR1btcIUD-o0e7WykpTWHuBDo5Mp9MqMmonPvrhNSIW781fLBtit7gcGzB0kRvHm6J-hYn9hLEL2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهدد كندا:
من الجيد جدًا للسياسيين الكنديين مثل رئيس الوزراء كارني أن يجعلوا الرئيس دونالد ج. ترامب "عدوًا"، إلى أن ينهار اقتصادهم، وعندها سيثبت أنه سيء ​​للغاية للسياسة، أسوأ من أي شيء حدث لسياسي كندي على الإطلاق. ترقبوا فقط!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89319" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">توقف ادوات الذكاء الاصطناعي Claude وGrok ايضا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89318" target="_blank">📅 18:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89317">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQjhoj8ilathf-6uT3RzWqh3JZ8P1uVvSxdZtTqabTiTBLZPjdi96ghgnnDbeS5j8tHUBJt698jEVx0ycTYgfrJHbIjxI8PZTS70GTWKDVCJJFXPeQLMH_ZRTClwJIg68U3u6MfdYkgWBL_fMZJUyHNW7jd0NUv8TKtaDoMZCiyDO_dnfN9nphonres30y5ryrTmJEHUYM4Dq-D6u9bw1svHDXttEN2ymqFjafaCvDpXE3gzrXK6dE27WlURvXBxRxfGELHuJ6OTeS6SLLfWg1SzD7oZmQwdwHi4qKcENhlLh6fOd17h8Xl728JAuPV_WqizOAVLu_4JtxZqZA4oGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
بالنسبة للخونة الأوغاد الذين يرفضون الإبلاغ بدقة عن عمليتنا العسكرية في إيران، لدينا كميات غير محدودة تقريبًا من الذخيرة متوسطة إلى عالية الجودة، أكثر بكثير مما يمكننا استخدامه في هذه الحرب، أو في أي حرب أخرى (وهو أمر مستبعد للغاية!)، والتي قد تندلع بشكل غير محتمل. بالإضافة إلى ذلك، فإننا ننتج الذخائر بمستويات لم نشهدها من قبل. نحن نخزنها ونستعد لأي طارئ قد يحدث. نحن نأخذها لأنفسنا، الولايات المتحدة الأمريكية، بدلاً من بيعها للآخرين، لكن المبيعات للحلفاء ستبدأ قريبًا مرة أخرى. أيضًا، يرجى العلم أن إدارة بايدن قدمت ذخائر لأوكرانيا أكثر بكثير، دون أي تكلفة عليها على الإطلاق، مما استخدمناه في إيران. تم منح مئات المليارات من الدولارات لأوكرانيا وحلف شمال الأطلسي مجانًا، والتي كانت أوروبا ستدفع ثمنها لو طُلب منها ذلك، لكننا سنطلب تلك الأموال، وإن كان ذلك متأخرًا بعض الشيء!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89317" target="_blank">📅 18:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89316">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1wRH7r5no22iXPh9oCe1AvCOwYvKylijCgK9yeE9M1x4VOBnzotf2Ue_R3AW3ValZui24TeeZ6lyKn_KRtbxmwPa1oPD0boUiibJkvWkd6FjqPB1vqyGYSrs3SKWj5cT75kDcCU4huXTJLka90cw2TH3qHSH-rO5PNSx-XvHYoR_ZB26i9rgTEW4XyGwyVK17GantnN_38VDwCH7BK8b1hLtMfWlsTBVYTZ7CGOLZoeIH8ipH8KuRboHte2_mq9scITDYi1UlZgJtsUigEAqkAMJi64OM7NGmZk1wcVlNPO-cto-PhBRCVsm2qiMCYwAfbGexb7XF7ZMvS4yJjvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89316" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89315">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1BACuxeYfFmpUmjC7T0lqh-QFhWplIjIaNG0vVs2bbFbg8_q1ZhQBLP83WkdHxoPNqd0gJ8RgJCCSyqg_zAjCBXRRczq86rhYZPPQoT8LC7vDvueIvu5zHsCrvlWJ6_cFeVMb2p-nbOd2jCj3hE4gt_kuxIxYCs0gCJ1UxIBXhMs1QQeZMBrzPokDqyZmBKPJoe80iPE1phYi393m2IX7iQMnso1la_TQdv-YW2uupj1Vh57g9hWcmT-TuV_S1Ed6AN-uXAjs5J3OfQUD-wNGrq168SmstZ82HTEt0gd2Ril9wpt7j8n1dJ8jRNUI5UoxnhhiSkoQSIyISJh5nJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
إنّ الأشخاص ووسائل الإعلام الذين يصرّون على حقيقة أننا لا نملك ذخيرة (وهم مخطئون تمامًا!)، هم في الواقع خونة. يفعلون ذلك لأنهم يفضّلون أن تخسر الولايات المتحدة حربًا ننتصر فيها بسهولة، على أن يروني أنتصر!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89315" target="_blank">📅 18:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89314">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89314" target="_blank">📅 18:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89313">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
وكالة فارس:
ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89313" target="_blank">📅 18:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89312">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
ارتفاع صادرات العراق من النفط الخام إلى 2.340 مليون برميل يوميا وهو ما يعادل 71% من الصادرات النفطية قبل اغلاق المضيق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89312" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89311">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwOgLRwBPB6JvwsEHItkGVHVXPGvFXR3dxqYqQARoD8i4WRlV-bVu8_5CPrvyyAp54r3iGzyYMKNiSZN2Vd4NLEOD13M7xNJHCrJrFomoC1H2PC8u844l5xox9fczjTY40eSGfRf4Y3MnZ8IpYvzqo56vJUoIiN-1vGCMCLx7jzhvyFzMREND3LyojQxcRWdoedHwGGeSuhZ2spKKPiX0Jqk2_PF_fvWtEEv2utNytfLuPKJOYAPS7ptL_b0Yqst3ypvVNz2Qo0or4wwmPc9MKaqaGbplivmrSC3i91LESQvNipXOoddZYAq3LX1_SIEi0XpVMlEE3mchMNRSRQBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارحلوا أيها الجبناء
تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89311" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89310">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام العدو يقول ان السلطة اللبنانية سلمت الكيان خرائط وصورا لمقابر ومواقع أخرى يحتمل أن تكون فيها أدلة أو رفات لجنود صهاينة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89310" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89309">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇨🇳
🇷🇺
بعد طلب وزير الخزانة الامريكي من العالم يوم امس بالابتعاد عن روسيا..
وكالة شينخوا الصينية الرسمية:
الصين تعمق التعاون الاستثماري مع روسيا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89309" target="_blank">📅 17:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏نظام ال سعود يعلن تقديم دعم مالي لمرتزقته في اليمن ويؤكد ارساله لما يسمى بـ"البنك المركزي اليمني".</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89308" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9vmE0Pv1ajtexsVzR91N6KrnIF96_t4zBRbyTGcY-f3iTYmI0CDvQTMW_XkKFM_fQ4rV5Z8_ztFdL_NiB-QklrNfqRVJ97An0x77zdQ4melMnYbjD9T8eFoSxtql23ilnTynFcTJoyauOOgMxZ31Fhg83AwRmAuMU3VKm6YyDZCBM2IVevusp9lPwZsxajaV6SitXP_jK1M2itKfTg2Egpl7INv070epWsP-Gk7AQJxMzUiI24d_cC301NSOaUdqdDbwjr7ARZRwnvMcsBOxBdQso6OQTt_u4oDXWGaMa_WNkBegLSzUQYaFYBe_TrM7YkkWbqk5mDjop14kuKYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القائد العام لحرس الثورة:
لن يضيع دم شهداء كوهستاك المظلومين، وسيُحاسب مرتكبو هذه الجريمة وقادتها. سيحمي الحرس الثوري والقوات المسلحة الأخرى حرمة دماء شهداء كوهستاك وشهداء سيادة إيران الإسلامية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89307" target="_blank">📅 16:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89306" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnB49ZWdQ4YhztgjaqlTm_9FfRnxAbPh2sKxAUqdcVO5Ne00uQg6neEfn57skP0TNMZS0_w-ZV5xMwa86rFAi6E3Vkf7WkrcwsgjJz-zHGaWR9FiriSKtrnbVQrKvimaVtC--Rm0Pw0aikrmVd_9RmiV6jiwf5pZDm7KYvJf-qZgAby5timtxEUpHOqBbSSmNbrzHlXz6OVfvbXUecvARuL_9njmFY39nBzNckoupvc30zH0r3EI-Xm5dWEb_5hP9sTTnBhigBP-TAh61lnTkIE5rrHkOBdY02eC0UaKmU1AoQj293tNCXN-8GOVvRKwMVKZtjZwfEc7IWVzfoUAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USwRVm6Vlv977uB8rsTGtx2RWV6hhfIjymxmFgYewgrBUnCds5OE_gDaTu9EFKTxplka1u05n6oSiqpZD20ccWI9epcH4ByjZiWUAG4GnP5wm3Q-o3Jy9q7kRSimJhqqMd6GAHEY13XL2Ly85oKj52v41XLQ2NOxtddkJNtLjb-HjVhYuIZD5LLH3DaqbQN-cj0_r5L_3OzbacHDPIHP4ZSep5eSKL9PRKw1LQQfqgSvR7nR8-cPaSwu1fT5kJWR3b5FPN5y1ztZNTi_BTvwfxQzK15T60SLdRbkGA1M278DlBMrVkFHBu-1HZMHcqIcG7v-OAdQnZ6CQrx1r8hgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBIPD4aMjzPbkmq2q-f1sJugQ-Hx3pIzlq6eNUiOM5v0GJsHvETejSNKeqSna8_xPnknHNxs_K52a1byR2nEo1AxqUWdIW26DykIKEp8orXiQfDORRdpkyrSND-UayFUN1P2m5jHCPXvn8Yrk_w78SSdpgEsnWVqW6qTqGR0XDxT6bjo-UjuMhrDEKNBqlfNAleN9wHuYIu19WMu_qqBmJlAWjFyP1cZGgkoBfouo8p5vPrYdimB2zoAaXjYOA6-OToKz3wLEPJMkgBOVKkKSKfqZ6aQ1drVJctEuq4zpe0USEhmCVrAECEP1HtJotPS4C58ayDQnQl2xa6cJ7ZL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3FemoPd3cGHxLZy01ZHRY6qPU_5qcnrWpac63Uep5bp53K4ayElNk42nwjd96_wDfHgMJMOaZS6Fw8eYh5reYUv3bdn8kO9XYvejzhYnnGNKAchlaRyB3Jcr_dVVoMd8gh8WgZm40Q_NOm31d3XaFsP_7OOrrgSyO_vRWrjua2wdvqTYtebOQtrJG1emWraAf4IADC4Uf5i9z7AkCiY7KXgRXu7KqWxDeWGJW1iet2T8yYEHbwvfPkqlFr0M6ws_DZ4WS2i3Yk3LPVLcFnm9i-malq0CycxQ4qJWV_bBz4rzTlo5x7C9uYdVpR7_JmQVIKuwy3RnwNhPDqeBNHmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhQR5ITrhqmVnq8oLIa8yBsVCftHmCJyh0JZXHHCOJs_XyNhCeTxU50jdHYZB5bi52zQn-XtXr7xZTgPdJZg0VYXHYRqi36V0hQdFUMaezCc3CK176rCpN2Z8fmbDX84ilZx2D1AqFd-uFpHUdd7d4ufpBoosSOQzC4wMUYnwKkjHayRsMTKUGU4SclszC_sHcrihDe6GNRfUMUfYrJ0RwNdIVcTO5dOPdkyiTyMN-YtUjNHoqpaHWGNjSrfJScrXyuZa_v0zLxnxcyGWSPDx0etGVwicgPKhLnATnlgTOw3Nw-kHvoegF7ikE1pyZLdWAI0fzIjacWJ0dHjJY5-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg0NPw93JrBpKZXQerzY0HdFii11i5cnAsDeE39bQ8oVmpXa4yZCE42rK30T7xfJr5vixGCl-vO3VCWR8NgoXzPHOeBasFGdTZvl0XtU7XscE6fqjYs5l0kEYzUGT_QvKvX5PnMtznn1nF4UuQqsh-UWQbuFiTwRO2byg7-GhE5pcD5UfoGl0PTvfQhA6h94rkod3zJRDduPvPA7Lb_CDI_DJJk4zbR4IhZrL8kT8VSnQRbvFXoFBD7cr2S3ch2WzT7all4FQSuYcVaq4qC-3AtjtevgKDATXK6ADuRkXLRmBzZH9nmimakEmFQe35FLt80H-vG_4wrz9wqVt49r5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knf1ZUNfNg7RBF8qVdmGtmxy3GDbWuop3RLHjmvs8heiFLo0HdQMvw-UR7U6lEUCdPNd4HNEWHp_XGqiS8DthK-OxnpMDM6S42ALMbUMSSpAit-CjbQ0IS-69txDAm2FroHuZ9bL0etSEk7t1H9uRupDQ2b6tAin9O8AEpzEHsN0nkVZlicxvTglvxBhOZmSULxOF82aNlXA8GyxjHMKIGZxmThDxBMh3J2aDmkTRFaUfHiRDDNpxi_z4maUvydn1a-eVm0I9-qJSs6ad8Fni_cwtgKdcbrwc6t93OIjdErfRz9d8x_4rSKjfjt7h1k7Gnp2UFgpmf3yPEjSuKZr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eq-QCNeStebouz5ssnYR12GEluuJZ2V9iK9ASuBqVIa2KyWvDqfPEVtKUL0eblKNZuYWF2Qm7_2RvriJDGa1aFczlOr4yhGuuVy-3UrpeOTWmbfz1OfYevjCsj2bul6dSumKp3O0EQYt8TKg-FV7U196YcrfmtFZB4xSrQkd-XHXTv5SFnc76chcp1hZl03bXHEeVczsPHHhUuGGFAvXyLoamvMzL_w73Y55cSCR-H29J1u6riNLjAGNd3X3KswbNDdhWqZdyuk-R6DA4G_vvb0f2ifvN8E-PqCK3-EgqqZNVLsfm0QAjtP1kuuYu_YtVVC7sM0_H7SkDnTj0Iu_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9KlupMSBNuCD31kHdweK2vysaFOvJVpQHw8oaZaTNWebt_cIZmLKoaweHU9giMfkt-SXRpmX4T-Xyla3oNJdSe7Iy1oVHZtDrIFdCFFgfAZ_idUuGj1RvTHE3rQAh5NjMORcih-ohLu8D1a8uv4pIG-0JHovP62kiTOZemjSc0LJ72uJteS7xxBYo17mrwENlRzsu-EOvFqan18iz9AtqsHA1GDB2VW_abCvidmp_rH9bZxF6PsTmFpjwaG8_8yC1MdWEvyXRj4bmqLbe0islXvQgXVRZ0pxmqdShzjigxr_gxK7y2Noit_N281BpacdY4_4ksyzKsXoLRAw4mK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkEerhn6uxxh10jIccdke2ohf4LbdOh4-X-Eer4EAZ2TwNVVWs_noSJSOfuhY2BKfTjWIlnsBhEXt-liuPivvIXajuxU2-GH8hpk863-e1q3H05ZDbJlqIb8DYjja452SaVCIKUigK1qkC7lJUS0uIs83igMLZHhfYStXQsXL9rd9va15QaIp0uLBBKLHLsVexZg3Ab2zkXKet1JPEfJeDmnmT5jNMyPK3wCTveCtk7c7Rs4v3eNwj1pm1OAS8MFcbnrhmVY8YzuFVMXsC0bSqNvgs69wnYY1EFizfyJdrTOlSDMwg5pgmY2fA9bIHRajtf2zLn399P2zNzAi9LpHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
صور من مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89296" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c54e19f0f.mp4?token=mNfiZNSINwc8aFWFkn582XKRY7x0r3nwEl_zdzbnriFGG59UYK6IcJLGFY9uQ9-c8vHJXbR603lFQuUNPtF8yvg3k8tX9YJTeI3WnTX5_inQCSTxsIs3vpJuajVcnq_kPDXzvRSNi85jkgpfb1CSJSGRGOJ8MqfzEQpVEMDDmeyFR-g2ZgMyb155-Ws_1al1dPs02ugOYRjffkPs6ou2fveErFGqG20LHjykq_jZOUMvRugpX_6BkXR-a_GQ9qnB2RUV1-65wLgZG8NV6NXd1I2qCC5m8A-_ErtuIAPJBUtG0kJZ_9l0xddIn07xA7gMMuKTR3hq7bHOvCNMv3nVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c54e19f0f.mp4?token=mNfiZNSINwc8aFWFkn582XKRY7x0r3nwEl_zdzbnriFGG59UYK6IcJLGFY9uQ9-c8vHJXbR603lFQuUNPtF8yvg3k8tX9YJTeI3WnTX5_inQCSTxsIs3vpJuajVcnq_kPDXzvRSNi85jkgpfb1CSJSGRGOJ8MqfzEQpVEMDDmeyFR-g2ZgMyb155-Ws_1al1dPs02ugOYRjffkPs6ou2fveErFGqG20LHjykq_jZOUMvRugpX_6BkXR-a_GQ9qnB2RUV1-65wLgZG8NV6NXd1I2qCC5m8A-_ErtuIAPJBUtG0kJZ_9l0xddIn07xA7gMMuKTR3hq7bHOvCNMv3nVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
قوات انصار الله تسيطر على مواقع تابعة لمرتزقة السعودية في جبهات الكدحة بمديرية المعافر والطوير والأحطوب والكويحة بمديرية جبل حبشي وصولا إلى جبل غباري بمديرية الوازعية والعقمة بمديرية موزع مع استمرار المواجهات الضارية وسقوط عدد كبير من القتلى والجرحى في…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89295" target="_blank">📅 16:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇾🇪
قوات انصار الله تسيطر على مواقع تابعة لمرتزقة السعودية في جبهات الكدحة بمديرية المعافر والطوير والأحطوب والكويحة بمديرية جبل حبشي وصولا إلى جبل غباري بمديرية الوازعية والعقمة بمديرية موزع مع استمرار المواجهات الضارية وسقوط عدد كبير من القتلى والجرحى في صفوف المرتزقة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89294" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1y6y9j26ldEHCv34IFPiO10uGrY23zN8Fq0ZE7jL8JwgHeFrxuSakeaRQtIgpVYro2hXOs1xLpGFEH0bjuppYLewtBhnAYAxOiLFroU5BD15zw23K6pHUBNpDVvDOkPyMLAwaRwTvayIgwgOYkdHoWNlYuhs4paJKK6KnRkhVW5YjL9miA-owcikATG-AplOhV0NpBUAOevc-GLd-oTrKfVXWAj1Dh1omMBgxDmv5QuZ-rDI9BYypLLjtf3lTozQX2hf6KZJz0AwhxqOOYL7YMj57bHigokI2I1jwa_mO91DYdnXv0oK7luVU61FWYDaWrwzkYPkIBP7WDM90ADrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
استشهاد 6 من عناصر القوات البحرية الايرانية التابعة للجيش في هجوم إرهابي امريكي على جنوب البلاد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89293" target="_blank">📅 15:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQplslJROc2mNCAvo8clzjcsiuirjeQjb8WrPmeCRBYJfPKBfLvOofU97lDkX0GZ_vqccPVRCw59G2hoV5xC7LSqAGOy5L49rLbjCE7A-mPhLSltqbLd00nNWV74HZfeMpVYE_cCeMTXZ2Z6j3L-NsM93iy-TvMG-WmJe1nRwOxZJyTqD3IKwRoMyDZPYMdk2D-NVG49Dm4WFT5auWzpSoFr5xL6WYTkU_J0Bp-oardiOiyZJUHb0meYyU1JNqOStOvU3ffShEJLtIJuNWeYF6mSYKjmR7Z3by8cpXbRoXCV25dyTBiRM92PKo16BZ4qpt_34epAluY_GRrCbA4akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5Fm5g3bpz0l2NNM6jCGxm5NhFHt_8JMZpAMW9dXLo7CFT3EZT8gl4CRw16mMAL-F60_mgyTa7YLHvXaFX42rO8p_QTf6XSoXgejoCpknGeW6GguLQq06VKl_M9zPK49zw5jeRuygcv80eGwcR0Jp6NllX2O52kiid5k2FhauSIKYx0GCj0Pty5pmrXWs50s1dlIKm5VOtfvajWwPzZtIG2ymKOmvIh-cRmdBALeidOmQbPADUFzGdm7GE4VSJLFFGaMgfw3Q4if8uAYT_2wAIcGywJWABelF1eRM7uT46vq9llnPjDbrGAVSb4FLLVaFCIKuzdClhmCXCoAzcMhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c92u0gagrqPrIZe6cIeZRwnlHDL_5Ti5guBWSBoMS-3z4SifOSwHItekQIqyuluy6bP8AVPG2TT8Zcb_nj0sD3QRjh3HcazOBjPWJbFKIHqsDgbcvYNVDxmabfrNCG-9MPWrz_GAKgOxcwwCRMOy0zQGz1yJniq4ySnCmd1GLIKk7a6V-n7-T52U3tpd7_DRo6hLxWIW07CHMtOiSq_MxbxTSEsCIt6PsrZIDA5RZ3BN-rqlCz9k_NGl8bVWTJwG2j-JD6lnRBv2xUfSgyWDb8K7GF6uA0KW04imCXB-27MgKx-cVAp2fK3fC6E-I45_7q5o4YMLaixWWyfaCyS7Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
🇰🇼
‏دويلة الكويت تدرج الهجمات الإيرانية على القواعد الامريكية ضمن المناهج الدراسية الجديدة وتبدا بتعليم الاطفال انها اعتداءات ايرانية على الكويت.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89290" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPNeG_uQb3F43Sdt9wjQeO6dDPhS3GjapZfOJ241t0IyII0fAwzCt_DH3rJ6airfDWvnjkhgKVbB5LaqzgkaTTxUoyqgcfeDTI0EV_sqU2-b6G5gv2pzHA2AqMpVMZkOSvx9YY1oFi5DDEFbTbHlxqLh2R8h25eTr22PWK39TMerT0vrY5TNFYb2GcQYgvGK8u-Z5S-ESKRi6GYMPfoVFWVCDjsth_KJoNE3yWHxlmbTPI0empNTy50m8q5IDL2qSdDH2cdf08xg7Rth2LLClwnj28j38oUydoVuDrd5KSFTJkWnh-fIJ-e3QtsRlJ-nvGmE4VIo7Ijugjc7o0WGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeafvQVIBYjQXEWMVVPnbjyzT-SHZzO5WaAekfKWMJuRFXK6XcvQx8psvm37jYLhuhL3Qwn-iUBBORBT1kr8oOszpThqX2SHqY5H8DcpbuAutb8EWgfOmNwzgcPuairG7L3Xl_-Zrc5p0F9a0Cet73QEWIq1KEs_Ud-IV1D-2LunLVCmgZYp-uixouZnYhfV8k9D2e_krWBWFp20I_GrvfZuCJcunNXuJ4QotY3PrfWbRhg7S3lGb9qPHIm67JAKkxCtfkiF1OoxobJfenNAgLluyMvyZUJbeOW7o-4dwvVwL56Vo7t-rAv75V4_fRIZ2iplZY2ymwY6BMFAd9AdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJC0VZKG6kVrOhMi2tiQDWdK9euhV6MWp3NWhisIddii86vdPLzDkNl318He6Te6L5X6Ty1F3BBXuBG5fTq8sp3Pz_NHpp_26eLrV9JYUvQZlbZPK2WJyRYB44sO-Jcc4grkDClefKrsbd2DtKFuGoOh-HK8Mz5hnrCCdTH856Eh1490_FNnsADsJpONf6lMZf7ySv1pMogng7Uz5vZ3X6BWjonuDo72koCDIDvMM3NlP6MN3oRxPap_0hw9wMAQVnPmTFv3tzEwq4f3MidL_jHg839Jj7cPkbFZrJtzaETBLx83VLBgAfcM-pkUVshXs0LDnBZ3W47zwrDd0bmsfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
استشهاد 3 طيارين من الجيش في هجوم أمريكي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89287" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
🇺🇸
🇮🇶
الحكم على ثلاثة مجاهدين بالسجن لمدة ١٥ عام بعد هجومهم على القاعدة الفرنسية في محافظة كركوك بصواريخ الكاتيوشا اثناء حرب الجمهورية الإسلامية في ايران ضد الولايات المتحدة الأمريكية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89286" target="_blank">📅 13:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS1kmMYrWee8jhZideACcj3yr-HFFtpKVKCqnr8sYXFiWjE5kvCT48h6xNecICJLE0g5s9zBMZA2q6JflOaLqbR-ksvL3Pvl7NsgsK8ATNe_JrkukW9Yqc7Nhe3E_3BSbHCP2QZx8zdSRk8OuuRk4AzOG6UklZrn6Dgy7uXXpF3CC34YnvSRAQU2OFcFrl_Z4SNs_rmTtGdDF9WbDZUll_S4ud3nDmzs3rAeznxodnXDNthyHbic_xvTXysqux8aC2mYdk3Ea49u-LfFdt1ywHgDBpVeaxMi_ivNM21GT0tMI6yz04KyrT9Chea_j-_x83OGkywNEj_hoqgHqbkuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇸
وفد قيادي من حركة المقاومة الإسلامية حماس يجري زيارة إلى الجمهورية الإسلامية التقى خلالها بكبار المسؤولين الإيرانيين وقدم الوفد شرحا مفصلا لما توصلت إليه الحركة مع الوسطاء وممثلي مجلس السلام من اتفاق على خارطة الطريق لتنفيذ المرحلة الثانية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89285" target="_blank">📅 13:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية جديدة لاستهداف تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89284" target="_blank">📅 13:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن تستهدف تعز بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89283" target="_blank">📅 13:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔵
🇷🇺
بولندا تستدعي سفير روسيا في وارشو.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89282" target="_blank">📅 12:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇷🇺
🔵
هل انتقلت الحرب إلى ألمانيا ؟!  ألمانيا تستحق "ضربة مباشرة تستهدف جميع مصانع الأسلحة الألمانية التي تزود العصابات البنديرية "، هذا ما صرح به نائب رئيس مجلس الأمن الروسي، دميتري ميدفيديف، في تعليقه على اتهامات برلين لموسكو بـ هجوم على مطار لايبزيغ.
🇷🇺
…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89281" target="_blank">📅 12:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن تستهدف تعز بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89280" target="_blank">📅 12:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇷🇺
🔵
هل انتقلت الحرب إلى ألمانيا ؟!  ألمانيا تستحق "ضربة مباشرة تستهدف جميع مصانع الأسلحة الألمانية التي تزود العصابات البنديرية "، هذا ما صرح به نائب رئيس مجلس الأمن الروسي، دميتري ميدفيديف، في تعليقه على اتهامات برلين لموسكو بـ هجوم على مطار لايبزيغ.
🇷🇺
…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89279" target="_blank">📅 11:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
الاعلام العبري: تم إطلاق صافرات الإنذار في مستوطنة نيلى الواقعة في منطقة بنيامين. وذلك بناءً على معلومات استخباراتية حول وجود مقاوم في المنطقة، تم استدعاء العديد من القوات، بما في ذلك وحدة "دوبدبان" ووحدات الاستعداد المحلية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89278" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7r8sCqx5mTcf7suBk1bpfoxSQRnnNmM25t7r0qYAbNVuZbQ60bzhPkLM1ifcDx1LgBZSBG-_328zhrxSOIuTprQs19_XXBR4pVTz1J16aS569TVMG44CPB32ylAOpuAEg0bMrYaMn9Jlikk30HAIFi8DF-EcuHbDOUnE-h9hPFQWYUJYC78Twwyhfom9l-jjfTuI3yCAW72LrJGgWIHba53Soxxh_IpXa4k5JDH51fsuehIrf8WwbcM7z6GV4uUJKEhob9-UDN17okfH7bPNtjNjYNOjbpigHDQ7ODbQOKpVDkUC9uX9Dtcu6Pf8yC6VeFj4hQGfOBYH0LehMaTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89277" target="_blank">📅 05:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال:
وزير الحرب الأمريكي يمدد انتشار القوات الأمريكية في الشرق الأوسط إلى عام 2027.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/89276" target="_blank">📅 05:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صواريخ ومسيرات تدك القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89275" target="_blank">📅 05:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
مسؤولون أمريكيون:
ترامب يجري، في جلسات خاصة، مباحثات مع كبار مساعديه حول إمكانية إعلان إنهاء الحرب على إيران، مشيرين إلى أن ترامب أبدى تأييده للفكرة.
كما يعتقد ترامب أن الضغوط الاقتصادية ستجبر النظام على تفكيك برنامجه النووي أو الانهيار.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89274" target="_blank">📅 05:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFy0GWmuto-nggiB_uRTLaxbTXcauOUjQ_qyQr4KNqVu6sFF4MIoorKRje9uAFNzLTZaLQX843xtCXUwtVZw1nVX0EooAdwczoU8J-BGHFBdIcaN1CkvnFqmd_mGaK1jGKZWpQFav8qVnRlBLcYB0fIBh3ib5Nc0x4IWhp-b-4XJSnM0qjyujNEonpUNRgGfIWUiTdB-d4DbOIZpTnWT3bY3EIi9t8L236dWaKdvIkzDT-8_UoKtiiOwigg-SDEp7_uCCmztbi8oc8iaKS1t67k1BK9DLK9jdvwJfunIxWDJoDqaZwdMrldo-1CgfvQo0Wyae_sIOPLemg2z_y-XFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ ومسيرات تدك القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89273" target="_blank">📅 05:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89272" target="_blank">📅 05:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89270">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89270" target="_blank">📅 05:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d9a8e6a5.mp4?token=SSuxZCnF47Qbxl0kDJeO5uSQkUq8swg1M0GdHZt-Jd6uRAjuVuci5CQ4dzSvsX9FUoY9aghfuay68VMHq8GP7s0mJtf_tqSdc6J5ssZ5941YqzcUxpB7hUAaZNE8ezInJkqrPfKRgmEtSXqvETtTWOGZfi0podAolK5c8hAFmYRpEmEfWQtQWxeAFVvcsz34n5x1nwyy4_7Bq6opP2hXCaw4id9S-U6OD3-rm2lHMpa_XZOl6iWauldIJg3zSnbjwOYmtvbOgRoBuxSuTSTZTZcUdKb0w-ML_8w331RPyHDYWUFT-OktkXhQyAnVZi6vapvzv7JmMskOVeCzMQUjdgP8dfEgXZ6uDiYx6vl6qmgVJbd9een7K0t5iHjz1SCdOPL0TC8ZZnWTh1CjwWgF9L_ZwgsYzmRaz5e3dyQr6LvyXSnHn4EpLv1_hkfOK6Y_OF_ijcInYyYJ6FmtNKorZQS7-HmiwIoy5jsI1sPqRVr9gx84xyMShqmP1laA6E3tk2Qfrtn_utRlhp2wnodJ8r9RqmANFYr2BqpSpbg2qFXBdildvyMSmR60tPzdlB5S6wiqdkIlzMfJCtLXBR1uny5mO6ADdjCgYz5jw8BUjY6fpd1dNsK6gJTzShg34F9b0EnaAE_-U1dWV0dyo3pU5OLKX_BI8kCj3ty5jWF_rrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d9a8e6a5.mp4?token=SSuxZCnF47Qbxl0kDJeO5uSQkUq8swg1M0GdHZt-Jd6uRAjuVuci5CQ4dzSvsX9FUoY9aghfuay68VMHq8GP7s0mJtf_tqSdc6J5ssZ5941YqzcUxpB7hUAaZNE8ezInJkqrPfKRgmEtSXqvETtTWOGZfi0podAolK5c8hAFmYRpEmEfWQtQWxeAFVvcsz34n5x1nwyy4_7Bq6opP2hXCaw4id9S-U6OD3-rm2lHMpa_XZOl6iWauldIJg3zSnbjwOYmtvbOgRoBuxSuTSTZTZcUdKb0w-ML_8w331RPyHDYWUFT-OktkXhQyAnVZi6vapvzv7JmMskOVeCzMQUjdgP8dfEgXZ6uDiYx6vl6qmgVJbd9een7K0t5iHjz1SCdOPL0TC8ZZnWTh1CjwWgF9L_ZwgsYzmRaz5e3dyQr6LvyXSnHn4EpLv1_hkfOK6Y_OF_ijcInYyYJ6FmtNKorZQS7-HmiwIoy5jsI1sPqRVr9gx84xyMShqmP1laA6E3tk2Qfrtn_utRlhp2wnodJ8r9RqmANFYr2BqpSpbg2qFXBdildvyMSmR60tPzdlB5S6wiqdkIlzMfJCtLXBR1uny5mO6ADdjCgYz5jw8BUjY6fpd1dNsK6gJTzShg34F9b0EnaAE_-U1dWV0dyo3pU5OLKX_BI8kCj3ty5jWF_rrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عقب التعرض الإرهابي على نقطة تابعة للحشد الشعبي.. طيران حربي يحلق في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89269" target="_blank">📅 04:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
عجلات الإسعاف تستمر في نقل جرحى الحشد الشعبي إلى مستشفى التون كوبري في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89268" target="_blank">📅 03:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead99d67d3.mp4?token=B8anXiHhCheF5LqMviBxS8Ix-1tGz_cD39qXMhAwdtnjklfxDS5-pCfV8TcHYydojwTS7YDK9EeX3uXp6ysGkHO5ZqWKMfbxl0-jX8r3cFB8D0_NqpM02pfkLrSw-qz778-brBnc4eoyUc-2DrQeEW2o3FREIPrZgbzAbogY8WTDIPduYAdF8o92mWurwoMo0cGUCtt8wmgnoBUkQXFQPK3AAyYsAaBaVMpDEfMnU-KtlVsZ-a6oGmvaSsw8iuqao_dClfwIiM2gy1gTm4G53o8zcVs0yXL-s-zWk77ewIHd1sbDm3bDTr614vem6yiW_Rtsn9ayq5xZlFYdpjsKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead99d67d3.mp4?token=B8anXiHhCheF5LqMviBxS8Ix-1tGz_cD39qXMhAwdtnjklfxDS5-pCfV8TcHYydojwTS7YDK9EeX3uXp6ysGkHO5ZqWKMfbxl0-jX8r3cFB8D0_NqpM02pfkLrSw-qz778-brBnc4eoyUc-2DrQeEW2o3FREIPrZgbzAbogY8WTDIPduYAdF8o92mWurwoMo0cGUCtt8wmgnoBUkQXFQPK3AAyYsAaBaVMpDEfMnU-KtlVsZ-a6oGmvaSsw8iuqao_dClfwIiM2gy1gTm4G53o8zcVs0yXL-s-zWk77ewIHd1sbDm3bDTr614vem6yiW_Rtsn9ayq5xZlFYdpjsKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عجلات الإسعاف تستمر في نقل جرحى الحشد الشعبي إلى مستشفى التون كوبري في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89267" target="_blank">📅 03:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azlgF3DAvJk53iB-tLFwWxQ2ILfJLznwq5E5H_K50vPmXDKJE3KwxkfEwe-Ddzj6JklyRilz60Eqbtlq6GE_6WhOsDi7p29_vJBW2JppnWKQe6V3NPVC8ScM-dFy9C0rS9W-x1YFc3OCpJ64uGbJBvZ-EQhv_OvYI29Q1FE6Ai-90ljUgsPwe3f3N-jbRzn5rEb5KAgPbyYKL-2QkzMmnthcAkEQ_Jftmup1cHsTW7nwFi4dWPZYB5x_wRnL126R1xb3GlE_v1UEI35yeX-3i0TjLhYM8ciHP2o0bV_tpkHlMsYwm4X2jRNAcrcY9XEwsnvBJuJJBIt70GIJKYtW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17c09a0ae.mp4?token=Ee0tEYJxY6hAQuL-dw7b64XR1KgMmk9NF1JtMQUjFYMyH_OAiXwmJEYSKuJ_nVySUerId0PrUo5d_uRxVKLIjwYC4LVUZwHOFY9hKdnlxPvhpzVCqoRQRvhrFvvYQkgnUtd3LCsXwkdL0VNMyaVcu7X_JwCVSXsmXGMONC29jKuRjXi7G8KwkXMzl0X-D1pIaLZdHj1vFr4zNo3T78QwT4Fso6modYMdDov6UwjfAZ7pbVNgb-K_1rLIsF2ZMeFIw28_j3h1NaJLYAIcHSnFWD1NzZ0dn73HtrgJYBjAymaWoLW5Hf_QEySmC580z6oH7Z11MyswSVFgYorKoXK3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17c09a0ae.mp4?token=Ee0tEYJxY6hAQuL-dw7b64XR1KgMmk9NF1JtMQUjFYMyH_OAiXwmJEYSKuJ_nVySUerId0PrUo5d_uRxVKLIjwYC4LVUZwHOFY9hKdnlxPvhpzVCqoRQRvhrFvvYQkgnUtd3LCsXwkdL0VNMyaVcu7X_JwCVSXsmXGMONC29jKuRjXi7G8KwkXMzl0X-D1pIaLZdHj1vFr4zNo3T78QwT4Fso6modYMdDov6UwjfAZ7pbVNgb-K_1rLIsF2ZMeFIw28_j3h1NaJLYAIcHSnFWD1NzZ0dn73HtrgJYBjAymaWoLW5Hf_QEySmC580z6oH7Z11MyswSVFgYorKoXK3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
نتيجة الهجوم الصاروخي الإيراني..
تظهر علامة احتراق محتملة على مدرج قاعدة الأمير الحسن الجوية في الأردن. ‏تستضيف القاعدة طائرات أمريكية بدون طيار من طراز MQ-4C تقوم بمهام استطلاع ومراقبة يومية قبالة سواحل إيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89265" target="_blank">📅 03:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89261">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj3AbiGYmb31cLnZpFF9lkNn_W4tH4GDyXht9zjvHe3WHwrCqtEEsrp3MaROeI-FXJaSVzh8CHdzUL0P16jZ2M-VnCxWu66lS7DNifrr7PxIkrG_yfC_Aa7OgKf8cTOOLhtEtbdk1xIHPWb6gn1dLyUi5cyL0BzIY0JLtDHK2wNBbla5C2lvoiXMEKVZbxaRPar0BjkuhclcvPZhKT8NqLE-o_70X9bWw9n3SxulgfajguWG42jCjKw6PRKVy1QnphHAyiBDE_4Lmu6wD9PsFjjaqdjsDZryAUNIisaovia_IARLJrjcwXGlSsoulvTANZXfQ6RDZkXdfiaiMTl31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_uTIxRWShnjYqSQa_pxggW63c8LkNe_A_dlAk1z6J0d5NfMnWdusUDWEhxtj-NtVyoMh5J3Iplx0bKwb5eom2I3XBXrf3NukqXjNLWp-CCJLTRibdrEp3ums7DRWizMazj6ta8H2v8FJiE8XirVocxSTsY6JZeVj5yNmcG1BZX_gQY4QHWz6dwIIhGnrVbcBIyyXKFysfrfMl6enqyM6C8Kp7bFNGMpn5y6ZE_RxRm5wBfUNxnEKKuKNVEvLVQBoBiZlgxw87egxzn9isigjCDPiEZd0Bcmoe_DjZZWfE4LRf7vew1Ja3Jzv1lKmAOaXIFyrNzKZ9JaALK350Cwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riE2QzDbpwSpSHjPUXTFjhXN1o34JwGM70z8a1Fw6vAKqSbxHeVXhNPs4hC9nzGfazj7YKIgwGnPbKZcT4CZC6GSBQ-K4y5cAm52a_j4vYsLYS_Rom_mHbpQBRVYn6wtd8ooIZYFDn00m54M13eZqfGotnw5H8xhb_9yjS0S8tHqRWDrOxJeym7u7bNju3Fg7UV8g7UYYJUHV4CEK9xXuDU1KT5dMcoEhAIKt03EwFNy66bdZ4jc_FWnLcJ-tICwx5hHh9EHf7zv8IU_fxZkSJrJCkDRRSMVZexScmhZnW7WhGZVPOTPfGMZx0udzCXGa7qYLIO5ZIaUwjpL8MarUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egZS6LXpvquXMA5-spay_F0lQ1vPTCRHUQl_z7uJgYLMeiUWtrpfnoTCGyHh84exCH9kFcdtGemB9ph0HwX1GUTzFi2TDfHb8tnR2Kgp4aMVL-nyPT4XYBo4nox9HObbB47Lr-eFvBgrmnXQynP4xc6LiS2mg3OUvi_k91_f5o7luxtA9z4H1cf7-B2uACLk_xCJD3iZcQleNX88JdLPg4SierZbUdO0_umr3HQs6zC-0U15rt70zeuna1Ciwr_MNkcvXQM-7j9f7XkOLKGspHcDletit1z9f7j4x78poP-g4Hre2sN3mKCI1n8zLs49CNsIsFrg6tg0pdjP3kQk4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
من مستشفى التون كوبري في محافظة كركوك.. شهيد وجريح كحصيلة أولية نتيجة تعرض على نقطة تابعة للحشد الشعبي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89261" target="_blank">📅 03:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a8d47d96.mp4?token=b-DzOJ6becQ2NJONEsnHtK9DfpHPBcKA_gVNNXKwrc9EyMPD9ebDK5xLDyY-U1B4T1HL0x9VYsZpNDFCFIcPC7HBiZ5REf9UrM9zT3J1Ylzl3MlDem73dL2qcHRKUiiY8OCcveYI0eEQuW8QHbED8DJymCjWYKAAbds8Gu6PQdEDqFnEsqJGTxbhILkuQGl__750ov3VUl1hwF37m0DyDMcmNSev_RQAFNUkbcEit4cxlWeoHqpI_-gtx4O7QoCwdkG3YLocg7aA4giXd8E9cJOZvDeuF36GPXFr0vAzRjcNOOhV5T6wuhow7TGnUhPJ0uEe1lcjfR9NGg2emxTkCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a8d47d96.mp4?token=b-DzOJ6becQ2NJONEsnHtK9DfpHPBcKA_gVNNXKwrc9EyMPD9ebDK5xLDyY-U1B4T1HL0x9VYsZpNDFCFIcPC7HBiZ5REf9UrM9zT3J1Ylzl3MlDem73dL2qcHRKUiiY8OCcveYI0eEQuW8QHbED8DJymCjWYKAAbds8Gu6PQdEDqFnEsqJGTxbhILkuQGl__750ov3VUl1hwF37m0DyDMcmNSev_RQAFNUkbcEit4cxlWeoHqpI_-gtx4O7QoCwdkG3YLocg7aA4giXd8E9cJOZvDeuF36GPXFr0vAzRjcNOOhV5T6wuhow7TGnUhPJ0uEe1lcjfR9NGg2emxTkCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 2 من منتسبي الحشد الشعبي جراء إطلاق نار من قبل مجهولين تجاه نقطة في منطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89260" target="_blank">📅 03:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cf4b10f.mp4?token=c89qhJtBoOBGjybpGgmM34Gxfw9m_rFRx8NMmJUzIreKmSJzdyUqqqALhC56RGu_4gDZCjN9J0DePUFmAGwYPT4KoLGIgZbWKlsVb4A82QwYK_BZ3k0ZjmZXaiJbY8_mhCjFmsKxQlgxuSH76ylhW_6b2AL24omh5dkTbJ5QHnTFx7wS2KkPmE2edAp57YYENRBHjIQTMglMl0CFLner5UjnqQUfx2qUHR7VpNPMUP7eg9qyAwciAyhwFmtuVvVM9Crwnqkv9AoY8bwYuFSzwfiTz06yBluqYcIYhkAZeCbsOjPgq_07dzofqstKKO83z-eXifH35CdtiPwNYPNAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cf4b10f.mp4?token=c89qhJtBoOBGjybpGgmM34Gxfw9m_rFRx8NMmJUzIreKmSJzdyUqqqALhC56RGu_4gDZCjN9J0DePUFmAGwYPT4KoLGIgZbWKlsVb4A82QwYK_BZ3k0ZjmZXaiJbY8_mhCjFmsKxQlgxuSH76ylhW_6b2AL24omh5dkTbJ5QHnTFx7wS2KkPmE2edAp57YYENRBHjIQTMglMl0CFLner5UjnqQUfx2qUHR7VpNPMUP7eg9qyAwciAyhwFmtuVvVM9Crwnqkv9AoY8bwYuFSzwfiTz06yBluqYcIYhkAZeCbsOjPgq_07dzofqstKKO83z-eXifH35CdtiPwNYPNAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 2 من منتسبي الحشد الشعبي جراء إطلاق نار من قبل مجهولين تجاه نقطة في منطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89259" target="_blank">📅 03:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e743d4eb.mp4?token=HCoIcbyqBEPwEx0qxZP2ceaYt7gpLZ0nxvAkstkPcIKmLUR1933kuOobPzq_bQMn27z9rL7rwL2uusm0Po850IhXANKFiPkmfWcXU5RNNsjE6gAYrTuMmNnVTbVju_cLdH33SfxYkeC0ii0vT5UMKQGJFICFdK3wCN89TRcfF40dEAFT3edO8ad_aZmgpuvtnbJZ1AJpOfJ92qwoiVhgGcA5zKatkWR6NEo_ziAnFmmtk0xL6AD0dXomjtkOyIiH1huwvdG2NbxXBgzCZiNGiKGWA505aEXWc6Rn7PSVsC9nwcxQjyw-HqGlNhuVjvze1rtkD7arJUcCZo5Z5Ta7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e743d4eb.mp4?token=HCoIcbyqBEPwEx0qxZP2ceaYt7gpLZ0nxvAkstkPcIKmLUR1933kuOobPzq_bQMn27z9rL7rwL2uusm0Po850IhXANKFiPkmfWcXU5RNNsjE6gAYrTuMmNnVTbVju_cLdH33SfxYkeC0ii0vT5UMKQGJFICFdK3wCN89TRcfF40dEAFT3edO8ad_aZmgpuvtnbJZ1AJpOfJ92qwoiVhgGcA5zKatkWR6NEo_ziAnFmmtk0xL6AD0dXomjtkOyIiH1huwvdG2NbxXBgzCZiNGiKGWA505aEXWc6Rn7PSVsC9nwcxQjyw-HqGlNhuVjvze1rtkD7arJUcCZo5Z5Ta7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
توثيق لإطلاق صواريخ من قبل القوات اليمنية نحو مواقع مرتزقة السعودية في مدينة المخا.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89258" target="_blank">📅 02:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da43261ac5.mp4?token=WowoqZ_4Yg_IOxDusUwIJJ8fvu7Immy_KapK4XOiZ2PQpGCxAkpX2gdHPNCqBvyfrPeRznsbJ2SGVRZHw3Be45dHFZk3Slbu_brBUmS9g89nHWskhiGjGnbgyl3OK7ASvwyObiUzXCF7u1iyrLI2jV1r87tdYLp73NW9xIcA8csltFsHQWhnYoUKgsrI3qVdXI2ehF4LRQ4puwpDswElS40igvUGk1QYdeFIYOfuxnHG5kr_ymy6iV7Fm1Hp9Fj0J3hFmQPC2xktQqg4igVfMfjLf9iOq83BIwRDPHvadm_LOtAe3QYWEB844oyHl9GEVF0j7RKmsYFrFza6xmQ9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da43261ac5.mp4?token=WowoqZ_4Yg_IOxDusUwIJJ8fvu7Immy_KapK4XOiZ2PQpGCxAkpX2gdHPNCqBvyfrPeRznsbJ2SGVRZHw3Be45dHFZk3Slbu_brBUmS9g89nHWskhiGjGnbgyl3OK7ASvwyObiUzXCF7u1iyrLI2jV1r87tdYLp73NW9xIcA8csltFsHQWhnYoUKgsrI3qVdXI2ehF4LRQ4puwpDswElS40igvUGk1QYdeFIYOfuxnHG5kr_ymy6iV7Fm1Hp9Fj0J3hFmQPC2xktQqg4igVfMfjLf9iOq83BIwRDPHvadm_LOtAe3QYWEB844oyHl9GEVF0j7RKmsYFrFza6xmQ9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حادث إطلاق نار في ولاية مينيسوتا الأمريكية؛ مقتل وإصابة عدد من الأشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89256" target="_blank">📅 02:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامب:
إسرائيل لا ينبغي أن تقلق. هل تعرفون السبب؟ لأنني الرئيس وسأعتني بإسرائيل.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89255" target="_blank">📅 01:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
سماع دوي إنفجارات مجهولة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/89254" target="_blank">📅 01:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daWS3vBqpZtFXNxk8d8bayRgRvp799of4EYixd0mFr1mquJR3WcKq-NknPvxnR-e702chJIJfQvWRU0FRk8QrsQtVSW7kZnqb3pcZ639LuNYJpFHVgdL-ejNIn02PxqliDUwrpGjUxNwgztPbDfE6zEgu4cVcSMmzdA6-kjWdE8YU-gfw9gCJhsUvMe9KW71ONGPOiV3osDqvFcTMQ68EzLLUGVFNJ3f9dZMAgQxVpBII0HN1oMckmjlFWJq2kt3cnr_uqZcciAfJSDYhFD7kBHfTlre6DK27vsPdsIp9oKZDJAp6tX5ey1RCQw9utiBwms1F6_1mfABYHH4kkZ9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أعلنت خرائط أبل للتو أنها غيرت اسم بحيرة أونتاريو إلى بحيرة أمريكا، وبذلك أصبح هذا التغيير المهم للغاية في الأسماء، بين خرائط جوجل وخرائط أبل، كاملاً ومصدقاً عليه وملزماً. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/89253" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تم إطلاق صافرات الإنذار في مستوطنة نيلى الواقعة في منطقة بنيامين. وذلك بناءً على معلومات استخباراتية حول وجود مقاوم في المنطقة، تم استدعاء العديد من القوات، بما في ذلك وحدة "دوبدبان" ووحدات الاستعداد المحلية.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/89252" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">المراسل: إذا كنت تريد أن يثور الشعب الإيراني، فهل سترسل وكالة المخابرات المركزية (CIA) لتزويد الإيرانيين بالأسلحة؟  ترامب: لا أريد أن أقول ذلك. لن يكون من المناسب أن أقول ذلك. أنا لست ضد ذلك.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/89251" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
🇸🇦
🇾🇪
بعد الحصار الايراني واليمني:
‏تراجعت صادرات النفط السعودية إلى أدنى مستوى لها في تسع سنوات، حيث تهدد هجمات على ناقلات النفط عملية التعافي.
‏بلغت صادرات النفط في البلاد حوالي 3 ملايين برميل يومياً في شهر أغسطس.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/89250" target="_blank">📅 21:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=C0O-DmVa0IciLRKbegyNB4tk_Raw9n0Nx6Ca_xkw_QNt_8BfbeG7O_rBbaC7-M_2jpdOy5SHRwl7JOO1Zu6CEkSXnDmrhBISkR_SqDT7RxUsgQvtp_dmRaXYpA0649h8CiCXbZSBGWkrzD9ATr_SxohKOSrXb3c19fkNMxeCNVeC5gOqxudS6L-ustuyaRsA5sabGOOQjI2qHyeWzQnzNaR1ZmkJPLTCbpvieOBNu1Cb5eP9GnLlZHfzwOcae6rGjMG8Vay7cpM4oP-fIBFLADQIlaC9w5GFSfZZIq_BEqjy2GKM7LwJdc_AvXrtX6DqJWBGxSynjlkLKkbplwG6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=C0O-DmVa0IciLRKbegyNB4tk_Raw9n0Nx6Ca_xkw_QNt_8BfbeG7O_rBbaC7-M_2jpdOy5SHRwl7JOO1Zu6CEkSXnDmrhBISkR_SqDT7RxUsgQvtp_dmRaXYpA0649h8CiCXbZSBGWkrzD9ATr_SxohKOSrXb3c19fkNMxeCNVeC5gOqxudS6L-ustuyaRsA5sabGOOQjI2qHyeWzQnzNaR1ZmkJPLTCbpvieOBNu1Cb5eP9GnLlZHfzwOcae6rGjMG8Vay7cpM4oP-fIBFLADQIlaC9w5GFSfZZIq_BEqjy2GKM7LwJdc_AvXrtX6DqJWBGxSynjlkLKkbplwG6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب يعيد ما قاله قبل ٨٠ يوما : السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/89249" target="_blank">📅 21:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
🇺🇸
‏
ترامب يعيد ما قاله قبل ٨٠ يوما :
السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89248" target="_blank">📅 21:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية: لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89247" target="_blank">📅 21:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية:
لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89246" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Q6M9z0QcGu7s-YMfTVGppjtzYFW-HMlm9l6dqdlgLdYa2cuffB_wJXfcoEwGu4KDX0nktxLNvKWrPtF7hxr-5iEKwm7Vi7RWYdtJpXYDCJSkLfadT32JZQV-Cv7ci-Z84LOMdR5sK6cFO8ty6ItC8A73MgPF_DnmHUg-kyfW3e_rzjyaITewwYaQNzEcpdcZWWecHVBxlVMFMN1ppvDC77cRar59Ded2jGV6Y8yiwR6RPjwuESs_xJthSHAk43RF4l7dGVTwdCaNzRe8nzafPC6Ga0lfsFw-1ngCWjkl_jiiy_Xel-zQBp7MrjCmLd_RQM3PRvTEM8LAPzQYdH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
عثور على ثلاث عبوات ناسفة في وارشو عاصمة بولندا بالقرب من محطة سكة الحديد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/89245" target="_blank">📅 21:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
🇺🇸
الاعلام العبري: ‏
بعد الهجوم، وجهت الولايات المتحدة رسالة إلى طهران عبر قطر: إذا استمرت إيران في التصعيد، فإن واشنطن مستعدة للانتقال من ضرب الأهداف العسكرية إلى ضرب البنية التحتية للطاقة والنفط.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/89244" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🇮🇷
المتحدث باسم الأمين العام للأمم المتحدة:
أعرب الأمين العام عن قلقه إزاء التقارير التي تفيد بوقوع ضحايا جراء الهجمات الأمريكية على إيران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89243" target="_blank">📅 20:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
:سنطيح بالنظام في إيران - سيسقط. جميع أنظمتنا تعمل على إسقاط النظام، إذا هاجمونا، فسيكون هذا الهجوم الأخير لهم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/89242" target="_blank">📅 20:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqW1egbhjQaIaxcxGkWsYazLsnouztJSvAglgyqvh1pwD3WG7Cq92op5-A_AFGpz9PreqhFPlSKBDlbEDr1wKueiQAmHP5OIn6vhkrzNEFziEdZdEEQkK8LATE0CVO3MmDFqExycMhEnW62Cz0N2WdmUWVyEFugHT_6sfNTdlOvBOblLcjluGzrxxbdtTGHS9RZnqaD3baxl-bnZZ7O7_q71R3OnYMrJbCjZVCkUUCv1ELhM00eqLqTjsQw4F3GT66fl9kBfhwGXXqqKNeFo-2ah2W7ti9jehzWlcykCz4jUcpASPvRHzgNhMciSUcmxgCwclyz3sSvHRsyyWAMWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
بعد 18 عامًا، تتبنى إسرائيل مسؤولية اغتيال الجنرال محمد سليمان عام 2008، وهو المستشار الأمني المقرب والأعلى رتبة لرئيس سوريا.
وصلت فرقة من القوات البحرية الخاصة عن طريق البحر وأطلقت عليه النار من مسافة قريبة، ثم اختفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89241" target="_blank">📅 20:19 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
