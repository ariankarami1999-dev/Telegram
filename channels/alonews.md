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
<img src="https://cdn4.telesco.pe/file/PvYZJF6_lG48crPabzVY03ab2gZcegIEUR9H7JAYXvU6XTGpqwfNqRDH785Y0y215X2klCtzRwDYmguNEgXASB4zEd-SFYet2Rx5tiXLOjsZSbu70iAsSlY3KeWT5cAonlDS0gMO-24vNuZBYdofTwzV6Y3G37cpJNQk5KrIntKM2j_mZJJBOty6bFYLOHmkWsqxlkRtbQrbZTMj3-VOdzr8BZ3pn2nJFB41JpZReKDWhB-8-31EbmojADQRoptUVSO1qWoHLQ-Xm8ucJjwqdvMjsoK72dOMLc8l8kKNj-OgGfM6CD9kLYmpNB_agMumdLYTIR7r5WGkYCglSOfaqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 927K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-146278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=R45Eg36aPRHukpxGYdBgq7gBHxWwbsoRkjnYUDihCOermW-_9GFM5AsEK3c9SePMWwM_zk-6D-GHEutk1OyxejMHLgNK2U0Yf6hwZ3qUNlFqGPmrgph11t0BORqdXtLaBglOQeJx-FzaRS9bXa51CVGOkZsXGVjGYKGDvWUbtPPIzzsXpD-jwzgYcukksyu5sj9WnVG900huRzk-Gmzcxv05zfrp2VcwLTIP8LKD80ecLLzUA9tNS-6QdfwEJ-WJ6m1JfqJ1I_Q6L3j53CWGZ3s6zKCttptHDblCt5DIYBXLQmktMaDZHVI7SmhCWjMp9DyBSSs-Pq_WM_3X04BJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=R45Eg36aPRHukpxGYdBgq7gBHxWwbsoRkjnYUDihCOermW-_9GFM5AsEK3c9SePMWwM_zk-6D-GHEutk1OyxejMHLgNK2U0Yf6hwZ3qUNlFqGPmrgph11t0BORqdXtLaBglOQeJx-FzaRS9bXa51CVGOkZsXGVjGYKGDvWUbtPPIzzsXpD-jwzgYcukksyu5sj9WnVG900huRzk-Gmzcxv05zfrp2VcwLTIP8LKD80ecLLzUA9tNS-6QdfwEJ-WJ6m1JfqJ1I_Q6L3j53CWGZ3s6zKCttptHDblCt5DIYBXLQmktMaDZHVI7SmhCWjMp9DyBSSs-Pq_WM_3X04BJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔴
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔴
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/146278" target="_blank">📅 17:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnF0H7K9f1JjFqtx9_ZS3toVSRgSb0zFwv3f-9Qok07zk1HfP0Prt15EtV6HOrlig-FoMv8VT0pNOVz67ss-j0BBRVG5NOo9iICQotrqvoGb0d3IqCPsa6B0ZoYaYHqy9nP9ODuwzu8Pc8yNi7ilfy3dgNSfMtfx--LIkr1KbwgnVuiGmaczVelVHZEhZnBrbcxJ4yO9gwKvGy5JSktQai1VDFwEirK5jjtkRymbiK3CZ-IXIitCwl4junIrws60bscP6GKmfxEZHJiEkp63kXG4ITYfpFKB8SEzPPapAjg5VRJFh6PwVbyh8SQ43ksF75C5VrmfXbV0s-JXIJdj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رومانی به دلیل خطر سقوط اشیاء از فضای هوایی، وضعیت هشدار جدی اعلام کرده است و از ساکنان مناطق تحت تأثیر خواسته است که فوراً به پناهگاه‌های امن پناه ببرند.
🔴
این در حالی است که یک پهپاد روسی وارد فضای هوایی مولداوی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/146277" target="_blank">📅 17:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3G60_akgeqqSgoFDd8A9sz7Z208zhX_2r_JXp-dJxW7qH5pMS3sZM-jJQklr6VCiWdcACyCVNta3vgGJ50EtoLajm3EWDCAFx2VqSOLgzwn2FlpMtgdJGVJqZ8T_FhKMBMWKur43HxRT0jqUVFxzgnr-lGLCn_JmRJgRsdAvlcsT_uyMLdVaKKXSNhyr7Vo9RFsp0xQn5Tkk0fgtFZJh7HP2jjYzdpS0wfa2SlBIcUaagWicUTkkYd0ELklI2endEXOS3ogqMQPp4-mNI9Msm_LvoSp5noTSrdquwp4ku2wIe0d5jiGza3R6MibbVWDlZ4XkHKiGmStj68SYkr_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاربر بریتانیایی: نیروی هوایی بریتانیا اخیراً برای دفاع از اسرائیل در برابر حملات ایران به آسمان رفت؛ خلبانان ما جان خود را به خطر انداختند
🔴
اسرائیلی‌ها چطور از ما تشکر می‌کنند؟ با اعلام اینکه جزایر فالکلند متعلق به آرژانتین هستند. عوضی‌ها!
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/146276" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بلومبرگ: نخست‌وزیر جدید بریتانیا با استفاده از پایگاه‌های خودش توسط آمریکایی‌ها برای جنگ با جمهوری اسلامی مشکلی نداره و این موضوع رو تأیید کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146275" target="_blank">📅 17:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال 12 اسرائیل: هواپیماهای تانکر سوخت‌رسان آمریکایی شروع به بازگشت به فرودگاه تل‌آویو کرده‌اند، چندین هواپیمای سوخت رسان آمریکایی امروز مجدداً وارد اسرائیل شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/146274" target="_blank">📅 17:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f71160ed.mp4?token=STJMXct3bwktC_ceTPkQ0X4uVhBFWOUqA5itCKcR_7BzN426CwzwoAdEK_izKl7MztI1-89pLDnzGDZLqiBouyZU-UcWqA1erIKN3AjWiEY5SX4-4y2vAixPU9cZnkFFFG9SCAFNmAdj7vRyiJuO4mWyxeT8KPTz8XMuhUFLyO5fdGmI2cG4WhjZpaB1C_h446O3QlxGAZtAlk5OFLHE1efDUtwr4kCOuRi7jXAKw-aNhBEsxiKoyQ9FkSqJaOHkchtistiZeiXyqaBjkit0MkOvdB7K-5oMpclibCTQQDCfuRvvHuC3nykxQK6jiaZ56JtFCORtChLfry6HVyckGxAyRwtoeT64kLQBTj8pbfb1tOaOtuky_10dUgCSwmIS8wXYuCfDu3or0E8Blx3rYFpkN1slH7jhec0dX-IhVI6IDkMETkazZX6crzLG8v_oQwkSsjgk2jv73ZUO___3xLgqWxM0zJoyH1uP3EX0mtQWVIbdUDiHJ6tGmLy_X09il_pfkQ_UxdP51MN-Sj4dYU9CnUsh85iu0wLJw84Wd29LZLixZ41_f04naEnJyQSrpNAQnve86sBfCWpLAG1uQxfR2eyRC0Zq2gvOgIBQ8ziZOLbGAxXxJNB9mjM4b-z6fJSkU0A5S3Yx9KSreGB6mujMF3vW8UfeGeIXn9TTD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f71160ed.mp4?token=STJMXct3bwktC_ceTPkQ0X4uVhBFWOUqA5itCKcR_7BzN426CwzwoAdEK_izKl7MztI1-89pLDnzGDZLqiBouyZU-UcWqA1erIKN3AjWiEY5SX4-4y2vAixPU9cZnkFFFG9SCAFNmAdj7vRyiJuO4mWyxeT8KPTz8XMuhUFLyO5fdGmI2cG4WhjZpaB1C_h446O3QlxGAZtAlk5OFLHE1efDUtwr4kCOuRi7jXAKw-aNhBEsxiKoyQ9FkSqJaOHkchtistiZeiXyqaBjkit0MkOvdB7K-5oMpclibCTQQDCfuRvvHuC3nykxQK6jiaZ56JtFCORtChLfry6HVyckGxAyRwtoeT64kLQBTj8pbfb1tOaOtuky_10dUgCSwmIS8wXYuCfDu3or0E8Blx3rYFpkN1slH7jhec0dX-IhVI6IDkMETkazZX6crzLG8v_oQwkSsjgk2jv73ZUO___3xLgqWxM0zJoyH1uP3EX0mtQWVIbdUDiHJ6tGmLy_X09il_pfkQ_UxdP51MN-Sj4dYU9CnUsh85iu0wLJw84Wd29LZLixZ41_f04naEnJyQSrpNAQnve86sBfCWpLAG1uQxfR2eyRC0Zq2gvOgIBQ8ziZOLbGAxXxJNB9mjM4b-z6fJSkU0A5S3Yx9KSreGB6mujMF3vW8UfeGeIXn9TTD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اد میلیبند، وزیر خارجه بریتانیا: من به یهودی بودنم افتخار می‌کنم و در حمایت از کشور اسرائیل ثابت‌قدم هستم.
🔴
هیچ تناقضی بین این موضوع و حمایت من از کشور فلسطین وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/146273" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c103c3be2.mp4?token=VBi2DGhOd73SVv2lpOriPZ73Vyk1FYCLwYVQEvE00PpCnddPA3n02rhkUVJtgvmznz1ySuZFlbrynsVkzxnL-__p4wfgp-CXK0j5DN_tRsFKQVp1dm0PUTo3pqvdCv3koTQ1ngqyte3DoYah7-uulqC80D8oggSH7cdyGeYuCBdNiCYJX-sm3n2dq-INTgA8R73c34I3y7O2pvRzUa6f2gdMTr023WRmZdvam1gJRyY1LGVMo3AxSChGx8XhS9VrhpedWdkXRLjfwIouDuEKVME2cbHRnDT5wVHJFANnw3-FO7y1FMIp0vzBfHn6-_NDKb31ujEDZOXXFVgRk8TaIr3Ob5L5pluh2FTGfZ-dJ5ZBjNOjllcNedGYvurWxoBMTuz9241jolaoToy1JNhxvxYudyI9w8dznmMQeJuWDjv0omeefFGWZzfAsqZjj7eqKxiBXcnkWG11JoMuADeeM4h_lrvpTJOpAuOPW-kQ1oVH3H-BrpRWs8O8LnxVo9kpfuEtTfI0RRrQm7Yvjqp2k0R4TOe703ClMjIhFUGrqGvlrdUx5rMSWgOEqttIsZoz8ZaBNA5zKy0uQdADNTDwHzUSBb9kmo1Id3ICEFIgsRN4CJjQQhwwwWHjpqeSwF_PBezcg8VdgPs1bfCqZaieiH08bnVAv60nil_8OM3KZK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c103c3be2.mp4?token=VBi2DGhOd73SVv2lpOriPZ73Vyk1FYCLwYVQEvE00PpCnddPA3n02rhkUVJtgvmznz1ySuZFlbrynsVkzxnL-__p4wfgp-CXK0j5DN_tRsFKQVp1dm0PUTo3pqvdCv3koTQ1ngqyte3DoYah7-uulqC80D8oggSH7cdyGeYuCBdNiCYJX-sm3n2dq-INTgA8R73c34I3y7O2pvRzUa6f2gdMTr023WRmZdvam1gJRyY1LGVMo3AxSChGx8XhS9VrhpedWdkXRLjfwIouDuEKVME2cbHRnDT5wVHJFANnw3-FO7y1FMIp0vzBfHn6-_NDKb31ujEDZOXXFVgRk8TaIr3Ob5L5pluh2FTGfZ-dJ5ZBjNOjllcNedGYvurWxoBMTuz9241jolaoToy1JNhxvxYudyI9w8dznmMQeJuWDjv0omeefFGWZzfAsqZjj7eqKxiBXcnkWG11JoMuADeeM4h_lrvpTJOpAuOPW-kQ1oVH3H-BrpRWs8O8LnxVo9kpfuEtTfI0RRrQm7Yvjqp2k0R4TOe703ClMjIhFUGrqGvlrdUx5rMSWgOEqttIsZoz8ZaBNA5zKy0uQdADNTDwHzUSBb9kmo1Id3ICEFIgsRN4CJjQQhwwwWHjpqeSwF_PBezcg8VdgPs1bfCqZaieiH08bnVAv60nil_8OM3KZK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلیبند: اختلاف ما با مردم اسرائیل نیست؛ ما با مردم اسرائیل روابطی محکم و پایدار داریم.
🔴
اختلاف ما با عملکرد دولت اسرائیله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/146272" target="_blank">📅 17:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80a6fae71.mp4?token=RjojotJ4ZFKjZR-PSn5zI2HKbtjOBvYmJNCzS8hryv5aLlQFXDaJrC-5Ux9ujAvb90I397fjwflJ9IrzBQiUh_1wQdPI8lCr457mFloRqMnGBbE4qzGe-bCZ4kjmeKYxvhj4I5X3R_OO7u_rqlIVXrklglyJKF8J_s8IaQ1Le9XrBsz5sm04leJX5Td5bY0yy6eWFOlUpRqkx1UdHnQ9gF9d6o7F-rH6Ry-0-2_4lgvsOjLLRIjGkFkOHmYclYxV97YmVrU9dC4lbuyETL9m8cpMQXpIfN4HO4l_t_Tc-wcj8BMNGF0gcfZR_GoTcTuVtRXF3rts5jyO0UD8Nmn294xiPtqsUqAGpyKV6CN0-KwDrwCw90K554a3pGiNd7C86wMzMGTqeMu_yKG5uA-Mysno7-bxDYpx-WzJXEYwBxJTnxoDz8NFWtDnLk4Fjk0zbtRz_8mKVYyvfYEg366qqR-vYK1B6uFGe-mibkG7vIm9mL1sk8zt2aLDmswu7ykdsvw0u2mCs5Nv-wVef29YHLYz5mmwpkDOU0puBXLBiKSJG1ZUrpalWjr5UsR-zwH8bS7ql7gyvlamQPDDzLZk9wcPqTou2qaSnDcVw7yqEC7lNbtKXNgYxMqKJMRfBx1yb13sANohhJM2Wie9dI0xHlVPX29_MeV7wx71ja7nOLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80a6fae71.mp4?token=RjojotJ4ZFKjZR-PSn5zI2HKbtjOBvYmJNCzS8hryv5aLlQFXDaJrC-5Ux9ujAvb90I397fjwflJ9IrzBQiUh_1wQdPI8lCr457mFloRqMnGBbE4qzGe-bCZ4kjmeKYxvhj4I5X3R_OO7u_rqlIVXrklglyJKF8J_s8IaQ1Le9XrBsz5sm04leJX5Td5bY0yy6eWFOlUpRqkx1UdHnQ9gF9d6o7F-rH6Ry-0-2_4lgvsOjLLRIjGkFkOHmYclYxV97YmVrU9dC4lbuyETL9m8cpMQXpIfN4HO4l_t_Tc-wcj8BMNGF0gcfZR_GoTcTuVtRXF3rts5jyO0UD8Nmn294xiPtqsUqAGpyKV6CN0-KwDrwCw90K554a3pGiNd7C86wMzMGTqeMu_yKG5uA-Mysno7-bxDYpx-WzJXEYwBxJTnxoDz8NFWtDnLk4Fjk0zbtRz_8mKVYyvfYEg366qqR-vYK1B6uFGe-mibkG7vIm9mL1sk8zt2aLDmswu7ykdsvw0u2mCs5Nv-wVef29YHLYz5mmwpkDOU0puBXLBiKSJG1ZUrpalWjr5UsR-zwH8bS7ql7gyvlamQPDDzLZk9wcPqTou2qaSnDcVw7yqEC7lNbtKXNgYxMqKJMRfBx1yb13sANohhJM2Wie9dI0xHlVPX29_MeV7wx71ja7nOLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه عربستان سعودی:
حوثی‌ها همواره ترجیح می‌دهند منافع محدود خود را بر منافع مردم یمن و خود یمن مقدم کنند.
🔴
آن‌ها به دنبال توسل به خشونت و زور در یک تلاش ناامیدانه برای دستیابی به اهداف خود و خدمت به منافع شخصی خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146271" target="_blank">📅 16:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cKZsnYSzuYhMLP7CxSv_G-x0m2U5iUbtnC_Mu9n6_dovTH0QJBVpbxvWs2eRQEUFJUtxfZxwOiX91z1etCnKj08UjoV6yEEi73qvdQtPZ_WZz3QLrYRSRPmHyvbvB5NcVkXq4EYX9GbtGT0aCJhicDKwk9CPwR5f4SjFs3ugkdyfn44Y2fcwf5O1tkK4gUpAEWyPCIWhym7Iz_qzeNcNrFX9NMq4VlnFVbrDKfsu8F5RxZw3Gm2HsmAcQv3-SUEwHy2skR-PA9TVl6SdgZUz5Bv0QbDWwxoCIpLfrJYZw18P3-f3g02nZsaTyoUncXl3I4e3eW3bzseIJeUUY9a3QS_opcZJFoCAk2nkwgMo5g5wAulO9eFdoowo8Bg93obxeQmk1E7A12Ki7DZv5SnoFTyH24cyU-Jn_MywTkJ43g_NBcwyqVYnaufKKL66gIc7iy9or2bJbnCxPkcwdgD3HVnpDZuOYeWKZxgd1bgwnEFi4vpRdvTA8sRXcbLuguHRh4g_hfgNkL7V8NezR-aiVaa5FV-k1M4824NBo4Ybaw-s8zIJanDly-xbBThashYBwJjiKbAviODY-7cy4dQbGFCwTmLHdEw05kdyMt6ctmzOf7lc09ERlk-Xo2q2U9lrc300uww0xN2kB6rhxrNekLLoPNRE4PaeV45gnbTcWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cKZsnYSzuYhMLP7CxSv_G-x0m2U5iUbtnC_Mu9n6_dovTH0QJBVpbxvWs2eRQEUFJUtxfZxwOiX91z1etCnKj08UjoV6yEEi73qvdQtPZ_WZz3QLrYRSRPmHyvbvB5NcVkXq4EYX9GbtGT0aCJhicDKwk9CPwR5f4SjFs3ugkdyfn44Y2fcwf5O1tkK4gUpAEWyPCIWhym7Iz_qzeNcNrFX9NMq4VlnFVbrDKfsu8F5RxZw3Gm2HsmAcQv3-SUEwHy2skR-PA9TVl6SdgZUz5Bv0QbDWwxoCIpLfrJYZw18P3-f3g02nZsaTyoUncXl3I4e3eW3bzseIJeUUY9a3QS_opcZJFoCAk2nkwgMo5g5wAulO9eFdoowo8Bg93obxeQmk1E7A12Ki7DZv5SnoFTyH24cyU-Jn_MywTkJ43g_NBcwyqVYnaufKKL66gIc7iy9or2bJbnCxPkcwdgD3HVnpDZuOYeWKZxgd1bgwnEFi4vpRdvTA8sRXcbLuguHRh4g_hfgNkL7V8NezR-aiVaa5FV-k1M4824NBo4Ybaw-s8zIJanDly-xbBThashYBwJjiKbAviODY-7cy4dQbGFCwTmLHdEw05kdyMt6ctmzOf7lc09ERlk-Xo2q2U9lrc300uww0xN2kB6rhxrNekLLoPNRE4PaeV45gnbTcWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / اد میلیبند، وزیر خارجه بریتانیا:
ما در هماهنگی با اتحادیه اروپا و آمریکا، تحریم‌های اقتصادی گسترده‌ای رو علیه ایران دوباره اعمال می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146270" target="_blank">📅 16:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ایران: آژانس در برابر حملات به تأسیسات هسته‌ای نمی‌تواند بی‌مسئولیت باشد
🔴
هیئت نمایندگی ایران در نشست شورای حکام اعلام کرد امنیت هسته‌ای زمانی معنا دارد که در برابر حملات غیرقانونی به تأسیسات هسته‌ای صلح‌آمیز و تحت بازرسی نیز اقدام مؤثر صورت گیرد.
🔴
در این بیانیه آمده است اگر آژانس توان یا اراده کافی برای رسیدگی به پیامدهای امنیتی چنین حملاتی نداشته باشد، اعتماد کشورهای عضو به عملکرد و اثربخشی آن زیر سؤال می‌رود.
🔴
ایران همچنین نسبت به نقض محرمانگی و افشای اطلاعات حساس هشدار داده و تأکید کرده آژانس در قبال سوءاستفاده از این اطلاعات برای اقدامات خرابکارانه، مسئولیت قانونی روشنی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146269" target="_blank">📅 16:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGRDYFtys1ZH8vSPD9Ah9B_Y1kB6vKLrwn96muJ-diQqY2jmLyCugeJ3l_yoSOhb-_-h9w_TdzrGzMGaqzq06eorDB5kgz0md1mp61YGBQVxcebWKBFZAxTTWEbHL5I_HBUkqFlfe3iCi-n-Lx4ksOjhwPzsKAR7ERqtGNhuhksziWVHdVHK9m9uiakVShIT2uMKa0EwyqH6cu-o-RAlarBwEkMnfVzsAaBwpIG_zRrOEON9MrHFl2Rfphe4UD49MjEqkac3uBmj7XK-6JWV0IV05OoZF-2NiCMRm42OHAPLrgpFsQi40EHcSXOEFWDLFpt8hM6OMzvOry9yg-md5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug7oxUl6zLWeE35HkS1i1uOD9zX3x8n08KZeXREDl9e4dd-jQH894te1tS_4jHpvKtFSxPFjiotMW1QEvFr_-TQFPVEJAyNVzcReP1SmNsYB90Ys4lDS9-hDmVbwELVnuKEBfoqOmmXkKNuIwHp2z5Zv0h2sk1XpQgkD6OtnbR-FoUVzngfHdkOhTzi18_osVRJNy8GRa3H0kfUI6tLGmXK33QZMFhCgCkURYLoSfvVd0TZD8z6IxnH2dZlh-msURWdUzAVLQ3E2iPiWpGe-GXl_97Lk9HVaxvVToryCtj_mteHLycBmfaX08CJH43YjNAOeZuvnqID5kaNmKo8QiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از آثار حملات یمن به پایگاه هوایی خمیس مشیط عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146267" target="_blank">📅 16:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
تحریم اسرائیل توسط بریتانیا
🔴
وزیر امور خارجه بریتانیا: واردات محصولات از شهرک‌های اسرائیلی را ممنوع خواهیم کرد.
🔴
ما شرکت‌ها و افرادی را که خدمات ساخت و ساز و تأمین مالی ارائه می‌دهند که به گسترش شهرک‌سازی‌ها کمک می‌کند، تحریم خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146266" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اوه اوه تهران چه رعد برقی زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146265" target="_blank">📅 16:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxBkbUjiWrgnAONqWnnvDuFK8HkmmG0RbJHJ2AmNWf9QVe3CtcIKNX-AMu0DMppz2pRSKHwQ6MJBe7cHUUoUYOVu4ElAlrvLgUV03iPEbBGO8jJ06peTjZxbEyMOmao6DDGledAo_jZ9kOCMvvKnrUDZZjBN9SD1ecvijwcrkgWhI_BYOnRW2zIuaANfojrmafzZOZQHS86rzQCmlWfU8S11daMuJZetllGxiad9-bS2b7askZ3ZhM2m9-Hm7_HcCHHCpAzqHwejT5e-PFSvSmwS_XYzcY3XqarDjJgnyX_rOq7hFOQJxWc_k_S2mbxczkwIr2qYgpc5IKm87dgGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز
:
تیم کوچکی از پژوهشگران شرکت امنیتی آمریکایی
Calif
با استفاده از مدل‌های هوش مصنوعی، یک
کرم رایانه‌ای
ساخته‌اند که می‌تواند در عرض چند ساعت، صدها میلیون حساب
WeChat
را بدون نیاز به کلیک یا لمس کاربر، در معرض نفوذ قرار دهد.
🔴
این بدافزار که WeWorm نام دارد، نخستین کرم شناخته‌شده
«بدون کلیک» (Zero-Click)
توصیف شده که می‌تواند به‌صورت خودکار در هر دو سیستم‌عامل
iOS و Android
منتشر شود.
🔴
بر اساس این گزارش، WeWorm از سیستم اعتماد مخاطبان در WeChat سوءاستفاده کرده و با برقراری تماس، می‌تواند حساب کاربر را چه تماس پاسخ داده شود و چه بدون پاسخ بماند، به خطر بیندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/146264" target="_blank">📅 16:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146263">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رکنا: دیروز تو کرج یه مرد ۶۴ ساله که تازه داشت رانندگی یاد میگرفت، با خودروی‌ آموزش رانندگی داشت تمرین میکرد که ی پسر ۲۳ ساله که راننده پژو ۲۰۶ بوده بخاطر آروم رانندگی کردنش عصبانی میشه و میپیچه جلوش، پیادش میکنه هلش میده و پیرمرده میخوره زمین سرش به جدول میخوره و در دم فوت میکنه و به قتل میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146263" target="_blank">📅 16:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146262">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d730932bb.mp4?token=VaH4GTPvrLRujpsluE5wNxacuX15v0RYA3ckiH4trI_LxI-a44AkYIDvIPw7CnTt2HpFH8anN7s8DG2Yx3pDg6yxkh06IGuQNHHbGE1ZbDt0fIiKnZ8RPNFYkKxeR8Ckd3cK0may0iF0-lFCGUGr5nQHA8e2VNrFxmxEUH2ngmicpokJ8d4NX98Tl3PQQJBf3Hl2N6MmvHg0zJbxVQo4N9rzlzp1PPlYmv9ilK6UT3UavUupam5IV9aRWyIrfkSLeQ4lXVwxyvKaYQbAkcXgVeWbmsVaiLfktSlyDQpQTQ39uMGiVxPNXWpRJ5avj357U4Z2vaqLJmVB7t133HOAxZnT2yTsstBtHwIEenh1dI2Hd4826rXGhJTv2_D3otPXWhDzMhswhkTGFKN-r3ocBLy-r6_l8-ZStbxbUcfOlOcU7DUOOH9FVN4swtGlGdwRSPrZLdYYUzjiXFztdrcMv_5XDgKQNbRpJnT5E3LAPGE3lhKT2gGcv2deQNz1txghMuDfbTGRD3ZAYiY_KqWXduWxz01lR_x8dF4iPLMPGOB5WUtN9QrIOVn3HsV7xnhJxpWUdbb9XNCIjcgBg1U2fyz-s506RRZnEsGmY5hf4M2fEHOJkILajW2THvFh_8iTZGsnSX3yRQanZq_8fXnh4y2L2QIS2pJkvT-ZN4irei8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d730932bb.mp4?token=VaH4GTPvrLRujpsluE5wNxacuX15v0RYA3ckiH4trI_LxI-a44AkYIDvIPw7CnTt2HpFH8anN7s8DG2Yx3pDg6yxkh06IGuQNHHbGE1ZbDt0fIiKnZ8RPNFYkKxeR8Ckd3cK0may0iF0-lFCGUGr5nQHA8e2VNrFxmxEUH2ngmicpokJ8d4NX98Tl3PQQJBf3Hl2N6MmvHg0zJbxVQo4N9rzlzp1PPlYmv9ilK6UT3UavUupam5IV9aRWyIrfkSLeQ4lXVwxyvKaYQbAkcXgVeWbmsVaiLfktSlyDQpQTQ39uMGiVxPNXWpRJ5avj357U4Z2vaqLJmVB7t133HOAxZnT2yTsstBtHwIEenh1dI2Hd4826rXGhJTv2_D3otPXWhDzMhswhkTGFKN-r3ocBLy-r6_l8-ZStbxbUcfOlOcU7DUOOH9FVN4swtGlGdwRSPrZLdYYUzjiXFztdrcMv_5XDgKQNbRpJnT5E3LAPGE3lhKT2gGcv2deQNz1txghMuDfbTGRD3ZAYiY_KqWXduWxz01lR_x8dF4iPLMPGOB5WUtN9QrIOVn3HsV7xnhJxpWUdbb9XNCIjcgBg1U2fyz-s506RRZnEsGmY5hf4M2fEHOJkILajW2THvFh_8iTZGsnSX3yRQanZq_8fXnh4y2L2QIS2pJkvT-ZN4irei8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع میلیونی مخالفان مذاکرات در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146262" target="_blank">📅 16:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146261">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الحدث:
نیروهای تحت حمایت عربستان سعودی از شمال استان الجوف، یمن در مرز با عربستان پیشروی زمینی را آغاز کردند و به سوی الحزم، پایتخت استان الجوف حرکت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/146261" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146260">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/کره جنوبی: به تنگه هرمز نیرو اعزام می‌کنیم
‌
🔴
همچنین یک تیم تحقیقاتی برای ارزیابی وضعیت در تنگه هرمز اعزام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146260" target="_blank">📅 16:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146259">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سپاه : یک پهپاد MQ-1 بر فراز تنگه هرمز منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146259" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e6929357.mp4?token=D6w9obxwHCziHOKEZv-LEUyDEp9p5cmW4KZ052eCQtnmrPWE1rWg2oBAceuZu4kemZMfhsYCOcPJIElep6F8pWQypTILkxv474A2omE3cFwkKylJQsYF0YCOF1BmvKFDgVVaesNqmKpqzGiROA8eJn-A3emHNj3iVcFSKNhrAikO0Jl-qxAAwclkrrA5U879OF0yZ0Ct96PDrR8t73nWDdGZGb7Iuk9zFJL9B-_fH_86i_UTjPRuF4_stVQF3jjBiCXzokTkL0zlwfZKIGDFoo32vG6gylxgeUZMBOzJrJCik8-Pt6qnIHn1ddBvourW-e0E9HNOSYdJuyQvjxR3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e6929357.mp4?token=D6w9obxwHCziHOKEZv-LEUyDEp9p5cmW4KZ052eCQtnmrPWE1rWg2oBAceuZu4kemZMfhsYCOcPJIElep6F8pWQypTILkxv474A2omE3cFwkKylJQsYF0YCOF1BmvKFDgVVaesNqmKpqzGiROA8eJn-A3emHNj3iVcFSKNhrAikO0Jl-qxAAwclkrrA5U879OF0yZ0Ct96PDrR8t73nWDdGZGb7Iuk9zFJL9B-_fH_86i_UTjPRuF4_stVQF3jjBiCXzokTkL0zlwfZKIGDFoo32vG6gylxgeUZMBOzJrJCik8-Pt6qnIHn1ddBvourW-e0E9HNOSYdJuyQvjxR3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی در بازار "ایتمه" در منطقه الجوف، پس از پاکسازی آن از نیروهای وفادار به عربستان سعودی، مستقر شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146257" target="_blank">📅 16:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e7b82147.mp4?token=jS5Op3eZKhWUXsTNmz3VWXXkZ05GeqaRj50wBFdxXbPPiZ28S-C0hOtcS83ro6itPVgJIdScV5ZBk5nSOZ1FvJtS_4HNWD959Ku8xzNfM_lm8HZzOgMRrX7480JKs5eDHY5InukF1FwymWwW8gJb0YVYoPksLGXalaj8eCYUhobJmybIngElXTASfm6F1NtYsc40ieyfJka5jBCBjnDtZ53uzIRAsfwJu5RDS5WMVXxvG7zkgysSFQnhDwgA6PgkI2WN3siFlDLv73Zv7wNjsSZV2o8OCChTZoviIFS1Okd6t_4xBG9LqbTaX42dYpMPx-mh4FYiwRtS7DaInTjpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e7b82147.mp4?token=jS5Op3eZKhWUXsTNmz3VWXXkZ05GeqaRj50wBFdxXbPPiZ28S-C0hOtcS83ro6itPVgJIdScV5ZBk5nSOZ1FvJtS_4HNWD959Ku8xzNfM_lm8HZzOgMRrX7480JKs5eDHY5InukF1FwymWwW8gJb0YVYoPksLGXalaj8eCYUhobJmybIngElXTASfm6F1NtYsc40ieyfJka5jBCBjnDtZ53uzIRAsfwJu5RDS5WMVXxvG7zkgysSFQnhDwgA6PgkI2WN3siFlDLv73Zv7wNjsSZV2o8OCChTZoviIFS1Okd6t_4xBG9LqbTaX42dYpMPx-mh4FYiwRtS7DaInTjpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان:ما حملات حوثی‌ها علیه عربستان سعودی را به شدت محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146256" target="_blank">📅 16:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: نشانه‌ای از اینکه پایان درگیری میان ایران و آمریکا قابل مشاهده باشد، نیست
🔴
کشور‌های حاشیه خلیج فارس نمی‌توانند اختلاف خود با ایران را دائمی تلقی کنند و به هم‌زیستی با این کشور ادامه می‌دهند
🔴
ایران باید بداند در کنار همسایگانی قرار دارد که دشمن نیستند
🔴
تنگه هرمز با وجود ظهور مسیر‌های جایگزین، همچنان برای اقتصاد جهانی حیاتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146255" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f30d079b.mp4?token=SIyKO5izO6aajOHo4U9AImHDuHmGfc3aKX8HM2cuEAY3BEP_pWkJ60Anybcrn_3FSEq2lvgDdZZFccrrGvZ-Xc0BB3eW6GA1Hqgf8pepS0S0XBcUpAGXX9WjePUypGeMd7cl_UAOQ_Zux9ZjpyP0I76eReeUZ8g_0Q0rwnShZExQYIyejyJ17EDuzYOcyVwisw_oyRWQKRfgwI4NVc25exyvADsu95EjeHHmbAlQ43-7Sb3exlMV8c-YntEjm9-xSMB6BzPcgnRkC1GsRBaViG9FThaM61u-TdzwfvOqTTvS37lVV1GCV_bTkFXcDSMaKsEIp5PtqGsz9mPSYadCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f30d079b.mp4?token=SIyKO5izO6aajOHo4U9AImHDuHmGfc3aKX8HM2cuEAY3BEP_pWkJ60Anybcrn_3FSEq2lvgDdZZFccrrGvZ-Xc0BB3eW6GA1Hqgf8pepS0S0XBcUpAGXX9WjePUypGeMd7cl_UAOQ_Zux9ZjpyP0I76eReeUZ8g_0Q0rwnShZExQYIyejyJ17EDuzYOcyVwisw_oyRWQKRfgwI4NVc25exyvADsu95EjeHHmbAlQ43-7Sb3exlMV8c-YntEjm9-xSMB6BzPcgnRkC1GsRBaViG9FThaM61u-TdzwfvOqTTvS37lVV1GCV_bTkFXcDSMaKsEIp5PtqGsz9mPSYadCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاکر بوری بلاگر بخاطر این ویدیو که سراسر حقیقت بود اما چون اون‌نماینده مجلس خوشش نیومده بود به ۱۴ماه زندان محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146254" target="_blank">📅 15:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146253" target="_blank">📅 15:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نماینده‌میناب: مردم باشرف جنوب حاضرن با قایق خودشون برن به جنگ دشمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146252" target="_blank">📅 15:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146249">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLWybyGNUdQNS2x20mCghZ7Fu6qgjFZDauVC2UvuYgTucgtoVFr6nxRHzvKKnc064oXTelddSVphCW1mdQ8dynEpppTddhFDcCkkpZnBnDvG2a9Zpjv0yX8iElPEDPve6y1B0Pe_GvrBDPZsdu2D02_gCTSXr4C4dYousSVBy7yg4ZpdMrTc_w6AvhZEjUm7nd8muYMhvzIi8PkyavMJHtJzZhF_gkQmAtUPFynxTg3MDokDJvbcFOvV4zGy-knBJ9Ix8vF4kOlVEC5CSGU08myQCdzESoSayQMb2rkr1uaBE2w2DffYcZKAlrDySOZT09wKerHIKMvYR3q2jVrkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419a009651.mp4?token=B22ESzny4uneoTjGFoFpXQVXSEFnsI1WNKybG7Q1guqlnluFXP3wBS2oOqscsphK9Ld1nlKioXgLynmUAdmOiu6xA-97vuOy0BRnDQS7UuVa7BJpkvyznKImhPaIr96dg_jRKHfUoNkV3U_MMy6OtxvcNA4TlwD5bKDY90aN_uHlGRXgtH953Kd_-XJSM0Olte3VB-4_XMOeaOWVe717GEIo2GKrSwBMEQiBJjh4tpRWGw39uTKfb_2RmodbhA2ISMqIPO15Qbr4tGi2vhCElGjKjavPbHYX2pvJ3hjGuWXEeSSeDAKt1-OQjzlJz2z-L3NHndChRKMV2ps8CYdqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419a009651.mp4?token=B22ESzny4uneoTjGFoFpXQVXSEFnsI1WNKybG7Q1guqlnluFXP3wBS2oOqscsphK9Ld1nlKioXgLynmUAdmOiu6xA-97vuOy0BRnDQS7UuVa7BJpkvyznKImhPaIr96dg_jRKHfUoNkV3U_MMy6OtxvcNA4TlwD5bKDY90aN_uHlGRXgtH953Kd_-XJSM0Olte3VB-4_XMOeaOWVe717GEIo2GKrSwBMEQiBJjh4tpRWGw39uTKfb_2RmodbhA2ISMqIPO15Qbr4tGi2vhCElGjKjavPbHYX2pvJ3hjGuWXEeSSeDAKt1-OQjzlJz2z-L3NHndChRKMV2ps8CYdqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های وابسته به انصارالله مدعی شده‌اند که نیروهای این گروه بازار
الیتَمه
در محور
الحزم
در استان الجوف در شمال یمن را بازپس گرفته‌اند.
🔴
با این حال، ویدئوهای منتشرشده
و این ادعاها قابل راستی‌آزمایی نیستند و مشخص نیست تصاویر مربوط به زمان اخیر هستند یا قدیمی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146249" target="_blank">📅 15:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146248">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ارزشی خیلی جالبه!
میگن اینجا دموکراسی حاکمه، بعدش میگن رهبرمون هرچی بگه همونه و اگه کسی حرف از دموکراسی بزنه(اشاره به روحانی) بهش میگن خائن وطن فروش مزدور عامل موساد کافر حربی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146248" target="_blank">📅 15:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146247">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صداوسیما: هزینه افزایش نرخ بنزین صرف بهبود کیفیت زندگی مردم خواهد شد
🤣
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146247" target="_blank">📅 15:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146246">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqyMBn1_3FjNeTrGFhUUyEINKGZvjScBi16AXBPFpn7zsqRiLTcwIe6rEpBayiYBvYi-UKqrP_YlS5qIaDj1vsTlHdvZr7SRor7hHejkNpugE4FFQCSSW9zyGr38LdMVTbC4bja-HOqNVi1wZE-Su2HkJ8G6DdKjyZ77Do2DOvSRgqmO72dMeANdsTOjXFJRwjV1zuw0btXkxGhhenJwkECRZYnds8DwZatrOYctEgxECOYoBjgrpMd5zj-DQXubHX6dvZXWdSz4eA7ehwdKDNnMPIDXh7VwFfMpFMHUCvdyE9QJ85RiSNgBi-_U0d86xooZ7tzcmM6It9A1I54DYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیکه کاربران فضای مجازی به پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146246" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146245">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa2a2a7ee.mp4?token=Y8vUtJ8Y9a_0FWSDL6mbtewD5eoOuGxr7GmQHZ2rpHcMYWKw2jPpYuqFDF3gh_i4C-FSIs2SiFfEcc4bqtwIWixp92wsNQG5Rk1hsME8xB9OpOht_N20q2c45wENa1ZdGyTxrefWHqal0c4Ey3w9zj43xwg1s0MY7kx1h4zDnI3cN5_X4zJpIInL_IMh2SojqsCothoQr5DdiB6SnY_XteMPgANIV1SwB1euIESJbzUslgUG5x2PVD6Gz2kVAwb8iuAiDX3xPDABRCRyHZaqSge1r_sG8Inyk1v4nhs8TTg9JWsLg9ds_6-nTaenJkIoZNXUAWN9Sou3eibkyPHHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa2a2a7ee.mp4?token=Y8vUtJ8Y9a_0FWSDL6mbtewD5eoOuGxr7GmQHZ2rpHcMYWKw2jPpYuqFDF3gh_i4C-FSIs2SiFfEcc4bqtwIWixp92wsNQG5Rk1hsME8xB9OpOht_N20q2c45wENa1ZdGyTxrefWHqal0c4Ey3w9zj43xwg1s0MY7kx1h4zDnI3cN5_X4zJpIInL_IMh2SojqsCothoQr5DdiB6SnY_XteMPgANIV1SwB1euIESJbzUslgUG5x2PVD6Gz2kVAwb8iuAiDX3xPDABRCRyHZaqSge1r_sG8Inyk1v4nhs8TTg9JWsLg9ds_6-nTaenJkIoZNXUAWN9Sou3eibkyPHHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
🔴
نمی‌شود صرفاً دستور بدهیم و انتظار داشته باشیم نسل جدید از ما تبعیت کند
🔴
تحول در نظام تربیتی نیازمند نگاه آینده‌نگر و متناسب با اقتضائات نسل جدید است.
🔴
حل مسائل جامعه نیازمند تقویت گفت‌وگو…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146245" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146244">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
🔴
نمی‌شود صرفاً دستور بدهیم و انتظار داشته باشیم نسل جدید از ما تبعیت کند
🔴
تحول در نظام تربیتی نیازمند نگاه آینده‌نگر و متناسب با اقتضائات نسل جدید است.
🔴
حل مسائل جامعه نیازمند تقویت گفت‌وگو و فعال‌سازی ظرفیت‌های مردمی در بستر مسجد و محله است.
🔴
آنچه امروز در جامعه مشاهده می‌کنیم، برونداد نظام تربیتی ماست.
🔴
در مقاطعی امکان مداخله تربیتی از دوران کودکی و نوجوانی وجود داشت اما از این ظرفیت به اندازه کافی استفاده نشد.
🔴
اکنون با پیامدهایی مواجهیم که اصلاح آنها به سادگی امکان‌پذیر نیست.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146244" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146243">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سی‌ان‌ان: خسارت ایران به پایگاه‌های آمریکا «سنگین و قابل‌توجه» بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/146243" target="_blank">📅 15:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146242">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود تو سیستان بلوچستان ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146242" target="_blank">📅 15:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146241">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2f0be2c9.mp4?token=T_3Dbag-T-A6ClOq06zX-9Bu1cwIxcfZmwcnlRo0v_FAV_T5i9WG_p5GB4yHGdv57BqjNAixvFMlJdGRYQs4-eQw6wkNwpq0U0yFgvtTjlBKF7GICB4ExUvrhLSnvnxTqNmsgyZ_VJM1qI2rCZYnevhIZ1u29n7G7eu6j4l2LVYS2gaKB9rTt9boL08e0rvb9n6v0FJQjNYVi9suQciePMZEwlXYlYzC5BeV66tQKz_YzLQT_bHG0kZVxuEJEkap3VmhyWD57s0FEahROQlgsItV5Yn4zZ1jjbXNS1UTS6VOxvR0urKWSpIWcMhiHYVJDHZkEei6TG8sGHjKKzOXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2f0be2c9.mp4?token=T_3Dbag-T-A6ClOq06zX-9Bu1cwIxcfZmwcnlRo0v_FAV_T5i9WG_p5GB4yHGdv57BqjNAixvFMlJdGRYQs4-eQw6wkNwpq0U0yFgvtTjlBKF7GICB4ExUvrhLSnvnxTqNmsgyZ_VJM1qI2rCZYnevhIZ1u29n7G7eu6j4l2LVYS2gaKB9rTt9boL08e0rvb9n6v0FJQjNYVi9suQciePMZEwlXYlYzC5BeV66tQKz_YzLQT_bHG0kZVxuEJEkap3VmhyWD57s0FEahROQlgsItV5Yn4zZ1jjbXNS1UTS6VOxvR0urKWSpIWcMhiHYVJDHZkEei6TG8sGHjKKzOXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از وضعیت ساری
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146241" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146240">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59092702df.mp4?token=sHZeqPoZfhKBKprrK22iCCGRy_fUtEWykYUBppjHCTMK0_vRHUn_LZTdZK8qnD48ACSeccFLh2v4nZYgV1-rosJxP0Nd1ZKjDDCpvTukvQ-ax-nWS_nZRDrR3ogfU7Jb6ch4WcJAhyNEJNsWXYioxX8-HN7bUblH9QMpnquSEo3JE26pa5ycxrGGJGfAVfCHPxtKJQ6VW_AaoX8RmYFVzd259S0toVIxSqHHli-FBz2V9Dj3y7KT2yz4snmzoAa1oU6mZ064N_v4L_nzyvH2R9e6ks81C6En-LJiMSx9hFPZNFSI_U1a1iKs3Xkng8jSjNnqL9V1GNuHtE-UQVxTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59092702df.mp4?token=sHZeqPoZfhKBKprrK22iCCGRy_fUtEWykYUBppjHCTMK0_vRHUn_LZTdZK8qnD48ACSeccFLh2v4nZYgV1-rosJxP0Nd1ZKjDDCpvTukvQ-ax-nWS_nZRDrR3ogfU7Jb6ch4WcJAhyNEJNsWXYioxX8-HN7bUblH9QMpnquSEo3JE26pa5ycxrGGJGfAVfCHPxtKJQ6VW_AaoX8RmYFVzd259S0toVIxSqHHli-FBz2V9Dj3y7KT2yz4snmzoAa1oU6mZ064N_v4L_nzyvH2R9e6ks81C6En-LJiMSx9hFPZNFSI_U1a1iKs3Xkng8jSjNnqL9V1GNuHtE-UQVxTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه عربستان سعودی:حوثی‌ها با تحریکات خود، عواقب ناخوشایندی را برای خود به وجود می‌آورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146240" target="_blank">📅 15:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146239">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انگلیس یه قانون جدید تصویب کرد که فشار اقتصادی به ایران رو چندین برابر  تشدید کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146239" target="_blank">📅 15:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه، درباره حملات انصارالله (حوثی‌ها) به عربستان سعودی: «ما معتقدیم که این حملات نتیجه معکوس خواهد داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146238" target="_blank">📅 14:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146237" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqz5k4uvp9eAlGVvgMJF4xyESXmTRAHEQpjL7e9jnyn4oAILHZZKlcxR2jx_fBx_f1fuGCjvTwE5ROVjp1EOFwQ9ESYsCmkeNeAU9yR5Jw5n8icG49sbWfhtT0uQw6H3pM7dHQNTfiXEy9_SGp6BG-EJbyEfpdSnXDlIGWIs70ZN134NE6l8xR03fW0wG1KvnosgRaqRpEW3CleQpstyNPKY4c-EXA3LxHrGNrxOXp14RpPOQy-Ch_rJuVRjC5WxrrUm54hKQRpb3wRYQbu_jFToZPyczZLWtbOcBSE24jTELMgTBce08EQUqOajwia5eW-Q1X1asUpOaO4lXU3elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3JwRMhm9ZCjWAyF_Wg9oqI6Sa1q7h9no96mAeCl2zgh4xMQx_U7dfbYR76QOCUtw5q1LboIfipSUpPjjO0iYM9-RsuCN679mRcrUZ9U23krFA-tDNFGXAXa2z5se_6Vh3AnbR3OGAnL1FNKAsC38IJU0XBGyY8kflR5YZoOrwy-04k7daugHA65t2tL1zxXxc1SmjavvzNXLGg2Hf9wrBvFkrjURmgJ9XTrp9XVhRGKQ8LZVkLWBOFtZYG-iBJ4ZE30NqcVCzq8Q_2yTNT8ZDcH-a0UdQ9cQq2thBXjKY7xwxJLxs89TCIsKKY74FjpYIZJhHwp31CcCXxfDh78tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COqQn680neUIhZYFZ28Jd5jNQrjOeoZa3Yg1HZ3RtQbRzcbUZne0nrGWul7LcofHKcAOth3-Ta1Pr9PwYnymMk-BpzADQvGnWDRjUOCntgs9Q24rbyHtq12mTt5mEq6LrVqgHMFC9Wzyv1E5bIR_jpxLGS2XOlZnavHHfzhUutxAmYD3YgBnmKV5zFjdnxVUOl_wJ4ZJXRODPH9kFzNceBjzdYacsz9B4p5DEhNlQheRIYAD4p0j0ncmNm1CXSQeOll7Uzfzp7hi-BJbABDJ2AoHRugRA-tUGv6mKLsZz1fmGm0-6kml6YFNRpLJtbcpNz7YJ_0t1-dqtLS4-CQCdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41eec3ec50.mp4?token=VgDOVB7O8wCNQi9KsTqnYWsaFkOSt-TpNUlix507GIO45J_uHAfQgOvfVG7gUC0MvYsevj_wt3AqWPHnqPMRlrtPGK_kE3jE-QSReP-AzFQbNvrSkdFIksm9VJwJyCzMvWSfd7mXqqAXJAQVCk2kMZM1g2cegUB0Iiu5bq6aM8ki2f5xGzz0amh5CzYT5ryTh0KXhDcfx1iBRqrXMHzxMeshVEVtLHyHHMaeax18s50YxGCX2gk3Wyf7wXmWx5_UNWZBAn7eEGJdxshJwMKvBCKhYK7InvG3G6SIzhFUKuJCr1lCpCoGPCj6VMtDt-7bskx_u2crM3RyhEpYozO2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41eec3ec50.mp4?token=VgDOVB7O8wCNQi9KsTqnYWsaFkOSt-TpNUlix507GIO45J_uHAfQgOvfVG7gUC0MvYsevj_wt3AqWPHnqPMRlrtPGK_kE3jE-QSReP-AzFQbNvrSkdFIksm9VJwJyCzMvWSfd7mXqqAXJAQVCk2kMZM1g2cegUB0Iiu5bq6aM8ki2f5xGzz0amh5CzYT5ryTh0KXhDcfx1iBRqrXMHzxMeshVEVtLHyHHMaeax18s50YxGCX2gk3Wyf7wXmWx5_UNWZBAn7eEGJdxshJwMKvBCKhYK7InvG3G6SIzhFUKuJCr1lCpCoGPCj6VMtDt-7bskx_u2crM3RyhEpYozO2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به مناطقی از غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146233" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزرای خارجه چین و قطر درباره آزادی کشتیرانی در هرمز گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/146232" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قطعی بیش از ۱۰ ساعته برق و آب در چمستان / نگرانی مردم از خسارت به مواد غذایی و داروها
🔴
پس از بارندگی شدید و سیلاب در مازندران، برق برخی مناطق شمال برای بیش از ۱۰ ساعت قطع شده است.
🔴
بر اساس گزارش‌های دریافتی از منطقه چمستان، ادامه قطعی برق باعث اختلال در تأمین آب نیز شده و نگرانی مردم درباره خراب شدن مواد غذایی و داروهای نیازمند نگهداری در یخچال را افزایش داده است.
🔴
شهروندان خواستار رسیدگی فوری و اعلام زمان دقیق وصل شدن برق و آب هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/146231" target="_blank">📅 14:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8ae66168.mp4?token=ClxgoadBgmZF3JHUus4PBuNF2Zlje-8WnWDvBY0F1SBu1RJU2emj9LVQS4tDbvswLS0QCu30db4Guwa0LKXegkn90e5JYq0BFV6ojQksBEZFhAZ_k6JVKd5saUJQaOICgLtVNLi9rpm5j87z_nPWW5kKYHqstY3RA2Z8-81x-vM7_4b4QpnFN77zGRfCXBYLztY8iCrtVsKeIuz5PXeRFOQ_X1U7DnnYDiCvDkQMT5W7-G3WnIy7wIeUlTTd8wI6TpcWZjrVg0fOdkU6OnMG9tzBobfLJO6h9X_HSNuVNUzNeb_ryr1jTcBVHF_Yh-aaDu8eUkKAymWR1ijHqtUSsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8ae66168.mp4?token=ClxgoadBgmZF3JHUus4PBuNF2Zlje-8WnWDvBY0F1SBu1RJU2emj9LVQS4tDbvswLS0QCu30db4Guwa0LKXegkn90e5JYq0BFV6ojQksBEZFhAZ_k6JVKd5saUJQaOICgLtVNLi9rpm5j87z_nPWW5kKYHqstY3RA2Z8-81x-vM7_4b4QpnFN77zGRfCXBYLztY8iCrtVsKeIuz5PXeRFOQ_X1U7DnnYDiCvDkQMT5W7-G3WnIy7wIeUlTTd8wI6TpcWZjrVg0fOdkU6OnMG9tzBobfLJO6h9X_HSNuVNUzNeb_ryr1jTcBVHF_Yh-aaDu8eUkKAymWR1ijHqtUSsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبگرفتگی شدید معابر در بابل به علت بارش شدید باران
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146230" target="_blank">📅 14:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQRyCATamU8W4VTGbeD7AP1Cxs8KcX-P7zxwC7oGvsrmc2V4nzFHMq1wIwvQAgoL7tiYxWne75eeFhoZvkpz4llFNzODmlsM9sKSKzS1AL_SOPqx-ZRIDqHswINwmDm_XanGQvrlfw0L9Nvw1AlnTh3Bj5YuV08pfRcpSM5LxHQlz1KXS7ZD41d-OcjnwXCVRyCMRY5nBYfGxiIJJu10CDPEUrtROFY2239AJ7cthbcFu8G1WqFAG9CUFtGyEfWkdw2YAj6ptHcLN166ZZkf_2Zj__BNCIbhN5H6WR5AWJXLA-6oPwfrJg5puReOKbr8Oi7eJdLUoXMcbNZRN3uJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیشروی گسترده نیروهای یمنی از چهار محور به سمت مرکز استان الجوف
🔴
نیروهای مسلح دولت یمن با حمایت و پشتیبانی نیروهای قبایل، عملیات پیشروی خود را از چهار محور در استان الجوف آغاز کرده و هم‌اکنون به شهر «الحَزم»، مرکز این استان در شمال یمن، بسیار نزدیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146229" target="_blank">📅 14:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: باز شدن تنگه هرمز از اهمیت فوق‌العاده‌ای برای همه کشورهای منطقه برخوردار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146228" target="_blank">📅 14:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رسانه روس: شروط جدید ایران به آمریکا منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146227" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قیمت نفت خام برنت در بازارهای بین‌المللی معاملات آتی، تا ساعت ۰۸:۰۰ به وقت گرینویچ، به ۹۹ دلار در هر بشکه رسید؛ افزایشی شدید که پس از حملات حوثی ها به عربستان سعودی رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146226" target="_blank">📅 14:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی ریاست‌جمهوری روسیه: برای عادی‌سازی روابط ایران و امارات آماده هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146225" target="_blank">📅 13:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ooi9IWhLgm2wXl7fINqyhl-iJhCrLfCjQLDYbg0_3xlBlKp1sUk64g9gDI_3nwcMuwOKOIo5U8fmQiu6A1T_k2M_IMV7uRJze0PXwVvr_-muGfQFgPUZwBy0uQigCAkCSG9DyPm4hrd4aNQ3WUeIdi2l6P6U51_HUs9LSZMEvt4YNUgOFtGwehz4lW83awzYIF0gpKen4M6rQE92zfjyAYORdSvnIxt3D_ddREoICZXC-37dTCYdQk4t1ZnrQt1rnnUoYj_QJ_D96yzWp2nGTAR2PIKLG1TNAqTxt7VSG32JpKq7_xZ75kDfADXIoJU1Jiud08L5HRoScqntGQGu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضاییه: محمدباقر خرازی در بازداشت به‌سر می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146224" target="_blank">📅 13:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146223">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های استان بوشهر: پرواز در مسیر بوشهر به دبی از بیستم شهریور راه‌اندازی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146223" target="_blank">📅 13:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjL7mpoBIhMGYPgdhIwhOCd1rmPjkFAu_oE9IOdg0laK1oqaM7_tH1gCwNh8aH-SjXawCVBGrb-zPKWOd-b5W_obXzFaG02krty7qhL1027VXOacyFSFVnO7ANO5vouAbVD68XuTTpMzeGRucic3zADEB6Lu4vNt3eQ2i0C3nSQAYpydK-_QbT_VAQGqNkbeu1MuYixc0iZBb2ao67B7jlFUrADmsZrrRjNeAk53AHtARa09GJuOVcEzF82rKefA3gRNkQujo3Sl0ogVj8JcECx8rncMJw66BYZ6M9yMSK50EC87nTxjHtlc0pQt7C3o2A6VXlamWxRmb039uMlyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146222" target="_blank">📅 13:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس: خودروهای نوشماره و وارداتی طبق روال قبل سهمیه‌های خود را دارند و برای آنها محدودیتی در نظر گرفته نشده ولی باید هزینه نرخ سوم را بپردازند.
🔴
در مناطق آزاد، نرخ سوم برای خودروهای وارداتی اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146221" target="_blank">📅 13:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
زلنسکی: «به نظر من، ما همچنین در حال حرکت به سمت مذاکرات سه‌جانبه هستیم.
🔴
نشست سه‌جانبه بعدی می‌تواند در امارات، سوئیس، ترکیه یا کشور دیگری برگزار شود.
🔴
ما در این کشورها تجربه برگزاری مذاکرات را داریم و از سوی چند کشور نیز دعوت‌نامه دریافت کرده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146220" target="_blank">📅 13:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146219">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahN0U7Z_S9lDA2scBQaDuTlQZsfcNWkj0f0WWSVJfYBGef498oTcUq4QL12tqU9JoQ4g-xJrcFITfyPpx8LS59Ds5DiGvg1nt-wK3nUUfutGztg1tj2w-0rITnCS67749pKXXcg51C9YOaS7v9uZqrPwmsMSlBrBVTdKh8ILmV4h8pH579Kf9i8ZzBRznkmMKTKOkEwC9WepoebBzkt2UP24Gve4buDfpx6T2uGiQZ4bljAeAciRGNETdOHakGZ7NTPIfhQs2QCCrhdLtQyke58g2YJLgfDFshNUY5fRRoHaZj4VELru74Af12Oy09kv40HV-S30eeCdKXmV0W4LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزرای خارجه روسیه و عربستان درباره ایران و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146219" target="_blank">📅 13:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=N_xXH8JQWNlms5e4sVftTG434fidv5_25OOQd6fOVrxXD0o2YvvVAV7BBKTCSS3O2FDFeR1Bp59y7xfXBHhiR17wYbFAGs7d-75DSTGbuKN0xVuNrzjrD_m3i6XiPXw-v_E5wrLM4j0F-Fc96sxgKT1QZAnu4_yq8PVeAYxrKEMJDGeqLNMRvtd8OgYtfOr_k1CyKRZlUJ-Cd4dq9_6SQUYq6ePiFi1XcIqm_TGit_xzFdgdj0qrQa8Ntn0-8_LupTK8jMEpPw2oEZ-aC-JN-GLaMrsEx8A7jOwZOtmMZw6et8OAm-WifmIDB2rQe_KN5ktvTBL_BUZ7Gq28Z0KV2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=N_xXH8JQWNlms5e4sVftTG434fidv5_25OOQd6fOVrxXD0o2YvvVAV7BBKTCSS3O2FDFeR1Bp59y7xfXBHhiR17wYbFAGs7d-75DSTGbuKN0xVuNrzjrD_m3i6XiPXw-v_E5wrLM4j0F-Fc96sxgKT1QZAnu4_yq8PVeAYxrKEMJDGeqLNMRvtd8OgYtfOr_k1CyKRZlUJ-Cd4dq9_6SQUYq6ePiFi1XcIqm_TGit_xzFdgdj0qrQa8Ntn0-8_LupTK8jMEpPw2oEZ-aC-JN-GLaMrsEx8A7jOwZOtmMZw6et8OAm-WifmIDB2rQe_KN5ktvTBL_BUZ7Gq28Z0KV2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: «ما به بسته‌های موشک‌های بالستیک از آمریکا نیاز داریم.
🔴
آنها به‌طور دقیق شنیدند که به چه چیزهایی و در چه زمانی نیاز داریم
.
🔴
من روی دیدار با دونالد ترامپ در ۲۰ سپتامبر حساب می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146218" target="_blank">📅 13:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=dCnfzXGXgRX2h1HGw5FFQfe9mLeWAIa6J39e3ab6BtzlWJJNu-NbiH7TYxhMmEw2HFzPIG3eWiRBnqHY5u9PWeahgFAO6iIRrKEyQxJ02st4S9EA6PnhZh_XmaVa71IC_gZLNefJreVc8m6aBEc91GAAo7CKkZXhDnYPzrrHtOQispUGV_VyomXBRNTIVdtJRLMB5AXcVIyGq_RpKPMmFUTw-sMb7QOQeJL5-X2_FnDXSMc3WJCPf3QMyC-Dj9L6YkJK9uDk1DU6MC03SgeLcskrygk8U7RcZed-f0v0lnzG1jQoNOLQALDljlvWJRprJjEO5JyDp8_9sYHNo5wfhXiKAUK6FiOxXujC3Q8TrJmvx1svYJtsUFUj_IrJiPhk88U78iSMxsG4v9efo1iq-v431b9osJcZSlToFNGVIgwzzpMED3mlMTDZbCDi4zLfEjq_zwQHDeOrJFv8Zeq63K003ofqB7PVDzsMsPjJfrlPi_K4K1wmXh55ucL5xJByWjgpW0ajV49y_gIQb2aCAov3rlyWBu-BNEHoPhcgmrAC70LKBf0EUd0LIsh0IrAWKUqmCLiTQl0Id-F2Xl8pRBG9694cWCBeKL4eD9s9DFFSAjusifaf4sESWKrND4HgxygWQJ2yjqUIUjZ1Dq6wKqIi27_0TKRKfS-7StDT5Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=dCnfzXGXgRX2h1HGw5FFQfe9mLeWAIa6J39e3ab6BtzlWJJNu-NbiH7TYxhMmEw2HFzPIG3eWiRBnqHY5u9PWeahgFAO6iIRrKEyQxJ02st4S9EA6PnhZh_XmaVa71IC_gZLNefJreVc8m6aBEc91GAAo7CKkZXhDnYPzrrHtOQispUGV_VyomXBRNTIVdtJRLMB5AXcVIyGq_RpKPMmFUTw-sMb7QOQeJL5-X2_FnDXSMc3WJCPf3QMyC-Dj9L6YkJK9uDk1DU6MC03SgeLcskrygk8U7RcZed-f0v0lnzG1jQoNOLQALDljlvWJRprJjEO5JyDp8_9sYHNo5wfhXiKAUK6FiOxXujC3Q8TrJmvx1svYJtsUFUj_IrJiPhk88U78iSMxsG4v9efo1iq-v431b9osJcZSlToFNGVIgwzzpMED3mlMTDZbCDi4zLfEjq_zwQHDeOrJFv8Zeq63K003ofqB7PVDzsMsPjJfrlPi_K4K1wmXh55ucL5xJByWjgpW0ajV49y_gIQb2aCAov3rlyWBu-BNEHoPhcgmrAC70LKBf0EUd0LIsh0IrAWKUqmCLiTQl0Id-F2Xl8pRBG9694cWCBeKL4eD9s9DFFSAjusifaf4sESWKrND4HgxygWQJ2yjqUIUjZ1Dq6wKqIi27_0TKRKfS-7StDT5Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
«اگر بریتانیا واقعاً به دنبال برخورد با مسائلی است که آنها را نادرست می‌داند، پس تحریم‌ها علیه کره شمالی، چین و روسیه کجاست؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146217" target="_blank">📅 12:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=P3y6fiiuVymaQ8GpzE1MbL8Nagf7UHzUXb4N2Iun3oN3Yfd4rmMnggEgPnz9eeSkuqnwl8BWthJIl6-517M7JLG0JRnSav1In3t5u8K7W6bfubdRJMD88qkx0O5S53RkwNVrtDqjQdWzRFuLOPM21JJneevjTriucKkSobK2opi6szCRMqxHlJkz8lSLywLW7rNPslxVy1rUDLbw92FeF1AgBMlU35zizCHITXibbDmq8ZJM2jtzthTOeuJI4dbToZp4Lcbbdjd7GI19KZHLNhN8361c70KRzIGAciiScgGNgy_AagBcEBwA7csvVEY0ufBzUqDDIYzaVzFu6s1aYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=P3y6fiiuVymaQ8GpzE1MbL8Nagf7UHzUXb4N2Iun3oN3Yfd4rmMnggEgPnz9eeSkuqnwl8BWthJIl6-517M7JLG0JRnSav1In3t5u8K7W6bfubdRJMD88qkx0O5S53RkwNVrtDqjQdWzRFuLOPM21JJneevjTriucKkSobK2opi6szCRMqxHlJkz8lSLywLW7rNPslxVy1rUDLbw92FeF1AgBMlU35zizCHITXibbDmq8ZJM2jtzthTOeuJI4dbToZp4Lcbbdjd7GI19KZHLNhN8361c70KRzIGAciiScgGNgy_AagBcEBwA7csvVEY0ufBzUqDDIYzaVzFu6s1aYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر منتشر شده در رسانه‌‌ها از انفجار در تاسیسات آرامکو در پی حملات حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146216" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرگزاری رسمی بحرین: پادشاهی بحرین حملات مجدد حوثی‌ها به غیرنظامیان و تأسیسات حیاتی در عربستان را به شدت محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146215" target="_blank">📅 12:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نماینده مجلس لرستان: کشور با اعتراضی روبه‌رو نیست و مشکلات معیشتی در حد گرانی‌های جزئی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146214" target="_blank">📅 12:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: حتی قیمت سوم بنزین با نرخ ۱۰ هزار تومن هم فاصله زیادی با هزینه واقعی واردات داره؛ هزینه واردات هر لیتر بنزین برای دولت بیش از ۷۰ هزار تومنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146213" target="_blank">📅 12:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de408d162.mp4?token=qMAsREY5Cay7nA5LDttWqVglDQSaLUt8-IZizHAtil07JdPLPFc2rbUCeqDDqQfmWwOlHZ1w7tJqRBNQKrUKqnoBzkNtPHERLEp8NFiWm-GW-U_3ZlJuToqgciqn_pZ-3jirqBc12DOe5ACM0A3jNtoONiZvbNA5WWYkn1BgCN7lkx0_4VbLyKlxHJiLemMGyaIyKdcgw8CgJ2rlW2MCf57kx8F7WLrWedhlgFMNo61t4uBW6iNVJ64104MLBpDETSwU1s5T7LC2P_azlKYFoeEOAjRPhcqho7cUUJOwUZ1IE8EkV4fZE7dQRY6HCSej0V8wmLxXkBZdtV_PLavPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de408d162.mp4?token=qMAsREY5Cay7nA5LDttWqVglDQSaLUt8-IZizHAtil07JdPLPFc2rbUCeqDDqQfmWwOlHZ1w7tJqRBNQKrUKqnoBzkNtPHERLEp8NFiWm-GW-U_3ZlJuToqgciqn_pZ-3jirqBc12DOe5ACM0A3jNtoONiZvbNA5WWYkn1BgCN7lkx0_4VbLyKlxHJiLemMGyaIyKdcgw8CgJ2rlW2MCf57kx8F7WLrWedhlgFMNo61t4uBW6iNVJ64104MLBpDETSwU1s5T7LC2P_azlKYFoeEOAjRPhcqho7cUUJOwUZ1IE8EkV4fZE7dQRY6HCSej0V8wmLxXkBZdtV_PLavPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: قیمت بنزین سهمیه‌ای افزایشی نخواهد داشت و فعلاً همان ۱۰ هزار تومان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146212" target="_blank">📅 12:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پیروزی AfD در آلمان؛ فرانسه نگران تکرار تاریخ در قلب اروپاست
🔴
پیروزی تاریخی راست‌گرایان در انتخابات زاکسن-آنهالت، تنها آلمان را با یک تحول سیاسی کم‌سابقه روبه‌رو نکرده، بلکه در فرانسه نیز زنگ‌های خطر را به صدا درآورده و آن‌ها نگران تکرار تاریخ در قلب اروپا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146211" target="_blank">📅 12:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نشست فصلی شورای حکام از امروز در حضور نمایندگان ۳۵ کشور، با محوریت ایران برگزار می شود
🔴
آمریکا و سه کشور اروپایی در این نشست چند روزه به دنبال ارائه قطعنامه‌ای برای ارسال پرونده هسته ای ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات منع گسترش سلاح‌های هسته‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146210" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
زلنسکی: آمریکا به‌دنبال کاهش تنش روسیه و اوکراین در زمستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146209" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRiZpKISLFcSnsDxkb-e9LbYMar31FsqGPI6fL9WYKGRHNlt8CcB2XsbIdsb-vuGr1ccPKbf_AopxDfmSJnBAhmjc850WDDDX3HyIwqwIXh3wG_so0C6r3YfblREPpfaNDKv0V1ubJ2-cC58KXOSyMmbHDB0CTU-aqTSBKO7W_F8ZzLSkvDH2vQSD0hJ6Kz2oRUNUkXqe6840LyRj3re8Holizy5omXjH4jPcG5sAoRO0tmXPhVxB5Uh1nx7ItDP9Axfg9la3htNGwu_wInbVYILK6TDhcJZIRO0uQ1QgxZSguwRFFgwI4Ac9qMJOJWau3q4Qah9ZIOqxhy-Fn0byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146208" target="_blank">📅 11:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که ده‌ها موشک بالستیک و پهپاد را در طول شب به تأسیسات شرکت آرامکو در شهرهای ابها، نجران، شهر اقتصادی و نیز شهر جیزان، و همچنین پایگاه هوایی خمیس مشیت در جنوب عربستان سعودی شلیک کرده‌اند.
🔴
حوثی‌ها مدعی شدند که این حملات "آسیب‌های جدی" وارد کرده و هشدار دادند که حملات بیشتر عربستان، "حملات قوی‌تر و گسترده‌تری" را به دنبال خواهد داشت.
🔴
این گروه اعلام کرد که این حملات، انتقام حملات هوایی عربستان به مناطق مأرب، البیضا، الحدیده، تعز و الجوف در سه روز گذشته (121 حمله هوایی) بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146207" target="_blank">📅 11:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146205">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cC9LuRxgwPQd4Y4XPyN6vQwNd8JgWPatJdYf8d8f24SFM682WpNg7iwCu41Bl_ts5u1K5r8SPEXZCU3F5P-vMlSd35-qmGEs-u5wOikgmtdiTDHDCNagBqeM_1wokFG19oXTWFdnVb5h7RrEYJLfBpcmubsgLwiFKgcgNjNqqWfHkHKsNO09ShgeQcLFXrQhdGEQNB5DSpRt7Qnl2eVDfucRgo7agFkugLvnTQK9CLRopFvOgj_EqK3pPHCB18bfmDk45FMcV0Svdr-DaCY1LIQjHOs2ufEyFQ8Z25_rm6A00r9-fP79QpUebyCBK5xw-K0blxlxIxRovos6qywLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7CdsD3N6AFIY6wm_MdgGBWGho4DbbARb_VbaCNAEdnUNudaJ2ZW_xo4jtkKqysw3nD7Ms5Ft5zZX2HhQJ7ng7-E9edB_RAEd5ua-7j6iW8JcMSf7m_fz1MHCw9B5WZCQBeRrQTFrQIK0YJOC1VlfDhpmj9n9ge2CH5tuekFI3QppuNEsxCsNiDQWoMT1gFJZ2VrY25Gtr3d6nPjHjUL-G7X0t6fdjn2L4F8w5Vo4ShwdD6qjytLtW4Phc4HrNK3Jaf9xcj1OIZi_nV-1k7BZhKYYPhZRZOc3cV5nBW6ECPGUfgmo7aF_CVmbqT1gY68lE4orKLU1Spva1DHSLX51w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پالایشگاه جازان همچنان در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146205" target="_blank">📅 11:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146204">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b51a6424.mp4?token=ZhFm02DkfHhh1BdwolGSLcNNtc4dgAzdnKuZDpwzTmhwmATSyPnRp-B2qF0AeALOmcogwXPtbuSO4M1NJVtYgaG7LFYoepDCm-y8LSAtyVlBeW_RbaPfFsRZMfZyXrtx8jPVCUIf0XjKO9RG-EFhhfOjJy81vpDHuofmvWCmvgmoO6dbzBgJkI--FzEl5CXMPc57A_3cuYY67T1qxn4xAOB8Y08CQ595yJVRzB4Lv7xzKNWQ4U9gEwECAfJQTvjxquBTnvkcXhEW5kh9euUe49D14HK6j1KOqUh4Ot7fsTWI9uFlPSdbQ5PnZCEYRwyVFkGmlWmIePXyZdCNGU634Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b51a6424.mp4?token=ZhFm02DkfHhh1BdwolGSLcNNtc4dgAzdnKuZDpwzTmhwmATSyPnRp-B2qF0AeALOmcogwXPtbuSO4M1NJVtYgaG7LFYoepDCm-y8LSAtyVlBeW_RbaPfFsRZMfZyXrtx8jPVCUIf0XjKO9RG-EFhhfOjJy81vpDHuofmvWCmvgmoO6dbzBgJkI--FzEl5CXMPc57A_3cuYY67T1qxn4xAOB8Y08CQ595yJVRzB4Lv7xzKNWQ4U9gEwECAfJQTvjxquBTnvkcXhEW5kh9euUe49D14HK6j1KOqUh4Ot7fsTWI9uFlPSdbQ5PnZCEYRwyVFkGmlWmIePXyZdCNGU634Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تو شب نشینی خیابونی برای مجتبی خامنه ای تولد گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/146204" target="_blank">📅 11:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b78bcc6b.mp4?token=NNAQYqc3rTHAAGo9jC5N354RI1--Y7gwORH_DBxqGya9Zwc5lhBabuE8Pv5GTdTjt7-nSc8nGJFsTIWliXH60aTLAK8-_ey_Li5xDDQ5h6jWgqEnvwkvVsGR1lOvCkfai_ayHDwle-99RfG5KL44sQY8w7i_xKQOgb4IFDkRINZ-W65xgkXHfjBOPZIkA7QCjfVKUfx-6bKkgiRdIJMzwLicqtiwcSjhzplaPxeJLCpXPPJs0xooU3LscUpaaS51kraFujJsCdHPKwlk3hV9YQ_CeGZIoQXiK9mqhZCAJDbyjm89vlj0ZdOW7ca3JS6Iy_Qxofzi4S4U0oLXm79LjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b78bcc6b.mp4?token=NNAQYqc3rTHAAGo9jC5N354RI1--Y7gwORH_DBxqGya9Zwc5lhBabuE8Pv5GTdTjt7-nSc8nGJFsTIWliXH60aTLAK8-_ey_Li5xDDQ5h6jWgqEnvwkvVsGR1lOvCkfai_ayHDwle-99RfG5KL44sQY8w7i_xKQOgb4IFDkRINZ-W65xgkXHfjBOPZIkA7QCjfVKUfx-6bKkgiRdIJMzwLicqtiwcSjhzplaPxeJLCpXPPJs0xooU3LscUpaaS51kraFujJsCdHPKwlk3hV9YQ_CeGZIoQXiK9mqhZCAJDbyjm89vlj0ZdOW7ca3JS6Iy_Qxofzi4S4U0oLXm79LjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بامداد امروز، بارش کم سابقه و سیل آسای باران در بابل
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146203" target="_blank">📅 11:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رییس کمیسیون برنامه و بودجه مجلس:
مقاومت هزینه دارد و مردم شریف ما صبوری بیشتری خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146202" target="_blank">📅 11:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خبرگزاری آر تی ترکیه: آمریکا پیشنهاد جدیدی را از طریق میانجی‌ها به تهران ارسال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146201" target="_blank">📅 11:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
حموم بودم برق رفت! خدمت آقای وزیر نیرو
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/146200" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-pPzclf5GvqVfZ-XHNvlwoUa7rnI3bFIm2AQJawRuZJr3KqW45rmkLkoISjuivreDjJxmm8NmZb8u3LTzGSzhZ8S-WpbCEGppY-MRgroikhZ5i5LTw09Dg8xDAd4PaMN2FJmWWJrBSxqp9dc2OMwsdxGL78V49M57F95Exvv5kZ45U0rtYD1GylC7n07xHNDFrkn6e3M_BdZjSLq1YSV0iViAa-qqKz7ocUC0RuBacmnaJlu6oX3NUaRjSxpcvTkkd8T8pTWEw4aD-Wfh2Jc_tTgRpKvimQAs5hfqe1MS2a0Dw0qc7ATPP7syTtImnOOYDRzmgnSEBV3w_XUrJIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی در یک نقطه از پایگاه هوایی ملک خالد در خمیس مشیط، در اثر حملات یمن، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146199" target="_blank">📅 11:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مسکو: ایران خواهان ساخت نیروگاه‌های هسته‌ای جدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146198" target="_blank">📅 11:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMtBxBYks4MuzfA3EWtm5Q8touaehsPBxCdJ6E3IzVMUXWFaXwc9-krlMUNTqzOLFcMUok-j5_1AO1OKU3ppA03tgneiJ2NOMBFQSmB4t4pJEBHHvoiVu1L_pqaCyeZoPmgQLni8dFs9vthvaXWmHNTl6SUnWI5TQJ_ypdY8O3iNdXlzSA85_A52bD3IzhdmTCMlxBUbOuJyskFyj47xY0QC7VAir2RPX8lovIpdYwEEmG6R--eWkbY_XbgKVysrn-4_fz27xNtzUUVDcSeCzs9lfh4039E_5mV92Kmw2j-gZ9ldqCPnHTs7oMTFYKsMM1aOzlkKDqm4nMDkGdCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که نیروهای یمنی به انبارهای نفت و گاز در ایستگاه مرکزی تولید برق عسیر در شهر ابها حمله کرده‌اند. این تأسیسات، منطقه جنوبی را به انرژی مورد نیاز تأمین می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146197" target="_blank">📅 10:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIuW47-KWW4ywRUQjHI8hG_4XmY6If6YMWTdT2PkFiv1MilTnk0Q6zGaN1GLrn3FcozMZMZwbhWYrglLB5Q0X2_nKQILkQbjD_5VsI_10W2XE0SPg_hWsG_Hj4poHXsXOrWxeGmwdKlVLIUg6TGyf63kHK7FU7gPh6pDK8mDN1vDFA5dJO4v5aFul2zg5gQyej58kdtjMXeCaCAbxCJNGlqR53N1jBu8M576p98t48MnqLGdDRgx9tGZ7KgWwRC1eDqZpYYEC94zf10WOVtGjf0P9YL5PyL_qn55BuHzUOrYQ2vkjr2HOKZ2J8cq9ps3Ykcdqi17OzASWXWX_qCR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهران رجبی:
گرونیا مهم‌ نیست! مهم‌حفظ نظام عزیزمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/146196" target="_blank">📅 10:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHNSZZXcYdeEuN_opjyEE7IAZSXyLyEO_6TccGsQfhXpShDn4mUsDm8InHhY8UjcDuixXi5XncNxYOEwuqmGAGj6Ru7SrfldGuZDssAd_enak19376etQSDfnYsPXKGE0rB1mcUxLpLwRyRGRqlenMDzazOp8YiIR0IPtOGvzoWTn27Xh4crpSrI71-UURbFdvfV9PWIeov8k5LOxOftAvVRN_yI7oNLsPGX-Nz_wgXk1UykCmauQBeJg_skXC6GLHuiQ6J5NQF_B0tAWlTwiu3mNNtZHerp-bpCRAWRJFOj6UswEujHIe4p8iPLp-T1Qu2o95nlrzw-Zk_5WsaoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی کاربران به برنامه پیام‌رسان تلگرام در کشورهایی متعدد شامل سنگاپور، آمریکا و هند با اختلال روبرو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146195" target="_blank">📅 10:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146194">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیکزاد نایب‌رئیس تحریکی مجلس: به‌خاطر حجاب در سفرها دچار تردید می‌شوم که واقعا اینجا ایران است یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/146194" target="_blank">📅 10:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146193">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کارت زرد مجلس به وزیر ارتباطات
🔴
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح شد که نمایندگان از پاسخ ستار هاشمی قانع نشدند و به او کارت زرد دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146193" target="_blank">📅 10:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc77723ed.mp4?token=ff1o0qrbZOjpT3Z3Es_HXEAkDK5l6JSkuCNcheC0amJPo53Y_i4bG5dj2FsRVbRZK3eTSMbDaUTfWCIxNXdQUJV81fyW3MMzdYxNRq40keeq5iMdU9UutYpkf2PlvEJxLj-x7GS6oXFr73q68j1EcI2D9P72gpRJQKIJiGgsP9YU6UO3awcdRxpgbO-DBetwlupzswuSbeTgpAnARasJmtwWArD4VZmsgWMNAaTfSvUeIVTN0jAGP82k5Pvz9WEMfwk1y5gwzej_VquFk_4R0FaRj-8pfSa0WqbbcaZr_GcEnqgyC35bGc_MpopiayYMKbSYNQxcOj5Wk_U3JsJOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc77723ed.mp4?token=ff1o0qrbZOjpT3Z3Es_HXEAkDK5l6JSkuCNcheC0amJPo53Y_i4bG5dj2FsRVbRZK3eTSMbDaUTfWCIxNXdQUJV81fyW3MMzdYxNRq40keeq5iMdU9UutYpkf2PlvEJxLj-x7GS6oXFr73q68j1EcI2D9P72gpRJQKIJiGgsP9YU6UO3awcdRxpgbO-DBetwlupzswuSbeTgpAnARasJmtwWArD4VZmsgWMNAaTfSvUeIVTN0jAGP82k5Pvz9WEMfwk1y5gwzej_VquFk_4R0FaRj-8pfSa0WqbbcaZr_GcEnqgyC35bGc_MpopiayYMKbSYNQxcOj5Wk_U3JsJOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاکر بوری بلاگر آبادانی به دلیل شکایت موسی غظنفرنژاد به ۱۴ماه زندان محکوم شد
🔴
شاکر میگه اونی که اختلاس دبش رو کر ه ۱سال رفته زندان اما من که قضیه رو گفتم ۱۴ماه؟ همچنین گفته دوتا باجناق لواط کردن آزادن اما من که گفتمش باید برم زندان؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/146192" target="_blank">📅 10:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146191">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ea4f701f.mp4?token=l-TFw1Ul4VXOapFF327eYi8J-jkhLWnaNMVT9PzPO7ATQnWml7q5XbIvGsIudGWgbEsIiE1ujomKJuT7topbGL8tSaAExfYsE8ynef0cZc0BhPvtyO30FIxkpF5Yf-EmnRTcwlyKmsSl0YPLG6k98gNRMGumbSPLVWBhy7HFLenO6YLzvJRbtt6cF1DYww-7Vu-h2-B9x3Q4p0a5FHQTDprzpnOlTL7jvgMYpuTrycfY-lkosicO5to6niUFTn9CE2-9MFA9y38cZZ--ezaO40Y_nnf1D6X3WJcYctmZrBzPugE97Az0yYwHXlZeKcVOI4YFwVXP_yn8QnTJ4x-I3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ea4f701f.mp4?token=l-TFw1Ul4VXOapFF327eYi8J-jkhLWnaNMVT9PzPO7ATQnWml7q5XbIvGsIudGWgbEsIiE1ujomKJuT7topbGL8tSaAExfYsE8ynef0cZc0BhPvtyO30FIxkpF5Yf-EmnRTcwlyKmsSl0YPLG6k98gNRMGumbSPLVWBhy7HFLenO6YLzvJRbtt6cF1DYww-7Vu-h2-B9x3Q4p0a5FHQTDprzpnOlTL7jvgMYpuTrycfY-lkosicO5to6niUFTn9CE2-9MFA9y38cZZ--ezaO40Y_nnf1D6X3WJcYctmZrBzPugE97Az0yYwHXlZeKcVOI4YFwVXP_yn8QnTJ4x-I3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند روز پیش تو سمنان چندتا دانشجوری عراقی حشدالشعبی به یه دختر ایرانی تعرض کردن و جوانان سمنان هم اونارو گرفتن کتک زدن
🔴
حالا رئیس دانشگاه بیغیرت رفته از این عراقیا عذرخواهی کرده! و کم مونده دختر خودشو هم به اون حرومیا پیشنهاد بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/146191" target="_blank">📅 10:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_eHcDxawDxRtXCp5cNGCZB55V2L4PDwI7tIuFljyM1TBHQMpfMmMT3kjbWGzd8gLZJGUfRoYa0t1antI_2TYQEIMQkFOKbELs4uTS9yQcasc5N-GbirqGX3yCFnYOc6o_EwN9-tYrdlp5e21qNb0JKJ2qZ05CE5Ch9gF7FBN8bF6ZQJBwQCfesC7fcZph9XVvx2ZVxgoH0UJ4A4cM5idX7SeU_N5Gff0AUPGfG-EeYbvXIq3Z5tHJSGikrl9z0b33I0v-Z4qdjD28m0sumYezZmMhD83uPvaXunkr4B5JQq20YUvZ1lFz63ww5XUIRgaHQRkZLATc_l_lg5lRzOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی در کارخانه محصولات نفتی شرکت آرامکو در شهر ابها، عربستان سعودی، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/146190" target="_blank">📅 10:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAaqzVfFOQFvh0MHMIoRgzY_cg4Cv41Pq0XJst06iydI-7JkuDM_2TnJsGF-GV4ASMUwje4goJRJTHMPnLPNKE1iYVnH673o0Cg_QkhwMvbE_lIsWcTwlw_hdJqm5hSICsHxKsXEWfWQ9CZhUd86OB3Yj9eHQXFA9qjLE2cIYFyc7GIF_CTAJXLfwYYQmPvmDHE3r-OEd7IL45CvC9PkqduHJN2BjzHX3NDLYMGTN3x1gPal-stuAvts1Fu-Knf9dNhDvo_jRaJJmj7iUCtiZYrq8U9UjgPjPy8RK8VjdywTOt_dv5dU1x99JBUrgTFKumy1ty0Vx-nqZIANsHp7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در پالایشگاه جیزان، عربستان سعودی.
🔴
تصاویر ماهواره‌ای نشان می‌دهند که آتش در پالایشگاه جیزان در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146189" target="_blank">📅 10:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146188">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde6ff7c1c.mp4?token=PI64q_fIuDuQTNoYBT_hEgkWltGEx0Q_GOp-6TWAGr69X_upS6t62-N76HcytuTB95pF5opJwn2in_FvB3t764N5-5VbLMj4a3geOLMOt14BEX-0hiT6o6ZULvOCRxB-XzA04H6-tfxDXQN1DI-s3dvFk0-vxOTw8j8eQn5LjIfH3roynscgWdugHIRMPIjTiWliRycCSaxCLfdkXFJKkAVVJcYIUnAJZRH67f5ulHlnx5tfr-fEWXRxYE7GqgOcblVhzZ-Q4ts3V-ul4OakVVnlSVDfuZBOS4sHRsQPPn6EXlNDHEvAcLixH9KMo_s4Ty4iqJ4vQM-Y2EMTBcaYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde6ff7c1c.mp4?token=PI64q_fIuDuQTNoYBT_hEgkWltGEx0Q_GOp-6TWAGr69X_upS6t62-N76HcytuTB95pF5opJwn2in_FvB3t764N5-5VbLMj4a3geOLMOt14BEX-0hiT6o6ZULvOCRxB-XzA04H6-tfxDXQN1DI-s3dvFk0-vxOTw8j8eQn5LjIfH3roynscgWdugHIRMPIjTiWliRycCSaxCLfdkXFJKkAVVJcYIUnAJZRH67f5ulHlnx5tfr-fEWXRxYE7GqgOcblVhzZ-Q4ts3V-ul4OakVVnlSVDfuZBOS4sHRsQPPn6EXlNDHEvAcLixH9KMo_s4Ty4iqJ4vQM-Y2EMTBcaYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چهارمین فرونشست در ده روز گذشته در خیابان رباط اصفهان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146188" target="_blank">📅 10:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsgZ7uQf2xRl3wdFhpXgow4dgC-6zp68i4_rKuN9AU9WgasxsClu48DF3ZdTHAQqVpz4tx5XTh4MZjHBHNXh-Rzj7Mzww_LGT-2LigcD44TyAME7bwn1e5PUnAc_xnOTBy_hbpkRYnIIwkHRHEYWxMJn4mlLOM4hOCMwTyAbScfr2C6AcR6lqUcn8RjtkR-hmLC-vIbNTVUYp1mTV9qRfp7tP4EFbtX5lH8je1o-mUGPAUWA5-hvNiYU9iQld4MyPUrXabI9gTP3JT5nzGRl7BeG_5VX5OLJgDZi_ZC5PuWSKRFj3GzFFDWh42y4OTxCCZLP69qHG1LblJkd3ts_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) طی ۲۴ ساعت گذشته ۵۰ حمله در سراسر جنوب لبنان انجام داده است.
🔴
مناطق هدف قرارگرفته:
🔴
کفررمان
🔴
نبطیه الفوقا
🔴
عرب‌سلیم
🔴
دیرالزهرانی
🔴
زوطر الشرقیه
🔴
قنطارہ
🔴
بنی حیّان
🔴
نبطیه
🔴
ریحان
🔴
المنصوری
🔴
تولین
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/146187" target="_blank">📅 10:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTfinooXkTJPK4BUFb6FkyS3UQm8812SpsdX3_O8_bt_LOABkcxTSbIYvMs5owxd6_NJSkofzwQAJFeVs3jQzQnoOxyI6a-FyRVqMBa9rfU8ZRPPrMSUzjNoRBsvMTDohW6hL7uWKot2uYBX_qf22oNSV5Vg6pnP7e1dMXgm9tjosrzKcYAd7f9Lj1CvJ5CnDOpprIv0rhCOynhJVnzlWi64GbOo0ul0pDh_cMfLpr_yphT5Vp7gT4n2as5qOCb135HdYTLhWJT9ebuXixhhiC053Y-q3Bc5TlJbzC8DlC3Lsjx58hdStIBRWcCNd1k1HXtEtLwnFtGBdtxJLMdLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی تحلیلگر نزدیک حکومت :از دست رفتن جبهه یمن، موضع ایران را در قبال امارات و عربستان تضعیف خواهد کرد و نباید اشتباه جبهه لبنان درباره حزب‌الله را تکرار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/146186" target="_blank">📅 09:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGeQfyZ89mGWevg-9Fx6XyC4fZABfSjvp2R26vqo2ahv_ytXZeqyTEhiFT1CNBE1w3SHxdL22VPebB_b5D7SYjP29JTWFPGlHGnounJFAYeNizthP923T9zHxmBglVLsh0gNFgxac8XJKSmV9I-1VQyYVbQ49eY3dKDhc7_G6kW41RWHMO8teRo58SrF1KuVtMHOI6AS4_dD1E6c9Vms0e47p8kdxYIzsdEynHs3x58CyQPwBCxK1mghYNb7R50qNYnSjxahGMIkshyqBY9iGTJVGWmHQpGlG_7gyO4yJllzGFAmSzIe6V2yYBka8EL83wund4KwZuBpYNn7aM5dzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ابطحی به نگاه غیرحرفه ای صدا و سیما به اظهارات اخیر حسن روحانی
🔴
صداوسیما حتی یک خط آن را پخش نمی کند.
🔴
اما دریک رفتار غیراخلاقی وزشت و غیر منصفانه کارشناس های جناحی و افراطی را ردیف می کند، تا علیه بیانیه خوانده نشده در صدا وسیما، در صدا وسیما فحاشی ونقادی و توهین نمایند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146185" target="_blank">📅 09:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نفت ۰.۳۵ درصد افزایش یافت و به ۹۷.۳۴ دلار در هر بشکه رسید
🔴
قیمت نفت به روند صعودی خود ادامه داده است. معاملات آتی نفت برنت تا ساعت ۰۰:۰۰ به وقت گرینویچ، ۳۴ سنت، معادل ۰.۳۵ درصد، افزایش یافت و به ۹۷.۳۴ دلار در هر بشکه رسید‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/146184" target="_blank">📅 09:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IouVngmucy_d6r9KrftbiDWLxuuDpbtPAUFhuGwZAfr3Hx6Uum3YMDFOu8kFQYk4dhQbA17lpgSkHVrI5OkGf_8fu4uDhmLwUYmMMo6n12N-QzJy3nDC6ZSGmEP7kCC9tAufRiC5X7lLl_wYURjU-9rkNq0Ojo9OVgUhzFMw1mBu6-wsJgXb2Z3oo5-HCeuTycOCc0fvMVpxJIyjKzcppDrBb5qWgSn64f7rgblsWW7VJvpsz8qfs046XCS__vFkr4dp22HF3WIWtHSRM3RKWDEWJjXnFc0xjo82baWi2KTvfzPpAHiK_4uuXQaAr9nmjdR98n0Big7SOYlkp5uSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش روزنامه هاآرتز، رئیس جمهور امارات متحده عربی، محمد بن زاید، حدود ۱۰ روز قبل از ۷ اکتبر ۲۰۲۳، به نخست وزیر اسرائیل، بنیامین نتانیاهو، هشدار داد که رهبر حماس، یاحی سینوار، در حال آماده‌سازی یک عملیات بزرگ علیه اسرائیل است.
🔴
در طول یک گفتگوی ۴۵ دقیقه‌ای، نتانیاهو پاسخ داد که حماس بر روی کرانه باختری متمرکز است و به بن زاید اطمینان داد که اسرائیل برای هر سناریویی آماده است.
🔴
بن زاید بعداً هشداری مشابه را به ویلیام برنز، مدیر سازمان سیا، نیز منتقل کرد و گفت: "به نظر می‌رسد اتفاقی در حال وقوع است."
🔴
نتانیاهو، به رؤسای سازمان‌های امنیتی شین بت، موساد و ارتش اسرائیل، درباره این هشدار از سوی امارات، گزارشی ارائه نداد. برخی از مقامات ارشد امنیتی گفتند که این اطلاعات می‌توانست بر ارزیابی آن‌ها از نیات حماس تأثیر بگذارد.
🔴
این هشدار، پس از هشدارهای قبلی در ماه سپتامبر صورت گرفت، زمانی که واسطه‌ها پیام‌هایی از سینوار را منتقل کردند که به یک "زلزله" قریب الوقوع اشاره داشت.
🔴
دفتر نتانیاهو این ادعا را که نخست وزیر، هشداری از سوی بن زاید، رئیس جمهور امارات، دریافت کرده است، رد کرده و آن را یک "دروغ آشکار" خوانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146183" target="_blank">📅 09:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146182">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smwJFg0q1JC1yNn0Gfssvgt5jDy7vLJQ7ku1XH6lpd1uv9qpc9PaEayxj25_vLq9uVMshyvw0qFFVrSHWLwYs_tafyG_L6EDiX0Nq_P9C9kGMpnXLLisZ1avOCMBhCw3n-S8qph8Z9RxC5aBaw-VO9YpLgAhz4xO5oNMSa-M2RZVq0Yy15pfzVshKKyHIcITlmKPLF8ZsLhN_TeLoflfJtAHL7rwHUg6yL4gmTytlmtW5x2C3Ct2lihsIftKVpoS7MkP35TyiKcAA-hDILDBlq8jTsmtrzwYsKcFieYt5POlqjtUQWr0B57Vt-j6W7CmSPaV8xdbbeaDQCUdtBmD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی:
در روزهای اخیر، واشنگتن هشداری آشکار از سوی موشک‌های جدید ایران دریافت کرده است.
🔴
جنگ اقتصادی با ایجاد یک منطقه ممنوعه دریایی در سراسر خلیج فارس تا محدوده محاصره، پاسخ داده خواهد شد.
🔴
وضعیت عملیاتی در قبال ناوها و پایگاه‌های آمریکایی به طور اساسی بازنگری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/146182" target="_blank">📅 09:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
داده‌های کشتیرانی گردآوری‌شده توسط شرکت کپلر و منتشرشده به نقل از رویترز نشان می‌دهد روز دوشنبه هفت کشتی حامل کالا از تنگه هرمز عبور کرده‌اند؛ این رقم در روز قبل هشت کشتی بود.
🔴
این آمار جدید نشان‌دهنده ادامه کاهش شدید تردد دریایی از این آبراه حیاتی در شرایط تداوم تنش‌های منطقه‌ای است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/146181" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت انرژی عربستان سعودی اعلام کرد که چندین تاسیسات و زیرساخت مرتبط با بخش انرژی در منطقه جنوبی این کشور، مورد هدف حملات حوثی‌ها (انصارالله) قرار گرفته است.
🔴
این حملات باعث ایجاد آتش‌سوزی و به طور موقت، اختلال در برخی از فعالیت‌ها شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/146180" target="_blank">📅 09:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/146179" target="_blank">📅 08:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8osYrdaY6hCLhkhMJXF3EYyzmpi7YBZ2gzoT6NZt1a5td8qKy9P5cYj0TwmfN-kVofZVcAevoU1yBI4lbmcnC9qNV2OCTI7uMXPHR4Bga9MZaTNf3AlhPl3J8Uh569HKAEOszoGnHDc0bh_g7ePL73JK-07UnhndHzjBhb6vzZ0wYYLMR-gqNK3ejXUNUoG6xr9PnoPGXMTtKie7rymujiiNRbV1jGMjmna2Fpi5qfTyQYcVhsr3DcXOOjR2y4PyydBMjzC_e-Ekd11uasZUd6FKM2_LjF-4lb0Vdz_WaWf1Wzd74QeJUkm8x9_y3Tg9fxMFXYdl12oJyOYz7Qqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتامار بن گویر، وزیر امنیت ملی اسرائیل، از دولت اسرائیل خواست تا تحریم‌هایی را علیه بریتانیا به دلیل "اشغال" جزایر فالکلند آرژانتین اعمال کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/146178" target="_blank">📅 08:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن ایرانی اسمش فاطمه حقیقت پژوه هست، سال 1381 تو خونش خواب بود یهو صدای جیغ میشنوه و از خواب بیدار میشه، میبینه صدای جیغ از تو خونه ی خودشه، میگرده میبینه صدای جیغ از تو اتاق دختر 14 سالش میاد، درو باز میکنه میبینه شوهرش لخت تو اتاق دخترشه و داره به دخترش تجاوز میکنه، از شدت عصبانیت و در دفاع از دخترش شوهرشو میکشه، تیکه تیکش میکنه و میندازش تو رودخونه اطراف تهران، پلیس میگیرش تو دادگاه ثابت میکنه داشت از دختر و ناموسش دفاع میکرد و به 7 سال زندان محکوم شد اما دیوان عالی حکمشو تغییر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/146177" target="_blank">📅 08:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه آمریکا به الجزیره گفت: ما در حال هماهنگی با شرکای خود هستیم تا اطمینان حاصل کنیم که مانع‌تراشی ایران در ناوبری قابل قبول نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146176" target="_blank">📅 08:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X44QqKkjzrITZtkHd9T87Dw683HEWG8FrNfenJy4XvmA_bJpjd6zSFDcP6kI3sw_yh-kvM1kqA0-zIb0QuKxJQ77FH4uTtPTKLspa-uAdGF-HoUdX_d7-6le5lsAjTwrM4T40mIZ5HuPAuOcXSCqZ_76jBNr86Vk8Rl7tqlfIAV7C6ubB4tBBra034q_FedMGUpyJdAWNCMEN1KPWi6oYTbC24ZCf5Z0P4uF2BqxH3r9SvkJ9qild_4fBY0-AbB4OgbB3hcBkntqk7hFikBc1qm0u16djAxd7fm-tG1uXhg_CgFZtZFIfBPRC_smqADz0YOL4bfWE70xa4pZaQjZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز پالایشگاه نفت ساراتوف در جنوب‌غرب روسیه را هدف قرار دادند و موجب وقوع آتش‌سوزی در این مجتمع شدند.
🔴
پالایشگاه ساراتوف از مراکز مهم پالایشی منطقه بوده و در ماه‌های اخیر نیز هدف حملات پهپادی اوکراین قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/146175" target="_blank">📅 08:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ اعلام کرد که شرکت هواپیماسازی کانادایی «بومباردیه» دیگر اجازه فروش محصولات خود در ایالات متحده را نخواهد داشت، مگر اینکه خطوط تولید خود را به داخل این کشور منتقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146174" target="_blank">📅 08:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjuKWL-fsiOe__cjz-wFGCHWLOCQgfTtRtN2ubBm3kXkMqEsqA7e9VeIrPIHYvBYUBHCnFY65D4ztGKE4jYZ_J5YmUBwQCHmPdP6NzJ1LTiLja1Gyca4skwUT4XuBitY9KsUnlZIPoxjNWBko8URxjRxqlt6wv1LJImv0tEoF2jjlZuoX5iQY-N5GHFrj68idotn2OIBXEap-5WZ7xapFRuuMbmSbaM8cqi8S8RdPilParcynExnv_XZo5UVZZ7JTeUW34bJ4gBktvHU3XTZNN-AeG3quidKRbqglDrkALepP2de3JTRbjS8xjDVEJnYXs4Cklj811oICvofSKMOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانادا رسماً تعرفه‌های تلافی‌جویانه‌ای تا سقف 50 درصد را برای صدها محصول آمریکایی اعلام کرد، در پاسخ به تعرفه‌هایی که رئیس جمهور ترامپ اعمال کرده است.
🔴
این اقدامات شامل حدود 20 میلیارد دلار کالا از آمریکا می‌شود، از جمله فولاد، آلومینیوم، پنیر، لوازم خانگی، پوشاک، لوازم آرایشی، موتورسیکلت و تجهیزات کشاورزی.
🔴
نرخ تعرفه‌ها از 15 درصد تا 50 درصد متغیر است، و بالاترین نرخ برای فولاد آمریکا اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/146173" target="_blank">📅 08:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTi_rHQR5Gcw01KnYaTIXzZUjSvuKombOSQXHq4h-OEvjG1xzr7U2UsQqWLjRbwJls8aHQMbzCd1fH79bpGDFS7Fn32gSzuwjpxmqDp0byXInjIx5XF2Avwf8A5Wvrt0s-DTCrFRCbv9n7oNl_fiqw0ZxWCtjjz7NfcNVjjQaCEw61AH6ok5QQmGBaKtbm2dYpgcFha5ndNouAkZahlie5e-KPK-qdRY7AjByUt-l4vqabPPZoAONP-zbqXcLTLRUXQPWqn8T73rYXy09Lp0PG0FGZrqkBj3yKE5z3gvBI_aGjHtaXtM9-E0xd-npo0im3uXiLWXwEDulzF-sTHbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت نفت به شدت کاهش خواهد یافت، درست مانند کاهش قیمت همه چیزهای دیگر (اما بیشتر!). زمانی که ما در جنگ با ایران پیروز شویم، این اتفاق خواهد افتاد.
🔴
قیمت هر گالن به سه دلار خواهد رسید، اما در نهایت، از دو دلار به ازای هر گالن کمتر خواهد شد.
🔴
این اتفاقات به سرعت رخ خواهند داد و ایران هرگز سلاح هسته‌ای نخواهد داشت. ما دوباره آمریکا را بزرگ خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/146172" target="_blank">📅 08:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چندین اسکادران جنگنده اسرائیلی به همراه سوخت‌رسان‌های آمریکایی در حال پرواز به سمت یمن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/146171" target="_blank">📅 02:22 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
