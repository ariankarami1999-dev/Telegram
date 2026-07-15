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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 171K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEQYYWgOAdUAGDHWSJyG01ge7Ol6bl7MfCiPCiPtdm9IRq1x4uMQKXyhOHX8-H_gqyXI-2HUfQ7d2yvPhHO8Okx1WA-_hquLua6zyzlF7Iu1dFRKDQjcj8yFURBp9P05JgQvPPOk-FRpMz8Kw675ExoBDcbPodma0N_rGg_ELnFbX1MTfWm5dR35BHRe4N1G3trohBFhNHT6zLkEaoQ-c2i6rJpKpuZ-j7ZIaBTsSMl_QWmN_RybHlKPp5uW3z6Mr3xSvpP27gSjVLhpmtH9CtbHy3SUodullvtYbprnrONP2WF6PiVsCuL8aVW9aZoSnx_P9Pq4X251B4p43JGuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuNlz9JoFGV16ojlrUBLMih6UUYa-igFsf2CLOyEB_0vmAxxyxrDzfCGpaUIyEhRc98Z_V2TXUWlGqHvyAteLTbrxG7Ue5RwCoXF8vwq_K9O-uooRcjoyfZw7Str2jr7RMUz_W8VTSRGJ1bGcBvbIC1_5R0Yb01y9IbYp5vTkqN5c1rWiWI6qZqrAgaNy6CSuDN7JA8TdzLnJ0urR78s3wVwsagLZlsjjgod3eSYeXb2jG1iWsRqaIlta-ABGjsz9oEQPzlUpbKpjk8FaHACKCeNusiChjp2slPdNSgdW1gVPcHaWtAfREmCBf7SNPoFwA8jVPyPkWbY3ODFo23LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksqSjg8n6CLwx8xkpnWZjJCmU5GubEPqEj1Ko3iL3Beu8RYmte7Ll_5GrNsqT7peMC9hPqqUV6QGw1Z5Ld1sn0MARHfqoxIlKXWvMYf3NwwqoKbn6rHHTlTYqXgnaHM9DXDbe6cYXG_vpSOnArZZvTacXaW7wIcCkkBz4O_3e95KiKaT1vqOSZBiMklSDXfKZGoidPmyZ-jLuED6UNK55tD-5Sbe93eYGur7JdD_3oYlcxQMOlygwA_Ixj6g0xah3MGjt7QdsuO-rEG0A7X970ydgQMEdFwmGr5D9OEUne0vHWqvoPE2nzbDS_k1FU-_3Ot86Zak4nnpeZxBEhhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuqjLK28YVYM6vM0RB4Djuca9WFuWPiGND66o_k4ZmmdEz8K_5lAeudahkdKpHJiVKhuUMFwAJPc3N3ZjmPhhLrtaJpJUvf6OIfF47aGvhL-GcxF-o05oc-2Wg8jYWYMD8wSGS5UK4IuWARNQGJNL8Fy2JKfF21Wu2oKI5gw8SF35t2_Oy1iKayidqAi8rbOaiPInJYZAoP4cDIml6npmOg-RMtRkSCLu5EAcTlFEgN2B2SEuL2HODDCx5QW5cqaNis9TJqGTfmdNpGc6_8a_Uv0TxxpNNy6alCoAc7oDLarjMkCe4zR8aiD8o2KnCpHRWM3ozW4jQPInQ6vwMSQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPZSYaTN-Rh-BT-W3syor8mQL6dF9yZxmQu4uxzBt-6cqBuP0dLqz6gD_7FXcrlK9tehmqrEDviTDWuW890NKJpuY1Srn1UmFPuuCyjt8bxvpMSzJSi9bz6N0rjavtvtCEcvuidfJhLb9HSCGInRIApSYTHgDibVZ8oUMwCbuSxxQjDaRdgm0v9ZwCsCljqiYl0oyXPKg5KXeULQGWB3JZgqrweXaScRibVPtB_BmTS4j5Ix7VfDO7a_t5oWIS6qsaNkMoY3Mjc0R2qvWEdcPRlilwfN_VaDUOOpHEmspwSlvtbPOq2CzDyhn4SWsKpsdHi_EA47A8om4xX5rFwjfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPO2AgPqYWAqwtP0WFQjm1TAeKQTaNcANatm1H6dtKdjytZU2ufV6mYLUH8EOoz9Mwuq0Q-YbXNh94KZalnYFtpGXww5mBaGv5yVbvfGA85HxLT8sE1xOU4fgyKNG8_HdhqJyvRyGUL3DuxyytXtvGJ6sPrrH-U8mER2EudF9UO3n7bDEUxVuD2piCHcMKREcYJQEXp1brwqSYMu7A3ZF8s86rIbu33AQVBMcQPXNNFXi-3VrcHUNNmRQoRLtiGItnZT9Uuaeq742z3bx6uHIJuK4Y_mSUo1FKXYPwuRPKLzAgh2PtGXdsowyBDOKzTtQaqIUL64PXFKzdYnTJzqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKSPKEC6mZjbHdmghtj2F9263_Ng0Kc4REMPHto7kM0dherxA3ts_FjjWN0oewdfMQ4DftVpSUcLB29i24OjjBjn0vRwX7VjM1GW5UDQEhfUgHESJCrFMMqq_wIMjFZoKR3P1CNDM4iojQPac0J9TVuI3woUDojSfVXObeeEdT4L1C8tTLmxmH2pULiVlQRES3ysxDZuREpZX4OQg3jwPwl_W1McEMANEWO6gOTeiFU_Lwwo70aPS2ydPQTuZSMOSlyrebZPJmSTSdtsB1NI_Kg9TEUscO0ZlS9UxEDKpzjDuRnyF2nJsiPFfcFC6njqDQa78-o0TMcJCPwnG632NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DI9lqE4sA3BBcqZRWqexaweO4dvG_cz4uz1Q4AP9Q60osj_pBr05qOOKhy1ZTvV3oMIGKgXNvd6PH4NM64PlozWEphc6w7JS1mB9KgG8AxWhFY6lML7Zu8P1c5BMV_R9w_Zkpfi5tfP4J_YAlVoDx010R3MpV8N4Pq8fDzjz-H2tSeMuNQs2x6qQkiI2uAXqzWZJqjqee2DK3q2VqZ2ZcVaHLNT1XTj3DHk3Oo2k3T1_4AtT3-sWrtdeBvU6bKQaPmmVxuWiUJdDQ45wbA3nEzXklTruIN0kqZjA488eB6TWE9kYxpF4ziBvs-8SnfSuic4Kf6l8CfEnE7Yi1Hqp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snyHiyjQ_OZHqXq6sBFWW4XIo4lJYXSnSnRHeQRQf0RGAPuSoOqI-ckJYMnWAw89ZnT9IzUA6WEOopsTAplI_sXtt3eBFtn7EdvH0H8s978yR88uPuJmsR01CM48SyeeU9ee6bAm8hBjkYSY_v5W_IPSc1uRzlxHGzIk2oMcsJSuqlxGb7qqXvXazDaeYeWN68HGiDiIuAcpwuLE-AoL7N2jjpqjIcRW2zdHl7HAJBDZZXSLIsX-7Kx6mXZwPFHsF85B-iI-zvJoXA1fvZeDGt-0hdwFqNVZ1LJ6PspekjV6MhMHXYXZMv5r5isTuU_QmtK37_sCk1z3MEIR3ZrNeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzXVSI8rV2an8u2p_e0nxQD3mm5SZA3gv3gGvJ50C46K-w-ti2wkBq4AphtjAGSkUnDV5iX2pUEAOfkhSaItWLJ_tSq881Q4W6GAriEPxEPDzfNRyfZQRsF6zlFh5xt5KlmhnH4mJrezIkJtb_1AEIHXe4L-B7dwsVQuSf4mYS4C-6r0B8jhjBRrPvdO9CGhChbT_2SKTdYYWCziLzPwS5aPWAFNydCz1wGdVBuc-lFyeCXMS6V4lcnvSyreBPX1ATUILSWv2S52QeKMBItRPNl1eFgMf6YmXpdKy3jpGmishSJl1FWg1pqfVwaw-f3Q-ql4qt5vXmz04oiGpbiUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYCrAmTkgUZyGi5Df8cLRnwQgHnZiVXeFV7ADVfACje1fwlNjDXyp6RhbAdUnuqeCuVOR3G5PG4W5nfBtoWCdE6rtJqGaDdf9_68ci_HOCoFF_IpzclofBIcXAhEzWgxHBAjEwiUgRCgG5O_R2DCq-WxYlyK2MrTT2naGteQ7t_ZF8yqwtDly3dL0YnbzJz9LA3N6MbbxkAQ46Xm46E6y9a0Dn76srgnPcLIUhVAKQGZD_JTHdPvV0caXRC67Ag21UjPy72VGOAEUMptW9eDYUP3tiuMKfIKA6qxu3XNBPLcPYXgxC0KVNdnn5epAIzDqyIZ0iQxHnFqXWEVdXD4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=n5Z6jBbNa94sOqM_Bw2kPhVnHqEs1U2EP_qlIf6Jt7wNC9_vcoVJg2WP-N_W83p_lYLtxIu-G-yxvquV4ZZChraPtVJsikvVm-oZUHFwOzlH7MzZUm8S3vtJ8h9mX_bePdeuLZbqcxy_cwfqo2FpJpxT8JME7sMvQfJYgfU4Wt-snS__OFOZbTv2W60WO_0fzWImY4uJK2VtHFGUF7AEa7aN-NOFhyCwSRvJW0NK89kBGhj1Fys3QOpI83rgVooAx44POgM1QmZXowIhM9cM8C6DrQHCorBN4rW1OZnI67hoBCO5nI7EHbvvfRZ_iGKc3eQ2ky8jkyEVSKR8zp7Aig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=n5Z6jBbNa94sOqM_Bw2kPhVnHqEs1U2EP_qlIf6Jt7wNC9_vcoVJg2WP-N_W83p_lYLtxIu-G-yxvquV4ZZChraPtVJsikvVm-oZUHFwOzlH7MzZUm8S3vtJ8h9mX_bePdeuLZbqcxy_cwfqo2FpJpxT8JME7sMvQfJYgfU4Wt-snS__OFOZbTv2W60WO_0fzWImY4uJK2VtHFGUF7AEa7aN-NOFhyCwSRvJW0NK89kBGhj1Fys3QOpI83rgVooAx44POgM1QmZXowIhM9cM8C6DrQHCorBN4rW1OZnI67hoBCO5nI7EHbvvfRZ_iGKc3eQ2ky8jkyEVSKR8zp7Aig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr49x1ssUWT38DVLWLt7GBu-kq6GgAUGdgI1Mv9OveYi02Ph3-l-VzJnRtR2Did2vdAaviVbsw2EBvcvCoSs-p8br3N6ix43ytWfoD5LgjoSGmUICx3S54qeOQmJchQpilmZKDUcOk9MAwdwroGhSP8eFFotgCJLwM3IC2lprlP9hSLNvNpoCGYQn5PtFakTzXNmfdS2xJSfdnUAzeaK3Fyaqv1zhZZfS5vF5WHBy65LS0pwEPDbmO_vHWEaoPyB7PrPXjM6r3MEhR7fUzpRndqW8SEywnkjLZG-Qvc49zATB38CUKU_ohNmYCb2jCtv_5-41KMH4Lmu1VEu3wORyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWHoinuFd6ieOmiEksiJ1UPRw9MhMbbJNYKHbVkmJaONFID-PXyn_ylByrqmAkTHB0dbJxsLc0HAPphm4vB6Wx1gibcx_ptr8jSs8J4pK3bwHuQEgeCWor2Ny_BrnjRp8lbsCTY0rrwnFJnp6-fsGdZg_xbagycAb3GkMw10hCO9z4ibzjKj-u1dFJXRST9qa9S1MEzf8RdNwR9v2cF1m3mPlgHs1mXeCHq0VrMmVmY8Cf5c19c1fFWkWMYWnwLkmoGYz9-kka8ORpR39xwbgphL4Orwy6t2I0ugMkB3ql8UzGXi0Sjn_iIsT0OrjbdDCovHzNuQ_LpkV8p2gz6w1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTUIiPOxRylAntRXpSdjsgJmX3j4oOl24HfergxfNGbAJEYXXDUsRB1XkwQzYGk1f84Rryr-tCPMTi9GVPPAnLOgHG6V9Be-YegRWEg2gFJmcIIHTgVuGQlw6WotynzBZ7txRHw15Q4mQU87CaT6G4GHStzJoTFZ7lzPP6HnBC1yRc0c0PWcSbbBrA93UDCZFAl-UNLLSCaAKGzlXW-3VGpusJduXvwBq1e7CCJHef5ItHD6KoLd7693assVFRmRbl0GE_meOtZ5JhG_jHAv7H5f-pcUfqm-7aE4dl-OxUbosITIvrjMrFMJ64sLeYOzyfTIQH0fHzOPdrmuTPDdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAHCQcKxYsCa2hLPFY2C9MtDdamynSw7gGZSiNMtest6agTvjtAdZsTsFTqslqKG2NRflIWSZIa6o16DkJRimFA-wXVI9sNM5pJAAckK8HD1V41Yi3p6epIA7l3lorLT_sZilIKDKjXp78zC94QY2NtgMVr0305NAyM37WFJR_P6UqpjTV2My6Ik6pw3WIaX2IUNcSg6VeWOuhxnCbSsOwfnt2FhOuKAjerY0Zw6SwE3sH-Q9jVuyYWfKblER89rkL7TILYpsgD1BAk4-oaenxLxWpLdOdR6OeM7QtiCvo-CFwb2Jg-CxwE-Ds5JE0LgpuWO7eqIlX9Awr4otn1pcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VZccJcbQzEvRvPo-RnVood_zouryF6_QOkFfUZgI79yrY5P9Cp87GmjawQXzKlNV-L9NbbC1bWeFnh914phTqCkR-BPLFUOVFHeQ-mX--8x24tjc_QJXqYmwQ23K9ateibaKyDTrMM2m6qJYXONh1TysuyhwJnFXjKsQuPdE39kb0QQHqpiKixvi4AHs8Vp46WwgjqQ-8-2QuR0Ked74yOUpxvqJNenOpTvsgR6dt95Q-po3hZ-2a_6N8i0hGvU4h7KJUFNSd796_zS-tumQ6h3athxtgLDYArX0uMza7ie-pmEqiq6AYTBOZCxI6oi2sVLaZY6adaphT3G0tgAeIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VZccJcbQzEvRvPo-RnVood_zouryF6_QOkFfUZgI79yrY5P9Cp87GmjawQXzKlNV-L9NbbC1bWeFnh914phTqCkR-BPLFUOVFHeQ-mX--8x24tjc_QJXqYmwQ23K9ateibaKyDTrMM2m6qJYXONh1TysuyhwJnFXjKsQuPdE39kb0QQHqpiKixvi4AHs8Vp46WwgjqQ-8-2QuR0Ked74yOUpxvqJNenOpTvsgR6dt95Q-po3hZ-2a_6N8i0hGvU4h7KJUFNSd796_zS-tumQ6h3athxtgLDYArX0uMza7ie-pmEqiq6AYTBOZCxI6oi2sVLaZY6adaphT3G0tgAeIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=jfb1ag88AUSeJ6tXm9Z4D4vRBLdPRxk85J1vkmX-Eqh97V0dr9t-l3mIFGzEvYGmTiF3HHkU7rNtg0OttpWXQPAVzjR_IxiK0TFx2gASqcbpCEQ0aCwhTogzHdPV65PySwuTBEJqXK-XQNpxOeeZCHfDMK_OYcZQQsNPFi7E-a1V-f_On_uVuEwBrFPTS1fpkjZEZce9piBLn5BavO35-QTAQW1xrbmAcGxy0WQT088XYVOg81OKpo7WaURdTcmj_3bO-NohzgEAos843l12l90TRUr3dCJsINEtY-yxzFtEg9lS9foN140yqfAy-aES847TI9he5nh6I3hmn69RjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=jfb1ag88AUSeJ6tXm9Z4D4vRBLdPRxk85J1vkmX-Eqh97V0dr9t-l3mIFGzEvYGmTiF3HHkU7rNtg0OttpWXQPAVzjR_IxiK0TFx2gASqcbpCEQ0aCwhTogzHdPV65PySwuTBEJqXK-XQNpxOeeZCHfDMK_OYcZQQsNPFi7E-a1V-f_On_uVuEwBrFPTS1fpkjZEZce9piBLn5BavO35-QTAQW1xrbmAcGxy0WQT088XYVOg81OKpo7WaURdTcmj_3bO-NohzgEAos843l12l90TRUr3dCJsINEtY-yxzFtEg9lS9foN140yqfAy-aES847TI9he5nh6I3hmn69RjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVU_FLkDlGpXiclb5Y-xdjfXHJhvuA4xb5BvUStB3iHiVTaQeJe1dUI43X_fj2857gmHlPpff2En1uz0HWUZH3PcMInMqdxwTFfVxuBWtLThGHRTefT_Er3tbWrvJwlXkFdETA-HJZ_lqXilljifpbLq5PGhRxRSF377OrLYT97hfDGGQ3kW_NBURN66e6ze94XrZUc03_YLTPGhfB9PhdFV2kB1H5kW2pHRbv02Xh6_z-ofya-w-1SsEIQvV1V9-xt_GL02GB8rnUB3g4zj9wjK-PIRgy-d1S4JFfmZXUBLdgKNT8OJJl5_b60eJmX2LZnR3jcQeTek6rzqfxFfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=WhDLHF-ec8L-4CWT1Ahzajw1vBxssdQAVhTlFyWcVktGWscgIF4gsnUWKFgT0c7sYLsj6oever0L1zDOHjB4M3SKPz2Aj5re3mnc2lo_mFJvvNzmMo4eGOOKGMwFtGlwGsNkj5wTdVzRjXK0QWD83ejgnPQGrno82VzhUdgfArbUW953uFgPTxKafy5fgJ4q3x76Fau6wmi_hc6Mrg3xv-lFjg4bTxOOfXqDooKd51BITZS6R98Uh1HpZu2ttdHn9VCD6FUr6VW01QTMAQzS9idQCpPxHdE8ha1Z5l1YOJyq2bxvZHaQOpKC4Ccbr3YY9s0g17Oho1JqNFUM0eHK9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=WhDLHF-ec8L-4CWT1Ahzajw1vBxssdQAVhTlFyWcVktGWscgIF4gsnUWKFgT0c7sYLsj6oever0L1zDOHjB4M3SKPz2Aj5re3mnc2lo_mFJvvNzmMo4eGOOKGMwFtGlwGsNkj5wTdVzRjXK0QWD83ejgnPQGrno82VzhUdgfArbUW953uFgPTxKafy5fgJ4q3x76Fau6wmi_hc6Mrg3xv-lFjg4bTxOOfXqDooKd51BITZS6R98Uh1HpZu2ttdHn9VCD6FUr6VW01QTMAQzS9idQCpPxHdE8ha1Z5l1YOJyq2bxvZHaQOpKC4Ccbr3YY9s0g17Oho1JqNFUM0eHK9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=dlJQ6ieKy1mAhqD71zvstPxmRKziuXGDHRu--ut9Zw-sWTmwhI9i8ZIABcBHnqOPiDkDm9L3JO6V-2ZA3PPfOxdLl6SAUHMq4FVtyNrCEDSMLKac2SQjuSAJQs-eZKUBBOpvnI8AFGIzMdQu1m7Cq_haxEuTmMiVWGOEtox0crpdC4CVdW6KT38X0-2TD5cKtBgbfZHS5WOF1OU5AarMy9WCygI6L3XW7lElrKxg9ptw4JGLgrOEMEZYhbo-vMBYU9mPeZ73nLa50WUezj0PByUvoL-B78HUv4aFX-om37mOPFwZbp-0J8eRSVAR27bUqThm9VlFj8-cGhFi-5XSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=dlJQ6ieKy1mAhqD71zvstPxmRKziuXGDHRu--ut9Zw-sWTmwhI9i8ZIABcBHnqOPiDkDm9L3JO6V-2ZA3PPfOxdLl6SAUHMq4FVtyNrCEDSMLKac2SQjuSAJQs-eZKUBBOpvnI8AFGIzMdQu1m7Cq_haxEuTmMiVWGOEtox0crpdC4CVdW6KT38X0-2TD5cKtBgbfZHS5WOF1OU5AarMy9WCygI6L3XW7lElrKxg9ptw4JGLgrOEMEZYhbo-vMBYU9mPeZ73nLa50WUezj0PByUvoL-B78HUv4aFX-om37mOPFwZbp-0J8eRSVAR27bUqThm9VlFj8-cGhFi-5XSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=HyMOFFUZdLk8_PqwaRZlYvNhUAAt42prkWu41DCF4nVnYH-53l7DiLbQAPY7AC1YEsleTSM4DUpLeKGRbkpW_3X3wOB_Dg2tNNYxGi--u2HvTI1KA6LdDtqf12AEgPXlGCsN65MZeozggKPcmRD7_z1W3bt3QHYJ-KUK9vVsGQpzTomC-D9rX1igIlXu-HhTgF4FJfpVHgC0jHFofliCvPZXCBvPf_C0wixjgmXXaL6qaWltoRhJLQzg5buAMwwNShQbmJqXstTK48nOhCS4owwp5GMtCoHZqA-mbOiWVoZga5n6MqYRJBP-20eGlPQ114MWqt_x3y-BlIl7xGD_1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=HyMOFFUZdLk8_PqwaRZlYvNhUAAt42prkWu41DCF4nVnYH-53l7DiLbQAPY7AC1YEsleTSM4DUpLeKGRbkpW_3X3wOB_Dg2tNNYxGi--u2HvTI1KA6LdDtqf12AEgPXlGCsN65MZeozggKPcmRD7_z1W3bt3QHYJ-KUK9vVsGQpzTomC-D9rX1igIlXu-HhTgF4FJfpVHgC0jHFofliCvPZXCBvPf_C0wixjgmXXaL6qaWltoRhJLQzg5buAMwwNShQbmJqXstTK48nOhCS4owwp5GMtCoHZqA-mbOiWVoZga5n6MqYRJBP-20eGlPQ114MWqt_x3y-BlIl7xGD_1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9U_oAPDcSDV1FjtcxBURg4-oJAr3ovbDFjNvqSy2tTOLR4m8OX3QtU4hpKFvpo-pdtce7i5nj5X9dUa53K6rMpNIsVJV8ra2Kne_sedwT-NIvBeipgncOsgzNFcsIV9BG6yzlfEJpr_C22s7h2Bjbll8f8SmzhKReiHBU2hHwewQlB_xXr-kEGSG1JDNrKfxpFAWn1R0P7t4aZ8Yc2d2dl7Ui71ZPgzWO0LDtnaoXN8rLapxE1mtoc9JSvpcig2OA4NfOdb-hP9osrYFj9wTK1gOsESaHO7btqKb2WWLXc-4IMPgsEcQwnW-Z239uXEsoczqNqbtzbLT9WfrfQeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA0-H0VjdiUWHevLixtMTzNZWvd2wyAvYXMllK1KZ3S0zSzqOYbC63R2tu_6PLsVdWNNuzUqXg49v9bLdbI_xo1Ul_wX5klp7N-3ogCD_zyTzqJfoPJIfH20WX43Sqe58y6b_OOBs5ikNUhuaAeGlHWktZglLNdFYaNj61QLYqyXTYRG1JdUMdQrV0KIo6lT787Hhw4vwKuAplLDlzZNySku2gVFm99DacGoFbf2SS28fIyt_VOkEqzeinL8BeHAb21KZWs2geYGiSFncoSPzIXxF2QNJdhCoYShaB1WhOZgyZz6e_ZmOLdLs7948TVkFVZbgChLxhmw3DS4_mEl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZaACSUzUPRYjRPFCs0eGm6Prc6i6ZYgxVWbaszEGsu10jwGNz4JQ8MSJ7PIIsLKZSEQBP39hjDQVRLSoWJ9zFkbLheGBYE-0h7BMl6KFlPFxVhv8DmaA0yTPNQTcG-cB5XUJ4eajt5ErX7JuLiIjj1vctbqiSswoIPEaDC_Xof9hhcPqm24H-SM8UPUbjmC7LWsZhp4WMRjhprkuK8no9OoUyohbCxVkrVY2LWDWTEkx7JYMurQUPbxlI8Tn26OGXe5jrXH6CFVKMMbEKuSFJaX7_5a1px9y2LkeatNIeSY67K21xGC4v8qoT_RNgYOtMkeDe7aILT49oC-0lBeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=aXrTuVpviy1Sx6XwHTntaj9W1PpmivJ7qWuRc_C2ikp-WgaoOj7GFpfh_RU2RT3fBPxC04pftg9UJEW4plGGlmjRNRjY44GyLvddeLmZksHVr4VQg7W9GtvHgnzQFdQzTKBAXMcjEaLiBMSx5EP85QUZqARUPTDIiPKaxGyZNaTTMJq3NFEwUpKQ7rxuZmvKerw2TUoOU9RqBbqS-Nc_A4d0nPfYiPHy_uUiNWT710bwzto98Vv-imNxEMtk1OnkzCC5llFRkLDI1WqU-dhrh6cETWWShKrAePZ3Sbg2rkFB0gHdQOi87oMC83ZnUdl2ShLYysJ5-qk7GkMqLcBVIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=aXrTuVpviy1Sx6XwHTntaj9W1PpmivJ7qWuRc_C2ikp-WgaoOj7GFpfh_RU2RT3fBPxC04pftg9UJEW4plGGlmjRNRjY44GyLvddeLmZksHVr4VQg7W9GtvHgnzQFdQzTKBAXMcjEaLiBMSx5EP85QUZqARUPTDIiPKaxGyZNaTTMJq3NFEwUpKQ7rxuZmvKerw2TUoOU9RqBbqS-Nc_A4d0nPfYiPHy_uUiNWT710bwzto98Vv-imNxEMtk1OnkzCC5llFRkLDI1WqU-dhrh6cETWWShKrAePZ3Sbg2rkFB0gHdQOi87oMC83ZnUdl2ShLYysJ5-qk7GkMqLcBVIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ-21ISTo-FdHi0nWlNHf8vE719EUijxZE_a8XrLVvZLyBV7VGCor1iEfaBPzrEP_LGJLIZVc-3GSYxee6nfHUimm-JPdxxacoysoeGKFYk12LT2laggD1yX755gP2BOf5Ezxgs61oEwBkPOsmlt236Uv40-h4HDPBhVJCRCMn5okdjTWeXe_aAvgvPF_pmTzTRV7CFoVPpouTzJ8EHdWkTFDNi1nkGadlf4NHuNLYOM33l-UYaf19CkfetVLlxUzbyzGNs1sxVoIUFMYcvTkcv3LvxkbJLqF1c-gJCf7_KM45iqIPD2Cw64mz4UEo3rObmSyLBse3G_a8A-15btQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlgdXHkWIkRy9TQCHU7yLUB8Q08-PJdqg7vqxDxI9lcZeq01Sf1xTpGob6qkghpNqpIgvOPQlKVzz4UZd7L19KPp-mgJpYRhcOFpfl3q10jISfR9XUmmGIY3hWW2Bh3sGZvkFn4L72psPM67HqWbH9wRVBn4c8AWaKC0QlWRG6ZL3hcMCl3IV4XgJ6vd1p8G7IAKP7Z9IAc973xhjPWJDiRXp5TMtR-3uleBe6Nvg92EYwLO5VEKMUrtrKXu99y2vXAYvekpjnTFS_6tASeJftMP3sLIKyheygM-Z3jriUrndsbggcrnKyfupSQWBqnCeseLgNh4_JtlQjhUaEQ-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jr23bwwXsQpbCkvo6omEd_m9pxqa6cKoFiXyG0vDmbjJxDtZiLW1JpHd2ga5Pzz0u9DSmbjcQwUIB5RBJ3yosILgHs-wFwPHXsgbF92us3kZOmMSGRnsp1a2xNojlIxd7T2uK5WMD1fDLtClH2dS8N2SUz792YI9Vp5v0H9IMAmKm7EU0b4SJD1456s4BRYTGp6d4aL9Djr3UunY9RlL1AnSJzyKL1n4sIilt9Zu_q4GRz0tne4vdX6nywJ3jVpX93fqs_r740HoxoH-t8Bte6hvhvayEr0iLVXyswRbfF2GxANaIPEtdkC2Acc_1Wman8P4YKpQUKiAp71JDpm3IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=aGTaQu6J609XhC3BqX3s1j2jnJ1qVGpRYSz1eTsCfgW5SXkKfJGQsn56xFeknPatAoC0lfqViATY513zXpdzmF6rzigwpU_cd3fRDgcdA8tBo6xIbcB-43hyEbUhIenMtGJbBh-UeVFdd2Rr-8XIUisrVsMDe92sLuSZShhmz-OOfIzyw2sBlsFZFKGeOHTsV9lx3rDEVEpU81Fw0wvX5tdghy6PRr5-bagXUknA6AjocQkrY7k9bgh-6lv8yVJr0KcsKD9ECEO6q2Y_4jtDF_-RaCQy0xrEy7a-aQDCzZqBzU4DO4ty8jxWV7-IWrvCEqdE3zcMqh1p_gZFIC6Zlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=aGTaQu6J609XhC3BqX3s1j2jnJ1qVGpRYSz1eTsCfgW5SXkKfJGQsn56xFeknPatAoC0lfqViATY513zXpdzmF6rzigwpU_cd3fRDgcdA8tBo6xIbcB-43hyEbUhIenMtGJbBh-UeVFdd2Rr-8XIUisrVsMDe92sLuSZShhmz-OOfIzyw2sBlsFZFKGeOHTsV9lx3rDEVEpU81Fw0wvX5tdghy6PRr5-bagXUknA6AjocQkrY7k9bgh-6lv8yVJr0KcsKD9ECEO6q2Y_4jtDF_-RaCQy0xrEy7a-aQDCzZqBzU4DO4ty8jxWV7-IWrvCEqdE3zcMqh1p_gZFIC6Zlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQCS0mwOq7urJmF2_hSfR6Nds6bifXYfIsjg4p2x6RZLViRQZn5NPRrlkHsnQX_7wVS-7Ekd_UASFM3yBemSePS2GNIAbhcKcTl9gRotPDaTPuxh4fxr8qMJ_c2OhoKjbktjaWHJR7cNdS-AoHAgwvd4jw9rc_JTcBUYyW3F1gt5YI0ExlmiURVV_ZhJgwgaYyx4dUZtiiZaKRRfMstdWZ7aTRZVn-l6D0p39Xg84QnON2_6Cxs9S8DvgGy-XKzBocRgTlA0xClu9c89P6mBPRQe8AsA__sg7RLm5-jg1jyaJ_6t0bjhoLkhcp6IaDjtiwKNoigE8OhKPmCLbxtyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyzQMECdMLvxgLt9KCelQecNb1byA4bawrlaNQn1EbkGEe_kufrB0q-OiAmk_cm8cthxcbUwKgG2j80syJ5n1RxAZ6OP8GOTetY4ue7pRXp7sr2-uid1R8mhxbP60vrpELzRlEf9dlB0SGwvZrNxEg4Xa5UlNccX52teIKshvPNZv3PVg1-nImRtPdgMC_rJw95s1RgBpsXBHFHxAFaHmYkkMVbaTdkutHs8MOFfyw1dTlUGqHyxQL3r774LDTlkcpblhdnag8Rg6UnZkqVGVqV3cSjsAgdDX2DZ2aMsUxetU0TmVbYktymQ4fg8ZRgQaL0CUnAkq132bzCTIHbIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRKmciiGVR22RtWw6yPuJLvE5E0VSUm3ZIvJgV0aE-b46-pFgxOQcljKqeObth_ZPwPZM87Sm4dxk9k0OkP1sN-FuC9s4lJZyd-pU7W12w3sgkE9gwc8BQW-8LDM3hiDfABrTFNI_bz0GTvi3zPR85Ip-YzdabU5KM0HByjt-yIUnV6TmEYlzjxkqTj1v1jDRKZU-zvFSiitcecrTaEGixwsH9z9f-FDKQlo9X4xj-s_rbSSet5x29LCWIhpYT28dZBmsVcCtkvQQ_prIMJKwh0h4dEtJ3MoGBVASL2nwOuywRRMjiWtvpF3MZ6SRwo1ZAn0Ie2feJ3eRTCTguMRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=mMNUIqx207cPtIYlFAKS_kn8rDbhC20_s9ljI9Z16mRO60pp4pYaXq3EzG2Y2k4oMgSb9sDER8n219m0ASlLavHWMWqA7efYogWgWQ5EGUtGzqjbwtzvjfChxzfa68p1ptE0SVe9BTPzRMFidu6b_aV-qP3OvknYmsEGfONKfxrxRVQZ8_pk6ML7jKCB7xsEo3WqfDGr3eGVVyWYY-uh98tcYzykxtfxQHEQ60htb6Guy2jLIS7L1QCd1iIjFsCHKnX4GHzoWfn9uFv9cuzMTJvMRRdDcR714AvdxwulBdU655CFtefVSwUrLo3e7023FiQc4T66JhY6BqieHqbn_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=mMNUIqx207cPtIYlFAKS_kn8rDbhC20_s9ljI9Z16mRO60pp4pYaXq3EzG2Y2k4oMgSb9sDER8n219m0ASlLavHWMWqA7efYogWgWQ5EGUtGzqjbwtzvjfChxzfa68p1ptE0SVe9BTPzRMFidu6b_aV-qP3OvknYmsEGfONKfxrxRVQZ8_pk6ML7jKCB7xsEo3WqfDGr3eGVVyWYY-uh98tcYzykxtfxQHEQ60htb6Guy2jLIS7L1QCd1iIjFsCHKnX4GHzoWfn9uFv9cuzMTJvMRRdDcR714AvdxwulBdU655CFtefVSwUrLo3e7023FiQc4T66JhY6BqieHqbn_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkCJMtudpO6_CTWSQ-4pYfknYKJqIHIBkq4HFROijHJWg5DpI6W8X4Zct7olLFZxRwdABmVF0t20xf88OzIDRpB2ClhYQjiiynXgr_zkQC42Mo2K_WLvRIoivRBW7Bf1chsFTe1wLE5r1wWnAjjZ3k-hLsD13VXxlRfsb8ZL_lnSMHpgwoZozrZRR2cLyv1vH26hOnPMU85FnfMxzidW3jFYEglGRfsmITyg6pMtxsPi7vqt-4YBUFNC-UeChyb-TPTmsFjnD5plN9pcpr6_U0nNtTFRYJO5yFXRT7uqWKZFJ9MOPlEWc-TboOuBiYsKU6lueNRVThjjKlzvuOkmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=nlnFxnIbS7Dvx9EPn3pc8RjaxTfDlTriGn1pwUaf4-vRTVGCtgmo9zZMyuL62rkfA5ePuyIQzs0W75qzUEKFps0LLRpxEPH4AHLY_BUV6gekWNL41x5IqysqHeuCT3EPuHpOVUHEm4xBd4P9WyTtQ9_YvOpnj3W2qaAP-R-iSBYbhZsRjLVehMEmL89wbjLHqpX-SYjnRZCkCmugId4LXhqLnERo-TFwW1YGZV1YkaiUdq240o1NDY7f2TN7hUFuae-J5MiKNKp5OE9MnVeNCV98lebIv0NwFkvfKI14m4rwjr3-DO_u8u5Vqx4340LnAkUIZlw72pf7qSAM0nKsGosrrfC3DXXERcEOYeYkHTBk1CuSODudBjo9ae2MW5s3ElE6k6WQ353WAZi5F4XsDR__BVKvdhuW-iOvu4BXITYP6K3vSyjFNluo3d6zYMPdnoVsN9x0tp4E-z9ZMTPBU2P11mGg98dp_LeH0B2r4zSubqsGrz9DQxosBTYJB2BaHbTFwxRgxaUv06Y4iouES7PQU-UHttRZ-A4bJ_9YVEHqiPJc23GFhzgUiifuA_dREg_9GffAER7AcEqu4oTc176m2lLYJXgleahYFb01BUgAA-A15iLwy1p2kHUCfIDEoGJMDGsbbJiJ95DA-ZSb2VeoUxe6BelEGqQz4HV2ajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=nlnFxnIbS7Dvx9EPn3pc8RjaxTfDlTriGn1pwUaf4-vRTVGCtgmo9zZMyuL62rkfA5ePuyIQzs0W75qzUEKFps0LLRpxEPH4AHLY_BUV6gekWNL41x5IqysqHeuCT3EPuHpOVUHEm4xBd4P9WyTtQ9_YvOpnj3W2qaAP-R-iSBYbhZsRjLVehMEmL89wbjLHqpX-SYjnRZCkCmugId4LXhqLnERo-TFwW1YGZV1YkaiUdq240o1NDY7f2TN7hUFuae-J5MiKNKp5OE9MnVeNCV98lebIv0NwFkvfKI14m4rwjr3-DO_u8u5Vqx4340LnAkUIZlw72pf7qSAM0nKsGosrrfC3DXXERcEOYeYkHTBk1CuSODudBjo9ae2MW5s3ElE6k6WQ353WAZi5F4XsDR__BVKvdhuW-iOvu4BXITYP6K3vSyjFNluo3d6zYMPdnoVsN9x0tp4E-z9ZMTPBU2P11mGg98dp_LeH0B2r4zSubqsGrz9DQxosBTYJB2BaHbTFwxRgxaUv06Y4iouES7PQU-UHttRZ-A4bJ_9YVEHqiPJc23GFhzgUiifuA_dREg_9GffAER7AcEqu4oTc176m2lLYJXgleahYFb01BUgAA-A15iLwy1p2kHUCfIDEoGJMDGsbbJiJ95DA-ZSb2VeoUxe6BelEGqQz4HV2ajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=rNKNIPCACObLm1boHZ2GZTknXXAmiZ_4MNYXYtgjyZ-eyUen45Sh6xy2A9UvUssCo3EjEalxWf1P8uBWjCEpHISVCabw86J26_h4GdGq6RQ_lHmcva99c8kj54Fdn1xQPV4Z0qrm7f_pNSfTqvOW06itqrvTyOFMiTkMdAV9i-4BqG_f52e1VZ6-yFNdx95YYbFlNr1WeEPakYjhHckzF5KhEeOZh1XGr3EjF7SpC8OITA_28FUdPnLTV2BBFKNVtKP6r7fBtCS2QvEKf0QiDXiBjFH0CtfZtDo-6SGCN7o1a64jY5FsqazfEF4CNdYFHTdsznV0o6575qwR-BozTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=rNKNIPCACObLm1boHZ2GZTknXXAmiZ_4MNYXYtgjyZ-eyUen45Sh6xy2A9UvUssCo3EjEalxWf1P8uBWjCEpHISVCabw86J26_h4GdGq6RQ_lHmcva99c8kj54Fdn1xQPV4Z0qrm7f_pNSfTqvOW06itqrvTyOFMiTkMdAV9i-4BqG_f52e1VZ6-yFNdx95YYbFlNr1WeEPakYjhHckzF5KhEeOZh1XGr3EjF7SpC8OITA_28FUdPnLTV2BBFKNVtKP6r7fBtCS2QvEKf0QiDXiBjFH0CtfZtDo-6SGCN7o1a64jY5FsqazfEF4CNdYFHTdsznV0o6575qwR-BozTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZw_7ZkTJPZp_Zzkmn-QCM13QpuwuAv--vNyo3usdFOt0IzyX8UkS32Aea6AfLnWLr3kKQ5KBvnTk3I6HmijEKr06vDLTUkARPkFvzxiuzFjptXPVqyOiWTJucCNZCCItbwWpydDgFvmm-oUwR1l3l1bOnSbWyV_LgqRAF82hU-XLPebrbdFqtSDL0kT7H7J4fWzXQONTgw8JJ-JCY6PQgIQAO1wTw4k8EK6T-_oB7OAzFTZf-QI26EBytiHwq3B-Oi0WtYixd_LzzN4wNoAwR3INKQQVFGGrw5p7-zsX0LGViy0PHCdnql6-POwZKqcUTjaFsarGo-ftlGsR0uItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=Gj50xd2pSVxS0BtOlom0G_6Noh2Nim39vJyrBNzYhhd17BQ-uZq2pRE2DmSQHCJ08r6TAn3uU1Rv3S7y-O0zpJFf3Km0F4yTnU_dNeHRBMAseFHPwNV06frhbs51_HU098VS62-r2vR7bDgMBlG1mfGKpY98mMYTiAHt7wVl55PnpRmAgL5M0Lo6RstsNJ_TvSYTf1bxBKf9azuB00scdbwFN36TUh4jK6rpN9B8QFzTXi86E9NzenhqbrjVVYrPj_Uuw7u3OaHE2KrJqk8hHd7n1Ip90X6HzMEQA2k4dOXrSy1TrbIHXCSLVZeoqKBrqDImHXEe3PmaWwASXkX3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=Gj50xd2pSVxS0BtOlom0G_6Noh2Nim39vJyrBNzYhhd17BQ-uZq2pRE2DmSQHCJ08r6TAn3uU1Rv3S7y-O0zpJFf3Km0F4yTnU_dNeHRBMAseFHPwNV06frhbs51_HU098VS62-r2vR7bDgMBlG1mfGKpY98mMYTiAHt7wVl55PnpRmAgL5M0Lo6RstsNJ_TvSYTf1bxBKf9azuB00scdbwFN36TUh4jK6rpN9B8QFzTXi86E9NzenhqbrjVVYrPj_Uuw7u3OaHE2KrJqk8hHd7n1Ip90X6HzMEQA2k4dOXrSy1TrbIHXCSLVZeoqKBrqDImHXEe3PmaWwASXkX3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=eRMniMPPps8ekyZgSONeCorhOH81AwKppjh0HTSvW8WYYVM7CvH7pNKBxI6VvGJhi6P1RfbEVguKDvHJNpzXsTfm8EufkFPR2CaNbRRam41XrRODr7AyapJy1jl2NI4s6gK5oQ0lsJpxlDTT0MMQYZNPdE1g2FIR9dZP-uEm_ujIzH9jw-NGKn6x_jgzALEyUSey2cjzOXyrnHXwn_ZvR8EELzpeb4UfK3wRjdS8KWU_gRapYsF1pyFODe4bca3q1q5ZBjm-zqG61W1IV310vAXw99F6Z8dL-oDoBYtqJ0y9pFzKtpz3ckgMfzChb7VLW_X5fg3-WTaAcYP3i0IY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=eRMniMPPps8ekyZgSONeCorhOH81AwKppjh0HTSvW8WYYVM7CvH7pNKBxI6VvGJhi6P1RfbEVguKDvHJNpzXsTfm8EufkFPR2CaNbRRam41XrRODr7AyapJy1jl2NI4s6gK5oQ0lsJpxlDTT0MMQYZNPdE1g2FIR9dZP-uEm_ujIzH9jw-NGKn6x_jgzALEyUSey2cjzOXyrnHXwn_ZvR8EELzpeb4UfK3wRjdS8KWU_gRapYsF1pyFODe4bca3q1q5ZBjm-zqG61W1IV310vAXw99F6Z8dL-oDoBYtqJ0y9pFzKtpz3ckgMfzChb7VLW_X5fg3-WTaAcYP3i0IY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=ZYkQzDgskb33igSEMTU2BwVQn-tpZ3S6eglrO4Llp6XAhp1XgRMRG5IcotwHiS1MlFt2j_ZJSJBdRKTOB9J7JIbtNbCDuJLiNGgMvSl7JT81uRyo14QUTDi4l1QBpvHq6myAg6JgU1uttINEEb1zX9DWWfFYKoJVBlU6CQJK0-ySYuV-n5PLbb0adTlR2PwDETzEWgDOZvJlWcXbCq4efCAt1irAkyIgud6pQVUVRE0hr8hZ7wl-8d58q5uB7OQxe7iUVaz4J-O5kCbB1H3lS3dSoV19ZYNIWrYo99Yo72_CgkPED2lMcx2HU8OHhl1ZLgVNMEHoN4f3_qA1UwHVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=ZYkQzDgskb33igSEMTU2BwVQn-tpZ3S6eglrO4Llp6XAhp1XgRMRG5IcotwHiS1MlFt2j_ZJSJBdRKTOB9J7JIbtNbCDuJLiNGgMvSl7JT81uRyo14QUTDi4l1QBpvHq6myAg6JgU1uttINEEb1zX9DWWfFYKoJVBlU6CQJK0-ySYuV-n5PLbb0adTlR2PwDETzEWgDOZvJlWcXbCq4efCAt1irAkyIgud6pQVUVRE0hr8hZ7wl-8d58q5uB7OQxe7iUVaz4J-O5kCbB1H3lS3dSoV19ZYNIWrYo99Yo72_CgkPED2lMcx2HU8OHhl1ZLgVNMEHoN4f3_qA1UwHVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=J3EY6XTjFTHLl2XLr-F2ooJnxKg81hvmvR_3laykuQjshrzfJcvDxdk5Z2ZmMMSQU2fmgQq0IhQMK5hBwBxdye6DAApH9bCadsOPtD-P2UH3OBa4qnQ1EeN_98sVIc5zcmqNAt1qfQhNabO04e0vqAmJxSwW-h8_dKTqfr7VC5lO09R8VDwCQMPmphz_WMFCbKc7Kgu1dbgCJ-71n1O-2P1-ezA3eD-j5Mc1J0dhs-x5xgGau6L-daFCrHXRtT_Gx_MkrR04_Y6IdrKMR62f7WLv4jr_M-FWq0QGqJtnuWpJrR8jgHzoSpQ992KB9qW7ZJhayGqrGtNK_sepTqRIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=J3EY6XTjFTHLl2XLr-F2ooJnxKg81hvmvR_3laykuQjshrzfJcvDxdk5Z2ZmMMSQU2fmgQq0IhQMK5hBwBxdye6DAApH9bCadsOPtD-P2UH3OBa4qnQ1EeN_98sVIc5zcmqNAt1qfQhNabO04e0vqAmJxSwW-h8_dKTqfr7VC5lO09R8VDwCQMPmphz_WMFCbKc7Kgu1dbgCJ-71n1O-2P1-ezA3eD-j5Mc1J0dhs-x5xgGau6L-daFCrHXRtT_Gx_MkrR04_Y6IdrKMR62f7WLv4jr_M-FWq0QGqJtnuWpJrR8jgHzoSpQ992KB9qW7ZJhayGqrGtNK_sepTqRIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=O2abjh8TJ8gUohbcCVWiT3IbC2376c51s_XbhraZgYXDcMVUIjvsN9cY4lFB0FoAj5DkmfBhltBiQsOltq18FpFnNwqXIKZYZomditDtsQkz-kM0LOaxvLEz_2WWXvkL4B_aH7yUMJ8d4ey_7wv0kAAS-KVGpB5tc2rUl5ZMOkoaLfetXaUY7Tgb0TF-3FpVQ2L3uncMwpd6e9gJ25dniTvVuAihoxEC3O1HPh8noCwJQd6Mra8wkJ6-ExxCJyWUTiYcyytMad-sqTvcY4N488NGOqfWp9g3W18xZsPUSucQCP72JuukjRs3RkiZJ_210ttY4oR1EysI-KLefUImJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=O2abjh8TJ8gUohbcCVWiT3IbC2376c51s_XbhraZgYXDcMVUIjvsN9cY4lFB0FoAj5DkmfBhltBiQsOltq18FpFnNwqXIKZYZomditDtsQkz-kM0LOaxvLEz_2WWXvkL4B_aH7yUMJ8d4ey_7wv0kAAS-KVGpB5tc2rUl5ZMOkoaLfetXaUY7Tgb0TF-3FpVQ2L3uncMwpd6e9gJ25dniTvVuAihoxEC3O1HPh8noCwJQd6Mra8wkJ6-ExxCJyWUTiYcyytMad-sqTvcY4N488NGOqfWp9g3W18xZsPUSucQCP72JuukjRs3RkiZJ_210ttY4oR1EysI-KLefUImJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=NuhsthK0h57MJ87ZRB2hbN8m0_B36a90V4O4WYUWGZiCQkzrDSg64vG8rTu_Ivpk4w5cKx3L72R67D0Bd1WLRZl76rqBNQcTVqmXEBSwmPKFkqrrFNZ8Ckz9GP1WOGJnj5oSWAm2HbB5Z8q31uNarwGsRVv2wP94F6xDqevvZeugNPnnKM2dBvIbzW-dU9zT5f3gKTHQCI4Qdh3khp8PmtGY5DFLUIHLw0OgFllcxZztIXBumCwNqW_OGa49wG8PmAx4Cgj-KZS3On0QaMVegNb0pZH49iWQxgu4a2QIGepOasuh4BchuBf72eqmVindSDrlqBeEt8vMECog3fouAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=NuhsthK0h57MJ87ZRB2hbN8m0_B36a90V4O4WYUWGZiCQkzrDSg64vG8rTu_Ivpk4w5cKx3L72R67D0Bd1WLRZl76rqBNQcTVqmXEBSwmPKFkqrrFNZ8Ckz9GP1WOGJnj5oSWAm2HbB5Z8q31uNarwGsRVv2wP94F6xDqevvZeugNPnnKM2dBvIbzW-dU9zT5f3gKTHQCI4Qdh3khp8PmtGY5DFLUIHLw0OgFllcxZztIXBumCwNqW_OGa49wG8PmAx4Cgj-KZS3On0QaMVegNb0pZH49iWQxgu4a2QIGepOasuh4BchuBf72eqmVindSDrlqBeEt8vMECog3fouAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=ryaGhOz-P51OqonHkogL2BTamaS4T5Svg9XHa4cH1_aEN01MOdLYIllDhgqvfIXYE2zCaOclHJFgKCpDApWeCA4wSLyT6nlnql7YWKEhoyCEHahCY7l7eYD1wM8XppN7kcac7qUp-B3be7Jo2wtflE_EE6c6xC2RCpEMpkCC2anBRs4HPVZwZwKY2f3FwgQKekvG67NCmWa2u-XdC8KkYdIJaKRQOjDl4-qKk9Acxm_og7Gph1bYhjjsQCGJBe0oyZ3Ev3Gi38CS_4KnqvhLwAP72KslBHiBM_Ynl-T8uQyq2UjLxfQoJJO2jMrsQnuFnjbKuSPovP3xClbydvUwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=ryaGhOz-P51OqonHkogL2BTamaS4T5Svg9XHa4cH1_aEN01MOdLYIllDhgqvfIXYE2zCaOclHJFgKCpDApWeCA4wSLyT6nlnql7YWKEhoyCEHahCY7l7eYD1wM8XppN7kcac7qUp-B3be7Jo2wtflE_EE6c6xC2RCpEMpkCC2anBRs4HPVZwZwKY2f3FwgQKekvG67NCmWa2u-XdC8KkYdIJaKRQOjDl4-qKk9Acxm_og7Gph1bYhjjsQCGJBe0oyZ3Ev3Gi38CS_4KnqvhLwAP72KslBHiBM_Ynl-T8uQyq2UjLxfQoJJO2jMrsQnuFnjbKuSPovP3xClbydvUwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=EJq9uZrryprbWuWZ75R0S8WpYOfiHXBFXnVr9ppm-rLxDT4Pm3oHzOgYw1arnD-IBSOkqFvQKRjPAR0xd5rG8ZCLib4ERkiTaCNqQRfq2hNRjE05C5dyBlaTK9xkeo8uGsPZ_wu7kHbI7WuwwVrrVcfeI_q2Nu15enHD6bb3ubUzHWZI_sUmVBBPveNQcyjR9EhKRQ7wk4AbB5vxNYqQU-a8-yv8v_P4kE9dJp1H94erIojOf68REy1o7I_purfypcctMmJrmwAY6oGaPSEGeMsuCl8T4wyVeHsEX5VWoNl3tAdQ5b_zKU9x-Xp6t3NHI4NcN4TIUtD6PT1WZQ14LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=EJq9uZrryprbWuWZ75R0S8WpYOfiHXBFXnVr9ppm-rLxDT4Pm3oHzOgYw1arnD-IBSOkqFvQKRjPAR0xd5rG8ZCLib4ERkiTaCNqQRfq2hNRjE05C5dyBlaTK9xkeo8uGsPZ_wu7kHbI7WuwwVrrVcfeI_q2Nu15enHD6bb3ubUzHWZI_sUmVBBPveNQcyjR9EhKRQ7wk4AbB5vxNYqQU-a8-yv8v_P4kE9dJp1H94erIojOf68REy1o7I_purfypcctMmJrmwAY6oGaPSEGeMsuCl8T4wyVeHsEX5VWoNl3tAdQ5b_zKU9x-Xp6t3NHI4NcN4TIUtD6PT1WZQ14LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=BTe89meGprgk-LxyHYQELjN3qyPM8irXmwe_5fbPbOXQlFGaYCpJS83_NTgc5GctS6fkS-Sq9LKjYcfWgKHjE7tcYJf75gfN9vz0eibOwgcQRDw4MmWfP3tFlk4UEihSQWiGqey3AmVOU_P79Cain-6aAmZqNAP5eHWOWYmVIB2DhsBbYhWiDSbw-JruLZxKeZbZJK4U1R_Mo7zljca9farCaMJIAiPDaSM0MHeO04b2W5ku8JyWt3YZa_tFwJzs1830Ukt1fZ7K8Cey5lau00tYhvKy9WfQ37vZnpBLEiJkin6g7u9CiFBZuO3a0kgYVbMjwp-57HS1uEMauNOelA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=BTe89meGprgk-LxyHYQELjN3qyPM8irXmwe_5fbPbOXQlFGaYCpJS83_NTgc5GctS6fkS-Sq9LKjYcfWgKHjE7tcYJf75gfN9vz0eibOwgcQRDw4MmWfP3tFlk4UEihSQWiGqey3AmVOU_P79Cain-6aAmZqNAP5eHWOWYmVIB2DhsBbYhWiDSbw-JruLZxKeZbZJK4U1R_Mo7zljca9farCaMJIAiPDaSM0MHeO04b2W5ku8JyWt3YZa_tFwJzs1830Ukt1fZ7K8Cey5lau00tYhvKy9WfQ37vZnpBLEiJkin6g7u9CiFBZuO3a0kgYVbMjwp-57HS1uEMauNOelA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=kL031LnfA3eqPok_gzQKtF2O0qEI4AsJnG4vEPjV8tl2DAthleKDbHDHjRBnwcHVgwC9A3ARF1baJDXYI5DtHyBPofR8ZYn1VVjC93u2t_NRIH4vYz6syUDRbaGGRVmy7ctRBJ_x6rUR7_dvjZOciahAMMrp_9uYzDlUTsStAfTefgP-tukxgELKUCoUArM5oYMBvFrhzSPNhh0lJT4mwLocf4NSQyyl1NUr8Bv2_g2VLbVsFPR6_9a7rd3IePHE5GsJ9FEiW9uObFL_wnu3_cLjKDI_cezq5gbetGkPhx5Z61zlocVsKIzys6Nwshk1ztwSd7W6LY3C4anRXIoqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=kL031LnfA3eqPok_gzQKtF2O0qEI4AsJnG4vEPjV8tl2DAthleKDbHDHjRBnwcHVgwC9A3ARF1baJDXYI5DtHyBPofR8ZYn1VVjC93u2t_NRIH4vYz6syUDRbaGGRVmy7ctRBJ_x6rUR7_dvjZOciahAMMrp_9uYzDlUTsStAfTefgP-tukxgELKUCoUArM5oYMBvFrhzSPNhh0lJT4mwLocf4NSQyyl1NUr8Bv2_g2VLbVsFPR6_9a7rd3IePHE5GsJ9FEiW9uObFL_wnu3_cLjKDI_cezq5gbetGkPhx5Z61zlocVsKIzys6Nwshk1ztwSd7W6LY3C4anRXIoqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=vTASpmB1dY3zRggOHvXtGeUNvTF2AyF3uhj-7ge0jWGuB6zsRwIP_JnLJhSzdrMRZCjP9MWNmRTY9deB2SRdr5zKrjdlVzolpBu-MI09W-NvDgyqCaJnJFyCGJeknQQa0SXvxhHDFRttABzG2QzYeihDfN-3xCLSAiCYG4EpzR9pKGV74hOLgQwB0k1iif8ccFK2wcfxg6IH-vkxYygXjXPh0QzaVUtB4u4CEJsJNFECQZZ5k6Pz2-AE8mbGt1QoqAmivYZtLSm9Norwjm-XP_J8_t5kUFaJHIrmGFttP5eKT821MTV0xiCNFqQ6l0YelgVDhInJWBtoQ80BJX06NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=vTASpmB1dY3zRggOHvXtGeUNvTF2AyF3uhj-7ge0jWGuB6zsRwIP_JnLJhSzdrMRZCjP9MWNmRTY9deB2SRdr5zKrjdlVzolpBu-MI09W-NvDgyqCaJnJFyCGJeknQQa0SXvxhHDFRttABzG2QzYeihDfN-3xCLSAiCYG4EpzR9pKGV74hOLgQwB0k1iif8ccFK2wcfxg6IH-vkxYygXjXPh0QzaVUtB4u4CEJsJNFECQZZ5k6Pz2-AE8mbGt1QoqAmivYZtLSm9Norwjm-XP_J8_t5kUFaJHIrmGFttP5eKT821MTV0xiCNFqQ6l0YelgVDhInJWBtoQ80BJX06NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=CCHRWjnKHugXFy_OMQQyarYkmMkDRTmF_jLliv_QPOlMG6qUSRnBvD-pPY-6fBbJ19-367zDYo8zsrPrfspFFwlQn7XLrH36gizuEknLvM-cN_yuYHUdy3tGeH7hHSuxaVTfVfr3GtqS-1i30P7LsOnbj87ia4TQLo3LrL4dpuhKVkOcFxNd15K_yrOGvwhOd1dUZjsGYfiAC-XlQV0YXFnfItB-cGVH04FMyCB6ZBofu_TAeUnVIJnL9sCdecF8qhklv1TVA5vPpzmG08P1gPb8KwMU6mHPKsDOpTWk0mEHzzWivK91Tuj0jqM7pquSkyxnOcWgwgjEK4NSlx7Xfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=CCHRWjnKHugXFy_OMQQyarYkmMkDRTmF_jLliv_QPOlMG6qUSRnBvD-pPY-6fBbJ19-367zDYo8zsrPrfspFFwlQn7XLrH36gizuEknLvM-cN_yuYHUdy3tGeH7hHSuxaVTfVfr3GtqS-1i30P7LsOnbj87ia4TQLo3LrL4dpuhKVkOcFxNd15K_yrOGvwhOd1dUZjsGYfiAC-XlQV0YXFnfItB-cGVH04FMyCB6ZBofu_TAeUnVIJnL9sCdecF8qhklv1TVA5vPpzmG08P1gPb8KwMU6mHPKsDOpTWk0mEHzzWivK91Tuj0jqM7pquSkyxnOcWgwgjEK4NSlx7Xfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=jpgEoDSo_UGbixakGKfRpo5iuIkNeIGZ62FQReOpQ_Ms3CnGlMDkZBwAVTkrA6nlANWAQR_5xJwiOvvHuKAI_fTLcWsvgXihPDlDxi98a5eGC1-2L7hAh0LtMUS02bgqehQD1G1TWiOmmqeXjzlibNA8EiPf3m8PpxtzMeWFVHCPpyXsNczgZ5KvisISHeFVGm78nq3PJwUa3U1vf_-0hI2KQiLRVgFN6-NliADdeKQFW6sGuGUm3ivXh20G10S5f3qU6I7-_JrY0T1-D7VGVkhH3ygEyxMuerujKiNAazHi96CaDtPo2EIEOwVZ5G90-vHCvRi9w-LMIICwJyUtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=jpgEoDSo_UGbixakGKfRpo5iuIkNeIGZ62FQReOpQ_Ms3CnGlMDkZBwAVTkrA6nlANWAQR_5xJwiOvvHuKAI_fTLcWsvgXihPDlDxi98a5eGC1-2L7hAh0LtMUS02bgqehQD1G1TWiOmmqeXjzlibNA8EiPf3m8PpxtzMeWFVHCPpyXsNczgZ5KvisISHeFVGm78nq3PJwUa3U1vf_-0hI2KQiLRVgFN6-NliADdeKQFW6sGuGUm3ivXh20G10S5f3qU6I7-_JrY0T1-D7VGVkhH3ygEyxMuerujKiNAazHi96CaDtPo2EIEOwVZ5G90-vHCvRi9w-LMIICwJyUtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
