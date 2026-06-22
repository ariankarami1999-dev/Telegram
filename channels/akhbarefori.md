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
<img src="https://cdn4.telesco.pe/file/jEVfE9TVkbI1P9uPkkDDb1LS0R0JVmcuABZnqPSmMbGaGrPZDYWye6DlkKmSAvTTonTPUTiHyjd2QnyR6y7ilTC_OZt8TFRPTKzOk6f0a3Kpk6hn4R5YYkaLA2z10YUq34Fdht9M01ByMduqwVtWacInfYt0h3OK7oCCZ24yc3X8Iaaik1K5oho41tN9Mxaoe32JAP6jjsiVYbVFmt-pZfHdpEwQ5eXbgJRmUYuP8j7pV899kHn4QBDvj1o7qqeOYvk_QuZxQAZ9opAvCfcclKoW5Yq5U9mrbmsKmrMeAfCzo6T7nyvLCpvdjYd0-K8Lp5hiZR0ED1RTUrgL7gEwxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 00:48:02</div>
<hr>

<div class="tg-post" id="msg-662469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7607a8c682.mp4?token=uOFbgbm9yCp5rNucYKPPvak6-6XUoYvDZhWMAYk2-86yIOAJ7QnR3BurpXDeYEKNS8gCCK5lv5MUpm5WSjPWy4i0z5Coy1HuEbmipDvOu6WLMt0PQ51ZBlcYk9zkvnl8-FfED1bTEA4CYEPM9NmPPRW4KVbD_RAJJRLh3V9MIjtiOaaXTVR9E3auZfl5R9uDsIKmwr4ACABGZVwvlCu5BZI1V9pPUd9-Uhqj5J2ydLTASHxWorchxU0D2jPfk9w-C5xCcg3Lu-n26IO7ya7hGAD9k7MGz8we9ZNTsokkEcOYKoY062dCH0SLyMuz5M1Z7WDlMNT2BdyYaRHAqG0aMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7607a8c682.mp4?token=uOFbgbm9yCp5rNucYKPPvak6-6XUoYvDZhWMAYk2-86yIOAJ7QnR3BurpXDeYEKNS8gCCK5lv5MUpm5WSjPWy4i0z5Coy1HuEbmipDvOu6WLMt0PQ51ZBlcYk9zkvnl8-FfED1bTEA4CYEPM9NmPPRW4KVbD_RAJJRLh3V9MIjtiOaaXTVR9E3auZfl5R9uDsIKmwr4ACABGZVwvlCu5BZI1V9pPUd9-Uhqj5J2ydLTASHxWorchxU0D2jPfk9w-C5xCcg3Lu-n26IO7ya7hGAD9k7MGz8we9ZNTsokkEcOYKoY062dCH0SLyMuz5M1Z7WDlMNT2BdyYaRHAqG0aMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به عراق رو موشک کیلیان امباپه
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/662469" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZKZ1aClO-IzhsWoUd5eCvt97y2lKyFDNPQkDdaiBtBqXoqNxsf2J4PQN4Q_77tkK1aAzYsl5pF5VHQauww3zvTDt66-ruv4t99xtr2R0SLvXST6xLMDHHaS5ecT-68Nw3vqiTkCMpGtg-RZVeNzk8n-NkFW6wjQOKLnIWubyeXh6PqQhMJeQ2OxgBl_O82NNxW7bEnzNUSbAmrgMP-oYLIbWwg0Xy4qmy12LdbdJwbfdSRLFrRBgNLNBwM9pzdyShk8xsE1aRLqSzlxFSbDium5S9JPQq3IKP6BdSo6fh3Ub3HduDqQM2fwmJWCPEFhekV6wGVRxPR2AISDLJtuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف، رئیس هیأت مذاکره‌کننده ایران: دیدم در [یک] برنامه [صداوسیما] اعلام شد که کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، مسلمانان و شیعیان لبنان کشته می‌شدن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/662468" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عبدالناصر همتی، رئیس کل بانک مرکزی: ما سالانه نیاز به خرید میلیاردها دلار کالای اساسی و دارو داریم و برای ما فرقی نمی‌کند پول خرید کالاهای اساسی را از چه منبعی پرداخت کنیم
🔹
اگر از منابع مسدودی بانک مرکزی بتوانیم این خریدها را انجام بدهیم، درعوض درامدهای…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/662467" target="_blank">📅 00:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7147ed8acd.mp4?token=BLuF-YbfmcdvRgvnU2RAjWrVr5Bc2HZZSZUc49SEuZDv2cZPh8P1tdPWv-kHGZ2sjVJxA-Au0PD1YJXEs5cGRW12DdjfIpLr1CGgBq61aMLQfmF5cYGe6gTyitBmdsgMRCRvODBijPBeMt3cLYzXG8iYKlUjf3Z20OWZC_P2X2izfqExN2ukUftynQfirGS83Iqd8XBKtIozOUtvqKQkTZiiShEiJ3moHc2PWr55b5SW0LbM7t5JvyXU85IUcenKAL3cdFQddN7KKhoXGvRICV3XC9wd4_paViLkGC0qWxfM20b4-KreQxt1ZsidS9YELr6txCD6xRiYAIecUAvyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7147ed8acd.mp4?token=BLuF-YbfmcdvRgvnU2RAjWrVr5Bc2HZZSZUc49SEuZDv2cZPh8P1tdPWv-kHGZ2sjVJxA-Au0PD1YJXEs5cGRW12DdjfIpLr1CGgBq61aMLQfmF5cYGe6gTyitBmdsgMRCRvODBijPBeMt3cLYzXG8iYKlUjf3Z20OWZC_P2X2izfqExN2ukUftynQfirGS83Iqd8XBKtIozOUtvqKQkTZiiShEiJ3moHc2PWr55b5SW0LbM7t5JvyXU85IUcenKAL3cdFQddN7KKhoXGvRICV3XC9wd4_paViLkGC0qWxfM20b4-KreQxt1ZsidS9YELr6txCD6xRiYAIecUAvyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: در لایه سوم مسئولین ایران؛ هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/662466" target="_blank">📅 00:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
همتی: اگر نرخ و کیفیت نهاده‌های آمریکایی در مقایسه با سایر کشورها مناسب‌تر باشد، مانعی برای خرید از آن کشور نداریم
🔹
اصولاً طی سال‌های اخیر خریدهای جهاد کشاورزی از طریق شرکت‌های بزرگ آمریکایی و اروپایی بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/662465" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46d577bcb.mp4?token=tqB_wXpxHEtle4WAaPdta8GZfbi9x11ZDj525WyTyNWC-eidKk-aYsydA3es2Nl3QfXgoqAqtFoKy4RIFL-Uw9jiMPxbb2BBE0FNfSHGi1c5RPr16rIxM_hWxRK6U9h7v1tNE3nEVRcfTn1oioFfw7iU_nQO5gVbmMkYguIs-cp37GDOgoW9YeRAyPcQIEcbBRENhbJ9bYywqvRzY6INOF7c3MdQkwzk0Cu0Ahgsoq1lzbF0hwjaoO-RHqMCqDM4AR3EOoSiNSrpmQKFjk0sXV5IaX4wsk19hcBb7wXXptFAcBWGdy9cYYyZ-eNJvJoidXCp-td0_UhWwS-GlVktXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46d577bcb.mp4?token=tqB_wXpxHEtle4WAaPdta8GZfbi9x11ZDj525WyTyNWC-eidKk-aYsydA3es2Nl3QfXgoqAqtFoKy4RIFL-Uw9jiMPxbb2BBE0FNfSHGi1c5RPr16rIxM_hWxRK6U9h7v1tNE3nEVRcfTn1oioFfw7iU_nQO5gVbmMkYguIs-cp37GDOgoW9YeRAyPcQIEcbBRENhbJ9bYywqvRzY6INOF7c3MdQkwzk0Cu0Ahgsoq1lzbF0hwjaoO-RHqMCqDM4AR3EOoSiNSrpmQKFjk0sXV5IaX4wsk19hcBb7wXXptFAcBWGdy9cYYyZ-eNJvJoidXCp-td0_UhWwS-GlVktXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: در لایه سوم مسئولین ایران؛ هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662464" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c7a1ff2a.mp4?token=avalT9vbXhsoASI-xGxXb1_R_dqNVnQ8zaGhckPvjlt8IHehauGAeVWObJofFhRHGgoksV0aTZQVuLBRfXv2eedDOIANq-QK5Y3o7LrS5-8F9iv4DDqX8SzsCHVj0Pi22mEf9DIUMbJR51y1iQFG2sSBG8oYPZFMXeVz7lM0kXYC6C2fioq08dfjBYSivgaSTJgKsnRtjcpDZQ5SO29sahqpC1wDGAyBssZG3RFt5GcUD6pQQHaDa5ux0ITUderj4JpZVXjcVwduboI5g_LFsDQrgRRWSHlQH1di_yhcBtc2DwqlZyelsd4bWNbieDv-2eN-QSoX31CKG0J850ZreHy2iyspO2kpE3q5WUg7PU5SUKG1Eba10PL1dJqKcafKxUN6Zwso_qJR-4NPXAyOvgY-AC32QGKeWPUun_VrFkBlFPvAF5ye12RhBCBM0oyEVkWVzq4iVlLaIZYCntCyI4p51mKNXj_eFi8VgHSuEsJnQ3irrT5C9KALOhF6fCmJsWD7eHfWeHhAllViGaURsMyAm-plWNjPPxFPQiaUTqClFh328bgGyIh1jkFm6hpkdn-pGM0zRpJ2WjPScBnOHAABZ7JjCKbUSdbFydujnIvTY9S07o4SjArWCUYH0ARO-Eg2mpVXYEQbd_tbdgz8-Rhetx5AYOAIZOP3HYnfMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c7a1ff2a.mp4?token=avalT9vbXhsoASI-xGxXb1_R_dqNVnQ8zaGhckPvjlt8IHehauGAeVWObJofFhRHGgoksV0aTZQVuLBRfXv2eedDOIANq-QK5Y3o7LrS5-8F9iv4DDqX8SzsCHVj0Pi22mEf9DIUMbJR51y1iQFG2sSBG8oYPZFMXeVz7lM0kXYC6C2fioq08dfjBYSivgaSTJgKsnRtjcpDZQ5SO29sahqpC1wDGAyBssZG3RFt5GcUD6pQQHaDa5ux0ITUderj4JpZVXjcVwduboI5g_LFsDQrgRRWSHlQH1di_yhcBtc2DwqlZyelsd4bWNbieDv-2eN-QSoX31CKG0J850ZreHy2iyspO2kpE3q5WUg7PU5SUKG1Eba10PL1dJqKcafKxUN6Zwso_qJR-4NPXAyOvgY-AC32QGKeWPUun_VrFkBlFPvAF5ye12RhBCBM0oyEVkWVzq4iVlLaIZYCntCyI4p51mKNXj_eFi8VgHSuEsJnQ3irrT5C9KALOhF6fCmJsWD7eHfWeHhAllViGaURsMyAm-plWNjPPxFPQiaUTqClFh328bgGyIh1jkFm6hpkdn-pGM0zRpJ2WjPScBnOHAABZ7JjCKbUSdbFydujnIvTY9S07o4SjArWCUYH0ARO-Eg2mpVXYEQbd_tbdgz8-Rhetx5AYOAIZOP3HYnfMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل بدون آمریکا هیچ است و ایران قادر است آن را بکوبد
لری جانسون، تحلیلگر سیاسی و افسر سابق سازمان (CIA):
🔹
مسئولیت حفظ تمامیت ارضی لبنان بر عهده ایران و آمریکا دانسته شده و در مقابل، اسرائیل به‌عنوان ناقض این تمامیت ارضی معرفی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662463" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
همتی رئیس کل بانک مرکزی: هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/662460" target="_blank">📅 00:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxOLoajVv1mJl_CqTz6dWZtFWrovjuz9FeJ-qmt1cxW-8zfS5SGS0Xr6vjLGXCbL172yrpyPWivECNh6GTM3YdVQLTkxIy3pYj9LlAne2urNbW6djLtLBT8S5BAtvTVcvLxY_gyKQzBBLck5iMYeauc5s_eyF1FZkJ_piW_nj3kko26I3ffFrXr2m5h8G1rGCiXDEaXBuCvh90ocW_WU3ib8V9K3gwzKEgdyF6UNnBKl806bdM5asmT-pRsFZ4-kYZkirZb-efc8kr9JtWoP9mq_bXIUynN9pN8GqHnbHwqiaQnYG9fYjXlBW8u-BX_F6DTHwFeqfT1JKLM_lcwBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند: موقع گرفتن موقعیت گل بلژیک انگار یک انرژی عجیبی پشت دستم بود
🔹
من آن لحظه نه دست خودم را می‌دیدم نه توپ را؛ فقط دست خودم را انداختم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662459" target="_blank">📅 00:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
همتی رئیس کل بانک مرکزی: هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/662458" target="_blank">📅 00:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e168bac7.mp4?token=bm6GBYdO9EXDvBnKfLm9cgVRXxbaLMab1ROkI4-heGNUAJl7f3mNJVusLGR2FEENl9OQLg5bGMOGQ61HvR0NUuyzVa_-ONsUxWvuZeu9tZ4wOK0YqYbsLfaQXy-TtlZt4E8HEWldBjJrPOG7Th3ipvlTK1H_M3rQsVeDf3qu7caUIxViSMGKxIwwH8PqbXHUOmutliMT9fDD5Lv2u13HZ6w-tB-hRUdo4z9MgHpKkZMr-9RJZ6Cf1Axha5tlnzoyVttOzC2ex-jT1PaZ2fR-JUod2oM6ll2O58Terhc6cY1syM6snDs1GraV4lKmbm4FZnaaacrNKcf8g5jupMZGrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e168bac7.mp4?token=bm6GBYdO9EXDvBnKfLm9cgVRXxbaLMab1ROkI4-heGNUAJl7f3mNJVusLGR2FEENl9OQLg5bGMOGQ61HvR0NUuyzVa_-ONsUxWvuZeu9tZ4wOK0YqYbsLfaQXy-TtlZt4E8HEWldBjJrPOG7Th3ipvlTK1H_M3rQsVeDf3qu7caUIxViSMGKxIwwH8PqbXHUOmutliMT9fDD5Lv2u13HZ6w-tB-hRUdo4z9MgHpKkZMr-9RJZ6Cf1Axha5tlnzoyVttOzC2ex-jT1PaZ2fR-JUod2oM6ll2O58Terhc6cY1syM6snDs1GraV4lKmbm4FZnaaacrNKcf8g5jupMZGrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دوباره ترامپ به اعضای ناتو: ما دیگر در ناتو هزینه نخواهیم کرد / استارمر گفت اگر پیروز بشوید به کمک شما می آییم، هیچ یک از اعضای اروپا به کمک ما در جنگ ایران نیامدند! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/662457" target="_blank">📅 00:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نقض چندباره با حمله رژيم صهیونیستی به خان یونس و جبالیا در جنوب و شمال غزه
🔹
منابع محلی فلسطینی از حمله هوایی صهیونیستی به محله الامل در شهر خان یونس واقع در جنوب نوار غزه  خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/662456" target="_blank">📅 00:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff99eb275.mp4?token=SDiwSpxygg82w5YTMudvYhUCBW2OLqVrv95AySjDDiLf36x4Ormt_C5ePdmOP--wsICBVaNfP3oCHOBydGXD4gVPG4Sv7nnmN3rJJzMpFI_2j0Rs5eTSTrzpUMuU9iMTdK8HxAV4PEm5sFVor-Ga1F4bEq2bBHn61Yjv3_w97P_YglK_AraMBx9SOl3miRV4RQvViZW62f5StGcbhs6TdVMhPCvGaFxsGkX8et3Zmb1VoLEeMycdh5rVz09q8drpXy0cSYgjqEaFfVhoLDJdr72y4GL3vVL5oWLPKB2gRbwLZQ2IlolPtV2UND7ZP14cRuasC1SJ4Qw4P9G3AatZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff99eb275.mp4?token=SDiwSpxygg82w5YTMudvYhUCBW2OLqVrv95AySjDDiLf36x4Ormt_C5ePdmOP--wsICBVaNfP3oCHOBydGXD4gVPG4Sv7nnmN3rJJzMpFI_2j0Rs5eTSTrzpUMuU9iMTdK8HxAV4PEm5sFVor-Ga1F4bEq2bBHn61Yjv3_w97P_YglK_AraMBx9SOl3miRV4RQvViZW62f5StGcbhs6TdVMhPCvGaFxsGkX8et3Zmb1VoLEeMycdh5rVz09q8drpXy0cSYgjqEaFfVhoLDJdr72y4GL3vVL5oWLPKB2gRbwLZQ2IlolPtV2UND7ZP14cRuasC1SJ4Qw4P9G3AatZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات خصمانه ترامپ: ایرانی ها تا زمانی که به ما احترام بگذارند لازم نیست نگران چیزی باشند / محاصره دریایی ایران از بمباران تاثیر بیشتری داشت / با یک تماس تلفنی میتوانم محاصره را برگردانم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662454" target="_blank">📅 00:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قالیباف، رئیس هیأت مذاکره‌کننده ایران: انتقاد و آگاهی، حق همه مردم است
🔹
البته چون در جنگ هستیم، اگر بخواهیم همه‌چیز را بگوییم تا مردم آگاه شوند، به همان میزان دشمن نیز از اسرار ما آگاه می‌شود. بنابراین ناگزیریم، نه از سر بی‌اعتمادی به مردم، بلکه به‌خاطر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/662453" target="_blank">📅 00:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR-bOT-Wi2GNqtZEnzF1wMyrqS7GNEYMfW6OVYJDJmO9zNZP6Q77uHdVNIe7DhLW8dqTeQKZESYdANkOgi7NNEejP18lqyr9LxF9EfXQVU2dxCY2mqIPm0jBWa7rFrMb5yS4AE-aN8ZFNSbvtvC9GPK9QdVoMJJln9RwmPCOILsoRVpobcfPjmD8o9Px5z5wtzYo0OzlH_zkPRO6goBSVftCNaZoJxaxDAsfn2ZmD6Y21K916KumgD0Kezk0v7YhXlLTSMBf5Zopo-xZ1eiv_XVWojsqdXtv_P_SgnvonKKMb6UgBFgillHo4VQpJhv41bmrmSBRYvvv4Y0DFS3fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/662451" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قالیباف، رئیس هیأت مذاکره‌کننده ایران: دیدم در [یک] برنامه [صداوسیما] اعلام شد که کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، مسلمانان و شیعیان لبنان کشته می‌شدن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662448" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d098b42cd0.mp4?token=e8eevo3icBeoQnjH6NOWvkdN-ICDFjKAEd7x-KFRkqdJuBgWUKHsRGNOP9xp0Dq6DZATpIvAthD0PdxxpyrtJlkPC9_93a_Cn-RYe_XMi0IbvjZiwM1VmasyV-Oh6y_f47JqZvYECzuBus-zbN9BGMM4rLaPdCEK8dJPCb_ju9zF_ZmUwotFl2iqR5JNCDjN0fm-2Ni6MLZRBR1ZHWMdvNGpGAtB9GzdbVHetD7wnAYSYOE6zawv4ssuJP6Usucl-3vxesr6oAGFYHdnaczLz1q-bJuEe_ucAXeUM3RcRq35PYsxPVs0Y_KWf2afA-1W4b1bWCQDtAwjxXNyqGEgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d098b42cd0.mp4?token=e8eevo3icBeoQnjH6NOWvkdN-ICDFjKAEd7x-KFRkqdJuBgWUKHsRGNOP9xp0Dq6DZATpIvAthD0PdxxpyrtJlkPC9_93a_Cn-RYe_XMi0IbvjZiwM1VmasyV-Oh6y_f47JqZvYECzuBus-zbN9BGMM4rLaPdCEK8dJPCb_ju9zF_ZmUwotFl2iqR5JNCDjN0fm-2Ni6MLZRBR1ZHWMdvNGpGAtB9GzdbVHetD7wnAYSYOE6zawv4ssuJP6Usucl-3vxesr6oAGFYHdnaczLz1q-bJuEe_ucAXeUM3RcRq35PYsxPVs0Y_KWf2afA-1W4b1bWCQDtAwjxXNyqGEgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات خصمانه ترامپ: ایرانی ها تا زمانی که به ما احترام بگذارند لازم نیست نگران چیزی باشند / محاصره دریایی ایران از بمباران تاثیر بیشتری داشت / با یک تماس تلفنی میتوانم محاصره را برگردانم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662446" target="_blank">📅 23:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaft1-KbGu1PjIgyviMXv9XHxGSOIRMwVjz-d-7S5tcL2Rgq_OiPCWwvk5mJMEe6tRg8ADerpeTBLmKcjhXKw3GeL3h2dmAV67esvFbyZPC2LFKpHt1__aXM5NmRWj7xYGDnoV5JwmHEK52Bp2ss3ECtBdtaTJxcu1h5Rm4LaVT_ObmQVx3YFTQGatCB_y5IRAAkZ9gEQd3xOtL7CzxKx6vgLwhuEVkGouvHwIC1HLk2jS6dTIvvETpZRD97gp57FbyCIWks208zMIYXIp2zHspfKvuf8Kn00uf7HOpLA9G1paFSm5_cJMYiTXO5Hyx_UekFXY5HKKDCh_RU1oQ0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ‏«إنّ للحسین فی قلوب المؤمنین حرارة لا تبرد أبداً»
🔹
هر کجا می‌نگرم رنگ رخش جلوه‌گر است
هر کجا می‌گذرم جلوه مستانه اوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662445" target="_blank">📅 23:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2c57e7a.mp4?token=XvUXM_1s5iMBfBRUQZSSGmIzElLnJghiuP_Q2xoptrCGVgfoNHL_RkhsBQw3wWAjtMCVTw7rUrqCNg2Dl1KDceh-CWLzUHsUzUy8vHNCB0kxCZoNphjIst6p5lUTSPBz-_DE1kSSUThSRrwr-NZcA6ZcIkQf7r-IJrQmBV31iFAQCQ-WaaF1AEQZTIQtvom3nGZdZudJiGFsAiBmteoRrIIgDM-It6tfLYg2d-MJIUh-MhoQxCM_vmS86voLc3CeQwF774njAOwHkrmP3l0iG5bHu3qcCemiAvEcPQ5HiJW6Q0zolWyFwgcM12s2nlJC-8eBfvVEU-6Ec06MOE2SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2c57e7a.mp4?token=XvUXM_1s5iMBfBRUQZSSGmIzElLnJghiuP_Q2xoptrCGVgfoNHL_RkhsBQw3wWAjtMCVTw7rUrqCNg2Dl1KDceh-CWLzUHsUzUy8vHNCB0kxCZoNphjIst6p5lUTSPBz-_DE1kSSUThSRrwr-NZcA6ZcIkQf7r-IJrQmBV31iFAQCQ-WaaF1AEQZTIQtvom3nGZdZudJiGFsAiBmteoRrIIgDM-It6tfLYg2d-MJIUh-MhoQxCM_vmS86voLc3CeQwF774njAOwHkrmP3l0iG5bHu3qcCemiAvEcPQ5HiJW6Q0zolWyFwgcM12s2nlJC-8eBfvVEU-6Ec06MOE2SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اراجیف ترامپ درباره ایران: در لایه سوم مسئولین ایران؛ هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد
🔹
آنها ۹۱ میلیون نفر جمعیت دارند؛ نمی‌توانند آنها را تغذیه کنند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662444" target="_blank">📅 23:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبرنگار: وزارت خزانه‌داری تحریم‌ها را از نفت ایران برداشت  ترامپ:
🔹
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662443" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خبرنگار: وزارت خزانه‌داری تحریم‌ها را از نفت ایران برداشت
ترامپ:
🔹
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662442" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای ترامپ: مذاکرات با ایران خوب پیشرفت / پول‌های ایران از بلوکه شدن آزاد شد و فقط می‌توانند از کشاورزهای آمریکایی خرید کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662441" target="_blank">📅 23:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60db3d5582.mp4?token=fHmaqWhUxwibOaaS6Cm9kv1rAFWVvbka7YR2QQYfQmPuFd4jnEKqgQUmBGIZYs-_q5LFJxr39-0aq9VQKwHZYS41kO-AO9ylfqQ4ELyKEkdX-P1FXTZNLK3lGQgSksiyVKfER4NKVTxJ68DO-Y-q97wnOGUKAg9-2vhtpDH6UjK32wrqeRJcdxzIl8WQlofHDVyi3x75jDJAZLt2lFPEGoTS46qYv7NC6yAlEcXbTI8UzVAIXPiOa9fs3iS-RkCzsO2-oCB7F6F6dl1Zq4UGRxOLuStPMx5hU37nwyUeJ5Ek0Bb_WRW71bqQYIyNLqiAgTmGZrMPcahVizjNyNO6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60db3d5582.mp4?token=fHmaqWhUxwibOaaS6Cm9kv1rAFWVvbka7YR2QQYfQmPuFd4jnEKqgQUmBGIZYs-_q5LFJxr39-0aq9VQKwHZYS41kO-AO9ylfqQ4ELyKEkdX-P1FXTZNLK3lGQgSksiyVKfER4NKVTxJ68DO-Y-q97wnOGUKAg9-2vhtpDH6UjK32wrqeRJcdxzIl8WQlofHDVyi3x75jDJAZLt2lFPEGoTS46qYv7NC6yAlEcXbTI8UzVAIXPiOa9fs3iS-RkCzsO2-oCB7F6F6dl1Zq4UGRxOLuStPMx5hU37nwyUeJ5Ek0Bb_WRW71bqQYIyNLqiAgTmGZrMPcahVizjNyNO6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال تعویق یا توقف بازی فرانسه و عراق
🔹
گفته می‌شود مسئولان ورزشگاه در حال حاضر پیام‌های هشدار اضطراری را برای شرایط احتمالی طوفان رعد و برق آزمایش می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/662439" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662438">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
قالیباف: باید حول محور ولایت وحدت داشته باشیم/باید بدانیم فصل‌الخطاب، کلام و دستور رهبری است
🔹
آزادسازی پول‌های بلوکه شده و رفع تحریم های نفتی در سفر سوئیس نهایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662438" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a752b4180f.mp4?token=ZHmgGjWF3IY7gFEDogTRw8bHRgI5iUXSkQCMWaefqd7SoYpUQ3ogKL-WSaIbjEDjT7Bv_ogDdyZpxNtrQfWv1Ms0kzQ_CEa6n5xDWg6e6gvcoo2txGiyJGbsQUE9u1_BTedDZlD_N6S4os5d_XxKpZtyE_hVq9x5bbMJbA9gNu0pTosrWfv_rFqoAw30g0vbHbgxDPCOurZt7sv73sc4618REjyiJuqCb8B0otKWYqdiYh9WORqhRhKUi8hCUvzBeGahbuRyQkBWWxJSg_sxzH0WsN8iJaNwiyihIr5CaZUstOklcLR_kOVr3bTfFrLziQpDsa5tfPJuR-z5ouL8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a752b4180f.mp4?token=ZHmgGjWF3IY7gFEDogTRw8bHRgI5iUXSkQCMWaefqd7SoYpUQ3ogKL-WSaIbjEDjT7Bv_ogDdyZpxNtrQfWv1Ms0kzQ_CEa6n5xDWg6e6gvcoo2txGiyJGbsQUE9u1_BTedDZlD_N6S4os5d_XxKpZtyE_hVq9x5bbMJbA9gNu0pTosrWfv_rFqoAw30g0vbHbgxDPCOurZt7sv73sc4618REjyiJuqCb8B0otKWYqdiYh9WORqhRhKUi8hCUvzBeGahbuRyQkBWWxJSg_sxzH0WsN8iJaNwiyihIr5CaZUstOklcLR_kOVr3bTfFrLziQpDsa5tfPJuR-z5ouL8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف
:
باید حول محور ولایت وحدت داشته باشیم
/
باید بدانیم فصل‌الخطاب، کلام و دستور رهبری است
🔹
آزادسازی پول‌های بلوکه شده و رفع تحریم های نفتی در سفر سوئیس نهایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/662437" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q03Y9LeHpKrv5Y-6-UjfDAL0k6a8MpYDqsn74ETS4vKmXxC5J9KCrElWkJwTJDMVnReoT6dkgOdOApzj0L0cV0RViNreTmF5xBwrsQMBRpDI68iw_C0n_IlM5OqSoMWlFRyfryYNHpw5Ze9HaPrZluSbM9ZpXkIJshjnI8j7VYO6Nb4NTsDWfBEPvwifenO24ajf1mVgdJ7iWmohJXqnx2zW5nmo4AO_JkVg25eCvunLrX2DmVCV2b3mngC_mdH9l2gs4YpgWOvKZNMrYtrqEMIIAHbWZsmH6zwU_wrx6uP81YUxwkqA-TPgYiXbFqwgXMvCBfIgtUqPwv27HlNveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بالای یک قوطی فلفل سیاه در یکی از سایت های خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/662436" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c41e0981.mp4?token=KDVzTPkP7c00Snfa5Ax7dvpH0vQjILoGKIT0RPB-6M71WB28FLALjRsJCwTcbzVMlziD6YF6Whq4anqHNkrsD3MTMu30i9B7aLdDTS2S-w9QCaPWIuFuZfA8pcPxt7ygMOrZ8R6_m9L6n0xwrHENLXCP-rtyBj1RSuN6uzmGHCkaAGNa2JEtmH71BLcoJvFz7RYuJLlvVPniEbACH8LX5aNwBqktV-LqbK_5ciibaZRoujrE25uZydCUz3dH6h0mJfubAazTB_ZtdzXIGVqGRlY2zxN6eTDSKyiU8t48o5NLUbv12aLMNzGWinH1TgJSA4_NQFiWsOQVDNT9_EZj3ThvHnCr2mhutavD5UPebMZBXOrygGwS5vumZTszedg-V4iullnHtFqVdfY8DjdF-s5nZtl-xLSgsEmcahavkl8hyyG_vPWGdAtRdVpXPFSQE5lDT94_xruz-sDnOJfqL78Dstj12Zo1vDvdlY0iTN8XvT8HVSBUdxXLUDe16R4pkBF-YcBaDg_yBlVt67ftS8EvZzmIJaRZ4QSa67huB2Hn3Mna4T3XRuG4NMzzpAIxWrPZ_F7O1vs7HFgwQl3W41DhoVnXCLLdqqCDCNQIx7Ai54zfxxchkZ2K2HJegKG-RDjmyAdThVEwVp8D7EGOCYav4smm65h7myEy7wi4_XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c41e0981.mp4?token=KDVzTPkP7c00Snfa5Ax7dvpH0vQjILoGKIT0RPB-6M71WB28FLALjRsJCwTcbzVMlziD6YF6Whq4anqHNkrsD3MTMu30i9B7aLdDTS2S-w9QCaPWIuFuZfA8pcPxt7ygMOrZ8R6_m9L6n0xwrHENLXCP-rtyBj1RSuN6uzmGHCkaAGNa2JEtmH71BLcoJvFz7RYuJLlvVPniEbACH8LX5aNwBqktV-LqbK_5ciibaZRoujrE25uZydCUz3dH6h0mJfubAazTB_ZtdzXIGVqGRlY2zxN6eTDSKyiU8t48o5NLUbv12aLMNzGWinH1TgJSA4_NQFiWsOQVDNT9_EZj3ThvHnCr2mhutavD5UPebMZBXOrygGwS5vumZTszedg-V4iullnHtFqVdfY8DjdF-s5nZtl-xLSgsEmcahavkl8hyyG_vPWGdAtRdVpXPFSQE5lDT94_xruz-sDnOJfqL78Dstj12Zo1vDvdlY0iTN8XvT8HVSBUdxXLUDe16R4pkBF-YcBaDg_yBlVt67ftS8EvZzmIJaRZ4QSa67huB2Hn3Mna4T3XRuG4NMzzpAIxWrPZ_F7O1vs7HFgwQl3W41DhoVnXCLLdqqCDCNQIx7Ai54zfxxchkZ2K2HJegKG-RDjmyAdThVEwVp8D7EGOCYav4smm65h7myEy7wi4_XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس هیأت مذاکره‌کننده ایران
:
ماجرای حاضر نشدن تیم ایرانی در یک قاب با طرف آمریکایی و خروج از نشست مذاکرات پس از تهدیدات ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662435" target="_blank">📅 23:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
قالیباف: سفر به سوئیس برای مذاکرات چهارجانبه، دقیقاً در امتداد میدان نظامی بود  قالیباف، رئیس هیأت مذاکره‌کننده ایران در پرواز بازگشت از مذاکرات چهارجانبه سوئیس:
🔹
نیروهای مسلح ما با افتخار، قدرت و شجاعت، این پیروزی بزرگ را به دست آوردند. در مقطع آتش‌بس…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662434" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
فوت دختر ۱۲ ساله در یکی از پارک های آبی مشهد
حسینی، فرماندار مشهد:
🔹
متوفی دختری ۱۲ ساله از استان گلستان بوده که به همراه مادر و خواهرش به مشهد آمده بودند.
🔹
این نوجوان در حوالی ساعت ۱۷ بعدازظهر روز گذشته چند دقیقه پس از استفاده از سرسره آبی، در محوطه داخلی یکی از پارک‌های آبی دچار مشکل شد و متاسفانه اقدامات امدادی و عملیات احیا برای ایشان موثر واقع نشده است.
🔹
خانواده متوفی شکایتی از این مجموعه آبی نکرده‌اند و علت دقیق فوت و جزئیات حادثه از سوی پزشکی قانونی در دست بررسی است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662433" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
قالیباف:
سفر به سوئیس برای مذاکرات چهارجانبه، دقیقاً در امتداد میدان نظامی بود
قالیباف، رئیس هیأت مذاکره‌کننده ایران در پرواز بازگشت از مذاکرات چهارجانبه سوئیس:
🔹
نیروهای مسلح ما با افتخار، قدرت و شجاعت، این پیروزی بزرگ را به دست آوردند. در مقطع آتش‌بس و پایان جنگ، این بخش را با مذاکره پیش بردیم. اگر در اجرای آن اشکالاتی پیش بیاید، در پاسخ می‌توانیم هم با موشک پاسخ دهیم و هم با مذاکره آن را حل کنیم.
🔹
طبیعتاً همه ما، چه نیروهای مسلح و چه دستگاه دیپلماسی، مرتب با یکدیگر در ارتباط هستیم.
بنده نیز دیپلمات نیستم؛ یک رزمنده‌ام.
🔹
دیپلماسی را دنبال کردیم و دیدید که پایان جنگ و رفع محاصره را با گفت‌وگو، به روش مبارزه و با اتکا به قدرت میدان نهایی کردیم. عرصه دیپلماسی و میدان، مکمل یکدیگر هستند.
🔹
در بحث لبنان، از وقتی وارد مذاکرات سوئیس شدیم، دیدیم که آتش دشمن علیه لبنان قطع شده و بخش عمده‌ای از مردم به خانه‌های خود بازگشته‌اند.
ان‌شاءالله با تصمیمی که در سوئیس گرفته شد، تمامیت ارضی و حاکمیت ملی لبنان را در این گفت‌وگوها به نتیجه می‌رسانیم
و تا رسیدن به نتیجه، آن را رها نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662432" target="_blank">📅 23:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اژه‌ای: ۶.۵ میلیارد دلار سرمایه ملی در حوزه ارزهای صادراتی و تراستی‌ها به کشور بازگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662431" target="_blank">📅 23:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3344bffe26.mp4?token=rbEoCdPbztwBylhTVIxsIrlyKpKVEuKbqSw0oIEOPbml_KQqxMTdaWFfYw_0hYpNuLAktLKwoXVgVCPk1Ny76mrZHMBS6ZQ4r3wAIjH33Ik314ODdwPnFRav_5bna0AcIXfaf0eHiq20JVkI_Nd_mmRmuKeQd6_6Fb5yRAAX6T6T6OutJEsQREBAw7rRJssQX6YcdejvQhh2AGLwf31POCgONIjewcu2oIi2iiAsobbt_VQ91q6xmavrMUff5igsuESzS2tD2LCeU1gkNxcy21zHEfZSOAouTCU--qUSZI3sOUOmX4FZvNM9oITu1LPrWn3mNuTL84wPIA3WRIK1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3344bffe26.mp4?token=rbEoCdPbztwBylhTVIxsIrlyKpKVEuKbqSw0oIEOPbml_KQqxMTdaWFfYw_0hYpNuLAktLKwoXVgVCPk1Ny76mrZHMBS6ZQ4r3wAIjH33Ik314ODdwPnFRav_5bna0AcIXfaf0eHiq20JVkI_Nd_mmRmuKeQd6_6Fb5yRAAX6T6T6OutJEsQREBAw7rRJssQX6YcdejvQhh2AGLwf31POCgONIjewcu2oIi2iiAsobbt_VQ91q6xmavrMUff5igsuESzS2tD2LCeU1gkNxcy21zHEfZSOAouTCU--qUSZI3sOUOmX4FZvNM9oITu1LPrWn3mNuTL84wPIA3WRIK1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: مذاکرات با ایران خوب پیشرفت / پول‌های ایران از بلوکه شدن آزاد شد و فقط می‌توانند از کشاورزهای آمریکایی خرید کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/662430" target="_blank">📅 23:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662429">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
آمریکا: سازوکاری برای نظارت بر آتش‌بس در لبنان ایجاد کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/662429" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610d94da2d.mp4?token=VwyTu7eByRSWhcqg3nYwgY32QjnQWC5SJhRe-D5wvcib_bjE8ZV3IQcgqfhzyW9ZmIHdctC4353Tl-y2UkHLMQknB6oHIRmXsjrfWLxmSfbxfRsy93m7PpqYnKbJXmuvmpgzLWaXs-gAqBo-cqQvYqWR_jWb5HhTuuHJwjXeexUw9sW-ST-Sw3Noip1O6dIiUCcFO4WiLGyHT7iYQicHi1FfEAxENnHBFS1np-TLR8sKC-6uwxJSYfvF4Eohwy4XIOCevD3mAqQ0R_KFetPa-otCSqXtkXvTBSjcrlNZ8GR2b-DhatUePpmQj6DkNA3UYkhJvtTnuyarow3S5gaYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610d94da2d.mp4?token=VwyTu7eByRSWhcqg3nYwgY32QjnQWC5SJhRe-D5wvcib_bjE8ZV3IQcgqfhzyW9ZmIHdctC4353Tl-y2UkHLMQknB6oHIRmXsjrfWLxmSfbxfRsy93m7PpqYnKbJXmuvmpgzLWaXs-gAqBo-cqQvYqWR_jWb5HhTuuHJwjXeexUw9sW-ST-Sw3Noip1O6dIiUCcFO4WiLGyHT7iYQicHi1FfEAxENnHBFS1np-TLR8sKC-6uwxJSYfvF4Eohwy4XIOCevD3mAqQ0R_KFetPa-otCSqXtkXvTBSjcrlNZ8GR2b-DhatUePpmQj6DkNA3UYkhJvtTnuyarow3S5gaYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه ۱۴ اسرائیل: به نظر ما ایران داره با یه سلاح الکترومغناطیسی روی مغز ترامپ اثر می‌ذاره
🔹
رفتار و تصمیم‌های ترامپ نسبت به قبل فرق کرده و این اتفاق عادی نیست.
🔹
این فناوری شبیه تله‌پاتیه، با این تفاوت که از امواج الکترومغناطیسی استفاده می‌کنه. روسیه و چین این تکنولوژی رو دارن و الان هم ایران هم بهش دست پیدا کرده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662428" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9285c43e5.mp4?token=WSyG9laResn_F9veuJSnGnzuREXOuTpCVeXBNraeVsIiO4t67cxzgExsVFdLB_MZin9N_AT7xWdmtOQaTic1j9WCnE0Kt2RVBECBrxaYXyjN3Nz4dSz-JiGARlq2lKcnutzCDqINmTVgVUsL8baxRiJH70ZjEkueHROogByQIe7vD_dFEGzfB-JQnWfgsmm6n1r5V8pVyeGHnn_iWTEty7AAU9z2NT8VHKxPAuIeMV_AI9d6im54LXDfJMhdfclYhRcxalUJdU0aaSyal3G-W5dGsj9DXZyAGboUg2ziSvdK8C4XDktKTCJhle0OwLkQOA52oGzV3x-5SlDFGoqtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9285c43e5.mp4?token=WSyG9laResn_F9veuJSnGnzuREXOuTpCVeXBNraeVsIiO4t67cxzgExsVFdLB_MZin9N_AT7xWdmtOQaTic1j9WCnE0Kt2RVBECBrxaYXyjN3Nz4dSz-JiGARlq2lKcnutzCDqINmTVgVUsL8baxRiJH70ZjEkueHROogByQIe7vD_dFEGzfB-JQnWfgsmm6n1r5V8pVyeGHnn_iWTEty7AAU9z2NT8VHKxPAuIeMV_AI9d6im54LXDfJMhdfclYhRcxalUJdU0aaSyal3G-W5dGsj9DXZyAGboUg2ziSvdK8C4XDktKTCJhle0OwLkQOA52oGzV3x-5SlDFGoqtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های طارمی قبل از بازی برابر بلژیک: فقط بدویید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662427" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز کاملا باز است
ترامپ مدعی شد:
🔹
ما توانستیم نفت بیشتری از هر زمان دیگری عبور دهیم، تنگه هرمز کاملاً باز است و ایران هرگز سلاح هسته‌ای نخواهد داشت.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662425" target="_blank">📅 23:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc84704817.mp4?token=ogqUffT8Xf95JEkZZAt686QJkEAT5SncDXSQ_JWVEXJMAxAmQOUm7Md8GxSjAf0tJUjDVyecHY7chbajhPGhu6Emuls_m8gBA9ZpP20MqoMjs4V_SzGgfFe-IA1X2cuodISUxSwzQmm61m4EbmAf8vUQVSi7Ik5wDBVfPJGcTByK6TakM8PaEvQphOOIvhRl4H4f4DKAHvs0Ihn5WffTswhKq1vFOPKK-Dgp9fmEoqu-TGVHnnpJbvRhe0kqC3cJ94NieVT9c269EQTOoQPNV_w3gguv5-3VA5Sz0JQSZfA1SqcJdRoYYyxLreJsNL0XMQnWOi7hOiaDFs4Sv-GbfBh9ozRCce6Yr9erFZRXJlIYfE-7yNSxSiilGhC07T1WTL7_zoRk96be6hJH34z6Ryw8ly-X56GL7V9DdRMiVEEtSCkOWGvoHc_aqYnW6INZb-yP59YKfGWLH35yF3eDG-L00nrmYdrQ4rxeBE6EktrB9lVZZbsl-DZCA-kzEkfxMe83L2HFCpp974_E5EBDfaP8ReJB3SvDF1caqHj6PRyf24c5Ls1Bmot39pYHqxjx4d_IobxtO_e_gNbLkDraDrWjwg-DpEJ7EgjlXNuqnMLQnjRA-zawnScT0dQAdC-6_m8mL8wcMYLHdTpcADqCx9T8E47V-1qr_AISB487_Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc84704817.mp4?token=ogqUffT8Xf95JEkZZAt686QJkEAT5SncDXSQ_JWVEXJMAxAmQOUm7Md8GxSjAf0tJUjDVyecHY7chbajhPGhu6Emuls_m8gBA9ZpP20MqoMjs4V_SzGgfFe-IA1X2cuodISUxSwzQmm61m4EbmAf8vUQVSi7Ik5wDBVfPJGcTByK6TakM8PaEvQphOOIvhRl4H4f4DKAHvs0Ihn5WffTswhKq1vFOPKK-Dgp9fmEoqu-TGVHnnpJbvRhe0kqC3cJ94NieVT9c269EQTOoQPNV_w3gguv5-3VA5Sz0JQSZfA1SqcJdRoYYyxLreJsNL0XMQnWOi7hOiaDFs4Sv-GbfBh9ozRCce6Yr9erFZRXJlIYfE-7yNSxSiilGhC07T1WTL7_zoRk96be6hJH34z6Ryw8ly-X56GL7V9DdRMiVEEtSCkOWGvoHc_aqYnW6INZb-yP59YKfGWLH35yF3eDG-L00nrmYdrQ4rxeBE6EktrB9lVZZbsl-DZCA-kzEkfxMe83L2HFCpp974_E5EBDfaP8ReJB3SvDF1caqHj6PRyf24c5Ls1Bmot39pYHqxjx4d_IobxtO_e_gNbLkDraDrWjwg-DpEJ7EgjlXNuqnMLQnjRA-zawnScT0dQAdC-6_m8mL8wcMYLHdTpcADqCx9T8E47V-1qr_AISB487_Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ حریف احتمالی ایران در صورت صعود!
🔹
سه سناریوی سرنوشت‌ساز تیم ملی در صورت صعود؛ صدرنشینی و یک قرعه طلایی یا تقابل با مدعیان؟
🔹
در این ویدیو حریف‌های احتمالی تیم ملی را در جام جهانی بشناسید.
@TV_Fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662424" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0rqgd7iIqeuJnzxwaJsZpvKAkSu7y4qJUFKI42DKVba3BR153g16ALeGgQCMM99cDc9zcDpztH_b97mRUVqO6P2HlS7A21oy7ggLJpzaRaq8_Ooz1pKTmBtkkSbXJuGGwxFaTiF63u_LH2wKWSzpIEn-y04iTInGag9QjEZe7JQsneyVnvMOuXwv2PloFcif9jElJThLqSp696bFGlqYlXzcZKfV8lUc0D-IYblrCfA2R850kbp3ejKAmZB8aeDAxsTtD4JeuKcimpnTbGtx4BEw6qSif0gFF_6d2JPtZ4BJ6utf5jgc7ttIQcumdvBx8qBVZbTdYSNY6GsstxBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنالتی که مسی به این شکل مقابل اتریش از دست داد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/662423" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رئیس هیئت مذاکراتی: ما در گفتگو‌ها توانستیم ترامپ را مجبور کنیم در یک ساعت توییت خود را اصلاح کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662422" target="_blank">📅 23:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: اسرائیل تنها تهدید توافق ایران و آمریکا است، اسرائیل به هر دری خواهد زد تا در مسیر توافق خرابکاری کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/662421" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8qGeDSqx2zxvCYjdMfoQJFSP-yU3TlYHiW5qDf5sNDcoGfYLnbo4h9jP8w0fuuOf51oHq0vfhOaKNwQuznOqmnzFR9vXTZxzMgzeCqBlxPqx-uUQbow0C7P-Xt8w2IxetJfhLQ_Zq_p0bi00H_Z6eApSntaf8s3IOZFIp51TsTwRUnbyiQjrnZAY41zjGZzp1IrcLXnHP2oN2Rq9TLKx0ce3UIxhLx7-IedDG7q6-2FFMuSQgyFB3cOYqJXNuPoXvIghVQSg0_tlSF9HmoQRpaZ8gBE5d1__NE5fV4Rfb6FcBka60ta_oVCWLyJNs-ut13BhaMUerZhNnuv7pfn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvSNhZ8_PprO7WfeLeWFlUr7o3VmFegiS4KMpPNvqAHeVd_VqgqPebLF7hKVHV3J5nn6eQQ4A4W-fFT-EhiTD2G5mNP7WqgNDah418STO36YLSMJNA2XiQ7g51zKjqb-LZ0Zmle6awwmpeCLSHstLYMhsu_KUkOxhCukNadtfVZAHewWan6kVAYb_OxqduQRaDrjlLbXNsCpeXkNIJD0oJDofdG7Ovilr0TR96SLVe5AnPzSxYE1d2eUjvmBdOCDc-1mwrNPD-Rzn23pW7Ii38-be0Huwf4xovmxo-Cv_pvNvX3a7adMOC_08MXsobcnF6vSc5eVaRBnUzn3o6Lw-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آکواریوم عروس دریایی دیده بودید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662419" target="_blank">📅 23:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662418">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52b1f0cf4.mp4?token=IHVcCtJ3zxfsbUy36cQMEHKRu9QznXDOnbNZ7R3orWXE6z-QEQI87706dzFVdAKcjBoSvaB5X80DoIf7gl6jkyfaEBjIe1qZQ9u8P5lN5peduFVbSUzGhZaGq3jij7nui_BgHQa0EIb7wWYZImO1NQy33e5ZtODoOUebVxtg6MYcrbqaY0faOba1dNDK0nrNROwX1h4aNuRq3VVSdFxWN_jq7EpoEN1mPyhWtQifExFMHZxW_T9wVe7w8zIt3fBpmRXWdzeDDp_mO3y4rbrJQbc8A377rfND-T8sujr9MAS5BkoK9RrwKzZSkmfHy__2_33Hsc-g4pq-okGJtAiANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52b1f0cf4.mp4?token=IHVcCtJ3zxfsbUy36cQMEHKRu9QznXDOnbNZ7R3orWXE6z-QEQI87706dzFVdAKcjBoSvaB5X80DoIf7gl6jkyfaEBjIe1qZQ9u8P5lN5peduFVbSUzGhZaGq3jij7nui_BgHQa0EIb7wWYZImO1NQy33e5ZtODoOUebVxtg6MYcrbqaY0faOba1dNDK0nrNROwX1h4aNuRq3VVSdFxWN_jq7EpoEN1mPyhWtQifExFMHZxW_T9wVe7w8zIt3fBpmRXWdzeDDp_mO3y4rbrJQbc8A377rfND-T8sujr9MAS5BkoK9RrwKzZSkmfHy__2_33Hsc-g4pq-okGJtAiANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهردار نیویورک: از زمان آتش‌بس در فلسطین بیش از ۱۰۰۰ نفر کشته‌شدند؛ نام عاملان را باید فریاد زد
🔹
زیرنویس اختصاصی خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662418" target="_blank">📅 23:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سفیر ایران در عراق: از هیچ طرفی برای مداخله در جنگ دعوت نکردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662417" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662416">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
پشت پرده تهدید مرموز ترامپ/ احتمال حمله جولانی به لبنان
👇
khabarfoori.com/fa/tiny/news-3225054
🔹
تکاپوی مذاکره‌کنندگان؛ قالیباف راهی عمان شد، پزشکیان عازم اسلام آباد است، غریب آبادی در سوئیس ماند
👇
khabarfoori.com/fa/tiny/news-3224854
🔹
پاسخ تند پزشکیان به شعار انتقادی حی علی الاصول اساتید بسیجی دانشگاه تهران
👇
khabarfoori.com/fa/tiny/news-3224880
🔹
چهره باورنکردنی فرزاد فرزین پیش از عمل جراحی بینی و چانه
👇
khabarfoori.com/fa/tiny/news-3225042
🔹
خاکسپاری بی‌سروصدای بزرگ‌ترین هنرمند عصر حاضر | تشییع فقط با دو نفر!
👇
khabarfoori.com/fa/tiny/news-3224999
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662416" target="_blank">📅 23:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxMnVe5FqOsU8sNudXedGr_v-XeE3DQn4uzlgFecY1qw56TnqcauJNXaWJsUQmk9myI2bkDCeSH8uj2_1sF_ofxkKbcivKCNCVWNT-9lLaqV6ja3V-s9MeWMrU-zLJeaUO6WwDT2i6TVnIIX246cwclz8b_NfoHkaR7GPiOWmgCfPNZn1oq8JcXKSrqpP6xbSalAZTKZeUoc6KXR0fpdOpSzwWUdV1lCoj2T3Dx0djjNW2388RWmH5DHH_LkYfnQV6oezlo5-zzgcl6pfHpi9HORUjyYXUDneYpx_--M5lDNrkY3UN7zJ09eS5sOhi799wCDXshCQQBck-GP4kPCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیر ترین زن ایران درگذشت
🔹
خانم "گلی پاپی" که متولد روستایی از توابع شهرستان دورود در استان لرستان بود، بعد از نزدیک به ۱۴۰ سال زندگی، درگذشت.
🔹
با توجه به تاریخ شناسنامه، خانم پاپی ۱۲۶ سال سن دارد ولی از آنجا که در گذشته سن دقیق افراد در شناسنامه ثبت نمی‌شد و همچنین بر اساس تحقیقات تبارشناسی و محاسبه سن پدر و برادران، خانم پاپی حدود ۱۴۰سال سن داشته است و متعلق به ۵ نسل گذشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/662414" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4c0QQHOC4agcYdsGZHNTMQUqMkAFwfoN0pxAnufDt3TMTC7B9FyR-pvUJ85i7VIqKnsWBpBVtrXulOCzAbskIxE-XfC68Qy3RYyCGMnCqbQ4qQxepuxB0fxtM1Vbx2EUo0mT8bEr15Gj83uEJsNThqIMMQdV7hM_Z138aOBBov-JqT8OGaycPHlskP6KCufSZZuTSTG29kBtf9M1PnMb0f2ouaQ8l8Ug20Kv_IkD1d0V1Ta9OzvRSN2WMqbW-DVjFAGXx8iu1nByLRZKjOHLiIZ-EzWfmS7UMWLOtuf1ImaHZH828aLiTZXVMfLkIeNlq1wjpJIx3UhozTHCFpdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWAy6HBI7hcTJokkmtN4iOObCCUYxrNuspswocVCuXNai2JqWHCBI4xwA1tkowwMquf1O12MNqy-5y6eOko4tgBJ7j4CnJHGWX0ta7Q5borWD4rcGihPPEq56ac-MK-ox7yT1PsLycn5Jyhf7uQE0_LRMdiIkBb4qCtva0SOBQ5JL421xrhKH0YKOJtnXXrFSaK0TR7TGZVsvVaKPPmdv79UtrNZ9oY-6UIRGarraspAtrYSx9NHQsUphBHkRtRwK-XQo__ka9sgn5HH1XS2KnhcykWAw_hxUcrbTnMAmW8RTKrLnI6XVGF4LtOMy2pH-OrZk8T33Gi3xMSrjLwbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSZ1GSex9a_2Q8FKLQBfRZfEu0eqy1aYuGFB2_cYfU9n2Yv0QIYZwdOMgZbQ5P-vcqLuQBKGktNTWBNbJW711cAg17HdMBiEzr8052qCS3cL3aDmzsi53gzMf8VRQ0pP4TR1j75zJK8HtiYlj8ObAqDOy_qZqUokdewRcuz_txQRYBCCQm0gXGU-16F4JS8gEs21Uo0Zz_sbOqnoq3qNgK0JbZg66j6AOMTGlvZcwGnUzr76Rf-RRWHkoKd5eA44pODk4Nwx7t2OAn-rm31AMx-JO6m0RYQikNlhOrXR_kLeXn98Y5LCeyQAKi7xQDC-7dLwhV2KCgVHLMEXnibq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebQhF0ZEuq-7c-jdzyvNiZimghbhtH1wE2E_jCQ7wH4T_0_hL6c9fNdIWqxwk_1UN3w1mJmfVgOxrMkuafYIIXkgpupvu7ZpncZlQPmkQbNyiVnMhCAMbNAD0p6ci8LsWiyRlxPOVbi1o7sWiLL2iYXKlXC1faPIWlRr7k95vXWmpmS-6WdM2isAbtqolApEcsyjizATVmUUznbzLM70GtqqfuZzeRYV24M0SE6e7nG89rG9acumAI9UVIWefjyqabXgKQsfP4mY6gnH_nHL7KN5OyLbEX4JNSaV9y4Y0cKB0p-BJ_j7_ad0TztWM5jOJ72USHEnje66s_8HuVisUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس هیئت مذاکره کننده ایران با استقبال وزیر امور خارجه عمان وارد مسقط شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/662410" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662408">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RV1A7n1_9Z00retpO7PT85A0q-JAp_HGxqPRL2kTJ8pzc1CjVb5d-tW_M8UASar-Q1E_YlxwZAM1LuhH0WBBLdHm0dJGQxccPaFH_uOFQEdYttW23clkBC4GgkxvDyGEpZHmEEQiDzoWNzF-6QLtarq00kMAgx6vKszKbFdz5JI3iHHfaxmkL52wFE0pZPjNeqep9HDSKd8R-YdyJGJfkr8jqC1DB_D3Qok-tTnaEXgXbDMzsjCP-xX-sJoZk18a-XoNwJKTgWpqoO9tCDOgoBux8wAuy8aGUNapDmL0uAIVB0kfcRIULRcuOyogmgpr9v6ub-l08vg5doOnZYrikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادگاری ویژه «بیرو» از بلژیک؛ لباسی از یک رقیبِ یک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662408" target="_blank">📅 23:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662407">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyTS3breIEeLNO8yvdl_JlQnZx0xNFZdHPWTRLsuCGdhL0swx6k5BalkxDiRF00z_x9BVA9Qratg6AB8MV_CwY-Jq-4UcyJB6LVGUxFpaqiMdRyuTeJyNYLuA-d1FEd_kLiXMdRt9HG9tA7otlVQMv3kksUucAfkGQlcAr0G1LJLhtGE7VwsEm2kX10kE6aUi7pNPj4UeHwszPuEMVeXP3FA_HADfXVcabB4MhywDXR1C-Jf_A0JLrje6_kXGZRF8LjhiZ9tLKOHlYWaGtS-qnuodpQMN139O8L9naKVxMqM0hxqmiJBlSfBD8bHilmm9_OKLp61DxaH950imhvaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌هایی که تاکنون به مرحله بعد جام جهانی ۲۰۲۶ صعود کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/662407" target="_blank">📅 23:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu94Ew7IfhjhAokQ6VLgDbV4ys6xLZ_NSBEQlpJ7TuJKtQL9ybQKZVSCVQ6CpPgMk2aMSZqhNG1sKyHUbs5QyezGRY1eaaoyi5G33AYSB4blA7iG_zYY_BbkTG-G-Ob0FWgAOVpzYPsCrivxxRSjhNUZNKTJy-njyaODXm3spGWI2rk28EwzCFMT7a734oTS_pjYcJr1aJ5JzVnT8-n165uiOKSVCDO-o6mJOtYqHxCKvaYmkqAsnb6XNhFmgekszVsDH0SwaMMqfJ6O2nacqG4pJ0TdhpmTTBwmgEKftR-tdbHsKJtMVbpy5PqHnPwUiHwnxW1jpTdTlrAf2fmMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مروری بر ۷ شرط گفته شده در تفاهم‌نامه اسلام‌آباد
رهبر انقلاب:
🔹
از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. ۲۸/خرداد/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662406" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سقوط بالگرد گشت ساحلی آمریکا
🔹
گارد ساحلی آمریکا اعلام کرد که یک بالگرد گارد ساحلی ایالات متحده در آلاسکا سقوط کرده است.
🔹
امدادگران و تیم‌های جستجو و نجات در حال اعزام به سیتکا، نزدیک جونو، برای یافتن این بالگرد هستد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662405" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662404">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCjjTF95f1e3VJDF0izNOzVDQ92ol0i4DT0wRf00_exTZa7nAzoPOJfFPr_8YDUFcwXkCrPr5QqnVwvFGs2D9qJFXvwozT9R3AU6oSLLwk7T4Xs7qISD7EjnyjYI2KJJJgqK3hx_MEZMxX816qz_ve5ZeC-ntPlh5mVyGzDE8EULFmKfUnhXq-Lctlk6k8R1h6gz_yemhPxRSFUIPChF32YmQdlBNe8ula1od82TUC95sPqNDmjzBdaQ2jvQh0fhSKiL4GSelBVmeRZUeLncoOZREN1_StoD_qmMr5PA9ncVv2VW_E8MVCHRvsnWs87PJAwKNWwRCG16werHOlzFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای اطلاع‌رسانی دولت: ترامپ اقرار کرد اینجا «خلیج فارس» است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662404" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEE2hVf0zXX7ZDFniqr9MNPtDATO8C527L4HKAXzQ5Q_ps2plCsd173ZpFgL47H7NTgYz4cHAYxlTyN0DEpMcChaI5Wbc8EwdtqIs_yQyS3CQauCV-DbRImCZ7oqt4FbGSbx2s7qihezpCDTxiwybxOp8JJ-D-0rvvK_5N4FVDhmku_C1tbSeQk3zq7jZorGJPTXyxqoOdqygr18xhF3d3L0LPUBv8cAkop8WN20XRnbuNUmWc2oMV9tr6-3Xu2ES8dhpI_DJN_K89lbzTcQ755VBSKYY2V2pgycgS3t2XWrIsohno5Ir3MOBnL_7vuBr-8vl6zjKMg4FeDmg_HtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقطه ضعف تهدیدهای ترامپ چیست؟
🔹
اگر به تکرار الگوی «تهدید-عقب‌نشینی»های ترامپ نگاه کنید بیش از آنکه تاکتیکی هوشمندانه باشد، اعترافی است به این واقعیت که ابزارهای نظامی و تهدید آمریکا، کارایی سابق خود را در برابر ایران از دست داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/662402" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
۵۸ هزار میلیارد تومان تنها در یک فقره فساد به بیت‌المال مسترد شد
/
ابطال ده‌ها مصوبه خلاف قانون توسط دیوان عدالت اداری
رئیس قوه قضاییه:
🔹
فقط در یک فقره از مقوله مبارزه با فساد، بالغ بر ۵۸ هزار میلیارد تومان، وجوه ریالی ناشی از فساد به بیت‌المال مسترد شد؛ و این به استثنای سایر اموال از قبیل ارز و اراضی بود که در همان یک فقره، به بیت‌المال بازگشت.
🔹
دیوان عدالت اداری طی دوره اخیر حدود ۲۵ مصوبه دولت و شوراهای عالی که خلاف قانون تشخیص داده شده بود را ابطال کرد. همچنین بیش از ۱۲۰ مورد از مصوبات شوراهای شهر و روستا که خلاف قانون بودند نیز باطل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662401" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای نماینده مجلس: با امضای تفاهم‌نامه، صادرات نفت از سر گرفته شد
عباس قدرتی، عضو کمیسیون برنامه و بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه کشور متکی به نفت نبوده که با محاصره دریایی به مشکل بخورد و بیشتر درآمدهای دولت از محل مالیات تامین می‌شود که تاکنون مسئله‌ای در تحقق بودجه نداشته‌ایم، البته با امضای تفاهم‌نامه صادرات نفت ایران دوباره از سر گرفته شده‌ است.
🔹
مبحث کسری بودجه قبلا هم وجود داشته و جنگ تاثیر چندانی بر این کسری بودجه نداشته‌ است و انشالله با به نتیجه رسیدن مذاکرات اتفاقات خوشی را پیش رو داریم.
@TV_Fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662400" target="_blank">📅 22:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5711d5ab98.mp4?token=UtIigXNcbE7I70tHdqKNHItzskFk3YQYhu4-CLoBUJgjkIXyZKlQj_C09ay3sFsiucLyDQApXjc28Kr9s8WNWYJq77JFOHkVtwy6TfTBwhZOSOZhX_GD2_ui6_UtQCBLwNfP5fgLXCoYPmtGH7hfIE2Z4HYpirb57_JTRiJyf8IdzjgWzToXOW6nEta_7XC5gFiu8QPaBuEy6wpETs14wz0NjDo9bZh1JGvFt96syMLUwO-5zUEfG7rdBkyN1-dgjBVEQOpFQ53Xb9DDhaCRHQSZj_Ox21p5x7mtgn3hcOjgqf7AxNl969518nDOcN1cGhTchflZO4Q2er2djE4frA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5711d5ab98.mp4?token=UtIigXNcbE7I70tHdqKNHItzskFk3YQYhu4-CLoBUJgjkIXyZKlQj_C09ay3sFsiucLyDQApXjc28Kr9s8WNWYJq77JFOHkVtwy6TfTBwhZOSOZhX_GD2_ui6_UtQCBLwNfP5fgLXCoYPmtGH7hfIE2Z4HYpirb57_JTRiJyf8IdzjgWzToXOW6nEta_7XC5gFiu8QPaBuEy6wpETs14wz0NjDo9bZh1JGvFt96syMLUwO-5zUEfG7rdBkyN1-dgjBVEQOpFQ53Xb9DDhaCRHQSZj_Ox21p5x7mtgn3hcOjgqf7AxNl969518nDOcN1cGhTchflZO4Q2er2djE4frA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به اتریش توسط لیونل مسی
⬛️
🇦🇹
0️⃣
🏆
2️⃣
🇦🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/662399" target="_blank">📅 22:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63b0044a9.mp4?token=gKwN86gNWLNAE7_lbqwvdK9m12uQzxpD6NL444zNAO0i8ZyDYYEiwPwIEqFi_Y13EyuV8gjU4ra10d6EirpuTSqZYTGP-yvBpI8UypoUMtP936Ur9dRfTn2s0fMVhjPDGK4m0LStXEwyYaaDIrFBgFnioBvbZLT6gO2X-iiQHbngcZWO3ZNWjHyIlsYViLXJTIHCuhqUnut8vRbIRD7MtPLnXuTDE9VEgUR3ukRdD6UWvy-Pl1rVIAXuW7tweigqGfWn956snAu5Z44F55TO_s3GUr_fV-fQnyml0AaP8iL0OGDFdP2CRhaTpvbsn0ARXe7-jD6fYmg-LofuDWuw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63b0044a9.mp4?token=gKwN86gNWLNAE7_lbqwvdK9m12uQzxpD6NL444zNAO0i8ZyDYYEiwPwIEqFi_Y13EyuV8gjU4ra10d6EirpuTSqZYTGP-yvBpI8UypoUMtP936Ur9dRfTn2s0fMVhjPDGK4m0LStXEwyYaaDIrFBgFnioBvbZLT6gO2X-iiQHbngcZWO3ZNWjHyIlsYViLXJTIHCuhqUnut8vRbIRD7MtPLnXuTDE9VEgUR3ukRdD6UWvy-Pl1rVIAXuW7tweigqGfWn956snAu5Z44F55TO_s3GUr_fV-fQnyml0AaP8iL0OGDFdP2CRhaTpvbsn0ARXe7-jD6fYmg-LofuDWuw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکایی‌ها چطور مردم ایران را به خون کشیدند؟
🔹
روایت مادر ۸ شهید از نحوه پیدا شدن نوه‌ شیرخواره‌اش روی درخت روبروی خانه هدف موشک قرار گرفته در حسینیه معلی شبکه سه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662398" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rivOF_rYhGM0zWUoZ5jStjQBPzEilA_e8uiLJVmhPEEOQzElCzXNx-KBATAcxApxAR8QkGeTJJAgdnBn9Awtxhgdpc_jtBsqDepg6xUb_8TxB_XatWsAB8Y-XWCaI4j6hmO40X629yjtI9yqnht2q89QbBa2rGkFv7IDCwnqosco3RO73wLDvI1ZD6LpPrSNFBDY-UkNQ950FtjexWm_-ntRSHrQ_JF2um3SDykyEvHm530WhTJAcPw_ZecrWgAadfSoQh5D4sh2TE4KcfgNQxgCCqcRAsnUuA66urQGxev159uJEAReEBuUOEJqv-pJ0alRlkr_0W3NxQW7TtfK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر استراتژیک نفت آمریکا
🔹
با ۹.۱ میلیون بشکه کاهش دیگر به ۳۳۱.۲ میلیون بشکه رسید که پایین‌ترین میزان از سال ۱۹۸۳ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662397" target="_blank">📅 22:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcVvASpopap8bUMaSVAz4o95B0HzJdOgj4oTUWnUQmAhflwp5NNSFOrSl1MjYI3cbiTsyLEvWbm9hJVwJGl4T_2kZeNkJqfEyk8rBX28_JNbdx9B40C1cJIW_AMvPwCPeYge3ymoJs3VR7upNgc8ebwMPFOjAUB36L4ecAMZuycCc0CZaxHUI0Q9eQyttZmTt_YO3n76XknwacHemDQ40S_l-Flvzet1Pl0R5gGmXR9iJ-hcjkA0cqDIlvR9ESucAXTbbefCyEd5siiAPhgYU2wSirMLLjPItt_D7fuVI28BXFvgGWeldE9CH63pT6TGn0IwmPg1ccpIzFeJ9y8AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴۰۰ میلیون تومان و ۴۰۰ هزار پزشک؛ گامی جدید برای رفاه جامعه پزشکی
🔹
دیجی‌پی و سازمان نظام پزشکی جمهوری اسلامی ایران با امضای یک تفاهم‌نامه همکاری، مسیر تازه‌ای برای دسترسی اعضای این سازمان به خدمات اعتباری و تسهیلات مالی باز کردند.
🔹
بر اساس این همکاری، بیش از ۴۰۰ هزار عضو سازمان نظام پزشکی می‌توانند از مدل‌های متنوع اعتبار خرید و وام بانکی برای تأمین نیازهای شخصی و حرفه‌ای خود استفاده کنند.
🔹
این تفاهم‌نامه، علاوه بر توسعه خدمات مالی برای جامعه پزشکی، می‌تواند به گسترش استفاده از ابزارهای نوین تأمین مالی در میان صاحبان حرف تخصصی نیز کمک کند.
🔹
در قالب این طرح، امکان خرید اقساطی از دیجی‌کالا و هزاران فروشگاه حضوری و آنلاین طرف قرارداد با دیجی‌پی فراهم شده و دامنه استفاده از این اعتبارها از کالاهای دیجیتال و لوازم خانگی تا خدمات سلامت، گردشگری و خرید طلا و سکه را در بر می‌گیرد.
مشروح خبر در
👇
👇
khabarfoori.com/fa/tiny/news-3225033</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662396" target="_blank">📅 22:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKu0LYmzv9ue2suhLP45zhhf9eYaYDRomXLf-W0NZYvNCHoOH1hBoP8Kl4T8EGgacyd293j9xs2xw2Wh6eX-SKxg0Gqvk1r3D0zr4hTfMd5XG82nI3cihSt7LAjAlo4UQ8GTZBDm5Ylc_pULpRN5DHbHneNr5gRnENe0YJhJiyCxxzji9RNsV6kN6H9eO1iw94p6t400fDvlxzljj-HGUGcQjzu6y0r9oD_r22G-VMnmB6CAX1o2Jm40fBtm3SinR6wt8FBGRnaLVR2e_KSfcGMsQ9_Tfr7A9fHxahQJLxp_Q7TayRmv9JiIcCXNSgZcemjJQJV4JwQuNWgetFtLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجارت جان؛ بازاری که فقط دو مشتری دارد
🔹
امام علی(ع) مردم را دو دسته می‌داند: گروهی که با دل‌بستن به دنیا خود را به آن می‌فروشند و هلاک می‌کنند، و گروهی که با اطاعت خدا نفس خود را می‌خرند و آزاد می‌سازند. آزادی حقیقی در بندگی خداست، نه در پیروی از هوا و…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662395" target="_blank">📅 22:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از ۳ بار جدایی روح از جسم به زندگی بازگشت
🔹
00:14:10 حرکت به سمت نور با سرعت بسیار زیاد
🔹
00:21:20 صحت‌سنجی مشاهدات مراحل احیا با پرسنل بیمارستان
🔹
00:31:00 من را به دنیا باز نگردانید، حال من خوب است
🔹
00:37:00 آرامش توصیف‌نشدنی در حضور نور که باعث از یاد بردن همه چیز شد
🔹
00:43:20 شناسایی پرستاری که جسم را احیا کرد
🔹
01:02:05 ترس از قضاوت دیگران مرا از گفتن حقیقت باز میدارد
🔹
01:04:30 شنیدن صدای سوت هنگام خروج روح از جسم
🔹
01:14:40 شرط بازگشت به دنیا
🔹
قسمت هجدهم (آزمون)، فصل چهارم
🔹
#تجربه‌گر
: شاپور سعدی‌نژاد
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662394" target="_blank">📅 22:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ab2f169.mp4?token=XsZBWTQLaWEpuhgfmkW5uZnHnUqIPJXkRW2OPnqdoF_gEuD2uhvFr2SDp-F8PK_Scg2FvMokb_J-_yEDjmZv4izk9O_ts2SN-rwETtX1sDYwzXsG94DRbTb1uJJfmG7zGmYvB16uQ43RNpTuKqYH9Vf1lH5afDQ5Zcp_GZEviueTi7br7y2LUTTaosdsYudis_D59_cUBCJoyhl_od0gWmtUJc54qplez69rimV8jYSeA7zdBFuD3gfaDVj8SQblIjTEywx6Gz1Q04_Djv7cnHLYCWLJEct9CSrwEXo2jWdYJ28OjAmYgxEegr1CjkyeL4EhypMw0XNbSWOg6tXRbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ab2f169.mp4?token=XsZBWTQLaWEpuhgfmkW5uZnHnUqIPJXkRW2OPnqdoF_gEuD2uhvFr2SDp-F8PK_Scg2FvMokb_J-_yEDjmZv4izk9O_ts2SN-rwETtX1sDYwzXsG94DRbTb1uJJfmG7zGmYvB16uQ43RNpTuKqYH9Vf1lH5afDQ5Zcp_GZEviueTi7br7y2LUTTaosdsYudis_D59_cUBCJoyhl_od0gWmtUJc54qplez69rimV8jYSeA7zdBFuD3gfaDVj8SQblIjTEywx6Gz1Q04_Djv7cnHLYCWLJEct9CSrwEXo2jWdYJ28OjAmYgxEegr1CjkyeL4EhypMw0XNbSWOg6tXRbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس هیئت مذاکره کننده ایران با استقبال وزیر امور خارجه عمان وارد مسقط شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662393" target="_blank">📅 22:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a903f249a3.mp4?token=tQPL8jEDcx2iuNa_OzbvnjLHYxiAb-mcW7wxwfZCJFLuFNruy-9wMUgI0MNbbgzXuJX8HZ-u6UDhHPzQAXV79dY1AohdCB4decZgSSQqVGc24oNQkMdbK_fsKjwepOxfUHLZ-iG-UxXTT2YUGrz4ITd-V9ajc_ibAcwi7StWeD1zhXVnbc3uqg6_Lr1On_eiKyIac1hpfV3dFBis24rUagSf5ICCBAA7iKySQwsCVyPaK3qJeSLRNwU2Fn3KpqoV1tbTsP26dqfgR6AdF1L-fGxMh-TdfzZFzwblTTYgFi5cLvV0P5oyEDmISTMZBdQqmnm4hu0IErRFOw-lfMGl9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a903f249a3.mp4?token=tQPL8jEDcx2iuNa_OzbvnjLHYxiAb-mcW7wxwfZCJFLuFNruy-9wMUgI0MNbbgzXuJX8HZ-u6UDhHPzQAXV79dY1AohdCB4decZgSSQqVGc24oNQkMdbK_fsKjwepOxfUHLZ-iG-UxXTT2YUGrz4ITd-V9ajc_ibAcwi7StWeD1zhXVnbc3uqg6_Lr1On_eiKyIac1hpfV3dFBis24rUagSf5ICCBAA7iKySQwsCVyPaK3qJeSLRNwU2Fn3KpqoV1tbTsP26dqfgR6AdF1L-fGxMh-TdfzZFzwblTTYgFi5cLvV0P5oyEDmISTMZBdQqmnm4hu0IErRFOw-lfMGl9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: دیروز لحظه‌ای پیش آمد که عراقچی وارد اتاق شد و به شما سلام نکرد، شما دست ندادید و بعد او بیرون رفت، آیا از این بابت احساس تحقیر کردید؟   جی دی ونس:
🔹
نه؛ باور کنید، من در چند ماه گذشته زمان زیادی را صرف تعامل با ایرانی‌ها کرده‌ام. گاهی اوقات آنها…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662392" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe1d4aa38.mp4?token=Bxjocu8P9eFv9ZJl94x2VahG-jLonDdbgxAIwKv1LxBW7QtWIbGTvfBZ1EC69E8PcYNw74XuhEIjv8R5cyuoR2EQdP_p4LDLWRDet_q5wnAO0yHfuwkjBLrcoBOgm9cUAeyOrAaOsRkOVZ9I5dGR8_7ezihzrYLq-XYozM4cAbxoDeiRsDryh10kjWJ5EKkdrjJ6nCPgPsz_iRrEJgD9L8JKvMtRhbXLp7P02CWFc_CwjPOaK_aiusf8wnw4LVfJYhU-jr2jgw94DS_ejmS1WCMnNxhCtIwPacFW-BtAINUj91TSK45c_sZC6W6NpOIOuuz7YHz4GeTLnep0g3hrkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe1d4aa38.mp4?token=Bxjocu8P9eFv9ZJl94x2VahG-jLonDdbgxAIwKv1LxBW7QtWIbGTvfBZ1EC69E8PcYNw74XuhEIjv8R5cyuoR2EQdP_p4LDLWRDet_q5wnAO0yHfuwkjBLrcoBOgm9cUAeyOrAaOsRkOVZ9I5dGR8_7ezihzrYLq-XYozM4cAbxoDeiRsDryh10kjWJ5EKkdrjJ6nCPgPsz_iRrEJgD9L8JKvMtRhbXLp7P02CWFc_CwjPOaK_aiusf8wnw4LVfJYhU-jr2jgw94DS_ejmS1WCMnNxhCtIwPacFW-BtAINUj91TSK45c_sZC6W6NpOIOuuz7YHz4GeTLnep0g3hrkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: دیروز لحظه‌ای پیش آمد که عراقچی وارد اتاق شد و به شما سلام نکرد، شما دست ندادید و بعد او بیرون رفت، آیا از این بابت احساس تحقیر کردید؟
جی دی ونس:
🔹
نه؛ باور کنید، من در چند ماه گذشته زمان زیادی را صرف تعامل با ایرانی‌ها کرده‌ام. گاهی اوقات آنها را به عنوان مذاکره‌کننده بسیار گیج‌کننده می‌بینم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662391" target="_blank">📅 22:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شور به عالم رسید</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/662388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
شور به عالم رسید
باد به پرچم رسید
زخم به مرهم رسید
ایران به محرم رسید
🎙
#مهدی_رسولی
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662388" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662387">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای دیگر ونس در مورد مذاکرات سوئیس تکذیب شد
یک منبع مطلع نزدیک به تیم مذاکره‌کننده دربارهٔ جزئیات مذاکرات روز گذشته در سوئیس:
🔹
پس از پایان دور نخست مذاکرات، با وجود درخواست طرف‌های مذاکره، هیچ دیدار چهارجانبه‌ای میان طرف‌ها برگزار نشد و متن نهایی شب گذشته نیز با تلاش و میانجی‌گری واسطه‌ها به نتیجه رسید.
🔹
علت برگزارنشدن چنین دیداری، توییت تهدیدآمیز ترامپ بود که با واکنش هیئت مذاکره‌کنندهٔ ایرانی مواجه شد.
🔹
ونس، معاون ترامپ عصر امروز در نشست خبری مدعی شده بود ایران میز مذاکرهٔ سوئیس را ترک نکرده بود/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662387" target="_blank">📅 22:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ترامپ با مقامات ارشد پنتاگون و صنایع نظامی نشست برگزار می‌کند
🔹
روزنامه وال استریت ژورنال به نقل از منابع  آگاه گزارش داد که دونالد  ترامپ، رئیس جمهور دولت تروریستی آمریکا مقامات ارشد پنتاگون و مدیران صنایع نظامی را برای جلسه‌ای در کاخ سفید در روز چهارشنبه احضار کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662386" target="_blank">📅 21:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
خبرگزاری
آناتولی: ایران از زمان اعلام توافق با آمریکا ۳۶ میلیون بشکه نفت صادر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662385" target="_blank">📅 21:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662384">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQmqGZJnn8zMoO0C3eZbjsiUKGsiAhys3Sy54fTkWZG0gryxWG1nmDvR-7VQTW7apdWHIs5Ynx4YzGnyEzHv3mZ-zNlHynXlahPOOmbHdoX6gHY2lNI5-bMKqCzVgNXGtEquzE4wIufe3uTWlQhIROKY1tPd6KhGvD6I8WXQ6S84elFZCsvHpE6RTvcU3VXdMembAJCuE-0YRvWrfil3_BlulnjWU5qSTcu5F1tm9376l4h2PRwR_KZcanic3Qv7smkeJvtfskKaNK_XCg2L6R77gDZb41JDPVGQNfF6XIkL2aCFUDRGtxWaNIPOMC_4zLIN2A1gD_8z-2G1rNlpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی با ۱۷ گل و با عبور از کلوزه به بهترین گلزن تاریخ جام جهانی تبدیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662384" target="_blank">📅 21:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662383">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c959dd72.mp4?token=TCghFfv8yoiCgHzx1VROr7kt1W4R4EDobeKciLKrmDwP6i2o5peuWzPgXQPhqf8K8LbI1Crdx3mw2lwGGvbMWuNkYOTSOmolCBEtMUmU3avFEJMKtY5na41cTXUQaeIkGoIIKQ44EDeFdQNz0nUx-6pEWC46fYVXPx3787NpZKm0rQmwgi_5swhvKaJuN-BXM_M7bMf4q4L0Qjm8SNhoJxJTyih2fMlEoQT6gxr7Zmwu4vfdNlquQyleb2vDG0IlH1wwlinEoQIHU03r_9Ol4clInx1vm2RrqQ9GpwrjAQ0YC6xCIOT_SvMZdbfywDtlUS0BGybEnv7_DS4KEM3kBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c959dd72.mp4?token=TCghFfv8yoiCgHzx1VROr7kt1W4R4EDobeKciLKrmDwP6i2o5peuWzPgXQPhqf8K8LbI1Crdx3mw2lwGGvbMWuNkYOTSOmolCBEtMUmU3avFEJMKtY5na41cTXUQaeIkGoIIKQ44EDeFdQNz0nUx-6pEWC46fYVXPx3787NpZKm0rQmwgi_5swhvKaJuN-BXM_M7bMf4q4L0Qjm8SNhoJxJTyih2fMlEoQT6gxr7Zmwu4vfdNlquQyleb2vDG0IlH1wwlinEoQIHU03r_9Ol4clInx1vm2RrqQ9GpwrjAQ0YC6xCIOT_SvMZdbfywDtlUS0BGybEnv7_DS4KEM3kBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارنامه کامل تیم ملی بعد از دو بازی
🔹
دو مسابقه، ده‌ها آمار و یک تصویر روشن از وضعیت شاگردان قلعه‌نویی.
🔹
جایگاه تیم ملی در بخش‌های مختلف جام‌ جهانی را در این ویدئو تکست ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662383" target="_blank">📅 21:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
جی دی
ونس: پول‌های ایران آزاد نخواهد شد مگر اینکه شاهد پیشرفت باشیم و بدیهی است که این بخش بزرگی از مذاکرات در روزهای آینده خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662382" target="_blank">📅 21:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای معاون ترامپ: در مذاکرات فنی با ایران پیشرفت کردیم
جی‌دی ونس:
🔹
از قطر خواستیم تا به ما در یافتن مکانیسمی برای اطمینان از اینکه دارایی های مرتبط با ایران کجا خواهد رفت، کمک کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662381" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عارف: هیچ اعتمادی به دشمن نداریم
معاون اول رئیس‌جمهور:
🔹
حتی در صورت توافق با آمریکا نیز حفظ آمادگی کشور و افزایش قدرت بازدارندگی از مسیر توسعه علم و فناوری، یک ضرورت دائمی برای جمهوری اسلامی ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662380" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662378">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تحریم‌های نفتی ایران به‌طور موقت لغو شد  وزارت خزانه‌داری آمریکا:
🔹
مجوزی صادر کرده که بر اساس آن ایران می‌تواند تا ۲۱ اوت ۲۰۲۶ نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی خود را به فروش برساند.
🔹
طبق این بیانیه، واردات این اقلام از ایران به آمریکا نیز در…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662378" target="_blank">📅 21:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
محدودیت‌های پروازی تهران، قم و مشهد در زمان تشییع پیکر رهبر شهید
🔹
سازمان هواپیمایی کشوری از اعمال محدودیت‌های پروازی در برخی فرودگاه‌های کشور طی روزهای ۱۳ تا ۱۸ تیرماه ۱۴۰۵ خبر داد.
🔹
فرودگاه‌های مهرآباد و امام خمینی(ره) در روزهای ۱۳ و ۱۴ تیر با ظرفیت و پذیرش محدود مسافر فعالیت می‌کنند.
🔹
۱۵ تیر محدودیت‌های پروازی در پایانه هوایی تهران تشدید شده و هیچ جابه‌جایی مسافری انجام نخواهد شد.
🔹
طی روزهای ۱۶ و ۱۷ تیر نیز پذیرش و جابه‌جایی مسافران در فرودگاه‌های تهران با محدودیت همراه خواهد بود.
🔹
محدودیت پروازهای هوانوردی عمومی در استان قم در روزهای ۱۶ و ۱۷ تیر اعمال می‌شود.
🔹
فرودگاه مشهد نیز در روزهای ۱۷ و ۱۸ تیر با محدودیت عملیاتی مواجه خواهد بود و در روز ۱۸ تیر هیچ جابه‌جایی مسافری در این فرودگاه انجام نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662377" target="_blank">📅 21:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آغاز ثبت‌نام ایجاد و ترمیم معدل برای کنکور از دوم تیرماه
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش:
🔹
ثبت‌نام متقاضیان شرکت در آزمون‌های نهایی برای ایجاد یا ترمیم سابقه تحصیلی از روز دوم تیرماه ۱۴۰۵ آغاز می‌شود و به مدت ۶ روز ادامه خواهد داشت. متقاضیان باید در بازه زمانی اعلام‌شده نسبت به ثبت‌نام و انتخاب دروس مورد نظر اقدام کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662376" target="_blank">📅 21:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782bf9bb54.mp4?token=ifXVIotpP_UsbiL0lKkE1t-mzL7GX3d-SrR9xl1mz-3fWlhGFdMpK9LaVX5YYoVvUtSVZIJYR_KoOvjUw2JxsS7R7vipE9GIDPjJ1XJ4tfCbn2y8ONCPpaCmMndQ4BU4yFlR5GexzKBgsqP7nKikekiggAahgN6AZE8enWlck10OKNrT9PlOFoirfLwbtz7vJQ6bE3r2GD-uay3xSbWKByRbwP9LpZfafuknfi8wQffVZMebQWtskO1-IvY6HcsbFyzHpw-Jthpoq9myhR1se5Ky4wt0INa2jnWUG69PUeqx1ORnNrrpzKQMsmKBXK_kYSNHg1ygdvY9gIuLcixlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782bf9bb54.mp4?token=ifXVIotpP_UsbiL0lKkE1t-mzL7GX3d-SrR9xl1mz-3fWlhGFdMpK9LaVX5YYoVvUtSVZIJYR_KoOvjUw2JxsS7R7vipE9GIDPjJ1XJ4tfCbn2y8ONCPpaCmMndQ4BU4yFlR5GexzKBgsqP7nKikekiggAahgN6AZE8enWlck10OKNrT9PlOFoirfLwbtz7vJQ6bE3r2GD-uay3xSbWKByRbwP9LpZfafuknfi8wQffVZMebQWtskO1-IvY6HcsbFyzHpw-Jthpoq9myhR1se5Ky4wt0INa2jnWUG69PUeqx1ORnNrrpzKQMsmKBXK_kYSNHg1ygdvY9gIuLcixlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: مذاکره، یک روش مبارزه است و ادامه آن است و آن‌هایی که می‌خواهند دوگانه درست کنند، که تو طرفدار این میدانی یا آن میدان، این موضوع در جاده خاکی صحبت کردن است و یک بحث انحرافی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662375" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b9cf5d2.mp4?token=DpfV7JM3FJfMJq1BCTLraoetpslmI3na1rkN87LlUAJDg8VrGYJk2oGPmHp1WNhmautHCCY0LSKXre4pmZxEssvCvjXd1urBEonVxath35gusk7b6SlLopSBEQnVeyGUcdzPF3X_e70ZYpdoi1G3PnPt0kdT7Q87H3dJHW5PUpQ9JSeYTKfQTr9jbpujgccQ888vdHPkuaIynFBheMQ0RfNgx9ra03sXY0W_mqwgWHdxc1T09xdgL6vPW0aDX8iHUPfWTkoaURRmYBN39PY8E22KjxIaubqaUTtfxXTaO7CYXOlxUeOwXn8EnGnHlmnaQUvuFTUL2Jrn9GbItRwqR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b9cf5d2.mp4?token=DpfV7JM3FJfMJq1BCTLraoetpslmI3na1rkN87LlUAJDg8VrGYJk2oGPmHp1WNhmautHCCY0LSKXre4pmZxEssvCvjXd1urBEonVxath35gusk7b6SlLopSBEQnVeyGUcdzPF3X_e70ZYpdoi1G3PnPt0kdT7Q87H3dJHW5PUpQ9JSeYTKfQTr9jbpujgccQ888vdHPkuaIynFBheMQ0RfNgx9ra03sXY0W_mqwgWHdxc1T09xdgL6vPW0aDX8iHUPfWTkoaURRmYBN39PY8E22KjxIaubqaUTtfxXTaO7CYXOlxUeOwXn8EnGnHlmnaQUvuFTUL2Jrn9GbItRwqR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به اتریش توسط لیونل مسی ۳۸
⬛️
🇦🇹
0️⃣
🏆
1️⃣
🇦🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662374" target="_blank">📅 21:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رئیس‌جمهور: آمادگی داریم دیپلماسی را در راستای حقوق بین‌المللی ادامه دهیم
پزشکیان در گفت‌وگوی تلفنی با رئیس‌جمهور ترکیه، ضمن تاکید بر تداوم ادامه روند دیپلماتیک برای استقرار صلح در منطقه:
🔹
ما کاملا آمادگی داریم دیپلماسی را در راستای حقوق بین المللی ادامه دهیم، ایران به دنبال جنگ نبوده و نیست و این آمریکا و اسراییل بودند که تجاوز غیر قانونی را رقم زدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662373" target="_blank">📅 21:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: همه به خوبی آگاهند که ایران موافقت خواهد کرد که بازرسی‌های تسلیحاتی گسترده‌ای را بپذیرد تا «صداقت هسته‌ای» را برای مدتی طولانی در آینده تضمین کن
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662372" target="_blank">📅 21:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: توافق ایران و آمریکا، به معنای پایان سیاسی نتانیاهو است
خواجه محمد آصف:
🔹
رژیم صهیونیستی در پی شکست توافق صلح میان ایالات متحده و ایران است.
🔹
دستیابی به این توافق می‌تواند به پایان سیاسی نتانیاهو و حتی بازداشت او منجر شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662370" target="_blank">📅 20:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeMzbBG_j4bZFlffLLgbnZH0iIP67W99FWBiUdga9k0-aHUMq0PHjKIvHB19r58JELtsg7TezOEdUBwGkZfZwDzc0yYu5oquh8iRXQKSF-90g8K0rnS5RpMdTwEK7XCTTwj7VV0FCPi4A9EAbUf2xh9_Jlxk_tIPtlvm0OLdhalhj8gGsjkc0O4KvbUaSClRabNC09QMebCr-6vsiwLCfmGB4n7gVbWFi73lVXv_uOpRJUfJtAvy9TxVhpAOb8zXTcs6AdDgm0rK3MlPLXIb5jzNjR4Pi7jk-9RHtHoJYuAFyjme7iCVqpaIjvSdp1pkWZJ0x6A6NNYxK9LpSYqLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد  یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662369" target="_blank">📅 20:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاالله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662368" target="_blank">📅 20:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820e1e95a2.mp4?token=bsliiWf-mWfxY6-P45BWxCDo2vn9D_JvUfUsZsZ4i94xxB0yzuDTb57582mFw35Fe8QQChBY07bWm43nDlXpJjOSTMUVkZAwwOHIOn1JnZVm4uPa5XRFxqzbRmbSs7kAzWfbxYTQM0zhbcn080LzceEG299C_1vRdR6WFc17r9OZywFQ1GsSrvCdxed2-_ymjcpIqTS5BtdVM6iHTE7y4euAVeq7jHZiE8pio9AGiE6-h0SQF33qPkFu6r28KydVArru-D6bAW5WWULryzbspFlN13IOWSgjyvmp9vO2pI8Z9H52XlNyraPdGJpSX-BGkTsA1W9htUTTBtBvsDIWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820e1e95a2.mp4?token=bsliiWf-mWfxY6-P45BWxCDo2vn9D_JvUfUsZsZ4i94xxB0yzuDTb57582mFw35Fe8QQChBY07bWm43nDlXpJjOSTMUVkZAwwOHIOn1JnZVm4uPa5XRFxqzbRmbSs7kAzWfbxYTQM0zhbcn080LzceEG299C_1vRdR6WFc17r9OZywFQ1GsSrvCdxed2-_ymjcpIqTS5BtdVM6iHTE7y4euAVeq7jHZiE8pio9AGiE6-h0SQF33qPkFu6r28KydVArru-D6bAW5WWULryzbspFlN13IOWSgjyvmp9vO2pI8Z9H52XlNyraPdGJpSX-BGkTsA1W9htUTTBtBvsDIWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاالله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662367" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSVIB7v6DIrunud08IJIP6pD5usFr5-LcGbZeCyDxj1q7_NoJyFcyalvPLjiswDIWtO2Hu0yf59th3Z9Pr86Rl-OjqPObSME513uOKdcTAz3uWkaMqVe7wWlEX0h2kW58d4ewEQ_uKV-i_GCodqj_cbDpMd979H0F1-tIE3Ok-biwMA3Cy-532U-nu5FDTLx-4QPOOBeFz2lipCqySW7EjSvc36xsbu8st0gEtFLP2dXxyAMZVeEeZ1bu5_tolyh6hrMW_iStJMWbN19XmO4jUFtJJm0OlhrzzeYAFnzcRNOWgz1FuMhwyQvb6k9BFkwNvF1NRbC9G5Wskj4nFDcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ایران با بازرسی‌های عمده موافقت خواهد کرد
ترامپ:
🔹
همه کاملاً مطلع هستند که ایران با «بازرسی‌های عمده تسلیحاتی» جهت تضمین «صداقت هسته‌ای» در آینده‌ای طولانی موافقت خواهد کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662366" target="_blank">📅 20:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662359">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac354b107.mp4?token=lgT90WG8r6Ki5rz0UN8tAA4Gwshg4EP_kHqf0kfvUMV6tGH3lBwcQufTGyG9Ne_y5sNs_Xj74u8OSdjc-iWl8_XkcxkvmrG02uB2y0_hPcnCR-Jc9xz2lKeCP6EzvBVUsM8yet1jRc9aprUTiCAiOOcdpUIyXcVn7jaIVOMLEc7ZqXl3A7milIc3IAbxJW--LBtMHTH8YqONHStou1IEIK5XOVcbupBNS5g31BpzRc-OMN4-zjS_e9IwD98-Z9-9Fd-E8VRxTIJTX6NsgcDA4Bd8i_YtMo0w9rfCnhtftRoDunzP62IhCZvqlBkv7SBgVS23e7gt2QrodUfH_Z-8XE3HPlokb5K9gMgeWGv03DD-nhcEmbonaVXxcWk5-j5-YKYe9a2b9t89pSHcjnOXeB_BUSYJVw4t3XFiHQVy3pPOEcbq1yat-tJGtuMZ_Htk7QELZ5NWEirJoHOQHpv7FtDommLErCJNsjGPUFEvHaMe1comcTLKl735l4mp6VuATLK-6Ltv11xzQLPN2ZE9UtzlCxWPoCYJvTa3ApevQeDsddbInxuuYV69BavYbIK2eRKO7MVkW68UO_3FCcikpqxNKqF3ISlhTgPXMacbO5rQaYYgcnQLkxbzA3N1X_7ziwbvNueC3c5k8_0Br0XDCNYw6FVJvDtRYFwtaONw1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac354b107.mp4?token=lgT90WG8r6Ki5rz0UN8tAA4Gwshg4EP_kHqf0kfvUMV6tGH3lBwcQufTGyG9Ne_y5sNs_Xj74u8OSdjc-iWl8_XkcxkvmrG02uB2y0_hPcnCR-Jc9xz2lKeCP6EzvBVUsM8yet1jRc9aprUTiCAiOOcdpUIyXcVn7jaIVOMLEc7ZqXl3A7milIc3IAbxJW--LBtMHTH8YqONHStou1IEIK5XOVcbupBNS5g31BpzRc-OMN4-zjS_e9IwD98-Z9-9Fd-E8VRxTIJTX6NsgcDA4Bd8i_YtMo0w9rfCnhtftRoDunzP62IhCZvqlBkv7SBgVS23e7gt2QrodUfH_Z-8XE3HPlokb5K9gMgeWGv03DD-nhcEmbonaVXxcWk5-j5-YKYe9a2b9t89pSHcjnOXeB_BUSYJVw4t3XFiHQVy3pPOEcbq1yat-tJGtuMZ_Htk7QELZ5NWEirJoHOQHpv7FtDommLErCJNsjGPUFEvHaMe1comcTLKl735l4mp6VuATLK-6Ltv11xzQLPN2ZE9UtzlCxWPoCYJvTa3ApevQeDsddbInxuuYV69BavYbIK2eRKO7MVkW68UO_3FCcikpqxNKqF3ISlhTgPXMacbO5rQaYYgcnQLkxbzA3N1X_7ziwbvNueC3c5k8_0Br0XDCNYw6FVJvDtRYFwtaONw1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ شب هشتم محرم حضرت علی اکبر (ع)
🥀
کار تشییع تنت دست عبا افتاده
تار و پود تو ز هم سخت جدا افتاده
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662359" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14951272bd.mp4?token=VoZJoWxKXP0EM9rKrAkchthKw8_r2PTGoQnvoH45TaFz78PiIyxknd_PKFfLhivfidcpih8SAcg5r08M5WjxBZ8swAZFaA5tH2-Ch4JZXlu25UmOwjO42R2kwi8OBG4hWnfXJW0lvVtRsI_1uYW9iir3lhzAnKKa27Tfh0MkWqho52IIxy6Uzge5upIMr2Jqfu2DczQgZlbPp5vKX1dxixt82TcuvEI2DZYK3QJgVQhutmp3LnfQwWlOqyYlbtyx5HzisAkYWTTVMjDoIJW1HXRB47ffEnJLcxyTHJnW0A4Q4XjCxq8Kbgo9_TpL5XTNBMCxIxbddHfSgraJWI6Edw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14951272bd.mp4?token=VoZJoWxKXP0EM9rKrAkchthKw8_r2PTGoQnvoH45TaFz78PiIyxknd_PKFfLhivfidcpih8SAcg5r08M5WjxBZ8swAZFaA5tH2-Ch4JZXlu25UmOwjO42R2kwi8OBG4hWnfXJW0lvVtRsI_1uYW9iir3lhzAnKKa27Tfh0MkWqho52IIxy6Uzge5upIMr2Jqfu2DczQgZlbPp5vKX1dxixt82TcuvEI2DZYK3QJgVQhutmp3LnfQwWlOqyYlbtyx5HzisAkYWTTVMjDoIJW1HXRB47ffEnJLcxyTHJnW0A4Q4XjCxq8Kbgo9_TpL5XTNBMCxIxbddHfSgraJWI6Edw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنالتی که مسی به این شکل مقابل اتریش از دست داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662358" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLQAiPL78LEGdg4wZGtBVJ8O9u1sAFGegt5aYNBgJm8WV1QVutCRMDRrc09TtwoFdzvt2w6VOBGSu-2hVWAJCm8L_Er1r85JVTX2PZ-08yO5HPvD0ieY7zjCSuPs5HOQy-kEmx5_-kek1WSWK7ewquKnswziQpVKI0QWYHdziAPPNhTwVC2uMIkbKJO0kWpDNI2lQdKRljPIEwrvluUEGaTMBBS1am6_AL5CXDOGoAFqQ9ptaLvdn4_83DguXBcncdUHBSpznN6Sp8RIfNgb7qNAmiLPmZ-icSsTAGxnLRXnrPBHCYF1HE3JO4JlyOwQvVmf8PGkfLQIXFzsO8kBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sb5wflrvoH7u0kyhuT3nIwXpHVFBPv2YlU4cBsRb2yW-MurgDWRTUJXcmErmJ0AE8sFqmOjs1nSP5FfiM21TB1i6nE5PgSEWMy72Rhg58xQ7RS53m2qp150Ol98SAzpaQ9MU2Hfg08DGSnXSrUeX3N6Xak9flxB8PyEXnvHAAvEjtI46DK5lgorqRuhmHSe4pC_GIYH4A_IMRiqUZ89MqA7_DU9GhjN9Zq12oSTSG_wvAeo_r2O8d_AThgn5PMf-V-PKBZohi5oesXdtC46r1EoBoTpT5SWlip7PYGR9V38LTlj1H-oOHQQl5SXhmwLrz3iqRgGPDAcvCSVimLPJ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر دختر نوجوانتان می‌گوید «هیچ‌کس من را نمی‌فهمد» این کتاب را به او هدیه دهید
🔹
احساسات دخترانه فقط یک کتاب نیست؛ دوست صمیمی برای روزهایی است که نمی‌دانی دقیقا چه احساسی داری. با تمرین‌ها و پرسش‌های جذاب به دختران کمک می‌کند احساساتشان را بهتر بشناسند،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662356" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
«
مسگون
»
سه‌شنبه ۲ تیر
در تمام کارگزاری‎‌ها
«مسگون» صندوق بخشی در صنعت «فلزات اساسی» با تمرکز بر مس و نماد
#مسگون
در روز سه‌شنبه ۲ تیرماه ۱۴۰۵ پذیره‌نویسی خواهد شد.
تحولات قیمتی صنعت «فلزات اساسی»
در کنار آینده ممتاز «مس» این صندوق بخشی جدید گروه فیروزه را به یکی از گزینه‌های جذاب بازار سرمایه تبدیل کرده است.
💎
تخفیف ویژه معاملات و خدمات اعتباری اختصاصی در کارگزاری فیروزه آسیا:
https://in.firouzeh.com/kargozari
https://in.firouzeh.com/kargozari
🔙
👨‍💻
واحد پذیرش و پشتیبانی کارگزاری فیروزه آسیا: ‍
🔜
+982152461000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662347" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تمدید خودکار قراردادهای اجاره با سقف ۲۵ درصد
وزیر راه و شهرسازی:
🔹
بر اساس مصوبه سران قوا، قراردادهای اجارهٔ مسکن که تا پایان سال ۱۴۰۵ منقضی می‌شوند، در صورت درخواست مستأجر، به مدت یک سال و با حداکثر افزایش ۲۵ درصدی اجاره‌بها و ودیعه تمدید خواهند شد.
🔹
مراجع قضایی نیز صرفاً به دلیل پایان مدت قرارداد، از صدور حکم تخلیه به درخواست موجر خودداری خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/662346" target="_blank">📅 20:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8lNaop5PP7uMGW29kq-OBxvPGR4f0f026aftoHph5ljvDaREYAxQz6Uc-rHPzOrzEwowWD4XGok9Ewd04dmz9O9vHLINHaCHoCD-pyOf50N5cJ47uvUBtMNuhxArVQ3sf5uBnGoOLqfft7GtPASUpxA0u9EMYOi5mDlefW7A7cwao7yJ5-ufqL32k1W73GWrU0NVeXqCbow_vYZ9N0kMt3C871D0g7LUk1-bTTJShINVvhaVkSFQiGJ4Ohs2-TzGuRw7exhxW9pNDzNfYyXG5Zt5G-G98KIAThgkBW4rEx7wZK39-sE-YT9-0pSCljOMwGZdN3gW4sw1xJ79sMcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIVkFiXt8vbh4VIqGazHun6lVu9G6I7WOcaFrBUihAXzxHcdkmrci-V7wR-FlJWbo1-cFN-7Mixp-LlWVo4khzU7dVBEt-efNwWBc9ySU82I5644KA1XvDFQY1Dk57K7QmkKBHICEInK5WtZZc9U6i4iTUF5PgNulNAbohfH3DFf8FNrt6b7auiNqpu0UfAneYXzTWkkyRSNbcFSGMz5OMb__Ztputyt-hocv351H4V3N4t45hXxV_9ftcv2XkemChse2ykfL5vpCEUU6_NOunAXT-lmXRqjdFLgkbGtSp7lvWVQeKJLt_vYeJ6hTP5RkhJlqYQ5_Uigd_f15s2jZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سن ازدواج در کشورهای جهان چقدر است؟
مردان و زنان نروژی با ثبت میانگین سن ۳۹.۷ و ۳۷.۱ سال در صدر جدول دیرترین زمان برای شروع زندگی مشترک در جهان قرار گرفته‌اند.
این شاخص آماری در جامعه ما برای مردان ایرانی روی عدد ۲۸.۳ سال و برای زنان روی رقم ۲۴.۱ سال ایستاده است.
کمترین میزان سن ثبت‌نشده در این بررسی‌ها متعلق به کشور اندونزی است که ارقام ۲۳.۸ سال برای مردان و ۱۹.۸ سال برای زنان را نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662344" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد  یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662343" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد
یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662342" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ea230cc81.mp4?token=er12aeHBV0TgnMqs49YA2onnLurd9eeXxaavtFHtiIw9bNNq0HTGg2A84TdeuY-6WVP3A8z-rfHpQQKdHwyIFlppARNs0TLhpUuc_-6Xh7Nsycyr05ZkdWofd9WYeVY-d6VfkUlpwLx-aIrAstURMk3O5SBW_dD-R2u0tcGwEj2T-I_3aERuEMr08RFAhWfGVotaViEhsqQO9dAjBpCt7WZK7JaZXTRL9iA2yQ-t4qsULCYUpLO93b3Mrm7wTT0t5uDQR-7ICudHiy3WfrowUsiIvV8aKfHwSd4KYqU2vmdCZV-Pj-59s0ol7FMGpkyTpgCdLhoGadMGV7IeL2-w5p-DBsBbo6GlQg_Ma2FsLWm48428_oLo0lbvvP5ScMfehySQC9QwwH7zCVew3n3xOj3BdNrgHy8WWfxQ6Ml9kdGXqtONHebPb5UYR4S7ewDnACyIoNoPh79Z6BUR9EdmztQh99F45mSWspGxXO8zWX-TwtToimrgEDNUDSyeihkuCuNsp-7XiWh5vCPs3o2btqJwO0CvA1L8Nr8aatrsoUCeD8fTzLbuERDKqCpb5CBkQciijBcg-Qfjx0hjFBrj3aNYlGS8OuF7LozxBtzUIto3N4uKVSLRu0ABBQi6r5RR5KBmFQ-0MFwXV5Zid_do2FvYawWr2npc56KgSLQokT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ea230cc81.mp4?token=er12aeHBV0TgnMqs49YA2onnLurd9eeXxaavtFHtiIw9bNNq0HTGg2A84TdeuY-6WVP3A8z-rfHpQQKdHwyIFlppARNs0TLhpUuc_-6Xh7Nsycyr05ZkdWofd9WYeVY-d6VfkUlpwLx-aIrAstURMk3O5SBW_dD-R2u0tcGwEj2T-I_3aERuEMr08RFAhWfGVotaViEhsqQO9dAjBpCt7WZK7JaZXTRL9iA2yQ-t4qsULCYUpLO93b3Mrm7wTT0t5uDQR-7ICudHiy3WfrowUsiIvV8aKfHwSd4KYqU2vmdCZV-Pj-59s0ol7FMGpkyTpgCdLhoGadMGV7IeL2-w5p-DBsBbo6GlQg_Ma2FsLWm48428_oLo0lbvvP5ScMfehySQC9QwwH7zCVew3n3xOj3BdNrgHy8WWfxQ6Ml9kdGXqtONHebPb5UYR4S7ewDnACyIoNoPh79Z6BUR9EdmztQh99F45mSWspGxXO8zWX-TwtToimrgEDNUDSyeihkuCuNsp-7XiWh5vCPs3o2btqJwO0CvA1L8Nr8aatrsoUCeD8fTzLbuERDKqCpb5CBkQciijBcg-Qfjx0hjFBrj3aNYlGS8OuF7LozxBtzUIto3N4uKVSLRu0ABBQi6r5RR5KBmFQ-0MFwXV5Zid_do2FvYawWr2npc56KgSLQokT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662338" target="_blank">📅 19:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662336">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W23SsaIkUuSiyEkoI73mWVBvGPUNhdHK0byrOJAGysZx34KUhFhzJ1m1Vif4XXOF_jHDjGQkBshtkDwoAsZ38MruszpqfsxKEfMx8Yt3qVbVlvfywWt81CpFLYqCSc95tkOnyDIom-vsN2N7UQ1ZEDNe9PhsyADnCCyypi8xrPz4TeG7JaNNoxYcP3U_htWG0kX1sRgMKh2TO5fuZRP3fMzTdqQnxoVJGRwXNaF9QGUxZrrEpQDwrgEUE-552mv6whJiNuwRQUT146Pd0fC82wy6cgJTqEvKevb2eQQG_ytP0clOh4LOrWqBYGl5LujLpz0eaylgp94fstDWAJHusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منابع بانک صادرات ایران از مرز ۱۸۰۰ همت گذشت/ تحقق ۹۹ درصدی هدف منابع
🔹
منابع بانک صادرات ایران با حفظ شیب صعودی از مرز ۱۸۰۰ همت در سال جاری گذشت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662336" target="_blank">📅 19:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c88ee546.mp4?token=cO8ekIIcUfoV6PRBPeThB7Hqo3sXKnmzQ1KdL-7cnjpsE0UlJGYtCDvk_LH0jxnLbELaOzDxrAUdJAuI5-GcLKD_NSS9ZGyT5ciIlZS9vy3OvhXcdv4KLloSdLDOJgOzKfukztkJMOPsP_ptFDo5cEXCkGCk2DVb41FGGVg-lz4DQCQl3lb2NXAYtNvf7wi-BIo9-KBXWxKsC3J0zTphYPJYwa3JX8JR81sHWwSptVhpDnABJ9pv0g5Aq-3sZ5WcObPAoGRCNwBGMOGvGj7vNqYO0op_1XF57ROv5qD8Xhd44X5w9b6xkpOBgGXhs_amsfdLsxBTFljyz1Mq-81hwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c88ee546.mp4?token=cO8ekIIcUfoV6PRBPeThB7Hqo3sXKnmzQ1KdL-7cnjpsE0UlJGYtCDvk_LH0jxnLbELaOzDxrAUdJAuI5-GcLKD_NSS9ZGyT5ciIlZS9vy3OvhXcdv4KLloSdLDOJgOzKfukztkJMOPsP_ptFDo5cEXCkGCk2DVb41FGGVg-lz4DQCQl3lb2NXAYtNvf7wi-BIo9-KBXWxKsC3J0zTphYPJYwa3JX8JR81sHWwSptVhpDnABJ9pv0g5Aq-3sZ5WcObPAoGRCNwBGMOGvGj7vNqYO0op_1XF57ROv5qD8Xhd44X5w9b6xkpOBgGXhs_amsfdLsxBTFljyz1Mq-81hwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان خطاب به بازیکنان تیم ملی فوتبال ایران: دمتان‌گرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662332" target="_blank">📅 19:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662330">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjInGmwUvN41JZ5GsFsSmWNwXHG26tdVvUBr58cT2oqrqxU7vAr7eRA1DXIo_EYUGeFcaDZGbAQie_wBRsNfHD47JuSQ8xbGSXL94GCfFqpyGFJu8D1Qb7yaHjweTJW27vBpt2USEl-edSFJExmnH0tdwltfdoRBPo6CELZyn4MF-_SwyCUq18b9FpPUFrZ3-vQqrF29a4abiTqsfTyhiSvbZAgio5rzHG_Wcy3Wcr6TbAt97p8eNWJ7T9rCiLYhJSUYS7crwKYPriyoguY2QUrevscd4D5wHELMZnpG41NJOHJfFgl_mkb9hM3lDUla3tpojwLQXGX---lK22zwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین خلق موقعیت در تاریخ جام جهانی؛ لیونل مسی در صدر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662330" target="_blank">📅 19:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8DPDwnvVWRtBdpgCK8fAIGPVIqoCY-IROOHfjpNP8GfWuixkov_dCB758UA_OpiI838qK91OLN3fLPxobKJFntTuTbvPGp4GYiTdK3UwM_5Ir4A5Tw3IA_NbAr9VoqIlq3w2RilhY87t4wPMZJ1BOa9eknnALE5hAjxH6QHJnwJ8Q-LePyhLYiPXysso2Hj7Sj91UfNXH8q4ufAaAFKz9KxmNJ-YsKR0vLWO0PWPE5Md5zh8uNhOm_Rc7tVkxz_7ybQRTCYrsmyRue-XGuI4qrmTQOptW_ROVoq6EQX-CyFbkLlWRQxWu7Aj62-rfS6M3HUuX96UWgr74JTBQzASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نام گراد در میان برگزیدگان روز ملی اصناف
🔹
در مراسم روز ملی اصناف که امروز (اول تیر) با حضور مسعود پزشکیان، رئیس‌جمهور، سید محمد اتابک، وزیر صمت و جمعی از فعالان اقتصادی در سالن اجلاس سران برگزار شد، از چهره‌های برگزیده و تأثیرگذار حوزه‌های صنفی تقدیر شد.
🔹
در این مراسم، محسن اصفهانیان، بنیان‌گذار برند پوشاک «گراد» و رئیس انجمن برندهای پوشاک ایران، به‌عنوان یکی از چهره‌های برگزیده صنعت پوشاک کشور توسط رئیس جمهور مورد تقدیر قرار گرفت.
🔹
این تقدیر به پاس نقش‌آفرینی او در توسعه برندهای ایرانی، حمایت از تولید ملی، ارتقای استانداردهای صنعت پوشاک و تلاش برای هم‌افزایی میان فعالان این حوزه صورت گرفت.
🔹
برند «گراد» نیز طی سال‌های اخیر با تمرکز بر کیفیت، برندسازی حرفه‌ای و توسعه شبکه فروش، به یکی از برندهای شناخته‌شده و اثرگذار بازار پوشاک ایران تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662329" target="_blank">📅 19:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قالیباف عازم عمان شد
🔹
رئیس مجلس برای دیدار با سلطان عمان عازم مسقط، پایتخت این کشور شد.
🔹
سیدعباس عراقچی، وزیر امور خارجه، در این سفر او را همراهی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662328" target="_blank">📅 19:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آغاز مهلت ۶ روزه برای ایجاد یا ترمیم سوابق تحصیلی
وزارت آموزش و پرورش:
🔹
ثبت‌نام متقاضیان آزمون‌های نهایی جهت ایجاد یا ترمیم سوابق تحصیلی از ۲ تیرماه به مدت ۶ روز انجام خواهد شد.
🔹
داوطلبان می‌توانند برای انتخاب دروس به سامانه
my.sanjesh.org
مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662327" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c489455039.mp4?token=bIUQXPTVK-jaX5X5KpIupSXlFtKklUILqkRBziWqUV5t6GNN_5FvZD5tt_A8VEaEVyxpWDirVzcqw7N2ICx9qLmyBu62u_dJ9J3Yi354hJ2JJdgdm5wVbx9blr3U2Zwf4bWQKe5vYRyxi2Y9cjRU9HL91ofpIeVJUXa1uGf6rOHjlg-r8CrYCaHT0mGyEo-OT0xlpBJER6Uax2dLux5igPDX7sqbmlq8SF3d_UWeJXqDvcOBR62Jad6LQi-lawn3IUv25cdkMZJ9NslVHDYkFtbPZEYObEW3qyCr3G8oBfbE5dAn1KzcdeOUFaia4VZLkVivYqvELcy4_WDE_w5Sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c489455039.mp4?token=bIUQXPTVK-jaX5X5KpIupSXlFtKklUILqkRBziWqUV5t6GNN_5FvZD5tt_A8VEaEVyxpWDirVzcqw7N2ICx9qLmyBu62u_dJ9J3Yi354hJ2JJdgdm5wVbx9blr3U2Zwf4bWQKe5vYRyxi2Y9cjRU9HL91ofpIeVJUXa1uGf6rOHjlg-r8CrYCaHT0mGyEo-OT0xlpBJER6Uax2dLux5igPDX7sqbmlq8SF3d_UWeJXqDvcOBR62Jad6LQi-lawn3IUv25cdkMZJ9NslVHDYkFtbPZEYObEW3qyCr3G8oBfbE5dAn1KzcdeOUFaia4VZLkVivYqvELcy4_WDE_w5Sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
ایرانی باغیرت
🇮🇷
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662326" target="_blank">📅 19:06 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
