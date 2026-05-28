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
<img src="https://cdn4.telesco.pe/file/eXeeqTiPK8IBdrWK16jb5Y2xtAYsgPudittf2XxBqOX6b9BjRhDmvtojjSBXBwPs_YWgWV9ZXs5OddtetVwPJSEqwpUUFgHv4tvb5Xq92WaxX_sv0OzsotJnMMa4zYNp4kIhCH4ii4PtZ8LVw3o4gziF7NwjLt-8WAcDdSgtYqNJ32YT309CI1vvUpxgu17S5xdGdLnWrLP-r7EzOhQq8kWlK6aYWK5pbgwHQ3ncaN72OWvqlg8iD2O-wsDRH43pvX6zZgbLHcNyFOb1db3_PyuuZbJ9p06-hqyf1rOByVThc7tEl85eqM1gEq-OxmiHiuJca_i_epw9frRGEhWA9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭐️
‏
أكسيوس عن مسؤولين:
اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/76295" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
🇺🇳
‏الكيان الصهيوني يعلن تعليق علاقاته مع الأمين العام للأمم المتحدة.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/naya_foriraq/76294" target="_blank">📅 17:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه الجيش الاسرائيلي برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/76293" target="_blank">📅 17:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه
الجيش الاسرائيلي
برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/naya_foriraq/76292" target="_blank">📅 17:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/naya_foriraq/76291" target="_blank">📅 17:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تنظيم داعش الارهابي يتبنى الانفجار الذي طال جهاز مكافحة الارهاب العراقي</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/naya_foriraq/76290" target="_blank">📅 17:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
‏
التلفزيون الايراني:
بينما انتهكت أمريكا وقف إطلاق النار مرارًا وتكرارًا بمهاجمة الأراضي الايرانية خلال المفاوضات وفترة وقف إطلاق النار، يسعى جيش هذا البلد إلى إيجاد ذريعة لبدء حرب من خلال بناء رواية زائفة! سيكون رد إيران من خارج المنطقة. المفاوضات ما هي إلا خداع أمريكي جديد</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/76289" target="_blank">📅 16:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/76288" target="_blank">📅 16:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN25WyLr_Y7O7yv-ijMMLgKoRNGVjeEVm5YIpcBie6Nnq0wapi-36RrOV2H7qrOSxZxvVOqGU32QofGa544jxqSQBfH-sp5VXBWWmN3QNXzDwf3IGaFAI2LjdBn-CvlrfNUKFbjHAaY4vLNYvjXFlTrg-tjeszbjHPjZd4nWjvhWj2raY-RvLPxrlgfnl-JQYubvTl2y6lr0uauVrJSAQ26kdh5z6JVX5CEffVJSKa87arYbuVrrCfFbLRb2qCRWR-35fBGKcfKI3-hnQirsd0ifAe7U4YRZdvoqnpy0tg1Rpz3AxqQG2nyorZ20KTKZ1dAlRRwoH25hDAxfKWJnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخزانة الأمريكي:
سنمنع الطائرات الإيرانية من الهبوط في المطارات والتزود بالوقود وبيع التذاكر.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/76287" target="_blank">📅 16:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وسائل اعلام تزعم:
إسلام أباد ستعرض يوم غد على واشنطن نقل اليورانيوم الإيراني إلى بكين تحت رقابة دولية.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/76286" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r08TeGoHRJV4wyPkwXihoJoDz1SKYnheW_778sVO5mwOi54AOArjds1bYWh84ic2mFsCaU-t06QWfY-dKqFFx8ie0assIqS-xRXZQ-AwJGd2E4KCuzNwbQSVt6QmyzVzw4Qcs0qPPeogAzaN_HI4OsrTNTFseoAiRFbLLmDE190f_QrjfWbMV4ZuXYSFP4pKjnw9Ti9TGatHu1bBkURBspP-O43BQy6FmjrwBNk4fW-_20nOVCMeKFYXpADF81vrIkh9R15k2hp4-5jEkPS0xmmuHmIwO8SvB21LPbxn82VDaEANt-utMeJsZx8hMxOMXV4U_jVBZWbawOkXCGfr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادي في حزب تقدم يدعو لمقاطعة منتوجات المدعو بـ(ابو جنة) بسبب حلفه بـ"الامام علي"!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76285" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76284" target="_blank">📅 14:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">إعلام العدو يدعي : اغتيال علي الحسيني مسؤول الصواريخ في فرقة الإمام الحسين</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76283" target="_blank">📅 14:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76282" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76281" target="_blank">📅 14:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76280" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76279" target="_blank">📅 14:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي:
في الساعة 10:17 مساء بالتوقيت الشرقي يوم 27 مايو، أطلقت إيران صاروخا باليستيا باتجاه الكويت حدث هذا الانتهاك الصارخ لوقف إطلاق النار من قبل النظام الإيراني بعد ساعات من إطلاق القوات الإيرانية خمس طائرات بدون طيار هجومية أحادية الاتجاه تشكل تهديدا واضحا في مضيق هرمز وبالقرب منه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76277" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76276" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#ترفيهي
الأمين العام لمجلس التعاون الخليجي: ندين بأشد العبارات استمرار الهجمات الإيرانية الغادرة على دولة الكويت
جا وتهديدات ترامب لعمان؟
😄</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76275" target="_blank">📅 13:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇳
الأمم المتحدة:
معلومات تشير لأن غارات إسرائيلية بما فيها على صور والنبطية أدت لمقتل مدنيين بينهم نساء وأطفال.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76274" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
‏
الشرطة السويسرية:
3 جرحى جراء هجوم بسكين في محطة قطارات بمدينة فينترتور.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76273" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
كلمة لقائد الثورة بعد قليل.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76272" target="_blank">📅 13:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📰
‏
رويترز:
تقارير للبنتاغون كشفت عن استهداف قوات أميركية عبر بيانات تحديد المواقع</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76271" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📰
اكسيوس:
إدارة ترامب تعقد تدريبات عسكرية لاستعدادات محتملة في حالة حدوث فوضى في كوبا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76270" target="_blank">📅 13:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل اسرائيلي قرب تل الجلع بريف القنيطرة جنوب سوريا.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76269" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تحترق بصواريخ حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76268" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0HSHG-uvsuXF0FFE1FiFJ0a6mEgekSzJNEWZfQCyb-QHaPH8pCGKDj3DVqi5Xud4jKtePAhF_CC8YD_tgV9fcP0gLzNxHlvlPMRaX9IrDeNSpq5TA7ZVgrzu6_YfHXiWXGJXKWG3J05_99I9S5r80Ns-pWcFU-qD3L5angLJUpmwzlRTYpNztKQufPn00U12CTbabWRzk42o_1mJ51Cie3xOJn5ryW2H9rXGClRU0bC4CIPMzKsM5e12ETlCNFwzZ5lKivAFngVnNjEtd2K8hARZdNVCf71R3Y1LxPmyMHmi3-ksCnS1P9ORecDVLA862fLbmTZqa6bp4x3sfav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
قناة العالم الفضائية تنعى مراسلها السوري "حسام زيدان"  شهيداً في غارة اسرائيلية على صيدا جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76267" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2pi2fjclkHm-LsXtz0J_J-aI6MJR03FKshLWNh_zU-Iyvt2rnYSqu0dvUJ9p0yKt_t-Rwot_kgLk7PYQ06UOwMBzGnOhSD70zddsXQBMXoEROTX1Xc-t8NFDCaeabjGBeCuLlgxBd5RUss_3O6Ux-RDTkD1sdSs6qr33k7T6j6Izd0RDdCuxJ3s5UOZsaxT5E3jMSYWsmhLaiRbAYuTO2-q9mHZJnnI-4SNauWO8kSW8qJWDlZRf6yrWldmkCup2QoERCXQYY0yWOO_7IlTNjbiS5rEg4RSNzAsDyX4qJnMDjDuDahuCyopr4-spWvOgQl7S2addRQMB4kR_QIZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76266" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76265" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76264" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: تحطم طائرة خفيفة الوزن في "عيمك يزرعيل" (مرج ابن عامر) نتيجة خلل أثناء الهبوط</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76263" target="_blank">📅 11:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏الخارجية الإيرانية: ندين الهجوم الأميركي على مناطق في بندر عباس فجر اليوم
أمريكا تواصل انتهاك وقف النار المبرم في 8 أبريل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76262" target="_blank">📅 11:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني ينشر مشاهد الرد على هجوم الجيش الأمريكي فجر اليوم على نقطة في ضواحي مطار بندر عباس.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76261" target="_blank">📅 11:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚽️
قرعة كأس آسيا تضع منتخب العراق الشبابي إلى جانب الإمارات وتايلاند وتركمانستان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76260" target="_blank">📅 10:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📰
بلومبرج: رفع ترامب نسخة جديدة من دعواه القضائية التي تبلغ قيمتها 10 مليارات دولار بتهمة التشهير ضد صحيفة وول ستريت جورنال وشركتها الأم نيوز كورب، وذلك بسبب مقال حول علاقاته الوثيقة المزعومة بجيفري إبستين.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76259" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بوليتيكو: القوات والأسلحة الأمريكية جاهزة لمهاجمة كوبا، ولا ينقصها سوى الأمر النهائي من ترامب.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76258" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بيانات التداول: أسعار النفط العالمية ترتفع بنحو 4% صباح الخميس وسط توقعات باضطرابات في عبور ناقلات النفط عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76257" target="_blank">📅 08:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76256" target="_blank">📅 06:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76255" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي عن مسؤول أمريكي: هجمات "محدودة للغاية" و"دقيقة للغاية" قد نفذها الجيش الأمريكي بعد سلسلة من إطلاق الصواريخ والطائرات بدون طيار والقوارب الصغيرة من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76254" target="_blank">📅 04:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
🇮🇷
أكسيوس عن مسؤول أمريكي: أطلقت إيران أربع طائرات مسيرة هجومية أحادية الاتجاه تستهدف سفينة تابعة للبحرية الأمريكية وسفينة تجارية.  اعترضت القوات الأمريكية الطائرات المسيرة وضربت أيضًا وحدة أخرى إيرانية لإطلاق الطائرات المسيرة على الأرض قبل أن تتمكن من إطلاق…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76253" target="_blank">📅 03:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">إعلام أمريكي : الولايات المتحدة نفذت عملية دفاعية في بندر عباس بإيران، مضيفاً أن "الولايات المتحدة ستتحرك لحماية مصالحها الإقليمية، وهذا لا يؤثر على وقف إطلاق النار".</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76252" target="_blank">📅 03:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/76251" target="_blank">📅 02:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76250" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNGzJAGCp8FP1yZwqwMsHYbdispmMsdGj9gOAhJRq8dBv4d_bOoHIkRQPjczMZoD4ih-WtQ16eC8n_YqjT1ULDbMgHu_sr0dK1IgOiFY7vkxZNXcbTKVhzHOcZybG9t4kZ-VeDTVxsZjvG3IEQXnO43tW7S41FOarMpj7PylOAii_s_mZJdj-0VY1-W2Mdj_YSAF0wKIeEVfrBqoVB98JjhCxqp2MzjYNKtYqsQxRSZuQUjGay69J1H_U73c1HwPOTtKjd0Me1DzMpoVONPbz_RogTjUkw_KY-oSMlemwqUAdgryfYyYBRgGmuSqvpmJ4XH3VD1ERgX9La8PVpRkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
وزارة خارجية كوريا الشمالية:
لن تتخلى كوريا الشمالية عن برنامجها النووي أبداً.
والبي زود خل يجي
...</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/76249" target="_blank">📅 01:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76248" target="_blank">📅 00:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=Qz4pglhEOoIeAEBOQXMA7ClQOb4s-WsGozpTxwmG5fioDI4vQgp11Y8UkKHJw1Uq6rLqvqkM4rTcFODwJRH-tGkKfltI0wboPgMrFXlhYHzZH39nirQyCcjQCSBShYuwgOtZHJFdBjVSLlDiGd5TxwIudcEynuNqu2_6wRut6r1nK0uQBt_JHDpD5WJfTt9y3r4zbwWHZ7ouYLWCQjmHIysAjFIxd9Hi1zIga6h-m6J1H_KyIJIllNSROY-gb4WM6yetteBhJji1LSygJg-W9EWSOaXNAaQOkypZCCCMUqIvO7se98CfDL7ZrrAcWLKvkseGbcNZ-5JTRV0DSba13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=Qz4pglhEOoIeAEBOQXMA7ClQOb4s-WsGozpTxwmG5fioDI4vQgp11Y8UkKHJw1Uq6rLqvqkM4rTcFODwJRH-tGkKfltI0wboPgMrFXlhYHzZH39nirQyCcjQCSBShYuwgOtZHJFdBjVSLlDiGd5TxwIudcEynuNqu2_6wRut6r1nK0uQBt_JHDpD5WJfTt9y3r4zbwWHZ7ouYLWCQjmHIysAjFIxd9Hi1zIga6h-m6J1H_KyIJIllNSROY-gb4WM6yetteBhJji1LSygJg-W9EWSOaXNAaQOkypZCCCMUqIvO7se98CfDL7ZrrAcWLKvkseGbcNZ-5JTRV0DSba13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اشتباكات عنيفة في محافظة كركوك شمالي العراق بين القوات الامنية وعصابات داعsh اسفرت عن مقتل عدد من عناصر داعsh وتدمير عدة مضافات.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76247" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هل قتل العراق العقل المدبر وأبرز مصنعي الأسلحة الكيماوية في داعش قبل يومين ؟!
ننتظر التأكيد الرسمي</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76246" target="_blank">📅 00:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76245" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDG1daCJ7dGDzmWFER-y6X4pyBFeBKzANKCpLHxGosO5tQyc44mHxQrjck0Yp0_fFqODbg_kulE583RDx4f10sRxjbsLl1KFyiKb-ZxM0xNPZg95M2O79FM6N74dilry8FK11s_wnxCUSdWUD-NMYjkznjjd7Mr6RmXycp1UpVIhMcv0s49mi6bCkvAa7kl4WAl1bfHLnxc2zutROkKzxGW5lczy9mioubaL9KctOn2z9cfJ9JbigWVgbdK1pONfQ8WNjPQa-J8v7I1rVe3Jam-zdAEzj4Pl8BU8QnSFCmtr6ZTffzCngdsWlEvuGnvpgyG_INgOWy3qUOAf_W6SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية: قتيل و7 جرحى في شوميراه بعد هجوم مسير لحزب الله.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76244" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
أُنقذ "ترامب" من الذبح خلال عيد الأضحى. اشترت السلطات البنغلاديشية جاموسًا أمهق نادرًا يزن 700 كيلوغرام، أطلق عليه السكان المحليون لقب "ترامب" نسبةً إلى خصلة شعره الشقراء الأمامية، التي تُذكّر بتسريحة شعر السياسي الأمريكي.
كان من المقرر ذبح الحيوان خلال عيد الأضحى، لكن الوضع استقطب اهتمامًا كبيرًا، إذ بدأ الناس بالتوافد لرؤية الجاموس غير المألوف. عندها قررت السلطات التدخل، فاشترت "ترامب" من مالكه، وأرسلته إلى حديقة حيوان دكا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76243" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026 منصّة منظومة مضادة للمحلّقات تابعة لجيش العدو الإسرائيلي عند مرتفع الجرداح على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76242" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: النرويج وافقت على الانضمام إلى المظلة النووية الفرنسية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76241" target="_blank">📅 22:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
‏جيش الاحتلال: إصابة جنديين نتيجة إطلاق قذيفة مضادة للدبابات جنوبي لبنان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76240" target="_blank">📅 21:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
ممثل المرشد الإيراني بالحرس الثوري: هدف المفاوضات ليس تقديم تنازلات للعدو أو التراجع أمامه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76239" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏المراسل: مع استمرار ارتفاع أسعار الوقود في جميع أنحاء البلاد، يدفع الناس مبالغ أكبر مقابل السفر. هل يدفعك ذلك إلى الإسراع في إبرام الصفقة؟  ‏ترامب: الأولوية القصوى هي ألا نسمح لإيران بامتلاك سلاح نووي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76238" target="_blank">📅 20:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترمب:   ما حدث في إيران هو تغيير لنظامين والآن نتعامل مع الثالث   سنمنح إيران فرصة وجيزة بناء على طلب رئيس وزراء باكستان وقائد جيشها  لن أقبل باتفاق غير مثالي مع إيران نود أن تنضم هذه الدول إلى اتفاقيات أبراهام. أعتقد أنهم مدينون لنا بذلك. لست متأكدًا من…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76237" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامب: بإمكاننا إنهاء الحرب مع إيران بسرعة كبيرة، وقد نضطر إلى ذلك. لكنني لا أعتقد أننا سنحتاج إلى ذلك</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76236" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب: "نحن لا نتحدث عن أي تخفيف للعقوبات أو تقديم أموال. لا عقوبات، لا أموال، لا شيء على الإطلاق."</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76235" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=CdmgmnuBelsx4brdPYaV8lmuB0eX1_2DDONGpvL7IW9XE_BKiWCXZsl2cW67I0yLQZiSiPwNYBmg5H3bgxsnKBaRk55CPnAVLdV3ZIr4KbczvXbe5SWFmMU7LJOCHB0oHlFDUL1ISa8aJKVDi_kaxvlbZbK-KhP-6qphWxORR4-4bA4GrJswUlvz_Ow01yw_SUwgJYKMLhRLzlx2uLyLEekvwQD_ISPmYlZzmgF3-l7n3Noqu052r4Pf2iRcFl1Dsm-PRltBUJEvh8nmDPwvv0PR7QTenKwYdozUJzzAXejBJU2s3TggnhYVpO0_TzAqcYEZltB0PoCSuar4JEe_m4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=CdmgmnuBelsx4brdPYaV8lmuB0eX1_2DDONGpvL7IW9XE_BKiWCXZsl2cW67I0yLQZiSiPwNYBmg5H3bgxsnKBaRk55CPnAVLdV3ZIr4KbczvXbe5SWFmMU7LJOCHB0oHlFDUL1ISa8aJKVDi_kaxvlbZbK-KhP-6qphWxORR4-4bA4GrJswUlvz_Ow01yw_SUwgJYKMLhRLzlx2uLyLEekvwQD_ISPmYlZzmgF3-l7n3Noqu052r4Pf2iRcFl1Dsm-PRltBUJEvh8nmDPwvv0PR7QTenKwYdozUJzzAXejBJU2s3TggnhYVpO0_TzAqcYEZltB0PoCSuar4JEe_m4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إيران بدأت تُعطينا ما نريد، وإذا لم تنجح الأمور، فسيكمل هيغسيث المهمة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76234" target="_blank">📅 20:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏المراسل: هل ستكون مرتاحاً لو استولت روسيا أو الصين على اليورانيوم المخصب الإيراني؟  ‏ترامب: لا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76233" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامب يهدد سلطنة عُمان: على عُمان أن تتصرف مثل أي دولة أخرى وإلا سنفجرها</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76232" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=WBr6ayAl_ompQ_AFTPHZ3CxUHf3hyeFvhCt2Ubz3we5akeYQvX4LBElO3uhIPwSpOWIdqvGFEDw4gffWShtpNfToqJ1hmtwOeESjvdfpHbigmB_SaCJPhlqK0_UL-aG6FB7NOdFuGwXjPOxNJEQkMOXq54ua3wuerzk5VVYEUSLsilWUd5bxoWwillfAgkLMfMJ5vW7W7l06izr8NcqQrpms501cUziioWsdQCJnp8ffwr_9_t3RYHknCNnK7R4nkKQyTUE3X2AFDkD97qjkPFwKPrGRnvNcAe7aMKr3K4d5iFBCc-QQYxxGfxqnhkvwe95hFvpxsxB-AOlLuLi3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=WBr6ayAl_ompQ_AFTPHZ3CxUHf3hyeFvhCt2Ubz3we5akeYQvX4LBElO3uhIPwSpOWIdqvGFEDw4gffWShtpNfToqJ1hmtwOeESjvdfpHbigmB_SaCJPhlqK0_UL-aG6FB7NOdFuGwXjPOxNJEQkMOXq54ua3wuerzk5VVYEUSLsilWUd5bxoWwillfAgkLMfMJ5vW7W7l06izr8NcqQrpms501cUziioWsdQCJnp8ffwr_9_t3RYHknCNnK7R4nkKQyTUE3X2AFDkD97qjkPFwKPrGRnvNcAe7aMKr3K4d5iFBCc-QQYxxGfxqnhkvwe95hFvpxsxB-AOlLuLi3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏مضيق هرمز سيكون مفتوحا أمام الجميع ولن يتحكم به أحد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76231" target="_blank">📅 20:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76230" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 19/20-05-2026 لمحاولة التقدم الرابعة لقوات وآليات جيش العدو الإسرائيلي باتجاه بلدة حداثا جنوبيّ لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76229" target="_blank">📅 20:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
روبيو: الدبلوماسية خيار أول لنا لكن هناك خيارات أخرى مع إيران.  ‏نعتقد أن هناك تقدما تم إحرازه نحو التوصل إلى اتفاق مع إيران وسنرى خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76228" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر.. إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76227" target="_blank">📅 20:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=jVbg-Pq7x6qIVKWJqHpxhaamYjZqRh4mSbNWLrwhbBmJkqqQvk6OLWNodMCyM7zC9U-e0ENYNgoOlKi8HCHuNOyOTXf5PWFecrM2vVlpPLgP-8JjdTgsd8PjEh_eogD_8U2QeFz_mB9ePqimEM6nilN3YUaju4CHo-0vXsV8pbFh3EDFWPuPGccZdeKNtQfwnO_DOudeXv9_Sid0FsdQHjrMvuvyzHkT-LsvaNc-4PzAX-kTaJUZwofFDbT6FSeuWoQxI6Ao585Se7SiY_fsZUFZkSXqBBe41jy3J_h-qmh5_ovVF21tJnIB0YSkEJpqmKblm7a0SSCAWSHLQwu_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=jVbg-Pq7x6qIVKWJqHpxhaamYjZqRh4mSbNWLrwhbBmJkqqQvk6OLWNodMCyM7zC9U-e0ENYNgoOlKi8HCHuNOyOTXf5PWFecrM2vVlpPLgP-8JjdTgsd8PjEh_eogD_8U2QeFz_mB9ePqimEM6nilN3YUaju4CHo-0vXsV8pbFh3EDFWPuPGccZdeKNtQfwnO_DOudeXv9_Sid0FsdQHjrMvuvyzHkT-LsvaNc-4PzAX-kTaJUZwofFDbT6FSeuWoQxI6Ao585Se7SiY_fsZUFZkSXqBBe41jy3J_h-qmh5_ovVF21tJnIB0YSkEJpqmKblm7a0SSCAWSHLQwu_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76226" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76225" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=WLtGAVpIpry-n4J9OLOZ-BhFA9kh-Y8gJqBDQgqTTRRXoE4WPkofoPOS6dlyE5xgOn3eVgCO9vP80fYzZVBe-6N0Lh0lniIPtCY6lUhH_wtOY15FevcBo7Ahn_awXdXN0AIb_hQwz-U5PC_aRQzIbKq2EVRg2LyepQJaNcgpsVhbyR16V1r8rMkYhebCP1BpDbOuXR7IX802h5DkPEEvd7FeWH1TRbt4CBod8wd3x2zmrZAibbgGRrIgYSJDBv4wtlrWm9yL4Xkb8QQtp_hEKSn-iyWdLUmVfD9-_6ibo-VBCy5zl_QPTKNN1CORaNfCkBeg7HEDNtZx64Rja2yBEp_DWtH-YQQDfIOgS8W9uLPtcPdc0yqvgAlZac_G6Dt7JY7gVa6h3sKr99v8KC9XExw52U1yEWZoGRNv7rTR2sXJiAjS4c4L61SGg1w1pGaAfR9aohmZX2AGHSBPTcgMYeL_4FpOjP1tLGhWRybZWVWalokdUfn0J1ZBLt8VZpo6FuQyAvLq611BCb4v1xMUVjK9Oc1sW-HY8hEQj2k686BzrVAukc-En3M0D7hAQ7bnmHcO3zojKbWkEUkxii-h6sUk9A7cim2tE5SWLUIGgqctw1eESryeNY1JBWxavK-frgooqHZYA1vIoLo9OSAobjr2e686I0EpBiqG-cxSy_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=WLtGAVpIpry-n4J9OLOZ-BhFA9kh-Y8gJqBDQgqTTRRXoE4WPkofoPOS6dlyE5xgOn3eVgCO9vP80fYzZVBe-6N0Lh0lniIPtCY6lUhH_wtOY15FevcBo7Ahn_awXdXN0AIb_hQwz-U5PC_aRQzIbKq2EVRg2LyepQJaNcgpsVhbyR16V1r8rMkYhebCP1BpDbOuXR7IX802h5DkPEEvd7FeWH1TRbt4CBod8wd3x2zmrZAibbgGRrIgYSJDBv4wtlrWm9yL4Xkb8QQtp_hEKSn-iyWdLUmVfD9-_6ibo-VBCy5zl_QPTKNN1CORaNfCkBeg7HEDNtZx64Rja2yBEp_DWtH-YQQDfIOgS8W9uLPtcPdc0yqvgAlZac_G6Dt7JY7gVa6h3sKr99v8KC9XExw52U1yEWZoGRNv7rTR2sXJiAjS4c4L61SGg1w1pGaAfR9aohmZX2AGHSBPTcgMYeL_4FpOjP1tLGhWRybZWVWalokdUfn0J1ZBLt8VZpo6FuQyAvLq611BCb4v1xMUVjK9Oc1sW-HY8hEQj2k686BzrVAukc-En3M0D7hAQ7bnmHcO3zojKbWkEUkxii-h6sUk9A7cim2tE5SWLUIGgqctw1eESryeNY1JBWxavK-frgooqHZYA1vIoLo9OSAobjr2e686I0EpBiqG-cxSy_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76224" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
‏ترامب: البحرية الإيرانية وقوات إيران الجوية دمرت.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76223" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc9zh-FUVy2OAj61IlgWmwTvRW96UJsdtA35Yi0IP8CZc5JpDlwwi8YgqWPvNGfZ1WfTEaU54ZTXVlBqzclTzYqNnK-3P07JL4aXyMX1aWHTQjnFsDVuA1E4XUIvKm2VRn19y73SRQOkUU0wAH-Jg-B6GQ-WFpzXIGdwnUfswcZ6WWhyXV44FAlDxvB0yC1kw5p5hwiEhrE1yHDvqW7175T8ISHgsLHCWZ_cM9a2yF5_7k8kK7L8B1L5jROhLdbx3o_QuQVhT95QEfXsUpIBAZ7S0KHLr7AVSAu_kJTSy5tm0ORjFJeGiK3ED0Y6QnHZ3r0WjHosIPUvVogyKWFAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: إيران لن تحصل على تخفيف العقوبات مقابل التخلي عن اليورانيوم المخصب عالى النقاء.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76222" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjrFvnQzbi7jsVgnCHC28VL49ZuQdkjgj68mI-AqHFqbbYEqhHphX_UWvIUxhreY6tJhzxx2dkHFqL5RBK1LDbCWzx4MKKPP8OWCNSfWHB2LVtolSjvlxM7ZejpC80r17O37XWouoOoRL9vXvWP2RZt0e3Uz1oZpJVZL7wU6pfMa1u4yDmtpF86RTaMyLyS3QXisfzBZ4dDgcYQGffaroRXxDfrVlFibK8l2-VfKlRqDsD5GwDMHUiFnAVve1dXWsyuLPwydbQi5ZPYxxv9oEAtXaKg-oTDTSjVSDNWK4wT2B_ecvJ4nRryrPs0UhSZf3VSIzhKq7GI1UHIwjFZcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كل عام وانتم الى الله اقرب</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76221" target="_blank">📅 19:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
ترامب: يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76220" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
ترامب:
يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76219" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
تشير مصادر مطلعة إلى أن الرئيس الأمريكي دونالد ترامب من المرجح أن يعلن خلال الساعات القادمة من جانب واحد عن إبرام الاتفاق الإيراني الأمريكي. ويُقيّم هذا التحرك من جانب ترامب بهدف ممارسة الضغط وفرض اتفاق على الرأي العام قبل تسوية الخلافات بشكل كامل.
مع ذلك، أكد أحد أعضاء الفريق التفاوضي الإيراني أن بعض القضايا لا تزال عالقة، وأنه لن يتم التوصل إلى اتفاق حتى يتم حل جميع القضايا التي تنظر فيها إيران. ووفقًا للمصدر، إذا تم حل هذه القضايا بشكل كامل، فستعلن إيران النتيجة رسميًا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76218" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76217">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
قتل عناصر إرهابية وتدمير وتفجير مضافات بعملية نوعية في أعقد المناطق جغرافياً في محافظة كركوك.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76217" target="_blank">📅 18:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر..
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76216" target="_blank">📅 18:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=jtITtvOq9d9NDzcA1Ga_eVdTdZjz_kcy48SGt8abSVYOSF8XFJvOsRN18pJ439rcFGF6RlUS31xPxmCpcLZxlZ-K7YAMpvVya5u2ii5VUC7JmH4dXdzeTgzaALz0NCwyNS6VcSmWX6QeWRwVUwUN9-LL1juG2ASs22Z--Cjee920njNk86A9VPheq9MFqd67_innEfFO8ZeVlwPbstk66L07uuUYwrK93sNG0JRag0um8YIGqehaGM_vmVzvY4d3esLHvjXenAL1Z7gnr3hz_edkfZW9TD-FUClGAVw7JIYFaHDNerw3DPbEFU7VwucieELRRfn23Ja9TOQca4c1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=jtITtvOq9d9NDzcA1Ga_eVdTdZjz_kcy48SGt8abSVYOSF8XFJvOsRN18pJ439rcFGF6RlUS31xPxmCpcLZxlZ-K7YAMpvVya5u2ii5VUC7JmH4dXdzeTgzaALz0NCwyNS6VcSmWX6QeWRwVUwUN9-LL1juG2ASs22Z--Cjee920njNk86A9VPheq9MFqd67_innEfFO8ZeVlwPbstk66L07uuUYwrK93sNG0JRag0um8YIGqehaGM_vmVzvY4d3esLHvjXenAL1Z7gnr3hz_edkfZW9TD-FUClGAVw7JIYFaHDNerw3DPbEFU7VwucieELRRfn23Ja9TOQca4c1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور اللبنانية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76215" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
‏التلفزيون الإيراني: طهران ستتولى إدارة مسار حركة السفن عبر مضيق هرمز بالتعاون مع سلطنة عمان وفق المذكرة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76214" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP_3Rz-wyxI5jTYoCQrm_O11CUALhsPUXB4CYg3Awpp5NiF8WE4-rL8xllvAJRfE9jiRzsAgnwtPTpoEPYyEfAEbUqTnjgxasnDqeNTxhVx26_iPq7V9PpOhbjak9c4pjY5epGC6BLl2V5fXVYJRSjxuI7-CjA-M5BtUXvpSCO-FgapBKyvRor_evOq1pk7n15ZF-_XltbUmMLtQUwJJBmdogc5467XsX4YPm0f3Hth9-Cz1KpV8KXBDuexqUxfdiPDSyr3pV7Z7jqSrrrOd7Cp3BxKjF0TXvrH3WgOqeaoEDHN-j39t8QJirznrg-yLoYuo90VW0PiU2m07Q0WHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
اعمدة الدخان المتصاعدة في العاصمة الإيرانية طهران ناتجة عن حريق طال مبنى سكني ولايوجد أي حادث أمني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76213" target="_blank">📅 17:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
الرئيس ترمب قال إن المفاوضات مع إيران تسير بشكل جيد وأوضح خطوطه الحمراء بشكل جلي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76212" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=taSuk_GyNX4O8ldb6NOuJue-auoTHzNi8WyboFw4NNi7J3gDHDdUsHQ1h1oaC-bDesUIk7MMhct_Xt4A1_oa3zrpQxoQDG_QOYSdfcFk3mcxLerq0JDWP1U9sWPBRZp4h6edqLAqqPz_Rbaoh0WR77iQTnvJ0uRbCkb_yTm7QDdPyaJfuCmEtIeMDeHQToZo0aP8Z_0sJlE4VHILX3y_23eK-EWIefWkNcENpo8wjXBIL-t59B7P1vzuVYWFqJYfbqlHADsJmactcYRQRLrhD604Sxl3Spp2VAWa54qAjvoA2DZFpM-zOb6x2gBvMrRyZxbQPDuLnL8MtqenREA0KVGgrbGFNjEcJ4DwaRFG-GT-U9A8LddnrADBWILTxe9SFqMplqFMS7YO_GG-kTOrPEgL72mT7pxkYQqLip0tsBGZyzsvDjcPhN5BI8HqI00nFYFwcxYLnaVWs686V4hoY8uFRXiTKrJD4IM55ETqpnMsDZUJuHb7GhHDHDJrOqx8M_Vg5ySOUb_QL2ZBz3TyN5olsZrDZDzNQQNJJUFHRzxAIUosWHGy_RHGk1CArgC69-UPXnohR8PO7HFN66vsCifLdHuAuI6vNRkU2nLTrMnf9S-VP2SmqkO8IvsftBytS2VSWgGFaoUuwQXtr3NwRfvy8z-F7sXF6gTM1QJpQ0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=taSuk_GyNX4O8ldb6NOuJue-auoTHzNi8WyboFw4NNi7J3gDHDdUsHQ1h1oaC-bDesUIk7MMhct_Xt4A1_oa3zrpQxoQDG_QOYSdfcFk3mcxLerq0JDWP1U9sWPBRZp4h6edqLAqqPz_Rbaoh0WR77iQTnvJ0uRbCkb_yTm7QDdPyaJfuCmEtIeMDeHQToZo0aP8Z_0sJlE4VHILX3y_23eK-EWIefWkNcENpo8wjXBIL-t59B7P1vzuVYWFqJYfbqlHADsJmactcYRQRLrhD604Sxl3Spp2VAWa54qAjvoA2DZFpM-zOb6x2gBvMrRyZxbQPDuLnL8MtqenREA0KVGgrbGFNjEcJ4DwaRFG-GT-U9A8LddnrADBWILTxe9SFqMplqFMS7YO_GG-kTOrPEgL72mT7pxkYQqLip0tsBGZyzsvDjcPhN5BI8HqI00nFYFwcxYLnaVWs686V4hoY8uFRXiTKrJD4IM55ETqpnMsDZUJuHb7GhHDHDJrOqx8M_Vg5ySOUb_QL2ZBz3TyN5olsZrDZDzNQQNJJUFHRzxAIUosWHGy_RHGk1CArgC69-UPXnohR8PO7HFN66vsCifLdHuAuI6vNRkU2nLTrMnf9S-VP2SmqkO8IvsftBytS2VSWgGFaoUuwQXtr3NwRfvy8z-F7sXF6gTM1QJpQ0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 تجمعات آليات وجنود جيش العدو الإسرائيلي في ثكنة بيرانيت شمال فلسطين المحتلة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76211" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0780e7c6b8.mp4?token=jwrgxxLnr7YE86AoiFeOdZBULX2_C8pvWASu1H_oaRtUEbIqENgPpbNXgEn_vrdFMmj2L4pcDEUASFg5wrFJVOhT4Qrwz5b_cQoy8EZJDdzhcIIPxlt3BawvuPaYSiE7KrRWx6-GA691hJoQwf4_fdl3RVrPLSOsV3P-gwgUbUsFxvlfVMmUQQuLetYPtVN4hOXfip47HRqogT26YG0ZV7sp5JeGv_KNTJM4PO1j6xbyDlDcXXH3WyYt4mOE8tEXR-g8qJY1jnDndlYCAc6ziLB-dJzGb8Mh9mgNzyZWcyZBIZEbL6cHpuNKHq3uRZoQksXJi5HVycOhBBbGS6EBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0780e7c6b8.mp4?token=jwrgxxLnr7YE86AoiFeOdZBULX2_C8pvWASu1H_oaRtUEbIqENgPpbNXgEn_vrdFMmj2L4pcDEUASFg5wrFJVOhT4Qrwz5b_cQoy8EZJDdzhcIIPxlt3BawvuPaYSiE7KrRWx6-GA691hJoQwf4_fdl3RVrPLSOsV3P-gwgUbUsFxvlfVMmUQQuLetYPtVN4hOXfip47HRqogT26YG0ZV7sp5JeGv_KNTJM4PO1j6xbyDlDcXXH3WyYt4mOE8tEXR-g8qJY1jnDndlYCAc6ziLB-dJzGb8Mh9mgNzyZWcyZBIZEbL6cHpuNKHq3uRZoQksXJi5HVycOhBBbGS6EBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اندلاع حريق وارتفاع أعمدة الدخان في القدس المحتلة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76210" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
🇮🇷
أفادت قناة N12 الإسرائيلية أنه من المتوقع أن تنتقل الطائرات العسكرية الأمريكية، بما في ذلك طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي الموجودة في إسرائيل، إلى قواعد أوروبية في غضون 72 ساعة إذا تم توقيع اتفاق مع إيران.
‏ستعود طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي إلى مطار بن غوريون إذا استؤنف القتال مع إيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76209" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭐️
وسائل إعلام أوكرانية:
أرسل زيلينسكي رسالة عاجلة إلى ترامب يحذره فيها من نقص حاد في الدفاع المضاد للصواريخ في أوكرانيا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76208" target="_blank">📅 16:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76207" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76206" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulg2a9S5s8PSc-8dtnUA1w0dLgJax3Dz1T8fxbYb8LqqWzoKwB-3D4YebrOMfZHPvxDCiYQoTm2nL3k_MXVaqtXqRUCCLeECLod9c5Dtsx9HnS8XV1kvhuFISqvrYV69LFcxuscq5RoK7C4GW1g8ycwpw3mLIq9-HhQkRXJMxmsJKYuDXJfm1u4wgMeG2uWQSy2X9An5i2xxbC3ikrlD_q_z-PY27dCqA0BM7Yxh0Pz3Vp8L9S3KkMk85L-5SICawwBePyNxiUcFXL2g7V9kUBlfG787xA6B5j5z_nOGn6h8PEUYmeXXx-Dslshvkt_MwF4Bpk2Z6oMR_YCc6CP-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
🏴‍☠️
مقتل واصابة عدد من الجنود الصهاينة في ضربة المسيرة في شوميراه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76205" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76204" target="_blank">📅 15:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXgzzXTeVGEQj-r_okpm9UIORkqvzGWXZM2Mf5Dxi1gIWr-Al4vyEpOBAgZXnifpTBri4LO5FN25mTm93FlLoTrYfIoW_2fJ5LNhN4ToTH6aqBbnH9eRFc-delJ1NzcKOjoYVy4XOacxC34jwdtpmLnSZxdXqft5Bm81u3S7AqCHighNmSU0thNxJRhOa95DgJw-jGdVMSJ4jHb5d5K5SkYwAXfcr0H-_8fl3CbDW8Z4TcE7tYCgfE4NKi8G99tx7W3j8wJAiXi4N8zsjKpeLMbpoulAX_8tgHxJpM5Dfg29B08RCPhyZTVdWPKuXkG0dKO_ZnDaI0bSN1IuAw6Cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي يشكر مقتدى الصدر لتسليمه السلاح ويدعو باقي الفصائل لتسليم سلاحها</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76203" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76202" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في مستوطنة مسكاف عام على الحدود اللبنانية الجنوبية بمحلّقة
#أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76201" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1y9wHQikB1wzSuCaQE_R4QSPiBkjhpx6jC1z0Tn2hibXzecwCbVbKbm_kiNCPiVE-fvIDuHsyESLMccyAaZeIRCwO0yXAXVwk4PQcNrrs278kS_ZjqEYsTOGmaHZAuuxwdDAJK4Xhz5N2z1LSf_iw0cGb95FZ5_e6Z78VyFUtn8jUKzKm2SwlP9v_FJzK6f43M0JxPHBpIBfNevryqb-clm0VvV9Q0C-jyfbjM0XDooMrBrUoGN-EJ6Dlmy8rtfjq__fabMiEmY8pWCKVDjC3CNMUHKpuzIhAsdw_d_Q0k-3hFaFe0t-xJ4z0C9X25ptaXdrtMdAdBYp2OSdPggEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SS636Nhio5vpfLYIcoH69FOBTc7insY5IUNeBrRdzw7nZ6K63vdA50HrSjTlu14ADIiwi3lDjxU878k2fAHxud2dJQURmlanxpoUfixeJXeBrg8KDcn9ZqoJ3O4Kq839VNYSC-98zH3amDKiOJA3_HmqNfFX0msUeSmlMrKPBH0vCYPn-RbNj7yCswhpiROJ2havpVYX_NqsJ7MeOS8GUs8I5zo6y52aGuZXl3PIlVMivupgg2PbPRU9X0NXwSpnfZqPH5BWmwOCDI5pcsuN1uGEMKx3bUYtWpXmTc5qtekXkEdLPoDL4Kvg6bP0cGYKq3exzEARMuitfcr4CknRrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76199" target="_blank">📅 15:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhrSYxotHV--Ie2cxhVW1eoT_FPor3WQbJ7-i41Y54pH3g6VhajNjgT_IqMDQ-PYZXpWun6jjPdErEyOjBCQQUFCOrGimVfNkbsuWN6DiNguz5BWsgi2c1Ahnt8_IROas2qjZG43frEEEZiCxkkx9wBERoZde58hBfk4KfoTt62H5wD1qtgQthAXi30UR2Yh32wZ_Nfvt0KdFBgf3GI7hdaT9Za52euQMR4xDGNvqc2ziG2AHjXa-pZWc1dxIIbJpP_TmhjhPQvRHfoJAGm5hg8vp8tkJpUaL9bvpuNIn32db60TTw9eLtzy4bIcE4zYTQ8xmgpA2xqnXBAna4G0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76198" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=YXDQtOS51j2pFu_F-aQCwoNT1v4AC-OyzL_PUZeZoOpr-z6jCeVo0fufwvkwLAIQwM8ZuhIXsOiEqmDf9vM4L30AjRx1ekvXS5GDTVS4nG8MGvo-If3ea1NnUf5Sj2K5PqI_mLLQHsMFCOa3BUmUqzTygSe_p5iThBs6lKiagSD1qihGCRWP3Nd0H0KVlNbxXdatoS5d_EXWeDSwfUtTPqArOrBjHH9AeXNu47qCeOr1zhWAP1xDn16zpX3UPWnI_OJ6cQUx5qQFQ8Tctjn7jk5tmOItHSzC24Edft6LEkl1zIXEeTHmEsSx_Iz0caIOpgDgv405eIP2tglvxKGVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=YXDQtOS51j2pFu_F-aQCwoNT1v4AC-OyzL_PUZeZoOpr-z6jCeVo0fufwvkwLAIQwM8ZuhIXsOiEqmDf9vM4L30AjRx1ekvXS5GDTVS4nG8MGvo-If3ea1NnUf5Sj2K5PqI_mLLQHsMFCOa3BUmUqzTygSe_p5iThBs6lKiagSD1qihGCRWP3Nd0H0KVlNbxXdatoS5d_EXWeDSwfUtTPqArOrBjHH9AeXNu47qCeOr1zhWAP1xDn16zpX3UPWnI_OJ6cQUx5qQFQ8Tctjn7jk5tmOItHSzC24Edft6LEkl1zIXEeTHmEsSx_Iz0caIOpgDgv405eIP2tglvxKGVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76197" target="_blank">📅 14:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaIRmrYtFDuXFLr2OZLRhKs1C3kuKX1g9UVYX0ndSXtDJVXKmo1ZqwcTwQ0u4dcLjAZx10V-A8h9nXwp977FrZUeupyaSYi0dz3lqmrhzBJ9vv7p8ffFG6TkHBDKYeX7d_J0FSCVX04xccg0Ak3zNUErIAnp0tOTGsipe-LGp79GFYzWRgaCGmqLMk4cYNclIHdzmJ6Xghzz9sIBksitXQLhcB-bpVI0z9nzz3W6w-Nh4pOjIgBQ-EpAT4T9BmO5-UOpW9n6G0dh1FwfkbhYY4ShIIuP07f8p4LiQI_v0GC0RQoZ6hycAw5fJs3sZEX2m4d_JFkNznc6blDTfhp48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dxx0fqdDRY9vZ5KCCjz6dxw6gofF1HACu3SJIHMKtTQ4jIZ5jE73qNgsAyfSj3WfEFzCLFarkQSmw1t7Ld6CuolcYq6zo38YGEo3aeiIRSePG0PZ6uPG3v7mt4PYpWF-lrzf3AkOtIUPXbmSn5ac96KWpVAim8mItpWrPHSRP9ij4yv0BPYgLohvqMl24EgtlVH8tpyZsJI_7V5Ux-OZhOaiVqk8fE-M05l3kLHYsoJY5eBpxk8nkwTUDThz0ViWPPMxD8SieL7QRPLUdFnclknyBl34ED_a5_pdYGDBExNWX76PdK1ddOGSEBeERldeIR-u-d11eHjUHBnsT_A3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4dAfN5Y9_odIJJ5FNT9nT9MXGBiHof-oPduqecGBAnlm-juanG8qMFvcwSSFYGqoRs7S6rBocmnmRAeEyf2UFYmM54W5y-U56R5jV4rG2PHECsNwNrbOPVZCGAQO9MlCd-ftE2Zj-XFqPHrsL7fP2_-Xf9_vQBClEaxa5nYpctGS83sSp27De4kGT2fQLegJNxXgu9s9VFKJONyxs8kkNSHc6Cy0uHLkE1IjNy27BDzGjdr6BRG7QveKVeOyy6hK0dRh4knNvZECLYxV0enrIc_yk6bobyvoVdU-jIsE-UGT85_SolG3N4s0PzecGT8qMcgU8oSpojX6OicSofkmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=EXhW4B3FgXXmgYzNQllHZNMX4LXoa3xx1YsemZihXmssCd56bKVzoOXDh28LZFKd9CItqiDqsT17p8twBPnOJHeXEtPng_Tu1f4SV5GgiC7DQc3yB7Qp3FDfREKWNmsSXOn1aQv25XbOUsyP8HJQj7gn4Us0ue5s1ku9tL47Pa-LdldzN_4IJO0wNtxMjE07Ud9UYgir0aArjQpa_U-S3TuHdrq1aV0WDrkGjH5JUGPOGDyMNVSSY9hSBIlcjqiy2ObvLvLiWHBDHuMhW6WOb4_Zai6p2Acwx2Lzpzu3ztDFzIHMVR9DzMvjWT5Wx7bhXTrGoMRQhaWrowNH3r33MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=EXhW4B3FgXXmgYzNQllHZNMX4LXoa3xx1YsemZihXmssCd56bKVzoOXDh28LZFKd9CItqiDqsT17p8twBPnOJHeXEtPng_Tu1f4SV5GgiC7DQc3yB7Qp3FDfREKWNmsSXOn1aQv25XbOUsyP8HJQj7gn4Us0ue5s1ku9tL47Pa-LdldzN_4IJO0wNtxMjE07Ud9UYgir0aArjQpa_U-S3TuHdrq1aV0WDrkGjH5JUGPOGDyMNVSSY9hSBIlcjqiy2ObvLvLiWHBDHuMhW6WOb4_Zai6p2Acwx2Lzpzu3ztDFzIHMVR9DzMvjWT5Wx7bhXTrGoMRQhaWrowNH3r33MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76193" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKaM_x-bDluELyBfwkwsMgDGoW4WEhZkeLMeljScpagGlUC24BsHArASq9lLXhRp0JKDFDwbSxp2omsGOKr_qibEjy2eXohCgkqqYqbvv7tlGrF6AxcCGP78VsCvG0op_7Ubu-PQzAQkMBq-VaOsyaWhn15iV1IkC6q5P-DzuDuCafnIK799cbC-p3pK7KbCdVxp8ff_npFK9WU95p8oGvrybYcxxcVMtDBjGVr7NSNe6uOOMritw6ZEeuPBwGEzFH2ZCGk38KqxgQYfcGfeC3oIK3g1E74CqUJQraOAlaMAet37QQAt-sIucgWJhdMuJvq2dcs-ug1XQQoziJysZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76192" target="_blank">📅 14:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=AJsqXB4NquRgV6pEpsJmlXdw8InkEtBvzjoX9YOgQrgakgJDTqlqvv7zTt42oclZUIpU22edHVSs9xhiO2aG9XF4TtqnWWXU2gxzYYA7HYGpqzS7CeGfQtL_hD52-HQ-peI5-UoZagEYOrQK1Jgo06XwaVg5_3AGDoCnLMWZ3ePhuHB1wPbAmdf8bzfgvH463xOPLaDsMKrZpDz0zc9E3waj5aQh6n8-V1AVoZVFXSoE5lNs_YUplf0UHmp0aHuAskIDLFyxy9xVux_-7rYCESOR4V9hwhcWOJniT9pKHRN8lCLDUALhpsncUPbE5c7N3zkouWwx1gsd8pZgMRD66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=AJsqXB4NquRgV6pEpsJmlXdw8InkEtBvzjoX9YOgQrgakgJDTqlqvv7zTt42oclZUIpU22edHVSs9xhiO2aG9XF4TtqnWWXU2gxzYYA7HYGpqzS7CeGfQtL_hD52-HQ-peI5-UoZagEYOrQK1Jgo06XwaVg5_3AGDoCnLMWZ3ePhuHB1wPbAmdf8bzfgvH463xOPLaDsMKrZpDz0zc9E3waj5aQh6n8-V1AVoZVFXSoE5lNs_YUplf0UHmp0aHuAskIDLFyxy9xVux_-7rYCESOR4V9hwhcWOJniT9pKHRN8lCLDUALhpsncUPbE5c7N3zkouWwx1gsd8pZgMRD66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات تهز مستوطنة شلومي شمالي الكيان بعد هجوم مسير لحزب الله</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76191" target="_blank">📅 12:38 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
