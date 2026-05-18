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
<img src="https://cdn4.telesco.pe/file/kj6FYt6MiYv7UqQB4ePZW9H_3yEoLRJgCBIdHqn3kTJs5IFDgp2OHNgxxg5RsFzbx7xy0bA-bU-GMWs90JvYR6OwotU_ikfSgWts4mpDlxjyR_8B_HbcFOpo74MAnpvd90n9iNCKP5HfMmgl281Jlz1_RjZCkqJzdYywyI0roVA4fiA7Vp7Ztf9kP9diPl_jwjk6BtB4QJfN4N5uwtoC81e2WVBnJITraTs02ybrJ662ek-InhaSAo2jPJW_FaWVeuk0uPrX1o6Omb5mVC8Eaw1cjoA7xhqPUhiNFC9Ewy8eDXDAQtLlFQjIKP4Jg--gkjcO40YBQMzgwH9wgi7MEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 21:57:14</div>
<hr>

<div class="tg-post" id="msg-120935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: بر اساس نظرسنجی مرکز ریاست‌جمهوری، ۷۰ درصد مردم نسبت به محدودیت اینترنت ناراضی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/120935" target="_blank">📅 21:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEldIHRBxunDOGWAC2c-TcHe3EJo8d_LohJdcGsPiaFJEri0AIUS8iSWJXRteVqAeJDyPbvwyTMmz-m_xW8qbn0YOEfCIWWPm7deepXRneVcGj7e3NQ5snoiyS8HHD8zlANCeoqZJhvvdh0MnGbfX1iWR88TU0fz7QO9US-e4m9TW22VuuvFIeP_cVzbuCx2BIdI4VSX4rPSdrHbhi1Y_VXs0cm5tl1zd58rQZBABrLhpLOS4-LHjbNXdJ60qO1ZvyEt-KjfJmKQtoReGWf5QWSNckKcQiD9PXMHgXnSEZNOw989U7syc7yq0lKrMloqNClrgnU-BVDHDTrFGDYC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالار آبنوش(ولایتمدار): آمریکا اگه تسلیم نشه باید منتظر موشک‌ها باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/alonews/120934" target="_blank">📅 21:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a95ed2f7d8.mp4?token=ur_paTiw2oQKVYmQHFO2B1gVg4f9QBEP1xyi6G7tC7KFBxoIrs0mSNTRW35ChkMmL2zLHAG8sUhVdpJMdD19wtpO4otpCLVu54AAR7Fc6jqZ8kgiBIk47JnKYbXkH2M2yPdRYGdbZdnXvBIq-LS-HcEqI3HntKjt1KrOsN1aQXI5YuKfD5Lx4JCfAI0pg73IvUx_7Aqeaak4OCUTSF7-eQjQfX5IT1m_0CT8VIRA-12gCPAdoMlRU_t_CEQ0k_tr3iQVYQU0lePrU4MhjC5vfFLEELyHiq5k8VdSfIZ5p2klxgJEp1alCc8k_0Vfr1Lb4M8cFFgu56hPh6GorkG4PhsFQV9vh6fwCZsDU5DKhpbCldAOi1n0tP39Hphf0kyuLpaCWm7zIu74bznqPRiC27Q33yu7VYnh_a5V97XbDc6OsDtCMhvlMzjy1Mwf5Hm_q-AILayjGIJ30xrIhjdUWp4dNBnQ70l2YanoZMoRwMy0vkgrFISC8TjioEbxN6ncypvDAtocZ_Dm66peCDE_A3LZUlG15rU9kHYseXBmXufQ1TFZ5OTz3FMoukdjrncvboB7pmOOIa_8u0LCDPp-XasIX_4D6L4Wf8HbT7drof6MGJJ9oY11mvnA7TfuFx7abhc8khZPG1WVsTdpGyG9zveKCLlvmgccpl3hSHRc5i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a95ed2f7d8.mp4?token=ur_paTiw2oQKVYmQHFO2B1gVg4f9QBEP1xyi6G7tC7KFBxoIrs0mSNTRW35ChkMmL2zLHAG8sUhVdpJMdD19wtpO4otpCLVu54AAR7Fc6jqZ8kgiBIk47JnKYbXkH2M2yPdRYGdbZdnXvBIq-LS-HcEqI3HntKjt1KrOsN1aQXI5YuKfD5Lx4JCfAI0pg73IvUx_7Aqeaak4OCUTSF7-eQjQfX5IT1m_0CT8VIRA-12gCPAdoMlRU_t_CEQ0k_tr3iQVYQU0lePrU4MhjC5vfFLEELyHiq5k8VdSfIZ5p2klxgJEp1alCc8k_0Vfr1Lb4M8cFFgu56hPh6GorkG4PhsFQV9vh6fwCZsDU5DKhpbCldAOi1n0tP39Hphf0kyuLpaCWm7zIu74bznqPRiC27Q33yu7VYnh_a5V97XbDc6OsDtCMhvlMzjy1Mwf5Hm_q-AILayjGIJ30xrIhjdUWp4dNBnQ70l2YanoZMoRwMy0vkgrFISC8TjioEbxN6ncypvDAtocZ_Dm66peCDE_A3LZUlG15rU9kHYseXBmXufQ1TFZ5OTz3FMoukdjrncvboB7pmOOIa_8u0LCDPp-XasIX_4D6L4Wf8HbT7drof6MGJJ9oY11mvnA7TfuFx7abhc8khZPG1WVsTdpGyG9zveKCLlvmgccpl3hSHRc5i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
ترامپ لباس‌های محافظه‌کارانه‌تر را دوست دارد. من این موضوع را به سختی سال گذشته یاد گرفتم، زیرا سنت این است که معاون رئیس‌جمهور نخست‌وزیر ایرلند را در روز سنت پاتریک خوش‌آمد بگوید.
من تصمیم گرفتم جوراب‌های چهاربرگ شام‌روک بپوشم تا نخست‌وزیر ایرلند را خوش‌آمد بگویم. ما در برابر خدا و همه مردم — احتمالاً صد دوربین تلویزیونی در جریان یک کنفرانس خبری زنده — نشسته بودیم و رئیس‌جمهور شروع به بیان سخنان خود کرد، سپس نگاه کرد و گفت: «با آن جوراب‌ها چه خبر است؟»
پس به سختی یاد گرفتم: در اطراف رئیس‌جمهور ایالات متحده به صورت محافظه‌کارانه لباس بپوشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/alonews/120933" target="_blank">📅 21:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni2B1TSNCg2owruJdTFjyKpddt_3trFZUgyCQe3uKxL1lZoUZ5hGtXuZPKBNZ-Q5wx9ftNMKf6L68tL2ipL1XS84SH7enb-4rMZV1j3HC8NhzKi-BFTmIJdqmTs4P_jrOHutlFak5mUKzKMamyQsZeocFlRNbUOXNGBqVoUn9bw_Jo0Iw9uE2AhoXdAFw1SwfDh-f98Prd1zcMu_lA6md9Ix88e0GgkdlQoZOghr7VGFB2HGXasM-oqAOrKFcVMh3xoB1LaS6mw7VaAcJH5_pJwY3xL5mvd1jMpG9zKFFmjYSY8uG2p-MDDAVZ-TQB0Qy36ahbULjJvAmaqkar2Oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالمالکی، وزیر رفاه رئیسی: ایران هیچوقت دچار ابرتورم نمیشه چون وقتی یه چیزی گرون بشه مردم پولشون نمیرسه بخرن و فروشنده گرون نمیکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/alonews/120932" target="_blank">📅 21:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKBvnUfE01vyr8hSke2fNApiP3WibvAgc2QmPePlXTMy-IB8qqSF-Zn0nkZ10qz--eilNjY3Uz4PHUP_S7dFSzr6lvt5l3uqK-9rW93atxc76UnEjzW64by3YBh8kRlNjgJx7eRJZcZD1n17fNT15FiDlmtEVT6NN7ptVPDCBcg-KMQQZ8KXxJ_kv2-jG4uMFHpp_NQfkGGdikzZ7weirRck_V-otd8bJF_Y_blUL_tnh-Ny_wCag-KqoOi9XuUgSpkc3jdvwyzCdo3-A4yeA3_awgHJCFOm7Ca5qjjhEDzJH_ac4IuGE0qCvZrRbfaqdJfdMAPzIwIuVUOAERwq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۷ اسرائیل: امریکن ایرلاینز توقف پروازهای مسیر نیویورک به تل‌آویو را تا سال ۲۰۲۷ تمدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/alonews/120931" target="_blank">📅 21:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a835e4e8.mp4?token=t2AGqjqHW9EzoX3yDtKdzoQ1L3lk9-UfMP6LKsJXFfKYuzMlB1Hrke7PFdP9WTjF-LRg7G4YBQE0xLyw_tOYLUZBWcVsKKuklzhhtc7TOCImXKS8UnfTHAiM7HLxzAfmX01POYkXvhpr6vEnTuCwpZDa_fv-JjGJwIpoykGJDo5fhlLOQeXxaO4q5IN552-OT2QMWxUfIWxQ_aPT8Ne2WyZAxG545Ao6haNoOvTeiJ_-pSPvePIvY4BxKUNptUJUwL_yFp0czCyaKFAKMs1RBycWJnNrv4k_xfnpf7EgJDI8MZq7_FfpH_xUfhtYSy2zUpKMT7CMjZ9nZVKFyC4KhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a835e4e8.mp4?token=t2AGqjqHW9EzoX3yDtKdzoQ1L3lk9-UfMP6LKsJXFfKYuzMlB1Hrke7PFdP9WTjF-LRg7G4YBQE0xLyw_tOYLUZBWcVsKKuklzhhtc7TOCImXKS8UnfTHAiM7HLxzAfmX01POYkXvhpr6vEnTuCwpZDa_fv-JjGJwIpoykGJDo5fhlLOQeXxaO4q5IN552-OT2QMWxUfIWxQ_aPT8Ne2WyZAxG545Ao6haNoOvTeiJ_-pSPvePIvY4BxKUNptUJUwL_yFp0czCyaKFAKMs1RBycWJnNrv4k_xfnpf7EgJDI8MZq7_FfpH_xUfhtYSy2zUpKMT7CMjZ9nZVKFyC4KhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اینا بهتر از من و شما میدونن آخرش چه شکلیه برای همین دارن مزدوراشون رو آموزش میدن برای جنگ شهری.
🔴
این صورت ها را به‌خاطر بسپارید. همسایتونه؟ کاسب محل؟ فامیل؟
🤔
اینها قاتلین فرزندان ایران هستند. نه‌می بخشیم نه فراموش می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/alonews/120930" target="_blank">📅 21:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرآنلاین: برخی شواهد نشان می‌دهد کشورهای عربی در کنار ترامپ در حال لابی گسترده علیه جمهوری اسلامی در چین هستند.
🔴
این کشورها به چین قول داده‌اند نفت آن کشور را تامین کرده و کالاهای صادراتی آن را به قیمت‌های بالاتر و نامتعارف خریداری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/alonews/120929" target="_blank">📅 21:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8ed7ff10e.mp4?token=ooAfoBoHjPicvfPgvyIE6sqzqMaQKx6AH8RxXkP_EW5T2Ueou0KMt79YkZFUgQbzXMHCI1eYxczlNAnTADcbgeZj_eL4mFpHqjnYPuYBKKEdq8PjY1wYW7GGTjEVl0l6ak9eeSUGJ9PYqzIIszM4WRkdxVfIWEXWQb8aFHfUWqXaRg2JvQq-tlq77VgZsYdnkY3MlMu-HiZMr1uWewng11Vx9rh16ZReKTjb2p_Jah5IHVQTymqf4AdVPH000aG-u-SyZ2iOcPvl7GwYhcp8yjoMHpWNS_oPWbbloooeaLA7x8zmd7YZOafufJElrc2gxfBxZlBWKdOJ4MXHLmWmwnEKMepD9IYlWzjHIa006IoAp7bXyezZxGvzaZZP2OeMTZhNIgMMr-B8Cmv4pGnSmrnFGCbGeSVnQFjUGfDfOm7rYrOMySjy2Hh2w_ENlKcgaHcVzdDHMUsSHK4gnkWMoYjxwE7pCIBlYEJOJdHDo3CwVH-ve9rDjdrED_Za-LO8MKtigReerDYBoEQJqbGvkPzL2tu6ca8rUkKiZ9S8Rn98ulN0OBICHkBvBkRyDvVS6WPNhdBSdgHq3hwZ04zipzWiK3koIDNIJ-52zv7YBVjj70J25gcsbD7eQ62jSQsFP5_Hsj8ceBEk8bLZKjfUxhxU0HMJySkdNb0LZdQ_8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8ed7ff10e.mp4?token=ooAfoBoHjPicvfPgvyIE6sqzqMaQKx6AH8RxXkP_EW5T2Ueou0KMt79YkZFUgQbzXMHCI1eYxczlNAnTADcbgeZj_eL4mFpHqjnYPuYBKKEdq8PjY1wYW7GGTjEVl0l6ak9eeSUGJ9PYqzIIszM4WRkdxVfIWEXWQb8aFHfUWqXaRg2JvQq-tlq77VgZsYdnkY3MlMu-HiZMr1uWewng11Vx9rh16ZReKTjb2p_Jah5IHVQTymqf4AdVPH000aG-u-SyZ2iOcPvl7GwYhcp8yjoMHpWNS_oPWbbloooeaLA7x8zmd7YZOafufJElrc2gxfBxZlBWKdOJ4MXHLmWmwnEKMepD9IYlWzjHIa006IoAp7bXyezZxGvzaZZP2OeMTZhNIgMMr-B8Cmv4pGnSmrnFGCbGeSVnQFjUGfDfOm7rYrOMySjy2Hh2w_ENlKcgaHcVzdDHMUsSHK4gnkWMoYjxwE7pCIBlYEJOJdHDo3CwVH-ve9rDjdrED_Za-LO8MKtigReerDYBoEQJqbGvkPzL2tu6ca8rUkKiZ9S8Rn98ulN0OBICHkBvBkRyDvVS6WPNhdBSdgHq3hwZ04zipzWiK3koIDNIJ-52zv7YBVjj70J25gcsbD7eQ62jSQsFP5_Hsj8ceBEk8bLZKjfUxhxU0HMJySkdNb0LZdQ_8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زوج حامی حکومت در برنامه صداوسیما اعلام کردند مهریه عروس یک «پهپاد شاهد» تعیین شده است.
🔴
در این برنامه تلویزیونی، داماد گفت امیدوار است این پهپاد «به قلب اسرائیل اصابت کند.»
این اظهارات در حالی مطرح شد که در هفته‌های اخیر، استفاده نمادین از پهپادها و تجهیزات نظامی در تجمع‌ها و برنامه‌های رسانه‌ای جمهوری اسلامی افزایش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/alonews/120928" target="_blank">📅 21:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IocPaynZuibVIhnNk17dSAD4JBBfX21SIpAnbwGXct1sn75VyqUWzymyIJIwKDBmBPVbrGNgrwda2oodh2NeJZpRcHraToWp8EHPd2itntFTq2IdHYZnsMOeFM1DDLfZM-Iu-iUdNUI6fGFU5hzr70qujOhmJp9kfmzuxO88z1iNPVYJL9XEs3LrvSXkf-_8emrhHEctXOVWPJ_qQtK0qmUu4zW7PPM388AK3qluPqo8CRzgK6x5MvWA86LMj_1NGFbrY5sWIbdz9iHhY0IFFBY9FQRzHs5HupOWBXmsFouTTju2HubEq6m6g3zb5T7ZITbdzKWjuaXsmmXGYzycKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UoITXOvj-KyZio2Tt3yDzxXAoNOjnRsaymIqIjyYHBwP8bn69Fi_LEWblpsa3AXn2weigoi0iuF3dCfuHr129lo13YV-17LzRUF4pSL3Oe4x4ugPj0l0T6GPI6uFEHazX5oQXWrlQ7_wX0jY1zQ7Cdi-8la_VLiQLyHT0tT3OUPFWPzGQv3lPv3py_yxsRDAbT-OvDLxMvHqHbdUIIMuq19AlRNozqSzBp9ow4DA73S4nWZ38UiWgdJo_Pa5P2OBZ48UhqVelsYkf5oEBRRwxh-DTTe_dKpGAO3j5vqbDL1ajNmxsNkdcL-ZqGQI3Grs6Ep0cHnnD9VtOm3v4RukNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SbddxTOLIrVNSz0tdXQJkAGhBe8CcKlz3eOIeLb-s22cDiulVK2alt3U9n_upYbdo2MAqUz2Eqei4xfqO8elOkGATq4FM69gEiVZgV3WP3pm6D9f7Vyam1LxWEKbEWYsaD7PzekID_OlLVMT9dk__Q125X1LJzVg3ZxZbfIWuqKmVXLWVxnbfsyMqpyCzGJH-GebeDp8VcHxovqH3lb4ICGMNRHpMgkYOlbZIuxIs6uSS_I6KrhdQKcKGi-_mQEVacIZz7GS9nViUzPv6DKLv0Dxhkmdv5vLD2wYqGwjBPMSgpAU9j4aObHVeedrAt3rOussI0xCbwTvh8inbuNCkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
روز گذشته در غرب جزیره هرمز یک نفتکش در حال نشت مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/alonews/120925" target="_blank">📅 21:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
حزب‌الله: یک جنگندهٔ اسرائیلی را با موشک زمین به هوا هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120924" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2pm4em6ATnmvMzO7dSWMZ87hR999AgLOugHeOJNlImCpjm9VO0I8Uy1wEeyEGkV7ruGOZHoa5Q9Bl-6lBvRZxA0a-Y2n5UtUZLuktdGwchceG6VQQxTLWvHGh8Qi9P5kmDfhkRSrJdyHMb-lcgE8Mur1s9pBDYyQTCxAqLZOjI6W2cFxr32-hCCRWiX-sH9JWM1l2YNpZbKUVAVhZ2LXoRJVCvKYrdRqjAjco2Sf7Tc6h0f2_0wvdXrFHnvuK1hrdppfPbRoj5aHvvi3W6_rkRLr12kSZ5ivIE57kornYtisGfEL3W8B2pkSHKkpv9DLbvapKO__FPTqwo3r1zaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر نیویورک پست:
ایالات متحده در آستانه از سرگیری نبرد با ایران با تمام توان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120923" target="_blank">📅 21:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: از دست تهران «کلافه» نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120922" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وقتی از ترامپ در مورد ادعای منابع منطقه‌ای مبنی بر اینکه ایران سعی دارد در هر دو موضوع هسته‌ای و بازگشایی تنگه هرمز، واشنگتن را «خسته کند»، سوال شد، ترامپ گفت: «این را نشنیده‌ام».
🔴
او گفت: «نمی‌توانم در این مورد با شما صحبت کنم.»
🔴
ترامپ افزود «این یک مذاکره است. من نمی‌خواهم احمق باشم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120921" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وقتی از ترامپ در مورد اظهار نظر جمعه‌اش مبنی بر اینکه حاضر است مهلت ۲۰ ساله برای غنی‌سازی اورانیوم ایران را بپذیرد، سوال شد، ترامپ در میان صحبت ادعا کرد: «من الان اماده پذیرش هیچ چیزی نیستم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120920" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwrQx3VcNOqZhFgm6HV61R8QFx-ak8PdzKOEa4_kh9c7BeIS6dYFqtVJz3lR1HUrEBmGyRhgnufgqn7Cg7Q-J5R8_szJuwpKzF7a2PwZIDmrKwiOb7u_HlVplPaIq0VWhsqFAWYYsSNs4sRn2vt_aRP3OnxW4F21zvVJFffKhR0JCWD8sDYmRaBytFEr-lonKD8wAxqgdVi16i4XV4T7acrd4GpoS3Exds6x1UkOPhq4kbtmsnaNmgMw6d7zavrOHKgtITAWuZdTB7vr4ouh9Mv6A6p6Lr6lXmy63RhHodkHVPhj2in2xY0SvV8NbpTCrzNu6KHRWFRIQqFGgpe10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به نیویورک پست : ایران می‌دونه که به زودی چه اتفاقی براش میوفته، هیچ امتیازی داده نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120919" target="_blank">📅 20:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سنتکام: تا الان 85کشتی تجاری رو برگردوندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120918" target="_blank">📅 20:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شاخص صف پمپ بنزین تو ایران رفت بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120917" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJjNZlFGI-d3oSYkQGFBfmw-liAX0bFrbLmjrrIUnK7Kt5RjVBEYnB-y7py4v1xx3iInKTAW2hU6IpcyGMQ2FNP6Q8O7Qbo7wF1s4CsJwn2KZqBh02WZUEzZfjtfYccX8wu33-uBZlAZ6s1fNlRtGkCyBeHEtk5QgJpEYnl3Dkov5CU3F2N6uj0iq1LfD-P8T4zhWuknEjlBdVGwkTT6OlMs9oizxK0QaOb_avy0Hc_-FQlSHLtBT7EGit7kLxO9877s6jMgLAUtsckC3MbM3KurEjbW7gEr-OBhz1Uq-LjqZ0NpR1x-Owc4yHcy91ecAp8eCBP3C1vKmUhD52Xb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۱۱.۱۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120916" target="_blank">📅 20:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: مجوز موقت 30 روزه برای خرید نفت روسیه صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120915" target="_blank">📅 20:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آکسیوس: بمب‌ها مذاکره خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120914" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
جلسه کابینه امنیتی اسرائیل، با نتانیاهو دقایقی پیش شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120913" target="_blank">📅 20:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePjMt7QiUH0IMqkG_-6lDaq3TEqJpUuAy7MXvJ9gPS4H0B374UuAOL1hHnGSVIhc4kRUyCrPMGEmZjMWGBU-cJlRWITpU5RNEEOBNEt4gORoMIdLbqh09Qa7VX80d45HHuy5M8FfalNmiOUDBf1dYgXduPDdErxcY63dc8ZkCiZCIEW_PNMkoQe30CzouuTmpXQ2_83lNzToqw-FOnhldpd88SXiM7Rb62PRlel1qpK24qswxk7obEVnINT1IvQ6rfyRuDTZPPFSTtNiSXlIgzM72DQdoRh7s7fXmSRf34AuB1vLZ4E-JjHyQGreCBxZuYi9clPtrxOyaCh-f-9ILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تری یینگست، خبرنگار فاکس‌ :
- ما تو آستانه بازگشت به عملیات‌های رزمی تمام‌عیار هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120912" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر کشور پاکستان که در سفری دو روزه برای آخرین میانجیگری میان ایران و آمریکا به تهران سفر کرده بود، پس از رد آخرین پیشنهاد ایران توسط آمریکا، دقایقی پیش تهران را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120911" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120910" target="_blank">📅 19:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
طبق گزارش‌ها، جزیره خارک ایران حداقل ۱۰ روز است که هیچ نفتکشی بارگیری نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120909" target="_blank">📅 19:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQhTytRL7rv09_bANBVJWHPbjpfdhG3EGjyVwbJYg4Rs34C72PhoWDnRYmHwk46_aztokvbZwAtaNUWJBqXNaxZmo3Ak8rfzAkGigs_mHObDpEUO5GjaTl96cUmRq03QbqLTQIB8ibDYbr89_RUGafTDxB22DMik6-Wgx-LrxcJGiq9hk8lKc_i3o7U_s7-z2oQYOXLf7DaEUnvP7bISIwwSca9EdCwW7TPcyXUhjIjJYQPqULDLoz1Tmvxtfe0WoL27kiAojBgvvaeAbvEpTU1EYUW2JpEo3fp9bsrBBB9uhdve8hhcOMdS6kOK_d4j6k9QNKzZAu56-Ob-0ip8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به العربیه : داریم کارو خوب پیش می‌بریم، پیروزی هم تو راهه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120908" target="_blank">📅 19:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0Iyuh_i3kMI17L-9IPyi6gsH9EKfBKMSf1udw17xd-Nt1HL2cIYR9P2VR4ux19Trvt3s_EOSsBOozP3dUeN72kOmqtaCgrmlR7Hl5yAruJMSjnsZAL_vrbnw-kTkydFHJxMboKvNOc-OWb93jJ1hdbwo6mBg7K2_lh_d_FVPOOXF2v1ANxrqFlo72LyJqCISBD_fqwy619FAx_T4Dcdn5b1bmhHzmL39Y5pXsfwr3kzUhTTpeSQCfGZ1R8IHYZ_UgA9wYuA88p7dgmIRJMjaTwiG5suFO0R4WMvs1zKn6RMRZaDxDvVEoS8KjvHlsAtTJwjR2Q-S5m65CrDprqXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیر
:به هیچ عنوان استعفا نمیدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120907" target="_blank">📅 19:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت بهداشت لبنان اعلام کرد که از آغاز حمله اسرائیل در ۲ مارس تاکنون، ۳٬۰۲۰ نفر شهید و ۹٬۲۷۳ نفر دیگر زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120906" target="_blank">📅 19:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
امروز فقط با گیگی 159 تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات: @manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120905" target="_blank">📅 19:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kskYLLxyBJ4NviOObWYuZFrtisug7E7H9G9Jz2CEeeTYoYNzMv-bIAfvKPXI7i77yAW3JLBArB-9NYfDOrlgs2b0yhtWZ2Che9M7BpXq1_iJx_yUEfws-KZvcjqzQJCXuHMU0vagQpLWu1rugVB14jVPWmiEunZXUdXQZvBoXMoyDZju6j5jx0_89ILAuy-JyY2g4_ZkZUyKlGN3jDJv4ht6LbZ86RT9uy6ziQKDc8h7SDPl9c5swPdldX5M5GEeqJnMiKd_lDJvUCIoLT3xjeGlO5jtw20tBnp012qN95TI9utkqlNZns2x91hQHDbGVs7gWrRHVo_odknrqwjVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120904" target="_blank">📅 19:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عکس‌ها و ویدیوهای دریافتی از فرودگاه بین‌المللی تل‌آویو نشان می‌دهد که حدود ۴۰ تا ۵۰ فروند تانکر هوایی (هواپیمای سوخت‌رسان) نیروی هوایی آمریکا در محوطه پارکینگ فرودگاه حضور دارند.
🔴
در چند هفته گذشته، حدود ۲۰ هواپیمای نظامی در فرودگاه اسرائیل مشاهده شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120903" target="_blank">📅 19:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رادیو ملی آمریکا (ان‌پی‌آر): عکس‌ها و ویدیوهای دریافتی از فرودگاه بین‌المللی تل‌آویو نشان می‌دهد که حدود ۴۰ تا ۵۰ فروند تانکر هوایی (هواپیمای سوخت‌رسان) نیروی هوایی آمریکا در محوطه پارکینگ فرودگاه حضور دارند.
🔴
در چند هفته گذشته، حدود ۲۰ هواپیمای نظامی در فرودگاه اسرائیل مشاهده شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120902" target="_blank">📅 19:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سردار طلایی‌نیک: بخش قابل توجهی از توانمندی‌های ما هنوز مورد استفاده قرار نگرفته.
🔴
آمریکایی‌ها یا باید در برابر دیپلماسی و شروط ما تسلیم شوند یا در برابر قدرت موشکی ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120901" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگاران مستقر در اسلام‌آباد و واشینگتن گزارش داده‌اند که پیش از ارسال متن تازه از سوی ایران، درخواست و پیشنهادی از تیم ترامپ ارائه نشده بود و هنوز به متن تازه ایران نیز پاسخ داده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120900" target="_blank">📅 19:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fa02f889.mp4?token=gZ1fxPB8cx1jxLlLHzaO4CN-FAlSwdJRieligOTb5F6uH-Mg5CtrO20su_4KV_lVT7ONXLZY6zoVC6wypVlAGPIBw_RXaKYRg1_GzROAJsfJxwTu9YMv-sSoWBrSIqTQeAT_obGZNFYNuH8PyPn6GZ-aEOt2OtUpQivCWeSL6ohc5BT4gim1H5bzA_GxynGbVIcVlKcvI8FmfgM9FuiWpBQVnonwfEIWRUBmo-EUmNX-6OOyvsznw095LCQXAd0BsS94tsM28OW4fwzOjEq4HqevV7LyrurQy2KDy6N-8GxBzGw2Z0LQIbt1EYaGuU-IiDc16OyiJm98-pi0_AoyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fa02f889.mp4?token=gZ1fxPB8cx1jxLlLHzaO4CN-FAlSwdJRieligOTb5F6uH-Mg5CtrO20su_4KV_lVT7ONXLZY6zoVC6wypVlAGPIBw_RXaKYRg1_GzROAJsfJxwTu9YMv-sSoWBrSIqTQeAT_obGZNFYNuH8PyPn6GZ-aEOt2OtUpQivCWeSL6ohc5BT4gim1H5bzA_GxynGbVIcVlKcvI8FmfgM9FuiWpBQVnonwfEIWRUBmo-EUmNX-6OOyvsznw095LCQXAd0BsS94tsM28OW4fwzOjEq4HqevV7LyrurQy2KDy6N-8GxBzGw2Z0LQIbt1EYaGuU-IiDc16OyiJm98-pi0_AoyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120899" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
اسرائیل هیوم: وزارت دفاع از نتانیاهو خواسته بودجه ارتش را 14میلیارد دلار افزایش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120898" target="_blank">📅 19:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / رویترز: آمریکا پیشنهاد جدید ایران را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120897" target="_blank">📅 18:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری /  آکسیوس: ترامپ در حال بررسی از سرگیری جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120896" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کمیسر اقتصادی اتحادیه اروپا: در نتیجه جنگ با ایران با شوک رکود تورمی مواجه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120895" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ادعای اکسیوس به نقل از یک مقام ارشد آمریکایی: ایران یک پیشنهاد به‌روز شده برای توافق جهت پایان دادن به جنگ ارائه کرده است، اما کاخ سفید معتقد است که این پیشنهاد، بهبود قابل توجهی نیست و برای حصول توافق کافی نیست
🔴
پیشنهاد ایران که شامگاه یکشنبه از طریق میانجی‌های پاکستانی با آمریکا به اشتراک گذاشته شده، تنها بهبودهای نمادین نسبت به نسخه قبلی دارد.
🔴
پیشنهاد جدید شامل کلمات بیشتری درباره تعهد ایران به عدم پیگیری سلاح هسته‌ای است، اما هیچ تعهد دقیقی درباره تعلیق غنی‌سازی اورانیوم یا تحویل ذخایر موجود اورانیوم با غنای بالا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120894" target="_blank">📅 18:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: اولویت، حفظ آتش‌بس در جنگ ایران است
🔴
هیچ دلیلی وجود ندارد که ایران و آمریکا نتوانند در مذاکرات بر روی یک زمینه مشترک به توافق برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120893" target="_blank">📅 18:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfLka8qAVwuD9LsFWyN5KR1oibwOHFdO3GYg0HaEr88vRr8oQU47Kp_B5ZO2hMFqucqyc0WTfej8nc6ek7ZZKr3u-IrFkM6_5IquSroJJss7o1iIiCW7j-mAPrZqPDYML-vH1XRsyvyVIZwK_AaTov6Mr9VPwUq8HhZuphQkIxC8gYAKKaQnaYKw_8nBPAXopiDZrY6x4RDG6TdlF7T8YbokwzPsPUcsxhwP7cMyntIRC21UM7NlnUem4hzL78VkXfVjZzr07IWNBQXBGQ3wyK6_JycNftzbnjZA-JPncebp8W1J8E_CHx3Lcl5cykacVOQTIRLu-kn-_OU9HRyRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دوروف، مالک تلگرام: دلمان برای موشک‌های ایرانی در دبی تنگ شده. دبی پر از ترافیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120892" target="_blank">📅 18:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azRaYrt-fRyNZIa-ITvSWFbm324AdIY4gN3MQfEX5pn0Cd-oeWpdrSJJe48-4fAyHgJqotWNCdmyzqA4OVr5LFupcfmKRNIzN0gKiXHk7UEQ8wmnf5E5884QnTEcAMRm0gaevc5dj0eTDo2W7fskXMzF-DdWoCfKC0zM24n-cRrWt9yN2pLIVFFO0azwc2_eneo1SX-C1UZU37ZptFGfoJfqhpmC2qjTb7Qd4jU637lNGTxZcd0gRfVfMlx61simfxh-2oqhjb2EngcVeUnoh5gfs9P4YKhppJp0x6dE--j9to65lJHpkAGENBTomoAWVT9GC1qqizzgkb0BXoMtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اگر ایران تسلیم شود، اعتراف کند که ناوگانشان نابود شده و در کف دریا آرام گرفته است، و نیروی هوایی‌شان دیگر وجود ندارد، و اگر تمام ارتششان تهران را ترک کند، اسلحه‌ها را رها کرده و دست‌هایشان را بالا ببرند و فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» و پرچم سفید نمادین را به شدت تکان دهند،
🔴
و اگر تمام رهبران باقی‌مانده همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت بزرگ و عظمت ایالات متحده آمریکا بپذیرند، آنگاه روزنامه‌های The Failing New York Times، The China Street Journal (WSJ!)، شبکه فاسد و اکنون بی‌اهمیت CNN و همه نمایندگان دیگر رسانه‌های خبری جعلی اعلام خواهند کرد که ایران پیروزی درخشان و استادانه‌ای بر ایالات متحده آمریکا به دست آورده است، حتی قابل مقایسه هم نیست.
🔴
دموکرات‌ها و رسانه‌ها کاملاً از مسیر خارج شده‌اند. آنها کاملاً دیوانه شده‌اند!!! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120891" target="_blank">📅 18:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کابینه ارتش اسرائیل امشب تشکیل جلسه میده - طبق گزارش رسانه‌‌های اسرائیلی
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120890" target="_blank">📅 18:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کابینه ارتش اسرائیل امشب تشکیل جلسه میده - طبق گزارش رسانه‌‌های اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120889" target="_blank">📅 18:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMQ2kc8xXFyRRLm3aheUlVwHo07lMJ8ITxKe1Ds0waxAQ5vGUx-TjfipW4vTJf1enZAYApGrm55E6IGaHQ_o1YvlWM3NYxYotWbGIyWDiAh93GPTwJTJ470Vba2lz0xHSP2AzjJbKE-kOmqWk26cP2h-TOex3CIYA5LZmmPBjcXiG3tZOrpNtWVk6faI0-Qhh2QS19cZ1xLMBqNkJwr4Ymuf7Wvai0FEJ3kj7qmgYjHGh1fYeLIU2aB7ftcxvURRYHG59FuGEPvk54y3ykyYMOKcATXsilrzF2CJ6LcS03NZKQ4xcroGH0wcmVCVFRxSKcE1WAPSYleIjMi1PKSt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de0486a18.mp4?token=j-xdvRO_DjhhfCljiFLh9MJ7rUhEEAhLbNzq3TxUdqkEtOlxQ4lU5aV4Ne9tPDrF5hhp9yPEIAPVjKI1n5kbONr4yekIm7ywHfnFOyRq8IQDwpS4bSKuZmUxI1lntcBXRakuE8pKtYXscqwINSYu7UU2j13NSdXOjqwO-3fgMUxEDXgp0qOBWs6ntEaRmbrHd8mbbgUNSTRLH5O-xVeUdELo-laUHthRUEpnDjs1tmkEHqw2rToUnQmKzYXjS1i_uuKZzDEm5jrylFxz-iIPLW-Pwr_1gInP5DwUKyghLxz8FUMw6b63r-cyqAm_Nraw12hSkm7RrXGWfT-0PooI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de0486a18.mp4?token=j-xdvRO_DjhhfCljiFLh9MJ7rUhEEAhLbNzq3TxUdqkEtOlxQ4lU5aV4Ne9tPDrF5hhp9yPEIAPVjKI1n5kbONr4yekIm7ywHfnFOyRq8IQDwpS4bSKuZmUxI1lntcBXRakuE8pKtYXscqwINSYu7UU2j13NSdXOjqwO-3fgMUxEDXgp0qOBWs6ntEaRmbrHd8mbbgUNSTRLH5O-xVeUdELo-laUHthRUEpnDjs1tmkEHqw2rToUnQmKzYXjS1i_uuKZzDEm5jrylFxz-iIPLW-Pwr_1gInP5DwUKyghLxz8FUMw6b63r-cyqAm_Nraw12hSkm7RrXGWfT-0PooI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از تول، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120887" target="_blank">📅 18:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رویترز: جنگ آمریکا و اسرائیل با ایران تاکنون حداقل ۲۵ میلیارد دلار به شرکت‌ها در سراسر جهان هزینه تحمیل کرده است و با ورود درگیری به ماه سوم، این هزینه همچنان در حال افزایش است.
🔴
دست‌کم ۲۷۹ شرکت از جنگ به عنوان عاملی برای اقدامات تدافعی خود نام برده‌اند، از جمله افزایش قیمت‌ها، کاهش تولید، تعلیق سود سهام و بازخرید سهام، مرخصی اجباری کارکنان، افزایش هزینه‌های سوخت و درخواست کمک اضطراری از دولت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120886" target="_blank">📅 17:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منبع نزدیک به تیم مذاکره‌کننده به تسنیم:
علیرغم برخی تغییرات در متن جدید آمریکاییها، اما اختلافات اساسی که از زیاده‌خواهی و عدم واقع بینی آمریکاییها نشات می‌گیرد باقیست.
🔴
عزم ایران درباره ضرورت پرداخت غرامت توسط آمریکاییها به دلیل تجاوز نظامی به ایران، بسیار جدی است. اما آمریکایی‌ها با وجود سخن از چیزی به نام تاسیس صندوق توسعه و بازسازی درباره عدد آن و بعضی موضوعات دیگر با خواسته ایران بسیار فاصله دارند.
🔴
آمریکاییها همچنان تلاش دارند مذاکرات پایان جنگ را به موضوع هسته‌ای گره بزنند، که این خلاف منطق است و ایران با آن موافقت نخواهد کرد. آمریکایی‌ها باید دریابند که ایران به هیچ وجه با اینکه پایان جنگ در مقابل تعهدات هسته‌ای باشد، موافقت نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120885" target="_blank">📅 17:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تا امروز، نیروهای سنتکام ۸۴ کشتی تجاری را تغییر مسیر داده و ۴ کشتی را از کار انداخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120884" target="_blank">📅 17:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اتحادیه اروپا محدودیت‌های وارداتی پسته ایران را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120883" target="_blank">📅 17:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره:
صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در مذاکرات با ایران رو به پایان است
🔴
ایران چند روز، نه هفته‌ها، فرصت دارد تا پیشنهادی به رئیس‌جمهور ترامپ ارائه دهد که بن‌بست را بشکند
🔴
رئیس‌جمهور تمایل به اقدام نظامی دارد، مگر اینکه ظرف چند روز پیشنهادی خوب از ایرانی‌ها دریافت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120882" target="_blank">📅 17:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=uRiiP2_QH54j_vTNmSmWkkAYzJGJ0XIkSHhcsSrg8tOc3fQLqdCuSAN3xeFq_SzIhwu5Q_Xinfzcs4hMveylW0JGOkpHxC9lZLaeRvnjIv5YybS2H5wdcXoVnR-nrmi5ZCG7lEoKp_fxniXObkssSrnCSnpiyi8e6_igNSfLXTdaTv_EEdGZhOM84EgbhekYcEtfJdAsLk3Zw6D8OFNPTLaAfnFkUeXtjULWhdQMhOSCZOxAbwwbF1PQ9uwxGDDRghY9HBUDjeU3uPu3d4WTfgmXCGoddmmFdKA6NFFCUZFaRyTI7UFLQ_k4iX4AStok1wHFfcibdqcCaAd_iVcUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=uRiiP2_QH54j_vTNmSmWkkAYzJGJ0XIkSHhcsSrg8tOc3fQLqdCuSAN3xeFq_SzIhwu5Q_Xinfzcs4hMveylW0JGOkpHxC9lZLaeRvnjIv5YybS2H5wdcXoVnR-nrmi5ZCG7lEoKp_fxniXObkssSrnCSnpiyi8e6_igNSfLXTdaTv_EEdGZhOM84EgbhekYcEtfJdAsLk3Zw6D8OFNPTLaAfnFkUeXtjULWhdQMhOSCZOxAbwwbF1PQ9uwxGDDRghY9HBUDjeU3uPu3d4WTfgmXCGoddmmFdKA6NFFCUZFaRyTI7UFLQ_k4iX4AStok1wHFfcibdqcCaAd_iVcUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی این کلیپ مربوط به ایران خودمونه و برای دیروزه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120881" target="_blank">📅 17:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b6b7ce4a.mp4?token=iz3fGcSH2lAjoAnyz4NAunMvzTSydgJ0Vh5HnECoI4AvYqRAseplanSze80D1JaEAr27yvy4kTR7tlThrTlM0RffMdy6Pjtoz4Dn2dZNws3E03mnzQvSODJRIoAOOqz7rjfMfajO4aUVk8WoyXXhQzn_-N1IiGaAXDYGT6N6jQToDLhTJisvbZwFU6RIYwGclKLPgUFtwiJMNeKA0pyCbN9J-OtVUbJ72-zawBYvj_5EVElY9XGHEwFPwH_xDLyEOkKb7Frx5zV9Bk1zz0c8YDzQZbtF8e32Iwdln6B_ZP1TD3EJ2m15YYC74OVyeyljTrA_Gs7__Elizslagx8tpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b6b7ce4a.mp4?token=iz3fGcSH2lAjoAnyz4NAunMvzTSydgJ0Vh5HnECoI4AvYqRAseplanSze80D1JaEAr27yvy4kTR7tlThrTlM0RffMdy6Pjtoz4Dn2dZNws3E03mnzQvSODJRIoAOOqz7rjfMfajO4aUVk8WoyXXhQzn_-N1IiGaAXDYGT6N6jQToDLhTJisvbZwFU6RIYwGclKLPgUFtwiJMNeKA0pyCbN9J-OtVUbJ72-zawBYvj_5EVElY9XGHEwFPwH_xDLyEOkKb7Frx5zV9Bk1zz0c8YDzQZbtF8e32Iwdln6B_ZP1TD3EJ2m15YYC74OVyeyljTrA_Gs7__Elizslagx8tpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیر استارمر: من قصد ندارم کنار بکشم.
🔴
باید به مردمی که به من رای دادند خدمت کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120880" target="_blank">📅 17:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878b8d0511.mp4?token=G3Qhgse0k3VbOCQU3Hn5RI_OqqyQpX9iuQyKXIwjU-7BRu6v7jaJ5HEjrQeK028CNu80_qcEGEWXvJ8oy2mIhph386UQhI8ln1KEl2v2rCHzGhnYw8QHoeT2SZXt_xs_7yeMzqrCchSSfVZXeI40L1YU8SIDHlsZAEfvEF5CV8m-v9seHkc-HOxCKYIvgVDmyq5xFF92OQBIa1RMEHvMTcKRzQVHGcDntpD_wfD6cC7SGCVCxNtUo5vYKiYb7t1tUAoBheShx5yEPa9bPbNTuXlFVCiXnpOKigmzWQE5l_8m5HKi1tTlVQU3_MDx1JLbQ9wsvtWTahFR6zTL_XT9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878b8d0511.mp4?token=G3Qhgse0k3VbOCQU3Hn5RI_OqqyQpX9iuQyKXIwjU-7BRu6v7jaJ5HEjrQeK028CNu80_qcEGEWXvJ8oy2mIhph386UQhI8ln1KEl2v2rCHzGhnYw8QHoeT2SZXt_xs_7yeMzqrCchSSfVZXeI40L1YU8SIDHlsZAEfvEF5CV8m-v9seHkc-HOxCKYIvgVDmyq5xFF92OQBIa1RMEHvMTcKRzQVHGcDntpD_wfD6cC7SGCVCxNtUo5vYKiYb7t1tUAoBheShx5yEPa9bPbNTuXlFVCiXnpOKigmzWQE5l_8m5HKi1tTlVQU3_MDx1JLbQ9wsvtWTahFR6zTL_XT9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چی شد؟
🔴
از ۱۸ ساله تا ۵۰ ساله؟ مگه ۳۰ میلیون جانفدا نداشتید؟ افتادید دنبال ۵۰ ساله ها برای خدمت!
🤔
انگار چه خدماتی قبلا میدادن به مردم که الان میگن اگه به خدمت نیاین همونو نمیدیم بهتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120879" target="_blank">📅 17:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120878">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0TB1VunzlJcTpWuiLdL6iHWgrs4aiQcDq9Iu3tubqRHKMHtuS5M5IZ8X4U6pAVvSB7VAY5uB6xbRVKHaLfQqGstI-zSNYndaY1HCJZLR7iZxBVGMM8hTNrEIKkR7z20xKFFDwMpljKUlXmiUb04Mj1TLl0nssFHYOTIGftrLwVBSFe2MABi-a7-d7QLsnqElrCHFTiXRIUS8M7vjq5uss9EK6FYiYblE27iGZ6QG5uBbHDXy2k8Bglx8gdE7xOnK4FjMiaJfbB2v8S3TAW-dG7R-VFQF0fBW-7fxXO2xfzUxJH_MyK33rZjB06KCNvJBhRRez23jRmwt9W8jOT9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ی ارتش اسرائیل لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120878" target="_blank">📅 17:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120877">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeUZ3kHzlA2o0GHi4RMW2VtJPpDn5YQVAQOrv6ikJZ4FzxP75Ye2D4Hg9WZhvqwikUts3ic5Ch0tKjbRcC13YbD4pdVU4FmBL7dIfQscO3IPbLMT7jkK1pUabarZlif4qLIWDmspF7F5k4Ja-kheG20ffDTx_90vESQgVACVTvofTDWvCvzXQCpmgCVtStPsKejB1YCykxNCtNsEcnntFebpxulf3p5HLx7U1cRneDcctdpZxiuEf0h6BLJKICDHjxZlVKKjW6yvIe49zIE-UUg4CzjT-kMnn3SPBqM3lkGGK3bCrAhynVsLOcv2TKLfy8r8qX05PuoxG5_XbPazTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بلیت بازی‌های ایران در جام‌جهانی ۲۰۲۶ مشخص شد
!
@AloSport</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120877" target="_blank">📅 17:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120876">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QvBURPlWSiXix7I6T7XAB_No-t6mFZjgbHFwb_XdmlIF8UzhJWXjJVNeEsLyUn06iDVl2mq-6xBm2729Bkdwhq8im6a3xzLmNI7uRWxY0wP9eKj9LBeKeojohB5u-C-_iJRnLpmsscSgFBP6LzYUx4SXPRU_9JXHBMx621YjMTum169psiWpxvTMbr7CzIY-7Y8F-P04MgoKj6leo29hGQkcsDcZIqUAuwEVv7O8gf2HoO9uaeR0ROpT3UaWGLfhYDlXH_fxDb8NFhQg3AAYAYFt8G6_aRIdU_QDKu_96SOPyrzNK_FY1qaTOFfBHLryoJmPCLK1ag8hDqki1s0JhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفتکش هَندی‌مَکس با پرچم روسیه که تحت تحریم آمریکا قرار داره، فقط از روی لجبازی مدام وارد محدوده محاصره دریایی آمریکا میشه و دوباره برمیگرده تا محاصره ی دریایی آمریکارو مسخره کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120876" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع ایرانی: پیشنهاد اصلاح‌شده تهران خواستار پایان دائمی جنگ، لغو تحریم‌ها و [لغو محاصره] است
🔴
تهران پرونده هسته‌ای خود را در مراحل بعدی مورد بحث قرار خواهد داد
🔴
تهران از واشنگتن خواستار آزادسازی تمام دارایی‌های مسدودشده است
🔴
واشنگتن تاکنون با آزادسازی تنها ۲۵٪ از دارایی‌های تهران طبق یک جدول زمانی مرحله‌ای موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120875" target="_blank">📅 17:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کاخ سفید: امنیت تیم ملی ایران در جام جهانی را تأمین می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120874" target="_blank">📅 17:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
منبع ایرانی به رویترز: ایالات متحده در مذاکرات جاری، از جمله در مورد بحث هسته‌ای، انعطاف‌پذیری نشان داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120873" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک نفتکش ایرانی تحت تحریم‌های آمریکا که ۲ هفتهٔ پیش در سواحل هند بود حالا در جزیرهٔ خارگ پهلو گرفته است.
🔴
این نفتکش حامل ال‌پی‌جی بدون اینکه شناسایی شود از خط محاصرهٔ آمریکا گذشته و وارد آب‌های ایران شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120872" target="_blank">📅 17:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رئیس‌جمهور کوبا: هر حمله نظامی به کوبا به حمام خون و عواقب غیرقابل پیش‌بینی منجر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120871" target="_blank">📅 17:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سپاه قم: تا ساعت ۱۷:۳۰ امروز عملیات انهدام مهمات جنگ رمضان اجرا می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120870" target="_blank">📅 17:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قائم پناه:هفتاد درصد مردم مخالف محدودیت اینترنت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120869" target="_blank">📅 17:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مدیرعامل آبفای تهران: تابستان امسال جیره‌بندی و قطعی آب نخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120868" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔴
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120867" target="_blank">📅 17:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر صمت: نباید اجازه دهیم کالاهای تولید قدیم را به قیمت جدید بفروشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120866" target="_blank">📅 16:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzQlUb16ENhSGcSEok55JYh3ATaGCZ0BnAlEwTztHloYtLrq-35URsPkwvJ0zaGwif4v98EOLH0LK3vwphNYJkhNWE7B6eHN60vMD6F722uafxxCm-TB4tTX0n_Hq7CEg66kvJN_5Rxlly-DsZg_Mz8-jV6mWY3KI5bfAdm5BmFwTgPIkO_uztk6aQa5MoAi_eMmz_kEAEqQ1daqwsuP21yMaiHEtPvssbyV2dw3bOZbbKW7879vd3jgPch1Jz6bDtja8tYR6EB-eWywVdkgz7zRBUpQKIaF808rJ_S9zuLjMgK_-Eg_UvU7gzPB5VZ_aFxzhxbC3wOb7S3E5HrJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ می‌گوید که «باید بیشتر از ۱۰٪ سهم دولت آمریکا در اینتل را درخواست می‌کرد»، و به مجله Fortune گفته است که ارزش این سرمایه‌گذاری از زمان توافق سال گذشته به شدت افزایش یافته است.
🔴
ترامپ همچنین استدلال کرد که اینتل «باید بزرگ‌ترین شرکت جهان در حال حاضر باشد»، و سیاست‌های تجاری گذشته آمریکا را مقصر دانست که به رقبایی مانند شرکت تولید نیمه‌هادی تایوان اجازه داده‌اند در تولید تراشه تسلط پیدا کنند.
🔴
او افزود که اگر زودتر رئیس‌جمهور شده بود، تعرفه‌هایی برای حمایت از اینتل وضع می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120865" target="_blank">📅 16:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqLXoWtivhjoPKbb_PQDp3sKTWvjRrRO56XXCmo88Bx8LzZ15ARmdwxURy28ctXOEDgvs0Erlh0f7RzBmm1MxIEzEULP5TH8fWrGPjJCzM0_9CRMSGw0q_WZqJUQlyngRz0XN_JQlrgk6x1Y72Y3d3rmEW4rJnBFTW26WA_rUw-jD5syusummXyE3etZNQFSwH_Cp7Mc0nRkg0pE65G-PBm3mpYKv7K5wMUkOXtketd9YFULWKvQChH0NW-4uKsZu16LFITXVwzoQ7ArjZzNBQG6d_zN069O15aEriaf3ywtBdqvSOZdWcsxQPXy3eX5umsTcJcg-CAml29a-vNnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw4TcKeDw62Mm-gW-ed8jz9Mp8xqq6Q7MlUnB3zuS7mzPNliw_-NkPf3aSHfhKThlApCiuaV_DgbxYTubacvO9A3rXI3FvqsjJmESw3w27i7R3aEnvmbNDhJXaPHh_7SlNUsy1-r_Gjq6_khD32GBePqI8SGtFR5-MsRc7uMHDp93B099I5sM2oI5medaWP_OQxQ7w5oB_audfSc0z75cT2is_zHC-LDhsb0m3WE5PeGl-WYOUF470s4SlCVllYu8bgP3TLExvsB4l6XzBKiHV3y9mj5FrIlfezpCSi_tHjfxcdfjEsDx1s-CsL0jjbaSRjuUBgiCmpy-lcn6Z0foA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92f75a629.mp4?token=pBlyAKpezDcrv8G7LL0MrYWDSy6KfTbHTP-lidHefH3R5QXIVHSGG0iIDcEAHmgAJ4QdhwW8yvfB8WkJCialjlpkib_Q5okSmbYSXwK43AgHzCM2IWBgoq4ZO2wlX_nQZbLxg-7WykJLdzLMYuVVPgODgdzUFT-gePtyBlJLZUlCgsFBiHypSDAdBMY_MFflQYe9VcQ16Cyp5B4wOmy0cxELxkubobaLHcoQsgbgzjVMCQ8gtx_WZpC-UUy0VdWYSnq6FVeG_JdqHODhXhtaECCo5270GBt96voHriesLx2wtEa15dicgBngUTgwjkDUsAECTWdGIvcaFuyo1iGPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92f75a629.mp4?token=pBlyAKpezDcrv8G7LL0MrYWDSy6KfTbHTP-lidHefH3R5QXIVHSGG0iIDcEAHmgAJ4QdhwW8yvfB8WkJCialjlpkib_Q5okSmbYSXwK43AgHzCM2IWBgoq4ZO2wlX_nQZbLxg-7WykJLdzLMYuVVPgODgdzUFT-gePtyBlJLZUlCgsFBiHypSDAdBMY_MFflQYe9VcQ16Cyp5B4wOmy0cxELxkubobaLHcoQsgbgzjVMCQ8gtx_WZpC-UUy0VdWYSnq6FVeG_JdqHODhXhtaECCo5270GBt96voHriesLx2wtEa15dicgBngUTgwjkDUsAECTWdGIvcaFuyo1iGPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به حروف، شوکین و کفر رمان در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120862" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه جمهوری اسلامی ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120861" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
👈
معاون سازمان بورس: بازار بورس فردا و پس‌فردا تا ساعت ۱۳:۳۰ فعال خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120860" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: به مذاکرات ایران و آمریکا خوشبین هستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120859" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کرملین : روسیه و چین قصد دارن حدود ۴۰ سند امضا کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120858" target="_blank">📅 16:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
غریب‌آبادی: هرگونه توافق احتمالی، باید جنگ در همه جبهه‌ها از جمله لبنان خاتمه یابد، نیروهای آمریکایی از منطقه پیرامونی ایران خارج شوند، محاصره دریایی برداشته شده و تحریم‌ها لغو و دارایی‌های ایران آزاد شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120857" target="_blank">📅 16:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmimWGMnjiJmLZUFG4BX4pn0W3ApqHDjfnh04XWUc8rSxIoWLhaXeCYrBuUpzGsk5Hvd3zrhSKwEiqXKTFUj33k9huns3h-Y0iWPqlllzwz-hc9w2i2cH3eQg_uF7WaPKEIscbSa-eZGRVFtjjcGCKkehFKjvCCYZfbnwXo9c8RMopbnU92exbj66Rp7Li0wYkoLGQi4w2OOBOq4ENqoiEjmzsblKrXLLfbQ1wFcpsIEHA6GVibd-S-o-RyTt1jKwN7x8IHJuffOKQJ4xFjcParqAdVVr6YeEnMBIbfBs8jMVwqvdbIkCL97a0mzFPIxYEITfziLWIdWhaLZKf7fgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120856" target="_blank">📅 16:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نایب رئیس کمیسیون انرژی مجلس: افزایش قیمت سوخت در دستور کار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120855" target="_blank">📅 16:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نخست‌ وزیر پاکستان: به مذاکرات ایران و آمریکا خوشبین هستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120854" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFGvsPGUyMMgJTkhVxgbazCk-LfxV5qGAxKTPxvh9WViCUNYLLyNLv1qrQqHjp5-IZLwCCAalEtGQtmTEkNiOS5eeOOsyZEbum7zYCnxgGO6saflQ4GpmPo6QGjcdKu66f1uwklZhxKpaTU_SqxqFM-Ak5ZQXZFk4lyRwY0OVgIpzur1bNB6k6myzQp-OCVeRMxNUm4cemn40IQeH1pwDEGN4huOgwy6iZm4nvAbu4xrW-3mmaT9uU03_0D6BhplTsHjPC1IxoYkrkaVBY7-lqmLFJ_RdCtRAsbzHi2ip6XbFJ6Zrli8yC_bXABQRwrwcheZDt2CC_-8L3ebnATJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی مدعی شد که پاکستان در طول جنگ ایران، ۸۰۰۰ نیرو، جت جنگنده، پهپاد و سامانه‌های پدافند هوایی را در عربستان سعودی مستقر کرده است. این نیرو شامل جت‌های JF-17، سامانه‌های HQ-9 چینی و تجهیزات تحت مدیریت پاکستان با تأمین مالی ریاض است. این ظرفیت اعزامی از پاکستان، آماده نبرد است و در صورت نیاز می‌تواند به ۸۰۰۰۰ نیرو افزایش یابد.
🔴
عربستان و پاکستان سال گذشته پیمان دفاعی مشترک امضا کردند. وزیر پاکستان بعد از آن اعلام کرد که «عربستان سعودی تحت چتر هسته‌ای پاکستان محافظت می‌شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120853" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
تیم اقتصادی ترامپ از اول جنگ، 3600 معامله روی سهام انجام دادن. %80 رشد نسبت به قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120852" target="_blank">📅 16:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8779033c.mp4?token=XBhYMGpZ9Xp-Nfwx4NJ5gCX7yikZBKUi31Sbvoza1GPumqXDTsve7AX4X1mnSwacQhdKSO05tJQFf29ZJbZKa5eLl76R3Nl46Rzg_q26cYpaW7MV5oUXuoyvMQs79HIhg90tNH2T1GRjEF7T8j_ojjhMQTcSVNKHwOBKPN2BS9f5K6KeeNM1uTAHT5iU-N9L-WN-w76LmvgicuXYPeptC2MupdSx_xNRK89Gq822mnX13p7lkJkymiuVYlOGOb-9IMgwzF05l6x1Gf-vaz9lvrjqlHZjtXF_Am7jvPrD5TM0tBZwiq4HG-gkEftL36q8GsME1CaJ65ZnAM-kAt-HtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8779033c.mp4?token=XBhYMGpZ9Xp-Nfwx4NJ5gCX7yikZBKUi31Sbvoza1GPumqXDTsve7AX4X1mnSwacQhdKSO05tJQFf29ZJbZKa5eLl76R3Nl46Rzg_q26cYpaW7MV5oUXuoyvMQs79HIhg90tNH2T1GRjEF7T8j_ojjhMQTcSVNKHwOBKPN2BS9f5K6KeeNM1uTAHT5iU-N9L-WN-w76LmvgicuXYPeptC2MupdSx_xNRK89Gq822mnX13p7lkJkymiuVYlOGOb-9IMgwzF05l6x1Gf-vaz9lvrjqlHZjtXF_Am7jvPrD5TM0tBZwiq4HG-gkEftL36q8GsME1CaJ65ZnAM-kAt-HtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل، یه منطقه از جنوب لبنان رو با خاک یکسان کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120850" target="_blank">📅 16:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/نیویورک تایمز:
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای ازسرگیری جنگ با ایران در همین هفته هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120849" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f8825d8.mp4?token=Zj-JYJuDVP1PxtEqJKEjZF_n8oxPqrckLAXC5KZEx35V2sEmmLPysqVCUBivcg6Lk-O82syZ5e1lOwPlNCXyWQV28vJTS2d4pIikyTg0O-sSmRz8kZy90K1GbQGqdCAEUW9t4AHxmAOBXgsbl7n4_tCOVPsUd6EGmkZWjycwr0c0GqWt10f1C2r_1AMbfpqzY7fe7NVHQruYlN-702jWuWbSfTbv3BcPvrZaSn-HkHPj3h5dfz0VBVd4STTSVNX0d3IsO1p-TOCOWYzcUUUBKE5T1Wc2AqElos9Guta4riYQORdqShfpjYh8co4HaafAJ6Ira0dIP9QriNZqVJo3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f8825d8.mp4?token=Zj-JYJuDVP1PxtEqJKEjZF_n8oxPqrckLAXC5KZEx35V2sEmmLPysqVCUBivcg6Lk-O82syZ5e1lOwPlNCXyWQV28vJTS2d4pIikyTg0O-sSmRz8kZy90K1GbQGqdCAEUW9t4AHxmAOBXgsbl7n4_tCOVPsUd6EGmkZWjycwr0c0GqWt10f1C2r_1AMbfpqzY7fe7NVHQruYlN-702jWuWbSfTbv3BcPvrZaSn-HkHPj3h5dfz0VBVd4STTSVNX0d3IsO1p-TOCOWYzcUUUBKE5T1Wc2AqElos9Guta4riYQORdqShfpjYh8co4HaafAJ6Ira0dIP9QriNZqVJo3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی آفریقای ایالات متحده، با هماهنگی دولت نیجریه، به حملات علیه تروریست‌های داعش در شمال شرقی نیجریه ادامه می‌دهد.
🔴
فیلمی از حمله هوایی به گروهی از تروریست‌ها دیروز نشان داده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120848" target="_blank">📅 16:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPVx75xj9_NeS7RcG2WYoSM4UiVbAMObb-3bB5tK-F_UQ9gKBAXhLVdQOGaHbAsLJB_6Q-wAUqj-2kFjiCXDcGMaan8rh9zOBl0T0prtBPvb4fP9qtdjH57E6AQZdlGuGEIcN1PhVbdsKi2yAVtsWZt2jXnvEaAmJ5h4R1f2BhqDJa1R5Nnp9ajKeSTWN2hqGtNYSWFemsf_wqfrvr3fpBu01HJ9crseRGXf6F9W6pM3E-VF8dk9iFMCLZYzW8OeHjYvhXZvVgD7Hj_3V7w8j0_3tNu6o_zvBKF-zG1fN-b1GtCqoodJukn9NQCtIWqNz_ZCieRli-UrhuGu2kXKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
ربات رسمی دریافت کانفیگ رایگان فلش‌نت راه‌اندازی شد!
از این پس می‌توانید با دعوت دوستان خود به ربات،
🎉
کانفیگ اختصاصی و رایگان دریافت کنید.
✅
بدون ضریب
✅
کاملاً اختصاصی
✅
فعال‌سازی سریع
🤖
آیدی ربات:
https://t.me/Flashnetgiftbot?start=5011918694
📌
همین حالا دوستان خود را دعوت کنید و جایزه بگیرید!
🙏
تیم فلش نت</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120847" target="_blank">📅 15:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvjUkaS3lMEbR3YjSM-7VrfxK1AG8g4yN75J9WyU2tY8oNoehKCsbvIqlguFb_JSlNR1nUI4eJXP8djC1cZDCsL87TgYNJbRcTrMjT-NQfHmGln0RyWnnQj5fJrZM_msAw_ghv75aMwz3Vd-G-Xq-lxV4GeMwTadsMoyA7ClsogenUq7iQ5AV18emlfubREwEWziO0-DrR18iFntL5v81dgM9gMq4ouBMvz97nxUf4FVUXvdtXF4HfMwoM4YpPTo7yZdOCE5ziUAJfX2YWivHBBIYyhINHcCsidSN_yP4Vb4cdUdKqXLFnKrM1881QOpdWY8Xf1JNKOkzKrC9ij8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال بررسی برنامه‌هایی برای نصب یک هلی‌پد در کاخ سفید است تا از آسیب دیدن چمن جنوبی توسط هلیکوپترهای جدید VH-92A پاتریوت که برای پروازهای مارین وان استفاده می‌شوند، جلوگیری شود، گزارش وال استریت ژورنال.
🔴
هلیکوپترهای قدرتمندتر VH-92A دود و هوایی تولید می‌کنند که به اندازه‌ای قوی است که می‌تواند بر چمن تأثیر بگذارد، که این موضوع باعث شده تا نصب یک هلی‌پد اختصاصی در نظر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120846" target="_blank">📅 15:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d3e3dc3.mp4?token=YueKI8dpFfNN2f-B20p4uzPQ7K7vqHlAR_n0mWN8CDYuG8n2kAcpheTemSC11DwJI6l_rPF1XWzNXvqafXV9BMvm3NCBHhIr5MXH2PejKF_5ua7AJ_XflKepDPm-quah_-HssmSt2Uu5Fnu1niA88qZ_P0FnYWLJfB9hSUgk6iv0C9Qm0Sk0tGU8PzuyraGuOj3prwXGwIg3YVhIh2YoR8LGDyFvCFfr-3bqfEqbEzfgre89rZKzQyAYcvECGBw11bljtTxZXijK2KKOstjWZbSfneGm4UuaRNqSoPmTiesDwakk-UNtC0yY9CKCsSUIwJuITmQa9jEZ9OEs0fTwJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d3e3dc3.mp4?token=YueKI8dpFfNN2f-B20p4uzPQ7K7vqHlAR_n0mWN8CDYuG8n2kAcpheTemSC11DwJI6l_rPF1XWzNXvqafXV9BMvm3NCBHhIr5MXH2PejKF_5ua7AJ_XflKepDPm-quah_-HssmSt2Uu5Fnu1niA88qZ_P0FnYWLJfB9hSUgk6iv0C9Qm0Sk0tGU8PzuyraGuOj3prwXGwIg3YVhIh2YoR8LGDyFvCFfr-3bqfEqbEzfgre89rZKzQyAYcvECGBw11bljtTxZXijK2KKOstjWZbSfneGm4UuaRNqSoPmTiesDwakk-UNtC0yY9CKCsSUIwJuITmQa9jEZ9OEs0fTwJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی نشان می‌دهد که یک کشتی از ناوگان جهانی صمود به سمت غزه توسط سربازان ارتش اسرائیل تصرف می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120845" target="_blank">📅 15:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: تلاش‌های میانجی‌گرانه برای دستیابی به توافق بین آمریکا و ایران ادامه دارد.
🔴
تمام توان خود را برای تضمین برقراری صلحی پایدار به کار می‌بندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120844" target="_blank">📅 15:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ادعای رویترز به نقل از منابع: پاکستان بر اساس توافقنامه دفاع مشترک، ناوگانی از جت‌های جنگنده، هشت هزار سرباز و سامانه دفاع هوایی در عربستان سعودی مستقر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120843" target="_blank">📅 15:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCK16HZ0erREkG0CcaCjtrKGj5-ZTs-hwdxil8CcdWeXaBUY56HnKD0W9f8rwoncBs53LZHVLEBANopd84V7EyHyCyYwYFHIbhilHw-9fk5QbxBj0hBRd2WUa58MYz2ZF0DdnB9wnec4mNv_F0XWRchUXaaz3o602FZmpoiurCGokZf4Tt-h0Y0oyrscM4I6_wtUPSuFS6JZk6GNI7Mv4pxzQxMgkWzBBWVZhr72a5r3hvhgO04vkQ7SqnjQ4oTWCzu_rEps2atvCEKY23AClJ2sYhMODGYSXjxUUApBjfB_moTFtFHv0PrasnDfgXhDdvmGPWt2NoPhaue2JGaVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل تأیید می‌کند که فرمانده ارشد جهاد اسلامی فلسطین، وائل محمود عبدالحلیم، در حمله هوایی اسرائیل به دره بقاع شرقی لبنان در طول شب کشته شده است.
🔴
ارتش اسرائیل می‌گوید او به عنوان فرمانده گروه در منطقه بقاع خدمت می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120842" target="_blank">📅 15:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کوثری عضو کمیسیون امنیت ملی و سیاست خارجی مجلس: قطعا و یقینا از طریق مذاکره به نتیجه نمی‌رسیم
🔴
ترامپ جنگ را باخته و می‌خواهد یک جوری خودش را برنده نشان بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120841" target="_blank">📅 15:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23f6a8852.mp4?token=G2rEd9uB_3GVsb-kU2XfuqfYEa8fr-CSVfzbGRBfqetPutw3UG85jFso5Gk9ujnYyRt4iB1WeLZO-Qld0aAo2LZRPnMfO1GyCoCCnsXpzO4gY0W3h2rR32otbCZQsc5mc573RNTmKnHt24jueGqpD5-T4I0I0AwYPnrKOPWZ1pN1aq_bxKjb10_OOIFquwiSUzyX4hvnvyczYJF-q9lXgdCC5qQWTUb2DdVjUZbWY2O9yVlHFYwBenu7RaU_tiv_RtwXrCVUQHsGuNfPzv9mdHzbJjlE_-4yKQuUe9RakhTrh4vyBYQWBO2TvyUWHILgWqLYoLgTZ1scwYNPiFyeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23f6a8852.mp4?token=G2rEd9uB_3GVsb-kU2XfuqfYEa8fr-CSVfzbGRBfqetPutw3UG85jFso5Gk9ujnYyRt4iB1WeLZO-Qld0aAo2LZRPnMfO1GyCoCCnsXpzO4gY0W3h2rR32otbCZQsc5mc573RNTmKnHt24jueGqpD5-T4I0I0AwYPnrKOPWZ1pN1aq_bxKjb10_OOIFquwiSUzyX4hvnvyczYJF-q9lXgdCC5qQWTUb2DdVjUZbWY2O9yVlHFYwBenu7RaU_tiv_RtwXrCVUQHsGuNfPzv9mdHzbJjlE_-4yKQuUe9RakhTrh4vyBYQWBO2TvyUWHILgWqLYoLgTZ1scwYNPiFyeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایی از تنگه هرمز از داخل یک هواپیمای مسافربری و کشتی های خاموش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120840" target="_blank">📅 15:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آمریکا در متن جدید خود اسقاط تحریم‌های نفتی ایران را پذیرفته است
🔴
تسنیم نوشت: یک منبع نزدیک به تیم مذاکره‌کننده گفت که آمریکایی‌ها برخلاف متون پیشین خود، در متن جدید پذیرفته‌اند که در طول دوره مذاکره، تحریم‌های نفتی ایران را Wave کنند.
🔴
ویو کردن تحریم‌ها به معنای اسقاط موقت تحریم‌هاست
🔴
ایران تاکید دارد که لغو همه‌ی تحریم‌های ایران باید جزو تعهدات آمریکا باشد. آمریکا اما اسقاطی اوفک را تا زمان تفاهم نهایی مطرح کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120839" target="_blank">📅 15:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLzEDCncO0MlrrD8rwGQd4jhLw_7WN-syvUXLHH1iVyFpG2KYuTtjIHdKGRkzTPHc_RGChE2HcumpiqV4Tajbzjk8K5dj99lDV0dJxnRi13jr_tk4sSF1GBqZg4SjTKpcn4QuvT7YEadkk5YNDX0JWzF6Db1hwiFC-tfVZp7etZwxzI3FaDbvnQ2Ot0bVGKhP6aPOXFuxSxqi4sKWopmj7aaaVehiiNjU1TVgctEqfZKz0dEYKJVGoD0N5VrCRsnOv4DkO45cihvYy8ZSlnRYk7SGsMkyhE5N_u106lqFyO8XAByeJHTxSeScQUuum-iXx6BbZu_CSZkdjD1eWvgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در شبکه ایکس یک حساب کاربری جدید به اسم  « مدیریت بر تنگه خلیج فارس» ساخته شد
🔴
امروز  جمهوری اسلامی از ایجاد نهادی مسئول بر مدیریت تنگه هرمز خبر داده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120838" target="_blank">📅 15:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیویورک‌تایمز: امارات بیش از ۶ میلیون دلار به شرکت مدیریت شهرت «تراکیت» پرداخت کرده تا نتایج جستجوی گوگل را دستکاری کند و گزارش‌های انتقادی درباره «یوسف العتیبه»، سفیر امارات در آمریکا را سرکوب کند
🔴
این گزارش‌ها اتهاماتی درباره ارتباط «العتیبه» با قاچاق جنسی را بررسی می‌کرد
🔴
شرکت «تراکیت» اقدام به ایجاد پروفایل‌های مثبت و ویرایش ویکی پدیا با حساب‌های ناشناس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120837" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای رویترز به نقل از منابع: پاکستان بر اساس توافقنامه دفاع مشترک، ناوگانی از جت‌های جنگنده، هشت هزار سرباز و سامانه دفاع هوایی در عربستان سعودی مستقر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120836" target="_blank">📅 14:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
لاوروف: پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120835" target="_blank">📅 14:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
معاون وزیر ارتباطات: باید دسترسی امن مردم به اینترنت پایدار را به رسمیت بشناسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120834" target="_blank">📅 14:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حزب الله: ما یک سکوی گنبد آهنین متعلق به ارتش اسرائیل در اردوگاه جنگل های جلیل را با یک پهپاد هدف قرار دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120833" target="_blank">📅 14:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7EgncOUDPwvwY_dwqQoAu96begZVGrvu83ch9eApgmtVa4hYEloLQujfZr8oEF40_7ffsNMT-YaNO6sD-92ZBFKORlkQNldB5akREWn7UbUq9Gm4x65vj-l6Wfuh3CWtWYXuXz6ZVYimu6ShuRg-BvMb7YMBUNFOyjCAkvmCuyHsFtRHIkDd8URgsJK9Tj9Mcmziz06xv7tw-E5sNp18wCywQwgD0pdRDLIZAHoLYYii2V_-2w_EUS-bKOtJ8a7-JGw2Xw4CkK4_NNgGzVUCUARZswSBdDUB5N0IXBxyIyKKufAzfuxMIj-G8YNIPE2YWZtcrihkLhZvv272H076g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqVWr7OjnjAg6q8uLrAZD9RcGds8uYejNiYX1jXiU5s9Ne1p4zCaZRz44s54un4mM30t1HE9Ww7ML_U2IXM7z-b5xKLJdx1Y0AxiDCCCdWpkM9ud3g_gnKsDw3_LaGZG7GvkXnB-pKTNlwT4PYnTc-kTSA4BiR2AB3TrabX3K8BOqcQq8zp7Sq_vClJNkB4njWyl9aM-hU6dR7Kf8eaPBsJW7mPh0HXaHuJqNHBGAaYVY_AzkYTzgGBCA9ANnbBjoSHx94gNXrSCncECQ9ymGyAK10FxGbpjED__nMAug6x0dldjaPsIJ9fxQOWsz4ELX2AaZuWoHiHBLQ40Q0iKkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120831" target="_blank">📅 14:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120830">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رسانه‌های عربی از حملات هوایی اسرائیل به مناطق مختلف جنوب لبنان خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120830" target="_blank">📅 14:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اتحادیه اروپا ضمن حذف وزارت‌خانه‌های کشور و دفاع سوریه از فهرست تحریم‌های خود، تحریم‌ها علیه مقامات حکومت بشار اسد را تمدید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120829" target="_blank">📅 14:19 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
