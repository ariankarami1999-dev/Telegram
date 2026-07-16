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
<img src="https://cdn4.telesco.pe/file/RtosBiRHBQXfuJf3ZjeeT2EgpGzcI_WNTkhjpilfTh0tyFVSZW1NUN1PssDY5DP811ESE2TC41e6UFAetSAPxknH7PkwmA7ZtEC4ri7XNO-8lO9vRVQ8mZPPWu-PWFhiMvXmkIe-RrGbZ0ZDDmbGrCLqdUdQS85w2HHje9HwWo8VnbEHLl2VsI3k5UjV8Onon-7APObhieV7kkZ2tQG-DWUUdbcDTfIO3GLO5PdyHAJk3nnxssuFuZPPlCbsDIfu3Ibg9c2G2JVpzgsRXCTstJ5DkhjaircDuIGty7nB_STLk_8oPW2GOGW-_sztB4V6MpItGe39Si3FVLYAN-5UeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات في مدينة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/naya_foriraq/83455" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الجيش الأمريكي:
‏
قام جنود مشاة البحرية الأمريكية من الوحدة الاستكشافية البحرية الحادية عشرة بعملية تفتيش وتحقق على متن ناقلة النفط "إم/تي وين ياو" في خليج عمان، في 16 يوليو.
‏حتى اليوم، قامت القوات الأمريكية بتغيير مسار 3 سفن تجارية حاولت اختراق الحصار، وتعطيل سفينة واحدة لم تمتثل، والصعود على متن سفينة واحدة لضمان الامتثال الكامل للحصار البحري الأمريكي المستمر ضد إيران.
‏يظل مضيق هرمز والمياه المحيطة به مفتوحة وحرة، باستثناء السفن التي تحاول انتهاك الحصار الأمريكي الذي يفرضه جدار فولاذي.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/naya_foriraq/83454" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMXZWFk1G1Um6QX1fB6Bp07-WxAi70qAZ7ljgXlim6cVLhRhqMKkDAwikumjSx_OvwGipasetbj8ld3MFTm52WHdeSL2FkpFGKmotPklAiQZ6TctMGgaVEHgZ91zcHPRHmcHPHG3p77ntAVJD631VkGWHZKOP8kZNhHVhdkcDjR2StCFwfPMjUKjnhw-_RLVpiMplF-Biy7YlYDPIeVr-x_98r7Dsu1RSTWLdxvVxSA7P4ZemgNY1fwXtXkTk4Y-IQ3DxxskO3q_IGa_AGzdmRusD9opDb4crr6PM-OcZc7Og-wIpqeBp_KdadsAQ3MQUhpuVL7N-lesjtVaIyUZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقطاع الطريل الواصل بين مدينتي بندرعباس ولار جراء عدوان استهدف أحد الجسور الرئيسية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83453" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
عدوان أمريكي غاشم على محيط مدينة بستان في محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83452" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات في مدينة الحميدية بمحافظة خوزستان الإيرانية جراء صواريخ أطلقت من الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83451" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83450">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">إستشهاد 2 وإصابة 4 مدنيين جراء العدوان على أحد الجسور في بندرعباس كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83450" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83449">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5MlzApgqNp0OSrzjKcZhqpiOe329jlFo9171mK61leRYqi8ewC6mRm00LjcJEeGAnitWx14XXJUDyO_ul9zcR-nZUVwp-AdExlaccMMODqUHRCBTKSH2IQ5L5FN3B-b1tJbb4IVLZKPGAjlEx0_vMndpOUvnuMSpEqyxgjVTOLVE_P32hiUO_1rm70DgwySomS8rMlAJuuQBeKaJHOmeyyNT58R0CMot5mWRZcMT6iNC6PbGSFr_pRYVk8z-HssxvgPU_ljPkNyk84cS9WvXdFPa2zf2drLLDQsaMAlB7pdeA2eG6fmhd8xhQFispAGhPiuSxq4o1p-M1eDMrXcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مقاتلة أمريكية من طراز F35 تطلق إنذار الطوارئ في سماء الإمارات.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83449" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عدوان أمريكي غاشم على ميناء سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/83448" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83447">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استشهاد مواطن وإصابة 8 أخرين في مرتفعات "الله أكبر" بمحافظة هرمزغان جنوبي إيران</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83447" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83446">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة قشم الإيرانية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83446" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83445" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83444">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انقطاع الطريل الواصل بين مدينتي بندرعباس ولار جراء عدوان استهدف أحد الجسور الرئيسية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/83444" target="_blank">📅 00:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83443">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
مصدر إيراني: لا صحة للأنباء التي تحدثت عن انفجار أو هجوم أمريكي على مدينة زاهدان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83443" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83442">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=nvvZt218fx1Pda5vYDq7QPdY4G7fmzOltbJmhUd0ujAcCUrCn33sDthd7rFcxtE_6p2f56Sj_8jdp2N89OYmoNR2BN6VAGfLy1kl3w1-CIHzoqJ8RkJv3LHJ4Eml-5aYJd_Zy3Tw4H0xDJ4xZVYj1dw_xPT9WsHryHFcUM6ba9pS4B-5EQSvT2L_ZbmyP8yYPV7cGPAhf3UkXDpewU_DiWdgQx-z549IVDEjDTPT9QQd5qhwETpBhrz9cakGRpyYe1bUJBHXDI_PwmGndoC9W1vIIkKLySEPfBu4UTadZj0ZwPT7Bbr1ZnFJYa8jeU96Z-zrt3dCw5TILqHyJ67Z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=nvvZt218fx1Pda5vYDq7QPdY4G7fmzOltbJmhUd0ujAcCUrCn33sDthd7rFcxtE_6p2f56Sj_8jdp2N89OYmoNR2BN6VAGfLy1kl3w1-CIHzoqJ8RkJv3LHJ4Eml-5aYJd_Zy3Tw4H0xDJ4xZVYj1dw_xPT9WsHryHFcUM6ba9pS4B-5EQSvT2L_ZbmyP8yYPV7cGPAhf3UkXDpewU_DiWdgQx-z549IVDEjDTPT9QQd5qhwETpBhrz9cakGRpyYe1bUJBHXDI_PwmGndoC9W1vIIkKLySEPfBu4UTadZj0ZwPT7Bbr1ZnFJYa8jeU96Z-zrt3dCw5TILqHyJ67Z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان غاشم يطال أحد الجسور في منطقة كهورستان بمدينة بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83442" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83441">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/83441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83441" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">المقاومة الإسلامية في العراق: بسم الله الرحمن الرحيم  (وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ لَعَلَّكُمْ تَتَّقُونَ)  إن أبلغ شواهد السقوط الأخلاقي للإدارة الأمريكية هو تبجح المجرم ترامب بغدره وعدوانيته في استهداف قادة النصر، الشهيدين القائدين…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83440" target="_blank">📅 23:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eudkl4jX_io6-HP2CucgLx-NmMaEtwGqZcJ-r4BNCza4HlBjkKiuRHdSr53yKhl1RL32JFwvhWus7P6yR8lLPfKRRzD7yPlfU0XAOpo6Y5IBRgNCcrDMjMWyQMUBC16J8-qGZQ3Ce99la2yqFaio-xjrtqsJhLs1KygTZAj8rmiw8kqrGILhBxixHlB6gBZDUpH6GVjyqClgQXQrar_qFOEaLCFlBI5mmeznFpgruR6JclrqTa0ylYWj-a4uEyrI5yLcpqj9q-W3iFEGdhx5z0fysOdr7BXlcm9AXVJrjQeOtkKn_oa_rh_BtrahXhptMDh09Tai9FkxuhcjpH7KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المقاومة الإسلامية في العراق:
بسم الله الرحمن الرحيم
(وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ لَعَلَّكُمْ تَتَّقُونَ)
إن أبلغ شواهد السقوط الأخلاقي للإدارة الأمريكية هو تبجح المجرم ترامب بغدره وعدوانيته في استهداف قادة النصر، الشهيدين القائدين الحاج قاسم سليماني والحاج أبي مهدي المهندس (رضوان الله عليهما) هذا التبجح الوقح لم يزد دماءهما الزاكية إلا رفعة وخلودا، ولم يورث قاتلهما إلا خزيا أبديا وعارا يلاحقه وإدارته ما دامت الحياة.
إن المقاومة الإسلامية في العراق تعلن عن رصد مكافأة مالية قدرها (10) مليون دولار جُمعت من تبرعات أبنائها الأوفياء وأنصارها الأباة، مخصصة لمن يقتل المجرم ترامب، أو لمن يقضي بتخصيصها أو توجيهها لفرد، أو مجموعة، أو كيان، أو مؤسسة.
وسيبقى أحرار العالم يلاحقون قاتل الأطفال والعلماء، فلن يذوق الطغاة طعم السكينة، ولن يجد المجرم مأمناً يتقي به غضبة الشرفاء؛ فالقصاص عهد مبرم في أعناق المجاهدين، ودماء الشهداء ستبقى لعنة تزلزل عروش المستكبرين، حتى يندحر المعتدين، وتتهاوى حصون الطغيان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83439" target="_blank">📅 23:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c55ba97a9.mp4?token=op3XuB4imsYUNNrr4hw22QaANCweCip2eHdLXeFE_TH_5txviJk1KI5ubEI-KXxSyHedYhIXu_jgRzNIoLx5wN7Tjuoq8PXn_yR3r0IKrgb_hiSvAvKIWEezNOLf5g7ukOI9bQs4AOnAymrsCbhj1H3zbDcherTsLqgpbdaDUu2_gKw1dx4-Wv9LsxrVgR1Kbo_hnfxeGpBxGwZoSKPsosKp6A9Jhu7SufujZh0yOfQ76a4yKRLAs8uT08ve5NrhsUDalTob9mkh8S23Vi6KoOldxjtHSL6rPeRjHIERhVn79ehwER8yRS2Q-Twfps5_R8eUJRMsPw6dF5-fpyzWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c55ba97a9.mp4?token=op3XuB4imsYUNNrr4hw22QaANCweCip2eHdLXeFE_TH_5txviJk1KI5ubEI-KXxSyHedYhIXu_jgRzNIoLx5wN7Tjuoq8PXn_yR3r0IKrgb_hiSvAvKIWEezNOLf5g7ukOI9bQs4AOnAymrsCbhj1H3zbDcherTsLqgpbdaDUu2_gKw1dx4-Wv9LsxrVgR1Kbo_hnfxeGpBxGwZoSKPsosKp6A9Jhu7SufujZh0yOfQ76a4yKRLAs8uT08ve5NrhsUDalTob9mkh8S23Vi6KoOldxjtHSL6rPeRjHIERhVn79ehwER8yRS2Q-Twfps5_R8eUJRMsPw6dF5-fpyzWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/83438" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات في مدينة الحميدية بمحافظة خوزستان الإيرانية جراء صواريخ أطلقت من الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/83437" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارات في مدينة ايرانشهر جنوب شرق إيران</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/83436" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83435" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1101d37db3.mp4?token=YJA4QthceMS4-t9-5NuUJn2zZrq0H_M4xtT2dDbgPSSIWZoIJd5pJf93VFAXiScX_04M1oBY6dC6BiptpSfl8J1pTutpgWbtI0nD-yXwNJCIgXTvbqT855fP3_FUU0G0eVFrwx5lQzdQ4IsqrW2FxZmTX-v9yAITeKwN-jR8yrBPG-P9mF_jo9SEegrnzxWlGmGwQ3H8SDFwUh9fKYAAOGPcDAId5kCVWEZtVNFmjDkTTCIQt9CtznSzrKPfaRJCIsYa3V8MXAn8RSnCTRtLmxy0-MXTtHakfQkukPOXnFlCYL5sRY4m3_IiIb6fmKI-0m4Y_AQaI-tSq8765pQGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1101d37db3.mp4?token=YJA4QthceMS4-t9-5NuUJn2zZrq0H_M4xtT2dDbgPSSIWZoIJd5pJf93VFAXiScX_04M1oBY6dC6BiptpSfl8J1pTutpgWbtI0nD-yXwNJCIgXTvbqT855fP3_FUU0G0eVFrwx5lQzdQ4IsqrW2FxZmTX-v9yAITeKwN-jR8yrBPG-P9mF_jo9SEegrnzxWlGmGwQ3H8SDFwUh9fKYAAOGPcDAId5kCVWEZtVNFmjDkTTCIQt9CtznSzrKPfaRJCIsYa3V8MXAn8RSnCTRtLmxy0-MXTtHakfQkukPOXnFlCYL5sRY4m3_IiIb6fmKI-0m4Y_AQaI-tSq8765pQGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83434" target="_blank">📅 23:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bca01c43c.mp4?token=fS2j7SKUvAb9OzWYrPYY18HsAH76uONxrMGy4YqdJYYL0oaKae7nljf2jKg_EhNP9PDT8E-gS6fScpeCONXyVNk8QF4Lxx0L1FlGfyHO06u8IiKphjWoZn4365WVMc6K0OInEJNDyfOMKLKqtxAMAYSGaOa3yhcfHBBwTM7sgIl7WsE2dRWBJzD0zxgEBinWXuqWgecnUNUBCAfaej0DuU02STKG5JGfzgOhGNuI59vAVeUQDI7OxEAHS0YNDikmuGxndAzwWTBfNlW3BxRzm3qom9t8Rn-qYIOC1j7FhWqO8uwZCkpZXJx2rRBzIsHkzZa-wtpqJKLUKBf417lTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bca01c43c.mp4?token=fS2j7SKUvAb9OzWYrPYY18HsAH76uONxrMGy4YqdJYYL0oaKae7nljf2jKg_EhNP9PDT8E-gS6fScpeCONXyVNk8QF4Lxx0L1FlGfyHO06u8IiKphjWoZn4365WVMc6K0OInEJNDyfOMKLKqtxAMAYSGaOa3yhcfHBBwTM7sgIl7WsE2dRWBJzD0zxgEBinWXuqWgecnUNUBCAfaej0DuU02STKG5JGfzgOhGNuI59vAVeUQDI7OxEAHS0YNDikmuGxndAzwWTBfNlW3BxRzm3qom9t8Rn-qYIOC1j7FhWqO8uwZCkpZXJx2rRBzIsHkzZa-wtpqJKLUKBf417lTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة ايرانشهر جنوب شرق إيران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83433" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c016d251a.mp4?token=ZTRK1MjSDs2p5niYxJrhuGpePSO3kWPi0lg49IWZFUoee4mfK8vADToOR0TmjB8zkcMts9ZRDMp6rYgrL-iI5Kw4BUkY_DP43tlacPnT97HX1PwWa0S9DJNiq9bDzvqiWAViqIhMJ0powFYsxNTOx6A8IXmB9EhOlu3bLEwpnbXMj8GQ3SgxIWNFiAOl_jNnvzo7O0pFPfHj9HjydM8qR9WuBfHQFCjGpJYzbgrNAEBM9OkCMw7WqX8gIs_Mx8NdOCogLoCG6RAjwNLK8_lOP2dS4V6IE5jxangTF5nCk_S6H8BBk00jW34TB8wV2gmhw_Jl5GXsRYQgWHgz2QB2Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c016d251a.mp4?token=ZTRK1MjSDs2p5niYxJrhuGpePSO3kWPi0lg49IWZFUoee4mfK8vADToOR0TmjB8zkcMts9ZRDMp6rYgrL-iI5Kw4BUkY_DP43tlacPnT97HX1PwWa0S9DJNiq9bDzvqiWAViqIhMJ0powFYsxNTOx6A8IXmB9EhOlu3bLEwpnbXMj8GQ3SgxIWNFiAOl_jNnvzo7O0pFPfHj9HjydM8qR9WuBfHQFCjGpJYzbgrNAEBM9OkCMw7WqX8gIs_Mx8NdOCogLoCG6RAjwNLK8_lOP2dS4V6IE5jxangTF5nCk_S6H8BBk00jW34TB8wV2gmhw_Jl5GXsRYQgWHgz2QB2Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الكويت باطلاق الصواريخ نحو الاراضي الايرانية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83432" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab26e08a3.mp4?token=Wy14QgjbKX3sVzEeRqtQVWnhZrbkridHTPH5iiwFVNmJhd9lUV758YY0r1Wfa96QuSVJhIJNUjFxJYTC1AhTxCvBxY1B9jeAHvIM-5LwMz1S5jQiNge1ko2wjvTQsjjGcbKAqSgrbfYv917PPgfMSSnx5m2j8Dj4pp7nT0M6j3bdHGxKuYDAXxCvjRynzRfysE9kIPuyADiQAZBCP10usFb7eC4C1PpjGz1ILimx3HjMKWYYkwlQe2INxm8wyBWlRHIzoYy91g_GnsvuIUiEcoJ7WtDipz6TjljamFhGO1QkUctdyInLQrIhswSiJ0a4QK5X7x84MJxMCWynHYadFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab26e08a3.mp4?token=Wy14QgjbKX3sVzEeRqtQVWnhZrbkridHTPH5iiwFVNmJhd9lUV758YY0r1Wfa96QuSVJhIJNUjFxJYTC1AhTxCvBxY1B9jeAHvIM-5LwMz1S5jQiNge1ko2wjvTQsjjGcbKAqSgrbfYv917PPgfMSSnx5m2j8Dj4pp7nT0M6j3bdHGxKuYDAXxCvjRynzRfysE9kIPuyADiQAZBCP10usFb7eC4C1PpjGz1ILimx3HjMKWYYkwlQe2INxm8wyBWlRHIzoYy91g_GnsvuIUiEcoJ7WtDipz6TjljamFhGO1QkUctdyInLQrIhswSiJ0a4QK5X7x84MJxMCWynHYadFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار إطلاق الصواريخ من الأراضي الكويتية باتجاه الجانب الإيراني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/83431" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83429">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd969d3aa.mp4?token=JSdKLk6X4-Sfwr54ppXX4qpnmva9Qfm-PmadWmrdQItsp3FWAQ6tghlGE1Oe_wkhTp4V7MKCgXdnZDOoOHuIilBmQgnTEsnonsQRhQSKwOfBhr9anlMFxpFfcdZPuOn2RU8NQ6ZVZ7VV4OJYtpozMSKsiqCkLgbY95zY8ZgI1cMVD1m4cGw2ryXECqeH8Rujo4RDHaBXOVz4BZyL8FBmfetVIezcrRU3cpTV-T_AIzykopxpHp8ao3SNJHJe4nkYqwza3E7KfEFxDIzX0gC4kzRz8uMrszq8IE_TFAqjRfKViX4QNRf7wIJqIjoIYwEoUULbMaUFr7a5b5SR3suP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd969d3aa.mp4?token=JSdKLk6X4-Sfwr54ppXX4qpnmva9Qfm-PmadWmrdQItsp3FWAQ6tghlGE1Oe_wkhTp4V7MKCgXdnZDOoOHuIilBmQgnTEsnonsQRhQSKwOfBhr9anlMFxpFfcdZPuOn2RU8NQ6ZVZ7VV4OJYtpozMSKsiqCkLgbY95zY8ZgI1cMVD1m4cGw2ryXECqeH8Rujo4RDHaBXOVz4BZyL8FBmfetVIezcrRU3cpTV-T_AIzykopxpHp8ao3SNJHJe4nkYqwza3E7KfEFxDIzX0gC4kzRz8uMrszq8IE_TFAqjRfKViX4QNRf7wIJqIjoIYwEoUULbMaUFr7a5b5SR3suP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من البصرة تُظهر إطلاق صواريخ بشكل متواصل من الجانب الكويتي باتجاه إيران.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83429" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83428">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=cxQ5E4yFcJzkjNDdEJlbMYxnxK3EQppZXr7chvOE36RVj6xWTqjS1bxJ6KGIXO9h9RMNWFBbzF4EssRb2e3rkzjSHEluQcl4ZA8JZOyWWTGV6k4pZOGJ4oULT9ztuZCINZnY1TeoBKRbHWQi3rI9OZ3TRKAMpjdD9QRDcedUOx8F_tUJbqG3-SsifUoX9Zn-2nNlQL-e-612fWVpyHpXA72VmC70NYp3za2nalQKZcEHFDtOpVKWkGmDNnuG1JoI33SIC2JzqxVzH1N_mE73lW6bfasjCZYTjkm7pU24YXmKL9S06TRcz8OcYkJ8ek5qbDBPQ0cc5jcGnP93vbGQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=cxQ5E4yFcJzkjNDdEJlbMYxnxK3EQppZXr7chvOE36RVj6xWTqjS1bxJ6KGIXO9h9RMNWFBbzF4EssRb2e3rkzjSHEluQcl4ZA8JZOyWWTGV6k4pZOGJ4oULT9ztuZCINZnY1TeoBKRbHWQi3rI9OZ3TRKAMpjdD9QRDcedUOx8F_tUJbqG3-SsifUoX9Zn-2nNlQL-e-612fWVpyHpXA72VmC70NYp3za2nalQKZcEHFDtOpVKWkGmDNnuG1JoI33SIC2JzqxVzH1N_mE73lW6bfasjCZYTjkm7pU24YXmKL9S06TRcz8OcYkJ8ek5qbDBPQ0cc5jcGnP93vbGQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من البصرة تُظهر إطلاق صواريخ بشكل متواصل من الجانب الكويتي باتجاه إيران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83428" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83427">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da81453cfd.mp4?token=j9emDUL5WVrjjjgey14ALIRKwqzQTLXQfRcApPZ43tnzo0n2ypYAJRQAfCwL77s_B2SEARYEGA8ObGA6bqpOUKxbhLiKAzD99CJqKEHDnECZ4Xtptlxf9GxA4mRX_ntR5CxnQ6vXVWLnAtyhW28KDNDP9n_mkNr7P46Hu_1XxYw2KspWPQeFuG7240MPzKbZosvqH5vTucyPCSIBwCiUR2mvAqJUpKMQKU3008b0iswPy1sd89_70UYPvvIRCOPc179wiZMchSkBOvdk51GnZ971bTQNao-OO4gR5PC1U4xvHExMhfa9-Y9gSOqoqoM4epQSmFjkToP81cDXTtOQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da81453cfd.mp4?token=j9emDUL5WVrjjjgey14ALIRKwqzQTLXQfRcApPZ43tnzo0n2ypYAJRQAfCwL77s_B2SEARYEGA8ObGA6bqpOUKxbhLiKAzD99CJqKEHDnECZ4Xtptlxf9GxA4mRX_ntR5CxnQ6vXVWLnAtyhW28KDNDP9n_mkNr7P46Hu_1XxYw2KspWPQeFuG7240MPzKbZosvqH5vTucyPCSIBwCiUR2mvAqJUpKMQKU3008b0iswPy1sd89_70UYPvvIRCOPc179wiZMchSkBOvdk51GnZ971bTQNao-OO4gR5PC1U4xvHExMhfa9-Y9gSOqoqoM4epQSmFjkToP81cDXTtOQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من بندر عباس تضهر ارتفاع اعمدة الدخان بعد قصف الاحتلال الاميركي الاخير</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83427" target="_blank">📅 22:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83426">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الكويت تعرضت مؤسسات حيوية لهجمات إيرانية بالمسيرات</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83426" target="_blank">📅 22:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83425">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الكويت تعرضت مؤسسات حيوية لهجمات إيرانية بالمسيرات</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83425" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83424">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83424" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83423">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
ترامب: سمحت إيران لمواطنة أمريكية، احتُجزت ظلماً في ديسمبر/كانون الأول 2024 خلال فترة رئاسة جو بايدن، بمغادرة البلاد. وهي الآن بأمان خارج إيران، وبصحة جيدة. تُقدّر الولايات المتحدة الأمريكية هذه البادرة الحسنة من إيران!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83423" target="_blank">📅 22:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83422">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Ae_xxFHMfk0QvHH9DCcwDHgFWO1R8RDuwO4BYknQ4stJXm5RIu3-OXD7VoMd8V97yyED3cIZmZAs1jvJJWdRwbr0NNtKhzx1JtxsHx0YUt-4QoyNPL6mbjGjTanQQcVYdOoRR3XmfYKGn9WQXHjyRV4gBM3EZOMwGAK1Jp2kKf0k0B6BM6f2O36KSf-UcsC4PugY6-y_1XCilGak3L-XjwPLchiU_mSB9YpJQ6fE6diokz9Ra3UCM_d06Wvg5F7sU5M4nAP9zb4MhRfc_u0N_On1rv4ELxqqVQ5LRA96lDkCKCHO1GzjPC8vP5nOoaVlL82WY0n7mQ1SoGKxQ6kpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Ae_xxFHMfk0QvHH9DCcwDHgFWO1R8RDuwO4BYknQ4stJXm5RIu3-OXD7VoMd8V97yyED3cIZmZAs1jvJJWdRwbr0NNtKhzx1JtxsHx0YUt-4QoyNPL6mbjGjTanQQcVYdOoRR3XmfYKGn9WQXHjyRV4gBM3EZOMwGAK1Jp2kKf0k0B6BM6f2O36KSf-UcsC4PugY6-y_1XCilGak3L-XjwPLchiU_mSB9YpJQ6fE6diokz9Ra3UCM_d06Wvg5F7sU5M4nAP9zb4MhRfc_u0N_On1rv4ELxqqVQ5LRA96lDkCKCHO1GzjPC8vP5nOoaVlL82WY0n7mQ1SoGKxQ6kpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
انفجارات متتالية في بندر عباس</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83422" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83421">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتكوم: ‏في تمام الساعة الثانية مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت القوات الأمريكية شن موجة جديدة من الضربات ضد إيران.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83421" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83420">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
🇮🇷
انتقاد شديد للدكتور علي أكبر ولايتي من رئيس الوزراء العراقي
مستشار قائد الثورة، في مذكرة، وجّه انتقادًا شديدًا لزيارة رئيس الوزراء العراقي إلى الولايات المتحدة، وكتب:
بسم الله الرحمن الرحيم
﴿إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ﴾
«زيارة مؤسفة، جاءت في غير وقتها، وألحقت ضررًا بتضحيات الشعب العراقي الأبي والمجاهد عبر آلاف السنين من تاريخ هذا البلد الكبير، قام بها رئيس الوزراء الشاب قليل الخبرة، السيد علي الزيدي».
وأضاف أن استخدام آية الاسترجاع في وصف هذه الزيارة معبّر تمامًا، معتبرًا أن ما جرى خلالها يُعد من الأحداث النادرة في تاريخ العراق الطويل، وأنها وجهت ضربة لا يمكن وصفها أو استيعابها لكرامة الشعب العراقي المؤمن والشجاع.
وأكد أن هذه الخطوة تمثل عارًا كبيرًا لكل مسلم وكل إنسان حر، سواء كان عراقيًا أو غير عراقي، ولا سيما أنها جاءت بعد استشهاد أحد أعظم العلماء وأكثرهم تأثيرًا في عصر الغيبة، في وقت لم تكن فيه مراسم الحداد قد انتهت بعد.
ووصف الرئيس الأميركي بعبارات شديدة، معتبرًا أن جرائمه لا نظير لها في التاريخ، وأنه يفوق أكثر الطغاة والقتلة شهرة في الإجرام، داعيًا الله أن يكون في أسفل دركات جهنم.
وأضاف أنه لا يعلم ما الذي كان يتوقعه رئيس الوزراء العراقي من هذه الزيارة، متسائلًا إن كان قد اتخذ قراره دون استشارة، ومؤكدًا أنه لو استشار أهل الخبرة والالتزام في العراق لأدرك المكانة التاريخية والدينية لهذا البلد.
وأشار إلى أن العراق، منذ الحضارات السومرية وحتى الإسلام، ثم في عهد أمير المؤمنين الإمام علي عليه السلام، والإمام الحسن، والإمام الحسين، والمختار الثقفي، ومالك الأشتر، وميثم التمار، وحجر بن عدي، ثم ثورات الأئمة عليهم السلام، كان له دور محوري في تاريخ الإسلام، وأن الشعب العراقي قدم أعظم صور الجهاد حتى أسقط نظام صدام.
كما ذكّر بموقف نوري المالكي حين رد على ترامب بالآية الكريمة: ﴿وَلَن تَرْضَىٰ عَنكَ الْيَهُودُ وَلَا النَّصَارَىٰ حَتَّىٰ تَتَّبِعَ مِلَّتَهُمْ﴾، مشيرًا إلى أن ترامب كان يعتبر المالكي عقبة أمام سياساته.
وختم بالقول إن من المؤسف أن يزور رئيس الوزراء الحالي البيت الأبيض قبل انتهاء مراسم عزاء القائد الشهيد، من دون أن يظهر أي أثر للحزن، مضيفًا أن السياسة تعني الإدارة، وأن من يفتخر بقتل القادة الشهداء كان ينبغي أن يواجه برد حازم، لا أن يُقال أمامه: «أنا لا أتدخل في السياسة». واعتبر أن هذه الزيارة وهذه الإهانة تسببتا بحزن الشعب الإيراني والشعب العراقي المؤمن والمجاهد، معربًا عن أمله في أن تكون كلماته دافعًا للتأمل وتحمل المسؤولية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83420" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83419">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنتكوم:
‏في تمام الساعة الثانية مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت القوات الأمريكية شن موجة جديدة من الضربات ضد إيران.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83419" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83418">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY_4IJJot_23e7G11LHOgunMys1A4naOX2Zht6MyhZ9anWibkac1lJA1krCi3aimvE3s_2rcySOHBz5YFnINl33gSwR6Qm23trq_mKtYagRT9uuHkjbclZrgqoVJk9V38Lmh4Nu8OQSDWz93IbdxSOtGq6RcLqQM210rEbZpheP2Pqijg7jyyvkf-Uegy-WOiUDHxj1HY44g62M1qfBbi6jYxxDgEYjJ5uz9g-3nWHkS38vo7SRycmZ5UVDpuj3I09dtOf2CN__jFstJVhpfHPx4D2JTCw_RB7i7ItE-bLcvvP9xHGUk4QvoiTKPwMbXfqj6xaUbmyc0ITHrtZvFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلة الغاز الطبيعي المسال "مبارز" المملوكة لشركة أدنوك عالقة في نفس المكان بمضيق هرمز باتجاه الطريق العماني منذ الأول من يوليو بسبب تحذيرات الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83418" target="_blank">📅 21:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83417">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
إيران تواصل الانخراط معنا في محادثات وترغب في إبرام صفقة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83417" target="_blank">📅 21:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83416">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
السفارة الأميركية في أربيل شمالي العراق
تنشر تحذيراً أمنياً شديداً بعد قصفها ليلة امس بطائرات مسيرة تدعو المواطنين الأميركيين إلى عدم السفر نهائياً إلى العراق، محذرة من وجود تهديدات وحالات عدائية تستهدف الأميركيين.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83416" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83415">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇶🇦
‏
قطر
: نرفض تقارير إعلامية إسرائيلية باطلة زعمت موافقتنا على المشاركة بعمل عسكري ضد إيران.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83415" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83414">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات شديدة في سماء دبي</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83414" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83413">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkZ6lnXE1nxI6M0oiwzhxddrFvW68vAfam68W_N3jjZrHgvUoduy7yi3exnXHGZoavTBjXbt22O_NHMPNxOTu5UFSM2TFIn8KiZ_oAPhsLSwNMxrAm6h_Ozj93XtBZtzLJ7p3EUIGyMXStMfw7h5lunAR1UyRtp1v9LOOQDYZKm9gli07aVAYT3hWmNFlLQp7z5Y74FDSTo9hdcCMkp0fH6Ok_tBDHNEH-2PPy7GCNL4Qh26U3iZkzBnTjnuaTxkUTVu155s2nfB60yN4Dj-xX1jD9hw9ggWlCQYR9JyPVLQlCf8y53gSUREJk9sGjhL7XwztOzVa9iaOFneBH9SHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر.. انفجارات قوية تسمع بقاعدة الظفرة الجوية في ابو ظبي</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/83413" target="_blank">📅 20:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83412">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رويترز: دوي انفجارات في وسط دبي</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/83412" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83411">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات على مقربة من الحدود العراقية الكويتية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83411" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83410">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رويترز
: دوي انفجارات في وسط دبي</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83410" target="_blank">📅 19:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83409">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
"اذهبوا إلى الجحيم، أنا أمثل الأمريكيين أولاً." هذا ما قاله نائب الرئيس الأمريكي جيه دي فانس رداً على الحملة التي تمولها إسرائيل بهدف عرقلة المفاوضات بين إيران والولايات المتحدة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83409" target="_blank">📅 19:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83408">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83408" target="_blank">📅 19:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83407">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇧🇭
‏
خفر السواحل البحريني:
تعديل موعد الحظر البحري ليبدأ عند الساعة 6:30 مساءً ويستمر حتى 4:00 صباحاً.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83407" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B648NWVMiUi8QIzJlzRd4Yo8MUJq0y9ja1I83JmSsxSSmkoUWqWV5h9UbQc0Ubpbbe7agvA0BZ8VR1gaFExDJAGw7N4KtoWj1OlsN72_VRViuj16ZqGmHKfWv3AkqSoxcrPQpMf2mYzsN0uxMFZUFBY0pLlltmNs4d7ff4I7FWX_2N1hlk3ix9jWfi2GSeqLTU93aM2Q6-hfleTqskApo4sL8kmz8GowdWx5xJaJCx6uADxx478s_m6WsuisQcEWY8WdnaWvp_4Zd4j4qb0dwuCWGz8KzWTd0qXlz1ozCRit9CCZek4FMnt0yOcnBGMASXTyo0tJUUZk_VWHc8y8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شوهد مضيق هرمز اليوم شبه خالٍ  ناقلتان فقط ظاهرتان تعبران المضيق ناقلة باناماكس متجهة للخارج عبر إيران، وناقلة عملاقة متجهة للداخل، وهي في وضع الخمول.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83406" target="_blank">📅 19:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JscGVBChV4Y6qogtWCWzguLYPK_6sxlkxr1OZQFRy-AvLqJ5dXp66DlQkEJaPlB4TPTyuiz0hNk7USLbX9soxCh1zpFoaugcwIpzr2CP_viSjhGtZlUFfXAELwnvLCQ7ZA8-9JCLvLNxpbk2jf4hYPd9QBw4Q_HPk3OxdvBgeIB51XHkLvl_gz85gOqMnAgJDZkKRC_t4dsMTmvNek-oamvqnq-v-cv-2Mz99kDEP3_hW7QIov9iNTowhE8J9pvNvJWEemaXJ9ooMU3qAeEarZafUVualTKaEIKtFu9fMII3pnit5MbPN9sAkzXkNlP42UxpfwcZvfM6tnsN8EXsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شوهد مضيق هرمز اليوم شبه خالٍ
ناقلتان فقط ظاهرتان تعبران المضيق ناقلة باناماكس متجهة للخارج عبر إيران، وناقلة عملاقة متجهة للداخل، وهي في وضع الخمول.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83405" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWPSRyTuTBM_zIjTBOgioitr9E8MYyH0v1Z14jhwB-a98_P7uNm4Zf8ujIos54rWeM8vJJh4yvSoTnfvsa4gom-s81USO8OAhvwokhiyLU6SdXJpIZa-C0lU5RhnWoL7t9ryxGMd57iiayo061fpgCZo02n9B1xvdktIdy-FeTYsZZlKVPG-LzSfV6rP9EgyN2tBgKKh2yEoZtkt0KeaqskZq29LSD1FvOW9tlsfdSCK5hi76Liw2RvGr3s7IW-n6Y4rcVM5N2HGv3B4Bkb6v2Rb0y3RwcpmVCPV22wjKcw3aokYKTCojfdXXz0JmYcXoT2e2CQtW1lC7sSsNoYgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb3o4OSpgh2cfoFmL0Ls-e8h-tbq8mnABMChr3OZxmkHiMV2pqdz844IfgjqVRC7NDkYKblCxNMZ7BkWWHwW1KxiOHUousiMNnBD3rzDpEkBH9k75y9NmWzCoI6O-qO6oVCgzysXbMj4TiNV10r_XSMc8PXgrXrPQQkr1LA-eTKugMMO5vEUHSvvIeO7ab70_mC-puGCbmFlGoMmOyANrRYMIIJ3T1Pbp_qoK5674JGnL4oWFbTn0t552OssuRxLVZyePT0OOKtbskb0AgEd21svhim-Fbg7u9YEeUNKPjDH3bQoKKpuh_XjXn_HNZ7AjnIKuwbP0_JOCyMd1y8T5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
‏
وزارة الخارجية الإيرانية:
بسم الله الرحمن الرحيم
‏وزارة الخارجية في الجمهورية الإسلامية الإيرانية
‏بيان وزارة الخارجية بشأن الهجمات الأمريكية الوحشية على إيران وجرائم الحرب المرتكبة
‏خلال الأيام القليلة الماضية، قام النظام الأمريكي المجرم، في الوقت الذي أعلن فيه عن حصار بحري ضد الدولة الإيرانية - وهو اعتراف واضح بانتهاك جزء آخر من التزام الولايات المتحدة وفقًا لتفاهم إسلام أباد - بتكثيف هجماته العدوانية ضد الجمهورية الإسلامية الإيرانية وارتكاب العديد من جرائم الحرب، وخاصة استهداف المنشآت والمرافق المدنية.
‏إن الهجوم على مصحة اللواء 388 بالجيش في بامبور، إيرانشهر صباح يوم الأربعاء 14 يوليو، والذي أسفر عن استشهاد 7 مدافعين متحمسين عن الوطن وإصابة العديد من الأشخاص، والهجوم على صومعة تخزين القمح في مقاطعة هويزه، والهجوم على مصنع لإنتاج المياه المعدنية في منطقة موسيان بمقاطعة دهلوران، والهجوم على برج المراقبة البحرية في تشابهار بهدف تعطيل تقديم المساعدة للصيادين وتقويض أمن التجارة البحرية، والعديد من الهجمات المماثلة الأخرى، هي من بين جرائم الحرب التي ارتكبها المعتدون الأمريكيون في الأسبوع الماضي وحده.
‏لا شك أن هذه الهجمات غير القانونية تُعد انتهاكًا صارخًا لميثاق الأمم المتحدة والقواعد الأساسية للقانون الدولي. وتدين وزارة الخارجية الإيرانية بشدة هذه الهجمات والجرائم المرتكبة، وتتقدم بخالص التهاني والتعازي لأسر الشهداء الأبطال الذين ضحوا بأرواحهم في سبيل الحفاظ على وحدة أراضي إيران واستقلالها وكرامتها، وتدعو الله عز وجل أن يمنّ على أبطالنا الأعزاء بالصحة والعافية.
‏إن الهجمات الأمريكية العدوانية على إيران، والتي رافقها خطابٌ بذيء وتهديداتٌ شيطانية من مسؤولين أمريكيين، لا تهدف إلا إلى استعداء الإيرانيين بسبب إصرارهم على الاستقلال وحقوقهم وكرامتهم الإنسانية. إن التهديد المتكرر بمهاجمة الجسور ومحطات الطاقة بالتزامن مع استهداف بعض البنى التحتية الحيوية، دليلٌ قاطع على النية الإجرامية للسلطة الأمريكية الحاكمة لارتكاب جرائم شنيعة تُعتبر جرائم دولية خطيرة وفقًا للمبادئ والقواعد الأساسية للقانون الجنائي الدولي، بما في ذلك اتفاقيات جنيف الأربع لعام ١٩٤٩، وتلتزم جميع الحكومات بمحاسبة ومعاقبة قادة ومرتكبي هذه الجرائم. كما يجب على المشرفين على هذه الجرائم ومنفذيها أن يعلموا أن التذرع بتنفيذ أوامر من قادة أعلى رتبة لا يُعفيهم من المسؤولية القانونية، ولا من العبء الأخلاقي والضميري لارتكاب جرائم حرب.
‏انطلاقاً من المبادئ والقيم الوطنية والأخلاقية والدينية الأصيلة للشعب الإيراني، واستناداً إلى المبادئ والقواعد الأساسية لميثاق الأمم المتحدة والقانون الدولي، ولا سيما المادة 51 منه، ستستخدم الجمهورية الإسلامية الإيرانية كافة إمكانياتها للدفاع عن سيادة إيران الوطنية وسلامة أراضيها ضد العدوان العسكري والحرب المشتركة التي يشنها العدو الأمريكي الصهيوني، ولن تتنازل في هذا الشأن. ومن البديهي أن مقاومة الإيرانيين وصمودهم في وجه الشياطين الأمريكية المتعطشة للدماء لا يعفيهم بأي حال من الأحوال من المسؤولية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83403" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
انفجار في جزيرة قشم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83402" target="_blank">📅 18:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9YTsI8O8APOzjk7q9tNusIdB0cL8oM9LYwZkUrxmhK0kpH_uO21P-Lmoz5BUHDbqJ7RokCKXv-yXJ8lyu76HCkXbiMFuKxsfWD1217VyOcRexCT8fTWaTN4b-TgYbYW9lepcHWxEd846_hEKtfvddae_9TCYi4yKdIrtRwUwxb2kgf6u2XEi3e30GPkCLCGQgLMxBess9h0O97SV2uyY5XBZ3Y-e6Esai6ms1g7Qhyi98koHtnRKiwSjVveLz-S7YqA6wcFsbcRHHtqoMT08qMEPCTbBoeFvYIsh4YaTe0v5TXAZMJ_si5xG_SKkWXgHpLd3xaW-KNvQFXi426w1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الخزانة الأميركية:
تتوعد بمنح مكافآت مالية مقابل الإدلاء بمعلومات عن أنشطة أنصار الله في اليمن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83401" target="_blank">📅 18:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
🇮🇶
إغلاق منشآت الإنتاج الرئيسية في حقل كورمور بمحافظة السليمانية شمالي العراق بشكل مؤقت</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83400" target="_blank">📅 18:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25f11c333.mp4?token=rtvLlXh_5X-5nDgh2eWxjIrC4R_PlPQG1LbIxJaCAafHd82d8NuXYji459vdDTodxLGXGANcv5_V3ni7j6ATEHaGUbh7-RdPHKrxt5eC_lH-VCQAL_nYvv8rGEpCdHumpw175lukILs9Kjr7DPGFQaOLgc9TNul41CyvVtHBDiXVOFnux6yb2o5yyLrG6YVCqnSlfGemIxMI8nwq0WG0VqBGyv5p7avfhfGFqLHYINNJlC0Ba7u7v4gukBnfO0lXl2S02GHpEpMQiar4biQaPrZnxVdGbr_Gk813KWrbK-jFskDuOjgL_vRP6AsasO-9E6Weg8hs5hCcUdZ-op9asA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25f11c333.mp4?token=rtvLlXh_5X-5nDgh2eWxjIrC4R_PlPQG1LbIxJaCAafHd82d8NuXYji459vdDTodxLGXGANcv5_V3ni7j6ATEHaGUbh7-RdPHKrxt5eC_lH-VCQAL_nYvv8rGEpCdHumpw175lukILs9Kjr7DPGFQaOLgc9TNul41CyvVtHBDiXVOFnux6yb2o5yyLrG6YVCqnSlfGemIxMI8nwq0WG0VqBGyv5p7avfhfGFqLHYINNJlC0Ba7u7v4gukBnfO0lXl2S02GHpEpMQiar4biQaPrZnxVdGbr_Gk813KWrbK-jFskDuOjgL_vRP6AsasO-9E6Weg8hs5hCcUdZ-op9asA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر تدمير بطارية صواريخ باتريوت امريكية في مطار أربيل بعد هجوم يوم امس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83399" target="_blank">📅 17:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇱
اعلام العدو:
المصادقة على توصية للمنظومة الأمنية بالإبقاء على حماية بنيامين نتنياهو وزوجته طيلة حياتهما، لا سيما في أعقاب اغتيال القادة الإيرانيين الذي ضاعف التهديدات الأمنية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83398" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📰
رويترز:
يتم تجهيز القوات الباكستانية في السعودية للذهاب لمحاربة الحوثيين.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83397" target="_blank">📅 17:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
السفير السعودي في لبنان يوزع أموالا مغرية لمسؤولين وشخصيات لبنانية لشراء مواقفهم بالخيانة لشعبهم ومعاداة حزب الله.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83396" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
لجنة الأمن والدفاع النيابية العراقية توصي بإقالة اللواء مازن عبد الواحد كبيان، قائد القوة البحرية، ومدير العمليات، وإحالتهما إلى القضاء، على خلفية حادثة الصيادين والتجاوزات الكويتية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83395" target="_blank">📅 17:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سماع دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83394" target="_blank">📅 16:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f066b021.mp4?token=K4E9w5L3Egpc_nepgTgDfou4eIlpnoS1NGqJBDSBa0sIk6pRvjO4Q7Mglw1yAYo4fCj4lzrBfjqgqNjMhEIIbUzeBNPgjvMDDD2VKDV_dM0uFJEae1wM4h0tqM7TttmKqx8GG7-cFiROm2Bb04ZKuBAb9froI7fgk_finiSRTNbhgNEtVj1AjwkGg9aYlT3-KM7Fuz8ygS9FrwQMYF0Js-6tI0tBk9Q5d_6kNljI2O5ko_NDzhCFlgSnzZibczPOgBqw-KR2HrOncImebHSZfTAjrvWBG_nUfqNDHIjN1ZtigaTG-82R4EwTGyz5RascoCkLqRb14s0PnnFUoT0C5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f066b021.mp4?token=K4E9w5L3Egpc_nepgTgDfou4eIlpnoS1NGqJBDSBa0sIk6pRvjO4Q7Mglw1yAYo4fCj4lzrBfjqgqNjMhEIIbUzeBNPgjvMDDD2VKDV_dM0uFJEae1wM4h0tqM7TttmKqx8GG7-cFiROm2Bb04ZKuBAb9froI7fgk_finiSRTNbhgNEtVj1AjwkGg9aYlT3-KM7Fuz8ygS9FrwQMYF0Js-6tI0tBk9Q5d_6kNljI2O5ko_NDzhCFlgSnzZibczPOgBqw-KR2HrOncImebHSZfTAjrvWBG_nUfqNDHIjN1ZtigaTG-82R4EwTGyz5RascoCkLqRb14s0PnnFUoT0C5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚠️
مصدر لنايا  الإمارات شاركت بالهجوم البارحة على بندر عباس وتم استخدام مسيرات إماراتية تحديدا على المدينة الإيرانية بندر عباس ، المصدر اكد لنايا ان الإمارات استخدمت لاول مرة ذخيرة متسكعة من طراز Yabhon Loitering وتم اسقاطها قبل ان تصل للهدف .</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/83393" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
⚠️
مصدر لنايا
الإمارات شاركت بالهجوم البارحة على بندر عباس وتم استخدام مسيرات إماراتية تحديدا على المدينة الإيرانية بندر عباس ، المصدر اكد لنايا ان الإمارات استخدمت لاول مرة ذخيرة متسكعة من طراز
Yabhon Loitering وتم اسقاطها قبل ان تصل
للهدف .</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83392" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار داخل السفارة الأمريكية في بغداد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83391" target="_blank">📅 15:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
🇮🇶
إغلاق منشآت الإنتاج الرئيسية في حقل كورمور بمحافظة السليمانية شمالي العراق بشكل مؤقت</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83390" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
🇮🇶
إغلاق منشآت الإنتاج الرئيسية في حقل كورمور بمحافظة السليمانية شمالي العراق بشكل مؤقت</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83389" target="_blank">📅 15:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
🇸🇾
قيادة العمليات المشتركة العراقية:
​
بعد إحباط عملية تهريب أسلحة وصواريخ عبر الحدود العراقية نحو الأراضي السورية .
​نودّ الإيضاح أنه بتوجيه من السيد القائد العام للقوات المسلحة، تم تشكيل لجنة عليا من الجهات ذات العلاقة والمختصين للوقوف على تفاصيل هذا الموضوع بالكامل.
​كما سيتم التنسيق مع الجانب السوري لمعرفة جميع التفاصيل المتعلقة بهذه العملية ، ومحاسبة المقصرين بما يضمن الحفاظ على أمن واستقرار الحدود المشتركة، ومنع أي محاولات لزعزعة الأمن الوطني.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/83388" target="_blank">📅 15:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83387">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
🇮🇷
🇾🇪
رويترز: اتفاق بين إيران وانصار الله على إغلاق باب المندب بحال استهدفت أميركا منشآت الطاقة</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83387" target="_blank">📅 15:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83386">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇷🇺
🇺🇸
نائب أمين مجلس الأمن التابع للاتحاد الروسي:
إن رغبة الولايات المتحدة في السيطرة على أسواق الطاقة أدت بشكل أساسي إلى التدخل في الحكومة الفنزويلية وبذل جهود ضد الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83386" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83385">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
🇸🇦
🇮🇶
🇾🇪
السعودية تقرر حظر حسابات عراقية ويمنية وإماراتية على موقع اكس " تويتر سابقا " بسبب نشرها حجم الضربات اليمنية الأخيرة على جنوب السعودية ، حيث أصبحت هذه الحسابات غير متاحة للمتابعة او الظهور داخل السعودية !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83385" target="_blank">📅 14:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
الموانئ العراقية:
المسيّرة التي سقطت على إحدى الناقلات خارج نطاق موانئنا، عمليات التفريغ والمناولة مستمرة من دون أي توقف.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83384" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83383" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83382">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83382" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83381">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/83381" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83380">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
🇸🇦
🇮🇶
🇾🇪
السعودية تقرر حظر حسابات عراقية ويمنية وإماراتية على موقع اكس " تويتر سابقا " بسبب نشرها حجم الضربات اليمنية الأخيرة على جنوب السعودية ، حيث أصبحت هذه الحسابات غير متاحة للمتابعة او الظهور داخل السعودية !</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83380" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
محكمة جنايات مكافحة الفساد المركزية تصدر حكماً بالسجن لمدة سنتين بحق النائب محمد الكربولي، بعد إدانته بتهمة الرشوة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83379" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
😊
🇮🇷
الكرملين نحن مع تواصل مستمر مع ايران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83378" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
وقف عمليات تصدير النفط مؤقتا في ميناء البصرة العراقي بعد استهداف ناقلة نفط بمسيرة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83377" target="_blank">📅 13:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb4f0a18c.mp4?token=QLf0hNyfsV3zOJ6LGEPNybNJv3GKGGO06imTi-1fHUuTuIJxJuUFs-FlkkI7cvnSYMNweZAqfiZhgdksonATethW_KPZTJaVhWH03lDIFRoy_jY39pnrugj3-aHm5sHH_WHASoIrwbKO3B0NPVJPfWqe8R_47Q1ms9w3llm1i5xxkEH9G-3w6MUltMe3Wq2hvqrpU7cBxLbewpJFwzxKzzwJ9ovNeDdsNOQLTRp_9hMRnjGxt4SsKEOuc3vefDvZCDTIeBYzbIDOfcrd2sJuFk83y9kvVfNYrZLEBMRYVe2Fv3tpYe44mHSVt_38Uun2rhWoo36MhT4HUP8QjYZ-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb4f0a18c.mp4?token=QLf0hNyfsV3zOJ6LGEPNybNJv3GKGGO06imTi-1fHUuTuIJxJuUFs-FlkkI7cvnSYMNweZAqfiZhgdksonATethW_KPZTJaVhWH03lDIFRoy_jY39pnrugj3-aHm5sHH_WHASoIrwbKO3B0NPVJPfWqe8R_47Q1ms9w3llm1i5xxkEH9G-3w6MUltMe3Wq2hvqrpU7cBxLbewpJFwzxKzzwJ9ovNeDdsNOQLTRp_9hMRnjGxt4SsKEOuc3vefDvZCDTIeBYzbIDOfcrd2sJuFk83y9kvVfNYrZLEBMRYVe2Fv3tpYe44mHSVt_38Uun2rhWoo36MhT4HUP8QjYZ-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
انتشار كثيف أمام منزل خورشيد الهركي زعيم قبيلة الهركي الكردية على خليفة اعتقاله من قبل قوات البرزاني في محافظة أربيل شمال العراق مطالبين بإطلاق سراحه أو إعلان الحرب عليهم</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/83376" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI9fIeeT4au8sTb9BsOOwNRTlyRGeG06xOddiOeMEqtlTLmOWnMP01f5OzEek08gUfIkXq0NmvecR6YQ9a_IR0pLyy0NitYpcKIrll7rMpAqwZEHJprWMQu1Y1meB_stORkYpuvn7EA3NHwEoN3CkayY-FKfyjigGFtpTHpQQxnYFS050aJWyHJDjS1ZZPWCZdzQpT2E0vyZLWvKydLTmHEhZnoiRimeYLcPnAUW6bQt89VgfEjmBO_qgkZVAt_N4Q_nJBCVWcYR0EoSoIbALjxksPYvmUgahqfMFbdcMVyB_oIr4eIwiTgjhvUJWJ6kI22rNKj1yiTNWHLz3Qgpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
صحيفة بريطانية: أنصار الله في اليمن تستعد لإغلاق مضيق باب المندب، وهو ممر بحري عالمي رئيسي. حيث ستعكس هذه الخطوة استراتيجية إيران في مضيق هرمز، وقد تؤدي إلى تعطيل التجارة العالمية بشكل كبير من خلال إجبار السفن على تغيير مساراتها والتحرك حول أفريقيا.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/83375" target="_blank">📅 12:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
سقوط طائرة مسيّرة قرب ناقلة نفط تحمل علم ليبيريا في ميناء البصرة النفطي ضمن المياه الإقليمية العراقية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83374" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇾
حكومة الجولاني الإرهابية تدعي إحباط محاولة إدخال ‏شحنة أسلحة نوعية وصواريخ من العراق كانت متجهة لحزب الله في لبنان.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83373" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
قام أبناؤكم الأقوياء والمجاهدون في القوة البحرية التابعة لحرس الثورة الإسلامية، خلال الموجة العاشرة من عملية «نصر 2» تحت الشعار المقدس «يا علي الأصغر (ع)»، بشن هجوم عنيف على القاعدة الأمريكية في الشيخ عيسى في البحرين، دمّروا خلاله بالكامل رادار كشف ومراقبة المجال الجوي ومحطة ضخ خزانات وقود مقاتلات العدو المعتدي، ولا تزال هذه المعركة مستمرة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83372" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: العثور على جثمان في منتصف حقل ألغام على الحدود مع لبنان الجيش الإسرائيلي يتحقق من التفاصيل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/83371" target="_blank">📅 11:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة الاوكرانية كييف نتيجة هجمات روسية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83370" target="_blank">📅 10:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83369" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83368" target="_blank">📅 10:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
قام أبناؤكم الأقوياء المجاهدون في البحرية التابعة للحرس الثوري الإسلامي، خلال الموجة العاشرة من عملية نصر ٢، تحت الاسم الرمزي علي أصغر، وخلال هجوم مدمر على القاعدة الأمريكية في الشيخ عيسى بالبحرين، بتدمير رادار الاستطلاع والتحكم الجوي والمحطة دُمِّرت خزانات وقود مقاتلي العدو الغازي تدميراً كاملاً، والمعركة مستمرة.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83367" target="_blank">📅 09:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:  أيها الشعب الأردني الكريم والنبيل، في الليلة الماضية، ارتكبت القوات المسلحة الأمريكية، في تعدٍ صارخ، هجومًا باستخدام القواعد الجوية الموجودة في الأردن، مستهدفةً مناطق مختلفة في إيران، بما في ذلك محيط مستشفى لعلاج سرطان الأطفال. وقد…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83366" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
🇮🇱
وزير الحرب الأميركي يُطلع وزير الدفاع الصهيوني على تطورات العملية العسكرية بإيران ويؤكدان على مواصلة التعاون بشأن الحرب في إيران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83365" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
المتحدث باسم الجيش الإيراني:
سيظل مضيق هرمز مغلقا ما دامت واشنطن لا تعترف بنظامنا القائم على سيادة القانون
السيطرة الاستراتيجية على مضيق هرمز أصبحت مطلبا وطنيا في إيران</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83364" target="_blank">📅 09:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
أيها الشعب الأردني الكريم والنبيل، في الليلة الماضية، ارتكبت القوات المسلحة الأمريكية، في تعدٍ صارخ، هجومًا باستخدام القواعد الجوية الموجودة في الأردن، مستهدفةً مناطق مختلفة في إيران، بما في ذلك محيط مستشفى لعلاج سرطان الأطفال. وقد أُخرج 121 طفلًا مصابًا بالسرطان من هناك. هذا ليس أول جريمة ترتكبها أمريكا باستخدام القواعد المنتشرة في الأردن. ففي السابق، قُتل 168 طفلًا في هجوم أمريكي على مدرسة ابتدائية في مدينة ميناب. ردًا على هذه التعديات، استهدفت قوات الفضاء الجوي التابعة لحرس الثورة الإسلامية، في الموجة الثامنة من عملية "النصر 2"، تحت شعار "يا زينب الكبرى (س)"، منصة صيانة الطائرات الأمريكية ومركز القيادة والتحكم الجديد الأمريكي في غرب آسيا، الواقعين في قاعدة واسعة في الأزرق بالأردن، بصواريخ باليستية "خيبرشكن"، ودمرتهما.
أيها الشعب الأردني الشجاع، أنتم أكثر من أي أمة أخرى، تشعرون بجريمة أمريكا والصهاينة عن كثب. لا تسمحوا بأن تستخدم الأراضي المقدسة للأردن، التي هي مهد الأنبياء، في هذه الجرائم ضد الأطفال. استخدموا كل ما في وسعكم لضرب مصالح أمريكا، وطهروا أرضكم من الغزاة الأمريكيين.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/83363" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83362">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇱
هآرتس العبرية: غراهام لم يكن حقًا صديقًا لـ "إسرائيل" بل كان صديقًا لـ "إسرائيل مرتكبة جرائم الحرب"</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83362" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecf157b56.mp4?token=O33Qu5huFsliLt9D4yugycLoL9Fhag5FjvosCPHSHkZSyeB7B5ps6YrZANPGGCmoMGPNYLBn61NVcLrMjBGcqmLfSlP5ovm-oUVvhabnTmX6RX3Bd-ky6s4WWv8Asu7Ar--5ubaCsXRQ47IUA3oTxwMkZ1rsj964tOqWGaNRQV0uz0-NDjXnwdzfQpslf3bnwgyPscghL-oFk_12BZuyUXCCpvBkLWsOb2w3XMS_U5ZLDD3NucRIGS4cm-0vS00Bt_aHRrOJ0v4rTNK9W-uhsxHRpD_2VT8UEOp1E8gTWElapA5Do0CXWOg7MVJzYyiC8bUL4zY5JSPqwSmUikDzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecf157b56.mp4?token=O33Qu5huFsliLt9D4yugycLoL9Fhag5FjvosCPHSHkZSyeB7B5ps6YrZANPGGCmoMGPNYLBn61NVcLrMjBGcqmLfSlP5ovm-oUVvhabnTmX6RX3Bd-ky6s4WWv8Asu7Ar--5ubaCsXRQ47IUA3oTxwMkZ1rsj964tOqWGaNRQV0uz0-NDjXnwdzfQpslf3bnwgyPscghL-oFk_12BZuyUXCCpvBkLWsOb2w3XMS_U5ZLDD3NucRIGS4cm-0vS00Bt_aHRrOJ0v4rTNK9W-uhsxHRpD_2VT8UEOp1E8gTWElapA5Do0CXWOg7MVJzYyiC8bUL4zY5JSPqwSmUikDzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تظهر صور الأقمار الصناعية أضرار كبيرة جداً جراء القصف الإيراني على سطح أحد الفنادق التي يمكث بها قوات الاحتلال الأمریکي في الدقم بسلطنة عمان.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83361" target="_blank">📅 07:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zon5w1xkvhn8xObhaWRFIcKQjXRugTDPQEGnxjk4IUipYoJDtGTV-ebiF2y9K2y86oE9wkgulPnt75DykyrWBbXBSWXwszu5YVBuAtRPO7riSscW3vGCTrCt6yzHUq-d1bzNVq5xZchKSwmvIpG7FjtKgsCm0nq-QWvHXs9WyzaCI7RVnvszxll8u7McqVHxjDmCdyO0G7AthGAUuJs49WUB7iJ2TEp6oxdR6AVxJNZ1ghtz8oF-jMx_oQrzTMu1ACxL0mbuJHA-pG2Woqoqk-vm3UPiezOK3guFs4wlK-S4T1WeL9wV3ywutdflskt85C8BB-W2PGjl0DvvYEavSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلة الغاز الطبيعي المسال "مبارز" المملوكة لشركة أدنوك عالقة في نفس المكان بمضيق هرمز باتجاه الطريق العماني منذ الأول من يوليو بسبب تحذيرات الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83360" target="_blank">📅 07:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
أصوات الانفجارات في خرم آباد كانت نتيجة إطلاق صواريخ نحو المصالح الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83359" target="_blank">📅 07:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الأردن: تعرضنا لهجوم جوي ب 8 صواريخ استهدفت الأراضي الأردنية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83357" target="_blank">📅 07:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7QTggPgJYyTG5H-fADbkG0E-3sf9UWWxlwIuUveNgPoQVyCFlcnEW5iZ7cYP3tZPzujLUQIZKlr2uFIZ9Gr8yPbs37FCzYwBArXKgOZJtBQwzvPgqg6H6IFhxKGezKZjv8xgNnVVyEeP7kBMqBF15Vcj3XNWydRh35FNg6Mrg570gQh7vsYhq3BIE6onCwlTJ1mGtYmw6JGHF7R0W-UGV4wKo3as7kueObfE22_wq9a3vVN55fnA7fl_ajfRifq6B3W-ywYvnfrPEHbMItMKoT0eZqjC7ZV-FQx3h4RVSPh9AT_8swyZ6EZv9gl0MUi89g03-RAI2u1aczpRa1y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇴
تحليق طيران الإنذار المبكر الأمريكي بشكل مكثف في سماء العقبة الأردنية</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83356" target="_blank">📅 06:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a1959f42.mp4?token=gE2fWeX26vRZkMl8iNX4jsmHtzRGs2dEFizks6n86xvi64XRSgQlL3hYEx0GFvXvPa-CuEQv-0u_i6GnHlXR8HB1CAjQKN5EwvLoqfU7uRX2A07qoeKrUJABP8H_5JbuKO3yfBZqEarUn0_svfwyTGVnFeQI06wZpl64zr23KgiE4J2rLAGHbrJcH_pAagqSSnTdkFoI1ykXZPtcoBrlPVIxdxoMzj9jkElu-lbllDqzP8iZsLSSdjuwBQM524-xhI-7G7FaYSiwHm10bdwwR3EPpDV0rpMGrePB_D77BPIrDciFA8LGD-L09JuTtXg07MJzMTwxIspvOU3AvEtr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a1959f42.mp4?token=gE2fWeX26vRZkMl8iNX4jsmHtzRGs2dEFizks6n86xvi64XRSgQlL3hYEx0GFvXvPa-CuEQv-0u_i6GnHlXR8HB1CAjQKN5EwvLoqfU7uRX2A07qoeKrUJABP8H_5JbuKO3yfBZqEarUn0_svfwyTGVnFeQI06wZpl64zr23KgiE4J2rLAGHbrJcH_pAagqSSnTdkFoI1ykXZPtcoBrlPVIxdxoMzj9jkElu-lbllDqzP8iZsLSSdjuwBQM524-xhI-7G7FaYSiwHm10bdwwR3EPpDV0rpMGrePB_D77BPIrDciFA8LGD-L09JuTtXg07MJzMTwxIspvOU3AvEtr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
طيران مسير يحلق نحو الأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83355" target="_blank">📅 06:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c8fa0dc1.mp4?token=aLjl5GBk_yL8yHTP0LfIU9gEFeMPNYrMzhD6zWugmMkGgEEwp-bjSIe6zaE00L-xtNWntjZDbFbmHsnR4vI1xyFDG6EKTbWYuwY1lGn4a-sIEWaSqqaQ2KpJQ_0fYJ3O2S69E9GomZ-9JuPbQInz3xQNJhaL5Aqd_vz2dgXS3OEauI2lyHeUylwIJqcFJV7H0VIOuj-SOIOP3H1fbCUu6XDD0bT_lqfDcwntiKCd60FTo0apQ1VMN-ogkG46O2lZU8sxwKWQlx0sbeeLLJPqK0VqPl_xDJKjkw3pbt0ast_vZmqG2qGy3R9XyZu0CoyM6AWQ_vR8phdkUJ6DZ-ws2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c8fa0dc1.mp4?token=aLjl5GBk_yL8yHTP0LfIU9gEFeMPNYrMzhD6zWugmMkGgEEwp-bjSIe6zaE00L-xtNWntjZDbFbmHsnR4vI1xyFDG6EKTbWYuwY1lGn4a-sIEWaSqqaQ2KpJQ_0fYJ3O2S69E9GomZ-9JuPbQInz3xQNJhaL5Aqd_vz2dgXS3OEauI2lyHeUylwIJqcFJV7H0VIOuj-SOIOP3H1fbCUu6XDD0bT_lqfDcwntiKCd60FTo0apQ1VMN-ogkG46O2lZU8sxwKWQlx0sbeeLLJPqK0VqPl_xDJKjkw3pbt0ast_vZmqG2qGy3R9XyZu0CoyM6AWQ_vR8phdkUJ6DZ-ws2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة التاسعة من عملية "صاعقة"، وردًا على انتهاكات العدو القاتل للأطفال لمناطق في بلادنا وقاعدة "بمبور" في مدينة "إيرانشهر" الإيرانية، مما أدى إلى استشهاد 7 من ضباط وأفراد الجيش، استهدفت الطائرات المسيرة الإنتحارية التابعة للجيش الإيراني موقعًا راداريًا ثابتًا، ونظام اتصالات، ومخازن وقود تابعة للجيش الإرهابي والعدواني الأمريكي في قاعدة "الأزرق" في الأردن.
🔹
تعتبر هذه القاعدة موقعًا لنشر أنظمة الدفاع الصاروخي، وهي واحدة من أهم المراكز الاستراتيجية والقيادية للقوات الأمريكية المعتدية في منطقة غرب آسيا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83354" target="_blank">📅 05:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931b2b49bd.mp4?token=kSwiSl82OybGOU63wTcHRmenaOfbyPqd5xliMNMX17-dRIuzXXB9l8GJgRWmPEuoo_AIwFU-EZ6mpQ1r2A3vRXhs6Kr04JgphHJiVbo-kgpypJQjRkZ9BQsrKS3Qz79HDxgQ3b08tWBjauDAISd8mMnUI2G_16ySLVXcXcQWXQLsIOw6ksSrDU5qjmYF0l0fOEMRXV0VHdDlpzzQKgPGGovUldzw0NHsImAlP-2WwXwmql5I4jEElA8MHVwLQQPRmWg-dxNPwH50bLhjoRniBHGLvx_y3SSK-Wc9vbtJe_qpX4pa2PMmhioV5timqaBb2EvWb82bp4DRYTXVzb2oCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931b2b49bd.mp4?token=kSwiSl82OybGOU63wTcHRmenaOfbyPqd5xliMNMX17-dRIuzXXB9l8GJgRWmPEuoo_AIwFU-EZ6mpQ1r2A3vRXhs6Kr04JgphHJiVbo-kgpypJQjRkZ9BQsrKS3Qz79HDxgQ3b08tWBjauDAISd8mMnUI2G_16ySLVXcXcQWXQLsIOw6ksSrDU5qjmYF0l0fOEMRXV0VHdDlpzzQKgPGGovUldzw0NHsImAlP-2WwXwmql5I4jEElA8MHVwLQQPRmWg-dxNPwH50bLhjoRniBHGLvx_y3SSK-Wc9vbtJe_qpX4pa2PMmhioV5timqaBb2EvWb82bp4DRYTXVzb2oCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
طيران مسير يحلق نحو الأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83353" target="_blank">📅 05:45 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
