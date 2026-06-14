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
<img src="https://cdn4.telesco.pe/file/MMkYbnMLq7bT3oAyC2ulmqpnP0UQ-w3lSepGhuGfhaYbiguWcpz6nso0jyQ32wMxS9HR4es87sDHn4OHV0_l4pPuEY2kPbHg9AP-yAFnCkaKVdrPd_AlPdN9v4Qi2DABJPISugjMw3-_ePqFvDOs5UNfsdOSYbw-4YdKIjyiBow7EEY04V0vACTgH1GemSzFg52OB5QS8bhmaqv3iDPlHPJtxj6_tGCrzCbHgH5i1HcYZpOcN99GG3SbJCWQF6_bJpiqU9XxEBbxJMpJR4Wd4hFXafSsIkw7FDp-82Hf1HyUCzvCg_TpD1XY4X-cynzdTDNn0sN2CQ_Tx2H6U_LAJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 05:10:33</div>
<hr>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚠️
🇮🇶
سقوط طائرة مسيرة مجهولة العائدية على منزل مواطن بحي الإعلام غرب العاصمة بغداد .</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/78660" target="_blank">📅 03:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚠️
🇮🇶
اشتباكات عنيفة في أطراف ناحية البشير جنوب محافظة كركوك العراقية بين عصابات داعش وقوات جهاز مكافحة الارهاب ..</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/naya_foriraq/78659" target="_blank">📅 03:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgXcQ8sUvpLcL626aUMP5hRTqfsZ_WzIBi8pE2Cj1I55G8gXZyp3moKC5NePDmEH1wkKBMpo_956CQY_1SuW8-aJYmvAuhLyUfx2G2b_7Se24dF_bjIXc4bPOTMKCbZ3cG6iCcGkqEedipRHYxF807cjOlKgq0JOmogO9oI3aE8R3pjapC5VkZETe6h56x9UvOHJ9vVmuX2ci_6lFToQgJMR-X6B5s47-Dm-3m3XS75oPWRKD3m6-ClzS2Smb4-0D43ZAzd-WIj_rO7Tv5xTvm9qio-vgWKtfnUU17Zd5W3IVqTU3Ebhm60CEQjzwQN9yRvcywWSOzXclZE6jN4m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في الوقت الذي لا يملك فيه المواطن الكوردي مسكناً يؤويه، يمتلك حكامه عقارات في واشنطن.
دولة جورجيا مستأجرين مبنى في العاصمة الأمريكية واشنطن لتكون سفارتهم في أمريكا
وبحسب احد الوكالات الكوردية مبنى السفارة هي ملك ل منصور مسعود بارزاني.. ومنصور أهدى المبنى بشكل تطوعي سنه كامله مجاناً للسفارة.
عائلة البارزاني الحاكمة في إقليم كوردستان العراق تحاول بشتى الطرق تحسين صورتها وبناء علاقات دوليه لمصالحهم الشخصية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/78658" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxbJbmolZDznao-g1UzLo7gZ0XVcdpDG5hhMH0VMjZeu1xb5QpQV85ehik3XtQRtS63vQVijKiI9rzWjG-127jDuM86TncHXZSjC8Sc8gEwoC71QBj-ASfhN8YyLkitY21mDtuUqJXsKzLOJRAxhnXxRrjjPCgWy7admKE55K6aoFtSS3xvRfIx4YmpbdPsMPA4ykyrSlZ7wltSMr1DW9IHPMH11_9jiDbntnwalMzb57hqByslHZG0F9Z7nQl1KDSi1Bai3dutxmUpew5942fcjG-XlXTuPZGkyu6EN0QeLNclpnXBArLNaclFOOoE3tJTKcZc0GH3IXE82-dSvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات مصطفى سند
: قرارات جريئة خلال أسبوعين شملت إلغاء مشروع السكك، وإلغاء مشروع تطوير مطار بغداد، وسحب يد مدير الموانئ وإحالته إلى التقاعد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78657" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2214529b91.mp4?token=uZvolXBWu6nl2f-3JRC7Hp1uLVv1qO6poGBLImlzmvSL8VHq6O5hD465HwoVIRZjL3pDRblmnhvTJkH9V3EsZ41wos93UaRYOZ1qR9IoeFbw08l4gfLP1DZQ6Q-JiYzJUQFlDIgD2zfXyPiZhZDfuX8nlIlB5pIr5LD5TQuaSWwGa5iRDDbz4s7tFLpfKKB8wO8VN-RVzLgx0vSniZ_d28_MlB6xWibK-sp2jnNWYmxpLpctLdy8orWKOydAjP7DOzKZez5bmiN3mFjyG_ouqaojbYregfsmWa0u1ZYxyrDT_K2Z7qXAGzWzzQF9th-O2-IYvMXJH57eJ2fzlX7VKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2214529b91.mp4?token=uZvolXBWu6nl2f-3JRC7Hp1uLVv1qO6poGBLImlzmvSL8VHq6O5hD465HwoVIRZjL3pDRblmnhvTJkH9V3EsZ41wos93UaRYOZ1qR9IoeFbw08l4gfLP1DZQ6Q-JiYzJUQFlDIgD2zfXyPiZhZDfuX8nlIlB5pIr5LD5TQuaSWwGa5iRDDbz4s7tFLpfKKB8wO8VN-RVzLgx0vSniZ_d28_MlB6xWibK-sp2jnNWYmxpLpctLdy8orWKOydAjP7DOzKZez5bmiN3mFjyG_ouqaojbYregfsmWa0u1ZYxyrDT_K2Z7qXAGzWzzQF9th-O2-IYvMXJH57eJ2fzlX7VKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
من مستوطنة المطلة قبل قليل اثناء رشقها بصواريخ حزب الله وتفعيل الدفاعات الجوية للعدو.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78656" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78655" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78654" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOXp5FswvOYVjvVtgKyYfsR0nTGVHuEl-toDkuz_wGakBtGbFnuPjQcV2RnwvzheAsLRZ1L71-Dw1hlQa_Bj6hioeKuW53zTv9bGSM6wE5eVTwFjXMWuMI_uJbypdAlLLFldsi7VfmigIJ1pnkFYJ9kG_PrdVPPBNq9WVAAq71q9Rky7j3nSruxOaA7CMt_2tiBIJ8IccJa1Zq4mA4Ci7J9I7b6WiO_KQ8SjYq-_BnSEd1BDYk17F8eypJyyzyzlbJwn-YX-eVa17MLe2TWyYFk1YP9bKA0C6w9P3fpnLrjkbILnzBLPfoNH7wWu0NQcZMhS0u-ExwMrM8bSAg8ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات يعلن عن توفير ٥ شاشات عملاقة لبث مباريات المنتخب الوطني العراقي في كاس العالم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78653" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية تنفي المزاعم بشأن تورط دبلوماسيين أو أفراد من عائلاتهم في قضية الدفاتر الامتحانية التي ضُبطت أثناء محاولة تهريبها عبر مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78652" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaa1f4ac3.mp4?token=QBfhNMgqIvex3OszRSgeJJPaqtyZ-_xOpsSO3Q8TcDeDmP86Ynfv-G5TKS_xm_SOnor07slcMt2iiAzq4yy9hhQh0K90HMAQY64SG_5G1Cvj16kiuWJntTmqiZljpZJ_Oz9NWLkJHBFA4iEtEfHyNiTf1NSdsIayFHGXJaN5pwliou89qPEH_tJX5Rzr41KHbQGy6Q9goRYE-fW6GSUZViXx4f6BeCPg33vn0lw13JP1et0vOZJyZfcBzpEIG2u-AB10KBS3HXg8BN_rS8pyNGtkgLCYU3brDvfYndmgVt8VkEeJrsXyjqdM969E89G1zuC6xNLaw60xd0e76b4glnDiOGUjhu-E5GkY0eCg2Bpnn3vpY-As77Rr3DrKv4qfi0WyRbnueM_y5_zH4KU2A10AirwQiiPV-7Adm6XA5yge0peamL5nGttKM0CInB60LnOY6Ey6z5Qg-6NBc8ajVGPIL2u6Ju59wWYK3WFPwPMUrPC1tS3KfTzkA5v1OoYfaUZMxXm_BiS1VZMyKP7JpanC8eiEqOzdpJ9zovgaDJdkQLt5t6ZF7iQjbnpLVPm9lR0p7jvhSn48FoMtO0lI4eUzJf0ICCKtMCUyPOArR1P2QcMO49-B3e3zhhZVdchwygmfCJerBpQHTiHfxUDHUWzqmiS9VFG_UClOGHmOT6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaa1f4ac3.mp4?token=QBfhNMgqIvex3OszRSgeJJPaqtyZ-_xOpsSO3Q8TcDeDmP86Ynfv-G5TKS_xm_SOnor07slcMt2iiAzq4yy9hhQh0K90HMAQY64SG_5G1Cvj16kiuWJntTmqiZljpZJ_Oz9NWLkJHBFA4iEtEfHyNiTf1NSdsIayFHGXJaN5pwliou89qPEH_tJX5Rzr41KHbQGy6Q9goRYE-fW6GSUZViXx4f6BeCPg33vn0lw13JP1et0vOZJyZfcBzpEIG2u-AB10KBS3HXg8BN_rS8pyNGtkgLCYU3brDvfYndmgVt8VkEeJrsXyjqdM969E89G1zuC6xNLaw60xd0e76b4glnDiOGUjhu-E5GkY0eCg2Bpnn3vpY-As77Rr3DrKv4qfi0WyRbnueM_y5_zH4KU2A10AirwQiiPV-7Adm6XA5yge0peamL5nGttKM0CInB60LnOY6Ey6z5Qg-6NBc8ajVGPIL2u6Ju59wWYK3WFPwPMUrPC1tS3KfTzkA5v1OoYfaUZMxXm_BiS1VZMyKP7JpanC8eiEqOzdpJ9zovgaDJdkQLt5t6ZF7iQjbnpLVPm9lR0p7jvhSn48FoMtO0lI4eUzJf0ICCKtMCUyPOArR1P2QcMO49-B3e3zhhZVdchwygmfCJerBpQHTiHfxUDHUWzqmiS9VFG_UClOGHmOT6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف تجمع لجنود وآليات جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78651" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfi5CDJCQT0GCtwEZGrkVX_YEX8JMlE2sLzmBwxmyeMjJBQEqOUcATA3lZ13k-Y3HjPGvQAHfrRipghdv0SCASmRzZwKAmq5iZFR9ndtbMZ6zb1hphHImUuWoBn-bWNPM8HBfuKXwgWyuK4YdyMYxTqWVDD4Kjyz4JbFVUEC2wyZLi9HedeHafSABpNUkCMMEmP2sXdQAuTlXMiB9OVCCxEZMu7-yQG6PP_7ItTbbY1VCBqN_NeEbC_YfqZuLxp7og-p1U5IcXbGQV1TMgOm5-WUpAMQJO8mxfGjJGE6MBq-KzTN80zzyiAV1xKhue17eKYyur4rHDcFzlq1u_y97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZFHYjfA6u8_OkbSz0v3_R7xp4QQPaG2Q8psPgF-h-X1gghNuU3E6DAVGzWpIFvvKkjffcN1UWutEKQvZs2DShCdxCp2vb7YCNLY1xGYWF3VMcD0aeT_8MSe1eHPpAg1X5eWCzGrjn9CItKpKE8WE4NpAc7QZizEskgC-EbLTE4xZAWgWoj8evZovMRwAbCg0WBnYVrH37VcXvuMsPG3aO-IWB63m9uBgk96kckRN-03jOi7e65HRxcGomH9ER9WTx5pXG3zcS26vEnJoR_leBimHIuwFlDKWH_bc4BEb5I0H87z2PubPeCK5R4ORUOJ3xNS25RSjXU1xfR_ZH4y8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🌟
اشتباكات مسلحة عنيفة بين قوات حزب الله المنصورة وقوات العدو الصهيوني عند اطراف بلدة المجدل.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78649" target="_blank">📅 23:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdqRm0nK1qKigpT4CORanoGYLr3xXsVP9OR6jdDW9DjD3T1KdCX0cgR5i4FUmxpWv_xahmeCrShgGu1J7cbPPwmF0H8YdseRww9_YjB1ezjd5cYX-hTlQt2rh5CpKI3w1jnB0vww5aUotFwKnj11D2yVrLfxdXV0UKEW75Y5Ik6Wvs2MLWLIJ6UAVCUYtdAJxGIyAB7aS6okrBtXs3twZ9t0j52AR7idNLS26EH6zcJZMZvn4pteQ3nY0bgqwu9qqQ4q93XkUQfNZwylZ66R18okin_W5igo8yWdHibcZkLhadNaiEE_OfOfNhdj3B_DZhiG_7OZ9_U9O823UCSbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954d8042fd.mp4?token=BuugGdD940pOoOHacUsd3x6KiXhbf_Z__V2B_Iz1wJ2K7t9yeIPyxwbji4-QX7ZMQn6TaeRcC6CXpXmf_P8IhMQTPyhyVyQvnQCLPtdQdq1TsxjIeWAUvTKsngB5ylaDLKvwFYULSSCyO-HCW-ZgO56AuYldQgfsBSVdbwMVdcg3VqEVnZhSzxzv4VzMtaMJbCZrB7yMSDpITww-TQ9cBDO9lmmQknB3Y0yEcmgNLZ47bnPwJjwOmz8r7omrboNuVBQTCXvZTep_8zyfUsu8MsD7azzD0YYisvh-ptmDgWdJ4C0Qba7g6ePJESrUqppIfycX-ZVFzDzUEn79d00UWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954d8042fd.mp4?token=BuugGdD940pOoOHacUsd3x6KiXhbf_Z__V2B_Iz1wJ2K7t9yeIPyxwbji4-QX7ZMQn6TaeRcC6CXpXmf_P8IhMQTPyhyVyQvnQCLPtdQdq1TsxjIeWAUvTKsngB5ylaDLKvwFYULSSCyO-HCW-ZgO56AuYldQgfsBSVdbwMVdcg3VqEVnZhSzxzv4VzMtaMJbCZrB7yMSDpITww-TQ9cBDO9lmmQknB3Y0yEcmgNLZ47bnPwJjwOmz8r7omrboNuVBQTCXvZTep_8zyfUsu8MsD7azzD0YYisvh-ptmDgWdJ4C0Qba7g6ePJESrUqppIfycX-ZVFzDzUEn79d00UWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف آلية تابعة لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان واعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78647" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbcbaedf.mp4?token=QVDc528V8lmQHBbIpt_QuJkSNrg-EWhTBXflW5cmsaztw7hk9I9Fb2FrhqS8_yO1aQrDigktQ1dYL3LpmWXOgswYSY-59GuT_q6TrwZkbVnRGI7Fao6RcoHC4pk7GfS98IsVKv9OKBpOFCImTmnoLJVrhSynZe8JFg9KGm-6VcW5_jLKs6gjt8t4BMjZ_WlZbop8kxqUkpz-EZkFah6mkV42kTCVftTwyRcQxzb7c2xTKmqAs6r21uxqAAHldp2HwCTs-9gZjbv000dPZb5rihNGmrnXV8GpRzZwm2p7XCJ46LT-UtX0Dq8uVVYkLnpevUkk3T6qin4_nDMe8iYddVoyJg6Sa9pUF9qReI4_Q1X1qmbwGTpMVygHSdHRYjsOxZ3Nivg8aJ5MLUbfo0B662im0kupY5dj5G2nlxdPwr95Cln9b9TjvJ8iXmGR0195nVOxBCpWpu7Su3CPCuHkBQW2VSb3A7YLgDaPoalwGkNquObAr3iifwHXL-AcoOazTAeTIHxqfOk7ng3C-OigE3SpQQ5YhPZdJRgFYkm2fy5UxHqVq-82H6rkHA4IxN6Zmm-sAf3538Ds6uXCw9FLaJtQkJIZA7vTCEN7MRrRDM7yZj19PPvyaEcLiIBDLWsPGd3mCjx3Ia5sKJNFEEJIzMk1cr8IeA7j40w8rgRxeU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbcbaedf.mp4?token=QVDc528V8lmQHBbIpt_QuJkSNrg-EWhTBXflW5cmsaztw7hk9I9Fb2FrhqS8_yO1aQrDigktQ1dYL3LpmWXOgswYSY-59GuT_q6TrwZkbVnRGI7Fao6RcoHC4pk7GfS98IsVKv9OKBpOFCImTmnoLJVrhSynZe8JFg9KGm-6VcW5_jLKs6gjt8t4BMjZ_WlZbop8kxqUkpz-EZkFah6mkV42kTCVftTwyRcQxzb7c2xTKmqAs6r21uxqAAHldp2HwCTs-9gZjbv000dPZb5rihNGmrnXV8GpRzZwm2p7XCJ46LT-UtX0Dq8uVVYkLnpevUkk3T6qin4_nDMe8iYddVoyJg6Sa9pUF9qReI4_Q1X1qmbwGTpMVygHSdHRYjsOxZ3Nivg8aJ5MLUbfo0B662im0kupY5dj5G2nlxdPwr95Cln9b9TjvJ8iXmGR0195nVOxBCpWpu7Su3CPCuHkBQW2VSb3A7YLgDaPoalwGkNquObAr3iifwHXL-AcoOazTAeTIHxqfOk7ng3C-OigE3SpQQ5YhPZdJRgFYkm2fy5UxHqVq-82H6rkHA4IxN6Zmm-sAf3538Ds6uXCw9FLaJtQkJIZA7vTCEN7MRrRDM7yZj19PPvyaEcLiIBDLWsPGd3mCjx3Ia5sKJNFEEJIzMk1cr8IeA7j40w8rgRxeU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف
آلية
نميرا قيادية تابعة لجيش العدو
الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78646" target="_blank">📅 23:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
اعلام العدو:
في قلب الجدل الآن: ما معنى الاتفاق بين الولايات المتحدة وإيران بشأن لبنان
الإيرانيون يطالبون بالانسحاب الكامل الذي بالطبع لن يحدث
هناك خمسة مواقع للجيش الإسرائيلي في لبنان كانت موجودة في يوم بدء زئير الأسد
تقدم الجيش الإسرائيلي إلى الخط الأصفر في وقف إطلاق النار في أبريل
ومنذ ذلك الحين تقدم بشكل ملحوظ أكثر
إسرائيل ترفض أي انسحاب
الولايات المتحدة ترغب في انسحاب إلى الخط الأصفر
إسرائيل ترفض</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78645" target="_blank">📅 22:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
‏
سموتريتش
: مقابل كل إطلاق نار على شمال إسرائيل يجب هدم 10 مبان في ضاحية بيروت.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78644" target="_blank">📅 22:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKqzoTo-wKfEbvv7YnRC_FDZNkTBq_8fitP0oLBT2d-hfwrwePa2a2u2QQTfVjqpimUAFwERZWZP8OqQlpvARSLD0uAAaqWO-wkQ-8BS65NpMYIzBkcyk-zffWPp8tayl0aEhRSFgJGCKbA3e4htfwWSLMX53D1qR8HxyU3ZsBB2vYo22B4SioVun-y4X01JnRcoVnMhvdFRvOFlBSRKvxqw74KGCeYxvA-ai8njPNyTYTyWTZttlGK-m6xlyqy-zEzMhNCS6lnVQ-KqHT3stHGMgSMMpGgjvsQNrluzH3pDwcTA0vOS7C5LfzP6JdPUNuPTsp66p8uB-8CKkZA-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي خلال ملتقى الحوار: الفتوى إلهام رباني والحشد مشروع مرجعية يجب إبعاده عن الهيمنة الحزبية
- فتوى الجهاد الكفائي إلهام رباني لمرجعية شجاعة، تبلورت فيها رؤية واضحة للمستقبل، صنعت من المأساة أمناً، ومن العسر يسراً، ومن التمزيق تلاحماً ونصراً.
- داعش مشروع صهيوني، وجسدت بما ارتكبته من مجازر في سبايكر وغيرها الوجه الأسود للطغاة كهتلر ونتنياهو وصدام والبعث، ولمدرسة القتل والشوفينية والإرهاب.
- لقد حقق الحشد بتضحياته وشجاعته وقوة إيمانه في غضون ثلاث سنوات انتصارات وإنجازات تدرس الآن في الخارج بعد ان ظن العالم ان المعركة قد تمتد سنوات طوال جداً.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78643" target="_blank">📅 22:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف آليات تابعة لجيش العدو الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78642" target="_blank">📅 22:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d51d4374c.mp4?token=R-wM0Bl1HQQCO_MkVLTxpYFoc_uOCsUVVdNCFqYutSPKyJcunVLxc3x8IQBRgOT7ShkgLdZRTqyEt8e3eHYwnGM_dsMX3gRRN1X0ZhIrxp3olwN53CW-K9COR2x5H3_t5Z2HAPC0pswwtjNXHDPgcWPslxbugAxparqkQl95XVs-znyl5QZyEqEHpnXw07kBbqKCDaD1iZBuKRvtxqvj_2uhWZMatpuX0Q1SRV1ReFXBt3A9_277fCCCCZef6k7_p3MgK5ZHliGseXrlI-dmhE1-fW-8nxVyjsNrTiZfgWmypEwLv7Rkg_lnGXz5_hEfBYDKyItxD3tnaL0OqRbSCk4146-p0MmBllBIpdCQVPjtk5CrU6TVczBhX8xLqmmlNwzRcbsezg9uO2A3jIYdVxbxiqbA3EuaZSr4jdz2pY-0FdNjipIwvi8c8IS4cAY6jiXoHDywOYDjFD421rUrkp0nieUweq6uatf2AYGc5H2EGndESRlIQYAAeFfSTZV6GxUcvDyY1VWY1rz20tW0jtGqRZFIvpnlRYaLcHkTDjar5nc96O7iUKnSzS-y5fSmQQeg09I6tPCqWSE-pGu-SCLVjubTZzlQR4s_aC39KfyzIkEJwMlfn64zuyPryTXQlB7SYtmf2KC11V6a9oVzMm8mKyKtDiMwRmJ3NxQSk2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d51d4374c.mp4?token=R-wM0Bl1HQQCO_MkVLTxpYFoc_uOCsUVVdNCFqYutSPKyJcunVLxc3x8IQBRgOT7ShkgLdZRTqyEt8e3eHYwnGM_dsMX3gRRN1X0ZhIrxp3olwN53CW-K9COR2x5H3_t5Z2HAPC0pswwtjNXHDPgcWPslxbugAxparqkQl95XVs-znyl5QZyEqEHpnXw07kBbqKCDaD1iZBuKRvtxqvj_2uhWZMatpuX0Q1SRV1ReFXBt3A9_277fCCCCZef6k7_p3MgK5ZHliGseXrlI-dmhE1-fW-8nxVyjsNrTiZfgWmypEwLv7Rkg_lnGXz5_hEfBYDKyItxD3tnaL0OqRbSCk4146-p0MmBllBIpdCQVPjtk5CrU6TVczBhX8xLqmmlNwzRcbsezg9uO2A3jIYdVxbxiqbA3EuaZSr4jdz2pY-0FdNjipIwvi8c8IS4cAY6jiXoHDywOYDjFD421rUrkp0nieUweq6uatf2AYGc5H2EGndESRlIQYAAeFfSTZV6GxUcvDyY1VWY1rz20tW0jtGqRZFIvpnlRYaLcHkTDjar5nc96O7iUKnSzS-y5fSmQQeg09I6tPCqWSE-pGu-SCLVjubTZzlQR4s_aC39KfyzIkEJwMlfn64zuyPryTXQlB7SYtmf2KC11V6a9oVzMm8mKyKtDiMwRmJ3NxQSk2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-06-2026 المقر المستحدث للواء المدرعات (401) التابع لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78641" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02861fd01.mp4?token=FJRsBQXofajnLBmM_XybOaWTrs_qQXMtgW97Bvd1g83-ETM4ilocD24zxOORuDsKIaYEGfcCGc0JI-E7LoTWFV4j6LWykP8PA_n6DIAkvRHxLuX9tMnz1PD1_BLAmS09wl87YXQMzfZa3PFR5ZFmTGsLvFiN0EZchkZbYROk4SmrX41bH6YJN3Vs88M7n1wGgnpIj_B4n-3n1-YUOvxaC_McPvXW9CZKdozLRhhkCRbOYhlH1jUPHhrefXHYfRrs-lRbOe_V39EB3RZVqcd4nJwzRyynVT5k5pHwfePfe7Owo3CYirBSDXgZG6VdS4Ha503a08wG_oTmetJnEnMgBXxd-Oho_VphVOVyyhhhdqxFoboEku_nQ0yEU9ibwoLrgZuy7CbilKuVO5vTJYs3fLv0opLyVucYHukfJNGTaQWSEKz1z56G2VvT3wU4V_URnud-WR4BXGrekutl0KLgazvc5KKIGeA6Hd97JW9c1x5Q3yfo9zsy-PhD71HmhvCP9_i2dFd6heRayL7LimlLuPE4oa9b90mqy5TpYsftgvGD_ZsGH6I9hNCcFfewtH9AArtInbmYkZukQ6w0NVr2KHdEFTH-3VMb2B6tFkKbL7HfwtN1VWK45jbaYbNnXfhn1tXLgygaEfhQ53hJoURNElllLAckNKuekTpfjXJegJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02861fd01.mp4?token=FJRsBQXofajnLBmM_XybOaWTrs_qQXMtgW97Bvd1g83-ETM4ilocD24zxOORuDsKIaYEGfcCGc0JI-E7LoTWFV4j6LWykP8PA_n6DIAkvRHxLuX9tMnz1PD1_BLAmS09wl87YXQMzfZa3PFR5ZFmTGsLvFiN0EZchkZbYROk4SmrX41bH6YJN3Vs88M7n1wGgnpIj_B4n-3n1-YUOvxaC_McPvXW9CZKdozLRhhkCRbOYhlH1jUPHhrefXHYfRrs-lRbOe_V39EB3RZVqcd4nJwzRyynVT5k5pHwfePfe7Owo3CYirBSDXgZG6VdS4Ha503a08wG_oTmetJnEnMgBXxd-Oho_VphVOVyyhhhdqxFoboEku_nQ0yEU9ibwoLrgZuy7CbilKuVO5vTJYs3fLv0opLyVucYHukfJNGTaQWSEKz1z56G2VvT3wU4V_URnud-WR4BXGrekutl0KLgazvc5KKIGeA6Hd97JW9c1x5Q3yfo9zsy-PhD71HmhvCP9_i2dFd6heRayL7LimlLuPE4oa9b90mqy5TpYsftgvGD_ZsGH6I9hNCcFfewtH9AArtInbmYkZukQ6w0NVr2KHdEFTH-3VMb2B6tFkKbL7HfwtN1VWK45jbaYbNnXfhn1tXLgygaEfhQ53hJoURNElllLAckNKuekTpfjXJegJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
08-06-2026
آلية قيادة وسيطرة تابعة لجيش العدو الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78640" target="_blank">📅 21:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV4XiZBi24LKpuGkJ7MQaxA0MAJ0LYW2dBNQRbyr05VnR9gYWTZ5pPohJQBwjB9efXviszeLguuDfe7Ch7MlYgN5Fb2hOusVE_NafRNZ-vAjafebVKrmjGX5QQvLUB8Ggmh68leXqWdlZVodAj6HRzt3i2w57KgMym__0c1lXjued5UTXaOFVlQfOuKNfw0qMr5gxIpQbI-_0wb8y8Js8UAp6wqbH6QlMXrQQxfTb7wwqXWCnndD2yYcRL2nXWxrQj34CZzDAoGWbwWL7ahGnjT0XIbaeJwyVznmGwVHaT2zyvhKcv0jlAgN6VMg5Fbld6Y-RXWObSrbXx0F2n6Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78639" target="_blank">📅 21:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامب: كانت صفقة باراك حسين أوباما مع إيران، خطة العمل المشتركة المشتركة، طريقا سهلا وجميلا وسلسا إلى سلاح نووي، كانت إيران ستحصل عليه قبل ست سنوات، وكانت ستستخدمها قبل وقت طويل من الآن. اتفاقي مع إيران هو العكس تماما، جدار إلى عدم وجود سلاح نووي! في الواقع،…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78638" target="_blank">📅 21:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية إسقاط المقاومة الإسلامية طائرة مسيّرة تابعة لجيش العدو الإسرائيلي من نوع "هيرون 1" في أجواء بلدة نحلة في البقاع.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78637" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الجيش
الإسرائيلي
يستعد لاحتمال وقف العمليات البرية في جنوب لبنان ولكنه لن ينسحب من المنطقة الأمنية في إطار الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78636" target="_blank">📅 20:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXgxcwbfUlidKuJJ_CR-vxHkYbF3e4o91X2erHUkGM_KqR_NHRcvcRbjYi4eKVF37T-cNDszBAERXo_i59Nz2wq0u2vUkqJ2zeyD9n4eru7Kad6isS4Yn-BUNephR55brrjV4ijLLZFyd2eMOq_QuHxJ9Cvegtv8ImF-X2fdJERMQBKAQD7neNzEPwX8SiRD3s5_-5siqC0k-2Ode3X0ixGiGkeO2mUSfjhccurh2MQmP4L2-Buzc_y0kUdRPUYRzHxlv9A6MzWRe2b0QJISRlxSz4bphArkGlz4sBtCARtuAmQRuEe7PfDAMGERbsm_Ood0nPHyi_cMJU6mQMa9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
كانت صفقة باراك حسين أوباما مع إيران، خطة العمل المشتركة المشتركة، طريقا سهلا وجميلا وسلسا إلى سلاح نووي، كانت إيران ستحصل عليه قبل ست سنوات، وكانت ستستخدمها قبل وقت طويل من الآن. اتفاقي مع إيران هو العكس تماما، جدار إلى عدم وجود سلاح نووي! في الواقع، لم يعودوا يريدون سلاحا نوويا، ولن يكون لديهم سلاح، إما من خلال الشراء أو التطوير أو أي شكل آخر من أشكال الشراء. من المقرر توقيع الصفقة غدا، وبعد توقيعها مباشرة، يكون مضيق هرمز مفتوحا للجميع. علاقتنا مع إيران مختلفة جدا وأفضل من الإدارات السابقة. على عكس مئات مليارات الدولارات من مدفوعات أوباما لهم، بما في ذلك 1.7 مليار دولار نقدا أخضرا وباردا، لن يتبادل أي أموال الأيدي. في الوقت المناسب، عندما يكون كل شيء هادئا، سندخل ونحصل على الغبار النووي، المدفون في أعماق جبال الجرانيت الغارقة القوية، وذلك بفضل قاذفاتنا B-2 الجميلة وطياريها الرائعين، ونمزجه وتدميره، سواء في إيران أو الولايات المتحدة. نتطلع إلى العمل مع إيران، والشرق الأوسط بأكمله، لفترة طويلة في المستقبل. نأمل أن تنجح هذه العملية بسرعة وسهولة وسلاسة. إذا لم يحدث ذلك، فلدينا البديل النهائي، ونأمل ألا يتم استخدامه مرة أخرى! شكرا لك على اهتمامك بهذه المسألة!!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78635" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84518f17ac.mp4?token=NnOK36wnmoP2cij_H32Y5szoWtVmjNu5Lt_s6CO_1jeraf9_ZwFOv-39zMciDuAMyp0vwmE85vbSBGDCewKnSHRzvq4ltasfNbIq8sDvSbkJyG2rhLWOvII5J256EJaCaA8WUWKyCzWCKhMMmEPmShwfOkZpQrYRN4GoaLGb1PQYfYClq_FYloVoM_9aeVqwpcp2hO6suE0LGEl_IYYYCYFkP6K1hkEpCH7YXvPBVjNkhqAoIEOMMr_LoQQa0Y5hcaAIfOaFf33PZOJ2eIMuWtzTE0TEdFAARIHyyWY0WPdDILpBg1_9ZHwaWVvu7LlFbQK-WOZ2PjBGbQMTa2hbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84518f17ac.mp4?token=NnOK36wnmoP2cij_H32Y5szoWtVmjNu5Lt_s6CO_1jeraf9_ZwFOv-39zMciDuAMyp0vwmE85vbSBGDCewKnSHRzvq4ltasfNbIq8sDvSbkJyG2rhLWOvII5J256EJaCaA8WUWKyCzWCKhMMmEPmShwfOkZpQrYRN4GoaLGb1PQYfYClq_FYloVoM_9aeVqwpcp2hO6suE0LGEl_IYYYCYFkP6K1hkEpCH7YXvPBVjNkhqAoIEOMMr_LoQQa0Y5hcaAIfOaFf33PZOJ2eIMuWtzTE0TEdFAARIHyyWY0WPdDILpBg1_9ZHwaWVvu7LlFbQK-WOZ2PjBGbQMTa2hbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يدكون آلية أخرى تابعة لجيش الإحتلال الصهيوني في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78634" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
توثيق يظهر توقف العديد من السفن في الخليج الفارسي بعد إغلاق مضيق هرمز من قبل القوات المسلحة الإيرانية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78633" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSg6uTE2p3MtJpEOR0JYDj1Nt8ng7bWB3YeHma7_VEby4Tz7W1eE08Jw1CP2jI0f59AJl4-6RdfAkXlOOSjHlN8d_m0BGnXpOq9UyIz89hUsYJbd9VLW_c3SwxPVDChiKSGXv4vXMwvvTJIedU2JFLH71XOLt2_u2m9OUCJu4fcoZ-y9u7WvUy0wrjYbIEjIw3wrylhyXO-TYUuWH3VQSlELCavTgYX9ebkIej-uee86QGP7SRWniTpunjowFMvYFQ-TSmT5xWqFf6bX8ncq5358ufRGzJLbO_KH1lC-bK11R-0p3CtYhCYYkC8pJ_kPz7FSQPX5Hmuq6JXbIG4Bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف آلية تابعة لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان واعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78632" target="_blank">📅 19:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
حزب الله:
ועוד היד נטויה - والحبل عالجرّار</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78631" target="_blank">📅 19:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
الخارجية الباكستانية:
إسلام آباد ستنظم غدا حفل توقيع إلكتروني عبر تقنية الفيديو على اتفاق سلام أمريكي إيراني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78630" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
يجب أن نتقاضى ثمن الخدمات المقدمة في مضيق هرمز.
يجب إنهاء وجود القواعد الأجنبية والوجود العسكري في المنطقة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78629" target="_blank">📅 18:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مسؤول امريكي لرويترز: سنساعد في إزالة الألغام عند إعادة فتح مضيق هرمز، ويمكن لدول مجموعة السبع المشاركة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78628" target="_blank">📅 18:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📰
مسؤول امريكي لرويترز: نعتقد أننا توصلنا إلى اتفاق قوي مع إيران.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78627" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية: سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78626" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية:
سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78625" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني في حديث مع نظيره السعودي:
تم تحديد التوقيع الإلكتروني على الاتفاق بين الولايات المتحدة وإيران ليوم غد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78624" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 آلية هامفي تنقل جنود جيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78623" target="_blank">📅 17:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🌟
وسائل اعلام:
وفد إيراني يضم وزير الخارجية يصل باكستان غدا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78622" target="_blank">📅 17:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🌟
وكالة مهر:
قدّمت قطر خطةً تُتيح بموجبها تقديم 12 مليار دولار لإيران تشمل الإفراج عن 6 مليارات دولار من أصولها المجمدة في قطر و6 مليارات دولار أخرى على شكل قرض أو خط ائتمان.
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78621" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
How did China , Russia, North Korea see the war in Iran ?!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78620" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78619" target="_blank">📅 16:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78618" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78617" target="_blank">📅 16:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية:
مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78616" target="_blank">📅 16:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان صهيوني يطال بلدة كفر رمّان جنوبي لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78615" target="_blank">📅 16:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاوةُ جزءٍ من وصية الإمام الخميني على لسان القائد الشهيد للثورة الإسلامية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78614" target="_blank">📅 15:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78613" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعلام العدو: طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78612" target="_blank">📅 15:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعلام العدو:
طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78611" target="_blank">📅 15:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdDu10DU6h0BTAT8ICOlIBgd8LBNZjaHR4pSCy-bmZYqZ2ybGlRydJea5QpoQ-puJn3-JeiBjoFYvof-bD8ldsqIRmgscfSpXCypkkiEFN5gjbItoR6ZWju68Lb0B-GmFUbfPFlAykN-khiXoIvpqvw6pz7HbnRLDIb0hb8CH7yeHrXOpnTXqQ-G1sq9wTNwTXZFoPx1kvwHyWlvrVDoMTaXM13fGYcXd7CtMf6AKVX_DpxwUWJWWX8JYi_2K3sW-yf55vUiJvZk4dsX8I_Xz1sHqHInJmKfj2Gntf3g9Oh9Fa3T476bJeL2H6AqJntD8Z_sqJRfzP2ja0ZtpaCCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78610" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78609" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئيس الوزراء الباكستاني: توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78608" target="_blank">📅 14:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78607" target="_blank">📅 14:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئيس الوزراء الباكستاني:
توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78606" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=Sx5nhlRbWIGBgblfOb3SZEoS6-fXeVWopwOSiyt89aB_bbPbJdJ51fOLlNx8XwQLhiV3fgKLupJBHttNpYESQL9qmAi6K5EJtH5Bf_TD-DwR6W3sECitwsNL9WY734rd9610nmVvOHOdI9xiXCn15Zf9mZZJZh19HzycUSsZy1m8yXKtCtagwolvzxMOvUbR1vGZy3tunU8u_xRyGRjftMXoHiNiLn4xzZDa9eoCQlWOxKi3pyWyYaidPM1i8alaYFkW0ghHqobGVdtXTwnNJbTsedlhXYdux-_YXV5Sq8Fn8HNLaGFIQjWn4J6j7o84GX8P-hF-t6SpYR3dWas9Mx_TPS2jy9Son-5HJXIy7IFdhSNNb1XIzrSKpXDFr_-bH9ALbrOz4Xna6anfoZBEpO-9jCtSL6mo5fEHVOxkqSrvrepFn3gSk3R9SfWiPCBr8ZQCXEyxmd4ZQ-d4tObSYLa9alDdYD1Udz2siknmO48z0-i-wMTCGTaIF9j7pdwMhcY7YTenl1eA2JPJA8U1aMfBnFuCS5llhHkiYsN6TAOEhTFY_HLiDDT-JgC8OE7Luz7m45a5Bopvz6olSdZdAJbl-wjwvAxRdQjoBpQiJ39vc_X-Rw_2bQWq2LSLl5UN_7rsWCOcRrbtqKsSPToM5-wvBaRvpVBaJzEJvy51BZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=Sx5nhlRbWIGBgblfOb3SZEoS6-fXeVWopwOSiyt89aB_bbPbJdJ51fOLlNx8XwQLhiV3fgKLupJBHttNpYESQL9qmAi6K5EJtH5Bf_TD-DwR6W3sECitwsNL9WY734rd9610nmVvOHOdI9xiXCn15Zf9mZZJZh19HzycUSsZy1m8yXKtCtagwolvzxMOvUbR1vGZy3tunU8u_xRyGRjftMXoHiNiLn4xzZDa9eoCQlWOxKi3pyWyYaidPM1i8alaYFkW0ghHqobGVdtXTwnNJbTsedlhXYdux-_YXV5Sq8Fn8HNLaGFIQjWn4J6j7o84GX8P-hF-t6SpYR3dWas9Mx_TPS2jy9Son-5HJXIy7IFdhSNNb1XIzrSKpXDFr_-bH9ALbrOz4Xna6anfoZBEpO-9jCtSL6mo5fEHVOxkqSrvrepFn3gSk3R9SfWiPCBr8ZQCXEyxmd4ZQ-d4tObSYLa9alDdYD1Udz2siknmO48z0-i-wMTCGTaIF9j7pdwMhcY7YTenl1eA2JPJA8U1aMfBnFuCS5llhHkiYsN6TAOEhTFY_HLiDDT-JgC8OE7Luz7m45a5Bopvz6olSdZdAJbl-wjwvAxRdQjoBpQiJ39vc_X-Rw_2bQWq2LSLl5UN_7rsWCOcRrbtqKsSPToM5-wvBaRvpVBaJzEJvy51BZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على ذمة اي نيوز
سجلت محافظة المثنى ضمن اكثر المحافظات فقراً ؛ ٣٦ مليار من واردات بلدية المثنى وتم تسجيلها من ديوان الرقابة المالية تسرق من رئيس هيئة الاستثمار بالمحافظة بعد بقائه منذ ٩ أعوام  .</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78605" target="_blank">📅 14:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78604" target="_blank">📅 14:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=guXDMyozIVkYpAvgCsTSp4UkP60abEVZQGOvw88Vx2hjkVY1MqG87BdKnffS8CIz47nAn8coANUJwJFM6GnbkgsF3j_8au8snmj9CchPFQkw9jgNFoBNkuUy3xpwFbSIIG3Fg7PNhOVxEEFsFKp1Vag5oSQYiH6yg1U9ycFm-aPkA_iqXP5zYw_90V0vPM6L94oXTclvoGJGYNLahJtqUjJICJnt5mR_QFH-OPPHsuS__ij7FaA4oKqb66R_bydLabj8hnzJQ6y-s9JI_c7daaUTQciCXeQ5eOPYYVvDDYHjo9N0ZZKzMU9jlTDYYta1COcQ7tW2jn_m7OIcell2nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=guXDMyozIVkYpAvgCsTSp4UkP60abEVZQGOvw88Vx2hjkVY1MqG87BdKnffS8CIz47nAn8coANUJwJFM6GnbkgsF3j_8au8snmj9CchPFQkw9jgNFoBNkuUy3xpwFbSIIG3Fg7PNhOVxEEFsFKp1Vag5oSQYiH6yg1U9ycFm-aPkA_iqXP5zYw_90V0vPM6L94oXTclvoGJGYNLahJtqUjJICJnt5mR_QFH-OPPHsuS__ij7FaA4oKqb66R_bydLabj8hnzJQ6y-s9JI_c7daaUTQciCXeQ5eOPYYVvDDYHjo9N0ZZKzMU9jlTDYYta1COcQ7tW2jn_m7OIcell2nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78603" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78601" target="_blank">📅 13:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">To Zendei (Echoes Of An Eternal Life)</div>
  <div class="tg-doc-extra">Ehsan Yasin - Ehsan Saeedi</div>
