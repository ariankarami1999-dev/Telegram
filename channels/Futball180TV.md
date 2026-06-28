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
<img src="https://cdn5.telesco.pe/file/K5KdHhrqbYE3bN8Xqoz16yQipHvGbIU501F09ppmQ5BVP_FyjxoxjHVINnFfTkgOVd5LGo2qhKgDtpYbkTPV1lHdlKG_vUl5zKeR51IwQ8JLqOxRMRzDNkXbk822GMzPU9lq9zQhxd0XRybI50iUYnB3iXkyqxxyr-5A3n_OtngYmTJR2oJ5nJykqYO6hor6Lt5fIsGP4MzzuHlMdLnLJP7C_3Fwrrdk5aUmCrlsWoez7WDOfDbLsujT8zDiDkoUW9ev624_IV2qPCEAunnjQ2wMXfIIXZ0askuf_XPUNuggih5o4Irct_TAGrAJoTcnIYI73cFl16fAXSKsKWb1Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 692K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 02:25:41</div>
<hr>

<div class="tg-post" id="msg-96733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy0rwRYH3YbZjqOt5zpnhZ00iaf9ooIVRk0QFUG8_C7jDL26OuJJw0hMx0FJ6NnpmLf2B5Nw5DachxhxJ1s-_RE_r0jtSnTw25Nn02KgZwigQMoGINbryFRFvNTYofPSZ-efHlu15yvY4DaPLbUShZEmF3vkLsL27yda_D-b8eboXA7RrwFBFfAujS79M-1DHg0RR5yvbj0Je6SmczeC83zHbDETO11Llit90-5BUaFIPwbGLWLVFW2656vnanrgMhYERjYEC5_i-mOn_JdzAQLTITgmXNjxsV3Ne6XXQwbjMTCBdUyIt44FK8tLF5U_HdsDQgT7VtFiyEG1iykhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند و ترویس اسکات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/96733" target="_blank">📅 02:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_XS3_W-Y0cYB5RBgVCbg-aiFdj_tSb2r6C_8MRPF8XHcSXVucolhTMtv7nODtDWkb7Sc9ClcDPX6EqvIpwGH-P9W6lOJ0LlS3C6KuT4w4j4JvD5FT2oNUDMIzDeoIMX2tjPvMnh_GqWJ7e3_ALvhreaSzZkfCrnOPidgOo8FVEcQrGItysfQSNXKJ3xLdU6s9R8yUvhfBhlmWBK-JRdq6dWOSHC9mr8zt3i-fpViF0mJvEwizoDNq-gC16v_YnC-nWXHy3_pzIDXM3TUm7wiYQNg8AYN9D7loqP8kugTMo6Yg6sV-rCTEesuxAqeFI9MO8KcVlkOnhNdRe3QfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک 230 هزار دلار رو صعود کانادا سود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/96732" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/96731" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G27n7M0AXmSBtJd02KT6MnURwwzfAvrxhGL_Dm0ywQDZP8Hehk-q00rUaOGOc3Z1h8pcbovzef_QwK_Ve9_lvVnqctpUJa2c-k9zM38kgfhQNyvYStBztYjHuy7IMzeZm2YxpDhCUtT_IHJz_bdne4D0KvVDr4ziG819uwneOqASX9hzgkitGCIGgMcbVQFX0E70a8v3BwvX9sXAWG2Of8k6-9zd9LLZOlbOldwlwJ25LwyA8AEuirbu7mkP3ceNksr1s_LrbUBpsZCNTFFtMwoNtCDauh5HGp_SI07UrYwYy7Z9NymSq2MbsJ5XD9PYM9CcI9FHCztcMVufi_WiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/96730" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn4BXUfYL3jIdhjIXYWgt8I2GkydhLXTy7A7FJegRC1HYxMV5qB5HS2cyvaoOTVMPMcSTvQOE1zpFvkbTCzFJtdZYR34FiAj1UF_5gAx9OU2PwbQR4kNNlat7PxiCVIEmYLrjn85T-pN1fYga_SxbIKZhgzR72cS7O_HKZyU2_SOdR9OITyrwujEnaddgMdtIiQdLW9jitB4UUtvEoo7wrv_BOzahM83rnFH9SHG4FHlNDUYz5XpOsvQhdrETClWXYXgpg3eF59Q9egEACk3gWgV1uPsj-C3VCC_xuPXJG0uhBnMF4t_oP67NnBA8lwkzXlM1Tb7Jv7vrQ-eYl8-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ماتئو مورتو:
بارسلونا قصد دارد با بردلی بارکولا مذاکره کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/96729" target="_blank">📅 02:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l6HgFqmCRkBOadb8-fGuBqMKFnPGKCf_Fktd5q8pynXSpV3wQowwZD5q6YoPv6x1kHIGSmpYLUo2mHCkOWvNLgGHiD9_T0cRB3PCVfvCfJPmM--FYZ7lwwLhQdh_oq9NRCsaJr5saRWcZNvBQiMb6hOfjt9GgO0A9f7xm9vWGJqAfo2BKV5jgd_WbFK8xuQseLdw2mZonWK2J-ElQMyLGDVAPSJwyJjRV7dEljtktLgd5D1P_Mx3MqmLZ-y5m98pskVkcCz_fNQ2uRSAz6OwjzMk13iJCiuG5WtmqEvmS40qJtMgxXYIC-m62kfUNC1iOcwE-WMYFaWC0b4jeDgWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
موریاسو سرمربی ژاپن:
ما می‌خواهیم برزیل را حذف کنیم، توانایی رسیدن به آن را داریم و فلسفه بازی‌مان را تغییر نمی‌دهم، اما برای این دیدار برنامه خاصی دارم و برزیل را به چالش خواهیم کشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/96728" target="_blank">📅 01:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlxnDliLTXlkRsFVc6uRgYNRkT_JHzEgOizrioQlm8ztOwpOchBnKFzVYjuOBTg9Z5gCyPNIesIGd9FTIG8DIXrO_IEB3cLGJElG8Z8m4lE05mbGW7bjKh6U_wR6abjiISVtAAsH_u1oNFCItLDM8bKk6GqCAUB93_O_88cjUCIhyIMaWIjE31cDyqOrukh1u4odV3IKl9sXeF7a-4tPjSgbwtaf15LS_NJkfjyqg1Za4XYSR0Rup1RvmYlSYd2-vgDZYV7ErEIuEGmKjedqSmC5JFIiJ8CIhtgkyqhZ1QYAuboX1LhoBz4j-2ilFnJ5hmkhY4FX3u0waH8JyKIo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو
: پاریسن ژرمن در تابستان امسال روی جدایی سه بازیکن حساب میکند، معاملاتی که تقریباً یک معامله تمام شده به حساب می آیند.
گونزالو راموس به میلان با 74 میلیون یورو
کانگ این لی در حال مذاکره پیشرفته با اتلتیکو مادرید است.
کولو موانی با یوونتوس به توافق رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96727" target="_blank">📅 01:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=Og6f5K5yp5cv0v1EA5leCgaGgqoI36VOJl9hDHj2W0NywHoNACrpGulEhk_C6CV3NMLHpzVsgpebIJhYO0McESJjvmfx6uuuXkoMqLQqn0Zm4erDhLUf0DyeLXCfV2qs0M9m4dAXGliN7hTlPzvOGFx6jpJdo2GOdcVVo4tUG-zGnOjrai5lvRFTgk5TqUiCq_L24MyFHV_S-brzHFzo0a_6ZqYvez4H89RaKouViKRI9WuWZ8HvLzOug1NMcs-5YlyqoigIjBmgPwXQnltJxXI50kY6oAwLa8p4eDWO0YEnKC2VsvhDDphSOXeNi1Cuvn1pBmEKIRc0qR7CJn0YBmZ-qC65oq4C8x7WABqAmkbahRmfMi-5QVytDxIC2LNqbmSiLeHgCUYys3eeiHECDkcq75WHKUUytQZVei0_CNXQqUCR1ETbs0Z_osm7u9zG532NHC_0WfkRMa36w4SUavvUdumaiXzL9rV1L762t18ygNK9qiXHLINtsElAIiYXO6aeZJfnwDKgpvDnH_agybQArZz0c2wucRDmKM93BnRJDBtWxJeLUHC2vK1q-2lfrrX9KDsCANy-_25klKsCmtKmghSPS0c8on6vvVcR482BjBM7Kv30ILFnRcVqzRSNdrfg2oTw9ro4GUfHHE2pD1Gf6VNgNnrdXCPmVMtgfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=Og6f5K5yp5cv0v1EA5leCgaGgqoI36VOJl9hDHj2W0NywHoNACrpGulEhk_C6CV3NMLHpzVsgpebIJhYO0McESJjvmfx6uuuXkoMqLQqn0Zm4erDhLUf0DyeLXCfV2qs0M9m4dAXGliN7hTlPzvOGFx6jpJdo2GOdcVVo4tUG-zGnOjrai5lvRFTgk5TqUiCq_L24MyFHV_S-brzHFzo0a_6ZqYvez4H89RaKouViKRI9WuWZ8HvLzOug1NMcs-5YlyqoigIjBmgPwXQnltJxXI50kY6oAwLa8p4eDWO0YEnKC2VsvhDDphSOXeNi1Cuvn1pBmEKIRc0qR7CJn0YBmZ-qC65oq4C8x7WABqAmkbahRmfMi-5QVytDxIC2LNqbmSiLeHgCUYys3eeiHECDkcq75WHKUUytQZVei0_CNXQqUCR1ETbs0Z_osm7u9zG532NHC_0WfkRMa36w4SUavvUdumaiXzL9rV1L762t18ygNK9qiXHLINtsElAIiYXO6aeZJfnwDKgpvDnH_agybQArZz0c2wucRDmKM93BnRJDBtWxJeLUHC2vK1q-2lfrrX9KDsCANy-_25klKsCmtKmghSPS0c8on6vvVcR482BjBM7Kv30ILFnRcVqzRSNdrfg2oTw9ro4GUfHHE2pD1Gf6VNgNnrdXCPmVMtgfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
😁
صحبت‌های ابوطالب‌حسینی درباره شاهکار دیشب جمشید خیابانی به زبان عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96726" target="_blank">📅 01:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za9Hx7S-5LH12RbYKDhkTAKIKsib0RX4F6hL6KHj7D8EBWSRAmIrwzL8G5ERMyenom9nbfQV3wHakzTvjwBZ5V74wTrAMUVEOPspEb-Nykp426EGYSEBPUfztUwa_qlCXFZwTcdbJSBtLUaBbATaQIRiNjDbq7ucpqRcO_Z71ErpmGV3k7pepSkitFs7T6pUuBmfgb9eH5J-6idUd0z0TYBybLjmXko0OQDNjJtCG0BeeNiANT1UoHnmmNyvOSII6MCgbIVvT179W07jQ-lVfcUhdWtuZtJ2CkU6YOxS_YuOkGYDfc_XFgYLy7RoYLPfnwambD7KmJT2wFaJawtjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇨🇦
کانادا در جام جهانی ۲۰۲۶:
🤝
تساوی مقابل بوسنی و هرزگوین
✅
پیروزی مقابل قطر
❌
شکست مقابل سوئیس
✅
پیروزی مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96725" target="_blank">📅 00:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV8TqLN80ak8f88710wnlT6wifb4nNQ6z0uPyQhyYHGWkunP5M0bb2KkNQQyeQf6WP4I1NBG8O4XIAhqI3RBa8ehBuJU3DwisU6mjsYeRxDYK5MH0j-Mdzbw9oUlEd8EchQGpxTMPTI8UyDW6l6y8YwpNlk-Vfbqz8hRy0WwzC4ou4FVLijRQI-INmLxq3GNGoGzPROqnoGSbSmvs1JvAsEU42fjFIFUUMT8e4u9_0tw3czk_EjFSPIhAJtkj8i0yw7YKL0elNRnKt8ZPmRRnXJ8-q4KCx7PNt4zSKHYvjRGYzH7DPrAb4HbH224Nhr8wgShq2jWrCH0YVeqlnpF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
جام جهانی تاریخی برای کانادا:
✔️
اولین امتیاز در جام جهانی
✔️
اولین پیروزی در جام جهانی
✔️
عبور از مرحله گروهی برای اولین بار
✔️
اولین صعود به مرحله یک‌هشتم نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96724" target="_blank">📅 00:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ocqmf2n_cOYzdd9puWFdb01FhUXckSis47k3Pd2i-3b2fz7l3jLccsN_Q-bhumevWSvrwtAJWu06U0hm1R8tvzNxs_hzjYx8IXaoVK2xE3U9RFB98lJpDII-rPFhit3v9dF6oYAIju-m1Gqn2Py1Iq1bOUPC5y2JjODE2akyi_6LtN9k2Rzp9TM_fiiOKBjXDSynyqNbq83JQF729wzhZPx8et6TAEQA7J4MKC4lfDWML_ZjHdp_MOB-mCfLn5emocYM9LmoOmCqCt2U_FMq11O7rCFAHsufruMvESkeJdLrWMX3p8r4FeERnCFxPg-InPAKSQ7rNNLhTW27IFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بازیکنانی که در وقت‌های تلف شده نیمه دوم گل زدند تا از رفتن به وقت‌های اضافه در یک بازی حذفی در تاریخ جام جهانی جلوگیری کنند:
‏
🇳🇱
ادگار داویدز (۱۹۹۸ مقابل یوگسلاوی).
‏
🇮🇹
فرانچسکو توتی (۲۰۰۶ مقابل استرالیا).
‏
🇳🇱
کلاس یان هانتلار (۲۰۱۴ مقابل مکزیک).
‏
🇧🇪
ناصر الشاذلی (۲۰۱۸ مقابل ژاپن).
🇨🇦
استفن (۲۰۲۶ مقابل آفریقای جنوبی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96723" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL2BSqtXzH-zpOFOQ9D6eEKzA-kmvrCsxQ33A5q9Rbn4YhcLnoK1Wx2wef1UQFdT0RCvd3d-ClmXSjQMDzhBgQOR-jTslI-eQvfT6FgZKzi_D1tKwEgw95IMmC7i_Tp1YbG3ix7jzYyKtALI7Sr46fY1BenJBSU7IXA54_gMTMh-gg-wOngG-r2w-CxFk8716zFzyrLxO3sGajyI-WVkyTri6v6hV-Ta_EkO6BXoVs13QHdSPJBdfAQRO1aMZwG48sDTUbYw8yZ9dHp4xptgVeiV45afG7XXo3oiI1bJWk946bQB-y8remUzyAN82PkvD9Sqm6XjbM-eBdSWvTYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
#فکت
؛ تیم‌های آفریقایی در تاریخ جام جهانی ۱۴ بازی از ۱۹ بازی مراحل حذفی را باخته‌اند. ⁦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/96722" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COPHEGiOUpypqKrt1ltmR_ybtCqeO3Ix4y9oDGukklfKqkKc9JK36wco9ZCJ9bbum28-Oy-gx81s-RStGOVb71Q7S7w6T3uY7uRc8wYzlGF9PAlaeunw5Hg2DIYvW73iuTXrR65WgRnUbjCW3loc7DXPs8_NN_GqP-e5eDrTnFe-OxVVqAQ9q6akpa5hUBFnBaH_TyPLPb7-mgToV9UeGgSgCSPm917DPPgKgOrX9uA07QjOf_qHtoaESkHgS7GUE0-kFcNgSff_8mG2nJI7mi-3KOSVQgEj7N_0JZ1JI-rQumVXt8tw8h0c8PJZOxwF0uYd6LCZbGO7eYXG0dtSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
📊
🇿🇦
آمار نهایی بازی کانادا و آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96721" target="_blank">📅 00:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-4MTrNP-JEHlaVpBYQWo23XImgIvihB4azvidCXf1QsRzgzHNAxK3laPerJNBzoEuj9ppVl8xilRk2Yxn6bH5Azyrtlcn_DggEsI-8jHzOH1nhLjTrfPH1McCRMXdBvoigY74KuobbwC9J0wepqvn5t2ePk_m0LmnXGWBuisALh9KlLFtT-u8TKB8hJEr5ZtXen9hXGzFCkABssEJzcXplM8cM_B4-pl5GDYmRBoQB9eWhbg0pP2pjOWmsygBKLId3v2CN0Agd7O0gejdIpGTjcEJYEib4jNBeip--MYIAIJ29u_06kf6AYzB-GXIfAWKhKJuP-8PLiIP4hxbTXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کانادا در مرحله بعد با برنده دیدار مراکش - هلند بازی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96720" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🏆
پایان‌بازی مرحله‌یک‌شانزدهم‌نهایی؛ اولین صعود کننده به جمع ۱۶ تیم برتر مشخص شد؛ میزبان مسابقات مقابل تیم چغر و سخت آفریقایی جان سالم به در برد
🇨🇦
کانادا
😃
😏
آفریقای‌جنوبی
🇿🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96719" target="_blank">📅 00:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy-1XWQrBo6Uj5hrOBXd7FmTEw07izeZ4bPPhEZtRrjXe1yXYQu6iZ6teVbUks7-BeJuyo6dKH6UzqLPhZGK3uxaoe9lL0gePCwQGtu8hP4O-PmfQx5VDKI-q5dbPN6mtBnLGlfm3bVrTEjrGV91aY2rC-C7Sc8w90CDcjVF-D7VlUK-o3GHTvrifCimeHxw2738uc_GctaQjIybrqYwPjjHZOAqs04ISUdW8ibBGz6tW-UFmFdFN-MkFLSH-MKcQSTPy8Mr8rTNVzYg5G84TqafU9-_JSwhx4aqZpMQEfC9ZQv3ChLsjKvab7m6Q6gXQMGBoTfXwcrjBjek-leHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به آفریقای جنوبی توسط استفن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96718" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1d55eec6.mp4?token=SeaGHnQDf6J6Y_n3qzlvxoceQDb5-7diFnympcrgLkYh-GTt3KHk38dyWHkoypVM68SOoIFlRnkMNZ0QckSBjpCv0z-Em76_aY9u5nbkH42z6B8ZzJidW6NsAqb6bVMTfs_1Oo-kab_LXtIny1EuqcpXbZIdZtgw8gYz_SKuJJgA5Hobg2tRBhtvvwHmVK2jCfyh8ULBQbg9bLKsYSrkeKaIuhDcUOnR7fdcOKO2OVkPJRCzricHqeOtfVoSv_v02MS2S3kh2HLPhOJpdwbb74y7l2Cjh_a1VQ1x4I_lJ2xY577UfgeX3Dd9dyhbJJB-W5EVeysSI7411ShYPDr_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1d55eec6.mp4?token=SeaGHnQDf6J6Y_n3qzlvxoceQDb5-7diFnympcrgLkYh-GTt3KHk38dyWHkoypVM68SOoIFlRnkMNZ0QckSBjpCv0z-Em76_aY9u5nbkH42z6B8ZzJidW6NsAqb6bVMTfs_1Oo-kab_LXtIny1EuqcpXbZIdZtgw8gYz_SKuJJgA5Hobg2tRBhtvvwHmVK2jCfyh8ULBQbg9bLKsYSrkeKaIuhDcUOnR7fdcOKO2OVkPJRCzricHqeOtfVoSv_v02MS2S3kh2HLPhOJpdwbb74y7l2Cjh_a1VQ1x4I_lJ2xY577UfgeX3Dd9dyhbJJB-W5EVeysSI7411ShYPDr_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به آفریقای جنوبی توسط استفن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96717" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چه دقیقه ایییییی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/96716" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللللل کانادااا زدددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/96715" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad99d57cb.mp4?token=Ntje8PUlKBsyZGr_k0FoRn-TfmufNaStJRFC_w2kXZrHcJHbjvJvN86pBkiYpUNtK8F0glL1_--kJuLUoQXharl5MJwAmE7ZXzFW79FodyoN2kPdzpEP7tH3hsxGfXZCMeSdKusjbghPM3ISPC7sJHssjgaZfGUAa2NrQpKrT1BGPMFt_58O5B0VFs4_f7YZwXYwPQfDWLMHZazikBtfTidOXhcALtJzUc95QQ-C3IqVO4wBFqw8Hw0th2s-5fYsjOQYOgVkUFkj7F7D9d_F0wlgiJuLH-C6Jj_sRrF_rbncCuOJckY5RpH1-c8Uy8B73PA-4xDsu0GPqtqICZd94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad99d57cb.mp4?token=Ntje8PUlKBsyZGr_k0FoRn-TfmufNaStJRFC_w2kXZrHcJHbjvJvN86pBkiYpUNtK8F0glL1_--kJuLUoQXharl5MJwAmE7ZXzFW79FodyoN2kPdzpEP7tH3hsxGfXZCMeSdKusjbghPM3ISPC7sJHssjgaZfGUAa2NrQpKrT1BGPMFt_58O5B0VFs4_f7YZwXYwPQfDWLMHZazikBtfTidOXhcALtJzUc95QQ-C3IqVO4wBFqw8Hw0th2s-5fYsjOQYOgVkUFkj7F7D9d_F0wlgiJuLH-C6Jj_sRrF_rbncCuOJckY5RpH1-c8Uy8B73PA-4xDsu0GPqtqICZd94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
توهین ناموسی و بیشرمانه میثاقی به مردم ایران: کسایی که شادی شجاع خلیل‌زاده رو مسخره میکنن، میرن تو دسته همون جاخالیایی قرار میگیرن که قبلا صحبتشو کرده بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96714" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBYgTYKjGSDHUk6KNFoW3YrzBkcDJPQM6mOo4cECdFrrLO5mFCLlKQHWMPyM4XHPsGhnQf_UIlL81nRnVmMKjMCvnG9kXhn8pv_yRdn0ULUFEH3s9ppEUpn2W92yBD1RRnkpu5HF-3JNs8r-FR9cA4GTxZ49DIwlHlxhKPtAyavy3tMf1_sK4_yJW_XMbYhT4ZngZ2J5Rtl6VwlUVs0QCxHTHMaB6tdsn5l1GhKlHfvpqQhZHnSZcdU8rJsv-shpw4F3WH_S2RZCSiQbLoHbW5DSyhnt4_RhdT0FzSmpLFqaqxg2lie08QPxAb-kC4T9AglN96UUvUe_BgwxRKGtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عثمان دمبله میتونه اولین فوتبالیستی بشه که تمام این جام ها رو تو یک سال فتح میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96713" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126ee96f6b.mp4?token=n0Q-WEYwStSVA2y7cU_YuCe4HEFjd401EQ07d3wHg7b2saDOkO7tBmDgknhZY9YZIrCdoFluZw50bYO6kwb_dZCDB9LTyyr_Afn8rsa_O1rDLcagVEzpc844FxuH8AI1GN4bCfqfBlC59RgnPbRXKHnzCe8OeqU9OM6VFyzxGeiDZqMFlLhb5lMNjG6jAo8vdE0CltoGp1l_kKSIYYNNp6DWKPzoOiT0cEOh0YTg0gqDdZ3jTNRIH6I93EkkrGKoQiZlfyrCGLpR-9W86yjINyE5Ly7q9Rx14tUnxdXlgWjMM0vOZ4w2WnT1hJ2En7K7hYOuxuGHq42bF0LpYbuZ9FHF91E4kXTDmDxTs0aQJC1OGxYA4Alz6O2JFR3QklerJv-7pRrEDQSTBjjBvq_UP5C_PgJm9ajahKtriq7qHDxQpRngHvdVxQhnFZa1BAxZ5sr11s-gvuCjbwVlb6TmyAJYjCIRLYqdV8pmjKhCOc2umfQvo2DGDSrw8hUpEZFo1urvlUCtCR6fC9u6OCRWTeL7RZMU45YZ7tLNlRvVHjZ-LRw5HOBb-vNx_vmHQXaIhc-4enXnLnuc6STBJw_XeLweAgLWav-h9nHtFBi2rHMflomqk3etz8SosPv_8ryravNFarQuQ8r5YvE1t5hyQh1Wy09CtPL1IhZNAjNL110" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126ee96f6b.mp4?token=n0Q-WEYwStSVA2y7cU_YuCe4HEFjd401EQ07d3wHg7b2saDOkO7tBmDgknhZY9YZIrCdoFluZw50bYO6kwb_dZCDB9LTyyr_Afn8rsa_O1rDLcagVEzpc844FxuH8AI1GN4bCfqfBlC59RgnPbRXKHnzCe8OeqU9OM6VFyzxGeiDZqMFlLhb5lMNjG6jAo8vdE0CltoGp1l_kKSIYYNNp6DWKPzoOiT0cEOh0YTg0gqDdZ3jTNRIH6I93EkkrGKoQiZlfyrCGLpR-9W86yjINyE5Ly7q9Rx14tUnxdXlgWjMM0vOZ4w2WnT1hJ2En7K7hYOuxuGHq42bF0LpYbuZ9FHF91E4kXTDmDxTs0aQJC1OGxYA4Alz6O2JFR3QklerJv-7pRrEDQSTBjjBvq_UP5C_PgJm9ajahKtriq7qHDxQpRngHvdVxQhnFZa1BAxZ5sr11s-gvuCjbwVlb6TmyAJYjCIRLYqdV8pmjKhCOc2umfQvo2DGDSrw8hUpEZFo1urvlUCtCR6fC9u6OCRWTeL7RZMU45YZ7tLNlRvVHjZ-LRw5HOBb-vNx_vmHQXaIhc-4enXnLnuc6STBJw_XeLweAgLWav-h9nHtFBi2rHMflomqk3etz8SosPv_8ryravNFarQuQ8r5YvE1t5hyQh1Wy09CtPL1IhZNAjNL110" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
کنایه‌های طولانی عادل فردوسی‌پور به حذف تیم‌ملی ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96712" target="_blank">📅 00:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
فوری - فابریس هاوکینز: پاری سن ژرمن به توافقی با یان دیومانده برای قراردادی پنج ساله دست یافت! اکنون مذاکرات با لایپزیگ برای تکمیل این معامله در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/96711" target="_blank">📅 23:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پشماااااام چییییی گل نشدددد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96710" target="_blank">📅 23:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ef2aada9.mp4?token=TR_PJBTVTiyAJRjW_yuX44xZ66lwrVlDkRQMtfFaFnnR7a-G-QT4Lb4rU7RNaUfxiSFxIZKv1YmbMsXE-eiRqhMlaZ-kT-bW0CZ0ZYpfjEnTwz-d8Njfa84cJ_B3T7yKx6xhHMHNkuaILPAgrC-Op3Web2exDWJPGzVNyrHBzvmT9H0sWH5Lo5TQ6FjezVDPtYFykfIUliYoUn6PT8X_r8GVsS24P5nMCt3QZHSv41KSm4Idf3BXKviUQtvzV9TowcWZ0QiZzTHHncmcXCMYLtZbzn-bdkEanqPxgI5D5a4fV4xQlCAqFU3lMTRcOIN1w8_uCMrmPdm-kr5oih2UFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ef2aada9.mp4?token=TR_PJBTVTiyAJRjW_yuX44xZ66lwrVlDkRQMtfFaFnnR7a-G-QT4Lb4rU7RNaUfxiSFxIZKv1YmbMsXE-eiRqhMlaZ-kT-bW0CZ0ZYpfjEnTwz-d8Njfa84cJ_B3T7yKx6xhHMHNkuaILPAgrC-Op3Web2exDWJPGzVNyrHBzvmT9H0sWH5Lo5TQ6FjezVDPtYFykfIUliYoUn6PT8X_r8GVsS24P5nMCt3QZHSv41KSm4Idf3BXKviUQtvzV9TowcWZ0QiZzTHHncmcXCMYLtZbzn-bdkEanqPxgI5D5a4fV4xQlCAqFU3lMTRcOIN1w8_uCMrmPdm-kr5oih2UFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
لاشی بازیای اسپید لای فنای غنا
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96709" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0RODC_rSJPEaR-MQk7YSeqtCpfy4tk2zJfQSs005s_PiNizw9znuiHVNrCNHNnTsfump8ICTQCiknTyvQjd0yd51rKrCBA9bpynWC6w_6lU6EeCmoa44DwjVS17y77_L64TqS0fo4hyay1GopIkPrr_1a-906BvuVY3Mqv40j52rKjPYnyBXcWKze1oS6IlOfE0WGjE0GOMyw4iG7LpbG1Mm2_lC4pDSsUjulGGSww9mZLLpfswr6ynRBJFvRSMdF4QcDqxTa_2R7c7k1M84b0CFK0YLyYPEWnpYTzoNPuqdLa9s2lIuuc1-yfVNL6lWt0CYvLrZXWmDBe-evw4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشویق و موج مکزیکی گاهی وقتا تلفات هم داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96708" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/96707" target="_blank">📅 23:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96706">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پنالتی نیست ادامه بازی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96706" target="_blank">📅 23:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96705">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پایان نیمه اول کانادا 0 آفریقای جنوبی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96705" target="_blank">📅 23:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96704">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پنالتی نیست ادامه بازی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96704" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96703">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وااااای چیاااا گل نمیشننن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96703" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96702">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
دیوید اورنشتین: یان دیومانده تصمیم خود را گرفته است، میخواهد به پاریس برود، او به پروژه اعتقاد دارد و میخواهد توپ طلا و قهرمانی‌ها را با پاری سن ژرمن به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96702" target="_blank">📅 23:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96701">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmGDzPsVPV5z7B7wQPzXC3tuwYY8NDC8kCCA0XStMwpsf205lVD8yKbnX-nkfBcX2ymkgCC6LiREM1Q24EGK7EVnkcOpLnRS8-SwXNCNRUcGyVNZPBkqwM5_-GHWTW2uwdASef_8Yn7HQ5Wz1CkkTz2A98WVcgEFmg7_djyDkNM6qY4oB0HTsgpJDy1lB9ZKquzJibt-cBiXn4AmI9Hd5noPlX8lnU9PHx1GgrCROoHcacBkhbpgmn754hb5xKonVSm_8umZUT3okf4FGEev15E-YVotGkv5MHhAfIZ7QCJVFpCLR52Bcr6pCU0ZMf1J1CnX6dr-2e6WloGOOAX9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی یه بازیو هم از دست نمیده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96701" target="_blank">📅 22:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96700">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ای لعنت به هایدریشن بریک گند زدن به فوتبال</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96700" target="_blank">📅 22:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96699">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-pBbnm7jarWZCaTmeZT-wJ0NdrIBxQCUwEdXO_P0SMx_z9kH-dY5rp6YrZm1aDK6yj7RS-g8pdHtzc9vD7GMs5a_CjfCidV6DZmfQ53eKCa7Y0A_istjRUUTzgidZuCUi7PewgJD0ed7OOALGSxbv2v5O-Ybw6zpH9FdGY4DyLefvq1XH0BgdRZbBFBCL3284ZuQl0SvmbB1UshH4DFiHOZtD4lPQdblm30sLJMZWqaZLLUER1PmgDv-mJvogQtzVOhJRpYyEI0BPoNcgvy3H8om0QbjAnSF5g7qafku680AdjVSxx5WG8KlgR6dX9mxgjy-g6LyQXKmKCA7t5yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست اول بازی تیم ملی والیبال لهستان و آرژانتین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96699" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96698">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شروع بازی کانادا و آفریقای جنوبی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96698" target="_blank">📅 22:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96697">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKz3_IB-iu_HksV6oSOt0__6ouNBdyCzQ4Prjyxx_xVDD4Hmf3UJTOQYUJDHtXfQRZzgIdravvOm40_l3fHcPPAsg6FM5Edq8YUqP181RnAWmURwbIpJ42PwwuPiImXfnBsru_Ukt-rtiND3r7gkTdgkACeWbmfrT1w8A2U5cW__rqt8CJrT7wnrNbVt4WJQg_X0L6-7gNWsySQCxfZOBctXGT8gbqFOg5B9WGzKQZX5tMCR56Sp1B2ILAnikGlJA69tZ7Ds-rpE1Hy845b6lg8ja9Rm1aIVy5lsgCr4Nt6Iw7ERsZQz8NdLDbo2606pESfBfTIm_q7Q_v99aDdyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
#فووووری
— نیکولا شیرا
:
🇸🇦
مربی ایتالیایی آنتونیو کونته در ساعات اخیر پیشنهادی بزرگ از یکی از باشگاه‌های سعودی دریافت کرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96697" target="_blank">📅 22:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96696">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPmJlVdK3pkLv88fPycNLwcOjdOddQMMDc8FeSgmc7-S0MlygrtYU_gyWQ8zA2BfSbF0wVoEfi6_km4m6YSFb6ZNrFG3Frp1-AzHrLhXZDuvoYUt6ZIrGfSLNZO1v_3XoVD0YZRdBJUZg2QOwZrIxyvyniUlYv8LYcXzlg-ZzM02Aw3_p7p5AcNG0Cely8IT3i2i60Eg8svJy_ZNFxtMKqR6m0oHLQLQlZQdwlqw-oN61BW9l60kExLE0fTIwViUjgaMdaZQiICkpLrZNwedlNfDV1_sZTPk90X0hihH2x4PBLI05O11_-5OyojhqboRTsH_I5tEYBsWtepzabjKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دیوید اورنشتین:
یان دیومانده تصمیم خود را گرفته است، میخواهد به پاریس برود، او به پروژه اعتقاد دارد و میخواهد توپ طلا و قهرمانی‌ها را با پاری سن ژرمن به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96696" target="_blank">📅 22:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96695">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری؛ فابریزو رومانو:  آلوارز بارسلونا و بارسلونا و بارسلونا را می‌خواهد. من مطمئنم بارسلونا دوباره به خاطر او باز خواهد گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96695" target="_blank">📅 22:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96694">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBP2GT-HHV5CufgWdC9U2lR1X8kxQBAnmAIE5Stc1QIYDFwXY1XLzmxzn6XERvIyGFy2B-TAQAoktY-s4JurjHw6yYgFsv0SB49_pZLtHO0Mf3HSB3_PtZ7OTz-jCmfsyPpkT6_8paRqYN6fr0sCF7Ob8Fk5pGC1aqZnkGMJ-_76q58643qzZFDrnkgGf_4ZvJqV21FHdYz4d5QiML7G8CEfjILUFBfl9-toLvOBByKODoePkkWXm10aL5YAmrHmteY0tMSI0akHKGRq686ucmaUAqJ1uLz0Mz_uiGuwVJD6895YzalCWlcltJlq82HHO7SEWVFCAX-G8G7jBqIUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/96694" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96693">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4IvaIn9_0yV5dpHEK3aQHejoPzOmL-fpcDZjc9tWWqXdHeFpvvIKaeAdm8mRhBu6kOw51bg5BMdllplP6HL_o33pnr5tdWKJnBPP7c_dr-kq7fkGDE0sXu5SwvIcR7Fua4MOWrKG-4Lbq2t3LghJ4oIgGvWGH7250RzH6G_j2jIb6QJVq9amRi7zUXTx65bidoJEEk8nzdmU2oSNqbnhRfwO-g4P6-EXfShQ3K4TBvRD-N1k8eVmhZQbDbUw1Qrvf8fQvtler-k_34xgwUkpEe4w9IMJMGdW2-DYVOrluJQlwXeQ2nItu1woo3X1Wayxasegu3WMJSi6YNtdiNOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
رونالدو نازاریو : نیمار؟ امیدوارم عملکردش همه کسایی که فوتبالشو تموم شده میدونن رو ساکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96693" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ فابریزو رومانو:
آلوارز بارسلونا و بارسلونا و بارسلونا را می‌خواهد. من مطمئنم بارسلونا دوباره به خاطر او باز خواهد گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96692" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKPJb9NT92IGPOufbib5xdnjY3quPAiF91_55zWBCO-XuqmlLJHc4ly2Vigi692xNdMVeTv9zp6-ACMyeOKaqX1Zfk9LDrSeaWCY9FUIlghe2ifyO6-ijv0Cp6gE1qpqCLnhRAAQHQ8iz1jOnf0IUXf4xFg-CeofrTQu2uXO3KKiUfPkXx1rXnL3JKKCDqEEUCosDr3mZqOp2Nr--13lCWzG2oh8OCyDtIbSWknEi6MPeaojppE8rUMQRvSfwrz16aOvEBaurWkWgsl7fie2rT6N4U5tTIlY4YxLcaS4h1bACHzaYTFaCN6YV5ap8zqqRXvaXxECHfHc0P9jfVjfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frv4e8RpEHXTj0TxypKKb--cE9x-BOseWIQb_2Ycj9cK3DPACXMHpGpOAio-pYFp7yfcWaapFOeNEMUAu0MiZv266TIquyLMeLpATnLAIxFHxC2uhnnPAod0_buRyQ4I2JztktgB2iK0w5OJd-6Wvy1f7hyTzw-oS8V4dkPqTHtPXR7HA3HFMNCSeflEW3FFi3ljI76qzxG523KWOV_Djmrl40Qur-ZPIZ704yRKqaOdirjqzNS-I9apRkSy0Yp29bJ5lDEF_091QP2VjDTttxvZRNGS3Xcj85XWOrvUWFfD6r02MN7rB5eQAAKz8g45Ph9vOd4QgavAEniQ8PHBdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇨🇦
ترکیب آفریقای جنوبی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96690" target="_blank">📅 21:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGqhnr8eDbGzRUQpFE_juOf48HccKNkBva2JbiJ_ozUNap5pYI4_j6hXAiKx8F0YDLczqm8rzGtuEkxR3s5PK1Q98rVf4GOkyG8HVcrBB3OiZTMngbbkBWydm__8npzlQ8nshc1rGi4vJ0BIMn4Wv2UyhgSHDuV1he9wSLBMjN1R9Uu8IgsRO1ic3wiYR0SRP95zJlSwZgrWAA6vWMAhHmwedaoZHFGKl9utC4AFy3viJ3UW7k6bQOp2RnZgr7rBRatLA7Og5v2Y3fYYzKcsjAznBAj0taqQOy5QE93UjBzzuVccU7Qae9a2Jh4Qp65WVMlxdmP6D1rAmj_3LLQPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
روبرت لواندوفسکی به شیکاگو فایر آمریکا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96689" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96688">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96688" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96688" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxnYfvSTPEw-AliczptmDSiXxsAKsxGp5qpDxx-PjNZQopiKxL8ZiSYOxrTgdDELkK7WcwcuBugYZlSdhf4TySHh9uYbDlvRKAKG8zLpnNohB-OaJ-4b5UvThzncOI7HF8eQ3OzsT1ida3aVzLXyOhfZ0jZJksSH65E1-RklENRXd2dp3AlGn3b6Vb5qtucwwR7UO0vvd6SyoNamFvgS-uGxcDDwhfS8Lx9YRDBiCqhazeE19szJjTcrh8jsujO4ZNyz3j_mqGCuRAIqq_ak0u_nKfqgsGYrdHgar-1dawe5a3dUilAL1YwDJYJtdQ5ZzLAikhaNShb_6o466RLeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96687" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=NlXheUCjWEEIc-yhEnuw8Ye7U3xHcv0wkc_uuB3KRfze7WdZn9JD4-302ifPp6i6FI-jdWstewTJ1BEcNtqgiGBDKiNvcLGfH-CVDGB6R1-fPlvQJtTO-OhFRTrkYy3l7vYA8Kh54Z7vmV3E1uv5a7v7C2gBZwWkY6dezzCenGtNYbD1PNBzSw9GNKeh6pDxsS_ITv0JGiTOTFNY3P90RD0FHa_L8pcJ2qxSQPO6S9AGXbTRYmS4WKl3iZuwJTLojaeu0ctT2tyXVa78EYvtNw-AyvXbqaZ7AGpMkZ6TxBEd0QKTI_e1vrA8tl2Do1rugQSMWrk-pNdQvExqS0_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=NlXheUCjWEEIc-yhEnuw8Ye7U3xHcv0wkc_uuB3KRfze7WdZn9JD4-302ifPp6i6FI-jdWstewTJ1BEcNtqgiGBDKiNvcLGfH-CVDGB6R1-fPlvQJtTO-OhFRTrkYy3l7vYA8Kh54Z7vmV3E1uv5a7v7C2gBZwWkY6dezzCenGtNYbD1PNBzSw9GNKeh6pDxsS_ITv0JGiTOTFNY3P90RD0FHa_L8pcJ2qxSQPO6S9AGXbTRYmS4WKl3iZuwJTLojaeu0ctT2tyXVa78EYvtNw-AyvXbqaZ7AGpMkZ6TxBEd0QKTI_e1vrA8tl2Do1rugQSMWrk-pNdQvExqS0_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
بخت یه جوون ایرانی وقتی ساعت ۷ صبح به امید صعود تیم‌ قلعه‌نویی از خوابش میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96686" target="_blank">📅 21:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2POhQD5Mme3zY2RE-rtO-QIX2wGoZPQQ_wftPxQrYwqW56nZF0UlIaq1X3oCoS7To5rKX1NfWsc8gnhvE1Bo45ODXQ8UXVv3l2Y3KR-jsK2wB6L0F_TXdgnllWWOtA2O6XJP-FIyiqFbXefgGWauhVXqWRoXGqg-mbHjAv_FqQE8_UXrZZOQnItyVkKK-r8qV-jSJPTW62EV59k2arBv_-k5NeSsR-yg58GJDEtLPUoS4OCC4Zgw8wwaWtxuitZbW4vexVlIUYkClsnU3WbSYlRbX3eKGkI9Ehs0qqkbyIqFjRmbnHYOSMA6krqMEY5zwrHE3NH0Co4PISBecUgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیکلی نیکول اکس سابق یامال تو کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96685" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=u7uKC8bdJ3yT72G4WOCECded5clOiC_Uo2alKiguLZgVJa-Go3-PewQRlo8cxfLefwNuys_mAscmwXA-DGDXkSgnDJj1alJNdHeRjYn52Lc8_UbDuVrO9RaRLe5Xc5W2hCAo4TzdTUONVh591TcyyJ46uc29B_blTBZDCOE5wFcwiN3jnd4pR3imtqL9F5GrVqtKnG4OmKUoVZrRmcCT04M4mW9sbFRNXfyHP-BB4G3SenD8eWE7pM6EEuadDEkQAUs2F1PH7080zfJTflVCn67snuJ1UDcn71yHf_tl4KheRg5HuEFVw7pKwFBxlxL6Qf78SBzGqM3WwB0VKGthaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=u7uKC8bdJ3yT72G4WOCECded5clOiC_Uo2alKiguLZgVJa-Go3-PewQRlo8cxfLefwNuys_mAscmwXA-DGDXkSgnDJj1alJNdHeRjYn52Lc8_UbDuVrO9RaRLe5Xc5W2hCAo4TzdTUONVh591TcyyJ46uc29B_blTBZDCOE5wFcwiN3jnd4pR3imtqL9F5GrVqtKnG4OmKUoVZrRmcCT04M4mW9sbFRNXfyHP-BB4G3SenD8eWE7pM6EEuadDEkQAUs2F1PH7080zfJTflVCn67snuJ1UDcn71yHf_tl4KheRg5HuEFVw7pKwFBxlxL6Qf78SBzGqM3WwB0VKGthaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
😁
دختر جذاب ایرانی با پدرش تو ورزشگاه سیاتل که به لطف‌طارمی ناراحت رفتن خونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96684" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207e25de79.mp4?token=ZZ5GhGDDtSx4_t6SS8VT-VhXKBN0Yo6psn1Fl0YyL1Cd2jxNczae_xCpXqVhcMjolCeTuUHdcS9h_HT6Kn3Qf5SD1grGRanMukhREvHlzR3DjGG7DIJHf3BLKC_3RZuRhl2xSbKabpXeglDSV2wfhpJCYuhx9r_-gOIXhowKF-5y799SCV5WWSiuApw5o4-Bhjj7le8BaJu-zIBtLGEWb7oSXksI9E3BzzEMfb00hjwniWGnP0xwF8wUd0JDjVzsby-GeLA77WUiEu_D38a65xz84pk_vhS3ld86DQiBdIcCAggNwpqXGfqZvMTLhU0GpUOcwZagpKW88vW-AhFeT1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207e25de79.mp4?token=ZZ5GhGDDtSx4_t6SS8VT-VhXKBN0Yo6psn1Fl0YyL1Cd2jxNczae_xCpXqVhcMjolCeTuUHdcS9h_HT6Kn3Qf5SD1grGRanMukhREvHlzR3DjGG7DIJHf3BLKC_3RZuRhl2xSbKabpXeglDSV2wfhpJCYuhx9r_-gOIXhowKF-5y799SCV5WWSiuApw5o4-Bhjj7le8BaJu-zIBtLGEWb7oSXksI9E3BzzEMfb00hjwniWGnP0xwF8wUd0JDjVzsby-GeLA77WUiEu_D38a65xz84pk_vhS3ld86DQiBdIcCAggNwpqXGfqZvMTLhU0GpUOcwZagpKW88vW-AhFeT1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید بین هوادارای نروژ : چه خبرتونه کصکشا؟  من اومدم هالندو ببینیم ولی چرا کلی هالند بین تماشاگراست؟ اینا همشون شکل هالندن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96683" target="_blank">📅 20:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktz8DQ4dU2K-4gBYS_-hITKDL18U7x6PJ329-BDUeUimDd9c3PtonUp8XEPeb0Je90dXR3Wn6Jr3BnSet6E7-EZhQ8ytwq_UJeG7DpbFTTffSLKLz28enfFLPVziAJTke2H-fTdqCjNY7vNKsPxgC4GB03AzraGZtk9nkgma7vfCFOo8faZo247h1fkKtnliUJ-UM0RTIw3-wxlbYTlxTBzjP1SnUMcwwiOTyUAMrOfqoWNzqtuBzl_bU2v8AyDEPkGfipgC6-26wUM95olhHj115JT3PHxEMknFyNze2qHU9TLGVE3nFIMqEaMTX02PZS13Ir2UUuEytGg08ubVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوکاس تریخو، مدافع آرژانتینی که در لیگ ونزوئلا بازی میکرد، قرار بوده برای بچه هاش کادو بخره ولی چون مجبور بوده برای تیمش یک مسابقه انجام بده گفت: وقتی بازیم تموم شد، براتون کادو میارم..
🔺
بعد متوجه میشه تو شهری که خانوادش زندگی میکنن زلزله اومده و بلافاصله برمیگرده به خونه‌شون که میبینه ساختمان کاملاً فرو ریخته. بعد از جستجو متاسفانه لوکاس، همسر و بچه هاش رو از دست داد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96682" target="_blank">📅 20:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=b2LVYG39gy9fEKLS_jFQS1SMl0EW3sEh5V9feiuSt7skhDKjfgBNy9eyd7YCR1ybe5t38vv6Prchh1DYth5k6VZQKA2TMYTZvBKyYNc1bChF9U-hsA9juW_xfdwQTOaIq-bMYTQ0xDnaZlKWvxTODuR2UAvmJFwKR6XSqnHD0AJ4i1Am-rAUKRc8aHvS4TZC1LcAEXxjRR_pVMhR8REKS_5zHC5QjdMGYhKXMcaLHqtK2PJ6ZiugHK6SxtxIGlFmsYi3_d9yxBmwkrSKqfcY_s5AmVx1MCgJAcmdsgQ7OxK-5BK46LGCCINco9mDTJlBwiRKKmi9xvBAnGTf70smVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=b2LVYG39gy9fEKLS_jFQS1SMl0EW3sEh5V9feiuSt7skhDKjfgBNy9eyd7YCR1ybe5t38vv6Prchh1DYth5k6VZQKA2TMYTZvBKyYNc1bChF9U-hsA9juW_xfdwQTOaIq-bMYTQ0xDnaZlKWvxTODuR2UAvmJFwKR6XSqnHD0AJ4i1Am-rAUKRc8aHvS4TZC1LcAEXxjRR_pVMhR8REKS_5zHC5QjdMGYhKXMcaLHqtK2PJ6ZiugHK6SxtxIGlFmsYi3_d9yxBmwkrSKqfcY_s5AmVx1MCgJAcmdsgQ7OxK-5BK46LGCCINco9mDTJlBwiRKKmi9xvBAnGTf70smVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
▶️
وضعیت نفرات تیم‌منتخب ایران بعد از گل تساوی اتریش مقابل الجزایر و شادی مردم از حذف شدن تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/96681" target="_blank">📅 20:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTYsvJvfzH6hu4-j0V5ob6GgdE-iBGnZc60xMGQdjRKo8rzVXvEqSjPTmy_zWyY6vL9su5FobwA0r1tnR-5xP_ShUMSnz8XWb8qzITzQO96DESD6rmSPyi27ZAdsWXE6pZq1YeGYckV8y5n2NJmFidxxkL3USd_yVKpHthDTcBMoqUjPuKDeiIB_6r6HZ3dJ3EpDVVSsu0ek0jdL-7X4sdhLxnbiFlxRcWIxV4vBt4erO5DSk_OkuGHiG49oWe5GqiE6nFJvZYXjFhAPbYSnT-HLJUfDBQcY8hteZ65G9Mk_iWGq7hx9tNhfvPpQZ_Be7TI1Di8vuuNlDKT1cydkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇵🇹
وقتی‌بازیکنان پرتغال حرص این‌دوتا بانوی جذاب رو در میارن و سوژه رسانه‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96680" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoe7SEvRNFhldGRbdMoilkg1mL4Kc3tVK71cUgRmkPLENSJ1wRNoG4xMHwt-CuJjASbsw9rzlXElmdg0k4rmhwI_qXxRx34Cp17H0i2nBiIxIndDUDPWA8pZcsSwdx0sJmJUuMoU2_MtaekheyYKII_RYcWuW9IHw4LCdb9kTgy-rElgiIRVtawLwA-qIiZxxbEiGGn3c92OrwicIBVNM2nxY4_Njp-GXhio0fjAHP6MKshQ4qFRA7oyJyjRwDSK-BOpb3OrMZzFpYusN2sXpxj0apKxbAwSQwxEsh57crSiZBPu8XbF9251j6xP3RoPFDWBTqzG85AK30BANI_wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJiGhs7i1RQlO2-veb6lGjIeG-Snx13AUITp-YPliEkhNE0PfldiqA1fcbqf0tdDakpdAQjt1VqK-LSac66gZwzbmq-ZEZJCokDQzQ-YY6oLXjeQf-74mtjCTdQTjfZXEG-f6b3xMBc_JhQ3fMRo_FkwrfWfCmbdFt0JCN76BhjdPzoRBXmZMnNxAUTEdpCM9xcDk9SOpFmuDKisXmNP9zz7VB3x2nyil0DwTeqZgbQwtjmXbRWvsCmNoedEXd4OnIgNh9ZP4lAyDbBaR4KR8S0A1SqAcinuSrlWlaKxZUMfNGEk6yW3MQlwI7GcOEUsqzX3i4X46lQwYGlsjnk6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Seqz263jj7lsDNF8fSrDcZ2mzXN8SisGR2dppJ7n5nRYpAzJo-JxWj5JveJL0ZuOfIbKGr0aFnh_vHPBewvSySBcO2GM2DrEXU8StjW_j6_kg7K-52g9W4c_Q5YrW6__vH4Znh0y30xjgqcMG7KsLTjuzQVYAfnQXyRAmS8AGeiUGq8GL1e-g6FbcQUXqU1Og4GIJyHopg-6t5n6JleRisoz8nCpxfy_sFpdEIDvcEdJ4GUC9W7J-E4QpvavHrPNRsuWT2bN2QlXu6F3rdvJLZNB2E3u3PUNDYjOvTHY4H713voljKGyuhKtSDaRMTbv_2oMoxJeIj_P4cN8Wyrhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJFSk7oZrDkQsgZE7k4BqmGgHLXFIKPx-LMvXAIgGYZQF9YWPw0hUysYKkFkg398cI8qKveWVP8uNnryOllnDZeLDgtiV7Hca0Ai_I4qp_xo-TwtIhmy41Mo8NOzdVJ0ytOZCxBMXYxBUGgtcQze-mNSF6iJwcWAPbKX261bx0SGSBOKgQE7mdCg9pdUXj4eB-jzoimB9ePj-rGPM-A0HQeq1weMzn1wVkiBYv-hq1gmK-PrUkhJM-PPn-z_zMpvCLQAq7T5MSwsGm0vyWpdIzh34swQ8I73SJS8Yxkb17q-zQ7_yN4PgAKuglUyj7p1wvQu9prkGXn7EzoBRSIUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p52Cnc0e6z9njLp1kp_yqZRvDy9A8UubstRvT2_JabDXk8ScQGuzc5PL-PwBfj-VqQdXHpDJu4HaTYkmo_cnsHIo7nf5hxUWYPh4BBhze-39rpnYiCCyKHEP1YG-jHzDQW4xcGrjZhV-A5Ufr_Psk3iaX9igN3J2yzMgFgNxUBud7xFlyFIbs5UdI7DT9wGhPeMapTdVQsKcKY7RAn_ftD1ykjMRpBPX6Pj1oLCjNTHybMreE2lkM44nYzTDsgQaG8BzJiTVOznZHxwaYtKMnHdZ2JGcnjOQZx7-bdMRluDC3m3bGNFhh4UYmvZ4tWWxBD2glyXqwfOfjIC6VZI5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onkTsbrwcVWnG8tSmNy6mFAjMEkuqhAs5Uzq2tSyACJjxFP-LGAhaFku5b9m4qkxgbHeWqgUhEI_Gg6ACisiq-r8c7Hl8FGNOgXub_ql0kdGFpCwV2wznjEWHj6UHjA18BnwNGnPo7idJIGbINoBjzW2G2kLMdfAPeJmoQm0LLj80y6Rm_DmkT0hL1B5vnxP3u-cprBkgVXjUmta1rmERcbqej2Sl6U1TdyPZBvGDv7ME0KM0-dkE_vDnfOgds9_rDcghbRX_kgaM9JzE7f2ZQfEVV4ljdfyHNib4oRv7QhiKTcFBqegPMjqWvQilWCUi_rD1vGpy6Wlef2wLvjzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ha42RFq3Ovcm-IinnnfkLw8xE48pd0cegPgFYkXADKG5Gnqc11ZmQtN_x6PlGLMGLBVlHF-DntA3VlAtECmMzbowr54qzuMtPwchnwKbf0ZKAc33HvHM8-tLicENbF-NnR96F92cpGyFH_k4CnLBYE2gkMoyOLTCxi3JkRctGEfHszQMyC06zzNL6Luqs5ZcSmFfjHJhISE9-xsawAjJvV430WUh6yg_Uo-U4baYSo8syxEdd_FaeZj5daIOwUlmcVZ5vR1cW_YKv5u1wC6uxyyYiORvWY96v7X6C5qGhAZYAkApuTogbvOFocfyJALjCiQiQT78WRom3IE4xdTWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNxoNYaDjBO14pKd0ofvjy_8nIuXEBBb-eMdl3V-C86il2eLjFHhb-7iTbc--eHVmpb1wcXMO08PJBRH_Bz_VRKCm7QssK6wKu3OWh3Verp6kDiDEdIe4eVBkvwsGWviG7MVeDNjCUL-3t7NAuJ1mvl1_MvsYbTN6b_r1cjVIebUnAJuGzKqyKGTB0rJELZF7Yp0fhaaSQJmD5MdjJFzeFWceUWtlW2eZ7VK03tAs_3icmqUJ6BjOJen-HNVTud-lV-w35j9U7ZqjJnTn4tAziAqo0e8be0gcy9fWti8qXv3t5FO9s0JyDM2wIwDkol5NKtRNWxon77jnY-Ff2vJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3pQ0h1qCgIZQSqQCEpJuA1ahgns8Fb8zpoKnELxddtmwdXIW38lWj_efgVQW_yDpAfoMaE__twxlSgiRomlbEMN46-ysQ3cq1wdM6lRo3Gfjff3EX1xHbEQ5PXD6NvjmMXOnJLZ0E6zTlbeqNe9XgByaGV4-igR51YwXwYXG6jX4qc-8tAcmcL1alK-u4NiX9sNE52IaA9i9gz9_OmfQFtDKaBQYk115eJSCuZnV7A2jE_8TuX6wkz5QzkN1JyqbUcUxQAvVkP8JXWV-t2Z-nSCHLWL1SJVSeUuDwMm2sa83cTMXaXneXbVGlkqomGJTXyz0sUlvj_P-h7mp_oexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😐
🇲🇽
تصاویر ازدواج نیکی‌هرناندز بازیکن تیم‌ملی بانوان مکزیک
💍
💍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96671" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇰🇷
سرمربی کره‌جنوبی بدین‌شکل ضمن ابراز شرمساری و عذرخواهی فراوان از مردم کشورش، از هدایت این‌تیم بعد حذف از جام‌جهانی استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96670" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWaiLvpD0zeTx_IuuPih9B4srXhBAy4sl50ViSTFNq4cUacuBS99TQL8b0s_UM7uSSqzyhIC97D6TFjrzus2mll1lSEP_VgVBVdsRpU3ZIPZQbaK-p9QrgZDoReb7DpmzAZgyWhXQGb9OpSU3K-1UChuCxa_F0197YN7orwCWzPqQUgjrRGyk1uNlZpNCztoNKd_7C2yrqaLcpCcVHANsn9d7AWrBVdPboA-xGJDpcor_gMpuDhzuBUpkQGA6WsVPVyxnclNdB6cR7sx7bFA5cS3ldUxwVx5Tv5UQ1uQpzNMZ9pD5myOvFchDm0FVdRbIx7SNn1vhmXNXLUwr7X4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه منچستریونایتد اعلام کرد که مانوئل اوگارته، دچار پارگی رباط زانو شده و برای مدت طولانی غایب خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96669" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📊
🇩🇿
پاس‌های فراوان الجزایر پیش از گل در بازی مقابل اتریش که رکورد جالبی به ثبت رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96668" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRKFaa9t7MuiMcMN1QylkVdT65KfaTsfDenSq8YbshfBkYanGCVkxWis23GoooemuZH6dQj0TTfXnZ6DBbfHCtWqA1-uF91R75cOtUc-XBTyYQsP7kWAYVIkRk8xn7Wgp1MkA6QMHjQ5QalrIkNGvISKYFCxzl0x6mhrLJjvFh68D8StvytvvzHocEm1_xQjwEohP8_oLPE8d_CYXPWghtYLR-WXBP9CubkGUutkiUVXQBOXz439aOnHnDoueUuYA_sRkvanlZue2RaWjXnVuwyn0l0ZeLcfyU8ItWDDVT-vTfR7Ydd2uDodAT89K3kGfbRKXHEkT5fuz0KGs6c-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
جاسم بازیکن کسخل اردن بعد بازی با آرژانتین برای تمسخر مسی این عکس رو پست کرده که جمعیت عظیم فوتبال دوستان زیر پستش از خجالتش در اومدن و مجبور شد کامنتاشو ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96667" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😢
🇩🇿
خوشحالی الجزایری‌ها از دریافت گل‌سوم مقابل اتریش و عدم برخورد با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96666" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXePFfY5spNHuZ6WamMoSY-t5aCVPvdN6oMqHNwykNPQcALXRALyDmkSWXNDEzjIgU-mdYJhRckXr23J0S3f3duKwzbSQB5z6nRa_rQJiwj8d8Of03dYg7Tw-pEhwjYJ7kxJBdXLGlhNyypn6XzEifFS4kHb2Hw5rBrgXr_LxO0G2lxVdvGQkPiDVnScBGuJecQu82YXnpjvs_J-h49pCs6MIxHYpYUdmi-cx8dtglv7S6BKx4NnPLN8zVU2DCEGQaSiCDegJI_kMeMGGu_PEpRMhDLQNMpMsCtEnBu-O7CIJkDiVHtj6XTnjjSUH2F7WdvIQmuNpSYAb4PTZTiUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🇵🇹
کریستیانو رونالدو  :
• ۲۰۰۶ مقام چهارم.
• ۲۰۱۰ مرحله یک هشتم نهایی.
• ۲۰۱۴ مرحله گروهی.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ یک چهارم نهایی.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- عدم کسب جام جهانی
❌
.
📊
🇦🇷
🤩
لیونل مسی  :
• ۲۰۰۶ یک چهارم نهایی.
• ۲۰۱۰ یک چهارم نهایی.
• ۲۰۱۴ نایب قهرمان.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ قهرمان.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- یک بار قهرمان جام جهانی شده است
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96665" target="_blank">📅 18:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWY_Qpo4w3TuKLt7yPIr4QU7lNyAuRYCqfqknm-Qpv4yjUf6ozEs1q2ZqkGI0EoApa0A9_c_c91-UdgkzIPR3S-n_kgbuYvoe9h-aK4ekCnvh-zF6pCO7EcFemID6m3hZ5jN1DrhUpWRviscxb2x09SWX8ZmYRW6TInMdS9E0Ea876v_41a_SDgYngP_hIHW_lWNrE70kxxqJ2SbecZtpKb9E_p8mFNEq_NkhmmyKP8g4u39tBG8_AL4pcsvC9MnJs-mslSUf1hk84aaCfu8uQfiOw3kK10KrJB6xyz_jH59-ug6Wdic5uqQD91Mgva_lOLkCPyUUO5G3xS3qxkk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🏆
🇿🇦
پیش‌بینی اوپتا از اول بازی امشب مرحله حذفی بین کانادا و آفریقای‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96664" target="_blank">📅 18:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO7nFyMK7kurZlSf5Id_wTSbAw6TCmXiDYfyqJV496kImmDNmxRdzqiXbbEWWKm1ns4l2O4mt-5ut6y_9z5f03XSaQ3t9HDC8-3CGNHDIV4yZxTx1EfLt_HZJmVy-RzIwDsbLwHsgn7qVXS_2pzAQ2ZggOHlBzh_PeYVXCsJxEVDnU1por8Odiut60XjY6Sino6ZvjZ_iBAzpZ-LQQV36Bex0Tg79sH2UBS5Fo3gFzSlXpKpCIMRulDYHzB2m8hkWMlDfEZV5zZFfUByMYFbjDSdN1LKsU74h7vQ8P7wnpXNBcgPueiCAfSikX9gipKhlnyBCZ7N6Ob1HbVaiF-UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA0tiCQPiHpcX67DZGYZyLCKB06-nkg9u909E9EjaiLqHA35az7wi9zsApLOox9I1eRIRTsW1a9z2v-1JFasxbjrT7AbKBkF0Dal8hcGWcxok7ev4gnOkjvAFeqkG-A8ndkI-ltI18zEZ4KO243RF7J4Sl_JbJW89j8Ce1EUvn9Ijf03B_D5iTymI8CIgZvHsNlulyzen0Jr8dpv-znxygdBTgzdrGzb_vRQCyNYfCreRV2sTCvgTVVq6MW02TDUhLv5IdAPQ94IKV94BDfUM0DPl6_YYqRb0eO4rIYfdD9Lkgf7amIgaxG7AvRsQ4zkgLNmEfwAbp4a9ix3WUvHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phMI55Co7H1ryIiHVR6-p__MSvuxLVjsD5ns3yFLifpQKK5lXD8iwqzX2xo12scgpNOZXAvOkJ2QB4gfQnQGaCknros1RQ1RFxBDT56dVLC4sr_G0HQdONm-Zywn-qd9REaZOF7pK6jLVyBkXcca0OMopiuNQBAoICAEZYUKYv88ISpuhaoLDTwvhliedIAY7UuNAuErCk6al13MBg-fCv8EEQc4Q431qTPPRGGCm63fGMpCbJLDyG8QlfSgcj9hcWyicCLtiubA7YNnKxiUWCRiW6iuCIX1Zld9gRfLWoj27S5m8i9mezc1PuTQIXGPYCaa8dw1rCHSXVxxvhS5ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🥇
رئال مادرید مرحله گروهی جام جهانی را با بیشترین تعداد جوایز بهترین بازیکن بازی به پایان رساند، با ۸ جایزه، پیشتاز نسبت به لیورپول با ۴ جایزه، و پاری سن ژرمن و بایرن مونیخ با ۳ جایزه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96661" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ کاربردی برای بازیکن های تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96660" target="_blank">📅 18:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vo4McMsm6DDst9ABZBvqIit5x268PPu5aVIMzs-Q-bihQ0MraujsuC5B25OsODvpCfwtsTOY206MwxXjdnhvKh218NgdlVI6J50ljeWn_G6KP1dk-KhltLtnH-2Q7dDcg_kXThxMlOrwGzI1ShgGKsW2Keb3gN74kU4R0Q5d3NPhbRu6f8ScQmgTDHKBTtSTCTnUFSFy83U8IFRWvi2Cg5MQMWvvPm471-ZT_w3rM_6Np1BITJWDGhON-E7arFNl73DrQ3Mv6yGSpBjBO7UJS5dEipyXB6bUE2hFT7BdOZdhCxj4cH_06TXt3l_ARBEJfmrrDXPkOFe10kZaIkUQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myoxrrvRZLoG6WC0X2IW-dLRUZmd9tKQGmHIJvsGZaHTBp-rOyN_KY6a2BYPdQ7mAxMzyQa8_DfjweRDvg5LkNKQzCHPOLitWAUtPoKXGCSJRzej7-y0jOjltTgoO8QudILFdZ0f0bxpfx7GLfJ0RA7tEwAChlos0G-3A-aXBYua5dV1OarS75FMLHdbmXkYb-fgeMA0aqlz93bVqVNJbQe7M46mcwW3EhM2_SSBzMAvO1Q9WQRZqRSLE2ES5mue-ScHnZn-ZpjkYn-J7R4rRYpQVYGGAN0kTsv5BLVxQb47Qo3o3AzPj8le38BW5uAxWSYui4vd-_FXYfFbEMTVnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یورگن کلوپ:
یه استوری از سادیو مانه دیدم که عکس تیم ملی مصر توش بود و براش قلب گذاشته بود. از اون پست اسکرین‌شات گرفتم و برای محمد صلاح فرستادم، فقط برای اینکه مطمئن بشم دیده! اینا همون خاطرات قشنگیه که همیشه بین ما سه نفر وجود داشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96658" target="_blank">📅 17:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt456INXgWqIQnrZufnjZv_HQLpAE1F6Hpcdw5Pl4KlHvi3_VXvQu_bnbGBpit9vx3eodRVGbb2JxfvPH6YM8SQLnf1J0X6p80d29h3Jj-4quc69rGmJWvmkq53XbKomJiuUzPpssTpZZgfQj5arr5EtZ85XiOHgo80BfKEKYAEok7avPr_cFX7s792-_veXJdBJ1Uvau6nNHSdP8gO45gHUp98h5gUDg93dSeotaXjq2urMe6Cd7OlOAKiHt2oUugeBTky5zDaK5pPt0kPg-tn4yFB4bvy_FdrVan-aOB7dmbdLmQattG6-fORpHnC7Eqdj2yAYX4DHEFPO-vvd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیووار:
در بازی کلمبیا و پرتغال یک فاجعه رخ داده و گل کلمبیا که 100% صحیح بود، مردود اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96657" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDpUqeTBeuLDPZwMhjgO059FR3hEchi4ZlgJPf9E5tIrbC5K3QdQ6n3HwA8BwQBwNZ3YcycqIhn-5XVjjlLMTvA2fUiJSxxM9Zkc9zqCfGu4ZG1dXxq0QkClGWwJ6fn554g8nr6k6dFj4JipAGkqDTnunjIQqx-avFEm8EutaxdkKT7Wbd7VesCedP9F3vmSRes5epqCaEqWfjLNod0iDq2vzyKisRY9oeBoGJa-omGtLv_u9b7aBRBdcq9O_DV1nX296e6rfEJMhZfve8vZoQqpvYzWfQ0u3kXQ-gRJGT4Pzm_9F6uV38nlnA-zplOdkEOD46VrawkKDAf7s2X_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان والیبال ایران و کوبا با برتری شاگردان پیاتزا
🇮🇷
3 | 25 | 25 | 20 | 30
🇨🇺
1 | 22 | 21 | 25 | 28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96656" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjUn_7ZOprzf36HeOK9M7rhXi8pDVBO_SwRzHjYxyH_K9pHCYB6C4PxlaVKt0pd3BhjAC_vuqg6Ib5iVt5F4z5vlweFmoOO4lrk-W6Z6z9AVC351xXwdfyzT2_IBbetwf4OAo9tmnK3TBA779qgxgKX2aJy4Vau5tghwx23s4jP8kkz1U_OR21DGgQafMVFh-4dAMUv6X2TkKgzpLyeOszmAOlIOnAzY16BaxLkCZRsHR5r3VhFlEiezOM6ahakiFinX9IWit2Ql4xc8UR2l5ipPBN_vKNZS5iYCzYVTFyiwzo0pCoaqN3P7Jel_KirIenLgni0SHM33MJG9cb66AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سراسر حق محمد خاکپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/96655" target="_blank">📅 16:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNEM1RBZQtcPAcvBJf_YRVAMOrKCYjj_7X-7gHm7oWZZ9nr6wJQLyqrm0OzfEaQxbsMsqN5GZ4Z_u4tfz2-zQNH8OasOAYWSZnfh5Xxh2wKGIlWrF8uVwpW1W4Ethac5XtoF67KWpyX5e8zAOZQuf1T1pBqHlVzE5fj-nIgtcsgfuaJa6yDijG-O3Uhhgzh7dyyMmEPEagZbt0HA8fpfWM9N4MWHLniOqKtWcc2KL2hDCqvHFpCbTjhni93qnob2SvVJs1Jd-_8ppSGOZQqp_aHNYYuDKiSdOc2RR9r4y_zbmX8E4ybLiEYwAyUNEkph1Sorpy84cA79IhBPg5MTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
ارلینگ هالند [
🇳🇴
]:
🇫🇷
فرانسه خیلی خوش‌شانس است که امباپه را دارد، کاش او برای نروژ بازی می‌کرد، او خیلی سریع و خیلی قوی است، او بازیکن شگفت‌انگیزی است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/96654" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😂
صدف‌بیوتی و رفیقای‌شیرین عقلش وقتی صحنه آفساید شجاع خلیل‌زاده رو تحلیل میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/96653" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96652">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZxgULz0fmfE5dFU37i3WEYzsAtEl4phWgM7nz9XD-yFx0Zh4O-mlLuz0IBQMIMTWmv9tKe6v2lVuixOGZwcxI23A1bqSVpHJK_TKmPdTBQEwB5dVud7ipKKsomXl55RihmsmejIL-ONJE58PiavJzL0guJ1ctHGvN1xxhO_R37IxFtwcbHq5mAcbBBYqxVfXDDJhlxzWnH9XGS773-S-Fx68v3jS2kJTreoJWj_87HQUq-fTtKPYMOFX1MoJiKDNhuhruDbK7TKciZlVqQNaYM9FxsxdL2mom40dMj0EMGziI1-nv625XJ2m8cJUhjZ2o6DFQpXD-16iCqiwqqgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛
پست جدید اینفانتینو تو اینستاگرام:
تبریک مجدد به تو لیونل مسی؛ تو رکورد جدیدی شکستی و به اولین بازیکن تاریخ فوتبال تبدیل شدی که در هفت مسابقه متوالی در جام جهانی گلزنی کرده است. تو در دور گروهی عملکرد شگفت‌انگیزی داشتی و امیدوارم در دور حذفی هم بدرخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96652" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه مصدومیت وحشتناک والیبالیست تیم ملی کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96651" target="_blank">📅 16:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=Q_P_z_oYBAHVCVGiavSIljKXBoii3ytWYkyRfe9LUI8yjFxOpeRYuVLqJA7PMbqfd8iGuF_S8HooLWVj34CPTma_yd0JYupy7_za8i7BKdt_MVTf5nKYgNdCMt2NRP_75erxnN4JcazVQMZcN1QXXbUSU1cJ9bO-eph2r7I95V_jVrmfxwfk_-XOv3OR9XpxccT2RULUSrdRNtokCeGGjL4DIV573w_DOy-yfYgWfKdjxGniVWEL6iXI7JMveA9pwXyeYv-xuBJCVCtt5tDU5jh9jfVKMDb_DHgOm4XLvjb_OYez8rAoAY7bakrYfYaaqQ6BVo_prF9_M725mrhWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=Q_P_z_oYBAHVCVGiavSIljKXBoii3ytWYkyRfe9LUI8yjFxOpeRYuVLqJA7PMbqfd8iGuF_S8HooLWVj34CPTma_yd0JYupy7_za8i7BKdt_MVTf5nKYgNdCMt2NRP_75erxnN4JcazVQMZcN1QXXbUSU1cJ9bO-eph2r7I95V_jVrmfxwfk_-XOv3OR9XpxccT2RULUSrdRNtokCeGGjL4DIV573w_DOy-yfYgWfKdjxGniVWEL6iXI7JMveA9pwXyeYv-xuBJCVCtt5tDU5jh9jfVKMDb_DHgOm4XLvjb_OYez8rAoAY7bakrYfYaaqQ6BVo_prF9_M725mrhWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗽
تو مرحله گروهی که واقعا میزبان شایسته ای بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/96650" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyugHhA8mrExAySqd9MrK5R3ZZHTyTPFGsTpv6yc3JatgXv3DJhPUZOom0_dqIZJTaLCFr2e3D1pCla3xM1bmPB0N0SUbm1wMpN1xRLYCSGVqj7sgsiPRZOXZki_71caGKACaK0qcxTU259kU0IQ7f5ao8n5J26wHl2LEpSOc_vGUax2-J-MyT4t5b6oLiKtkfJ8ttzG0slU-r05_MMB8fyYLgnCpjsDC-57St7LhUIZVaOA0NMuqf6PaoPAGFuUGmV7wArOEfHUl8WELTC-GsVUBXgJIhafxUIYugYeWwPrHSPQpCZyztDHAqzNckGu9vtfYDSfNAdH3sewz3AOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله گروهی جام جهانی ۲۰۲۶ از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96649" target="_blank">📅 15:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz2mElp2ADggGRPx6--qMyD1ieuUE3snot5O979MSWrS6c337EvbxfyhEYEz_6wmVnXW_IbhCY1s0vRmPtCQnebyD_AIehJgdVcSFIMLEYukQ7b54v_MhF_7EtIbeXkCaU2NoOwfTjBDB5F_4RN6WTs2ve9TmjN764ZefBVHGBgxQFVHWOK0LYsyfksROCgw15fTiHNdstFpHfy9_hAQrb5-iMKBBXtTi15fEaEegvK69U1kcUW1FjbDOtUdlNuR3MrOVz3aEv2HbSJXv-_JGJ9g8L6kb3GKiIHmtk4mf4EfZFooBLDSYFgTJaocsk9UNW8l7pVKEGs09JgXRaEVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
رونالدو بعد از بازی با ازبکستان گفت "من برگشتم"، اما کلمبیا تو بازی دیشب بهش گفت: "به دنیای واقعی خوش اومدی!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96648" target="_blank">📅 15:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=r39zY33LAOSZbWEAXqlX_8-6itPI0uCxoXP0RArIoB-wm5XgKWKEKdvqZ0Im8IIX_mSEsJ6Kd54yfYrRKrM21iJPdvtxrUPcbW4Djam47gjN3PXe0JLk1EzZbPhC6s_dR3S6PiFqYmjto_8vbDvZrl0WjTELyDBbEGoJJQiNQoA74oSUxgGb_dYYW8rQcnshHUQeaIIZLNozV13Qf7bozwkupS6fJxSAwZjUamjJW1ZcF2mN7X-GX4rr-uletKLgRllCJpu4wnRrZ35t9wPZJC30s16_QV9W7v07GpB2Q0mkcDSrCyjbdlM5sJnLiWs27eidZ2d29RBAiXWtmrNjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=r39zY33LAOSZbWEAXqlX_8-6itPI0uCxoXP0RArIoB-wm5XgKWKEKdvqZ0Im8IIX_mSEsJ6Kd54yfYrRKrM21iJPdvtxrUPcbW4Djam47gjN3PXe0JLk1EzZbPhC6s_dR3S6PiFqYmjto_8vbDvZrl0WjTELyDBbEGoJJQiNQoA74oSUxgGb_dYYW8rQcnshHUQeaIIZLNozV13Qf7bozwkupS6fJxSAwZjUamjJW1ZcF2mN7X-GX4rr-uletKLgRllCJpu4wnRrZ35t9wPZJC30s16_QV9W7v07GpB2Q0mkcDSrCyjbdlM5sJnLiWs27eidZ2d29RBAiXWtmrNjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
خلاصه‌دیگر از بازی ایران و مصر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96647" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5op8HbmUgqLpOxM26qTejbt8t6u672sfRomfl58EzYioEQF48FIYWOGgB3XE8eX0AXll-nmHSPmbJH7FZJlf5zQfMYtb59Pk3RI5NLAj5XqNh6N_1aE5KGpxtY84jlry9u7LJTNPWpECUz_j-AdVYK37acTl84sfXSeezXbN3UtRECJkrJ2JhEE0OELPNlqGTklGdfO1_F1__CxvRNyijLfsnSRzjyzeCVgDkIJbrbJKljo59zP38PXPKaawSFbBOIilnazRGqSNeaB9a5G_Gfbz-GjZ5_xR-waQ7DlRPzVGnXMFwJKF7CobK_Y9UXDGmhoPps5yncLriwnQ3fstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر چند هوادار ولزی : ما اومدیم اینجا و به همسرامون گفتیم ولز صعود کرده به جام جهانی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96646" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSTypRZUQn6Oi1aPVTrFyMvK7n5Wln0ojCn5dxYh5b3Bde0mKtmWif2_gREoJ28rs50hEkOQC_hnoDH1sZt2IjzeRioB_1WMhucf-VnYJAaV7T08LWt7B6ZLg66Wzi34QLZzFu-raIPVWSJ8bbFTS-ND2dmWBY2_F5xMLuDwy9mNcI9rzLqIz6LYDqx60mXYxrJ_0wy-7jN1Lah8oCGzUfHsDlPcETJuQjMBI7NsynVNg_LRpo2Twa6HxrUq-z_q8p5OVWR9hL6J89HIi5uFOODbLtu6RXZnHZ2b0r2_YaKvtCIwALDVec-R7FKO1xv6dZAOp4ma8qGGrwWS3wb3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
مصریا بیخیال کون شجاع نمیشن.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96645" target="_blank">📅 15:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
🙂
علی‌نظر محمدی سرمربی شهرداری نوشهر رو مشاهده می‌کنید که درحال ماستمالی ریدمان تیمش تو لیگ‌یک هست. این برادر بزرگوار سابقه طولانی تو ریدن به تیم‌های شمالی کشور داره و داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96644" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=M-6SI7fbhJm3o49N7M3luXbLgbDg1QwhyyzWXGAOWieI4b-00T2iqaKBTkz665-GerTP77IoFZtOmLiLg-ybxHOdt-PQTjaBqlcxDxd1H_nNdNfSru0Lk6Cd4_XgeagdY6Qxcoe34_orplsg0er5GLtlwjBuE5wqpCO0xsu96nCm6mOq2G1EHjQgAgr3awqQ04ear44W25MRZ1j2yt0tRSTsYWKp8v6LaTIN6MmctOxIZUV_-8_2X8XU6pWUF_BzHERxhwpuk028cZOl8UIa4J-HxaxY-TIvk9-gfGgHvr3CAWgC0rja919xf-c9f6oukpeePvSdCimreRWfsHyj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=M-6SI7fbhJm3o49N7M3luXbLgbDg1QwhyyzWXGAOWieI4b-00T2iqaKBTkz665-GerTP77IoFZtOmLiLg-ybxHOdt-PQTjaBqlcxDxd1H_nNdNfSru0Lk6Cd4_XgeagdY6Qxcoe34_orplsg0er5GLtlwjBuE5wqpCO0xsu96nCm6mOq2G1EHjQgAgr3awqQ04ear44W25MRZ1j2yt0tRSTsYWKp8v6LaTIN6MmctOxIZUV_-8_2X8XU6pWUF_BzHERxhwpuk028cZOl8UIa4J-HxaxY-TIvk9-gfGgHvr3CAWgC0rja919xf-c9f6oukpeePvSdCimreRWfsHyj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
اسپید از شدت ریدمان دیشب رونالدو کلش کیری شد و وسط بازی از ورزشگاه رفت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96643" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDcGtL-RpJ2w8-iDEupZLnofOge608tkmemWa6AZt2cxYI3-TO0L1Q5KzYUr0IvwNWQ_nXvH03PwOnARWYjhnYsZ_sGpLmqO2Fkr0Ec2QYAfelJHqDO86eKhJNuiGA0JFh7_9n8ooZRVrDQKRan8fkYeAQ9KmIAF2ZHurh2d-BozYBoaxQqkUtf5nkn70nHLE8ZT6caLhT6QSwcyXgw3BG2C_g1h2hjlZ6pD18Wnr3vtfqQzT_LI-U1SVZZaqEkHXXw09R7Sqz_aXbJGDJppY76lJ1QZjEMBGSSrNGtV5OY-She7ZspK_zCZGr01jU-bZSJhSUXMQq6HZXbl5aKTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇺
🏐
🇮🇷
اعلام ترکیب والیبال ایران مقابل کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96642" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=fuO2kMgHlPum6r0grI8wyIG5f7waAdT1XDKqJBO3HyZ1_Rg0alvr3xN0B-msciPhxaeFI_24DYlmufBDyj6to9Nt2dE53uNl9IRHGT9j23tFYgvIMdRZIqR3hsh2dYaDZ2qYmcys7eDGBvJKXu6-VhP9M-3_HW3ayQzSSnNEoYAr_AgDBZ7YeKOndD31qZn-FW-UYyDNIjVTLUNNyR-FEFhDgN1PmIUlP3zQArFQxgChlQQZRx_fx_RzpIxfzGgLs5wMPiiGGmrjyf4QoBF3BfqFUO9rsblp0hXFYaiHRP8ByRlOkXurPhNiP3ga1TZTWuJXIWGGz1ZHxNmNTdWBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=fuO2kMgHlPum6r0grI8wyIG5f7waAdT1XDKqJBO3HyZ1_Rg0alvr3xN0B-msciPhxaeFI_24DYlmufBDyj6to9Nt2dE53uNl9IRHGT9j23tFYgvIMdRZIqR3hsh2dYaDZ2qYmcys7eDGBvJKXu6-VhP9M-3_HW3ayQzSSnNEoYAr_AgDBZ7YeKOndD31qZn-FW-UYyDNIjVTLUNNyR-FEFhDgN1PmIUlP3zQArFQxgChlQQZRx_fx_RzpIxfzGgLs5wMPiiGGmrjyf4QoBF3BfqFUO9rsblp0hXFYaiHRP8ByRlOkXurPhNiP3ga1TZTWuJXIWGGz1ZHxNmNTdWBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت ایرانی‌جماعت بعد ریدمان اردشیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96641" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBT7Y0xmmYsm3pDZ1uhh-AvVTN4RlT182yj3KwdnPa_2YNQ_q1lmKeLRgAIYa01oXm4BkUw42GcZOX2rWc7yfG6PIFwdzEQ81U6gyHFay3nWza20slpXa-41x-9KDJ9UVF3Jlbrspkq3BDPV-zjkJNAFnK82oApaiR70DQpwajgOlwOIyk9xp_K9pRx3r2hxA24C39yE1mQHvIaqA7o799fmGDZUt7q-ndv6BVywW7b0L4z9bA11gwLuL8GlW4SHT30Q4Eo4rL2WjC3ycruM9MmKan1CqmP8ejibRxh7a83wGVY31zBesKW-mkHH6ht_v1Z2jiWcvfZ62JtMZMDl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
فکتی پشم‌ریزون از هالند که نمی‌دونستید
👀
مهاجم تیم ملی نروژ و همسرش، ایزابل هاوگسنگ یوهانسن، در سال ۲۰۲۴ صاحب یک پسر شدند، اما تا امروز نه اسم فرزندشان را رسانه‌ای کرده‌اند و نه عکسی منتشر کرده‌اند که چهره‌اش مشخص باشد
🇳🇴
در دورانی که تقریبا همه لحظه‌های زندگی در شبکه‌های اجتماعی به اشتراک گذاشته می‌شود، هالند مسیر متفاوتی را انتخاب کرده؛ او زندگی خانوادگی‌اش را دور از حاشیه نگه داشته و از حریم خصوصی فرزندش محافظت می‌کند
❤️
👶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96640" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96639">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96639" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96638">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=SML688RwWXcA8uGX4BSq7tMYXjOy941fGlfSkePqmf4hWann_E7YCeVFGIXg0JOOd9D8mwXiGtYEp36YCASgYsfsiAyYrDVBRMQ77xiKLnYIOYSWOYhiD-d6Q1bx9IucV5rqKKfyvMTzOOh--K3jfppqE2hw4w2qB3bi2GiAwrae7MJRFrejj_KbexLin14kcpVC_54IsEOukE_SrPC1-HhTujN4O3Otk0eqqrdvOwhLw0RI1eIlXH9V4Hl2QB7G6aR9Km8JKcCn3Uew_sMvsRSNV7hOUtVqj7RQmXD50ytFKwvBTtynVl2dDdxrHx5a4aSo2X-SPRoYyQsNJbbqcrYXrQugDDCOSC-sAFxmdUGiJ7DnfZEzExCcRsU1_bVR7leq91hzZxYdKDDTZvMBLYQJtyKH8WDUfvt7z57pWNqTGSWX87Fb5vdm3CgzNWHlTNzABOHl_Rht6hp9rBQqrJ6z8al1Kh0PDKbcQePdDVk-ajggq4anBy_IM7ZQ6CuPl2xiAfWrIGtf1o7eV746sloeC8ufmoG7HoMYeb41MYlUQcq0E35uOcXJYN6LmFt49XHFzUfojt0VA19lIKTLbxloQcrp20lgp43YlScSFCyyEvVGlW0wc-bpKhpH5okE6fnH9fGFNaksx5-WhT8YYrMavB1nxM9gKVPwlof69Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=SML688RwWXcA8uGX4BSq7tMYXjOy941fGlfSkePqmf4hWann_E7YCeVFGIXg0JOOd9D8mwXiGtYEp36YCASgYsfsiAyYrDVBRMQ77xiKLnYIOYSWOYhiD-d6Q1bx9IucV5rqKKfyvMTzOOh--K3jfppqE2hw4w2qB3bi2GiAwrae7MJRFrejj_KbexLin14kcpVC_54IsEOukE_SrPC1-HhTujN4O3Otk0eqqrdvOwhLw0RI1eIlXH9V4Hl2QB7G6aR9Km8JKcCn3Uew_sMvsRSNV7hOUtVqj7RQmXD50ytFKwvBTtynVl2dDdxrHx5a4aSo2X-SPRoYyQsNJbbqcrYXrQugDDCOSC-sAFxmdUGiJ7DnfZEzExCcRsU1_bVR7leq91hzZxYdKDDTZvMBLYQJtyKH8WDUfvt7z57pWNqTGSWX87Fb5vdm3CgzNWHlTNzABOHl_Rht6hp9rBQqrJ6z8al1Kh0PDKbcQePdDVk-ajggq4anBy_IM7ZQ6CuPl2xiAfWrIGtf1o7eV746sloeC8ufmoG7HoMYeb41MYlUQcq0E35uOcXJYN6LmFt49XHFzUfojt0VA19lIKTLbxloQcrp20lgp43YlScSFCyyEvVGlW0wc-bpKhpH5okE6fnH9fGFNaksx5-WhT8YYrMavB1nxM9gKVPwlof69Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96638" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee3960474.mp4?token=Auww7mNtRWTMutZO3TnEw3x7CiQxiLX4GbD4XujYw1dgxLav4I9jfSG9eV0NoxpIdeJML3FnUjKiUQUrPTd1F_KreyuSE13FJdDTTTz0mXfCh9m8VOmG0UBiDQ3YcNQr9zUkp1a-BpXjuSQT3UA-kviaByK8RVCO3JUGyLNiyPS6A8DSgLHfbJkNDQ9KbJGGYcmDPk2MafrU74UVUGXK5-fofRQMF36XJKbzAdO2ywWBT5TrOmyX0U51e04KjsjxnBJoWmxMpUU080-6VYJRqE_ocNNQnWN5xGOo1GDtZ_boLic4Y3ezo3wsM5ig2QWgfijdocV-XlvizWW-jh5IqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee3960474.mp4?token=Auww7mNtRWTMutZO3TnEw3x7CiQxiLX4GbD4XujYw1dgxLav4I9jfSG9eV0NoxpIdeJML3FnUjKiUQUrPTd1F_KreyuSE13FJdDTTTz0mXfCh9m8VOmG0UBiDQ3YcNQr9zUkp1a-BpXjuSQT3UA-kviaByK8RVCO3JUGyLNiyPS6A8DSgLHfbJkNDQ9KbJGGYcmDPk2MafrU74UVUGXK5-fofRQMF36XJKbzAdO2ywWBT5TrOmyX0U51e04KjsjxnBJoWmxMpUU080-6VYJRqE_ocNNQnWN5xGOo1GDtZ_boLic4Y3ezo3wsM5ig2QWgfijdocV-XlvizWW-jh5IqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدادی که فیروز کریمی تو بازیگر شدن داره رو هیچوقت تو فوتبال نشون نداد
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/96637" target="_blank">📅 14:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9HsKmG_1rhsKqq4VImH2ym14dQLMSqgDZPPoVO44g9-lLO1E0yuhgFwByUKleNGr_ilwDWrufPqRKcJZO4yCF_3XwoxfvBiVvlvUlv_hV8bSsKGNvxzR3QEZd2vtE1pfPMwmSasAzLP0sCOB3Y0VwPkq3GBmhOJzp25eMqUOfViPM5_n7ET2d6AvOPBzDw0XEbne0Q2VdDPDIVJp_kYhm5RHsYmlEZ_cjX964FexzWoQZpNu4ZaCDr326qkZwTc-qWZpSqIAT3-WI7lOSgdkQ3-Q0HC7O_9lv9KrgJicDpGhCBBKwZyvMt7wOWjbjWFk1yUxXrS3YQx_peXCdDeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ze2QhLv4azyhQqvJowbHBQex3erAtj_H53xaTtRb9s-l2N5Pl0wEMT8SBzjgUCT5bUjmSaYVveR4wtZhY8V6oz47uyaui51BeVmbyKI4wKXPpPfPkT-Agn7S57xD3hMU3jSk0Gh9k2hKSCuyKoYUDjD0jP1aSqA_LM2TtNYsWZQ7WCXPPeRRvwXhksr3SxtnEeTkQwKuXFuGJZ5IKKYqxEwgKhOR4E2hlH2eSiDO9m5xhgksD6OgQ5NLVb8x_wj4EhrFWTfSoUS4nEnAPNYzBhj8Y3HkrSQpmjCTQQuuxXhQiN46Q4qfDh_LHR0qXksry8lwDec2bpKsJGFt_ZHNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjRz3kaa2a6fWmjnJfHvgGNtx3Pd4G_BuOB2gj-h7OlToAJYTpHPXWOi7mHCS9GDTcCglaHk16cRlj3q5VOkDqHIddruMJyikocTmI1dGSEKTmJqhrGNc7b0zcH2moXJHfd-2V0yRg-FRbHujyE2f9mnggl0XdjHAo6v11eU_OxpKwOMQ1S2iscSC3ILkjUIV-ud2u4tkVUjKjaqA2UtcpwDSJdy2tShmh-PCkz73xUUvCAa-Lp1TdHzXU560QP-5nGIaI4HV_KDQbkQH7-FgjnuLtrV2s3XcCk_0xPVYJSmqE8QzrCnjXjp0nBw3IAqtXB4YeVOJetimaiZD1o1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-Dv3PiUEpsj28z6TIYNaQI_dvUhuMtUhqCfPR_O2nh_B931Iq8K5bgXaX_CInN4L4s208DUpWEDPVm_5q4OmHjQtigbNudJAF1j5o_qZPOCn3I-h4XcZUEM3rRdrdgGd-1gnvaqwnPK4XMNTntb88s9QMto8VnOt9-IRKqBYmQ5vmm_tjjt4pMi5cF8S7kVDzcQh2r8TacpaJnCb0yLq0z-FnUcOcoweMOIqmqA0m9_oPU0EYPjobo9hPeKv0k9UQ1VFZT_UJWDkmQaaByzYdYwayU-3I-QvHITcwaSR2K1vfplJA8WFRIWqyzmYwF7YaPTlKbUOTWJXqdox4GJEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس بگو چرا کلمبیا صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96633" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6330122b85.mp4?token=htXHH1w3af_HIpV4m5NzcBB3QmRKQDW2EWelYy0iGqzwWq7GQCRNFYbvnOieL_F3c8UWx_lzfOsL1d9o8J7QPNLktyhdQli2zM2uUK0XP908sEhaWxsMVf3qCrDj6RRBvMl1j20okyBkwwHMBkU6ippTIWl9M00Cla1Q0LoqmpHwLB_hsKgFS0KZ3di0kTEdV1cwe52XSQ0y5EGH7anzCN0qBGnH-pp4bS2JjoY-tOnwZtFWbvhBjOU6TGJMbbNbIJXaj7qhYakRN_3dD2QnMnU-62UG1M0a8_NHODk6ZeJp50lTF4jkiDRZnagXCHDlxLNIt9271RgAWPbL3r2JHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6330122b85.mp4?token=htXHH1w3af_HIpV4m5NzcBB3QmRKQDW2EWelYy0iGqzwWq7GQCRNFYbvnOieL_F3c8UWx_lzfOsL1d9o8J7QPNLktyhdQli2zM2uUK0XP908sEhaWxsMVf3qCrDj6RRBvMl1j20okyBkwwHMBkU6ippTIWl9M00Cla1Q0LoqmpHwLB_hsKgFS0KZ3di0kTEdV1cwe52XSQ0y5EGH7anzCN0qBGnH-pp4bS2JjoY-tOnwZtFWbvhBjOU6TGJMbbNbIJXaj7qhYakRN_3dD2QnMnU-62UG1M0a8_NHODk6ZeJp50lTF4jkiDRZnagXCHDlxLNIt9271RgAWPbL3r2JHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
وقتی کله‌سحر تو ایران فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96632" target="_blank">📅 14:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=tuROnA5EqTILrA10Cboj1JxfxfXQEeFrvHY70ky6XYcyHFMjNK96rJglio4hblwxUacl35GOvj_bnSj1h852DWspyoF01IQsglvyItnDA1Vi8Lnijn7n1BLSvBMkrifdoZCxWG5LCvl1Iu8a28BVucmbnVs_OqLEy88lTAy7eulb-z_-VReWGyn2EUsHUf4QBe08JpJzwtax8a9i3lv4Kehb4NHGYBiss5M0lF6P6_VAJMY2fHOelUK2MMygnQ5jyUvy_BY52ew0I8fMLIhj9lURaZG3E6xZdNc8CN432GtXTIClLnY8EF9T7dx65TalOA63Wn73eNxV1j6Kb1LJxkf8SCdoxIK50KjFApUkT4IDa82iz615DkYr97svvXGh-SBXBPMh6026QLObpUkFxw6XMIN36UIB86s0pwTSANifwMaEaZWfJ2mSOU63LRgHNAetldh5EtHQz4WjfNDHLvsoQD0eP2RxVELsRuvC32s6_QZCHxj6Y52uKMoQ3cdhCaFJvcj72F29PxmyGxX5fkVEDlxlgSi3vRosPBxbjE418b5oYDyoox3tsJUJQsEHWOJwuZjHZHTTq2ZodaW1d_vMRM2-d_m7KfpVZPEEm06OWqHdTJNW2XZuFBo6eOjG3g704TnCEIA4om-g2S6_54F9u2BaF_AwgF2DOaldsG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=tuROnA5EqTILrA10Cboj1JxfxfXQEeFrvHY70ky6XYcyHFMjNK96rJglio4hblwxUacl35GOvj_bnSj1h852DWspyoF01IQsglvyItnDA1Vi8Lnijn7n1BLSvBMkrifdoZCxWG5LCvl1Iu8a28BVucmbnVs_OqLEy88lTAy7eulb-z_-VReWGyn2EUsHUf4QBe08JpJzwtax8a9i3lv4Kehb4NHGYBiss5M0lF6P6_VAJMY2fHOelUK2MMygnQ5jyUvy_BY52ew0I8fMLIhj9lURaZG3E6xZdNc8CN432GtXTIClLnY8EF9T7dx65TalOA63Wn73eNxV1j6Kb1LJxkf8SCdoxIK50KjFApUkT4IDa82iz615DkYr97svvXGh-SBXBPMh6026QLObpUkFxw6XMIN36UIB86s0pwTSANifwMaEaZWfJ2mSOU63LRgHNAetldh5EtHQz4WjfNDHLvsoQD0eP2RxVELsRuvC32s6_QZCHxj6Y52uKMoQ3cdhCaFJvcj72F29PxmyGxX5fkVEDlxlgSi3vRosPBxbjE418b5oYDyoox3tsJUJQsEHWOJwuZjHZHTTq2ZodaW1d_vMRM2-d_m7KfpVZPEEm06OWqHdTJNW2XZuFBo6eOjG3g704TnCEIA4om-g2S6_54F9u2BaF_AwgF2DOaldsG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
کنایه‌شدید مجتبی پوربخش مجری ورزشی اسبق صداوسیما به افزایش قیمت‌نان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96631" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqXjj4XWuLOmTJfJzOxjmy7YF1LFqg5LnmuZ7ZQTNOTrxKZg50XyZ1QMZNayIfLuZhZqNgodRSgX63Fn7FjYhGkOtcxSqp6z78FnSiLs6kcskyDgpF1g4n8sNXFCYiC3rGYkwWKvCySGdDETKPb5vyB0LgtmJlHse7-0Nuk1wDSmR4ynJ__liSz-587WwuTdjdILhTx1oknfHbIMLWv9jB3MMwD8UyqIiwOM62TGoQIWA_NaoOiJ8j7OBNzza7qIG9UZr08KxYseoaWhOXCAc9ELI9pDc1QKhFpBQVz1UJ0wKwVjSm5JT3PJ9QUgdxmoomfkt1xdF0bt-l5YH4XSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین گل‌های ثبت شده از ضربات آزاد مستقیم در تاریخ:
۷۸ گل —
🇧🇷
مارسِلینیو کاریوکا
۷۴ گل —
🇧🇷
روبرتو دینامیت
۷۲ گل —
🇦🇷
لیونل مسی
🆕
۷۲ گل —
🇧🇷
جونینیو بیرنامبوکانو
۶۸ گل —
🇧🇷
مارکوس آسونسائو
۶۷ گل —
🇷🇸
سینیشا میهایلوویچ
۶۴ گل —
🇵🇹
کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96630" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OiICshdZt2XNkTAAGiWINqPQxSXX0-V-2Kt83m4Rf9E1RcIQysfvw8jbliE23e8bKcloYv569kK-Nfm_o39V_lTGhjTmdPC7CifjI7KmxJEI7-_ty6CUwiMEKusrRtm76yisA3XARagjUhZD21Fnk9BKiguPUpsAyppyaFh2WmHSG95OgJf-cNtRS0F5yUQD5Sio8Y5xGtuUxxn4u-ArmCepU7EiU7a1wmuLQCe-xy8CivQZERafdXwyx3GAKbcids6k3skzC4FBU3u70ldDqc8NYHJ_aYh1OW4Ld-6z2DzzvFlL9-gIZrBs4IB9Ne1R6_rK5hZDac_ND-GXGzOG5ieZt4i_u8JfTMoooq_E154aW7AJFXEaJqXphkpluJ9QeNiN2c9oaWXCr32WDCRZQhsUXi-U_abwFQ7FfxmtjZr6WT9k2PPcYiZFtZcLTIl3B0FuYSO3lVF_Emc0PDH0RbHO8ibb5swCcYAp4ypP0OIodDl9igdTCH12NRMQBtWrBRK4AD27mM3xszB5uuwyxrhVk9cZ0sE1Hr1FWhghX-HDSPdxa0ER3Lfn3E7OwpfztyXn1BBFciX-RNKbxn3CaeA38rGhUJRvKPrKsI88PA8O1FPhYOixeqUceJPuFkIPAb8wMhqX5LLuVjWc-eNkwx0JfdFcxIHgtdNkuczkOVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OiICshdZt2XNkTAAGiWINqPQxSXX0-V-2Kt83m4Rf9E1RcIQysfvw8jbliE23e8bKcloYv569kK-Nfm_o39V_lTGhjTmdPC7CifjI7KmxJEI7-_ty6CUwiMEKusrRtm76yisA3XARagjUhZD21Fnk9BKiguPUpsAyppyaFh2WmHSG95OgJf-cNtRS0F5yUQD5Sio8Y5xGtuUxxn4u-ArmCepU7EiU7a1wmuLQCe-xy8CivQZERafdXwyx3GAKbcids6k3skzC4FBU3u70ldDqc8NYHJ_aYh1OW4Ld-6z2DzzvFlL9-gIZrBs4IB9Ne1R6_rK5hZDac_ND-GXGzOG5ieZt4i_u8JfTMoooq_E154aW7AJFXEaJqXphkpluJ9QeNiN2c9oaWXCr32WDCRZQhsUXi-U_abwFQ7FfxmtjZr6WT9k2PPcYiZFtZcLTIl3B0FuYSO3lVF_Emc0PDH0RbHO8ibb5swCcYAp4ypP0OIodDl9igdTCH12NRMQBtWrBRK4AD27mM3xszB5uuwyxrhVk9cZ0sE1Hr1FWhghX-HDSPdxa0ER3Lfn3E7OwpfztyXn1BBFciX-RNKbxn3CaeA38rGhUJRvKPrKsI88PA8O1FPhYOixeqUceJPuFkIPAb8wMhqX5LLuVjWc-eNkwx0JfdFcxIHgtdNkuczkOVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشین قطبی: کارما در زندگی‌وجود دارد
یک دایره ای در زندگی است و هر اتفاقاتی که رخ می دهد بخاطر تصمیم های قبلی در زندگی خودمان است و سرنوشتمان به دست خودمان است. گاهی فردا بیشتر به خودمان فکر می کنیم شاید پنالتی طارمی میتوانست باعث جشن صعود شود و حیف که این بازی را نبردیم.⁩⁩
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96629" target="_blank">📅 13:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=o3arIwVmZ0cu8ioifalwtVhsekcG908E26qEYF5HoSaHOJGQNMsQVrYCi4xe5ZKMu1DNEN8FecxY8ILYh8z-p7G-BtXgFrYqYN6o96tesNV1pxoVNIrapBcoWqQuZmPm33Ti3E94KS8f-JFGTcFmf07wkqyudORUjGaWT8Ukjb3l87cZtlKXoOhr-1AyDj9Gh6iLOAp2A8fKsvx2cvymOrRrQgl6Qdk6ELwHIledQrga44pvsnDrF6PM2_vCDGkycBtcWGEWMaY0Yrq63FHMXFn0hL_nQSLZ0sw7_jrQy9K4jfEJLWYP0Zz1aTEiQY_vPSgBUVID2AgHScesz0S1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=o3arIwVmZ0cu8ioifalwtVhsekcG908E26qEYF5HoSaHOJGQNMsQVrYCi4xe5ZKMu1DNEN8FecxY8ILYh8z-p7G-BtXgFrYqYN6o96tesNV1pxoVNIrapBcoWqQuZmPm33Ti3E94KS8f-JFGTcFmf07wkqyudORUjGaWT8Ukjb3l87cZtlKXoOhr-1AyDj9Gh6iLOAp2A8fKsvx2cvymOrRrQgl6Qdk6ELwHIledQrga44pvsnDrF6PM2_vCDGkycBtcWGEWMaY0Yrq63FHMXFn0hL_nQSLZ0sw7_jrQy9K4jfEJLWYP0Zz1aTEiQY_vPSgBUVID2AgHScesz0S1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇪🇬
مصری‌های جذاب بعد از تساوی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96628" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=WUqQJizoqmiKZ-JFh9XWr3WHcLq-_JxMko_nvzXELDIhNfxS2yEwJbH9BG_w3rTLJm5jqkijlYmeeK5smyZmDqER89V5br_NNhereLYYBJzn8gEBuC2IeKAJVWqm1k72-Iop1IhqH9rw-3QUp6BMjBmR0Uc6JEmiNL0NyGYZWWy6lm6aZmQR6KiLXdM7nS4rI07gfvZRcROBrG1U2fpNSviKnBMG4YnHa8YvjkvKYeJwKJxjk1XgepP6bdyeeFnbPPuRy6TxejknSxZn6WKIapA1XTnanexxJwICGctGypGL690MZcxFHgc3OmaZwJJ0m9ah9jeX7RL01Cf_I8nsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=WUqQJizoqmiKZ-JFh9XWr3WHcLq-_JxMko_nvzXELDIhNfxS2yEwJbH9BG_w3rTLJm5jqkijlYmeeK5smyZmDqER89V5br_NNhereLYYBJzn8gEBuC2IeKAJVWqm1k72-Iop1IhqH9rw-3QUp6BMjBmR0Uc6JEmiNL0NyGYZWWy6lm6aZmQR6KiLXdM7nS4rI07gfvZRcROBrG1U2fpNSviKnBMG4YnHa8YvjkvKYeJwKJxjk1XgepP6bdyeeFnbPPuRy6TxejknSxZn6WKIapA1XTnanexxJwICGctGypGL690MZcxFHgc3OmaZwJJ0m9ah9jeX7RL01Cf_I8nsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
حمله شدید وحید قلیچ به بازیکنان پرسپولیس بعد از تساوی شکست مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96627" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG0B4zBeAf4-lDuqcoBxdA5USpjg-Y0s6nzc6N2jkPh5rdI6yf6QGVCmLiyNGCsenzjCzBG-rSMYGYzDzbFdvhtS0A3iY7J1bxljff3MrwKPHg7gmHek5KZIxB_nDMUQuE_yl7kpm8Y4zu1wBXwexJKYjefy7VLfOrhIRJeIVAFu65bFqGxVlKny4bO3ijKHu9sa-N7yX6G7UREptNhdB3zbt8wmbpnZ8QCn6cs-SvWgIem9K5UrNz3d5kgu7IM_wRMbAV9djiBtG_p_7OisLHfkUP7FIUZlzUKdfDXcmjCGCNmLsBbR3YdBO0eOcaN151xr7GZVhMLQJyVhvzz0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ابرکامپیوتر اوپتا:
فرانسه قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96626" target="_blank">📅 12:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOkNFDyI23tsKOtL_CEp1LSZgTYngLm7_QWQ7vdNGCf1X804KMospHiO07hC3ZvgEscLRaaEhnRYxWf1OITz5ODL5f8bk7Zc8mV5bgcSPeBaVA5d-uJQLS1z6llkvfVxZ12ajRvb3VGLmSAIQJio0vh3PNXczU8Lnil46L0Yh7P2eW82W7fV6P3VRcMZOgYrKJVTWVvjHz6fW-tBljn_Pwby7VKJRd2yjVyHGyqjpglYUuGZpXMnakPKgPpH_Sbxj3tzozKfgAXXqAcVTkCHzLeZNEaKDUgcXCP8vqqRGQy3ekN0yXMnlnL4PddGX3FP-05fwl2pMOAzcvUBxzhPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇦🇷
🇦🇷
مسی در مسابقات جام جهانی:
‏تا سن ۳۴ سالگی:
‏
۱۹ بازی
🏟️
‏۶ گل
⚽️
‏بعد از سن ۳۵ سالگی:
‏
۱۰ بازی
🏟️
‏۱۳ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/96625" target="_blank">📅 12:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgL7n6ntWZyj3x-NftFkL3lxqv-umeBizWIJ6xFsAiCvO8r1krkZ3EuP0VtZpjFvrzWFi0eYAo2urZcJ9h4EoJBzBMkzadWQ2U_7TA8nrDdcxac0MaO8laWhMKGHJjYJ8hZlru1oY96xSjncuCIhx3rTxirxXJ0iWZd79tFE3clEA-Nfzza6rNj4yO1lxkS7wBFjL7QQJClh5m85_khwBOQEL1PLtwDyQlOHvrHVHL2DXhCdofepADG3CBxWFv1acyji53Vj1jNGR6JfL11MV9DPftQZ7k6vYUPo3qNr6bTlF10slpVFbHejm7JmqCr-cbcZ4juh6RuxtC98sPxqDpDM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgL7n6ntWZyj3x-NftFkL3lxqv-umeBizWIJ6xFsAiCvO8r1krkZ3EuP0VtZpjFvrzWFi0eYAo2urZcJ9h4EoJBzBMkzadWQ2U_7TA8nrDdcxac0MaO8laWhMKGHJjYJ8hZlru1oY96xSjncuCIhx3rTxirxXJ0iWZd79tFE3clEA-Nfzza6rNj4yO1lxkS7wBFjL7QQJClh5m85_khwBOQEL1PLtwDyQlOHvrHVHL2DXhCdofepADG3CBxWFv1acyji53Vj1jNGR6JfL11MV9DPftQZ7k6vYUPo3qNr6bTlF10slpVFbHejm7JmqCr-cbcZ4juh6RuxtC98sPxqDpDM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
جلو جلو ذوق‌کنی کیرررر میشی(قسمت ۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96624" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=eegKGWN93YvRfDCXPoWpyAz7ld99Bjf7RfT-lAbqoqFEcsIwlGDiaa0YPHCKn6-e1HThCVL-jhpPZlEk-t477cazyl1mC6pDJs1Ly0JzSx9EbvPNDgji93AJJPJludRffNtzviJvnDdSh3jNphKtI3rjPM05zW693f_u8oWFUEcJAEtTO6gmBpStLTFHZcgZEEObJ73wOE9VWW59OS4tw-_cYDc4LxLLIq70nHszYMdbQFH9tEK5W58-IIuO5Zmw44K23lyaEbl5dxlFhQPYidCQGJTydD8DDjnY0Dty7Cplh8ME4uwzZr3BIOyeNH6t1DYa5skMMLHccE-OAGH9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=eegKGWN93YvRfDCXPoWpyAz7ld99Bjf7RfT-lAbqoqFEcsIwlGDiaa0YPHCKn6-e1HThCVL-jhpPZlEk-t477cazyl1mC6pDJs1Ly0JzSx9EbvPNDgji93AJJPJludRffNtzviJvnDdSh3jNphKtI3rjPM05zW693f_u8oWFUEcJAEtTO6gmBpStLTFHZcgZEEObJ73wOE9VWW59OS4tw-_cYDc4LxLLIq70nHszYMdbQFH9tEK5W58-IIuO5Zmw44K23lyaEbl5dxlFhQPYidCQGJTydD8DDjnY0Dty7Cplh8ME4uwzZr3BIOyeNH6t1DYa5skMMLHccE-OAGH9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
ایران رکورددار گل مردود در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/96623" target="_blank">📅 12:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDhgEEkKFYcHZ1eu4BHlSrJejqQvo375xSo7ctMKX7RZK5J098n0x-a8BhYYo2s1m7p_Ju6ZAfDicWt2ao4aZgyHTWlJGCjBsB_yUnoEUBz8F6aueuS6WqwdGbYsNgA5Ya6YV43PMkUvEFKPwtHYQG2LZz8v_CkgyIM2wIsAUobsZpHIQyBif9g5T-rbZ8M5WYyoV5c3A1-xukYhDQQod6QYDXwep8Vtl43wrXIm0T7jjLlgEn3-ykzx038MpovELkA13SVeELhUP03ruEZrtAppFA7-9PsKKixnIU-Vw_f-2yb2FRol55aIsbJnHDjOsQMxkkvn2QRsz-AAnHHAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری:
قبلاً گفتم، مسی رکوردها را دنبال نمی کند، رکوردها او را تعقیب می کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/96622" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz2eJ-jzogpO8Mm2CXVWSB4LzbDxsuIXtG7WekD4khNUedYfupw23f0sQrIeE3Wo7pxvl90f9NvSdNyKg01v7pJXV7NJpLeviLvGv0OTF8meDqU7TgyxRwEJnvQ2g-WIIMP8EiEiW3GzjnvBkJEq-MtHJ8nTQEe4iznXI7kXQkDGusXQDzfpS1JDR9AnqS7GZF3PTGfiaNpS6VTEsNBSaF-jB0IcsQl_4q2JcohP3uYVta-Ew-OCNe9KIMFVEKfV3ZQl1N_WnivDBRthxgXs7sQ_lAfTZOpJWmmCSxhR2Qc73cs0bTHIu4_WeS8bwcCoJvWRKlqX6-cMdnBV2eSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
مسیر تیم ملی پرتغال در جام جهانی ۲۰۲۶.
• مرحله یک‌شانزدهم: کرواسی
🇭🇷
.
• مرحله ⅛: اسپانیا
🇪🇸
یا اتریش
🇦🇹
.
• یک‌چهارم نهایی: بلژیک
🇧🇪
یا آمریکا
🇺🇸
یا سنگال
🇸🇳
.
• نیمه نهایی: فرانسه
🇫🇷
یا آلمان
🇩🇪
یا هلند
🇳🇱
یا مراکش
🇲🇦
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96621" target="_blank">📅 11:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0tbXsu-5VZxiJG-3Na9TD8ovKtr681MBpQLu3F2F7NBF8N4VuLEwXBTfbKglJ8nF1rWLAQpAq9WcRUwCIWqjwiYXPijQYwGYCRgfJZU2x2QN8oE9ys5fS_YWHp2e7ZjBbAPHJ6kcUOUGrywQsNgMFb51J4DKEJZuEtWoZoqMGxcdQS4OgMYkKv-p7MhPRSAws-lopIlIzfwtbTkAGY0XEt33ZM8U2KCmp_-1IUo3s0dIspKIXVrmiLX5M96zMjGPWI1Yawow89hBdwg-UVM2MZeNhvqtP-p9GLC2pdmTNCZkWayIYI68lC1FiFor7-H9NBsufJg_ktB_QTlYYvpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
ترامپ: مسی دیدنی است. او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/96620" target="_blank">📅 11:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957600e824.mp4?token=IU2K0t8vL4Z76Srk74QzPxteGWTy0grCK6JRu81hjlNrpozNB_ove65TH9Jl7Wzwlp3K9kdHmKJsZ5zsy-v56WDbGaDEydFqwL6yUy2D16QgpLu04nsEyBqBacsjnUkX7NHYAhQOnT4qeB5ZPybKW0G-n4K3jlFxYxWCVEIPphRKYsr9bePZrWtX9vvHWXqt9BGpNiJxKYH0D3ssNRdoAVz5hl_0x8a1X2tQcvzbMyWQBBk8mees6VgEIeuN-2rHU2cSDRPYcmZZp_mCys504dUQJ3jfMvU5nbk8YsNwq_XC6exuAlk3Cvfc8lMAhr3crVVYQoODRJKYRJ1TeuKBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957600e824.mp4?token=IU2K0t8vL4Z76Srk74QzPxteGWTy0grCK6JRu81hjlNrpozNB_ove65TH9Jl7Wzwlp3K9kdHmKJsZ5zsy-v56WDbGaDEydFqwL6yUy2D16QgpLu04nsEyBqBacsjnUkX7NHYAhQOnT4qeB5ZPybKW0G-n4K3jlFxYxWCVEIPphRKYsr9bePZrWtX9vvHWXqt9BGpNiJxKYH0D3ssNRdoAVz5hl_0x8a1X2tQcvzbMyWQBBk8mees6VgEIeuN-2rHU2cSDRPYcmZZp_mCys504dUQJ3jfMvU5nbk8YsNwq_XC6exuAlk3Cvfc8lMAhr3crVVYQoODRJKYRJ1TeuKBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مصاحبه چندماه پیش استاد مهدی‌طارمی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96619" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
