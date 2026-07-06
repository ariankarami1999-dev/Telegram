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
<img src="https://cdn5.telesco.pe/file/DBUGyP9XCfgTskyw8EO2l4-RpnBK0_ZTVJWRtCI5E91WaIR6xpo2WHurdDurbgmH6xqcmllNw-UjnxmcpsO0d1oe-1Uv_yAmQrWuBOdtwPYAJWXva-WTUxitvYs0kQIZINNLH44h-RgFA8sccEI-2Ny-1zNJW6tXAbmlcBXP4gcDJqHGpolqv1_Yg051_vs4Jk95oaTlPCPveQkVazjw6hv1rsWx2bZXGe8TVociXohw8qF4np_vMxbtuyb8oyEO4EgAY87W5l98c6uyVxzLceXbO2eltfrEWo9rT9-s1wI87MTfZAZr42z_vwEj994isPXn70fnvwK6ZJIIXmt-Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 626K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-98590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ9Xk3RKDxpXbCCCkeOQNaLRRwJCEpdgqCjtbpbWX3YMZMnusSvCxT4thNGYmnCHo-tYB5cGUtNODE1R-b17wkJB1FdAnUVqORPXqZVAeINeEcbiluh-yLE1aZcNavsxxBfs7-oVEq18sHC7_cdjd2d-rc_ALM6TRUIYqwcq2qZ1V89vJRIVMdUb451SJtlSF3B9h7J2KyMHOHH9A_UNn5Yp9vq_pPXZC6QG_rIIcG94IicJEnlDg1daAO98VFaftcBOlV8A6u5PV2GHME7oyh4TjA3wyW0kFtnJuoIHJfU9R2J95Q-PfPAAZOlQkoraUQ_gCGsnmUpxPfP9IKLEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یامال قبل بازی حساس با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/98590" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvnkWGkvVIXUwSSeQ12VorPoi5-ZjI3b41KvJbuaBzK1Pt5RogmT6lx-p-AiNzh5CoHNpiFRlhykRtdPhHbuaFlCE26WuAbkMkiz8IE8gqNPLcBTKq5VSpQq0GdLvNmc8xY0AOKd08e7GCi_upqmcBc58HoBE_t6C83o_EvLZ7ochOjvBRvm393VIxZdI2SW33YKjathkY_BS097XMuiHEc2460Fs-0m2_5oiJLkvmRYzpD3mBn-W4QqUdfwo0SG0whlQTVIzuzftwaxyr-M_Lv5BXhd7tq1vR2Bl-OudEbZzys3iafJoo6ZXBkyfEmJDoGw1wFxVd1KNR2iim3Nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRYurzXpV4xFPA8qAPvuykRvcy0gRWKNXRMrN9xa5O1Vysa66pAqcNAcbPtrWRb89pYma0pvQhV-YXIMkLCIbUCH1czirqCBycWS1cTKjX2eP2x1QO1mJN7kfJDa7QCVF4v76Gu38kwkZ3K4F72fqHyIwh_kufObGF0SpgMYFHX_5i91a1DFxvZFGGZLVLQpRIg2ZCiiq6CAoNO_lm1cn0Bhl0Zs7uhqGXsdmsh2G3VkjDgbHC8OvDkUcqJEb0LDs3A7egdzStT-9x5UpnDlrH17_dqYRwNncF35Y7qDv9mYCD_BaVNzermcnJcIDRBmXeXP_6CBJNEsJEjyAjq0TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🚨
میگل سرانو:
مورینیو ترجیح میدهد وینیسیوس در رئال مادرید بماند، اما معتقد است با توجه به ترکیب فعلی، تیم بدون او از نظر تاکتیکی منسجم‌تر و مستحکم‌تر خواهد بود. با این حال، او تأکید کرده هر تصمیمی که باشگاه درباره آینده وینیسیوس بگیرد را می‌پذیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/98588" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98584">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0TiQkSNXZSXFR2Z2gjaaAwPvWYL4bYkwW6NCEzX82qsbX3CIoywHC5vHFz-EGI3kS4zcGD2BCqo3O2M7E1Nv0EvS3_E6yWQv73w-cMXy6_g4Hu1dIq1noTLo82ZTzdfzjkaXsTRYVgHkO7qgztfsElP0Eg4WRjDeBmx9ag47lLbgaYnNB9gVEZRwoDhpaczWJlb6YqN3F0UQ27tkPI4Kl-JXZEZOYYT0hzLx3EgUkU2a0TSg5pKDDPrq56xvkYUSFoGdSNXlv7rAIE37I55zpAZftxDczdbyscxKhxJ6temdDB9yj-GVbPU8t30fc_jYDlynop5ziEZ6MsnMTWieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMvNphVOj1EmQpg7wKScKaBRQvyUEEdjIT2rekvIL-SOwczY6bmbp8oPvaGxWOZ-qYkba6pFKe_X37oGdDxVf5desccZgNPbXlusB2EC8VdPj52qM7pZqCTeeNa2qQSnLdomiC2uxs39QaZHX_Gyfc9k41nTLQZu37MFTQLNHilozLvhTO2lPD7GUjsOHA4NFIVwuEIwvfT7iFaSsEg6f1TiamsfoHB-N2IuP2a-X8lsgPSgOQC97hmPzi3uh_iHlU7UPRIj8eSu9wwD0ICvTKvJ1UChBBa_o1O29bZaZycSVphb1QWox_a6p_h9hmkW_6e2aKUAoaW2UQstOuhq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW38f1KPkGBLqmNfOVxg3r0kB8hXsMQ_nnsJpyhqOAvj0FNn7Vv8HGfxzDavQiBS0i6g6_kKY5y5XaecP6KeD_1TrXpE_f2QcW49Q4y5DMZszVqg4qhysEcD-v9G0UqMv1EcPeH8gO_ctBigKr6NQCiTbYakUizOlaG-i_iRleMSoSK1-okFV1OUl42PqXWuCFOBBzerNdVM9bt_y9aHN1hpkNZpx911oWLhIMUv4smsGqwPZ7Gs0hirSsW_dojQKAmhwuoUAEOMifqV3nV759VRL16GIDTdIzfqwe91sxdzLv_bxl7UQdS773rGxHqytgQZhYwu-r5x9WhzJxNxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMlWgMOQFSjT5JNWjPpLTglx3ePZq3g_ZVLBgMTlxES1bfCzoua8wFuHBHQtkddfgxn0f5ETukLed0HE4glf6vphaZlbOrQZlQU0Q6EkgItFwEl_60BDnMsLRhnnpsp8VLw-slNu1qUmCIrMBWuaW0_OFiH0WasJGOuwHcLG6EPz7AOfuNGu9FrJC2N_Qmrt5t4nXw8dsjmq4WWS1Fww4S34kEVZCnpl44DEMR46t9lw9XPZxhxx_YjgKZMfdlSbAijCMdqNE_shVGY_bB5iS4NshoAbS2KlGJelqljd1IKixzrqqh0jlIfzVTmdJlpXgdqStbBBYx07ow9Nelbe_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
🚨
توپ رسمی فینال جام جهانی با نام آدیداس تریوندا (adidas Trionda) که قرار است در دیدار نهایی ۱۹ جولای مورد استفاده قرار بگیرد، به‌صورت رسمی رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/98584" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98583">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
‼️
🇺🇸
#فووووووری ترامپ:
😂
با اینفانتینو، رئیس فیفا، در مورد کارت قرمز بازیکن کشورم صحبت کردم. این غیرمنصفانه است که فدراسیون بین‌المللی فوتبال یکی از بهترین بازیکنان ایالات متحده را از مسابقات محروم کند و خوشحالم که دستور من را به خوبی اجرا کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98583" target="_blank">📅 18:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00267e7cbb.mp4?token=d6vDmYIYPKmqLyV5iRPcA7cUBeIpH5Illf2SrdEHMZnapcUzsRTDffdJnxL6SKtQL8vt-s7aikFu7MnkF_4mTbNps4jWHxh7hDiuvskjoQiTPLD8v28XWDLnG0i4WVMrF8-qgql5QiN_NVn7PGy0NDLFaSSUYV2GwninlMzY-RmbQtab5TCHvOrwIxvNbK6kLYnJFdF_-uNpqk7Gne5si71Kj5CsScXOOMALylcF_mFxpGHFAZOcGHSHF56GGoLnVrpcgZd3KItxE30OKX-O7JhJIPP3WwK3wlT8csaigloLo8ACmy0aKlRCjDomYTixVsZGXoUZ5eQhjDsWLpheVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00267e7cbb.mp4?token=d6vDmYIYPKmqLyV5iRPcA7cUBeIpH5Illf2SrdEHMZnapcUzsRTDffdJnxL6SKtQL8vt-s7aikFu7MnkF_4mTbNps4jWHxh7hDiuvskjoQiTPLD8v28XWDLnG0i4WVMrF8-qgql5QiN_NVn7PGy0NDLFaSSUYV2GwninlMzY-RmbQtab5TCHvOrwIxvNbK6kLYnJFdF_-uNpqk7Gne5si71Kj5CsScXOOMALylcF_mFxpGHFAZOcGHSHF56GGoLnVrpcgZd3KItxE30OKX-O7JhJIPP3WwK3wlT8csaigloLo8ACmy0aKlRCjDomYTixVsZGXoUZ5eQhjDsWLpheVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇳🇴
نیمار و همسرش بعد از حذف مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/98582" target="_blank">📅 18:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3386b27428.mp4?token=YclYqQCsqpe50BivrRGoIS7c-SlrsWhXYNpkYjUtU_kdT7NQMoWl3qU9YFiCK7txyFc5mpUvdUBy54HSsR2R2Wln4LlJEH55C7oboi2_bVE_PIE7y5yOzMO514GeW0Re4hz01fLbw0G5Uv_0a4-Y9sh5vfRDld5H2X5v7HXb3Bkikp-wPdbeaTPWzsJydwDv7Am421WTt8JMXx5p3E4yzAZmhXpVWq05734Roy8XGYQKlov09iR66CgLpHfcICuZRehUiyF3RPS3xqpiFBrK_Z-GmCN1fBVKT7OyPFOVVVNXWugw8tPvdahUF-WcVTOukwE1FKlUJXRBiOo1g-8K7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3386b27428.mp4?token=YclYqQCsqpe50BivrRGoIS7c-SlrsWhXYNpkYjUtU_kdT7NQMoWl3qU9YFiCK7txyFc5mpUvdUBy54HSsR2R2Wln4LlJEH55C7oboi2_bVE_PIE7y5yOzMO514GeW0Re4hz01fLbw0G5Uv_0a4-Y9sh5vfRDld5H2X5v7HXb3Bkikp-wPdbeaTPWzsJydwDv7Am421WTt8JMXx5p3E4yzAZmhXpVWq05734Roy8XGYQKlov09iR66CgLpHfcICuZRehUiyF3RPS3xqpiFBrK_Z-GmCN1fBVKT7OyPFOVVVNXWugw8tPvdahUF-WcVTOukwE1FKlUJXRBiOo1g-8K7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
طبیعیه ‌مردم نروژ با این طبیعیت و کشور عجیب و غریب همیشه خوشحال باشن
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98581" target="_blank">📅 18:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🚨
🎙
🇺🇸
مائوریسیو پوچتینو سرمربی آمریکا درباره بخشش کارت قرمز بالوگون:
⚽️
-این تصمیم از سوی فدراسیون بین‌المللی فوتبال (فیفا) اتخاذ شده و بر اساس مدارک و سوابق قبلی است. و این تمام ماجراست. به نظر من، این تصمیم برای فوتبال بسیار خوب است و چیزی است که شایسته…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98580" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrVs49rC1vdaoioBbhgww6kJ8vb5zIXrGCnqSoDo6ukLS_SLW-6EV0jV9-j5sjHO1BPSfIyGOV5NhvxonW13_POcLYvGGVl4XvaBV5Q_P5S0TWDFSpAZUiPVC8pRe-09PMV0o2Ufp08EYPI3ha5EV9VoC9W_0tqreAxpud8Ux-_nNNqvX0hjDvHu4NsQRyV0Z37a3oOehLrZhiI_xokZ5Mhn31vSR5zZdqL50b4J5RkYjMyp3Xib1DJUb2mvBY-RXNW_h3zACRmKkt2q9MY2hnq0e56ssYtyYk_4mFyNPAERwisdVd42zm01T1vtLcraJ36KSy9ecstiqrbrSthMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
🇺🇸
مائوریسیو پوچتینو سرمربی آمریکا درباره بخشش کارت قرمز بالوگون:
⚽️
-این تصمیم از سوی فدراسیون بین‌المللی فوتبال (فیفا) اتخاذ شده و بر اساس مدارک و سوابق قبلی است. و این تمام ماجراست. به نظر من، این تصمیم برای فوتبال بسیار خوب است و چیزی است که شایسته جشن گرفتن است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98579" target="_blank">📅 17:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS_cBK5gXbprM72-3DaMh2Ap84Vccf9aVgg6U_B4UMVIvmjkuOmFMI2jEwnTQT2twx6LBP5vvt83gUfmX2GWchuluNG1rgds_7YcS3I88_mNFS2PQ9xCLsIpsOqpMwmyKyQD5RGR5EBWwZmkCg2gpoomEd8MsTvt5m4K0z4tNwskimJL0NTV8hKes9wBpOgRpT1b1D-1NmlmWy2bPCbQ3Y3tv-1iMGxvg_M4LGxLwY8SCYwfOWd4mm-LJPD0F_x7sVvZ_sg40fwkJvqnlUfQ358BmDwI0tw46t1UH-oPMaaO1IPwdN9OBOOAceGWgqR_DQE_vwgquYGWgvohUPqIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
🏆
ترکیب آخرین تقابل پرتغال و اسپانیا در جام‌جهانی که در سال ۲۰۱۸ برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98578" target="_blank">📅 17:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحنه مصدومیت دیشب هندرسون از این زاویه که احتمالا ادامه جام‌جهانی غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98577" target="_blank">📅 17:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98576">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef353a211f.mp4?token=mtU9Fngd5CnXRk_WreDnw4zlcypdAXGwDRJexlURgpiwJvBgWolDxo4ohDdy88p2Up6jnN-YfesuG9Ydh6cibzo8D4F1IF11ccYpcFyNpqeqJE6MCpKoNgmgaJNuGVGNWyj3dekydOYV0GfjwSJV4_0jVV4lKAFzmCxr7EBeLHmNkP5JhWAOVxOKPfujBCW1yn-Jge44uplYHpfEhPWNVvQuKRj3ynFT9uTsGR3iiTNCDi8cTYjqEtveaj5nWK0Y1FvArClmjTHusvNPj56qLERFFkfRAjzrZNGkFSfhAF3Bocj3C1erNTJ0cc3FULig0iDOiQvI4HrOrCpPKnAqMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef353a211f.mp4?token=mtU9Fngd5CnXRk_WreDnw4zlcypdAXGwDRJexlURgpiwJvBgWolDxo4ohDdy88p2Up6jnN-YfesuG9Ydh6cibzo8D4F1IF11ccYpcFyNpqeqJE6MCpKoNgmgaJNuGVGNWyj3dekydOYV0GfjwSJV4_0jVV4lKAFzmCxr7EBeLHmNkP5JhWAOVxOKPfujBCW1yn-Jge44uplYHpfEhPWNVvQuKRj3ynFT9uTsGR3iiTNCDi8cTYjqEtveaj5nWK0Y1FvArClmjTHusvNPj56qLERFFkfRAjzrZNGkFSfhAF3Bocj3C1erNTJ0cc3FULig0iDOiQvI4HrOrCpPKnAqMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🇲🇽
آشوب‌خیابانی در مکزیک بعد حذف مقابل انگلیس؛ ظاهرا بیش از صد نفر دستگیر شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98576" target="_blank">📅 17:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJAduqngQb-8RvCGwf_YzDeFWTy4mC0C5u-P5d6ssWIFtPMg24Y2hG-xBqG6AxeVmb_X6X1pxr4Khg-2FGGCUfiY_EXMk1gQXbl7wkPPF2As6lUinkDtB3PkINCJvFaYaIr4Gjy59AS7GJugDMt6AKZiUvthGwEYArz-qPM9JaYJKkUsxrEPEPvv5LOb87g9OPV7-wqAttNry-LIDyDlucMHFQl40eFoiHPlk6MKADH8cGSgIHCZTplm4bdE50YcJ5hf5s8MjdBG_JA-tM7qRvqC9K2iCFGOXVsyUoxFMYbevUGPCf9bI7eBCNyxAwEuSv5TxNtjLXXR8FxLopFKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ درباره ارلینگ هالند:
- "من یک بازیکن کامل‌تر از او بودم. اگر هالند دو فرصت داشته باشد، دو گل می‌زند."
- "اما اگر من دو فرصت داشته باشم، سه گل می‌زنم."
- "هالند باید خیلی بیشتر تلاش کند تا به آن سطح استثنایی که من داشتم، برسد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98575" target="_blank">📅 17:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b9f4e618.mp4?token=tZpdqNs4eSVosiiBGnhwxSpjvf9dqjMxCVhck1hZ29jhnYHBqpdOwP8TrPlVFtLyo7xw_7VJ7BvkpOHRzWjgcFH3oi1uOCHwEOBOwRIajO5YQPBGu1w96ddMNeH1rPIPHD-jAMvjQ3XdlAT2MIYMUqG3PgTX-McKEQk9egbQaQscJhqlf9NpriEvM5yVS2fivo-eRc4xiTbDtn9Vyvtpv-rcU7fmcxlAaqTfprGUdtfsISlB_0zpeQfcVwqQgclVM8VuhEcUbWO1OwzBYZJI3KkeqX_4P7oO-q5qmPwpquZS2zQFUjZamF9R9jH6MN770mc_w8GZ0kkocshPXTdS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b9f4e618.mp4?token=tZpdqNs4eSVosiiBGnhwxSpjvf9dqjMxCVhck1hZ29jhnYHBqpdOwP8TrPlVFtLyo7xw_7VJ7BvkpOHRzWjgcFH3oi1uOCHwEOBOwRIajO5YQPBGu1w96ddMNeH1rPIPHD-jAMvjQ3XdlAT2MIYMUqG3PgTX-McKEQk9egbQaQscJhqlf9NpriEvM5yVS2fivo-eRc4xiTbDtn9Vyvtpv-rcU7fmcxlAaqTfprGUdtfsISlB_0zpeQfcVwqQgclVM8VuhEcUbWO1OwzBYZJI3KkeqX_4P7oO-q5qmPwpquZS2zQFUjZamF9R9jH6MN770mc_w8GZ0kkocshPXTdS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
تنها جامی که آنجلوتی از جام‌جهانی برد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98574" target="_blank">📅 17:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e9c60132.mp4?token=eSPzHR3n48fxpB_0hPmM3so36_Q8rl5xm-i6OHrEa-wub-tip9aMGINdYCjTsVMm4Lc2yW3Dqw0LYKSLNAxlI_VAWpkYQvDNCAXgEkk14rfy7ATrH0WFu_8KmIHZBXZa-RltBRTU5kWEgnriHGmPgHeSqR0tN4hxSO7rzu89GrEInvP6H8ro2h3YOsA-na7fYlfVTlFWfSjpjn6nMvAVYHqjk58DyqbJu39M5xjvkeb59DublISR1ab2raHw3x1OQppj2jXFW0Cy4_zNcJiYkl0vBXMWB6ASS8F2bR9UIaNYqPDu2htbRbBPJv_X8Z9qGs8n3y9x3WLUutrx-XFPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e9c60132.mp4?token=eSPzHR3n48fxpB_0hPmM3so36_Q8rl5xm-i6OHrEa-wub-tip9aMGINdYCjTsVMm4Lc2yW3Dqw0LYKSLNAxlI_VAWpkYQvDNCAXgEkk14rfy7ATrH0WFu_8KmIHZBXZa-RltBRTU5kWEgnriHGmPgHeSqR0tN4hxSO7rzu89GrEInvP6H8ro2h3YOsA-na7fYlfVTlFWfSjpjn6nMvAVYHqjk58DyqbJu39M5xjvkeb59DublISR1ab2raHw3x1OQppj2jXFW0Cy4_zNcJiYkl0vBXMWB6ASS8F2bR9UIaNYqPDu2htbRbBPJv_X8Z9qGs8n3y9x3WLUutrx-XFPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تفاوت گزارشگر عربی و فارسی در بازی دیشب بین مکزیک و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98573" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029dc7290d.mp4?token=fpLPGPrYyF8o0tKKnb5aRHH9WqobdshxA3OfSVRtgQUVlWor4ANZkgICQB-0Jk8zpL6uE1sMh9lXvF3bDa2uGvzcaGG5miNPj5WnD47Z-QPzHNytIVc5yw6hg3QycM5u-fL-uwUJ6AmN0WLAI3LUFO6D0VbDqNys2QcWnpG-X0GImoLXwB3Ith2G5gOFIioOcrn_o1HgYA6-2ZI0cMkvIZ2gpq6OPFHdBKwdNF0IAQpvcywR52rxmqyx1TfH0tyj0sjF_lz4anOrQIejG-MpkCsU6wW5jUjb5ywINrzSFudT50WFhskbf0NLYNfBh4eVaRf9lXDwCmD-eWlHhq6jQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029dc7290d.mp4?token=fpLPGPrYyF8o0tKKnb5aRHH9WqobdshxA3OfSVRtgQUVlWor4ANZkgICQB-0Jk8zpL6uE1sMh9lXvF3bDa2uGvzcaGG5miNPj5WnD47Z-QPzHNytIVc5yw6hg3QycM5u-fL-uwUJ6AmN0WLAI3LUFO6D0VbDqNys2QcWnpG-X0GImoLXwB3Ith2G5gOFIioOcrn_o1HgYA6-2ZI0cMkvIZ2gpq6OPFHdBKwdNF0IAQpvcywR52rxmqyx1TfH0tyj0sjF_lz4anOrQIejG-MpkCsU6wW5jUjb5ywINrzSFudT50WFhskbf0NLYNfBh4eVaRf9lXDwCmD-eWlHhq6jQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
زرنگی بازیکنان فرانسه در صحنه پنالتی جلو تیم اروگوئه با همکاری دمبله و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98572" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98569">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21007d5c7.mp4?token=hOhiDSYxphYfRmCthNAt2jME4k63UlFNqTOEZUOytbUASh7ADuGas7KrQXdnv6Rjagyg4gb3OapTR1iEjv36sc3mg0X4J4aiZ37piHnyXnPvOxzx_PmnFSy-MUhjzFJH_zOLpk2Ay5guKuEoE6ML0qFyY5oB8f1Y4FpDgZtNBCxvgvScCPo0NaYiFO6hL6YYDhHlCRZLGPAwNeoGeU8sfxlyL9Sl9jN7tpyDquxfqvNfWYQFM2nWjVir60kRa1fbqwuJ0598R2u8sYQszMZjWipyY__wcQSGXIohFqfnJ2H_jFGamWDd5EOSueILbwP6BWJM_lhLYGsgYPSmxsJ1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21007d5c7.mp4?token=hOhiDSYxphYfRmCthNAt2jME4k63UlFNqTOEZUOytbUASh7ADuGas7KrQXdnv6Rjagyg4gb3OapTR1iEjv36sc3mg0X4J4aiZ37piHnyXnPvOxzx_PmnFSy-MUhjzFJH_zOLpk2Ay5guKuEoE6ML0qFyY5oB8f1Y4FpDgZtNBCxvgvScCPo0NaYiFO6hL6YYDhHlCRZLGPAwNeoGeU8sfxlyL9Sl9jN7tpyDquxfqvNfWYQFM2nWjVir60kRa1fbqwuJ0598R2u8sYQszMZjWipyY__wcQSGXIohFqfnJ2H_jFGamWDd5EOSueILbwP6BWJM_lhLYGsgYPSmxsJ1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇴
تو پایتخت کلمبیا بعد جشن صعود به مرحله بعدی یه خانمی این‌شکلی سگ مست میاد وسط خیابون بالا تنه رو‌ لخت میکنه و تو حالت مستی با سر میره کف آسفالت
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98569" target="_blank">📅 16:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRj84uAAviySkvtMkJ0AjYtE5fKWyxm9SjAbijnuH4xgPQmgKjUCrZqj1goXdiHz5Nnn1_fXrTdOlGHzu2QmTVASv4of7EUlN8pMUmDCAa1hWAYHQkoDJP-VnqsZxWlvllmq7TGx2bEmCa-cho9tM8hDdCBOmuK_zDNBLDNhqSzIZbl1fkH-DP8xtCfMvvfglRoJlysJEwY4kemaxp5hzAV37xOsmHIScYF4g_OJUpox_M2KN-C1KYK2-beJ5_PskqCzBEVtKdF5h6Zg-yQ9_-Zh8utInVA34OHcK7HyXk4w4jb1rrf4Pvh0FXYmhndld8i90SJuBtyXXmrJf8z5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه لوئیس رسما به عنوان سرمربی موناکو انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98568" target="_blank">📅 15:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98567">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=UoBzsiwTWHTL_3wits3nCqGpybthtiwyFgxG7x0mxRLj70vISo5_EbuHWWccP-x7Z-UEkIKkhJKueunMyBVuYbJLmbH0oL39bjEElU7j1zWG8Rwtve1bMw6yRH9wkeCUvkToY_G27xvSfwEbr_VhbxKCNdHAYO7yINzjQp28s0lNsDIuuH3B6VHTDffHfMOeuvJQPzTv4OaqTHP2UPpZ0cHrYFEgy-uCpClFDrQAgeBsX6Nugnh8ymRLlKipoPtrT52lYruMDfw0YvXsU1QIBV55-wbhLRfp4-DuuG3TzcBqQBP2DOw8lVT7uInUizcEbgswngpaTbTWktKgVNJ6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=UoBzsiwTWHTL_3wits3nCqGpybthtiwyFgxG7x0mxRLj70vISo5_EbuHWWccP-x7Z-UEkIKkhJKueunMyBVuYbJLmbH0oL39bjEElU7j1zWG8Rwtve1bMw6yRH9wkeCUvkToY_G27xvSfwEbr_VhbxKCNdHAYO7yINzjQp28s0lNsDIuuH3B6VHTDffHfMOeuvJQPzTv4OaqTHP2UPpZ0cHrYFEgy-uCpClFDrQAgeBsX6Nugnh8ymRLlKipoPtrT52lYruMDfw0YvXsU1QIBV55-wbhLRfp4-DuuG3TzcBqQBP2DOw8lVT7uInUizcEbgswngpaTbTWktKgVNJ6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی برزیلی‌ها بعد شکست دیشب
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98567" target="_blank">📅 15:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgGIXUgXCnZni2gwJnckjVjTPNAsVvtWoFlJ9y4iL_f7RIQZ_0OPcu4NpcGCBhVtzZYn6_pRskaxfhz0T7hjUX4hJvQqixl39WkK2EOxaW5AWIcqLn8U-XfcSVHrZqChmrBwMz-_qPtReychzJoUUzsMTmCkSJrN6OaUoxLVMvoIWMQZdCoFYC00YQc53CuQ-5aUcJ3MlwyiYmJoEv8TkuXMAUabVhhNKMc6a0s2lBbSfi7t2Dq0LFHGuVqVzgqmV5_kxSJcbJlIhNbFwQy72BgniR-a7H7vuJlRb-dK-HER94kqsfgT0u9sLM-xG5SLUcTTFRzhAluk-yMbfg9guA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو:
کانگ این لی از پاریس سن ژرمن به اتلتیکو مادرید پیوست؛
HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98566" target="_blank">📅 15:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=u47PXxohTsmaq1EoVw0IuYiJ0EHuRQUVr7Vf071RzyUUIIi_IjtqTucqK78W73kZLz2dbVyqcVZg8C-bh5Qg_uWOwtzGmDHIu2s6-0P--9qnOpmYrgFHBgc2hE9-UrdHZxAL9IjK1PJJJ5xdjNLfYvAsLc6U9CP0d3sHw8ybjKauADr4xYu80a-SfUg7YajHzr1RxM3zZIm-6x2zdS-bh3Iyb1ZpMaWEAsR-0YQ5VedbZQXnqb7auDR1-8hAt9sJbkSAqomjZSkidDDScGxeqHIzlPKZ0m8C8sQussLec1jmmGnkXL3OEiq0bTx8nPoQ24sBa5isHc5ABmkyEgZEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=u47PXxohTsmaq1EoVw0IuYiJ0EHuRQUVr7Vf071RzyUUIIi_IjtqTucqK78W73kZLz2dbVyqcVZg8C-bh5Qg_uWOwtzGmDHIu2s6-0P--9qnOpmYrgFHBgc2hE9-UrdHZxAL9IjK1PJJJ5xdjNLfYvAsLc6U9CP0d3sHw8ybjKauADr4xYu80a-SfUg7YajHzr1RxM3zZIm-6x2zdS-bh3Iyb1ZpMaWEAsR-0YQ5VedbZQXnqb7auDR1-8hAt9sJbkSAqomjZSkidDDScGxeqHIzlPKZ0m8C8sQussLec1jmmGnkXL3OEiq0bTx8nPoQ24sBa5isHc5ABmkyEgZEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
دلیل انتخاب گیمارش بجای وینیسیوس برای زدن پنالتی از زبان کارلو آنچلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98565" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlMtebpHaH3132DvvEvTjMGvOXJ6bm2-jLxZexfP2fBJLN49l8RqtLL6G7vKcDc3ndsFG87jg9Q14OL0Pu0dl01dnXr-KGpVfejU1Uh9lOQJNGZuWmRo64yMJ0wpto1x5xQdmWEuZeWnVViiHstLDE5ZqOxUBs42lu8LzU5gsj_AA_eLJpICLcMrN7T8bLiXszQsDfcCo4P-E79_J2v5jp_EK_oDJpOgQ3VD90UqojEx4wMXg71YVrZI_GZYHFzZoJjyHiovXeykIzKc51FvkT7cZE_WUJApz08WvIbJhpHH_pd_BRndQiTJlVvgFhi4Vw0i3QSeUqDexStJT6_WXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oT6iG9MGdkSreyHYe6gXaI_LQ0q-kCDIV4J8muNjXn4S0gH2k1uMFTlOMFFTrILjzm-dvyMCWxnFeI3cRjbKGG4WxDGidFrslQr1o5KM4mBRco14lNRWFw0hmDKQ_XXAM-i4bEnEQbhYoBTvJLLRmvhw1igb-NofZ9oZMDgLiDKtTHhKqizCgoNh0iUkphg0Ly_y2jyXlPHu032C7DxuEBldHpOOzbXlD0VTsAQa_zBEW4T-4f90NCQquECc7tPmVAibFHLLB3vAl6MjC-DcX2-9PekWenGw4f4iWRUQPPlAJy2ChhmOzifJKbr3YUhZF9XCGwNQpSY1CI9sOLenog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
لوگو ناپولی برای فصل بعد به مناسبت 100 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98563" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98562" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98561" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=jgjK13AYbtRrxTxpreB21Fp9kknYxV2oruMDCJ5ps5LcuVytHuI0SHWOZ7hLM2AZzbR1KpskIhOPHSi6BccJyRHFcciUpEMcZ1KOTRS3mayHqEREiLeEu1Xt2Bu51k-Cryd1oO9XdtQ_w9RDOkjd7rwR71vEKgTwpsV-go6hOtQQID__xbPTvx5gmat6I3rmIg6pLmH1dBOG9IU7HjcE1Svm4PVrc9uz6T4kGvQY3-hKmBNdTv164orLIo5ESQuh3SmCHwrjzNMdpv2-gGPgcVWNpCojL4M9GGKjJX8_WjDBB9E6b5WLpq3WC2FoI-yATrmMP8r2sZtje5fJqamtng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=jgjK13AYbtRrxTxpreB21Fp9kknYxV2oruMDCJ5ps5LcuVytHuI0SHWOZ7hLM2AZzbR1KpskIhOPHSi6BccJyRHFcciUpEMcZ1KOTRS3mayHqEREiLeEu1Xt2Bu51k-Cryd1oO9XdtQ_w9RDOkjd7rwR71vEKgTwpsV-go6hOtQQID__xbPTvx5gmat6I3rmIg6pLmH1dBOG9IU7HjcE1Svm4PVrc9uz6T4kGvQY3-hKmBNdTv164orLIo5ESQuh3SmCHwrjzNMdpv2-gGPgcVWNpCojL4M9GGKjJX8_WjDBB9E6b5WLpq3WC2FoI-yATrmMP8r2sZtje5fJqamtng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
کثافت‌کاری رودری تو تمرین اسپانیا که یامال حالش بهم خورد نزدیک بود کونش بذاره
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98560" target="_blank">📅 14:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=Ho4ZkNbfwoEGcUUTkmO9ny5lsUZ1Lt-CXmszkJPBL9sjgYuPKgtTE5t08Jljgl49hSilPm-xyuv3zwYFuY7u1tgA1cz02Zwv22pbRHe-rB9JwA8nF0tos5VJa2e3RftlHX_XcQU-i5Sr1FmsyZbKCdWiWDbc2OQmrYlu3jecb6147SdlcpstezvYqfumDpEJ-XoAgleqWvpcr0g5W4fL4yfzKIOfpA51K96cbgpcYK8SUPqO7iyBxrts-8irgjp1FYdCaBB1BmXH-HkpVEpKvz9R4P3CHQwklzm7t1kjILF8bsMxqFIOBxWgk9NhiuaSCIpI7mci_4ir80b7fn1EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=Ho4ZkNbfwoEGcUUTkmO9ny5lsUZ1Lt-CXmszkJPBL9sjgYuPKgtTE5t08Jljgl49hSilPm-xyuv3zwYFuY7u1tgA1cz02Zwv22pbRHe-rB9JwA8nF0tos5VJa2e3RftlHX_XcQU-i5Sr1FmsyZbKCdWiWDbc2OQmrYlu3jecb6147SdlcpstezvYqfumDpEJ-XoAgleqWvpcr0g5W4fL4yfzKIOfpA51K96cbgpcYK8SUPqO7iyBxrts-8irgjp1FYdCaBB1BmXH-HkpVEpKvz9R4P3CHQwklzm7t1kjILF8bsMxqFIOBxWgk9NhiuaSCIpI7mci_4ir80b7fn1EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
ابتدا، او به عنوان داوطلب وارد زمین بازی شد تا پرچم آرژانتین را برافراشته کند. چند دقیقه بعد، در حین پخش سرود ملی، دوربین‌ها او را در حال خواندن هر بخش از سرود با احساسی که همه را تحت تاثیر قرار داد، نشان داد. و در پایان، او مانند یک هوادار دیگر، تیم ملی را تشویق و دلگرم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98559" target="_blank">📅 14:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRMjMwpb6BhOVXWGbd4JLIaSh8WdNhHz6L4Y4LlQVL8N0wY0BNfuJyGGNhOki8UVzXLt8psC_grHuoubqWQc6NYL6MnXRqLkJrjHDvpm4DaJufsTtqwRhw2jUkcTrgN25pRkFbjONPEmwoeJdxTNboTOYB23ue5CLBXcHmHYoJ7jhzoZOnAH6qO6AuMtst751gk2iQsHzZqu3GPinwFHlveaRsZr32TusKRS4QOPTe67o1uUsmEhJUoBi4E9LSaFzxFclmhLQX5OlVr7c2ADkmlR89_66jHDYXqkWOazlTPGkJO4Lxm8VqQcs_IKVAOUyIRnUgcrx94SkAV0MRKFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
فلوریان پلتنبرگ: آرنه‌اسلوت گزینه جدی سرمربیگری تیم‌ملی هلند است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98558" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=Msmsva_c7ChV77mzMb-7fBl8EVKYXiKDPYXugj8jE9aSnYNLdfp7hMlC6aZBjzEcPfLIRkHEBLZ7pgn7j2ijc-huXKqnsxazWnX9xcJoIyokU9M9OECa8VhRuj8-0r4cdLsblB1RANvH8PYK8WfjviBAbKTZPl0EVXRXsXtudeyeoBTlLIY8JcmNe6S9U5t6JrBG6CaiNzLBjmTI5s5NmXkeOJkEw2GK2TFlvtuWbII0hLu5m6BEq6guLmdYBLWFpJ5odmLa-XP3NBn1QhE-rMAfCPy8BrMedcTddwQvO_pOj7SzNcgC_5_THXmFwkD_nAaOdR32SHz98ydfg5ny0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=Msmsva_c7ChV77mzMb-7fBl8EVKYXiKDPYXugj8jE9aSnYNLdfp7hMlC6aZBjzEcPfLIRkHEBLZ7pgn7j2ijc-huXKqnsxazWnX9xcJoIyokU9M9OECa8VhRuj8-0r4cdLsblB1RANvH8PYK8WfjviBAbKTZPl0EVXRXsXtudeyeoBTlLIY8JcmNe6S9U5t6JrBG6CaiNzLBjmTI5s5NmXkeOJkEw2GK2TFlvtuWbII0hLu5m6BEq6guLmdYBLWFpJ5odmLa-XP3NBn1QhE-rMAfCPy8BrMedcTddwQvO_pOj7SzNcgC_5_THXmFwkD_nAaOdR32SHz98ydfg5ny0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
فیفا تصمیم دارد تیم‌ملی پاراگوئه بدلیل نقض بازی جوانمردانه در بازی با فرانسه، جریمه مالی سنگینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98557" target="_blank">📅 14:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98556">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=KP7KX_DufFGPOLnL5XztSDB8npvwyEBCHTekE_6NZqcXc5ny-Uc-6BEV0zO24t68uTXLSPwO4RZ_cf67UjxP2nEIQ4JTAim94qyVm5l_d0o5de_mRVdxFfbRvvfrydM0AsGaRK877oYskmFKlSgv1EywpbPkaWrWRfOLjFK4kLkVs9vIli4RzJP9XRRNxgZ2mM5CMXcTEVdvMtZzIFsk5MR41kEwKsaf0DUqtaET4goyn88ROclH3OWOTf5VTw5bbeadZeiljeIjoZjI49Fe3qkgqhFImB5kKslpN8DkqZMSphFNAgv0U64uK6kawj4F7CaUvb0hYuf0-jl3G9z9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=KP7KX_DufFGPOLnL5XztSDB8npvwyEBCHTekE_6NZqcXc5ny-Uc-6BEV0zO24t68uTXLSPwO4RZ_cf67UjxP2nEIQ4JTAim94qyVm5l_d0o5de_mRVdxFfbRvvfrydM0AsGaRK877oYskmFKlSgv1EywpbPkaWrWRfOLjFK4kLkVs9vIli4RzJP9XRRNxgZ2mM5CMXcTEVdvMtZzIFsk5MR41kEwKsaf0DUqtaET4goyn88ROclH3OWOTf5VTw5bbeadZeiljeIjoZjI49Fe3qkgqhFImB5kKslpN8DkqZMSphFNAgv0U64uK6kawj4F7CaUvb0hYuf0-jl3G9z9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات دیدن فوتبال با گزارش عربی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98556" target="_blank">📅 14:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChdTaPQN77_x7qDpDK8DqA315a6XRNFYfDo0gqI7mdFLvZ-GX1MdgqoPRSdLNVq19nP3LhuO0wwX1s7goxnJi0vKi2Qm0GhAcCrJ1jVB3H6h8e5JBMp4o_NLIuDmEZae8UIhqiUalfQXdcynTTX-aU3TZ7fBaGVpcXHDHbXdZWNnFWimvPjgx1SCI6XiElOMFE_a3Wp-RcNtIPro5FexMhwaCRCnsObLNoQvtoEFoaJsrDOTxTB7I3dHfGyQ0EQrmqF3PMPr5nal6YiRFxbaApCV43aZfpJOy7PUimx7D801rWQfGEPnQmNiHrGup58YKraVMtPlochCQn4siX-nNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس‌توخل درباره قضاوت علیرضا فغانی: فکر می‌کنم قضاوت داور بسیار ضعیف بود و همه سوت‌هایی که زد علیه انگلیس بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98555" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=TZAPSuLAFUtMvs2vIQ3vDCU0pJ6pAJSQWhONSAJgk304grB5W8qv68M6NSa4sorzZgWtpRynhEgFfir61ajOUvpk5vWxzo4wi2XsmwIAKs08uEoD8P5V11SEv2WK6Hjhf1rPHx1FqYSa40IOVxawNXjk19MMTStaJU6huDMkTi1z_0-OfXm1kA7UrmakFKosAh6j3f_slQsQ3iESMJ-NiNiGaYXWPVTAF3nOwmodpuKF5jnJA5ywBLXNJuJWWpenNgjMjBMMrDseIi7KFhEu9jO-lRVeGIXVPG5aBhxQn9wB4tqM6_SEDy5RWS_amUhAY0-W0MR6L-b5t5ez_7MnF622xcKXS7MjjjSh16BdJ1h90djK7bDCUd-bXHAH8K01UyD0oK_7GqfNRR5jr_0wGihPBe513MDlNx8Fejlk4wXul9lc2xLUmYFYGUzm8as1AoHN0dGgOWoed2gfuf5FZZCbgvwdr19EiCBL8xc42lK4HIjx2QTMFOFhFv1mN_QzSIBU_wqZVE7Q2vGCKAnZzjQTYdrFlZADR0uXSSU7hwILyL4eCRNLiafjLMFeLH3Vv7YuD9SpQvoMbmi7ajYl_vXqrhwiuSClHL3Sl_sHKIqoKlxgu5p0UDOSA9llYyYffDSVZTBOd7p1mZXBI5ybl15JLD7sd3IAUnfqAk1Jrh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=TZAPSuLAFUtMvs2vIQ3vDCU0pJ6pAJSQWhONSAJgk304grB5W8qv68M6NSa4sorzZgWtpRynhEgFfir61ajOUvpk5vWxzo4wi2XsmwIAKs08uEoD8P5V11SEv2WK6Hjhf1rPHx1FqYSa40IOVxawNXjk19MMTStaJU6huDMkTi1z_0-OfXm1kA7UrmakFKosAh6j3f_slQsQ3iESMJ-NiNiGaYXWPVTAF3nOwmodpuKF5jnJA5ywBLXNJuJWWpenNgjMjBMMrDseIi7KFhEu9jO-lRVeGIXVPG5aBhxQn9wB4tqM6_SEDy5RWS_amUhAY0-W0MR6L-b5t5ez_7MnF622xcKXS7MjjjSh16BdJ1h90djK7bDCUd-bXHAH8K01UyD0oK_7GqfNRR5jr_0wGihPBe513MDlNx8Fejlk4wXul9lc2xLUmYFYGUzm8as1AoHN0dGgOWoed2gfuf5FZZCbgvwdr19EiCBL8xc42lK4HIjx2QTMFOFhFv1mN_QzSIBU_wqZVE7Q2vGCKAnZzjQTYdrFlZADR0uXSSU7hwILyL4eCRNLiafjLMFeLH3Vv7YuD9SpQvoMbmi7ajYl_vXqrhwiuSClHL3Sl_sHKIqoKlxgu5p0UDOSA9llYyYffDSVZTBOd7p1mZXBI5ybl15JLD7sd3IAUnfqAk1Jrh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گوستاوو آلفارو سرمربی تیم‌ملی پاراگوئه: با انجام بازی خشن جلو فرانسه، میخواستم یک انقلاب را در مردم‌ پاراگوئه امتحان کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98554" target="_blank">📅 13:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afvOV5PnABY0QBq1RgaGcdEK8kN-R7eaaVOK3BT4G0sM7bCf_Ng1sMYROj_MIBsrmm2l9id-lAZvW_w9xrPA2wv1xssdN7wlnYXLirnQKRinehhu90_8hjqO0aSIBc9LjOomb9PI3u2hIsyGnXS-7zeiSqMhj2hBhKwolgO32c2mW_ihP-_y1kpAGS7sGmIMwEbf_FQ4N29rTc8Wl1LixiSoHN9YbEmpWoeAaWXpetIyhoVMhhya8lJa8betxLpH8mNcXECWhw1ky9eKHtsnrGStvakssjEQHTiT2tkHgo3QFXDK4Rigk-xTaCYpbkE295WN21VF1aUbWujgG-wWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاتنهام از جذب ساندرو تونالی از نیوکاسل به مبلغ 100 میلیون پوند با بند تمدید قرارداد تا سال 2032 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98553" target="_blank">📅 13:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98552" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98551">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=tIODs3iETqK7S4eiKxYX86ai9MJCyv21SgCSDfrvViSzLOPKVARU2YkWz8UYR_woy3c2zN-wVl4tiGnjIfskwCUFrHPxTgTa7FiIxJ4n_DA0exAltGBIX4dVXnW6C7JIkZxLFknG7ciZRRMPZVNHHgL_fBRui3bTgyKfoMU_SwuvP2FZyfVmGFUSvqggUZ5dBTAVbvmCt5nUZW21yr3lczVY11f7u9fz7n-89DixzaxM0zYsNpK1wqCcVb5rY3B_j_oOwjYv9FH2ZC2Dcn5-gUnOwVeg0AH-JoV5gtxxmnLbjvJxMKwYiV2_1WXtdQqIoOLX-TM5qq-J9dbxGqJpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=tIODs3iETqK7S4eiKxYX86ai9MJCyv21SgCSDfrvViSzLOPKVARU2YkWz8UYR_woy3c2zN-wVl4tiGnjIfskwCUFrHPxTgTa7FiIxJ4n_DA0exAltGBIX4dVXnW6C7JIkZxLFknG7ciZRRMPZVNHHgL_fBRui3bTgyKfoMU_SwuvP2FZyfVmGFUSvqggUZ5dBTAVbvmCt5nUZW21yr3lczVY11f7u9fz7n-89DixzaxM0zYsNpK1wqCcVb5rY3B_j_oOwjYv9FH2ZC2Dcn5-gUnOwVeg0AH-JoV5gtxxmnLbjvJxMKwYiV2_1WXtdQqIoOLX-TM5qq-J9dbxGqJpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحنه مصدومیت دیشب هندرسون از این زاویه که احتمالا ادامه جام‌جهانی غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98551" target="_blank">📅 13:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=blXlulK5jg2IhfglIM-BpZICJulOuTfXMaXM8FHyPBxhyI7EUDqyCoBga8Bc1DIKAfIfur2z12CneJf3VOM4xQM15HNjurh6aUUGMbaYkZG_dpVfD0RP1qZ6z671rF669Al_HesnPVB-Ot7Z4KEb7SYGxR43riiCt2xng9qwQndmoDYho4V0p6TM_NWY7NUaGNFolG6b39vW9bqLehwC-UX-1YdSbGpGgsgfLzm4S54SSTvCoG16s6EjZ6yrtF9plrhEByPxIr-k4PbCR1U0BtF5cFky41CR64--pWLHGTDoXJusm5acid7XqgndfMS3XevRgm3zwZfJTiV_djD67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=blXlulK5jg2IhfglIM-BpZICJulOuTfXMaXM8FHyPBxhyI7EUDqyCoBga8Bc1DIKAfIfur2z12CneJf3VOM4xQM15HNjurh6aUUGMbaYkZG_dpVfD0RP1qZ6z671rF669Al_HesnPVB-Ot7Z4KEb7SYGxR43riiCt2xng9qwQndmoDYho4V0p6TM_NWY7NUaGNFolG6b39vW9bqLehwC-UX-1YdSbGpGgsgfLzm4S54SSTvCoG16s6EjZ6yrtF9plrhEByPxIr-k4PbCR1U0BtF5cFky41CR64--pWLHGTDoXJusm5acid7XqgndfMS3XevRgm3zwZfJTiV_djD67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر ابوطالب درباره حضور احتمالی ژاوی روی نیمکت ایران بجای امیر قلعه‌نویی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98550" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=nAElG_LuXL_6D7cDEIlb3o3UfGNMaf78iOMOf0KQF76vCVHcFTALnuJJqeXJ-z7hpMadfHKej8Gazzc_uJttf4kXSS0o-y_SYj-LdLInDSkRlrEzAG8QplmxpskxxKu1BwZIA_qAdVDF35xGnbVBmJ7bT-7w82kG4eUVd8QVYk-1m8k-bRigh8PRJJAu64tkf0LDbE9gxYLBdOMojq-A2qTupfKAPzgHlmbgaTpfUCc94h44fREcYpNqohf3q0Mgz-84tO3j0rlpOtvU_c7Iv-E3f_ITonBBBKivU39odcGUWubBfzrpkqO2BQYfpCSxrqfcYi2ILAD03bWSLXwUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=nAElG_LuXL_6D7cDEIlb3o3UfGNMaf78iOMOf0KQF76vCVHcFTALnuJJqeXJ-z7hpMadfHKej8Gazzc_uJttf4kXSS0o-y_SYj-LdLInDSkRlrEzAG8QplmxpskxxKu1BwZIA_qAdVDF35xGnbVBmJ7bT-7w82kG4eUVd8QVYk-1m8k-bRigh8PRJJAu64tkf0LDbE9gxYLBdOMojq-A2qTupfKAPzgHlmbgaTpfUCc94h44fREcYpNqohf3q0Mgz-84tO3j0rlpOtvU_c7Iv-E3f_ITonBBBKivU39odcGUWubBfzrpkqO2BQYfpCSxrqfcYi2ILAD03bWSLXwUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
🇲🇦
بازهم تقابل دیدنی فرانسه و مراکش در جام‌جهانی اینبار مرحله ¼نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98549" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVWNpbkna7uw6agWPjqVvTqwoNFcuOuFR3hlEXSG2KaeVVsaXUIKnB2ZJ8afBWbDatcSQAphPkXiiHIxsP8MQTWJwePl5uTdDgiEdMUXDVjXiP5fhqyqBb40quI4GXn3Gw134ZE1a45YFk6XoCsb4LsMAkepmxqOOo7ehg76m9CZffD31Rpj-epsChgqUKSNrTxmeIJixX1QlHso6I14aCMDhFFgonA1HSJf6mJ-_IFKa1leMkVyzSg0DTotb3m-TG_2dOUUA6H2LPA49ckqhw9V15wzMUqJ6K0V6Z8K-zWAVHMLTGti4Pits7p0dROyZS0hnc4vIqhMoJslJ0ltNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلاسنر سرمربی فصل‌گذشته کریستال‌پالاس هدایت ناتینگهام فارست را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98548" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=hf6O6RQzvCUfrPgLnBYXEchK-x0_-a96i84tLhxncpYFdl1F2YhJ1h2kYC39D1fC0ibHImNYAqSk9i3gC-C47eQ-I-K-4J4PEkd3GPFEvH6qy2S6ohJJC335ToijlQB5Wy9f274YoXSje77SlwpSyVbGbu0tNv-rFrsmCJR3JHZ36-oHphG3AA7yks2jxrkonMEa0dAvJcXV0rW93gFgO0dDIAvSS5jb0hmOW_03o_6h6p-YzNFn9hXR4LjLaFnLp3bhz-pcWHEe0HENdQhwcKW1ow6t4ef8QSNaRAkuDOXWGmGphwmOGTqxJyrZ9cP_IoSW4UXZWfgZX2sJyZDntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=hf6O6RQzvCUfrPgLnBYXEchK-x0_-a96i84tLhxncpYFdl1F2YhJ1h2kYC39D1fC0ibHImNYAqSk9i3gC-C47eQ-I-K-4J4PEkd3GPFEvH6qy2S6ohJJC335ToijlQB5Wy9f274YoXSje77SlwpSyVbGbu0tNv-rFrsmCJR3JHZ36-oHphG3AA7yks2jxrkonMEa0dAvJcXV0rW93gFgO0dDIAvSS5jb0hmOW_03o_6h6p-YzNFn9hXR4LjLaFnLp3bhz-pcWHEe0HENdQhwcKW1ow6t4ef8QSNaRAkuDOXWGmGphwmOGTqxJyrZ9cP_IoSW4UXZWfgZX2sJyZDntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
شادی مردم نروژ پس از صعود به مرحله ¼ نهایی جام‌جهانی؛ آدم واقعا حسرت میخوره...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98547" target="_blank">📅 12:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effa95670e.mp4?token=AH7KgAclnv-mv7DDYjeLIa_zYjadkC7PMOVCgCeeGuc4J_FgoaU9cVIBwftl1prZkV7GePyohedLeHfHge9hTMNLHRmxeRldNMCrYPpru7shmOg2sTKWGpW81EyfNB7Io-KGbI6Qsq-eM9ii5MdtybN7Y-7pJXiBKPVOHUwQzVn3A95RlfJAAQpkjX8WIsxYhxI3B8wTLO6O0YYUH7iapvJp_4A1m1xs244idHkuN1-Dcljjm2etQkjInFqLawuA4gf_QKm7qHfKiwG53CeCnywtWj28N8dOosuGHxqetEiDLcAHCVNPbWMVkdi-QirxnJ1JJHmFRZUTiACGLwb9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effa95670e.mp4?token=AH7KgAclnv-mv7DDYjeLIa_zYjadkC7PMOVCgCeeGuc4J_FgoaU9cVIBwftl1prZkV7GePyohedLeHfHge9hTMNLHRmxeRldNMCrYPpru7shmOg2sTKWGpW81EyfNB7Io-KGbI6Qsq-eM9ii5MdtybN7Y-7pJXiBKPVOHUwQzVn3A95RlfJAAQpkjX8WIsxYhxI3B8wTLO6O0YYUH7iapvJp_4A1m1xs244idHkuN1-Dcljjm2etQkjInFqLawuA4gf_QKm7qHfKiwG53CeCnywtWj28N8dOosuGHxqetEiDLcAHCVNPbWMVkdi-QirxnJ1JJHmFRZUTiACGLwb9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نروژ رقیب خودش در یک چهارم نهایی رو شناخت: انگلیس!
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98546" target="_blank">📅 12:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=Ct0y4JgEDQ0xiUiDlrToiqoWAr5vc6F0rhiyF9Gh75o_6sdRECrEELbH8ZfWjjKRnkCXi83651Ubm0685qOre9aBmPMfHcFtmbTaUDd9zQidd4n0mXLYXeEu3RzJ46XXj5UMJK5r_tk_csQUBqnVxNq-YT08VnFi2v6vlQrsaMPlt6UYYK-VKJX39SoOBPlRQ_3LXcgskGONalL0IYYWQNKElCdP3737NvV_z1NDBeLV2rXq3qP152XStCVrCwyjQAnyrsB4C5uJn8kxdN7K6tyDhM-chqKDUQA9Ymiuu9-A7BFZ2PtZIxox-rd603ghsfTV8wlKy39HOCNdOCSCDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=Ct0y4JgEDQ0xiUiDlrToiqoWAr5vc6F0rhiyF9Gh75o_6sdRECrEELbH8ZfWjjKRnkCXi83651Ubm0685qOre9aBmPMfHcFtmbTaUDd9zQidd4n0mXLYXeEu3RzJ46XXj5UMJK5r_tk_csQUBqnVxNq-YT08VnFi2v6vlQrsaMPlt6UYYK-VKJX39SoOBPlRQ_3LXcgskGONalL0IYYWQNKElCdP3737NvV_z1NDBeLV2rXq3qP152XStCVrCwyjQAnyrsB4C5uJn8kxdN7K6tyDhM-chqKDUQA9Ymiuu9-A7BFZ2PtZIxox-rd603ghsfTV8wlKy39HOCNdOCSCDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
خلاصه که هیچ‌مهاجمی نمیتونه مثل رونالدو اورجینال باشه و گلر رو دریبل بزنه. اندریک و بقیه تازه انگشت کوچیکه اسطوره برزیل هم نمیشن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98545" target="_blank">📅 11:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QueeZ4Et2gwB3H1rp3bEDXD511UV6UDvfZK1hVncUb3getXFe5jEQePf7bD_TpeaTo-wN6PFHRwsqBI6FASlLkjtVFFQvKVCJiIzuXk0uqux0oOcUgf8sfg-k06hSLnZrRjzepmZUIroyfU7C3dLCSzowO7oLTD6IQMgFENU3olwbzBizoX_PKuLli_ZFZaNAr69Db2dUYf-NriE5wk2DcT4f6ZqI98ZRzzdR4KM1GdfHFxUiqNFoWXMHzx8EjW5N32KXF5bFkdJ43QuhdypxB2jjFDMLY0cYmL1MTfsuBmrcobA9nrqdBJzK4biSoUEHGtslzfMZ3U-UJCSdIOZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇧🇪
بیانیه فدراسیون فوتبال بلژیک: لغو کارت قرمز بازیکن تیم‌ملی آمریکا در آستانه بازی امشب نمونه واضح از نقض آشکار بازی جوانمردانه و دخالت قدرت‌های سیاسی و نفوذ در فیفا است. شدیدا این تصمیم را محکوم کرده و پیگیری این مسئله را ادامه می‌دهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98544" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f91878075.mp4?token=lm8jEOXLLFxFaK7LEmddDqbMoUoucmaGdErfRGUdqI0I0_mtKVee0hA9TiV3x7abkK91qmXqsl3T00Ct6YYXurpnT6K9ApAGBQy1X1xu9nvA4tsGRcqb0Y0KxPSccw0ppLqBRZwRI9WPk9oH9s6zj20n51tHzGCMsQXOG63ySCbjvj3ppuFFdlSPetrPMDoRBJlSsPxlD9TPMtSbNToDH5nkH_p1w2J2kjEwnSLbParEyFfZk8P88vHbE2FTzd_cyhHXmAFfleeJE-X1qDk6-5DbgIrk_5mGknbZ54hAEiq_Tsarb54SVad_ertBF0V_pC2wL05fqYgYRiXJdmfREA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f91878075.mp4?token=lm8jEOXLLFxFaK7LEmddDqbMoUoucmaGdErfRGUdqI0I0_mtKVee0hA9TiV3x7abkK91qmXqsl3T00Ct6YYXurpnT6K9ApAGBQy1X1xu9nvA4tsGRcqb0Y0KxPSccw0ppLqBRZwRI9WPk9oH9s6zj20n51tHzGCMsQXOG63ySCbjvj3ppuFFdlSPetrPMDoRBJlSsPxlD9TPMtSbNToDH5nkH_p1w2J2kjEwnSLbParEyFfZk8P88vHbE2FTzd_cyhHXmAFfleeJE-X1qDk6-5DbgIrk_5mGknbZ54hAEiq_Tsarb54SVad_ertBF0V_pC2wL05fqYgYRiXJdmfREA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🙂
خلاصه اتفاقات دو روز اخیر جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98543" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=V5mD_iFlZXi_CLhmk8N-oSKLL4DyF725f3dfWprK3LvkfgWBNHiD1eh1_snmkDG9lxzTA1T6keZPLOJcyTpkc6z9tnUh1wMgm3zhhYrCSr_Nxx2YTGYtlNnzs5KUE4_dgOH7gOx0inqnKtYEPMsV5oNgdkLhob8G88JITu01vwC-6XksNTGcDLGrHVv4dFvMJAHHxvZ5RWKwRtpDBeb9gNEVSjDhxDdGdKJcc7XSWDP8PTTZKww3Ra8RfxM5vmUUzYCVUsT1kRzLNrjdzxciQwDYOgwsn3kr6jNig-Nsr_l54WG6vPEmozQl9uE-7_vDigiQokobEtqOU97xO0cMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=V5mD_iFlZXi_CLhmk8N-oSKLL4DyF725f3dfWprK3LvkfgWBNHiD1eh1_snmkDG9lxzTA1T6keZPLOJcyTpkc6z9tnUh1wMgm3zhhYrCSr_Nxx2YTGYtlNnzs5KUE4_dgOH7gOx0inqnKtYEPMsV5oNgdkLhob8G88JITu01vwC-6XksNTGcDLGrHVv4dFvMJAHHxvZ5RWKwRtpDBeb9gNEVSjDhxDdGdKJcc7XSWDP8PTTZKww3Ra8RfxM5vmUUzYCVUsT1kRzLNrjdzxciQwDYOgwsn3kr6jNig-Nsr_l54WG6vPEmozQl9uE-7_vDigiQokobEtqOU97xO0cMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
پشت صحنه‌ حماسه‌ای که دیشب اساتید فیفا در بخشش بازیکن آمریکا رقم زدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98542" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98541">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=JHNdfi2PViRhCfRjnFGcUNOO2u0UFaGxXmyncs6B1BTT2jHeZSpWUbVTlfmZHl0G3qKUobctXRLBNRzZsy6B1LLTmlgA54lkim7kjxLttlmnItmGemDek6CSgZQbRiVHslkZxdax4tCbTtkFs5n2PyzoAEHvnr2kJzzB-55hrs8o4uQHO6F_Xq7BP3Fte6TqIfTgD__Br2wB1OS5hq-s0kA4vwm9Zy2ZIocg4jMZvAynoIbVyeJSRrSvAEWHMir80WQXB2xI56GtBxDQhlOieoMAmxuF5ZMF8S_FMAwADKa4tT0FLOX3dn39lxxiN0DGFbQPrOkTlSNXJzRWYYkiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=JHNdfi2PViRhCfRjnFGcUNOO2u0UFaGxXmyncs6B1BTT2jHeZSpWUbVTlfmZHl0G3qKUobctXRLBNRzZsy6B1LLTmlgA54lkim7kjxLttlmnItmGemDek6CSgZQbRiVHslkZxdax4tCbTtkFs5n2PyzoAEHvnr2kJzzB-55hrs8o4uQHO6F_Xq7BP3Fte6TqIfTgD__Br2wB1OS5hq-s0kA4vwm9Zy2ZIocg4jMZvAynoIbVyeJSRrSvAEWHMir80WQXB2xI56GtBxDQhlOieoMAmxuF5ZMF8S_FMAwADKa4tT0FLOX3dn39lxxiN0DGFbQPrOkTlSNXJzRWYYkiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇧🇷
توصیف‌های عادل‌فردوسی‌پور از نیمار...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98541" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f587817b79.mp4?token=kJ0-fXq9SY5m_VSxJrHVchDhYTG6HAJ0SPoPg8d5qQS2ig4gknp80OfI1HxK8I2V7ldfYn60sKWwq7JCtJzpgTJgXL6ykbtydtmv47zxsRg88r83mjpqw5EqNUG5Dkwj0r21kSrsfpxuBdZU4s27w9280OwvX2_eiuwq7DYwKh_JgIEX11-agsKAhCox18XleB60Lb-djM-uaR9iI07bJvz0j-XIxm3lyAquV-u438dt9jUXbepOQsdw4GxLXJcZc5ZRXHT46itXBF8VUsjJGsaMz-zmWrD7UDdVaYnwOueWYr3G-_GDQn2-ARlebpTf-VBwDsBWgE9lctVjnP_E9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f587817b79.mp4?token=kJ0-fXq9SY5m_VSxJrHVchDhYTG6HAJ0SPoPg8d5qQS2ig4gknp80OfI1HxK8I2V7ldfYn60sKWwq7JCtJzpgTJgXL6ykbtydtmv47zxsRg88r83mjpqw5EqNUG5Dkwj0r21kSrsfpxuBdZU4s27w9280OwvX2_eiuwq7DYwKh_JgIEX11-agsKAhCox18XleB60Lb-djM-uaR9iI07bJvz0j-XIxm3lyAquV-u438dt9jUXbepOQsdw4GxLXJcZc5ZRXHT46itXBF8VUsjJGsaMz-zmWrD7UDdVaYnwOueWYr3G-_GDQn2-ARlebpTf-VBwDsBWgE9lctVjnP_E9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇴
خانواده سلطنتی نروژ دیشب بعد بازی با برزیل برای تقدیر از بازیکنان کشورشون وارد رختکن شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98540" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=kfXvfjJmkeEajlgzrGBySlrtBu8LilHndTg7Ifucxpreo0ZTjeRUBGuPHvz8z8eyYUmyGggQXY0pzJd76MEof0i-RrbKay4fZ46Led277DUUMdYth3So9x8GHkj0sQ5UZl7Se0A4v9CNg5PYchHQIJD8qFxuXVKttNZS6Hc8771auZXc9bZ0stK0a6ROxH9igXUnS3MGVXQvr8WXoltsW6ZirQxLrZw7ca8oj_IMU1bE0njBNn6bPX_838B5veVNYoGwHTgTFgiNgZsNAZxrF1lm7R5CKbnGA44P7BRHXGHrcC8Cv4pCvsNvg1J55AFHM4EmOXX6cNgjWeulgU_5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=kfXvfjJmkeEajlgzrGBySlrtBu8LilHndTg7Ifucxpreo0ZTjeRUBGuPHvz8z8eyYUmyGggQXY0pzJd76MEof0i-RrbKay4fZ46Led277DUUMdYth3So9x8GHkj0sQ5UZl7Se0A4v9CNg5PYchHQIJD8qFxuXVKttNZS6Hc8771auZXc9bZ0stK0a6ROxH9igXUnS3MGVXQvr8WXoltsW6ZirQxLrZw7ca8oj_IMU1bE0njBNn6bPX_838B5veVNYoGwHTgTFgiNgZsNAZxrF1lm7R5CKbnGA44P7BRHXGHrcC8Cv4pCvsNvg1J55AFHM4EmOXX6cNgjWeulgU_5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف برزیل از جام جهانی به دست نروژ.
🇳🇴
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98539" target="_blank">📅 10:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=iAH-rqC2NWW0Jtw_Dltp38lPtT2r181ydQB8bDGnO86deSlxtyk-eR9ut95OmxS8ymvoGZ7TD1z8Y35Wchvb9KGATy7evQP9xRuxwg4UNGfH94pBapi25VSfI05ZK6l9lVp-e5XJiENtSjUPiqDRDejX_PrFfPYHQR3JMigZXBs8nBbrb2KHRjR0ARLDGBpCWBBJjLA_VrEA-K0UWwFNgoCVrrZyaBmJgw4CafiRXJuFZTFfreSOjl3x3Kby18WkDPqq3BuEFDPn0Dmntoz9Pbm-E0wglI-8t7vZ1XMCbSSP7MemI3Aq7JrJarSZNuaOZBey1CuPwUPivD_w6dUAaGiy_W5lEo1vzZeNPX_TLCyLNIcJqfsJg3IeCyFj8NJ7YodvbNmSEKvFJafN3ePay3-z6j1xBJahiPURUTsvQ8iXy7ZzJX9cpT0BomqQ0gcr_tU2mShn0mtL-DfvM9dSHf6F1UxpoqM-eUjZr3FhFO2CsJqDJ44ulC0kyvqvlN45KR6TciNxwYH8VBRZBxe-pE3HLwd64GY-NWWqP2w9r63UZJCHHCkhOttXpsA8kZWzB-EA84AGG5RCDXYqzDXVEif0grhBv6H0CAKfQ42Qjpu6SQNr_VGitWSuypkv3kLQsUXmocZe5CHeCS0AUm3ibwqesDsKTIBykZsn1TxbWH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=iAH-rqC2NWW0Jtw_Dltp38lPtT2r181ydQB8bDGnO86deSlxtyk-eR9ut95OmxS8ymvoGZ7TD1z8Y35Wchvb9KGATy7evQP9xRuxwg4UNGfH94pBapi25VSfI05ZK6l9lVp-e5XJiENtSjUPiqDRDejX_PrFfPYHQR3JMigZXBs8nBbrb2KHRjR0ARLDGBpCWBBJjLA_VrEA-K0UWwFNgoCVrrZyaBmJgw4CafiRXJuFZTFfreSOjl3x3Kby18WkDPqq3BuEFDPn0Dmntoz9Pbm-E0wglI-8t7vZ1XMCbSSP7MemI3Aq7JrJarSZNuaOZBey1CuPwUPivD_w6dUAaGiy_W5lEo1vzZeNPX_TLCyLNIcJqfsJg3IeCyFj8NJ7YodvbNmSEKvFJafN3ePay3-z6j1xBJahiPURUTsvQ8iXy7ZzJX9cpT0BomqQ0gcr_tU2mShn0mtL-DfvM9dSHf6F1UxpoqM-eUjZr3FhFO2CsJqDJ44ulC0kyvqvlN45KR6TciNxwYH8VBRZBxe-pE3HLwd64GY-NWWqP2w9r63UZJCHHCkhOttXpsA8kZWzB-EA84AGG5RCDXYqzDXVEif0grhBv6H0CAKfQ42Qjpu6SQNr_VGitWSuypkv3kLQsUXmocZe5CHeCS0AUm3ibwqesDsKTIBykZsn1TxbWH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
هوادار برزیلی بعد باخت از شدت عصبانیت هیچکی نتونست جلوشو بگیره و تلویزیون رو شکست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98538" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=nN3xPfIP1DA_bgDlwfbdj9XdI0HDPB4mEtEoi0pSXtWLALWrNrPwD8Kl-OIqkuYnbPI7S517mrcu32MGM2cV5sQ-qQ7OiiYi03ZkyPnJjzb7pZmgXZyN86FxjkpeViR83nTMLbQB3JqvK1aQEegP5tAt0XUJkcLrREF_U9VWXHzEfkpvSalDKg9IqLbqklO3KjjclhgligfTCZK5IkGf3wrvDDtLnyB8qkgMA2czgXupwbHnid2VA4UboWWdkMiTRnjjVJ8irpfaFZxKjATS7zEe42OYEwguPNy7eIpW8eXQxGBz8c_iP4cp3KvM1EcR2mKeawDZt9mZhCyHGSlTsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=nN3xPfIP1DA_bgDlwfbdj9XdI0HDPB4mEtEoi0pSXtWLALWrNrPwD8Kl-OIqkuYnbPI7S517mrcu32MGM2cV5sQ-qQ7OiiYi03ZkyPnJjzb7pZmgXZyN86FxjkpeViR83nTMLbQB3JqvK1aQEegP5tAt0XUJkcLrREF_U9VWXHzEfkpvSalDKg9IqLbqklO3KjjclhgligfTCZK5IkGf3wrvDDtLnyB8qkgMA2czgXupwbHnid2VA4UboWWdkMiTRnjjVJ8irpfaFZxKjATS7zEe42OYEwguPNy7eIpW8eXQxGBz8c_iP4cp3KvM1EcR2mKeawDZt9mZhCyHGSlTsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گریه‌های شدید این خانوم برزیلی بعد بازی دیشب و حذف از جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98537" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=UgjNVihbKrdAdNJcODopqbSGRjpI_PRaBE63kIQdGIbX2HX7rcmWhL0DV8oRCM5TU2FqHa4KVMlohXUa-GpiKzIfq2thJWbUU23pZGuwa4B6Xf0JT8a5S2zvPbTXoK--7nmLf0wLLQET76QxVhx3rl_Pt-4oS9eCKX1ZdljzCppPRG1Aqt0J1UC-vfTnxTwMYoRHditXPDi21G6de5LVG6QyC_pfRJ_JLcgVomivfa-VGjDkQhgfuIH6XOAxvldce6ZMfaxAc7_bqQOQ2SLYrzZbgx_W3ZA3Opb6GHHeQTm7hnXdR9DgT2SS5xT2_V5AwFZLSN_OeAJ4Oq9YDNYNbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=UgjNVihbKrdAdNJcODopqbSGRjpI_PRaBE63kIQdGIbX2HX7rcmWhL0DV8oRCM5TU2FqHa4KVMlohXUa-GpiKzIfq2thJWbUU23pZGuwa4B6Xf0JT8a5S2zvPbTXoK--7nmLf0wLLQET76QxVhx3rl_Pt-4oS9eCKX1ZdljzCppPRG1Aqt0J1UC-vfTnxTwMYoRHditXPDi21G6de5LVG6QyC_pfRJ_JLcgVomivfa-VGjDkQhgfuIH6XOAxvldce6ZMfaxAc7_bqQOQ2SLYrzZbgx_W3ZA3Opb6GHHeQTm7hnXdR9DgT2SS5xT2_V5AwFZLSN_OeAJ4Oq9YDNYNbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
حسادت عادل فردوسی‌پور از وضعیت مردم کشور نروژ که در رفاه کامل هستند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98536" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUl_i-tazfEXmfn-hliHBCwDz5Lb5xAbeR5945aB75qqyR7ENBf8lcaO5Rd5N-RmVt0JKr1rXdgLFfEiv_08ToDFDpoEnliQLeDh3TAaVa3i1N_lGz_nOmTM5ewt_jQMafP-TyccOaAfRhd6GRhlRp5_Jdy3e85Q6Q9UNPa8F9Dg0hrwfYi6SfU_-3fqIl5APA4_sFTx-Tlf3snt0AZzCSehsc1tMAMDq3w7N2R9dde6sXM9YDKx1FRXoBmFszEGrKSuCRwiZQXzKmYQT4QhitgbT6G0_eik_p4y9xRs7BAUL6MUuAh7GX1Vx7B-_MiogEBKnYSayD9wTiKn50gTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون پخت و پز همیشگی
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98535" target="_blank">📅 07:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6rErd5g51H-MBzQcz4CIgXd-rh0DfilBE5XEVx3DL2YUBmFHiN3P5i7mHYxuKc5DcSEp_Fk35AOs4tBLGo8DBJwsO3LLXthrQ2NI9SsGsF_0q9hZrq6DFBsmVmn0fblXTfslysypHVQ3x0Y1wGg9a0qzj8ir2ZV3irKOoibf2o3NNsA4mAPRBKW7Ruob-akEgHM9ny8pVqy_u-Qsg6_tLB_HuFhsD0KngxGREWCv3_N_a1-U6TVZQo7iKEwvaUfoF4s_vylybN7YXXn469979HCkoTiE_aEJIOvfv8e8p06e4d21I2NwV9rGcZ654EA9UYOXuB0qrxgPI6COE_NwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس در جام جهانی 2026، یازده گل زده که ده گلش رو این زوج فوق‌العاده به ثمر رسوندن
🔥
🪄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98534" target="_blank">📅 07:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4010363319.mp4?token=rwSgCFNbhw5Jew4UszizlsJBml3q8RJOROYMJ9wsGYevscu4S3wgqsNwlBIUJF0Ot3tJleSxtLiRLWhC9muiUbPbx6cZtGtw2M8tG_30lGzAU4no83QaClzBYo95f_53X5VanK7i5kcR5npOyB3m3H6FLhMWNtp8HkbIZHndnMcqlL324VuaeKP4CYryvg5607ySE6ng2pna0P7WHteYwYReBFuxplfFKYa7al8CpY-b2ZErcOIDK3u_a8Y4g3Y3pGQMJ5wQn5Qsfdpd9A2_4lSKRDd4yiMmSFXhbNUBPRSAbBSfKbHm-6k7CcJsnSA7HsXxgkLcxikWTRX0YO-EYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4010363319.mp4?token=rwSgCFNbhw5Jew4UszizlsJBml3q8RJOROYMJ9wsGYevscu4S3wgqsNwlBIUJF0Ot3tJleSxtLiRLWhC9muiUbPbx6cZtGtw2M8tG_30lGzAU4no83QaClzBYo95f_53X5VanK7i5kcR5npOyB3m3H6FLhMWNtp8HkbIZHndnMcqlL324VuaeKP4CYryvg5607ySE6ng2pna0P7WHteYwYReBFuxplfFKYa7al8CpY-b2ZErcOIDK3u_a8Y4g3Y3pGQMJ5wQn5Qsfdpd9A2_4lSKRDd4yiMmSFXhbNUBPRSAbBSfKbHm-6k7CcJsnSA7HsXxgkLcxikWTRX0YO-EYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98533" target="_blank">📅 07:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xelj9BUQoA1pRGzpv9K6oUjHQfdhfuXEQimAEoz5gnhxuz9HKmQSYh72FOXmiNMd6-WjYr07WvIbXa9GpGOFL-uNRyR-WepvG_excL26vNW-aEYBe4_F0hCTCLQMah3zH8wJXg48DhSojA9iit0qQGxEGDtBNGvAiux9eLn9-FjRkcyllgSU-R50XRIofYZ_r7-6psRkFZwqjzAHKPsCFlPg-YR3zGVTiQDKwG4YdPklnb2qI373RNn_e1FFUJsbpCrXk0jIDngGT9L6TRWDectkyVZ9PX0OCqppQfq3OhtnpsoZ789wxJx195zJcSu3CmWiBW9vcMrcyLkTIQRGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98532" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=CvuFwVgiAGQk4aMF3sqZr4BoPP5jaYlTGdrZbMXjzi6eFeQYbpxLu9tFmZVxPSXjC8rBvroFQwtb1f_EGnI39QUMOXCbL1lCjIWqHRC0RJSDh5W1u3dbH9Kn8e5csYAzQanKQf6w6Wv9S7cO6KnJgfEtMfXCciFx3_LurmwhMvuWYbnOiKSPgN9WKQfw7Q2obM666A51TQDBKwIqQ8R6nDi1uP5ggK_F4fxTooP93Vqbya163wRCgMlIIHTyUb3J3ZPNb5oPIey6wvXORcpwTk4dArGlXse9KPwjmQlPjf2TMhOvnGJKjMph-dbeGq85-WJxs9zQbi9HTijNASFJZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=CvuFwVgiAGQk4aMF3sqZr4BoPP5jaYlTGdrZbMXjzi6eFeQYbpxLu9tFmZVxPSXjC8rBvroFQwtb1f_EGnI39QUMOXCbL1lCjIWqHRC0RJSDh5W1u3dbH9Kn8e5csYAzQanKQf6w6Wv9S7cO6KnJgfEtMfXCciFx3_LurmwhMvuWYbnOiKSPgN9WKQfw7Q2obM666A51TQDBKwIqQ8R6nDi1uP5ggK_F4fxTooP93Vqbya163wRCgMlIIHTyUb3J3ZPNb5oPIey6wvXORcpwTk4dArGlXse9KPwjmQlPjf2TMhOvnGJKjMph-dbeGq85-WJxs9zQbi9HTijNASFJZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صدای هری کین بعد بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98531" target="_blank">📅 07:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AViOKstxSUlNO10QcNJiUeZsmp_mEID2Z1HHp1janICRGg67s4S2yzGzI9FmVPKGSQiPmKj8oNZf5-nftnuNBPtVl-z3L64kVZoGy5KZAJ28M5ZSfUxgm6tGGQaw7NfrYxQ80UT8Y0lGIwzNKxfTODo_axkwL-Bk1XThjU0SyU3zZZ4q3HTPn8sM-8S2_SMFxxvWkbEQWFc0VilTz7rUEoBkIdeVMRnerv0U0yXSHqx-jBLMaXqMiKIi6WOTM-gnF1QjRdqRaNVkTsplFfOiEdOjTbzTYE_PGVSOS-I19CMhuPGD65tuoFlSCy9YRY8AuAGJP4gFqe8S25MabD-XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ۱۹۶۶ سابقه نداشت تو جام‌جهانی یک بازیکن هم پنالتی گل کنه هم پنالتی بده به حریف. پرینس هری یه پاس گل هم داد و همه‌کار کرد تقریبا برای خود و غیرخودی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98530" target="_blank">📅 07:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-voa3LCoOtECMcN746Rs9xELWup2C_l_pLfiUd0jTzvDLEW1JqMStUY4IQo0NRlNYeWIzR0PMEWmew6agB--qdeR2_DGJVNvxn1UGZueSKOmus6HnY2iW-txVhvElInrazRJbXs3iVxU2_fS2PdfbYpIXA4kLbTszswndAYiM4e13Jr2ijjE_mFOOiiGWXzchl0uoPms13H_fcfbSgfORiNd76BI5S5IwwE_ebai6r4okdkgPXo3rj1p5spDr-g0fbeZIe1D50d3xPUHnlH-6BH0c6fDI30KsaoaudGt-IKYELgqEAy-QB0IRjJ6al5POUkP5WzbVvFNqlbx8fRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دونالد ترامپ در اپلیکیشن تروث:
🔻
‏هری کین، بازیکن انگلیس، یک بازیکن فوق‌العاده و بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98529" target="_blank">📅 06:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arB5jiPCmuqw5UVSUJp1IwGH_CZu65X4k0_llemXwtxjkuaCtmWf1IcKSuOx_o8IHKOcK1Oco0JXNzdDw26FnacytUARv1seR9ydil-9cbNY4pMqi-GNpz2WQ8LJYxIB7YpmLR5_kUCTj7xkpQSt9o-pz29z-BMWaWDhiF4KG1ctmh1YMbN7cyUDtuvqPDmD8CZPN4JQ5qliCK4IIfvHnOizwVxalEDULfRIK7KdXyl6qZ0RqejSciRjcfi7PMe57GNtgN28bgPucOWpVUUYtP3CsNENghwcaLNr1ACa7ZpTBJVNh-lJIAk9QfoHsAfvPq9CnkWp-F4ean3RtXNHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
دقیقه 36: انگلیس 1 - 0 مکزیک.
🔸
دقیقه 38: انگلیس 2 - 0 مکزیک.
🔸
دقیقه 42: انگلیس 2 - 1 مکزیک.
🔸
دقیقه 53: اخراج کوانسا.
🔸
دقیقه 59: پنالتی برای انگلیس.
🔸
دقیقه 60: انگلیس 3 - 1 مکزیک.
🔸
دقیقه 67: پنالتی برای مکزیک.
🔸
دقیقه 69: انگلیس 3 - 2 مکزیک.
👀
‼️
یک دقیقه سکوت برای کسایی که بازی انگلیس - مکزیک رو ندیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98528" target="_blank">📅 06:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pmout8AMovTC8nmfJsjhUQQWqH9FAIKmhBfKYBOTTtFgqJsjDHGRST19iePPQ-PFLXGhOU6YOfyfeXZXseEKZ_LR2gLQK0ljRgV_BmKJqb3OTj5huH-6NVaxtZ-E-YEQwNtK_Hh08IXvxEoj17wsiDFM7Oy9DWkMWTEtPad-M7JZG3yYjmSYEP3YPUTtFWAwaIgtO1Ta4oI0cUTJA_8psvlaFo6mP5zk4kailq6XC30BbauoqgZAx5TUcNnOkV6r5x5T7RiszLTOnWuFi9DnywjU1_Ila3h7tmTdGya5MUv4Mva_o8ffiM4EvZM_D8__SvsAghzJmBp1TUZyg3nJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwzysRPxDbmZjIu2LfAb7W5lenc0GhRLflFaGKBQ5FmvHLpltxC5HCz4xK-lx-VY2-kjy_kTnhvCPJDgTx-9XvEZM87xmy8zgw-Zl26yqB8iWYTEabXRfUTM2Y6IAs1aJ4rWn3r7sNVPpMbt3krK34gewnzjVdQzHVbHFCdg-S1PLs0SCuR7Vn2J4-Lu3hvTx8-UJHfrOMt_xtcD2DfSfmLLBGfreLx1s0Yk3Ufd2PjySmnO1VJ8SXaii3_Xc-pCYhNE7UubTBJq4B14JpTM5vFiUZhopSTbn5HeajWlUqdbE3Fggk0EVVFfEnElCY6Gz_K5iJvaCbWKHZYiN5iEEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوچوای افسانه ای هم از بازیای ملی خداحافظی کرد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98526" target="_blank">📅 06:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1iUw4k-01sfLyumZUpoMug_DlrkQKsixum75HeZ8yKgOqbe_bwbB14oIlTTXBf_1ZyYq7Ll3kAwIGxsH9U6IMUNr-pooCu8qzBJUetQ2yygl96DyiUe86pl3j9Wiqri_gt_xbOuxhRoNHmcDZ3LhSo9lLuO4KFi1vUHZ_qjIRKDoj0mNGeoUUpPZ4OwCz93SPAOEklgYPx4dGZV86tWn8faF5TOtWXVK6_-L3KvlSmics37yb-3shrOqjlnQMpCayiR83KdqY1KZRbw4LQosrNxTGOD57B4U3TLDunzmv0NmyO28e2B1kzRUtppMbKSW__FLx6c3eRfGqv-WaCI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
هری کین در این فصل در تمام رقابت‌ها،
73
گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98525" target="_blank">📅 06:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7FANi-1lkQMRLALVZlDFhB2xt-25-cEkG-TTUU9PUBNDQwEXYuoYUrlvXjX0c92K3bsSD5kcGD_Son4b12T0Lo8IRhyVzsdcXymm0ElYnZnfQk8TGH4uNiu5aVOpgkAlM-3FLWf932s824IkHK9RAbALH-cCCXvVaYhw3TjH4OdGHVjEDMfSZPwp-Ak9mAZJMlMqgDc5zIi-7xJZvhdBF_4cDdegYV8mVG2jSSNVkHq9IiT7Oh4yRv00Vr-THM8j8mwb6DVwQ4WXwIo7JXvn77ePzIB-PV87W3VPb1jeJvQ3oUZq9d02OCHodV4Zd-0ZDQZbghsVSluiF7DKeTGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
واقعا مکزیک با این آمار هیچ‌جوره لایق حذف از جام جهانی نبود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98524" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnT-muUK7rhI-4EabJB8KqJd1TWblQT2MB2PXhDcmrnY-gTzzgLcOHDWSfnZuZza99dCu6mKAZ2egWVUQgi7CIEsMH5lVPuQ2FbnqVj5RcREeQY503aTdLqJ2MP-WGbYHcPSfjllc0PTOEyZXq8RP5As4qtGNBeclR6DTcYxiGfuC-3HcnvE130OMJORxuTJmPwhlMGy0mUedijPgtujw05TgyUKGFcg5MolysGEGnaFX8zVNNsmXH4ZJCHyZisLNPC-J9V16ywoJiNPP2GSWMyu5nJF3HY-1QIL8eRFVKN9rPxfAmKhqPUY_S2xfiFNc7fvUf65wcM7Uyc_Fq-o7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇳🇴
نروژ - انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📆
یکشنبه 21 تیر ساعت 00:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98523" target="_blank">📅 06:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeDs_oQPXiNEitZj1e2C5P1aGuHYJk6ENVH3bLd_62TZfbv9WiNEOAJEnbeNz7o-FQxZLvYTxzBnFqXShs-K2nrdPPYbgFuEzsTBIiLKIrAI4v0MjD5Mh6bUXthKuXNxM2m39vt9Zb38NpFBUFqoIFYJahooGyp9XJilVO2s3xulXhCt8yWa1DPc_MzW1NPZUfWNb4p8SKn7dkw5Hqv_aWeaVtNXsUsAktrRbTdOQ5DD3irAVwfIQFEydPbYs0SnAyQQTDk0IT2rOgQPr4uwF1_LP3c9gV4vVXDb9ldJ0dLH6WB4clEM7vYbuujCFy0SFnmhescI4ml9hErGACmx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98522" target="_blank">📅 06:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY89vG5HaSJzR_jtVYFoZK-zKFGd9k4Vyns-dejLdwM8x5pEOk7oPOeYjJF5fu1bDeBYGE8Edv3vtVVEgObsomivVeSo8b9g672QEkaUst3nlTSHuomTswiBUXYwlmGGSANMCZo0xnld72gYxkogxR4S7P-7lBtE5qONu8uMnxXpKsDx_el9ZMTxJ1vAZLjnb25EFxhj6qvcS8Xaqjf-mWGuc_FogE_qqgURhEGL9NT9DHQMlMB2f3yzo7zwxaBTSLnRvoKpD9W1pwVW7vRvI0e8PwLK1lTYhXYKAjiIsFaT3M8A9Ea9ajnG_fTMWLv2AUjakLrJuCzZ1GEIyhB4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد انگلیس ۱۰ نفره مقابل مکزیک در جنگ فراموش‌نشدنی آزتکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
3️⃣
-
2️⃣
مکزیک
🇲🇽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98521" target="_blank">📅 06:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">11 دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98520" target="_blank">📅 06:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98519" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حیفه این مکزیک حذف شه از جام جهانی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98518" target="_blank">📅 06:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqc9R-POdy0pd-RzDppqxbb9pWIu7aqEGj1gT_8-VK-M6gFP4gDgSBMuhdUT25ylNTWQ8OBd77u57tuMX0X0hK6dJBW7Jeyz7G0qyQjLVNeK0ch77iAxKCi8N44TIm5zk2mxnWRO1kq0Bvn6WmYJ1KCdWbEwTdLHX9K0n92ak7-rasbVqm6juKF22TM4iLI46a9ff5S2kzzoWTXNVkR6qD0_isscmaf4K7cwI6-AIOyixqvhXMoB0TCNJapcLE5rBTgojUccw5JPMLjywFc4dCWW0cX6KRZ1ud6idNDxfxCl0b16lkfrnMoze-iYakaEDAUC7PcZUVlQnqpMOnXLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی تو بازی انگلیس - مکزیک:
⚪️
اخراج کوانسا بازیکن انگلیس
⚪️
گرفتن پنالتی برای انگلیس
⚪️
گرفتن پنالتی برای مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98517" target="_blank">📅 06:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=Dw5HBpQO_Iesa2CoPamiagkMPreKhjSuGVeXtFaRAyV_HYpbGSUPyRPeel3tEbYwgA9LPweo2Flk7eCEa0A0n019GG8qkux0Y9aVmtAhyuIv2Hmh0axv14v5q4A9fsUJi9qoq7DAXut5TEA6IrCPXq_2acLo-tv31yvhTvRVA78KR2KR1ka4oW6Mi_YFK9bgxFEc3BskzidPxiWhJS3NrC5XtDnvwF6tpuRabn5aZ_o4ITHR843S06-d6Xxkvy4DtGD4EO8MlvnCT1BhiF6pGQBwccXHZkWZ3Nf6umSLZsZmEgH6ih7rzmQ9hYoXvcdNSZ08V2dfcxb0_qKH7k8xHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=Dw5HBpQO_Iesa2CoPamiagkMPreKhjSuGVeXtFaRAyV_HYpbGSUPyRPeel3tEbYwgA9LPweo2Flk7eCEa0A0n019GG8qkux0Y9aVmtAhyuIv2Hmh0axv14v5q4A9fsUJi9qoq7DAXut5TEA6IrCPXq_2acLo-tv31yvhTvRVA78KR2KR1ka4oW6Mi_YFK9bgxFEc3BskzidPxiWhJS3NrC5XtDnvwF6tpuRabn5aZ_o4ITHR843S06-d6Xxkvy4DtGD4EO8MlvnCT1BhiF6pGQBwccXHZkWZ3Nf6umSLZsZmEgH6ih7rzmQ9hYoXvcdNSZ08V2dfcxb0_qKH7k8xHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🔥
گل دوم مکزیک به انگلیس توسط خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98516" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فغانی رو بنازم
🔥</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98515" target="_blank">📅 06:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه فوتبالیه ولیییی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98514" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">3-2</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98513" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلللللللل برای مکزیک
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98512" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کین کارت زرد گرفت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98511" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رائول خیمنز پشت توپ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98510" target="_blank">📅 06:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98509" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنالتییییییییییی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98508" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چه سوپری شده این بازی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98507" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وار داره پنالتی برا مکزیکو چک میکنه
🔥
🔥</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98506" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فغانی اصلا تحت فشار قرار نمیگیره و شدیدا به بازی مسلطه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98505" target="_blank">📅 05:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=F6T8uFn4ROKiatMBvqad02T7U8pxlcw7_RSq5KB69UUVd67aP_IV_pMZCxiSUnW6PiJOP5Ry08I3tWyca_-roMkdOkJP1tPX2SNXbWDeCLF_0SOjdskodc3cSWA4EHL37evEP5SSTX3xa8BQWMs-9I-hgiQzCJuixXFjVt-9xd3gK67iJg2vFGVYzADmbcEFJJnKcKJZJIp8fHoC3_B2cAvzQGoSf5uqLjw5cn3X3NzqQjDkorBd_UMfo27Cju2ej4dXWns3RY2jN0GlQWSXSHQHkxhWb6RaR81GMvL4Y94K2PCHcXCXJq7iFexP0BCS_mXq9LsZWg2am_AvhaCh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=F6T8uFn4ROKiatMBvqad02T7U8pxlcw7_RSq5KB69UUVd67aP_IV_pMZCxiSUnW6PiJOP5Ry08I3tWyca_-roMkdOkJP1tPX2SNXbWDeCLF_0SOjdskodc3cSWA4EHL37evEP5SSTX3xa8BQWMs-9I-hgiQzCJuixXFjVt-9xd3gK67iJg2vFGVYzADmbcEFJJnKcKJZJIp8fHoC3_B2cAvzQGoSf5uqLjw5cn3X3NzqQjDkorBd_UMfo27Cju2ej4dXWns3RY2jN0GlQWSXSHQHkxhWb6RaR81GMvL4Y94K2PCHcXCXJq7iFexP0BCS_mXq9LsZWg2am_AvhaCh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللل سوم انگلیس به مکزیک توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98504" target="_blank">📅 05:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگلگلللگلگل سوم کینننن</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98503" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کین پشت توپپپپ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98502" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98501" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برای انگلیسسسسسسس</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98500" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پنالتییییییییییییی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98499" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdxrgycqV6tMMAW2XXusQUAIJJji6yhwXM-ts2ozg16QWMbtmnmisZtTqGFzr3cGBuTpoEqmH0tNbKR-RQS5sQ6o6PVk-YiQztBA41ftmU7ifA5fPjb3q2ZSrBCRfGJi18EHrl4Dw86k_5MhlfWWFub1paXpvLvDUFUWNz8d1isq3tNF2ADZMJouUHcc5xfgYSk82Z3LZRvUkBfyGPq9F6i8apBLk56KeinwhasDWFN-5AooLPb-J6uDikG08HYlh0VZydGDfTqlmEL2_IPyzRggT0-C9PdyEyAdV70PNPpmt2b5-JhDNzcTSvndK5LhTU05jKdq_Ia9NV2rYryJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98498" target="_blank">📅 05:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98497">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98497" target="_blank">📅 05:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDDxurX2-0K_GhP3fJ3MnSPs-2CbHk8JCUeUGweO-WRly6_eSZmbbMztJqjc4UI7PqfnQtMU4_ySHD4dcGsNOIcKdkSOnhWCu14oyLUtBftQgdHqMle1rKFeN3ywZxB3YWarjxQBEi4HCNm2kZzsrNXzm6nlZdmNxccN8IMhVRAiSuSKrYHpOzEhOcE_JU9_-k1fmWsWIYtPPZ4DTNJfsE2O4d6LTaF7dLthiIz5_V0CFxqA1fg34YR6kR4bGNSi3Jkp8n6T5Ctw6NDWOo0aJQgK3UTQz0GN-8WlTzTWsXNw7sqMhddtpVXedH9emwPffTdHaLANSwyB9CX_fchqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با گلایی که مکزیک خورد حالا تیم ملی اسپانیا تنها تیمیه که تو جام‌جهانی 2026 گلی دریافت نکرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98496" target="_blank">📅 05:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بریم برا شروع نیمه دوم
🔥
🔥</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98495" target="_blank">📅 05:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcsHya2TEDVGHGpp6Flse5-F390Ee-Sy1xkrJaUjewGMUunmvXsQt0CwIFCiSl0Wnmew45xrLD6i8KCMr4LezmLwhvfI2WnLcoYKpdR6i3Pc0dYU3f8ULjRsQvDoxsrOu_nRnhl9CxzHaHn59RJmjJNRlP2YazPBxl4DEka-QuZbt1KtzoCwRU8J9fWCMgpb9rkbg2kbC9xp_oU6bcS8qSy070ABxqWZ6M-eOFwh6ohwvoGhx2Mykgcg70nQuESUaC4-Y9lx4st8BDs31LDMLHhcj1lfJ7WQn1CKTi6QRemOLqLN7br4GZWzla6tPtA1aUMAHn1ZWuxPYHloRwbuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">19 نوامبر 2026:
توماس توخل، مورگان راجرز را در پست شماره 10 به جود بلینگهام ترجیح می‌دهد. [دیوید اورنشتین]
6 ژولای 2026:
جود بِلینگهام با 4 گل گلزن‌ترین هافبک جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98494" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr9KWtWM5FYpWOOgDMT40ptz2QuG5bM7bK_80D-21JPWgKetoJlRn7dG-JKo-4sK48kjCOrsslGG4Rz4XAfaqf14PDhtlIthrBZUCSbtWffYUmRMxoiTcMNKkV_-qtW2fWYxpCxvUSv0HP3UGCz-duveZN-3eBReudCp2nU4lpvKhaH3dE7Ry39GkOcTt4xHbyp4szY07bqL3SEvAtvKtnI1uTLzK20e-dTNya40EzM__oyLvcyt5nvYnwNRNpgk9Ui7mbb8A-JX41mZLVsJ1OiMUDutLwICTwDWwvkwt1a6g3uAIqoOVC_HJDL_9fJtLJPtwI8DO9bCUPXWssDO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیلیان امباپه: 7 گل‌زده
🔹
وینیسیوس جونیور: 4 گل زده
🔹
جود بلینگهام: 4 گل زده
🔺
🔻
کل بازیکنان بارسلونا: 4 گل زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98493" target="_blank">📅 05:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1mbVxT0dOrN-pgH8tn3Fi5ToHdQW5WJxnbK147axrpsb6LTFwEN6E5B4fqnJ11AGtNHrkPankm-28BYxgxmqFqHodN-q4E4jiKFV6dQXr1yRGsWJPwvabKmrWOg0eYRjZT5-0wXJZG3CGYnnd5OFM_RPi7WQ26_fRxp1oxMou6QW29R0-7jhESMY_mlR1hGg3aPZOMVJNgmZ6IBhqbWD8jpc9abznLBTNxs1p4VejD0_o6RIgClGqIqsHKC08aAg6GuWIiz5xHjgSfe0_FszHgbcSAbJZFf5ZoqQe7CHIDFsV137vuFBw1IeNh9CsUPBHmn-Ehvuxmk3MMC419uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98492" target="_blank">📅 05:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntm3WgFZCJuSOIi8CjLniI6aRSbHN5TBVEa61G4UCCq7u5S6zxiAYX3ldwKJchxluWqfj1tcrqLn1xLcsxLu5FuH-pstOzxWuL2GrR_f_pO9kfcQ64waejkbikY6JVC-UsZadfJcL4iyUwZWHtPEUh3LNxRADCFsXz3GItjUuG02ijrNeKjh2nrj_GIC60dT6H26e8ZMrh_19c1Ext-EPL8Gc6r5UKNIUs2k5aZ8g2OnAr4zg-RV3tpGiHo5sBn0OucGL558Ddm28Uuk61HFJvbW46274TGBIdMbmUU9Z2lnwqxqsOHHKZ8aasOvw3RVuulSe5baLTqxyRwzqby6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUUUURRRRRAAAA
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98491" target="_blank">📅 05:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgKD74NkhLNKDNzpwVm-jja1FrVjRDcF1nyaW5-O_OnIjTxrEfFP4t3adHeQeomwArSr0JKXU8No13iUbQpjl1yj1D_jq3ABS9woZvtdK3A5inRO7A2PACUgK-6MBW8ZLM7kvjrK71pQypgpLwxdOvyPhuW26stKAoKDhZHnhEQH0EnR3jVbePCAR75HZXEHCsCXYmy9R99fOd0wePvYmgOk13wiK20ppy98iqDD6VudZpX2eKlljKnkktbis8fjJYWmW1XzdG_-55t22oPlqJL9kVIWTGTADTt-lGtc6d2NA3MBOFoe0Vsb30qwLy-M_NNgTF1HROO7_O1rYUlvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
تو جام جهانی 2026 مکزیک هیچ گلی نخورده بود.
🔺
و اما زمانی که بلینگهام از راه رسید: 2 گل خورده در 100 ثانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98490" target="_blank">📅 05:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیمه اول تموممممم</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98489" target="_blank">📅 05:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مکزیک واقعا داره عالی بازی میکنه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98488" target="_blank">📅 05:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=V7OseCAhCvM0Zhr6f8QqknXw5nxVNux7h-hrJyR36HUHk4x06TLjUoQT6NHZvVuGWkQoSO58F7E9YKNEeGlK3CxOXmbHIRW4l76zbrluCSnTpNY2oNoB1TI1KJHbuQ1tpkF8XVym-A0OZ7H9U6ibue_pKEbS4k0-teob1NPmJarulfDvIpGz6uKgQWA2yn5XLGZHKOrOffa8NJz7O9O1i-5uNfoir-g2nRZP3s1cO27-UHhks54La9nnLaO6Qn-U8gqgTYbqK9A3wS_bGzdyUceeFApy3cqjeaNgG6ShGF81T7DYi60nEgccTgK_IcbRO6gdWi6ZnXLCKQR7Rc8P8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=V7OseCAhCvM0Zhr6f8QqknXw5nxVNux7h-hrJyR36HUHk4x06TLjUoQT6NHZvVuGWkQoSO58F7E9YKNEeGlK3CxOXmbHIRW4l76zbrluCSnTpNY2oNoB1TI1KJHbuQ1tpkF8XVym-A0OZ7H9U6ibue_pKEbS4k0-teob1NPmJarulfDvIpGz6uKgQWA2yn5XLGZHKOrOffa8NJz7O9O1i-5uNfoir-g2nRZP3s1cO27-UHhks54La9nnLaO6Qn-U8gqgTYbqK9A3wS_bGzdyUceeFApy3cqjeaNgG6ShGF81T7DYi60nEgccTgK_IcbRO6gdWi6ZnXLCKQR7Rc8P8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول مکزیک به انگلیس توسط کوئینونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98487" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کوئینونس با این عملکرد شاهکار داره عربستان بازی میکنه
😐</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98486" target="_blank">📅 05:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تو 6 دقیقه 3 تا گل رد و بدل شد
🔥
🔥</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98485" target="_blank">📅 05:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=feQIdQBmMevabFkCxhdimBTdc4yAlS_s3ol_U27SDOOVwvN7VzKuW2XYs6D_ZeB-0yxUYpq29zPRyLmrAo0USzyHbKu88IIGn1UosZ_8FT59TbNq-B4nmy9kW0wtaZWeyrx1J9vtTQ3djUtdLsvSXEX6LsggQ-a_Q78VjzPBuDvjxpKeps_bygo7UBgR_jWJRNYhl-ZX0SSzY-dM19cI5mD2AisJKyP1bV-dgBDV0Jn74sR4zD7pXSNJJXvqeFvdTSt0hbmTX76CtZcJOd3kl2HvmPs-VHt4AnxZJkckX7dCYKmMhtcyq1ZmJMSpmRGTpWMnvIrffJoiC6049WVyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=feQIdQBmMevabFkCxhdimBTdc4yAlS_s3ol_U27SDOOVwvN7VzKuW2XYs6D_ZeB-0yxUYpq29zPRyLmrAo0USzyHbKu88IIGn1UosZ_8FT59TbNq-B4nmy9kW0wtaZWeyrx1J9vtTQ3djUtdLsvSXEX6LsggQ-a_Q78VjzPBuDvjxpKeps_bygo7UBgR_jWJRNYhl-ZX0SSzY-dM19cI5mD2AisJKyP1bV-dgBDV0Jn74sR4zD7pXSNJJXvqeFvdTSt0hbmTX76CtZcJOd3kl2HvmPs-VHt4AnxZJkckX7dCYKmMhtcyq1ZmJMSpmRGTpWMnvIrffJoiC6049WVyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم انگلیسسس توسط بلینگهام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98484" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مکزیک اولییییی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98483" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
