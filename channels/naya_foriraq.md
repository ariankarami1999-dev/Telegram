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
<img src="https://cdn4.telesco.pe/file/NR1vxTSY2mIJ4gsEyvk5cFoUPwdBiSGR-bDJNfzw7BNengGlMhyp5mZJKB404PgwImPHiefJf3mJVT5pHMaka9m4y2t8k6BdjAo_BZAdd_b5aMJEuE6SfZFRiUbzjKB8T0OZGs-QuT5UFO4Wdxlr3j6ZFkSLRDQr2GBYZwQktMYRmH4cRX9dG8pKcHB-gO8FaK5MV-PFrmOymgYXY9gAdaFlEpqU147eiWSFlahWoa2mp8PIwzguZAV8FpWWy1_MOKmycPO4SkqhdsQZ_eMlyQiA06144vyYvC8E82NEwUvMDMROen6B6umhC9-Pfbyz7StVb2RLfhrkpvqtHa59Bw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjL2V44BVtBoMcPuaNRJnq951AI1HMTd-mdHcfGQ961yycg6xZmcDHCVb7ZxbZaCE49QUdqd3zWlKXUYd3lHucI7goBxclC53TF2f6Dz828mjZ0TsU337gXVRhRDH6eU8VnWvVVsaugRFaB4mam99TcgbbIc48O-lyNS1FF1Gt-n3tJ9a2KJ8vYA_XC7j12CZbICa_pxEPHQp22lPHwRsT6-ZFbzBV3dDK86bknuYUlrFNEwcsTRMZtjaYyNf1ePVKMHFi5sBtrhWxm_KOZf4lCgJ-Oih9w2oT-7jmPjhWXguo_mnaLCaj7oPlTpYGacIz0xCAx1RITg45wXq2n91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPUTiCX0mu6qN-qAGEF-pr52P5kVR3_TpBtdM2FUzJ81vY_ejozrr_n7i0fPTyWHFHW4ceSfUaumgm9Bbtlm_w1PKXtEW3lw69-MXvwYPTA9PCXhh0UQRVGmWnKlqUOtMSkau-cNd7nyBWCLlHDmWFFGV4XzFABcugLRGS3R8sDJmeIeuZ4Y06bbD3E34ej0O5J6X7jDbBcY5gp4wwvcxHB0GsH7SQs2cdOwzu14SQLGFQueDNRuF6hYDHVlGSlapG8PUPMRmvk4CKycLnufl454THrx3U2q2aQkmcSL5T0omszhW5ZIeDDKfdeBPbPtBpZqmbu8K4JtgRkCYGPK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8YJeI0cFiizC3qaBJcdJSRa9WN5BjNZbequKWbq-Uq23TKBbSoWnUQlKsAtkBTh7Nprdf8kf9DaBhdLIGTYZSi5YTvLzIe3dyfJIvmwi0iYGKumGeUyOm4h5lqYNa3-kfUgZHfLvduyYxEp9ORd1h76G6VS9_Yy_jqeYpSyFEZCwp4GDP0MG1s4S7XH04TYp51E2M_B5MWwu7oQkabINJQoBI-6B4xSEFwlVvqNmwPI9r0ovgrMfGf4Il35YCP_Ot3xz1MgxogV6QsNLkpyGV9eH2GxL8GGR25EAQ0MXtjBTLf5LCMgtR7nNKj2Uf4rHeQy_kuTYLuN8dqeP_BDqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان ينشر بنود الاتفاقية مع الولايات المتحدة رسميا.
- تُعلن الجمهورية الإسلامية والولايات المتحدة وحلفاؤهما في الحرب الحالية الإنهاء الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان، ويتعهدون من الآن فصاعدًا بعدم بدء أي حرب أو أي عملية عسكرية ضد بعضهم البعض
- تتعهد الجمهورية الإسلامية والولايات المتحدة باحترام سيادة كل منهما والسلامة الإقليمية والامتناع عن التدخل في الشؤون الداخلية لكل منهما
- تلتزم الجمهورية الإسلامية والولايات المتحدة بالتفاوض والتوصل إلى الاتفاق النهائي، في مدة أقصاها 60 يومًا قابلة للتمديد بالتراضي.
- فور توقيع مذكرة التفاهم هذه، ستبدأ الولايات المتحدة في إزالة حصارها البحري ضد الجمهورية الإسلامية كما تتعهد الولايات المتحدة الأمريكية بسحب قواتها من محيط جمهورية إيران الإسلامية في غضون 30 يومًا بعد الاتفاق النهائي
- عند توقيع مذكرة التفاهم هذه ستبذل الجمهورية الإسلامية قصارى جهدها لاتخاذ الترتيبات اللازمة لضمان المرور الآمن للسفن التجارية مجانًا لمدة 60 يومًا فقط
- تتعهد الولايات المتحدة مع الشركاء الإقليميين، بوضع خطة نهائية متفق عليها بشكل متبادل بقيمة لا تقل عن 300 مليار دولار أمريكي، لإعادة إعمار وتنمية اقتصاد الجمهورية الإسلامية
- تتعهد الولايات المتحدة بإنهاء جميع أنواع العقوبات المفروضة على الجمهورية الإسلامية، بما في ذلك قرارات مجلس الأمن وقرارات الوكالة الدولية للطاقة الذرية وجميع العقوبات الأحادية الجانب، الأولية والثانوية، وفقًا لجدول زمني متفق عليه كجزء من الاتفاق النهائي
- تؤكد جمهورية إيران الإسلامية مجددًا أنها لن تحصل على أسلحة نووية أو تطورها. وقد اتفقت الجمهورية الإسلامية والولايات المتحدة على حل مسألة التخلص من المواد المخصبة المخزنة وفقًا لآلية يتم الاتفاق عليها بين الطرفين كما اتفق الطرفان على مناقشة مسألة التخصيب، وغيرها من المسائل المتفق عليها والمتعلقة باحتياجات الجمهورية الإسلامية النووية، وذلك في إطار عمل مُرضٍ يتم الاتفاق عليه في الاتفاق النهائي.
- في انتظار الاتفاق النهائي، تتفق الجمهورية الإسلامية والولايات المتحدة على الحفاظ على الوضع الراهن الحالي لبرنامجها النووي، ولن تفرض الولايات المتحدة أي عقوبات جديدة، ولن تنشر قوات إضافية في المنطقة.
- تتعهد الولايات المتحدة بأنه فور توقيع مذكرة التفاهم هذه، وحتى انتهاء العقوبات، ستقوم وزارة الخزانة بإصدار تصاريح لتصدير النفط الخام الإيراني، والمنتجات البترولية ومشتقاتها، وجميع الخدمات المرتبطة بها، بما في ذلك المعاملات المصرفية والتأمين والنقل والشحن
- تتعهد الولايات المتحدة بإتاحة الأموال والأصول المجمدة أو المقيدة للجمهورية الإسلامية للاستخدام بالكامل عند تنفيذ مذكرة التفاهم هذه وتتعهد الولايات المتحدة الأمريكية بإصدار جميع التراخيص والتصاريح اللازمة وفقًا لذلك
- تتفق جمهورية إيران الإسلامية والولايات المتحدة الأمريكية على إنشاء آلية تنفيذية لمراقبة التنفيذ الناجح لهذه المذكرة والامتثال المستقبلي للاتفاقية النهائية لعام 2001
- بعد توقيع مذكرة التفاهم هذه، ورهناً ببدء تنفيذ الفقرات ١ و٤ و٥ و١٠ و١١ من مذكرة التفاهم هذه واستمرار تنفيذ هذه التدابير، ستبدأ جمهورية إيران الإسلامية والولايات المتحدة الأمريكية مفاوضات بشأن الاتفاق النهائي حصراً بشأن الفقرات الأخرى.
14- سيتم اعتماد الاتفاق النهائي بقرار ملزم من مجلس الأمن التابع للأمم المتحدة.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/naya_foriraq/79178" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
بيانات ملاحية:
ناقلة فرنسية للغاز الطبيعي المسال تعبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/naya_foriraq/79177" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في أطراف بلدة مجدل زون جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/naya_foriraq/79176" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
بناء على الحاجة العملياتية تنتشر قواتنا في المنطقة الأمنية بعمق 10 كلم داخل الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/79175" target="_blank">📅 13:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79174">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/79174" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/79173" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/79172" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79171">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtRY8wZYH8U7sX2f2qWk-y1teMWEJ6fqriaSMyMiAgO54wRpe30HNNKaRYAtKFTJ-MwxMs16fLEyW5WsExg_XO6lG1iHBpmJVb9-gKEDwymtsMi2gZMDITqgrqKxQxBupnIE8acao6qeKl7i-4WyN9-2PI69IIOtN9E7AT4Hi7qM5Xd-Hz2DJr65NKJGp-fb69eBJEB7bWxgaQg52NJLiPIQ6t2QiKFVY-I24-oLKa1p-N9TBBQvNLFZfzusWljunZVNaHysmdW5a6jPV8RXbw2NAYHwQERVoUvr5zPz-h2wwKuuwulbW18XtzNJFnelJORxV0jdRZQ56AjUFLsLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
"هؤلاء الحمقى الذين يظنون أنني لم أكن حازماً بما فيه الكفاية مع إيران، في حين أن سوق الأسهم قد سجل للتو مستوى قياسياً، وأسعار النفط "تنهار"، إما أنهم حسودون، أو أناس سيئون، أو أغبياء. لنجعل أمريكا عظيمة مرة أخرى!!!</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/79171" target="_blank">📅 12:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=XgjUkXqqR97M5y2xrnInk-pTrzIttR1xUZQpAYTIUfKA57nzBOtSlL0vRpD7Kdv9KIQ08C3X9JTnoj3lXJGCCb9e-FGYB-VB6jBi2AFJsy0ZX8mgzd5SofI7bU4rnC8QcVIHWYLQ4us9ERDRCxmlD6yHAiTO91UowZGsXmD7OzgGeHtDn0R5j6Wilz_vqHf8U-Z0TgR5WZIzoG95PxCryi1p5sAmofYoWsAREniKt-NAJ3fUqiPcoayqnO3lE1JdwFpjJeVv2B9_U2SlrTmnhWF267a7sFyDO4nOBZFKBvLfhDromQJkw-P3TmZekobe8hcyXyeAnR7ptUsD29xQBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=XgjUkXqqR97M5y2xrnInk-pTrzIttR1xUZQpAYTIUfKA57nzBOtSlL0vRpD7Kdv9KIQ08C3X9JTnoj3lXJGCCb9e-FGYB-VB6jBi2AFJsy0ZX8mgzd5SofI7bU4rnC8QcVIHWYLQ4us9ERDRCxmlD6yHAiTO91UowZGsXmD7OzgGeHtDn0R5j6Wilz_vqHf8U-Z0TgR5WZIzoG95PxCryi1p5sAmofYoWsAREniKt-NAJ3fUqiPcoayqnO3lE1JdwFpjJeVv2B9_U2SlrTmnhWF267a7sFyDO4nOBZFKBvLfhDromQJkw-P3TmZekobe8hcyXyeAnR7ptUsD29xQBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/79170" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
حان الوقت للجلوس مع الفرق الأمريكية والإيرانية لاتخاذ خطوات ملموسة.
سنشارك في المفاوضات التي ستعقد في سويسرا بين واشنطن وطهران.
هناك خيارات عديدة بشأن التعامل مع المخزون الإيراني من اليورانيوم.‏
الاتصال مع إيران في أدنى مستوى له.
إذا لم يفتح مضيق هرمز حتى نهاية يونيو فسيكون الاقتصاد العالمي في منطقة حمراء.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79169" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79168" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79167">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79167" target="_blank">📅 09:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=DEZeN_SGUG4OPgi-_FjL2rrIgjp_svseY3nSyu_g8drdB30NaP3wCz7gcrl6SV01WADDDD4dwEzIt8lGTEnzRfP2inlzOVc76XuG3PTRQR5RnroefCNaXkz6QtLXu2q4N8Kj8hMoy-jZlHgrOn-ONnByn6LTt6_KHZ19jjgETZxbvEwJ8yM7Zzt66IGeuDoQy-IUWgl5faRTezjgMXcT_nWpfEdDIEO3zfYHX-HmOAgR_y-hXYsEXAYG4XejJ5t-86LUZc3cvuzJtN3Lvr6DIKi3sjB0t0WNYLS3qtL20DOfb2AT_l1lbT7dpRzeuGDyGkUHNAruEumfkdc2GWr_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=DEZeN_SGUG4OPgi-_FjL2rrIgjp_svseY3nSyu_g8drdB30NaP3wCz7gcrl6SV01WADDDD4dwEzIt8lGTEnzRfP2inlzOVc76XuG3PTRQR5RnroefCNaXkz6QtLXu2q4N8Kj8hMoy-jZlHgrOn-ONnByn6LTt6_KHZ19jjgETZxbvEwJ8yM7Zzt66IGeuDoQy-IUWgl5faRTezjgMXcT_nWpfEdDIEO3zfYHX-HmOAgR_y-hXYsEXAYG4XejJ5t-86LUZc3cvuzJtN3Lvr6DIKi3sjB0t0WNYLS3qtL20DOfb2AT_l1lbT7dpRzeuGDyGkUHNAruEumfkdc2GWr_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79166" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79165" target="_blank">📅 09:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
لا يزال استهتار البعثات الدبلوماسية الأجنبية في العراق مستمر
اصابات خطرة لمجاهدي جهاز الامن الوطني العراقي بعد تعرضهم لحادث سير من قبل رتل تابع للسفارة الأمريكية على طريق مطار بغداد ؛ ثلاثة جرحى كحصيلة اولية من الضباط …</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79164" target="_blank">📅 08:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79163" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm8WzINVH4E-0aORjKcySjk2nAjcRT1ZhfM3j4hrcTZKIuLcqHD7zwuMv-2jmgj6q4t5sxTV722WVhnHYl3P6uX0XlGJB-Ui8aNaoIWiUQZYbI_mHLtU-_jvtIeXb1Y1vofUCLlB45iAU8BerO-eKDGY6tfDzTS106W4ly3jllThff12VjsFYRZr8fhDYyIxNKNqvaOmlNCLy7Hafuob4qZXoLJsJ2FBi31g5lj8bLNZbo7AhEsHl71zMo0StNFECDXOHOGksPc_lZd-2MCe2pilSnBZYFYKYL5AJ89L6F1ldQP-C6RRbE5GQimWhuFG3rxtx0LcpWILCO678Of0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5a5ACxIUHlAdqc9W29ctZys1GaOMkCQj36fpvQSFmEPOz9o0aErW4m62xVsrOqaMFIBOIIil61wfjs0CwekFK7R8f_wO55d3gPy5paOhWn_2lCI6sUqz3ALIYUjs4RD9LnPbF0z-JFYWwdyEdvPGumaeQgKMu5xsN_xqD6Rpgx2rjBwCi9_oyQ10whf87cJtoFELJR1FY9eQq00zG_9BoIgu_cRzEEkC_FeE3u2tVSpKGtSXzQffP2SLjalC37Pa5PS1YN85-IkVjucjdGX48OwkAdReYiTF2fYydFKRwijiwsywMV9T9OMA47_GODtQtVg_7baZrly4W3qf9_xBvi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5a5ACxIUHlAdqc9W29ctZys1GaOMkCQj36fpvQSFmEPOz9o0aErW4m62xVsrOqaMFIBOIIil61wfjs0CwekFK7R8f_wO55d3gPy5paOhWn_2lCI6sUqz3ALIYUjs4RD9LnPbF0z-JFYWwdyEdvPGumaeQgKMu5xsN_xqD6Rpgx2rjBwCi9_oyQ10whf87cJtoFELJR1FY9eQq00zG_9BoIgu_cRzEEkC_FeE3u2tVSpKGtSXzQffP2SLjalC37Pa5PS1YN85-IkVjucjdGX48OwkAdReYiTF2fYydFKRwijiwsywMV9T9OMA47_GODtQtVg_7baZrly4W3qf9_xBvi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لحظة توقيع اتفاقية التفاهم بين الرئيسين الايراني والاميركي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79161" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية: تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79160" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية:
تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79159" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏اندلع حريق في الطوابق العليا من مبنى الإمارات في دبي
‏أبراج فاينانشال: سبب الحريق مجهول</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/79158" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
قالبياف:  بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.   وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.  بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79157" target="_blank">📅 00:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=GIJde_Ns3kvneVbZJZtRsfkxRujpBoafqR-WdRlerTDFfIA_BiV91IIpGYOSvRpDxJ1nKQrhrcK8yyboHIHc8q2j_2cZhecZkPYYOKMh2UlQT4hW5_fLke6Za6NtF-xdlcb2_tQQVIXPh9droagSJI9pUdQ2sGqg4oORcEy9wvVSrqetNy6QV-sJ5-tHfJrnhTzfjhqt6p9ioKRmrYcMq8wecpzheGjTwLHbHl312jZTF_mJOOt643Brx6LrujIhuCbeXe2R8O75vBhA3Ub32xCaatSdwnaldDviVBrMRSAWhIkmN9U10dHA8Xqxx0YZQM_V3fl5nbwS9ggFnhtvLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=GIJde_Ns3kvneVbZJZtRsfkxRujpBoafqR-WdRlerTDFfIA_BiV91IIpGYOSvRpDxJ1nKQrhrcK8yyboHIHc8q2j_2cZhecZkPYYOKMh2UlQT4hW5_fLke6Za6NtF-xdlcb2_tQQVIXPh9droagSJI9pUdQ2sGqg4oORcEy9wvVSrqetNy6QV-sJ5-tHfJrnhTzfjhqt6p9ioKRmrYcMq8wecpzheGjTwLHbHl312jZTF_mJOOt643Brx6LrujIhuCbeXe2R8O75vBhA3Ub32xCaatSdwnaldDviVBrMRSAWhIkmN9U10dHA8Xqxx0YZQM_V3fl5nbwS9ggFnhtvLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالبياف
:
بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.
وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.
بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان المرور عبر مضيق هرمز وعانت من حرائق واسعة - وهي مسألة أكدتها أيضًا صور الأقمار الاصطناعية.
ومن ناحية أخرى، تم استهداف أي مطار في أي بلد انطلقت منه طائرات مقاتلة للعدو. حدثت كل هذه الأحداث أثناء مشاركتنا في المفاوضات في نفس الوقت.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79156" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
‏ترامب: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79155" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
‏ارتفاع إنتاج النفط الخام في جنوب العراق بنحو 500 ألف برميل يومياً ليصل إلى 1.5 مليون برميل يومياً، فيما ارتفع إنتاج حقل الرميلة إلى 650 ألف برميل يومياً. كما أعاد العراق تشغيل حقل غرب القرنة 2 بإنتاج يبلغ نحو 150 ألف برميل يومياً، في إطار تعزيز الإنتاج وتعافي عمليات التصدير.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79154" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
‏
ترامب
: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار النووي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79153" target="_blank">📅 22:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امريكا وانهيار سياستها الخارجية؛ ‏الرئيس البرازيلي لولا:
لم أطلب عقد اجتماع ثنائي مع ترامب لأننا
نتفاوض بالفعل.
‏ما فعله كان عملاً شائناً تجاه البرازيل. وهو يعلم ذلك.
‏لهذا السبب قلت إنه لا يزال يتصرف كإمبراطور.
و ترامب كثير الكلام وقليل الاستماع.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79152" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g__rnL45vuwu9SASCDZ0R_wEsU-FIth3Icn64zWsl-0FY8AbEw3KRay5tm1Ddxqx2VT4t-zmja2MHl82c99kwhITJKgcvebhmnNLvJhO8BzZNPtnV9_9YwnU_tTvHqO2_ZHQSXCdDLwXigwVpA2sWprlMyED_XxgVLXiOnyaykuK9HqpiXqcF8mQweeoWCkJccKHvpNI-NiFur0bTS_VEzekXIyjcyoOZ3BhIGnQrqt4XhRnjY8G3642iAqd5SIpPRc5f6EKAwDUDv6LTqV9pBueSjQk99dLVkSRe-NyC3QxBwlgAWxCAzeAVxRQpwmEE2dIbe-9B87FhUs5OitE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيلون ماسك يعلن دخول ستارلنك للعراق من خلال زيارة توم باراك للعراق !</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79151" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=MR0lfSkpphHEshHe7wz1XLjSpUb-iR4hWwn8BqGCzIhfiMmMUFbeSMTAjAQPSE4GXFFs6E-bTJzwNERJsMRq2qtzg5E4KutlXGFn2vx42E_78UtxYrfPgD71TpucVmmiHWC1Ohhq3thUDd4Hq-At11bgB8vDuLR3rp2E4KZFzrAjihe28ZYF059yvy_H3wTMiXVyt5pApklUvtlDEYMLyfLk2vIKoXZl5Jt1PkCf6AV6d_LJnxvbYsZvk-axQZeLzV7T74OSsxVs-VuiG0_38t1oSXGUxQS_WRNktuxTKs7y0N2ZjjRd2wD3Q6EmM_7-rLOt1omcUqzPjr6-n0VLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=MR0lfSkpphHEshHe7wz1XLjSpUb-iR4hWwn8BqGCzIhfiMmMUFbeSMTAjAQPSE4GXFFs6E-bTJzwNERJsMRq2qtzg5E4KutlXGFn2vx42E_78UtxYrfPgD71TpucVmmiHWC1Ohhq3thUDd4Hq-At11bgB8vDuLR3rp2E4KZFzrAjihe28ZYF059yvy_H3wTMiXVyt5pApklUvtlDEYMLyfLk2vIKoXZl5Jt1PkCf6AV6d_LJnxvbYsZvk-axQZeLzV7T74OSsxVs-VuiG0_38t1oSXGUxQS_WRNktuxTKs7y0N2ZjjRd2wD3Q6EmM_7-rLOt1omcUqzPjr6-n0VLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ضربة قاضية من طائرات إف-5 على القاعدة الأمريكية في الكويت خلال حرب رمضان.. الطيار الإيراني يتحدث:
تم التحليق على ارتفاع أقل من 50 قدمًا (بينما الارتفاع القياسي 500 قدم) لتجاوز دفاعات الكويت المتعددة الطبقات وأنظمة باتريوت.
العمل في صمت لاسلكي تام؛ على ارتفاع منخفض جدًا لدرجة أنها مرت بين سفينتين وكان سطح السفينة أعلى من الطائرة المقاتلة.
احتراق مروحيات العدو في الحظيرة  قُصفت قاعدة العدو بقنابل متطورة، ثقيلة، دقيقة، وساحقة.
دُمرت مروحياتهم المتطورة في الحظيرة نفسها قبل أي رد فعل.
دُمّرت القاعدة بالكامل، وبقوة ضاربة هائلة، لم نرحم العدو الغاشم.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79150" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79149" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cli2R4T3oqHlrhffY2eefakfZCRD2XWEJs9ENvWWgfMzQxscN-UmvJNrSefM_xXxmvWvjB2NGfEp2zyxvS7YstlHyWlVy59XT1ulO3oHHcKfum9zZ0XKx6D52VAdV8dWFVD8x32SEt-XoNufA9UuWeLoHM4Dl_o5Cje8WscpkswZUNJPNyE2Z8AsE0miTPQF1N2T2ysi_zH7n6ImKelUJzMcGpyUu_7ap0pafsQpuUB5kO_iyZd09vP0ZK1PXb2kjDOs69Kj61eBp6S6J0OuGENMCLn8mqnilANugCdNJe6w85umOtcRELqURr9C7jG9FEwTulcwTG4bgy-Foz31_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏اعلام الاميركي: ترجيحات بمقتل 8 من طاقم الـ B-52 التي تحطمت في كاليفورنيا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79148" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79147" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
إذا كان المقصود أن علينا الاستسلام من أجل رفع العقوبات فذلك لن يحدث أبدا.
غير صحيح أن جيشي أمريكا وإسرائيل عديما الكفاءة ورغم قوتهما هزمناهما خلال الحرب الأخيرة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79146" target="_blank">📅 20:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد محمد بن سلمان.. ترامب: أفغانستان تقبل مؤخرتنا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79145" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن الحرب على إيران: أيضاً، ستنفد احتياطياتنا في غضون أربعة أسابيع تقريباً، كما تعلمون، هناك احتياطيات في جميع أنحاء العالم، وستنفد بالفعل، وسيكون هناك وقت لن تتمكنوا فيه من الحصول عليها.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79144" target="_blank">📅 20:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79143" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79142" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:  حسنًا، إن إلغاء التجميد - إنه سؤال سهل الإجابة عليه.   لقد أخذنا الكثير من أموالهم، وقد - أموالهم التي أخذناها منهم.   عندما لا تكون أموالنا، فهي أموالهم، وقد جمدناها في وقت معين.   أعتقد أننا سنضطر إلى إعادتها، أتعلم؟   إذا لم نقم بإعادتها،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79141" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79140" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يسخر من محمد بن سلمان:  لقد تحدثت إلى ولي العهد السعودي عدة مرات - إنهم سعداء للغاية لأنهم لا يزالون... يجب أن تجعلهم سعداء أيضًا، أتعلم؟   نحن نستخدم مطاراتهم، وليس أنهم يمكنهم إيقافنا إذا لم نرغب في ذلك.   ذهبت للحصول على ذلك الوغد الصغير. لكني أخطأت.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79139" target="_blank">📅 20:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO3i-4CIzyTPVXgDPSFUX1ppe0t_PbaeQm4BfGecINhLTk9vcEWx2psB7579gAEtgaRhJ5g-kBzfAs3im2U-wGWML_nuT5Y-YJ0k40Pa_rKQeLH8oqzhZ8ZUnOayWAuCKXxEEfs-tdK9jvWqq7_NKPIC2YVwKoMX-aZzlN60fB19ACNt4BmX4tKeqO3JDtEVXPa4LT8G5fglOitiocwgWfVNXUfIQiUxELpnLojMOl4cWwcwEdX3pTX_524MikltTeD391BPzwNd6YfMwNm6r0ec4sKnG4HAwLMHhwLAML_1-77eCgisST-1eTsQ2dK3HMwmiBNJDigSrqVtOkCIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ إعتراضية في سماء مستوطنة المطلة في الشمال الفلسطيني المحتل دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79138" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=HMl_lKGcVwlcOCvRIaPXAihVOKuDe4znmdwedxNg0TQiJwd0HT0_ibYjYz8pdJzBuNlIA2xXoGuPXQy19H65wndBXIGxLt834OT2yHLx0e6Akw2SqO7Go_Mgn6P-5hKzwfxFLZsOF77jlqvb5cQQkRRpcQbvmvFnDuIew7_I2c_m96cDxar8if1j8VbShtXyg9sL_z_o-3in5R71xkAQO9-uDMe_2qy3wNwh1hEKnCEOHdTR5r3p66HsFXLQ--rX770pH2-BpI2X9vHPj_-sUjKR8yBxbzEz3grDzpvHRkhou8powhRbvspNaW1X_NaRkJ3eV5CEzxD0_cQEvnp2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=HMl_lKGcVwlcOCvRIaPXAihVOKuDe4znmdwedxNg0TQiJwd0HT0_ibYjYz8pdJzBuNlIA2xXoGuPXQy19H65wndBXIGxLt834OT2yHLx0e6Akw2SqO7Go_Mgn6P-5hKzwfxFLZsOF77jlqvb5cQQkRRpcQbvmvFnDuIew7_I2c_m96cDxar8if1j8VbShtXyg9sL_z_o-3in5R71xkAQO9-uDMe_2qy3wNwh1hEKnCEOHdTR5r3p66HsFXLQ--rX770pH2-BpI2X9vHPj_-sUjKR8yBxbzEz3grDzpvHRkhou8powhRbvspNaW1X_NaRkJ3eV5CEzxD0_cQEvnp2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏إن توسيع نطاق اتفاقيات أبراهام هو الأمر الآخر الذي نأمل أن نحصل عليه. ‏وأعتقد أن المملكة العربية السعودية، إذا قادت الطريق، ستكون قد قدمت خدمة كبيرة لنفسها.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79137" target="_blank">📅 20:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
🇸🇾
‌‏ترامب: الرجل المحترم في سوريا، الذي أصبح الآن رئيسًا لها، قام بعمل رائع، فقد أعاد بناء ذلك البلد في عام ونصف، مثل بلدنا إلى حد ما، عام ونصف، بحجم مماثل تقريبًا.  ‏قالوا: "لا، من فضلك لا تضعهم هناك، إنه رجل عنيف للغاية، من تنظيم القاعدة".  ‏قلت: "حسنًا،…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79136" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=E9gUMnqxjhln202zbPPxutWQBWdXm34pDB_ors6JPtA-nrV1WYnF9kRoQb90v4Dxrj5pEbLVDBs3xARt13-L9nESxlxDTeMQ-J9eHngnGF9KwZTR1LwViU_oEQYjd4_sjcWXJ_JoDVyp0FoImrxlv1GM0S9KvU_m3qakCg1eLNCEj-VeoJNcY119RFoULBjDce-5li3mY7Z1PmFhaSUg_beWHza7SvgSXuBgoqjs2T7i7STQ6nznS1dnQTcAIvNYIFQMotfTkM47SRWR7MYscKDJ1qLSvuS9miwDVUkgxs4ZaMYvAFcQ2NNzc7To7FDLp3z5JleuGpI0Wcs0KG2topFiVdBcTKTlCiWS70VgG4B4tDv-xsk8YTN4N3FXAhsND_fzaEasmYoCKNmf5-9qyOZLP2Kq42wtIhgoPQj0X6KplxWXW91BHNJGRkaI08uBhaWVhEyZcJJhhMzaRkVD4giRjmRZh8HVqx_dO6801bJyXmo-5leh7_1wX2RmNfDNW71R0WbaCbhb3UdTkZyAAnH1aAHKlU5PcMETKrxTd4BwxuGpDIQFeuEP58UsGe4_ybJhw7tZC9zqgSKA84bZcWXIBhhexkJ65_3XGJj-H2JEdhHjaDL8a69OkOQrCGTD16CsMxzS9nT4NWA_Mihj0nOsEeh11A0JWxIbV3v-Nvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=E9gUMnqxjhln202zbPPxutWQBWdXm34pDB_ors6JPtA-nrV1WYnF9kRoQb90v4Dxrj5pEbLVDBs3xARt13-L9nESxlxDTeMQ-J9eHngnGF9KwZTR1LwViU_oEQYjd4_sjcWXJ_JoDVyp0FoImrxlv1GM0S9KvU_m3qakCg1eLNCEj-VeoJNcY119RFoULBjDce-5li3mY7Z1PmFhaSUg_beWHza7SvgSXuBgoqjs2T7i7STQ6nznS1dnQTcAIvNYIFQMotfTkM47SRWR7MYscKDJ1qLSvuS9miwDVUkgxs4ZaMYvAFcQ2NNzc7To7FDLp3z5JleuGpI0Wcs0KG2topFiVdBcTKTlCiWS70VgG4B4tDv-xsk8YTN4N3FXAhsND_fzaEasmYoCKNmf5-9qyOZLP2Kq42wtIhgoPQj0X6KplxWXW91BHNJGRkaI08uBhaWVhEyZcJJhhMzaRkVD4giRjmRZh8HVqx_dO6801bJyXmo-5leh7_1wX2RmNfDNW71R0WbaCbhb3UdTkZyAAnH1aAHKlU5PcMETKrxTd4BwxuGpDIQFeuEP58UsGe4_ybJhw7tZC9zqgSKA84bZcWXIBhhexkJ65_3XGJj-H2JEdhHjaDL8a69OkOQrCGTD16CsMxzS9nT4NWA_Mihj0nOsEeh11A0JWxIbV3v-Nvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب بشأن حماس: ‏عندما ولدوا، خرجوا وفي أيديهم رشاش.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79135" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
‏ترامب عن محمد بن زايد: ‏محمد في الإمارات مقاتلٌ لا يُستهان به. كان يُلقي القنابل الأسبوع الماضي، فقلتُ: "من بحق الجحيم يُلقي كل هذه القنابل؟"، كانت الإمارات. إنه مقاتلٌ بارع.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79134" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79133" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=ObPOazdZukEEpUwXrQiRd26fP_Ooc9pCt_XpY-XikqDc8Eh4NaKNCIlhXe_pAaPLZJ0VoXxXZZmOLxX0bC2G4t7BUGdiMrKCIgV25QUEOdt5_JZ_FXnil9HL8K7X_SCZohrjLoZBJdpRZFmt4UTUQHh2yUlLbORiZ8_N00V6H3Edbg8BrG-m51BroFPdpu09IgRwkWG6HBx71P9AyEEPBcoE9QFIZum5fSRN1Zk9iaf44TQv9PvpW2CZUuH3Y2M38Qrz4yTDTVDV8t6-DR0t8lIgeZltQmdRGmf01s3HUBCB9Zu6Zk_N3amWPru2JJeAvvh5hHaQG1KMCBXXPowSoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=ObPOazdZukEEpUwXrQiRd26fP_Ooc9pCt_XpY-XikqDc8Eh4NaKNCIlhXe_pAaPLZJ0VoXxXZZmOLxX0bC2G4t7BUGdiMrKCIgV25QUEOdt5_JZ_FXnil9HL8K7X_SCZohrjLoZBJdpRZFmt4UTUQHh2yUlLbORiZ8_N00V6H3Edbg8BrG-m51BroFPdpu09IgRwkWG6HBx71P9AyEEPBcoE9QFIZum5fSRN1Zk9iaf44TQv9PvpW2CZUuH3Y2M38Qrz4yTDTVDV8t6-DR0t8lIgeZltQmdRGmf01s3HUBCB9Zu6Zk_N3amWPru2JJeAvvh5hHaQG1KMCBXXPowSoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لدينا القدرة على الوصول الى اليورانيوم المخصب في ايران.  لدينا عدد القنابل النووية الأكبر في العالم ونأمل عدم استخدامها.  ‏من يبيعهم سلاحاً نووياً سيُقصف هو نفسه، إذا باعوا سلاحاً نووياً، فقلة قليلة فقط قادرة على ذلك، ستُقصف.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79132" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب عن إيران: سوق الأسهم رائع للغاية. وفي كل مرة قلنا فيها شيئًا مذهلاً، مثل "سنقوم بتسوية الأمر"، كان يرتفع.   وفي كل مرة، في كل مرة قلنا فيها شيئًا سلبيًا، مثل، "خمنوا ماذا، لن نكون قادرين على تسوية الأمر"، كان ينخفض — بشكل كبير جدًا، كبير جدًا جدًا. …</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79131" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=bNpnWRYoCAEkAYGU0DbTWh5FtWZfbnSKj6mTwSPPbrGu-Qw8Iz1p3D_7oXOInHXXvO-7P0UiDVHpBkZrkJkfuJ4n6ADJeqJhxMkmF8SUgRpNzBU8LDHCwWv2eqOI_FKunJLFKM8_-CzZ2XTrNI61KsT5HMMJciL6IFlSrvIaX3MYPqegu_EhsdLwOuNID2rCkMNOsAqsS_sUbVk_vRri0JDRtGkAq9dKebxSrNN2Ay4zuqiSYxP5X0iTiQKdSkphtmTOZpmXdFAGN14f1fVl0xGCll9uTSp8SqKrdu6FY04O1e8NXQDgR9UOM7MNbw2hpA1Hua2CPIhotS6HnAo9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=bNpnWRYoCAEkAYGU0DbTWh5FtWZfbnSKj6mTwSPPbrGu-Qw8Iz1p3D_7oXOInHXXvO-7P0UiDVHpBkZrkJkfuJ4n6ADJeqJhxMkmF8SUgRpNzBU8LDHCwWv2eqOI_FKunJLFKM8_-CzZ2XTrNI61KsT5HMMJciL6IFlSrvIaX3MYPqegu_EhsdLwOuNID2rCkMNOsAqsS_sUbVk_vRri0JDRtGkAq9dKebxSrNN2Ay4zuqiSYxP5X0iTiQKdSkphtmTOZpmXdFAGN14f1fVl0xGCll9uTSp8SqKrdu6FY04O1e8NXQDgR9UOM7MNbw2hpA1Hua2CPIhotS6HnAo9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نتنياهو ينفعل قليلاً أحياناً، لكنه كان شريكاً جيداً.  ‏نحن الشريك الكبير، وهو الشريك الصغير جداً.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79130" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=axnQ25ELKrI194IU7LC3YWZAM5gRBv1LUYdQaUseMq5Odbv8SDiq__qtEG38KPEpnWuptDo2wxo4e_c1p5XNmqMv6BIzy83wCs5VnhIpK0sGNwlRdNuynv5tgQZFYeQ-AyiTsKaFXUvAiE5gqDyJo9kWGL6zHWnaNcuSpcM1DaJ3VmA4I6_Fa1cGMFL7DT2AsE9lZGCCy-_ZEWtPZLDZJvTYedLLVQ_EIEfIbwpkMyotnuPfsmM_2f0Dvr0Bu72YLheydGcsLuiDHk4JDp-iubryAJyRFtjKPm4nuhwYbmMJ4h18hgyWpRcdCQac9iLOOKD9ROu7VcDCpRw9lOHAMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=axnQ25ELKrI194IU7LC3YWZAM5gRBv1LUYdQaUseMq5Odbv8SDiq__qtEG38KPEpnWuptDo2wxo4e_c1p5XNmqMv6BIzy83wCs5VnhIpK0sGNwlRdNuynv5tgQZFYeQ-AyiTsKaFXUvAiE5gqDyJo9kWGL6zHWnaNcuSpcM1DaJ3VmA4I6_Fa1cGMFL7DT2AsE9lZGCCy-_ZEWtPZLDZJvTYedLLVQ_EIEfIbwpkMyotnuPfsmM_2f0Dvr0Bu72YLheydGcsLuiDHk4JDp-iubryAJyRFtjKPm4nuhwYbmMJ4h18hgyWpRcdCQac9iLOOKD9ROu7VcDCpRw9lOHAMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: أبلغنا الإيرانيين بأننا سنعود للقصف إذا لم يلتزموا.  ‏القادة الجدد لإيران أذكياء، بل أذكياء جداً. ‏إنهم أقل تطرفاً بكثير. أعتقد أنهم يحبون وطنهم حقاً. إنهم طيبون.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79129" target="_blank">📅 19:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=PPRW0SO9FAxF6KgrvNmRkUhOFzf9OqIWseGqttfdgOKx_cLJ1HGQ_Ge1FwqvyqAqTRdpmMeh28El0-gt72xZvUY6-FQNmK19NOTZ1wo-Ef4el3KDUXJ9L2dm_cqewbxKAWZE67h3QKl_M6UCxmeOB45ic3RiRI3mQHJ6aSgqByZzgjW6g4cnvCklFeJXIQqAto8euij_BKsjTsZFltUfQypVFrhEQzfqA4POpP7xUVKqkM3jZNV0_7lnSYT7kmqGV-tJ2GpGKx-Gpetdo3KMssMHNEvX6Xb2dLlCQlUl63b5Gxo0yg-hM5TohABt40XtiuOw_TIWmwbKNfPXYb0FUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=PPRW0SO9FAxF6KgrvNmRkUhOFzf9OqIWseGqttfdgOKx_cLJ1HGQ_Ge1FwqvyqAqTRdpmMeh28El0-gt72xZvUY6-FQNmK19NOTZ1wo-Ef4el3KDUXJ9L2dm_cqewbxKAWZE67h3QKl_M6UCxmeOB45ic3RiRI3mQHJ6aSgqByZzgjW6g4cnvCklFeJXIQqAto8euij_BKsjTsZFltUfQypVFrhEQzfqA4POpP7xUVKqkM3jZNV0_7lnSYT7kmqGV-tJ2GpGKx-Gpetdo3KMssMHNEvX6Xb2dLlCQlUl63b5Gxo0yg-hM5TohABt40XtiuOw_TIWmwbKNfPXYb0FUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:  حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.  ‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.  أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.  ‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه -…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79128" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=UpYw4l_W3JtzGrtm8-G_O5Y1wuX4TV2fLbY6YKEN1Zy0jivp5f67r9npV2mnDEN29cBash5jI_7UsQnNOmnz-OTFrKqdxXRAaVd-LpNk9HzTn80BA-dxvqtIS2VYy1warpiNgV1LS0EwqlQThwZTQ8ze2zRqFcaS_-otxwIalp0yBKUpFP-Ubjnld4pXD7BBW8TKZoOVPc1oU8OxCoCFIq1_BxNGO_q8OuuQAU3cTAumzXeIId84TzXJmVTGJloo4Qp_cIT7YcieYU_fu_L4f_fSatf1kbIZFfapbDm7MXS-LJHEIqqfLZryRN_-YlN2_sDQl8puFDAiN1gDewu_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=UpYw4l_W3JtzGrtm8-G_O5Y1wuX4TV2fLbY6YKEN1Zy0jivp5f67r9npV2mnDEN29cBash5jI_7UsQnNOmnz-OTFrKqdxXRAaVd-LpNk9HzTn80BA-dxvqtIS2VYy1warpiNgV1LS0EwqlQThwZTQ8ze2zRqFcaS_-otxwIalp0yBKUpFP-Ubjnld4pXD7BBW8TKZoOVPc1oU8OxCoCFIq1_BxNGO_q8OuuQAU3cTAumzXeIId84TzXJmVTGJloo4Qp_cIT7YcieYU_fu_L4f_fSatf1kbIZFfapbDm7MXS-LJHEIqqfLZryRN_-YlN2_sDQl8puFDAiN1gDewu_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:
حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.
‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.
أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.
‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه - كل شيء وأكثر من ذلك بكثير.
‏أعتقد أن القادة الإيرانيين سيتصرفون بشكل مختلف تماماً.
إذا لم نقم بهذه الصفقة، كان بإمكاننا إسقاط المزيد من القنابل لمدة أسبوعين أو ثلاثة أو أربعة أسابيع أو سنتين أخرى.
لو واصلنا القتال ما كان مضيق هرمز ليفتح إطلاقا.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79127" target="_blank">📅 19:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
مشروعهم في لبنان إنهاء حزب الله عسكرياً وثقافياً وسياسياً واجتماعياً وشعبياً ليسهل لهم ابتلاع لبنان، ونتنياهو أعلن صراحة أنه يريد إسرائيل الكبرى.
لم نمكن إسرائيل من تحقيق مشروع إسرائيل الكبرى فنحن كسرناه.
عدد آليات العدو المستهدفة 518 آلية وعدد الطائرات المستهدفة 85 حيث أسقطنا 12 مسيرة و12 محلقة وأصبنا مروحية.
لا وجود لمناطق صفراء أو حمراء وعلى إسرائيل أن ترحل.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79126" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
وكالة إرنا: لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79125" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ يوم الجمعة 19 يونيو/حزيران. ولا تزال آلية إضفاء الطابع الرسمي على الاتفاق قيد المراجعة من قبل الجهات المختصة في البلاد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79124" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79123">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc2cjGdOlhAYX1dcSrcd7-ezHey2N3KeGKoOVLb6z79CLdHSp9H-hZiJ3zub-PxcqLpECNxc5fvn_qnTRHJa3kdPSd_rVzk6lshuKF7hqyPnpydxLi-LWta6BMbdOefhwElbCfFi29vheqtm7TMKT-5hmOpEXf0g6QnY7_G_ut5UvUHxaNWPwbIY1cAbNMYq8qZTjhv2lN386kmS2KM25zpHIBJBdy3POMuRW2e8K0-MJNB19LcJHjvglmxrm9R1griR7zwZ-mFmFPktpcqv_HwRmHXIjydt-UUd2WRU4UkZ7KA_sN_Zb2OJ1NNJtR8D6WCsuA6Fi8LQffIVnDwskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الغاء رحلات جوية من مطار النجف الأشرف في العراق إلى عدد من المدن الإيرانية دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79123" target="_blank">📅 18:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79122" target="_blank">📅 18:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=ZWIMYj1_xREGh-6Wl3REJmcPjLa-bdxm1J7Di2zib2P2eMEgD9qBzFP-36o3jXrXND5IImnSbddIZcMbWjOcTy83tkzDll82oMZY8Nehd26cIb289lPjvouT7nRxHSWfN816LNDuL-HQpWk60Uc6wpDESjHvZl76OINbofT1gLODrEa0YAMqmwvCcfmL0YQTL-sRxVYu2eTBiIDcSEjnJiIKGsrdFGdSuXDoh8HjeqJI3gpm61gWA-dqbSRHYjNbrO-yaTKpFJio0ptGfRoKkZKZiU3agVnl0NB8ssqHLAGwOYbbobUC_DhYZE8hw2y532ydYNYtdTo0S5N3w-yC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=ZWIMYj1_xREGh-6Wl3REJmcPjLa-bdxm1J7Di2zib2P2eMEgD9qBzFP-36o3jXrXND5IImnSbddIZcMbWjOcTy83tkzDll82oMZY8Nehd26cIb289lPjvouT7nRxHSWfN816LNDuL-HQpWk60Uc6wpDESjHvZl76OINbofT1gLODrEa0YAMqmwvCcfmL0YQTL-sRxVYu2eTBiIDcSEjnJiIKGsrdFGdSuXDoh8HjeqJI3gpm61gWA-dqbSRHYjNbrO-yaTKpFJio0ptGfRoKkZKZiU3agVnl0NB8ssqHLAGwOYbbobUC_DhYZE8hw2y532ydYNYtdTo0S5N3w-yC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇳
‏ترامب: سنساعد الهند إذا تعرضت للهجوم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79121" target="_blank">📅 17:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1QFlkaLyr82uz4-tuGkdVKrPysE2u54pYfAsTNf_cSbn7qkVEldFVRW9Wmy0JOpzdwRbSehDky0CBcfYK37lt7SBMV9IyPxeBJFsL_zeUHx6jRV9Uk-jOVEwvySh-tJdr17mjYILB1vJOJayb7S8ud9mjfJbRKj6g036UVL4pmpxDUVNCi8nEaR10hQV1MBTWdPo29WUoHMkgchZIrTTfWSkKHoz5Thc72nCDiD0hiPDep9eUjZ_hX_xMjFa_AgVgaiKAAMOnH8MU15wvQ_uaJTmfGplrO0V8oTbqqsbGbQ6VoljQZth3C_glG7XNfbXB6PygtklSwMCDlVIzqRd3sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1QFlkaLyr82uz4-tuGkdVKrPysE2u54pYfAsTNf_cSbn7qkVEldFVRW9Wmy0JOpzdwRbSehDky0CBcfYK37lt7SBMV9IyPxeBJFsL_zeUHx6jRV9Uk-jOVEwvySh-tJdr17mjYILB1vJOJayb7S8ud9mjfJbRKj6g036UVL4pmpxDUVNCi8nEaR10hQV1MBTWdPo29WUoHMkgchZIrTTfWSkKHoz5Thc72nCDiD0hiPDep9eUjZ_hX_xMjFa_AgVgaiKAAMOnH8MU15wvQ_uaJTmfGplrO0V8oTbqqsbGbQ6VoljQZth3C_glG7XNfbXB6PygtklSwMCDlVIzqRd3sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب: نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79120" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المجلس الإسلامي الأعلى في العراق:
استجابةً لنداء الوفاء.. بلدية طهران تُلبي مطالبات المجلس الأعلى وتشهد بغداد تشييعاً مهيباً للقائد الشهيد الامام الخامنئي*
استجابةً للمطالبات والنداءات الروحية والوطنية المتكررة التي أطلقها المجلس الأعلى الإسلامي العراقي، وتأكيداً على عمق الروابط الوجدانية والجهادية التي تجمع الشعبين الأبيين، أعلن رئيس بلدية طهران رسمياً عن تلبية هذه الدعوات المباركة.
حيث تقرر أن تشهد أرض العراق الطاهرة ،أرض المقدسات والشهادة مراسم تشييع جثمان القائد الشهيد، الامام الخامنئي، وذلك في تاريخ 8 تموز (يوليو) 2026.
وتأتي هذه الخطوة التاريخية تلبيةً لقلوب العراقيين التي نبضت بالوفاء لقائدٍ عاش مدافعاً عن قضايا الأمة، ليمتزج تراب العراق بفيض وداعٍ مهيب يليق بمقام القائد الشهيد، وسط ترقب واسع لمشاركة ملايين المحبين والمقاومين في هذا الوداع الأخير.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79119" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79118">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13deced209.mp4?token=SuTYJibOMadK1mb_bh_Oju1Vo3KSciVJNpdmZ1MJtzpo39LuajjcUwGjKRvI9HUilraUD7Qp3wpfrAomA-4WGM8CLDhUFRg4VkVylh2otMwrMBK9sbiwCsORirV6PcSyyBa7KdCxDg1YkKtSngifMsZgtaIuFg7xbP4mDONJ0_oeJS15viz_sEXLkJrQwe5eUR5_suDia57xET9lFIDwSV3hgHA7FKZiC82weJ9jsS9P2rHouMtmDQhBSHfpbaG0xDmYkHsJ3qwoVFRoAui8NkaV7hBEIEjQcwSTt1hibZzK2ygm9qWuyrrqP1N7U5INSdzfbKcKVb_efQHYeHB3xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13deced209.mp4?token=SuTYJibOMadK1mb_bh_Oju1Vo3KSciVJNpdmZ1MJtzpo39LuajjcUwGjKRvI9HUilraUD7Qp3wpfrAomA-4WGM8CLDhUFRg4VkVylh2otMwrMBK9sbiwCsORirV6PcSyyBa7KdCxDg1YkKtSngifMsZgtaIuFg7xbP4mDONJ0_oeJS15viz_sEXLkJrQwe5eUR5_suDia57xET9lFIDwSV3hgHA7FKZiC82weJ9jsS9P2rHouMtmDQhBSHfpbaG0xDmYkHsJ3qwoVFRoAui8NkaV7hBEIEjQcwSTt1hibZzK2ygm9qWuyrrqP1N7U5INSdzfbKcKVb_efQHYeHB3xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل:
هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب:
نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79118" target="_blank">📅 17:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله:
بسم الله الرحمن الرحيم
(يَا أَيُّهَا الَّذِينَ آمَنُوا إِن تُطِيعُوا فَرِيقًا مِّنَ الَّذِينَ أُوتُوا الْكِتَابَ يَرُدُّوكُم بَعْدَ إِيمَانِكُمْ كَافِرِينَ * وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ آيَاتُ اللَّهِ وَفِيكُمْ رَسُولُهُ ۗ وَمَن يَعْتَصِم بِاللَّهِ فَقَدْ هُدِيَ إِلَىٰ صِرَاطٍ مُّسْتَقِيمٍ * يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ حَقَّ تُقَاتِهِ وَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسْلِمُونَ)
مع اطلالة شهر محرم الحرام ودخول أيامه المثقلة بالأسى والبطولة، حيث تجسَّدَ جهاد الإمام الحسين (عليه السلام) وأهل بيته وصحبه بأوضح صوره في طف كربلاء، وأثبتوا فيه أن «الجودُ بالنَّفْسِ أَقْصَى غَايَةِ الجُودِ»، لتبقى تلك التضحيات العظيمة منارةً تضيء درب الأحرار في كل زمان ومكان، وتعلّم البشرية جمعاء أن الحياة بلا كرامة لا قيمة لها، وأن الثبات بوجه الطغاة أمر إلهي لا يجوز تركه أو الحياد عنه مهما بلغت التضحيات وعظمت البلاءات.
وامتداداً لهذا النهج الحُسيني الخالد، ننهي جولةً أخرى من جولات الحرب ونخرج منها بانتصار ناجز، وندرك تماماً أن المعركة لم تنتهِ بعد، وأن أمامنا جولات ومحطات هي أكثر خطورةً وضراوةً؛ لذا، يفرض علينا الواجب والوعي أن نكون على أهبة الاستعداد لأي طارئ، متمسكين بسلاحنا، وأيدينا على الزناد.
إن هؤلاء الأعداء من الوحوش البشرية لا يمكن الوثوق بعهودهم أبداً، وأن التغافل عن مكرهم هو الغباء بعينه؛ فالمعادلة واضحة: لن يرضوا عنا ولن نرضى بظلمهم، فكيف نرضى عنهم وقد قتلوا إمامنا الخامنئي في وضح النهار وبين ظهرانينا، وقتلوا العبد الصالح عروة المجاهدين الوثقى السيد حسن نصر الله، واغتالوا علماءنا، وحصدت آلتهم الإجرامية أرواح عشرات الآلاف من شيوخنا، وشبابنا، ونسائنا، وأطفالنا في غزة، ولبنان، واليمن، وإيران، وسوريا، والعراق؟!
فأيُّ صفحة تُطوى؟ وأيُّ جريمة تُنسى؟ وأيُّ مجرم يُسامح؟! لا سامحَ الله من يسامحهم. إن قتالنا مع الباطل ممتدٌ وفي معارك صفرية تطيح بها الرؤوس وتحذف فيها دول، ليرتسم من خلالها عالم جديد، ونحن نعلم يقيناً أيَّ عالم نريد؛ عالم تسوده العدالة والكرامة وتتحطم فيه عروش الظالمين. إنها معركة الحق ضد الباطل، ولن تنتهي حتى قيام الساعة.
أما أولئك الذين وقفوا مع الخنازير وأبناء القردة، فعليهم أن يترقبوا أمر الله وحكمه فيهم، فلا نامت أعين الجبناء والخونة، وأنّ خدعة (الصفحة الجديدة) لن تنطلي علينا، (يُخَادِعُونَ اللَّهَ وَالَّذِينَ آمَنُوا وَمَا يَخْدَعُونَ إِلَّا أَنفُسَهُمْ وَمَا يَشْعُرُونَ).
وفي الختام، نتوجه بآيات الفخر والاعتزاز والامتنان إلى صناع النصر وبناة المجد:
شكراً لحزب الله، درة تاج المقاومة الإسلامية وعنوانِ عنفوانها.
شكراً للقوات المسلحة الإيرانية الشجاعة.
شكراً لرجال اليمن، أهل الصدق والوفاء.
شكراً لكل أبناء المقاومة الإسلامية في فلسطين، والعراق، والبحرين، وأرض الحجاز عامة، وخاصة أهل الشام.
وشكراً لمجاهدي التبيين الذين أبلوا بلاءً حسناً في معركة الحق، ولكل الأحرار من سياسيين، ورجال عشائر غيارى، وعلماء دين مخلصين، وإلى شعوب أمتنا الإسلامية الذين نصروا قضايا الأمة العادلة، مجسدين أسمى معاني التضامن والوحدة في هذه المرحلة المصيرية.
وعظيم الامتنان والتبجيل لمراجعنا العظام الأعلام، الذين وقفوا موقفاً تاريخياً، مشرفاً، شجاعاً، وواضحاً لا لبس فيه؛ فبيّض الله وجوههم في الدنيا والآخرة كما بيّضوا وجوه الأمة، وجزاهم الله خير الجزاء عن الإسلام وأهله.
﴿سَلَامٌ قَوْلًا مِّن رَّبٍّ رَّحِيمٍ﴾
الأمين العام لكتائب حزب الله
17 حزيران 2026 ميلادية
الموافق لـ  1 محرم 1448 هجرية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79117" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrNGAJ-4HrITZTNtaL922B4hkiA4TCYj7x-Vvw6-xuzEeLMbk84AoOCkmmn7czd5XO0TBFQnYzMNlvPBkTyav8zXEjIhChsDIk9WIYsbixwCaeYbZgunOpX32WhPioguTHgbQKys8V1cMhu81NyY-6PGSQjhsNsoEYB_SORyqNkiPMMMGHUGrZnTkRjkzkKd6jeCglHb3fJ0m5zKWtOdjPHVuz-iELy8N0OOzCWL0LzehHQw9YjcA-vZgzp5JpDUC3Wb14A_XXu59_D_UhXT3BlXONAgTUkeoT9V3RfoVMTOWugL9Livp4W5YqeCip8vrYLKH6c__JrzizW3Uj-_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
سأعقد مؤتمراً صحفياً خلال 45 دقيقة من فرنسا. ثم سأتوجه إلى فرساي لتناول العشاء مع القادة الفرنسيين والأوروبيين الآخرين، ثم أعود إلى الوطن الليلة! كانت الرحلة ناجحة للغاية، ولكن ما أراد الناس التحدث عنه في الغالب هو حقيقة أن إيران لن تمتلك سلاحاً نووياً، وأن مضيق هرمز سيُفتح على الفور! أرقام رائعة في جميع فئات اقتصاد الولايات المتحدة مع عدد أكبر من الناس يعملون اليوم أكثر من أي وقت مضى. يتم استثمار أكثر من 19.1 تريليون دولار في الولايات المتحدة الأمريكية مع المصانع وكل شيء آخر يحدث، ولكن الأهم من ذلك، أن أرقام سوق الأسهم الأخيرة مرتفعة للغاية بسبب التسوية، وبالمثل، أسعار النفط تتراجع</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79116" target="_blank">📅 17:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79115">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي يعلن اصابة 5 جنود صهاينة في جنوب لبنان</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79115" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79113" target="_blank">📅 16:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79112" target="_blank">📅 16:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79111" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=IRa4ayt2F8tAdAB1KeRUoVQtUbhpwthgeRZpNR1Z-t-CBojamOajz0futWCIsiZVWYCVgVeZrX8PwSmTjVV1i_vLVFTQ0C0ItFwJyyP7VX2JxNLygxlJcNPP4NN9t8da0vky_wK2XxaudLXMWreXnbxyoSeO09xpYE3hr4Jq--a0yiF3VmbdlPULP0j1ijN6v5aZ26-l3AOGWJk_S5J9UnrLo8BkPqJlAObmW-Vrci6pCIwcuqc9mzk6sY_nvHiBuyQ4rYOsVXy01YnTeiJ7-LdL1QK3hrSLfPn2QE3sFSxHMNdCnmHGGoxnFvEA14tB6He84Bl2RGGzIcZu87OS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=IRa4ayt2F8tAdAB1KeRUoVQtUbhpwthgeRZpNR1Z-t-CBojamOajz0futWCIsiZVWYCVgVeZrX8PwSmTjVV1i_vLVFTQ0C0ItFwJyyP7VX2JxNLygxlJcNPP4NN9t8da0vky_wK2XxaudLXMWreXnbxyoSeO09xpYE3hr4Jq--a0yiF3VmbdlPULP0j1ijN6v5aZ26-l3AOGWJk_S5J9UnrLo8BkPqJlAObmW-Vrci6pCIwcuqc9mzk6sY_nvHiBuyQ4rYOsVXy01YnTeiJ7-LdL1QK3hrSLfPn2QE3sFSxHMNdCnmHGGoxnFvEA14tB6He84Bl2RGGzIcZu87OS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79110" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الحكومة السويسرية: توقيع مذكرة التفاهم سيعقد بمشاركة ممثلين رفيعين عن الولايات المتحدة وإيران وقطر وباكستان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79108" target="_blank">📅 15:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79107" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKD6LyuOPQpZbJpY0FzUgKQIzEPL9nMu06GdbpyNJC69m6F4TR1b9WT462zahWu1pPD-XkkGJukHGiqnf-fF9ynAsynLkn-vlcf1pswIzDZUYLFL8ShFO-XSW6Y4dZ8onBuQtYsm-qCITm4jNFcsYiJx2bl30gduEXfNui0LALDvfT2crC1Q7W9HH8Xt44nuDxkVa1QsEGo-b50K4XaqOfF6sPnwN2cL6RJFZ6sGXtarvgq7C_IchIo421mr_bJH1zLGzddvmszG3RqtWU_oWPrb-7SiinOLzo0SonqPTFZQCNEoh02Cc6uKylfV8hW3uN1wAcnbNomcpQ_0N99rKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختفوا وابتلعتهم أربيل
!
العشرات من شباب الوسط والجنوب بسبب باج معهم من الحشد الشعبي او صورة لسيد حسن بالهاتف او الشك فقط او العثور على اسمائهم ضمن قوائم رواتب الحشد الشعبي ادى الأمر إلى اختفائهم ، وسط صمت مخزي من القوى السياسية الشيعية الشريكة معهم في الوزارات وتقاسم الكعكة
المواطنون يناشدون الشيخ علي الزيدي مدير الامن والانضباط
بالحشد
و قادة الإطار التنسيقي ومن لا نزال نحسن الظن بهم لا سيما الشيخ
همام حمودي
و
إلحاج العامري وسيد قاسم الاعرجي لمتابعة امر المعتقلين الذين تجاوز عددهم ٧٠ شخص حتى اللحظة
!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79106" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#ترفيهي
الرئيس اللبناني:
لا خوف على السلم الأهلي ومن يهدد به أصبح ضعيفا وهو يبغي إخافة الآخر ليبقى موجودا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79105" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
تنفرد نايا بنشر مشاهد في حرب رمضان من مدينة إيلام الحدودية مع العراق تظهر انطلاق صواريخ توم هوك كروز مرورا بسماء العراق ؛ الصواريخ رصدت حوالي الساعة 8.50 بتوقيت العراق …
يوم ٢٨ فبراير</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79104" target="_blank">📅 15:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
محكمة جنايات النجف تصدر حكما بالسجن الشديد 4 سنوات لمدير مؤسسة السجناء السياسيين في النجف</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79103" target="_blank">📅 15:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79102" target="_blank">📅 14:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇸🇾
🇺🇸
ترامب: تحدثت مع الرئيس السوري حول إمكانية القتال ضد حزب الله.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79101" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران: النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79100" target="_blank">📅 14:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران:
النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79099" target="_blank">📅 14:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
ترامب يواصل جعل نفسه اضحوكة للعالم:
أتابع كأس العالم وأرى دولاً مختلفة من شمال أفريقيا مثل المغرب والجزائر وتونس ومصر. إنهم موهوبون وسريعون للغاية، لكنهم منفصلون. تساءلت: لماذا لا تتحد دول شمال أفريقيا لتشكيل فريق واحد كبير؟ لو فعلوا ذلك، لفازوا بالبطولة بسهولة! هذا يعكس نقصاً في القيادة هناك. ربما بعد أن ننتهي من إنقاذ أمريكا سأذهب وأترشح لرئاسة أفريقيا ، سنربح الكثير!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79098" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
🌟
الجمهورية الاسلامية تحتفي بطفل عراقي باع دراجته الهوائية وتبرع بثمنها نصرة للحق على الباطل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79097" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
3 ناقلات نفط إيرانية تبلغ حمولتها 5 ملايين برميل من النفط الخام عبرت مضيق هرمز</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79096" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=DUnFVQvFro8TCb8xyYcme-VDQxw_wkItTHnecwoLzqZZAyMTn497sQXUAOUoW6Dm0vub6LpPxiwemtJACi5Aa5TOceGTvOy9AY_H1EZ6OVs-gBHYv1thOw-lDW8xKBSdDCKKw59Rj6HWBVVlZKu3hQVwrcYRudlxeN1gBKCBJ8vTfn7D_qENp4N042BaxuuVD1GOFM_R7uLCRDF9ApDm9xh-kAa2b7pbAlmWOpOipelxTeSUUifxlH1EHWvEd0pgw4YK_PZWNBFFL-wWfMOiknl_lvbMtYifAx4vbMFovwuA1DHdy-SM71ZH8KW_k8GzPTALWElYtEsl8Y89aTxd2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=DUnFVQvFro8TCb8xyYcme-VDQxw_wkItTHnecwoLzqZZAyMTn497sQXUAOUoW6Dm0vub6LpPxiwemtJACi5Aa5TOceGTvOy9AY_H1EZ6OVs-gBHYv1thOw-lDW8xKBSdDCKKw59Rj6HWBVVlZKu3hQVwrcYRudlxeN1gBKCBJ8vTfn7D_qENp4N042BaxuuVD1GOFM_R7uLCRDF9ApDm9xh-kAa2b7pbAlmWOpOipelxTeSUUifxlH1EHWvEd0pgw4YK_PZWNBFFL-wWfMOiknl_lvbMtYifAx4vbMFovwuA1DHdy-SM71ZH8KW_k8GzPTALWElYtEsl8Y89aTxd2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد قضينا على رجل يدعى سليماني. هل تعتقد أن هذا كان سيحدث لو كان على قيد الحياة؟ لقد كان عبقرياً</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79095" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=oAiKbz6aJbwx6fVDho1ljvmacpwpGoKmH_kaWn__ACbie-vbCpbq9Nr-ASCYT20NfXb57hnbAHbWscPrJb_ypymw4T3e5ugUkU18rZrS1l90ThtZ8eFaIuytEmhAISdyGOm3pdIhjQmUniJcGTSaFZSA9j-QSNlpnlV8jqrSstIN8YAzySK00eH1sLtLiw5XTFo3DHfrPfr-DkrKopGAtKLowVVZnBKS5841oAzVw0Cy_7A_yuYwiSmHYSYC4c_EVvzL_wD7_3T6V_AsEpLwUgy0GLCAkxN64F0bnBe5wYsDRzeT4ikW-_i9s4p-AWdhqJ3WldozxcY4Av3-y440tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=oAiKbz6aJbwx6fVDho1ljvmacpwpGoKmH_kaWn__ACbie-vbCpbq9Nr-ASCYT20NfXb57hnbAHbWscPrJb_ypymw4T3e5ugUkU18rZrS1l90ThtZ8eFaIuytEmhAISdyGOm3pdIhjQmUniJcGTSaFZSA9j-QSNlpnlV8jqrSstIN8YAzySK00eH1sLtLiw5XTFo3DHfrPfr-DkrKopGAtKLowVVZnBKS5841oAzVw0Cy_7A_yuYwiSmHYSYC4c_EVvzL_wD7_3T6V_AsEpLwUgy0GLCAkxN64F0bnBe5wYsDRzeT4ikW-_i9s4p-AWdhqJ3WldozxcY4Av3-y440tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الإيرانيون خدعوا أوباما وحصلوا على المليارات من الدولارات</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79094" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترامب: إثيوبيا عاملت مصر بطريقة غير منصفة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79093" target="_blank">📅 14:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6EcNUEVi-mq9tz7FN-RTQbJ3jyppWvHYneO9WI9aMgyNsy4BpDCD68GWOawwMacyr-OInLXmHznFTcteOxDzbqM9Rzh5RrS6VmB7MIIIEkWMZBuCkjolwc6Hpm1SYLr6E0_xDL7EIojn7xKJrwGQcYgsMveBryZjqW1AfIaUpiSQTJGjt6UYzpbFoPOwPca3glCbKcBc3mvl2naCNU89UwB5CVCJ2JRsg4EoezFkxg3cS6IbkXWxeV6wv3El0hnMApA8N-JnK1llNnxpf4naPZ8M402aF9-7kcCuShsqbYca8rPwq8oq_A9KUkm61iLTEoezG31cJGNHTa5X2ZBwgas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6EcNUEVi-mq9tz7FN-RTQbJ3jyppWvHYneO9WI9aMgyNsy4BpDCD68GWOawwMacyr-OInLXmHznFTcteOxDzbqM9Rzh5RrS6VmB7MIIIEkWMZBuCkjolwc6Hpm1SYLr6E0_xDL7EIojn7xKJrwGQcYgsMveBryZjqW1AfIaUpiSQTJGjt6UYzpbFoPOwPca3glCbKcBc3mvl2naCNU89UwB5CVCJ2JRsg4EoezFkxg3cS6IbkXWxeV6wv3El0hnMApA8N-JnK1llNnxpf4naPZ8M402aF9-7kcCuShsqbYca8rPwq8oq_A9KUkm61iLTEoezG31cJGNHTa5X2ZBwgas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا الزعيم "..
هكذا قال ترامب لقادة مجموعة السبع بعد وصوله متأخرا !</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79092" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79091" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79090" target="_blank">📅 14:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhElkNVxvEFjOyfn6oy1RJtZzBTtlDGaBPVJ5cD5XeDAON9POSh1vYNec1N3VcArloqrOBdn6Bl9zMA76TSDQNtvX3bczu5e5Hz3j_SGnKB2OsMA00bWvim5BeG_hpeVBT6Yg25nxnLS2HWgQCWjCeJni8bmKwoxytK1D8avj-HXa-Al5aERcMK5sQiymnXjezmWINk0nPY35XUFNelkTFj--IBzXGSQZyu05XAxF9IqGGAT2uN4wiYfEii6KVSeQMEoBBaQAH6SU8xncln1Gzei3P5-v25sWdNV7rii6WBo_eTr-npuKF65ro3kbAl6wga8mKZTP57QRgX4MfdxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
وافق الجمهوريون مع الديمقراطيين على إبعاد ويليام بولت، وهو شخص موهوب وعادل للغاية، عن منصب مدير الاستخبارات الوطنية بالإنابة (DNI)، مقابل حصول الديمقراطيين على موافقتهم على قانون مراقبة الاستخبارات الأجنبية (FISA). لكن الجمهوريين تحركوا بسرعة كبيرة في جلسات الاستماع الخاصة بجاي كلايتون العظيم، المدعي العام الحالي للمنطقة الجنوبية من نيويورك، بحيث كان بولت سيغادر منصبه قبل أن يصوت الديمقراطيون على قانون FISA.
والآن يقول الديمقراطيون إنهم سيصوتون ضد قانون FISA. وبالتالي، كان الجمهوريون سيفون بالتزامهم، لكن الديمقراطيين هم من نكثوا بالاتفاق.
بالإضافة إلى ذلك، يجب أن يتم اعتماد المدعية العامة المرشحة حديثًا، جيمي ماكدونالد، والحصول على موافقة ما يُعرف بـ”الورقة الزرقاء” (Blue Slip). وبسبب المواقف غير المنطقية للجمهوريين بشأن هذه الآلية (مع أن الديمقراطيين غالبًا ما يكونون مستعدين لتجاوزها)، فقد لا أتمكن من الحصول على موافقة جيمي، الشريكة الاستثنائية في شركة Sullivan & Cromwell، ولا أريد إبعاد جاي كلايتون عن العمل الرائع الذي يقوم به حتى تتولى جيمي المنصب.
لذلك، ومع إضافة هذا التعديل البسيط، ومن أجل مصلحة الوطن وشعبنا، لن أوافق على قانون FISA ما لم يتم تمرير قانون SAVE AMERICA ACT معه أيضًا.
الأمر ليس معقدًا. في الواقع، وقع الجمهوريون في فخ.
وفيما يتعلق بالموافقة على الوطني العظيم جاي كلايتون، فإننا نلغي اليوم جلسة الاستماع الخاصة بتعيينه مديرًا للاستخبارات الوطنية، ولن نمضي قدمًا بها حتى تتم الموافقة على جيمي ماكدونالد كمدعية عامة للولايات المتحدة.
وفي هذه الأثناء، سيبقى بيل بولت مديرًا للاستخبارات الوطنية بالإنابة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79089" target="_blank">📅 13:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">في تصرف مستفز وخسيس..
قناة AVA الكردية التابعة للبرزاني والتي لديها مقر في بغداد تحتفل بخسارة المنتخب العراقي في مباراته الأولى بكأس العالم عبر بث الأغاني وإظهار أجواء الرقص والفرح داخل الاستوديو!
علما ان المنتخب العراقي يعد اكثر منتخب في العالم يضم لاعبين اكراد ويحترم حقوقهم في الوقت الذي تحرمهم البلدان التي يتواجدون بها من ابسط حقوقهم مثل تركيا ووصلت في بعض البلدان الى سبي نسائهم مثل سوريا الجولاني</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79088" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن: - طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات - طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد - طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79087" target="_blank">📅 12:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFDdaRsAj1nflnM8o5w-jBOVF_15HpXvLfWRzLrAoZ93Gzvink1tEPedUy_YjBSjLAVU64R76qGpMey0r2QHSvCyACA5tUHPDJ098Smh_U-PJ33DbJNwU1h5IdBtOmcm78rJ5L0Jb8UBgkvmJEYSeT34XldHxijmUescOJhIrV3rV6zijco2YPW-Rhn4cVjEgAHHCVjPWMNM8F7tZ0KMV1cUV3Yd-25ywwwf4lBh4yWya8wXpR2o0g_MeicTfmMW3ubCteCnrAy-GvVWMb5t5_tKpQ5TcfPF_N7FGakS47dPSRSfq7tXGYpC1RDoDBVJngk8ieAihNu_d3Jh3KGB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
سفير أمريكا في الكيان المحتل:  الفكرة: ترحيل كل أعضاء حزب الله وحماس إلى "السفينة الأم" في إيران.. النتيجة؟ لبنان وإسرائيل خاليان من وكلاء إيران الإرهابيين. امنح السلام فرصة!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79086" target="_blank">📅 11:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=O4VtAbD2E3pkx-UZypCIA0FItbn6ymbQJJnwGUuwuqZgWg_iTl1gYCMWQ9ijw8_EDcCeNASRS9BVtuf8-6EscZOqI7I3aWMP2VS78af5VGNeMSG-jkmc9p5L31Ovq7oX0cHKtg7XTi-Jj5ss7O68oQQLvkguu2p721djzWNNFhb0_0x6Oh9n6fcHAD3ML5cM0LGEpqwWYLSeuL9ab4Q7_r7X0iRDHawE2e1REc6N4y9Axs_B2jcn-499zpexlHm_9EhFT-s59QQQAJMqGW3xRcfpfzVQyqnLo9HK5Eo_SgunN5JsSHRSgTfxjGQdkPAAquU_CqiHJVbQAYYBkvzhDqH-eP50moKCGRQS0vkjsR_hrIM2CNQT_sWVPJFg7JPyutbWeoC5fLRDs8hj-OH3U_dOpv8g5f2n2iZfnGK4aHw1XsiQnLMZBeGw7ZuEYOxj511rSU3zQqGVx9314KivibKF5H7UYMMHv-sZTNZ4amNfMkssrNnXQlY7JUCWy5HW33QdFxmm-GjlgeqMD0ri3esdc4TcqoONvT-6wg3qGq_sLoX5tqUE6aV7gyhXb_8VruPk752SGEESoJjKawYI0czw38Q3-W8zV_vzFt5cVRGHG7CdvmlZljwv8Qq86qLDt_UZ9tO9jANKbC1EKnv4mBDy_-36xfiMlCRecp-XTyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=O4VtAbD2E3pkx-UZypCIA0FItbn6ymbQJJnwGUuwuqZgWg_iTl1gYCMWQ9ijw8_EDcCeNASRS9BVtuf8-6EscZOqI7I3aWMP2VS78af5VGNeMSG-jkmc9p5L31Ovq7oX0cHKtg7XTi-Jj5ss7O68oQQLvkguu2p721djzWNNFhb0_0x6Oh9n6fcHAD3ML5cM0LGEpqwWYLSeuL9ab4Q7_r7X0iRDHawE2e1REc6N4y9Axs_B2jcn-499zpexlHm_9EhFT-s59QQQAJMqGW3xRcfpfzVQyqnLo9HK5Eo_SgunN5JsSHRSgTfxjGQdkPAAquU_CqiHJVbQAYYBkvzhDqH-eP50moKCGRQS0vkjsR_hrIM2CNQT_sWVPJFg7JPyutbWeoC5fLRDs8hj-OH3U_dOpv8g5f2n2iZfnGK4aHw1XsiQnLMZBeGw7ZuEYOxj511rSU3zQqGVx9314KivibKF5H7UYMMHv-sZTNZ4amNfMkssrNnXQlY7JUCWy5HW33QdFxmm-GjlgeqMD0ri3esdc4TcqoONvT-6wg3qGq_sLoX5tqUE6aV7gyhXb_8VruPk752SGEESoJjKawYI0czw38Q3-W8zV_vzFt5cVRGHG7CdvmlZljwv8Qq86qLDt_UZ9tO9jANKbC1EKnv4mBDy_-36xfiMlCRecp-XTyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
بعد إعلان نتنياهو عن تعزيز تواجده في سوريا.. الاحتلال الإسرائيلي ينصب أبراج مراقبةوتركيب كاميرات مراقبة وأجهزة رصد على قمة تل أحمر بريف القنيطرة السورية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79085" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇱
المحلل العسكري "الإسرائيلي" يوسي يهوشع: يشهد الشارع الإسرائيلي حاليًا شعورًا بالخسارة يفوق ما شهده عقب حرب لبنان الثانية عام 2006.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79084" target="_blank">📅 09:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇬🇷
إعلام يوناني: البحرية اليونانية تستعد لنشر وحدتين بحريتين عند مضيق هرمز</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79083" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=GLDLCYgZs0WTwFuNaxY0PQUTtM0ikMFaBn47jHyPRUD5aWa55K7oEQaCHiw7ss_to5QvWvNfCyIC9tR6Dv1gqCs7a5y9kI5w7kyCagp9njHSCUnK7BBrl_6OMlkAGjR1Q6ktsP2a-QgwGk2aICRL7V40OMGrxHCVXLbl-YfzXsW0FONIUZTzh-Erd3eQ1-ruWotnSF56Tn_9O6QNV-rT9aS4ySPsdOBUpp1P-r256QBTM0z01AlE7xI6vMm-fLeKBvSKKHVmC4-DGP5jnJU1KgmksUnnO9Ca0wv3_wT3BE9SyBosAt1Gd6UFHANWunWr38J6ogjG5gDS7gIvykFqEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=GLDLCYgZs0WTwFuNaxY0PQUTtM0ikMFaBn47jHyPRUD5aWa55K7oEQaCHiw7ss_to5QvWvNfCyIC9tR6Dv1gqCs7a5y9kI5w7kyCagp9njHSCUnK7BBrl_6OMlkAGjR1Q6ktsP2a-QgwGk2aICRL7V40OMGrxHCVXLbl-YfzXsW0FONIUZTzh-Erd3eQ1-ruWotnSF56Tn_9O6QNV-rT9aS4ySPsdOBUpp1P-r256QBTM0z01AlE7xI6vMm-fLeKBvSKKHVmC4-DGP5jnJU1KgmksUnnO9Ca0wv3_wT3BE9SyBosAt1Gd6UFHANWunWr38J6ogjG5gDS7gIvykFqEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
أهالي الجنوب اللبناني العائدون إلى قراهم يتفاجأون بتوغل صهيوني جديد في قرى الجنوب.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79082" target="_blank">📅 09:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني بيزاليل سموتريتش يتحدى ترامب علانيةً: لن يكون هناك انسحاب من لبنان - ليس بحلول الجمعة ولا بعد الجمعة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79081" target="_blank">📅 09:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
جي دي فانس: السعودية تحولت من كونها مرتبطة بـ "انتشار التطرف الإسلامي" إلى أن أصبحت شريكًا مقربًا للولايات المتحدة بعد أن "خفضت ذلك تمامًا" و"حولت بلدهم".
إذا كانت إيران "مستعدة لتغيير سلوكها بنفس الطريقة التي فعلت بها السعودية"، فإن الولايات المتحدة سترغب في أن تكون إيران "دولة ناجحة".</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/79080" target="_blank">📅 09:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79079">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184d624d60.mp4?token=Q4d1QEMCoCaCL7hOJKWW72Y5_H74QObxE_abdkKI1Qpq8a1gShtWwxZ1GD5J_jnPU45iG4XXJnpKVvoQEZZUT5J0LoyjxZoXe0jlM6-nC9sI9GwG5OKZu2emxOvLFV3L3gakttMr801zLsHjj9eq_hnJRLQnGDQQ8Bs6C_uCQvRzkzKDDgl3PYS3af4zGR6Sx__NOeeOdvpczhH5JDrJXEHxb4Lr_3G2JpTK4YQO6t1RopSNhxExbDrn69uSJbs2Ef2iWZ7OCS9u87hRXH_MbwHC0O9eTInjwYnpMm3siepIyfmEzhO81Rj_JgEh3bjTlC5DYk1aAkmFZnnR3HyoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184d624d60.mp4?token=Q4d1QEMCoCaCL7hOJKWW72Y5_H74QObxE_abdkKI1Qpq8a1gShtWwxZ1GD5J_jnPU45iG4XXJnpKVvoQEZZUT5J0LoyjxZoXe0jlM6-nC9sI9GwG5OKZu2emxOvLFV3L3gakttMr801zLsHjj9eq_hnJRLQnGDQQ8Bs6C_uCQvRzkzKDDgl3PYS3af4zGR6Sx__NOeeOdvpczhH5JDrJXEHxb4Lr_3G2JpTK4YQO6t1RopSNhxExbDrn69uSJbs2Ef2iWZ7OCS9u87hRXH_MbwHC0O9eTInjwYnpMm3siepIyfmEzhO81Rj_JgEh3bjTlC5DYk1aAkmFZnnR3HyoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تظاهرات وقطع طرقات وأحداث شغب يقوم بها الحريديم في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79079" target="_blank">📅 09:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79078">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان ومروحيات الإنقاذ تنقل جنود مصابين نحو مستشفيات الشمال المحتل.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79078" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/79077" target="_blank">📅 03:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=OZBz4lnQ5bZFhdLzTekBQGWA_ZvdUqC3_VsXPMVhLre1IoXc8Y-4g7r5MoINsNNiNMNt_67hdeam-fL7dSyfaugDtyCfPoNtgvz0A8ekWSoU-EwxFsgIxm6TxVv6RX9X5hReOaLSUWVaPWBGzZTGk8aeGVuLqENbtQXq0TOhCPZlHva5DYpgZUbDXiACV0s6FDd0tOrSJYFjVCf4gIEHIvZy4_CROzFwTxgOA8eL0yZPwdCEYm1r8J4dVQqDM2LwY2gEdaO3bPMQn8_-mDhepsFJgevXAdHLkwTxRTPqDot9eGFuAMFINnGLVrqZUCetey1yjEo97ns6IxW9m6kELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=OZBz4lnQ5bZFhdLzTekBQGWA_ZvdUqC3_VsXPMVhLre1IoXc8Y-4g7r5MoINsNNiNMNt_67hdeam-fL7dSyfaugDtyCfPoNtgvz0A8ekWSoU-EwxFsgIxm6TxVv6RX9X5hReOaLSUWVaPWBGzZTGk8aeGVuLqENbtQXq0TOhCPZlHva5DYpgZUbDXiACV0s6FDd0tOrSJYFjVCf4gIEHIvZy4_CROzFwTxgOA8eL0yZPwdCEYm1r8J4dVQqDM2LwY2gEdaO3bPMQn8_-mDhepsFJgevXAdHLkwTxRTPqDot9eGFuAMFINnGLVrqZUCetey1yjEo97ns6IxW9m6kELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتخبنا الوطني يخسر أمام النرويج 4 - 1 في أولى مبارياته بكأس العالم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/79076" target="_blank">📅 03:33 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