</div>
<a href="https://t.me/naya_foriraq/78600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">أنشودةٌ موسيقيةٌ بلا كلام «أنت حيّ»
هديةٌ قُدِّمت بمناسبة أربعينية الشهادة إلى الإمام الشهيد خامنئي الكبير، ذلك الروح الطاهر السماوي
نغمةٌ تكسر اختناق الدموع المكبوتة طوال هذه الأربعين يومًا…
#شاركها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78600" target="_blank">📅 13:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/78599" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78598" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل
زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات معدلة ف " جيران  " النسخة العكسية عن شاهد ١٣٦ أصبحت الزائر اليومي للقطعات العسكرية الاوكرانية المدعومة من حلف الناتو دون وجود اي حلول ممكنة للتصدي لها كيف سيؤمن سماء البحرين والسعودية ؟!
😆
الحل الأفضل هو اتباع الطريقة الاماراتية دفع أموال لايران و ضمان عدم استخدام أراضيهم كمنطلق للعدوان .</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/naya_foriraq/78597" target="_blank">📅 13:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-VAcIzQ3P-PvAfSGo6A6DXFeySWw1ds6BPDVy7EfEepaZGJ7O9E3G-NpJJ2amOEin7-HT0jWEcpbOZo9NX6NNDd2IueHDpnm5Un_X-z7QdhguFUSp-gzeqYakvUCDKrNG5UnSTxNJGxF6pdWK4J0rhxfBl-2JeW4qWIll7H9Ghnw9lZMB5L4zHwIBaVsLSs59OjgV2OgcY0GgJ2SYVSp9wU15LW6vamwx4Ft-a-EcIwuF6ktZXcrF63YXae35bYMUX7xE5oiEnKhREe8VZygbcb9ZqP7edQRB4z5PtH_xAPC9iGzMSNo0EuQXlcSY9a2-makTq97iJmpxdEFdysMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🌟
صدور مذكرة القاء قبض وتفتيش بحق مهند الزبيدي مدير مدرسة النعمة العراقية في العاصمة الاوكرانية كييف اضافة الى موظف وموظفة في وزارة التربية العراقية على خلفية تورطهم بعمليات تهريب الدفاتر الامتحانية المدرسية الى الخارج.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78596" target="_blank">📅 12:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏نواف سلام: مشكلتنا مع حزب الله هي سلاحه وعليه أن يكون قوة سياسية فقط
من المفترض أن يكون الجنوب اللبناني خاليا من السلاح</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78595" target="_blank">📅 12:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=EFmVUXgHppUu03n6ePZttDBS716cKh1mJ3W11gJytvAm36ubAlZld6BS-L6LCHEbtSeJKz1lCw7n1K1BNdB9Pzmk5ez1Q93lcp1B3oEQtrQZ7ob0R6c7xsRcdTfcJnUsIWD4n8uPeuxU3xVjppXm3HF-cL0wJY_nneZzE3fQ-7JIpo_uJ4mc8OZlWFSYrHDbG0u8yDpTyTV8cZYrJ9-aG1B-AL1cnSBRcAikOsjT-Xr5e9V1lHTASSsxItxE3a34eAiwUC2kvxYDf9CJuT0gcPTZP94OW744bGnu1jHnTL1IcRHFIuTKGu68C11byohYCAFMyy7-R6V_g8C5bQ5TGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=EFmVUXgHppUu03n6ePZttDBS716cKh1mJ3W11gJytvAm36ubAlZld6BS-L6LCHEbtSeJKz1lCw7n1K1BNdB9Pzmk5ez1Q93lcp1B3oEQtrQZ7ob0R6c7xsRcdTfcJnUsIWD4n8uPeuxU3xVjppXm3HF-cL0wJY_nneZzE3fQ-7JIpo_uJ4mc8OZlWFSYrHDbG0u8yDpTyTV8cZYrJ9-aG1B-AL1cnSBRcAikOsjT-Xr5e9V1lHTASSsxItxE3a34eAiwUC2kvxYDf9CJuT0gcPTZP94OW744bGnu1jHnTL1IcRHFIuTKGu68C11byohYCAFMyy7-R6V_g8C5bQ5TGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: السكان والزوار الموجودون على الشواطئ الجنوبية لايلات يبلغون عن سماع إطلاق نار من جهة البحر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78594" target="_blank">📅 12:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📰
تقرير شبكة CNN:  في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب  وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات  وفقًا للمصادر، أصبح…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78593" target="_blank">📅 11:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
‏بلومبيرغ: إيران أضافت على الأرجح أسلحة روسية حديثة لمخزوناتها خلال وقف النار</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78592" target="_blank">📅 11:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📰
تقرير شبكة CNN:
في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب
وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات
وفقًا للمصادر، أصبح الوصول إلى مخازن اليورانيوم المخصب الآن أكثر صعوبة وخطورة ويتطلب وقتًا أطول مما كان عليه قبل شهر فقط</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78591" target="_blank">📅 11:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: توجد فجوة شاسعة بين نظرتنا إلى أنفسنا والصورة التي تُرسم لنا في الخارج ؛ يُنظر إلى "إسرائيل" في الخارج على أنها بلطجي الحي وتُعتبر تهديدًا للاستقرار والسلام العالميين.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/78590" target="_blank">📅 10:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
تسلل مسيرات من حزب الله نحو المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78589" target="_blank">📅 09:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=oKexbVTnwOzCsX76uJLVrOyoI4tD2InQAlv8pf7lPGUdkve0HOZwU9oSM0nBuY3wwwOF_38DTMWbE6IK9maGRf6cDkutrEOdB05uoxkCcvuDzyRsCNwdelcR-1p0N3tl9LKRRQWqcpgUs7CHalbnIjbIJDa93njIxblQ8j5kUWVihYwUbxRgQ38yNzes3hRe1k5Qn9SW68MP25ea3U7gtlWnE9atNB6q00zXDoXm4t-xgGvNnztbJU1ClEJ3Vl_1cABmipqDBCIJ1F_GIAYR0OihwEAP8NDddtnDPoYBeDjj-6VwQFDmMj8UWiX0s3LW9XrwvcW6Svq_LMOVaHVSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=oKexbVTnwOzCsX76uJLVrOyoI4tD2InQAlv8pf7lPGUdkve0HOZwU9oSM0nBuY3wwwOF_38DTMWbE6IK9maGRf6cDkutrEOdB05uoxkCcvuDzyRsCNwdelcR-1p0N3tl9LKRRQWqcpgUs7CHalbnIjbIJDa93njIxblQ8j5kUWVihYwUbxRgQ38yNzes3hRe1k5Qn9SW68MP25ea3U7gtlWnE9atNB6q00zXDoXm4t-xgGvNnztbJU1ClEJ3Vl_1cABmipqDBCIJ1F_GIAYR0OihwEAP8NDddtnDPoYBeDjj-6VwQFDmMj8UWiX0s3LW9XrwvcW6Svq_LMOVaHVSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
عدوان صهيوني على حي الراهبات جنوب لبنان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78588" target="_blank">📅 08:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDfckSiuRps_EqH_5eTK30OfaTCg3snWJuY4MbmC-dvoTXvTQg3D52-Zue1cRTDfrISBWr_UykogrjT-u1rBeb3KJHAKeiArBdydcWWZU8qunrawaSNHyInR_rGbBtE8L1VfBsg8ORNmirzV8GbUBZ5bk3SI-GTiSdjFXUCk0pN6Hv-RaT6S7MHUXhPWmcCrzKtjBrDol_sRYTZdbzlMJX8SN5ZLAcqmqrE-plp5D42mqIIsdOj4bIJsA8VR5BGGbHxG71gM0VJ0wRSN5qPbbnC_T9ziGdO9n-3t1vCeD2eyiFwVHRyPgyN_YxBr3LPPze-DNNA2hFse7umBIdObKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: هبوط مروحيات إجلاء في مستشفى الوادي العفولة شمال الكيان بعد نقل جنود مصابين من جنوب لبنان جراء تعرضهم لحدث أمني صعب.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78587" target="_blank">📅 07:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
وول ستريت جورنال
: محادثات فنية إضافية بشأن قضايا شائكة قد تجري بعد ذلك في إسلام آباد، جي دي فانس سيتوجه إلى جنيف لتوقيع مذكرة التفاهم مع إيران، عودة وفد قطري من طهران الأسبوع الماضي حاملا صيغة اتفاق جديدة شكلت نقطة تحول حاسمة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78586" target="_blank">📅 04:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=Zru7HaAkCuq4goJ_YB_hGWCtvNczW9V2L0wv0zgBQxnu34TuSbE58D4gXT330adUm1FeCGb-PIUjLUCi0bQTWZ_h3XpzwK_JxOrKFLa1VUo48K9C1feYKbQ9YgtDaYT7a9ETHmRqE6r07yneim0713eG527ZNO7rTz2culZZfu7ji0evrICEHbaV4waU08oOFZpOSqtkZoVvjYbpGiM8TQ3xFLBXS3F3qPNndF0mHHEWzzfwNNg92m1Q28c7fKNHq_kKytY_gQXRzfm3M8v6_xjY86n35olDPR7dZ9wnYzEF6_n4PnZDjNVPSjjzrIwrP0DQbe5bzMGuJFLlxwXtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=Zru7HaAkCuq4goJ_YB_hGWCtvNczW9V2L0wv0zgBQxnu34TuSbE58D4gXT330adUm1FeCGb-PIUjLUCi0bQTWZ_h3XpzwK_JxOrKFLa1VUo48K9C1feYKbQ9YgtDaYT7a9ETHmRqE6r07yneim0713eG527ZNO7rTz2culZZfu7ji0evrICEHbaV4waU08oOFZpOSqtkZoVvjYbpGiM8TQ3xFLBXS3F3qPNndF0mHHEWzzfwNNg92m1Q28c7fKNHq_kKytY_gQXRzfm3M8v6_xjY86n35olDPR7dZ9wnYzEF6_n4PnZDjNVPSjjzrIwrP0DQbe5bzMGuJFLlxwXtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب
:
"بتوجيهاتي، نفّذت القيادة الجنوبية للولايات المتحدة ضربةً سريعةً وقاتلةً أسفرت عن إعدام نينيو غيريرو، الزعيم سيئ السمعة لجماعة ترين دي أراغوا، إحدى أكثر المنظمات الإرهابية دمويةً على وجه الأرض. قبل عودتي إلى منصبي، فتح جو بايدن حدودنا الجنوبية أمام ملايين المجرمين غير الشرعيين، وسمح لهذا الجيش الأجنبي باغتصاب وتشويه وقتل مواطنين أمريكيين دون أي عقاب. خلال حملتي الانتخابية، تعهدتُ بطرد هؤلاء الوحوش من بلادنا، وتحقيق العدالة لعائلات ضحاياهم، بمن فيهم الطفلة البريئة جوسلين نونغاراي ذات الاثني عشر عامًا، ولاكين رايلي ذات الاثنين والعشرين عامًا، وعدد لا يُحصى من الأرواح البريئة الأخرى. بهذا العمل، حقق الجيش الأمريكي الانتقام لهم ولعائلاتهم وأحبائهم." في بداية ولايتي، وفيتُ بوعدي بتصنيف حركة ترين دي أراغوا منظمةً إرهابيةً أجنبية، وترحيل آلاف المجرمين الأشرار، وشن حربٍ على عصابات المخدرات التي لطالما شنت حربًا على مواطنينا، بينما ترك القادة الضعفاء أمريكا عاجزةً في موقف دفاعي. وقد تم تنسيق هذا الإجراء بشكل وثيق مع أصدقائنا في فنزويلا، الذين نتعاون معهم تعاونًا مثمرًا. ونتيجةً لذلك، لم يعد لإرهابيي ترين دي أراغوا ملاذٌ آمن في فنزويلا أو أي مكان آخر، وسنجد هؤلاء القتلة المتوحشين وتجار المخدرات في أي وقت وأي مكان، وسنرسلهم إلى قعر الجحيم حيث ينتمون. حفظ الله أمريكا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78585" target="_blank">📅 04:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
رويترز
: أطلقت الولايات المتحدة صواريخ على العديد من طائرات بدون طيار الإيرانية أحادية الاتجاه أثناء توجهها إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78584" target="_blank">📅 04:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
اعلام العدو:
ترمب أصدر تعليمات بتخفيف العقوبات عن إيران إذا التزمت بالاتفاق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78583" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE_JcHTQ_3VuVfO0RwiqoZPsVLWnhX6b9h_5kk7KLjaQwdWGAD1x-6Gnhl5SLClFR7l7ehOa97_jTywofQ8F8MC_4cpOmaPOrJIKDYsgWPVfHbje7JXOuLroWhGChqJGlV7eh3BswucBKvWUvPF8X5po5u6xbyL71fJNJYrkX3DDND_XKQqfxOFZV2y5b2liI7dxVmvUrE4hibYgmsiVQ9wAnST_T1xKiRRIcz0rjwuUsQDnSp0qkBWN9M478eVPjQS45Sa4wa0XB1qxQEGFhNiAxCcuDDhJfh-9-ceKfh0m4FqZzIINESxcIBWS2oiRa9CIJqcQhQuqBzAtuBf6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t026jkTKSLL560471FZ5GKZ56nACaBxHYbNhzLy1sDgFRNk-Htt67yxInjuPN0YABzn_KPLIQsQzX2N5AemtO8ZNCZ6SgCtBY7IelGMCwkB-B6Gj4brf1tGcZh4QpRqGZOPBaaKBEYVBhpoURj61Se-6G_hvshgDKvPDiRsINglppKLiofzovZX2Sij-qJuHHGcGzmgdMUDMgKZgeAaEnR3u6WGCRCcgqXv7Zk3Y3ft35g5wCpLUDrGB0Bz6dR6qjj5HUZGlwiVsAsjDgCjAw_-q0z19e8HebBCX88TWXohgncG5qA8ePV_EhPqn_TIyTgYKxtiEzc783jpFrqHyPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
عُثر على جثة في صندوق سيارة متوقفة عند ملعب كالينتي بالمكسيك، وهو ملعب تدريب المنتخب الإيراني.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/78581" target="_blank">📅 03:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇬🇧
🌟
المحكمة البريطانية تحكم بالسجن 29 عامًا على شابين كرديين من شمال العراق بعد إدانتهما باستدراج فتيات قاصرات والاعتداء عليهن جنسيًا في دونكاستر، فيما تواصل الشرطة البحث عن متهم ثالث ما زال فارًا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78580" target="_blank">📅 02:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
أكسيوس: نتنياهو وجد نفسه خارج كواليس التفاوض ولجأ إلى الاتصال بحلفاء في واشنطن لجمع المعلومات.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/78579" target="_blank">📅 01:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
أكسيوس: منشور ترمب يوم الخميس الذي أعلن فيه التوصل إلى اتفاق مع إيران فاجأ نتنياهو.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78578" target="_blank">📅 01:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
أكسيوس: نتنياهو بدا أنه أدرك خلال الاتصال مع ترمب أنه لا يستطيع منعه من إبرام اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78577" target="_blank">📅 01:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
أكسيوس: ترمب قال في اتصال مع نتنياهو الخميس إن الصفقة مع إيران رائعة وحان الوقت لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78576" target="_blank">📅 01:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
أكسيوس
: ترمب قال في اتصال مع نتنياهو الخميس إن الصفقة مع إيران رائعة وحان الوقت لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78575" target="_blank">📅 01:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏الإمارات تنفي بشكل قاطع بشأن نقل أموال إلى الجمهورية الاسلامية الإيرانية كتعويض، مشددة على أنه لم يتم الإفراج عن الاموال أو تحويل أو نقل أي أموال إيرانية مجمدة عبر الإمارات.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/78574" target="_blank">📅 01:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: أصوت الانفجارات قرب ميناء سيريك ناجم عن إطلاقات تحذيرية أطلقت نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/78573" target="_blank">📅 00:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxxNOYvnSKFcAU6sFEHMyzzFm0FBZP3iL4z1Qgs1uR7xJesLBu0C9vx-QIACGLD_eS6Ck5W7Y6zOlqIUUZfc7VLwGgrm6EYOqv3c8bYAKjoVbjrvU2T4hXOYy4w9nf55Qqt5UvDYSZYzN9J9qGgAIntnefLG2RHHCIBfcuqKKw7Y_tkxJ-c2VX4igPQtUdGsXSsa8O4kWEdIvcMnHCoJViXJ6O40TZPc0zXClrNJ9pqSkUIqb6kqZKu0VPnPnOWsYC1vs_4GAK5RRbkZDyMNDhxo-rwXxGBATa924kIJOgxlEfthpD1EEVEBFAqqqq8VNWIt_Z28p110l5oZjQ53Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: أصوت الانفجارات قرب ميناء سيريك ناجم عن إطلاقات تحذيرية أطلقت نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/78572" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">أنباء أولية: سفن حاولت العبور من مضيق هرمز وتم استهدافها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78571" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سماع دوي انفجارات في قشم وسيريك وأنباء عن اشتباكات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78570" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سماع دوي انفجارات في قشم وسيريك وأنباء عن اشتباكات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78569" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi28LKi0k3W66keaBslxnF43EkrbMQ40eOYSW_486-MQfKa89oCHfyp9oRtS2kSViXZfMC2eoabS3_jtbFGUr27X-VbgtTBhn0cyEMh04ssziSxXJMMpkxnnmlNvoeORsm6kulzIOPALsHJW776_g00RVc-pbKeJsDRctT19CdM6z6CjSW8liw1kt6ahkTOsTyivH3DE4Zk6qTvdD8kTqTkeF_HJBK9klTX74BIajfiFqJy4JOeq5rb7waBNHrh8PM1N5WVbEFlCGkHFb2uClnp31y_4pVTK0TeXRsPLN0ipk6FojdrtdJsVhJ1wzmfHxVu4CnCoRl_wTBukvJIt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
رئيس حركة حقوق
النائب حسين مؤنس:
قرابة 600 مسجد شيدت مؤخراً في أبو غريب وحزام بغداد ناهيك عن المحافظات الغربية ، تستغل لنشر الحركة المدخلية ضمن مشروع منظم يُراد له التشويش على المذاهب الإسلامية المعتبرة، وإنتاج توجهات وشخصيات فكرية منحرفة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78568" target="_blank">📅 00:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
نحن على أهبة الاستعداد للدفاع عن الشعب الإيراني بكل قوة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78567" target="_blank">📅 23:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d230a970a.mp4?token=AH8oDxfkDT0jVZxefJ7T0g8Y4zhBDe7u-kE9503CtF3ZxmuEwSLGQGayF5xEcO7VbKuCcn3-6LIXKEce4XRN6p_a9QM-95U7PBaq76jkDWYiAGr0iNc4mxXX474AAI4kIH29cxjbs9vOtQY1XiYL7jDACxjezxiWfrk4h-5FCaBIfhMZnVOEYuH_A81xCH6aMsQvzuK_So3XpZV8GIYBlWeqmtZVzNg1miyXso8R8xS8vuK_TFkA55LWsbsyvWqnBcVOlOry8V_gQZoY2ee2EzhOUC2MWHIkermMcMV_6jTiznw6cWNqGNaOEx2amBp5c-uMrptmkbk8RH8AtzGmFTlKYFoOtCqOvnu0OA2SsngcUi_clkVVsN50U7ytH9ZI_U_80fdRjLyoUQ5KaF30LjUTBXLMYHbNxNqOzvTEAuK27sWEMO0UZqLOnCgWNjyZ8y7Q4fIzyDG3YN_xKTvmgyq_FCCvdvrJzFJKr9xYo3KH7UVdCEMLFOWKNfw68pAXeOi7CFRvE_HBC3uZiKygQ_1LS438SSqvLQn_MSNUHKOCqMhY7jvvnEcc_-NLXVgCd--6w6p7e2X27mygGcPFvbM1epUrBTO3YS_jkqdW1b6auTpyfXL3ikK1Gw3YgNNz9AQSatIdWARZyZ5nUdKRBaLTAF9F3lorg7ygtb7FFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d230a970a.mp4?token=AH8oDxfkDT0jVZxefJ7T0g8Y4zhBDe7u-kE9503CtF3ZxmuEwSLGQGayF5xEcO7VbKuCcn3-6LIXKEce4XRN6p_a9QM-95U7PBaq76jkDWYiAGr0iNc4mxXX474AAI4kIH29cxjbs9vOtQY1XiYL7jDACxjezxiWfrk4h-5FCaBIfhMZnVOEYuH_A81xCH6aMsQvzuK_So3XpZV8GIYBlWeqmtZVzNg1miyXso8R8xS8vuK_TFkA55LWsbsyvWqnBcVOlOry8V_gQZoY2ee2EzhOUC2MWHIkermMcMV_6jTiznw6cWNqGNaOEx2amBp5c-uMrptmkbk8RH8AtzGmFTlKYFoOtCqOvnu0OA2SsngcUi_clkVVsN50U7ytH9ZI_U_80fdRjLyoUQ5KaF30LjUTBXLMYHbNxNqOzvTEAuK27sWEMO0UZqLOnCgWNjyZ8y7Q4fIzyDG3YN_xKTvmgyq_FCCvdvrJzFJKr9xYo3KH7UVdCEMLFOWKNfw68pAXeOi7CFRvE_HBC3uZiKygQ_1LS438SSqvLQn_MSNUHKOCqMhY7jvvnEcc_-NLXVgCd--6w6p7e2X27mygGcPFvbM1epUrBTO3YS_jkqdW1b6auTpyfXL3ikK1Gw3YgNNz9AQSatIdWARZyZ5nUdKRBaLTAF9F3lorg7ygtb7FFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الداخلية الأمريكي:
كانت كاليفورنيا تعتمد على النفط القادم من مضيق هرمز. سيكون لديهم أسعارًا مرتفعة للبنزين.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78566" target="_blank">📅 23:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال محتل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78565" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba9b3581f.mp4?token=K1_EIMqx8rDRcbecrdYM3xGg5HIgz9gS9BUeKkHgF4eXs3yjIkPq8Tmy2LluqcgvO7IlXFgV27RLjIMECVEOd8MLmOLOhBP4yBB66RdjZ5ho8wAVObgadkIWzgMDafeN3Yd-bTQ7D6_znoJsrdbueQ-zR4CuE6_v-UPM4_R3qCJ4Y35nk2unY8xmPjuZ8bMC3EK4_TBQO_JGW_6uS0C94JE2jh7u5iwz-VvF-SwKV0hNUd86FvScAeI69KU1tJ7UPVIirQnrd8CQGGphHO14irOjJHVbmN7DAqeNdbdIqrdoNWrXuw4JTqPWBcTaA9bz1l5NNs-hfxMHgGMq5ozJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba9b3581f.mp4?token=K1_EIMqx8rDRcbecrdYM3xGg5HIgz9gS9BUeKkHgF4eXs3yjIkPq8Tmy2LluqcgvO7IlXFgV27RLjIMECVEOd8MLmOLOhBP4yBB66RdjZ5ho8wAVObgadkIWzgMDafeN3Yd-bTQ7D6_znoJsrdbueQ-zR4CuE6_v-UPM4_R3qCJ4Y35nk2unY8xmPjuZ8bMC3EK4_TBQO_JGW_6uS0C94JE2jh7u5iwz-VvF-SwKV0hNUd86FvScAeI69KU1tJ7UPVIirQnrd8CQGGphHO14irOjJHVbmN7DAqeNdbdIqrdoNWrXuw4JTqPWBcTaA9bz1l5NNs-hfxMHgGMq5ozJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقجي: أول ما ورد في الاتفاقية هو رفع الحصار البحري الأمريكي.  سيتم الإفراج عن أصولنا المجمدة.   أُدرجت مسألة التعويضات والأضرار في خطة إعادة الإعمار.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78564" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عراقجي:  مضيق هرمز بلا شك تحت سيادة إيران وسلطنة عمان ولا يوجد ممر مائي دولي في مضيق هرمز.  مستقبل إدارة مضيق هرمز لن يكون كالسابق. لا يمكن لأحد أن ينتقص من سيادة إيران وسلطنة عمان على مضيق هرمز.  لن تكون إدارة مضيق هرمز كما كانت في السابق (قبل الحرب).   ستصدر…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78563" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقجي:
مضيق هرمز بلا شك تحت سيادة إيران وسلطنة عمان ولا يوجد ممر مائي دولي في مضيق هرمز.
مستقبل إدارة مضيق هرمز لن يكون كالسابق. لا يمكن لأحد أن ينتقص من سيادة إيران وسلطنة عمان على مضيق هرمز.
لن تكون إدارة مضيق هرمز كما كانت في السابق (قبل الحرب).
ستصدر إيران وسلطنة عمان قريباً بياناً مشتركاً بشأن إدارة مضيق هرمز.
سيبقى سيفنا حاضرًا دائمًا فوق مضيق هرمز، وستدخل القوات المسلحة الإيرانية عند الضرورة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78562" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cf391ca6.mp4?token=tOIdNSFJOtTVhUuTLgBW1RARxeJMlbSGVARHLM2WLtGEn35OY8C2P_FLCWTKmHQ6xw2AAYASBrlTm6ejbMeQNG-7-b2Xa9yDrbt6nlniDSMQjnPNOitnJg5MpFQYNy8WeFn2aF5JiTYPU1oyreUQegd8xp2ezcprnKiGQUhZVG6X1F19xKt-ta6hTYcstwGvYKAcRWRnLFoRo0Oeft7JWiNnhJrtRAjOA49zxY5djfRORuP4WCJWYkk8RyHJ3fk2gxK0y-zjUEiN13WE9DpGRHAE_odCo6S8lfeyoXtudTZ6GvGZqHYAQs9tiZ_I0ThkFA_cXij4HNAw3rqd-_c86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cf391ca6.mp4?token=tOIdNSFJOtTVhUuTLgBW1RARxeJMlbSGVARHLM2WLtGEn35OY8C2P_FLCWTKmHQ6xw2AAYASBrlTm6ejbMeQNG-7-b2Xa9yDrbt6nlniDSMQjnPNOitnJg5MpFQYNy8WeFn2aF5JiTYPU1oyreUQegd8xp2ezcprnKiGQUhZVG6X1F19xKt-ta6hTYcstwGvYKAcRWRnLFoRo0Oeft7JWiNnhJrtRAjOA49zxY5djfRORuP4WCJWYkk8RyHJ3fk2gxK0y-zjUEiN13WE9DpGRHAE_odCo6S8lfeyoXtudTZ6GvGZqHYAQs9tiZ_I0ThkFA_cXij4HNAw3rqd-_c86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
إيران لاتترك حلفائها.. عراقجي: انسحاب جيش الاحتلال من جنوب لبنان ضمن الإتفاق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78561" target="_blank">📅 22:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عراقجي: تُعرض نصوصٌ مختلفة في وسائل الإعلام، وتُثار ادعاءاتٌ متباينة. وقد أكدنا، نحن والأمريكيون، أن هذه النصوص غير صالحة في الوقت الراهن، ولا نوافق عليها.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78560" target="_blank">📅 22:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقجي: إن مسألة مضيق هرمز ورفع الحصار البحري واردة في مذكرة التفاهم. وقد طُرحت مسألة إعادة الإعمار في صورة خطة لإعادة الإعمار والتنمية الاقتصادية، وسيتم الاتفاق على آلياتها في مفاوضات لاحقة. كما يجري النظر في آلية لأموال إيران المجمدة. وعند الانتهاء منها،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78559" target="_blank">📅 22:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عراقجي:  سيتم اعلان نهاية الحرب بكافة الجبهات بالتحديد لبنان.  ‌ سيتعهد العدو بعدم إشعال حرب أخرى، وعدم استخدام التهديدات أو القوة، وأن يحترم الطرفان سيادة بعضهما البعض، وأن لا يتدخلا في شؤون بعضهما الداخلية.   لن نترك حزب الله في لبنان وحيداً.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78558" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de96c18531.mp4?token=LA22DyNDULfOv0gkz2fEXAT8n-STTZqTgUEBuwJB1cgTxy9BWraSgSNgFHTLr7mCoLAASHEW6WA46Kj2a2nK2YVZThgt-RdrOpMKPPd00Eti4p4qdEWzyyx5GynNxnR3yJH8pPE8csu_v9zcP1WLah1NX4JYqU81W6iKpzqq--R5yebS9Ys1bfrPY53G66dvnwP8smc4pKEqw7QgxOLFVNhN2K3Esq-CJANd1TPWlNtGF5UXcoAiEl4GFU9NwkwsDKVApLg1gYPv4TmF3PLvNXfQHz4LafTT7EqOA5warTEnoiod5caY31FG74qffKpfWX00hhQFGlLO-YLDUGN_IUsT-wCVSYghYlKPG77Oh5V9AseJpI3z5Pul64pGTxOv06QzQfEe86b_UEv1ihOGj_XEgD0-k8paSFOnd55CrzA9x_x6RNljLVZuNob5e14ERXxlU0hFGBXXjdZrlL2RLablPqYsubSZwcDjFWmEtJvAHxa1ae4UnLnSOyUe3LM4u51TWBSNb6mCBeuXWQRIPVbqT7LcNjP9WpjuFhS01XfJxbmAbgAFeGBcJIujkFoN3YcPeuTmO8-aPOXKDTxo9Yfl2KY89u_DI41bYN51nyF1hBL_cBjBWTt7H6jmXHuFTfyeb9DFYEpG_mz8kJXBDp2Jlxdm3Wqihgh2wSdchto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de96c18531.mp4?token=LA22DyNDULfOv0gkz2fEXAT8n-STTZqTgUEBuwJB1cgTxy9BWraSgSNgFHTLr7mCoLAASHEW6WA46Kj2a2nK2YVZThgt-RdrOpMKPPd00Eti4p4qdEWzyyx5GynNxnR3yJH8pPE8csu_v9zcP1WLah1NX4JYqU81W6iKpzqq--R5yebS9Ys1bfrPY53G66dvnwP8smc4pKEqw7QgxOLFVNhN2K3Esq-CJANd1TPWlNtGF5UXcoAiEl4GFU9NwkwsDKVApLg1gYPv4TmF3PLvNXfQHz4LafTT7EqOA5warTEnoiod5caY31FG74qffKpfWX00hhQFGlLO-YLDUGN_IUsT-wCVSYghYlKPG77Oh5V9AseJpI3z5Pul64pGTxOv06QzQfEe86b_UEv1ihOGj_XEgD0-k8paSFOnd55CrzA9x_x6RNljLVZuNob5e14ERXxlU0hFGBXXjdZrlL2RLablPqYsubSZwcDjFWmEtJvAHxa1ae4UnLnSOyUe3LM4u51TWBSNb6mCBeuXWQRIPVbqT7LcNjP9WpjuFhS01XfJxbmAbgAFeGBcJIujkFoN3YcPeuTmO8-aPOXKDTxo9Yfl2KY89u_DI41bYN51nyF1hBL_cBjBWTt7H6jmXHuFTfyeb9DFYEpG_mz8kJXBDp2Jlxdm3Wqihgh2wSdchto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقجي: المفاوضات مع أميركا ستتم على مرحلتين.  المفاوضات حول الموضوع النووي سيكون في المرحلة الثانية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78557" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
