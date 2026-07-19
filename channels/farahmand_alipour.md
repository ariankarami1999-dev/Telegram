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
<img src="https://cdn4.telesco.pe/file/dki_9AGfKzqq05ffQ6hyBlKPwjQnZdnmOaaR6AHJt_Pb7kqUw4IALCfZVpLGbMqpdn1vTMJnDajQ7vnIbGbP9kP01RobGblvHC1jfR_pEk2xGsW0b_jC6btOLTZniT37jljGizM5L1dqRl6jUyinBSorGqTKhM5liv7fYdfpAReNq-6L5Tj81Aizyg-HGv6eVrUqlkxGRtpqpRdmagI2FU2ddA3oeF8gFNbfYcZNrhel8QaqhK0xQisb6D9Jf59G_ZG09Oz6aO1UWC7i-cGKrw0DA-iIOjAkQWCpebMGlJ_o5gjdteVgCHWpWNwWzTcbuI_jn6p2M86mpBWuMZJIaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 18:26:48</div>
<hr>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuBAHLtebmp0i3zJGSC5DvPZLoX0F73DMm9ioklhszLVkTkQTTk7Ib6Y8n0sW50riJ4q-AXm3cOCek1gjlGdlp6GsdkJg4NfLJURDqngcNydiTooRjcG2OvbApBBXj6_rv6BXOT4qv5ZrAG7nzgi-hjSi1Hzef8m-7sFMZElJIU_6_x6ZoIbRBEinOBXPdNi7H1q-4fGeVbLxjPe8-kYr17fX4uxSmgV4lLXgS030geLc4v1hkkxcFTRdn0yBfFJ4p-Mqm1W3Rm6JqMK85quCs-k5rzVomzbggdxg07eI_XnruxRUNW5_u7eDYBpwyMsNKX392qK6JTH2RFBhBsV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZiXrTQ7SbWFTYGt-ISF50z8dQUcWY13qDeYiPD2ddmdAS-WAnfIqxtm_f8K_z0BXWF0jU1K7dQU-_35j37WAlPoIBqn-I7xhBv2A2uFes3oWutiTahuNH7M-ou9bkSb-xbubaCy3faxnVzMsdMnXk7mVB_0AuEeM2C1IP_rvXKqaqSGZo__TIVSBFSH8dj9eUIomA37Xfm8TlS4wnjPzQWqp0Yvvy2jcEyXfIUZal3Qu5vklyVFOnGqDx22Q6V1D4xdtTVNWW4jZSGwqtxunPoP83AlHCSTxp85GpuM_P1VDnRJtXBUYfDMyHfE0HdsaNOFQ8yJSUx1_iwtmJotrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKJ4HzQmGUukaK2SOoS0nZMqIXq1oLpO7eY3wwGSmb-Cxtwukf22u7q0kMUzk5jzt-RAuWt_n8WZAILkqFSdSJMptQIsofkk1VV2t0b__g9shXjxrx502QVekeO2uMrEx62SR15iuXlEW4IiwL0Q7ZWkKc9Jq5Es_fvmTpmJpOzouQUOWfTsp03nImNmMdEjB6O09NSUa8uYYcJLUhtuzu_D8uDEF3XBqZNRHcf70OH7xLM_USA_Rr1KLirlNRSHX8if7bnad9Z3l_T7Gwom45j79DuTfCSTTwq_Iib6lW7kG4oIErYy6nuPgopZ8vWJqTrAyGSAWeRLkNTvmSQ8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Z7H6AxPLkyH08Qs4N309MhQcJ-cfZczl-6AnA7GxAz2qm_AGmdBIHTqAucXON4WqK4aACb3gabC9cmvlX2PnzjO2550JDIkKGrb3OlPNXyRkD2tqBdU5eXp9ON-jv8w3bM7ALNaGiJ3KIUK8X0vodjwcT1JCl7fPkG23hQBA2k0lATISQGAIhXLRQzNQVYnTF99k4uwg7Wt98RiHwGO6GMHydnNfgcKnWnYEuSVBuBQFKL7T1gkWxRWL2lkBaI0Ny9FwFJOynrWsSfiMK1tuWxODNhMK_0ajpYZu02CE32yiVS_Ftg4EVi3SCoUcI0cajLTH8rNRikZU6CJRL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTKEs0y4J_GsjRjOZY7AbzmvKlAy6uPOMFYRmW1lPTvJlgCJ3Jvtw9pqngLfwOXScTksFiSJPZc6imgv0vrD0BuM1beog2zL3YNHkDB9qpUPddpfqOB_R8fKKZWNb4YyCmWBufZdhWpS6-LmD90ypwcVjm-3X46AIMW8a043GLONKStysH-AnNhshpxb9rWSxafzpE3JhxBQqmvnf0-M4gKETMpweTmdnAi0TSRAROtLoHU7rCQMDKLE3mEZMnOUxoLABN2Qetls8jyBjaCim8G7CuYvJjBOX8HhQLjYkFVJhnWXqKBGpcEZg5MWFPUXBySPpB5dtQER_cz_Jdq7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9LuuOXkJJJ11GtRZ9pNp1zF4kdbQHHlGLDop6TDMS7y97g8_HSOOhVpyy1MsmJKocbNFTnDDXn7f5imiuMb4MoFiCm9Ei2UBSB_mkQLJNhf_f1d6eaA9K54shcZwqCCGjhyzl-4PASTS43QNJ1sUFZWe5GOKi3k1j2pDkJdRzzpgogM6eXbhla0b7rBsovEBbA0qS-FVF3rQw4Hjlb8iB075ez5448hzCZwDLqdYPFL3ubjs4UfA3PhOqxQCK8ImOjwEaraC3a7d-CXgRZU35UWxotshIt3xFvFatUgDx3U9nl8iwFMmkFvMem_3GJGR3Toetms_y7fB_m113PvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrNOt-CW2L5JLjxkZKkgl8EmF8BmWbcUU2ZKxDBKHXoXj5HG8dxXk4-6DSEvHjTjX0TSmxbfEeApMyrkSBOuiM_ZsdUqRQbl8STGj9VST-Em3rlUdt7ZfrAC3D6rzCF8O82XgMRsix1CcA1gc69Li53wxJdrvbpCUFy5_lvRNfmaYbRe336hXmbO43Ej_ZxY2N6mBmlsPGQg5-8AmiAGR11zPUNaGbw1FmnjvKjU77F9xNoBRgzikpZJZ9NiqLTeSpP1q3q0UelR9fbKjYmmLAwQZOTDaK3W9XfPBD4K2VrM3G4uSdacVqaeDbrTlq-RFPZlZqnNSm-7lLcROWs3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7ikFIj4_DwTz1Sr67qWh99Mrl5ZVjykvQ4yGS7KA1nONqdcHGtoE2-okydxf9y_h0rS3Yad_wkizIV-8zgDTLKrlxsjNMHNmhOGhkTZCVl0U1w_IamV_B6DRQHYLJlE9ESIxVpx-Q5cPMrPBk_uzNywry_g2r2J6Sw1ZSyre-xMQpO5c_egB8hQfcNpSzKY5_Ezo3IViUS-Cao4d8YKSIRBn0QwTf-hcZZaZYfmYlw1vkOj8FHq7UhdHl2aou2a49gLr_EpyFg6SM7NKGBO4ixhaHVim4ftrFxf2vYhNzLBffo4tUFrz0KkvYr9tSz2XrfdZDEh-Ie6k2jojc1_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQmaqj2znh910PgYFUickh9cSYSQSEKk23mODS4oc5Tw4j2OKjXfwzyviYK6GOE0cckAcVjHf82gZ2vUSedI7BrvOEP6OavDvOAGM1-5n3cZDpASYjZY3PbM2jTCX5ywKyxZpfF51n0nLOP1E6-g43HIlYsXlTbPTI_dp-5kyg8X47MiqvvJZEityvlJuntqjZVOK_TctEhxEfqJpobSj_oHzSo_Uw4wCaGZMH5_2PDRaGtlDvC8_zyyiSdUo20MYJ-lloMRGPxN4g82F6lbHcLK__-UlcM16h4-seVHVUP1IsvLwFLcRu8CoIF7ZXSTWRtmP8G6lETB0EIisSjiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvCFmUtvfuNtNGXmkAPvQhx7izSTjXeuHQWPlQm-A4TeAExBEzaw_97BUkrAASFsk_doeF0tVdhINOENh_Z_QHPDxQvE8w6vkBcCryi-UDogSN-LITUKFPK_aHqV-nfCW93sLiWb5Y932N6J0snW_glbGwG7saVi_VwdaRZhLdnZ2YD3pq_HG_c7Nly0C2kQ4fwC8hVC1-M9AfAGjP9h6h80tmzQ47vv2xiBpvkryi0bqAiCZDR8xyCupG6_hgpR9ECssza-tf40i4C6UMFMNYtDTFRvjl9rFlSXdQoiKseG4q-DrxYXGyaNfqz07VfGtUHPKosEaWkQRghf0xtCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMECqOwn2RG4FjbZg66sNlV03Q9xyxbeG6xPwRQ9JGzvENT207LFdFdTdnEzP70vhWsIeU59uAMx18SyaHZO8rPZnlhxJLkE62PZPVLPEoCWX1690LetexRhM9pCO3YW_Xt2SlzhGmGn4qNwu37h-BGaKqaoijmwhmldtDP7Rnsf-MYoWMT4kR9OCm40diAe94m4Jf92X7rTLASsgfnVsVQmSh2O-bXclHIm8e19m0ruGW_61iYM9PnGhgpoXjI_xYlB1-d2AlZtZDRhgsLqBDPfwUovyXKVrK6EaR9qL6BJGFj-HZ7oM77dhSC4wz_JUNasot61bjeDypLj3LUSOHY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMECqOwn2RG4FjbZg66sNlV03Q9xyxbeG6xPwRQ9JGzvENT207LFdFdTdnEzP70vhWsIeU59uAMx18SyaHZO8rPZnlhxJLkE62PZPVLPEoCWX1690LetexRhM9pCO3YW_Xt2SlzhGmGn4qNwu37h-BGaKqaoijmwhmldtDP7Rnsf-MYoWMT4kR9OCm40diAe94m4Jf92X7rTLASsgfnVsVQmSh2O-bXclHIm8e19m0ruGW_61iYM9PnGhgpoXjI_xYlB1-d2AlZtZDRhgsLqBDPfwUovyXKVrK6EaR9qL6BJGFj-HZ7oM77dhSC4wz_JUNasot61bjeDypLj3LUSOHY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=RjKu4zI5aqjUxk9jGNQdvCbhx-F3-oiDyNfBOcgKvc_h7wyT6Kqq8zxNr_V08Gkf9YKnLR8smDTy5dNWXIn9u6iZ3F00Af7UUEhx8aGgUa5H8HXX57E0imIeEZx6BHMFP_whIaWTzyyMmu5_3VK_QIH6bIMeZuTjUwcy-XheFvc122ms6df64VkwV6tuqO0qak6ra4stz7DhE6KgoupXjdtZcK0ixY4rlxAM44FR7AmeJ9ZaLzCTGmO7d77yuGU5gE44MmqoZYhN7V8OoUNH84HPL3pEdikheVFt9SellNo4HizKmz-GRdPFKsyJXVO17EKgIt5JaToTOQR_8Jm9KguPISBxRdzqH0Issuasa9IfeJh4rTO0OhLwpcDnC_UGAmVY_Zt8Y3tTQ-W_qiAFB_0-fQUxJIY9k8uoapiQYZTNk3Uw1H67FSTnevqTeKSgKVbObUFhVl_HoMRh3w_QAbMBbZV85Hy_Zbu3pTmJMFW21EyScBWVqXNj5zmOQ5n9eOHfXTMhUFf2BNmYbEWjddgFk2chThtkJLzydpAwYKZ-sgSTZ2sAGIGmZgpIJvWZG9rOznFC7n_cvZXJbgSPHDao08B1hS4HZXGovNhY_KfweZE-31uHc-qYuVUW7kn8s9M8UW9y06j0Gu75cmKmuzheTPWbtoHFfHbboYvRGds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=RjKu4zI5aqjUxk9jGNQdvCbhx-F3-oiDyNfBOcgKvc_h7wyT6Kqq8zxNr_V08Gkf9YKnLR8smDTy5dNWXIn9u6iZ3F00Af7UUEhx8aGgUa5H8HXX57E0imIeEZx6BHMFP_whIaWTzyyMmu5_3VK_QIH6bIMeZuTjUwcy-XheFvc122ms6df64VkwV6tuqO0qak6ra4stz7DhE6KgoupXjdtZcK0ixY4rlxAM44FR7AmeJ9ZaLzCTGmO7d77yuGU5gE44MmqoZYhN7V8OoUNH84HPL3pEdikheVFt9SellNo4HizKmz-GRdPFKsyJXVO17EKgIt5JaToTOQR_8Jm9KguPISBxRdzqH0Issuasa9IfeJh4rTO0OhLwpcDnC_UGAmVY_Zt8Y3tTQ-W_qiAFB_0-fQUxJIY9k8uoapiQYZTNk3Uw1H67FSTnevqTeKSgKVbObUFhVl_HoMRh3w_QAbMBbZV85Hy_Zbu3pTmJMFW21EyScBWVqXNj5zmOQ5n9eOHfXTMhUFf2BNmYbEWjddgFk2chThtkJLzydpAwYKZ-sgSTZ2sAGIGmZgpIJvWZG9rOznFC7n_cvZXJbgSPHDao08B1hS4HZXGovNhY_KfweZE-31uHc-qYuVUW7kn8s9M8UW9y06j0Gu75cmKmuzheTPWbtoHFfHbboYvRGds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS3iFX2mGqjUIgNV2KkdzREj4YGFYns07Hh8Gokub7v7qOpIoNWia8kdAnAYR3ODhhdkjPNXFHvF1QBoJYaJnzEP-ExD_QTz1ZJd8XefZpqk8UrCy9VXpIUNVLBJNQL7jFzv89i35-KspfG0BS358BmyxPLLHiOGkQegkeNS12fb3l0dqlTtJjjw-kCr-BHaWD_SIqn723oJlEs7fIQNWoYCPDzKEAUrb9tjrVztE9V2W5yMykd5xF5C_k0hKXuKRL7-ng3nrIoPhaskiHDpEL-4CNzUVRIhbNt4IL0v3SsXIswEqPg8i9hLIy9YDqOAcNW3TYY6cJzb9fDHUjaQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=iDBW4NAiWPOvh5Af6vsOegz4gdHmLeWkqoq2EGo8IY_7ogWCXtdoM9J0EgWukulGtl7qlIztstm1p5fzL9kznF9elA8D_XI4HeDzrTeJF9Q3wURxjGocilx-ocXbLOVuZUwteBTVTlcxGI1-gMe4nms-WkJ2jOjwvjI5WkmJu_CM1w3wIXg4lFE3VtSP-_ERCG2OJBuidfNue841mEib2nXUl3Tl-UQlA_uiOCsSxunoPTKtRVmZfnCotI8WcbyO_15Ph_dw7Zi-5vMcqDhhgY8Geq_sjZz2bV7WUKEfDgjc3kHR6eTr50MweP6UuUGUFkd8q93sVqfKJNWf-VZs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=iDBW4NAiWPOvh5Af6vsOegz4gdHmLeWkqoq2EGo8IY_7ogWCXtdoM9J0EgWukulGtl7qlIztstm1p5fzL9kznF9elA8D_XI4HeDzrTeJF9Q3wURxjGocilx-ocXbLOVuZUwteBTVTlcxGI1-gMe4nms-WkJ2jOjwvjI5WkmJu_CM1w3wIXg4lFE3VtSP-_ERCG2OJBuidfNue841mEib2nXUl3Tl-UQlA_uiOCsSxunoPTKtRVmZfnCotI8WcbyO_15Ph_dw7Zi-5vMcqDhhgY8Geq_sjZz2bV7WUKEfDgjc3kHR6eTr50MweP6UuUGUFkd8q93sVqfKJNWf-VZs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATS7l0bC8EtplUbd8Xzjw8ibrAuEIuSJosDtG7AFHUIffZSYUP7GZS1KoDqfNYE2A3GVtuOQhpJb3s-V9pNcoTTTLTRACmFWePOsHdl-4i5kZqiQq9jMUpAR7nxMUUQ8-5IPSR27n9zbZ8l8ZiS55XwycOLjGP_7fnO0GBe9knc8iIceA5Nx_vvNbBxmMGBdBTsSmoJVa7gQrZb2mybN7hmfdnDs-sgd0Sp5x6Qoh4hLSDSsvctne2sFcR55uIxj6ZHI8UCVPg79aeL3wrLStXewFyBUnol9HyWtzMvW-RQJW5DB3D5sG6l4XDxsvlz1wsaK3larcAvCIiWPIovt9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snv3LsVqpySOHc7kE6cchvx8w8r54MJKZfjrExVd_PagMHb1mNdZB94xDWgSi7yDmPrm1AWuGU3VDIxkkrujSlcus4HWPdBd9XHmozRAKCA8U5Rj9B7HAh4FoImSLuREFLOWSIQiHY2J-MmIB33Lnm-bjKL-TnTPvOk4OcyXlmk_lgHSWtYr6A4sQghk0U0dlPqegPDZSGj-RPA19SgN5qdRp9QN_DMyeufDTOFz9Ul94wStc0xCu1IM-fN265GGCsMbMblY-iweHjPOItooB-9qn60bZ7FoPk8h8bhNofZ--5EqgYU2GyM_t4KZRClIsSldwL7toytcoNSKVI28VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=X4roJU_Q2caXZKrWmzEF2C43tMaXxAE-gm0zgu21OtXkGkhjLCe_uydTQgQ39XXGCHfaHuLlDZFYjlnb2YmlPv79Z1EFIxkDCHDAMG1y6Z3jxJYqv5lKzqWkyXbAoZfAHmpFIHTSpdyPA-Rbj5QKd5_LLdC4pGts9hKwOBW9KZR0xwB_vlH-9WlzWHZguSAh5KtkbViN3JTP3zzzkvAIqb3tqL6Mc2lGrpFvqrJZDTA6fS_VXJo_6iKq6uhC3tlqvs7D-L1f1f5LZyn_ckXGh8WtsIRxJnSrh1MDMlth2cqonn9IWrbMaSgF-jtBHLnvO8GjS9_Nem66QvyKTEI4O7k4sqqQIGYLDikMdM64xbMapYqv6_OT2xNi6hQv1wBWp_tFdy15kE-mtZNtNMgfkH3WpKbeh6Yvmt20eITw0uUfLE4XP7fsv2JjnqhBuFTLXNKH9NRlsnA8Y1W8VoiS2U-05r3IT71Rm9aIm514vvUnkNPz_QAj9ntZQzXnEv3jYow4KOYnbBzJEcmQ8aaBw8VK5DDqOasFiZN3P-vrFtbZ2yyiGFuG-Ro9yhZt9QadXiDPR1_jX1OcqMIYotveokQR1Bq0g2xbRc6GstEJvIk3BiRwQSS9RoDgzOYjhUxvzrtykXIWOeZwzRrcdLr0Zt4l3fhyNRG7DxQQM8-D6U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=X4roJU_Q2caXZKrWmzEF2C43tMaXxAE-gm0zgu21OtXkGkhjLCe_uydTQgQ39XXGCHfaHuLlDZFYjlnb2YmlPv79Z1EFIxkDCHDAMG1y6Z3jxJYqv5lKzqWkyXbAoZfAHmpFIHTSpdyPA-Rbj5QKd5_LLdC4pGts9hKwOBW9KZR0xwB_vlH-9WlzWHZguSAh5KtkbViN3JTP3zzzkvAIqb3tqL6Mc2lGrpFvqrJZDTA6fS_VXJo_6iKq6uhC3tlqvs7D-L1f1f5LZyn_ckXGh8WtsIRxJnSrh1MDMlth2cqonn9IWrbMaSgF-jtBHLnvO8GjS9_Nem66QvyKTEI4O7k4sqqQIGYLDikMdM64xbMapYqv6_OT2xNi6hQv1wBWp_tFdy15kE-mtZNtNMgfkH3WpKbeh6Yvmt20eITw0uUfLE4XP7fsv2JjnqhBuFTLXNKH9NRlsnA8Y1W8VoiS2U-05r3IT71Rm9aIm514vvUnkNPz_QAj9ntZQzXnEv3jYow4KOYnbBzJEcmQ8aaBw8VK5DDqOasFiZN3P-vrFtbZ2yyiGFuG-Ro9yhZt9QadXiDPR1_jX1OcqMIYotveokQR1Bq0g2xbRc6GstEJvIk3BiRwQSS9RoDgzOYjhUxvzrtykXIWOeZwzRrcdLr0Zt4l3fhyNRG7DxQQM8-D6U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=QjsLo-SV8shHIrjUcjPrOgcr1GTwdeC_iEaiPgdXP-RL3uiG1ej02U7IG2-uf3Dixdbgt70gVUCAe_FjHRWTykq6cUBW6h0-0BazSPzcTBkHxDqYF6tM6xstw8RiQ7b4rG6BClWM2lSiC-_L7DxA4hJaom5gYY7DQUpJ8DE4nUfHY06WUn_wQziPlxf6KIgn2t6asalOB0NQf0pAeGM6CSRBAH7lw-mUt1EEUWwGToNQT9e9rR_3RV6e3Pvhqaai3OS84Vt5vVZBcZFLtmR9fWWqJzqRbktQwelJpySEJD3xPBDb4S1eY9qg_ZW65hBRxFVyMuPQVPNN-E6-eLvshEaQyh4S1i64VUijh9wCKdmNzMIjxwTdsI4ccW9cHoE5hmJ4sXBJepFUOtWUhVcR9usJUD-ekLMMRKyz7a2NZz1oKLt5HYHZe0WNx_dPZwz7lbSZNSInRFfvM1ZoTLBkABQpW3vg-FlkxFUIEw_i3I0Cqz8hKXsvkN7HqyUJNBmR67vJM9fVlqIh8Dxpgcr--wZaC0lcKOLehunWPdWe1hKvuM66eZvBzPWkRzEpq60tRclwwQo0Fddx1s9rh_xIGegoWGeykkMLZXanNRbKcUTDox2fPM4XiOO8fUNbVYeUJaKYw5sINgMIxtizzvcxbM2IjQ10onrESUjM_fdfFJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=QjsLo-SV8shHIrjUcjPrOgcr1GTwdeC_iEaiPgdXP-RL3uiG1ej02U7IG2-uf3Dixdbgt70gVUCAe_FjHRWTykq6cUBW6h0-0BazSPzcTBkHxDqYF6tM6xstw8RiQ7b4rG6BClWM2lSiC-_L7DxA4hJaom5gYY7DQUpJ8DE4nUfHY06WUn_wQziPlxf6KIgn2t6asalOB0NQf0pAeGM6CSRBAH7lw-mUt1EEUWwGToNQT9e9rR_3RV6e3Pvhqaai3OS84Vt5vVZBcZFLtmR9fWWqJzqRbktQwelJpySEJD3xPBDb4S1eY9qg_ZW65hBRxFVyMuPQVPNN-E6-eLvshEaQyh4S1i64VUijh9wCKdmNzMIjxwTdsI4ccW9cHoE5hmJ4sXBJepFUOtWUhVcR9usJUD-ekLMMRKyz7a2NZz1oKLt5HYHZe0WNx_dPZwz7lbSZNSInRFfvM1ZoTLBkABQpW3vg-FlkxFUIEw_i3I0Cqz8hKXsvkN7HqyUJNBmR67vJM9fVlqIh8Dxpgcr--wZaC0lcKOLehunWPdWe1hKvuM66eZvBzPWkRzEpq60tRclwwQo0Fddx1s9rh_xIGegoWGeykkMLZXanNRbKcUTDox2fPM4XiOO8fUNbVYeUJaKYw5sINgMIxtizzvcxbM2IjQ10onrESUjM_fdfFJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=eNoTkUlkmnkFOvDI4g_z9SNR42RmUl-NquYkERWrb0Cu08pcCZi1P8bW9Mf1h3Edepqr7S-q8TnLR3Q5HKZ8hhxobyI9hPuvvMXkL0YEn0Y39P3hBjPxECG-C9VRXeChs9Z1R70XpI-HMZjbNNyJbH3RldfT020cAMs1ZgqnMClNIQvTuTParvq51s3u_fDov_aBOf052rs_Zbf6HZICCSmRJXstzJ9c4o-wQFLyXlyjLkuDfIlOSsRMEm5l7GXG_JuDr4k4uSYALEFD_wPYZmQKg9wCK8X5j7VgbkfWYiGbhop531XzHqbQdbrELBva6Ot__YWa7I8gJUMsR7MlCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=eNoTkUlkmnkFOvDI4g_z9SNR42RmUl-NquYkERWrb0Cu08pcCZi1P8bW9Mf1h3Edepqr7S-q8TnLR3Q5HKZ8hhxobyI9hPuvvMXkL0YEn0Y39P3hBjPxECG-C9VRXeChs9Z1R70XpI-HMZjbNNyJbH3RldfT020cAMs1ZgqnMClNIQvTuTParvq51s3u_fDov_aBOf052rs_Zbf6HZICCSmRJXstzJ9c4o-wQFLyXlyjLkuDfIlOSsRMEm5l7GXG_JuDr4k4uSYALEFD_wPYZmQKg9wCK8X5j7VgbkfWYiGbhop531XzHqbQdbrELBva6Ot__YWa7I8gJUMsR7MlCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMGczMAiG1QNkHhhd35X9jVDmhO8Uy1QOjYGdM9QzdMhN-HkjmIbIoBx0c7Y7SaHHHHKe3r5CefgNAGb9kAibhBcrzkvxx6ZLPUqQ9bmeyfnNtNAx15jvCbn0Mk2-1VSf5uyoqvl60vp_tusuzVEiebil7sE3GZhjR2JuSdMFSi5Izvpq9rbq724m_7AAPj3U_q23KHWNb2dkjNaSQiLIpO-mxKTuybQvzW5oGxSNCxPLZKgopr26j-P_1ikkaLHGXZcdEjmDpjliB5LkjFdtwoqigWi-vn7dex3oiL5jzezEmTxFTvemkZ3ngELY2Tu9VSFaFk-dQezZiHA05Garw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=PckkyUhh4KU1SOBPz13IsTWgmycDSpRDEPZ4a-UsypRQFmlQ47FPtsk6wToerx6brmE65WfTmNBVNBzNYzX3D6fITNulZZPzpNkgYp5Gv-cUsgJ61RCL1uUbUCGlyrehlsPwlFUHSPJx1QmBYZybes3otAOVwo_mJoUYb8CFZ3QVaHezhp4Sk_80r80h2OiWXkuNIj5bT552aBlnAtDVjFsDpPXZ20O53C11yTDIoNbSXJpMWDrmeAWDKaNS1JncgcJdZqMdJ70AScTm335YmX5SQ5yVqoDAxqaT6yNcuT9O6kCmra1kZyKyLIIh7DxpDhOaukluwnlVugTe2oan_H1GqSszC33sMdzB-xTZvXXjQ2kRe7wPRlvOhvAGLzOg4u4HEFd9y_9Mbpsqdgkvf564XTrPvdSnQD8Ft0rjBrbVqLpuUQbJkW7OEV2QzRokPFjHD2d3DAbAOB_GaQX7m1N27cCWZcNKrJNjFhVTuxML5rvKYPDMolxzuBVvjoNik-MwyCKHlktNBjpO1KlZiyZAkeOFl1hAhyZWBs8YMPRl5R9Yi548WfvFGUmQee7Qs-ud0QXLtbLqeU1YlGyIPBLyhFYTa36UxW9t_V2txfYPmm4nC98yOc_gm18fV8hngRKwdh8urJNoVhBhaOh038Ha4uqBNtQF_VOYAv--uOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=PckkyUhh4KU1SOBPz13IsTWgmycDSpRDEPZ4a-UsypRQFmlQ47FPtsk6wToerx6brmE65WfTmNBVNBzNYzX3D6fITNulZZPzpNkgYp5Gv-cUsgJ61RCL1uUbUCGlyrehlsPwlFUHSPJx1QmBYZybes3otAOVwo_mJoUYb8CFZ3QVaHezhp4Sk_80r80h2OiWXkuNIj5bT552aBlnAtDVjFsDpPXZ20O53C11yTDIoNbSXJpMWDrmeAWDKaNS1JncgcJdZqMdJ70AScTm335YmX5SQ5yVqoDAxqaT6yNcuT9O6kCmra1kZyKyLIIh7DxpDhOaukluwnlVugTe2oan_H1GqSszC33sMdzB-xTZvXXjQ2kRe7wPRlvOhvAGLzOg4u4HEFd9y_9Mbpsqdgkvf564XTrPvdSnQD8Ft0rjBrbVqLpuUQbJkW7OEV2QzRokPFjHD2d3DAbAOB_GaQX7m1N27cCWZcNKrJNjFhVTuxML5rvKYPDMolxzuBVvjoNik-MwyCKHlktNBjpO1KlZiyZAkeOFl1hAhyZWBs8YMPRl5R9Yi548WfvFGUmQee7Qs-ud0QXLtbLqeU1YlGyIPBLyhFYTa36UxW9t_V2txfYPmm4nC98yOc_gm18fV8hngRKwdh8urJNoVhBhaOh038Ha4uqBNtQF_VOYAv--uOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=m5oOadJMZLOtivKEfRXHmm3q_TkFpq2IC-KR1nrt2H4dp6Fjv40XSS9O0u_wz5m6Cj0CEBkdNUIFgIGUpNlSBpkGyIx7omGqgY_T2y1Fjh-Haz3ZEBjBMtXc-5e4t4P6z0H44_8WYfxxykKh6X57IM9tCM-X8ARfNa1FQkjUJpK_KpFFgCjkpm6DGYu9GGlUSO_seSaN0SPPGHAcbYDsCL3Ltg5gasce6qxK6vkBmc-6BZqJrI1AfDF03dP9JXvKx6TgOKlgEZNOqqRJDolm3PMWd_9txe1L9LlisD42DPVIHoRZcVMy1ZF9yDuanXZmFt2MuMxmauIFK09S-uqZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=m5oOadJMZLOtivKEfRXHmm3q_TkFpq2IC-KR1nrt2H4dp6Fjv40XSS9O0u_wz5m6Cj0CEBkdNUIFgIGUpNlSBpkGyIx7omGqgY_T2y1Fjh-Haz3ZEBjBMtXc-5e4t4P6z0H44_8WYfxxykKh6X57IM9tCM-X8ARfNa1FQkjUJpK_KpFFgCjkpm6DGYu9GGlUSO_seSaN0SPPGHAcbYDsCL3Ltg5gasce6qxK6vkBmc-6BZqJrI1AfDF03dP9JXvKx6TgOKlgEZNOqqRJDolm3PMWd_9txe1L9LlisD42DPVIHoRZcVMy1ZF9yDuanXZmFt2MuMxmauIFK09S-uqZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZVEmFkFQ8fUXj3jFntNl9JlCmQ6IWGX_lkAcU7Uiawd-QmsNJwH3NUfabP1SHtK3JhIOrVx8D1roRa0VwhH5BykGruYzwHG3CjMBve9Obj4mp5sJKwfIupRxYRduLD0-iR1qnyS5A6R7y7evM3Tb6d9XniXfvNuwr94sc0Fu_S8mcHYHxMRGv3jGT9hioanqBycaTMi394wAcjIk3lRkUZ_qL3xkhzWsxXkwzrkFJksg9P2oKmAP2zUVnhoSQ6S6R0el2qhuSmf1hu834NXSP92e-OpIx1MA1POnz2WOLJ86GNTUVCd7ZPSfnF-pX3CTf4NHW7aBUrfnZ2viKvfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnD8a7WJs2OUND52Mb8U7jmTC6yYAzNkeYs6KRsBQKs7FycNh_BUQ4_oBU3lUD_uj1ifeBLc5yxkiFPS9XRSPWAlaViZRDvP1Aj-7zzEOzk2myDsWYWp7Ysw-2BnR6RYQbSb385F0AyYcLqznGAzWz1GD1F-q4pOpXyish5pNM2eVVfpW0JO8m9TuxYmEpi5Zweb8fHBb5L01L47hCOhGtXfRGE0XY2_0soTTSN1_QagaMpAlXG1CBfyeIz2Ir00kGUo6v9nd8kdtIMIbhmOn87PNXiHWxu6JrLlRvy3FqCHa8d8VCrayqVSSyPe5AwOYqbW8KnJQvuvNNrtJSmyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJHmRZh-z2ZhA_XCSV-bfxtUgsU3eh2Fk65o2ADgqV9oO7N2K9pxULN0mhxNIC_zWsKdyRzr37nBgBu8UqKwwP1pb4ieqxiQSV_vMWLaUQKkZQDd4guxdUJymMGWlcJyWi47Yp-x4vfaZjpJLohZgmEpBl2lqN6TDZ78W6MM3vR4pOCa0u5uQDtpfpaaJQf4Tze0kN2_Vvr3AjbQ-51jQv1zaJl6H2sKd7WZfTPw3YKYE9h9rCjgop0AIq8v0s7Pe2suZkYKWgxjUk-uJWV3c9RjdMDsdHy97SSh4i3AzIwEWEP7dQ-lu9NoMtGJN-QxZIBmNT1rBYJXxqvc61QWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JpggpHi-i4Utdi-Rcthe4Cd6PSvHb_L_XXJZpBH_fvccHdaRea4k65tE2-eUATWbwljXos5ocDpIT8-ShNRv42QSKR1ly_-fU9eGUFYF7pj832ApowGSONmR4NCuEB27sMLVgWeCCAywk8k50qG-7tMdNWVV6tElkAsFH2L12E2uAjFcyQlePK8D_xJvD88YjusSf8bJi3KVb1gdkJVcEKx43Z5uHCaJwCfdMK9S9CGFm1ckjb2f8SypZDkQgOoTB4MLtDZ4as9ehKNHZVer6VCIQLKSPqXXOnlXdeY27utXaGNJWKot9nGQMhuio5cV0_E5n7i4koCI-JWIn_vLqC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JpggpHi-i4Utdi-Rcthe4Cd6PSvHb_L_XXJZpBH_fvccHdaRea4k65tE2-eUATWbwljXos5ocDpIT8-ShNRv42QSKR1ly_-fU9eGUFYF7pj832ApowGSONmR4NCuEB27sMLVgWeCCAywk8k50qG-7tMdNWVV6tElkAsFH2L12E2uAjFcyQlePK8D_xJvD88YjusSf8bJi3KVb1gdkJVcEKx43Z5uHCaJwCfdMK9S9CGFm1ckjb2f8SypZDkQgOoTB4MLtDZ4as9ehKNHZVer6VCIQLKSPqXXOnlXdeY27utXaGNJWKot9nGQMhuio5cV0_E5n7i4koCI-JWIn_vLqC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEHJyd87AaGzXG9cq_pUjmg0GGvFMq1Q2GbaWWnSbKayLiVG5Y-MRWwGVq5Zp3geogYZ9O6oc-uVv2RQgfuwBUfRt_kwvJIw744UN_cCEeB87BcHv3GMVIDfcTcDNI-gV_xFc1-9fvUAkAkJ8bu2-7ArU7zqLbRX-30iQ9JtTXHNL4s4-F7-8_7ST2VB21jJbjjmbdH5BMcuWf98SDSmAvOxAXLvxGOHyD_Uyw8nHRR6v5raUdOUH6A4C07JTp_k6zmIT5ZbPeT78EkCQ1dgMaBJZtyqdy_kMQDiTc6q0lUu_PBltsZUIv3B9q9vuouGOLDzmSyQW_k0Tfb8jvZwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=puy2fGvi6j2KejF44199UKtZiX9lsH6QYjn3jpnRsq0QKyXuyCuhBxrcu-pY0oZzvsvaR6jqelCo2wbYlPD_VWFHakwM1VX8Q7m0DFWNWq5U4OHi1ALZj7knPJssZmouiu0B0KfY4vjiYxgbjSiCN1iA7HJWe4V31NDLjhFoVEm6p_qaRDWSouQ12HO5PhivaWJhrWM3857KfKxuVcfAU9oAEMAgbHD9d5lPBjMh-K-YqBy6vK1FNzxFF1OpumbmwQygbVtrjTFAZY5X3KWoCM0zHUVwhI8bZNTG2jLh3fh5kyp2jjSavN_tAS_VOMbhlbnI4XbnbwZxUMc0yNB-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=puy2fGvi6j2KejF44199UKtZiX9lsH6QYjn3jpnRsq0QKyXuyCuhBxrcu-pY0oZzvsvaR6jqelCo2wbYlPD_VWFHakwM1VX8Q7m0DFWNWq5U4OHi1ALZj7knPJssZmouiu0B0KfY4vjiYxgbjSiCN1iA7HJWe4V31NDLjhFoVEm6p_qaRDWSouQ12HO5PhivaWJhrWM3857KfKxuVcfAU9oAEMAgbHD9d5lPBjMh-K-YqBy6vK1FNzxFF1OpumbmwQygbVtrjTFAZY5X3KWoCM0zHUVwhI8bZNTG2jLh3fh5kyp2jjSavN_tAS_VOMbhlbnI4XbnbwZxUMc0yNB-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Rf7-FUNboOdEIQmsR52gxyBL-PO-KAldJuBHPMIDX_s8rJdSDsXdaIMP75q2jS5mIjg7zO2HVMr_w44qLtv1tTnIeK5ogxi8Kdlhi7FK2XVNRHBatPth4cns1_xZ6mJIAWysjIz0O5eAiSsa-qWTjJZWbp7FfR4Q-6ZVZQ1Z09wpz-RmOwjLROtWyIhsVJw1yVaswnDJfv5yFwFb09lyXSZYSBWgqKM2knBEMFrVobiVfrXFDjBGXYU8V5lic7PIn4Pd_IWZEhqNs8ZwJZ8NrPmOtCnsZqhHU6FBIrnnn-OyB-twlndi0qZZiZwedIJXSTPvrCyzB7KLQUq6OMI-RqXZLoFu3A72KNKd9L2VDmWu5O9Symnj0hohSnB_9r47fE8V7R9EaIE3P6-twRuIyMjF38DcnNK4EKMU3n601ShmcNcRlLEV816BQHlFZP9dxF6kUcrfRubQCCuhWTrQXYTxbELeH2Tl9V8_z_HrQzNjB4VVHW5s1xxY4fnvWRypUFqxbdsYYqTgB3mx5DAcWKdQLAivg8zYt-2EjzZLokKs6se6SIcNCWxAIEWRgi_3T-rlCLZTi6HpZyyjaa_efWwt1CJJSKLgg9kDN9uUXidzGl6L0SRMIy93ucxm9Hr2M69bWXJgZDdXmHM5spGPNg97BfKWd4DP1L6L1MBoZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Rf7-FUNboOdEIQmsR52gxyBL-PO-KAldJuBHPMIDX_s8rJdSDsXdaIMP75q2jS5mIjg7zO2HVMr_w44qLtv1tTnIeK5ogxi8Kdlhi7FK2XVNRHBatPth4cns1_xZ6mJIAWysjIz0O5eAiSsa-qWTjJZWbp7FfR4Q-6ZVZQ1Z09wpz-RmOwjLROtWyIhsVJw1yVaswnDJfv5yFwFb09lyXSZYSBWgqKM2knBEMFrVobiVfrXFDjBGXYU8V5lic7PIn4Pd_IWZEhqNs8ZwJZ8NrPmOtCnsZqhHU6FBIrnnn-OyB-twlndi0qZZiZwedIJXSTPvrCyzB7KLQUq6OMI-RqXZLoFu3A72KNKd9L2VDmWu5O9Symnj0hohSnB_9r47fE8V7R9EaIE3P6-twRuIyMjF38DcnNK4EKMU3n601ShmcNcRlLEV816BQHlFZP9dxF6kUcrfRubQCCuhWTrQXYTxbELeH2Tl9V8_z_HrQzNjB4VVHW5s1xxY4fnvWRypUFqxbdsYYqTgB3mx5DAcWKdQLAivg8zYt-2EjzZLokKs6se6SIcNCWxAIEWRgi_3T-rlCLZTi6HpZyyjaa_efWwt1CJJSKLgg9kDN9uUXidzGl6L0SRMIy93ucxm9Hr2M69bWXJgZDdXmHM5spGPNg97BfKWd4DP1L6L1MBoZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=gp813uLm5o8XLcXb6C6-Wl_rYpv348PEqcVOxnJ2T1DCAK6OEdIIt3crk6NYM42eOHu_Ncys2v7uNwfyxsP5KrGx0jQrfW6C3ciRzjgdoI_Apmpbco2-QpcgOXvZ8xH6podv9qgNh6Uo2D7_c2f7sLE9hBOTrzXVfeyUDJM9nf_t6yOLDc0rjK6-xpcmN5uU7Ol0Cnw4Np5binj-ARTFrjZQM5xSpJi7xNv2gkQt8gxulao_KpmWXTAQGRuDpkjXoCPprYOgJUIiF3v8zsHDgG6T2JRjXkGiemHPiwUwg44TnzGsV6HtWhV4ZKgYIa9K2jQwvEoQJN2zWaqKg5YtFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=gp813uLm5o8XLcXb6C6-Wl_rYpv348PEqcVOxnJ2T1DCAK6OEdIIt3crk6NYM42eOHu_Ncys2v7uNwfyxsP5KrGx0jQrfW6C3ciRzjgdoI_Apmpbco2-QpcgOXvZ8xH6podv9qgNh6Uo2D7_c2f7sLE9hBOTrzXVfeyUDJM9nf_t6yOLDc0rjK6-xpcmN5uU7Ol0Cnw4Np5binj-ARTFrjZQM5xSpJi7xNv2gkQt8gxulao_KpmWXTAQGRuDpkjXoCPprYOgJUIiF3v8zsHDgG6T2JRjXkGiemHPiwUwg44TnzGsV6HtWhV4ZKgYIa9K2jQwvEoQJN2zWaqKg5YtFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLhbEwd0q0uiEBfGeTtVV3dC4QpsLfDYbzdLzBn-0NUT1oJpWaz-pbSd0ghJFuRWDj03iMWkcqT5MYGZQiv-QAaeYxcMLNuWQD1AdsrVn9rcb6sCM5lLmEENuQesLB7mMZwNUQmh99V42p37W3BPHCFIKnvWuV2oV1HZDnXmfp0wtuKW3_gy9fwsS4l6zx3no4G2NSG1fiQDfnvPr-rxtDZ_96-M6TQ_B59s3s6c-TOCvCB2Xv47uKgutE6tggdMBVp4fGtECtMBroYoHMksTfueBmugFDfjMi8XwxJlXY7v7RJUuehat8uUa5iUgq8R5vYHeDcRJyhLH32bCLjjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=IVrLpiz_QZTycZFMW-eukzHSOp6dDnXZr4CpQrLv7XFy812BzkoSGxFOqlsuL1aumv0hPp0ygyfRBrioVaN8tr0k1-IRRedVMY43Sm0mnI4P-MgJfaePG_eJr0CcptcVDXCccXROsyDs7iCQpzOIgsLOM1yig_Yw9_OTmmExdNmz3lRP6yq2y2dSNmZ9zkCfVceI2mHgxA5xCr-ikkhYCk5OcGzNX4ncXrn6jbR1whV8rWQRc39fr-_WpE8qF68_ShFoO5IEAX-K9u3IQNXy_pzmZI0uFZU-7nrA2YoZwN5L0fBvyGXsp-UHZOvWqXzh6UCQzWbzjW1aN0bSiIGM_I6xYk-w08nMHm5HfyodhQ88K-4r0-T7yuQVcp2G3WnYlMCXlS9Wu7c709xpv2cICqddNKWZVkfa9VJMLpPv5TPFYIDhZdb89Xx7p5liwCNyqGihnKEnmr_mzwSGavLNYPE5YV4UjtniYr9_sm-dCRSyx19aEM7Ka7989TT9cXHU97GCwRaX6mZKIO9kMaxlmAVpKK4fDWMJKil-JjXkRTDBuuRHr7V6iqIN_W3rkeVAbBydrGE3rKwFqOOQNBHUSlJGQIwCEmYK3c7ErWlDbKjkN8QjQsbIAFZrNiVnxFjm79Fi_JwOBwolbvlwTMc5U5NjVIijkyfEzFggJAKYtPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=IVrLpiz_QZTycZFMW-eukzHSOp6dDnXZr4CpQrLv7XFy812BzkoSGxFOqlsuL1aumv0hPp0ygyfRBrioVaN8tr0k1-IRRedVMY43Sm0mnI4P-MgJfaePG_eJr0CcptcVDXCccXROsyDs7iCQpzOIgsLOM1yig_Yw9_OTmmExdNmz3lRP6yq2y2dSNmZ9zkCfVceI2mHgxA5xCr-ikkhYCk5OcGzNX4ncXrn6jbR1whV8rWQRc39fr-_WpE8qF68_ShFoO5IEAX-K9u3IQNXy_pzmZI0uFZU-7nrA2YoZwN5L0fBvyGXsp-UHZOvWqXzh6UCQzWbzjW1aN0bSiIGM_I6xYk-w08nMHm5HfyodhQ88K-4r0-T7yuQVcp2G3WnYlMCXlS9Wu7c709xpv2cICqddNKWZVkfa9VJMLpPv5TPFYIDhZdb89Xx7p5liwCNyqGihnKEnmr_mzwSGavLNYPE5YV4UjtniYr9_sm-dCRSyx19aEM7Ka7989TT9cXHU97GCwRaX6mZKIO9kMaxlmAVpKK4fDWMJKil-JjXkRTDBuuRHr7V6iqIN_W3rkeVAbBydrGE3rKwFqOOQNBHUSlJGQIwCEmYK3c7ErWlDbKjkN8QjQsbIAFZrNiVnxFjm79Fi_JwOBwolbvlwTMc5U5NjVIijkyfEzFggJAKYtPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZX8S4kohqZxYq9jnBm_8AuwS617Hjp68VR4Zk_NwU8W6OYbFhrWoyr0-ZIA3epgGJsJcWXHeuXaBvVejkCZDgWuT9CxLLQ_12xBHRohB1uAgdC_s1v8abBB9iUPRWi0hbmXbE2IU1jvLgk83AD2GjyWsnhLVcenhWFj9dPBwUu3hvr2la-q6Q17CvbL93jR-LgkYRCe-6zzXvO5Ypi890sLrvkU23T410KX6d2Zb_REdYmOhex21YZGVStxdmkfylb93EzCVgPodjTYIwvZ79KKR1Cso4xXuRv-bFFixR8xeRhnEOv1GN_nF57cN9G7I15nc4TD4qPgknMpJ3-JDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZX8S4kohqZxYq9jnBm_8AuwS617Hjp68VR4Zk_NwU8W6OYbFhrWoyr0-ZIA3epgGJsJcWXHeuXaBvVejkCZDgWuT9CxLLQ_12xBHRohB1uAgdC_s1v8abBB9iUPRWi0hbmXbE2IU1jvLgk83AD2GjyWsnhLVcenhWFj9dPBwUu3hvr2la-q6Q17CvbL93jR-LgkYRCe-6zzXvO5Ypi890sLrvkU23T410KX6d2Zb_REdYmOhex21YZGVStxdmkfylb93EzCVgPodjTYIwvZ79KKR1Cso4xXuRv-bFFixR8xeRhnEOv1GN_nF57cN9G7I15nc4TD4qPgknMpJ3-JDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=taHht2EWfx7BJ76tM0W5glWNB4yxxDN9cu8n-8lFpaWSV08iC6etHQYrzi_DV99WRqIIE2YLqfd7PSuimG2xiZ_HpXlH-Tom7UWwzv7iXxRQSBlo-_cQgqOcyZt9DqsqoXmEkB_76AEgDcBpD0P4eNB7rManH5koiuKUiW0COdvGqsrw87vJJbJvuqzc0kkWkapMSqPrfdgtp5y3R4SdpKoGJwPn7kzGoasm8lcn8heGk8dZIVAIfex1CGh1t6csYjJGse4ghj4wIaAdRRVD33hVVZWP0R1U5nTXVXtJf47ttOKDMtAJAJ8QhhHB-QYtWPt1eh62I3OAGETlm8jPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=taHht2EWfx7BJ76tM0W5glWNB4yxxDN9cu8n-8lFpaWSV08iC6etHQYrzi_DV99WRqIIE2YLqfd7PSuimG2xiZ_HpXlH-Tom7UWwzv7iXxRQSBlo-_cQgqOcyZt9DqsqoXmEkB_76AEgDcBpD0P4eNB7rManH5koiuKUiW0COdvGqsrw87vJJbJvuqzc0kkWkapMSqPrfdgtp5y3R4SdpKoGJwPn7kzGoasm8lcn8heGk8dZIVAIfex1CGh1t6csYjJGse4ghj4wIaAdRRVD33hVVZWP0R1U5nTXVXtJf47ttOKDMtAJAJ8QhhHB-QYtWPt1eh62I3OAGETlm8jPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFtuZfa6rKzDtOiNMW78OlFrE1LdY0S0IrHUz1JaB7yuTpxekgs-vi7RwJ_L22XcjdJgEhOZOCgp83e9_ysJy2Nz-MWVTRpyzaaLhHuJMKMWpGgVnGecEk4stFKxvAo4Ah8R_qiAauyH52TDLyfgWLCPrbcJdDE_9VhzqCrM4qSSeVEwwOfN3KnsyJiYYrqDuc2CfPLv-1XKaUViwUjwI_hmTCOLGfqpU8ocbxIynVN5SnzdgiZzdypW-EXa6qOrBKuedobPCjOCFLliO9Rq56O023hmE4Sm8a_xxhGYq7upYZYvi_hVWNquQa6vXRDdWc1lZYtTbi2IaLtykYisRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=sGWiXM7xtPf19JTZ0PLP7Zqkv6bI1l3SAjI6hER8kJhBLOVNk_sSi2h60vu3cJwpd0lD-Dvyul0yfmowCB434BUQ_xAZDfN1tlPUcTo_fqJ0KCPUagWiAachSPjmu8-ufHhW0LDz3t6scctrYOJyLUiUxGAZKuU4zfEAuE6blgy0ca0dX3N5YnaGcksAnQ_vu8pczsgpkly3JZY29E6bekRltebpDZQnnpZ4ImoOYDaQhP4BlQhlOi2a3c6SGxPzOMT9i6ulhNEKFpOG6z48cN1Ate4ihHRPY78ASwrT9GVokFRLiTkAEu14ZpqJ6oUXg1gdnn_6rLb8jtHhsJQCyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=sGWiXM7xtPf19JTZ0PLP7Zqkv6bI1l3SAjI6hER8kJhBLOVNk_sSi2h60vu3cJwpd0lD-Dvyul0yfmowCB434BUQ_xAZDfN1tlPUcTo_fqJ0KCPUagWiAachSPjmu8-ufHhW0LDz3t6scctrYOJyLUiUxGAZKuU4zfEAuE6blgy0ca0dX3N5YnaGcksAnQ_vu8pczsgpkly3JZY29E6bekRltebpDZQnnpZ4ImoOYDaQhP4BlQhlOi2a3c6SGxPzOMT9i6ulhNEKFpOG6z48cN1Ate4ihHRPY78ASwrT9GVokFRLiTkAEu14ZpqJ6oUXg1gdnn_6rLb8jtHhsJQCyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdS_5Rz5UQH31r_EHfx0syIEIrDlgPwZxxrP1vla5qKO2GeTe4vNuteyaT1tIy5KDDCRLIDdOewKpUq6Z1y_rilri9SIJZHi71-PU7H7LpHrKfsvXiAFYJBr16Jm4-33iK_xieFtKOtBte3FkFqD8BzfHFyU_RK7HaJ-hBnHcyDviwlZFDbj5y6YyjSLJNKWCjtb_GLaxtNbxPtatedWyakZg0RkAtYkeoWf4wWGFeZtBqsb2v6N2s-v0ByVzSD0gEKzmBqL7biJOApmJN9xYqMTXlb3oJh8UxQUzQBwn0EWyEL7SFHRk-UW5K0uebRQQamgSihX_JiTx-OfWifT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHjsqDp-Xz9ab_pA7ZjrKUKI5r3p3OHy0At4caa5hYxHSQ0kwVvR1pQBaYulH9gx3OVhk76iORcPeC9kn52GMYL-LuVj6SuX5bOh31yvzNi7PDj4gO5fL7TbxuZByMglY_TRAXZflyFbwxLTU8M4ZGC7mDrmjdFax1jplYiAric4VQY1_kHl5KWe9C2_SDnE39oK2PjdSsfpclDH571yhEHTWstUGcjQ6BFxgJzCfQF19Xz68AgX7hjiC2NUzdg5LJoSODR6VVs8OvKLOJLU4nMm41qIRY8JQ9mcZeOMSJOFFrEneObGaFwcp7QXDQM-_Qy3h4mL6bLEuBq2D--f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=JK5WtsWUMe9ys4WYztEIB4Zf1GYLK8SWJbAWtQIxpglrHjMXKc-NZ4mFpXDVHiChZQDqgy3omij0J4MdWn18oyLBfE4kKlNbdHsuy3PPd0XwIAti2wEsXsOThD27sYSwf-4I1lFBSTXYc9lysQjYDLE7O9BvGo2uoPWbi0F3xZHlRITZBy9jALQEfKKZnc_ZF7lW9O9omect4KKkc9rOuKrwGjZT6cgl_K28251SqtddKU3EgdQiZ1Ya3OhpRp3M2qQY_nSVpxMX5MzDinAODIRYr_N6m_LyqAIlrKy1eZuioR1joMxslFLIFPvbsFKeTyKe-KzXJHcrjpvJyq_gdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=JK5WtsWUMe9ys4WYztEIB4Zf1GYLK8SWJbAWtQIxpglrHjMXKc-NZ4mFpXDVHiChZQDqgy3omij0J4MdWn18oyLBfE4kKlNbdHsuy3PPd0XwIAti2wEsXsOThD27sYSwf-4I1lFBSTXYc9lysQjYDLE7O9BvGo2uoPWbi0F3xZHlRITZBy9jALQEfKKZnc_ZF7lW9O9omect4KKkc9rOuKrwGjZT6cgl_K28251SqtddKU3EgdQiZ1Ya3OhpRp3M2qQY_nSVpxMX5MzDinAODIRYr_N6m_LyqAIlrKy1eZuioR1joMxslFLIFPvbsFKeTyKe-KzXJHcrjpvJyq_gdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=UBT8IPJiH-6lXkgpaQwahG_nZF-_1djhHxfGVDf4FmL8J6UnBsFA7bXvb0iSWNyd6kjPYCBui29CW1dE9pM6Q1A3_EGQr49kXXbZU2U3x8VyGNY3lGdcoWLFlsxtHqZOoYCPsTh-HcvQ8j6WGzxn2O_N9MhVr2xezpxt-S8VTOUW6Fq1LZhX9fX6cMGEiLrsKZbAjKHEL2FyEKZ4WlVRX3Tueb9XATTouF_u57uzE8sBCPUgvRsAsmBugo5GaPLfq5TQyZSIlEEDknm5YW-0rg_cisOaDxYd8g8CAgzp2vBru2dFEfRIHH9R62HJpIevQvrRl8sJRoeeRAVpHUfJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=UBT8IPJiH-6lXkgpaQwahG_nZF-_1djhHxfGVDf4FmL8J6UnBsFA7bXvb0iSWNyd6kjPYCBui29CW1dE9pM6Q1A3_EGQr49kXXbZU2U3x8VyGNY3lGdcoWLFlsxtHqZOoYCPsTh-HcvQ8j6WGzxn2O_N9MhVr2xezpxt-S8VTOUW6Fq1LZhX9fX6cMGEiLrsKZbAjKHEL2FyEKZ4WlVRX3Tueb9XATTouF_u57uzE8sBCPUgvRsAsmBugo5GaPLfq5TQyZSIlEEDknm5YW-0rg_cisOaDxYd8g8CAgzp2vBru2dFEfRIHH9R62HJpIevQvrRl8sJRoeeRAVpHUfJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4kyzOPHkDtTf9GO1ZImQwImQ6hp1L-RFgRfLErdbake9jvfRga7gZFQjbRq9sJpWwttN6JU6UHeyqH1WR2VZz7caf-pcKOkPFnWYui2SUzL5ItXaIbTibqR7QKbnkLG5AHTjE7tj8Br3elQRxHWBuKbpRAKtujSRtBRWPHpVoxesg7irmGJz3ukbzgO-N1FG3zODRDHlSXJdyGnXUHE9HhaRcqSmiq4UZKPBuTpRpASkuT_TdrRYMfuceDevydgLIj3ZY9trbPxLlsR9-OIzkTfkcmMVrQKqoMaVwkA_pQPsL1ziJfzv47DdvOM1vD5Q9J0q3voBGr7ycK7Bpb0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-xSsD9tzZe0ClxZHEmFJHQw2Q2-BXyMk-nnOI3iu2amQPwh7bOdc797kXax0NoqRidbVrCF3Fk8isbT09kHHTHaS2Bf_m-7PFhrc8IVDqRrHM_gXEh--13c8zG8Nh82zKuJI0XU0ubZUxIitHC8FICmdT4wzfSVTeVPuozY9ix_aVKRSv11Y5-BG02P1s1A787BjBMBHW6sTdKx1KeFpKHyBQWxB3j_m_g3d97_zaR7lHHz6CSaq3kz8KEber5SIEpoqG82NopbssiF5aoFzRcR00opSXq5UOrqegmfFkVA4tcqIFWkFOWt7WxHRA_IhXMoX9VFvN3X5M_mGsghdAoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-xSsD9tzZe0ClxZHEmFJHQw2Q2-BXyMk-nnOI3iu2amQPwh7bOdc797kXax0NoqRidbVrCF3Fk8isbT09kHHTHaS2Bf_m-7PFhrc8IVDqRrHM_gXEh--13c8zG8Nh82zKuJI0XU0ubZUxIitHC8FICmdT4wzfSVTeVPuozY9ix_aVKRSv11Y5-BG02P1s1A787BjBMBHW6sTdKx1KeFpKHyBQWxB3j_m_g3d97_zaR7lHHz6CSaq3kz8KEber5SIEpoqG82NopbssiF5aoFzRcR00opSXq5UOrqegmfFkVA4tcqIFWkFOWt7WxHRA_IhXMoX9VFvN3X5M_mGsghdAoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=REj0_Kxi9HclAlct5fn6tft0MeP5dsZJ4pkgj5xMBik-lzCHcuIKMFhoFcW38hr55e0hjtFDPqXdNvPrzyQwy2bnj9f9XyEcWq00wJ2frIejJvZMIWmoeeM2vzvIuyYLpo_LLW9KpjPu4J2GFa_WNkwd0H4VwcrwkRJ7am1DmlvvPAhZs9CrwdMMJB4YjbJZTSGLMwdQrq576OBaZ5-FcOB4nPLP9WHlZn399bSBsRO-jxNN0nCYeEHBmGczqAhx_ve1Stpchc63tkCsGhJR4r4TosCkRhfM9ywtYpk7cpy4CQbumHEpBEtGt9BoQ3eoq28_jyw9uLtBk4jqSU9Ihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=REj0_Kxi9HclAlct5fn6tft0MeP5dsZJ4pkgj5xMBik-lzCHcuIKMFhoFcW38hr55e0hjtFDPqXdNvPrzyQwy2bnj9f9XyEcWq00wJ2frIejJvZMIWmoeeM2vzvIuyYLpo_LLW9KpjPu4J2GFa_WNkwd0H4VwcrwkRJ7am1DmlvvPAhZs9CrwdMMJB4YjbJZTSGLMwdQrq576OBaZ5-FcOB4nPLP9WHlZn399bSBsRO-jxNN0nCYeEHBmGczqAhx_ve1Stpchc63tkCsGhJR4r4TosCkRhfM9ywtYpk7cpy4CQbumHEpBEtGt9BoQ3eoq28_jyw9uLtBk4jqSU9Ihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=cMLNGIZ-Ttbrvi_MWKLDj-WJRxRIzxXpGquRr4g3yp6hfOvl8zNqBRImSgvUQm9tMoODcUJ4o8xFjD--YYeUkLw5xPVLaIm27W_sWlb_vra617Yng--nGqS8nWOdV1PTzBPecb7ejzpo7YuX8Z3300u8UWnqNI-icwyhUP1ULNhm6cN7a34BxjEM45bYm0paOkDlVbaJ8Yy4g58kP0-yDn6Wvare0HWmOM1DaDrR0uQy1CGZAnJCbAbpmvZXeh62mCBAwiVQ8iIDnmfXUeXsPvZuVFIct5uaccZYGPEJnsBz2ZrMwF29oUGvoDkKN94Mq0stGLlEGKKp4yMIqLKfgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=cMLNGIZ-Ttbrvi_MWKLDj-WJRxRIzxXpGquRr4g3yp6hfOvl8zNqBRImSgvUQm9tMoODcUJ4o8xFjD--YYeUkLw5xPVLaIm27W_sWlb_vra617Yng--nGqS8nWOdV1PTzBPecb7ejzpo7YuX8Z3300u8UWnqNI-icwyhUP1ULNhm6cN7a34BxjEM45bYm0paOkDlVbaJ8Yy4g58kP0-yDn6Wvare0HWmOM1DaDrR0uQy1CGZAnJCbAbpmvZXeh62mCBAwiVQ8iIDnmfXUeXsPvZuVFIct5uaccZYGPEJnsBz2ZrMwF29oUGvoDkKN94Mq0stGLlEGKKp4yMIqLKfgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdq5vu-V0H3CEOtdzXqtBeY1ST3QXILwlejvtcs4Z9U6iIbEpsoNkImSABtxtND-p42qGkTqtyPo631JxVFMy6GcvN0FjuxZqobixHHULufRJGs-vejam1iYw2nsodssqXWRV22vr11LQFt12BNMx3zVtX-0cZGk0P7IVOjmaG4-1EgxHY1EfMNPJCulRabNJpaZav3NHP9qckhXjGzbfZsgqR7qKI-YjjAy02vwNzhGMA0dW4c2THjabFKFZnr9y9y0c85CAOJ0Beff2N9lHGksFPCnZ_4lqZidHEFKYfWI0FM-zeaiWh3y-MMGIljQatuWGzq5sQWJTS06qhttvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=mvKy_GOP-SWRwzNt3E3a_TsjZZ1Vavi8_o_tOwNdpmrHmzA7zpCKiEEGeuwiWdvl6FpQL0mN9lu1RrQqaP_qFiTg-XYQQKvEX1e-Kc8XtQOkZpn3cyR9OQpro9pxgHL5smyeeuhcwrfVEKsbZnqALIooEDR_GjufRbBQTv_eKU3b6b6EuA_Qf4O-CEM4advdRgtplmYHSWi5aG92Gj5YIBH0jFxm-U855acIhWtgV0dlwZrAXvd7P4lbuomHnuvAznicMn6QrqTySvySmjKM_if4EJBia7mkXlJy7ycdKDeTdCbR9Sizqyce25TdaKVQgWWxuk1SpUnBlpALrQYkfTIJUpyVN5HKQF3TbEz2ZTYch4DI01BKX6F88-W-BMSUsjonCf0yzvpbWYktobnXzv2vr3-0eVkIIMR7joDxu-gj8vsCX7jXfiVzimVs0gxOZPwoZi-jF-uyiH5-qCyfauUwtmpbNIZTEsumFtkTF-37E-ivJn_wIe5tMRl-fQi9ydX8-3GJVCzo7l35ILKdajTQOydv5YYUfp9hXFMoaq1UMepplFBHz4uvty7f_1L6ImgjdJVucWve9t73cBWC1QMTEJt_htnUijqkqoAXiPDl9RBPBWK8NXwJvfvzEwHFUP9sZtQLUA6ZVkiP-16hW0B4UFWP6GnQnMfQRvdAYZc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=mvKy_GOP-SWRwzNt3E3a_TsjZZ1Vavi8_o_tOwNdpmrHmzA7zpCKiEEGeuwiWdvl6FpQL0mN9lu1RrQqaP_qFiTg-XYQQKvEX1e-Kc8XtQOkZpn3cyR9OQpro9pxgHL5smyeeuhcwrfVEKsbZnqALIooEDR_GjufRbBQTv_eKU3b6b6EuA_Qf4O-CEM4advdRgtplmYHSWi5aG92Gj5YIBH0jFxm-U855acIhWtgV0dlwZrAXvd7P4lbuomHnuvAznicMn6QrqTySvySmjKM_if4EJBia7mkXlJy7ycdKDeTdCbR9Sizqyce25TdaKVQgWWxuk1SpUnBlpALrQYkfTIJUpyVN5HKQF3TbEz2ZTYch4DI01BKX6F88-W-BMSUsjonCf0yzvpbWYktobnXzv2vr3-0eVkIIMR7joDxu-gj8vsCX7jXfiVzimVs0gxOZPwoZi-jF-uyiH5-qCyfauUwtmpbNIZTEsumFtkTF-37E-ivJn_wIe5tMRl-fQi9ydX8-3GJVCzo7l35ILKdajTQOydv5YYUfp9hXFMoaq1UMepplFBHz4uvty7f_1L6ImgjdJVucWve9t73cBWC1QMTEJt_htnUijqkqoAXiPDl9RBPBWK8NXwJvfvzEwHFUP9sZtQLUA6ZVkiP-16hW0B4UFWP6GnQnMfQRvdAYZc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
