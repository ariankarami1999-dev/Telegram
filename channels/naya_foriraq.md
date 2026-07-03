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
<img src="https://cdn4.telesco.pe/file/P7nTMMYZW1uopl_LxhZtKZgHZpDaQ6rLs8PMneULNQ5ZkNWAMBJyePT2jv6Vx8xuFN3xTdc98P-GWwnWwmCzS2CugbgpEVkt9CUztCa0AWA1SooBI96HMX2MwS4I3WxHzuHkAUeas98vWhLiyHEb5GQAk4PMNF4QHQTU62TEerC53U_9sJq3rD0CbGgbYdUQ0VjjeDs9r_5qMF-wLKnk1SxVl-TAC0zBdVToHklHNpmuZauCXT63mQa0f0uZjx4ipF90BOtzxgDQ_zW1boo2ZVPPbCSXMT9IIC6gq_srQWqmx_nsvhpW-w0yxTvKHv9-Okdbtp6ppLRfsGeqH7-nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 22:33:56</div>
<hr>

<div class="tg-post" id="msg-80860">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=mXZcKNvGZr5hQvBPgVHaBeY4EFbApaUsfAitRMXKMC3RGaG2AYtW-4lp9JcVbNO4njELcOlH4Q8NI7U4AqT7KTOuxi7HPZ_chfT30qv2ZFI93BmzroVx6ZoeyyRdY-f5wfhNspDxDeLn3IH8MGlu6ifIfa2m_rzC7_uEou7HeVHEvjZIMkKr794UfPvMll9yReamsNTWUxengw7UW1fgNU2F_4eNl7dZpNe5eRnsdF_DFJ6w28z4OLKVF3VnLOa_3bJvF68pzbyLYRQvT43pRJqWdgKKgCHwonlKlP55IiS2v1pA1Sk4lLKx26HFl0e6OovmiEa1iT2o_GFq1hAr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=mXZcKNvGZr5hQvBPgVHaBeY4EFbApaUsfAitRMXKMC3RGaG2AYtW-4lp9JcVbNO4njELcOlH4Q8NI7U4AqT7KTOuxi7HPZ_chfT30qv2ZFI93BmzroVx6ZoeyyRdY-f5wfhNspDxDeLn3IH8MGlu6ifIfa2m_rzC7_uEou7HeVHEvjZIMkKr794UfPvMll9yReamsNTWUxengw7UW1fgNU2F_4eNl7dZpNe5eRnsdF_DFJ6w28z4OLKVF3VnLOa_3bJvF68pzbyLYRQvT43pRJqWdgKKgCHwonlKlP55IiS2v1pA1Sk4lLKx26HFl0e6OovmiEa1iT2o_GFq1hAr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تدعي احباط محاولة تفجير عبوة ناسفة زُرعت داخل حافلة في حي الورود بريف دمشق، حيث تم تفكيك العبوة ونقلها إلى مكان آمن، دون تسجيل أي أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 476 · <a href="https://t.me/naya_foriraq/80860" target="_blank">📅 22:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1485646dca.mp4?token=uU1OVNG-hffPgV9VjHN5NtGzJ1JYEIxdXctcJvEDmX0pYr06WS4bTrE2SNVD9weQFYDHpd15mEVABtE4A1LY6mvmK_ts2vnGi7o1KCMfYA2K_mFdl7A5IhaunL84O5JrtiPhaWbxC0d0n0kl0WRjqDD7lyeEpcYcnyfKR7xMS4SkNVg6FSIDnAN5MIatURE1aJISgbD3CF1H-nJRwsSd7g-G29iPeFTboecYV-m4FyWG7RhueszbV7cj5fueZKTFvMTBAWQSkl2Fh24tMOJfI6hARE4kQANFmUORWGgUH0n_cN3a68okuYbfIaQPskvM1P5fge_cg59zzKiyGoYr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1485646dca.mp4?token=uU1OVNG-hffPgV9VjHN5NtGzJ1JYEIxdXctcJvEDmX0pYr06WS4bTrE2SNVD9weQFYDHpd15mEVABtE4A1LY6mvmK_ts2vnGi7o1KCMfYA2K_mFdl7A5IhaunL84O5JrtiPhaWbxC0d0n0kl0WRjqDD7lyeEpcYcnyfKR7xMS4SkNVg6FSIDnAN5MIatURE1aJISgbD3CF1H-nJRwsSd7g-G29iPeFTboecYV-m4FyWG7RhueszbV7cj5fueZKTFvMTBAWQSkl2Fh24tMOJfI6hARE4kQANFmUORWGgUH0n_cN3a68okuYbfIaQPskvM1P5fge_cg59zzKiyGoYr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. من اللقاء الأخير للجندي الشجاع الوفي وقائده الشهيد.</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/naya_foriraq/80859" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/naya_foriraq/80858" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
يا أمةَ الوفاء لرموزها وعظمائها،
يا من تؤدّون للكبير الجليل حقَّه حيًّا وميتًا،
إنَّ سيدَ الزمان، ووليَّ أمرِ الشرف، والشهيدَ قادمٌ إليكم،
يريدُ أن يودِّعكم عند أجداده الطاهرين.
قادمٌ في يومٍ تاريخيٍّ سيُذكرُ حتى قيامِ الساعة،
فقوموا لله،
وانهضوا بالسوادِ والغضب،
وشيِّعوه جموعًا تغطّي أرضَ العراق،
وابكوه بحرقةٍ تصلُ الأرضَ بالسماء.
فخيرُ السادةِ الكبراءِ
له حقٌّ على خيرِ الأوفياءِ .</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/naya_foriraq/80857" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXSy1XWGSicTgTjTS9Rfr2LDgjvkQj6qC6JsGfTeRT8hn8jCf8f-7d5ZwzLkV2emeobU3ZWQzuu9WFKdVpGb6gUWVfll14WYNv_O-d77UhhOpKFDDd_8lCIoxes03XnZRnPg0N385LXcKi_m3nyYZgXFNfayyQmMsJd5myahGEzMzdFhMgN2cb9lI0PcNsesk0xqrQXFIHdBts-4LttDIstqpunxBZIMntyiVD-_-2wPgquaCrnGQ-NHMR2L_rzHuv2ul71t2VvmR4QyB49iw4_NvpP7tn2X9BwpHWMElEapisgH-RDJW93rT7CVfYJxLKWJfD6GdR7wcdF8uUDGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
تخيّل أن يكون لديك نحو أربعين مليون مواطن يعتمدون على برنامج قسائم الطعام، ثم تصف دولة أخرى بالجوع. هذا ليس تصريحاً، بل مجرد إسقاط. احتفظ بنصائحك بشأن برنامج المساعدة الغذائية التكميلية (SNAP) لنفسك.
‏مواردنا، خياراتنا. انتبهوا لمعدلات سوء التغذية.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/naya_foriraq/80856" target="_blank">📅 21:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=sziBlZ6tTzjBq7D7S-Y8X1yid8TFLV7ub6EGtR-jcqEomLVB3M4P87NdseTqZkcl5ucDcmj2bjpB7HHTGunQNj-HoWMGysI5KU1VCNQgRolyCLCOg3OKWXB9ZfHezMeWEZymiYYhEpHHZNzVgTEtY1CZqCofCKfAsfTyfdgUkoJ4VbnmOIAitlDbBbWIojltqyFQ48PQaH7QX5VDenaFszhAKTZhf41V7rgAhRdTeie00GztlO4mc1LSWxBcZEKnsm1Q-D02D9xnLyEroy9yV7QNCUfhmRdAgXtW3EpnaexgzJQXcY77EudJ4xLUdZXLsFQ8WzzkbJ3QHQ1w2QXk3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=sziBlZ6tTzjBq7D7S-Y8X1yid8TFLV7ub6EGtR-jcqEomLVB3M4P87NdseTqZkcl5ucDcmj2bjpB7HHTGunQNj-HoWMGysI5KU1VCNQgRolyCLCOg3OKWXB9ZfHezMeWEZymiYYhEpHHZNzVgTEtY1CZqCofCKfAsfTyfdgUkoJ4VbnmOIAitlDbBbWIojltqyFQ48PQaH7QX5VDenaFszhAKTZhf41V7rgAhRdTeie00GztlO4mc1LSWxBcZEKnsm1Q-D02D9xnLyEroy9yV7QNCUfhmRdAgXtW3EpnaexgzJQXcY77EudJ4xLUdZXLsFQ8WzzkbJ3QHQ1w2QXk3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/naya_foriraq/80855" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=HAgSCTG8ZX3c--mFTMne_rfbaKnDoh96EIH5Gba75ZN7lcoFnZQvce-TyvfBGucgqde4xSwCt3IUmoOGZK7KXCMpVymv_YWHnhM-aWkK6Af_dQ8x2rC3xcHyU6xcQ0XUOqtEAgSKihiCLSmYaZwMxeE_C3JOSBoX-1mH6enmo9GrxKfCHuWlmKvzfiz3euZia3YSuuqnRm_8I9HhmVQnnDtsBn1IvGIomtIvNU1Lrgz2CbdYaRlqEn9uIBizBMblcOd6hTnrq08UHshmzya4VXBJdj0PAluDpTX6R6CZ0ioRYaL7x810V_7GNuB8dGq1ElwMEUiALrYTSHm7KIdlwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=HAgSCTG8ZX3c--mFTMne_rfbaKnDoh96EIH5Gba75ZN7lcoFnZQvce-TyvfBGucgqde4xSwCt3IUmoOGZK7KXCMpVymv_YWHnhM-aWkK6Af_dQ8x2rC3xcHyU6xcQ0XUOqtEAgSKihiCLSmYaZwMxeE_C3JOSBoX-1mH6enmo9GrxKfCHuWlmKvzfiz3euZia3YSuuqnRm_8I9HhmVQnnDtsBn1IvGIomtIvNU1Lrgz2CbdYaRlqEn9uIBizBMblcOd6hTnrq08UHshmzya4VXBJdj0PAluDpTX6R6CZ0ioRYaL7x810V_7GNuB8dGq1ElwMEUiALrYTSHm7KIdlwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/naya_foriraq/80854" target="_blank">📅 21:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
‏
رويترز:
أكبر مشغل لشبكات الكهرباء في الولايات المتحدة PJM يعلن حالة الطوارئ بعدما بات غير قادر على تلبية متطلبات الطاقة المتوقعة.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/naya_foriraq/80853" target="_blank">📅 21:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=mkzoaC357OM9f2MVpIT7vzGgNmf0rYYnIX8rZp2PGp9hSl4eo--xThaCIFYlHCF_shZKxEpWJen9Eoe5OjnC4ugjbe6hEhG_79AcNH-nZWZN2gM3brjN7dKaQMpqiOwOkKWK46immVo-egkEJ-p0dLfDTw18VrIzqaNqpuk2XBTi_PMb5NayoUkqF6LczU9kVmbmGDAUTNqUfjDyqk0ZEuw7flgnHe8M6QLzhtiKZ3oRhV1Os0J1oy1uxbWlNAMpzDzL_7hL0Dn-SY7u36EY5NAjysfbf5z8DqX51fkwLb0nf6oPaQsWYLMuaGMFWoeUmhiboJsCyYfslbPDi6U2QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=mkzoaC357OM9f2MVpIT7vzGgNmf0rYYnIX8rZp2PGp9hSl4eo--xThaCIFYlHCF_shZKxEpWJen9Eoe5OjnC4ugjbe6hEhG_79AcNH-nZWZN2gM3brjN7dKaQMpqiOwOkKWK46immVo-egkEJ-p0dLfDTw18VrIzqaNqpuk2XBTi_PMb5NayoUkqF6LczU9kVmbmGDAUTNqUfjDyqk0ZEuw7flgnHe8M6QLzhtiKZ3oRhV1Os0J1oy1uxbWlNAMpzDzL_7hL0Dn-SY7u36EY5NAjysfbf5z8DqX51fkwLb0nf6oPaQsWYLMuaGMFWoeUmhiboJsCyYfslbPDi6U2QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:   بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/naya_foriraq/80852" target="_blank">📅 21:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
🌟
مصدر إيراني مطلع:
مسؤولين أمريكيين كباراً شنوا، على مدى الأيام الخمسة الماضية، حملة واسعة النطاق لثني الدول عن المشاركة في مراسم تكريم القائد الإيراني الراحل. ووفقاً لما ذكره دبلوماسيان عربيان -اشترطا عدم الكشف عن هويتيهما- فقد ناقش ماركو روبيو الأمر شخصياً مع نظرائه من خمس دول عربية على الأقل. وتشير التقديرات إلى أن ما لا يقل عن 13 دولة -بما في ذلك ثلاث دول من أوروبا الشرقية، وخمس دول أفريقية، ودولتان عربيتان في منطقة الخليج الفارسي، ودولتان رئيسيتان في شرق آسيا- قد قررت عدم حضور مراسم تشييع القائد الإيراني، وذلك بسبب الضغوط التي مارستها الولايات المتحدة.</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/80851" target="_blank">📅 21:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGd4FdU131nOQVQeZuDuSFLEkCsrFtHE_xVxQP4gP5W_AhKCJIQqK8b9xEQQ06Vq0m8VF3jXIpux1Pb3oNHFxcL-suwL5LobV0UuEWzz0NVG8tWf5XifTF_W8u7qs9uSr4hdjwya7qkyFyAVYutv5W5t8DFUfq8zg5zuBoi3wuXJLpEjPkEWdcJofmq9rMRQFo55ZjNQ_tzCZmPp95e2_uBZwfhskT8GfSJH61f_8Y9UK7Qv6V-7Zk9619vSB7xe-AOu--89nPs17qBMAhFCcGHVLbEXPPc1ml3TgYVBs_VpH8-fw9zc3IvN53FQBoNpVDn8FRTOoJ2EA89nw1fRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/80850" target="_blank">📅 21:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=HoSiRdKEeHPCI9mo94j7tmJ-5wBbLX-lLu1R11LbTxz7oQLLqFqu9XhnjQMzMyT5MXmTPC2zdiAyrxnK4tt2ZGnHZxXzhpfgoXm2MgcqodBQWRbUKi9rtkHpbzhvujtN_RClMK2L_RLw8FRfT19BsmWTjFTDJxh5awkdS8H8NwW1e_lC5RCTd_tCQCnXtV3CAxPZea96tTDDkq_wmQiMG2f8xJKepTMezHI-Mfgs04Pv8cU5hYcpIt3aAYJDVlEOCUa_ccs7ti9klbrKYKZiKHNHiYoNXgYIbeisdW2NR609QiLSoxL9aA9sCPGimMQg66k_hl2PIGAIJ9wx0myygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=HoSiRdKEeHPCI9mo94j7tmJ-5wBbLX-lLu1R11LbTxz7oQLLqFqu9XhnjQMzMyT5MXmTPC2zdiAyrxnK4tt2ZGnHZxXzhpfgoXm2MgcqodBQWRbUKi9rtkHpbzhvujtN_RClMK2L_RLw8FRfT19BsmWTjFTDJxh5awkdS8H8NwW1e_lC5RCTd_tCQCnXtV3CAxPZea96tTDDkq_wmQiMG2f8xJKepTMezHI-Mfgs04Pv8cU5hYcpIt3aAYJDVlEOCUa_ccs7ti9klbrKYKZiKHNHiYoNXgYIbeisdW2NR609QiLSoxL9aA9sCPGimMQg66k_hl2PIGAIJ9wx0myygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80849" target="_blank">📅 21:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/80848" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شوارع بغداد عاصمة العراق العظيم تستعد لأكبر حدث بالتاريخ</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/80847" target="_blank">📅 20:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80845">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_BIDEQuY4THyYro6hIyFP-Sz1Y1Zoo7s-mzQajRhLkj17Ej7qH_5K5wDpjedJBUaRxboGeO24QtVmPTZNkje4LvnnL438CdDBbLRiGTlx6LEylPtBD1bKSsQfSrmwwi4_r5B2AUqwLPSNrrEO4-qrbY_xn0Oxnucbo6ZZ4686lNjpS-WR0nkuOU1JU2dftEU-GiXj47dAw2XF4mTLk-HnfK5JCtWEBDxpdxa34agdaun2-Rji-qjEdBshPO4PigRQWfYTlPKexeelPPnFfbrINUfEYSqCPFzW1atiRc9XGWHcPriiqStqf_NSR-nxNSLPYRSQ8Z00HuTcH0rueFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kp2COK2q_Q5Ad9acjbBGFTQ9OpzINX3Mf3NyniAigNHRBhiGjkSTv_JOCsKwARyS4vMrXa8mfCZfF5UtaHE-qCNzSLd3R-wcA7h1-FruWbEdo5upuOlBNZ55VCXo3oZ1iqxqhEGVJxYwQLfOnrY5_GkaDZwwkja3Sof-0HLwVJE7u_w112SQas7zaeHyTSCPetj3Art18LCw_ybe4UmEAirBRaRiCgqwsxCxeOd_k3slN0kJaniz3-cQeQcZ4CMdl_IXojkQ97sJc4wsS1kD6mDl6dWgatspNapbMHKA-b903jmsNq_g1MBQQUegn8gboBFgZwuQt_Ts_YN0kAoCNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80845" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80844">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=a4tNQQdnLriurEnhfLFAnpcOP2DhDMZrrBI17aWptnrx42PUcU-3TZHhbzsR-ugn-FKCVW1RpCunplqBP6VWS48lvGf2bHukmOoaDRru6lMAjkpEiXOcQc4pERC-SiJRYW2Iuv2JRvB-pWVwp1bJnNUJEnnihOsis45BHgnSPlU37_AX0ICmayt6Vk9ZifN-2ZStU79HD5h8oRzZKfW3WmmQXAJqlfrdkJJgPhAAaKg8TEzfH3bpTtA2hWOkJs1atpwcH43xe38XsZWBaFRxh0gdY0FaQD16ZpTl_atUoH4O9BYw0cDUR1FLp1pl1kMwBPRK4jHKplcHZkoA8My44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=a4tNQQdnLriurEnhfLFAnpcOP2DhDMZrrBI17aWptnrx42PUcU-3TZHhbzsR-ugn-FKCVW1RpCunplqBP6VWS48lvGf2bHukmOoaDRru6lMAjkpEiXOcQc4pERC-SiJRYW2Iuv2JRvB-pWVwp1bJnNUJEnnihOsis45BHgnSPlU37_AX0ICmayt6Vk9ZifN-2ZStU79HD5h8oRzZKfW3WmmQXAJqlfrdkJJgPhAAaKg8TEzfH3bpTtA2hWOkJs1atpwcH43xe38XsZWBaFRxh0gdY0FaQD16ZpTl_atUoH4O9BYw0cDUR1FLp1pl1kMwBPRK4jHKplcHZkoA8My44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/80844" target="_blank">📅 19:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">هذه أيام الـعـراق التي يعرفها العالم..
🏴
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80843" target="_blank">📅 19:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:
بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي والعلمي والاقتصادي مع الإقليم.
نيجيرفان بارزاني: شكل استشهاد القائد الإيراني خسارة كبيرة للشعب الإيراني والمنطقة. نعتبر إيران داعماً وحليفاً ثابتاً لنا. لم نكن يوماً -ولن نكون- جزءاً من أي مخطط يستهدف إيران. عبّر الرئيس عن تقديره لموقف إقليم كردستان المتسم بالتعاطف والمسؤولية تجاه التطورات الأخيرة، وشدد على توسيع التعاون العلمي والثقافي والاقتصادي.</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/80842" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsWQu3lf_V3FIlxdXcm1EM6ZN5OSA4nO_ChbpYkjZr05TlzcYf8bp-pDn9kzJIL9YfwJaII2JqnIkjWZm0FN40JNXyRGq7u_2GgrYff6hli05nzkcX-82JeNGPyqr_Wc7Qtq8IVl1YtAdGKy4dw5aZfs76e1FYuZKPcm1hKrFqWkSBSYF4bNkQM9ic3_HZsHqsd0ApsvsyVlK2mgW1Kxwz8HnDsljBPGiGbfuQY-XPA-ITS8ZvOGGhkgiuLWwIHSgUjbd1BFJdRnsoiqMrfGuSnPwMksQ6tsPqOpB5dJFnXQlaZS6HYjtgmKZWNjR2OSMze5zRWiisNxybj0itn_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتري مدفيدف مبعوث الرئيس الروسي يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/80841" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYlqfRpQatMhcrbUNPF_tRcQ_62J6GKgDok_JG78q8wtc8VYlWhZWk16XO6i6Kd00M22tRY2NrUSetwvMXOQ5ohh06Bbhj87IRumBB9efYbYjb4a0G8jGaPA2lu6pu0iPj7A7UT7b8QKR9NqBMGjUvp78Jl5dveFnemFPCh-PeC68ysa_xdqZNUcBf-gp9PsSQaOi1DRMaoKtgvF-r0sqcR5jKNPmZvLRFBqjXM6GG3DWRHkgbgA-GTU2VR4g8IrASep5aLzauXvQHzeNXd69wJCpvQ2z_byTU4Er3mlnZSrqWVz4lkr0OmpsM7dGDP3PvgtTXNJuD_Bo96xYwW9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
قائد فيلق القدس"اللواء إسماعيل قاآني" يستقبل الوفود العراقية المشاركة في توديع قائد الثورة الإسلامية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/80840" target="_blank">📅 19:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=NmLqlfTNgExc0Pr7SuOYD8L4soPydjVPqVyAwtnoLjNs1eEInO9vY0uW_KZqMEZri4-8AwfNj1mLng9LHtO0z2XIMHu75RIR-SN9XG73eB-LwFnnO1CWjyEsJVHvAGu716hD7kbakpTgprKeff-B4665PKmEfsg-LcuVDg1kSvr45sW2j-HiFB3aXg0JyzUoJMgIMY7xxuVmEY7LS7Iv62pPFwLsxcucQZFxB3v3Gahf0iFa0JvXFyWtV1kBTNlBBQQLdQQ9X99Tvy0pV75VnrBOKu_VasGI_TIml9aQRdmIEcrlcLT03ru7uWDbhqNG_egJwSO_5TSwJ-4Qouwheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=NmLqlfTNgExc0Pr7SuOYD8L4soPydjVPqVyAwtnoLjNs1eEInO9vY0uW_KZqMEZri4-8AwfNj1mLng9LHtO0z2XIMHu75RIR-SN9XG73eB-LwFnnO1CWjyEsJVHvAGu716hD7kbakpTgprKeff-B4665PKmEfsg-LcuVDg1kSvr45sW2j-HiFB3aXg0JyzUoJMgIMY7xxuVmEY7LS7Iv62pPFwLsxcucQZFxB3v3Gahf0iFa0JvXFyWtV1kBTNlBBQQLdQQ9X99Tvy0pV75VnrBOKu_VasGI_TIml9aQRdmIEcrlcLT03ru7uWDbhqNG_egJwSO_5TSwJ-4Qouwheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق من الإستعدادات النهائية لمصلى العاصمة طهران ومحيطه الذي سيستقبل غدا مراسيم صلاة الجنازة والوداع للجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/80839" target="_blank">📅 19:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الحرس الثوري يتمكن من قتل إرهابيين 2 في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80838" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80837">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
نود إعلامكم بأنه تم إغلاق الاستمارة الإلكترونية الخاصة بمنح الهويات الإعلامية لتغطية مراسم تشييع آية الله العظمى الشهيد السيد علي الحسيني الخامنئي (قدس سره الشريف).
ونود التنويه إلى أنه سيتم خلال الساعات المقبلة الإعلان عن موعد وآلية ومواقع تسليم الهويات الإعلامية، لذا نرجو من الجميع متابعة الإعلانات الرسمية الصادرة عن اللجنة الإعلامية، ونسترعي انتباهكم إلى اعتمادها حصراً.
اللجنة الإعلامية الخاصة بمراسم تشييع آية الله العظمى الشهيد السيد علي الحسيني الخامنئي (قدس سره الشريف)
الجمعة 3 تموز 2026</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/naya_foriraq/80837" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ماجئت إلا مودعاً... سلاماً عليك أيها الحسيني الشهـيد
#طهران</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/80836" target="_blank">📅 19:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef6d3a147.mp4?token=r1FRvz-0kgNEqPpFxa7DgoaM8GOJkVYtQqV35IEWlJLe7N6rMjsdAvJARlVERxGwxPRu3P4rXB0XP7ExhuybU1GHbjZ8Zkywz1GoN_w8ZoQ-HcT3gJffi9HEsmc6WqUebjaHxkDjmCAMzoQD8rLbSvqUvzyHZLhGvD1XrZTDBng6ArScDMSDyQpcqzY1H_cHE0CCMJ_4_tJlNSXTW_aoGCJVjSOW2LDUhIloxQyyYln2frwkdqixqFOanFSZ8uPNBx_YE-QZHTzwJ2nWfio-69dYUsGtQIlwMN_dDY5YeVMlXsuLkB1gwxR7X3p7kly7yCvQpCxOh94lNXZSVsS7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef6d3a147.mp4?token=r1FRvz-0kgNEqPpFxa7DgoaM8GOJkVYtQqV35IEWlJLe7N6rMjsdAvJARlVERxGwxPRu3P4rXB0XP7ExhuybU1GHbjZ8Zkywz1GoN_w8ZoQ-HcT3gJffi9HEsmc6WqUebjaHxkDjmCAMzoQD8rLbSvqUvzyHZLhGvD1XrZTDBng6ArScDMSDyQpcqzY1H_cHE0CCMJ_4_tJlNSXTW_aoGCJVjSOW2LDUhIloxQyyYln2frwkdqixqFOanFSZ8uPNBx_YE-QZHTzwJ2nWfio-69dYUsGtQIlwMN_dDY5YeVMlXsuLkB1gwxR7X3p7kly7yCvQpCxOh94lNXZSVsS7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق من الإستعدادات النهائية لمصلى العاصمة طهران ومحيطه الذي سيستقبل غدا مراسيم صلاة الجنازة والوداع للجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/80835" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
مسير موكب تشييع آية الله العظمى المرجع الشهيد السيد علي الحسيني الخامنئي (قدس سره) في محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80834" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية عند الـ6:00 مساء بعد قليل.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80832" target="_blank">📅 18:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=b6X99J-RNTyseFozZRzDeuP7o8WuR_bHfwUGHNRulPiQKKzs8dTQuskORshJf6vgWn7F71yQDfAu6W_PYHoZ9bj4e8e_k9s0qPupqwprRAp4j83AaBXHa-9gxBzRCQcpTgzrv895Vb9ypyGxutWKD9ttz2gTkfwE5N667VNpTYhbFWkdEXIvpC4Fa2oL2gdZVcoGd8UioED3g33hHPZUtcPt2kkC0-OiNR_yd3opPP22qYhlmVKSOlrOFow7Ld_qfYO0YP1mUHuHaDc9V0AoV9E7iZqzRxMESimR_a69DShFMcPk5Q7OKzX3lDrpsFtHfsG6HcP3JdLgLkTb0woXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=b6X99J-RNTyseFozZRzDeuP7o8WuR_bHfwUGHNRulPiQKKzs8dTQuskORshJf6vgWn7F71yQDfAu6W_PYHoZ9bj4e8e_k9s0qPupqwprRAp4j83AaBXHa-9gxBzRCQcpTgzrv895Vb9ypyGxutWKD9ttz2gTkfwE5N667VNpTYhbFWkdEXIvpC4Fa2oL2gdZVcoGd8UioED3g33hHPZUtcPt2kkC0-OiNR_yd3opPP22qYhlmVKSOlrOFow7Ld_qfYO0YP1mUHuHaDc9V0AoV9E7iZqzRxMESimR_a69DShFMcPk5Q7OKzX3lDrpsFtHfsG6HcP3JdLgLkTb0woXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة التعاون الاقتصادي (الايكو) يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80831" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
هيئة الإعلام والاتصالات العراقية:
نفذنا بالتعاون مع الجهات القضائية والأمنية المختصة، سلسلة من عمليات الضبط بحق منظومات البث التلفزيوني المشفّر العاملة من دون تراخيص أو موافقات رسمية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80829" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=hoo9hUzueq5xxRQa0SgEL0_hQ_rx6hi8kLJCE3ws-oe_6ZrMnjKRAmCpvRvRq-66lyp3ZhM3jAD71UIXH8fArmxi0gNTtwoKkZiHXTtQjKnET36jMOxtkQD_reN3ln8OUImtS2wDQl_CiX-upWWVmXISvjnSQz6CmuGvuDn0aAbh_qdjHsWC2xqwPCslMBCfdOh6-YTltC1b3p1shd7H8DlbYwDl0FwQllWhicp8Dj6WB0eoYyeorMNe5HuCOMqsG9kTP0Q76Rw-W5CjxLqHyio_JBBTIjZ0UOGgtKBy3OL1SjroQ3DRZEpXbusAWS0M5rMvbU9_-OH8cQvJAlD1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=hoo9hUzueq5xxRQa0SgEL0_hQ_rx6hi8kLJCE3ws-oe_6ZrMnjKRAmCpvRvRq-66lyp3ZhM3jAD71UIXH8fArmxi0gNTtwoKkZiHXTtQjKnET36jMOxtkQD_reN3ln8OUImtS2wDQl_CiX-upWWVmXISvjnSQz6CmuGvuDn0aAbh_qdjHsWC2xqwPCslMBCfdOh6-YTltC1b3p1shd7H8DlbYwDl0FwQllWhicp8Dj6WB0eoYyeorMNe5HuCOMqsG9kTP0Q76Rw-W5CjxLqHyio_JBBTIjZ0UOGgtKBy3OL1SjroQ3DRZEpXbusAWS0M5rMvbU9_-OH8cQvJAlD1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الهندي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80828" target="_blank">📅 17:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=Neahk8GmPFHdL_RCsXWvMdbDpyB7nL6sfX71-pWOwM07Wz1T3uicw6vfgmN4POKwpcF6LjSka5qQ8K7FGzNi7sR5Md-DtXJ4sLLa7eDVPyrT_HKHjcejDwSqmJN99eG-pqFd28FwNvp-XW7N8jhVE9cg9Gvy6m_WtqHmliA90nMlZCHdprRFPK3lRCs-tb38hEJCOw9LvPUHGf97EAg2tAwprUWuh2u15vn_m6LUlX-e0FdgTpbUAcfDBIiME87N_JrQNgrg8gJdLqvnzuvUMoLh3FYSxXyic7Sc3gO1wCkMHiNIKBxwqqZW3gEYPYAHoq0cO1QGeTkMlN7QG0THYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=Neahk8GmPFHdL_RCsXWvMdbDpyB7nL6sfX71-pWOwM07Wz1T3uicw6vfgmN4POKwpcF6LjSka5qQ8K7FGzNi7sR5Md-DtXJ4sLLa7eDVPyrT_HKHjcejDwSqmJN99eG-pqFd28FwNvp-XW7N8jhVE9cg9Gvy6m_WtqHmliA90nMlZCHdprRFPK3lRCs-tb38hEJCOw9LvPUHGf97EAg2tAwprUWuh2u15vn_m6LUlX-e0FdgTpbUAcfDBIiME87N_JrQNgrg8gJdLqvnzuvUMoLh3FYSxXyic7Sc3gO1wCkMHiNIKBxwqqZW3gEYPYAHoq0cO1QGeTkMlN7QG0THYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد التونسي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80827" target="_blank">📅 17:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80826">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية عند الـ6:00 مساء بعد قليل
.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80826" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=mE0jLJqlsmjEmDVHTiuKQbLDl2ZfKRIfp0fJDg7TpwIzb-U3JuwsZSx9ma3kWTCJv6ZZXHZG_uTJTrU-gZqiTY4l35Q-pGacmibHNf92L4pZsUBsKtw08WTuL1cEdj_Y-ePKeex7XZv0zl8eMm8tQp1Btsh57SuF2CeLBvf_38Xq-IiXZPO6n2EhvUSwVI0sJU8nbwQJDOyYjzTGAgscNTAAfm9GkWoNQyZD924c_d1LjCyUBxqS2gJCKyUtlpgnglYfKAfV4sLGkzh7HUPMTnMOfINYEPLrHU-UrKe9A4Qg2D2-x70oi7JjcKH2811r5GNHV38EScRZrlJ8HF3NVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=mE0jLJqlsmjEmDVHTiuKQbLDl2ZfKRIfp0fJDg7TpwIzb-U3JuwsZSx9ma3kWTCJv6ZZXHZG_uTJTrU-gZqiTY4l35Q-pGacmibHNf92L4pZsUBsKtw08WTuL1cEdj_Y-ePKeex7XZv0zl8eMm8tQp1Btsh57SuF2CeLBvf_38Xq-IiXZPO6n2EhvUSwVI0sJU8nbwQJDOyYjzTGAgscNTAAfm9GkWoNQyZD924c_d1LjCyUBxqS2gJCKyUtlpgnglYfKAfV4sLGkzh7HUPMTnMOfINYEPLrHU-UrKe9A4Qg2D2-x70oi7JjcKH2811r5GNHV38EScRZrlJ8HF3NVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الماليزي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80825" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=QEHN3N6ZeYqZq98YuGRUbBRy5SYb6Ubz9lfhDrMMy-ZY0t5XfK7xRiOKNoWR3bHCzd2V438364OXuaC88TeUJx99TlYrFQtzVhEQ1K1OiJApcI4l-mDciYXlLd46FGYo6UoCaGYPE9lAQIdZubNQIfBC3Xeu9pvSFN-KkjTBSPQFZMx0ltdo7yZAptRI8k5QnAdgNyCH_qUqBcmhAXD5jhhliEHwigW51Z8CXP5mLeTgC0BAKBfuzR42pT0qXtPPc_bKLr3TvmSmrKyjpKpaCPJzCW8X4E5fxLWwf2w6-_aTGhX2g8VQL6qg7m99nr0HvqdHcHaAIBKLI1knrTqbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=QEHN3N6ZeYqZq98YuGRUbBRy5SYb6Ubz9lfhDrMMy-ZY0t5XfK7xRiOKNoWR3bHCzd2V438364OXuaC88TeUJx99TlYrFQtzVhEQ1K1OiJApcI4l-mDciYXlLd46FGYo6UoCaGYPE9lAQIdZubNQIfBC3Xeu9pvSFN-KkjTBSPQFZMx0ltdo7yZAptRI8k5QnAdgNyCH_qUqBcmhAXD5jhhliEHwigW51Z8CXP5mLeTgC0BAKBfuzR42pT0qXtPPc_bKLr3TvmSmrKyjpKpaCPJzCW8X4E5fxLWwf2w6-_aTGhX2g8VQL6qg7m99nr0HvqdHcHaAIBKLI1knrTqbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الصيني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80824" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c6119361.mp4?token=qh70bulOEQ9_ISFD_IIWbRkBmvt7euszhVdEROX6Vl6uQLT-MhHmnMjO5awtShSQJ8v4mNUmem-kjsgVUg-JTaQz3wnYipMcTYS4HqqGgJGITmhtsgdBcNhBEp8KnGG-JiMH_pUInhX06kGl-zXf1JSg4fMIimEGEFju3bxCxHtambDLeMrhRRk6Z75w9DYbkUlDUxBSKbwF2jUdh42EAJZkFcYZ5JIzfVvclw31iDgWuy8xZ05FBRsmS9zDuK54YptOLiI-DGeHopgHDOFoemGDC4-G5gVDYM9jyYCKjA-rO_K_dNE7-mHe9_Mf1NRVUN71EodstfGOPM_ipM4N8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c6119361.mp4?token=qh70bulOEQ9_ISFD_IIWbRkBmvt7euszhVdEROX6Vl6uQLT-MhHmnMjO5awtShSQJ8v4mNUmem-kjsgVUg-JTaQz3wnYipMcTYS4HqqGgJGITmhtsgdBcNhBEp8KnGG-JiMH_pUInhX06kGl-zXf1JSg4fMIimEGEFju3bxCxHtambDLeMrhRRk6Z75w9DYbkUlDUxBSKbwF2jUdh42EAJZkFcYZ5JIzfVvclw31iDgWuy8xZ05FBRsmS9zDuK54YptOLiI-DGeHopgHDOFoemGDC4-G5gVDYM9jyYCKjA-rO_K_dNE7-mHe9_Mf1NRVUN71EodstfGOPM_ipM4N8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الامين العام لمنظمة B-4 الدولية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/80823" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=MdCz2pgbYwQRpRzQlZsQMrrEukFFFjnQAB9aVCwTQJ2GqtlvBQZDLkwxxNhNQS1EeygbUWp_5O9yxOt1PIfMkLB99Kdl3UKNWR9g3LntSV7Xc5d8IrXtdLVmEhUf34t9_VSovnWI8xuwh128frZt-FKpfK2dd2eV-n2uJXow_erAPq6gTLsAzkylPkrrq8DSyz-grTSIj79OmxzUHkwbialCJZrq-d2KxBasa13qOc-V8nDazIqYgFgBAeWXCxsDnbohXauxXCZapSJ2i8w0B9s2pEVUsXC2PX4XR-erXvbqKpNgmc_XTbWIjRzYuqBg9TkmqJsyAG80dKuMM0llgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=MdCz2pgbYwQRpRzQlZsQMrrEukFFFjnQAB9aVCwTQJ2GqtlvBQZDLkwxxNhNQS1EeygbUWp_5O9yxOt1PIfMkLB99Kdl3UKNWR9g3LntSV7Xc5d8IrXtdLVmEhUf34t9_VSovnWI8xuwh128frZt-FKpfK2dd2eV-n2uJXow_erAPq6gTLsAzkylPkrrq8DSyz-grTSIj79OmxzUHkwbialCJZrq-d2KxBasa13qOc-V8nDazIqYgFgBAeWXCxsDnbohXauxXCZapSJ2i8w0B9s2pEVUsXC2PX4XR-erXvbqKpNgmc_XTbWIjRzYuqBg9TkmqJsyAG80dKuMM0llgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مبعوث منظمة التعاون الإسلامية يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/80822" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979449faf7.mp4?token=fNUx9zdLQ7t4-ugnCoVsL7dzkdHJPAYxY0rRYZbYXaJe6g_kK7c9cAdZiUPLIRH2wXHHxph4nfTaWykI9qOCbmQJaN49i2tp_zrokoagslFs4Q_fm4oU7tFOxtyM4qXUG1EobMFNAWZKCcMfXuOnHbyJriYsG6Dj605UV81Gw7Ccs_o5YvH2c_E9WkNlJ4JNnRKAqXjMq6Pn5bfHkhMnr-rTc_AN1ACLhso7YpHubOs9kNH_4h9b7fMx7KnKf3Sa-3fkgBIsMTxytq-jfLLyMhYEUoKdrK_7Kz4oHWFD09xx0HreDwiIh9Zm2oT5-pa-X2PuYi4CT4mjycCfZWBYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979449faf7.mp4?token=fNUx9zdLQ7t4-ugnCoVsL7dzkdHJPAYxY0rRYZbYXaJe6g_kK7c9cAdZiUPLIRH2wXHHxph4nfTaWykI9qOCbmQJaN49i2tp_zrokoagslFs4Q_fm4oU7tFOxtyM4qXUG1EobMFNAWZKCcMfXuOnHbyJriYsG6Dj605UV81Gw7Ccs_o5YvH2c_E9WkNlJ4JNnRKAqXjMq6Pn5bfHkhMnr-rTc_AN1ACLhso7YpHubOs9kNH_4h9b7fMx7KnKf3Sa-3fkgBIsMTxytq-jfLLyMhYEUoKdrK_7Kz4oHWFD09xx0HreDwiIh9Zm2oT5-pa-X2PuYi4CT4mjycCfZWBYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة التعاون الاقتصادي D-8 يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/80821" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80820">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=HUSg-bLIxXUYCrPgSySd8-GbylNDRP3G9wKhY4bG9if8oq4_7OK61Uf3y5-Bq9MtVnDQUsqMDbcxqKF40bQLS5SsmlJEQA5RG8Ohp2B2pLY_-BcDSjOLHvizSjH8W5guy9E4kZgrX08b_lfKE26Asstd1tHauuDZ-dCIxbGi1yPo3OLZy3gH5N7UNxkWF7W1PIx-MqVjLe10ldaZwv3I-zaF8cgZiG1Oo4F618Zs7lIC7ARli8ZFQrh70vkoNravnuFE9myDa6MBLjvP4RCrtleP96nI-rWFUErkWNcFHxc2VnS6w5ghxBkLoabWvvp1F_byqMXodHisCTVialS6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=HUSg-bLIxXUYCrPgSySd8-GbylNDRP3G9wKhY4bG9if8oq4_7OK61Uf3y5-Bq9MtVnDQUsqMDbcxqKF40bQLS5SsmlJEQA5RG8Ohp2B2pLY_-BcDSjOLHvizSjH8W5guy9E4kZgrX08b_lfKE26Asstd1tHauuDZ-dCIxbGi1yPo3OLZy3gH5N7UNxkWF7W1PIx-MqVjLe10ldaZwv3I-zaF8cgZiG1Oo4F618Zs7lIC7ARli8ZFQrh70vkoNravnuFE9myDa6MBLjvP4RCrtleP96nI-rWFUErkWNcFHxc2VnS6w5ghxBkLoabWvvp1F_byqMXodHisCTVialS6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد تايلاند يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/80820" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4313681fa.mp4?token=mP0RoHYdgKVdAfmpwATz9jb3-GZYIWjKic3qt7AR_GxgGNqrYfwukzB_lPIqAO8UlFyTm4wcn27tR2JEfrTrUbF9ZYraeqY2o_t5PTP9RGks--OhIGsiIT_lyeELKL-hMI3Mc1SOVVMFNMmHJESuBDmj1PDZbB-5ngFrFrUPUgjf5PyRQkd2NAeRbTJoDLpAk5oeC0GccGPF8GW75v_PaySsjfLNFIDG4vd68VSC1zSbTklseKfI4QO50s0asSG_uYRrJz6nlinUvxgA0LPZw5ky56odOI0hf8Vy4CM_EP9mi7RorRkTrSw1A1Jc600b0HTMx3vnyavgvfxhZzTw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4313681fa.mp4?token=mP0RoHYdgKVdAfmpwATz9jb3-GZYIWjKic3qt7AR_GxgGNqrYfwukzB_lPIqAO8UlFyTm4wcn27tR2JEfrTrUbF9ZYraeqY2o_t5PTP9RGks--OhIGsiIT_lyeELKL-hMI3Mc1SOVVMFNMmHJESuBDmj1PDZbB-5ngFrFrUPUgjf5PyRQkd2NAeRbTJoDLpAk5oeC0GccGPF8GW75v_PaySsjfLNFIDG4vd68VSC1zSbTklseKfI4QO50s0asSG_uYRrJz6nlinUvxgA0LPZw5ky56odOI0hf8Vy4CM_EP9mi7RorRkTrSw1A1Jc600b0HTMx3vnyavgvfxhZzTw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد ميانمار يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/80819" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=MyLnVDV34vkqjJY-aQY4ARX9Z4JYhbLRg6WrXN3dX0xRqDMJgMg6jprSc9TaYf4P_QaHLFl0OlMPMEv29tx2VDhwqazsTWdVh7brkl8Ic-OhkEd52e0MyKV5KPs8XWyhS1qYlKh-bw5CId8eiGrgTkTnp9X3wARFfAGncsowSzwHd3q9UbcJM72O0IaqpyR1s0Bya6r9BPjr5usqiTBY4QSHW1Aq9rDaEeNHhrajFnVB6vgw1vPlgRgsA-ZjCc9o-l_2EcQgH_8qd9RO009beHXW6Twvw2QbqfXgHcFHbKsvdq66EoSD13zSEoZNk3EehZNinIzZuJg7Xg8ItyQ9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=MyLnVDV34vkqjJY-aQY4ARX9Z4JYhbLRg6WrXN3dX0xRqDMJgMg6jprSc9TaYf4P_QaHLFl0OlMPMEv29tx2VDhwqazsTWdVh7brkl8Ic-OhkEd52e0MyKV5KPs8XWyhS1qYlKh-bw5CId8eiGrgTkTnp9X3wARFfAGncsowSzwHd3q9UbcJM72O0IaqpyR1s0Bya6r9BPjr5usqiTBY4QSHW1Aq9rDaEeNHhrajFnVB6vgw1vPlgRgsA-ZjCc9o-l_2EcQgH_8qd9RO009beHXW6Twvw2QbqfXgHcFHbKsvdq66EoSD13zSEoZNk3EehZNinIzZuJg7Xg8ItyQ9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزير الداخلية الباكستاني:
في إحدى اللقاءات، صافح القائد الشهيد يد قائد الجيش عاصم منير بحرارة وقال له: "أبناء الإمام علي (ع) لن ينحنوا أبدًا."</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/80818" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=Al5gLhkJHW9SxPEWSKzZKIl_ecY-xEwEPnhm3WzL2V_LENWtSoxdPCAbFgL2hzgiEVZVKdOueNrOtXmV3BxvjrqNQA1ZlhwpZ98R--T7FLQjNdRQ1n8TtOuzxFVSwb1Pv7lf5ytyeUDcYTPIgYu2sVOM9AVe7Ha5XFZZBpIy5S1tA8kuXnTQ1E5GsGVdYSmL7YUembReSpH2xXeDdYwvzel8O3CGmfiXGsCAIjbW-10AkWFLJfyBPFLKtaB-fVDlvx5pmhqN3lEU3wWZEcDzXFPQ_fQQQQ8MdpQx-iFHalaJUWyKsROLvclEy80tkoDEvcprENuljSCRvPFo3t2iUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=Al5gLhkJHW9SxPEWSKzZKIl_ecY-xEwEPnhm3WzL2V_LENWtSoxdPCAbFgL2hzgiEVZVKdOueNrOtXmV3BxvjrqNQA1ZlhwpZ98R--T7FLQjNdRQ1n8TtOuzxFVSwb1Pv7lf5ytyeUDcYTPIgYu2sVOM9AVe7Ha5XFZZBpIy5S1tA8kuXnTQ1E5GsGVdYSmL7YUembReSpH2xXeDdYwvzel8O3CGmfiXGsCAIjbW-10AkWFLJfyBPFLKtaB-fVDlvx5pmhqN3lEU3wWZEcDzXFPQ_fQQQQ8MdpQx-iFHalaJUWyKsROLvclEy80tkoDEvcprENuljSCRvPFo3t2iUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد صربيا يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/80817" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80816">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8718f7b7a.mp4?token=ss2aPA-5bJj09xWrTHGHsBCDKdhoqYLKXvXD-Efdx7hPh7b5gMerbdNRp7jW4Sk5QqUxzsDojqQpZ6JRtqK-03WRK0CPOH3QfAf-sM4gn-r3nmR3FOexYnFhpd5kPyiz1r9eL0pbSDqb0fbPAqAdWUt-zUGxPd-Qef6l1QUXdbnkILgDtvI3SesNh8VmeF1YdQ6__6cnEyGEju-u1EvYOerZePhm1u3yeeKxlp8RwqBncunLscrLyrZAaWxapp-aPKS36B42Z_bBAaQIKb0SObIudUlc7R1S5KpALGYl5omTnECh13x-QVYWcqT3warB9dXm5AcwX5vhbPPc66xcZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8718f7b7a.mp4?token=ss2aPA-5bJj09xWrTHGHsBCDKdhoqYLKXvXD-Efdx7hPh7b5gMerbdNRp7jW4Sk5QqUxzsDojqQpZ6JRtqK-03WRK0CPOH3QfAf-sM4gn-r3nmR3FOexYnFhpd5kPyiz1r9eL0pbSDqb0fbPAqAdWUt-zUGxPd-Qef6l1QUXdbnkILgDtvI3SesNh8VmeF1YdQ6__6cnEyGEju-u1EvYOerZePhm1u3yeeKxlp8RwqBncunLscrLyrZAaWxapp-aPKS36B42Z_bBAaQIKb0SObIudUlc7R1S5KpALGYl5omTnECh13x-QVYWcqT3warB9dXm5AcwX5vhbPPc66xcZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دمتري مدفيدف مبعوث الرئيس الروسي يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/80816" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fc63366.mp4?token=CUAXa6JgQucU3y5LAStxu9YF7SZkyt0LFn_ZWe149OV_yOVDtTJAuh3PFWmG46Uerf54cyYORuL7KCTRUVW3SFaaSZDG5RDOfXjLEeXN9DmNE-29b_AacOTskVB4PR-0mNBm4n4MUhzhZXARgpngx7jcMjDBKfFtlsDIT_6V4FkBST8Hvuv8GRsZIeMGhHNWFBOB44yOJXFOpualDvcwQnFnp3iOZyDQ3sACo_OY1RGmq5QYj1uzyzvasdx8I9gkgsUQjbsZGfksu8mrlZX-gHR0Lz8VxVPnDaGsZGyWl7f05tZKZ-KObwoDkfM0BU7FMhzAo0YCSgdk6biKOH689w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fc63366.mp4?token=CUAXa6JgQucU3y5LAStxu9YF7SZkyt0LFn_ZWe149OV_yOVDtTJAuh3PFWmG46Uerf54cyYORuL7KCTRUVW3SFaaSZDG5RDOfXjLEeXN9DmNE-29b_AacOTskVB4PR-0mNBm4n4MUhzhZXARgpngx7jcMjDBKfFtlsDIT_6V4FkBST8Hvuv8GRsZIeMGhHNWFBOB44yOJXFOpualDvcwQnFnp3iOZyDQ3sACo_OY1RGmq5QYj1uzyzvasdx8I9gkgsUQjbsZGfksu8mrlZX-gHR0Lz8VxVPnDaGsZGyWl7f05tZKZ-KObwoDkfM0BU7FMhzAo0YCSgdk6biKOH689w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد كوبا يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/80815" target="_blank">📅 17:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df855a6622.mp4?token=Gixh_XDifjqD65cU3SPzj_spcirdxPH3ZEqAoyM1AR3HIb3lTxqNtFIDdCav5C9X_Rr4yU9C22qaVKwXfOKmo_VqbQfY-fCpfHYSjuAbzyiuQj-jyB4NdKcBqbHip-nIGJOVPG4FvmUfFcvnyw4bOgfz3RcA4-wTfI59dHB9QKBBhxO2S5z5kflZIN6YuO2ZakUlLhRaRVILMkTjqUza7kdvZdjMLFptoqsnYBgTQqbvBCOiWtqIH3mM1MrevcprF_F1FqCqG9U1rELkCjoH2YrKsmS_G_rWIMQ-jhisC9NXk1FvZPlU10rXrNdMqwMIfvAMhIZzRjLGgKBaLvbjNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df855a6622.mp4?token=Gixh_XDifjqD65cU3SPzj_spcirdxPH3ZEqAoyM1AR3HIb3lTxqNtFIDdCav5C9X_Rr4yU9C22qaVKwXfOKmo_VqbQfY-fCpfHYSjuAbzyiuQj-jyB4NdKcBqbHip-nIGJOVPG4FvmUfFcvnyw4bOgfz3RcA4-wTfI59dHB9QKBBhxO2S5z5kflZIN6YuO2ZakUlLhRaRVILMkTjqUza7kdvZdjMLFptoqsnYBgTQqbvBCOiWtqIH3mM1MrevcprF_F1FqCqG9U1rELkCjoH2YrKsmS_G_rWIMQ-jhisC9NXk1FvZPlU10rXrNdMqwMIfvAMhIZzRjLGgKBaLvbjNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
نائب الرئيس اليمني يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/80814" target="_blank">📅 17:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3584cfed.mp4?token=NemkkM7IdjJGFCuDs26_SOWwvfL__VbVVkYdU8sfh-jQm0h99nCfVkXcatrjXel45oohNMVTWUGWcM_n6jSEDsPfzHAA7W8dL-qRv1cJVHrqSAxaq5TVaYYsq8bebPQwJTRM09d45DX8qa9pO22wiTvjO27zWpZeZditVpFGqMzCdgL6VcUwxZNvjr8sjI6BrZesvIoZEu3O6aOFT_mmAaxzalW7rD6uWUlJOX9uNIEXrxR7ZED1zMcZn0TYZFZEW3QCl8mQWzpaWu4Osj9hIsBkYA1179yOuJbMSlzvEBFk7LNcnLYcExJNThkTUB8sPzCVXm5bzFQpYyoKQiFngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3584cfed.mp4?token=NemkkM7IdjJGFCuDs26_SOWwvfL__VbVVkYdU8sfh-jQm0h99nCfVkXcatrjXel45oohNMVTWUGWcM_n6jSEDsPfzHAA7W8dL-qRv1cJVHrqSAxaq5TVaYYsq8bebPQwJTRM09d45DX8qa9pO22wiTvjO27zWpZeZditVpFGqMzCdgL6VcUwxZNvjr8sjI6BrZesvIoZEu3O6aOFT_mmAaxzalW7rD6uWUlJOX9uNIEXrxR7ZED1zMcZn0TYZFZEW3QCl8mQWzpaWu4Osj9hIsBkYA1179yOuJbMSlzvEBFk7LNcnLYcExJNThkTUB8sPzCVXm5bzFQpYyoKQiFngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سعودي يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/80813" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=TFgcgnvtGxROiq-78JQ0SNE7q3AGXi5Qsa3NRy98jE5LAJvmd-sJ7VfQL4jCdxVAcADc6cfFjDkKy7jT8D1anMTB9M81QuEC9qefmSsYwiG4Al5-riJg8E86fSQ0Zx9KNh3b5aO6gmS_ofOjZkKnUAVwkgaQmBcOWJHu2XGyd0tmgOvFUvN-OJK63WJw7BhkjV8IpdcweomlHSZdiHxgAGnId2yS8QSb1nLC14vYVvLXVjpOTOUDlHWX7vc7uBqv1WL4woBPQWK5kInn7qME_5P01E53x3o4F_F2HAZVU5GDl4T9jiH67YZsvYfPRr3evSkszdYVqzLi2ZmTm9XyUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=TFgcgnvtGxROiq-78JQ0SNE7q3AGXi5Qsa3NRy98jE5LAJvmd-sJ7VfQL4jCdxVAcADc6cfFjDkKy7jT8D1anMTB9M81QuEC9qefmSsYwiG4Al5-riJg8E86fSQ0Zx9KNh3b5aO6gmS_ofOjZkKnUAVwkgaQmBcOWJHu2XGyd0tmgOvFUvN-OJK63WJw7BhkjV8IpdcweomlHSZdiHxgAGnId2yS8QSb1nLC14vYVvLXVjpOTOUDlHWX7vc7uBqv1WL4woBPQWK5kInn7qME_5P01E53x3o4F_F2HAZVU5GDl4T9jiH67YZsvYfPRr3evSkszdYVqzLi2ZmTm9XyUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد غوام يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/80812" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb79238e21.mp4?token=lZc2fNMzju8y1A5kcvGQpXal-KnpzqkpKeH0w6s_2Gx-LEWDatIwyYjcEK3HkA0Pp4xyYcum9FuPwCTktAdw7E3yU0Ufkg2Ja3MH90Xh_x-LKBDl0WgJU0Iy_M0FSYGtRfJBBYNlPaB9vt4TxDqgNqz5LR_yJ4TRE-CgrKkop8W-lD1JtvlZ3BOPez6p15x9LsmCOpQj73-pK0yzgXREHwi-F_JVgYVb6lVSUcR88Fk5_Q5MU3E_zqy88HrJZqHh4VOfBDi17VAkSEoqz1y_wxnESmagMQsyMZd8McNVHs7lRTXDPVRo4ZFFDksgx6xMW6HPEOVhGU2NvjAcY9GXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb79238e21.mp4?token=lZc2fNMzju8y1A5kcvGQpXal-KnpzqkpKeH0w6s_2Gx-LEWDatIwyYjcEK3HkA0Pp4xyYcum9FuPwCTktAdw7E3yU0Ufkg2Ja3MH90Xh_x-LKBDl0WgJU0Iy_M0FSYGtRfJBBYNlPaB9vt4TxDqgNqz5LR_yJ4TRE-CgrKkop8W-lD1JtvlZ3BOPez6p15x9LsmCOpQj73-pK0yzgXREHwi-F_JVgYVb6lVSUcR88Fk5_Q5MU3E_zqy88HrJZqHh4VOfBDi17VAkSEoqz1y_wxnESmagMQsyMZd8McNVHs7lRTXDPVRo4ZFFDksgx6xMW6HPEOVhGU2NvjAcY9GXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية حصلت عليها نايا توثق قيام الجيش الامريكي باطلاق صواريخ هيمارس من الاراضي الكويتية باتجاه الجمهورية الاسلامية بتاريخ 28 من الشهر الثاني</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/naya_foriraq/80811" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=pfHEFOf9fJTPPREWxEQLqE8xroZGrZfwL6fCKgRSipVPAKqgYoSoojruwdr7FDXNozf5V6l6naqSM4V6L3ekopvvoNNk5tCCaAAY5F7eei0BxDBw2sgfeOvLUrjqrsk5AEZ0NaYTzo7vRbL5gWCW-r45L-h6U0jkiTf5OVBgCH1cZQPR8oBzcS0CtV0Cjv0MUTg0YJb27buorWjxLybM7M3c7PpBglcxKtyqwiwhJqCQs5RrVU1Xw0hLfnM0jKRwaKVXu_KntY5KJbSnm9LvLCpCnYeqpBF_o5IPvx6YHK0H3aWdtYJrXPlCY_agRJp333h_QXBEM7mtwSfWXr9Upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=pfHEFOf9fJTPPREWxEQLqE8xroZGrZfwL6fCKgRSipVPAKqgYoSoojruwdr7FDXNozf5V6l6naqSM4V6L3ekopvvoNNk5tCCaAAY5F7eei0BxDBw2sgfeOvLUrjqrsk5AEZ0NaYTzo7vRbL5gWCW-r45L-h6U0jkiTf5OVBgCH1cZQPR8oBzcS0CtV0Cjv0MUTg0YJb27buorWjxLybM7M3c7PpBglcxKtyqwiwhJqCQs5RrVU1Xw0hLfnM0jKRwaKVXu_KntY5KJbSnm9LvLCpCnYeqpBF_o5IPvx6YHK0H3aWdtYJrXPlCY_agRJp333h_QXBEM7mtwSfWXr9Upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس النواب الباكستاني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/80810" target="_blank">📅 17:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0472153.mp4?token=EGQ6Awavo0yQhFrj4DWwU7-sDxjMc6yVS4HFguTdSqzJWrV4HkZgIyebgTOeky9s1njIKmkMo3oBeST0_NtiFlO-QrREINZjA5ZD31H9sKvANZ4yKSXsZ3ydrz6M1VhwfOlJEsdceLW2lM1xqP5YacbHnzd_bdApW4LBIzjQ0nhqUMio2SHATtH_2Xf4iwTIx0q1tssv2qQoW_6GJi4rU9on2rze-xmaLDhAUXZ6Hjx78y7tZEAL1kTaVC7KIZ_VYomjOwqifj6Gl7dg0sS3GhxUaXOQUpIcAAXlM7X26Qu1iPX2oMlvUaUUewyXWFkS4f_K_SiVnmzw79KUxOQ5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0472153.mp4?token=EGQ6Awavo0yQhFrj4DWwU7-sDxjMc6yVS4HFguTdSqzJWrV4HkZgIyebgTOeky9s1njIKmkMo3oBeST0_NtiFlO-QrREINZjA5ZD31H9sKvANZ4yKSXsZ3ydrz6M1VhwfOlJEsdceLW2lM1xqP5YacbHnzd_bdApW4LBIzjQ0nhqUMio2SHATtH_2Xf4iwTIx0q1tssv2qQoW_6GJi4rU9on2rze-xmaLDhAUXZ6Hjx78y7tZEAL1kTaVC7KIZ_VYomjOwqifj6Gl7dg0sS3GhxUaXOQUpIcAAXlM7X26Qu1iPX2oMlvUaUUewyXWFkS4f_K_SiVnmzw79KUxOQ5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزير الدفاع اللبناني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/naya_foriraq/80809" target="_blank">📅 17:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135827909c.mp4?token=rwgTnvVO60ned8Cw66vac2ot982dxuKAvc8mcNSPWCC-FNzNWsHWRa8hR62y_5oiViDH1b8Vmgg1wTHwmy6uoJVSM2F4UmyiPdaukLlHe028poSNTsBwC5_6QDbqR7CmJCAFq4emkol45TWRBQzGN_OA748cSOqBCleDZdPm3ncWTIEXVObEQwQtVE2l7GgfvI2Zkn0fteey9gaoQInx4deJZXXHYSnKIpFXyn2h-h9xqV2IZN9WzH2ci-3Bnj219cHFmwBAN3b8JFhqeoKCIdorYYObYxndE4ReMVsspyISVoGWbt10WiCIRRiSnuJYrTiR-0-Fbi0vcOfN5SrZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135827909c.mp4?token=rwgTnvVO60ned8Cw66vac2ot982dxuKAvc8mcNSPWCC-FNzNWsHWRa8hR62y_5oiViDH1b8Vmgg1wTHwmy6uoJVSM2F4UmyiPdaukLlHe028poSNTsBwC5_6QDbqR7CmJCAFq4emkol45TWRBQzGN_OA748cSOqBCleDZdPm3ncWTIEXVObEQwQtVE2l7GgfvI2Zkn0fteey9gaoQInx4deJZXXHYSnKIpFXyn2h-h9xqV2IZN9WzH2ci-3Bnj219cHFmwBAN3b8JFhqeoKCIdorYYObYxndE4ReMVsspyISVoGWbt10WiCIRRiSnuJYrTiR-0-Fbi0vcOfN5SrZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة شنغهاي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/80808" target="_blank">📅 16:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=chsDBRmo0DXHcgYYH2baYxF9mEkSTj47UNYPFlyPw0vVq1DbZFj51ABLyX04om1HAjMvikYXp8aUYsg6sw_vd-x1ie6azslGxi98DsQ-pDDHzDR9dWrzP46dhHU57oQ-Ia0XzS8DqkiAd9t83XQjuoVhZCZ7Ba-KZoNDpQ_6Gk21weZFggH-I7G9OhFzcGWifzYYfOipZ6t_1a5xYn4K0S4vCJ_UDuENCquChYauryEB-jPqoYyD9_LAnQqp1HJWnWOgCyDGcWvf73dCyuxvVJGOHocYAA1lMCzEO-YFWf3QM2194wg5uY49_mpXJ9-xN2Tnloh6hLhi7EbT2cQ9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=chsDBRmo0DXHcgYYH2baYxF9mEkSTj47UNYPFlyPw0vVq1DbZFj51ABLyX04om1HAjMvikYXp8aUYsg6sw_vd-x1ie6azslGxi98DsQ-pDDHzDR9dWrzP46dhHU57oQ-Ia0XzS8DqkiAd9t83XQjuoVhZCZ7Ba-KZoNDpQ_6Gk21weZFggH-I7G9OhFzcGWifzYYfOipZ6t_1a5xYn4K0S4vCJ_UDuENCquChYauryEB-jPqoYyD9_LAnQqp1HJWnWOgCyDGcWvf73dCyuxvVJGOHocYAA1lMCzEO-YFWf3QM2194wg5uY49_mpXJ9-xN2Tnloh6hLhi7EbT2cQ9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد كازاخستان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/80807" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=eSQOMDQg0bKLPcM8KcBr3TyqKHUlQUV3KZJj2y7JqibGehtN7Fj9amnLgqU85S2JKr-Wvw5qUtMkUqjUyOgle3kJ0UwyQqeLEWBQN6H3R01wUZXnZTcR7EJeZ6k0z7C_EkA53q0uHdeTRMFgnFm40M2Sg20u1vQHMRzxUm4UEvBJ9zANMRDjHbAUM4-T-SvhJhjD-it4OQLAIHrgsHXA7W0x2iAy-cQVTAZDf_nUjqdLAjUq771SZm7SCkcRCrNa5r3nNC1yL1PWyHTr2BFX2iROtJ9tZllU2dQvHLqCpslkdFZrj4tFNOTHEukiyPgp73rhkjGp44qZfz3BaUmEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=eSQOMDQg0bKLPcM8KcBr3TyqKHUlQUV3KZJj2y7JqibGehtN7Fj9amnLgqU85S2JKr-Wvw5qUtMkUqjUyOgle3kJ0UwyQqeLEWBQN6H3R01wUZXnZTcR7EJeZ6k0z7C_EkA53q0uHdeTRMFgnFm40M2Sg20u1vQHMRzxUm4UEvBJ9zANMRDjHbAUM4-T-SvhJhjD-it4OQLAIHrgsHXA7W0x2iAy-cQVTAZDf_nUjqdLAjUq771SZm7SCkcRCrNa5r3nNC1yL1PWyHTr2BFX2iROtJ9tZllU2dQvHLqCpslkdFZrj4tFNOTHEukiyPgp73rhkjGp44qZfz3BaUmEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سعودي يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/80806" target="_blank">📅 16:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e927a24458.mp4?token=tZNGGEWEEGV1sqFoOFzhhgzg5JI46ii4tGPcTWS5BdETPWaQdoqvPBmBVoqQwvsSy344dJ3YEDT2zF7bky4DuvJEetz0Z8JjxSwua-bG755vdJwceSGEYB-JKdp6Gz4C-ma_4eJUIZiJFA4el-0-IqWFkm1EhBZaisaE_oWrJTnGMjWwymyN4Ts5iwuM7rCWQsnSucQS6bejcQRb_sO9BB-GEIWANlUnPhjFSY0sIt-KwLThF7EZEySw5NGbwhHQufOForqRyysu560wKrHhdKyojrELhzRfSn4ZDlV1h4IE53dDal_ofhCU45O07QVs5Nsp8dXf5_qbLNQwZemRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e927a24458.mp4?token=tZNGGEWEEGV1sqFoOFzhhgzg5JI46ii4tGPcTWS5BdETPWaQdoqvPBmBVoqQwvsSy344dJ3YEDT2zF7bky4DuvJEetz0Z8JjxSwua-bG755vdJwceSGEYB-JKdp6Gz4C-ma_4eJUIZiJFA4el-0-IqWFkm1EhBZaisaE_oWrJTnGMjWwymyN4Ts5iwuM7rCWQsnSucQS6bejcQRb_sO9BB-GEIWANlUnPhjFSY0sIt-KwLThF7EZEySw5NGbwhHQufOForqRyysu560wKrHhdKyojrELhzRfSn4ZDlV1h4IE53dDal_ofhCU45O07QVs5Nsp8dXf5_qbLNQwZemRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سريلانكا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/80805" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">إمام جمعة طهران:
طلب الثأر للشهيد القائد هو مطلب جميع المسلمين. العالم الإسلامي فقد أكبر شخصياته، وقتلُه ليس مسألةً صغيرة.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/80803" target="_blank">📅 16:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=chnD_V-foXNFfWecsWslAYgovcoMQ-p31_Qemzn4Dea6s79-nyYG_GNZaZOA8E33RnQEHNJTyW1guKRV379xe_FVX2Fjm-scSiUtcXDd5KzDhkH0_6tNym5sMyLR9GArmOi2HWVAtDwxC9arblJm28sWyD6fQaEWbxNPmV4GMMb0_bqvXik5sE_OYX3oYMDws9woPj2nVi22Vm3kpbbypy_R2JjfS_BMdNB3EkmrAMiqGkSVFKkAPQ__gXE4saSKnIti979W5ywZYhFfCOQ9b6s8ZgzWionIrbKWLDj6DeaGOOEZcy1eW0rlWSRx-el55QN585OvsDiPXiGXNXcG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=chnD_V-foXNFfWecsWslAYgovcoMQ-p31_Qemzn4Dea6s79-nyYG_GNZaZOA8E33RnQEHNJTyW1guKRV379xe_FVX2Fjm-scSiUtcXDd5KzDhkH0_6tNym5sMyLR9GArmOi2HWVAtDwxC9arblJm28sWyD6fQaEWbxNPmV4GMMb0_bqvXik5sE_OYX3oYMDws9woPj2nVi22Vm3kpbbypy_R2JjfS_BMdNB3EkmrAMiqGkSVFKkAPQ__gXE4saSKnIti979W5ywZYhFfCOQ9b6s8ZgzWionIrbKWLDj6DeaGOOEZcy1eW0rlWSRx-el55QN585OvsDiPXiGXNXcG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قطر
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/80802" target="_blank">📅 16:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80797">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBMY1EyoTWZFdVJ7tXjho1NKZjjf364XSCFSqYiuhB5RCR-CYKRU39Dhe1fCPvfSKnGN-HcqF6gt4Luc1M0IAZcuxD4ZBy4GbqeOimjfEHzBB5Ciwi4CZRJO2LxWkYJAjD4rlanK8J96et2N4vYRPGqp4-p14D41f-SWNpTjakRGHYDpQfOTMR5zkZteH7S7Q3hXxeH4jGQApjZRbtser8bFmqI2i-PSQrTy2UDnqPyG1s_s-3AQdkVkriLYd0qCgSgLD9X6eF71gjhmNpVPCadEbNui82k3EWwn7aibGr3dm1wylSDL2T3lTllbn0YKvktk1BzEalHd0qXKrA6qAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwmKojMcbv9lW2dr-s04wgY1V9u6a3LzxdPOxH7LKConEasPyQwTw9THu6NX7k0WOYADP82J3wgFWtK0HQuc534Muo1OSctmBkkcZaKF_y6tZRM4ZGUIxwz9-aHeUQEyHupRzSamtmi2orhviQDHoW_shrmm3228jEu3jyc0VvVGzmAQ44d-XeUzum78B9nkPCi4l0wjOE8hFgkUVfwRbXoyyWY5_E6SlQDQKVzQR_dndHY4VlTPYTG5AAwoShUNABgHybK81m8Zs0elMPP5oPobf7HHbWxdDd5GSzBAMdAuwrWlVjUT4waYLVqD9dX6-uAxU3D4FDrAX38E8D2ElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctZVPE8Gr9E2fPlkXCgXazGLfSOfSaI5fc1DhnFeCo47n_7ba7RUg04lUYhsCj4l843ZGDVHt2YbNKRxJfCRbLCnXQQvZU9o1xk_ll6DUIkPGDkwWEC9ay__iU4fM_DZyaxLMowW3u96KLhLIsTRin6O9dwMdtQTONqb30MJ96wloxi2eiPvQvpCUwiZ_3Yxwy5nFI_vDze4_4xgmuaYfDl2e4Dr2jYymqCGgpqz_JX_QZxBkqB56EeVgYSBD4IU61lMM40XpY4jUgVp-pfZbV3qsjh2mSlTzKLeyFm4ldxXnJ_2Uk2CsM7UtdAdjs17Y0bimnlDcnsSz_vbOsiPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1RNTfOf2TxhULHh0_oykegpsxiy-OZNW4AM314USLZGayHwKr9xPcOy-hOrdK92OkXNNjfbKHQiKnKMl85-VdkkkWAEzwOAJFpVtUXOblyNHOwJwcW1pu-cgw0P6FWXKV2hcmdZksIxy03QEgasApFsjGisW8mAz_3kq7zVxSEpYCvngQmWrIX_6FnAYsFW_K_HOuS47-PohXZKHkj8QbPWA0jtkSW5NHChXPq7Nq3t-dNMG6yCU9noXAQZSGUKbhcfasp1IYVPK0_NNtqylb9G_2JZ_WmZ8qm0-xm5boI4Bi-mpYcjVjZYDZ1O8ipN9uf8Zax8jUsKAVmIWGg88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUuaE36UfQjUoqv6lccMHqFeWQINZsf7hRuR1NJzcOyENYMNCvyxExzeAXsmvdpQQIXtSYR4a1W8axFac6FjtUeo5lIxrxSIa4eL-LvN8C7cHrq32Iz3m7sFU7teZdHzC_X3DNc0v2dg58ji7sLvo_l4g_OxatAxwTKPf3wEq3WT5IqjWlmjh-FR3vzXGgszMhTgZw5hT-HsSjV73oMC1o4wLW_s1b0AnyvSmDnbRWFhH_6NOeyiEnU0VYykNk0OEI2GO2WVNfImPUjiU3gWCETW0pWfBxAIv06cJBav_BMyhqGjJE3bp2UseEYuO8IkoaA4Zjt5ywfytJdYU1af4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الوفود الاجنبية تواصل توديع قائد الثورة</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/80797" target="_blank">📅 16:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80796">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=VzpQM0OfkJxYZKUoIx0bv7Yl3d-fhblPE_DpNafMGIF6gfFOsOJhfTZekH3qmsM3vS1A9qGQ7sSoY37QonXsF_n4NKif9yp1chD4laTbQvZy8TspgYSyuRthcKkOaTDKuIAtTkflGSzBVo2_5YoqgtsYpBaeWGUOGtcLO8xFdg26X-S8DpCsxdvy2_lQ_bMNZvOt31jc3IBMSqsBLk-7d_LwnCiEkG5NBoZbOPmpUhZBVNyTL5_hw-clOEdrOxlp71Yt7za9G0XM-6CtQttOKLW3rlRxvPxBFCtaTYefgcAr_Shm9IRr6TExS2wZUdaIbTv2v51tOzBXCNKLHHj2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=VzpQM0OfkJxYZKUoIx0bv7Yl3d-fhblPE_DpNafMGIF6gfFOsOJhfTZekH3qmsM3vS1A9qGQ7sSoY37QonXsF_n4NKif9yp1chD4laTbQvZy8TspgYSyuRthcKkOaTDKuIAtTkflGSzBVo2_5YoqgtsYpBaeWGUOGtcLO8xFdg26X-S8DpCsxdvy2_lQ_bMNZvOt31jc3IBMSqsBLk-7d_LwnCiEkG5NBoZbOPmpUhZBVNyTL5_hw-clOEdrOxlp71Yt7za9G0XM-6CtQttOKLW3rlRxvPxBFCtaTYefgcAr_Shm9IRr6TExS2wZUdaIbTv2v51tOzBXCNKLHHj2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد تركيا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/80796" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80795">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=H_PuRETce66GTM8AXE7A516OMthxysealFFX-gFgwwslHsM-IkYdjfmoxoKT6YCtk-WBf58QJqTZiZOOo-1GAIzyPfjusJZ1p57wMQqIMjBwX0FHg5p8Q2yniusdFW6NJOEBvORMc9cQhadQVvF8NtM5ovJ_4nEYjzQu-E37uU1Pic1yJJUrvcmu1i4E3RTtKkOtVuvkeRqeY7M0wz-yFAkYw-m0SmXnTaFaS8GsCw8Rh0nhIXHazTdNSVG40W5VELGbHihcr_P1RO2jWFt29HuU0UVxU1QrauGx8HaeErbGxNJfCWyJFgwucdSi3qqehZL9bNIXRxjVIk69XICPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=H_PuRETce66GTM8AXE7A516OMthxysealFFX-gFgwwslHsM-IkYdjfmoxoKT6YCtk-WBf58QJqTZiZOOo-1GAIzyPfjusJZ1p57wMQqIMjBwX0FHg5p8Q2yniusdFW6NJOEBvORMc9cQhadQVvF8NtM5ovJ_4nEYjzQu-E37uU1Pic1yJJUrvcmu1i4E3RTtKkOtVuvkeRqeY7M0wz-yFAkYw-m0SmXnTaFaS8GsCw8Rh0nhIXHazTdNSVG40W5VELGbHihcr_P1RO2jWFt29HuU0UVxU1QrauGx8HaeErbGxNJfCWyJFgwucdSi3qqehZL9bNIXRxjVIk69XICPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد نامبيا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/80795" target="_blank">📅 16:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=fB-DeyeClPI7H_DykykKF86T4U4TKN3-YJ_yIg6ZqIH2SRFBPE6SpIXErl3OPoFqDY8R5OSh9a_zaqWW1kLluSqJI3RLQ-cYG3bv-3qKIyQxHYPl4DRbrtuEz2ip6SjbW2HrN153JeFcvwPuCxAijyxmHCjGMeaNs88CaeRI1R6dCJGdnB6f5F39L_Ru7RV4VSS4YDMc-9qXHkASFU5fuwVwcVjENg-_atkcxLG8SXq_-JXlg43yTFn0TYv2IeKqByD4AhbapJiXNUWZtwh6vDlaOzdXSPfBIyL1UOFLwVFPRPpcxil49l55oV5BIQ9P-3ZksR6cAfgK5RJRo7O-ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=fB-DeyeClPI7H_DykykKF86T4U4TKN3-YJ_yIg6ZqIH2SRFBPE6SpIXErl3OPoFqDY8R5OSh9a_zaqWW1kLluSqJI3RLQ-cYG3bv-3qKIyQxHYPl4DRbrtuEz2ip6SjbW2HrN153JeFcvwPuCxAijyxmHCjGMeaNs88CaeRI1R6dCJGdnB6f5F39L_Ru7RV4VSS4YDMc-9qXHkASFU5fuwVwcVjENg-_atkcxLG8SXq_-JXlg43yTFn0TYv2IeKqByD4AhbapJiXNUWZtwh6vDlaOzdXSPfBIyL1UOFLwVFPRPpcxil49l55oV5BIQ9P-3ZksR6cAfgK5RJRo7O-ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس المجلس السياسي لحزب الله اللبناني
يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/80794" target="_blank">📅 16:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇮🇷
الاعلام اليمني: طائرة إيرانية مدنية وصلت إلى صنعاء كان على متنها أكثر من 200 مواطن يمني من المرضى والعالقين في الخارج وغادرت على متنها الوفد اليمني و أكثر من 200 مواطن يمني من المرضى والمسافرين</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/80793" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e102375304.mp4?token=EkAvo5JE8L_JBabnUGL-OBkvHcxz6bQ-TIkvSGT8Pvgz2WPSsvfb3Tt63eqwOXxHB8t7USpAjT13oLzCBFSaECN9pn9jqDzakviWgpO0fCQtHuwT8KvWHSU4jFJJ3LClgUd13USqrr09BpLWqZXcInkE4nsOWJDVEsLgRoglvPdibaVXh5iYdTK7pLDaW_qxPGoruauRP9A3aQWw1vLD7oqqocsoFU5gdHJ_9natiUi7HFhekQiHoMSV9zZ_WEhlG6ScPDcXulDADpb2hErZXUTktLvpOEOEjOzWFyijV5OdGzKZD61LysM_OKQ4HR5Z8ST401evnXsvXJp1pwyeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e102375304.mp4?token=EkAvo5JE8L_JBabnUGL-OBkvHcxz6bQ-TIkvSGT8Pvgz2WPSsvfb3Tt63eqwOXxHB8t7USpAjT13oLzCBFSaECN9pn9jqDzakviWgpO0fCQtHuwT8KvWHSU4jFJJ3LClgUd13USqrr09BpLWqZXcInkE4nsOWJDVEsLgRoglvPdibaVXh5iYdTK7pLDaW_qxPGoruauRP9A3aQWw1vLD7oqqocsoFU5gdHJ_9natiUi7HFhekQiHoMSV9zZ_WEhlG6ScPDcXulDADpb2hErZXUTktLvpOEOEjOzWFyijV5OdGzKZD61LysM_OKQ4HR5Z8ST401evnXsvXJp1pwyeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد حركة حماس الفلسطينية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80792" target="_blank">📅 16:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80791">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9913937.mp4?token=EAMQaF1N0NlBj05M8MvfURURdwDBjMHNJPSxotphsPgzjWRtgQ_VvjknFy_xo2YM_UiDY6gCPaQq8ulnK7KPMTgtq-MHQanIgX7DqC034tTuHf7Kz674ZtCmGXVHdXEOVIvfH-YuxECi_qmOsonC4ubRSpdv3LgR1Ju58EYr5yIiFlerVSmvrZFD3ljLdTRd2qVnL2QCc2GGag-r1glyCwXXB5G1-VZwRJk0mer8irAvKc9TjWeP24MsWxu58qYZutviCzJjmkCjO_kpwQ1YilLYVOZ7G4zw9u5JfwJmpqRH5cn0NGapmsOX7Ghz5lEp3H4YP0utyPmjtmYQAJR9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9913937.mp4?token=EAMQaF1N0NlBj05M8MvfURURdwDBjMHNJPSxotphsPgzjWRtgQ_VvjknFy_xo2YM_UiDY6gCPaQq8ulnK7KPMTgtq-MHQanIgX7DqC034tTuHf7Kz674ZtCmGXVHdXEOVIvfH-YuxECi_qmOsonC4ubRSpdv3LgR1Ju58EYr5yIiFlerVSmvrZFD3ljLdTRd2qVnL2QCc2GGag-r1glyCwXXB5G1-VZwRJk0mer8irAvKc9TjWeP24MsWxu58qYZutviCzJjmkCjO_kpwQ1YilLYVOZ7G4zw9u5JfwJmpqRH5cn0NGapmsOX7Ghz5lEp3H4YP0utyPmjtmYQAJR9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول دمتري مدفيدف المبعوث الخاص للرئيس فلاديمير بوتين إلى إيران للمشاركة في مراسم الوداع وتشييع جثمان القائد الشهيد للثورة الإسلامية</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/80791" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmxxFEyC5JOVxib_UOngjgJEHf5FcZkBxPhDUU2UPDa66RXD6gsZlMtG6FX2iyKBooarvEtrcFefZOkuQ6E77Yh08SBInIhJ7AJ5uuiDX_kbZBwf5oBlbS2HCSQ6KLg64O2PVmGF8PHkPGH6AgTOLPV9sfGd4uM-6k2ttKIFEbIdMotO1I5xaIzuCeg-B_kPqyuNBS-e9_cEasJ40hrCXAI30vCpATF9_vSUCy8Wa9r_pXMGElk7T1DyYM44EsDU7xezyjLyoTWQ9mrhXyj20aRPN8n366hEbE2Q7CDPsgpeOIraFeotjq6Zar0Y2pVgnV8oVSDNB2NGscfgd7uK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنشر للمرة الاولى
🇮🇷
الإمام الراحل يمنح وسامًا للشهيد الحاج قاسم سليماني
.</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/80790" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=mpQm06UMz2yJ519r3AzUxaWF7W-EsliFBOr7V6fLXxm9Ro_-uYwYolPAQrNZDQx7tSq4A3HkiweQ-Vtp2iPrRk5TK9NUlGADTWocdw6c6F_qWZDjNwC7ONsfHD_pRQ_nORLL25IoFyC7jx_Sz2rornPoAp7KL0zDrQR5TfSkUC3eO8tifJgkljGyhYxi5hAGFmol43C0TOkGhm7A3NPeOu5NL5KsDbgAMdWzlW_bx-ll8uLP6OGw3-AEnWYUUnhYHq60s4aXznS7WDst95DzR3YRDEOXuJ6Le6HsT2FSH9pM0-N8H-Scs6goYxuvN93w-Gux7uDkpChU88SC7yEDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=mpQm06UMz2yJ519r3AzUxaWF7W-EsliFBOr7V6fLXxm9Ro_-uYwYolPAQrNZDQx7tSq4A3HkiweQ-Vtp2iPrRk5TK9NUlGADTWocdw6c6F_qWZDjNwC7ONsfHD_pRQ_nORLL25IoFyC7jx_Sz2rornPoAp7KL0zDrQR5TfSkUC3eO8tifJgkljGyhYxi5hAGFmol43C0TOkGhm7A3NPeOu5NL5KsDbgAMdWzlW_bx-ll8uLP6OGw3-AEnWYUUnhYHq60s4aXznS7WDst95DzR3YRDEOXuJ6Le6HsT2FSH9pM0-N8H-Scs6goYxuvN93w-Gux7uDkpChU88SC7yEDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لحركة الجهاد الإسلامي الفلسطينية يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/80789" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وصول الوفد الرسمي للجمهورية اليمنية إلى طهران للمشاركة في تشييع قائد الثورة الإسلامية السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/80788" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وصول الوفد الرسمي للجمهورية اليمنية إلى طهران للمشاركة في تشييع قائد الثورة الإسلامية السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/80787" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=YtC7KRHyKYUPRokZYPxkbfuE1gv3ID5LuSBNNDgttmsGuRpXjESYSmwI_EASOZFXSbwycroY7GLRc0ssSl3RBLhymFHAV734MzKUyqMzJNsEfTLhATPe3fdrPvSd2H-GB4zBPWAS_oRuVYM57kk0RHKPyzrJ1PjFfLCUZRUcZzs-2rsyJ7AzFYsUrTf-FCXvVrxtIJ6yt_bEjYkEEl5yPTa_gHBAU49KcdVltQNXPT64vz_BRp9-C5V2qOw1PehVcmoVDCAEkwVNSwjAMUeUJbelIGaelpI-fQSwNmhpPt6yKwbIEiVmhnGNDhBBOangq56QsKj1wbfw2BgcMi2jcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=YtC7KRHyKYUPRokZYPxkbfuE1gv3ID5LuSBNNDgttmsGuRpXjESYSmwI_EASOZFXSbwycroY7GLRc0ssSl3RBLhymFHAV734MzKUyqMzJNsEfTLhATPe3fdrPvSd2H-GB4zBPWAS_oRuVYM57kk0RHKPyzrJ1PjFfLCUZRUcZzs-2rsyJ7AzFYsUrTf-FCXvVrxtIJ6yt_bEjYkEEl5yPTa_gHBAU49KcdVltQNXPT64vz_BRp9-C5V2qOw1PehVcmoVDCAEkwVNSwjAMUeUJbelIGaelpI-fQSwNmhpPt6yKwbIEiVmhnGNDhBBOangq56QsKj1wbfw2BgcMi2jcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سلطنة عمان بقيادة رئيس البرلمان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/80786" target="_blank">📅 16:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=bOUhdxO7yjN-Yzc1ddFsaq3DOM43YGlXHENq_O5qLL87dq4rXWjCvzomtyu3V63fEq_Litoxy52LkUCCStLGzwrsivYfF-v4kYggLKzDB7PgtZRog1XwIjx0C43m7N-xH0uWMgopEB8HfFco5pl4pOfbYEr7q3g8gZIY8bqOZU882PPLIrzf0cPsSlYyCkhpkOIRy7lrZvibA09Gc1EnKqbOLdp4e3c16akAxva0nffGlfmCAUS6CPxgCa8ico4oUiftVwzV69UKX7Q2zZwCJIt0GdObJwzoC-0ReH5M0jxQTGtYXhg8Xaqnq03ynBfY7pkuqlvxNzgzbwikhi7Phw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=bOUhdxO7yjN-Yzc1ddFsaq3DOM43YGlXHENq_O5qLL87dq4rXWjCvzomtyu3V63fEq_Litoxy52LkUCCStLGzwrsivYfF-v4kYggLKzDB7PgtZRog1XwIjx0C43m7N-xH0uWMgopEB8HfFco5pl4pOfbYEr7q3g8gZIY8bqOZU882PPLIrzf0cPsSlYyCkhpkOIRy7lrZvibA09Gc1EnKqbOLdp4e3c16akAxva0nffGlfmCAUS6CPxgCa8ico4oUiftVwzV69UKX7Q2zZwCJIt0GdObJwzoC-0ReH5M0jxQTGtYXhg8Xaqnq03ynBfY7pkuqlvxNzgzbwikhi7Phw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد الكونغو بقيادة وزير الخارجية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/80785" target="_blank">📅 16:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدر روسي لنايا : المجاهد الكبير ولعنة الناتو دمتري مدفيدف سوف يشارك في عزاء السيد القائد في طهران</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/80784" target="_blank">📅 16:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuLcmGgUlZM3qnXYhP_fc6zcBjSisXhXlno62WctSzfxkep_y6RowOddF1kEXPC2zbRJx6EOrD7cyT6b0tc8JIGjTmHQsez_2mMu6jwUTsis5GW1VI_93_9FE4uaDV_YZjYuC5_K_9PJW3H7-2nM66gKchKx4N-25fr0DtJ-B41jDRwFL8hbTbjeHPh0XLxWi-UWXJ8GYLnewpdbVTX-o3S-Icz5Dunc0XXC7kNdvjBrLJmFmRyzO6eYk6IAIGsCDA7UbNkCCNoH35yramyBPEtCZBTTv90wj8At5LRmqBVGGTOHCc7xMKdIqC35bb6htjUXRG170SSSGBePyeIj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يهاجم الناتو مجددا: من السخف أن تستمر الولايات المتحدة الأمريكية في هذا المسار الأحادي الجانب في حين أن العلاقة ليست متبادلة. لم يكونوا موجودين من أجلنا!!!</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/80783" target="_blank">📅 16:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=Bhgf6UN08h4zfn2raXV8W1e-F_fMoDTCZJzQwwmnRyfxAtLAdLb79EanEe94llenH5Wya5iael1vTD522-7NVy6dalRsViEWwtxSKw6kfWKMskCpKj-7egSuHF7sIUOe7I2IHhdzz1UXGcFV18Rd7biqWryVLaa-5Rg6FX07KzejIXVEv8Qs23lSnRjuTHo6iTkyZI-UckZ_jmbBNuAWk-hludoYXdiANW1YxJvvwmf2m6p0uEl3riX9gAaTGBX1uavAjbE8nTYYD7XE32MuDBUBh3EQyYEcM_TKigciKaca8mMZ3u278cWN4Gerb3WuSeAmrI6GhI51u3Ql0WEwKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=Bhgf6UN08h4zfn2raXV8W1e-F_fMoDTCZJzQwwmnRyfxAtLAdLb79EanEe94llenH5Wya5iael1vTD522-7NVy6dalRsViEWwtxSKw6kfWKMskCpKj-7egSuHF7sIUOe7I2IHhdzz1UXGcFV18Rd7biqWryVLaa-5Rg6FX07KzejIXVEv8Qs23lSnRjuTHo6iTkyZI-UckZ_jmbBNuAWk-hludoYXdiANW1YxJvvwmf2m6p0uEl3riX9gAaTGBX1uavAjbE8nTYYD7XE32MuDBUBh3EQyYEcM_TKigciKaca8mMZ3u278cWN4Gerb3WuSeAmrI6GhI51u3Ql0WEwKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد جورجيا بقيادة رئيس الجمهورية يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/80782" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600ab9c890.mp4?token=PXgOefPjLU5a_cvOr4DPcvewLOdu_el-Qvbx4pLof3hnKohA2_f8Vjfx2YRb0cJHo9LPinFnXkJomAP38JinddICJdwa34is-IxTAOJqmobeE4vcPMYMAIeuhfxRwZqq_zj6vfrtepfEsBew9QhgYQaQJgumwvN6kEit_TQTvNZaIcshfWn42dyzkU4lXjhaacbSSSbhwf85R-hRGJKPLsVZl8S1QbmlZy7HBPbWJWR7Xxs74whu_I4Cu5ij4Phy35y4UAgJw3CS3b1xSufR6lQmoiVdCgZ3LEI5F6OPw1wn4DJpl3HwiqhZeLvjBRaUh4OCBMSk18V-zFjLJlGnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600ab9c890.mp4?token=PXgOefPjLU5a_cvOr4DPcvewLOdu_el-Qvbx4pLof3hnKohA2_f8Vjfx2YRb0cJHo9LPinFnXkJomAP38JinddICJdwa34is-IxTAOJqmobeE4vcPMYMAIeuhfxRwZqq_zj6vfrtepfEsBew9QhgYQaQJgumwvN6kEit_TQTvNZaIcshfWn42dyzkU4lXjhaacbSSSbhwf85R-hRGJKPLsVZl8S1QbmlZy7HBPbWJWR7Xxs74whu_I4Cu5ij4Phy35y4UAgJw3CS3b1xSufR6lQmoiVdCgZ3LEI5F6OPw1wn4DJpl3HwiqhZeLvjBRaUh4OCBMSk18V-zFjLJlGnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد بوركينا فاسو بقيادة وزير خارجيتها يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/80781" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34e716852.mp4?token=fK-BpFzRrfxQSaQQ4_YU9kTpd7tXhTzJheTi4WOs-lmjsX_TDiEkaP99BVMmD55k3qB8Ywt3GNS0TBQmYxWTzkwP_cmZjAx2pLeRfjIyciDD9xGT4EA8ppjc62QmyabgWsRZ3t3Vj47_v0vQHA2Y9-rDEwIqLvf3Zz3ArFJCWXozrbvIAuV1IIFV-8rQUjGVYp70ygg6cCk5VsbBKbZ9YE_II5AMC-7eTBbJZJTv4gZXbZ34d0Fjt-byr1fC5aXGVGRPSRSvVd7Of8-FtDWWInAjxSpW5lr9MRUxkESjHxkgVFifY1tkWi1JooaJGFLz6yic1Lh9lxddZO2mSK3ZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34e716852.mp4?token=fK-BpFzRrfxQSaQQ4_YU9kTpd7tXhTzJheTi4WOs-lmjsX_TDiEkaP99BVMmD55k3qB8Ywt3GNS0TBQmYxWTzkwP_cmZjAx2pLeRfjIyciDD9xGT4EA8ppjc62QmyabgWsRZ3t3Vj47_v0vQHA2Y9-rDEwIqLvf3Zz3ArFJCWXozrbvIAuV1IIFV-8rQUjGVYp70ygg6cCk5VsbBKbZ9YE_II5AMC-7eTBbJZJTv4gZXbZ34d0Fjt-byr1fC5aXGVGRPSRSvVd7Of8-FtDWWInAjxSpW5lr9MRUxkESjHxkgVFifY1tkWi1JooaJGFLz6yic1Lh9lxddZO2mSK3ZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد المصري بقيادة رئيس مجلس الشيوخ المصري يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/80780" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ccb792b1.mp4?token=MJX63nufUZ0PKgHLPjc04B8NK0ELwGak84Sqo-WSodu6p0qCVeZkjEyo8D5ptID5M1_tjrTBADtcVdCOGhXPV725Lbh5KHRgq42I7CbN3V68zFoM0HCCarbMgxcHrHELbG9ur-qnu1IM2PNWVfJi4LGuKIB3P5VZCJS4avQxkV6m-BOf2bo6LT-UanHXR_VtXvHDsQazO8nJ35q8JZ1UhYx_SFkpmtSo_Ox5WWQ0TBH2lJNhBB8iShknLaY3cST9Gpk0VaztcEkf8aYQ9LCky8twW46nhzP2s8CS1V3-RRF_jgjXaoLngBfQrbnHN1I1niZmLGfEIyYJtsHFDLEYN36noDfHa6codPLADxBxQeg5EYFXpeHEM0vJddyGFkAiUBrAiF3y3nVsiBDpEkJJc39wLniheWJ6-Oxvmy1oo9i9x0RakV_PxvU-_xdjQw0VR0ysn6yzzpqDa7FpcNH1zyf_UGMVJqbN4eCJNkLZkMIz3UTgNsxleHb3gz7LHm82cebl47rjYBchkLeNKFlUFNma7bjrEqiJI2PxKLhxS94uyugnxX8ZZGgrijiALqNJgZSCwYitJpBc47fGWCDnvSMeyaZwxZWNbtKE8GJhBV7hXTUp2G6_uWetcghwuavUU1qCBzZCOolLg77G6sWLlQH_83N-LFIzkA9TdkytiLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ccb792b1.mp4?token=MJX63nufUZ0PKgHLPjc04B8NK0ELwGak84Sqo-WSodu6p0qCVeZkjEyo8D5ptID5M1_tjrTBADtcVdCOGhXPV725Lbh5KHRgq42I7CbN3V68zFoM0HCCarbMgxcHrHELbG9ur-qnu1IM2PNWVfJi4LGuKIB3P5VZCJS4avQxkV6m-BOf2bo6LT-UanHXR_VtXvHDsQazO8nJ35q8JZ1UhYx_SFkpmtSo_Ox5WWQ0TBH2lJNhBB8iShknLaY3cST9Gpk0VaztcEkf8aYQ9LCky8twW46nhzP2s8CS1V3-RRF_jgjXaoLngBfQrbnHN1I1niZmLGfEIyYJtsHFDLEYN36noDfHa6codPLADxBxQeg5EYFXpeHEM0vJddyGFkAiUBrAiF3y3nVsiBDpEkJJc39wLniheWJ6-Oxvmy1oo9i9x0RakV_PxvU-_xdjQw0VR0ysn6yzzpqDa7FpcNH1zyf_UGMVJqbN4eCJNkLZkMIz3UTgNsxleHb3gz7LHm82cebl47rjYBchkLeNKFlUFNma7bjrEqiJI2PxKLhxS94uyugnxX8ZZGgrijiALqNJgZSCwYitJpBc47fGWCDnvSMeyaZwxZWNbtKE8GJhBV7hXTUp2G6_uWetcghwuavUU1qCBzZCOolLg77G6sWLlQH_83N-LFIzkA9TdkytiLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الاتحاد الوطني الكردستاني بافل طالباني يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/80779" target="_blank">📅 15:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53048897d6.mp4?token=AzUMLLei3kS8b0eWh7n_eJacRfUopWXKQ7J-19NSdJjukdTCHAIYMYp3Zvgt2YFlxYxzCHhmUzue5ZPzwLckQeB4jiNGlmELVhTWozccSXMKdcbZQTsntjzAS2yiwVkK_NHDhGePMl8hi4miwgels5yRiTvWvngGietyVPkgAzvD4wYnpYvmNj9TaEI8kjMHdqAT5DJBECWH4usyDx3E9Mi0OkDgqXhx02BZrA-tUNlf2ROWXJHZCWMOkmjnMzKpmPZu44OODe4bsblyjH5Q7x2mza-5akUE8k5b8N7y3D4qvzy-z_vQMUojvMCjqE6WVzjthjXcdcU2lW26RidEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53048897d6.mp4?token=AzUMLLei3kS8b0eWh7n_eJacRfUopWXKQ7J-19NSdJjukdTCHAIYMYp3Zvgt2YFlxYxzCHhmUzue5ZPzwLckQeB4jiNGlmELVhTWozccSXMKdcbZQTsntjzAS2yiwVkK_NHDhGePMl8hi4miwgels5yRiTvWvngGietyVPkgAzvD4wYnpYvmNj9TaEI8kjMHdqAT5DJBECWH4usyDx3E9Mi0OkDgqXhx02BZrA-tUNlf2ROWXJHZCWMOkmjnMzKpmPZu44OODe4bsblyjH5Q7x2mza-5akUE8k5b8N7y3D4qvzy-z_vQMUojvMCjqE6WVzjthjXcdcU2lW26RidEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الجمهورية العراقي يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/80778" target="_blank">📅 15:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية:
وفد عراقي رفيع المستوى يزور أنقرة.. من المؤمل أن تشهد المرحلة المقبلة التوقيع على بروتوكول تنفيذي يضمن استمرار صادرات النفط العراقية على أن يشكل هذا البروتوكول خطوة انتقالية تمهد لإبرام اتفاقية جديدة بين الجانبين خلال مدة لا تتجاوز عاماً واحداً من تاريخ انتهاء الاتفاقية الحالية.</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/80777" target="_blank">📅 15:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dcabb0626.mp4?token=YNPvwhr-thbA7j7KH2-AWa91Vg-qjRwe5I92KY7pqiSE70J5iWVINlkoKhmFlRJa1IRAEv2eKSVJa5i0DEQRNTh3V0cq39F1fy6yDYAHdpGfzUd4sErzrYSx5YYnowJx0K2iPCFpf3Ee62o9bGA8f8GwEAwxUTQICjx9L9byLIBm8lFZhvOoOBsBOqobhqO6YSQovabfHmN8bhhBA7yFx84nJLY8uiS9h_genxvxgkpcMsK4sj8JsUd634ZJEHj6xDsO73epLez3HG6HM27qi5_yLg5kukgpM4rglwLGt9CkXQJH2-T4aj6ZpWJxZjz4R9qWQ8XqohAC_KBu9qCfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dcabb0626.mp4?token=YNPvwhr-thbA7j7KH2-AWa91Vg-qjRwe5I92KY7pqiSE70J5iWVINlkoKhmFlRJa1IRAEv2eKSVJa5i0DEQRNTh3V0cq39F1fy6yDYAHdpGfzUd4sErzrYSx5YYnowJx0K2iPCFpf3Ee62o9bGA8f8GwEAwxUTQICjx9L9byLIBm8lFZhvOoOBsBOqobhqO6YSQovabfHmN8bhhBA7yFx84nJLY8uiS9h_genxvxgkpcMsK4sj8JsUd634ZJEHj6xDsO73epLez3HG6HM27qi5_yLg5kukgpM4rglwLGt9CkXQJH2-T4aj6ZpWJxZjz4R9qWQ8XqohAC_KBu9qCfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد بنغلادش يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/80776" target="_blank">📅 15:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=N7m9vrDCEdxE6arrqSKl-liIspIzXGb8LZmm1cEwvMQsKbioBHUanGCK_4LrsMM-jkHOdtDE2ba70ZcHFVtnB6vnaHmbX3urv-cLDFB8nAoK1KwZy6ifdnkcZI-q3FFdWZhdFf2MapvmFka8bBaDJhXtGLYPc1rfpViHl4Dyd86ogrOOkBUpYbChSF1zqMp5396YKvOY2olpoS9urcu1qDWvRMPeJRgRbL8NAuURu_QOa5u8MuEpFaDMCvBcOQFKcmGzLqDorV1bSowry-lO7hMvt6sp8gU49w7ufK0x3zYGWFARcwSwGfiglHPXcNd3k_y55fJ0f_Cy6l3ZP2N73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=N7m9vrDCEdxE6arrqSKl-liIspIzXGb8LZmm1cEwvMQsKbioBHUanGCK_4LrsMM-jkHOdtDE2ba70ZcHFVtnB6vnaHmbX3urv-cLDFB8nAoK1KwZy6ifdnkcZI-q3FFdWZhdFf2MapvmFka8bBaDJhXtGLYPc1rfpViHl4Dyd86ogrOOkBUpYbChSF1zqMp5396YKvOY2olpoS9urcu1qDWvRMPeJRgRbL8NAuURu_QOa5u8MuEpFaDMCvBcOQFKcmGzLqDorV1bSowry-lO7hMvt6sp8gU49w7ufK0x3zYGWFARcwSwGfiglHPXcNd3k_y55fJ0f_Cy6l3ZP2N73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد طالبان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/80775" target="_blank">📅 15:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e68ef245.mp4?token=nFjDSiYukMay1bD6pHpymzFh1evxMCjstct5H3tFW4M6pM3oaMAYcxMEzlXSU_WPutEtATmOH5RtL9SaWhDV7TgIYJeLZf13iGpjeWCISg7VB8B0ce8vfnJRJt7kInXyjz4q-oUeG3H9rcy6u0W9Yw0tz_5qYXB5bBUhNdsyLtZycOZ2WCYy2JfPfBDHGrvZYX7i1Gz4X6_qIUrlHRavmKU--Uko4JN19R5hMlyK5smTp5BOIR0Z_Ldy4oZeGNoJaMb6_2XG62h6nmiP-Ad742_HF-M6mp-wPdKw6a5BgCIkDLjVX7TrThvFhK1dKg6YbD3zDp_XxS3DCIHLTbS8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e68ef245.mp4?token=nFjDSiYukMay1bD6pHpymzFh1evxMCjstct5H3tFW4M6pM3oaMAYcxMEzlXSU_WPutEtATmOH5RtL9SaWhDV7TgIYJeLZf13iGpjeWCISg7VB8B0ce8vfnJRJt7kInXyjz4q-oUeG3H9rcy6u0W9Yw0tz_5qYXB5bBUhNdsyLtZycOZ2WCYy2JfPfBDHGrvZYX7i1Gz4X6_qIUrlHRavmKU--Uko4JN19R5hMlyK5smTp5BOIR0Z_Ldy4oZeGNoJaMb6_2XG62h6nmiP-Ad742_HF-M6mp-wPdKw6a5BgCIkDLjVX7TrThvFhK1dKg6YbD3zDp_XxS3DCIHLTbS8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل خمسة عناصر تابعين للجولاني جراء انفجار لغم بهم في مطار التيفور في البادية السورية</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/80774" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6962df27c0.mp4?token=sO2Xpnc7nYld5mWLSRMWtmTlknk1PRUipaat8HAhRBvMx7zjaFaLGfC4VHaGbSMYlrCH0cQexzP4TILXvRFQRdKD8KAS5ZjxLKDSTUxByDiLZzh-HQn4KgBW1f-7pE5FB7cIyfaFWCAAW0i0g2YA144-VH_f6eF9B9YBY8V9jEmsJEs0HgEOovZrKyT9qvYwakj8o2f1kNBKXp2kysSFgio8P7IpYDNf1M1YDXOrcE9dMBVl7y0pfm1kySQMEQ8Vi9B68Yo48yz0iNUz85AzeuFsb2EUBhnVYh38vljNbT2T4uFsq1erWaJ-UgxX2wWOthbhYkB9v1_91aZ93xNCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6962df27c0.mp4?token=sO2Xpnc7nYld5mWLSRMWtmTlknk1PRUipaat8HAhRBvMx7zjaFaLGfC4VHaGbSMYlrCH0cQexzP4TILXvRFQRdKD8KAS5ZjxLKDSTUxByDiLZzh-HQn4KgBW1f-7pE5FB7cIyfaFWCAAW0i0g2YA144-VH_f6eF9B9YBY8V9jEmsJEs0HgEOovZrKyT9qvYwakj8o2f1kNBKXp2kysSFgio8P7IpYDNf1M1YDXOrcE9dMBVl7y0pfm1kySQMEQ8Vi9B68Yo48yz0iNUz85AzeuFsb2EUBhnVYh38vljNbT2T4uFsq1erWaJ-UgxX2wWOthbhYkB9v1_91aZ93xNCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد النيكاراغوي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/80773" target="_blank">📅 15:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795d46a877.mp4?token=jqmwU7v56BL0Y_JGdu3ukaqSFVOD4xZVEratYTnevQ-w6DQxX4wC_IwWFRpFnC1oJkxEQRnmHMfC7XaBC5kXvyPBdpyLgFe0IyXkpJuxF2aF4H7PVQfWumZmOEM22nQkKRcyZDnLIxS_jEzo5mdbUBE67NCAlw_zXSyFYoMqypK-fIcqQJypgAJD62dU6s_n8L78BUGO01D6xKqxpOw6Q1lf-qn0w3bvydGpslOhCj81eyDC8EA-XAt9MlCBpwJX9vBUpebzSo1SxlDnH4yNnTJIMOfFH9bN4BUc7ebT7IFeFOCfpZD2KHxmIz35y609xvV_r0HiEgVhgkNltaoc9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795d46a877.mp4?token=jqmwU7v56BL0Y_JGdu3ukaqSFVOD4xZVEratYTnevQ-w6DQxX4wC_IwWFRpFnC1oJkxEQRnmHMfC7XaBC5kXvyPBdpyLgFe0IyXkpJuxF2aF4H7PVQfWumZmOEM22nQkKRcyZDnLIxS_jEzo5mdbUBE67NCAlw_zXSyFYoMqypK-fIcqQJypgAJD62dU6s_n8L78BUGO01D6xKqxpOw6Q1lf-qn0w3bvydGpslOhCj81eyDC8EA-XAt9MlCBpwJX9vBUpebzSo1SxlDnH4yNnTJIMOfFH9bN4BUc7ebT7IFeFOCfpZD2KHxmIz35y609xvV_r0HiEgVhgkNltaoc9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد اوزبكستان يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/80772" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام غربي: مشترين يابانيين يجريون محادثات أولية مع إيران لشراء النفط الخام.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/80771" target="_blank">📅 15:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قرغيزستان يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/80770" target="_blank">📅 15:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo5EHO9n3dnk-9ngpio9C3wuiZ6BqNWpxTFxQ14rvSQtMug9dTZ9lpOLlzwDIdvKK0kOJOyDOs-AUwh62IxiuJjYHodoTQMBcvOALFeYBRa6eOWgrD6s2ecKNtvQ0G2bCQTotEFlZXI_WSW4LaIhEJe6C2C0MFCsAg-irTd9LV4LC-vP5ZC7oSFCcp6KGAxwiGGWOjetWmOInqyhVjaTU2oCbOPbwNYUg7zFnyRFKjUMuykcmGkRVJHjFuMe0bR55xmOq9wyr_fbLGBwtpw8YjbZcBkluHKT115k2WBQab19xXepz1qSG0szefsa1RIEwN-jhHtQyW4gIo2j0586rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6E4XySn8G_HuE1dsrwfCK74QG3L_bUvY9pS9L04nDKObf0P3TZXueRzlhsmQHt4Jg5YNxrtt0qyC8udt9g421mIFBJ-bXg5Mc4S1QPwbjjCqwgAevTV7bJih9NNLLc6vXRNBLxaZBnIq2k1fYju971S8QL-0h_Or3LVR0IJ5ygJN3mGR0UEFkjkz4keet9ZiXGBw9vqNYLq5gyIag-0NVVzKrVaDJzBDC4poIBHjEPem_-UYKQf1UPiFfVGW_NX7TKCKf38eNwkZYFIgx6h88ipiO1ETCDsxvnfdVSwXaCuLEytEsChvDrzFv3iEnOct8QtCqZtH6PiAkeLwnRkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_eCH6Traf04675Bx--B9a9fYLWl2mrxURDeShVPAAKn_NUbeMFuLxs0OQNwpcmr27Ev33_7pdN_XgenxjgPWt-Ve8WxGWXTyCF5Ck0gTeVW596E7MIlsevTMJMqBR07qh-iYmjpY-69gx97nlwe1j0SLft41fLOFJN0y0zEPZOxDiLKNh3dSbYWx38yOwc__8ozYSub8DoHHarK-TnXhJmS_jyqyytoNhh4VUWQ3GThLDM0NiZmFPr9LgejV0SMiG0tLsQFd0-70pdf--DeM-IlrvMV5hXxLaD_UrH3atllA-LLBgpsMy3fCQeeQMG5iCI13rDHu4XThvRZNxqBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G08AhgpPJ0YMLZKqfaYx1QpMpUSm9IG0oQKRcp4kQpRj8DXjHSFBaL9s7Yd6xSPYuKXV9Sv3KEivg69wh3--GgAaKaMaKbhTGEgPDjHKrKFhmoQOk0gueAhMi8WjEL6P0ianFeT5iX3Otiu6rml70sTXjjNvAErAajzBv8N5V3YRN0A9dQJLjjKg723nX4eenvs9YhAUM9ylkPK5fF1zj-IbcW7WpcVl1TLKbngGZWHzjzMjP2UUPwvbSwsxE09QJQH80RX_UUC4zWcswGFCmt89uvRAyunSf8JMxJvzE10izZKa0Og8Yif0R6YSdfJ24XQxfzhyQwOoKAOSBKR1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران  ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/80766" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/80765" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس اقليم كردستان العراق يشارك في مراسم وداع القائد الشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/80764" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=XeDziE8GHrZ2fO6b4yxnJT1-PddisosLKMp7R142i-Ff-eDZH4_LbEKN4tPtbEZZpYjBfmlMyq-siw3dP-C-VPzzogtdLUafFNYsQLhPPEo27rEGZj_yrLNn6NxxiS-3wC3BnjPq20RZqmYcN_of-fTqR9JixUTYa1uXBvDm3VW6U4Xe3NCtmkEHFjwrg72UX-p0XrdyMVVFLxEity5nZFSUIRYg_YzTzIrteMatfGvfCwR3BNy4vBT0vCyHrHcJFKdv0C10cQCMx7FYIZGQURiwDquwEs_RQMGJbOh79tMCrnMVkAuFtSfEYzo1W-kPYCMUndCEITzYNnIHtdwlDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=XeDziE8GHrZ2fO6b4yxnJT1-PddisosLKMp7R142i-Ff-eDZH4_LbEKN4tPtbEZZpYjBfmlMyq-siw3dP-C-VPzzogtdLUafFNYsQLhPPEo27rEGZj_yrLNn6NxxiS-3wC3BnjPq20RZqmYcN_of-fTqR9JixUTYa1uXBvDm3VW6U4Xe3NCtmkEHFjwrg72UX-p0XrdyMVVFLxEity5nZFSUIRYg_YzTzIrteMatfGvfCwR3BNy4vBT0vCyHrHcJFKdv0C10cQCMx7FYIZGQURiwDquwEs_RQMGJbOh79tMCrnMVkAuFtSfEYzo1W-kPYCMUndCEITzYNnIHtdwlDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد هادي خامنئي، شقيق القائد الشهيد للثورة: الشهادة كانت الأجر الأمثل له.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/80763" target="_blank">📅 15:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الباكستاني بقيادة رئيس الوزراء وقائد الجيش يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/80762" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPm85U35oVYFmwa20SWbx6I54WGhFi2hBUP8KoFouEcL1tNc6fA7N38_cMB_MP5Zk4H-RuwVtfOGbMPzk2gvpku12p2PRmd90pCS0cBF7QoVd_5XO2peg7rkNeGcGdqLIFTcy8NmzPuwOH7r6YicTjYrRZJn3LAO5ZWecOm0ghcxb1n9iPNbeXk6ybPhHHU-L1YDEgmvDF850BMjzFXXzZqT5NI-ir0Nfk1jiq70IawMvOKmi9AWVtW7nHaPuFFVBuEBZaqt0WiN4S2QeEN7OUIVp5gN08A7bGruht3DEiQjgF8w0K3T2lSYfjPYIRXc5ZEII1dTIgsMr_p-VcJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس السلطة القضائية الايرانية يوجه رسالة إلى القادة السياسيين الغربيين:
افتحوا كتب التاريخ، الأيام القادمة ليست مجرد مراسم تأبين؛ بل التاريخ في طور التشكّل. عندما يملأ الإيرانيون الشوارع لتكريم قائدهم الشهيد، لا يمكن لأي إطار أن يحتوي على حجم التعلق والولاء الذي يكنونه لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/80761" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrDERSv3NuP0g1xGozIMjpH89Aioi3CM7rLoNqDaGUsXlMQatAFhmZnzv30qU6X3NufFWhRDLAI72Q0tZ1AMM19eKGDy7dOJ5KxgpQ5qHuWBQmxge-Hx2BjxJof87AckYLyK8VUajO4KR-gmTkF6XUvLz_mSRx6diqxBWoIp5buX76f1Py7kT0_lYLg67T0obckwELxkmz_lxz2xttZ7Ih8GZWQB-rrtxRRBe5o0ofPoDqHanw-4gpoZ812z_ROxtVn99VPaJEgHcJtao1j-Fg9DU8C5PmKW075u9DHX7ZyRGYrBqf2ExM6X_9KgFStXfGptL71t4GJ1vYwS5Kpusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرتين روسيتين من طراز إليوشن Il-96 Il-96-300 تتجه الى طهران.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/80760" target="_blank">📅 15:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaRxvMGd0cd7_Z8TyZY-tXYwOrJky7BueWnEEfTW5BT15LWy0xJ9t1bdS6pcVyyFeOvM7LF6Jln1dZD7WWtnOj8WRnkwNaPMw98xuVARhy-WACwUaPCR0ryC7tll_zE42Xr3ppZ_gAX3NgvHxNVWy1P-z_L2ooJtWh3w-CfzvlPVFngBQ_W9AFMOcLeFws4cL9enoJMo7TEV35Sj4JUu-HhEwoF-vLtHl-FIp2riIFr2h2bEM6PYrUuMd9fyJzdOKqtLRU5y1Shdn8smoYyFOX08SX4rG5VyTJyZSkA0EDjMAX07ym68hTzFkCozGli2A--W2yW4aa3TRQ9kyWVmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG17GXvvxLU5IoACp2OjFAmzqOcl19gEY_P7Lqp5s24ONDtuebtURYKeiBLIlbMiprYbnCQCCtCFJcoskoj0OykTuQ0Vkqd-jWkfu7CzMAePmRAfjy6cfv7o1c5F6qiLE6HWE1KastJ1lhe-7HT_x1HfyrQHFWz2XoFwUKerrmZhAt1hbXkUW4N31QFDhVrxKRU18QkCsdbqFqPFw7ue3ZNfMOcSZSm-MdGzZ_Jdokyxzgo12Z0h6xMbYYIAr_-ctUDxUVhr8fmWNwsW2ucLSOt6vH-YaCSWy8CyJYD_Qfo4EehDQ0r64-Evep1sbfIPTeTLml32OtaUbiiug-mJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور علماء أهل السنة في مراسم وداع القائد الشهيد للثورة.</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/80758" target="_blank">📅 14:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الطاجيكي بقيادة رئيس الجمهورية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/80757" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZwW7TjJTcYCWBc2vJOw_-hr-mXg_5p-obrsFdCbY8LNagLk2FOxF_daQruiM-zGHO4hJCkNd4blBNrF9emUqScw_FjY0awk9JKSzr3SyZuv6-xuDddkwtiT2zB1fYZKyZLSBWZV9Q9p03mbqLYeT6YEAq4au_dgGHz3tgKJpv2x_wj8oNetfI2MFjaWOkbAMxGoWqCItuS31ziL_JZnArFLIg-vWTxmGrukb1z6Bx0jf1sLY7X8dpec7zFp_S1XirTdyYPkq_ft266gMGgjQAq41hyfgCCtt1vg8oeI--6FkcXmfW8GM-v4-dDfVrYVuHPduCV0GiedYoqu6OPubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجمهورية الاسلامية تضع صور شهداء مدرسة ميناب عند مدخل القاعة التي أدى فيها المسؤولون من الدول الأجنبية احترامهم لجثمان القائد الشهيد، في مصلى طهران.</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/80756" target="_blank">📅 14:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد البيلاروسي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/80755" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الارمني بقيادة رئيس الوزراء الارمني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/80754" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=twvnrlLz8rYUE7NTOGDH_tEAQqU6Ctbk_HWA7Ptb3V0VNuEYNRuvcUNv3Pz8aa0w9jPnuP_MW_MB8OaKeEjd65Md8aIekDPc0ILK2Q3WD6n0NZZhb9DNJPcX3IVPEr9Pz5v-C_FE09dzXfLA8bOF88XKBHICVOcA-RwG14EcHWfH-KgYZw5vdDQFrgmhT_skKTGmTls3z9bksz95u287iUzosy4Z0Vr9-JfJJsNy1IUAlJfjKJHXj3ICtgdmgHynSYEPGtqWY0mU2MScVeS-ELyfzK3nKmOBu29SOxmd1J8XA3lvYz1SFbqXhwG0-zRYmSSXIFRZniH6qGbqOrBVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=twvnrlLz8rYUE7NTOGDH_tEAQqU6Ctbk_HWA7Ptb3V0VNuEYNRuvcUNv3Pz8aa0w9jPnuP_MW_MB8OaKeEjd65Md8aIekDPc0ILK2Q3WD6n0NZZhb9DNJPcX3IVPEr9Pz5v-C_FE09dzXfLA8bOF88XKBHICVOcA-RwG14EcHWfH-KgYZw5vdDQFrgmhT_skKTGmTls3z9bksz95u287iUzosy4Z0Vr9-JfJJsNy1IUAlJfjKJHXj3ICtgdmgHynSYEPGtqWY0mU2MScVeS-ELyfzK3nKmOBu29SOxmd1J8XA3lvYz1SFbqXhwG0-zRYmSSXIFRZniH6qGbqOrBVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سائحة امريكية تتعرض للضرب على يد عصابات الجولاني في محافظة حمص السورية</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/80753" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الاذربيجاني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/80752" target="_blank">📅 14:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/80751" target="_blank">📅 14:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/80750" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئيس البرلمان العراقي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/80749" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
