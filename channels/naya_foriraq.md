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
<img src="https://cdn4.telesco.pe/file/oO-Io2zz8vx2YQ3OGKIx_zt-LEDfmTadNxBwh_mhw_v0TjrF3JLb7wFBAFxQ1g4pSIvzY4G2caYkNEc_aXuRM-t-Gyw8tDpLER34bkp8pPhhbayimLRqrNrzg61ShwaWl4GFPyQqgE9yg0o-Q3k5MKdHOW3EP0sOJTynjpxj6YXeJmuoFdoIowAei8_4FD-5YydbLauPkqDLmTY_9Np3J7KY1Ad_MNQQudNyKhI3eDzJFkGtn1ATnTENWl-sv9Oc4MdTIcNsaKR0dqMpF6irl_SFPblooVZrA3iFfx_lYQIWsKLFX60RebdvVUa-ufPbwo-UuG1C9yqnmAP--A3YqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نايا - NAYA
pinned «
جمهورنا العزيز..  القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه   https://t.me/KhameneiMediaIQ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80943" target="_blank">📅 13:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهورنا العزيز..
القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/naya_foriraq/80942" target="_blank">📅 13:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
المتحدث باسم الدفاع المدني الإيراني:
لم يتم الإبلاغ عن أي حوادث حتى الآن خلال مراسم وداع السيد القائد الشهيد.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/naya_foriraq/80941" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
سيقيم صلاة الجنازة على جثمان الإمام الخامنئي في طهران آیة الله سبحاني (حفظه‌الله) ؛ في قم: آیة الله مکارم الشیرازي(حفظه‌الله) وفي مشهد آیة الله نوري الهمداني(حفظه‌الله).</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/naya_foriraq/80940" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lygn6Gpft4LY3PeEYLERmRv8bLdlU_GTq0dESAAll3-h6JjKxtewraDm-yaegCUntzbBeg80J3pPLo9iPNyAO-Y1hwNuxmdKJCqM28HFLmLKygD43ziGtK3RGIDEHB4OVa-WXqk-Ummviw-zDnXmU6ODVyYqguvg69lbbT79L6M8BIXE2iTLOf2Ce271E5AiWL2iM6zraEQIYHNqirp1cuhVLuwDjbW4nhqEMAhhuQwId80aOINEz3oq-dtVoK5qH5KB-c3csdAQqR7_c_I50L7W8rA4LW2VvJuQIwXZr4W1ic7tiAtvnJ5_lnmk0-zhd4mVKAi6siuvI7wFpSzT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
في العاصمة الإيرانية، قام المنظمون الروس بإقامة خيمة خاصة لاستقبال جميع المواطنين والضيوف من روسيا، الذين جاءوا لتوديع الشهيد الإمام خامنئي وأفراد عائلته.
على القماش الأبيض للخيمة، مكتوب باللغتين الفارسية والروسية: "الأتباع المحبون للشهيد من روسيا".</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/80937" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M45Q-7SEEwMskZTXi5zJOHVX177pkEpqd9DZy_hqySM2WHV44uP-jcs2AHcn9_5J3j56BRku-_5wOqLMuTVJm_UKCoFOXI8B8Ej9ffshr45H8x3Q4_SoqjbaHZPIuFk8lsMWoSCEHYdrAVs8YL14xmIHmC3QsJktiHRJMEdg-kJMVujTDuothLLH4APurXjdhTIG5t45dmTwRq5nevEm8jSi1L3Cpt0x6601aoiAA-7cwjnUsg84H4eXUcdKCJqrWYHeepkWwKXEKraGOtWoaWl3M52CHe5D7vxDjBa7KbCw6oMf9kBMGyquBMHpM5VNloDJyt4DV_u4CQxpehUtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئيس العراق : بعد الانتهاء من ملف الفساد سنتجه إلى "سلاح الفصائل والملف الأمني مع تركيا"</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/80936" target="_blank">📅 12:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
معاون رئيس أركان هيئة الحشد الشعبي لشؤون العمليات، ياسر حسين العيساوي:
اكتمال الاستعدادات التنظيمية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره)، والمقرر إقامتها يوم الأربعاء المقبل في محافظتي النجف الأشرف وكربلاء المقدسة.
الخطط شملت محافظتي النجف الأشرف وكربلاء المقدسة، وجرى إعدادها بالتنسيق بين تشكيلات الحشد والقوات الأمنية والجهات المعنية، إلى جانب وضع خطط تنظيمية وخدمية بديلة لضمان انسيابية مراسم التشييع، والاستعدادات تعكس مستوى عالياً من الجاهزية والإمكانات المسخرة لإنجاح المناسبة.
مراسم التشييع تمثل رسالة وفاء لدماء الشهداء الذين ارتقوا جراء العدوان الصهيو-أميركي.
العراق يتشرف باحتضان هذه المناسبة واستقبال المشاركين فيها، لما يمثله الشهيد السيد علي الخامنئي من مكانة دينية وإسلامية كبيرة.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/80935" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8fo5ThK6gn2jEHcSoyXkvXORE4tdmTY4i9robs08zkTv4LWMjDDk2fFMiVSgI1D6XBph3p6uxvzHhzFFZrBeYIEjtkPO2VTsmcNit7srdZNuFfiMOh8GIi1ZY50-kUMyMfHYw71_eLUKnnKRyFcq8qKQbBGdEpK5Dc9gfR1OXEKl4NU5a0Qz_WWIXZxhbRU9nbbtb3A593yEBWK9JT0AUqa2zyBVlvzU60E5ygQ0tCA-F7wEElUFkzl8C8LcfEEEuMbPPzizTKenm79BHbF42YvLuRpf4lkMbm2oypMoJ_vY8zCNoXcxf8ClPo-6c8-c-iuRr0dAu_6XN6zGWQo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/80934" target="_blank">📅 12:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt8HTY4JijYmVmuRRkCmIpw9QNfhUC1nZO1d9L6-belWdJ5rybUmD3dxEJvLN7hkx3jczQaUhgPSSqsSrK6QzLsqufzEtHDJlfuS8WY1lNRydsUqbfXvul57_1Es-NYMXjVZy2BpwxcJKqmhro2JX8KsMYAz6i1sOEL9rOu4I9ofs9DiNcYJ7uY-V00mX8UNnWbATAKreXFXTmRhwwBXpPZuOAD6EFv7imW8BbmeyVdwXAb7hN0J0t6u6Zfm6osgM9XyZiKziCV_rJCV2Np_xI6zD8EW6OlXOEGsgwVkxquxncUXr7nGdQVZTJ1Et_vLQiwYURZir1F5O6c1m5Mh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
عمليات الفرات الأوسط بالحشد تعقد اجتماعًا لاستكمال خطة مراسم تشييع الشهيد السيد الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/80933" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">المرثية التاريخية للشاعر الفلسطيني البارز تميم البرغوثي في رثاء قائد الثورة الإسلامية الشهيد.
#قوموا_لله</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/80932" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
في حادثة أخرى.. عصابات داعsh الإرهابية تقدم على إختطاف مواطن في منطقة التون كوبري بمحافظة كركوك شمالي العراق، وتقتاده الى جهة مجهولة.</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/80931" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/80930" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
رئيس الوزراء العراقي "علي الزيدي":
سنعالج ملف الفصائل المسلحة بطريقة حكيمة ومقاربة عراقية تضمن منع إراقة الدماء.
‏أميركا شريك استراتيجي والعراق يقرر علاقاته وفق مصالحه الوطنية.
‏العراق سيقيّم احتياجاته الأمنية بعد انتهاء مهمة التحالف الدولي.‏
العراق سيحدد ما إذا كان سيعقد اتفاقيات أو مذكرات تفاهم مع أميركا أو غيرها.‏
سنعالج الملفات الأمنية العالقة مع تركيا وإيران وفي مقدمتها "حزب العمال وسنجار".</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/80929" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
جانب أخر من التشييع الرمزي لقائد الثورة الإسلامية، في نيجيريا.</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/80928" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN7WwXkL9S_QxFA3fWrC8UWzJBoK8e1LMlqbfjC4Yh9zwKvIA5EIJ2CFxi2GEMsZDzfBm4LWYzzojYrr6E9YiXOGWJldiwxIB-GsIfO4skv-7czjf0tsHCpgQgQ_gdu9u6mphqShiTFeIIkMeh2CIX8-lCqWy-9qES75WFlnWJkI4XjihhfXck9RAeLL9u2cYFJ4vVbMvx3TySUENX4_RnP8b_TwgUB04SCb19lG86CLcMc1GGt1_xMo94gbKQmJQEuP1HBpXMY4TQaca96OvTqyksjFZ__9jeVv7ySNA_UcXcqFr5bMtTXzjrJxrr5U4w1gbxbT4W5AsAsePncAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxdYW80rybzMVadlHErks1HPsDro8pRS278QzZMcsT4VLGnhPkEWOS-mwibGQUsXfWP9_Fcu_bLfUX56PAqdFKOnkQGWleN9PdKcdPoyOekJCE56omyEmPzfRYoxIr4Qb-eg6X8gs-XhQkSF4u94wg8BGSOscPxVMejlJG2d0R6jU3B3X3XvydUhwKaaFERSzpXfygieJnOvR1OIHOHIB4_oQxe4YvY_cuGkgKb717n8uZO-DymTHB0AutkTq8sWtEbOOZBxwoZFGup-FEPoakeh5x4Ga8Ag5X22XObtf_gEloQTgTcdrAWnNta_TlZzLEAAJ0n4jNFuQVUfL9IEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zvd2Z7LFug3xtDMEBWtMPUHuG8DOcEZWbVSyUBSIM9HjUl1rWa_408WoseO6inpuRLdTmhwZ4CuVVBxA9DgALwaxfJtTLDgfwC1kiQR2EJMaLNUcKmMvukNcYlhZdNBJOS2wYnf3A-W8BcKGVOc5gF9EQTj1jd8_GgwFZS1Qdyv0888pCdw691jnmgqzhCbXO_cIQR9VSzdXT2P5TJdsNs4ogSPxrr-hFLbQmcn5psFFegpkAV3_6-udTNHDIUdS7peK02bwe3EaMC6RVpl3OJFRD7uWj3S3kx23BJHdgQ6plUEqTuYjAgr_xyMN8WqzZ205DSMWgP05FzuDezD7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg2RaBPfs61eyI2d3wb-S36ZsQxHoWfxPhYwAs1d7vD4iqwezeVYck2w6ulvdg4mTEKVmm24mVe39zJo98tZRsKXl7e5zI36zZIA-pVAnLkD6-5nAiP31QxvbLZOzVFH0xqb6nqSdOJuuYQqrP1A8vP-7mmunu4dNZ7P-WCuC4NAEi2qgnPojlND-UrTy98vxI3q_kqD6sQp2-uBECznbbZa7yY9tzgC-nup77K63FLaMI0IuSwEsotyOJpoSXgz4Sjv3qoA8BHVLcGNqQv5_lPjQ5jtX6qE-dZRu0NZtywwI6TlzjLZLakb7QymWWRyu6cso9GGFHQKyQCRj14H4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على طريقة خدمة زوار الإمام الحسين.. المواكب الحسينية تقدم الخدمات للمشاركين في مراسيم توديع قائد الثورة الإسلامية بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/80923" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsEQPDQM0ntULBupv9Pe2Wvdf9KkqFeRkZFrpuEdYn0l1t0cAPdTh1ES2j3iiS9mmU080KSl4m9qMLC2fN3qJvjCBp9zJ_kY13Dm_7nIcgl1i1IyF45p1wGWrromfkRkOXGWwjVvkLaFqR9M805TOOfFqrQuZDN289U7L26YxL6S8k7mBj_8CuiTDSHVaPovlPngiTPX9w3_a-KC8VD77aN_5qdjnwFgL7LK4do3akk38dhHT73vUP8-HciYvpMvJIIlvjzrGBoLyDoKvxr9WTnAFS1798bZed3W-RrCkkQdrOls5JHAn5S1Ym586FUtqN4fMx7BGM0_TSY5k595zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إرهابيي ماتسمى "وحدات حماية شرق كردستان" الإنفصالية تعلن عن هوية عناصرها الذين تم قتلهم على أيدي القوات الأمنية الإيرانية في مدينة مهاباد بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/80922" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/80921" target="_blank">📅 11:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
غدا الساعة 6 صباحاً بتوقيت طهران ستقام صلاة الجنازة على جثمان الشهيد المجاهد الإمام الخامنئي والشهداء من عائلته في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/80920" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyFq6G7B7WUn0gecCivWeceM1t_9aL3iyH2-ubBQhFqwZ2ysIcuXh8Co5ZRoWaeGJ_swEst2ewr3qCAl69G80jLAwRR-1AKf62nK6w1KFMdXedBqJxtHuEcyCKvSsWO79aGuQipI0tkRWdnq-a5qxu3O2uZml-GcIQd52grNvr7070-MVvnPlSjD1-yzAMiBA8cRnJpldWMB9WSKJx9TxD97OQtTWang_j9klHF1UyIhP3GB9m3R3LSaRZDsw4P4iZ2Q48U4CPbKX8QMmjz5PwUFXVJAUuefLUJt_FyUUapQacUw8UbN8j9SKW5D3KADx3sBlVTkhIaOivfyW5o_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لازالت الجموع الغفيرة تتدفق نحو مصلى الإمام الخميني في العاصمة الإيرانية طهران للمشاركة في توديع جثمان قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/80919" target="_blank">📅 10:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fb197939.mp4?token=WKUvJBa75C6tSYxETPreeiFnUxYWs8xa393GUdyblvl2C4YGYEWcoz-x9Io5Md8U_fl8CEKbqhaHclDCKSS62SCyyCxGsg5tcgvnjh34bHcIpS-sdxsjKY3Mq5WkJFzpgU3_RiYzZO_39APZ-Mbos3_N2agHTz_OM76rHTSlQhagx6KGAJ7KqpCTGgyoG6KriGC0RhI3h8kirOBh80SwZ2eZQu9G7JargU0GewQIUvI9J-cwC6wGpQVcexAihQk9x9AofqJDSWQ48J7cJ0qPauj0ryjiqvqO5rQoDJ-yFqy2Mqy46vpF62lFPn-ZrDtlfUHMRpBldv7N_5n88LAlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fb197939.mp4?token=WKUvJBa75C6tSYxETPreeiFnUxYWs8xa393GUdyblvl2C4YGYEWcoz-x9Io5Md8U_fl8CEKbqhaHclDCKSS62SCyyCxGsg5tcgvnjh34bHcIpS-sdxsjKY3Mq5WkJFzpgU3_RiYzZO_39APZ-Mbos3_N2agHTz_OM76rHTSlQhagx6KGAJ7KqpCTGgyoG6KriGC0RhI3h8kirOBh80SwZ2eZQu9G7JargU0GewQIUvI9J-cwC6wGpQVcexAihQk9x9AofqJDSWQ48J7cJ0qPauj0ryjiqvqO5rQoDJ-yFqy2Mqy46vpF62lFPn-ZrDtlfUHMRpBldv7N_5n88LAlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/80918" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=OEgCk-GtSLro1Ilp9LEujEU3kiAN3Y6brOf0GEwKYPNVjIs0ED927I9L-V-GWMroV74nOBojiDLrVBTUOq_HDlXpCkGo4i1DlC42kjTlM8GeofLS3dW1yFPFYTVh_ZcbBFEWMwnyjnDMqrYiAzMXsoNnnBI1a_T3hRcOwqKCaXAM8SFPuUA7PuvGIvsL9v2yqSGsSf9NWyeBj0Vokm2HMrtfmn-QbzrJCPMDeqgMdzKFi5mqU2xLw3c75aA19nJD02oWG9ivUtQuqz6Cz5wf9V1sE9mylu1OR8PuXZL8LwKJUYdfJvNPbcOZ2ZlEjIrrUPtVdptj5rIIRrSUBKln30UM8AH9x0JOXQCg9NgihwgGYI949wglvL6T0Y0FWcuqI7FN7oTI7Og2aLAtjiEF8846O3IJl1lzmGNoaaQEucOV-368p1Xe3FKEk4eRQwumDVqXSKpgOwM290p0EMUG63kwevTs5eIzF-bv4UlxiYPx1aUYAouHw6fQRB13ykYTU53pVrpBWxxd0LjLfPrt1YBDlbprBWSc0bt1kmyvGs1oOKFnxh9D_DvSfUg3g2UUzc5x_QCN0qJK0g-FdTNLhNJvUgmjIYFD1BgLV-uWgsveylfcLMF-wjXZMFqLRXjQMKFPjQcNRiX-Hrr_xKDy9rjb-h7bY0cSKpnS0vTCAm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=OEgCk-GtSLro1Ilp9LEujEU3kiAN3Y6brOf0GEwKYPNVjIs0ED927I9L-V-GWMroV74nOBojiDLrVBTUOq_HDlXpCkGo4i1DlC42kjTlM8GeofLS3dW1yFPFYTVh_ZcbBFEWMwnyjnDMqrYiAzMXsoNnnBI1a_T3hRcOwqKCaXAM8SFPuUA7PuvGIvsL9v2yqSGsSf9NWyeBj0Vokm2HMrtfmn-QbzrJCPMDeqgMdzKFi5mqU2xLw3c75aA19nJD02oWG9ivUtQuqz6Cz5wf9V1sE9mylu1OR8PuXZL8LwKJUYdfJvNPbcOZ2ZlEjIrrUPtVdptj5rIIRrSUBKln30UM8AH9x0JOXQCg9NgihwgGYI949wglvL6T0Y0FWcuqI7FN7oTI7Og2aLAtjiEF8846O3IJl1lzmGNoaaQEucOV-368p1Xe3FKEk4eRQwumDVqXSKpgOwM290p0EMUG63kwevTs5eIzF-bv4UlxiYPx1aUYAouHw6fQRB13ykYTU53pVrpBWxxd0LjLfPrt1YBDlbprBWSc0bt1kmyvGs1oOKFnxh9D_DvSfUg3g2UUzc5x_QCN0qJK0g-FdTNLhNJvUgmjIYFD1BgLV-uWgsveylfcLMF-wjXZMFqLRXjQMKFPjQcNRiX-Hrr_xKDy9rjb-h7bY0cSKpnS0vTCAm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/80917" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiLQUP1muG187dvg3YMz2ePkqPw3shGtqQU4FRvWU4p_eu4iBGiBK5vRQU5RAArOT_xc7XFJo6Yfc2tp3ak9DhDDtnOxKme0sgmijWqsLWeYy5a0crQtGr69apwsGvEyjxNAZw2Ao1wQfuKRVfjp4GmR0DIzz2iSIW4SR9dPJ2zMdt4R-ysPt0pbTFWpZ_EqhG_W7YfhOja6XR8yq46K0n6SdCxp1rjmeAo-DQh-HvHEke5uhUdPB2GLW20b2B6f9ZOyAH5xpwGjjEOp7iOY51lqRljfUnDvOe76nuGD1mEMie_Ngzwr_XEMHcvBxbZropcBNa62BJ8Bb8RRnHIn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpykl1F58E5cVLtPNDLLerwMuJGF-NRiCt-6Sn9W_J0nX-XCgkVu6ZGxYpF2xpHob_dBVSGmihI1TJUXIGZhsnAr97mCcqslLKDnIu-fGPGDp6XkXa2NXDFhB4nCpZ6hzTy02hpObMFUQQ2vGh_ldBw34c33bqtn9AqNHsDxtolJMXjaiMdlst3ZmzyXGv0UTaS39t3dxjr2_CxITn8ddnKbbvnRdGfWlcD6Iu9arEGJAl6MPODVBiovxBe2Hv7y99R57RtHcqXN3WcTBxMn896U1WvO3RN2hiyPEq5no5wZSexaq2Ak-zKoyMddcZb8EP5VubcCvUPlR7IxVMjabQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/80915" target="_blank">📅 09:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t80QycNRPq2qPMYmAqH0UfEKmA_jDpEwmTaMpU-dkuEKuvivxJ8ldHMlIytEr2krm9tOvtIzj4VpO8Pmbz-q1JomMdIAPADXHQqXtMaW1nA-A2XwxWd194NANav9mI0RflLLqBOptkFyJD4WsSLthwd-pxFD696N2yAXqe5-ofHPU7q6F01V9HY3VAWW8oQdWu2F7uY7CWh9fHu0NHrCeHle55X832DmPmUy8tsQxftDOjH7o6NaqL5pmw5YXyijNmcLyX-RQoigwkVqC39wxQdAo6yF8W2IDVfjShN6KUjXe_KtGu_FfE38BZGMAcQStOA1wb41isJ_Zbva7NTMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdIayw_10LlEwQGCUAZ1DpeXTms4whMnWpz8C7I2lw6HfaHXA82yF1pQdIrH6tuAyxHzRsWKH0lIK5CNO6SDhNhkUx8EGe3pEdzgUB5SjBOCbtbGdQ11Zf9PE_F1f9VJLkWdnF3K2iPnr38V_ZjQ17C0itk8SWmulfbC-7WhaG0m_T1qBAyYPks1rRo27PuZQ7rPNu6QRGj-c2-AMl7eAkFv00lGHa-HyUsBGE8sRXh4IhMEmhqqRxnvCGDI6GV8mSLYLDdIElRPFkvnILAgshrahGimTyfFn2ObeqXXOywB6kKMJyHmcuOWrxa3uENXIWahpU29YsRPp1h74EnudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-bgW-LDqJx9rlAAiGoVSHiEvWwNXS5S4yMC38e5jfPKQy6X_W2z2Rwvbzw5R8aU8_wd6Rwd5XWCbpNGu-4YIg3TYZSS3EQS3XKxT5IT8s90k4SIurgvy3nitxm-dEWImCjk4ssIlZdP6X5sqMuF_5QpcPJZ_g4e134a4J0uA81kjGvDieePGsa2xN3FB7DB7Qo3hmlxW3pHVbchvUAHzk1pdep1-TjJLt2BSGYKQxgZDvkiEkrvE_D3Of6Oj1KlOH_b64ge1rCvB1vOtZj8x5Sl-_VkBq1WV2wLz9ikjg6VQg_HPNkWBIMVy8C0BftLjdTgNnMUXxRyBq3_AS1tYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIykLzyx-TW3o0DeVE10FBw2eLU0t2wE8i_W5eM-hGPrJ2d9f10n5sMVAvA6KcPFLwKR2xM0cxlg0STp52X9mhQX8v5nygNjDS0R3uL-QUrKr7hcrDB1FcE4ssoq7NtFDiyPqaz_KYe573UmS5qF3QjwILFy0sSt8NlunEJWSkzxP1P8FLy_yGpel6hbqfLOTRiUS0gFEm1r-8aWWni4QLdeLpwBSkPrWvuR9RReRotRHwysRDsXTngDZCjkVm2Y7IC4bF1eTBj89OnrhSwZ_oWAo79PZydB1T8d290NJlupkQO3st1-bdYnPOzHjllANo58nHDesY2cZSTFfYCL2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">أقيم في نيجيريا مراسم رمزية لتشييع جثمان قائد الثورة الإسلامية الإمام الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/80911" target="_blank">📅 08:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=UWokhg4aY7CS6r-oJQOeaOh4Y3xa2OugjgqL7ZYqsnKncinXblNdReJ3TYqpfj93NNOqTys_mipVVrop7ID8tKb9fRPkOvj1340Di7uaDwK5lmdaU2z5-wc6FA-cxw7y3x2RjmKC1L0YDa9llCducdikoHJER5RfMd8c_P5t1d8iHAxO52OK5TCe-dy-Tsezs_J1-Gi5vNhyhnya1pFskuFoKNZcfl0z3wMaMGy2YheXkqRz60nT91zHH1o8ViBrgmLy3GsVSmrnewSoiXq0Cw2wwlAZTgQr_quTIU1kyZUZ2Oz1Z0DQC--59pTXWll3Hvlxgdjxo6g66MPeUo0vBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=UWokhg4aY7CS6r-oJQOeaOh4Y3xa2OugjgqL7ZYqsnKncinXblNdReJ3TYqpfj93NNOqTys_mipVVrop7ID8tKb9fRPkOvj1340Di7uaDwK5lmdaU2z5-wc6FA-cxw7y3x2RjmKC1L0YDa9llCducdikoHJER5RfMd8c_P5t1d8iHAxO52OK5TCe-dy-Tsezs_J1-Gi5vNhyhnya1pFskuFoKNZcfl0z3wMaMGy2YheXkqRz60nT91zHH1o8ViBrgmLy3GsVSmrnewSoiXq0Cw2wwlAZTgQr_quTIU1kyZUZ2Oz1Z0DQC--59pTXWll3Hvlxgdjxo6g66MPeUo0vBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود الغاضبة في مصلى الإمام الخميني تطالب بالإقتصاص من الرئيس الأمريكي المجرم ترامب.</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/80910" target="_blank">📅 08:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnlwgjbaRWjZwx8JEwo8kiAym6ty-VkGlrXT2ShOEMIq-8FizxHEliJGrYJbaN_CE9oiegyNq99OE7WJNCwKUCH5e2sO-hq0axuY6HMLElCQQ95x8yor3WINdENkqheNPCUbxx4kA5kmNeRTGHJPUZtn5kqVAAv7IzyASqQi9i2UNWybo6pWEBGdZn0_wjCQGZp8QEBhCUlE3vouXepJgIerw4wKslRDAoFq1CoGZmJQgMt_jhUlW0NY_MVjoUZIhIv9M-7Ui9SEPp_6K8mEfzou_0qObs58eL9IE-fkxw9p3Dw8F40FmnWGV5quNDtvf-z95yXqnZM8BcRB0hdPPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/80909" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=a4IJBZz5sSv-jJLtyzR0qP622m56H2J5L3YGGg5wNAJ2R7o0sL8pSpFR-_q-Bq_xfCaPXuVphzDtSAjEUPF37Kvr_PVI8HlaH6hLHDMHCjoFVnpeEsdrD3krhA84qbXdCIva5txpN0_O80s8dOjejPd62WUrS24SciXAVw-p0TdK_NG0u1GpV47oCVQ8szM1GlLJjUbnlYyD3iPCkn3D7hFMXuzl5z0cd34zzFSxesEA3l5PGjurCXw3Ed8YgpepdfoS-wJN3yDIIZfUhfVzp1lsXKTQaTw-mqRSqHcswqrg13rzXCx8kbkZVqtCDznzhRZSYLc5A3O4tkZyKBoLa0j3AppL35u4BS0zzCTNqRwJoCyddVuHdk-epS2utBX8bHJkKVTLPIwPiXKh59WqROwpgyVy-kOJ83JxKh6W4eIgOHVAiVYaA0fWr6lvGZgpjF3D6VBnm2PY5KVP2yeaZiL6QAGaZhD8wbv3bJkhwsW0dS7uVTLY6NGckwYKImrHD7waaCImORCRgvskt5nnlYQ-iIYbqlxnuXFEnBAsUD_xdLcK1jiOE8vF-1qbQCBpcPRdFfk7RU6PhdWBl74S0jczx6iKFLHjCsisPwqwyIvZH3Rp6ok8EKhSRuBk76xs16FEjqBea6ozfHzJrq12QTzrDOlENJm-f5VoYeVQu_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=a4IJBZz5sSv-jJLtyzR0qP622m56H2J5L3YGGg5wNAJ2R7o0sL8pSpFR-_q-Bq_xfCaPXuVphzDtSAjEUPF37Kvr_PVI8HlaH6hLHDMHCjoFVnpeEsdrD3krhA84qbXdCIva5txpN0_O80s8dOjejPd62WUrS24SciXAVw-p0TdK_NG0u1GpV47oCVQ8szM1GlLJjUbnlYyD3iPCkn3D7hFMXuzl5z0cd34zzFSxesEA3l5PGjurCXw3Ed8YgpepdfoS-wJN3yDIIZfUhfVzp1lsXKTQaTw-mqRSqHcswqrg13rzXCx8kbkZVqtCDznzhRZSYLc5A3O4tkZyKBoLa0j3AppL35u4BS0zzCTNqRwJoCyddVuHdk-epS2utBX8bHJkKVTLPIwPiXKh59WqROwpgyVy-kOJ83JxKh6W4eIgOHVAiVYaA0fWr6lvGZgpjF3D6VBnm2PY5KVP2yeaZiL6QAGaZhD8wbv3bJkhwsW0dS7uVTLY6NGckwYKImrHD7waaCImORCRgvskt5nnlYQ-iIYbqlxnuXFEnBAsUD_xdLcK1jiOE8vF-1qbQCBpcPRdFfk7RU6PhdWBl74S0jczx6iKFLHjCsisPwqwyIvZH3Rp6ok8EKhSRuBk76xs16FEjqBea6ozfHzJrq12QTzrDOlENJm-f5VoYeVQu_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/80908" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=rgitaro6B3gu33nwpK23Oag47OUb5WALKTiwq5PPlP80Bf4CZHM9g-jZPgNcWKN0X1j6YtCT9eJ3YTApZx5ssLS5fliuIlZ8sVFaY0NbUKJ4tEZR2q0ldFPiUkrT31kiG_55aq4_jfTohycU9YxAXJBsLKRkPF2-Gf0yQSNc953oV-r7BuZpr8Tcm91sUoKO9rfnDHgVqpKggNJN_MZX0otQvSVD8uNkBnorxPzyVZiUGwThEko_CVFr46y7VXxOE7Y8JCnqqa8lpu17sSRaA8-9HFv_XTdDC-tH3R3j_ctnasoKt90O06BVpiT87Xs4Qv_OdF0z0Q96FVPpo0Ff0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=rgitaro6B3gu33nwpK23Oag47OUb5WALKTiwq5PPlP80Bf4CZHM9g-jZPgNcWKN0X1j6YtCT9eJ3YTApZx5ssLS5fliuIlZ8sVFaY0NbUKJ4tEZR2q0ldFPiUkrT31kiG_55aq4_jfTohycU9YxAXJBsLKRkPF2-Gf0yQSNc953oV-r7BuZpr8Tcm91sUoKO9rfnDHgVqpKggNJN_MZX0otQvSVD8uNkBnorxPzyVZiUGwThEko_CVFr46y7VXxOE7Y8JCnqqa8lpu17sSRaA8-9HFv_XTdDC-tH3R3j_ctnasoKt90O06BVpiT87Xs4Qv_OdF0z0Q96FVPpo0Ff0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجواء حزينة تخيم على مصلى الإمام الخميني خلال توديع جثمان الإمام الخامنئي الشهيد.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/80907" target="_blank">📅 07:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=l9cTqyqiZrGZ9EdkSBClvetv_TSE_NtdLufFZYq5qjwaSbk4WZlUdKscFa_j8jkXiVxCmxya61rLfupADBapfN70lJZMkVMX_nyJ4d9x6vW1hAcJASkohxDgfuA_V5AQexZnFc44CsdlMUnE7j711iZY9Wa4x7pOnmAbtKZWPswAgYu7juBx7ktAXNntcQ5p70cXH5rpuWgSNaFAyFd5Rs0T8UsoSrH37d-DQOGeiok5WgLtZEWHWOvvWgvdS1nARnbfjlKXJfx7RXyg-SfuIeLOwIhoWIbALsoUaWe5oqEUZxuFpqf4V9kliQuSZFmk5fjnuKWVgVp9F6SSdB1Dfr-9JLKOHsKQLSnfqOpImbgODWJl7jHWo4-B2ilYeDC9tLQr1tLlRYat9738S9YVIht2ck9v0maTGdK4tyakxivZXVhg6ycYaCSUneF2N1LH3YpxCdK0NukvNdWz-UiIMA-SHZk8m6EwPiaFmhkVuT2VG0u2skizewyX7HnD-aIT35Xn0moYDBwg55KqE7uWWd6qq1tKWUCo_O9nX6Lfe7m2co58NA4w_t3f3onSwVr4J4fQmfZE-wZicypFOqHkU0JAfEaLIjoEcQc4ogvQ0G1rHhKj7JI77zRbbkNKzGwd5ORgepReJTNiQs_3ZO-cFryFxRIIqsIzZ3aSbiAX9W0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=l9cTqyqiZrGZ9EdkSBClvetv_TSE_NtdLufFZYq5qjwaSbk4WZlUdKscFa_j8jkXiVxCmxya61rLfupADBapfN70lJZMkVMX_nyJ4d9x6vW1hAcJASkohxDgfuA_V5AQexZnFc44CsdlMUnE7j711iZY9Wa4x7pOnmAbtKZWPswAgYu7juBx7ktAXNntcQ5p70cXH5rpuWgSNaFAyFd5Rs0T8UsoSrH37d-DQOGeiok5WgLtZEWHWOvvWgvdS1nARnbfjlKXJfx7RXyg-SfuIeLOwIhoWIbALsoUaWe5oqEUZxuFpqf4V9kliQuSZFmk5fjnuKWVgVp9F6SSdB1Dfr-9JLKOHsKQLSnfqOpImbgODWJl7jHWo4-B2ilYeDC9tLQr1tLlRYat9738S9YVIht2ck9v0maTGdK4tyakxivZXVhg6ycYaCSUneF2N1LH3YpxCdK0NukvNdWz-UiIMA-SHZk8m6EwPiaFmhkVuT2VG0u2skizewyX7HnD-aIT35Xn0moYDBwg55KqE7uWWd6qq1tKWUCo_O9nX6Lfe7m2co58NA4w_t3f3onSwVr4J4fQmfZE-wZicypFOqHkU0JAfEaLIjoEcQc4ogvQ0G1rHhKj7JI77zRbbkNKzGwd5ORgepReJTNiQs_3ZO-cFryFxRIIqsIzZ3aSbiAX9W0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء مراسم وداع الجماهير بوضع نعش القائد الشهيد السيد علي الخامنئي وأفراد أسرته على منصة الوداع في مصلى الإمام الخميني بطهران.</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/80906" target="_blank">📅 07:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=UnYVicFF7jfEetpwZOpa5k6eq3bHgXGzxBB72ZC2iptiW4Bpbhogp1D4P3wrsNeQ-7N8B3v-WzL3KtRNQh0G5KNk26tukNaRMQd3_4SeyJC93mNHBIUyv3nGmXAdzatYVtuYFTDRzFJwmmimpsbAET-0-OvFe2-HSm5ztGnX3kItDDTUN_gZeTwMd8Qh1Z_LSoSkmxz8QWrZ10rbC9y-T4jN3m7gkhvT3MagzgRGAW5K1tG3T5dF9goVLOVAnn71_FaB_wBcHWTY3X8IdOXOl_l-IiRr5Yo-iTbKkpZuMGTDVHocwkBP0a0SxGCJ4PaFqNtu6iSKK11mEdac358k8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=UnYVicFF7jfEetpwZOpa5k6eq3bHgXGzxBB72ZC2iptiW4Bpbhogp1D4P3wrsNeQ-7N8B3v-WzL3KtRNQh0G5KNk26tukNaRMQd3_4SeyJC93mNHBIUyv3nGmXAdzatYVtuYFTDRzFJwmmimpsbAET-0-OvFe2-HSm5ztGnX3kItDDTUN_gZeTwMd8Qh1Z_LSoSkmxz8QWrZ10rbC9y-T4jN3m7gkhvT3MagzgRGAW5K1tG3T5dF9goVLOVAnn71_FaB_wBcHWTY3X8IdOXOl_l-IiRr5Yo-iTbKkpZuMGTDVHocwkBP0a0SxGCJ4PaFqNtu6iSKK11mEdac358k8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ای پسر فاطمه منتظر تو هستیم.. مصلى الإمام الخميني في العاصمة طهران يعج بالحشود المعزية.</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/80905" target="_blank">📅 07:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=K7U9RPoCO6s0RyO1PklTrNFqunPcUIf-xAwP5EMs5dVXTV60fwh8ZeaTVOfl1u8QAJ2dAdkX6sxiJlQEACsFHCWch2SY1T4L7w1BnTIwUQ4tHOdEA4aDLNy5qg_5UyOcLUyXbZuBOue1zfi8y6brZqESFPctjuY5uSD_2AaJLTr1GtmUdBBzKUIJkXO6pmc3wanZ97brBB143OPDBnbIVZWQa69Pr9fFcnCzYQdWDS1s48KK3ws75U3oP2skj8O4KA3l9DNbflvMdJI4YDIm_v6yRy1QXErJeqKUGb_UVA-upBBRoWKcBAnaxG1LVQQ5MKG95y1EBYoqE9Z9R7Tvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=K7U9RPoCO6s0RyO1PklTrNFqunPcUIf-xAwP5EMs5dVXTV60fwh8ZeaTVOfl1u8QAJ2dAdkX6sxiJlQEACsFHCWch2SY1T4L7w1BnTIwUQ4tHOdEA4aDLNy5qg_5UyOcLUyXbZuBOue1zfi8y6brZqESFPctjuY5uSD_2AaJLTr1GtmUdBBzKUIJkXO6pmc3wanZ97brBB143OPDBnbIVZWQa69Pr9fFcnCzYQdWDS1s48KK3ws75U3oP2skj8O4KA3l9DNbflvMdJI4YDIm_v6yRy1QXErJeqKUGb_UVA-upBBRoWKcBAnaxG1LVQQ5MKG95y1EBYoqE9Z9R7Tvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عَزف النشيد الوطني للجمهورية الإسلامية الإيرانية في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/80904" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=U6dNFO7gnM2q0_VeZvB07ncMnGrDtbpBeoWIyMLPdqp-QnVK3a_ehiwTS7tfkvikCBE88e_T5jGgzat3XtvrnQhO4F1b1KonTbB287Tv9hdJSCXsppLhWQU_mTIMVH_5jOVycxGHtDsGZuOVFfdg4zwlEpTtPIPSJtq0CqJqvD7ctxWnvBoXDKMFT6zeBqjhvKr10gKUyHI2QrZluywS2AIuvHK6AGxiVq7HeazZ92MarYhJLuV8B7gM_h0iw2Sq0e86-qtjCpfkOJjHJlBM3Iq5XDKcdX5XiSYklLnvqsOu56IOiV8HOwX7cgVrlwOQTg7wK5tEjtZ6qqfwM_tH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=U6dNFO7gnM2q0_VeZvB07ncMnGrDtbpBeoWIyMLPdqp-QnVK3a_ehiwTS7tfkvikCBE88e_T5jGgzat3XtvrnQhO4F1b1KonTbB287Tv9hdJSCXsppLhWQU_mTIMVH_5jOVycxGHtDsGZuOVFfdg4zwlEpTtPIPSJtq0CqJqvD7ctxWnvBoXDKMFT6zeBqjhvKr10gKUyHI2QrZluywS2AIuvHK6AGxiVq7HeazZ92MarYhJLuV8B7gM_h0iw2Sq0e86-qtjCpfkOJjHJlBM3Iq5XDKcdX5XiSYklLnvqsOu56IOiV8HOwX7cgVrlwOQTg7wK5tEjtZ6qqfwM_tH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/80903" target="_blank">📅 07:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boF62TQEm9yeTNbRskKe7py7iLza2BxWM99PZ1jAyVAVh4IDh1zhliJRasCowh1mM0JQJ0M87hkj8BXo-n4Mq-gsmECVhE1VQwJEcoZxWiIhABLNIvW31UpozBGa1u748S6E87deY9bx8gso-5MgaVnu5RyCp16m7qO7q5YI3q4OkV6rGXvgfuysZDjEDaCCWhuNuEPMrwZA089QbwgoXg4QzvFXPCTWfJWfy2XsJ4xRyC_imQcfs35nCJUPSclz6sTVQvcEW2X-1AfNsjy9jKeGf0mcT5Ik5MlpBxSzIhK2ol-E6yaJ20UBNKoXJIni_YURrkre-ClDZJCypBMljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/80902" target="_blank">📅 07:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZany8LEpf-RR50A9SkFhtID23f066sEYpC5VZ3jVk4DkZb5sQN0IX1YJFovXRABZcosNj6MgtlXKiYjX-DQrEdOO-kiufVwbEbCtDnGMQg8munhfKK-_wm70_uGGEJBhK1EyQxqdD0yYGdFXPvmMfoIgAObfJroIImXkiHyeSF77tmpfy_yEkYa4bf3SbNYRW50J91CD7Emz9dy8vQnJbOSBetRlqx9aNkIHcuZWiE91v6nwXIOCWHGzltw83pEWZ9kPQX1PCVdyytixwYBzykKqU1YXPbL7nHlh-gYD_QY7tF6Ncu9WF37eECloRWAplM3UQfqFePEVpHtrZ1uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرچم سرخ انتقام.. راية "يالثارات الحسين" ترفع على قبة مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/80901" target="_blank">📅 07:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_af2Y7B7vsD7JUZciMZVxzA6D7fT4S74zRb-CaJxdOn7b7EsqjZdHhGJDBJACcDNFfru79lwwIv4N4XMnBGBDmVojylfkAuHk9lySqwq8C-vqwcg6BCEmzp3eb9fNIBapXpaZJDigmy9wGv3rdBMFA-hixkjRcm_Q3USZhkkVLRaoHeLXO985QMO0abh8zMn-bnCmLZmETImz1nZ9zUEVXh6ojhJHSK4B3KJ1tpLg22MYbkfe_dbqe3RNcD6ukcyeaNWH_O_7uSw9Hhnhp48M56UJ0gW5PEkJL4KwC06w9YPqldMbYSO92xKb-gES7JFo8-ygNaLwNwZNvn-l--3Apo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_af2Y7B7vsD7JUZciMZVxzA6D7fT4S74zRb-CaJxdOn7b7EsqjZdHhGJDBJACcDNFfru79lwwIv4N4XMnBGBDmVojylfkAuHk9lySqwq8C-vqwcg6BCEmzp3eb9fNIBapXpaZJDigmy9wGv3rdBMFA-hixkjRcm_Q3USZhkkVLRaoHeLXO985QMO0abh8zMn-bnCmLZmETImz1nZ9zUEVXh6ojhJHSK4B3KJ1tpLg22MYbkfe_dbqe3RNcD6ukcyeaNWH_O_7uSw9Hhnhp48M56UJ0gW5PEkJL4KwC06w9YPqldMbYSO92xKb-gES7JFo8-ygNaLwNwZNvn-l--3Apo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
المجرم ترامب:
منحنا إيران مهلة أسبوع لوقف العمليات لإقامة مراسم جنازة من منطلق لطفنا.</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/80900" target="_blank">📅 07:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=hxRzcHx0ZGHRb1pwuV2JlXb3_l7U7CjGEbbTQtd4n7EbnxnjPg1smkpYIuecUt-Z6x38ap_tZFJopz7bTd6PIUChS_lQ-x9KW2f1jeVd2umY7Q1QNYXxLixv1GPQ7esgcRcFwiind9wfOiN2hyFNuyf6a3okyuAy-caTFsOYQAsjje2-muRVEm3ULmsHAQFGkX94sj9_J53eaFwlDphf-6UjIed_IMV9KfDstfsXUndIPl1gOUyFv9X6dJ1MKSInKlFTckfEHGDopKm5jevH5REgBswd82iLELNiZyfPkNIcmGXBLjPFm0FUWG_B2jQrwXBAGFJlfMNGiZVtNBRRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=hxRzcHx0ZGHRb1pwuV2JlXb3_l7U7CjGEbbTQtd4n7EbnxnjPg1smkpYIuecUt-Z6x38ap_tZFJopz7bTd6PIUChS_lQ-x9KW2f1jeVd2umY7Q1QNYXxLixv1GPQ7esgcRcFwiind9wfOiN2hyFNuyf6a3okyuAy-caTFsOYQAsjje2-muRVEm3ULmsHAQFGkX94sj9_J53eaFwlDphf-6UjIed_IMV9KfDstfsXUndIPl1gOUyFv9X6dJ1MKSInKlFTckfEHGDopKm5jevH5REgBswd82iLELNiZyfPkNIcmGXBLjPFm0FUWG_B2jQrwXBAGFJlfMNGiZVtNBRRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/80899" target="_blank">📅 06:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350b75f432.mp4?token=OYa7wj5gLBWOcSiQZ8tgd8v1q6Y8uXKU-Ij9CJ83qyGeyWZuYGxPlYWEsbDHfKW70EpHVtu6vEeuMwg9nJUcBSKw2DX5H_SncPLqyTILvHdoUpBrFnWZW3V0H4KlPcIxiRIgYtDvTar-TJGacp1nQY0PKqvmk82ucBfizPSLWuh4zUEbsNE-tqEvgipHuojjwNrQmj4VBHIumDmhyV4BRad-6t0TZU1XhcEsOon5Tr7Dq0fu3GLM3NWDD28pTasfxitM0dpmDsOyc7yq--o_D0TyLvJKeMz9jayJA1GOHm1Ev-UJcPhhf9LZmfUEaveR4lk0uYEgcqZufceeOnAMlaECKgaPS0fT8Rf6qN4OlLgd8cSmLFCknJJFMngrGEJb8iCUTAcFgBCmsmnqsBFfI6_uJaCOix_zXfnN0NCNlr-KAs9RqvZnKRG8m7fBESi6aH7ohGu3AeC4CRSHrNHAJfXeJmsJsnIRtnnDhOK4zgEa6PcJnGiQ40T-OQqfScC3_10M4BNncMFF5inXDG6g6Za3bDMLJFKezYeZRG7aqoSWz04NW_ZxiEStAt9EZt3wOqCPkLpW9DCcW1tR5LGESD1i2SfbFfa9QX8vtTFuqctfPvNJwqmDBBpSl7y9N5v4CVsJp1Xg9_B2UeJmYxhZ1gBcILiNksXIhAoDZ_2xKNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350b75f432.mp4?token=OYa7wj5gLBWOcSiQZ8tgd8v1q6Y8uXKU-Ij9CJ83qyGeyWZuYGxPlYWEsbDHfKW70EpHVtu6vEeuMwg9nJUcBSKw2DX5H_SncPLqyTILvHdoUpBrFnWZW3V0H4KlPcIxiRIgYtDvTar-TJGacp1nQY0PKqvmk82ucBfizPSLWuh4zUEbsNE-tqEvgipHuojjwNrQmj4VBHIumDmhyV4BRad-6t0TZU1XhcEsOon5Tr7Dq0fu3GLM3NWDD28pTasfxitM0dpmDsOyc7yq--o_D0TyLvJKeMz9jayJA1GOHm1Ev-UJcPhhf9LZmfUEaveR4lk0uYEgcqZufceeOnAMlaECKgaPS0fT8Rf6qN4OlLgd8cSmLFCknJJFMngrGEJb8iCUTAcFgBCmsmnqsBFfI6_uJaCOix_zXfnN0NCNlr-KAs9RqvZnKRG8m7fBESi6aH7ohGu3AeC4CRSHrNHAJfXeJmsJsnIRtnnDhOK4zgEa6PcJnGiQ40T-OQqfScC3_10M4BNncMFF5inXDG6g6Za3bDMLJFKezYeZRG7aqoSWz04NW_ZxiEStAt9EZt3wOqCPkLpW9DCcW1tR5LGESD1i2SfbFfa9QX8vtTFuqctfPvNJwqmDBBpSl7y9N5v4CVsJp1Xg9_B2UeJmYxhZ1gBcILiNksXIhAoDZ_2xKNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصلى طهران شارف على الإمتلاء قبيل بدء مراسيم صلاة الجنازة وتشييع جثمان الطاهر لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/80898" target="_blank">📅 06:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQVRY2g0zi4c2e0Esr8b8bXGCdkrQzMrWfPB0vn0YU1gossgmgphgoQcTWDMNc9j6rYtf6kMJkIGvy_yr6_VufOZvkl9Wr-OfnQvaVgyLSqyYv5GXcag6MEFLSwnMVRbJS4qhwtzKsqKKZowSC9xevb_kFTFq8G89prMUQWoZgPgPdh4lDXmmBIKj3Fqbo19Turt0BfYWeq_NeDnZm5zR6I9s6x-q0BySj5ruc9oeUiozvT-rB9LL0Bl2enJYPb1_FA4EZHhV5xUgCBWtEzqN8Vdx9HEKKLGJCEfMZu60IPAxW8f8v4JURc16WJjl4tLA2yYBjgoZbxBLh77zpFa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGicGdP3YUXGhAu7xLi0y7hLKMcw7tY0_W9asxyQgoLDMVwUw7fDxUbKYFc67jowUapTbKPbhN1sKEWP3Z5t2BcsuCeBe9gI8b5QxYF832b9jYMUBgM-Cen2sq8oCpqhi9ZzcfihEjCNCu_sv9r_gBR8JeK14naPY9m67mczKcWDOgWn-OpxFF4Yjv5LYqKRe2VXpGH1SiwA0d6QVokLbgcn7wZTSfyXeC2rrSHpXQuhhFm4IOe8_QPlYaPgArtl-cvpwxG6WcM4_OIk2YTbdBmoUcREzz5xO--8zWDz5tV0HOfRyw44dvgL3TRuT812lIIVBAJGRhbLSBlMgnRu5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=bg5hJ9uhG1KhVCqiXxekWftDuCwhtel4KGzyWWs-pXz9S3VxJOih2axNf8hKGF9bMGWD-alnpCElXPZY3ek6H68kOocfQx6LmvC77r6kLsGPtdKPMYpJxuy9O6HmNZpuxg33ourYofOYBjZ7nLYreVq0rQ1nbElD3FpYj2zPYGz9YDKOSLBr8MeXSkQvUIjcYEvXNdZtujuWuCCXMCnUFjGa_CeB3s7Q1KIkLE1r8n8c4WnFjHjWTqszOMcXl02y4mUhdcR0rNoWf6_yA2fAhhMJZ59J0LwllZFxrGSVUEu1fItPs5CcKfkGcMZmc6JRSPsFUNtoSgrCO1whYE0-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=bg5hJ9uhG1KhVCqiXxekWftDuCwhtel4KGzyWWs-pXz9S3VxJOih2axNf8hKGF9bMGWD-alnpCElXPZY3ek6H68kOocfQx6LmvC77r6kLsGPtdKPMYpJxuy9O6HmNZpuxg33ourYofOYBjZ7nLYreVq0rQ1nbElD3FpYj2zPYGz9YDKOSLBr8MeXSkQvUIjcYEvXNdZtujuWuCCXMCnUFjGa_CeB3s7Q1KIkLE1r8n8c4WnFjHjWTqszOMcXl02y4mUhdcR0rNoWf6_yA2fAhhMJZ59J0LwllZFxrGSVUEu1fItPs5CcKfkGcMZmc6JRSPsFUNtoSgrCO1whYE0-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/80895" target="_blank">📅 06:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYAtmbFiqXi8FvUVMKIHo8J0lobI5KS4DRRu_O7pcT09Wfp5IlYPS915jUEdXTqIMW9-VDXJXqxRvkdvMsMunyzF6xt-9MWxzlh-_75H6gdLgG3fcobojrbfo_RfXhDP7BmGhBppKSGBURASZ8sGdi9XP-6OVR-t1rYQU20_wg6bY2fs_HVOSK1CNy9XM_gAt0dpUP33Dgs7hEjB2uJQr9Y9pd3XG2Z2lZLc0J1pQIFRcV8SkStlAZIKyvSuvlyf0rzjmnt6Soga01FbknS8dXemZeWaONupBsVwX_-GKMH_56bgAZ1Ez2krz0wBD5nXdaOlfzxVfCrBXRc8LqamAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/80894" target="_blank">📅 05:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=nCqTmqVKQMkLDgkxDqE5Ya3zuNOOpcEK8DafoMvAT0JSv_qh9IhvkUAEUfVvw2rZcjILD1S-x_bhky-WMW33hPVqo6fsW8r3QVnbEv0tzmuJYFtvXtOvSsHH7fad_WhlXaX_HNsM66zQDkJqXEmfpJapUEdkVCNNAVx0KuCYW_wY4NuON47T7XrixN6f1V_MJNO1tnoAGchnD3d2LMMUOpsw3lB8YJsHIIacIzife4AEkvZHqAfWibmM4ZdI8-TV21qkUsUbzwy0nx_fwk2wXuUd4YMMBG6kjE13qQoBP2z41rAkjOQVB1By02WQ5CjtUvBwaRLqnItJgHKcPaAPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=nCqTmqVKQMkLDgkxDqE5Ya3zuNOOpcEK8DafoMvAT0JSv_qh9IhvkUAEUfVvw2rZcjILD1S-x_bhky-WMW33hPVqo6fsW8r3QVnbEv0tzmuJYFtvXtOvSsHH7fad_WhlXaX_HNsM66zQDkJqXEmfpJapUEdkVCNNAVx0KuCYW_wY4NuON47T7XrixN6f1V_MJNO1tnoAGchnD3d2LMMUOpsw3lB8YJsHIIacIzife4AEkvZHqAfWibmM4ZdI8-TV21qkUsUbzwy0nx_fwk2wXuUd4YMMBG6kjE13qQoBP2z41rAkjOQVB1By02WQ5CjtUvBwaRLqnItJgHKcPaAPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/80893" target="_blank">📅 05:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=Zyrxqydi_v_Ot2YpKnTB-r40ouA_VQRoN210AIS9NZg99Y6hf8MnR48egKmd9PhnufnqJQz8VXJzI56InX8DuKpdWZM3o8FAqKwpuoT_zJf33hfQwPQzlBmCulEJ9t9oN0EC5tOQ4uCUlql8lGU-uIsJRN5UjB4zVvaZSyQ68NVyNqf9rDWmajp1eHYl2H0sDRTdxf2wvTUG79Usr7_bh1cYE7bqc4L78PhEwPBwDOR-VTxss7_ny3KPKa4ihb3R4bzrkTf-Zhhq9qfRw30t_F1cqgpHIzbrGYQSbFzi2Im8GIu91MEzbiOWlf3nKxoTetQqraYDx2Oh4Z9nLAudOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=Zyrxqydi_v_Ot2YpKnTB-r40ouA_VQRoN210AIS9NZg99Y6hf8MnR48egKmd9PhnufnqJQz8VXJzI56InX8DuKpdWZM3o8FAqKwpuoT_zJf33hfQwPQzlBmCulEJ9t9oN0EC5tOQ4uCUlql8lGU-uIsJRN5UjB4zVvaZSyQ68NVyNqf9rDWmajp1eHYl2H0sDRTdxf2wvTUG79Usr7_bh1cYE7bqc4L78PhEwPBwDOR-VTxss7_ny3KPKa4ihb3R4bzrkTf-Zhhq9qfRw30t_F1cqgpHIzbrGYQSbFzi2Im8GIu91MEzbiOWlf3nKxoTetQqraYDx2Oh4Z9nLAudOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مباشر من مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/80892" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgepij0w74SZtaygZOdf-7gQopqMNGYu7ZDNyGbhn0jJY33Li47BQN2HSJCIYHrU44Tdt9JkZf_mJ9CMhCed0F3K7_XnAOMDjQ2NdNOe-16q6bk6iOgrLFdIanrgmTz-kwLlD7lWVV-RGDXjQUdQfMo3IXj7HTnI7kQr9WPPaY-Qe-UGQlZis4soCfHrIUQN_O9r5cYX8NZh0ncUBeclx-9o3ofZrhyXOe66wM_EQjk-3NKRU9KmlQC3KytHwotIthFMwiLj2ldSRmhGpO990IAd22IRN9T9h6dbPePsXGnZR5hLSO-nyToWiLYW9efxBDedAIcUswAmSKCnucmt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/80891" target="_blank">📅 05:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX7qLI6tgEEr2zjZDN7nXwrSwiwtKmmR83Y1vBt5yf2GUTfo_kDejnTUQm-4A_3xmZPfNsmhhEYtxLGuOqwIMG_ISkdqMW1VRJ2am62IJqaSFGKZM0-1_IMrKYJOVTGsbgbVkAUktdGEH4S3T4pFF4RVkJODBZfWk27-mkbN2FDHtGEX2TDr2AfTDzX7jKygjjwKqUgH8_YIRQ7CWx9rInqMPO4DdAqgiGsYLHQ2-RVsrAnkqdU8ju_LCTthJg7VRpOfPbavmpIlMCfHZD1Vdin6_vxuz2BqiJ-wUheFcdkUpPtwoueLdt5QPKJ1mnm_DGGdFw-ShyvH0_InihU9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعة ويبدء الحدث الأكبر.. الحشود المعزية تستمر في التوجه نحو مصلى طهران.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/80890" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=TgHXwfm0oVPT-UV4xMWsXAAsBhLz0yxx72-_zCXSW68VFwtsBWjuXBoiZ8k5KqO6ZHIMvLwntP7ptOQgYEC_g5TPbP0IN5CQL9fEfV6ouHF8WsiLH7mSwij7LLG6NTxAOhVLXlMgcAx9UaGfWJcw098wRrsFNgrksiH9NZbFzLkER0SmBQXSyEPxZfmLzv_LFGpliLHbLKbXWWDwOaJbrqpgnXa8aHTa0sPodN3j4jggxDWgsQ4JLdbtkSkTc4K1PSHc37d_JSH159TrSxD6Hcqmw9ZWs3AxxHmDrAOjoGqQSc6gzXQBJq2i1KOjsYJ_g2U3CfOr_bMYlNe4KYlcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=TgHXwfm0oVPT-UV4xMWsXAAsBhLz0yxx72-_zCXSW68VFwtsBWjuXBoiZ8k5KqO6ZHIMvLwntP7ptOQgYEC_g5TPbP0IN5CQL9fEfV6ouHF8WsiLH7mSwij7LLG6NTxAOhVLXlMgcAx9UaGfWJcw098wRrsFNgrksiH9NZbFzLkER0SmBQXSyEPxZfmLzv_LFGpliLHbLKbXWWDwOaJbrqpgnXa8aHTa0sPodN3j4jggxDWgsQ4JLdbtkSkTc4K1PSHc37d_JSH159TrSxD6Hcqmw9ZWs3AxxHmDrAOjoGqQSc6gzXQBJq2i1KOjsYJ_g2U3CfOr_bMYlNe4KYlcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار "الموت لأمريكا" يرتفع من مصلى طهران قبيل بدء مراسيم تشييع إمام الأمة.</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/naya_foriraq/80889" target="_blank">📅 04:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724637f597.mp4?token=gl4UJgsRXzEiTBfrriScyBkxXgTIqwQbjeavCW3f_zFGhf4xnXpuS9XdIdEbGzdaruGq54uM-os7IvNcio6qGf0Y2_dN3b3R0L49OaHlCIOMIvc90YxLGJd1X3kigyKt4hx6TUSqRwV5Ll50ZCtZt7iP0k-qR0hWKtK2ShPStA8wwittzSGHwOIiJUykWPzfh7MpXcjXoJkW2gJAuGmUWdpQmH8W1i3pVU67XhMUx008V8GShHf-Rb1rc4Tj0FOOkqyZNyJ1l70oeUuHJ2lrekVE-rabGv0hkoH6-I_uYlKADtf9BdGWJl_wTFL8rjz9qaKNfN-7CwR4yz7xUjB7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724637f597.mp4?token=gl4UJgsRXzEiTBfrriScyBkxXgTIqwQbjeavCW3f_zFGhf4xnXpuS9XdIdEbGzdaruGq54uM-os7IvNcio6qGf0Y2_dN3b3R0L49OaHlCIOMIvc90YxLGJd1X3kigyKt4hx6TUSqRwV5Ll50ZCtZt7iP0k-qR0hWKtK2ShPStA8wwittzSGHwOIiJUykWPzfh7MpXcjXoJkW2gJAuGmUWdpQmH8W1i3pVU67XhMUx008V8GShHf-Rb1rc4Tj0FOOkqyZNyJ1l70oeUuHJ2lrekVE-rabGv0hkoH6-I_uYlKADtf9BdGWJl_wTFL8rjz9qaKNfN-7CwR4yz7xUjB7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا مصلى طهران حيث ينتظر العالم أجمع بدء مراسيم تشييع الإمام القائد الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/80888" target="_blank">📅 04:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQc4vCa8ttJ9RkBjzJg_Cmly13qTVPaq4xzc9ee9vt1QthlLDpgAgGBNHTJ8Gez3l_XAJ9fNlkdbh8UvoqifhINtsLTS3DY4gBlBguyPMkG5XDIHASSS17yHZt8XKpo3SxcXtxaCcWxp7xs7akXlMyRfPDhydR8-RMtCpBdF6EoxUd4Q9XtUdSjNgucKiktmS8zaXhvG6dxEXIo-zic7rcN0mTDej1XsNJGnOc-XFxg1wsS4agDwEHr__czzugO2sz8HUPxYStFVDqFu2D1k8CzLNfKgd7CvGhPGbtiMCxr95dUKfseDpUVOn06_1LgJo1_piJIDhPfi3YeU_oM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرق میکنه با خانوادت شهید شی یا با خانوادت فرار کنی.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/80887" target="_blank">📅 04:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=TIQ_YlyC80Elb03sP5PynReMShiZQSRxBdQ67rmDSOWsihO4zz8kFH0KHlMDsWorqvRRpWA7y5d-_wWy55q1pEh83lPrkZMtNyH_PWWyxRyKDO6cXGp0DR2nUXE0XLIacJ7lJzRaKCJ3q6tkmuzLVQrehCDffRBgaj9HgTTDpkv7bp2g9_GvRNDd91HlPb2GZN8_t9OTWL5Z2ufA6t9PsYLaDAafwoSH2y0Gccp0jPI6NBnqa7uvfZBDczvcJunIpdzRWnuzXC4r_tyfFERDi3wxd4f0LsBDPvfBXl0CdazcLJVxojFtRWCi8PnXEZlPQTiENSZ0IqpdioML9MZSjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=TIQ_YlyC80Elb03sP5PynReMShiZQSRxBdQ67rmDSOWsihO4zz8kFH0KHlMDsWorqvRRpWA7y5d-_wWy55q1pEh83lPrkZMtNyH_PWWyxRyKDO6cXGp0DR2nUXE0XLIacJ7lJzRaKCJ3q6tkmuzLVQrehCDffRBgaj9HgTTDpkv7bp2g9_GvRNDd91HlPb2GZN8_t9OTWL5Z2ufA6t9PsYLaDAafwoSH2y0Gccp0jPI6NBnqa7uvfZBDczvcJunIpdzRWnuzXC4r_tyfFERDi3wxd4f0LsBDPvfBXl0CdazcLJVxojFtRWCi8PnXEZlPQTiENSZ0IqpdioML9MZSjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح الأبواب الشمالية لمصلى طهران.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/80886" target="_blank">📅 04:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
توافدت جموع غفيرة من مختلف الإثنيات والقوميات والاعراق إلى المصلى للمشاركة في تشييع الإمام الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/80885" target="_blank">📅 04:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS7NLTGQn9Ki_yX4-fkWITmsW8nxZUy_QSboT6f1gE5mbm8CetS-O7Jkj3YUOIZPf14m0uhlyMkuKZQsB4LuS_SdSuC2id1o7BNmUXfvq_4JCfGSwCzfV3MnKoZkwFm4xBQn3NGezlo68bXL1TL3toGZ2uSLgr9b0IC3666abFbkz41xYQcEUGLUNEcAzD00JUc7WM2acLUJc6uj6fWqrKzl3Ymo5SWWbEiocbnwCNjLmHkh4B7ecBK3nLFezm6f0nP_h8pgHuFy_GY3xYwUpj4pcG3oL7SxEQ2tjaYzx94MVlvnQCWHc_iZmSMJXCJV6372kZRZ8_u1qbNzidJrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بدأت جموع المعزّين بالتوافد إلى المصلى.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/80884" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=QMEl6E_snXCFT6KUDR6pcjzwJWGHJWtLKOFaySJT6HAp7dkHshg-BS4Ce_y6B66HTu9SAdrs_7DE3XgaF0fZ-yql2Kvv5wvShQg8mzOXFUcmduANQPWxrW5zJzmrf7vZguFfQBrQ4_cAEzYzj_IXIRXl_sVS8ejCZL6RyN9muY2hhcR13dyDERWL9UEJCByEDwPhmGst5k7EFcWM-J_QIGa5f4AHlevHyxp1JzLh0TH_jfMqKBYmYY38_PKHCWjv8hPzoBlwzgWrCYU1Ok_xfBYVZ4r12xcHgNqPpEowZfUw2w_nltRc8ahslJ0e-VjUIuA1PI9KvriPPVjWDMJiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=QMEl6E_snXCFT6KUDR6pcjzwJWGHJWtLKOFaySJT6HAp7dkHshg-BS4Ce_y6B66HTu9SAdrs_7DE3XgaF0fZ-yql2Kvv5wvShQg8mzOXFUcmduANQPWxrW5zJzmrf7vZguFfQBrQ4_cAEzYzj_IXIRXl_sVS8ejCZL6RyN9muY2hhcR13dyDERWL9UEJCByEDwPhmGst5k7EFcWM-J_QIGa5f4AHlevHyxp1JzLh0TH_jfMqKBYmYY38_PKHCWjv8hPzoBlwzgWrCYU1Ok_xfBYVZ4r12xcHgNqPpEowZfUw2w_nltRc8ahslJ0e-VjUIuA1PI9KvriPPVjWDMJiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إزالة الأرصفة الجانبية ومحطات النقل والحواجز المؤقتة بالكامل، لتوسعة الطريق وجعله سالكًا لاستقبال مواكب التشييع.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/80883" target="_blank">📅 03:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY1owMKus2oqWQuMmI3tQO8KaIkoasC1O2czJSiYRLXXOCMf4lxPUDsiQlOTFlN7TNtppABZS6oYs6bN2bJCQaU6yp6ciTr7Feb4vT9K51D1AJkxR7bBRmouYfB_dMDqITkFsMYiUOAsEU2riP9XKrleLrhfCwcpPGMrCisGle78g42F92XI--HdzIsKJoGdFvxUEXn9vGCxoxGe7MyIxYdvprjnl_CP0pEbp-RoXSdIEzCdnEaI7z_89lGQTYe3EbkPJAwemo5fOuLHRkz53UsskyG0E8dDwzr3GH8Goab-3Wo2DocaAWjay6OjMAtkWEDGkXVYnoFb2W9mtrpfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
من المصلى توافد المعزّين بانتظار مراسم تشييع السيد القائد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/80882" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11361885ff.mp4?token=QyCIOFLMYlGLFm6NCdzyh-jK59HzOAIFv083Nwxx1MlnYMQd9rQtc8MFKoSDGmPsvziXhXqFtKgspMY-EKGBoWprC8pkpMGT5DpDt730pAK_pKcnawLtAPUrMMP1PGCYH9cMJljQklmu3eacI-AtWoCTzHJHzO5zhk3jMz_99WqjCa3uvArC8m1UIQWkA4bUb3X5-_B0CfyGHnKrsfEHwftamxzIICFn6KUJKSv5XtcBJpAFdTQdvw7L7A_GRAiWWOS7vlj7VGVNL440yY0G3C6sxZ1R5YgTVu-dpKrl7YxoJnRxDaIi9PLOVpDUScwOpf-vL83_YR15yDMCfk6Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11361885ff.mp4?token=QyCIOFLMYlGLFm6NCdzyh-jK59HzOAIFv083Nwxx1MlnYMQd9rQtc8MFKoSDGmPsvziXhXqFtKgspMY-EKGBoWprC8pkpMGT5DpDt730pAK_pKcnawLtAPUrMMP1PGCYH9cMJljQklmu3eacI-AtWoCTzHJHzO5zhk3jMz_99WqjCa3uvArC8m1UIQWkA4bUb3X5-_B0CfyGHnKrsfEHwftamxzIICFn6KUJKSv5XtcBJpAFdTQdvw7L7A_GRAiWWOS7vlj7VGVNL440yY0G3C6sxZ1R5YgTVu-dpKrl7YxoJnRxDaIi9PLOVpDUScwOpf-vL83_YR15yDMCfk6Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أجواء مصلى طهران، قبل ساعات من بدء مراسم وداع قائد الأمة.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80881" target="_blank">📅 03:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80880" target="_blank">📅 03:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfmYItuj_dIrZkCUn_YFcFtwj5_TKjSTU5Am_oQLrHNabh2IU76xKskx8m7EaA0rKAee2hoXVUQyPn-OTxvuPS4kT1vsCedbhsDLt9lLoUjnvEE2-4_5_gj3zrZrheH1p-L752DKm-9nulKwPAn2A0kJKEJuN_zzjgbHSoyk5wbmmiW-r2rV_gL4Dhi16IRdRLz_xGmM2b1LWgNNpKdqShxppEslnF6EUjKouy55BHXks2-USh7J2bgGCfurLtAtocl9-f8zKPSGEnH0OM9PXa9p3RYcouYWQ3MF1lGV0m9zeZRjKOWcIi2Xj1j1tupUDz9n06m_NEeGkIUPPsHjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ج
مهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80879" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=h0m7K1nsw2ByUaBdrE9XC1_uoU0fGfJVpG8lDmNPfxrer6KHL3qowBF0DLKChXi9U_7KiwLyJairVsW9ujlfvuHTC1j91qqfiwzVJkaTCyS50ziZv_AVp2D9t8_M-oW2QAzjoUKIco4qJF6FYGgzMbascMjkjRheEsTlfw_JiAasbGlTYiILh_6MippzoM3-fdWRTzIjIzQWiykBOA7nzR-QQ7aZVZLUnLOXnPacZUMhXJqho_M0TGUmjPdqnVcE9eq75qM_W6l04uNebcMU1toQWGvawV3G5ZzZYloJEUyxkzQUTvk-ui5exIxnVzl51NKIh1sj6m8FyuiOW7njjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=h0m7K1nsw2ByUaBdrE9XC1_uoU0fGfJVpG8lDmNPfxrer6KHL3qowBF0DLKChXi9U_7KiwLyJairVsW9ujlfvuHTC1j91qqfiwzVJkaTCyS50ziZv_AVp2D9t8_M-oW2QAzjoUKIco4qJF6FYGgzMbascMjkjRheEsTlfw_JiAasbGlTYiILh_6MippzoM3-fdWRTzIjIzQWiykBOA7nzR-QQ7aZVZLUnLOXnPacZUMhXJqho_M0TGUmjPdqnVcE9eq75qM_W6l04uNebcMU1toQWGvawV3G5ZzZYloJEUyxkzQUTvk-ui5exIxnVzl51NKIh1sj6m8FyuiOW7njjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80878" target="_blank">📅 02:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=MmiVw-Z-bBiI1MtoBusx82YuEeKDSNpe2abq9Zay7plxKCtzyP5oyXyj1ipvWsXlqNt3kDgz7eZ1qWfLal-4nXUHDUyPBIVoLdArNWrR2fXqOzMVzkDx-8LJJWCwiLAXpC7w3QjvJBC5WP2KPOvzJvMU-D2A2YIj_gDr2oq9dly1q3n4g0Gv_gM2_Rr8k5L85SL000MrUirqur7TNHyNokNL2hX144FJ0jvAv2Qc3bAXaeU34hufaPlZfhiF9q9_9rY_u2yH7kfgIhf7VWZgG7ox5GkxG7Em0Zz9vvvZmZSgx9m6IHgS6cMqYL3C5J9baNI0VdTEjw1nPXjat8NAIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=MmiVw-Z-bBiI1MtoBusx82YuEeKDSNpe2abq9Zay7plxKCtzyP5oyXyj1ipvWsXlqNt3kDgz7eZ1qWfLal-4nXUHDUyPBIVoLdArNWrR2fXqOzMVzkDx-8LJJWCwiLAXpC7w3QjvJBC5WP2KPOvzJvMU-D2A2YIj_gDr2oq9dly1q3n4g0Gv_gM2_Rr8k5L85SL000MrUirqur7TNHyNokNL2hX144FJ0jvAv2Qc3bAXaeU34hufaPlZfhiF9q9_9rY_u2yH7kfgIhf7VWZgG7ox5GkxG7Em0Zz9vvvZmZSgx9m6IHgS6cMqYL3C5J9baNI0VdTEjw1nPXjat8NAIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80877" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=OPnH6wNao-IJkE0DP3h0F9b3i1aDh1-WzuGPDbmd34SdCUKuSLrxZ6Yw74kj3vcbCKVyBUV-W6rceyqFI-UJWmNLxPBaps0M4FgwrnvC6AYTA7cl7Y44TtSeSrZwgoo6qWyuMg8wf5w9PJT95ZVhERMwrmppkx-eEGafiHIWCoWkVFJeWTcaili7opusFBX31CzJD8vGWy-qUe-SY3unb9oUxOamtxgcyhVA7lef_gwOUdz8Drp4YAiTBhKu7NNA2MRMGdr8p16h4IFZm-TrJ3eiZ91gfxfKIthxTeYxhNIgQp5m0TtbG26A-6jKanYudkv4yxBjdveGVtZdH_NEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=OPnH6wNao-IJkE0DP3h0F9b3i1aDh1-WzuGPDbmd34SdCUKuSLrxZ6Yw74kj3vcbCKVyBUV-W6rceyqFI-UJWmNLxPBaps0M4FgwrnvC6AYTA7cl7Y44TtSeSrZwgoo6qWyuMg8wf5w9PJT95ZVhERMwrmppkx-eEGafiHIWCoWkVFJeWTcaili7opusFBX31CzJD8vGWy-qUe-SY3unb9oUxOamtxgcyhVA7lef_gwOUdz8Drp4YAiTBhKu7NNA2MRMGdr8p16h4IFZm-TrJ3eiZ91gfxfKIthxTeYxhNIgQp5m0TtbG26A-6jKanYudkv4yxBjdveGVtZdH_NEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصورٌ كان يوثّق مراسم العزاء على السيد الولي في مصلى طهران اليوم لم يتمالك نفسه فترك الكاميرا وانهمر بالبكاء تأثرًا برحيل امامنا السيد الولي.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80876" target="_blank">📅 01:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
مجلس محافظة واسط يصوت على تعطيل الدوام الرسمي يوم الاربعاء المقبل وذلك لاتاحة الفرصة أمام المعزين للمشاركة في تشييع شهيد الأمة آية الله العظمى السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80875" target="_blank">📅 01:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d4d82aac.mp4?token=UIyMi5C4mLh1GXkdykQPzuvOrYxFdwGB67b_OQkGRxxEuOiRAN-hjJtn7Bt2inbw5fLkMfLg0EckJRbmvXaLxKZ4rFi3pGhWsihavatx55EhjkpU27P2wh3-apg-ajiRcGjf7wRJBvCxQqRMovwwgKE14sYvsCP_YdXXvG7yUa1psrPl4tnZl3LoQ3vnll9g40586RqJ5HhCyAB9J6XRSYP9fhzxX5hxzqoclzOKvPBPOPmc-w04AbZGJWtiUOnxsFJqhGFTj3CocLhWJvv2HfpSN-IoCqJDXOap8pz5BeQdfn5TiujIdQkU9sfs4Yjw0vSmdHR0x3A6ZhN_9nySEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d4d82aac.mp4?token=UIyMi5C4mLh1GXkdykQPzuvOrYxFdwGB67b_OQkGRxxEuOiRAN-hjJtn7Bt2inbw5fLkMfLg0EckJRbmvXaLxKZ4rFi3pGhWsihavatx55EhjkpU27P2wh3-apg-ajiRcGjf7wRJBvCxQqRMovwwgKE14sYvsCP_YdXXvG7yUa1psrPl4tnZl3LoQ3vnll9g40586RqJ5HhCyAB9J6XRSYP9fhzxX5hxzqoclzOKvPBPOPmc-w04AbZGJWtiUOnxsFJqhGFTj3CocLhWJvv2HfpSN-IoCqJDXOap8pz5BeQdfn5TiujIdQkU9sfs4Yjw0vSmdHR0x3A6ZhN_9nySEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بهذا الوفاء لقائد الأمة، انتصرت إيران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80874" target="_blank">📅 00:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieqdR-mA8tAfB9cjQY_Am6rIbDsL2CcTv1X89RBoHWGLyFD8vQxuiaVPM93IIjruOQhIgb9Eb9BO4j3uw8uZ1JtPi0ELPAe4zZRb1tfcOhTgl9NZvKhgJXZT-Jpmi4s10XBWEuiNTpBCZLlq-zXT_gLKVHHQE53vKr0wIHN8E5ppEsgEtOfzfZgi84mfUxN6EGCqQKPumVauk1VVno1L1fds7PBuMheiFFdLeKGRan_WM3qGbaEuCywfLKyKUU3rPrlPBF9dqaltjHJ1sLseY2UGE1UzchlcvDKQluiT4ZsLk2MqD-oiWHdc2JUkpkmEC5OfMDJb4XBNHi78sAPiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللواء وحيدي يزور مصلى طهران للاطلاع على الاستعدادات الخاصة بمراسم توديع جثمان السيد القائد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80873" target="_blank">📅 00:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
‏زلزال بقوة 5.5 درجات يضرب قبالة سواحل وسط تشيلي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80872" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eff78cbb38.mp4?token=ll87YEUafJrCSt5196VimdVjcIbOyJ6UqAKxVGsOjGmKBQb0G1pJlFW4Ix0v-RouVmVudJs7GHc2zBidku_ABHzRR-ppdyTzfC5y_tu4WgWloR_QZol6zpOV1MMQine1Oy69gKikyw28B7b6ATZVfOvoDObvK3tM7rFuTCpKfPm1IWGhmwv_eNjHBv5xiEY12Y-zb-NV5CrxzRF2bGC5QNHqdD-oR6dI5YQb9xv3LFwFxd29kwu-3jCK3QxuCpF_Erkw-HqMY5P8Nlhryx8xh75ZmvDXID2rwxCtUy-N6nFAJlE6jTtexQpH_8DLBfFe3KeOVJfbEM7BYSC35rQjvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eff78cbb38.mp4?token=ll87YEUafJrCSt5196VimdVjcIbOyJ6UqAKxVGsOjGmKBQb0G1pJlFW4Ix0v-RouVmVudJs7GHc2zBidku_ABHzRR-ppdyTzfC5y_tu4WgWloR_QZol6zpOV1MMQine1Oy69gKikyw28B7b6ATZVfOvoDObvK3tM7rFuTCpKfPm1IWGhmwv_eNjHBv5xiEY12Y-zb-NV5CrxzRF2bGC5QNHqdD-oR6dI5YQb9xv3LFwFxd29kwu-3jCK3QxuCpF_Erkw-HqMY5P8Nlhryx8xh75ZmvDXID2rwxCtUy-N6nFAJlE6jTtexQpH_8DLBfFe3KeOVJfbEM7BYSC35rQjvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الشعب الذي وصفته بالشعب العظيم سيُشيّعك على أكتافه ويحملك بكل وفاء ويطوف بجثمانك الطاهر في رحاب مرقد الإمام علي وأولاده الأطهار.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80871" target="_blank">📅 00:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">أنشودة
#قوموا_لله
له بصوت البحريني محمد غلوم..
🏴
#باید_برخاست
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80870" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyWtIFOQoNrdTMWDExKcRjdV61htVI0n0C7-9r7WzUaPf5sutSbjlV8KAFpFO-pebXwnYqn-2DYadUC3JUsMG1rOxjxJpD_cmX6WMggUlMTTjvzvNh_bF8xlN7VXhsTDFfymHAWn3irQe_YD7WG4MuXO0MoXZseULT0HtLTP4Q9Sw6Jn9CcOoY61qjrWYFRGPP6YeZaSnbq6dwhi0DJCvymbVDqQ6-46EaEEBQXfqxPiIxKTxR93R98ucfVDj0wPQdQuBDl_sYOY0Eo7CdEVEZ1roIrOju8dVp9ZXgFgKTh_zqxPF-forfyfKXfcXpej7SlROaBphCKZq4AzfXfHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الرجال الأشاوس الذين لم يتمكنوا من حضور مراسم تشييع السيد الولي لبقائهم على أهبة الاستعداد خطّوا عبارات وفاء للشهيد القائد على الصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80869" target="_blank">📅 23:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9b039651.mp4?token=sW8gZ_aF9I079vVk2mL7gnwUjO8zpq_8_hEL6ZABMFMmGos7cgjEC0KnBSkn3byiO4Ij7oy0fTSII1VJyyEj5RD8rEU4aRWHO3baE73K-ZxQt5ZaOU6bAj4nWvxW9rF5zzdZosMcwCLCQLPBHu2pWjYJUfilV_3NJRqsy8Ugdg8ruoeQBAnnUTduRs8lv-DXRtNadcYmt_3baUdbkEuxwEK_GvubjDBpwlJYYbNKzwlnYxUTqNGSZ04SfzFUzd5D-Rm6gdytBlJYyS5X6wrbqsq0TG-ivYhi-gQ7YYR1OypUWMcJHswrF9PJRUsxER2-85H-Pk5u02jBqqMjvlkZJ7AoBlDvgjZxLSNJ4xmYUfDLIXJ7Jt6p2Le1XESyUpuk_xQ6i39DdYcgyloESx_o5GRRytMtFejRIv8hYzuLawgdluvnX320njETbrv9bgnxL_qnmjYour41hyx9xj2Zl2nThQ7g0zjzYXifyTkbkif97NASpmEg2tzZIHW4eykxkr95N7K-oPt-YpX5I055JCrk1BEu92xLeVpC5QkVfPV1nYNR2C3-0GnOmx4NjL_-xKcc04cshg7LLb-h7gmt_8_Dbth3bm32FWxKvPhN8FkcYUz0CverdFySWCuuImWd92MmnCwI7q-3Yq0c0ZxG67C-rkJUnunc9aOuJRw673A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9b039651.mp4?token=sW8gZ_aF9I079vVk2mL7gnwUjO8zpq_8_hEL6ZABMFMmGos7cgjEC0KnBSkn3byiO4Ij7oy0fTSII1VJyyEj5RD8rEU4aRWHO3baE73K-ZxQt5ZaOU6bAj4nWvxW9rF5zzdZosMcwCLCQLPBHu2pWjYJUfilV_3NJRqsy8Ugdg8ruoeQBAnnUTduRs8lv-DXRtNadcYmt_3baUdbkEuxwEK_GvubjDBpwlJYYbNKzwlnYxUTqNGSZ04SfzFUzd5D-Rm6gdytBlJYyS5X6wrbqsq0TG-ivYhi-gQ7YYR1OypUWMcJHswrF9PJRUsxER2-85H-Pk5u02jBqqMjvlkZJ7AoBlDvgjZxLSNJ4xmYUfDLIXJ7Jt6p2Le1XESyUpuk_xQ6i39DdYcgyloESx_o5GRRytMtFejRIv8hYzuLawgdluvnX320njETbrv9bgnxL_qnmjYour41hyx9xj2Zl2nThQ7g0zjzYXifyTkbkif97NASpmEg2tzZIHW4eykxkr95N7K-oPt-YpX5I055JCrk1BEu92xLeVpC5QkVfPV1nYNR2C3-0GnOmx4NjL_-xKcc04cshg7LLb-h7gmt_8_Dbth3bm32FWxKvPhN8FkcYUz0CverdFySWCuuImWd92MmnCwI7q-3Yq0c0ZxG67C-rkJUnunc9aOuJRw673A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الحشود المعزّية إلى ميدان انقلاب وسط العاصمة الإيرانية طهران للمشاركة في مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80868" target="_blank">📅 23:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
رسو ناقلة نفط عملاقة في ميناء البصرة جنوبي العراق وأخرى تصل غداً لتحميل 2 مليون برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80867" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11a685fe4.mp4?token=OrDqqH6RiFq7XLrye39MXqAgKy6BIpW-3-RcYDVSjbhkx_Q3m_oAtBvy2irtc4QY4hSj1pxDXKO5TQlwjKw_BxnzFuORY1U9C7VVdO5HTQwU424L9EuLjxurKjv4IMz1Nvf7HYJ07VxFwKoGz88DcFIqXf-fZPysCjNyl2e6e1rb29q6XLA49iWUvOVjtulke6WE7JR6XWlGTwGtWeV2KWiCvDXZSi7REnRf4ZTY7tQLNUBHkRkGnxfNc6068Vru-Z3MXknbx3qW-AUHvz3it4dl3Vc7UTF2LpqwDSI-EV6eKblmhXBTnkfVIDB7-g9UJJfpua3jx4qu7QqVY26z3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11a685fe4.mp4?token=OrDqqH6RiFq7XLrye39MXqAgKy6BIpW-3-RcYDVSjbhkx_Q3m_oAtBvy2irtc4QY4hSj1pxDXKO5TQlwjKw_BxnzFuORY1U9C7VVdO5HTQwU424L9EuLjxurKjv4IMz1Nvf7HYJ07VxFwKoGz88DcFIqXf-fZPysCjNyl2e6e1rb29q6XLA49iWUvOVjtulke6WE7JR6XWlGTwGtWeV2KWiCvDXZSi7REnRf4ZTY7tQLNUBHkRkGnxfNc6068Vru-Z3MXknbx3qW-AUHvz3it4dl3Vc7UTF2LpqwDSI-EV6eKblmhXBTnkfVIDB7-g9UJJfpua3jx4qu7QqVY26z3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الحشود المعزّية إلى ميدان انقلاب وسط العاصمة الإيرانية طهران للمشاركة في مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80866" target="_blank">📅 23:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZBonxT8jEoGcO9irLGk14DDphFu79Tvy25MGCUsL_dMLlxylLgz8j3OQrx0n_6OiWtLiXCOfDqCxqgIDzYhxVGUQQX57IYsLuL1FNU5oEeuLwlGd3gr1MGayVIqTcrWbkj7kbYOephe_bR5666cYhFUP5ZgTQR3hQ0aubqE5_VVEFsfw4pDMi1Pxi_pZ6qW3zvPtRLKNGHeWsjKKMDO3uIvEkuLVDvYp7pDDQ21OoIB64iLgS_YkJqsDEhfsVvsHSBkJB_za6S_B4VPMOb_J82rcEJK2EgzxbVZ3P6f8D-GUfwcoNPPvwYOapS4kZnG4eF8lRsKFpNY5PZosV6LBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتلاكن روحي وروحك مثل الماي ولاگه الماي</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80865" target="_blank">📅 23:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
العاصمة العراقية بغداد تعلن تعطيل الدوام الرسمي، يوم الأربعاء الموافق 8 تموز 2026، بمناسبة مراسم تشييع السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80864" target="_blank">📅 23:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
من ميدان انقلاب وسط العاصمة الإيرانية تجمهر المعزّون بانتظار انطلاق مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80863" target="_blank">📅 23:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
‏
ماكرون
: حاملة الطائرات شارل ديغول ستعود إلى  فرنسا بعد توقيع أميركا وإيران مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80862" target="_blank">📅 23:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
من ميدان انقلاب وسط العاصمة الإيرانية تجمهر المعزّون بانتظار انطلاق مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80861" target="_blank">📅 22:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80860">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=mXZcKNvGZr5hQvBPgVHaBeY4EFbApaUsfAitRMXKMC3RGaG2AYtW-4lp9JcVbNO4njELcOlH4Q8NI7U4AqT7KTOuxi7HPZ_chfT30qv2ZFI93BmzroVx6ZoeyyRdY-f5wfhNspDxDeLn3IH8MGlu6ifIfa2m_rzC7_uEou7HeVHEvjZIMkKr794UfPvMll9yReamsNTWUxengw7UW1fgNU2F_4eNl7dZpNe5eRnsdF_DFJ6w28z4OLKVF3VnLOa_3bJvF68pzbyLYRQvT43pRJqWdgKKgCHwonlKlP55IiS2v1pA1Sk4lLKx26HFl0e6OovmiEa1iT2o_GFq1hAr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=mXZcKNvGZr5hQvBPgVHaBeY4EFbApaUsfAitRMXKMC3RGaG2AYtW-4lp9JcVbNO4njELcOlH4Q8NI7U4AqT7KTOuxi7HPZ_chfT30qv2ZFI93BmzroVx6ZoeyyRdY-f5wfhNspDxDeLn3IH8MGlu6ifIfa2m_rzC7_uEou7HeVHEvjZIMkKr794UfPvMll9yReamsNTWUxengw7UW1fgNU2F_4eNl7dZpNe5eRnsdF_DFJ6w28z4OLKVF3VnLOa_3bJvF68pzbyLYRQvT43pRJqWdgKKgCHwonlKlP55IiS2v1pA1Sk4lLKx26HFl0e6OovmiEa1iT2o_GFq1hAr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تدعي احباط محاولة تفجير عبوة ناسفة زُرعت داخل حافلة في حي الورود بريف دمشق، حيث تم تفكيك العبوة ونقلها إلى مكان آمن، دون تسجيل أي أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80860" target="_blank">📅 22:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1485646dca.mp4?token=uU1OVNG-hffPgV9VjHN5NtGzJ1JYEIxdXctcJvEDmX0pYr06WS4bTrE2SNVD9weQFYDHpd15mEVABtE4A1LY6mvmK_ts2vnGi7o1KCMfYA2K_mFdl7A5IhaunL84O5JrtiPhaWbxC0d0n0kl0WRjqDD7lyeEpcYcnyfKR7xMS4SkNVg6FSIDnAN5MIatURE1aJISgbD3CF1H-nJRwsSd7g-G29iPeFTboecYV-m4FyWG7RhueszbV7cj5fueZKTFvMTBAWQSkl2Fh24tMOJfI6hARE4kQANFmUORWGgUH0n_cN3a68okuYbfIaQPskvM1P5fge_cg59zzKiyGoYr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1485646dca.mp4?token=uU1OVNG-hffPgV9VjHN5NtGzJ1JYEIxdXctcJvEDmX0pYr06WS4bTrE2SNVD9weQFYDHpd15mEVABtE4A1LY6mvmK_ts2vnGi7o1KCMfYA2K_mFdl7A5IhaunL84O5JrtiPhaWbxC0d0n0kl0WRjqDD7lyeEpcYcnyfKR7xMS4SkNVg6FSIDnAN5MIatURE1aJISgbD3CF1H-nJRwsSd7g-G29iPeFTboecYV-m4FyWG7RhueszbV7cj5fueZKTFvMTBAWQSkl2Fh24tMOJfI6hARE4kQANFmUORWGgUH0n_cN3a68okuYbfIaQPskvM1P5fge_cg59zzKiyGoYr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. من اللقاء الأخير للجندي الشجاع الوفي وقائده الشهيد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80859" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80858" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80857" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXSy1XWGSicTgTjTS9Rfr2LDgjvkQj6qC6JsGfTeRT8hn8jCf8f-7d5ZwzLkV2emeobU3ZWQzuu9WFKdVpGb6gUWVfll14WYNv_O-d77UhhOpKFDDd_8lCIoxes03XnZRnPg0N385LXcKi_m3nyYZgXFNfayyQmMsJd5myahGEzMzdFhMgN2cb9lI0PcNsesk0xqrQXFIHdBts-4LttDIstqpunxBZIMntyiVD-_-2wPgquaCrnGQ-NHMR2L_rzHuv2ul71t2VvmR4QyB49iw4_NvpP7tn2X9BwpHWMElEapisgH-RDJW93rT7CVfYJxLKWJfD6GdR7wcdF8uUDGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
تخيّل أن يكون لديك نحو أربعين مليون مواطن يعتمدون على برنامج قسائم الطعام، ثم تصف دولة أخرى بالجوع. هذا ليس تصريحاً، بل مجرد إسقاط. احتفظ بنصائحك بشأن برنامج المساعدة الغذائية التكميلية (SNAP) لنفسك.
‏مواردنا، خياراتنا. انتبهوا لمعدلات سوء التغذية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80856" target="_blank">📅 21:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=sziBlZ6tTzjBq7D7S-Y8X1yid8TFLV7ub6EGtR-jcqEomLVB3M4P87NdseTqZkcl5ucDcmj2bjpB7HHTGunQNj-HoWMGysI5KU1VCNQgRolyCLCOg3OKWXB9ZfHezMeWEZymiYYhEpHHZNzVgTEtY1CZqCofCKfAsfTyfdgUkoJ4VbnmOIAitlDbBbWIojltqyFQ48PQaH7QX5VDenaFszhAKTZhf41V7rgAhRdTeie00GztlO4mc1LSWxBcZEKnsm1Q-D02D9xnLyEroy9yV7QNCUfhmRdAgXtW3EpnaexgzJQXcY77EudJ4xLUdZXLsFQ8WzzkbJ3QHQ1w2QXk3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=sziBlZ6tTzjBq7D7S-Y8X1yid8TFLV7ub6EGtR-jcqEomLVB3M4P87NdseTqZkcl5ucDcmj2bjpB7HHTGunQNj-HoWMGysI5KU1VCNQgRolyCLCOg3OKWXB9ZfHezMeWEZymiYYhEpHHZNzVgTEtY1CZqCofCKfAsfTyfdgUkoJ4VbnmOIAitlDbBbWIojltqyFQ48PQaH7QX5VDenaFszhAKTZhf41V7rgAhRdTeie00GztlO4mc1LSWxBcZEKnsm1Q-D02D9xnLyEroy9yV7QNCUfhmRdAgXtW3EpnaexgzJQXcY77EudJ4xLUdZXLsFQ8WzzkbJ3QHQ1w2QXk3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80855" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=HAgSCTG8ZX3c--mFTMne_rfbaKnDoh96EIH5Gba75ZN7lcoFnZQvce-TyvfBGucgqde4xSwCt3IUmoOGZK7KXCMpVymv_YWHnhM-aWkK6Af_dQ8x2rC3xcHyU6xcQ0XUOqtEAgSKihiCLSmYaZwMxeE_C3JOSBoX-1mH6enmo9GrxKfCHuWlmKvzfiz3euZia3YSuuqnRm_8I9HhmVQnnDtsBn1IvGIomtIvNU1Lrgz2CbdYaRlqEn9uIBizBMblcOd6hTnrq08UHshmzya4VXBJdj0PAluDpTX6R6CZ0ioRYaL7x810V_7GNuB8dGq1ElwMEUiALrYTSHm7KIdlwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=HAgSCTG8ZX3c--mFTMne_rfbaKnDoh96EIH5Gba75ZN7lcoFnZQvce-TyvfBGucgqde4xSwCt3IUmoOGZK7KXCMpVymv_YWHnhM-aWkK6Af_dQ8x2rC3xcHyU6xcQ0XUOqtEAgSKihiCLSmYaZwMxeE_C3JOSBoX-1mH6enmo9GrxKfCHuWlmKvzfiz3euZia3YSuuqnRm_8I9HhmVQnnDtsBn1IvGIomtIvNU1Lrgz2CbdYaRlqEn9uIBizBMblcOd6hTnrq08UHshmzya4VXBJdj0PAluDpTX6R6CZ0ioRYaL7x810V_7GNuB8dGq1ElwMEUiALrYTSHm7KIdlwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80854" target="_blank">📅 21:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
‏
رويترز:
أكبر مشغل لشبكات الكهرباء في الولايات المتحدة PJM يعلن حالة الطوارئ بعدما بات غير قادر على تلبية متطلبات الطاقة المتوقعة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80853" target="_blank">📅 21:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=mkzoaC357OM9f2MVpIT7vzGgNmf0rYYnIX8rZp2PGp9hSl4eo--xThaCIFYlHCF_shZKxEpWJen9Eoe5OjnC4ugjbe6hEhG_79AcNH-nZWZN2gM3brjN7dKaQMpqiOwOkKWK46immVo-egkEJ-p0dLfDTw18VrIzqaNqpuk2XBTi_PMb5NayoUkqF6LczU9kVmbmGDAUTNqUfjDyqk0ZEuw7flgnHe8M6QLzhtiKZ3oRhV1Os0J1oy1uxbWlNAMpzDzL_7hL0Dn-SY7u36EY5NAjysfbf5z8DqX51fkwLb0nf6oPaQsWYLMuaGMFWoeUmhiboJsCyYfslbPDi6U2QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=mkzoaC357OM9f2MVpIT7vzGgNmf0rYYnIX8rZp2PGp9hSl4eo--xThaCIFYlHCF_shZKxEpWJen9Eoe5OjnC4ugjbe6hEhG_79AcNH-nZWZN2gM3brjN7dKaQMpqiOwOkKWK46immVo-egkEJ-p0dLfDTw18VrIzqaNqpuk2XBTi_PMb5NayoUkqF6LczU9kVmbmGDAUTNqUfjDyqk0ZEuw7flgnHe8M6QLzhtiKZ3oRhV1Os0J1oy1uxbWlNAMpzDzL_7hL0Dn-SY7u36EY5NAjysfbf5z8DqX51fkwLb0nf6oPaQsWYLMuaGMFWoeUmhiboJsCyYfslbPDi6U2QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:   بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80852" target="_blank">📅 21:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🌟
مصدر إيراني مطلع:
مسؤولين أمريكيين كباراً شنوا، على مدى الأيام الخمسة الماضية، حملة واسعة النطاق لثني الدول عن المشاركة في مراسم تكريم القائد الإيراني الراحل. ووفقاً لما ذكره دبلوماسيان عربيان -اشترطا عدم الكشف عن هويتيهما- فقد ناقش ماركو روبيو الأمر شخصياً مع نظرائه من خمس دول عربية على الأقل. وتشير التقديرات إلى أن ما لا يقل عن 13 دولة -بما في ذلك ثلاث دول من أوروبا الشرقية، وخمس دول أفريقية، ودولتان عربيتان في منطقة الخليج الفارسي، ودولتان رئيسيتان في شرق آسيا- قد قررت عدم حضور مراسم تشييع القائد الإيراني، وذلك بسبب الضغوط التي مارستها الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80851" target="_blank">📅 21:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGd4FdU131nOQVQeZuDuSFLEkCsrFtHE_xVxQP4gP5W_AhKCJIQqK8b9xEQQ06Vq0m8VF3jXIpux1Pb3oNHFxcL-suwL5LobV0UuEWzz0NVG8tWf5XifTF_W8u7qs9uSr4hdjwya7qkyFyAVYutv5W5t8DFUfq8zg5zuBoi3wuXJLpEjPkEWdcJofmq9rMRQFo55ZjNQ_tzCZmPp95e2_uBZwfhskT8GfSJH61f_8Y9UK7Qv6V-7Zk9619vSB7xe-AOu--89nPs17qBMAhFCcGHVLbEXPPc1ml3TgYVBs_VpH8-fw9zc3IvN53FQBoNpVDn8FRTOoJ2EA89nw1fRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80850" target="_blank">📅 21:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=HoSiRdKEeHPCI9mo94j7tmJ-5wBbLX-lLu1R11LbTxz7oQLLqFqu9XhnjQMzMyT5MXmTPC2zdiAyrxnK4tt2ZGnHZxXzhpfgoXm2MgcqodBQWRbUKi9rtkHpbzhvujtN_RClMK2L_RLw8FRfT19BsmWTjFTDJxh5awkdS8H8NwW1e_lC5RCTd_tCQCnXtV3CAxPZea96tTDDkq_wmQiMG2f8xJKepTMezHI-Mfgs04Pv8cU5hYcpIt3aAYJDVlEOCUa_ccs7ti9klbrKYKZiKHNHiYoNXgYIbeisdW2NR609QiLSoxL9aA9sCPGimMQg66k_hl2PIGAIJ9wx0myygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=HoSiRdKEeHPCI9mo94j7tmJ-5wBbLX-lLu1R11LbTxz7oQLLqFqu9XhnjQMzMyT5MXmTPC2zdiAyrxnK4tt2ZGnHZxXzhpfgoXm2MgcqodBQWRbUKi9rtkHpbzhvujtN_RClMK2L_RLw8FRfT19BsmWTjFTDJxh5awkdS8H8NwW1e_lC5RCTd_tCQCnXtV3CAxPZea96tTDDkq_wmQiMG2f8xJKepTMezHI-Mfgs04Pv8cU5hYcpIt3aAYJDVlEOCUa_ccs7ti9klbrKYKZiKHNHiYoNXgYIbeisdW2NR609QiLSoxL9aA9sCPGimMQg66k_hl2PIGAIJ9wx0myygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80849" target="_blank">📅 21:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80848" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شوارع بغداد عاصمة العراق العظيم تستعد لأكبر حدث بالتاريخ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80847" target="_blank">📅 20:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_BIDEQuY4THyYro6hIyFP-Sz1Y1Zoo7s-mzQajRhLkj17Ej7qH_5K5wDpjedJBUaRxboGeO24QtVmPTZNkje4LvnnL438CdDBbLRiGTlx6LEylPtBD1bKSsQfSrmwwi4_r5B2AUqwLPSNrrEO4-qrbY_xn0Oxnucbo6ZZ4686lNjpS-WR0nkuOU1JU2dftEU-GiXj47dAw2XF4mTLk-HnfK5JCtWEBDxpdxa34agdaun2-Rji-qjEdBshPO4PigRQWfYTlPKexeelPPnFfbrINUfEYSqCPFzW1atiRc9XGWHcPriiqStqf_NSR-nxNSLPYRSQ8Z00HuTcH0rueFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kp2COK2q_Q5Ad9acjbBGFTQ9OpzINX3Mf3NyniAigNHRBhiGjkSTv_JOCsKwARyS4vMrXa8mfCZfF5UtaHE-qCNzSLd3R-wcA7h1-FruWbEdo5upuOlBNZ55VCXo3oZ1iqxqhEGVJxYwQLfOnrY5_GkaDZwwkja3Sof-0HLwVJE7u_w112SQas7zaeHyTSCPetj3Art18LCw_ybe4UmEAirBRaRiCgqwsxCxeOd_k3slN0kJaniz3-cQeQcZ4CMdl_IXojkQ97sJc4wsS1kD6mDl6dWgatspNapbMHKA-b903jmsNq_g1MBQQUegn8gboBFgZwuQt_Ts_YN0kAoCNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80845" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=a4tNQQdnLriurEnhfLFAnpcOP2DhDMZrrBI17aWptnrx42PUcU-3TZHhbzsR-ugn-FKCVW1RpCunplqBP6VWS48lvGf2bHukmOoaDRru6lMAjkpEiXOcQc4pERC-SiJRYW2Iuv2JRvB-pWVwp1bJnNUJEnnihOsis45BHgnSPlU37_AX0ICmayt6Vk9ZifN-2ZStU79HD5h8oRzZKfW3WmmQXAJqlfrdkJJgPhAAaKg8TEzfH3bpTtA2hWOkJs1atpwcH43xe38XsZWBaFRxh0gdY0FaQD16ZpTl_atUoH4O9BYw0cDUR1FLp1pl1kMwBPRK4jHKplcHZkoA8My44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=a4tNQQdnLriurEnhfLFAnpcOP2DhDMZrrBI17aWptnrx42PUcU-3TZHhbzsR-ugn-FKCVW1RpCunplqBP6VWS48lvGf2bHukmOoaDRru6lMAjkpEiXOcQc4pERC-SiJRYW2Iuv2JRvB-pWVwp1bJnNUJEnnihOsis45BHgnSPlU37_AX0ICmayt6Vk9ZifN-2ZStU79HD5h8oRzZKfW3WmmQXAJqlfrdkJJgPhAAaKg8TEzfH3bpTtA2hWOkJs1atpwcH43xe38XsZWBaFRxh0gdY0FaQD16ZpTl_atUoH4O9BYw0cDUR1FLp1pl1kMwBPRK4jHKplcHZkoA8My44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80844" target="_blank">📅 19:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">هذه أيام الـعـراق التي يعرفها العالم..
🏴
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80843" target="_blank">📅 19:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:
بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي والعلمي والاقتصادي مع الإقليم.
نيجيرفان بارزاني: شكل استشهاد القائد الإيراني خسارة كبيرة للشعب الإيراني والمنطقة. نعتبر إيران داعماً وحليفاً ثابتاً لنا. لم نكن يوماً -ولن نكون- جزءاً من أي مخطط يستهدف إيران. عبّر الرئيس عن تقديره لموقف إقليم كردستان المتسم بالتعاطف والمسؤولية تجاه التطورات الأخيرة، وشدد على توسيع التعاون العلمي والثقافي والاقتصادي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80842" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsWQu3lf_V3FIlxdXcm1EM6ZN5OSA4nO_ChbpYkjZr05TlzcYf8bp-pDn9kzJIL9YfwJaII2JqnIkjWZm0FN40JNXyRGq7u_2GgrYff6hli05nzkcX-82JeNGPyqr_Wc7Qtq8IVl1YtAdGKy4dw5aZfs76e1FYuZKPcm1hKrFqWkSBSYF4bNkQM9ic3_HZsHqsd0ApsvsyVlK2mgW1Kxwz8HnDsljBPGiGbfuQY-XPA-ITS8ZvOGGhkgiuLWwIHSgUjbd1BFJdRnsoiqMrfGuSnPwMksQ6tsPqOpB5dJFnXQlaZS6HYjtgmKZWNjR2OSMze5zRWiisNxybj0itn_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتري مدفيدف مبعوث الرئيس الروسي يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80841" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYlqfRpQatMhcrbUNPF_tRcQ_62J6GKgDok_JG78q8wtc8VYlWhZWk16XO6i6Kd00M22tRY2NrUSetwvMXOQ5ohh06Bbhj87IRumBB9efYbYjb4a0G8jGaPA2lu6pu0iPj7A7UT7b8QKR9NqBMGjUvp78Jl5dveFnemFPCh-PeC68ysa_xdqZNUcBf-gp9PsSQaOi1DRMaoKtgvF-r0sqcR5jKNPmZvLRFBqjXM6GG3DWRHkgbgA-GTU2VR4g8IrASep5aLzauXvQHzeNXd69wJCpvQ2z_byTU4Er3mlnZSrqWVz4lkr0OmpsM7dGDP3PvgtTXNJuD_Bo96xYwW9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
قائد فيلق القدس"اللواء إسماعيل قاآني" يستقبل الوفود العراقية المشاركة في توديع قائد الثورة الإسلامية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80840" target="_blank">📅 19:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=NmLqlfTNgExc0Pr7SuOYD8L4soPydjVPqVyAwtnoLjNs1eEInO9vY0uW_KZqMEZri4-8AwfNj1mLng9LHtO0z2XIMHu75RIR-SN9XG73eB-LwFnnO1CWjyEsJVHvAGu716hD7kbakpTgprKeff-B4665PKmEfsg-LcuVDg1kSvr45sW2j-HiFB3aXg0JyzUoJMgIMY7xxuVmEY7LS7Iv62pPFwLsxcucQZFxB3v3Gahf0iFa0JvXFyWtV1kBTNlBBQQLdQQ9X99Tvy0pV75VnrBOKu_VasGI_TIml9aQRdmIEcrlcLT03ru7uWDbhqNG_egJwSO_5TSwJ-4Qouwheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=NmLqlfTNgExc0Pr7SuOYD8L4soPydjVPqVyAwtnoLjNs1eEInO9vY0uW_KZqMEZri4-8AwfNj1mLng9LHtO0z2XIMHu75RIR-SN9XG73eB-LwFnnO1CWjyEsJVHvAGu716hD7kbakpTgprKeff-B4665PKmEfsg-LcuVDg1kSvr45sW2j-HiFB3aXg0JyzUoJMgIMY7xxuVmEY7LS7Iv62pPFwLsxcucQZFxB3v3Gahf0iFa0JvXFyWtV1kBTNlBBQQLdQQ9X99Tvy0pV75VnrBOKu_VasGI_TIml9aQRdmIEcrlcLT03ru7uWDbhqNG_egJwSO_5TSwJ-4Qouwheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق من الإستعدادات النهائية لمصلى العاصمة طهران ومحيطه الذي سيستقبل غدا مراسيم صلاة الجنازة والوداع للجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80839" target="_blank">📅 19:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
الحرس الثوري يتمكن من قتل إرهابيين 2 في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80838" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
نود إعلامكم بأنه تم إغلاق الاستمارة الإلكترونية الخاصة بمنح الهويات الإعلامية لتغطية مراسم تشييع آية الله العظمى الشهيد السيد علي الحسيني الخامنئي (قدس سره الشريف).
ونود التنويه إلى أنه سيتم خلال الساعات المقبلة الإعلان عن موعد وآلية ومواقع تسليم الهويات الإعلامية، لذا نرجو من الجميع متابعة الإعلانات الرسمية الصادرة عن اللجنة الإعلامية، ونسترعي انتباهكم إلى اعتمادها حصراً.
اللجنة الإعلامية الخاصة بمراسم تشييع آية الله العظمى الشهيد السيد علي الحسيني الخامنئي (قدس سره الشريف)
الجمعة 3 تموز 2026</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80837" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ماجئت إلا مودعاً... سلاماً عليك أيها الحسيني الشهـيد
#طهران</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80836" target="_blank">📅 19:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef6d3a147.mp4?token=r1FRvz-0kgNEqPpFxa7DgoaM8GOJkVYtQqV35IEWlJLe7N6rMjsdAvJARlVERxGwxPRu3P4rXB0XP7ExhuybU1GHbjZ8Zkywz1GoN_w8ZoQ-HcT3gJffi9HEsmc6WqUebjaHxkDjmCAMzoQD8rLbSvqUvzyHZLhGvD1XrZTDBng6ArScDMSDyQpcqzY1H_cHE0CCMJ_4_tJlNSXTW_aoGCJVjSOW2LDUhIloxQyyYln2frwkdqixqFOanFSZ8uPNBx_YE-QZHTzwJ2nWfio-69dYUsGtQIlwMN_dDY5YeVMlXsuLkB1gwxR7X3p7kly7yCvQpCxOh94lNXZSVsS7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef6d3a147.mp4?token=r1FRvz-0kgNEqPpFxa7DgoaM8GOJkVYtQqV35IEWlJLe7N6rMjsdAvJARlVERxGwxPRu3P4rXB0XP7ExhuybU1GHbjZ8Zkywz1GoN_w8ZoQ-HcT3gJffi9HEsmc6WqUebjaHxkDjmCAMzoQD8rLbSvqUvzyHZLhGvD1XrZTDBng6ArScDMSDyQpcqzY1H_cHE0CCMJ_4_tJlNSXTW_aoGCJVjSOW2LDUhIloxQyyYln2frwkdqixqFOanFSZ8uPNBx_YE-QZHTzwJ2nWfio-69dYUsGtQIlwMN_dDY5YeVMlXsuLkB1gwxR7X3p7kly7yCvQpCxOh94lNXZSVsS7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق من الإستعدادات النهائية لمصلى العاصمة طهران ومحيطه الذي سيستقبل غدا مراسيم صلاة الجنازة والوداع للجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80835" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
مسير موكب تشييع آية الله العظمى المرجع الشهيد السيد علي الحسيني الخامنئي (قدس سره) في محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80834" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية عند الـ6:00 مساء بعد قليل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80832" target="_blank">📅 18:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=b6X99J-RNTyseFozZRzDeuP7o8WuR_bHfwUGHNRulPiQKKzs8dTQuskORshJf6vgWn7F71yQDfAu6W_PYHoZ9bj4e8e_k9s0qPupqwprRAp4j83AaBXHa-9gxBzRCQcpTgzrv895Vb9ypyGxutWKD9ttz2gTkfwE5N667VNpTYhbFWkdEXIvpC4Fa2oL2gdZVcoGd8UioED3g33hHPZUtcPt2kkC0-OiNR_yd3opPP22qYhlmVKSOlrOFow7Ld_qfYO0YP1mUHuHaDc9V0AoV9E7iZqzRxMESimR_a69DShFMcPk5Q7OKzX3lDrpsFtHfsG6HcP3JdLgLkTb0woXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=b6X99J-RNTyseFozZRzDeuP7o8WuR_bHfwUGHNRulPiQKKzs8dTQuskORshJf6vgWn7F71yQDfAu6W_PYHoZ9bj4e8e_k9s0qPupqwprRAp4j83AaBXHa-9gxBzRCQcpTgzrv895Vb9ypyGxutWKD9ttz2gTkfwE5N667VNpTYhbFWkdEXIvpC4Fa2oL2gdZVcoGd8UioED3g33hHPZUtcPt2kkC0-OiNR_yd3opPP22qYhlmVKSOlrOFow7Ld_qfYO0YP1mUHuHaDc9V0AoV9E7iZqzRxMESimR_a69DShFMcPk5Q7OKzX3lDrpsFtHfsG6HcP3JdLgLkTb0woXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة التعاون الاقتصادي (الايكو) يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80831" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
هيئة الإعلام والاتصالات العراقية:
نفذنا بالتعاون مع الجهات القضائية والأمنية المختصة، سلسلة من عمليات الضبط بحق منظومات البث التلفزيوني المشفّر العاملة من دون تراخيص أو موافقات رسمية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80829" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
