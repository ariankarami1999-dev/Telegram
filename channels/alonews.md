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
<img src="https://cdn4.telesco.pe/file/OkNnPhH7KymmABjXjlJA3J4cTf_AikVTNSbnH1m4bDqm2NWJha84kZoIGCy220omjQvpXfiZyP81aMPa7vRsfjA6FFCglZgFwNTD1lEsxrrdfRZCyuPTiHl-w1JugPXxQBdJyt8O3VvwfxlTJ8-HKCcUMbDy0hbCyaKUBngeRLl-kFrq9TYzamj5_moK0N_dYiNJUTp22EzDwIzDnGIZf7YqE1_bnhlOTx7Sc2_7PCewFqGL2yFB7DQRmWj_jmERyePfxGyLKRZfWLo-rXS6wRiQmIV-r3yquTpWK9H5jgKKOhNBUHl_2oHGdCq9wVqJf05BrhR4d1eHTquHnYMBcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Kj0Btsy3BkSq3C7zm8qE0kYZHAMpvDo4-A3kJadzNLmIrSWAdTfBhZYJdqDwBx_e_SKYOjzXiJKbgw9njMZds_9f4jv7-WCy2mp2Fo4a1D9LRVZQ6Oq9FL0xVVVtlcgy3nigQ35jH7Daj_7O8nKAXgwDwOJyStEXcqRWUwQdcRr7NY1-xQyOAfkiRmKSYz7QweC0MZM5fkHsMSqFgVgLdmQaJX68aVChnEH9huLo2amKuk5Q020bKM--eL3N__rkvQ_mZTudK2SwOfW361TwpUtiggJF6LzYDCZiR4wPSycUOiaySqPpCPMfkGM-9sTZeKTBW-2JByWfwRASw1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دفاعی بحرین: حملات هوایی ایران را رهگیری و منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/135279" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مدیر سازمان سیا، جان راتکلیف: اگر چین از نظر فناوری بر ما برتری پیدا کند، این یک مشکل جدی است. ما نباید اجازه دهیم این اتفاق بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/135278" target="_blank">📅 10:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/135277" target="_blank">📅 10:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رسانه لبنانی الاخبار: رئیس دوره انتقالی سوریه طی روزهای گذشته پیامی از دولت عراق دریافت کرده که در آن از وی خواسته شده است از ورود به پرونده لبنان خودداری کند. دولت عراق به دمشق اطلاع داده است که اگر شیعیان لبنان یا حزب‌الله از خاک سوریه با تهدیدی مواجه شوند، گروه‌های مقاومت عراق بی‌تفاوت نخواهند ماند و هر اقدام سوریه در قبال لبنان می‌تواند با اقدامی متقابل از سوی مقاومت عراق علیه سوریه همراه شود.
🔴
احمد الشرع در گفت‌وگو با مقام‌های عراقی تأیید کرده که دولت آمریکا از او خواسته است در پرونده لبنان وارد شده و علیه حزب‌الله موضع‌گیری کند، اما او این درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/135276" target="_blank">📅 10:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
امتحانات نهایی ۴ استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، یکشنبه و دوشنبه ۲۸ و ۲۹ تیر، هم برای پایه یازدهم و هم دوازدهم، لغو و به زمان دیگری موکول شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135275" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88f12b6e5.mp4?token=XvlofKveSzt8p-OyLNdTGHqQgJQPjCRwt9Fx0u510e1m55thi1ceAHfTJ6cdfbcnGZgLsZQwymfoH864VHisPrnwKjLEzZfBESV0NPmqBZx2RGekYjLNLUHIhydvVoZJF_UXdCwH0r4WFWIrduKlkJOS3VRzodC1C3WxJiuAclKVh_7Pv6rJ5K4oOPGakpimcxBmFRBBZ-WHcrFCuRRVyPX4GUKuViQ8-4T6pl5bLXf8qtJw9YZDXF1jEzPCZ3x1mmudrZ7kSiVOF768neO-WDH-0LuJ2VgV6R4fLwcbwkRzsBBun4heoA9T1uitva0OBmj-J-jieuuDqbhEi9sy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88f12b6e5.mp4?token=XvlofKveSzt8p-OyLNdTGHqQgJQPjCRwt9Fx0u510e1m55thi1ceAHfTJ6cdfbcnGZgLsZQwymfoH864VHisPrnwKjLEzZfBESV0NPmqBZx2RGekYjLNLUHIhydvVoZJF_UXdCwH0r4WFWIrduKlkJOS3VRzodC1C3WxJiuAclKVh_7Pv6rJ5K4oOPGakpimcxBmFRBBZ-WHcrFCuRRVyPX4GUKuViQ8-4T6pl5bLXf8qtJw9YZDXF1jEzPCZ3x1mmudrZ7kSiVOF768neO-WDH-0LuJ2VgV6R4fLwcbwkRzsBBun4heoA9T1uitva0OBmj-J-jieuuDqbhEi9sy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید سنتینل-۲  نشان می‌دهد که یک دیش ارتباطات ماهواره‌ای در پایگاه ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، توسط پرتابه ایرانی مورد اصابت دقیق قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135274" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135273" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
شرکت برق کویت: یک حمله جدید صبح امروز به یک ایستگاه برق و تاسیسات شیرین‌سازی آب انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135272" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
زمین‌لرزه‌‌ای به بزرگی 5 ریشتر، جنوب‌شرق ترکیه را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/135271" target="_blank">📅 09:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e21fc7be.mp4?token=FKK5XQSnUmZp8DiFLphE_LUz_U_aLB48wZxKLEHoqeH2ucKtvVE15ia62UXGSNLxMeSDaPktzbxK95RpxsQSg9BPMQKZP75Y7lG6VBIpBsIYyaYWDBR4N72_nUY1m_9QaZaDiKVOVmcS1neUEIWZgqQa74FLYswj8T7m0OHG355NNPPZHHjTq8-fOpW9NkSxuwCORE0aWACTqcsfZwliC0ABbttOeXh_qlXd6Cc9sh5RLD7qd-0DtT57XyDuhXEIlrfH0I5W_U-eqZIlb80moY52JPeR4Xh0NoQNzbw4bd56evs3Tii5YEiXJSsPJLZHjA3Z9w5Ex4wWtyNMujMfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e21fc7be.mp4?token=FKK5XQSnUmZp8DiFLphE_LUz_U_aLB48wZxKLEHoqeH2ucKtvVE15ia62UXGSNLxMeSDaPktzbxK95RpxsQSg9BPMQKZP75Y7lG6VBIpBsIYyaYWDBR4N72_nUY1m_9QaZaDiKVOVmcS1neUEIWZgqQa74FLYswj8T7m0OHG355NNPPZHHjTq8-fOpW9NkSxuwCORE0aWACTqcsfZwliC0ABbttOeXh_qlXd6Cc9sh5RLD7qd-0DtT57XyDuhXEIlrfH0I5W_U-eqZIlb80moY52JPeR4Xh0NoQNzbw4bd56evs3Tii5YEiXJSsPJLZHjA3Z9w5Ex4wWtyNMujMfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی به ثابتی میگی چرا جنوب نمیری؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/135270" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فرمانداری دزفول: به‌دلیل انجام عملیات انهدام مهمات، احتمال شنیده‌شدن صدای انفجار از ساعت ۱۰ صبح امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135269" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سنتکام پایان هفتمین شب حملات به ایران را اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135268" target="_blank">📅 09:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ونزوئلا اعلام کرد شمار قربانیان دو زمین‌لرزه ماه گذشته در این کشور از ۵۰۰۰ نفر فراتر رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/135267" target="_blank">📅 09:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
منابع رسانه‌ای از وقوع انفجارهایی در شهر الخرج عربستان سعودی گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135266" target="_blank">📅 09:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
حمله آمریکا به آب‌شیرین‌کن بونجی جاسک /۲۰ روستای ۱۰ هزار نفری بی‌آب شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135265" target="_blank">📅 09:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135262">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f6a6ca0f6.mp4?token=rQN_AhO2Bml8w8mXVJbZZpUndaRfPv4nYAxHjlY52dB5dvSEF1mZMaegYNB30X8nDweEsp4wwHWngH42I5fKrLWNgT_olNUT3in5vRtN5PzgfEDG3kv1iNj7aoEqXIoE9T-yzshBnCcPrYgkt1xNQrBSb_aotL5irbbB65ZG_aDT50gHGTS0CsHt6zxpo3MUCA8PhJELHwcVRkycbYWIEeBtYHvQyBOJ3vIMxdTbZBet3IfAOwNo8-U2wQ6L6cdTW8QZ4DVOd1PLZZVOHT0J4fIVG4tjV7tBhzALsJrV9kEhIJBhO3-rdJUhpSq5FzeTBfoksk6uEehZxUoQ3XQ84A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f6a6ca0f6.mp4?token=rQN_AhO2Bml8w8mXVJbZZpUndaRfPv4nYAxHjlY52dB5dvSEF1mZMaegYNB30X8nDweEsp4wwHWngH42I5fKrLWNgT_olNUT3in5vRtN5PzgfEDG3kv1iNj7aoEqXIoE9T-yzshBnCcPrYgkt1xNQrBSb_aotL5irbbB65ZG_aDT50gHGTS0CsHt6zxpo3MUCA8PhJELHwcVRkycbYWIEeBtYHvQyBOJ3vIMxdTbZBet3IfAOwNo8-U2wQ6L6cdTW8QZ4DVOd1PLZZVOHT0J4fIVG4tjV7tBhzALsJrV9kEhIJBhO3-rdJUhpSq5FzeTBfoksk6uEehZxUoQ3XQ84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادهای اوکراینی به انبارهای نفت در مسکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135262" target="_blank">📅 09:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135261">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRvYeymlKxhDrxCBOc1tWJXVOkTL-mzMH1Uh19m0nevFd6jjUW8kE02EC-zTCtCx4Burb5-8fCsYiPzDvOfddzrxXcVWwrnFGO09p7uqZKYyUT5MCKTt9Na2BeaxCZFi45gb_LWtazBJfdyVo_o-Xw-NTSNGGncG1v7BZNd-3x5phHw7GMEeJwaq3WNJwhBo3PB6NZMWJQG-EjyoevisVrxOSkJ_jFPOkr-5RMLw_-_bNzAqGct8IxigRbxH36yBxHC8-eIylJ5Fia_DM1E6IGS0f68Yw41gtg04voJrf1IhQVnJ_ybB3QopPWFdu14dhBQXtBT3OiyGLB5ZdnnM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان بوشهر امروز صبح
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135261" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135260">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6J780IQ0ojfLNbOkN5DGWdhG4h9H1qe6igdQk__yTa9Ic39vJzkhRiImUEGXBhfSj8WdqY0HGgCIF_CsEyEgFzZLia9NBjBZ0rVV1cDTzBVbZwZBaNQwubIBy8ANeFrB9x7PR_5m08U_BbWUXUfOq25RjCQpYP9aV5XsXqvx1p_Zy6pszI_DdzZbREgg3Ip0d_YAA0XwNxtHKg2lK4_zp7uheOgC98c4Y_T_Gc9u-1MELBN0H81uAWbHo6VgzjHCI8Sdyjgx2vIdyv7xWVTGmSypd2Tw81pRcd3C4wDztwhK3bZtNFYReAIRs-vLL0tCE1x_HouO2tLwHTGxCTTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازها به‌دلیل تداوم حملات از ورود به حریم هوایی کویت خودداری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/135260" target="_blank">📅 09:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135259">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کیهان: کشورهای عربی پایگاههای خود را برای ترور رهبر ایران در اختیار دشمن قرار دادند بنابراین باید سران آنها را در کاخ شان بمباران کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135259" target="_blank">📅 09:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135258">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام آمریکایی: ایران یک موشک بالستیک به سوی یک پایگاه آمریکایی در عربستان سعودی شلیک کرد
🔴
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135258" target="_blank">📅 09:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135257">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNJqu1VZqH9DOAG--kClV1F86TlTs3klIqVvDvGkLMPoSSYANRY_hZOHxgo8c5aTzJ54Qnl1OMrP0Gu1rdz5ktYQpjgbVmzh2CIuChURQMSe33vyOKfnjvi8IV68uzBuwJogryT1lbPSAdW-bsK5hc9aGgAQPg-REk-yFIk3Db7voMlBNJ-Uzmvby-vKcxUPFbB2PtgKYBMkj_iog5js8ofPjYqibiqVeQsuZ7alto6_qr27TYWF0lBJYrFMZ1V93t_zAksHfMjMDx1cb3AYSUvatIaDzWBMBlPeTcF0Dihjr-Ibfkx4_we7WYm99BbygSrXBEglzorho0EZhfuEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلال رشیدی کوچی: تصمیم جدی برای برخورد با جریان تندرو اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135257" target="_blank">📅 08:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5459jC3SOnAPU6k3lX4rjzS5a2u3sNqH2X7U2Fq09v7oMt7o3czh7qwtP4D6aoyr71MgEtl4dtnjyCkSN5loO9trSVgjVdICu9-_T8imGC1LfKjPEJzXw4HYhmb7NmLfLu3kqXd7XK1sww846fFMF9RUZTTUEz_OjqxUVKHcecUhVfU3e34mwFyeJrVy1qWaiflnacIA5hINmLOvT35UwSI-wJfaANkiRj2xmwySRyPjYHRdDJmXoc5dfeXhXmjAZ_p9JfPZ1IlSQ1DnZpreR2aitntmNdnPiwEswENcH5T4mjX95KklRbELAZ1wfsKJeYMsh5jdZJHuDiotFKrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی سپاه :  در ساعات گذشته ۴ کشتی متخلف با موشک و پهپاد و ۲ کشتی دیگر با برخورد به مین در مسیر جنوبی تنگه هرمز و آبهای عمان متوقف شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135256" target="_blank">📅 08:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nywx1K6ACgd4la9cdU-2WQFz_ge631mq_kC1Ap3_6X7CpbMlKpoaj75duxAkK6gMOu9knKWUroKVSiEtsGiVwMXgzdKXFJDqxlUX27cZOWeRDkdyAMLcSGGzptTbRihwJ-C2_xk5xKCeyRwHWVVJiRA5wHZHaBz7hpmjFrnyg18Vfo7VQ1CEJftVy2CbAiUk5OcVoeE5unUt5PZ4mmj4C8EKwgjdxFBo_40nFe203JvMGJtptUUZSiWNc4ndLH-9ws1o1O-UZfVenV3Lb64FYFDYD2oBOXRJQft2oUTV9kJ1NbHsdZ8t0hVr1oNAIF3aLdwDBqLIaTv153LwfY0kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صداوسیما: هدف ترامپ از امضای تفاهم‌نامه بازگشایی مجدد تنگه‌هرمز بود.
🔴
شخصی که تفاهم‌نامه را امضا کرد باید به این تفاهم و موارد آن شک می‌کرد، این تفاهم نبود سوءتفاهم بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135255" target="_blank">📅 08:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d51a50d3.mp4?token=u2DV_gLw27FSV1pBCiCpL3konI9T3C7bBcNGzBroNZ4Vfb840dfS7OkIWKWZmOlh4QZDrZXYLAS8ORlh8IhZ8HKYirOoiept3M2NMEM0o13sYDZ6ARqU3mL1S-WtVJXhyWSSCewGwCeUGxyF8S-5WLzjgq5vyHRjEMOvQwaJUBOh6n-Ym4P2TkIfA3ofarDJ-TDlV4mAbwWj7WxdwZqSPNC-Ez3yGmYVkPRbyz3TevdRRgnRDocr0B1tFmuHd1s-FTr7ksBoQOaW2FNbdYMkr8N848_uXc7BH_ZWM8EdplCeRPqHt_dCALfl_flnA4YR9qqEPTKSN5sPbCsEty5WTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d51a50d3.mp4?token=u2DV_gLw27FSV1pBCiCpL3konI9T3C7bBcNGzBroNZ4Vfb840dfS7OkIWKWZmOlh4QZDrZXYLAS8ORlh8IhZ8HKYirOoiept3M2NMEM0o13sYDZ6ARqU3mL1S-WtVJXhyWSSCewGwCeUGxyF8S-5WLzjgq5vyHRjEMOvQwaJUBOh6n-Ym4P2TkIfA3ofarDJ-TDlV4mAbwWj7WxdwZqSPNC-Ez3yGmYVkPRbyz3TevdRRgnRDocr0B1tFmuHd1s-FTr7ksBoQOaW2FNbdYMkr8N848_uXc7BH_ZWM8EdplCeRPqHt_dCALfl_flnA4YR9qqEPTKSN5sPbCsEty5WTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود ناشی از حملات به کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135254" target="_blank">📅 08:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رئیس پلیس راه راهور فراجا:
بخشی ازمسیرهای خروجی هرمزگان به مقصد فارس وکرمان موقتاً بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135253" target="_blank">📅 08:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه : تاسیسات نظامی آمریکا در کویت را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135252" target="_blank">📅 08:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
انفجارهای جدید در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135251" target="_blank">📅 08:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XH8IM20yFNLxfeaGrtWyaa0lUvJf9GqTKPEOKBhUdOAMtY-oBA-4Xxtlh9aBIqr0Te6NGa54fro13VX2xbZUrKuCp8UwwZ2BZsem-O_AbrpxVxfeihXFVwys0ep0tYAC5ib4gGLFZCtlgGF0m1AgKNPEsAx-lUqBc2nrIgMKOTFE3q0G5VnJgE9njyyUOlybBySd8UpmrBVFXuxXrqzZ04t7_PM6JwCgOeNOJO7JtTTOZ7GzFqhYL4MvMrZUtTOhmWRtPMUs0xfmZ-flzA3f6mMyJbpWwyR0i0ku5xIv0AyW5v2pA1-tQHgEWtOvm5z129UQfkYAdqlm2Q0sFiOiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9V4vDhd2hA2o-lT-ouB9Q5k9nADWkkVhck7gLNENMBfoL5s1AbErT_JafqZz-L9i8DlLzJEHG0OQnuZKWmuMXYxIDVU2ot2xM0rLAsQcwMrf9AvSHxR9oukOaJxz4zZvfL1GGT6jIEbU5-XJ95gC2VYtPSFYPrvcxBRuWxAg3Of3FlbF_BB0aKH46ecamiGWwkmPiKbeu2t4jSRLNHHZ9apGEskdJlffwN3STxQe8Uf1gqeLN1XOMrOWCCKQ3gC8Dqgt8AeSQ3yTYCcz8mKDXwBjXVwJITT5qAoGRSLa5tUyK76wsVQtxcHJwTvtXAJZOZj2wccpFYE_gocjPnClA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اصابت مستقیم به اهدافی در کویت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135249" target="_blank">📅 08:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/135248" target="_blank">📅 04:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در لرستان و جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/135247" target="_blank">📅 04:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انفجار در جزیره لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/135246" target="_blank">📅 03:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انفجار در جزیره خارگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/135245" target="_blank">📅 03:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حمله آمریکا به جزیره لارک به یک دکل مرکز کنترل ترافیک دریایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/alonews/135244" target="_blank">📅 03:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf49d074e.mp4?token=b_yCtM84aF5HQnRxcvEN9OHh2bz5fd7R55w7x4RcbXFa88-tpqsf0WmhDgIVpcORhL4PFdPadeUDj_ZUghOncJpLwYh0xOOMBAl3qgqiq1f4mA61sN3YSd5EMDwz-YXvkUWeT00oa_DK39rVUkw6uid9Zf9wmMM-KQYTE7tf2qwtHAuTpnsBLGZny4ARLhIQ1cpfVnW3oeB25Rinfdwmmq4Wi1E97e0yRlWvGOdQEmG3U77v9kALz_ogVhzo7m7xUJrGT69BtS9F1IwO1rxQI_lpiG3Il2oovyFMR1vaSWHN4AutZdlq1apZ2y_IaCYSf6Oh2NXUsZjzVf0IFszrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf49d074e.mp4?token=b_yCtM84aF5HQnRxcvEN9OHh2bz5fd7R55w7x4RcbXFa88-tpqsf0WmhDgIVpcORhL4PFdPadeUDj_ZUghOncJpLwYh0xOOMBAl3qgqiq1f4mA61sN3YSd5EMDwz-YXvkUWeT00oa_DK39rVUkw6uid9Zf9wmMM-KQYTE7tf2qwtHAuTpnsBLGZny4ARLhIQ1cpfVnW3oeB25Rinfdwmmq4Wi1E97e0yRlWvGOdQEmG3U77v9kALz_ogVhzo7m7xUJrGT69BtS9F1IwO1rxQI_lpiG3Il2oovyFMR1vaSWHN4AutZdlq1apZ2y_IaCYSf6Oh2NXUsZjzVf0IFszrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت دو موشک‌ به پایگاه موفق السلطی اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/135243" target="_blank">📅 03:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
صنایع دفاع و شهر موشکی در یزد بمباران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/135242" target="_blank">📅 03:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجارهای پی در پی در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/135241" target="_blank">📅 03:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/135239" target="_blank">📅 02:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پدافند اردن فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/135238" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اکسیوس:
ایران امشب یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد.
🔴
این اولین حمله مستقیم ایران به عربستان در چهار ماه گذشته هست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/135237" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/135236" target="_blank">📅 02:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/شلیک موشک از ارومیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/135235" target="_blank">📅 02:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/حمله به پایگاه شاهزاده سلطان عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/alonews/135234" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLvkoXaJIoUQ5Ufpbgf_252uzpTXYcYMlqyUcputFj9XuJNJzd5FtavF7ndzaDAtP3XQ1mTOUZLmvkHMEcxWtg-iT4nMof0HYIg9k_0-L2JLlxv5gIXjk7ry2oBadcghFvtM3sxZHF4CpSQwGHNYwAcljMJMCYWLY0aaLR7b8tyQH-DY7zQHWX8oi9buE4Yu0PgfrGudJ8n_F-1D0EqeLl6tAop3bdG2hKdbZWQoB5J3Ur82eZ5ruz51DX8QkrgJnltB3r_KD-x1uJ3e-24ePPsQTN242vCwIW_hYPw0p0T_Lm9MDDDP6hOD8o2RXiwC_vNfREiQ8zjE6YYK__iJJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/حملات موشکی به عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/135233" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بندر عباس از سه طرف از تمام شهرهای اطراف جدا شده و هم اکنون هیچ راه زمینی‌ای به اطراف نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/135232" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhDIydGuVovPz9zdnaxYTLiLiKz5zIPhJ3emqSUhgb4afudTID71Ps-WjxsMUQMsOTm0pdzn_YU97vEe2dbPPD_sq9bIlU5KxO1siM7DYKsPMxjBFBDThrkS50LdU0qimeGJztbRTJfeq-0zIRdT1iXUxWgmvhFUYX8d2qBeetkC5QOyUdsrXfNHDZdIJZV5u-7l7Q2oj42TKSQnTzdgKmqx9HOk3ErwI25PJ1iS6qXG1PgRriLCahV7yP5wk8XppPS-EYZGM3AbYxaD8MLb3bhwW6BZpiEznAE_1AOeIwVjWnhsqdT18cp8ESTdauiSJEZnqRNBy2h9FV69ThYhlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعيت پل سه‌راه‌ میناب به‌سمت رودان
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/135231" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/شلیک موشک از لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/135230" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/135229" target="_blank">📅 02:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/لحظاتی پیش پل استراتژیک و ترانزیتی واقع بر روی رودخانه شور،
در مسیر بندرعباس به سیرجان نیز بمباران و تخریب شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/135228" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
از ترامپ بعید نیست یهو بیاد بگه بندرعباس ایالت ۵۱ام آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/135227" target="_blank">📅 02:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/135226" target="_blank">📅 02:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/امشب 3تا پل تو بندرعباس نابود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/135224" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/به تونل شهید میرزایی بندرعباس هم‌حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/135223" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnAsvQYc6LYy1IepGhEfbNKfFVJlvcSSiETcGtv4XBEX5eFsUWknNizDzaKCDUKvpQSYaS9zPSdQL3qKQKuMPGA2rLFesDYGWob99DNLETOfJXBzQEwHeFxY-ByB8dMvXS5uYxI0lVht58smI9R0zb6c6obPoQshZovMWvRnTJIBRHal6rABtr3EwbyFJCNcgbqR4JwQdV_f-gCgsL_bMpqPgT9PnOEGn3YYqrBuf0V1jESA6LtBTnvmXdjVFAZ4dHxR2qUr6P_aJeLJwR59hbf72VVSudk0gUmuh6FtddkhDmwbOIBuWH0AyW3kLTai8_NEtldAa064qCHXNtYFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/پل مسیر بندرعباس/ رودان هدف قرار گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/135222" target="_blank">📅 01:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حملات به شهرهای جنوبی همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/135221" target="_blank">📅 01:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هرکی از این خایمال بدش میاد لایک‌کنه
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/135220" target="_blank">📅 01:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">ترامپ درباره قلعه نویی: اون مربی بزرگی هست و تنها مربی‌ای که نباخته
@AloSport</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/135219" target="_blank">📅 01:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/135218" target="_blank">📅 01:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بندرعباس برج رادیویی رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/135217" target="_blank">📅 01:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5uIXqouGSYekamrILgUlqIndpcHLLeX_KPAq8XN1JB92c2t_TGe6r0hW9hnU8xP4iw1GEzkSbXFFSR66IMNurVBOk7DBBYoNMNXaQxY3SAnlTTS_fAzhAg9NnVicuJP-1UoauYbbhoKPd673WTOnTi3eZzbE-LwYyVC_3BZ9cppZXsLbKWpRtcuWWtwO4W_FukF7Oo41BGIZqVm69EWF-QuU3fUGrG6RfYyZnSkL7BQ5hDkHisIo2o6iNIu9ocSB2oK9TwC98Ozc7SA_rhy-gA06UGXUF3DKNZpVYrgNqt2KziQEdZMDdC1Lq46qfPM06pRmtEPAoxldnR0X1l4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه مادر جاویدنام سامان ابراهیم پور که پسرش ۱۹ دی ماه در رشت جاویدنام شد، بعد از ۶ ماه تحمل درد از دوری پسرش، امروز خودکشی کرد و به زندگیش پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/135216" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/شنیده شدن صدای جنگنده در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/135215" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/ سپاه:
دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/135214" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرنگار: به نظرتون کی قهرمان میشه؟
🔴
ترامپ:
به نظرم ایران نباید سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/135213" target="_blank">📅 01:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CZMBOw7P4nhzp-nGU8m2nGKGMrhTkEcswyaJrg3hgx5pB1T1boTZsZ6W882q80muJp8Rdz9duuJmZmO7uEFMmSGDlIJ_C8bxDh8wTJNLZ_p3OuP8Hxr8uHeLi1GjOXaECIugW1vznH3OY-GkSv6FYs0o_L0Y7e4TDXtpV3ayeXGe0Cr5mU1oiLEj2gLfitys3SGjxF3BvGrwhiS9TTQTsir1tgEbgKX3aXN33DXJMSZBj_hr_MPa9zhAjKBazRtg54sKDR5zDPJWP58DyB5-U-iPZipixRAIUeeLA-3jX8P0gVRh1kdCaLD9nvYgEfd9AO6yXr3-zTjCDL9-l1ewNQgq31MhkS3dOTlJ-v6cV7OABmB2JWaULnUnjJnAcYaTsbfpmoQ85JZTbXabkn5RWbC7kSphElsFH8cMs75jOsrnx65v-PSFiswNhcxPZ7G4wXDeavxJt-YnX_LagsITQvtBf2xOMghUSsX4OEb-SN2qqj3yWZX_eVOFCLTu9dj7azb-PlfI3O_c9_FUcikyn9Zw5ZROAlOQia5P9xMPrLWs7Pdxa3KUm6c0rIQl5d4MReBS9LzfZ1qmMWe4GKIcQ25KokCF88ra1rFJ_Y21oGpJIDmD-oKXw5QuGJkrKPlql07C-k-Gq2C2co3YqShMZnbT2eY_biKeSUCwWGFIzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CZMBOw7P4nhzp-nGU8m2nGKGMrhTkEcswyaJrg3hgx5pB1T1boTZsZ6W882q80muJp8Rdz9duuJmZmO7uEFMmSGDlIJ_C8bxDh8wTJNLZ_p3OuP8Hxr8uHeLi1GjOXaECIugW1vznH3OY-GkSv6FYs0o_L0Y7e4TDXtpV3ayeXGe0Cr5mU1oiLEj2gLfitys3SGjxF3BvGrwhiS9TTQTsir1tgEbgKX3aXN33DXJMSZBj_hr_MPa9zhAjKBazRtg54sKDR5zDPJWP58DyB5-U-iPZipixRAIUeeLA-3jX8P0gVRh1kdCaLD9nvYgEfd9AO6yXr3-zTjCDL9-l1ewNQgq31MhkS3dOTlJ-v6cV7OABmB2JWaULnUnjJnAcYaTsbfpmoQ85JZTbXabkn5RWbC7kSphElsFH8cMs75jOsrnx65v-PSFiswNhcxPZ7G4wXDeavxJt-YnX_LagsITQvtBf2xOMghUSsX4OEb-SN2qqj3yWZX_eVOFCLTu9dj7azb-PlfI3O_c9_FUcikyn9Zw5ZROAlOQia5P9xMPrLWs7Pdxa3KUm6c0rIQl5d4MReBS9LzfZ1qmMWe4GKIcQ25KokCF88ra1rFJ_Y21oGpJIDmD-oKXw5QuGJkrKPlql07C-k-Gq2C2co3YqShMZnbT2eY_biKeSUCwWGFIzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیونل مسی
: مسی به‌خوبی مهار شده بود، اما ناگهان خودش را در سمت راست زمین پیدا کرد، در حالی که مدافع بزرگی که مأمور مهار او بود فقط همان‌جا ایستاده بود.
مسی ضربش را زد و همان گل، کار بازی را تمام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/135212" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_h4DWnjr9OVlcYkowILBSh-n6d8zSotizpv23RS7HPaeUrdhJ-IIwwO_DbX76kbXCQUqWN9lpscqqSGfYRYpYnBrtQmiVxOLaXyRFFdzdHYseBBNaXzUcmLD79HvT1C93ZACwQqosgt4lticBU4otg8p7hdMRoiKCl8ubwlPMr1Tnphn3e1sV76OVIwSBBop3pURx-wpP79nzoMt60aVq_HIOXEziiHfgflxUKh6XgnRP3J-NgiQfmLekKjvIbqBPRTvP1_X93vyz608qX22w9ZcIbul3Jblw85w_ciQb-yZ3FDU302QxMwasonVnecTXdaVjo-3FGl00txOnfrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
بنظرم حق ماست که یکبار دیگه میزبان جام جهانی بشیم، ولی ایندفعه کانادا و مکزیک رو قاطی نکنید.
🔴
در عوض با چین میزبان مشترک بشیم؛ بین هر بازی یه سفر دلپذیر یک روزه بین دو کشور خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/135211" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/حمله موشکی به داراب فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/135210" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4df16a59.mp4?token=VYOmgM4UKvzDwJZcuRt0U0bzLafKWqVYQuS-2IWaCWUFEMsG2iRsCIe6OQ8sCUyep66UxXU7UsPv4V2oUGTwuczeN_PwnzIOdnyc6soPTkEf5IBUAj85mzLaI322xA_VQBAsEJDHYMFI2dWrH9ot0MmSqs7sj0xFb3Nb2GpoYop2EmQnU288DqE9jiEtY3j9o6E5_P0qXoEt0BDFCy3bmomPIcCz5-w-MnQfRTpahmreX24lK0_tWq8-fxLVDxLzVt2xpvd2DEqzum9bqkxfj-zaYeFEFMNtsXdxTCAUea4pcZPRP5K9TC-E66fy74hQ_EXIx_4S_DZE1AGL-GC1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4df16a59.mp4?token=VYOmgM4UKvzDwJZcuRt0U0bzLafKWqVYQuS-2IWaCWUFEMsG2iRsCIe6OQ8sCUyep66UxXU7UsPv4V2oUGTwuczeN_PwnzIOdnyc6soPTkEf5IBUAj85mzLaI322xA_VQBAsEJDHYMFI2dWrH9ot0MmSqs7sj0xFb3Nb2GpoYop2EmQnU288DqE9jiEtY3j9o6E5_P0qXoEt0BDFCy3bmomPIcCz5-w-MnQfRTpahmreX24lK0_tWq8-fxLVDxLzVt2xpvd2DEqzum9bqkxfj-zaYeFEFMNtsXdxTCAUea4pcZPRP5K9TC-E66fy74hQ_EXIx_4S_DZE1AGL-GC1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پلیس به جشن هواداران تروریست نساجی مازندران
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/135209" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/حمله مجدد به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/135208" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KsvbQ4IZvEKiypftPan3lLx8TDJ8uIlL9tUEXgtwsAXA-xIP8WOIdJ2yn-BHPB9DlTY5F2laAUVOX-duAhAlJB-3Bayeo2OcaQKrC-o0VTN9opzX6Wqe12MFNztzRigRq-zfdFVMpCe5Lq58MSayJteMmZsjOBqvqULfsMN7Z6i9MnuWajqKJ7H1QvToiS52twpmVBKwsV2MxuMhtgzkkbDtW2USSYcug3JTag6Z1E_p-OM6xwPdxTG80Of4_ZovQAoYuBwzKm8we_cGjGFbsn_6A0DJbIsn58GvdQGAhSWghStkbfwpqMGAA5Ya7Ga49bngzuAf-KovyVl1qHHdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KsvbQ4IZvEKiypftPan3lLx8TDJ8uIlL9tUEXgtwsAXA-xIP8WOIdJ2yn-BHPB9DlTY5F2laAUVOX-duAhAlJB-3Bayeo2OcaQKrC-o0VTN9opzX6Wqe12MFNztzRigRq-zfdFVMpCe5Lq58MSayJteMmZsjOBqvqULfsMN7Z6i9MnuWajqKJ7H1QvToiS52twpmVBKwsV2MxuMhtgzkkbDtW2USSYcug3JTag6Z1E_p-OM6xwPdxTG80Of4_ZovQAoYuBwzKm8we_cGjGFbsn_6A0DJbIsn58GvdQGAhSWghStkbfwpqMGAA5Ya7Ga49bngzuAf-KovyVl1qHHdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/135207" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
به اربیل عراق حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/135206" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f5bfc22.mp4?token=bjJEM9XM_Mr7P95ca-5FR4hQi5RKi6m3SxOBWxRQ73p4r8r_VeSzS4k7WijBfHSIGLo--Ut8l5iuKVF_75IGUQI0MMKDcnz0v7Qd5AG5pPtBGXu9TMXj7nzqVAuQI6Btx7I4xaMvshhkFrzAtX1o204p-kkjDqear0fjNPLNwfD_zHFWWMh5NwssxEOqYzMTQ8eEAyuIQpginpwyAY5s1xY9eQM7kk4rl2krnFHa0P7mJiCSOI_nLg_8BpVgawaEJWoHyMtlJyUwB41SQKjAYJsFqa7keuuQDD1pMmVofPRL1n4YDYCT7JDN_5AcXYXQkvv_gtUr46ssEmwpKpmP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f5bfc22.mp4?token=bjJEM9XM_Mr7P95ca-5FR4hQi5RKi6m3SxOBWxRQ73p4r8r_VeSzS4k7WijBfHSIGLo--Ut8l5iuKVF_75IGUQI0MMKDcnz0v7Qd5AG5pPtBGXu9TMXj7nzqVAuQI6Btx7I4xaMvshhkFrzAtX1o204p-kkjDqear0fjNPLNwfD_zHFWWMh5NwssxEOqYzMTQ8eEAyuIQpginpwyAY5s1xY9eQM7kk4rl2krnFHa0P7mJiCSOI_nLg_8BpVgawaEJWoHyMtlJyUwB41SQKjAYJsFqa7keuuQDD1pMmVofPRL1n4YDYCT7JDN_5AcXYXQkvv_gtUr46ssEmwpKpmP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی سریال مختار از وضع فعلی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/135205" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ممد نبودی ببینی با گنده گوزی یه سریا جنوب هرشب زیر موشکه.....
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/135204" target="_blank">📅 01:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
امشب بازم دارن جاده‌ها رو میزنن. اینبار حملات سنگین به جاده‌های جنوب غربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/135203" target="_blank">📅 01:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/به جاده اهواز_اندیمشک حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/135202" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">💢
خبر فووووری/4000تفنگدار دیگه عازم خاورمیانه شدن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/135201" target="_blank">📅 01:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/برخی گزارشات خبر از هدف قرار گرفتن تیپ ۳۳ المهدی در جهرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/135200" target="_blank">📅 01:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/135199" target="_blank">📅 01:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش‌ها از حمله به سایت موشکی یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/135198" target="_blank">📅 00:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ایران اینترنشنال:
یه گزارش محرمانه که برای دفتر پزشکیان تهیه شده نشون میده فقط ۹ درصد مردم ایران موافق ادامه وضع فعلی‌ هسنن.
۵۳ درصد خواهان اصلاحات اساسی
و ساختارین و بیش از ۱۹ درصد هم میخوان کل نظام سیاسی عوض بشه.
طبق این گزارش حدود ۶۴ درصد مردم دائماً عصبانین؛ ۸۱ درصد برای تأمین غذا مشکل دارن و اعتماد بخش بزرگی از جامعه به نهادهای حکومتی از بین رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/135197" target="_blank">📅 00:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135196">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/99d23f8757.mp4?token=GTUlQRVCZJAjG9O_17yL5DvC9-UimYe05LtRYJEQgnYHwBoPr-tnzK6FjIpy7V3XduTlPzSdXnWbR_UDN0AFDRsSLtV3izSIntg5vWu3PU0Do03qCoBDGsJqD3yZnmnetAdVpytLQzh6dtkImMeYi-qEEFggNisN6lwZ6e0G2zM_alzyQMIGy4xBkpC2Pim7gVZib_iiFXXOUVuRMrdU9KyUmAgvFxJ50X480X6_xDhzGAlg0Y-ThG6H1oc1m2RIGDgLLeqtZbAakUhOWPlPVK5YGD2dj7q7_a-_4HA-TVAG-BwajA0GZRfbBdpTZIPTArAH8n2ZrFTPShXotmySpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/99d23f8757.mp4?token=GTUlQRVCZJAjG9O_17yL5DvC9-UimYe05LtRYJEQgnYHwBoPr-tnzK6FjIpy7V3XduTlPzSdXnWbR_UDN0AFDRsSLtV3izSIntg5vWu3PU0Do03qCoBDGsJqD3yZnmnetAdVpytLQzh6dtkImMeYi-qEEFggNisN6lwZ6e0G2zM_alzyQMIGy4xBkpC2Pim7gVZib_iiFXXOUVuRMrdU9KyUmAgvFxJ50X480X6_xDhzGAlg0Y-ThG6H1oc1m2RIGDgLLeqtZbAakUhOWPlPVK5YGD2dj7q7_a-_4HA-TVAG-BwajA0GZRfbBdpTZIPTArAH8n2ZrFTPShXotmySpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/alonews/135196" target="_blank">📅 00:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135195">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl_U_k9rgs9a1XGwKEtJvO6b6YZlh16ZKY2VRgTvC_M6X8iEPXAtQIsIY_ob5iiWhlP0Waljy5dCSAnygZQZ7uHcjp0-wGJvKOMbOwo_Ft4QYOTV9K60NBQA_awDaFjUSQImHmd6gsglAoaMnC5OLPfq9OfgtfpK03O84Rz_9mQnXg-mXpd1SrDux512ZxpR_8NxSXtl3J0oOJwQJY7Lso01teFBDIC_07qe_G_hB_FGyqa4Tlem2UDW0hZLOYN2ijXsQUNS2nRPfgAh3jaM4LOFvHhdsZ7gKOK_LNro12lI_-RcH-RXWMwLtUGvkFm1_LRHqazfU2Fyrfi2GgP7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/135195" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
محسن رضایی: فعلا به دیپلماسی فرصت دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/135194" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135193">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جنگ تقریبا به مرکز ایران رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/alonews/135193" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/۵ انفجار در یزد گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/135192" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/135191" target="_blank">📅 00:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=Mq0pfv8eqLqLxkFMxUQo2IkuGR-DTYlZeF_sP7LgEVwM6bIjJiT72PD951TL8g_XHg9oL_jU3SAMV40p9WAHbKHXkwBgcugnV3sQFUzzUVB5_EUhDeR802vq1Ho8B0g1__o1ARVz8PyEbhVARWLyx4VPuBgt_gsX9DeLMbAJyOaUBk-XnvEL6gDelxD7A6ZNwRLxCAO2enHsjKnos_xNYfcesRiNfFDQ7oyASOBp-s2BVqYDlBKYjGsf9yLdcY77jOrYTISDKpTrkZskvHseIZQ2z7ONTwXPHA4Y_O6K-BpV_-UAgpSsFoo6mPbipnmLyheqvHFuHSq3QMdLKElqsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=Mq0pfv8eqLqLxkFMxUQo2IkuGR-DTYlZeF_sP7LgEVwM6bIjJiT72PD951TL8g_XHg9oL_jU3SAMV40p9WAHbKHXkwBgcugnV3sQFUzzUVB5_EUhDeR802vq1Ho8B0g1__o1ARVz8PyEbhVARWLyx4VPuBgt_gsX9DeLMbAJyOaUBk-XnvEL6gDelxD7A6ZNwRLxCAO2enHsjKnos_xNYfcesRiNfFDQ7oyASOBp-s2BVqYDlBKYjGsf9yLdcY77jOrYTISDKpTrkZskvHseIZQ2z7ONTwXPHA4Y_O6K-BpV_-UAgpSsFoo6mPbipnmLyheqvHFuHSq3QMdLKElqsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک آمریکایی به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/135190" target="_blank">📅 00:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135189">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
طرف داره با موشک تاماهاک و بمب‌های سنگین میزنه بعد یه سریا میگن پرتابه! مگه تفنگ ساچمه‌ای هست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/135189" target="_blank">📅 00:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135188">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYECPPcAx7GdiET_MJLVSbPRs0MLDqnVN34DQK59XdO-EyBoX1exGyq8KTvWsiuKjhIWyJhB5WlBYOJTsaT2hMxLFX8_CSPtWe3OUiHQQ6ZEAatwCJ7cRtKTjHld_9XVYKp-guPy6lDNI6S-c4obuiJmkq1bbmiGozuJJ6pg1hZ2i3BEC6rO0UYTG-e7jsZxHwGd9UQUvCa9hZNYyI2UmPKrXfhnfEfg5yn4mNXiIrFms2g8HhrCR4BiQ70iMcr1jJjWiIDkwHh3Ov4zkgBaUwR7ohKWzePuWVumuIwJMYl8Jrv5dXGV78qYq3HloZB_6YGQSFrzn4-uYqoNnznqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت عراق رسما مجوز فعالیت شرکت استارلینک در عراق را امضا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/135188" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135187">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به حوالی سیریک هیچ مصدوم و یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/135187" target="_blank">📅 00:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135186">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آمریکا هر شب داره بوشهر رو میزنه و فرماندار این شهر هم هر شب تکذیب میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/135186" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9o7fXPbbwRfFfFj6LwpzbCOk2vqYFST8hgSZA4BfaMmjm8eYDOPWn1anOYRSG0Lej1uK2jPIb4PdI27GcEBW2KXAfL9hpLyQvyw7gDi_DR3v7-79PuXPaQNm2sXidOhKHjgoWg9GI6vY8kMVflYhDaOd6gTgE-15MWC-OGZVqi3y-Eja8XRkqOshwntlo816xMpO8A9-KPLrHFk7PZLUfe_BQGMoQy0VtXVsSYJyARWroQLqN-1mXpcgtHniJPQoX2DZQn9HSqkZhbYxTTVJ7-Xv79eksHjPSMY90QLZvSkMUfHa19AdOnHrvIDoOdeLurI2VH7rsG9dYXpeo0huQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZRpb27b5pOBD2gRj1f9zz54vS_WN1tucFpY--lew1Ps6yL6dUctnFKI4EorvvAujycGsSOEiUGi6Q4hevHDWrn4WNRAPwZJnToU-WxAursD1UTSi8LFvZMYs-pmhLcpz5wvuYzGassFvL3BdOie2W6yRmArT1grsxJAns9Ufm7nnzTb17WZuS9cdWGLhUI6yaL0Ka425ZLjoZxDW95JmbJpyyrwj6f42lWvHmoSPGYrTRz32sJky8TZ0nzGWPnsutpYv2hGHHoeMHfDZFL2ckMTS3H293atr7MM157elHVV55XNhRi3erytSZ_aMF9MINhz0v8smDpoqGLnpGu79g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکسی که با کپشن انفجار در اهواز تو رسانه ها داره پخش میشه فیک نیوزه
❌
عکس مربوط به غزه‌س
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/135184" target="_blank">📅 00:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آمریکا از توافق عراق و سوریه برای بازسازی و احیای خط لوله انتقال نفت استقبال کرد؛ ظرفیت این خط لوله روزانه به دو میلیون بشکه در روز خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135183" target="_blank">📅 00:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe4f4684a.mp4?token=uLNQOJb5di1JHPQbFs3quUxOSe4Jh7RiXvcFeF7aU7xBF4ntoLZ5OMdTwNlkaBuaEyOwXEa8AahyX5-X_UGwAWFF37BUFXPxhj8juryDAU1aj9Ui1DrPphtdYpvco5B994vx57lUQUGP1qaCF7gpnOr0lryayoj2HzbKDCtI7vQlMmPioQcHGOQrBW5QUzZ7njKRhP9wqfZmJXNS6-DIDtZxcy2ewQ84Iy2zDdhXaJwANiCxvdJBbueU70hLa8aIRFph_oHyFd-pEGL6FNq3QZ0DkB2qdmH4FOt71y-bF_UcCzZW-cxL-FfiBiOUvreBW0U93o8ud5692C3fHZiHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe4f4684a.mp4?token=uLNQOJb5di1JHPQbFs3quUxOSe4Jh7RiXvcFeF7aU7xBF4ntoLZ5OMdTwNlkaBuaEyOwXEa8AahyX5-X_UGwAWFF37BUFXPxhj8juryDAU1aj9Ui1DrPphtdYpvco5B994vx57lUQUGP1qaCF7gpnOr0lryayoj2HzbKDCtI7vQlMmPioQcHGOQrBW5QUzZ7njKRhP9wqfZmJXNS6-DIDtZxcy2ewQ84Iy2zDdhXaJwANiCxvdJBbueU70hLa8aIRFph_oHyFd-pEGL6FNq3QZ0DkB2qdmH4FOt71y-bF_UcCzZW-cxL-FfiBiOUvreBW0U93o8ud5692C3fHZiHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
دل‌تنگی دختر جاویدنام
#مجید_جمشیدی_گهروئی
برای پدرش.
🔴
لعنت به حکومت اسلامی، لعنت به نسل ۵۷ و لعنت به حرام زاده های حکومتی که چه به روزگار ما و بچه های این سرزمین  آوردن.</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/135182" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eLOalQj7S3RYFY62wwCrFR8WaVI1rSph2Y8FTy47Ta5ZGxGquZ8aeoFLkT0puLNLghgwAE5NU06p96fx6-Y2qzvh8mJmPbmGrfzNJdI6Y7Mfadk0s9K9oq5Sm2YkLcolgIhpBssnCHTVEB6Yl2_yV07eBEMcc7DmP_q1f_YRWAjlfMAkaYIM9ISJrQqcOAG2H1XeXKUkIItHUm4vtCPJsZdRcOd8TOyP-0l5DbK4a0l0Nqz8owyMMgbkuYNJHdRLJzEwfRAuN7jlqDx7Wc0nulsZCaZUXpF7xLJjlTzM_6ezOwIVjoRmh34GaFIKkpbPhbqiDKxgF6_8xJYbUaU5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی کنسرت جدید BTS، این شکلی یاد جاوید نام‌های ایران رو زنده نگه داشتن و به نمایش درآوردن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/135181" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚫
مشاهده برای زیر 18سال ممنوع!  ساسی عکس فوق العاده
🫦
از حضوز آرام همسر سپهر حیدری اسطوره پرسپولیس تو خونه خودش منتشر کرده
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/135180" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش انفجار در لار، استان فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/135179" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDytmcqE3S0pISGsaUw68PsmBS8kuXp-aYxbpbDKD4eetDXbECSsXcLfgsHyLj4LVpTjXOPYOU4g8L4PnbFhgQwKo1bj65iOUH-8f489OlJz_b-AN_oQZNUBD7bgyfph7tO8QyHv6Bd_LKayr6yFju4gyvrZcG1Qf9yxZ5Bgzp7XlW3mOKq8i3MT8tfkCd82icrJr0ZMYgABkisC351s77ACmuAB-4CzKx3Q0nZJGPtXePQ_5qHf3tfqrCaoSyx-8WRxhnVTGej_1Q8jdE0QLmAnSubYoDXd8uKZ5mQVOGKCzqixUjf4du4Vm0-4yRiKNlWNIGG4VPuDCDLx3c70cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال:
آمریکا اگه زمینی بیاد، راه فرار نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/alonews/135178" target="_blank">📅 00:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZadPHAc8zgzI_94OwcDyxheIYktSNdYmYEKPbMNJXUV8cuuFBCSACmNPeLYRI0qf41l7WjbGsLjf8kVmeS3S-uVvegVd_4vfDxoJMSfSZFiMfiSrruL-f-eFOc2NddTZlYCpqJ6YdpKk0diYnOyZ1iLlBfvJU6YqNVqk2Y7SwicwC6MdUI2SZ3DicMe1p5Iq83WSf_j-cdR5vlx6VO_OZUu8WeZY2sBa1DBE5gkAIvhs1Seeb6SdgaYQ4orcC00w0iNrlen0OePVfv0riUOkGN9ED5E93b93ZTiaBOOZL70k11jzD_unPbTnGH5SrYuQOz429QXictqd-FzHopqhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرکی از این خایمال بدش میاد لایک‌کنه
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/135177" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کوچی، رئیس کمیسیون عمران:
از این به بعد اگه ۱ پل مارو بزنن، ۲ تا پل ازشون میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/alonews/135176" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مهر:  شنیده شدن صدای انفجار در بوشهر، قشم و سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/135175" target="_blank">📅 23:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/سپاه خورموج و اهواز مورد هدف موشکی قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/135174" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
