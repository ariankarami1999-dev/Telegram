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
<img src="https://cdn4.telesco.pe/file/fcSczguZhzWkNT4Y0H6_ap6u4sFmKrS9C84Ru6_Lso_TXG7gyxt6_XGD7XLBZTVl_FC_ZL9894jcx1IHrvriYne9fqNC-DatzhoHxXdTG1B_y4JdVNI6Tm-MrL_VgpmidCsX7FuiR1xuRQJjEX_OdABZnhgOkVuD7-g2jyqbKQNu-aCJF5PE2SbD-Pcjf30cKavUo3B-3CnyIpfxKg975R6pBkf2ivYmtN4aF8rJvVHCf5qxVwMmwru2aU8ziYn7DFnDSZM7-9F6Jw4r2CgQN7jfE3Yk-7xnQ3jrYCjUZF3sN5NQj2w4869HMFPyDBbOhKuSLUQ_ryGe6vNGCreN9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 13:07:41</div>
<hr>

<div class="tg-post" id="msg-87679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
شركة تسويق النفط العراقية:
شركة طاقة رائدة في أبوظبي من بين الجهات التي تشتري النفط الخام العراقي وتنقل شحناته عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/naya_foriraq/87679" target="_blank">📅 13:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس:
نخرّب منازل اللبنانيين في الجنوب ونبني الاستيطان في الضفة</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/naya_foriraq/87678" target="_blank">📅 13:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
اعلام خليجي:
واشنطن رفعت وتيرة الأرتال المنسحبة من إقليم كردستان العراق تجاه دول الجوار.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/naya_foriraq/87677" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇸🇦
إعلام سعودي: ‏اشتباك بحري بين زوارق سعودية وزوارق أنصار الله في الساحل الغربي في اليمن.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/87676" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueq2AcKZKK1Jpkm8qrdFIRpIC7EUTtx_nHF7HpF7sW6TziH1KL1Db12gLLZ5A1jmEO-HMu533-LVylOKbbgtejcfgDeG0OxkqLVOtSyyoqCQNgeREdJMoEn_Ls7rV9I0QL67ad4HRUm9amjqF7GBCTndln5R1YXvie0nucXvh4vRrodFJ7pxQgylmQntHDynUDfkjtAd8QgLg6eDdMy-8HeMRgtZfPeIZWHExcBmPcuYSm4jT26OSVd6vtbEWDVs4Cprmz-9Oo5ViuAJpLMr1_amzt9l-wE1ZiTNTrmAJ_4aQPKVLy4-Fe2i-c5C6maNCGofXYMlXG1D81uK2nYRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رئيس مجلس القضاء الاعلى العراقي يلتقي وزير العدل السوري فور وصوله إلى سوريا للقاء الجولاني ؛ في الوقت ذاته الذي تواجه فيه حكومة الجولاني الحالية انتقادات مستمرة من منظمات حقوق الإنسان الدولية بشأن ملفات العدالة والتعامل مع المكونات المحلية.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/87675" target="_blank">📅 11:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFPKO2pBtTQnYOse6Yc5L3nGfF5LTU-LCxEnjx72hkslgG-KtoWxIVTZSteUf2hEfXCLxtKtpqzyanawhMF9viUppocUOmsE7iPQhgksAvZA5NMOX-8nTimIFDblC0oyOD9cfPDdxn0ciLQbk5j-itLI53fw_fjiosIpvpnTbtYjnZi7g6d6L3rWkaTZL9ri13clP3vtjO6tb2NvmVB_yQ5WQVdULpfkl4L_phlPtBz84NpvcKtF6Jeija3HHsHopWwJvUovk4TVbgrEuyhS1l45qXNThqGzMEkfSb5W6rKDphxMRDGGnbpzh62vx3pApJ3zpEhVw0GGFg2X--hQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
لطالما أخطأت الولايات المتحدة في حساباتها بسبب قصور في الاستخبارات. خير مثال على ذلك: الحرب على إيران. والآن، خطأ أكبر في مضيق هرمز.
‏أسوأ من الأخبار الكاذبة هي المعلومات الاستخباراتية الزائفة. كن حذراً.
‏الله أكبر، أعظم من أي قوة على وجه الأرض. بالله نتوكل.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/87674" target="_blank">📅 11:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">أمبري للأمن البحري:
نشارك في عمليات إنقاذ ناقلة نفط منكوبة قبالة ساحل عمان وسفن الإنقاذ في طريقها إلى الموقع
أفراد متخصصون صعدوا إلى متن ناقلة النفط لتقييم الأوضاع</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/87672" target="_blank">📅 09:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrBhmK7jUJL_a6FQAGjh7LKIw663BbpLjW1R4uEPdJXmO5SlfNy0V-7ChO0UUfHG_lde1kqDDYGKZY4Iao_a85e1pOyF9R9-NjWuvoNUzFqNcMXMm5rqtk3BRNiAIq8LKDO-Ow6xKdxWmU8w14c6MYTnn-dqnBczRK_dhzEp9UIbgcIkakCassuiQAr2HrwHgGBNIvg5GCKBA-XUKNjgN0SbCTYo4JX3EZAmr1GINbC5r6fhvUmlN4RwonI5QKwTt1P-0N0bvStnyYpQ1RO_7LjwNVm5N7VOFybCRfa_eIaCZD0tkasf88QYrwU2YgSXuI1dX0fvFmqd7yELzOHN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
😎
بسبب القصف الإيراني مؤخراً الذي تسبب بهروب وفرار رجال الوطن الإماراتيين ؛ وزارة الدفاع الاماراتية تستعين بفتيات الإمارات وتدعوهن للالتحاق بالكليات العسكرية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/87671" target="_blank">📅 09:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4,7 على مقياس ريختر تضرب الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87670" target="_blank">📅 08:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
عصابات الجولاني تطلق قذائف الهاون ورمي بالأسلحة الثقيلة على الحدود السورية اللبنانية بذريعة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/87669" target="_blank">📅 08:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNX04msXNwmuYbGXqIfZhwpDVhFab83ZicB5ZhQYc5LB92Bli_9T4DBvA87-xrztDLXXJWaqkPYnHk_C3BaTXGkSbp2ZFjWOAhOi1VZST7VG3FtytmS8JrRF49JvUNzCM3HId5SORhkuLq5MhKYgF7iMbGAiKJUqUx7X89Dv1rD-z8NpG9Nynk5eWkVCheyGVaI9pBAwVe2cPY-VK0sEuxZ1QXELN4xIIXJyMyAqB1KKcs6ztit4tnTftJZRiuARoc_Uir3SXENS0hOdVv42VJej6746l05V_Wan0TvKqi5vpTHthOmSFX_6p5Ch0sTtfAwgzWfBekJ7-MvMnzdCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
دول مثل فرنسا يجب أن تتوقف عن إلقاء المواعظ على العالم بشأن "حقوق الإنسان" والقوانين الدولية. هذا نفاق واضح ومخزي. دعمكم للإبادة الجماعية التي ترتكبها إسرائيل في غزة، والهجمات العدوانية على إيران، قد قضى على أي اعتبار أخلاقي كنتم تتصورون أنكم تتمتعون به.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87668" target="_blank">📅 06:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87667">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZC1kMQEg51Wx_xen3Ab61_pkA0GcYqvUwz-h5B75nBFzG-1RQnlLYD-jxiZjn8kzmANJRTi9sow5-llYkTYbMCzjlx4tZJ-JPHQiLiKKK0JPjiLJaSa8C_jVslcdjiLcJmUlF5sT8ll46sEVopI9hcL0yjJ4lg4si2cNuyOxcayf3nbe5LvmdtbHshodvp4rYj-EgolUnTSCWiGDscMwLKV3_RL_DREHUGP1NojD641kXGo2fGqb2nqmYwq65iPG0n4yF4d5RvW6uUz8wxCskrTaULuyZPNdzTrCCoQxJSW6sQT5-F7MA-F4_AMNIiUJ3MRKJQXt8qPE8-kYtW6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
منصة X تقوم بإغلاق حساب الناطق الرسمي للقوات المسلحة اليمنية العميد يحيى سريع.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87667" target="_blank">📅 05:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
طيران حربي في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87666" target="_blank">📅 04:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
علي الزيدي:
سماء العراق وسيادته تمثلان رمزاً لن يُسمح باختراق أجوائه أو المساس بأمنه من أي جهة كانت.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87665" target="_blank">📅 02:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إخراج ترمب سرا من أنقرة جاء بعد معلومات بتسلل خلية إيرانية مع صاروخ يطلق من الكتف.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87664" target="_blank">📅 02:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrpOQFuRgstk2uf9M-Hgd4VwSwOfpNvh5HfnhOpGyDw2EKVrKbIWYXXQaDPkppC4dfMeCuASmv6akwHKKGdIdgUj-hltd2XMBC91CASscx9ny2NN2epebeCobC9axfVLMg_zZkRk_R-D7zbD8URZcNao70_mRXUpTWBUIqDQwoib6QnNMe3R4_4_jnmlVrQMopDZAPqqxaCe36mu7gKlQuvT_dASpZNX0zrM_7m38RXeYi0lgNPePfUtFiGaNQlUYfoSWpndyLpugo1bl-Y-_aO2YyhZVlxpo5__dzLjKd3WGwsu7N9ghKCQyR6n8vyFUYL5ovpQHxa-JoeHiIXQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارة صهيونية تستهدف بلدة المنصوري في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87663" target="_blank">📅 02:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا...
انتشار أمني واسع على طول شارع مطار بغداد بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87662" target="_blank">📅 00:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اندلاع حريق واسع جراء تحطم مروحية عسكرية في تكساس مما اسفر عن مقتل جنديين في الطيران الاميركي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87661" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">طائرة من طراز بوينغ 737 تابعة للأسطول الملكي الإماراتي A6-RJA تحلق من أبو ظبي إلى طهران  ‏هل ستتجه المزيد من الجزية الإماراتية إلى إيران، أم أن مسؤولاً إماراتياً رفيع المستوى يقوم بزيارة؟</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87660" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFHl0brrzXq_saSS8lNqi0vTWnQawZKodLxxj7P3S7Zk7au3RS1u5FCEnrYzx2Bzy2LCDXUUyQOaOYB0LQXlMb3gjqaR6X_yxmdbqzH7xBdX0s2Nz8_YVEu79VHjkZJAg5mLAOCRsQFZjCT9VNq_RAd5qX9hxa7_NmotLqGneHpMciHm2ypNnzMFtHUt-nOBrl1UY0VXyEoi1pfF0-tS-NKIcvrNSxFnUZekVPeSvaMZDf-8JU2N78X9Xwe0n3qxxXPyiILz2jPa43FBqulF9tzX7KRAxH7cEF4YrwWPjJrKQAatwEx0gT5_W4vyweCeZHmZ4wFtq_p9PAtRFfQzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترمب: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87659" target="_blank">📅 23:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbKa2zZqoaqIKpH6_UtZHiXhjHI5l2Yje_PSNuFUDfXf02J9FPd7znZCBVt4p2fJz0OCCKiLyNHxCsJGolaF6CWK7EElSV4Z2CqdoTJXr1i96wI8FY8Lmk0B2dCXRuEsWITGtijy_w19R1iDPaMMXvHlg8C9M8LMErbOai3Orj4_5PlhrqwUdp1gfY3y99U-hbKTmGO7KXHugG931czc6FMwOvqZ3YyLmAXgB8g-VxaDEn9K6v8XDfeuM5TwzK0IBj9DyIwUxLmZfs_L8UlPNiJsd0AOCl-cwMW2QAUTaURKb2OWupOvy71Tf88FEpApZmHNYRScgjzUUQiB5v6Adw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87658" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
على الرغم من الارتفاع المهول في أسعار البنزين في إقليم كوردستان فإن جودته لا تتناسب حتى مع دينار واحد من سعره، إذ يتم خلط مادة الثنر والماء مع كمية قليلة جداً من البنزين.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87657" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87656" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87655" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKN-Ohq7VCVOzfYmD7BYNvI05Y0Tw5EH8om7fGUPbbx4PQAIC8ADOOqaBojE36XguxZCzcDoF9EyNPtiij6XnRGcvRJmbzcl4aj1EBlCtGma8F02_spN8gm6yODLJOQ1ypiNMWgfKXdDIZEyImyK_GNYQIVmljOGiPh1zSCNFaY4fRnRxc5y6hajDPsNCttYMUZjkKhPHsmOjDk4TvYBnE15BYlJFqfjUyqm0PRq3qOG1wRK-pZEL6T_EtXyeKiuXmIjK3EJY16r5RS8lkwFqttL8nzMjSzjryjmJFOeRKaPGVpYY58KXj8fLXwdnvx3r8dPCeng8oNcFdkDZd44hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة الممرات المائية في الخليج الفارسي:
إن الادعاءات والمنشورات المتكررة من قبل المسؤولين الأمريكيين بأن مضيق هرمز لم يعد مغلقاً لا تغير الواقع: فمضيق هرمز لا يزال مغلقاً ولن يُعاد فتحه حتى يتم قبول شروط إيران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87654" target="_blank">📅 22:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من حادثة الهركية ومحاربة مدينة كاملة بسبب اختلافها السياسي، إلى حادثة فندق لالازار والرعب الذي عاشته السليمانية جراء الهجمات بالمسيرات ومختلف أنواع الأسلحة، يأتي بارزاني رئيس اقليم كوردستان اليوم ليصرّح بأن فصائل المقاومة ستجعل العراق في عزلة دولية اذا لم تسلم سلاحها.
هل العالم بأسعار النفط الحالية قادر على فقدان أربعة مليون برميل ؟!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87653" target="_blank">📅 21:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87651">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nox_3M2t8riZK_pv_a8ZTtrpC6cRLCHMkBKYwVKgzsHkF4tMMt-_YxMnaDW7iAshd0UVfoTFfebgXGspViyxrxo7DvsEfvxynz9iJmO1gbqg_J9E8CFi8LkKtzVmybGwv4fgG8uJlVwC7t9wvXB_650DAxN1aSssO0DbCe3O1BKdFcGd66nA187ZCbBxRrt9cx2lTCUsHnLRUrJoqRL5JmJwOf3NXVqNV_onYPbozod-KdhPzXZuA-Tp0ND8YyMuP6jpDlODu2N9FvaINHB9y9V1RqRw4vFfdsscX1gxS7kD8wk6L8j7iwNPxYHqRuD0NJlN7SAzfiLqMEcygyQY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuV5FI-vBWz-A7vQURvjtUWvum23r93ej95B9j1SgBJ5yEA0TvIdy4T_lDIH2KZDU0nuMG28eeB-ETfrkmnrbgwXco-R3RBR1IKqs3S_j2Arde5oVPA4Hg4G2G9ji-zTsyRt0PyhD-fqbwoC618sVrmCXI6rdDEvrg-4tgx-1vZ_b1nZcResXy-fFL6eaRLFdv9UwD3oDA1cm31mrYCJbrIm-TlLSr1nEFSCZ9Op_oZ1bxvK_vYIAvXkOL0E4_onQsMT-UuHj1-YLNyeF1mKHS_L2tdYvocDh15wuBGMSscKSha5HrxzhjXlUE8j-X9RGRcqg_zNtvGywCX3nSb5hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇭
سلطات البحرين تستمر في اجرائاتها التعسفية من اعتقالات وغياب قسري في حق الطائفة الشيعية التي تشكل غالبية سكان في البحرين.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87651" target="_blank">📅 19:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
🌟
‏ترامب:  الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87650" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني: قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87649" target="_blank">📅 19:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
‏رفع دعوى قضائية ضد ترامب بسبب بيع حق الوصول إلى منشورات Truth Social.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87648" target="_blank">📅 19:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBpDVWhpIPbszAswz-9JXTaUYIUAAP1gnEE1qXpikOdlwFuUxhMV6WHWPWJThs5Ir0zEAG86huciA2rZHc6nsnMvoxcREfRyPTUbrUoEqUkecd6WVQtxLti_BwSLiA74aep46-Yk1Corr9sazWTZvEep44Qd8h6p_Ont-ldJvuI4rGlK9q9kPyWqOBNi4VCWSqYPQxVl3ltdewYLsUzBhywU70Gl8juTO2kfrKLVa37rGZKpWd7eQqkkeYhP6c8Ds1zkEvmsHXfTHYiEGTaftoysai5cstPLqMshiFgkmwAsqScuY_h9CD5dUQ6FZ_O4uWJQopbV4WFgVuacD9QeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏تتجه ناقلات النفط السعودية حول رأس الرجاء الصالح لتجنب انصار الله في اليمن، فيما تتوقف معظم الناقلات في البحر الأحمر عن العمل، وتتجه أكثر من 12 ناقلة فارغة نحو موانئ عُمان والإمارات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87647" target="_blank">📅 18:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تذبذب عدد من خدمات الاتصالات بالمنطقة الغربية في ليبيا بسبب تعرض الغرفة الرئيسية لاستهداف بمسيرات.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87646" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87645" target="_blank">📅 18:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87644">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني:
قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87644" target="_blank">📅 18:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87643">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تطلب من سفاراتها في منطقة الشرق الأوسط خططا للعمل بعدد محدود من الموظفين.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87643" target="_blank">📅 18:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrnPnc_k3Ipne9j6lZxgHyBY-eQc87vd_U-W0bsHYmNNYPYo0lYgE6SWPtS6Yvuu1d5tzd-g2PGlAvrJlFhkrJxRVa2v6EGCMpw-aTFVgdD1tlJqKyxlzH4-DUgB-auNj_w_sb9OqQNUrdxLERbGj9KFKj-yIeGRkZnrRw4eqnYL1Tdp-QRx3HL_HT4Cpmc-v_HZpPSyRHCn5C8ie7ShwlY0aCXg8EBlTE-fhkHXfRjykP7R0U5HLSRHqhqtNq-IrSGxWMB8bIZpAxWGmMoQ2I8cuKskT7IbyhZ4J0wORrp8ArL47iyggW9KWwKBE-S7mkXAzDyAdqslBS36H4mlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87642" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1ydzolvdGx6afw0iuEfkiKDAmcxF2mNV5Xhb4ykmMyHXKOCoOioy_9uwgeQ74XOo1xOpcjpAVtMdpRfBzNdFktURP-gJi1C5TdYjYA0W47A0iCQma29y79XDVQlrPFkXSsjXXkKr292-R8BpWcHeuFdJQwFN7Nrc-hVpmc93t3XWAfyKjh8O7qQvnyYwrgcDMyjL7dcF39xkRhA8sL4OGkvHq4x6G93DBM3ybXJ13JBh059PhERRRTYiWne8B8JMz6Q4VqYNS9EoYBhDAwfWvSUMxjXpfqiVgfQNKo7_F6k4BGO5UQcuuEX2idLxJWd5oT1jTOMZJshKH4j2nV3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري الإيراني مُنهك ويهرب، وقيادتهم غير مستقرة، في أحسن الأحوال! ليس لديهم مال - بلادهم في حالة يرثى لها. كل ما لديهم هو أخبار كاذبة وتضخم بنسبة 300%، والوضع يزداد سوءًا! إيران مجرد كلام بلا فعل، لم تعد مُستبدة الشرق الأوسط. الحمد لله!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87641" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
يقول صيادون إكوادوريون إن رجالاً غامضين يتحدثون الإنجليزية ويرتدون شارات عليها علم الولايات المتحدة هاجموا قواربهم بطائرات مسيرة مفخخة ما أسفر عن مقتل أو فقدان عدد منهم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87640" target="_blank">📅 17:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6HAMoUyl3-LUH0SWJIfVe9HhAe3lYIWxkd90_Lx-jZzGHLm1UA4eOB4f6h2rLcLFrfvYnZz2XCLza1L8qvbBrJbyFm2jpxMuJgBDu7CYf4GwNMaM5CpiGVaA6rszK2oqBuUcY49ZxVC8SvVH-sgnGBNRHgf_u1UiKJA60EIitjklzYusSbpFZyC-3YAFpPihgH8Aj1RWenCowVc4aurgmPMPG7rX2CuhOdRedi8MM28d9yLeRIdBUB_g-RyJJwBt885V14scc_TaCV1iqkJU-TkE1VqNe9UhUEukvVas5SSzJKv8yblzB5LunZ4H-sTnseesKiR0fwIiAnjzGBPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النائب حيدر المطيري:
يا وزارة الكهرباء العراقية حقيقة أم حلم أم خطأ مطبعي. 801 ضعف بين المبلغ التخميني (900 مليون) وبين مبلغ التعاقد (721 مليار) لشراء 4 آليات، هذا ما كشفته اليوم لدى مراجعة تقرير ديوان الرقابة المالية الاتحادي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87639" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله:
السعودية تخفي خسائرها لا سيما عدد القتلى وحالياً نستهدف البنى العسكرية فقط. ننصح أبناء اليمن في المعسكرات السعودية بالانسحاب منها للحفاظ على أرواحهم وسنقدّم لهم مكافآت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87638" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=otv3Xmu7Mh6B5Bnt6BU1iumzZIrN5YS3u_9T3Xc9cQQK275KTQG6wfR2sW0o4rQfdBVdaQXdCDg7U9K99AC9vuE8SWjfuTd430LVKRUD2dTQDvhFeC-w6Dh__VSPhn-QUMF9pUC5QGcld8Au2GLitk_H57laucwioRQvEWgSUaioh-Yf5Wgd9AHEtiM_jSDcQpzV0Lu40_ojzGkiVKjOqqXzfQ8QeQPhhNFGrW1OTodSrLPqKJFIvnrzGHcV6ySVQW24m1oA0mCmoSxJ68YALTSeSflaJYd9sk5p9gyu4neX7XXLlFajXqSWO2K4g2WlpTXwrnFW_LW86xfeWgFu8V8mPQtfWyQjazD-6TCLgWhvqLEPZSuQeZOSDd5SJeNU68UP-xa9SE8MIDNwwOZnsjh_Aw-jND_GBjtfMoavZ-HV0kVqg50SFyW6ZycURDDdSMekNA8v7YXwfAziHslZjhbiCv06ZCInf6RcbSbNavyjcHyMO-6HSyKDqsZtTrIw9k_s67DFMgyOWSxYP9lOE8-679ktVU_-1giF0-kxiMNhJ1v0b32xSQ6Lw8m-ZzCbHGJdrncJKe2b1hC4DpMDggT_6kWaZu84PkmDpGv6vU2q9Bbkw1F1YBWlZ0407Upf1unmzEIkJuIhDX6dCvtD9W8gPWlWBQ__JPs1brrNuzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=otv3Xmu7Mh6B5Bnt6BU1iumzZIrN5YS3u_9T3Xc9cQQK275KTQG6wfR2sW0o4rQfdBVdaQXdCDg7U9K99AC9vuE8SWjfuTd430LVKRUD2dTQDvhFeC-w6Dh__VSPhn-QUMF9pUC5QGcld8Au2GLitk_H57laucwioRQvEWgSUaioh-Yf5Wgd9AHEtiM_jSDcQpzV0Lu40_ojzGkiVKjOqqXzfQ8QeQPhhNFGrW1OTodSrLPqKJFIvnrzGHcV6ySVQW24m1oA0mCmoSxJ68YALTSeSflaJYd9sk5p9gyu4neX7XXLlFajXqSWO2K4g2WlpTXwrnFW_LW86xfeWgFu8V8mPQtfWyQjazD-6TCLgWhvqLEPZSuQeZOSDd5SJeNU68UP-xa9SE8MIDNwwOZnsjh_Aw-jND_GBjtfMoavZ-HV0kVqg50SFyW6ZycURDDdSMekNA8v7YXwfAziHslZjhbiCv06ZCInf6RcbSbNavyjcHyMO-6HSyKDqsZtTrIw9k_s67DFMgyOWSxYP9lOE8-679ktVU_-1giF0-kxiMNhJ1v0b32xSQ6Lw8m-ZzCbHGJdrncJKe2b1hC4DpMDggT_6kWaZu84PkmDpGv6vU2q9Bbkw1F1YBWlZ0407Upf1unmzEIkJuIhDX6dCvtD9W8gPWlWBQ__JPs1brrNuzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي عن ادارة ترامب: هؤلاء الأشخاص لا يعملون من أجل مصلحة الإنسانية، بل لا يعملون حتى من أجل أمريكا. إنهم يعملون من أجل مصالحهم الخاصة. بمجرد إغلاق سوق الأوراق المالية، يبدأون الأعمال العدائية، وعندما يفتح السوق،…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87637" target="_blank">📅 17:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: حتى لو استمرت هذه الحرب لسنوات، وحتى اليوم الأخير، ستُطلق صواريخ إيران. إذا جاء يوم لا يتبقى لدى إيران أي صواريخ، عندها سنكون أكثر خطورة على أمريكا. تمتلك أمريكا آلاف المصالح الاقتصادية في جميع أنحاء العالم،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87636" target="_blank">📅 17:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87635" target="_blank">📅 17:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e9534074.mp4?token=fcAr6dGGWzpLfn7nsqPPzhZJGNwRBm1Qz3MseMTBYv4etksg_pAXQYs9X8pl_hYobib_7FG4VPXueJn00v4UC2rlx_iAiQSnRjuycQwt0Gjsj6BQEpVph2LbIeH8XC_3drbA0XUxIhg3UAwv2RSvo0B4Kep24bJ1XgKMPW0k6kEFR3YAU7SJDhCErOpEJ9Kki0gSQFJirBTKsbhvrPLCtkan0CXNNU2tqxkNS_OwexuuxsHozV0LYFKi829nCME2yfBTltzKMfIyaFZ8F24EFIOox8i9OATHB-EzOfEStlUMzGKe8DH6U3Hh_BxxdmAe6QvFFdjr7lfptZpLpUuYgrnDbzrmIXzhGxaXMvt9SYWzz1884iCles2YREWVLxOdb508zt_ak0USyPQyYOi2Zs0G8XvR96LyWzr339zLW784_DtLEtLxoXb9Xmnhri9WkTxYkhd1YVMJ1vi_Manv6LBRb2Urah0yfFTe7235mmsCJzvH_Cu1y8rlLYAWu93GzlTqLhcy9kLRFk5QK23SM0p7EwdThira0phvXyv3DimSLdi1-fLnzade1WeqL2B5ISTaqXe2M_k_42zryRcV40My7NeZRNJd7CBa7k_HYjGTRZ5RvkHNHrpBLxCVHT9Ft0nwaOES1YavhfEGfXChQ0mawGuHq_4oDX9-fwhLVuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e9534074.mp4?token=fcAr6dGGWzpLfn7nsqPPzhZJGNwRBm1Qz3MseMTBYv4etksg_pAXQYs9X8pl_hYobib_7FG4VPXueJn00v4UC2rlx_iAiQSnRjuycQwt0Gjsj6BQEpVph2LbIeH8XC_3drbA0XUxIhg3UAwv2RSvo0B4Kep24bJ1XgKMPW0k6kEFR3YAU7SJDhCErOpEJ9Kki0gSQFJirBTKsbhvrPLCtkan0CXNNU2tqxkNS_OwexuuxsHozV0LYFKi829nCME2yfBTltzKMfIyaFZ8F24EFIOox8i9OATHB-EzOfEStlUMzGKe8DH6U3Hh_BxxdmAe6QvFFdjr7lfptZpLpUuYgrnDbzrmIXzhGxaXMvt9SYWzz1884iCles2YREWVLxOdb508zt_ak0USyPQyYOi2Zs0G8XvR96LyWzr339zLW784_DtLEtLxoXb9Xmnhri9WkTxYkhd1YVMJ1vi_Manv6LBRb2Urah0yfFTe7235mmsCJzvH_Cu1y8rlLYAWu93GzlTqLhcy9kLRFk5QK23SM0p7EwdThira0phvXyv3DimSLdi1-fLnzade1WeqL2B5ISTaqXe2M_k_42zryRcV40My7NeZRNJd7CBa7k_HYjGTRZ5RvkHNHrpBLxCVHT9Ft0nwaOES1YavhfEGfXChQ0mawGuHq_4oDX9-fwhLVuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي:
يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد أي شخص آخر مهاجمة إيران، فسوف يعرف أن هناك ثمنًا لذلك.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/87634" target="_blank">📅 17:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزارة ‏الداخلية الكويتية تزعم: الموقوف تلقي تدريبات تتعلق بصناعة المتفجرات والطائرات المسيّرة لاستخدامها في تنفيذ مخططه الإرهابي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87632" target="_blank">📅 17:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌‏وزارة الداخلية الكويتية تزعم: جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87631" target="_blank">📅 16:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌‏
وزارة الداخلية الكويتية تزعم:
جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87630" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
على إيران التوقيع على الاتفاق وهي تعرف ما سيحدث لها إذا رفضت.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87629" target="_blank">📅 16:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57727b7186.mp4?token=BYmtrRRNdLD8FQJ_O1MMcvN08Ngt61jTwC7KlTylBBvIwo3BR6lMMi_rdGqF6Fr_ENKhqexvUxYIQDRSrcEpiH1Bh-CY4LSMRaZsGraUWOtLAZsSqr1vdpefglhSY0L84GPI7uj-_u302hr-LZTpHVwLD2yxZogZ17SwnDYScEOBidJfNAgmxNewsqPmtqUOthsPWmSVQr4RqRR5QfsQTRF7pb_qcspaQjxD1ahgunLBXZd_LjZBbXaCDWRuUS0GvkdYK604A_Wxf3geumtmne84Tro1yEEftkhbPL_f7VWcFSz0el3cmrGFqLeQ_d2CgyUjGazP6abwZTZO58g0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57727b7186.mp4?token=BYmtrRRNdLD8FQJ_O1MMcvN08Ngt61jTwC7KlTylBBvIwo3BR6lMMi_rdGqF6Fr_ENKhqexvUxYIQDRSrcEpiH1Bh-CY4LSMRaZsGraUWOtLAZsSqr1vdpefglhSY0L84GPI7uj-_u302hr-LZTpHVwLD2yxZogZ17SwnDYScEOBidJfNAgmxNewsqPmtqUOthsPWmSVQr4RqRR5QfsQTRF7pb_qcspaQjxD1ahgunLBXZd_LjZBbXaCDWRuUS0GvkdYK604A_Wxf3geumtmne84Tro1yEEftkhbPL_f7VWcFSz0el3cmrGFqLeQ_d2CgyUjGazP6abwZTZO58g0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">التقى ببشار الاسد بعد اسبوعين سقط  تحالف وية باكستان، باكستان دخلت بحرب وية الهند وانفجارات الارهاب كل اسبوع  تحالف وية تركيا، مباشرة سقطت طائرة F16 لهم وبدون سبب  الدرس من ذلك: لا تتعاون مع بن سلمان فگر ابن فگر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87628" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGeR3W4fcNWfM2yDrlTLfLghwCtKMN7xWnCRxtj6GgpLGbKg9nGDDxU7PRVOKanwN0y8pWcSZSB8sDibMTWkL_s03uJk6PUfGWL4dQrdrKV-cd2qW_FfO_3kGeGNtfMGphcHf8xFyOmLLVAZvSRrq3ANCQcIidkP3t0RRJ0H-xlC0vammXINxnis7V-90jw_h5qbfo6Fy120EQSnrTaiIVPIchq7Rd0_7ksYATMK3zdFT-dqeH5E_I6j-n70n1eeBnGduultwWe-N23tnHudZFchet_SjkNNCmjgqQoaZc2Bc121uCWml_Lkx3z2Fbi7l55D5PXNdqfqgnjqs5wjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87627" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=RD6TdtTdS-fruhENaxcLwYDtcl28WSLkcnb54itADaj9V4ZvtUfD5faGMbnO9D3QwyTYjA7cTVKmjvIt8pnjPR1t7WRY-Z_8uW161PxGdj4BikewBH-yZcc04sU7eOmwh5wkimHQvsVx-wUmnRSgS9g9UlQ1IDlq2ioJYA8RnyanFrlUGkjp6ai4bAM09MorghGtROjUZSG6vzEHklNcuwgjWdC6kZfcrzexfH8xsLXTXKOvswI66S9826va28gRia5E54sveEmfpXjqgd9QNFwkUgEIlqxdADWu6FoFqra90tuRGfTnLclMn6-KR0mRRm_5KR1kMdC9aS5RNo_6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=RD6TdtTdS-fruhENaxcLwYDtcl28WSLkcnb54itADaj9V4ZvtUfD5faGMbnO9D3QwyTYjA7cTVKmjvIt8pnjPR1t7WRY-Z_8uW161PxGdj4BikewBH-yZcc04sU7eOmwh5wkimHQvsVx-wUmnRSgS9g9UlQ1IDlq2ioJYA8RnyanFrlUGkjp6ai4bAM09MorghGtROjUZSG6vzEHklNcuwgjWdC6kZfcrzexfH8xsLXTXKOvswI66S9826va28gRia5E54sveEmfpXjqgd9QNFwkUgEIlqxdADWu6FoFqra90tuRGfTnLclMn6-KR0mRRm_5KR1kMdC9aS5RNo_6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87626" target="_blank">📅 16:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87624">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي: وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87624" target="_blank">📅 16:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بيانات تتبع السفن:
السعودية تقوم بعمليات تحميل النفط في البحر الأحمر مع إيقاف تتبع السفن بسبب هجمات انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87623" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇲🇦
وزارة ‏الداخلية المغربية:
منشورات عبر مواقع التواصل تحرض على العبور الجماعي نحو سبتة ومليلية يوم 15 أغسطس.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87622" target="_blank">📅 15:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو:
بعد اختفاء مواطنتين إسرائيليتين في النمسا يوم الجمعة الماضي، يحقق الموساد في القضية، وسط شكوك باختطافهما من قِبل جهات إيرانية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87621" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منظمة أوبك تخفض توقعاتها لنمو الطلب العالمي على النفط لعام 2026 إلى 580 ألف برميل يومياً (التوقعات السابقة 780 ألف برميل يومياً) وترفع توقعاتها لنمو الطلب العالمي على النفط لعام 2027 إلى 2.16 مليون برميل يومياً (التوقعات السابقة 1.94 مليون برميل يومياً).</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87620" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqeqkyF2nu2yP4v5P6A0CKqmAohFYru30qH5mGUH25mnUlMXAyCS_OT8Xoh3kUOud-oBlyZv2G5UqKuRO0B5escV0ugQ5qxO-KKw7ncuCLznQ08jlrhpxe9xCOyNs3bO1wKS4jhtr5b2HRK2YwjYN9-_-pxPa9BW7SGpMPKIBWUhEXLMGnH528jN-20P5WULnEdZB0rwLDW7ygwMfTvMOyhH_7Mn4CVPxBD2wYttVBHED9XWq2tnoIM-xTHeHCwARTraXR9E0So0BI0lI5NUKRPvTyhu93rzrcS9f_hXQdV05oEEyHX1rY8923op3oMrk_q8VePxHhT0n4_oQuap4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كانت داخل شاحنة اردنية..
كمارك طريبيل العراقية تحبط تهريب سحبة أركيلة إلكترونية متكاملة و(390) قطعة كارتج و(310) قطع كارتج إضافة إلى (12) حبة مخدرة فضلاً عن قطعتين من مادة الحشيشة بوزن إجمالي (5) غرامات كانت مخبأة داخل الشاحنة بقصد التهريب.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87619" target="_blank">📅 15:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عدوان سعودي مدفعي يستهدف منطقة بني معين غربي محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87618" target="_blank">📅 15:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
فايننشال تايمز:
اوكرانيا توقف هجماتها على الناقلات في البحر الأسود عقب طلب مباشر من جي دي فانس نائب ترامب بعد ان اكد أن هذه الغارات ألحقت أضرارًا بمصالح الشركات الأمريكية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87617" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇩
وزير الدفاع الإندونيسي:
لن نسمح بإنشاء قاعدة عسكرية أمريكية في البلاد، التعاون مع واشنطن يقتصر على التدريب العسكري فقط ويجب احترام سيادة إندونيسيا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87616" target="_blank">📅 15:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
رويترز عن مصدر إيراني كبير:
لا موعد لوقف إطلاق النار ولا شيء هناك لتمديده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87615" target="_blank">📅 14:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي:
وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87614" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
وزير التجارة العراقي يبشر:
الدين الداخلي للعراق كبير جدا وتجاوز الـ200 تريليون دينار واصبح عبئا ثقيلا على الدولة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87613" target="_blank">📅 13:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات تهز العاصمة الاوكرانية كييف بعد هجوم روسي كبير صاروخي ومسير.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87612" target="_blank">📅 13:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feafd64b6c.mp4?token=fVwJFa7NFlcLlrc_vtcHtB9RiTq04R2dFApGN5PCbvJG-s7FiXK0rJbTw0QjM-9w-XTCJcE--UZNAqPu5jcMbTrCg-XU6aGnRUH7SwGkUFwFQ7mC5L2meDYaqz6BF0D4yfJ5z5zkdHyVyHT7w764-HaOk3V3wC1FQ4fLYhuSelqbdgs85-nB-RdF9CVfzE2DJWWg7XiLCuRBCimLQiitsM4F4m1IP91d2Emo4CDudeGBy_nnhg5ydzEiiXQhtErJ577V3YGtA-Go8CfozamJbODX57xlvQhiHbV7Tv80IYgB4g4YqUuWVbdr0A8UKHQ0RRGWFKbnxDgROSC3Z-ERDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feafd64b6c.mp4?token=fVwJFa7NFlcLlrc_vtcHtB9RiTq04R2dFApGN5PCbvJG-s7FiXK0rJbTw0QjM-9w-XTCJcE--UZNAqPu5jcMbTrCg-XU6aGnRUH7SwGkUFwFQ7mC5L2meDYaqz6BF0D4yfJ5z5zkdHyVyHT7w764-HaOk3V3wC1FQ4fLYhuSelqbdgs85-nB-RdF9CVfzE2DJWWg7XiLCuRBCimLQiitsM4F4m1IP91d2Emo4CDudeGBy_nnhg5ydzEiiXQhtErJ577V3YGtA-Go8CfozamJbODX57xlvQhiHbV7Tv80IYgB4g4YqUuWVbdr0A8UKHQ0RRGWFKbnxDgROSC3Z-ERDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مروحي مكثف في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87611" target="_blank">📅 13:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات تهز ميناء المخا في اليمن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87610" target="_blank">📅 13:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇴🇲
‏
المنظمة البحرية الدولية:
تسرب نفطي من ناقلة انجرفت شمال شرقي جزيرة القبلية العمانية ومن المتوقع وصول تسريب النفط من الناقلة كارولين بيزنجي إلى عُمان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87609" target="_blank">📅 12:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات تهز ميناء المخا في اليمن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87608" target="_blank">📅 12:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏بيانات ملاحية: تراجع حركة الملاحة في مضيق هرمز إلى أدنى مستوى لها هذا الأسبوع</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87607" target="_blank">📅 11:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📰
بلومبرغ: مخزونات النفط العالمية ستنخفض هذا الربع بأكثر من ضعف المعدل الذي تم تقديره سابقاً مع تجدد الحرب مع إيران</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87606" target="_blank">📅 11:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇵🇰
الخارجية الباكستانية: لم نغلق ملف الوساطة بين واشنطن وطهران ويمكن تمديد فترة 60 يوما في مذكرة التفاهم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87605" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6eb0f77f.mp4?token=u9kYqAdFT0KwkMPPLLNIi2DLy51t1mwtkEHRpgkGDBhckS-0865xH9ISBBN9xHhsa0tPHK4QOINLmKZnOI9zcWSbHnTovUdEPdWPUn3nKeQDiFlileeiwXOtqJBuEjUb1UAuz1KdxW9KC40rZBQOMVJgFhV82_4fgh9uI5LUIGlBqIwsRpmSNvAI9MDPzYKwtxfyjE5j_rvOLcgz_RTmR-27uyGliPEfTAyEqMWns7AKR7qmuAVBxoP9dDKBKWx5yEyhjLx7P4P4MLGqNRhLpgI07xgVm-wVQArYsVoWTMdweQyM-hjzUx6FyqiCjcTfy5NW84U8_P7E9GnKwWukxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6eb0f77f.mp4?token=u9kYqAdFT0KwkMPPLLNIi2DLy51t1mwtkEHRpgkGDBhckS-0865xH9ISBBN9xHhsa0tPHK4QOINLmKZnOI9zcWSbHnTovUdEPdWPUn3nKeQDiFlileeiwXOtqJBuEjUb1UAuz1KdxW9KC40rZBQOMVJgFhV82_4fgh9uI5LUIGlBqIwsRpmSNvAI9MDPzYKwtxfyjE5j_rvOLcgz_RTmR-27uyGliPEfTAyEqMWns7AKR7qmuAVBxoP9dDKBKWx5yEyhjLx7P4P4MLGqNRhLpgI07xgVm-wVQArYsVoWTMdweQyM-hjzUx6FyqiCjcTfy5NW84U8_P7E9GnKwWukxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مروحي مكثف في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87604" target="_blank">📅 10:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e86b5f40.mp4?token=sshHcolzZxk5OhxJvL4RO7-7oJ0bSq_z223E1E5NYyf2e80d_1yp3M2ScvINFlhguWZq_D0J5olNhaR4-4swtw4ze3XDFQcVEays4fbSBseDvyyy4j7Z8QZB1fwcKORv4SM2hhi5lw1FTRodcaCh7Erw8SRwjsduSmaDY9AWx2_ptLsSOmJsJNoppybzNtFOsJfTw5yd8XPAAVLfvyCVTIrs79mGO-iHc58-LRgInxav7kVWBaaMN0njHvMcL0hwqQWb0SIC1vD9YdMxAgP-HgTWeSTEh3LqY0Y1CitfNqyFp3tupe15QdlBbNseQt8PSe_BSiqlQFle5ppLr3ZYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e86b5f40.mp4?token=sshHcolzZxk5OhxJvL4RO7-7oJ0bSq_z223E1E5NYyf2e80d_1yp3M2ScvINFlhguWZq_D0J5olNhaR4-4swtw4ze3XDFQcVEays4fbSBseDvyyy4j7Z8QZB1fwcKORv4SM2hhi5lw1FTRodcaCh7Erw8SRwjsduSmaDY9AWx2_ptLsSOmJsJNoppybzNtFOsJfTw5yd8XPAAVLfvyCVTIrs79mGO-iHc58-LRgInxav7kVWBaaMN0njHvMcL0hwqQWb0SIC1vD9YdMxAgP-HgTWeSTEh3LqY0Y1CitfNqyFp3tupe15QdlBbNseQt8PSe_BSiqlQFle5ppLr3ZYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية.. إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87603" target="_blank">📅 09:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏بيانات ملاحية: تراجع حركة الملاحة في مضيق هرمز إلى أدنى مستوى لها هذا الأسبوع</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87601" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=NQzlE7g39rQTf92caheWocW8UFG4cEykh6BhxGR_euIyXHhCLh7FcxzHOEV312SvMQtxkl_x7bWUfukV5HaT6YyN2wqfq4shZAgXptxLrGw3_jmbIKcRdI8IjcXH7suwYBKeVTea5r4TdP3A9rC4PK4K1XdisS8IpUqp_t47Q9dzSiqDjiunUcyRtWbMBmBbQqrONToZ9z_KiOLzvwRoIzDw0qqOSOOc41uP5D3qkkj5JfrXRt29Zq_s6jp75jmpy6Jp5_UmIlN08P_o8NKlzC20dO1Zluo-6Ptj--m0M_nvPAQq1TnTM5LicItUR9tTaY2TolOqaUs6X9gW79GSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=NQzlE7g39rQTf92caheWocW8UFG4cEykh6BhxGR_euIyXHhCLh7FcxzHOEV312SvMQtxkl_x7bWUfukV5HaT6YyN2wqfq4shZAgXptxLrGw3_jmbIKcRdI8IjcXH7suwYBKeVTea5r4TdP3A9rC4PK4K1XdisS8IpUqp_t47Q9dzSiqDjiunUcyRtWbMBmBbQqrONToZ9z_KiOLzvwRoIzDw0qqOSOOc41uP5D3qkkj5JfrXRt29Zq_s6jp75jmpy6Jp5_UmIlN08P_o8NKlzC20dO1Zluo-6Ptj--m0M_nvPAQq1TnTM5LicItUR9tTaY2TolOqaUs6X9gW79GSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية.. إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87598" target="_blank">📅 05:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=nB_OZUL6Jt4yvk5_bredwwTFMlkk8anZaYRo4HpMtHRi0YkU0S6FBQKqfdhR50wZBVigYXVdB_SVNx-WVoSd-Nl5cnmzg7IfywKl4eE6DeAsR1VNhv5dS6DfOLT78q7CE1Ng2nB1HX2Xt80cUz7wOHp_rN7qreMf68eyXIs5KVfF2C1rHTQPuNcDOEGNbEf-TGYOeKqM6JqzI-nBNMgpbR4OntPxatIyNsH_jZEfc8_0jLbsx8eBIL1Iel5sh5cTDNkRtxq5ioa57K8V7mSoU1aZ9-TCTBteTQBaVSCQ5mnmXD6sm3qvMvC0HDI_zIYKta1B-Ad-FuWOu4HrkRnlcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=nB_OZUL6Jt4yvk5_bredwwTFMlkk8anZaYRo4HpMtHRi0YkU0S6FBQKqfdhR50wZBVigYXVdB_SVNx-WVoSd-Nl5cnmzg7IfywKl4eE6DeAsR1VNhv5dS6DfOLT78q7CE1Ng2nB1HX2Xt80cUz7wOHp_rN7qreMf68eyXIs5KVfF2C1rHTQPuNcDOEGNbEf-TGYOeKqM6JqzI-nBNMgpbR4OntPxatIyNsH_jZEfc8_0jLbsx8eBIL1Iel5sh5cTDNkRtxq5ioa57K8V7mSoU1aZ9-TCTBteTQBaVSCQ5mnmXD6sm3qvMvC0HDI_zIYKta1B-Ad-FuWOu4HrkRnlcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية..
إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87597" target="_blank">📅 05:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87596" target="_blank">📅 04:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=cjaRT3Cc8wWo2TL4RAOcq02vgXSxUQvvWeMaYD9A9Uudv92jxX3MjqT4bCpflcuz-Abj_5fHu2QaRje4MGA1zeXQ6WrUNfB2HdSCJywZadVktzz6enw5RcPUS5xh9wfoEN33oySavr8-A-nvHgseKhgZUy47MiGY1qgzW4a52cdGWAQK34uvzyvhWmaMem2qvNpR3XK0YleXbkDcET5IQ2n5vNqcN89MOoS_DLA8HZOwUq9ZXkenkqKmExAW9IqAxG6BpGtHU0_WyCeuTPFf0Xk7T0PT7DhopU5YPz6H9P25MtP8uDEAJR1FnCTlMHchhbukufnM1CUb2TJY961rwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=cjaRT3Cc8wWo2TL4RAOcq02vgXSxUQvvWeMaYD9A9Uudv92jxX3MjqT4bCpflcuz-Abj_5fHu2QaRje4MGA1zeXQ6WrUNfB2HdSCJywZadVktzz6enw5RcPUS5xh9wfoEN33oySavr8-A-nvHgseKhgZUy47MiGY1qgzW4a52cdGWAQK34uvzyvhWmaMem2qvNpR3XK0YleXbkDcET5IQ2n5vNqcN89MOoS_DLA8HZOwUq9ZXkenkqKmExAW9IqAxG6BpGtHU0_WyCeuTPFf0Xk7T0PT7DhopU5YPz6H9P25MtP8uDEAJR1FnCTlMHchhbukufnM1CUb2TJY961rwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87595" target="_blank">📅 04:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=N2n0dzx7uxJol7Jv792xMCjoPrpISmGdTzlzE1Lw-3NhBC6SD_yBEwBjE7RwQGH2tSD1qmxBV6nxrKeUCYvQmYi0Oc-vrsL-qO3pMBrCSTUAdjqf25c-h-QNsiGynBTxuClrAyPF-991ujLmGKxvJZVc6kzE21KxusQzjmKyndlAwAllZ10JGh4gP9eHmmqKr0_yD8oLoRbUEwuT9emMj4b02jViA1gEXjhxM_vFzdyEgAvTV2Ke6chfMZYv2lqtOTzQvzz62qXqy5HnlNtBCIDRR1Y4Wcr8lEzCC8GURtxW8N0WJ-WYjk3DktYE-Vs_pz6cc_rrYbsWvQ681zhuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=N2n0dzx7uxJol7Jv792xMCjoPrpISmGdTzlzE1Lw-3NhBC6SD_yBEwBjE7RwQGH2tSD1qmxBV6nxrKeUCYvQmYi0Oc-vrsL-qO3pMBrCSTUAdjqf25c-h-QNsiGynBTxuClrAyPF-991ujLmGKxvJZVc6kzE21KxusQzjmKyndlAwAllZ10JGh4gP9eHmmqKr0_yD8oLoRbUEwuT9emMj4b02jViA1gEXjhxM_vFzdyEgAvTV2Ke6chfMZYv2lqtOTzQvzz62qXqy5HnlNtBCIDRR1Y4Wcr8lEzCC8GURtxW8N0WJ-WYjk3DktYE-Vs_pz6cc_rrYbsWvQ681zhuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.  إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.  ‏إيران لن تصبح المتنمر في الشرق الأوسط.  إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87594" target="_blank">📅 04:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87593">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=VtUn8WqOVzEheA1rPLe2Euq2qSNfP5zUXRdt7TQO4NBJfLm-hiFek-QBnDNKd614AOtiVeBD3u_GDfakDcjM6UsW7_eGlPHFLYUAlVC-LUxWvni4zgF_kXws8vxfV6W_KhyLQ47b_1SADQRVcgV-OTOso5C0znnDKdjdlWYL668QIpwzWcwLr1ObGn6Br0tIoFaFXwiJ4iHlnp27pKHUjZhlyVkcVYHKk7qA6gGz634-5hlgK94tjQ-UE03RR1_pRMLsMiVmkD_aF2INuWpToSIaUJIlgiyYIrkx56Jzfq6AysP1cQH4g_BAZXzqC5_eyk0RxujnoJ7jdvTAtP1ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=VtUn8WqOVzEheA1rPLe2Euq2qSNfP5zUXRdt7TQO4NBJfLm-hiFek-QBnDNKd614AOtiVeBD3u_GDfakDcjM6UsW7_eGlPHFLYUAlVC-LUxWvni4zgF_kXws8vxfV6W_KhyLQ47b_1SADQRVcgV-OTOso5C0znnDKdjdlWYL668QIpwzWcwLr1ObGn6Br0tIoFaFXwiJ4iHlnp27pKHUjZhlyVkcVYHKk7qA6gGz634-5hlgK94tjQ-UE03RR1_pRMLsMiVmkD_aF2INuWpToSIaUJIlgiyYIrkx56Jzfq6AysP1cQH4g_BAZXzqC5_eyk0RxujnoJ7jdvTAtP1ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.
إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.
‏إيران لن تصبح المتنمر في الشرق الأوسط.
إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87593" target="_blank">📅 04:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U33tErTnKHK4OosJLq8C9P7iiujiVTETTvpHFMbER6BUNlxXB7qo_fdmoX0bkOqaCYQZJehe0OV94fNklHlvNxEun05j32bp7n3F3toXBa6CevqWjv13x-_z14p9GAsPId8j-54w77Ug6ftMvXZEsi-CC3A1LLjpLz5lZ27wsq9kk2W-TyO0OdZQbY6BZ3sse03Wui2dRd24_jFaNNFveWncmwrAMlYRrtpJq13mPzOP4vs0dgLRi7gxXPPtuFEwYyIrVQes1_l3pTFheFLIXLbRV2vuNBeUL9xLdNHxCb6eI3k-ttspuBlkDC8KTnK3NKqc5T6hjV0rsNbQQfR-aFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U33tErTnKHK4OosJLq8C9P7iiujiVTETTvpHFMbER6BUNlxXB7qo_fdmoX0bkOqaCYQZJehe0OV94fNklHlvNxEun05j32bp7n3F3toXBa6CevqWjv13x-_z14p9GAsPId8j-54w77Ug6ftMvXZEsi-CC3A1LLjpLz5lZ27wsq9kk2W-TyO0OdZQbY6BZ3sse03Wui2dRd24_jFaNNFveWncmwrAMlYRrtpJq13mPzOP4vs0dgLRi7gxXPPtuFEwYyIrVQes1_l3pTFheFLIXLbRV2vuNBeUL9xLdNHxCb6eI3k-ttspuBlkDC8KTnK3NKqc5T6hjV0rsNbQQfR-aFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87592" target="_blank">📅 03:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
أُطلق صاروخ اعتراضي نحو هدف تم تحديده لاحقًا على أنه نيران من قواتنا في المنطقة الأمنية جنوب لبنان.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87591" target="_blank">📅 02:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=olMkJFDuVaBjFq_kCJOctKWNXSiTdHu1HwRz1qs09OvTU4cxAlMwoup1cFeb6EqvdfUZEKAyjOv6NbWlSZiZpGD8ShnrDKTQQjTxoesCWSFa0nHjaPbqQnUADacXUNfiFg8RGOZYuqhVDoz3KCp0SNCcLeZ61ySLrl-PclJLMv0juSQ5RN6qE1j8IvRvcutitjuLSDGuf5mIepViNJ-A-fH5CjA918qcTbA2T8H7YGPH1SbOMRFZPmvWYCOWP2AWCW6x9ZZmfEOY22wR_EIIstuFsayOD9SPZbhxAlBr64wdAdTRBSBD3_u7egxTMziY2k34AaKOau4SCxfQKESFgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=olMkJFDuVaBjFq_kCJOctKWNXSiTdHu1HwRz1qs09OvTU4cxAlMwoup1cFeb6EqvdfUZEKAyjOv6NbWlSZiZpGD8ShnrDKTQQjTxoesCWSFa0nHjaPbqQnUADacXUNfiFg8RGOZYuqhVDoz3KCp0SNCcLeZ61ySLrl-PclJLMv0juSQ5RN6qE1j8IvRvcutitjuLSDGuf5mIepViNJ-A-fH5CjA918qcTbA2T8H7YGPH1SbOMRFZPmvWYCOWP2AWCW6x9ZZmfEOY22wR_EIIstuFsayOD9SPZbhxAlBr64wdAdTRBSBD3_u7egxTMziY2k34AaKOau4SCxfQKESFgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من مسافة قريبة للحريق الكبير الذي اندلع وسط محافظة أربيل شمالي العراق والأنباء تتحدث عن حادث إنقلاب صهريج محمل بالوقود ماأدى إلى إشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87590" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=ZTNL7Igzy-QaU8GGMHM6rzbrDsmxS58y8oUs6Zqskf1Zik2LAFHvlBaldtJEeIlmpYYBZAauBMYx-mJ4frohwv96K_4S_2ABcwGDFsrjGg-Wq9pbIMOXJIAaDQffSk1SORUnxEuZq3SSxJueLLdXwv6vRtc1aSfyLPG012yp6v9_AqtKhmJrAeaYYTLyNcAd4Nyovr-OXUCw7bgwyAvoSHtaXknuV_nYgAQeHyz-cHifqwIKM8Wc-P9sgX3xBU1mcZhKd5BLwaD4dSF2XCOftSJ8nG_nlI2d8VhoGH9V57oK_DNUM2oOg3OR0hhFipMyJH7GAa2v4Y2W6s9AsCkQGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=ZTNL7Igzy-QaU8GGMHM6rzbrDsmxS58y8oUs6Zqskf1Zik2LAFHvlBaldtJEeIlmpYYBZAauBMYx-mJ4frohwv96K_4S_2ABcwGDFsrjGg-Wq9pbIMOXJIAaDQffSk1SORUnxEuZq3SSxJueLLdXwv6vRtc1aSfyLPG012yp6v9_AqtKhmJrAeaYYTLyNcAd4Nyovr-OXUCw7bgwyAvoSHtaXknuV_nYgAQeHyz-cHifqwIKM8Wc-P9sgX3xBU1mcZhKd5BLwaD4dSF2XCOftSJ8nG_nlI2d8VhoGH9V57oK_DNUM2oOg3OR0hhFipMyJH7GAa2v4Y2W6s9AsCkQGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الحريق الكبير في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87588" target="_blank">📅 01:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=rk3eNruKrVkcDsoSYTypmSCdQKlJGkvtU7BQlDayXU94O0wzDhdJltzokww8f6QDbPnNr6ME3Ucsv7aYwGPruaV5Y8c00ILyVEui_X2540sxph_ACvTbmlikkyiYsnRqSR8O1jeU6HRx2bmJCVGiSgHlmABgg_E05uBiSEYXCf612Qi1WS78QBDrqEqY-0XmxN1q-OMh-UVAryZozSejmoCqfc4drwnYQnN_oluzUnnVfD_g7EURXY6TC_Gj0W0d97evJ_GGYx1uaQuobwc65u8eMmrb7zdPqGVnUaZFXiO4D4LPbYDyQLhJS8mQ5xwaGf_WzoYtwfIcHFbWNBCm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=rk3eNruKrVkcDsoSYTypmSCdQKlJGkvtU7BQlDayXU94O0wzDhdJltzokww8f6QDbPnNr6ME3Ucsv7aYwGPruaV5Y8c00ILyVEui_X2540sxph_ACvTbmlikkyiYsnRqSR8O1jeU6HRx2bmJCVGiSgHlmABgg_E05uBiSEYXCf612Qi1WS78QBDrqEqY-0XmxN1q-OMh-UVAryZozSejmoCqfc4drwnYQnN_oluzUnnVfD_g7EURXY6TC_Gj0W0d97evJ_GGYx1uaQuobwc65u8eMmrb7zdPqGVnUaZFXiO4D4LPbYDyQLhJS8mQ5xwaGf_WzoYtwfIcHFbWNBCm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق ضخم جداً واعمدة دخان واسعة تغطي سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87587" target="_blank">📅 01:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=D0kgzrmIDZzUvJaJcNyilo0A-82MD1qmSTlLnEMVDaN75cH91mkhWw7oDxXncG1G5uSQn0hLQLjnDZUHyZgnTXGr_RwApgKEiigsTpQd7gXu3vLM2bMJQ2rKW0XOjb6zDh8zh7tG9Q-3ODELkaCVfinyqBHZ0AVaW4bTQAJhnNsHJCYwwkELAoq-kbHrZ08BoE7ZV87UO0U4a89B6yTxN7674s4gHvoQO7gAyLym1mEP8B73T9Gzfe1qKR1JiEwdvrUCie2Kq1OYtzVv-9S8RPAF-EzR70BqQdzdvTe0qUF7A0Mqkmmin7ht2zN2_IWLwNo9FkbeNcm6mtM8kYj5Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=D0kgzrmIDZzUvJaJcNyilo0A-82MD1qmSTlLnEMVDaN75cH91mkhWw7oDxXncG1G5uSQn0hLQLjnDZUHyZgnTXGr_RwApgKEiigsTpQd7gXu3vLM2bMJQ2rKW0XOjb6zDh8zh7tG9Q-3ODELkaCVfinyqBHZ0AVaW4bTQAJhnNsHJCYwwkELAoq-kbHrZ08BoE7ZV87UO0U4a89B6yTxN7674s4gHvoQO7gAyLym1mEP8B73T9Gzfe1qKR1JiEwdvrUCie2Kq1OYtzVv-9S8RPAF-EzR70BqQdzdvTe0qUF7A0Mqkmmin7ht2zN2_IWLwNo9FkbeNcm6mtM8kYj5Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87586" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=nzpnXU0g1sC1MOnUHZS1417p0hUQ12Brt9PQdD-85k02O7xfcU8PhbiWAhCQ_8qPBKRfprxvn1slUmdMl206-TKgwiFRc5nFx7ON2Wwu26lHxEbF3exLNb8WioKoRr1LH0bXdmXS_N2RKdihHEOxaCEpr7kY4ygcpB6fHaM3kB_A6HmXJcp8DpCQcgY2etd9_O2ngrTKRP4lOF5-v2jioC4EhitgSGrDaTRJeCMZxYh0rQnhpKRQCoCfbPDoWMbcq9KGeMq1UIMD1cAH2xBEYKMwiWDLETsF8gbCcFayfAdD1vavY1kM2W6E5rpZt-ACGBlhiHF0JPmWaUhdhPoQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=nzpnXU0g1sC1MOnUHZS1417p0hUQ12Brt9PQdD-85k02O7xfcU8PhbiWAhCQ_8qPBKRfprxvn1slUmdMl206-TKgwiFRc5nFx7ON2Wwu26lHxEbF3exLNb8WioKoRr1LH0bXdmXS_N2RKdihHEOxaCEpr7kY4ygcpB6fHaM3kB_A6HmXJcp8DpCQcgY2etd9_O2ngrTKRP4lOF5-v2jioC4EhitgSGrDaTRJeCMZxYh0rQnhpKRQCoCfbPDoWMbcq9KGeMq1UIMD1cAH2xBEYKMwiWDLETsF8gbCcFayfAdD1vavY1kM2W6E5rpZt-ACGBlhiHF0JPmWaUhdhPoQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87585" target="_blank">📅 01:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
أصوات إنفجارات مجهولة في سماء منطقة السيدة زينب بالعاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87584" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtVaZDW94LXjqgUMoRYPUn7edJTYDRJX5VLi9VBY8tRHUx-Ko1aZU-qEMw6UKdlRvIyQzdyKDoeXvkSGfM3DrENYqO1V_91U5yCI-I1FFIVKn5-uZ09K8RT49fa37WCyN9qx7bajIF3IRwBHfLiixHha5dXc-YTacPt5mwzXBo_OIeMQ3o18V1RZT_8nJXqIhrxdMyC5YySDzvSVmJRclAvnGXrdFcdG8nPCXQ0PO-ewk9QZOv4rCwTgxJ6BJhVK0Re0YF5hWQSEn5PKjjfrXuzUYSrw7JafiAUDGw5qtidc4eMdNX-UqWOgPITFlEuATLlrMnpmyDY7A4AY-ImklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
الأدميرال علي عظمايي
قائد القوة البحرية للحرس الثوري؛ رجل الخطوط الأمامية في المواجهة مع الولايات المتحدة</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87583" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87582">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي منشغل بازمة الصواريخ الاميركية:
أطلقت القوات الأمريكية حوالي 50 صاروخًا من نوع "باتريوت" لاعتراض الصواريخ في يوم واحد، خلال الهجمات الإيرانية التي استهدفت القواعد في الأردن في الشهر الماضي. ويقدر التكلفة الإجمالية لهذه الصواريخ بحوالي 200 مليون دولار في يوم واحد، حيث تبلغ تكلفة كل صاروخ حوالي 4 ملايين دولار.
استخدمت إيران صواريخ ذات مسارات قابلة للتعديل لإجبار الولايات المتحدة على إنفاق مبالغ كبيرة وتقليل مخزونها المحدود من صواريخ "باتريوت".</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87582" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
في خبر مفرح للشعب العراقي
الأنواء الجوية:
انخفاض تدريجي بدرجات الحرارة بعد منتصف آب واندفاع كتلة هوائية معتدلة نحو العراق.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87581" target="_blank">📅 23:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFb0n9T-bTWELtV64sb7HQx2p75GM-1WBJ33hI-MqpTrPGFBwfc-NWgB4OrDHYtmDJQ7OcFbBEFarmFvbBJK1nRUziprqEP3-4gzAw-HHdlRrDjvPvWeIW5WPJxy_RmZrtYXXFMjr8N4rf9gfLx8kfTAGiqk_EwNrwQ57sAzxpbzo5ekOZyJuRIuU4vNTYmt0yAvQREJBf34v7lJPypkdgEAVsWiJ4G-68U-hdxaeQ2gHf3Y2E2bNONsYo-UJK7uceM6y4Cx9D1zcXZpOmLSZiZLjCogroG9oo8TkKWzc_YXdbpXA6MhpFln60Sfh8RJlhsVEWZaHIwUryT0_WziWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAaOZViDHaY852El_77PVQfdYXSljgjBtv-1zEWPh9cx6TETsZOmxCjmG2ppkdMpoUklu0uRvaLx5GvXbSvqUB_7py7n57nk4I_vZQogr7YgW9NguuqtQS3icjunleirKc_qwjHQuvmrewhrKrUMZFZGiaF7bIG-SyGmxWmqcE9R10BIqjmBfD3GTFt58qvksxipfreQpW2-EjwlRpdVBsLS-u6bYpLrFMTyEIYpS8AdjveVfXI5IHjiBHQJAyCTigbe972YVK7vE4YGJbO7OtbBKmLLW4XP1LOy9aPqi8V09rtUPnHqWWwtx8V89xyXf0lf1Lfk3PGjbuLzOAsbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ow0dlG7apzcPOYlDfc0DE_bPV5Yw67DOjQIzbWiwB1usT4xf9VGD0QK5vZITn0DWNaPRCIEDxV_bnGFhRDxXry32MS6jbuyqzhJmaAWPcV8s9Kbm4X9Fie4U0F-mxzVO-ww3Bp6wMdnEvNjdzJpY-cQ5WKfUw-9KCYUSPC5vgTXL-R8DHBNdpR7RhYeG68Uqwc33fHEg8mGx4qBuqIGoaXQWvt8SXELkKAJOuDWlSRQZ4mz4SYbXPE5qxJsr_18eha_u9PE4TBKNzADF0wGqRnjhiKwdBjZHsUnO7z23qABWasaGBt5JYViBeoAeGzeSuh60L3WspWjdQ_B06eKcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Anu1WERRRESWgr_s1VJk4XEcb4rRfic2TJpkU8AVYroW8tAYWXgrSOXOjeRrGSE_VsOTbPLiuERRfqxr8gvG3mpNsr0DBois9Vzj_Q8dql0i3xFkuE5Yg3uN_o39-qAAw4tFHrr4vJIA1dlxUiglv8RRxj0-AMv-Dnxlnmm0tmyFvUoI4VL5FewgV3OftU8nIcS9ErnTukqBaFgqFU7lpNR4x7sJ4dsW0xWDbRJnuQ8CChFLHoAdRLfvBA-oQNR8_zHXApQL79Qyc-fQ3e99L9A4XxclunIBDpZCgF5941AWLPHgT-CH3UjFSlPWAw44SjpX37p7XlbqsGsaM05Jfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87577" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87576">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇾🇪
المتحدث الرسمي للقوات المسلحة اليمنية
:
تمكنت القوات المسلحة اليمنية بعون الله من استهداف تحشيدات العدو السعودي ومخازن أسلحته ومقار قياداته في منطقة المخا و معسكر تداوين في محافظة مأرب وذلك بعدد كبير من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابات دقيقة بفضل الله وخلفت عشرات القتلى والجرحى بينهم سعوديون.
إن القوات المسلحة ستواصل عملياتها في استهداف كافة التحشيدات السعودية التي تسعى من خلالها للتصعيد والسيطرة على بلدنا العزيز.
تجدد القوات المسلحة تحذيرها لكافة المخدوعين والمغرر بهم من أبناء بلدنا إلى مغادرة مربع العمالة والخيانة قبل فوات الأوان.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87576" target="_blank">📅 22:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87575">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يوجه بإعداد مشروع قانون لحصر السلاح بيد الدولة وفقاً للسياقات الدستورية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87575" target="_blank">📅 21:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87574">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87574" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87573">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارين متتاليين في مأرب.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87573" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfIcEvg2P9M6hjv8ssOd4B5u1IRMHrHk2cHmOiu1Qxc7aiWxNnaL2xgw63aga9Tz-XdIMogM3oKrquzFll6oA01TW94TccSPM2eExUdeOJiLnBo9_HcNerhW15jV2w3_y96Kwd2hKOUudfPtOzuO9WkaLBqQL5vNNhvW1IfbC_idtxAZJ8DmU2Z03Cn1LaKz09IUGJn3fVgbMXmhsu9plzNm0a3ZnlE3AL-NZbXJTpxz5WOsyCFH1HCUJFd8UtRrgubuoXMUEVzxVpn6bG6qsI27m7OfXIvg1qNCvYAejOHvJhHy5_pLpFv5KOVtJ8qtcaUvPnr5V8rRC6I-r5h_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87572" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtC-y_jwaPDyNGUK0A9ctKKETmXiJaRanJCBcxFCii7fo1XOL2gNnBTwYMI46jmuCVrU5lCi_5udhdo1tSjpX-AXDSllWSc6FhNkP2xktZnqbL0wVBQMKOT9Tpudb7V2us8Ezjz9mTk_kmxiZOkbe-o7piHBwcuajf3vpa4VJN1wcHqvXbYfGscNPIRvloAuWe-wuDVaqWiqQFlR5PqvEi_6DYLhIqmqXfa3r-umMYQJi8c2Dxeb1TDMBL_ZTJrCL52XQ8t6NSycaNebv2HD33Kl8TeoslCbnB9e2hlqPIJ8dUjQkE53E7LU1uTB4VGNpch-xfLEPaR4viWS1bMxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
‏دميتري ميدفيديف: أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87571" target="_blank">📅 19:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏ترامب: "ستصبح دولة جهادية. انظروا ماذا يحدث في ميشيغان..."</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87570" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">المركز الأوروبي المتوسطي للرصد الجوي:
"أفاد شهود عيان بحدوث هزات أرضية في كولومبيا قبل 5 دقائق"</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87569" target="_blank">📅 19:27 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
