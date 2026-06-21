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
<img src="https://cdn4.telesco.pe/file/mS2imGDr675hJ8BXp3mRkUQ_ZEafQTKKiL8CoLokq8OPRpG1z5D_8or4yLr28va6PjJQyCHTwbTOxtUux3JH9PGq_baAWflqybossL7_40CsPQd3FBJATjqe86Ks2Aa2RlNejQ-w8YWtH3pmjIkIsZrejsg3GPT8_-wKQnPXRFqlJuNbQUTsosnaiPLjXeRKUPKfgfzjSyBNLq34OiiOJcEraAyzw0Bpkq8STWb9b5-HLK8Ye9jwhmHnZi8sUEa0N9XCkqxXehLLBUCrLiwPYF-jXmCvQVcvYg9L0px62fiail2YCysZO_lyTDbTPU4zxWq4ixhge4sgigRgkSDM8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-79502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
حققنا إنجازات عظيمة ولن نتخلى عنها. سنبقى في منطقة الأمن في جنوب لبنان طالما دعت الحاجة. وبالنسبة لإيران، مهما كانت التطورات السياسية، لن أسمح لإيران بالتسلح بأسلحة نووية.</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/naya_foriraq/79502" target="_blank">📅 18:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/naya_foriraq/79501" target="_blank">📅 18:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
السيناتور الجمهوري غراهام:
لقد أمضيت أربع ساعات ونصف مع الرئيس ترامب يوم الجمعة. إليكم ما أعتقد أنه سيحدث بعد ذلك. إذا فشل هذا الاتفاق، فإن الرئيس ترامب سيسيطر على مضيق هرمز بالقوة.
ستتحكم الولايات المتحدة في مضيق هرمز. وسنفرض رسومًا على جميع الذين يمرون من خلاله لدفع تكاليف العملية.
وسنقوم بتوسيع اتفاقات أبراهام في السنة التقويمية 2026. سنجعل المملكة العربية السعودية تنضم إلى اتفاقات أبراهام.
وإذا اعترضت إيران على سيطرة الولايات المتحدة على مضيق هرمز، فسنقضي عليهم.
إلى الإيرانيين، إذا كنتم تستمعون: عندما تستخدمون حزب الله لمهاجمة إسرائيل، ستكون السياسة الجديدة هي أننا سنهاجم إيران.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/naya_foriraq/79500" target="_blank">📅 18:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
🌟
مبعوث الولايات المتحدة في الأمم المتحدة:
إن إسرائيل والإمارات العربية المتحدة "عملتا معًا عسكريًا" لـ "الدفاع عن بعضهما البعض" ضد إيران.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/naya_foriraq/79499" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله:
لقد بات واضحًا ومؤكدًا أن جولات التفاوض المباشر التي سيق إليها وفد السلطة اللبنانية إلى واشنطن، ليهز برأسه ويبصم على ما تسطره الإدارة الأميركية من إملاءات تصادر سيادة لبنان، وتنقل موقعه السياسي إلى ضفة المتصالحين مع الاحتلال الصهيوني وكيانه اللقيط.
ليس مأمولًا على الإطلاق أي خير ينجم عن هذه المفاوضات التصالحية، لأن منطلقها خاطئ ومريب وهدفها إذعان واستسلام.
إننا في حزب الله ندين مجددًا نهج التفاوض المباشر مع العدو الصهيوني وجولاته وما ينجم عنها. وندين وظيفتها التعطيلية التي تشكل عثرة في مواجهة مشروع العدو وجهود الميدان المقاوم والتضحيات الكبيرة لشعبنا العظيم، والتي يمكن للسلطة تثميرها والضغط بأوراق القوة هذه، لتحقيق انسحاب كامل وغير مشروط من أرضنا اللبنانية.
إننا نعتبر أن مواصلة الحضور في جلسات التفاوض المباشر هو تنفيذ لأمر اليوم الذي تُصدره الإدارة الأميركية للسلطة اللبنانية، التي تُلبّي متفردة بقرارها وبمعزل، مخالفة للميثاق والدستور والقوانين، وتستجيب لما تعمل له أميركا وإسرائيل في زيادة المخاطر على لبنان واستقراره واستقلاله وسيادته.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/naya_foriraq/79498" target="_blank">📅 18:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVEsNOtmxlBXvv0BARLXZwXz4fvdCxvGNQFR-AT-bxLficnVmH3UhFZ17h8qLBra19317sdoLp7JPZGOJbjyiWWVZgUlEzX-SWItj40qGctAm2jIeJUNP7YmW397B53i3m6qu_qsHm7mrVglXi1ql6wT9aA3yCR-cfuXRYOggn_S_lBU19c9Kpvlm7yxU2dfVhTvnvIfbXQ9CessqN9e19HqQulEnDWTkmLMBTCXv9w7AJc_Ok7OBO-Sp_385cE7CAv8mJSnKwtTGEo0Osp0lyS9BK3sMlml2QHMeLNAw5dgDuqM7L4cFD9yeKnHQiQMlqu29aovrG1k4kbuevpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
لن ننسحب من المناطق الأمنية العازلة في لبنان - يسرائيل كاتس</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/79497" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منظمة UKMTO: حادث على بعد 50 ميلاً بحرياً جنوب شرق مدينة الشحر في اليمن.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/79496" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/79495" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRO4UfjIfucl7vfknGTo_WadG15cs5-LHzJk2cUJ29-SMufxiw5Q1xiR2IecCndaxcrI597QQcnnL-Opf1F9CgBZOaFd4WypPvJfRGSdunB5SxI9TnDAymAGSUq2XpK0vFoP9vDlmJ6GJjIe8DbNiaC_T8-1jaA0LzarDRO4qWvRktaz0VLYg58ILG60I5mqRgodCCpIws0VfpqI2-PMNuMrCveCkjMVyMpBItEyRxx7uWwle1Mm6WVbSpTPqzcRFBQPXGHFju1HfQAtBL13uLqIE5GJlYj6xPMaOl7bHrPMH1Cpu610D8iuAaEIRl9gY6zJcGrFxAW3hZ2cmm_uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/79494" target="_blank">📅 17:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-zUPNm4xFq3dAqds0VDYNOaEAIHmWMwVbFaGHr132egM4Mqak20c1iFb36qnp94jP-W32u0nr1SxQBQ5REB4ojrN8syImCBCFouFcIeBdc96eKOnCf3dIiWTrA8-JlvoCBTQUBdeROEfUcgQKUygOHECzW0RGjqEmnGpHESEEJNdQRks46G5ZqKNYWeTuGvwxdFuX0HVC1h-8rNijSdodhk1Xld_oEl3fRgFFcUgqGgd4cevbM--VKjNm8Dbt1AbLt8xFTOMurVFWfiVOFUS91qLWxj7wVTuIdxPzOHkt4RYJ0s3vfW2cc_OR2LFEtS6VUgkfJ6WEc34fSZXdl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
🇺🇸
ترامب:
سيستقيل كير ستارمر من منصب رئيس وزراء المملكة المتحدة. لقد فشل فشلاً ذريعاً في موضوعين مهمين للغاية - الهجرة والطاقة (فتح نفط بحر الشمال!). أتمنى له التوفيق!</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/79493" target="_blank">📅 17:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من الفريق المفاوض الإيراني: مضيق هرمز لن يفتح دون كبح جماح إسرائيل في لبنان.</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/79492" target="_blank">📅 17:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/79491" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
‏
ترامب:
على بزشكيان الالتزام بقواعد اللعبة وإلا سنستولي على إيران.</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/79490" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/79489" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZhGE8ts5VDxzp7BiaZD86KP_j0aSgepsksxlho9RDVsXllgBCgZClLTk-i-efbAA_1qkEkrhOb5H_Up2VHFotzl8-ufPLFsT4fzDvA8c0M407qWkURUsgCYhSMLoh3CQUwUPgL6hNKRbK8eE-LjU1nIYwLuYylc-WEvxPuCzExLwKwSXi2IFY4qzK1iYtxAcpyMsN07Nhg16H8TVrZEJ6EJ1BIhRvlP-8PMsaZyCPcNqRmq5JxBLUoQ8CP2pCiYLMcLx1iBDWdL2lxZm9H8ACblDahHLKUbSf8-Ep-47pggQHhgU7Ok7UkTVEVcs78RycxwonQVty4Kx6hjYd9EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
يجب على إيران أن توقف على الفور وكلائها المدفوع لهم بسخاء في لبنان عن إثارة المشاكل. إذا لم يفعلوا ذلك، فسوف نضرب إيران بقوة شديدة مرة أخرى، تمامًا كما فعلنا الأسبوع الماضي، ولكن بشكل أقوى!!!</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/79488" target="_blank">📅 17:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79487">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/79487" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgdG1-wdCOBUoMhC6QqFSISP-FwN-t41mGNAX_OrwKcZCaB6J_GW5JaOMcmfihpa5PZ57zcPrUeC9TY5SWJ4__ULSYpWGI1WRjEfQwY5snM52q_PD-9valGjxkfiGQreFt3fPJZ9NAj9dmiAq0V6rUXZ3uKrxoiqbgLHm12TYsni5MxwvNzgw8HUOG0u6QS-GK6GnUqmfPz4In2wdDRgBgciAJcM26TcaCSlBXQ-cWOgLFdHgvVwrmr7ycVUA8z0YmkbbS7C2wThb96fW8wG8OJacnxw1VoUg65T1N6RL_UxgPZ02KOqCysLa7ndEnA0OAn0yqTlEIaQS7MI7L_MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب عن الانهيار الامني الذي تشهده المدن الامريكية بالتزامن مع تنظيم كأس العالم:
هناك الكثير من عمليات القتل تحدث في شيكاغو. 22 شخصًا أصيبوا بالرصاص، و4 قتلى على الأقل. لماذا لا يتصل بي الحاكم بريتزكر لطلب المساعدة؟ يمكنني أن أجعل شيكاغو مدينة آمنة في شهر واحد، وفي عام واحد، ستكون واحدة من أكثر المدن أمانًا!!! لقد تحولت واشنطن العاصمة من واحدة من أسوأ المدن إلى واحدة من أكثر المدن أمانًا في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/79486" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79485">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏ترامب يهدد: المفاوضون الإيرانيون لن يعودوا إلى بلادهم إذا أغلقت إيران مضيق هرمز.</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/79485" target="_blank">📅 16:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇺🇸
الوفد الإيراني يرفض التقاط صورة مشتركة مع الوفد الأميركي.</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/79484" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#ترفيهي  ترامب: أمريكا قد تصبح الملاك الحارس لمضيق هرمز وتأخذ 20% من النفط</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/79483" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
ترامب: إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/79482" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
ترامب:
إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/79481" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فانس:  إن ما يمثله اليوم حقًا هو بداية مفاوضات فنية لن تحل كل خلاف، ولكنها ستسمح لنا بالجلوس معًا كفرق، ولأول مرة في التاريخ، لمعرفة ما يهم الأطراف المعنية أكثر، ولتسوية تلك القضايا، وحل تلك المشكلات، والوصول إلى غد أفضل.  ‏إن سبب وجود القيادة السياسية للدول…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/79480" target="_blank">📅 16:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فانس: ترامب ملتزم بتحقيق وقف كامل لإطلاق النار في المنطقة</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/79479" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فانس: هذه الهدنات دائمًا ما تكون معقدة بعض الشيء.</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/79478" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فانس: حثنا ترامب على "طي صفحة الماضي" لإعادة تشكيل العلاقات مع إيران</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/79477" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فانس: هدفنا هو إعادة تشكيل الشرق الأوسط من خلال الدبلوماسية المشتركة</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/79476" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فانس: تم إحراز تقدم كبير في الساعات الأخيرة</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/79475" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/79474" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCFt2XLFVQR6gg6h2FQsEwFc340nibuF8paYuU1ndj3VjZdG_bIbPcBfkiClI0IK0fPw4HdHYtHRIK4_KnSwsTCB6ofmvmKFLwnvH-k7Izs9T6R3GJp8FuqVejFCzx3YkUnMLGV02l1fvH6zwzc97Y09imt3DjPNPmqWC0RwAFaAh_QuV3T2uLByTsSTB5TcXbuSchTUFEY2Y7b4qc63qLbIcXqvTWFSH7oVox3uhj1rcoXtMTyS--9-pzYx2kDEkB32GPAWlopkHJYpLQ-fgmkHJ1R-Xfd73dRWx0ARfadFiA9lecHVf1gi1w7KaBRMS6z7ph5cSDvbdYZqnXkF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/79473" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/79472" target="_blank">📅 16:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-06-2026 آلية هندسية تابعة لجيش العدو الإسرائيلي في أطراف بلدة أرنون جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/79471" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/79470" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQpzmUtV_mCiPvwXfPKrNwz5sIk8KRGZ34WYJvhDa5igczdGGTUlz3RhEKDFBnSLXt-DB4qGa804IwvB-FDlqdFLMlZklthJXbgmb7UtpQGjzy_hrQ07nz9efTHvvBs0Xw0Z0Xi_8Jg2dmZ8sdQvssCyzdAdAs78djy1P-eUxoMY4hBDVW7OxLx926RT08XG65ZGj5DSFWtgm9V2UNJgmKc-ZrlQMiCQ6CN_crUiE1y8LfGlsF6BsWFPe2624fyBDLisa9eJsYboeaEnnln6FajrPSuhA4vHaWpEjVheEKBM7_zcR8-BPwLEUuN34T0DMa-TIJK28mrZZY3P7yxmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿ وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِندَ رَبِّهِمْ يُرْزَقُونَ ﴾
تدعوكم المقاومة الإسلامية في العراق كتائب سيد الشهداء لحضور مناسبة الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي واستذكار سيرته العطرة ومواقفه المباركة.
حضوركم وفاءٌ لذكراه الطيبة، ورحمةٌ تُهدى إلى روحه الطاهرة.
📅
يوم الاثنين 22/6/2026
🕐
الساعة الخامسة مساءً
📍
بغداد - البنوك - شارع الكنيسة</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/79469" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiT8ewQNS14nIts3HcpszNKoUYWLoLlawfnQ_2Iq5d01NYYPdAocPheOoy6yJwnwYo8zecDAhADYvHAhlLRSAjEqOAbvUJHfTwp9DYzhQZOVyR4KDZxXNXrvNfO7jpWFTjvaWDF1EQlI6Q3o8CfbMSOTqdRPrjOWhrZSdPVh7J9HYBVakCPJt5QN6Ah56z8XIGFP9wbJcjkkk3ylBwIOW4hDInTWv-Bjy3-CHtBqvmJN2fVkrlqXTXK7I49par7Xn-drL53rYySQ3AMa29ghs_JZCOehYvO0LG5NJYXqZFWvEVCVVC-6O3VMop0v2sHA1D32z1yve2H8bVCsGoDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران الشيعية
استخدمت مضيق هرمز من أجل شيعة لبنان
برأيك لم لا تستخدم تركيا و(الخليفة اردوغان)
مضيق البسفور من أجل غزة!!</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/79468" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy7d2Fs0JwfLra41C8mst4CIzPmep_3VjHxlong7WydQAml8d-Z-tQ2LTummghxvAiPhXhI2BT6EjAMMREsL3gEgXQwhKJ4dV-pUER7mxNKmptEQPufTjQkc7ZzSLXdWLWy6BYo0dRWyu_hhBXhAfb7ydarz3BGBuseF6XWbTEypSA0KgA43ovYPyiW9qOlErWChvZUf2y9ocaVDtgp_smabBvsuib1H7uz-Ey702vQJsE6lLCkXE37pjDFDtufz6jOKgJYrPFWx6nVoIhvYxpj74H51HvzkByrhYcdq2JSNrP2c0bjtW7Wn_vB2cMMad1QiUk72jsFYHWNTI5EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعمدة الدخان تتصاعد بالقرب من سجن بادوش في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/79467" target="_blank">📅 15:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
‏
وزير خارجية باكستان:
أميركا طلبت نقل مخزون إيران النووي وتوصلنا لحل "خفض التخصيب".</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/79466" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
مجلس محافظة الأنبار يعفي (رهيب حميد هايس) من إدارة مؤسسة الشهداء في المحافظة اثر خلافات سياسية داخلية داخل المحافظة.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/79465" target="_blank">📅 15:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دهوك ضمن اقليم كردستان العراق قرب احدى المستشفيات اثر مشاجرة عنيفة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79464" target="_blank">📅 15:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
محافظة بابل تقرر تقليص ساعات الدوام الرسمي إلى الساعة الواحدة ظهراً في دوائر المحافظة إعتباراً من يوم الأثنين الموافق 2026/6/22 ولغاية نهاية الدوام الرسمي ليوم الأربعاء الموافق 2026/6/24 لغرض فسح المجال امام المعزين والمواكب الحسينية.</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/79463" target="_blank">📅 15:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قاليباف ينشر مع بدأ المفاوضات</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79462" target="_blank">📅 14:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcfQNDZqDt4HmBt1OIaNgUh-uz7OQIMGi9iEvhEQ0WdEo-EgNp-zkth92YxlAXfzYyrppe5sq1_hZlTKOesNUeMQKTNyHdm6-qFHr9VIhAW0VxpWiic1XK1ROi-b_hcTsP_yXMRsKlqfkgTJrKaveMjRr7Vl_faAKeLUUk_lc9yK57p1LM51qm-QC94dH5xNZ8pUR4TcpY0SMNau7Twy59tv6YHUu3PDt_lxv_cIHKlhGpRpMTrw0tf_LuPTE6uYRU-qGa67JWlsyhnDiAoJjcVdBPAD8demKAQDEV-YJ1jpNnsaz9KYtVSbwmxNxm9fGr_RF1KwtePOGFfEdMfeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضيحة تهز إقليم كردستان العراق..
ضبط رجل الدين السلفي البارز وأستاذ جامعة السليمانية (عبد اللطيف أحمد) متلبسا بإقامة علاقات جنسية مع طالبات قام باستدراجهن.
أكثر من 10 طالبات أخريات ضحايا له تقدمن بدعاوى قضائية ضده بعد إحالته إلى القضاء للتحقيق في القضية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79461" target="_blank">📅 14:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🫡
خلية الاعلام الامني العراقية:
في تمام الساعة 02:00 والساعة 02:20 من هذا اليوم، تم تنفيذ ضربتين جويتين ناجحتين على مضافةٍ لعصابات داعش الإرهابية في مناطق مترامية في عمق صحراء محافظة الأنبار. ​وقد خرجت قوةٌ مشتركة من أبطال الفرقة الخامسة والصنوف الساندة بإمرة قائد الفرقة لتفتيش المكان المستهدف. وسنوافيكم بالتفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79460" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم الثلاثاء تزامناً مع ذكرى استشهاد الإمام أبي الفضل العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79459" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
وكالة مهر:
اجتماع سويسرا سيناقش 5 بنود من الاتفاقية من بينها بند وقف إطلاق النار الشامل في لبنان وبند الأموال المجمدة لإيران.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79458" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
في السابق، كانوا يقولون إنه يجب التفاوض بشأن صواريخ إيران أيضاً؛ لكنهم الآن يقولون إنه كما تمتلك الدول الأخرى صواريخ، يجب أن تمتلك إيران أيضاً صواريخ باليستية. القاعدة تغيرت</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79457" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
- تحذر مصادر في الجيش الإسرائيلي من وجود عدد من الحالات الأخيرة التي ركز فيها حزب الله على استهداف كبار قادة الجيش الإسرائيلي الميدانيين في جنوب لبنان، وهو ما يثير مخاوف جدية ويتطلب تغييرًا في أنماط العمليات.
- يُقدّر الجيش الإسرائيلي أن حزب الله قد أعاد إنشاء نظام مراقبة وجمع معلومات استخباراتية مقابل الخط الأصفر في جنوب لبنان، وأنه يشن عمليات ليلية لتحديد مواقع القيادة العليا في الميدان وشن هجمات.
- يقول مسؤولون عسكريون أنه لا يمكن تجاهل حقيقة إصابة قائد سابق للواء 401 بجروح خطيرة جراء هجوم جوي بطائرة مسيرة، وإصابة نائب قائد الفرقة 36 بعبوة ناسفة، ومقتل قائد الكتيبة 52 في هجوم جوي بطائرة مسيرة، ويجب الأخذ في الاعتبار أن حزب الله يستخدم التكنولوجيا، لا سيما ليلاً، لرصد النشاط اللاسلكي والإشارات الدالة على وجود قيادة عليا في الميدان. وأضاف المسؤولون أن هذه الجهود تتطلب مستوى عالٍ من المهارة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79456" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية: استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79455" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية:
استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79454" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZh3fznDi33Fi9vlWmwFPjCodsYTxFtnDpVwRz_J1SYgI2D_yksTmGFUWA5QeE55r2KkpVWENjCbO0svav-UoB20cx8Rj7Bc_vqT1vz75Ra4YQV08W_Qkv9qRCBTwSWfhc-41i6LbHIS7YRGTWxL6r5DCedKDF3ZMbcV33sWZDY3hnH53A4Aoa7QOp5tfxJv1A-KH2LGwHF-VBhHNweI1cI1RSBIk8YJl22xaCjbvtE1aBkeS_CG_MFJbYFO1NPd43BOhxysxBzlCpu0yPyyW1Ua_rcEaOYsLNc4rC2MQ5hgQFRbBSqH0rAMTwMR4xNh6OLRo4URiXBAJc82mbBjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
رسالة نائب قائد كتيبة 52 في جيش العدو بعد الكارثة التي حلت بهم على يد حزب الله:
كانت الأيام القليلة الماضية من أصعب الأيام التي مرت بها الكتيبة. فقدنا قائد كتيبتنا وجنودًا أعزاء سقطوا في المعركة. الألم عظيم، والفراغ هائل، وقلوبنا مع عائلاتهم المفجوعة.
رغم الألم، أنجزنا أهم مهمة ممكنة - إعادة رفاقنا إلى ديارهم. بعد جهد كبير وفي ظل ظروف صعبة، تمكنا من إنقاذ القتلى من ساحة المعركة ونقلهم لدفنهم في إسرائيل
اليوم سنرافقهم في رحلتهم الأخيرة. سنقف شامخين، ونحني رؤوسنا إجلالاً لذكراهم، ونضمن أن يظل إرثهم وروحهم ومثالهم نبراساً لنا.
هذه لحظة حداد، ولكنها أيضاً لحظة وحدة. الكتيبة قوية، والمهمة مستمرة، وسنواصل القتال بكل قوتنا، بمسؤولية ومهنية وشجاعة - حتى يتم إيقافنا، وللمدة التي تتطلبها كل مهمة!
أيها العائلات العزيزة،
في هذه الأيام، أنتم أيضاً تحملون عبء المعركة على عاتقكم. إلى جانب المقاتلين والقادة على الخطوط الأمامية، تواجهون القلق وعدم اليقين والتوتر المستمر. نيابةً عن قادة الكتائب والجنود، أود أن أقول لكم شكراً. شكراً لكم على صمودكم وإيمانكم ودعمكم وقوتكم التي تمنحونها لأحبائكم كل يوم. أنتم جزء لا يتجزأ من
من عائلة الصغار وقدرتنا على إنجاز مهامنا حتى في أصعب اللحظات.
"سنعود من مهمتنا مرفوعي الرأس، بعد معارك دامية."</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79453" target="_blank">📅 13:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
‏
الرئيس الإيراني مسعود بزشكيان:
لن نتخلى عن حق تخصيب اليورانيوم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79452" target="_blank">📅 13:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCZDP9cvt-PxZOKWruB5r6CbvsarqMxzYaatTEWaWceAilI1k5uaLHoWzqPZ21CUGG2hDO5wEOWBjs6JlvT4VaUEmpq22rWYvldcq4eCX1R0aeTRJJVie_WxLr5s_6Gw01xv4ZWRf_R0bFv6WN4bOK56-ks8Ppvkroifc0fBa8MwtyxIBzoD6xJKeXh_Dfjpawvkh_sB2iNADobYwiQijyl63g2ak4s-1B6AHdIePIepZqaE07_QtxqKyXBUp9Fa-5XmfUoG5pzqBeZSnqBEq95vC0nVErq4bYQi6Z-5wDYzLZ9JXSpmvA6LXNTKRCL75Wv2FWfPgjDZ3PccJYTm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🌟
مطار بن غورين يشهد إخلاء طائرات التزود بالوقود وتوزيعها على قواعد سلاح الجو في الكيان المحتل حيث تبقى طائرة واحدة في  الساحة الغربية لمطار بن غوريون</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79451" target="_blank">📅 12:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
هارتس العبرية: نتنياهو أمام معضلة، إما البقاء في جنوب لبنان والمخاطرة بجنوده وبالعلاقة مع ترامب، أو الانسحاب وتلقي هزيمة في مشروع حياته.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79450" target="_blank">📅 12:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNeoX7vjSlUboH0k1EEzHnxTHti2F3TSlXvnWuy3bkiX8U3KONZnufiLX4gf0wyHd2CYc3nHxvFxKXvkJo0lboJ7SC6-1xf7grXJ3yIdhxnoEIl6H72NI_Mu8HsmmlzcyEoMtil-tWV4OdHKmxja3VfkFv_X8Hn0Qdgzdjd-7g-2zR6aBJfpQnwvzs_fq_LPeBtoidHujIf2YNofPs5m1p8ikHxYLTGa4ztMHW2P8_ikP9HKF7VmZUfseB2_dq1a5evZDmat65Hl1lWQPUf_yWJXttckgZxberc-Q9snlNw6sIGQ-BqtYF6FvsXwtwXhrD1_q2YrlQ2vAEHE9XBmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يراد منه دثر إسم قوات
الحشد الشعبي العراقية
تدريجيا من الذاكرة العراقية
الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79449" target="_blank">📅 12:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79448" target="_blank">📅 11:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مقتل اسرائيلين اثنين بظروف غامضة في لوس أنجلوس</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79447" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79446" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=kBy0AMGwSSeigKzntbErqFEprp22CvFJ6shqlbfe2JK7KH-GwH1pQKZYXlEfhaV8Q4KzSz4jj-tC0sg7ATF2N2X6Pd9uQNtksuFZ7EXJ0RGlveXLg16WX97yxy23yN-_4WbKWfjFlkNpsZ2dKVSWZGSAAk2XuYaA8tNo9JnsxtCiDPXd1NNjac0aaasZYn45c3pzkDJkXaKhRYQR2DmCEImj-1Kgvazc9QClwjUe_eDfNPG52N4gl0OWRiSnQR8PjKQeFnIpRckGQKCG4-xFPrNdSTZS-8EFVhMh1X0dCUGA3TQ1nav1cRDnp8B2u24SFToGZEiNRt84qXL7OFzlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=kBy0AMGwSSeigKzntbErqFEprp22CvFJ6shqlbfe2JK7KH-GwH1pQKZYXlEfhaV8Q4KzSz4jj-tC0sg7ATF2N2X6Pd9uQNtksuFZ7EXJ0RGlveXLg16WX97yxy23yN-_4WbKWfjFlkNpsZ2dKVSWZGSAAk2XuYaA8tNo9JnsxtCiDPXd1NNjac0aaasZYn45c3pzkDJkXaKhRYQR2DmCEImj-1Kgvazc9QClwjUe_eDfNPG52N4gl0OWRiSnQR8PjKQeFnIpRckGQKCG4-xFPrNdSTZS-8EFVhMh1X0dCUGA3TQ1nav1cRDnp8B2u24SFToGZEiNRt84qXL7OFzlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بث مباشر لتوقف حركة السفن التجارية في مضيق هرمز بعد إعلان إيران لوقف المضيق يوم أمس.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79445" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=DJ7NCskD4T14zZNfNV1uljU6miyZQ3OrlwpVgOH8rquMPF4EyhvUyNBNM16nB_d3qG3C4XQw_RF539tmoGyD4ZJkT9STrKZFbOpo-hC55Ce4J8SJsjpewJXs-eUZKEftmcWT4jPHhJsNXyZ3-PkZV3h-uQ7HmmvrLuH-og4OQEKKsmVtrjAcy84C9nVAhp7HZpbkWLh70y24HR2h-d2zLecK0443k2J2k_NDGnwIsGP8dZFDaa7sErZpL5TQZQN4SBxCh1Uy4Wi6myrtUdmLn6DwWqhNLYy0k4GfnNviWfDNUbkZu05a12p9KYcS6kbHJMkGusS3-4wZfzPsclsRUwv7NhY8GGjFDkmG49SGnPDRoFPh1TdEVEn4Wt44et_1HnnLOy9qFwkEiHZXWqb_i79lpG_lK1eO0SfnIKZY3GNjlLBKi-t2ORf8pbCQ-UlUMFl9-_-QP11w4FJjDH6HI-OMZKR-6fD383OYQNulOGCZUbqaEYcKMd60Zhx64QMeltB5MuxbbUR2Z-vsVPaT3cxEvsUQGFLYRT0ga821pkRGCkbv2RSTSBSzBTaCf9_57jdICG5PtRmnGd9RUMfQBCODkRrVw5651X-489_D3u89jmFuipcbN33B__VVlDsa9YEOFvAyWGjhHRpBjKMGpUhyqwYUE33ZWYpiYZHlQ3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=DJ7NCskD4T14zZNfNV1uljU6miyZQ3OrlwpVgOH8rquMPF4EyhvUyNBNM16nB_d3qG3C4XQw_RF539tmoGyD4ZJkT9STrKZFbOpo-hC55Ce4J8SJsjpewJXs-eUZKEftmcWT4jPHhJsNXyZ3-PkZV3h-uQ7HmmvrLuH-og4OQEKKsmVtrjAcy84C9nVAhp7HZpbkWLh70y24HR2h-d2zLecK0443k2J2k_NDGnwIsGP8dZFDaa7sErZpL5TQZQN4SBxCh1Uy4Wi6myrtUdmLn6DwWqhNLYy0k4GfnNviWfDNUbkZu05a12p9KYcS6kbHJMkGusS3-4wZfzPsclsRUwv7NhY8GGjFDkmG49SGnPDRoFPh1TdEVEn4Wt44et_1HnnLOy9qFwkEiHZXWqb_i79lpG_lK1eO0SfnIKZY3GNjlLBKi-t2ORf8pbCQ-UlUMFl9-_-QP11w4FJjDH6HI-OMZKR-6fD383OYQNulOGCZUbqaEYcKMd60Zhx64QMeltB5MuxbbUR2Z-vsVPaT3cxEvsUQGFLYRT0ga821pkRGCkbv2RSTSBSzBTaCf9_57jdICG5PtRmnGd9RUMfQBCODkRrVw5651X-489_D3u89jmFuipcbN33B__VVlDsa9YEOFvAyWGjhHRpBjKMGpUhyqwYUE33ZWYpiYZHlQ3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79444" target="_blank">📅 10:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
مصادر:
الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79443" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🍅
الأردن: محاولة تسلل إلى المنطقة العسكرية الشمالية الحدودية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79441" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=FCVcCpice6aEF-TSQk9PDQCw1_CB--6znVchUfcMDKF8IOUfIX0QVfbnLBzx4gVY1mzALSPiNx2dj88qBvDm4KWH0O3mG27dL4atD0UdFHvwqXZel0CRaCD_J-Rd61gSYN9HvbqQaIV0N0sf5JVXbfA5HWYckaHKmehmQkMCkBhYT8M1xkarCVB9VPZDPVKlQDP92AheGapAmgRICMa93XcSpI8_-feH4bDf2wIAsaQia2JweeLgRORQcAOPB_UFLxOMnYA_KpJZ-C9QbHEJ1VUYPHAPiSWPdW_C1hJ1LH0py4N5C8x7hLkaCx0w-Alwm4UgCoCXHGGRE8yRW5TnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=FCVcCpice6aEF-TSQk9PDQCw1_CB--6znVchUfcMDKF8IOUfIX0QVfbnLBzx4gVY1mzALSPiNx2dj88qBvDm4KWH0O3mG27dL4atD0UdFHvwqXZel0CRaCD_J-Rd61gSYN9HvbqQaIV0N0sf5JVXbfA5HWYckaHKmehmQkMCkBhYT8M1xkarCVB9VPZDPVKlQDP92AheGapAmgRICMa93XcSpI8_-feH4bDf2wIAsaQia2JweeLgRORQcAOPB_UFLxOMnYA_KpJZ-C9QbHEJ1VUYPHAPiSWPdW_C1hJ1LH0py4N5C8x7hLkaCx0w-Alwm4UgCoCXHGGRE8yRW5TnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قائد الجيش الباكستاني عاصم منير ورئيس الوزراء شهباز شريف يصلون إلى سويسرا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79440" target="_blank">📅 09:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/79439" target="_blank">📅 01:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
وزير داخلية إقليم كوردستان العراق:
أربيل وبغداد اتفقتا على توفير ضمانات أمنية لحقول النفط بهدف استئناف الإنتاج والتصدير، استجابةً لمطالب الشركات بعد الهجمات التي استهدفت الحقول مؤخراً.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/79438" target="_blank">📅 00:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLQbIjj57M9NuRCoPUcOk7RnT2ZGH3ZUI9uw6y5UdQX1f4J4iaCsPyEMCzLnmiUL2Bf4k_DSYcvlu9LotIqrEDwqpddgCcGQj98QNFcrk6925odLMCgeNeFhR9GYn5veFvBjsig5IjzSBD7aaUmOr_lp0xkI1Xwkqu_wa3m4FOi2cizFLugtItD-3o3iLXP27aeR6fM6k8413Vrb060DtiBRKQO_nNfG6_lrd3NacCZK-brCHMjnjMu7AoPWJcsqsIRLTh68rDUwgtCObj25QElbX02Qd7kmx6--huDHc1xSlIfRT0Kxjl-vrLJpzpg9IzmJE9z59IUNWnY1QMvptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/79437" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9HrE8eGACe_z3mTJAExQWy_n9VfdFvlm-39G7YS3QT0aSzoS3A-zLmLw_2Irkx8Y7hp5XDRQLUcRElzSWtU7W7Kbq5275rNmOnpKgp3JLA1ijFNw6OQXd9_maAyc5Q9XeLlJCvztQwgHhHZpmv1Vy-_Pe8ROA5u9tU3cDk5PEINTrDweHXIzyE8IhbQJj3ENturgPQxCak9yHgj7IkFtA1xd2FX1eQ-seNeF3f48N-657Nzv69J0-3D8S4BDaKXhkItm8XaYz06ZmRU86oG0NW4iSNyQO3yo6KYX7qGTe4yZnVfIMiSicmh671qt_tHpMXguNgmCSJQUiIm9UqkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79436" target="_blank">📅 00:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=dqQ1z_KynzusqDhriixO5bM8Gjh4xx6udT57sR2MUerzJq74XNZV1nMYqnsi0dn84ESah8b_MMxz8vzQCA_rYUqAYgrXBPAZf0tsUz3ybcAU_h2g0iSL6JOrlut-okjUMTVBT2ooF3z0kbk8uooRJALqbzCz3viKShCArAAbdOsxU2Kpyjr5SpmdKawYNZX7ymiINMDflE_-w5tdh44v251MtaMwQwGrPRUrq3t7y-x6y8H5jp4RMV_xPOj8orKvWMTDpGLiM7uqgxjlIXr18Gmw4Xaau7XTYMZAvNq5n1duejXxkNq5RDxDHDUj0EEoBFUdT-ndrCrSc5kc2H1L-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=dqQ1z_KynzusqDhriixO5bM8Gjh4xx6udT57sR2MUerzJq74XNZV1nMYqnsi0dn84ESah8b_MMxz8vzQCA_rYUqAYgrXBPAZf0tsUz3ybcAU_h2g0iSL6JOrlut-okjUMTVBT2ooF3z0kbk8uooRJALqbzCz3viKShCArAAbdOsxU2Kpyjr5SpmdKawYNZX7ymiINMDflE_-w5tdh44v251MtaMwQwGrPRUrq3t7y-x6y8H5jp4RMV_xPOj8orKvWMTDpGLiM7uqgxjlIXr18Gmw4Xaau7XTYMZAvNq5n1duejXxkNq5RDxDHDUj0EEoBFUdT-ndrCrSc5kc2H1L-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79435" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=kX6mSro0di8O4IDfUOyrmQmqX_iat5wFztdGt2TIrGMsbj38KoMQp7-b5Rtl5tAwU32Nv7qyjH5Zfz8oW3FeIxe6RpnPSpaqJxJCPJzQoGGURZAsQLiUN84H2xOHxeb5r_Bi10s0fncJ9yCunkl8gICZ-eYgbS4EsirB6F43_1RMmot4twxtdyMmdO_fIVVb87FwPu5RymoArrAiMcDxfIA4mVmtP9mrHBVTPDamGJ8KAYTMjaLzTJqB6xV-4IhxUTCJAuPA_G15xK_5FcHEfYgfXyKmGPQ0CgAdEE0z1kGjTUWuG63BzUL85GX5te8SHI8DkMwEzKByqMXpKm5l9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=kX6mSro0di8O4IDfUOyrmQmqX_iat5wFztdGt2TIrGMsbj38KoMQp7-b5Rtl5tAwU32Nv7qyjH5Zfz8oW3FeIxe6RpnPSpaqJxJCPJzQoGGURZAsQLiUN84H2xOHxeb5r_Bi10s0fncJ9yCunkl8gICZ-eYgbS4EsirB6F43_1RMmot4twxtdyMmdO_fIVVb87FwPu5RymoArrAiMcDxfIA4mVmtP9mrHBVTPDamGJ8KAYTMjaLzTJqB6xV-4IhxUTCJAuPA_G15xK_5FcHEfYgfXyKmGPQ0CgAdEE0z1kGjTUWuG63BzUL85GX5te8SHI8DkMwEzKByqMXpKm5l9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فانس يغادر واشنطن متوجهاً إلى سويسرا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79434" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
مجلس الوزراء يقرر تعطيل الدوام الرسمي في  الوزارات والمؤسسات الحكومية كافة، يوم الخميس الموافق 25 حزيران الجاري، تزامنًا مع إحياء العاشر من محرم الحرام، ذكرى استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79433" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
تعطيل دوام الرسمي ليومي الاربعاء والخميس في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79432" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79431" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5fboRqejbAAqDMkd95mQuutQC9cSvzsWG1ztkwhhEscpPXFquPobujteDZEen3z4lXBpLWZqz3kAScmbnI8-PflOVGJuhEETROQwEZfGmJshtD8uR0-qycGO5LX_IDcbPnW40M46UDXYhW9QXklNKxhwg37BiVQtWW_nFoyA4dDxrb8n_HpIyVjYT2pR3Q0rgcF3bbcKptUieBghaAAuVIXBA6IYbUDcPZEt5xIifeWqlRVWLVOWUcEPP94OSM6Rw34BIOo_LwBSMu4kstDbLP59dEwC8IZvZXiprTVcycB0Q0iMSvG1lXXl_F7UVhSvqghF4lNX6KeX_iXxmkpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الصحافة الإيرانية من اجل لبنان اغلقنا هرمز .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79430" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOQNyBaldAzPQreX0qxYQcbAVhaPSSNy5IN2QpBOMc05iLXjC2pcPeCE0QojUYZmAQC5LBuEG5JmLRT9i7rsRRi31ZoMin35Rp0RDYS3CDeEgg4H7lhrVZbtpmOG5xPuAu2teTbftwZ9F3omTx2cRg_KfiCYKTf0GSXBTtyqzoosoBtdouTsKNzvVA_5BuGdwz7g54xel51uqJXuF4J6xXZL1b2Fatb5UbimBbLebq1ZUhl6-W3IpblkqauKIZjR_HK-ubMLHevObKAhugW9jinqRe1mmy88kg5OX8ZeXJntaxyU4xgIHDysqaOR4-8khMabDvBxS0hGWmwTEqp8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
: يجب أن تفرض الولايات المتحدة رسوم المرور على مضيق هرمز ولصالحها.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79429" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPdbFSYDo3orTmI9cTZQYqn86d1DJhBcEqjLtC1-yXCevBa1IxHh_Sd7vJsaIqpBwRy-3DVUiOvLFsUjjIHvyuDR9lJbpPuQJpAeTGrSSKriJi5D6JnvpatS0bJscdU14WubTVXnxfmVP_l0-yFNbpPX0LkNedbzpMQThI-5X_nxXeR3uVYbxgN1IKRdu-cJnaee5Mq4U0c-nuFJpbac2Z0SijeSW3MjqqNsLxzyPNkHAZy2IZ_s1wd7lg83J0KKkNkzZN8QkovlC2xmbfMKZVnGejlrr6U26nAqROGrjDQJgU9ZRAO8mTGx-v14yrEV_WkU9bAOpkSgX_f2zw_pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFqioVgf3Ub0T1SW-EsXhJTzpjrjS5yGDCqf6Kzhm3-2vqayC5JEV0gI2_1lAwXZFbF6szKtAeOFdrGbXOJ4W8D7fBCKREw8vvqUpVNF32-BZRQon7-agmFX2WCf0CLXvaxDjwvf8nNk4zTlZBWdcIUkRMnHiQwsHgmYGc7-NZxGj6wXeZcLFSs2LWBUv-_rHrHPAjVAzdK_Pvr92pIU-uSQxT93MlCFKqCLk4SJLRpF5JQltx887yBWgiBZux-k-CFCD3mOf3hJFOELX1TyV4efk-uYA4JzN6aIq4iZ_VvBp_Ibkt3fDsI0_mmwn9Rj-TXgM3VihNBa5yjKle9klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhINZ6z_Wa3hEJomuiKx9SMClBH881A8xJf3A8aYxhZSZ-zqSvmOqMKZtO3DCAvRWxYo6D_sxCv6U0XGSXEWn8ihokm5oBtl7c54XnDFP-dy1uV-JKO5mUX1UzIYLh4Qy9CrD8VSD_zBePcJ5iqN65Kl6NGCdfKtUaIaUBgtRm0uMaZC04B0Pbx1ZbfZVvbpvF_QtgtnG9MwtMo4pfs3Btyuq7Wbb2D6AjnIeQ07h962La817x2dYgDO0mWAjcz6EgpI1HzurtkXSTCo8SxuBssloO7EFU5iDZk9kGdePjjCbIXivVco49FDwdsXwyl91A0w-Py-9mbzg4RZRw007A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79426" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79425" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79424" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
حزب الله:
لَن نَخشاكُم ولَن ننكَسِر... قطعًا إنّا غدًا ننتصِر.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79423" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79422" target="_blank">📅 21:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79421" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA1wWK7Qjii5dyRtogmJUzxAlcHOOeF-gNT_5OlpB4pckHQ_Zh7guSjZkyobjOKkQF2ak6mUe3SByHTbrvgGojJ8zjdXG9S1S4Z7u-uWW7uMRTydutFDaVrjmhrJaHhB11BhavasGvFdPd5_1p8b4-EpspKiI9DitdCTj9xcmalVwCYRc8Lebi82wLkT1OhGKuRt4frATxow-Bp4peeSIsg2zQLxQOAxOzyQaKA9YUwT0L4t4XRINViBrZ_VPZfqOF3F2bpW04p9k5n23wXiQflgd4x_MS0o-R-gB5YDbHmFoOvw_ReWUqZZFhmIqN1adsWuVXj1CVoeN64GFru5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله..
جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79420" target="_blank">📅 21:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كربلاء المقدسة تعلن تعطيل الدوام الرسمي يوم الخميس المقبل الموافق التاسع من محرم الحرام.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79419" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
جرافة (D9) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة
#أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79418" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭐️
بلومبرغ:
‏قال الرئيس دونالد ترامب إن احتمال انهيار الاقتصاد العالمي كان سبباً رئيسياً لتوقيعه اتفاق سلام مؤقت مع إيران. ويكشف هذا الاعتراف عن نقطة ضعف رئيسية للولايات المتحدة قبيل الجولة المقبلة من المحادثات مع طهران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79417" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هيهات منا الذلة..
أبناء البحرين يخرجون بمسيرات حسينية تحدياً لعصابات آل خليفة المتصهينة ويرفعون فيها الشعارات الكربلائية بذكرى أيام إستشهاد الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79416" target="_blank">📅 20:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGIj2spfYLqeqxtAM22GnNJ0Yqyn47DfWOXm-zcBoPw_I2R4elUTbyN9_XUbski4eeVarEmEg-Uw_Ci4Le0UTCFCe3s8S3-iZxjJvIL77XmScOCXV19qhjKOR6cokZtGDH7O3X25aetcC3726L8WrphlcJ1r4rRX_HrxhQdD3gzOkWHQGohZjTyFpAnaIzMc228eghyQUcKgOlotN5yMhE3oxRf2w9KZffFnRP_w1fNOsmpJ2Cpk_KA8PsIGDf-_0rEVibgjpDZMKwMZG9MfyFjxsv-Vm9XVxT12LbPIBjTjTvc055WogahKhtSoKTSWn9stHCVP3-lDSTNxvYqASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الجيش الأمريكي: تبقى القوات الأمريكية حاضرة ويقظة لضمان الالتزام التام بجميع بنود الاتفاق مع إيران، وتطبيقها بكامل قوتها ونفاذها.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79414" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzF__c7EoyV7PPD2c3YPhhjLPxupMtRhjrjRgDU19TWskRJIrlvn1crnWa9c7pjAhGB0xgDld6IszAZgEzfYW81PU2aMxhAdu4DQwfW3HfRNgHC8n9MwmEA5CQiO7x7KF5GN_BB92FsbUF6p2mUzz4JMofE30FejZcRZMZqQRq08McJIsGx2fbIj5cEIX72NXY7EOE9CWrl9qUBBV5Hb1UxEWC4AicwISZzz5FwpJvvYnm1xjExyRae_E1qpnUKJs2F9xnggsemzTdDBg515Sx3HkzaZkX7hQH0HmbuAUvnt6tqUAFdnM-oMPjDT7CgClAwl_uv-bJWtwYrNSG1INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79413" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTSsh-QDj6v2TeJtzqk3dyzv4IAMGXsGK0uNNFpqS9OJcd5caBQ85eHXi5uIFxyZdaHMcXQcgqfcA3GUUixdBP6ZfH75pP1cTDrj4qxjJ32R9qhuLpQqsYGwLsZvTsexolgcjcNQjxrZs3yFwi3Lolbgy5F8rP8hdsEoH4EGxe6yTa4ma_My_f-NDX_TJ3636Y3zvqCJpqoCupjCCrUaYeh_nWJi_DqC5l9OR1-0rkCkZ90iJMbcuAbqyrUUkDPLitWRieC3lRJy6duYIv62q2zIZBQ5do6jEPR-Ug06lhM3kXheHNBVM7TnCMKXaAQMsR8LenscHYfm1HApvQ6Arg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:  مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!  ‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79412" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هزة ارضية في مصر بقوة ٥.١ على مقياس ريختر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79411" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQYy4yQix93FdMKL_g3D7xDYdu9YTuWkAY9nDhmKa9t4MUCq3Saz6iogNSt0GaZpbAACVbgz94_WDLJ0jcCqhuW-CNg15M8LJNZY-n79whROBYWD1KkAx0k42uBYfxAYB8oFFdCt46ka6VTlzqUOUaRSo9Y4dWGyAZwzZm7VbCekCWXqgpb4GuAV8FFo3W8ydkJEywcMy5PCQvHmo5o8HvnANUO3wLfYrzamBSFD-1H_FYTSCaIbya_TO-vBrNDYiwLD0FUrwK5Qc9leDbmTNmd1zGHEj3xvqJE6eYz0W1xnIKIKUEULPpXkhg7KqBjhiW78J75kAw_201RqyvZTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
لاول مرة
تنشر منصة كاف التابعة لكتائب حزب الله في العراق صورة تظهر نوع من المسيرات تشبه لحد كبير لمسيرة صماد ٣ اليمنية بجانب العلم العراقي ؛ لم تكشف الكتائب عن طبيعة المسيرة او مواصفاتها التي ظهرت بجانب مقاتل يرتدي ملابس عسكرية تشبه لحد كبير ملابس متطوعي سرايا الدفاع الشعبي التي تعتبر اقدم مجموعة عراقية مسلحة ظهرت إبان مواجهة عصابات داعش في العراق .</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79410" target="_blank">📅 19:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">أنباء اولية عن مهاجمة قصر الحلبوسي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79409" target="_blank">📅 18:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79408" target="_blank">📅 18:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79407" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2w7FPVAMr7hWUyBCrCEeYK8ijXcEYN20ackvoTRBuBfOknKDUSyP61fxbSey_WMIC12JmIlFUprH4Tv-0zOl-YBWGvdyJvlhPIGZmRYANMZNa-It2GaeITu3jepXI8SQ56NuOUNU8jV6kDfGSxhkWR0lZjK7_xROVAMgiIoPp9ZrZ3-W22nPUo-GljURmzjOwGYm2zkTWeW2Jeaxfdv33WkT6n-TziDLuD0MVhqEDTIWpmjijG3_36R-hBbyGqR6KXBJssGaLT0LHn36ErEXJ2vb87oNrNkVlf3E-Q8zQzGQNB3ZoWkQVq2apuWi5DQ4St5nqdbTyof6GjrpzPGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل   زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/naya_foriraq/79406" target="_blank">📅 18:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.  يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79405" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79404" target="_blank">📅 18:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
بيان صادر عن العلاقات الإعلامية في حزب الله:
في ظلّ الادعاءات والأكاذيب التي يواصل العدو الإسرائيلي ترويجها بشأن مزاعم خرق حزب الله لاتفاق وقف إطلاق النار، في محاولة لتبرير اعتداءاته المتواصلة على لبنان والمجازر التي يرتكبها بحق المدنيين، تؤكد العلاقات الإعلامية في حزب الله أن هذه المزاعم عارية تمامًا عن الصحة، وتندرج في إطار محاولات العدو المستمرة لتضليل الرأي العام، وفي سياق محاولته الواضحة والمفضوحة لتخريب الاتفاق بين الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية.
فقد تجاوزت حصيلة انتهاكات وخروقات العدو الإسرائيلي منذ فجر يوم الجمعة 300 خرقٍ واعتداءٍ موثّقٍ، تنوعت بين  الغارات الجوية من الطائرات الحربية والمسيرات، والقصف المدفعي من مختلف العيارات، وإطلاق القذائف الفوسفورية، على أكثر من 25 بلدة وقرية، من بينها مدينة النبطية، وقد أدت هذه الاعتداءات إلى سقوط أكثر من 111 شهيدًا و176 جريحًا. فيما تشير المعلومات الأولية إلى استخدام العدو للقنابل العنقودية المحرمة دوليًا.
وقد بلغت حصيلة الانتهاكات والاعتداءات منذ صباح هذا اليوم إلى الآن ما لا يقل عن 180 اعتداءً، وأسفرت عن سقوط أكثر من 28 شهيدًا بينهم ثلاثة شهداء من الجيش اللبناني و35 جريحًا.
ومن الثابت أن هذا العدو الكاذب والغادر لم يلتزم يومًا بمندرجات اتفاقات وقف إطلاق النار، لا في 27-11-2024 و 08-04-2026، ولا بعد إعلان التوصل إلى مذكرة التفاهم بين إيران وأميركا بتاريخ 14-06-2026، ولا حتى يوم أمس الجمعة 19-06-2026، بل واصل انتهاكاته وخروقاته للسيادة اللبنانية عبر الاعتداءات الجوية والقصف وتدمير البيوت وترويع المواطنين وقتل المدنيين.
إن هذه الوقائع الجلية أمام العيان تُبيّن بصورة لا لبس فيها الجهة التي تنتهك اتفاق وقف إطلاق النار وتقوّض التفاهمات القائمة، بل إنا ما يرتكبه العدو الإسرائيلي من اعتداءات ومجازر لم يعد مجرّد خرقٍ لاتفاق وقف إطلاق النار، بل يشكّل عدوانًا موصوفًا واستكمالًا للحرب بكل ما للكلمة من معنى. وعليه، فإن المسؤولية الكاملة تقع على عاتق الاحتلال الإسرائيلي الذي يصرّح مسؤولوه علنًا وبصورة متكررة رفضهم للاتفاقات القائمة ورفضهم الانسحاب من الأراضي اللبنانية المحتلة، وعلى جميع الدول والمسؤولين وفي مقدمتهم الولايات المتحدة الأمريكية ممارسة الضغط على الكيان المحتل لإلزامه بتنفيذ الاتفاقات ووقف الإعتداءات، بدل رمي الاتهامات يمينًا وشمالًا.
ويؤكد حزب الله أن من حقّ لبنان وشعبه ومقاومته الدفاع عن أرضهم وسيادتهم في مواجهة الاعتداءات والخروقات الإسرائيلية المستمرة، ولا يحق لأي أحد أن يسلبه هذا الحق الذي تكفله كل الشرائع والقوانين الدولية، وأن ما يسعى العدو لتثبيته من حرية الحركة للاستمرار باعتداءاته أمر مرفوض ولن يمر دون ردّ، وأن طرد الاحتلال من أرضنا هي مسألة وقت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79403" target="_blank">📅 18:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز..
إعلام العدو:
نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79402" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.
يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية في أمانة مجلس الأمن القومي الأعلى، وعبد الناصر همتي، محافظ البنك المركزي، وحميد بورده، نائب وزير النفط ورئيس مجلس إدارة شركة النفط الوطنية الإيرانية، وكاظم غريب آبادي وإسماعيل بقائي، نائبي وزير الخارجية، و... أعضاء الوفد الإيراني.
ووفقًا لتصريح بقائي، المتحدث باسم الوفد الإيراني المشارك في مفاوضات "ميناب 168"، فإن هذه الزيارة تهدف إلى متابعة تنفيذ التزامات الطرف الآخر، حيث يتم اختبار كل اتفاق وتفاهم عند حلول وقت تنفيذه.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79401" target="_blank">📅 18:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:   نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79400" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=g8ojpeLfBmfQnYtZrgCP7Jh3ZjSIytoznYt92vMvPPL1wa1g8h0ZYi48Oa4xz5Pw2lGVFUuoqHM1DDwqCAchy_0q9mDoCERJdz8VTuc5kEqeOjfNKrgy3abTsGjaTbXNa9rad0Dq0SjuFFHqwJCRdh4mGeOcXX4ez5QG8t_sbnyb0HhEP-kOZiLbhSBoIKbR0St8gX5c5CX_U7ZS32E4ragEn6JoN_Zn573ZU8yxiOvC38RcgthJgR8E-d3GFbjwTFLsK-ixYSU8zkcKEFCxmtrC_ZCo8hb3SkYjLWILfbmY8Rl-VsfKqp-PxQR14g32K_bzKrwzzqo6_W3J1318bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=g8ojpeLfBmfQnYtZrgCP7Jh3ZjSIytoznYt92vMvPPL1wa1g8h0ZYi48Oa4xz5Pw2lGVFUuoqHM1DDwqCAchy_0q9mDoCERJdz8VTuc5kEqeOjfNKrgy3abTsGjaTbXNa9rad0Dq0SjuFFHqwJCRdh4mGeOcXX4ez5QG8t_sbnyb0HhEP-kOZiLbhSBoIKbR0St8gX5c5CX_U7ZS32E4ragEn6JoN_Zn573ZU8yxiOvC38RcgthJgR8E-d3GFbjwTFLsK-ixYSU8zkcKEFCxmtrC_ZCo8hb3SkYjLWILfbmY8Rl-VsfKqp-PxQR14g32K_bzKrwzzqo6_W3J1318bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79399" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
