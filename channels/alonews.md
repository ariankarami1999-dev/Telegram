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
<img src="https://cdn4.telesco.pe/file/M6Ie8xSixTc1Aw5onol_Ny4Z6LVAEz6I9lsFxDZW1crsh6AIbX2GeYg89_7fUnrEH4d4IxftbhAVwj8w6QxW8TMVhwiIzyMbsEr06YSKMGkEfqBOe3OzO_xzBlHHFxxbzh67hZB_BzsdAvYRGnxV9AAqa0shOW40QcSmz0Mp1fPK6iRyX09ctWIXIx0W_wkFlV_YIeIFZ9QysLDwBIhSxAmMI5yRE2HzeE6Ir7swtADjiFbvywEfk1twvbybh8ukKTyQm0X8cB6fW-KCOeE6Ap6dgeu1RMfbVj8hUF-gY7w_RgV0_jokmfsm5LhEkFtFCRkR1547hEOU4NV1HqsWFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwNRcRI2xZGh5M7PkhvqDWL7PTrTNb9Asm0_PDSAnc1JoLzgd335pG-yaDPJhduquyIzVU0XVDhyex3Ua4J-2EZeeKQyGt1iJqI9R4V9eS4iqtYcJE98z-I13lsTnIr0WBMYgFXyBQouOH5o7hUKYxq0RIQVHA0T33q1A4mokK66GjvZO3yfKVOeDhv7qwE7j_ShHqNjjNEsK1FWmKzTGUTyxi99TePpacb_WgVDXMqear3xmX2blBlJ3acR3QI8qgpX_Si8dwed2A9zpX_E2EXJRquQXBaOM9No1arBvhb74Ycj5pXEO_bxbBYALzsTNLwQHqtPlLkXkaDoNAPY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKKymkDjYtSSWGp0Xd-UGLArphowzzQDc9zFRHx4V0zIv81jBrSrOUceWngkwgZvt49EBJIhWlEzZb9SZcXIONfHZkJx2ZC_MY7gyo7hxbCprEyr0HnDMVv5zpRTNzdy49GaFbD7Uav6FFXT9YQRKz8ufR7J-oSb_kgI72otP8vi_ctmqnnSaQcXkQF6kXYDmrQGtk1St9p_55c7aPL-ygdRoKdH5sUk0IeB1dXGBuVwLEceEw5q0HLlG04jnoumKfBYQ5mrJySzLDX0rlT0V9klKNvhjN-V0j2PgrucMMPq3zDyt2xtzqSNAeEmzYcZf1bYq_fOnyIL9s9TBtNcbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعد حملات مشترک آمریکا و اسرائیل به پایگاه هشتم شکاری اصفهان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/132176" target="_blank">📅 11:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودرو در نزدیکی هتل محل اقامت ماکرون در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/132173" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGozmNsWCD1jWO3aWRYZnKqoIpTn-D8btYIziEs76IZIIQ1tvpeNACulOwt2XmNqgRFfIYvOL1zGu7wQlzd_L599AxmcI8ndBXAbl_fI7OGacHaEf20BtLTGzPc_EEBeJKQ1DISjZTnblrQiPr8q4Nq8Zk8n24CIHxWKWhsJpGFBHJ58XX72oxfVzSJ_p9OTpZ3zXzoM5Ka-oERyEJZd5uwQmLrlkS1fVxAXoRvhz3AJmgYBgyozs-dj6yhili_3eg-upGVnl6rrTuVbR8_x-mMfwj27C7brs58ykTnszlv_uVkNx3r_j1Th_NEQZreNjtXhvTwE9e4V96hrVmDHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش پیج رسمی تیم‌ملی ایران به شکست شب گذشته آمریکا مقابل بلژیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/132172" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ولادیمیر سالدو، فرماندار منطقه خرسون اعلام کرد که حمله هوایی گسترده اوکراین به منطقه خرسون دفع شده و ۵۲ پهپاد منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/132171" target="_blank">📅 11:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn3JWAm_wLMHpdd-EDeftkMxAgzDkKc4sgePGVc2nVOf2cMdAERm0ot9W5ofyNRHQ11TiHrrGhMS8KLGyKxCfC64SZl2uxgckzeOmlAt3uQuFonCfnVstIvCF293_fjhFp55yQh91QS3LNTzrYIqouIn4hCA8uyMPCuxVniEuaq8AvYC9d91DlHDzTTbuXl5iIAecf6N0Q4wioi6SbfelNA6PMUWFhBbnyqj8kz-QwaDSldbBzUhDm9E83xJ23UQvkWlSafDxLUm3DiyYp9jE-F29DP76xv2LfmfH6C7d6-aJgKZ4O2JtPDf_Fz58VbCyO4VAMy0Kn2A05yYb_dRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132170" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/132169" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/132168" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132165">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/132165" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران ایران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132164" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سفیر اسرائیل: دور بعدی مذاکرات بین لبنان و اسرائیل، ۲۴ و ۲۵ تیر در سطح سفیران در رم برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132163" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJHkfYQtOqoKpaIetWaAa4vGwoR9oxiz04-63g9M1snTjKHSDJgKEuJW-XWVpdcw7s0qpBxehH7SK9BxtbkJDwWzawl7rxEIG_DFIMSN-VTfBkGQSEj2Dwx2jnlJsjBMrmQg1RZDWOEcI9ZY8jjPmw1FkBL0pd2tgfXDiSwjwgNEf4JpgyTR0gA-cfpm-6jlMu_DBo35J0Im9XP4x57umayUpm36Ck534ghdwVniHe6A6z4w47uw03fjuh_ZXljdCsyFblGnO9-visVT-9UlrKNdWMXcZBMUrIvLsClkgUA03byoCvXmzuNgWFnDqU4GUPNToijHV449MnKhEAhxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون، رئیس جمهور فرانسه و احمد الشرع، رئیس جمهور سوریه در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/132162" target="_blank">📅 10:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع آیت‌الله انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/132160" target="_blank">📅 10:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرگزاری «رویترز» به نقل از منابع: عربستان سعودی در حال بررسی امکان افزایش ظرفیت خط لوله انتقال نفت خام به سمت سواحل غربی در دریای سرخ است.
🔴
عربستان سعودی، مذاکرات اولیه ای را با برخی کشورهای همسایه برای کمک به آنها در انتقال نفت به خارج از تنگه هرمز آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/132159" target="_blank">📅 10:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Fdla1Qz_EE-aXf6pFHW8p0hA-n21EXyAlTckq-2_E4tTCbu_h3MzvdOE0FZS2JDL9C3DNQmHHTK_PgOP78NwkgPxI3GuVsLr0THdhlfJe7kHAxswq6wZXwfEnbKPslXCV7xlpkVaPVXB4EXhzam4sFo0Iq5CBSDnlrwo-X5zVim-DqKbPVPJpPNIuhxCFrgOt_W_T-86H2lpZkM6W-b-N1jb8ibWr5eDTnJIVA23rOocr3E0Owe8jQiA5tkD-qLwP96x2yditnZ30Vy6pxJoYuXlYzkBY8XiBUFIwPp0YO38QN-Ntdm3nfQZe1ZlJvFPlL4lr0sgMftCrkGavDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی: بدون سلاح‌های هسته‌ای، شما دیگر عضوی از باشگاهی نیستید که دیگران از حمله به آن باشگاه می‌ترسند!
🔴
در عوض، شما عضوی از باشگاهی می‌شوید که می‌توان به آن حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/132158" target="_blank">📅 10:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز سه‌شنبه بازار جهانی، کاهش یافت و پایین‌تر از رکورد دو هفته اخیر خود معامله شد.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۹ درصد کاهش، به ۴۱۲۶ دلار و ۳۳ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۷ درصد کاهش، به ۴۱۳۷ دلار و ۶۰ سنت رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/132157" target="_blank">📅 10:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/132156" target="_blank">📅 10:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdoxZ1kw3iN50lYINd9LC3HPqGXnl26_5VBC6Zid7mw4guNH-zzWjzVx52CvQsFo4qFrAstPKmzn7cCcG1Xs1cXLlmO_zGMHBbLyVfoZKG2OV1DWyD4uKEDOSGwlWcfEBrRptmnsmvhH8waeKyhfXoQS0PJLk25zV0ghX1-sNRD1OFJBkFE9-lJWgELFewZrZ2uLDgxAcvt8wtosz7-1ihCT--m2qZIBMgfE0HGooLQbrp60fyFaWAPxRTq1K3Lld_dFMN-jvmBWHpQv9_0dor_6Zm86RRjcRRCL-GrxAZJpZ6NtdI9qXF8Zc0k221FkyiAhEp3I6PdoUDeBX5SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل ایست نیوز: تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132155" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین بوسیله موشک‌های سامانه HIMARS به بخش تولید خطوط لوله اصلی گاز  در بلگورود حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/132152" target="_blank">📅 09:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSyOx6E0nh42GspToaYe10YFetOa2RCyIo2lcb0mB_nF4nmr4Ywz5yKIWYUu2Ii8pHCsk2MQ5KpSm_CCN696oShexSzDrEUgNF4EhIFAVN1ctzQd5gRjeCf37eaCrUgqaER6gIaoVdJYn2Lr8fK03DlxilB51Y9tgG2NUQqft0ytu04L_s8q4eFGfIpcL5XtoI9iEtvOaRp9JcrR6-gQuFVAjZAFeHqPLKUIn6ARo9OjMRDfJbOM438hpEaMci40xUZh9Cqacp9tue7LFQxMni_HCSOuie7EWIiel0vfTpql3DP6jsdrTvrqieYS3tHqS8NIVHK8zNUaNk5Ritj1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۷ هزار واحدی شاخص بورس بعد از سه روز تعطیلی
🔴
شاخص کل بورس تهران ۹۷ هزار واحد رشد کرد و به سقف کانال ۵.۲ میلیون واحد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132151" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عراقچی: تا زمانی که تهدیدات علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/132150" target="_blank">📅 09:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
واکنش عراقچی به ادعاهای ترامپ: تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
🔴
به امضای خود پایبند باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132148" target="_blank">📅 09:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در آنکارا: اگر شما یک جوان هستید که در روسیه زندگی می‌کنید و به فکر پیوستن به این جنگ هستید، دوباره فکر کنید، زیرا احتمالاً شما یکی از ۳۵۰۰۰ نفری خواهید بود که این ماه، ماه آینده یا ماه بعد کشته می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/132147" target="_blank">📅 09:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/132146" target="_blank">📅 08:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خروج چند واگن قطار باری از ریل در زاهدان
🔴
روابط عمومی راه آهن جمهوری اسلامی ایران در اطلاعیه ای اعلام کرد: بامداد امروز تعدادی از واگن های قطار باری در زاهدان، از خط خارج و موجب مسدودی موقت این خط شد.
🔴
کارشناسان فنی راه آهن، جهت بازگشایی مسیر در کوتاهترین زمان ممکن به محل اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/132145" target="_blank">📅 08:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
🔴
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
🔴
گفته شده نفتکش مذکور حامل گاز صادراتی…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/132144" target="_blank">📅 08:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری /
یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
🔴
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
🔴
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/132143" target="_blank">📅 08:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0f3440e1.mp4?token=b-p2mJWSGr4oEKstflab5_knK-370eYtAthQG-q4I7jMOM4QoRRlHh92NOYnXP5c_k7HI2scGjTg9XQxSOdR9GGiyEnnG-uagxiMYSok-yhnb8f0F7Qx8F27a7UyZcGUPqXJcMk5FAAb97aInc_oTJ5ltZUrWZ6pUVsqtH51Jho0QGf2-t6xc02TS9bkXblo5ZK8jTuCyV2a0ifebJva7LNVau4urPqZ_wWPDyPLfAkmycybWUykVgnTiGzS8bt58rJMuOZeVhkZ1f8dz3rWRwZlr8CwBH94S4GxefpRzsSxqPsQ1C-110-oJLGsqvvleTI7vkDQymQKpwkkaR0vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0f3440e1.mp4?token=b-p2mJWSGr4oEKstflab5_knK-370eYtAthQG-q4I7jMOM4QoRRlHh92NOYnXP5c_k7HI2scGjTg9XQxSOdR9GGiyEnnG-uagxiMYSok-yhnb8f0F7Qx8F27a7UyZcGUPqXJcMk5FAAb97aInc_oTJ5ltZUrWZ6pUVsqtH51Jho0QGf2-t6xc02TS9bkXblo5ZK8jTuCyV2a0ifebJva7LNVau4urPqZ_wWPDyPLfAkmycybWUykVgnTiGzS8bt58rJMuOZeVhkZ1f8dz3rWRwZlr8CwBH94S4GxefpRzsSxqPsQ1C-110-oJLGsqvvleTI7vkDQymQKpwkkaR0vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مجلس قانون‌گذاران نروژ
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/132142" target="_blank">📅 07:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دلار و تتر دوباره در کانون توجه بازار
📣
پس از اختلال‌های بانکی شدید، تعطیلات رسمی کشوری و نوسانات شدید اخیر، ۳ نقطه کلیدی خرید برای حفظ ارزش سرمایه بررسی شده است.
لیست سه نقطه ورود مهم برای خرید دلار و تتر
☝</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/132141" target="_blank">📅 01:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPC5UQ0PG_b6hnEZF6fIyXz1pq27vsPMa3c9ofEZUXCcKJxL4syui70zhTeR6m0nOjPExB_KJCDPcEL74ljF-8cZcpbO-ZryEX6DDvXCxfS0QIALN_pSNSCc2budw_qY-qWx9brvRwS2Z8J1_Ob8zdpSxDssUWiT1WlcAb-qTSOMME_6SPAI4h-6wz95fvsX2vEPftysnuBeSM_vTuKK-ijP4URZ1UQX9-_kUaZfMAs_LG_GTV45Py6RL6uym5i7fk9nptie1iAosN-KQBoeXe-Yj4WV-fhAwMmcMgiC_SRoMKJ6-vWV4eFsu2kQKe5WO2xTXk67jYF5SAHyaPzhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/132140" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8QRneu50ZYQntUwNBT7oR-0tT7FuWqaz9DMmYCC9V-opI3uZC47t_svqlgfw05FsdeOGj3jbByjrAjh3ZMiGEvBXb9gJOtXfmgs4o74CDaKSSE5VF5ceImalltFz45fq1ybAz5GQfNUVG6eQOfvis4DXIH487UKGBs9nAEffzutsFGt2IyNJmpfTeeDPf0iveyPjZ7Zut0jvmeBLtf6b86R4CtkhPCNrBEaqEb2GofTmdbP9MDS2uLa5HC-mNeNX9BCXAXsH-43FaPEIZgM1-sQqV5nZ2QFwoLrsR3XKsRAYVwpUlgF8AiHj8kE52cSXiFkCHm9mtGcn0QTwHCdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عجیب و غریب کانالای ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/132138" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHklvmH1nifSOArtbRJxWudnsGBREh4oz07WUqCxxifgJ7Pfb9-ZkymxN87gIJJ6dwFUEEzEeBfLEAfRgWEbIrCvPdYBQVdOfbEwQ5ujgzk3_pvrRZqGp8rQw6a_KRR1trtl9IP9CMQfPI1b_4KIb_nJq_1BIrse1pbvJeOiUgVa8jz_qGKRMchgHj84iCQtl-hTbinOfSTf2mCCDSedYiCRbtoCg0ulgbWW6t0fXEkfLx-FSQgEYTGR7Ma0PI1Zduk0kXL0MvehV6wsfhopB2euRm_4F0bCnYVGrINM1jsNwDmOtHsNpvMtgzDLX7jyQnBOh0gggtPyex4GAxg6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رقص رونالدو، پایان یک عصر؛ وداع افسانه در شبی به رنگ زرد و قرمز
🔈
پایان مسابقه - پیروزی اسپانیا برابر پرتغال و صعود به یک چهارم  @AloSport</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/132137" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdp20fjbM1lNDxcDNCFfPEkUkJ6O9QmUVHWJTQVJuOKh7DdHbyI_S12zQUR5plXJZZiVd614D7pCGpoTPAD7e04CHRRMpE2VvoJnv_GzXPOGZWryxBniW8kW8GtgW1io2OvTLx-MUGzIdpH6V46ouz07U3QTVIuhB2CRnKfA9bqTjncxEuk8fCBWnJYcXt8kkRRnCA6d_sCVJpi8CCbMMzstmXlBZvarG32B-jIEfMkQULfzsjUiYb8opOdXbdSon5094Rn_Gh8U7ny01jwCN8k-C7c2JyHoJVvQ-VeBSUpJU0R3Gk07r5SPsiSsXEt3kO_lNtEgu-M-yPxyAvGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رقص رونالدو، پایان یک عصر؛
وداع افسانه در شبی به رنگ زرد
و
قرمز
🔈
پایان مسابقه - پیروزی اسپانیا برابر پرتغال و صعود به یک چهارم
@AloSport</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/132136" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=QdcBaBIveFUT_hkhE6m7hktPlvhK_6Mbzvd-fsBjR594ItIMNaRAsoDs9LDEod9feSCDR6MARQ-oIdAXu_sHTcbaf-EvSDn-GxyzLfHi0-KE0p_pxE__lUwaNA2V4JFZolOly1I1dMv-Hul8keFYbX_MeQ_8lFWfhFIMOnp56MKyvcv_lT_uHNxBq6NKKWx5uiJGp-cqZrDLJwm5vM40uRQVOIf2Glwnx5AtwkZNCwmsoDxccFEKzIzhP6qshsiGxo2_Rq0F4q8SZgoA3IaAwxv6pMyvtJSxsqJAoFs6q58v38wpKtNRQ_Jrb_SVJHq4QZI2FRsHNMUPEqf95HITIhn1QKwCakwsW9t_GbWF4PcOAedfG6ohvJ_yVccpSpNdXIA7YLrmSPZkzo-pDbVMVMICnjvPt1Z6RQoY3cYrTxfil3kztQryhSC2EfcDicvjDgNjCfkEhsEJW-f1HNvUMq_liosfTrkgg2L5PTJg7k6qpyMl62UsstjEQoiJBG3tIanmqxievdB2yhHS_2USn9JfXTRR1PbXBoRh3nib9GmhiCvrNVST1tB6T6OuBDOzf7GW1PrZHKaizVHEjJpL-Xa-RI55FJMF0kvrSR3-wvXRReFSjPR3a20-eVhcTg6INc3mqvYW69rGAgtcxcWjE-qXQ9L_k8R-LmhLBKjOwls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=QdcBaBIveFUT_hkhE6m7hktPlvhK_6Mbzvd-fsBjR594ItIMNaRAsoDs9LDEod9feSCDR6MARQ-oIdAXu_sHTcbaf-EvSDn-GxyzLfHi0-KE0p_pxE__lUwaNA2V4JFZolOly1I1dMv-Hul8keFYbX_MeQ_8lFWfhFIMOnp56MKyvcv_lT_uHNxBq6NKKWx5uiJGp-cqZrDLJwm5vM40uRQVOIf2Glwnx5AtwkZNCwmsoDxccFEKzIzhP6qshsiGxo2_Rq0F4q8SZgoA3IaAwxv6pMyvtJSxsqJAoFs6q58v38wpKtNRQ_Jrb_SVJHq4QZI2FRsHNMUPEqf95HITIhn1QKwCakwsW9t_GbWF4PcOAedfG6ohvJ_yVccpSpNdXIA7YLrmSPZkzo-pDbVMVMICnjvPt1Z6RQoY3cYrTxfil3kztQryhSC2EfcDicvjDgNjCfkEhsEJW-f1HNvUMq_liosfTrkgg2L5PTJg7k6qpyMl62UsstjEQoiJBG3tIanmqxievdB2yhHS_2USn9JfXTRR1PbXBoRh3nib9GmhiCvrNVST1tB6T6OuBDOzf7GW1PrZHKaizVHEjJpL-Xa-RI55FJMF0kvrSR3-wvXRReFSjPR3a20-eVhcTg6INc3mqvYW69rGAgtcxcWjE-qXQ9L_k8R-LmhLBKjOwls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد
خوش‌چشم، کارشناس مسائل فوق استراتژیک: باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم/ کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم/ این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/132135" target="_blank">📅 00:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDxbIGCkfiXSQrvpmwIEtfnsxVcXFxBp-Z57lBci4JbTLwjE0jNZ_RIVDr5T38OAaDWBCAusOvb3yYGDI2x34tgLGmw3Kz-8YvuH5u5xAfd-ite6qdpjYmXuP2X4g6Xqs5rqQzoYbJ7F5_Y_SqeWG26XdrGPmIUHq34fY8Et_X-I9k02PLmKgyCqKxZTHouHDUPYIlZqL8BKNVpE-xGlCYl1m19KgCXXY86eKCb2fHkz76j8gX1KURHU48_JaLp_OKqWRNfeGLZ9AGuwbua0m73SXcTyrOFjx71wBLhX1CrgpawJfBSKyKtD0Jz-EzUMl-Z3_YmHGCwHhDTORrkZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دادگستری :هر کسی که بعد از ترور آقا از نظر روحی و روانی آسیب دیده، می‌تونه با وکیل رایگان شکایتش رو ثبت کنه و پرونده رو برای پیگیری حقوقی و مطالبه خسارت تو مراجع داخلی و بین‌المللی دنبال کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/132134" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxhR4apZTbl_IhLJ8yXKlf16-01At3ze4pjW6r6DH8dLh9F85QJAHXDE2LkF3Ik4pR9Fc3ZhZbPdiCdujYHo9BL65hIJXUyZDscV1zhSPLmxc-5wKgbtcjf4C0XYNYcaMAlBEXMydJtsiw-Q9DRJ8IxXneK327CMv8SXXetO13EfPmkDM2nLLw4V2QjzqGeQ70GT0DaWszYPx5AXlG8_qWr3x87hgJ-jTwcftV8IZETC_gJLW3OyZXMTOGwuinjbJmTWt-atORTOagWzoAMKBEEOcIIvcS-xdMKD-o_i5w2QU8w4bwwppINT4Fq_K6uq8lTIknTZB5RmpAvDAPzvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت هادی چوپان زیر یکی از پست های مربوط به علی خامنه‌ای
جونم برای لحظه لحظه‌هایی که از تلوزیون دیدمت
😭
😭
😭
😭
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/132133" target="_blank">📅 23:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7guL-z7rzkTbOeDHdw9LRb1dxYM1BZO6TGYXoY8fz6mCEo7GaOqkWCAyHgpNimmebeItjCoknj4rUf6_yJhKeavaKouiEPHCygu7SV89SZlSIwSDORarLQ2aphesvZnY-Q1-dgVb5GLYY5wBx9geg_aqK6WAqY8QxcMWgS5AOqywvrlCsk3Cl_pKa-8CLrcWZjM9WoZtLSuMM7dTqIepiGq11iZynZvC3mMOTD4fSpUQb2KVFkKtl2xGZTQrFxTqvlkJU6SoI1REKsxWtKknfv5nhVRKTlNfIfOrHoEKwzlGpWJIU5_aKTBfxd3Oxn9G6XQw4ZuZvj3O5NaoALrLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو تصویر به فاصله 6ماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/132132" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رویترز: ارزیابی یک نهاد اطلاعاتی اروپا حاکی از آن است که روسیه با یک بحران بانکی «انفجاری» مواجه خواهد شد
🔴
بانک‌های روسی بار فزاینده تأمین مالی اقتصاد جنگی را بر دوش می‌کشند و همین امر آنها را به‌طور فزاینده‌ای در برابر تحریم‌های جدید اتحادیه اروپا آسیب‌پذیر می‌کند
🔴
پارسال بیش از ۵۰۰ هزار شهروند روس اعلام ورشکستگی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/132131" target="_blank">📅 23:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjpqB2C3wBzgnC77HSBFrZ2r-agJHuLOrP_r2Xyl6qHfmcQFNqqk6CtUSSrBfjjtZjj0z_WsGsjo9bKyZOAaSnnLqVRk4W96OypqauSaNTxcpj0PUdZEmZDgKPMsqa4j8LUUPO6yQMNBf--B0WhKapK8bY9Fx8LXnVJiNmb7rr3D0TbFdeSIeU4RSjYHprAq6tRtCQGq8yWGxjLmwO-fLGm1qYlDWuJ3VRyOdgHREVLIYWjduTv1g7pNMQGM7UWNaRecesJnLzC9VmVaZg9WqRf-mO3Wsd9vag1NiurS_lValf0q6r05rvQ1Qs-f7v95xb17GofRunIuxQ4Ui-nD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قرار دادن اتوبوس برای جدا کردن مردان و زنان در جمکران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/132130" target="_blank">📅 23:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
جوزف عون، رئیس جمهور لبنان: با بنیامین نتانیاهو، نخست وزیر اسرائیل دیدار نخواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/132129" target="_blank">📅 23:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جوزف عون، رئیس جمهور لبنان: با بنیامین نتانیاهو، نخست وزیر اسرائیل دیدار نخواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/132128" target="_blank">📅 23:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b01ad335f.mp4?token=e-KvIctMpwjAD9QGlFdl5tpAOdk8kYf69JKV3tk5VtKkf1i1FmfKMUxZsWrL-nhbwle2vN3yvF6PpjXeOpRIF7F7RwukPIGBgI3Ppr9x6Vw0_xcKAmSyzMOb7FMdhCYccSSYHjyDJsloBWgZZhoEjoujVSBHP_Rl6Nw2eaDKNpJdmHoBQnqtP8MCVJW3PfjgxNyjW0Oxk0ttIic1j4rSD5PFzHyCFPSr5J5WQHrY9A34RYb6Q1PL_4DOg5zC_fsPa5aWi8rWBCCK7H9n_Y7KyI4HknDuIT1A7PZWOABGWxyA5ggAp_QSnDtNIT0sK-16w0o7z_btsNohrX2UrRmfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b01ad335f.mp4?token=e-KvIctMpwjAD9QGlFdl5tpAOdk8kYf69JKV3tk5VtKkf1i1FmfKMUxZsWrL-nhbwle2vN3yvF6PpjXeOpRIF7F7RwukPIGBgI3Ppr9x6Vw0_xcKAmSyzMOb7FMdhCYccSSYHjyDJsloBWgZZhoEjoujVSBHP_Rl6Nw2eaDKNpJdmHoBQnqtP8MCVJW3PfjgxNyjW0Oxk0ttIic1j4rSD5PFzHyCFPSr5J5WQHrY9A34RYb6Q1PL_4DOg5zC_fsPa5aWi8rWBCCK7H9n_Y7KyI4HknDuIT1A7PZWOABGWxyA5ggAp_QSnDtNIT0sK-16w0o7z_btsNohrX2UrRmfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون صدر اعظم آلمان: جنگ ترامپ علیه ایران غیرمسئولانه بود
🔴
لارس کلینگ‌بیل: جنگ غیرمسئولانه‌ی ترامپ علیه ایران، رشد اقتصادی مورد انتظار آلمان در سال جاری را به نصف کاهش داد.
🔴
این جنگ هزینه‌های مالی سنگینی را بر آلمان تحمیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/132127" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubgtkYh80I_dq1apGLKGzpZXYYhlcu1veu0CO7VhEJVSjApFld2dXES5ZNItjdWMHHTksoD_XhAMqEczkq5-hQ6mM82jZxaW9B4Ap9heO21qRibFDTTDhykeayaa6jhNGVYihCQennflS8iRfoeDFapeCIxlCmXK8JYnOEcysFmoT1awXJygz5Dn9iKWDUCfU80cfh-ggQSPgi2R4qxNBQuC3YUo9OXMHaTZjBDXDwbVW3Wb3zhhWLpGd6c9kTnMV2mcTqTlrOqqP4andkry7vJtDKiayw9pXF-upDAWxSXatMkpWTOVGJtnklQV-z0aaAnbCpc5tpc8OFd7JvtzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاینشنال تایمز : تاکنون حدود ۱۲ تا ۱۵ میلیون نفر در مراسم خاکسپاری خامنه‌ای شرکت کرده‌اند و این امر آن را به بزرگ‌ترین مراسم خاکسپاری در تاریخ مدرن تبدیل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/132126" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8yt3ehLWf50O6qu6Qj-nHPjug6DjjuQfP9rfFclw1GuICJACIaxcyqqG-1GlbXdRmYpyHStbZ6iRUOXdB7Sf-LTY0POlPdqRIu2UAvP8n9wUhEUxMK-NvUP2PVPAcGVD_0XO_oqIUfYjcSI7TzSfOo1Ql6uF5MNx33dO1HlnO3EikoVvMKSJ9h8xw9eGXxInb8fmvLDToxY5bpnchNEKSxaRSeoSiDX-NLTz9eJMdN1xYrcm_W_Jn3GEAM3oa2cDeUZDmjLs6T9ESTUTH_oz6vAUzApzYtVSDe787jMml8c-En08LUf9GDBsJamtklZny27J5TpsEzmw4qFmk22qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/132125" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
لرستان هم فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/132124" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سی‌ان‌ان: یک‌سوم کشتی‌هایی که طی چند روز گذشته از تنگه هرمز عبور کرده‌اند، مسیر ساحلی عمان را انتخاب کرده‌اند
🔴
از جمعه تا یکشنبه ۱۰۸ کشتی از این تنگه عبور کرده‌اند؛ از این تعداد، ۳۰ کشتی مسیر عمان را طی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/132123" target="_blank">📅 22:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXaf_5WIgjh6qeE5csK8CvJpgVFkP_f0kunpKPoQOHhYAtZNXIpc3s9NiTZbD3GNS036UPbkri4mAVN1IcYsEoaLBA9W4XqZTrgwxjkmFPRPVq17F1VOrbHZuwomVgcwiTBZAFV1Ur9o0FhQTAwEIQikrG4wH9RWmwYuq-AzxX5lDs11oz0T3rUoTiH0ShKhow9m9v47sqbk4ejcXGUHc4JH9OwYavSSVM3vYDuwrRFMCRoJv19mtwFf_pTb4ne5LCFHXQhpMcycPvuSwFpmDJ_sX0rtCQPkjHxunHBQjeOY8Ssowl971SsuDHqztu3SO0ChIZLBPNBnA7CbyMhX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای‌عالی امنیت ملی، خطاب به ترامپ : با مردم ایران با احترام حرف بزن
🔴
قبلاً هم با تهدید چیزی به دست نیاوردید و آخرش خودتون دنبال مذاکره و آتش‌بس رفتید
🔴
اگه دوباره با لحن تهدید صحبت کنید، ایران هم متقابل جواب می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/132122" target="_blank">📅 22:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7a1205f8.mp4?token=gti_pm_byBIU2SNDNFrs5e3WPH4jHbF1HRecSjUZW9zYNE25PDG-qN2WkOr3gO8_nodd7uVgbBE0oiLjW-p9hq3r2i5-DdfmYZr_2X9AyMdNkQpAXFSVr_BuM9l0QNj0fVumpj8oiPlrn4W34B6WrrALHVGaLIlHVnE6DVSRNgDJeBudDmo0LZKqgv4pTebhURMboHccNASb7SO0zxD3_PFuQhRZcn6bOAO0pC7zbiifp5GhIpuHlbTLJ2MTFV-CJLAJoij9zacgLDz2j0FT1hzdACSRxuQIHTTCtHsQmDAS662jYFasuGmYoD8OiQtW4wTiPs7YdpFDsq9htDBI4lg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7a1205f8.mp4?token=gti_pm_byBIU2SNDNFrs5e3WPH4jHbF1HRecSjUZW9zYNE25PDG-qN2WkOr3gO8_nodd7uVgbBE0oiLjW-p9hq3r2i5-DdfmYZr_2X9AyMdNkQpAXFSVr_BuM9l0QNj0fVumpj8oiPlrn4W34B6WrrALHVGaLIlHVnE6DVSRNgDJeBudDmo0LZKqgv4pTebhURMboHccNASb7SO0zxD3_PFuQhRZcn6bOAO0pC7zbiifp5GhIpuHlbTLJ2MTFV-CJLAJoij9zacgLDz2j0FT1hzdACSRxuQIHTTCtHsQmDAS662jYFasuGmYoD8OiQtW4wTiPs7YdpFDsq9htDBI4lg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مینی تندرو: قیام کنید و بزنید و داغون کنید تا توافقی شکل نگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/132121" target="_blank">📅 22:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / هم اکنون درگیری مرزی میان نیروهای طالبان و پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/132120" target="_blank">📅 22:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: پوتین می‌خواهد به جنگ اوکراین پایان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/132119" target="_blank">📅 22:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78086417f9.mp4?token=Jzj0Oh9NwdMgzsOFKRj3gwxZQquIDj7moGUAgF8KXUmmX9UBXQrCL33qAm3qMFyW2ej43SHt6UWZLa0XlmQlWQ_RD7BsSW2LrQC21VIqTHstfoD60keJrEPye6P3Lt3Xj0KL-yiTT8707ALfGaHVIwz5q7vPpSATuAal7kNCJKI2JH_6C2PtGk_2E_8KHi1JbjrHMlVDbD5ElnWolyZcR0ZDTMGFXdKaFmUvd6DUEQ-hyS9NafkKc__o9vox42PU_66BT3WZI_f_ME87qFLw7F0ejKayY_dwjcfEICaKr91DKyiTL3eqnsIdsmNF51pV_hARvMZjlp7dk0flENnd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78086417f9.mp4?token=Jzj0Oh9NwdMgzsOFKRj3gwxZQquIDj7moGUAgF8KXUmmX9UBXQrCL33qAm3qMFyW2ej43SHt6UWZLa0XlmQlWQ_RD7BsSW2LrQC21VIqTHstfoD60keJrEPye6P3Lt3Xj0KL-yiTT8707ALfGaHVIwz5q7vPpSATuAal7kNCJKI2JH_6C2PtGk_2E_8KHi1JbjrHMlVDbD5ElnWolyZcR0ZDTMGFXdKaFmUvd6DUEQ-hyS9NafkKc__o9vox42PU_66BT3WZI_f_ME87qFLw7F0ejKayY_dwjcfEICaKr91DKyiTL3eqnsIdsmNF51pV_hARvMZjlp7dk0flENnd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه: سرمایه‌گذاری در سوریه، فرصتی بزرگ برای کنسرسیوم‌های بزرگ خارجی است که به دنبال رشد و توسعه هستند تا زیرساخت‌های تخریب‌شده در طول 14 سال گذشته را بازسازی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/132118" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/132117" target="_blank">📅 22:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
🤖
ربات خرید
@SafeVPNXBot
✅️
📞
پشتیبانی
@safevpn_secureSupport
✅️
📢
کانال اطلاع‌رسانی
@safevpn_suportt
✅️
😍
رضایت مشتریان
@safevpn_feedback
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/132116" target="_blank">📅 22:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یزد سه‌شنبه ۱۶ تیر تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/132115" target="_blank">📅 22:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
آی 24نیوز:نیروهای نظامی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با حزب‌الله هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/132114" target="_blank">📅 22:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مکرون با عینک آفتابی خود وارد دمشق شد و توسط وزیر خارجه سوریه استقبال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/132112" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قالیباف: قاتلان شهدای این سرزمین به ویژه قائد امت به سزای عمل‌شان خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/132111" target="_blank">📅 22:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae44e7.mp4?token=Kf1GazPgmIGmMlP_C-yvo3a0-bTCwGk_GU3RrHtR0cfDX-y2TsNKGvrRFA_JU5Ms2FI7QsbW4h7NHD5VO9lcGvzdRCY_VvCyebD0Ls1XsDRublEHJE1riQ8BBEFPGeCxoeDgbaz9zNng7CAdmk5Oxn9jV3C8ciYRweh4DY-JZLbg5_cBkJUl8JpbVUqkAEgl-DeP8HDXY8OmGcCEPC6eVylSzaTRiCQ5yFNw55JF-A7Hfbdd9m1LIMJkExfd4nPZh0GcNDk97eHXo6w3CGybjWAGqvHj5ubkma4slvh5_UHEmmseGC5xV023InJS5Zz_bjMpZwLRFhYALh2m0LyVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae44e7.mp4?token=Kf1GazPgmIGmMlP_C-yvo3a0-bTCwGk_GU3RrHtR0cfDX-y2TsNKGvrRFA_JU5Ms2FI7QsbW4h7NHD5VO9lcGvzdRCY_VvCyebD0Ls1XsDRublEHJE1riQ8BBEFPGeCxoeDgbaz9zNng7CAdmk5Oxn9jV3C8ciYRweh4DY-JZLbg5_cBkJUl8JpbVUqkAEgl-DeP8HDXY8OmGcCEPC6eVylSzaTRiCQ5yFNw55JF-A7Hfbdd9m1LIMJkExfd4nPZh0GcNDk97eHXo6w3CGybjWAGqvHj5ubkma4slvh5_UHEmmseGC5xV023InJS5Zz_bjMpZwLRFhYALh2m0LyVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله زامبی‌ها به عراقچی در مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132110" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رئیس فیفا درباره لغو محرومیت ستاره تیم ملی فوتبال آمریکا: ترامپ با من تماس گرفت
🔴
من تصمیمات کمیته انضباطی فیفا را زمانی که صادر می‌شوند می‌خوانم؛ گاهی از آنها شگفت‌زده می‌شوم
🔴
اینکه ما شخصاً از یک تصمیم خوشمان بیاید یا نه، اهمیتی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/132109" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
حشد الشعبی: نیرو‌های ما وظیفه تأمین امنیت مسیر انتقال پیکر از جاده کربلا–نجف تا حرم امام حسین و حضرت ابوالفضل را بر عهده دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/132108" target="_blank">📅 21:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نیویورک تایمز: طبق داده‌های شرکت «کپلر»، در سه روز گذشته ۱۰۸ کشتی از  تنگه هرمز عبور کرده‌اند
🔴
با وجود بهبود نسبی تردد، مقامات دریایی گزارش می‌دهند همچنان حدود ۳۰۰ تا ۴۰۰ شناور با ۶ هزار خدمه در خلیج فارس سرگردان‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/132106" target="_blank">📅 21:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a913fff9.mp4?token=P_V-gyu8ROwlib9Dhxy1XHy-5xuys3Hi9YrsEgBmDjUQ2nelEqV-X4V1iWZqiBFEQ9zkT4-cugfQjHTe2R4F2vOvjo5wpHYjTgkLC9NYELSxjLVqbCqHuZChZgRifeN_6WHt4cHAhVkkzdnwVrPWREG4c87FTv7oVNkVD6nf8bT0nswATN3m8q3Z-I_WSKbWWdZ2WCcowmEmxZmRW1rytHe7nkGKJuRpMKtAHGIrtH5qtKlH1bYbvbJVzA3R95in_eiIy8YvkYF8B_Iv1_TPYxu6824UlHCEVothqVAb7GrEiB8-ThdQUqgcaKlMwGc37W0UPvTStSf27R4GVMaczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a913fff9.mp4?token=P_V-gyu8ROwlib9Dhxy1XHy-5xuys3Hi9YrsEgBmDjUQ2nelEqV-X4V1iWZqiBFEQ9zkT4-cugfQjHTe2R4F2vOvjo5wpHYjTgkLC9NYELSxjLVqbCqHuZChZgRifeN_6WHt4cHAhVkkzdnwVrPWREG4c87FTv7oVNkVD6nf8bT0nswATN3m8q3Z-I_WSKbWWdZ2WCcowmEmxZmRW1rytHe7nkGKJuRpMKtAHGIrtH5qtKlH1bYbvbJVzA3R95in_eiIy8YvkYF8B_Iv1_TPYxu6824UlHCEVothqVAb7GrEiB8-ThdQUqgcaKlMwGc37W0UPvTStSf27R4GVMaczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون با عینک آفتابی خود وارد دمشق شد و توسط وزیر خارجه سوریه استقبال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/132105" target="_blank">📅 21:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شبکه ملی برق کوبا دچار فروپاشی شده است و یک قطعی کامل برق در سراسر جزیره گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/132104" target="_blank">📅 21:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ادارات برخی استان‌ها سه‌شنبه و چهارشنبه ۱۶ و ۱۷ تیرماه تعطیل شد
🔴
روزهای تعطیل:
🔴
سمنان: سه‌شنبه و چهارشنبه
🔴
مازندران: سه‌شنبه
🔴
هرمزگان: سه‌شنبه
🔴
کاشان و آران و بیدگل: سه‌شنبه
🔴
مرکزی: سه‌شنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/132103" target="_blank">📅 20:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01f989eae.mp4?token=SPG-q95njn365MW0Gflarg9cSF4ba_mDrTOCL0Me0iwc9fRZ93iNKIsn58PiuGiKwuc3Sp1y-aPF9FNgMLZST7mN66G45dREjNGxIhyVxgohBcq6IUM2wbRMD2WJpJPWyk8E6kHWKM6f9jm02fFaJRvMTFsRxpcOSHpLge-or8WGm9M1X3oRbj-RmGzaAVog_52KyGdid4pTjZwVayBxRTSIy9itgvIa48qgx3dgibs-VtpO8856T4pbWxlBsWcP-a_y4gRS6edd7XofMTAJmUUCkj1QY7SQsfXJiuEdiOqvHgF4uFKLoySTWDhgQY_zCBehx-2sbAyVvviCDIQryTg9Q_i3e4xUscH-E4KyjzHMKUNKIUQXfMku4mHIkIe0WIX-IA4vQZ5xV0bEzcxZrqDLl1q_N6NXovI1Mo9cvZbla3NtaysJoVrlMUGLQEyN4Ny7aK85l-iCB4qZRFGJLwiGC3KYjmsxfXXcf83Qs-Q78zK9-Hha8NNW7ijI4Boz6OLc8jlGe8FFZQ3MizXv1Qn0vldNLdXkL46AIBtmNabRZZclUhoIjdJAYcFtzTJlo4nd2CsMcFhYsY2lZlQ4yFRbKixtljA4SOk02m4g8JXNAbki1aJmD5ZJVZ2LVVTh-434j_LEI3XOyVBnnQlKuIHlQUzZ8PwZ2EZ9DpQ_i3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01f989eae.mp4?token=SPG-q95njn365MW0Gflarg9cSF4ba_mDrTOCL0Me0iwc9fRZ93iNKIsn58PiuGiKwuc3Sp1y-aPF9FNgMLZST7mN66G45dREjNGxIhyVxgohBcq6IUM2wbRMD2WJpJPWyk8E6kHWKM6f9jm02fFaJRvMTFsRxpcOSHpLge-or8WGm9M1X3oRbj-RmGzaAVog_52KyGdid4pTjZwVayBxRTSIy9itgvIa48qgx3dgibs-VtpO8856T4pbWxlBsWcP-a_y4gRS6edd7XofMTAJmUUCkj1QY7SQsfXJiuEdiOqvHgF4uFKLoySTWDhgQY_zCBehx-2sbAyVvviCDIQryTg9Q_i3e4xUscH-E4KyjzHMKUNKIUQXfMku4mHIkIe0WIX-IA4vQZ5xV0bEzcxZrqDLl1q_N6NXovI1Mo9cvZbla3NtaysJoVrlMUGLQEyN4Ny7aK85l-iCB4qZRFGJLwiGC3KYjmsxfXXcf83Qs-Q78zK9-Hha8NNW7ijI4Boz6OLc8jlGe8FFZQ3MizXv1Qn0vldNLdXkL46AIBtmNabRZZclUhoIjdJAYcFtzTJlo4nd2CsMcFhYsY2lZlQ4yFRbKixtljA4SOk02m4g8JXNAbki1aJmD5ZJVZ2LVVTh-434j_LEI3XOyVBnnQlKuIHlQUzZ8PwZ2EZ9DpQ_i3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقام از ترامپ با دمپایی و کمربند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/132102" target="_blank">📅 20:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ:اگه بازیکنمون بخشیده نمیشد و مقابل بلژیک حذف میشدیم، من میگفتم مثل انتخابات ۲۰۲۰ اینجا هم تقلب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/132101" target="_blank">📅 20:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilxyP6aGgqwZKAEaDmwWk_8DFEIvAaCtBcGLX068_BOjlLq_-rG4VwWkXIY1EfN8i4miTWJj7C_PhQzF-ZaMzT3yIjIT9bf-xw6m-_AR-wgd-HUPTEgIWNB1bD1o2lELZUKfzACarzagryhavEN6__gsAier9K1QYK0jKB5GuASgjWTXjSpI_r1crVcMw5OzkFsPsl4hypzqZo3Oerm8dEW3qRrJdJo509Bd5HyDkViKOr4C-pWXtQVQleiND515WqLCt8uUjGGq9LrAAiYklVEXdhjBJQXqUC4H5mXXhgGepGwcktpGbQeW-EKBNJGBkwSuam0QFsZntcEA_HIogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط شریعتمداری، مدیر هولدینگ خلیج فارس هم کلی پول رپورتاژ داده تا کانالا بزنن که اومده به مراسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/132100" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سفیر اسرائیل در ایالات متحده:
ما معتقد نیستیم که ترکیه باید هواپیماهای جنگنده F-35 را در اختیار داشته باشد.
🔴
با این حال، اسرائیل درک می‌کند که دولت ایالات متحده مجموعه‌ای گسترده‌تر از ملاحظات استراتژیک را باید در نظر بگیرد، زمانی که در حال اتخاذ تصمیم است.
🔴
ما مخالف فروش هواپیماهای جنگنده پنهان‌کار F-35 به ترکیه هستیم، اما به هر تصمیمی که آمریکا بگیرد، احترام خواهیم گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/132099" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFHzuVCmK9h5kduRkXQzWrc4nLGytDO5jIcfI3eaZlCvJrgF1IgTB1i59IbyEdmtAK3YwCSfNvomodbFsHu-lczI1aSkURm1CYWvPAC9DX-Q7ldP-kdmcWDMl-AxWM4NpR_AydFTftinjHGLHczcs5Fg5WD869_ywA7Alh7u-kqTMVeqsPdiIkJEZ-Q9hFAWJSImB5uf3Om1DR4C9Xo4DMuawQaFn7aw-UHDB897_xFJSRpfOy-MmFY6LQCTeBm-93F5CUljsMagKAf_tz0nj5A4TuHFjU8W3Ri16vhNZby1iLYjwTKgImk3r3BmcMfxv80lgDEL8B_2PrBV8NjOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ حسام الدین آشنا به عدم حضور حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132098" target="_blank">📅 20:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132097">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b484bee13d.mp4?token=H7yAzKM-PWzLfa0Z7wiw-b6lr7slb5iUV8aLm7JUEWpXQuI2l4wCV43HbviObl8jeETY2iME6xsIzEZGZl6QZMWUoWZgfjLiwDwjNAhGUsoFoZngPJszTN5WNcMUpCjyLpLvMIG79Pp6uevi9sIMNNBUh-lPgkoBCINPWSjHONffFQg6lDVNnf6_aSCVTHIAwlVWbZbq_gRz15hfrkHU3hN91ofIMbhdSwCi1x7tj5pOV-Z4j_Jmp9xca8NcsCLJkgNpZenJpVuNnOkCakhbgcUqh4qczwQj55nPuMwc0WZJZ_5Vd36kKPCauQIGa2uqBLClGePZN6ZeGGI0JRg3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b484bee13d.mp4?token=H7yAzKM-PWzLfa0Z7wiw-b6lr7slb5iUV8aLm7JUEWpXQuI2l4wCV43HbviObl8jeETY2iME6xsIzEZGZl6QZMWUoWZgfjLiwDwjNAhGUsoFoZngPJszTN5WNcMUpCjyLpLvMIG79Pp6uevi9sIMNNBUh-lPgkoBCINPWSjHONffFQg6lDVNnf6_aSCVTHIAwlVWbZbq_gRz15hfrkHU3hN91ofIMbhdSwCi1x7tj5pOV-Z4j_Jmp9xca8NcsCLJkgNpZenJpVuNnOkCakhbgcUqh4qczwQj55nPuMwc0WZJZ_5Vd36kKPCauQIGa2uqBLClGePZN6ZeGGI0JRg3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: یک سوشیال دموکرات، یک کمونیست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132097" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : خیلی از اینایی که اینجان
🔴
حتی درست‌وحسابی نمی‌تونن راه برن، ولی خرپولن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/132096" target="_blank">📅 20:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: من لری [فینک] و برخی از بزرگترین افراد وال‌استریت را می‌بینم: گلدمن ساکس، بلک‌استون، بلک‌راک. همه آن‌ها اینجا هستند.
🔴
به آن فکر کنید. من همه آن‌ها را نابغه می‌دانم. هر یک از آن‌ها نابغه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/132095" target="_blank">📅 19:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: به پادشاه چارلز گفتم شاید بهتر باشد یک لقب خوب مثل «چارلز فاتح» داشته باشد.
🔴
او گفت: «نه، نه، نه، لطفاً.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132094" target="_blank">📅 19:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حالا که حماس تسلیم شده بهتره اونایی که تو ایران عشق جنگ دارن رو با کامیون اعزام کنیم غزه تا به آرزوشون برسن، البته اگه
تخم
داشته باشن چون همیشه عادت دارن جاهایی شعار بدن که امنیت کامله و خوراکی و عشق و حال به راهه</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132093" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4810d9bf95.mp4?token=FQ-mF2A5IOtEiGabyOoQ4_ZXOYkVCBVwyQq0rDk4rGE8D0qQk0w1eFzxuz7DBkXj6qTNS82m-Ph909SXNbpU8cZ1GAo4XmQpjz7WC_1puOAbHpV4og8fmKEA1CcDEIOZUw0toiK7BGDPzQyth3dD41ffHz5mi_QT9MDvrHyaZliSyToPDh4pwp8NTQSY7Oo3dPxfaF5293r_u2NZmkPP262v4Yf0roDuxICTX18LF_ApALvGS5p2rqYy4L7-fyphQuEI1ZPW_02YsqZIVYhlSRl42eKUuVMoISwTdcvu_rqjk7XcfsvATLBHPjgtvmaGlGmFEj41yNxxuLHuEEnlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4810d9bf95.mp4?token=FQ-mF2A5IOtEiGabyOoQ4_ZXOYkVCBVwyQq0rDk4rGE8D0qQk0w1eFzxuz7DBkXj6qTNS82m-Ph909SXNbpU8cZ1GAo4XmQpjz7WC_1puOAbHpV4og8fmKEA1CcDEIOZUw0toiK7BGDPzQyth3dD41ffHz5mi_QT9MDvrHyaZliSyToPDh4pwp8NTQSY7Oo3dPxfaF5293r_u2NZmkPP262v4Yf0roDuxICTX18LF_ApALvGS5p2rqYy4L7-fyphQuEI1ZPW_02YsqZIVYhlSRl42eKUuVMoISwTdcvu_rqjk7XcfsvATLBHPjgtvmaGlGmFEj41yNxxuLHuEEnlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاجعه مراسم امروز
‼️
🔴
حمله جماعت تندرو به پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/132092" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ--dFLo3a1Ig1CGYj6Oj2MXsqTVTNZsUcy-fX-D7swQNCWT9-65YaSMD5-mpCQHJOqbV4vChEtsjmrUu6FQkkB15rmqsLoJk6yC9-1NRyrV0yO9Ok8M1V6Pr6qbuTuJe2lEnCYxvAmIsrwaJXZlra7InNVrRCWkKZZM3rDA3S398NxrApk0gVJW78Cf5YspEKKGrqOfEma9H8MSaVCurqbEgQ_54gO29de7CMpZKxPVeMxBypy_M0xHdoQASm-J60BhzmGDiKbfrNqAdIxI7Rryck9lBWQnRhYvdZhiDk6Ht11czOwDDzV_4w_rpYQ3nyvULJmhfZw2ombv6YIbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی عبدی، تحلیلگر: امام خامنه‌ای بزرگترین شخصیت تاریخ ایران هست
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/132091" target="_blank">📅 19:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHx7ujAucCEK74i5etLJAWbz76iz_OlWnZkYJDRiGS2pm0F9XnbJH_YL3Nd3t4XcgIW_g0m8HQibtfVTUhqMmK7r7PaaYLA9kHgAMsKUe9b7QYXXgNa1Sh0Wzg3UrEwfNDyzTLwpaFKWXpv4rNLEviSDRpkThhGwYQ6tkxP0nxJEY1PBWtT7qUIZqImqcoYa_1y_S28ZF_DxSRiW9sSPqanCEAl0g0276rqePnZ0F2YcEbvMjk7OO4lxTgdhXkXunWFRaZtDb4l-6eWCroFOtlFn5UJGz5tzNBQeVwvmPLSV1FUONMJZOgKdfic-vA5FUalaUAYqKPPddwoAfnzJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132090" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
🔴
می‌شنوم «آن‌ها بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
🔴
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
🔴
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
🔴
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/132089" target="_blank">📅 19:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / الحدث: ساعاتی پیش حماس تسلیم شد نخست وزیر خود خوانده او طی یک کنفراس خبری استعفا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/132088" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فیدان: روابط رجب طیب اردوغان، رئیس‌جمهور ترکیه با دونالد ترامپ، رئیس‌جمهوری آمریکا می‌تواند به کاهش تنش‌ها در ناتو کمک کند، زیرا رهبران کشورهای عضو این ائتلاف خود را برای دیدار در آنکارا آماده می‌کنند.
🔴
برای ترامپ، این موضوع صرفا به اعتماد و دوستی مربوط می‌شود. ترکیه قصد دارد به سود کل خانواده ناتو رفتار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/132087" target="_blank">📅 19:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQnRxkY94kFBquVF7dp36rqDW9c2uGLsnWgSxIv53oEJ1WZ99uIFRAKppDeka7o7O3ug3ZCV4q5Odzu2qlFKsC3TCvxfLF12Xe04_aWg2Dts2s4GNCsMrPd5BSm-6PXQn5BVPENfh-cSAESCM12z2I3vKeqS-Hrws-ZqIBPDM9KuAn6CqGPrvdoVbQt3zUIxWaHMfji6ih3vRXOb6pkeGhLZv4x7uYL_ge2SV7WoYOEGYUGje5ILMv4j9r6vmcuhj6psatASo4VSFK9SCtpglEsfjfMuhYYAtfx_N9okn1GACeORruOwlR-BiBIH9dSeU4hDFDQb3xrwG-vHMXl3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtrGLbMcoUjvANrIFkDWyceKUaHj0Ru5uP4LAIIxo07PYcrX87gIyUG5JX-n6I9kQEeJfyGFusUuAmopzUyS4Xgaxlh90OMhAmh1NpchU49jUQF2c041Pt_rQ2j1pM_7cxCCmxewZjaz76avLBLXpNMNcOmm0lJiAnl5BHw8FPLJLtE0jaSrw9igIPGh4jCCOfkEuQZ75fhz66g00zPIoe3XIvPMiEEDXCqvQd434mkrCV7Y8I6zoBNh7Vs1Ei6oZF-uWwiK-dCnt9aSYlZw8uKvRfm-W6UtBI2JXVMk2r7p_p74ML_nNaWRAIo_fKUeDABI7uzd-I_6WXM6bUbiLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال با انتشار این پست ها از مرزهای کشور در دوره بایدن و مدارس دخترانه تمام محجبه در مینه‌سوتا انتقاد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/132085" target="_blank">📅 19:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285e95c239.mp4?token=duZwU2VaihFIrzj-xifCGlBOqzoHiBmUwboUL1YrgXu9qiLOztGX1Pn3kg1vnL2HyGlGgOgPtlhHklRErds-1Kf_4qm0ZmLdsox8aO-ZgtN0J2V5kwuuWw6ERatyBp7yQvO7JMAkld-OnPnn3yz4SyL12ZKyksvSEjabcCJWeeUodNVe9xQjoqW6l-VgrY1M-a4qHIgkg7f3fu2_dBG5MgiV_H0VVlZM9NpLVui3qoZpobFeQQwTJTS3fLzP_UqO5w2gahPKT3jJzrZPvmTNeATjwMf9C1MTjd8TQQyKqsyLNmUr4ycjG88ki8_eHnebWO7GH8aDFmg49GfX3de8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285e95c239.mp4?token=duZwU2VaihFIrzj-xifCGlBOqzoHiBmUwboUL1YrgXu9qiLOztGX1Pn3kg1vnL2HyGlGgOgPtlhHklRErds-1Kf_4qm0ZmLdsox8aO-ZgtN0J2V5kwuuWw6ERatyBp7yQvO7JMAkld-OnPnn3yz4SyL12ZKyksvSEjabcCJWeeUodNVe9xQjoqW6l-VgrY1M-a4qHIgkg7f3fu2_dBG5MgiV_H0VVlZM9NpLVui3qoZpobFeQQwTJTS3fLzP_UqO5w2gahPKT3jJzrZPvmTNeATjwMf9C1MTjd8TQQyKqsyLNmUr4ycjG88ki8_eHnebWO7GH8aDFmg49GfX3de8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در حاشیه مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/132084" target="_blank">📅 19:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
اکونومیست: بسیاری از کشورهای اروپا از هدف دفاعی ناتو عقب می‌مانند
🔴
بسیاری از کشورهای اروپایی تا سال ۲۰۳۵ به هدف ناتو برای اختصاص ۵ درصد از تولید ناخالص داخلی به بودجه دفاعی نخواهند رسید.
🔴
این گزارش می‌گوید با افزایش نگرانی‌ها از تهدید روسیه و احتمال کاهش حمایت نظامی آمریکا، کشورهای اروپایی باید توان دفاعی خود را تقویت کنند.
🔴
همچنین بررسی‌ها نشان می‌دهد کشورهایی که به روسیه نزدیک‌تر هستند، در سال‌های اخیر بودجه دفاعی خود را بیشتر از سایر کشورها افزایش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132083" target="_blank">📅 19:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/132082" target="_blank">📅 19:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل : وقتی برای هر شرایطی آماده باشی، دیگه هیچ محدودیتی برات وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/132081" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ درباره دیدار آمریکا-بلژیگ:
باید اجازه دهید از بهترین بازیکنان خود استفاده کنند و بازی امشب شگفت‌انگیز خواهد بود.
🔴
ما یک تیم کامل خواهیم داشت و بلژیک نیز یک تیم کامل خواهد داشت و می‌دانید چه؟ اگر ما را شکست دهند، می‌توانند واقعاً به خود افتخار کنند.
🔴
اما اگر راه دیگر را در نظر بگیریم و ما را شکست دهند (اگر کارت قرمز تعلیق نشده بود)، می‌گفتم که بازی تقلبی بوده، درست همان‌طور که انتخابات در سال ۲۰۲۰ تقلبی بود، اما من وارد آن موضوع نمی‌شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/132080" target="_blank">📅 18:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار: آیا در حال ساخت فرودگاه هلیکوپتر هستید؟
🔴
ترامپ: بله. در طول ۵۰ سال، هلیکوپترها روی چمن فرود می‌آمدند. چمن خیس و گِلی است. شرکت سیکورسکی بابت آن پرداخت می‌کند.
🔴
ما تعدادی هلیکوپتر سیکورسکی سفارش دادیم. خوب، آن‌ها حدود دو و نیم برابر قدرتمندتر از مدل‌های قدیمی هستند. وقتی روی چمن فرود می‌آیید، مشکل این نیست که چمن تغییر رنگ می‌دهد. چمن کنده می‌شود. کنده می‌شود.
🔴
یک بار هلیکوپتر فرود آمد و نیمی از چمن جلوی در ورودی دفتر بیضی نشسته بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/132079" target="_blank">📅 18:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132078">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ: من فقط به یک دلیل به یک طرفدار بزرگ کریپتو تبدیل شده‌ام: اگر ما آن را نداشته باشیم، چین آن را خواهد داشت و آن‌ها دوست دارند آن را داشته باشند.
🔴
اما اکنون آن‌ها حتی تلاش زیادی هم نمی‌کنند زیرا ما بر کریپتو مسلط شده‌ایم.
🔴
من طرفدار آن هستم. در ابتدا نبودم. خیلی درگیر نبودم، اما تماشا می‌کردم. می‌دیدم که پول زیادی شروع به ورود با بیت‌کوین و، می‌دانید، اشکال مختلف آن می‌کند. و گفتم: «این چیز زندگی زیادی دارد.»
🔴
ما در هوش مصنوعی به‌طور قابل‌توجهی جلوتر از چین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/132078" target="_blank">📅 18:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132077">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رییس جمهور دولت مستعفی یمن: گزارش‌ها حاکی از آن است که پرواز انجام‌شده از سوی ایران به مقصد صنعا، حامل پرسنل نظامی و کارشناسان موشکی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/132077" target="_blank">📅 18:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9701b8ad3d.mp4?token=LZhLIXS2pImEIAgU3_ZW7coORJcICqD5DdoVaEISX8dmTpn7NyuOwYgBn4AQS_vQV5J3j92766lqqT0ypS2AsgZ69hi336mnfMNhUFLIr6nDrKGjDXb0n2ouhe7KU0f63uLE-dquWjGzjWUQ44XSENqADEc_SQSK20o4PmgnwOmS8YtWfnDwEulqXkOu9IEYzYRMkUT11FrVU4gqXOA9xBSHVsEAOM32YQjVQanuPKw6ErUZ31H8ERgVu_7WNQaFyKiXefzmjJj6p5YAuCV56jDCROjhtqhn99bFC-l8CLS51uilEeXJxub5hDSDeigcFjPw8l8WRyXafyNIEczOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9701b8ad3d.mp4?token=LZhLIXS2pImEIAgU3_ZW7coORJcICqD5DdoVaEISX8dmTpn7NyuOwYgBn4AQS_vQV5J3j92766lqqT0ypS2AsgZ69hi336mnfMNhUFLIr6nDrKGjDXb0n2ouhe7KU0f63uLE-dquWjGzjWUQ44XSENqADEc_SQSK20o4PmgnwOmS8YtWfnDwEulqXkOu9IEYzYRMkUT11FrVU4gqXOA9xBSHVsEAOM32YQjVQanuPKw6ErUZ31H8ERgVu_7WNQaFyKiXefzmjJj6p5YAuCV56jDCROjhtqhn99bFC-l8CLS51uilEeXJxub5hDSDeigcFjPw8l8WRyXafyNIEczOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: هر بار که مردی را در حوزه ارزهای دیجیتال می‌بینم که تحقیقی را منتشر کرده، می‌گویم: «تو خوش‌شانسی که من رئیس‌جمهور هستم.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/132076" target="_blank">📅 18:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49e2cfdc7.mp4?token=PKMU0FWKmspVfRnGcp5kn5hdRG6wYwf1w4V_eo8UaGwGWMcJyGF67b6ZVc7jxciWRyghqgzLOQsZWqJ_edBefbSyrnUNKgt-5iIUsgx3Zh2WYPFgNyjvLuNRETISNPUfh83d-kazLPsw2aEJ_5byl9E9MfdNaQx_A6EjwFKsioPDx6h-ZKqjrfA1S4UrUVL9SRzihNt0Ud3V1AxAoVLl5_UnRYm8RTTHbJVUbYOSIazRFUgrxw-6ZJCb8ibSir93oE9vNe9fF3vd0CGYoMADw6y8pQQBnf707dqg5zv55Tpete8-e281M217abQcRD6Uv1ZYIYPJJpLT4cIF-SQJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49e2cfdc7.mp4?token=PKMU0FWKmspVfRnGcp5kn5hdRG6wYwf1w4V_eo8UaGwGWMcJyGF67b6ZVc7jxciWRyghqgzLOQsZWqJ_edBefbSyrnUNKgt-5iIUsgx3Zh2WYPFgNyjvLuNRETISNPUfh83d-kazLPsw2aEJ_5byl9E9MfdNaQx_A6EjwFKsioPDx6h-ZKqjrfA1S4UrUVL9SRzihNt0Ud3V1AxAoVLl5_UnRYm8RTTHbJVUbYOSIazRFUgrxw-6ZJCb8ibSir93oE9vNe9fF3vd0CGYoMADw6y8pQQBnf707dqg5zv55Tpete8-e281M217abQcRD6Uv1ZYIYPJJpLT4cIF-SQJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
ادعا می‌کند که انرژی بادی برای محیط زیست مضر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/132075" target="_blank">📅 18:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روس اتم: ما مذاکرات ایران و آمریکا را بسیار به دقت دنبال می‌کنیم، به همه جزئیات واقفیم
🔴
به احتمال زیاد به مشارکت ما در حل‌وفصل موضوع برنامه هسته‌ای ایران نیاز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/132074" target="_blank">📅 18:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: یک برنامه‌ای وجود دارد به نام تیک‌تاک. آیا اسمش را شنیده‌اید؟
🔴
حدود دو روز پیش اعلام شد. آیا می‌دانید که محبوب‌ترین فرد در تیک‌تاک کیست؟ ترامپ.
🔴
تایلور سویفت در رتبه یازدهم قرار داشت. من به طور قاطع در رتبه اول تیک‌تاک قرار دارم.
🔴
آن‌ها در مورد خطرات بسیار زیاد ناشی از نفوذ تیک‌تاک صحبت می‌کنند.
🔴
شاید این برنامه بد باشد. شاید هم نباشد. اما یک چیز را می‌دانم. مردم بزرگ آمریکا، افراد برجسته تجاری و شرکت‌های بزرگی آن را خریداری کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/132073" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b9f4c114.mp4?token=OGcxO-ZTYV1lMJWZ9_UX1vXixxUSZV34ajtrlYaLJy7xFaMkw68a3rq38GVT4uDaaIeMK105FljNjYn8c_Z06BCRFaIptKO0JPHx9FTCdc2amgLhBDFMfiyW4wmMRn92Dlv7t2fKbxr6nt9kG8KOkkxRMjlh4Ym3XP-8wv5RACKqGzuuLUmqUd1JetZLASEJ6s9hJHcblkTFUmfw3P1Fl0Hf0Y0TuYepdMzFTCqVvYhpGjSO6ExDyWO4DZVzztnMQHGPoqMuNXXjAEbX4BOnKZNpP2_LhxCuWAmosXjxIR5xOwWI_vephaP_oR38VcyAV0UhC-aZ-3kDgxoX1D2w7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b9f4c114.mp4?token=OGcxO-ZTYV1lMJWZ9_UX1vXixxUSZV34ajtrlYaLJy7xFaMkw68a3rq38GVT4uDaaIeMK105FljNjYn8c_Z06BCRFaIptKO0JPHx9FTCdc2amgLhBDFMfiyW4wmMRn92Dlv7t2fKbxr6nt9kG8KOkkxRMjlh4Ym3XP-8wv5RACKqGzuuLUmqUd1JetZLASEJ6s9hJHcblkTFUmfw3P1Fl0Hf0Y0TuYepdMzFTCqVvYhpGjSO6ExDyWO4DZVzztnMQHGPoqMuNXXjAEbX4BOnKZNpP2_LhxCuWAmosXjxIR5xOwWI_vephaP_oR38VcyAV0UhC-aZ-3kDgxoX1D2w7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
من به دنبال تغییر رژیم نیستم، هرچند که این همان تغییر رژیم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/132072" target="_blank">📅 18:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740daf8e44.mp4?token=Anneaq-BPAcyKnkgdTqglGPGLV4YiOzr-MLTqJsI19fpE4DKKlNNGV_Oq-VmpWZRsZu19QQq7qdBnku_PjRqci0XV-3piDQzMjp_55gFA4vpmrMUq-0VpjwD9MU7B4QJW2nip0gifXzGfH6b2Z3IW7V8hqX1IA6ugj_5mmfKyx_7lT2azLmd0lBRNmcmRnHawlFCMXIL_nNE7mVPjqV-pZzAEAnt9ztcqtxqi7kdiPXcWKV7Fu9gTso3AT06fYTIxYunuB0ewcPE8RvAYFZOni2cNQgmdPtMFnRBqIk_wD6GMvYS465oYI5R8hKbTK-wnKOoShesmABBs4ilydaK5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740daf8e44.mp4?token=Anneaq-BPAcyKnkgdTqglGPGLV4YiOzr-MLTqJsI19fpE4DKKlNNGV_Oq-VmpWZRsZu19QQq7qdBnku_PjRqci0XV-3piDQzMjp_55gFA4vpmrMUq-0VpjwD9MU7B4QJW2nip0gifXzGfH6b2Z3IW7V8hqX1IA6ugj_5mmfKyx_7lT2azLmd0lBRNmcmRnHawlFCMXIL_nNE7mVPjqV-pZzAEAnt9ztcqtxqi7kdiPXcWKV7Fu9gTso3AT06fYTIxYunuB0ewcPE8RvAYFZOni2cNQgmdPtMFnRBqIk_wD6GMvYS465oYI5R8hKbTK-wnKOoShesmABBs4ilydaK5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد جنگ پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
🔴
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
🔴
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132071" target="_blank">📅 18:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfaf82d48a.mp4?token=dph0VDgRBFMP5BdAOucb0oSPhTV6xodA9fM4E0n5iTJZv_ue6eCHqmwnhaFcjgDcFXqlvqjqEP4FoSnbfHYI6V_wVo-qJWbx3db0ZRH--p62x2TRJsRDrgnD99YiqqYBrh4La5qImXicsF92-jFP_C9B60g24bqhhgZTUnWvrTn6-4lNDbski-TFof3FRB6zdC500z0w6oLotgz7c2EKqmvFu_xPn0-lQpH0IGySUMYakD3Tb0BM2mJHvrSRRIYCzK0bxgnEK7FYrftvz4ZTEVlpwsYHfyYCTn5ghMFt4MAcCHMVwnC60z28t8_4S7B9qFt6rHxMzKmo2j6ZAmnlQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfaf82d48a.mp4?token=dph0VDgRBFMP5BdAOucb0oSPhTV6xodA9fM4E0n5iTJZv_ue6eCHqmwnhaFcjgDcFXqlvqjqEP4FoSnbfHYI6V_wVo-qJWbx3db0ZRH--p62x2TRJsRDrgnD99YiqqYBrh4La5qImXicsF92-jFP_C9B60g24bqhhgZTUnWvrTn6-4lNDbski-TFof3FRB6zdC500z0w6oLotgz7c2EKqmvFu_xPn0-lQpH0IGySUMYakD3Tb0BM2mJHvrSRRIYCzK0bxgnEK7FYrftvz4ZTEVlpwsYHfyYCTn5ghMFt4MAcCHMVwnC60z28t8_4S7B9qFt6rHxMzKmo2j6ZAmnlQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته دبیرکل ناتو در آنکارا: اگر شما یک جوان در روسیه زندگی می‌کنید و به پیوستن به تلاش‌های جنگی فکر می‌کنید، دوباره فکر کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/132070" target="_blank">📅 18:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b1f31782.mp4?token=Ulplcr02h4X4CnHFzyC0aIOoa5zFsU4OY6QitGRFMiayfGUGhJNgvaBX4mG3a3ohWYDkeL8C60vwqcD6Rs8DTpsJIxuwW3urqu0kOy3jJUC8TYMCitZWiChdMGmUo6BuTQv6HKJVToCpqs5hOwu_zflZ4WZ09gFXcaO46xw4gesDd1axBcUuhCCXI1wYXIKeUTJnFMnR21okBpQ9cRP8fYuEBeOCcVAyVYveQnDxSQYHLv1FWJ-BgflotNv1MB5O9hWnlFufDujx5_QY0_xyJPMPcEsav8z7WXtlE3dAiUdcUkhzMuDYBsdhwLSztpKow56dsZn_7XUbRAXUJ6VS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b1f31782.mp4?token=Ulplcr02h4X4CnHFzyC0aIOoa5zFsU4OY6QitGRFMiayfGUGhJNgvaBX4mG3a3ohWYDkeL8C60vwqcD6Rs8DTpsJIxuwW3urqu0kOy3jJUC8TYMCitZWiChdMGmUo6BuTQv6HKJVToCpqs5hOwu_zflZ4WZ09gFXcaO46xw4gesDd1axBcUuhCCXI1wYXIKeUTJnFMnR21okBpQ9cRP8fYuEBeOCcVAyVYveQnDxSQYHLv1FWJ-BgflotNv1MB5O9hWnlFufDujx5_QY0_xyJPMPcEsav8z7WXtlE3dAiUdcUkhzMuDYBsdhwLSztpKow56dsZn_7XUbRAXUJ6VS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تنگه معروف هرمز؛ ماشین پول ساز بزرگی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/132069" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0da10c12.mp4?token=Qdx9aqadCTI9ByF3pSoz4SbFZxi1pHEMkbSUKPOeObW8GrxTe_IeyNWh68fYYdZXh9ukTeBL6eDKBXqEMPcAMtD_Awjm3PApbH3w_9qGb6TS0QC8iIIa3AtB1CI-q_n7OPybheec_aC3bDUbaLt0vyPeSYy8n0oVQ7mexbB_w6oe4io-dtUVFhBm3kf5cBc9ARrqFTaBvmpLzWnl42p93YvSjGoi54qrzMvP83ZE7vJRZVDOg2T6sV8IwjlR1AsFF97FvbaAc2Hp9QZ2dPqFfooHP6s-AMQBFY6jjA37qpMVIeGSm5fsFqawEcXxE9ayXxsULvjrGbrDCfRO_p8LaLKg87j5ctSDW0FfCfMARli5lfnPXUy3MKJBk5YXgEx0NY9_PdL3qbDKbR5TQ7JwNGlcYV8LcNXU12P1GdSn8Nzlf_IcIXgrvdXDSEP0ppzZDQ3zf-H5o2wT1pdWTh1oSqmQgHFdPcHfbUW7T8oAk7Hm3GbFFwADyjLlONf0zZCxN5673Y7sw744CkPmKVlKoGZ_2fzdgHusKLhr9NrKw6cH5gOWSefXAbojWn49vc7wW1c1ykHI0huE4FEtAqt46l3JPaqjaa0tCZNHMJz8SsE12V7ZOHQAl9DyewtgHxSpQMUA1oF0FJqxdHWmlSJOd3k3tYNnHID9X4roC-GzQhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0da10c12.mp4?token=Qdx9aqadCTI9ByF3pSoz4SbFZxi1pHEMkbSUKPOeObW8GrxTe_IeyNWh68fYYdZXh9ukTeBL6eDKBXqEMPcAMtD_Awjm3PApbH3w_9qGb6TS0QC8iIIa3AtB1CI-q_n7OPybheec_aC3bDUbaLt0vyPeSYy8n0oVQ7mexbB_w6oe4io-dtUVFhBm3kf5cBc9ARrqFTaBvmpLzWnl42p93YvSjGoi54qrzMvP83ZE7vJRZVDOg2T6sV8IwjlR1AsFF97FvbaAc2Hp9QZ2dPqFfooHP6s-AMQBFY6jjA37qpMVIeGSm5fsFqawEcXxE9ayXxsULvjrGbrDCfRO_p8LaLKg87j5ctSDW0FfCfMARli5lfnPXUy3MKJBk5YXgEx0NY9_PdL3qbDKbR5TQ7JwNGlcYV8LcNXU12P1GdSn8Nzlf_IcIXgrvdXDSEP0ppzZDQ3zf-H5o2wT1pdWTh1oSqmQgHFdPcHfbUW7T8oAk7Hm3GbFFwADyjLlONf0zZCxN5673Y7sw744CkPmKVlKoGZ_2fzdgHusKLhr9NrKw6cH5gOWSefXAbojWn49vc7wW1c1ykHI0huE4FEtAqt46l3JPaqjaa0tCZNHMJz8SsE12V7ZOHQAl9DyewtgHxSpQMUA1oF0FJqxdHWmlSJOd3k3tYNnHID9X4roC-GzQhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کارت قرمز بالوگان:
من [به کارت قرمز اعتراض کردم].
🔴
من با جیانی [اینفانتینو] صحبت کردم، که بسیار محترم است و به گفته آن‌ها، او موفق‌ترین جام جهانی های تاریخ را چهار بار برگزار کرده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132068" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ راجب هری کین : فکر می‌کنم کین بازیکن فوق‌العاده‌ای است. با او گلف بازی کردم و خیلی دوستش دارم.
🔴
گلف‌باز خوبی است. واقعاً عالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/132067" target="_blank">📅 18:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ:
نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
🔴
ما می‌توانیم تامین انرژی ایران را مختل کنیم و تمام نیروگاه‌های بزرگی را که ساخته‌اند، نابود کنیم.
🔴
هیچ پولی به ایران نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/132066" target="_blank">📅 17:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af6138603.mp4?token=gthX2TyY3GkhnSr4GaK96WARHM-l2aATuTQni-9aEwatdppaYsCtWDAp-hWwelpd8p5_QI_BRt6CMjjkhOwt6B2FZcIR9j3WHTYvjJy-IQ7tYM8I_6kLD2L7ukWW5ShZykVUsrYbE6vJ2asC3y2zjq1Byw-gQZw4LTWhitT9kPbbRNMwD4LkurtHvjpCIqwQs0p73OSoNwSQCMDT-Io-S1L6ljCAp7xE7BKIbGTq3Os69UmDHzncvSgrGgeyxwJTGNQ5fMuQuY9g6NGFIowx-vA0Z-7Jq78k7i96B_OKpdOI2W4o4soMG95A1VoaxNEgaVye42R9c9xPHbsCcmoJskuX9gsoWLY5LSvrvQy7pSMhve0yYjVcFQ76w28XRsu12ndkhvln6sCXLWswPf7W49XQAU7I3Ehn59kXYiIlsCM7s91JNlHl0Dfv9L-Kknfz3fwXteZKD9HQf2_U_uOw0theHNwPpF8gF9K_JngAqz8dXafFNPtXdK2BMAQ8UkkdRo82yENOEwbmuH1fYYds79vy5VVwTuSjHJh6rQ9CK4tSuWg2TTopM4ADkusABjl61F_1RMJmmJ0O43kJa8JIAZ4GyKSJabAR2jqPXecAE8YpQ2YLmTn4eRf8naeWYmyQNZSsXQwBKyA2JN4pcUsmFVn1N5WrTVl6WGJJKf9LNcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af6138603.mp4?token=gthX2TyY3GkhnSr4GaK96WARHM-l2aATuTQni-9aEwatdppaYsCtWDAp-hWwelpd8p5_QI_BRt6CMjjkhOwt6B2FZcIR9j3WHTYvjJy-IQ7tYM8I_6kLD2L7ukWW5ShZykVUsrYbE6vJ2asC3y2zjq1Byw-gQZw4LTWhitT9kPbbRNMwD4LkurtHvjpCIqwQs0p73OSoNwSQCMDT-Io-S1L6ljCAp7xE7BKIbGTq3Os69UmDHzncvSgrGgeyxwJTGNQ5fMuQuY9g6NGFIowx-vA0Z-7Jq78k7i96B_OKpdOI2W4o4soMG95A1VoaxNEgaVye42R9c9xPHbsCcmoJskuX9gsoWLY5LSvrvQy7pSMhve0yYjVcFQ76w28XRsu12ndkhvln6sCXLWswPf7W49XQAU7I3Ehn59kXYiIlsCM7s91JNlHl0Dfv9L-Kknfz3fwXteZKD9HQf2_U_uOw0theHNwPpF8gF9K_JngAqz8dXafFNPtXdK2BMAQ8UkkdRo82yENOEwbmuH1fYYds79vy5VVwTuSjHJh6rQ9CK4tSuWg2TTopM4ADkusABjl61F_1RMJmmJ0O43kJa8JIAZ4GyKSJabAR2jqPXecAE8YpQ2YLmTn4eRf8naeWYmyQNZSsXQwBKyA2JN4pcUsmFVn1N5WrTVl6WGJJKf9LNcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ خطاب به مقامات تهران:
یا قرار می‌بندیم یا کار را تمام می‌کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم قرار ببندیم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم.
می‌توانیم تأمین انرژی‌شان را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی ندارند. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132065" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
