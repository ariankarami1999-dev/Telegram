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
<img src="https://cdn4.telesco.pe/file/KbteY4qQzX364hZpKecS82tCojVcWe9zjkVDtcoN_rC3Kjf9zpdqtfD7e1hssJiT2A6sCfQP3BlC_97u1PJTDq57O7SwDpqfc_BhNx0NfdkqMe1WPsRV7Bmr2clmJ4yDJQtOL18KArR-Pfxvb4Tl7kGWMBeKzk4JPKYz5dQmfLjK6mwOAU6qQlvsOYtcRGm_tCmu0jm4RdGf2aFz96lr4SUAgVuE3UhoOf5q2zDiJAIIaMdODAIhys2CZS51-2kpQDAI8YM1XqBtGHP2xAgemElLvHpVmpxD-ulylKqc9H-aQ4VRArDkP4j59vK7U2uW_Zjwp7yFu8lv51dGbIfJWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭐️
رويترز:
تتضمن اتفاقية إطارية بين الولايات المتحدة وإيران صندوق استثمار خاصًا مقترحًا بقيمة 300 مليار دولار أمريكي لدفع الاستثمار في إيران، حيث تم بالفعل التعهد بأكثر من نصف التمويل.
الصندوق، الذي تدعمه شركات من الولايات المتحدة ودول الخليج وآسيا وأمريكا الجنوبية وأفريقيا، يهدف إلى تشجيع كلا الجانبين على إنهاء اتفاقية أوسع نطاقًا.</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/naya_foriraq/79037" target="_blank">📅 21:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
🌟
هبوط سعر الدولار الأمريكي أمام التومان الإيراني بعد الإعلان عن توقيع مذكرة التفاهم حيث  100$ دولار كان يعادل 18 مليون تومان، واليوم وصل الهبوط إلى 15.5 مليون تومان في مقابل 100$ دولار.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/79036" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني.. بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/79035" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇱🇧
No need to press ok</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/79034" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكِّد على جهوزيتنا المستمرة تجاه أي تصعيد أو تطورات في الوضع الراهن من جهة العدو الأمريكي والإسرائيلي يستهدف المنطقة أو يسعى للانفراد بغزة من جديد،أو أيِّ ساحة في محور الجهاد وبلدان المنطقة.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/79033" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني..
بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/79032" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/79031" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
محافظة ديالى تقرر أن يكون الدوام الرسمي ليوم الأربعاء الموافق 2026/6/17 من الساعة التاسعة صباحاً ولغاية الساعة الثالثة ظهراً وذلك لإتاحة الفرصة للجميع لمتابعة مباراة منتخبنا الوطني أمام المنتخب النرويجي ضمن مباريات التصفيات المؤهلة إلى كأس العالم.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/79030" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79029">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
تحطم طائرة عسكرية أوكرانية، من طراز MiG-29، في منطقة خملنيتسكي.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/79029" target="_blank">📅 20:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
سي إن إن:
تشير تقديرات الاستخبارات الأمريكية إلى أن إيران باتت قادرة على إغلاق مضيق هرمز متى شاءت. وقال مصدر استخباراتي: "لقد منحنا إيران فعلياً سيطرةً على المضيق، وهو سلاحٌ يفوق في قوته أي سلاح نووي".</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/79028" target="_blank">📅 20:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYfbZoQElxGIJqRSfrMiHBY9rN38PkWSX0Z6yPETPKKNOMQ4tR1-5nh9RfGEtaElRffBKwTyR-OAsqaXKcxWz8qJtS_BP9GWHDYMXe_xhVFWgGTqtXQkrHSIqBumiWyasthV2xGZ2TeJlcrbe2oRPvOjW7nO6LZ2JeOKFJYz1NTHLZzIEd8KvqVWY2ibVEBTMR3bhnH53A4zmGMz_6xneRpimzOBf8J2Cs6dwqTZtolsAohLkvbtr8heWa21mpiudhJKx8MC8WaHthgFT5r5BKk2IZe_gFl0nuFFK0afQ0MEtK8jKjL8F6B-1u-ZixVRRBKNg_CtFQspHsKzyCbVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🗓
بخشی از پیام ۷/خرداد/۱۴۰۵ رهبر انقلاب اسلامی
🖨
نسخه کیفیت اصلی
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/79027" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs-C0T8mGTqO3BDsiYmU_r9tBwmn8KF1h9K9A34tqIwcmiTuGesW4hHvHG1JkCo3XmipVzFrU0CUKmCpIPE1k9TK2E-MKfggpTHGvDcTGOEwsKP8hK7ddfD4uPR64wbJDdiOgnBpf8C64WikMksUvNWmIKPV7ST1Wu1KesXlmjuocr7R3BHq3Xtzit-gt0XLdYrcNWGCKtqGJb3vwoAgLiEXrsENu4klhgenqqxhC5fzXqA72FnIUg6z1jpUWzdVj8sLmCUXCAE-d8EsIG_3xuNlszj7xyEXgNRG-9znr1HxWV0cyazJe1fcbG3ArjIt9v-E75dPYAX_smeljuJ1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/79026" target="_blank">📅 19:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79025">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
غارات صهيونية جديدة تطال بلدة ميفدون بالجنوب اللبناني ؛ إرتقاء 4 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/79025" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇫🇷
🌟
فرانس برس:
تتخلى وكالة الاستخبارات الداخلية الفرنسية (DGSI) عن شركة Palantir، حيث يشير رئيس الوزراء سيباستيان لوكورنو إلى مخاوف من الاعتماد الاستراتيجي على الولايات المتحدة.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/79024" target="_blank">📅 19:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79023">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🇮🇷
مصادر أمريكية:
واشنطن ستسمح لطهران بالبدء فورا ببيع النفط والوقود بموجب اتفاق إنهاء الحرب.</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/79023" target="_blank">📅 19:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWh7R-zaud31Va3UWmunPpzj9K7SOi8u9rtlo08Vs_NZy8AIw0kAh6V71Pcj71Y7__rG7byyEQnQsaqibOS5uq-t3m9JYbk0n7rxkdxX0mzvwwedf_aDKBQ3YCCanthOlWcImxAMzdRHI7T_Mcn9nAtuf3zz6j34Qeb7eZV5Lilv_eygNGB3FpXnn-jROc5rsFBNJHYTZAxgnP7Zrk4-JPOZUDj-kRL5Db-SSkTfq8X7LLfTIowp0efgoTqcV5KNnyk3iQJqBMYbhHqYB8wgW5TgY1mgLMRJ8QDxGW6eoJnOpa9r8cUK_I1MFQPPRRGO8nU-Vp6dziBbTXy5fpCqXlSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWh7R-zaud31Va3UWmunPpzj9K7SOi8u9rtlo08Vs_NZy8AIw0kAh6V71Pcj71Y7__rG7byyEQnQsaqibOS5uq-t3m9JYbk0n7rxkdxX0mzvwwedf_aDKBQ3YCCanthOlWcImxAMzdRHI7T_Mcn9nAtuf3zz6j34Qeb7eZV5Lilv_eygNGB3FpXnn-jROc5rsFBNJHYTZAxgnP7Zrk4-JPOZUDj-kRL5Db-SSkTfq8X7LLfTIowp0efgoTqcV5KNnyk3iQJqBMYbhHqYB8wgW5TgY1mgLMRJ8QDxGW6eoJnOpa9r8cUK_I1MFQPPRRGO8nU-Vp6dziBbTXy5fpCqXlSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79022" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇷🇺
🇬🇧
ذي تليغراف:
أطلقت الفرقاطة الروسية "الأدميرال غريغوروفيتش" طلقات تحذيرية على يخت بريطاني في القناة الإنجليزية يوم الاثنين، بعد اقتراب السفينتين من بعضهما.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79021" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=lNeGOIpKh_sGnG9jicZ0TDr6NInYwk5RSJFYiqrQrraM24igD21VOujbJBW_7pVDaFNrUpBlvs_Du0W7TAxBwDyG-XchXforj90XPGaNMQwGchsFyBVRxx2IQ6H2vmoNp2AqIoZs-KWIjA7MAGGEQO_sl-wgRFGgX8dPF59nJ34UU6ryHzDfxSik4WCr0FBJVTYfbiVYjdgYfw8pTnv8XsEQ_MVV6M1E7dZRYdlgcSapP8iOA8MVAXVY0mc-6_Yw-qBU7kc3k3wNK2cOaEadl9gwZMgBdr6xJqRb0qOqJB_sFZjDVzQtQdpbmXeWMpN_0q7lhgvAICWGKDs_VHk-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=lNeGOIpKh_sGnG9jicZ0TDr6NInYwk5RSJFYiqrQrraM24igD21VOujbJBW_7pVDaFNrUpBlvs_Du0W7TAxBwDyG-XchXforj90XPGaNMQwGchsFyBVRxx2IQ6H2vmoNp2AqIoZs-KWIjA7MAGGEQO_sl-wgRFGgX8dPF59nJ34UU6ryHzDfxSik4WCr0FBJVTYfbiVYjdgYfw8pTnv8XsEQ_MVV6M1E7dZRYdlgcSapP8iOA8MVAXVY0mc-6_Yw-qBU7kc3k3wNK2cOaEadl9gwZMgBdr6xJqRb0qOqJB_sFZjDVzQtQdpbmXeWMpN_0q7lhgvAICWGKDs_VHk-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79020" target="_blank">📅 17:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇨🇭
‏
الخارجية السويسرية:
اتفاق أميركا وإيران سيوقع في منتجع بورغنتشتوك الجمعة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79019" target="_blank">📅 17:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند:
بالتنسيق والتعاون المشترك مع جهاز الأمن الوطني، نعلن عن تفكيك شبكة منظمة من الشركات المتورطة في إعادة توجيه وبيع سعات الإنترنت المخصصة للأغراض التجارية وغير المنزلية، وتسويقها للمواطنين كاشتراكات منزلية عبر فواتير غير رسمية، طالت أكثر من 10,000 وحدة سكنية.
ونؤكد استكمال كافة الإجراءات القانونية واستحصال الموافقات القضائية اللازمة لإستكمال العملية.
إن هذه العملية تمثل ضبطاً لمجموعة واحدة فقط من ضمن عشرات الشبكات المرصودة التي يجري تفكيكها تتابعاً، وعمدت بعض الشركات المخالفة إلى قطع الخدمة فجأة عن المواطنين لإخفاء معالم مخالفتها ودون أي أوامر إطفاء رسمية من جهتنا.
تُقدّر القيمة المالية المهدورة لجميع عمليات الفوترة غير الشرعية  والتي تزود أكثر من 1.5 مليون ونصف مستخدم، بنحو (200) مليار دينار عراقي سنوياً.
وتتعهد وزارتنا إنه في حال تم استرداد هذه الأموال (أو جزء منها) بتوظيفها مباشرة في :
تقديم خدمات إنترنت مجانية لبعض المؤسسات الخدمية والأماكن الترفيهية
خفض أسعار الاشتراكات الحالية
زيادة سرعة الإنترنت بنسبة 20% لشبكات ( الكيبل الضوئي واللاسلكي) خلال عام 2027</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79018" target="_blank">📅 17:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwQbcWT9Ms6mKFcPulJrHfDUVDVJqSfxj9Wvpg45aoC5-GG46b-8UToxuMFCdYqEYwNrc6BAzIfeOYRZZnzP4YjskNV4NXHdObqPp3mVF86ezSdJa44_rPOZ980QPQDQdFwW7ilVsSYfT_vh8OAckTRIcGEec_De-L5rwKlhebPqUniPiNTSzsbbBeXAsiGseOdguCRPeM4lr39JMfYwPp2wLevI4if35af30yF4UgCJryl3yWfyUGg5v9z06cSkstfcOsNydbJjjTmwAlxTMKGYQ-5czK-VxHJGLIP3_SdqHtU4I-UhF0xQmHS3hTJmP_NFDMg8Pgrk4S69-OXdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
المبعوث الامريكي توم باراك يقول أنه حدد مسار التعاون بين بغداد واربيل خلال لقائه مع مسعود البرزاني ومسرور البرزاني
شنو هذا التدخل الايراني ماله رداد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79017" target="_blank">📅 17:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇹🇷
🌟
تركيا ترفض طلبا عراقيا لتمديد اتفاقية تصدير النفط عبر خط جيهان لمدة عام على الأقل لحين توقيع اتفاق جديد
الجانب التركي يمارس ضغوطاً تفاوضية لرفع معدلات تشغيل خط الأنابيب الذي يمر عبر أراضيها من شمال العراق ليعمل بكامل طاقته الاستيعابية البالغة 1.5 مليون برميل يومياً على ان تكون اتفاقية استراتيجية طويلة الأجل تمتد ما بين 5 إلى 10 سنوات وتتضمن بنوداً إلزامية تفرض على العراق دفع رسوم مالية تعويضية مقابل أي طاقة استيعابية غير مستخدمة أو مهدرة في خط الأنابيب طوال فترة التعاقد
مسؤول تركي يقول انه في حال وصول المفاوضات الحالية إلى طريق مسدود وعجز الطرفين عن صياغة المسودة الجديدة قبل نهاية الشهر المقبل فإن تركيا قد تتجه لمطالبة العراق بوقف تدفقات النفط عبر الأنبوب فوراً</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79016" target="_blank">📅 16:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تواصل فشلها في تنظيم كأس العالم:
اشتباكات عنيفة بين جماهير الجزائر والارجنتين في ميدان التايم سكوير بنيويورك.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79015" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79014">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
إسرائيل طلبت الاطلاع على مذكرة التفاهم مع إيران لكن أميركا رفضت.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79014" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaGQXPpp5_GX6JaZYOSlUS2uqNPdUETIMtWAKdjqbV9uwiFV0NOk3n-i7ZgURmWXGhfLm6yfmfneETor1ALetW4oq6nsaxDpR7KWjHyg2CIfqf7tzH-oJxUMjeJb0kSnYGkv_ffi_YbANFY5OOrSHpxqaxgStHEPzP4rUKlczjH4mW2FnBgWAk2pKkSitKUe6DKP5Y-_5GusdoaAeCQVfcb-pnyQ9fROLA09A-jNFpV25QaS-g8evbwaOSBZ4KiaqZAG8ZbaTJ583rC9k3pqvTXZdF7DyTqebw2XFgJcCgfb3kPxkRE37rq7Z9GjvWGVa4m1RfGAIC97GHB9TnQIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اليمنيين ينتفضون في صنعاء تجاه اساءة ترامب لمكة المكرمة وسط صمت من قبل نظام ال سعود</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79013" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
الكابينت المصغر سيناقش اليوم طلب امريكي بالانسحاب من لبنان لحين توقيع الاتفاق مع ايران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79012" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79011">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79011" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: سأرسل اتفاق إيران إلى الكونغرس لمراجعته.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79010" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: سنناقش اتفاق إيران مع وسائل الإعلام في غضون أيام قليلة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79009" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسالة حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم إلى رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف:
بسم الله الرحمن الرحيم
جناب رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف أيَّدكم المولى ورعاكم.
السلام عليكم ورحمة الله وبركاته
تعجز الكلمات عن تعبيرنا بالشكر الكبير للمواقف القوية والداعمة للبنان وشعبه ومقاومته لإلزام الكيان الإسرائيلي بالوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات بما فيها لبنان، ربطًا بوقف الحرب على الجمهورية الإسلامية الإيرانية، كبندٍ أول وأساس للاتفاق بين إيران وأميركا. فقد حوَّلتم بارقة الأمل الوحيدة والفاعلة في كف يد العدوان الإسرائيلي الأميركي على لبنان إلى حقيقة أثبت للعالم بأنَّ إيران نصيرة الحق والمقاومة والمستضعفين، ولو احتذى طريقها آخرون لما تجبَّرت أميركا وإسرائيل، ولما بقي الاحتلال الصهيوني جاسمًا على أرض فلسطين والقدس.
قلنا دائمًا بأنَّ إيران أعطت حزب الله والمقاومة ولشعب لبنان كلَّ شيء ولم تأخذ منه شيئًا، هي أُعطتنا لخياراتنا، لقوتنا من أجل تحرير أرضنا، لبلسمة جراحات مجتمعنا ومساعدته. والآن تبذل إيران الدم، فتتصدى بقصف الكيان الصهيوني ردًا على قصفه لضاحية بيروت الجنوبية، وتتحمل تبعاته التي تنذر بالحرب عليها مع عظيم التضحيات. سأقولها صادحة: إيران أيقونة العزة والشرف.
أشكركم بإسم حزب الله ومقاومته الإسلامية، بإسم المحبين من الشعب اللبناني الذين يرغبون أن نوصل شكرهم إليكم، بإسم الشهداء وفي مقدمهم سيد شهداء الأمة السيد حسن نصر الله(رض) والجرحى والأسرى، بصفتكم كبير المفاوضين مع فريق عملكم المباشر ومنهم وزير الخارجية الدكتور عباس عراقجي، راجيًا إيصال الشكر والامتنان إلى القائد آية الله السيد مجتبى الخامنئي(دام ظله) الذي غمرنا باهتمامه، وأحيى فينا بركات ورعاية الشهيد الإمام الخامنئي(قده)، ورئيس الجمهورية الدكتور بازكشيان المحب للمقاومة، وحرس الثورة الإسلامية الإيرانية هذه القوة النورانية التي قلبت المعادلة ببأسها، والجيش والنخب وكل الفعليات الرسمية والشعبية.
وأخص بالذكر الشعب الإيراني العظيم لقد رأيناهم في ساحات المدن الإيرانية وسمعنا مطالبهم في بذل مهجهم لإنقاذ المقاومة وشعبها. شكرًا لكم. شكرًا لإيران الوفية. والسلام عليكم ورحمة الله وبركاته.
الأمين العام لحزب الله نعيم قاسم
01 محرم 1448 هـ
16 حزيران
2026</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79008" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب: سأعقد مؤتمرًا صحفيًا حول الاتفاق الإيراني.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79007" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامب: سننشر نص الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79006" target="_blank">📅 16:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇱🇧
الأمين العام لحزب الله سماحة الشيخ نعيم قاسم يلقي كلمة في افتتاح المجلس العاشورائي المركزي يوم غد الاربعاء الساعة 6 مساءً.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79005" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامب: العلاقة الجديدة مع ايران باتت طبيعية وأعتقد أن الأمور ستتقدم بسرعة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79004" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامب: بدأت السفن في العبور عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79003" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79002" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79001" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مكتب التحقيقات الفيدرالي يزعم احباط هجوم بالمسيرات والقناصة على البيت الأبيض</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79000" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
مستشار حكومي عراقي:
عدم إقرار الموازنة لن يؤدي إلى توقف صرف رواتب الموظفين أو المتقاعدين أو مستفيدي الرعاية الاجتماعية، هذه الرواتب تعد من النفقات الأساسية التي تلتزم الدولة بتأمينها بموجب الأطر القانونية والمالية النافذة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78999" target="_blank">📅 15:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHxkZ3dH46p7v8yOxmqOudkAAf194gjFyW_0clVmmjrOqXjTMCWErmYkDIj_fheXAnf0gCxKDGj9CepcJN01T4W646mwrxxEQk0cZWSwTrl-iILZc-thcy1IsI1_ft-Ii-jmb3pfOiTfY1Y5_K3GidyaX83BCc4QKQr8n11qjt0sk11dIHy758LJFvH542dZKtYlh7fnAlpQbbDpQ2ZP2ypt4yJYqjmcpTHg9S0DgIZ8PXffaSzEH4w2Lhsacs1PIG_R6WatiUekLwzFUiOOaq-NCcKdPQhKucgFBcCm2FynHAbN15593RrKORommiyw-UQrakrvC6Zop1UBrI1HXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"سنعيد الامن الى الشمال وسنصنع الامن"</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78998" target="_blank">📅 15:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇹🇷
‏وزير خارجية تركيا: كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/78997" target="_blank">📅 15:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
زيلينسكي:
ترامب منفتح على دعم أوكرانيا بصواريخ للدفاع الجوي.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/78996" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: لو لم أكن موجوداً لما كانت هناك إسرائيل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78995" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇹🇷
‏
وزير خارجية تركيا:
كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78994" target="_blank">📅 14:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رئيس وزراء النرويج يخاطب لاعبي المنتخب النرويجي: "احلموا بأحلام كبيرة، واذهبوا واسحقوا العراق"!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78993" target="_blank">📅 13:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب: إذا لم تستطع إسرائيل إنجاز الأمر في لبنان دون قتل الجميع، فيجب على سوريا أن تقوم بذلك</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78992" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏ترامب: لم يعجبني هجوم إسرائيل على بيروت قبيل توقيع اتفاق إيران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78991" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامب: أنا لست غاضبًا من نتنياهو.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78990" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامب: أقترح على إسرائيل أن تترك سوريا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78989" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب: إذا هاجمت إسرائيل لبنان، فقد يبقى الاتفاق قائمًا.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78988" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: كنا نريد الذهاب إلى إيران للحصول على اليورانيوم المخصب لكن هذا لم يتم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78987" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
ترامب: يجب على روسيا أن تبرم اتفاقًا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78986" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78985" target="_blank">📅 13:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#بالفيديو
⭐️
اندلاع نزاع بين حماية النائب خالد العبيدي وعناصر حماية وكيل وزير الداخلية في مدينة الموصل.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78984" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78983" target="_blank">📅 13:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoHOzLrlJVF4QAGNDRmVrLNaAZ7zKAVfwhgXU8B-zFWNqXvotNtP4MUVko6spiiLLH18ndmJ7C-nbjMDijwCQAYAgdZF_o4mTSjzNhAoSoBbKO9H8FaAV7hn5s6GRRBU6Lalwi2YQiBQdS0zJFNsL5_VJjvS2hAzZH1rO7M6cOph3DiljBPBeee4pvCDwsQVpxSZWpcxJRYNjQYXW1d_Mq_lq29wzKdMP-s0E5xxQK3uYDso0v_70xIPyq1VtxtZLqcEAm1NH-nM47Go_VzhGnYWFcL3ONlGSlNQKc0wLBf9y6I4a3E5amGJnxoD2mlQB_7jiLpzkH7bL-TJ51V3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المبعوث الامريكي توم باراك يبلغ قادة اقليم كردستان العراق أنهم سيسحبون قواتهم من أربيل والاقليم في شهر التاسع من العام الحالي.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78982" target="_blank">📅 12:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euuxFV11RqNWdiKHR3iu4etNHhp3cin99TJHxvZG-jSeDF18CfzyD96ndm5db9Z0kJIFmD4_BT2vUqz2wf5NbptWuTJIRr5yY8xTV_k_oG8uuR1y3-oPl-aXkQRLvuS6IuMI46wZZZAXRPU4A6engG3sXmM7ISpiudnGz01G53uUqdvUtbuzsSDTGHTFz9SRFceEZSJ7c9qQnFXuLP2r-yJgpFy3lam6UTDGFabO3nCi7eLvSM_iy79VIubrBkNBZc5veFlLkiC7b9FPqUXuNwqARk7W7L6KLeEvNaWpwaIZcGiHzbHBExalu15dUH341w70g0zFptoyPXleb-Cufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78981" target="_blank">📅 12:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026 تجمّع لجنود وآليات جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخين نوعيّين.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78980" target="_blank">📅 12:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني: واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78979" target="_blank">📅 12:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78978" target="_blank">📅 12:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=qopE5VceYdb5Dbk9SxXpu2HijpsNESw7z_oN8paCkuoU02UdN6K_MY0alnRIxo6E-H7qu2tdryf594oFH8al_Bjf02_CekwJIZDezBenStWGVFr2cfOQRyZfanq-agRk5tqyQWOqGfdtURqSTT4uqgi189QjhMv6zQ5xpDeOSbHNoZHB0yi6z0iaKIJYkaqm-eZuyGw2sPo9m7epPK8sweaNgvYZG9fJP-N2NdoifGE7hqF_SOoguAQL2h0Zp33S8uUwTvn2nzKRz9eI1NqXGVisZgNdcIQijqLVm_U2u5ncloGRKW9Z4iLtnXgneU3vk9CQiImtO7vlelPuR-KFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=qopE5VceYdb5Dbk9SxXpu2HijpsNESw7z_oN8paCkuoU02UdN6K_MY0alnRIxo6E-H7qu2tdryf594oFH8al_Bjf02_CekwJIZDezBenStWGVFr2cfOQRyZfanq-agRk5tqyQWOqGfdtURqSTT4uqgi189QjhMv6zQ5xpDeOSbHNoZHB0yi6z0iaKIJYkaqm-eZuyGw2sPo9m7epPK8sweaNgvYZG9fJP-N2NdoifGE7hqF_SOoguAQL2h0Zp33S8uUwTvn2nzKRz9eI1NqXGVisZgNdcIQijqLVm_U2u5ncloGRKW9Z4iLtnXgneU3vk9CQiImtO7vlelPuR-KFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78977" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLbUS8PMxU1cJ0kodBD-jJvmORYkY4dO1UEIywl8U27eNuAMi2GHihAMjRi-6Ko32v04VC0O5lvBsDWFebhJGfQQMXZHj8xcn0rRLRblr0S2pk0_UtGY-AiqPLLDGDA3ROxCrAPmEpZ28lyjnFZd91_1lAhsC3JnB-VJCzXwQmfmOQGjlAO8wivddM7Ks_BTJvQ1XyuwMUHG03pQi7dj-xQWynuBpMKSB64BPMLhrftmtztaRva8Gf3kAFuQQnO-CnWLcWgtKg9OZpo0LWRFUME7IwWRn-DO2jkV5oWvq1GoTW-dixC4Qo2_ruTzj3VsLK3oJCSdjxZ99RdslGavdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78976" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من إطلاق صواريخ اعتراضية من مستوطنة المطلة شمال الكيان المحتل لاعتراض صواريخ حزب الله.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78975" target="_blank">📅 11:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات  إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين  جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة  البدء الرسمي…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78974" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات
إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين
جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة
البدء الرسمي لتنفيذ مذكرة التفاهم سيكون يوم الجمعة
نهاية الحرب في لبنان موضوع ملزم لنهاية الحرب مع إيران
سنناقش الملف النووي والعقوبات خلال فترة المفاوضات التي تستمر 60 يوما مع واشنطن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78973" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=qWyZdvKmlpy8qeyw-BIuLgP5ajukC495G4bjqSk6Ye9GU0qYrBZfScvltTPBSDnaxJwkU7l4cFFFb8C_XYyVd-_yKEA061sxwEPNoJJDEO44eqDjR4QXzXtyEkZTpMfFeY-nSpOO0s7_5jDx6bVn6YJxiLIk-uJdZR5hD0KSD8TwAK05kAwLETNI98iUksDcp2PDhwLd8MbuODLz98CbLnLukDV80VFOCfcRNI7ZVzqVjHXjDXpcQMzMm72hsX3aJFyndTg39-BZOvg2CQcmgKGZ-dQWsl6nUIc6j1Jh-q8OjbbUeyx_vKc-IRhxaaWIc6bno8n4lGZNB4kRzcZYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=qWyZdvKmlpy8qeyw-BIuLgP5ajukC495G4bjqSk6Ye9GU0qYrBZfScvltTPBSDnaxJwkU7l4cFFFb8C_XYyVd-_yKEA061sxwEPNoJJDEO44eqDjR4QXzXtyEkZTpMfFeY-nSpOO0s7_5jDx6bVn6YJxiLIk-uJdZR5hD0KSD8TwAK05kAwLETNI98iUksDcp2PDhwLd8MbuODLz98CbLnLukDV80VFOCfcRNI7ZVzqVjHXjDXpcQMzMm72hsX3aJFyndTg39-BZOvg2CQcmgKGZ-dQWsl6nUIc6j1Jh-q8OjbbUeyx_vKc-IRhxaaWIc6bno8n4lGZNB4kRzcZYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇱
الجيش الأمريكي يبدأ بإجلاء طائرات التزود بالوقود المتمركزة في مطار بن غوريون حيث تمثل حوالي 20% من الطائرات المتواجدة حالياً في الكيان.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78972" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📈
بورصة ICE في لندن: ارتفاع أسعار الغاز في أوروبا بنحو 1% لتستقر عند حوالي 512 دولارا لكل ألف متر مكعب</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78971" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78970" target="_blank">📅 09:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة المطلة قرب الحدود مع لبنان متحدثاً عن نتنياهو: إنه منفصل عن الواقع، أدعوه للمجيء إلى هنا لرؤية الدمار عن قرب.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78969" target="_blank">📅 09:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78967">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماهير العراقية تشعل الأجواء في ولاية بوسطن الأمريكية قبل ساعات من بدء المباراة بين منتخبنا الوطني والنرويج.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78967" target="_blank">📅 09:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78966" target="_blank">📅 09:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=MLaKwn55zED4KHMd8W3GhD0sRjPDZ0LFupMS0XqRR4IPcODx46oSCbh1xyzwXIk6JrY74Q6yg4xw9XHlVXyB0Pizkryn08m3EXSkAuniSARsUiwrCjp669cRRDiU-pAo7KvLvniLB_1XUTnzvR6Xy1mCdZWW03ZmTK99sOWe1RRckyfKTVxi6h6YjALkE7J6_M-hi8RMGBOe9Zbe3H7Ha6Zkgd-oS-Y1Y0l7pI3l-GAj8MYQO5SpxYUz_wWVHD_JsbBXlQvOegUgrI1sTZvx1VQ79XQTMD7RWgoiOKNk3Rx0S4fdvRk1Eh13Bi_ah1vq_Yd-Pxft-ew8gJnmglWSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=MLaKwn55zED4KHMd8W3GhD0sRjPDZ0LFupMS0XqRR4IPcODx46oSCbh1xyzwXIk6JrY74Q6yg4xw9XHlVXyB0Pizkryn08m3EXSkAuniSARsUiwrCjp669cRRDiU-pAo7KvLvniLB_1XUTnzvR6Xy1mCdZWW03ZmTK99sOWe1RRckyfKTVxi6h6YjALkE7J6_M-hi8RMGBOe9Zbe3H7Ha6Zkgd-oS-Y1Y0l7pI3l-GAj8MYQO5SpxYUz_wWVHD_JsbBXlQvOegUgrI1sTZvx1VQ79XQTMD7RWgoiOKNk3Rx0S4fdvRk1Eh13Bi_ah1vq_Yd-Pxft-ew8gJnmglWSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فكرة رفع علم الأسد في بطولة كأس العالم كانت حلما لترامب ونتنياهو لكن الأحلام حين تتقاطع مع السياسة غالبا ما تستيقظ على واقع لا يشبهها وها هو علم الجمهورية الإسلامية الإيرانية علم (الله اكبر) يزين ملعب لوس أنجلوس.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78965" target="_blank">📅 05:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78964">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=XhB0NKIH4lcd8EVid2OsvvwoG4zJ36Sm7yX3V2e9VkIG-caxxqHLN0LF23NqbJ0D1jrQWvRE91CaW0D-mDZIiV00xnmBuxO74vLuErL1A5doRmf1RgGgDg-CWyvUZ5kQhvDZC6ClJAZ4RBRaJ6Y3Ih_W3KIcpy0ewB01fib-dRjbHBMfCHO711IY4VUcsD1v9_8qQ9SD0qkdou2atxL_R9aPA13ESKzaDsACz7Y77cCdmr7Ot5WfKPp_s4tW30P6fg7lRCHBL3aSR-UZPRCpPwdxp63-SyyOJjaIsmSs4ThpRfJtSGeqSxM-z6hNj2f17eLKm1ESL32ulx6Q2jdrmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=XhB0NKIH4lcd8EVid2OsvvwoG4zJ36Sm7yX3V2e9VkIG-caxxqHLN0LF23NqbJ0D1jrQWvRE91CaW0D-mDZIiV00xnmBuxO74vLuErL1A5doRmf1RgGgDg-CWyvUZ5kQhvDZC6ClJAZ4RBRaJ6Y3Ih_W3KIcpy0ewB01fib-dRjbHBMfCHO711IY4VUcsD1v9_8qQ9SD0qkdou2atxL_R9aPA13ESKzaDsACz7Y77cCdmr7Ot5WfKPp_s4tW30P6fg7lRCHBL3aSR-UZPRCpPwdxp63-SyyOJjaIsmSs4ThpRfJtSGeqSxM-z6hNj2f17eLKm1ESL32ulx6Q2jdrmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بداية مباراة المنتخب الايراني و المنتخب النيوزلندي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78964" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4th6v1Ik4lf7gfVitP_oaeNHqyk97Bhz7-z_AGvS4-SFlI3a4Bo6z7jpaKV7DYyRCbEO5KHlvsD6SaoQcKackHl_aE95lcyojPAKpdD_YsaFP_tbnpKm-wDRW812SzXAkyeaZuxJIKb9NTbVlGw2wWR3Kz2V63SgF-kxxY28hbKreqmsOMdLUhC1v-akhMHDXnxcnoFuMCyy9TbpBhZxbeGfJdGbId9KfDHVU1bEvC2HetanIOMxX_qSMkXWs1r0j_V0VvmT4bRr2ZkCVe9I6p7G8-_7YIYhNrMOdeJJaz6aqT-QAoO5wUGynZH-S0mVaViiuKdtFTDJ2FAuszAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:وافقت إيران على عدم امتلاك سلاح نووي أبدًا! كما أن قصة دفع الولايات المتحدة 300 مليون دولار لإيران هي أخبار كاذبة، نشرها الديمقراطيون!!!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78963" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئيس المرصد الوطني للإعلام "خالد السراي": أبو آلآء الولائي رجل شجاع ومقاوم والإطار التنسيقي أساء له ولم يدافع عنه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/78962" target="_blank">📅 01:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC5AClBBnvRBANnLFnhDESRXW7Gl8rcMz7LAG1i7eWy4bclWJLKIQoE1GGevgCHRM6EOUD20xdBqsgLVJ3mLVcdCNrew6gWHajB2ocQ7dU1-C9PQCGh35Gas4yWylZ7F4249VQYJ_w-nwV3ExR0lZ8OV86hrJc79p4AVR-fJwyimEU75ZqlLGKBxtRdjnWq6mXviNsAs_gw3PUvj4qbCYRBvlscsUtT9Grz5c5KX-w5fPGfoOZYxfrNb1eWOW2_kTi3uPOrbNckIRVOQZiz6HBeqQZlJ4t5MHjZerBnVN3AxnT3cmxFtFDL5WRBn0yeFSkcnl3avc6NOnWg_1eLSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78961" target="_blank">📅 01:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مصدر امني لنايا
...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة من قبل القوات التركية إضافة إلى تنظيم شراء المواد الغذائية بكميات محددة لكل عائلة!!؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78960" target="_blank">📅 01:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=GKDaceVQmpqtKBQ9xLefIe89XpOGKo1nZfmEkChibWzUr1Jb7t06q0OzNrpePyIHy7I6vvku5t5p_Q68zIY_1Sy0IOzzo8yaVrHdymzCMQy057SYlnPp969i8c6-vYAFy3qvlwNI_B-u4HYrN7eLmHqPHO9kXig3gMxV2XwlhBUxtN1TN_y38PkoIvf5-yQX00-KIJZyUCyhQxhJu_N6BMdn8edIUySVYhQW1bG6UWbcDzLGMZZmVOrDbsFtYRLE4HZjiUnAHEhJhKX2zAR2eKdTrcs5ZblsjjT15klzY2HBce7xjTFRju0VXFCX6j8l1GpXloKO07bP9bmbyPnwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=GKDaceVQmpqtKBQ9xLefIe89XpOGKo1nZfmEkChibWzUr1Jb7t06q0OzNrpePyIHy7I6vvku5t5p_Q68zIY_1Sy0IOzzo8yaVrHdymzCMQy057SYlnPp969i8c6-vYAFy3qvlwNI_B-u4HYrN7eLmHqPHO9kXig3gMxV2XwlhBUxtN1TN_y38PkoIvf5-yQX00-KIJZyUCyhQxhJu_N6BMdn8edIUySVYhQW1bG6UWbcDzLGMZZmVOrDbsFtYRLE4HZjiUnAHEhJhKX2zAR2eKdTrcs5ZblsjjT15klzY2HBce7xjTFRju0VXFCX6j8l1GpXloKO07bP9bmbyPnwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هروبًا من المحسوبية وتدهور الأوضاع المعيشية في إقليم كوردستان العراق،
لجأ شاب كردي إلى ألمانيا لكن رحلته انتهت بالقبض عليه وترحيله إلى بغداد بعدما وقع في اشتباك مع الشرطة الألمانية أثناء اعتقاله</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/78958" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الاعلام الايراني:
تم البدء بتنفيذ رفع الحصار البحري الأمريكي المفروض على إيران، حيث عبرت ثلاث ناقلات نفط وسفينتان تحملان سلعاً إيرانية أساسية "مرتا" عبر الحصار البحري الأمريكي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78957" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQnHZ6zVelCqa1I0bX3Waksr-xE_nXVsuPAcN5le9llTBKhKSZE_tmsTU2C4TrBJ1HFQwQse8NejA3YMyMHBVEoA4Z92IIhYalfYaOUPwWvTIgiWNpSHKmN83o1W2-FwgQSyM1ASN2jklg-wTcFh-CyISAO0I2glLvUJYBDglpsDEQmT9QQAnEXNRfLzaDmxmg8-ZoFme3F9bfW5vGtsZ03Ae1DpOkiSvniaS4TjQ9qB7T43ED-U7LP-Mi9vqemJ2P4sWQ3aS3kD5SDb-Z_lCk-F_cskcYNNdgrp9SA6vRrD6ntUOw2X1GXzbNATm70uH7zgcDc36-6pDssbMsxgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
في ظل تعثر السياسة الخارجية الاميركية واقتراب الانتخابات النصفية للكونغرس لجأ الإعلام الرسمي إلى استخدام البروباغندا لترويج لإنجازات استثنائية لإدارة ترامب رغم أن العديد منها يندرج ضمن المهام الاعتيادية للإدارات المحلية ورؤساء البلديات.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78956" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj0rwz5kBZAIml6E117yMcv-3u27iIIjhSt-dAv7E6cPzcusgIiKLcqw_OR2mc_4k41ZZMPXYbXeU9mQ_4sIerzFdG8ZSZqd4Bd-i-OnFhBlxe4PSfAGFVrqBNqRsopnFJUhgST8_rgu6esEbA7B1B0QRP3O-mflycyqjsauBKC5FnzVKjnJXZwrxJzoxgYnXwavQ5E6ZlIXv_fsECDqm07q_Wu0aCyk0bUExNhzFRUiUDj_XR_LopRrrnXqqr_K51lIXuGGsqWOWWO57bCMz0xY6IueSpo93-xx3L77I01gl5IlFD5X-TA5lTPBniWIwfXEdeu1GBA8VB6DAFKdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الحاج ابو الاء الولائي:
وإنا على العهد باقون وعلى النهج ثابتون(لن نساوم).</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78955" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الطائرة التي سقطت لها قدرة على حمل القنابل والرؤوس النووية   وشاركت بهجمات على المنشاءات النووية الإيرانية …</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78954" target="_blank">📅 23:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
‏عقب تحطم قاذفة B-52 لاسباب مجهولة، أعلنت قاعدة إدواردز الجوية إغلاق المطار وتحويل مسار جميع الطائرات القادمة، كما علّقت جميع تصاريح الزيارة غير التجارية حتى إشعار آخر، لتكريس موارد القاعدة بالكامل لعمليات الاستجابة للطوارئ والتعامل مع تداعيات الحادث.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78953" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKkWkSGqbCM1-_OCw0Dy-d-pIjWr_5LRQHLogEhMT3_0XbQbpX1aSyyBiayM46d4MC-hTCOPARxB57206uxV6EsZZnpdE4xQ4cHYKfMBk0scNS-9k2wUyE-UH1UjfLA1PM2k6eds9VH1hKWvVSHUD9DuyxSqYsHtAnUqwFEu4jf1hz6veVY1U5r06eZKTzSmjQW3NM4ivq1HucYvNX4RrBqlKUpvqG4YrQSs0ZfDxQgtJapn3e2w5kiIqwi_mGuLDSvxW-CTwBVnX94d9rNipwnLf2Z3G9gaKcYY3jp1sLiDaQJyV6ggZNCS6HohkBTvTlAeeEthTicZRCGIrD9DHB2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKkWkSGqbCM1-_OCw0Dy-d-pIjWr_5LRQHLogEhMT3_0XbQbpX1aSyyBiayM46d4MC-hTCOPARxB57206uxV6EsZZnpdE4xQ4cHYKfMBk0scNS-9k2wUyE-UH1UjfLA1PM2k6eds9VH1hKWvVSHUD9DuyxSqYsHtAnUqwFEu4jf1hz6veVY1U5r06eZKTzSmjQW3NM4ivq1HucYvNX4RrBqlKUpvqG4YrQSs0ZfDxQgtJapn3e2w5kiIqwi_mGuLDSvxW-CTwBVnX94d9rNipwnLf2Z3G9gaKcYY3jp1sLiDaQJyV6ggZNCS6HohkBTvTlAeeEthTicZRCGIrD9DHB2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
العراقيون يطلقون وسم #الله_يستر  على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/78952" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رويترز : تحطم طائرة بي-52 ستراتوفورتريس تابعة للقوات الجوية الأمريكية يوم الاثنين بعد فترة قصيرة من إقلاعها من قاعدة إدواردز الجوية في كاليفورنيا، حسبما أفادت القاعدة.  ‏"أرسلت فرق الطوارئ إلى موقع الحادث فوراً والوضع مستمر"، حسبما قالت القاعدة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78951" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=HSWxYmoUlf1F73b6zaqMRsKN6wuNb4GtVhI8ydb1z55psrvso_UWu063U8IcPzwKzTuu6mpI3xiG2i1ycYmnJmo3w91DaSp0iDdNcFr5Uzr9pJgE3yEDEv_DZeAUKXI4VPmaFOb5MOc59Et0c3MRGxpjIARXk_mCZXTLSrasT-QC05qpaetFRe3bJneQC4s6Zgqpe4cDYSIF1u8KglM586XYTjBtfYkbrD0KEsPU4jPre3LtbSvyHP6JmNMu-1XBOOwWGOfMNnmy5XzC_YEvfCan0NUMMm259wzBdvmthPvYRBvtsN5hKQEYUGIAAX8eMedMp2kqBYCDiZrkZWDhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=HSWxYmoUlf1F73b6zaqMRsKN6wuNb4GtVhI8ydb1z55psrvso_UWu063U8IcPzwKzTuu6mpI3xiG2i1ycYmnJmo3w91DaSp0iDdNcFr5Uzr9pJgE3yEDEv_DZeAUKXI4VPmaFOb5MOc59Et0c3MRGxpjIARXk_mCZXTLSrasT-QC05qpaetFRe3bJneQC4s6Zgqpe4cDYSIF1u8KglM586XYTjBtfYkbrD0KEsPU4jPre3LtbSvyHP6JmNMu-1XBOOwWGOfMNnmy5XzC_YEvfCan0NUMMm259wzBdvmthPvYRBvtsN5hKQEYUGIAAX8eMedMp2kqBYCDiZrkZWDhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تقتحم مدينة تدمر بريف حمص السورية وتقتل عدد من الشبان وتحرق ممتلكاتهم تحت عنوان الشبيحة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78949" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVMU1TbtHzPCR-KaU_OCqJIOI-uhhlXJLKLHW7dhH3O5gdJ4dfBbVr2FIvC6NDXJ7_kxWVJwZCr2JW_3UoI3c-GhZtytNMMMVGuzwmVHJoVSdIA_6wH31yzJS1GOTXb-HApFPnCu-GE1oYufCL_Qz1Xnoz3t8uT1C2y0jmOP306jYysUXVqYU-dQ94x_95hzNHLw4blliLzF8US-hHMyW_yTxIEFAvjMqd2OO-v9humL_goFvbhR-UhWL_BdoB_jTGdErbyjZb_lYIYOQeLZ39PM7wIIKYNFeb58VkaUeg7e9U0qTgclmACq9AcKgY3zM6R7GsEUaF240xOWmBqrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
العراقيون يطلقون وسم
#الله_يستر
على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78948" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=u6IXo32dokccPsVYCXAwteP49Gw2e5NrIzAZ07D9vX_iq6RPgw8O2nGmVLxTrKXjWUf7eXv044LhPzWl4UfTP78m6PDd2qLOeXYvx4tgOG8rBxwBJKkY83mPfyavq6f86Qtrvq5L4hh0uUbqTHpa7H50v0SOUzRK3C9yQBiVl-g64fqvZs3bRiFVKvq-pPVZU06SOGc7SSXQ7pT0cDlCdb6ZQUaKJ8fY0qsdDiw1nl_bUdkdJ5-3x9Mmve5hLKkE1JNCPmtpx_HDql8QY6cqCyAn8Vwv2hCGylvYFlNdsBIAAdB9K2Xmv_OSouiykEhvjYFjHgiTWltSDXUH9Ke1RTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=u6IXo32dokccPsVYCXAwteP49Gw2e5NrIzAZ07D9vX_iq6RPgw8O2nGmVLxTrKXjWUf7eXv044LhPzWl4UfTP78m6PDd2qLOeXYvx4tgOG8rBxwBJKkY83mPfyavq6f86Qtrvq5L4hh0uUbqTHpa7H50v0SOUzRK3C9yQBiVl-g64fqvZs3bRiFVKvq-pPVZU06SOGc7SSXQ7pT0cDlCdb6ZQUaKJ8fY0qsdDiw1nl_bUdkdJ5-3x9Mmve5hLKkE1JNCPmtpx_HDql8QY6cqCyAn8Vwv2hCGylvYFlNdsBIAAdB9K2Xmv_OSouiykEhvjYFjHgiTWltSDXUH9Ke1RTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78947" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78946" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGmZyUNZstuibGDGz_NRPYu_ct8gwVoLo9n5h9zBwaqSkZz5G01ib5HeJMHGtGGUSCK78vgqN-ayq7HZdQ77U-iUO8qtksQBRow5-vxVvgC879alVPdF6UMYu9O6oJ8AaXlBLfpVoJpLR4KGIYpl6SRoDGIp5bpOo--r8qy6LT4UW8UhZy1IJIv-ucv3Tr_PvOLrJtJDR8xdC_k8sJVU224DSSL_RqurV76LUOyidpn-KYe5wUOGQm39hHnfj18TSYz0bXW_K4kbwA4T6nnD-m_56KhE1ZzP3945BQ1owpvtqdXDLdAfxmL-9mWL-Ks2qruqX98scxdtPLqOIHBYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=NbLfVWzvzd3uX0gd0-GFeb-KpQpInLSSIRsyGFTYPpaJEBvCbz81UbbKUdVj40udfJdQzmIb_T__MODm77gCX-8IgUBuL5pASgtKHITOhVOyn0NcCMClQO9OUU0Q75SzSf6Gg2iB2KqEq8NVUrZcMzOXCWVhzZGZg_nv_YWBYFESzaCEPHa13SdwV6VCu4juvl7czmFzXZgSWG0h5LkGhVRg8bMKm2OhTaXiLzcu4xDGqv_dGP3A6wVpxdmDGSKVL4s1cPn1jHlM2vc_GQCL9acR30T41evjr9bROy7M6LjBlN5ngGQ7tcm-eaEhJkTatf1-HEzkeZAyITqufqMjBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=NbLfVWzvzd3uX0gd0-GFeb-KpQpInLSSIRsyGFTYPpaJEBvCbz81UbbKUdVj40udfJdQzmIb_T__MODm77gCX-8IgUBuL5pASgtKHITOhVOyn0NcCMClQO9OUU0Q75SzSf6Gg2iB2KqEq8NVUrZcMzOXCWVhzZGZg_nv_YWBYFESzaCEPHa13SdwV6VCu4juvl7czmFzXZgSWG0h5LkGhVRg8bMKm2OhTaXiLzcu4xDGqv_dGP3A6wVpxdmDGSKVL4s1cPn1jHlM2vc_GQCL9acR30T41evjr9bROy7M6LjBlN5ngGQ7tcm-eaEhJkTatf1-HEzkeZAyITqufqMjBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حطام طائرة B-52 في ولاية كاليفورنيا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78944" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlLB9rccyaUO2l3ztJeQwV2Koggz2b6CvmJ40ps7EDcruabLRuyB1E-jh6iyluz7h2R5EBmseGG60dkBKziSsBoTY8kf3PLYRfZlTJRtkpvrQYSJXwhj05qEkdN2FEOAWjpDDZyY4YwVpRb6sJkPMtZHTPr7ksi0t5QlwXlRXgEGgGZlvEpnMNMW7d4ufdjwll1HgZI4QwmOLLXHXIZ0yd32eBO438DUoFVvtpgUGWVpvI0Ldyn4ABuoS5Zp2uvzKp-KJFggAaTc4ieldiBNy5FiOVuAykHikW0fXaMgRaWtCL2b5C29k-6z2m4A9pG19Khj1T64_c6Jf58TqqUZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
طائرة قاصفة شاركت بقصف ايران من طراز B52 تسقط في امريكا !!!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78943" target="_blank">📅 22:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unQEzZGnpCj_Tk7Fl1t_vVZcLWZnhW5Q54TECqWwmOecar5ZyMNCMiUJ2W_AD2PQRF31nm7zi2ZQ5j8vbtxu548dglpMXouAv-9RBuOyCktGFNgqSKRh4GkLOc-VVHdUdbuSxTj8jFD-YUsl_5RPterr-VUxMYQXOHJuEHOsBI_L_l4-8e_VcGDQuR9lAJmt1lLtrE2w94K48y-j3qNDetsWAi-aZOyO7kXVOgiV9gNrKW9X_klquPlK5PlpS63myvwtmnAMlBqKCph-jk_LoZXkZvzk_weIADI-J1BdG7FBFeLIrX6iZkhn6WwccHUCNqKh2PdspL5otMtRyCUWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78942" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78941" target="_blank">📅 22:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">إغلاق مدخل العتبة العسكرية في محافظة سامراء !</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78940" target="_blank">📅 22:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مالك تطبيق تلغرام :
تريد حكومة المملكة المتحدة حظر وسائل التواصل الاجتماعي للأطفال دون سن 16 عامًا. بموجب القانون الجديد، سيتعين على جميع مستخدمي وسائل التواصل الاجتماعي في المملكة المتحدة "إثبات" أنهم فوق سن 16 — باستخدام بطاقة هوية أو مسح للوجه أو بطاقة مصرفية. يتم اعتقال الآلاف في المملكة المتحدة بالفعل بسبب منشورات سياسية كل عام.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78939" target="_blank">📅 22:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78938" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78937" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !
السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !
ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78936" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=DGjfj3_SNpvgia4nswth-xmv2WrJynAwfAqa2PT4IxexpHAJFc2ZuykwDu8mJOhY__D_GWIeLz0BjWej7JEh3In9xvAvH88XG8rOnHrRs-w0wAdUjMLiwt7aAMFCntEAaYQ0S8WAwnx7nN-6r5SNE82gRt3kvVC6WdsnJhJ2OZWaulV_uxaRT5YCUpDgLsM08nPwu9pYV1h0GWYci0fcAUltEJdm_JKceTRrz3zjQH2JMDGMtuYaUQZ1TV20-NvvKGj89d2wTKoAbYYRFDOVZRPATwUUut5KnouSwnsEiXSV7h3BYPmzzzXHZjE_QKVlie3KAEZEZ3xS1M1TzkAzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=DGjfj3_SNpvgia4nswth-xmv2WrJynAwfAqa2PT4IxexpHAJFc2ZuykwDu8mJOhY__D_GWIeLz0BjWej7JEh3In9xvAvH88XG8rOnHrRs-w0wAdUjMLiwt7aAMFCntEAaYQ0S8WAwnx7nN-6r5SNE82gRt3kvVC6WdsnJhJ2OZWaulV_uxaRT5YCUpDgLsM08nPwu9pYV1h0GWYci0fcAUltEJdm_JKceTRrz3zjQH2JMDGMtuYaUQZ1TV20-NvvKGj89d2wTKoAbYYRFDOVZRPATwUUut5KnouSwnsEiXSV7h3BYPmzzzXHZjE_QKVlie3KAEZEZ3xS1M1TzkAzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78935" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Xq3KTf0wKqBIxyXsgQ_AiNozD6gY-8N1qwVLn5iyz8a3S4aMUMb03XOAsvdp3rh5E6W97XiUyAMQFBBjh_3aQDUWe0PHvWgKzUAjQ8IVYr2FICVaE_bidDnOKx0OIH9F9obyOjxNc0JhJz9x7Btw1zolPkBuNdSFr-vA_lYJMStCl4JIYfnh1N-7dLKsB3DF-PR9bIBAdzYf_GsmvGPOX6d4KT7EEJZwwWViSOcvNogf_p0Job0SjmDwrgIkYNv9YHejPznEJIdquS89H1yOuEyDlEMwJ9jlggAMjbxq2HO5s_h6HIwEt0gtQoDY5mErAZqJSudZrvTn_NRfE4jaaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Xq3KTf0wKqBIxyXsgQ_AiNozD6gY-8N1qwVLn5iyz8a3S4aMUMb03XOAsvdp3rh5E6W97XiUyAMQFBBjh_3aQDUWe0PHvWgKzUAjQ8IVYr2FICVaE_bidDnOKx0OIH9F9obyOjxNc0JhJz9x7Btw1zolPkBuNdSFr-vA_lYJMStCl4JIYfnh1N-7dLKsB3DF-PR9bIBAdzYf_GsmvGPOX6d4KT7EEJZwwWViSOcvNogf_p0Job0SjmDwrgIkYNv9YHejPznEJIdquS89H1yOuEyDlEMwJ9jlggAMjbxq2HO5s_h6HIwEt0gtQoDY5mErAZqJSudZrvTn_NRfE4jaaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: ترامب رئيس الولايات المتحدة، أنا رئيس وزراء إسرائيل - أنا أدافع عن مصالحنا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78934" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
