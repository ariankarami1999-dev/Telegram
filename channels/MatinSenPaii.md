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
<img src="https://cdn1.telesco.pe/file/piKRg-JRumOKG9OdjfaNLN_0Mzpn0VKkXqks6MnanZWjkhudmz4oNsdEaiX1kqIpKxXL_vNnIxevdRvZbdjQltdBhGjPuBYCXSZobk7HAf_PXIrHZjPqWbz7BxfdEH2txhXmiWFk7rZr9GM-tFuElUZ3QVvpX7isM2BWXSq18Yh28n7ivvxjyALakuYqK1FdDmuVZ5sPSmACErAx8CxxApMLaMRSLFgtA3MHZiyKSr9uyTG2_lw4LHzNKPwaE0FEprEbIDYvGoyaUAdkYXcxp7ullGsDpWAlvyVVYi4mi9RAAp6emqq93d2Mj88Wirsoi9iWZtfSVE7RNim2jKhhTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gI-sMrOCtRWr11sRwaWAQPNMoUWUQ9ofBIOCUF6HIO-hOK6kuk2hnDWkbGweCG9oGfv6qs9Zvl0l6jJVuXU2ut3ZAONl-hNhfrWlNTN_hW632eNmLlyFskyInfvj_KTTDJHAFvx21_WvO3-LGiP7cCBa664-UXgigEQJQeg718TbcBPACPcVmx5Hc8rszjuN9wl4BwDCwi0Z1JZ28mgjuXcSa-VJ2p7_dDAf9Z-0c8xjOE8Y8ot-G20IuZBdU1-BIAvswpu77XBhTdzI4-aHRedDgj9LLiatJb-RYF7u_1kbHPFG9TVEu18zOnCdqIZdyasKVnmUt9uUM-XMo7Uo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G6IDtRUM7F6lKIYjDiG2dozUuGdL6P4jS02kqw7-iMTwsPg1GlmTSwsx-3h9piG26THvWuRU2DdWZhYx_TnzLhuiFJ44I5jqXawDIsvpF4-ZkPtLJRIz6HkJQRLP58soZZvfOgG8Rvoztx0wg3_Jpt6HerJh07WqdwCvk5iVpqGcC7HcpfgNoZu14jAYLSiLlp2WRdu_pMq9a6QC7k8pK0pnDUvvEpNkerTh6wm1UnFTfmGOwatpHJL8pq0F_Uw_yjxL3eiR4k7hF_4u_1QCemNvne8C7KkWBtGvUFmaIbS7oOQJY-Po3NE0RrPLOEdPTxfu6ZWxc-Nj43zrJfN8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bM190OSB6SiusTV-f2kLFZvHWA6RTphgLFgvRhLzqgQ2ac0skie5MnIjmWTEcnUJ6JUDY60NCdLBYF0w-9l6KnOH5TTSRcVuTkA1QtVcxLRLC5rXNJwt49lXVDM5esvyT4LsYGwnRDxXeBTG7eNSZmiRc49tGeHYKSKvh9af0t-oqHP7H3u6fhrmKpN32luUoRE7T2o-omgnhcqzzq_x2V65gYkFR3Oy5duQrZrO-y5QDxiLZrPSzU75lc03bdPMe53luApit-qZtLWXvBr4xzLo6YIBKnCNc1FVVfFXDiULV298NBBlPP8iURvt8tco0x0sdRIpHRa93JMr2L9H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=vnNuHpQL9SjQJjFsFNkMjTXxr6EK5JkWhMsSnAdchKjXR006MHS2G7pG1fYin4xTeX6izvtFHD9FgFO7ONSIYrT_iYj1CKBrhTW_wkkBVOo6n_Z_VLPwsZlVUs5ZNHP3dx74aL_3MToI7d-kQuWPXrRnHYNxOHvzLLrqSiJmpXk_z-YC354u-XOGY4WYf-RqlMg9jG7d5pLn9u3GmboiN5UGGkcgPXUQviNcXTUZGcU-kKdyS_sIJwpaGw_bDku355_a3TCF3Qt9lyDlE8Dr_gx68xh0CUNEkmZbQYVZJsQryVWO_sJAT-5G4oxDXTgUCz6tIs7Mm_UifPCl9QsNAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=vnNuHpQL9SjQJjFsFNkMjTXxr6EK5JkWhMsSnAdchKjXR006MHS2G7pG1fYin4xTeX6izvtFHD9FgFO7ONSIYrT_iYj1CKBrhTW_wkkBVOo6n_Z_VLPwsZlVUs5ZNHP3dx74aL_3MToI7d-kQuWPXrRnHYNxOHvzLLrqSiJmpXk_z-YC354u-XOGY4WYf-RqlMg9jG7d5pLn9u3GmboiN5UGGkcgPXUQviNcXTUZGcU-kKdyS_sIJwpaGw_bDku355_a3TCF3Qt9lyDlE8Dr_gx68xh0CUNEkmZbQYVZJsQryVWO_sJAT-5G4oxDXTgUCz6tIs7Mm_UifPCl9QsNAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEcCMIdjNtzYDoVyBBdOUhKvCwu_zyFUObysxvmUifK9L1fYEkqEREWL1L2QTdAeGhyGOUnFTym2kLkfIT-3TpB6sXeuVr42xwmjMMzN_TO_rGTX9j52RkTFcr5e9G6mgttIjoqI0yKNZ_oTXqPO2Qw6Ma20PMPBJSzTlkAk0_zNjcH2eqfecFcQj4Zi1GNFh-9c1Wwt3N6MsE7s5Fq-DDI3i6tskjDXA_H4Sy1zkno9RvH1JL803yfbCYb0rq3prYeON1zVBwSpe_8uFOZcVad3ZOqWKVBjbCFLVEdRomFKl3tK7_q-uU7jEEysl5_PNqlqpAldVxjpCbbzxdI7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=IvJf8gOuDYZ_fc4-lMlrfTcnhuiuFSshKolHiwOrys_-SXW9MZ20FDrC6tdq71zNKufQrmqbop5LZUaCoXtrOQPeZAWH5sDOxwt_o97xvDyJ-6f5DtkKM3En_iCK-IZr_zB0hjTqUg7oeJwsb4ds1TiNcJlWo_c1NIAG8374KDwD1ea3JkuS6CHSzBjL6r1Yg6bx5pzcnkA8JnYwBIQRIziU7TbXO5j-5wVZ6mLtWeY2jObQTyc4VN55q5elhPrpjY9bLM_84Qj9BmrH5L8zf2EMDML0YjMdcYEJX1WdSelibfPnXW0hOtI_P-PcXQ7BxwfLfDbZb4fJCGxuXHhC2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=IvJf8gOuDYZ_fc4-lMlrfTcnhuiuFSshKolHiwOrys_-SXW9MZ20FDrC6tdq71zNKufQrmqbop5LZUaCoXtrOQPeZAWH5sDOxwt_o97xvDyJ-6f5DtkKM3En_iCK-IZr_zB0hjTqUg7oeJwsb4ds1TiNcJlWo_c1NIAG8374KDwD1ea3JkuS6CHSzBjL6r1Yg6bx5pzcnkA8JnYwBIQRIziU7TbXO5j-5wVZ6mLtWeY2jObQTyc4VN55q5elhPrpjY9bLM_84Qj9BmrH5L8zf2EMDML0YjMdcYEJX1WdSelibfPnXW0hOtI_P-PcXQ7BxwfLfDbZb4fJCGxuXHhC2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=emt5NItz0B5J2e7RT5qGLcyPxxBytWiW9sqWSmD7F-V4aUnxQjBirROimwUh49QxEJsAr048YHGTftPFTQNC1h-fVKs-fkysel781lrmx-uqBS_-J3Bas1Kn_fM-mVghM2_ElMlXRR1wCx_eP2rE957nss18FM9vvKUQn6yra-71exPIVjk1iBOScTRakuN5_1jBZDxCSmIKjSXr_jw2RHAYqdJaoTz-NVE8R7qGpyuzBnZlXQSTBttlkGcfZz7xgdrWy7f1ADXC_wg-YXK4tq5NdGb_wXo7PZUgkfnGOQ2CQf_uSXE_A8HrwomJqK_TjdoTYRV15mIJncAHWceePg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=emt5NItz0B5J2e7RT5qGLcyPxxBytWiW9sqWSmD7F-V4aUnxQjBirROimwUh49QxEJsAr048YHGTftPFTQNC1h-fVKs-fkysel781lrmx-uqBS_-J3Bas1Kn_fM-mVghM2_ElMlXRR1wCx_eP2rE957nss18FM9vvKUQn6yra-71exPIVjk1iBOScTRakuN5_1jBZDxCSmIKjSXr_jw2RHAYqdJaoTz-NVE8R7qGpyuzBnZlXQSTBttlkGcfZz7xgdrWy7f1ADXC_wg-YXK4tq5NdGb_wXo7PZUgkfnGOQ2CQf_uSXE_A8HrwomJqK_TjdoTYRV15mIJncAHWceePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uw9o09v-oSVNKdp-moSyyQEdimMbq5i31v_58Tb8L3JvVQE8EIvRbc8y0xUiMEMzhbcgdrBKnEuYFFBjkPIZlLA_TS2p8AHYQIk9oy4MDUJTtY8xFRguY2DgLKfmQ9rdmdgt_Mlx21F462a3YO8gI-QO2JUSzusV9MGOaDb1MW-FvTJUghrZ1tt7-MLCAygDOLRVdbILWAa8H1f7x-y7c5ZE5JWsbwMND8ZA256cZOvyH7wXaDP9YmD8ZdurBy0edZIDTWustkyqsQS7g1FNCultjDjfgT9JLkVg81KWjBJ6RgsbVJZ9pdlFYR0UB1OHJe_YirgoWZ3x6Q1EFUheuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQQKFR9zIq_O4_AtdB0ktIFPPlGD2td81x_mQeXtXuWPynB8bmQe-tlH2iu8Kjc2eWzuO10ZMLuL4-VBiHHZ-6xnTYtdbJ31gR2Iqb84lPvhd2hST7hyTsiV2HPBbbvWg0q7K12YRNoY4LxEuSuWngfPhF30J43dxCIVWjv6AIjpdMJWyIBYyuiTIachNlFUzwrXW2L3YCkV7bm57XCzbucFChbxc9MDnsgDS77Z_1hoO5rZ3-xX83wNHiGq3KqcCFG_-yn-1MdeHsv1tvsHStdqc9FCpS0o3wnNE0BpuBceMrmSvip6NYLkeeJ9QCW0bLmr63MaQZUKf3mVURyA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQzITiwUu2Re1Jif1d1Ej-xsGOMsHJGW8TASmAemJaihGR32vtgVnK5-RdiVTuNEdHI61A3hI8vM90PA8-3pV4fpvvS13nW_WnQeJQc8My55fUYk_yTT_TsDiaF59J1rZ_ERidLnN5_-y2oEX29pB2nJio3VunH9c4QeLfCEmMJVCwjTsMS-DlqrAuPfwR7jvIJ8CE-zij8q5AoDMPRpQyap_5mtAY289hvfO9FjcoyzfXVvFzwzpWiXlOQfy2qx5yroyuEAk0TYLg6YumYLeoUdIgAXhJeg2jLyFx3VrKxN0W21OL8t6JNBBbzBtFI8abEvugjxTGFCK9KrICI6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifotAPyI2NRwI7KU8VJV-Beootx2y0YyLKTBiv2NT7H49n4odGqBE4LIaTPrNTXtW7Z9UIXQIDkEIfBVlT0JvLaCvxQW5ecogZd0XUo7e3O5s7ucCK5ET5eHOvywGh92BnTmpveoO6zgHrEoqBPRLJzhe7T75Eq8vLdc2PjWguAC9Hh9NX6Q5fgFj2F1rHUN_l9nLL6W7k5KI2FWe2ZAidjLD5CmkZeWih3RC-UI2UjUexHPTyeBP1nBB0lYcQ3tUmKRup59TAR9Ol4Xkafb2bxI-S2sFd7mrtYBqLxdwA6OPsmr0eBRaw_AA4eSXVazeggeTp67nhPHGgpnrEMX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dKcCwOONO-5pOEiRydVjfwHn8oFQG8YTsMXID_mqV85mSKWUBDwL2lfuhCP5a8OBt_Yu29zpNsSScmd7pF4OmLbYye5z6ko0fT-aegn2cTGGedqArOh8doJlfASzG8faGWiEfXrqKlH-syM2LuztV3TNdMl0piDM7FVgbJ4D0DUWkxFvWkkRo9VLtq-W5_AdetApGbdaF7w1Faj4t2BLfENJLBI8DluEZ294sXfsrD0oBfDXPei5jmdVH0OwGefQLYAZaBbGOWtHcc_DfixEj8c_JFFr2nE9p4nD6olR3oy-LzrSeMKhHmJMpy6T3BI4HePKrYnfa3vJC7WjXHrFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXO9k7gwh5F5rve-msUdpT5CvTi4YR7g4i8cXernfphq5HcDljQ3bX5YCFSGiPFa6_EqYue7VNYB3y86-9kNa1RK8DeX5OLbVT_aa01OA908kbYwT-Xim_o_jsyfWE54Fv0ANUYlngtA8ciwRLaxUsQVVAUvp4cm_htVulXFGd1rdNqWcg1W1_a_cAA9QjsKbDLKmenJF_2JY3k-dwyXx5lhMa0OjsLz1ofAxk1ynmrFyxKe-bmoa7IPWrXWZ5Txi0KYylvpSjGg4dy4CXi_1MoE2QgrVAbjIL6f3tq6TVmiKswl02BnnVc9OzGmff7eVPexNdlBwe72j_nUWrH68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=NDFrhcis926mBPXAejmekz4lUqmrRbJfx6YkObdgRHG3_Fatv97_L16vPpfwAQIn4Fz6ZgAYaD_TIkO2TddW5S0SKZY_t_mvW-7axqh03Ix3aTlVW7GjEIITvpVBu-0Qe93GmkMUiCRZ1OZ6yGfkHR9GfpZcs-y87fZ_F7nfyXdjHYw612YZchMGvlGgvWwJd6IjD8MmiLWB3UrFsEUvDD8ZISj16hom3Z9av9HX-S3Wpbcz9ZgfuUOUu_tjg4Jwgad5ufljPDuCimNDcPoFxqCvg7z-RlYk-gF0f0Wt8FmrVXzEbJtLe3i3H6tUiwKXXaERmy3HafiU_E9pBQ7jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=NDFrhcis926mBPXAejmekz4lUqmrRbJfx6YkObdgRHG3_Fatv97_L16vPpfwAQIn4Fz6ZgAYaD_TIkO2TddW5S0SKZY_t_mvW-7axqh03Ix3aTlVW7GjEIITvpVBu-0Qe93GmkMUiCRZ1OZ6yGfkHR9GfpZcs-y87fZ_F7nfyXdjHYw612YZchMGvlGgvWwJd6IjD8MmiLWB3UrFsEUvDD8ZISj16hom3Z9av9HX-S3Wpbcz9ZgfuUOUu_tjg4Jwgad5ufljPDuCimNDcPoFxqCvg7z-RlYk-gF0f0Wt8FmrVXzEbJtLe3i3H6tUiwKXXaERmy3HafiU_E9pBQ7jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOBEPGRbMedbQeKwn6ELGafYzAIpeW0w820JqTeWX40mFy6hqfifemmJT8FuklyURh0mtDTqcfssYnHJIXqvg3I6_pdKmC5D47Idres512Fs60fAJO5KMN6SA3H5KyrJKkL0aiDJVX15jBkKEImwvIWC3lYz2VGqIxaAx0yuJFu3oZk0HF5xpalxL6qYSR2ltZH7QUfx8cCbOT1QR-ONMb3Kr-WdPlB0rYk3rg4eoix729IBMHdsUQolglSTNbMD5I9lHYxxp_kHIUwuVeTc4S7ImHeA2MU9NsWcn_u55Avf0_GcyKkpzS-KrEfjBcjbVMx1nJpp3-O269qbLDyMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nBCYfi2Hjqvwl19l0j4KVAiHu3qanjvDca1Dj8LipISWl3mFI4SHSgDzDKbMjq-NJQlLSBGYeCQThiIQpdT9JXhPpcG2tM-bgVwh9XcwMC-HCRxdP1QLlfQ5InoqJudAhNELPH74zaPS1h3s8_FGZ4o8fYyOb-GdE7suzGX4jZfHa7yt7bMg7VczUz7WyXhH9lGL4RHcIc82IZP5K1sr0cBtI3v45JTm-kErGzMOxzuHI3TDr2TlKhZnBaWhDQ2UktnoClovNcIR4fDZDfvdnOg0lb_Ojt4wKT1uA_Eq2J7MpqL2s1geAGdyhFpN53S3eaezRp0W6V3yYFhoy1vN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcM_ULss1bvdwogSC06GAhq0wRaf_h59sbkib6fCRE6dAMhy3VYDAJmfETnIJG0CY73eQEWUsiNF0oZR4G3g3TDoIPfMQAecZ7V06BpOXXMncK1nI5SaTAeLMiG2KM8CXM4AsTkyQXRmCMOgA-N3Adn2XpXqyfetZYWanC6nd_Brcp1kIgA0OAKQuwpJnXza9h8fIQIJjuDoTlXarhl2SBzYVWLJo4_lYcAsVPLtiWrepaDs0YLX-7Fmvair6UI_FADPJLy3eP7U43MpROimuqEPjtEEsszJUCSpjosbhD2528vSNQyypZ1pVPtmvsfiKEiGEVa_NpoLOEU1Gqn-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h85qj0CVO4rnATwSQB_WK9da4vL-m0QSbHOygeSpRlrOkKVD6LAn3diScvZA-KRlioAQNStkvEmwMhDfuzC_ImY9zxdy9ZbIHcrtmx_qK8lWNIeyWN593jWZidSCGC4g07izWVye8WRN2wXXD40ysRx14Tvc7pbe6INufw_8QgsnAX1D6TRBVnbJqDLrFFn6l9DGlMD6u_RdfArVMmKVvJDT_43VqjmICpp3bPp9ty1qmdN5z0Kve012-aCPIeW5VgVevk0S6L2Reg0xtI0SOakuKCSKMcpz8Nb11BICE31jBGqVCb7uPBpwFpuqjI6UZe_3x4K6zu92C9bmRR2sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gd3gnveq6__2qroaEbRW1Hyn5iMs04lLUQi6G1a5BaIpGgXKdLNmrrJGiQvM5EA6dAu7wmO3T5P9az4_0BwV4qQeV2qOUUIwPTj-Mm0KZCLLXNH6E-3Lz37UmcRkpphkHSUTR4G_U828nGu0rzkUHGAs2Ysv12jwbo31NW1wb3HgGEDWCM4WUMp3ts7YXBCsVfCcIKUkJCKZXXlz4YhwYzv4i_PNZn3KViK-XMwPBRBlTyDxU1CVjkto19FObeWfS6wjYxJAfMcuQe_LJprsewStuYWX15crGxvFP0QQOtraW4OzW3J5v-MF81DYa0KT_s4uSk9OpGPaBseCMYSJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PD60vhbLbBCNGO3CLhZ_o5xjXCi52ws7VpKqSF49R_5i7QCRfPszcpqm7vQvJFj5ITtMtLLypJ8XVML6iAJF1FHo5OBU867hiCHPWI35sJgAkB3Ka4wZmMMVs4OB-N7ogJ_pfa6syphqOjlLlUzxjPVGc4poxreHOcRllmFh8h5uAGZgb4cfEUruHONI6RFbTojIn99qthOS0mZq79n0XfkioA8Q_Y2PbMM4gbgydyylwNbTV5yNRPqlAd9QeJjE51mVWWVdMZ3jmlLck2XnuAQOm6hWl43F3Ca-Fbq7VPQ7fOMl06bS-kHGCkXr5QSMEFiwWegu2OXsyN4jIR_PvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-b7zN0ao8vR4Jf93t5tuJvsSli0bRK81ayj8_ESbtxuUNcs5Eg8Tflb7GcqAvBsovUJ2x870a5Khq3CKbEOiLlWksf317zwIj_mIAHPJaVMW0k3AEinYplq6xfcEiWbXCpnwOTdw7XkRO-e8yis0aLRJo6rWFjizJiuQj_Ajd1gxpUE2iEB4qXTdtRm9XPCZavEFkyPurqk8RHPUeZuYgckAMse90fRqQi18PyZX2y3Fd3xYL8lYJSjFwh_4Onx1v7uhnOvAzksrDCuuqK1sh8GGoOgIW8QktcVi_8AwAfBL0dWdKAyIeOuEZvScDIhO8y-ONqbXgOHWaIk399QQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=PYk8sDNJ7eVv241iYZZrgQipCW43LwEF9EydIEVvrs0PV_jWx2vaJatgS5qQy4EEdAd2xs2Pgsih1ytoIRYaRs425u8nDY6D17YYzRCnidhKZ5fFg7RMcr0DD7H8FdumcuqgbC2iVgzOMH7EOAkpWz3p9L50znTfFYhAsJHDTkaUm-G9Sy_ktj9Br1eOwxI7PoLF7LoSW6l-CdZoW7f7sUgvruFyJJcCX7r5fH_S8ODrppz9eig2NbYjes3jiXhZUFXWm1yBmrC0vZTA-30eaOvmfSr4Km2vyTRbRdqIdZCLlLhDcI30sa2LvWZbU4p5x3KXGikXF2OeOx2nShDpYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=PYk8sDNJ7eVv241iYZZrgQipCW43LwEF9EydIEVvrs0PV_jWx2vaJatgS5qQy4EEdAd2xs2Pgsih1ytoIRYaRs425u8nDY6D17YYzRCnidhKZ5fFg7RMcr0DD7H8FdumcuqgbC2iVgzOMH7EOAkpWz3p9L50znTfFYhAsJHDTkaUm-G9Sy_ktj9Br1eOwxI7PoLF7LoSW6l-CdZoW7f7sUgvruFyJJcCX7r5fH_S8ODrppz9eig2NbYjes3jiXhZUFXWm1yBmrC0vZTA-30eaOvmfSr4Km2vyTRbRdqIdZCLlLhDcI30sa2LvWZbU4p5x3KXGikXF2OeOx2nShDpYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L0KRFiCSYPtWZkNOK4YI58m8N8SPo0IAMBWsLd6hFJvCnS3qDz01cc6ANDWecGvQ_8wVJLD16ofEwcjbE0D97_iYoDWGvjL8-XeYy2Qcf-HdCoyrQn1lodFdKj2R-pdzEThiwkvOkPDhSQOK5DZKjApkdHeslwMn2ve-MhtUZQEjaMSDlHDBiXOnaq2CbOo5EkvaG4c2Ph7YJOZQlPJlOUjiCDoUpNBf4xhVBSfLcH6-194eT08pEl_viXcNK51Jdigz-T8WV5TTPALNB7SzEkr8AMGYnA06Cbhc8BoSTItXm5XFaEalBd2rDeCvCjZi3ZiS_s9CHRA697jCPtapwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G_cZjsAKq3tQw0-uCxaqDLqDRjzgSbb-1GKqFTpH-fss_8RykNIUShj_GtyQgCuXUXZv_bd88jp9HV9QW-BivLmh1MAnWta2SNtZ5xcvli_DS38ol8q03BgPQb50pd5joG5VORVMirmvYqRViqTjbvrMbzk2wqNVkKmF1Dfq2ZbhwGGskcm90bgu4CzGhv1Z4VN7wYtAFSVIKokNTbz9_DcIdmkO61oA2RBGRIbJAM5GXmV21BRhVaPBzCW-H5-a8o27Cb5lqTamUuId12dOC27SzqhNiSc0gp_ctSLc6rHDbHyosE5YsmR9KqG0cF6dOieWgNasL-OMZd3Qi-a4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/met1vhdf9pRuVGsquv1jHYNwHvMgfI0936-6gzDtFZIb-H4kID4E1a-c01OYB8zcID4-isOFnYY8LP_I1u7ee46CGUsB5aUcZseWQ41IOPn_Ygaw0fmXuy75KkfqrwIj6PmRe20WM-KDJonBEbauv3CRTDv3TnHimPxX7T1S_tBYWggOfnsACYdKZPtl319NUvYsWGwYFSYvIn5fa0_vL6cO1oxxtxDhtvG1KkbyQFKvHc2DKHdhO9fd_2mM8raW8AWHXTGS-xzAij_U2irIf-pK5tdzNQwVNfeXeFyFkIrsyT0g40olrY5YhW_NtCj1xbYyTLqG4hRUYSnyRGVg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UUIc5oGxmbnT237krnzL7APqUbCoHmh2fXTBMIBJ89fI2NmWgZiDuC1yAwDDcLVaI3L6F63o9p0bMWqX1WoHlfQrAhdho4-Yqjs3cFuU1gmrmkW8hArNKuLV1ZzwfEVp1i1OJrKo2V6R6w-dC4cdJA1TywMgjUBdTo1s7vXOXbXf8O7YtaqWyHR5gzuJR7cU4hkfxDOJq1cCNDIH9UMXQyK_soRsPtxZhkSw4kSIqIuFIueVsiVbnPJ9GlN5OKsRR9_gJqc8iVLiTrTZmr-k0KiYy-dKdPGu6766uPGqfHP85LLo2AFhR_VIgVDtUsIsFMtrllcijWaPr40xmacrlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjHPRJDRP7Qz_mQLKusUJ8F0NcBwpByq4NJW0JRPRPY1uusDZpkag2bT0t18YRTG9NZIOecaxyLwds8oafVm5WHQjDK06N2U7H6-IYXsUK0EOexCZPW5jEl0rhDFvnqM1nuN2bNMalYr1pxpNnH-jX5a3BBJLMbo4PtO-d_EEXRzu0NgALfUIXW-JuFyh9v2-PsR7Ps0rDEvJQ29lrErbjxOY2F6Sta4ZApNp99JyUbktBc72dTtGOdpmfGwdAxBG1lq23F3-NOOgxkJW5EdXJmMOA4CTE1tMx9hdA48Pt7SHkp9RGEuuChytpCd1ciPsTYtLPenEaSjHVBki9IG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سالواتوره سن‌فیلیپو، هکر ایتالیایی و خالق Redis، توی مقاله‌ی جدیدش توضیح میده که نبوغ واقعی لینوس توروالدز(خالق لینوکس) فقط توی کدنویسی اولیه کرنل لینوکس نبوده، بلکه بزرگ‌ترین تصمیمش این بوده که خیلی زود کد زدن مستقیم رو کنار گذاشت و روی رهبری، هماهنگی و تعیین اهداف پروژه تمرکز کرد. برخلاف خیلی از مینتینرها که خودشون رو درگیر پیاده‌سازی جزئیات می‌کنن، لینوس فهمید برای مدیریت پروژه‌ای به این بزرگی باید زمانش رو صرف رهبری کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4702" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پشت‌پرده بازار فروش غیررسمی توکن و کلیدهای API هوش مصنوعی
تحقیقات جدید نشون میده چطوری یه شبکه‌ی بزرگ (عمدتا توی چین) برای فروش توکن‌های LLM با تخفیف‌های سنگین شکل گرفته؛ این پروکسی‌ها از طریق سوءاستفاده از اکانت‌های Trial رایگان، ربات‌های پشتیبانی ناامن سایت‌ها و ترکیب کلیدهای API مختلف کار می‌کنن.
که برای به سرقت رفتن اطلاعات مهم استفاده میشن یا Train مدلهای AI چینی.
به زودی بیشتر تحقیق می‌کنم و بهتون میگم
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
اینم لینک مقاله‌اش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4701" target="_blank">📅 03:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خدا لعنت کنه این جاوااسکریپتو با این سینتکسش من ده تا زبان بلد بودم اومدم بکنمش یازده تا جاوا اسکریپت رو هم اضافه کنم بهشون، همشون رو یادم رفت الان فقط جاوااسکریپت بلدم
@Linuxor</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4699" target="_blank">📅 20:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روی اوپن کد هنوز میتونید از nemotron3 انویدیا استفاده کنید</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4698" target="_blank">📅 19:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فعلا میریم nvidia(با اینکه delay زیاد داره) تا ببینم api رایگان امن چی پیدا می‌کنیم باز</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4697" target="_blank">📅 19:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4696">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مهم
راجب Mimo
😭</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4696" target="_blank">📅 19:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t40Tb2dG89pccBPZC-r6C904IeZcgfTYYCqRiOGsZghkGm2Ko_ozS0N0qfHGw2KChL_n21CU27kb6YEimiCZkO2v6fss9-UMeY3vxdX9TZiXNtgKr8q7X6p33cjMJtZvHutd7tIPF91wMmEjIhxli-tjAcup83qGTSbF2JgXXGIJ2rHJnMmm8UBZqUhpsOdAps_0IzjrQ49ZBooPYmapMcoUVYfQVjEoWUVS8YK0NT7dmHp8-upBTC7fhaIM0xatpoki4kNtf38VtK7-r1g6a6SmCmdDwEYK_cSJ1KJnhgzRsd8MTrgqV03_tY-_8FrCsspY_fa_Pf660Th1S8VXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JhcPcwp7grC3F0TYJIwOSnedTbNFJUaqUoXy7rPcEldaGByAF_mhgShLZUXK_9rR82k1C-qqipwAzu_k2QZZxDTMuOAkdEueHoQaGY7WTjAfrRyK7Ht3PscdDLagM_Cmv3OvDFTHcEM3yMrSIvxpVtfHrymuA5By7KbrCTpb1dx3XBfHBe-KoKSmvrUa17GTeWljI1sSoqmm52rGl0CLfamtqx_tgnAI76zYCsK5D4G7EuzFzMQyC0m5GgvlfS6FsoIrA_MS-3p0qvFjXKVaiOnuLQ1uZkzvZwFS0dvIavqx2AFlbKSsL2zQBBFQVL07ioZr78l3f7ebSHuKp70rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dW0sa-779kiL2X7cea3jOYX8krjIuDzFv1oQTud3SCVt61pvGyrpLvGEHZW3UXDvgxgDj_EG7k-PeupzdtJxHFe6tO6KTaeKbrOc6mNTpaBKgO1dFLY1DwQmvCTV8IQqn-YxWO5M66KUuHvVYtMZqN9k8SYjOgcb5-3tPQ3cP6jFgMgDIKA73fr96SRm78UhjMCs359tMXP3CBW46Y0OHXCIHoxFWVorHIsdIUU-fASWy4euxnJJgnNz6bFUVl3jfHbtbtQyrmjjlNJb0DSLP6AjBosK2FSvMrCQVNCY6Mb1HevlgxNREXa8DxO7Jy-w_W73LZWRfN-dYts5aMloBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای این از proxy relay کلودفلر که توی ویدئوهای قبلی یاد داده بودم هم استفاده کنید مشکل برطرف میشه دوستان</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4693" target="_blank">📅 18:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4692" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4689" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B84sR13AwP4mOX1PfLzGqjqw6fGCTayOz8hOirDlosiV8pB-U8p5p1WEpu4Y_ABABaMZsyh85wFESzqUDkjMVjmlVn6JlMuh1AmdrqUj589VpKxqKOiF9IXljZQOvoD4oIFN6a3N_lkecV4F-lMPWnylhvB4wBu7VmsWQPELffxVs9tEYrZBi8rG0XK2iQSWochYYnWNP6TN3S0NTF1M8fmdg02EtMzbIAL6XFJT_dxzefsacFCWKV9CjQhJyHLPv0zXzwSKHNGD3WkqSpW-G9XZ9Zyeo1TSV2CMkP9SxwHCy-Wa3OG94rjkR3D1rKx_vN2iLQnFD88oohtgNKfUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش
طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4687" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4686">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خوشحالم که این ویدئو برای خیلیا کاربردی بودش
🔥
روی یه سری آموزش دیگه هم دارم کار میکنم واستون</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4686" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4685">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNFHK_CU6Q0qbyIL02qPOyAiJdspRXMSbby5Sdlck2OSur36n4K0ndV1wlfQ6H9oyvaddyNdY-yPGBvZiqCUdkfy6tPnRvtvmLdoHxn3lC07lnPb8og0w4p9MSFbpVKLJlsjFo4rlGGLCYvKO8VcmI-_28KPYojGSD2b46vvgnItDf7UMK9s7H2KUK3s86K0XB-OLKaFc5PcI6gpxpYO5LJmAEZ-6v14_Ge2KdynF7lkLTjwoh7tpC3cEWpvcqYvmY2j5b5uW-cQ3xtBgooroosOs6eRL7XoOsm_xbIyCd1TW-0fSrCcAf_WQpcB2uuEYDRaGQ8XBRcibe6awKXChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اگر به ارور workspace has been restricted خوردین، باید یه ایمیل جدید بسازین، با ایمیلتون اول اکانت گیتهاب بسازید، و با اون اکانت گیتهاب توی railway ثبت نام کنید تا بهتون گیر نده و فکر نکنه اسپم هستید. خودم الان یه بار با continue with email ساختم دقیقا به همین ارور خوردم بلافاصله بعد از ساخت 9router، ولی درجا یه atomicmail تازه ساختم و باهاش یه اکانت گیتهاب ساختم و باهاش لاگین کردم، سریع ساخت 9router رو و گیر نداد</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4685" target="_blank">📅 05:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عبارت VPS هم زیاد درست نیست. صرفا جهت شیوا بودن کاری که قراره انجام بدیم بیان شده
👍</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4684" target="_blank">📅 04:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4683" target="_blank">📅 04:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riEyU9hX9dL8NlbmhswNy0zrxsK4c4bYYFXIuoBHvy_ZtFCNPhJSp9rNZ3Gs5B3zCKIxhqobVnIkyuu8SaGtfOjs2rmKmzcQry-HDV_Diid5ukDKPUvwtCExQdFfVhvSNqiMVg8XCTLNfo4xuv2sDeE5A3TxsoSA5vvMNjZdKdkBoxvrCnZa5Cv8GDujiZ-WVhROP4AgZAuHt5e4G3n_i7rqS_SwgdY1k8vZ_yQvwtw1pHJxsAmFKok9bEIgXYPge26d_ynvoSZMqBYs0eRxU4wys4_8znHGsZ3QuMu4LbcLndvNpDRPQBnhIYTj1OzfJ_2LIerKM1MK5v3DTBxwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4682" target="_blank">📅 04:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فکر کنم من تنها کسی باشم که از اینکه مردم از کانالش لفت میدن خوشحال باشه
😂
به خدا حس میکنم هرکسی لفت میده، جمع اینجا خلوص بیشتری پیدا میکنه و اصلا کیف میکنم
شبیه عصاره‌گیریه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4681" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن و از تلگرام باهاش چت کنن 24/7 خیلی باحال میشه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4680" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHaKRcBKqzi7tGUjp4eRu7AhJVcr8h9qSk4DYkHcX9qMe-A0wCDH73PEJRMkYdwcwspZ8Nr9cufq0HweTQ6Gj2PHaGgDWdScAU-bJzjdklUyk3Egwvk9knJ_Il5SqGboEqhBE-iasPBQRPKDfrcw3SuZHt9w80571W61K8MHzTW3aUJHrxLMg8BZk-0fBRDr-Q7JunzqFwbeuJxiNbw4x_db5gci8z1_9M374PqKSdZOOCeX1QJcinLNCkK_KSkmZEYHi-CWWR5QsILlLOViQ-IIoOMeZNzNf46mvz7Rns7iTESLywyh6eNtuUY9YPC5Fs4x78hfvaVKxH0X8-U_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم
که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن
و از تلگرام باهاش چت کنن 24/7
خیلی باحال میشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4679" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">برو برو
🥰
موفق باشی بعدا میتونی معرفیش کنی خودت و بگی چطوری توی تحقیقاتت کمکت کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4678" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خجالت کشیدم، میرم پروژه رو راه میندازم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4677" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تینا شاگرد نمونه‌ی منه و به ترسش غلبه کرد و هرمس رو راه انداخت
❤️
پرسید، تلاش کرد، به ارور خورد، و آخر سر تونست با اینکه تجربه‌ی چندانی از کار با کامپیوتر هم نداشت</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4676" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">باعث خوشحالی منه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4675" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">من به شما افتخار میکنم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4674" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در مورد این، یه وقتایی به نظرم بهتره آدم کمی پروژه‌های پیشرفته‌تر ببینه که هم بدونه دانشش در چه حدیه، هم یه دیوار جلوی خودش ببینه. نه برای اینکه بترسه، بلکه برای اینکه بدونه دیواری هست که میتونه ازش بالا بره! و انگیزه‌اش بشه. من خیلی از مطالبی که میفرستم اینجا…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4673" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4672" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم. اما خب، شاید برای کسی مثل من که کلا هیچی از دنیای کدزنی و چیزهایی که آموزش میدی نمیدونم کمی ترسناک باشه این موضوع  این‌ روشی که بهش اشاره کردی رو توی کلاس هم پیش گرفتی و اونجا به من هم حس اینو داد که خب وقتی متین نمیگه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4671" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خود هرمس و راه‌اندازیش مثلا شاید یه دیوار بوده برای خیلی‌ها.
من و بقیه‌ی بچه‌ها توی توییتر و تلگرام و اینور اونور، طبیعتا تجربه‌ی کار با کامپیوترمون بیشتر بود، زودتر راه انداختیم.
انقدر نشستیم بالای دیوار و از منظره تعریف کردیم، که چندین نفر دیگه هم ترغیب شدن و تلاش کردن بیان و بهش غلبه کردن.
چون واقعا کامپیوتر، و همچین مفاهیمی که شاید برای یه سری از دوستان ساده به نظر برسه، برای عده‌ی زیادی اولش ترسناکه. و باعث میشه فکر کنن خب، اونا که تونستن از پسش بر بیان باهوشن یا هر چیزی، و من نمیتونم.
که اصلا درست نیست.
کامپیوتر و این مطالبی که اینجا قرار میگیره
همه‌اش مهارته.
و هر کسی با تلاش و پشتکار، بدون استعداد، میتونه یه مهارت رو یاد بگیره.
شاید یکی زودتر یاد بگیره، سریعتر متوجه بشه، ولی در نهایت همه با تلاش می‌تونن بهش برسن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4670" target="_blank">📅 00:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اما تفاوتی که هست اینه که تمرین‌هایی که توی کلاس میدی در راستای چیزیه که بهم قدم به قدم یاد دادی اما مثلا اون پستی که برام فرستادی برام آشنا نبود اصلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4669" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4668" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به نظرم این شکلی یادگیری خیلی مؤثرتره
😂
موافق نیستی؟ آدم اگه 5 بار هم قدم به قدم جلو بره با ویدئو یا آموزش یه نفر دیگه، خودش اگه یه جا گیر کنه ممکنه نتونه انجام بده ولی اگر خودش درگیر بشه، واقعا تأثیری که داره صدهزار برابره.  بچه‌هایی که تازه اومدن توی کار،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4667" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من تاحالا وارد گیتهاب نشدم، پروژه گیتهاب دادی بهم گفتی برو برای خودت درستش کن
😭
😂</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4666" target="_blank">📅 00:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">:)) کاملا درسته بانو
❤️</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4665" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.  دیروز یه پست برام فرستاد از هرمس،…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4664" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده
اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.
دیروز یه پست برام فرستاد از هرمس، بهش گفتم من هیچی نمیفهمم:>>
گفت جلسه قبل بهت یاد دادم چطور چیزی که بلد نیستی رو با استفاده از AI ساده‌سازی کنی برای خودت..</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4663" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک کاری دارم میکنم مربوط به هرمس و مدل رایگان و ران کردن هرمس روی گوشی بدون هزینه و 24/7
نتیجه خوب بود بهتون میگم
😁</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4662" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیش از ۹۰ هواپیمای سوخت رسان آمریکایی در اسرائیل حضور دارند و هواپیماهای ترابری به صورت گسترده و بی‌وقفه درحال پرواز به سوی اسرائیل هستند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4661" target="_blank">📅 22:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">یکی از دوستان برای OpenWrt یک پنل مدیریت نوشته.
این پروژه یک اسکریپت نصب برای Aether روی روترهای OpenWrt است که امکان مدیریت از طریق LuCI و CLI را فراهم میکنه
https://github.com/moein8668-git/aether-openwrt-client
خودم تستش نکردم
اگر مشکلی یا باگی مشاهده کردید لطفا به توسعه‌دهنده اصلی گزارش بدید. (Issue)
توجه: این پروژه فقط برای روترهای OpenWrt طراحی شده.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4660" target="_blank">📅 22:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگه بک‌اند کار می‌کنید و Go می‌زنید، پروژه‌ی Gsxui احتمالا براتون جذاب باشه. این پروژه کامپوننت‌های فرانت‌اند استایل Shadcn رو مخصوص اکوسیستم Go زده که اگه با ابزارهایی مثل HTMX ترکیبش کنید، می‌تونید خیلی سریع وب‌اپلیکیشن‌های تمیز و مدرن بسازید بدون اینکه درگیر فریم‌ورک‌های سنگین جاوااسکریپتی بشید:
https://ui.gsxhq.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4659" target="_blank">📅 19:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4658" target="_blank">📅 16:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
برای اینکه مطمئن بشی VPN درست کار(نشتی ip نداره) می‌کنه، می‌تونی از سایت BrowserLeaks استفاده کنید. این سایت IP فعلی، موقعیت تقریبی، اطلاعات شبکه و همچنین تست DNS Leak و WebRTC Leak رو نشون میده تا مطمئن بشی
#اطلاعات
واقعی اینترنتت لو نمیره. اگر بعد از اتصال به VPN، آی‌پی و DNS نمایش‌داده‌شده مربوط به سرور VPN باشه و نه اینترنت خودت، یعنی اتصال به‌درستی برقرار شده و نشتی وجود نداره.
این سایت ها
#امنیت
سرور و نشت در اپ ها رو نشون میده:
https://browserleaks.com/ip
https://myip.theazizi.ir/
@xsfilterrnet
👑
@xszapass
🤩</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4657" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تا اکانت گیتهاب سازنده‌ی Aethery اندروید درست میشه، به هیچ وجه از پروتکل MASQUE روی اپ اندروید استفاده نکنید.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4656" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMIPhEuSIFBqNiAgj6qRtiQtJJAWXWtTCDgEZwN3u7GWR9PRun0j1S6Tw75TZCojkT49QsktP5QNRZHDwyuDHIFC9vDIAE5pY51THqIu9rg0UEWIv1u6gMnBa1YRT6c4Mchcl3brn9Fqj2yGL6WIcDfABNWW1akhZrK4xJ2sR5GHZVaHdABdnw6aOwEhU7r3RC1_2NXkWJL2CxMmg3VP6TABvvGUTsSBKSDG1e52NGZvCdLi0R1NAscB_T2etT6CPtPvNhBbo-qZoLrdAeOg9i9lbH2XHSiHNGQOtiTq_QAqdRn5nGcatA4pXj5rgenljy7Ey4bIQvO0Bg3QWzn3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/4655" target="_blank">📅 05:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtZNqKmKDDGONYO1pXB5hkmmQUznia9u5pO0hYenikax3U7K8kuiUi5jXeht1FqdHkPvVReRTuGK3tgGG1_Rep2-Kn_o1IxGv2Qnd1JAQ-UJRcLtz7Ixh4iYyv-dkRi1Qjk8-5YPGufulDzZfIVEDS6YlsaOtvdHjpvlEfRRy6OK1FrvHMacHDCWHQZTPtrICo1zUse0V1tpAqAOnL82GDR_0J0BjxdR3oLKF_7JPxx1vtAPUuIalmkbPGbi2Ed5eG_RcAHTlaWvkL17qZvkEKPx5fWhvwk84Pr6XIVJ0jeipav1YcFYoOveLIDGvHD4PzGZBeOBOS6MsOYGvudVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با تشکر از علیرضای عزیز بابت تیزبینیش و زحمتای @CluvexStudio  این مشکل خطرناک که شانس MITM داشت حل شدش. حتما aether رو به نسخه‌ی 1.4.0 به روزرسانی کنید. آپدیت GUI هم به زودی منتشر میشه https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4654" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آپدیت جدید Aether v1.4.0  https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0  توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :  فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4653" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.4.0
https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0
توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :
فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد (verify کاملا خاموش بود)
یعنی از نظر تئوری یه نفر که بین شما و کلودفلر قرار بگیره میتونست یه سرتیفیکیت جعلی بده و ترافیک رو ببینه الان اضافه کردم که سرتیفیکیت edge کلودفلر با هش‌ های واقعی که pin شدن چک بشه هم روی HTTP/3 هم HTTP/2 این رو یکی از کاربرا (Matin Senpai) گزارش داد و خودش هم pull request فیکسش رو فرستاد بررسیش کردم درست بود، مرج کردم :))
فیکس مهم دیگه روی WireGuard و گول (WARP-in-WARP): گاهی اوقات "Connected" میزد ولی داده رد نمیشد. الان هر دو مدام چک میکنن که واقعا داده از طرف مقابل میاد یا نه.
اگه یه مدت هیچی نیومد خودش میفهمه تونل مرده و خودش دوباره وصل میشه. گول هم قبلا اگه تونل بیرونی قطع میشد کل برنامه میبست. الان اونم دیگه ریکانکت میزنه.
یه لیک هم فیکس شد: هر بار reconnect میشد (روی مسک یا وارپ) تسک‌ های پس‌زمینه‌ قبلی درست بسته نمیشدن. که روی نشست‌ های طولانی با قطعی زیاد رم رو الکی بالا میبرد. الان هر reconnect درست پاکسازی میشه. :))
--verbose
قبلا همه‌چی رو یهو میریخت بیرون که خوندنش سخت بود برای بعضیا که الان
--log-level
اضافه شده با ۵ سطح:
error warn info debug trace
دیگه راحتین :))
حالتِ info آرومه و عادیه
debug
جزئیات تونل رو نشون میده
trace
همه چی رو حتی تک‌تک پکت‌‌هارو
و...
Aether
الان موقع اجرا رم و تعداد هسته سیستم رو خودش میسنجه و اسکن و بافر ها رو خودش تنظیم میکنه که روی روتر یا برد ضعیف زیاد مصرف نکنه. با
--perf low/medium/high
هم میشه دستی مشخص کرد.
پشتیبانی از OpenWrt کامل‌ تر شد: علاوه بر armv7
الان بیلد استاتیک برای x86_64 و aarch64 هم هست
aether-linux-x86_64-musl.tar.gz
aether-linux-aarch64-musl.tar.gz
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4652" target="_blank">📅 04:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مدل Opus 5 توی یه سری بنچمارک‌ها از Fable 5 هم قدرتمندتر بوده توی کدنویسی
با نصف هزینه
ای کاش زودتر بیاد توی کلاد کد تست کنیم. فعلا توی اپ اومده</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4651" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=fIOG2nsjJ3mcenLOw-ga3m008KX-fzf6EWsT9QtQs49WSgMuxclEJV5Mf_Dibf1xT2k5JydlYmaBElhFoC-DvlHUMPS_ZX_Z333IWophjYQxfqY5lNFRy1qr4kzV9M16iWjzM3DWlMA2UlTmqd70NccF8T-33zQwmsIbzyUfaZyMbdwINOD545Rd-lC_IkfJIxr3_THT4tC_oVMOlD-tzhYyKTQt6GEuyB-tGM7oiqMx2Ix_g6TMNF8wWPXNDEzoMd8ayznKHSMkI8a0m3QDS4qGx74tIxZVoRjWULnMOxlUhiFPxCWBvoYXHzfEKF0nDFRsxsCQg_vDQZ-joyCl-JwJXUBgwgW0VDEkJ7zGw6IQBcytFrrLI1zS1_8rpuyv6EE-2Q53jx8KmFBjxz6kALHf7lxTQbbserrDYX2IpgGurJWw6S7WYk5X8vtg0MZkP3QPPM2BuriXSjXvLRlaff_m3UVVtm_k_mMNc5VcmEJO4cmU4Jz-AeuDii1b5x4XiOk7B1Y5ZzZ1zXfmOl3QETuDDW-kzEHdan4KmYCdDh8rQxe52XZVSGvZEr72tnl_4JliLR8LAuwot1HrTFpCWI-vZ0cGijydE3RrZgSv1Jc2QWt5NY1Ke_KHRTJYkazAqNRlcEExwuGfOY6ETcDttzv_YFfVJbVFHGpFHkldMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=fIOG2nsjJ3mcenLOw-ga3m008KX-fzf6EWsT9QtQs49WSgMuxclEJV5Mf_Dibf1xT2k5JydlYmaBElhFoC-DvlHUMPS_ZX_Z333IWophjYQxfqY5lNFRy1qr4kzV9M16iWjzM3DWlMA2UlTmqd70NccF8T-33zQwmsIbzyUfaZyMbdwINOD545Rd-lC_IkfJIxr3_THT4tC_oVMOlD-tzhYyKTQt6GEuyB-tGM7oiqMx2Ix_g6TMNF8wWPXNDEzoMd8ayznKHSMkI8a0m3QDS4qGx74tIxZVoRjWULnMOxlUhiFPxCWBvoYXHzfEKF0nDFRsxsCQg_vDQZ-joyCl-JwJXUBgwgW0VDEkJ7zGw6IQBcytFrrLI1zS1_8rpuyv6EE-2Q53jx8KmFBjxz6kALHf7lxTQbbserrDYX2IpgGurJWw6S7WYk5X8vtg0MZkP3QPPM2BuriXSjXvLRlaff_m3UVVtm_k_mMNc5VcmEJO4cmU4Jz-AeuDii1b5x4XiOk7B1Y5ZzZ1zXfmOl3QETuDDW-kzEHdan4KmYCdDh8rQxe52XZVSGvZEr72tnl_4JliLR8LAuwot1HrTFpCWI-vZ0cGijydE3RrZgSv1Jc2QWt5NY1Ke_KHRTJYkazAqNRlcEExwuGfOY6ETcDttzv_YFfVJbVFHGpFHkldMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از کاربرا اومده توی توییتر یه مقایسه‌ی خفن بین مدل‌های Claude Opus 5.0 و Fable 5 Max برای ساخت کدهای فضای 3D (توی وب) انجام داده.
نتیجه این شده که تکسچرها، نورپردازی‌ها و جزئیاتی که Opus 5.0 تونسته خلق کنه، اونقدر باحاله که هیچکس باورش نمی‌شه همه‌ش فقط با کد زدن ( و بدون نرم‌افزار گرافیکی) درست شده باشه.
البته مدل Fable 5 هم این فضا رو با یه بار تلاش (One-shotted) در آورد، ولی خروجیش جای کار و بهبودی داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4650" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4647">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر نمیدونید معماری پردازنده‌تون چیه، این نسخه رو نصب کنید
Universal</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4647" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4642" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPOYzXoYTDwSfdCAIsem2AieqkJNk6uzEzpMjHjVlvDnKiYqyPhgGqMdvhjoJedp7IrK38Sub1wtzYK5250r-TQfcw_AxsKrXSn7PTh0QIvVrHpZMwVj2qMhkikHSsbgP_DFL2BpVqYu9ep80n_p3dzUNN6K8oKZGOPYGw0g2WIEQ_UgLvgsxdI5KBUOSGnNob95ug_iBZ7RdPK0RpH_JGaTC59SwMt-XmS2HSjhW-Sllp5tEdi35jfKMfE4yEZPQlgB9ALb5paYlrrV_ANCNKQEgaqMryQGfgep3IEzQ3XSBAIrOA7iv_AMwieHOaR-TqjXgKWt7lVMQny9cKlItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4641" target="_blank">📅 14:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4640" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
