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
<img src="https://cdn5.telesco.pe/file/uy0pCmQWRcQAFmCkJzS_9MQyl9edPLLnk2gDfpjAW6YUQc1tXX_7z-J6tV8DNxB8ghogv8YowAMGCLJOehYVmVhTwjyOS8xZ8HBd4fA0_eBblHYUrli2Lqnz4EsItRKvRPz9A2jOkcE7LcjK7EkaX1P0rQGsIN5ACh7uIYSvRBawlEqQa8pHn8GDp5luzKlbjiDGIeVLC5oEMitpOfJoj9WFyalq4_e23gYTIUR6e9_Ez9dRqm6GtxNXSmGWpBsvuE7VVif-rci4Qxyn5vc5H8Att5GF2O9iNeBcvFlST4MgHH8dWQRHZlAtKQOVU5MsUOAJ5O9h0in9NyTJRGPi_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 445K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 03:13:02</div>
<hr>

<div class="tg-post" id="msg-104618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431f50241e.mp4?token=gYz-SKpzH1DqxW4u0H6ax07UJ38wiAIUW7zSizkTtgTAPwjiRyZ2MxcBcuRMhabe5MesWSNg9LWI7Z0Q97t3oLV6CmvlIK0s0ecdNuocUqp_ZJgHj6tTEmVJichj4D9S1VtpODI6fHIKjMZ4kHtfd1OetRx6_LRDLUgFu1qMmRwYONSS85a68j7AynOYvbS4rF8sxBor-B7Ro4nhg81rhPqmrrVWvUxY8ZhhKkTUEMkTR-WbFOtbbDU5Hc1u3STx6s5uhXMo-weOECq-5va8p6Ln0Bwmmo1NjXkfTxFy3TfxaGwqN96LmUaiMWdbhc6VBfWPDGZyfqwhmI4BUqYRiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431f50241e.mp4?token=gYz-SKpzH1DqxW4u0H6ax07UJ38wiAIUW7zSizkTtgTAPwjiRyZ2MxcBcuRMhabe5MesWSNg9LWI7Z0Q97t3oLV6CmvlIK0s0ecdNuocUqp_ZJgHj6tTEmVJichj4D9S1VtpODI6fHIKjMZ4kHtfd1OetRx6_LRDLUgFu1qMmRwYONSS85a68j7AynOYvbS4rF8sxBor-B7Ro4nhg81rhPqmrrVWvUxY8ZhhKkTUEMkTR-WbFOtbbDU5Hc1u3STx6s5uhXMo-weOECq-5va8p6Ln0Bwmmo1NjXkfTxFy3TfxaGwqN96LmUaiMWdbhc6VBfWPDGZyfqwhmI4BUqYRiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
آهنگ‌ خاطره‌انگیز جناب سندی به نام "حلیمه" که این‌روزها مجددا بین مردم جنوب کشور حسابی وایرال شده. به امید سرافرازی میهن بزرگ ایران و ریشه‌کن شدن تمامی ظالمان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/104618" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=VJFKl82nGfVqbOgiaxDmlmEujGb34XTeQY6OIf9gbvEdzSU_ZKnrFpjxwLtyhNvacBt0Y9yneVjPcDmAQLkCnhhGK_MPrNuqPCchx590HEIRFkOVXa8nGWvyr8WoSGfEd6LktiJy9E-49z2xBd1qViKlW6PAQ_dwEEnEuMugP7EJB9PGZB_XJer50shdPErOy-uJRMLUu3-SBSau6AStkaLhofN__FcD813dX_CxDhWitWWm76XhTQkz17AvWuO6M_3_kBz8q-Z--atSmjOohhSyO1d8wIL8x30i_sK0033SsOy2zwqSdQT7rYzPc761anJUfd812ZybhWx0IINkpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=VJFKl82nGfVqbOgiaxDmlmEujGb34XTeQY6OIf9gbvEdzSU_ZKnrFpjxwLtyhNvacBt0Y9yneVjPcDmAQLkCnhhGK_MPrNuqPCchx590HEIRFkOVXa8nGWvyr8WoSGfEd6LktiJy9E-49z2xBd1qViKlW6PAQ_dwEEnEuMugP7EJB9PGZB_XJer50shdPErOy-uJRMLUu3-SBSau6AStkaLhofN__FcD813dX_CxDhWitWWm76XhTQkz17AvWuO6M_3_kBz8q-Z--atSmjOohhSyO1d8wIL8x30i_sK0033SsOy2zwqSdQT7rYzPc761anJUfd812ZybhWx0IINkpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سخنگوی سازمان‌لیگ: بحث قهرمانی فصل‌گذشته استقلال هنوز مطرح نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/104617" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=hW-nD3LRgx3skabaslsFPVf-aPfQAnaNPefR-TfJM8JkVGLStJcIrMEb0q5yl0WsG-NOEQ2lqizuiqTzxcD1CBtACOGkcQhpizGw-NMGEQY9nGqZj0NdNkkbSP7Lx23kBuR-LfTZr_VI66McSbECDWLHKXMMY20_2rsgp8QXZelxB4W_ZSz0bVjm9DCp_omsia5aC4OUp93Ff6A-S0mraokUAdSo2XfExwrN-bWw5oO8HtqN0yoOgLskvS2CyNdJGl9uWf_41PCUkmIZHuQzhAdx-2Lag_hKYw_ScnjafayZDlIQb9xjBqV0ZzQbZVwoHbvcViLnt-rtBMtY48NeVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=hW-nD3LRgx3skabaslsFPVf-aPfQAnaNPefR-TfJM8JkVGLStJcIrMEb0q5yl0WsG-NOEQ2lqizuiqTzxcD1CBtACOGkcQhpizGw-NMGEQY9nGqZj0NdNkkbSP7Lx23kBuR-LfTZr_VI66McSbECDWLHKXMMY20_2rsgp8QXZelxB4W_ZSz0bVjm9DCp_omsia5aC4OUp93Ff6A-S0mraokUAdSo2XfExwrN-bWw5oO8HtqN0yoOgLskvS2CyNdJGl9uWf_41PCUkmIZHuQzhAdx-2Lag_hKYw_ScnjafayZDlIQb9xjBqV0ZzQbZVwoHbvcViLnt-rtBMtY48NeVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از حواشی بازی استقلال و سپاهان که حسینی حاضر به خوش‌وبش با روزبه‌چشمی نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104616" target="_blank">📅 00:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGCO1S6wOPev_MbUuzbO3nNFGG-6mATYWGlpotuDxpwjAahHU6XlKXZfNdCh7jGdyvUf7Rtg8-GI_IsVyJTxbCShyLZEzchpdnCWXDwo7Me-UViqkW9MGXQfN2w2BymZnZYy-VCeTvd2qw_X2yds4S7FH7p2UFBNvTTqsSiGmPF3EeZyAJEy7uyHlTvXxtUfPSxNF4QQ74LuqdRS6Zqtb5mHxAwsO4gfhhsEws4Ig8w8XzC8UKbU7rRQ2bcrrlGGoybFbsa9BHPYKOGoLPPpZqGSBL7FPyRNTCJyIksxaTT0rQQPEUg_VHI3odLWcx_u_B0T77fkJKinEmWOFS4O8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌اول لیگ‌برتر فوتبال انگلیس؛ غرش شیرهای لندن در خارج از خانه؛ جدال سرمربیان فصل‌گذشته رئال‌مادرید به سود ژابی‌آلونسو خاتمه یافت
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😆
-
😀
فولام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104615" target="_blank">📅 00:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104614" target="_blank">📅 00:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6g4kaL_V63ws93BbdWTiYDXaaxNI8zZy3x6UwKAb7BR0N-86NrPFxLdhogFwtgztnMjUpVhyrbe1Q4vL-_EwBZXQd2rGds3LExuiMZ-9AQJ93KRcI57XUDMIbaEtHNFUfUrnAjkM73i-ltY5sNOVqp9iKTZ7SybnOXJJrcTMPBcBmhwc747ZbfBBH6YYpJhcXszFMq4KJA3TP42CS9nfK-5XPF3i6TwZQ-vwuTCL8zIj64CsNRA4L9aQgNslAQCwp4BRdB6no_eKRZt4Jf2IeCyb3e7GRBbGQN1ixrKcVcvoDUcR7aK8zAx_l60Ygy25A2bT_3i_K5lVIRU8LAxuenE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6g4kaL_V63ws93BbdWTiYDXaaxNI8zZy3x6UwKAb7BR0N-86NrPFxLdhogFwtgztnMjUpVhyrbe1Q4vL-_EwBZXQd2rGds3LExuiMZ-9AQJ93KRcI57XUDMIbaEtHNFUfUrnAjkM73i-ltY5sNOVqp9iKTZ7SybnOXJJrcTMPBcBmhwc747ZbfBBH6YYpJhcXszFMq4KJA3TP42CS9nfK-5XPF3i6TwZQ-vwuTCL8zIj64CsNRA4L9aQgNslAQCwp4BRdB6no_eKRZt4Jf2IeCyb3e7GRBbGQN1ixrKcVcvoDUcR7aK8zAx_l60Ygy25A2bT_3i_K5lVIRU8LAxuenE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104613" target="_blank">📅 00:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Khu8sixfh78AghYvbbHl52jXW6mvkmyJwLvCpxIl1pRkgB7dbr-joHffi4U-lpk4Np6Syzpm2-HDFtHKcEaGtwz_0PSbhzNYuBGe9sxBgIJgBLbTtWOvPIEH-xTtdqN4Zc-FKmsPenpd84ka35P3wtyrqukUWLwC9pF05jdyYnKZjfsdfJIXqfOU0vBsTTYL61na2kzV1e9GRtUwfADRwSFz_u6l8mgR63Xw8OwGh5GtcVNgsQ_QzoSkc35IOPiImPeJ-1OTwElQVeF1aiCzjCZ_ioffvJNDx_mvQohT4myp3xFwHPLmwEqqrnsPY-M9RVM6cChAW9pNWgN2ze39ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Khu8sixfh78AghYvbbHl52jXW6mvkmyJwLvCpxIl1pRkgB7dbr-joHffi4U-lpk4Np6Syzpm2-HDFtHKcEaGtwz_0PSbhzNYuBGe9sxBgIJgBLbTtWOvPIEH-xTtdqN4Zc-FKmsPenpd84ka35P3wtyrqukUWLwC9pF05jdyYnKZjfsdfJIXqfOU0vBsTTYL61na2kzV1e9GRtUwfADRwSFz_u6l8mgR63Xw8OwGh5GtcVNgsQ_QzoSkc35IOPiImPeJ-1OTwElQVeF1aiCzjCZ_ioffvJNDx_mvQohT4myp3xFwHPLmwEqqrnsPY-M9RVM6cChAW9pNWgN2ze39ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
👤
🇮🇷
#فوووووری
از علوی سخنگوی فدراسیون فوتبال:
🔴
سرباز شدن علیرضا بیرانوند؟ تاریخ بازی کردن بیرانوند تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده است و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104612" target="_blank">📅 00:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5U5rD_aalZeJUVFTDVisxs1dNAycfpCAJVBOO15t_-F5uDSF7gKAUyJIMA9dnD-_pSNCwFO2uy1XCU9ja_a9dQQmAXAleBSInvfEfjNU1w00-og83GSzjGiMyWrOTpxbKARygpgMmAb668PcYfFPzl2cEUobXO7gfXeFVjXMTe5oLUFJT1DIca7Ex-tQ6O4cJWRScNUwCZesLfRQZYLCdKeVfotUjVMmHhyZnub02DH2s5ioqWrpSjhrGPXO0ain2UrzG0kgZnAjBgo7gL1961ibsGmqHkQdDso-ogSMiY1vjkKhgXK1woAjyIupUQh30JqahXsvWELBJf4GXebgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
📱
انتقاد شدید جواد کاظمیان به عملکرد تارتار در بازی امشب: کمر پرسپولیس رو شکستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104611" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=T5UYN9H0JkTyl36LkdfjRwDWoyv_ZNAAp7Q4BWkPy40H4XpXhSawTlGURtb40QYeYcdSj7P9Ppywm8NurzFEpfd6VcYd0Okuxg92abKfzC8i4XbOkiNkaEwAnlQDKmVPYwsI_YDn3thMC6a5-XYtTga2CSaMQA5AsLKJHCDduHa330pI6WP97keAeUytZ5LUcYTBV5SxF0PU7h3ZcIeo7MUQnE_o3-PUKa3K2Q6XBCv-IECZ5guKfd5ukuUeWEjLVJ6UwaZObcleXufvCmwG6DhmwMnh838QYA1Wqbvn6mQV3S713UPD5IqgmOHfnd768dc7_Su97w-TIcN1WZQ3KDiLP0HgNWmxDG_kVV4h-aoRbQMwdWo0pxXOCQKJ-diy2X8-E4lSnPbnCkMoQqVW2aSAk7ifPShgC26TCXOTZ5QTfNIZkLsgdT_zSTiIesi2a45PIwOB1tBnhQDjmvqIq8boIJ8__ombZh2Ki34oHathotQNoaRnMKWVj73yMUweMUU_55cD1sAFt_HPndvbbhvMa_CteWZclrKNHnXyOiCbVG4sBaZaFt3eBe0I3B44yiEALycMG3vGWL4mBbLO33ZzPFFTeE1O1p3dcUoIHjqK2Tu2_WXKH-D6poiorjiColTpdMlBczy4ZK1RHwuKdV2AHCL9NjZgnlafN9a5oJY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=T5UYN9H0JkTyl36LkdfjRwDWoyv_ZNAAp7Q4BWkPy40H4XpXhSawTlGURtb40QYeYcdSj7P9Ppywm8NurzFEpfd6VcYd0Okuxg92abKfzC8i4XbOkiNkaEwAnlQDKmVPYwsI_YDn3thMC6a5-XYtTga2CSaMQA5AsLKJHCDduHa330pI6WP97keAeUytZ5LUcYTBV5SxF0PU7h3ZcIeo7MUQnE_o3-PUKa3K2Q6XBCv-IECZ5guKfd5ukuUeWEjLVJ6UwaZObcleXufvCmwG6DhmwMnh838QYA1Wqbvn6mQV3S713UPD5IqgmOHfnd768dc7_Su97w-TIcN1WZQ3KDiLP0HgNWmxDG_kVV4h-aoRbQMwdWo0pxXOCQKJ-diy2X8-E4lSnPbnCkMoQqVW2aSAk7ifPShgC26TCXOTZ5QTfNIZkLsgdT_zSTiIesi2a45PIwOB1tBnhQDjmvqIq8boIJ8__ombZh2Ki34oHathotQNoaRnMKWVj73yMUweMUU_55cD1sAFt_HPndvbbhvMa_CteWZclrKNHnXyOiCbVG4sBaZaFt3eBe0I3B44yiEALycMG3vGWL4mBbLO33ZzPFFTeE1O1p3dcUoIHjqK2Tu2_WXKH-D6poiorjiColTpdMlBczy4ZK1RHwuKdV2AHCL9NjZgnlafN9a5oJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم چلسی به فولام توسط کول‌پالمر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104610" target="_blank">📅 23:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=H6HJmye4pgHCjwXSvZDWQzzrXeoAo05afoRJ9mUqOY53D_gTdCrd0mCt1DkyYE2w3IvhTICfJ6zxtbyb-TnbR11-GDhrr8XTSdAPWjja6e2lzObMCNWhLzphDru4VSwpmk6rDJTn8bBqw6mRH067A7m-2ma8hin2vn-ztPvSrZ7swFWjcfdDvTOkDXzpnhEaubPHo6I0R8SVEdjm_8LGzrJI89zV8I1DCV6cOZN_TcW7p_G7mV-i-3QYBV5eVaLVufp47JGwa6ejVcdms7CaQiAVvNgQvS0Ckl8YSaRAVeZoFtCsNkvHCzM8S3khZsf0Uavbw_m8iI-atfNebGGKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=H6HJmye4pgHCjwXSvZDWQzzrXeoAo05afoRJ9mUqOY53D_gTdCrd0mCt1DkyYE2w3IvhTICfJ6zxtbyb-TnbR11-GDhrr8XTSdAPWjja6e2lzObMCNWhLzphDru4VSwpmk6rDJTn8bBqw6mRH067A7m-2ma8hin2vn-ztPvSrZ7swFWjcfdDvTOkDXzpnhEaubPHo6I0R8SVEdjm_8LGzrJI89zV8I1DCV6cOZN_TcW7p_G7mV-i-3QYBV5eVaLVufp47JGwa6ejVcdms7CaQiAVvNgQvS0Ckl8YSaRAVeZoFtCsNkvHCzM8S3khZsf0Uavbw_m8iI-atfNebGGKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
استوری طعنه‌آمیز و فوق‌جنجالی علیرضا بیرانوند
پس از برتری در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104609" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=GrLYkwLnZ8XLFD0Bbw1uUBCwpzD_Z1QANQU5k9t2R3rU20HVKXW0Y1ilRMwrx5k1UvZAMyL_ubrsu2WUI5qLqD8qDqlHBF613JW_BCJi4T6MQbQNKPCNwrnncbQ4vCK5V8EeByt77QBxghgRhXCKk4Vbmxp9ZdHMtBURhrIvfBUwHuOg6drgy7OQMEnikBw-uWtxKXfIfCCkskmRE9xeP_EqGhNI1PKjAdxAin_VjZJeYaMAH_YhCGTXNAtFQiM3cXw_faBC-5fbm7enkHuPDcPMoIkUwA3CCi_4vVVve92ZqcF-veNnapL1o7S_xufplv5c8Ls5dYCzhqUxNFdU-EDsWyk7JKHm6zysoVCuuJaXRkx7YG_3mMqyvnDnf3CBRmJxnJCVhPSY5p5POYYKPFRhI56IY7vPfkOMtfyIAtBtqA2obfb4VQkuj0NrMkaVK2KO4uJycNu34Uxxxjl7kyvTYxzmHCPdil0jnF7QAy0rLAKx2UNiSNgb4FyKlk3aHBkzpmg-Ivt8qS1cr4x3a2FVmvZIjUO8vMbijjYXCs6iJmnzrYQP8Fk5TTU1QuClGfSpDX0gTflj_Kw2q_-QPHiKFrqDm4KwEDyD0N16v2LObFdrzwUA7WvIcP-omhBLGZ0UGEtKCU-5Ab2Z2LIIZIVcgZNIM1NKp6k2G37WArk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=GrLYkwLnZ8XLFD0Bbw1uUBCwpzD_Z1QANQU5k9t2R3rU20HVKXW0Y1ilRMwrx5k1UvZAMyL_ubrsu2WUI5qLqD8qDqlHBF613JW_BCJi4T6MQbQNKPCNwrnncbQ4vCK5V8EeByt77QBxghgRhXCKk4Vbmxp9ZdHMtBURhrIvfBUwHuOg6drgy7OQMEnikBw-uWtxKXfIfCCkskmRE9xeP_EqGhNI1PKjAdxAin_VjZJeYaMAH_YhCGTXNAtFQiM3cXw_faBC-5fbm7enkHuPDcPMoIkUwA3CCi_4vVVve92ZqcF-veNnapL1o7S_xufplv5c8Ls5dYCzhqUxNFdU-EDsWyk7JKHm6zysoVCuuJaXRkx7YG_3mMqyvnDnf3CBRmJxnJCVhPSY5p5POYYKPFRhI56IY7vPfkOMtfyIAtBtqA2obfb4VQkuj0NrMkaVK2KO4uJycNu34Uxxxjl7kyvTYxzmHCPdil0jnF7QAy0rLAKx2UNiSNgb4FyKlk3aHBkzpmg-Ivt8qS1cr4x3a2FVmvZIjUO8vMbijjYXCs6iJmnzrYQP8Fk5TTU1QuClGfSpDX0gTflj_Kw2q_-QPHiKFrqDm4KwEDyD0N16v2LObFdrzwUA7WvIcP-omhBLGZ0UGEtKCU-5Ab2Z2LIIZIVcgZNIM1NKp6k2G37WArk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم چلسی به فولام توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104608" target="_blank">📅 23:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=G73MONsQ9IEnPN65FwYJRviwk1-FnQ_Y5sOE9oR-NA2xPYCytkhawASnY5cysRZALm_Krhgh6rKlG7sGYAnEM8LQt3tEPgsQ9gGKLzbtipJDrKlnIPjTv-7pnCvAEI2J-astDxy8jA7_KOcsX038eHWcmz34FozZnly5O-6Zu3flNX82Rs-IGESBMg_YWfE9eZw9lZ9-TG9U0bFzLNphu3n-5eKUtP-BXoRkZFViLRR6yNt59llRWbHvRaN53E4WZgrH3-23WkNBFPKnNst_d_8BsijBomFohANCmEZvfTecrDKnqPi2Y0jHYqo9NBzV3478olkSK-6egd8I1FZlQh8xU58gar5FQlham3BQyiy1RJeq6M__prD9yo4AJvs0OAsafkj6zA5XHVXeYJide7JIjux_TzC0Svp3zqac0xwgrd7QgdokYKRa228AwNho671HR-qQDImjLNrcdLMZgXkqX38f-n3JV5QYGnNG6tkPhAx4a5ic11jZaSXBr1xxOmO6Y2LSCc6co1HS69unckN2E7sFkdWXKlSFxEf6OVYWZikmAY_lblz8SZ_TGFZwBVOqcuzioYCMHy8uvBSM_rOA9XxuNJdjW0Mk52k_0i1IXZsNe8D65o0BSpRFXfs6AMvreshmUKsoCV6piFngfnUuurP0_7flqLZMHO6_cwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=G73MONsQ9IEnPN65FwYJRviwk1-FnQ_Y5sOE9oR-NA2xPYCytkhawASnY5cysRZALm_Krhgh6rKlG7sGYAnEM8LQt3tEPgsQ9gGKLzbtipJDrKlnIPjTv-7pnCvAEI2J-astDxy8jA7_KOcsX038eHWcmz34FozZnly5O-6Zu3flNX82Rs-IGESBMg_YWfE9eZw9lZ9-TG9U0bFzLNphu3n-5eKUtP-BXoRkZFViLRR6yNt59llRWbHvRaN53E4WZgrH3-23WkNBFPKnNst_d_8BsijBomFohANCmEZvfTecrDKnqPi2Y0jHYqo9NBzV3478olkSK-6egd8I1FZlQh8xU58gar5FQlham3BQyiy1RJeq6M__prD9yo4AJvs0OAsafkj6zA5XHVXeYJide7JIjux_TzC0Svp3zqac0xwgrd7QgdokYKRa228AwNho671HR-qQDImjLNrcdLMZgXkqX38f-n3JV5QYGnNG6tkPhAx4a5ic11jZaSXBr1xxOmO6Y2LSCc6co1HS69unckN2E7sFkdWXKlSFxEf6OVYWZikmAY_lblz8SZ_TGFZwBVOqcuzioYCMHy8uvBSM_rOA9XxuNJdjW0Mk52k_0i1IXZsNe8D65o0BSpRFXfs6AMvreshmUKsoCV6piFngfnUuurP0_7flqLZMHO6_cwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
❗️
درگیری شدید هواداران در دربی خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104607" target="_blank">📅 23:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=S3XWSfNiZWfTRwH-DZ894xN4Cdm9aeDdykngCnPbyJLGWWC9CLPCzO8-Hob95CMHtNlvoeMKL5PcBIL1DzEYyV5Rx8rmmBt9RKcMsPM7GSLjrPqGCM0U2TgS2Clngm_CTiWI2gPYtIo2FlKxSh-eFtieFOqo5GUl5oYADZqJhUrgj7vTDySqWMb-lLQmNW8bArcL_jOf0HrMB_lapW0UFqFMDyDhUDWBee4ThvGVIdfZlqiBsyxM9ibBiM5XenmY6nppQwdPzrKXSszWrbU6mOd3vzVhiepe0glf8SM4uhbMtn8LRkoa3QD6L3t2bPQOjK620ajCWtuOq785aigu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=S3XWSfNiZWfTRwH-DZ894xN4Cdm9aeDdykngCnPbyJLGWWC9CLPCzO8-Hob95CMHtNlvoeMKL5PcBIL1DzEYyV5Rx8rmmBt9RKcMsPM7GSLjrPqGCM0U2TgS2Clngm_CTiWI2gPYtIo2FlKxSh-eFtieFOqo5GUl5oYADZqJhUrgj7vTDySqWMb-lLQmNW8bArcL_jOf0HrMB_lapW0UFqFMDyDhUDWBee4ThvGVIdfZlqiBsyxM9ibBiM5XenmY6nppQwdPzrKXSszWrbU6mOd3vzVhiepe0glf8SM4uhbMtn8LRkoa3QD6L3t2bPQOjK620ajCWtuOq785aigu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به چلسی توسط جاشوآ کینگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104606" target="_blank">📅 23:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoHFLrOObgvHeZMT7_BQruYY675UaKFGmihutKQwiImRRmOp979_x8ar1ixmpdLQnf3t8EljTAoNa6kC24s_8I5tnFO8QlypfHcPmsoZpgt_mDYAJwthrI8YgXalIze1Vp1XizSk_IQ36_dIrHRmzh7MEkiGhXSFLZEpYYHqfPRD8njAaZUcgRCaQ4eMEuI3woX4QgORL-1HawHTh4nKhncCaUTi1GJ8rEoLBEUJfGfp3Kv-GIEKvvgxcUKr6tr3bb2wrBKXrQLPLHPnuaSGT9Coftos8jLOYYlbsIaHBywBa0MTuo1jqFdqGqBtu4TjxgPE5rdClxKbwabLfbyhLxx0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoHFLrOObgvHeZMT7_BQruYY675UaKFGmihutKQwiImRRmOp979_x8ar1ixmpdLQnf3t8EljTAoNa6kC24s_8I5tnFO8QlypfHcPmsoZpgt_mDYAJwthrI8YgXalIze1Vp1XizSk_IQ36_dIrHRmzh7MEkiGhXSFLZEpYYHqfPRD8njAaZUcgRCaQ4eMEuI3woX4QgORL-1HawHTh4nKhncCaUTi1GJ8rEoLBEUJfGfp3Kv-GIEKvvgxcUKr6tr3bb2wrBKXrQLPLHPnuaSGT9Coftos8jLOYYlbsIaHBywBa0MTuo1jqFdqGqBtu4TjxgPE5rdClxKbwabLfbyhLxx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به فولام توسط ژائو پدرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104605" target="_blank">📅 22:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjFk7KM4L2Z5if5FGUygYQsX-16TcX0ovw_poKJgD2yrU5QPmOR4PcmHekwDpPjGqotNAZtfMMaG6fI96nyFxHpl26lgY5f9hwzT6yBGBCDI90pB9b2sxTfB8kMfR51tZkwBS0-N9cLRP7kgJef_qyVFlcXfKJ-8KmkSkaLgbFTJi1Bz3VLlv4_5B8AxLHIdBCxONAy1gyJkvVcnZS9KjKIqJmJArpCeBvMYqWx0Wbu6j92RRZT-gDsMWcot7cdYvx460mWRVr-h2N6Ne63bZU6HLi-MvRFHJoUEH5JfoE5ls6Z_k0OMrocSt8-F6Lw5e9JYwfm6lPukInya9OMRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
نتایج‌‌بازی‌های این‌هفته لیگ‌برتر فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104604" target="_blank">📅 22:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b217109864.mp4?token=kWMfaR13CQVZyQCLOKAhlelDYQbvA79QZzCtae61jbwaCWqfK-vv-WyGVj5hlzzX5Se95vhhZOcQGSEU8CPj1W6nwgWVONcaO-_Qg3GEnmgwVC3uisPO7r4nvZxs8Ia1ECWj8FisqKwizjtD8L_W6PpcqbkG-lCWoSDeJcD2VOLx2MxTqTNEco9eqDbNy2_Gmykl_GnbtjPsbauD7cNV_57zzdL5BhPfaPocXd9uy5_XmYC3IcT7Loi7m8p4xzXID2W0_62h5dyAx5iZGl9aRmNy8e2BFoQSNQhvaTk4aS92j3PN54eK2CAJlHWR0n6nDd-Y0MndezVNQe0aiSy9XKha-KlnXhivWg2cmgLy1y0bj7VEqk00NYLa8S5RL3j-1Kd3fk6P3eNI4RFnpIbTvhxXpelY8lsENZYtK1etvhz8ofduH4cPASd7Dh_7NpaOP7O1E6mGqFLV63eT2p0nWbUkbdpfVYqDEv10-PLqbwUvnmrdB47vwHFg1oNQ0fSOd1XgugVLfc4eksU90EPhjTk7-GtcHK83-QZSVsshsJVqk6Nv6AVmMlrUzSMo99iFBQXsAyTrgxaB2ERr6J4GC0Rv4KqMw2NNolCq6cbdnCjYtIje4JXDHVII6IeBiH-6njSypBzZwfPb28rdZHQRG1Y0JSRjcpQQHRgHWEqx1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b217109864.mp4?token=kWMfaR13CQVZyQCLOKAhlelDYQbvA79QZzCtae61jbwaCWqfK-vv-WyGVj5hlzzX5Se95vhhZOcQGSEU8CPj1W6nwgWVONcaO-_Qg3GEnmgwVC3uisPO7r4nvZxs8Ia1ECWj8FisqKwizjtD8L_W6PpcqbkG-lCWoSDeJcD2VOLx2MxTqTNEco9eqDbNy2_Gmykl_GnbtjPsbauD7cNV_57zzdL5BhPfaPocXd9uy5_XmYC3IcT7Loi7m8p4xzXID2W0_62h5dyAx5iZGl9aRmNy8e2BFoQSNQhvaTk4aS92j3PN54eK2CAJlHWR0n6nDd-Y0MndezVNQe0aiSy9XKha-KlnXhivWg2cmgLy1y0bj7VEqk00NYLa8S5RL3j-1Kd3fk6P3eNI4RFnpIbTvhxXpelY8lsENZYtK1etvhz8ofduH4cPASd7Dh_7NpaOP7O1E6mGqFLV63eT2p0nWbUkbdpfVYqDEv10-PLqbwUvnmrdB47vwHFg1oNQ0fSOd1XgugVLfc4eksU90EPhjTk7-GtcHK83-QZSVsshsJVqk6Nv6AVmMlrUzSMo99iFBQXsAyTrgxaB2ERr6J4GC0Rv4KqMw2NNolCq6cbdnCjYtIje4JXDHVII6IeBiH-6njSypBzZwfPb28rdZHQRG1Y0JSRjcpQQHRgHWEqx1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
مهدی ترابی: قهرمان آخرین دوره لیگ برتر ما
هستیم؛ حق تراکتور کسب سه امتیاز بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104603" target="_blank">📅 22:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3_V-b9mLlQsvEPEU0MRVukqBi2Dzp2YJsKYd3UT1BP5ojSuMMxZQoB7uTgTNzOtuK6H0N493ccGI2JGRC_EE8obnmLiMVGcMWyDfUITbzV6_fsH6_teLdqyVjDbftmHuRCcl6QX4Q4eXAUznNUVwoNZdlMkNEgSW-3Rh3oAo18d7EzRkqI-ujM-XVrQcSFJ5tjKEJ8uSEcvnJs7aaybpAkkneWIFc69OVs4tBTkwq5eR4sBi4O_EGzylOr2BKv1tYuBj3xDlEXtv9DdEkhRbN9r2X5ArIBz5ToUcjq9JKAPoH-p7_pT-ilAS3vcfh8d5DG7nuo7T66CJL0y6fjVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
کری‌خوانی صفحه تراکتور برای پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104602" target="_blank">📅 21:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723487d9b9.mp4?token=Fdh22A_JEcmAUNKVOSI77oUsPLiiRCbB1fnkbI-1lJPREbfeChNl3YWJ3FVerR8b6_LrdDF2wPyQh5ewVa6sKbi3t2hZANdRa6EDdi2r503h0Zmv-Ew23ceO0xihDTekikk_AjWiP_rfT2iVIMdiZvSmieMBy0O7gfH4vWvrTrkL5lhbZd_PtKnyr6WT4D4UqcDS85PEEE8je0SDHyYmktDUupMI9UtzsUu3__oXJr-27w1cFM3zqK1KyQzJ-SIcxKtcOPe7T4z7XRw6nw8jqGHwbA8BUZxOpm_g_BqdC2V61_knDFAnuAUI3ZMV-kCINdI_oe10A7Qi_C8cBXcE-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723487d9b9.mp4?token=Fdh22A_JEcmAUNKVOSI77oUsPLiiRCbB1fnkbI-1lJPREbfeChNl3YWJ3FVerR8b6_LrdDF2wPyQh5ewVa6sKbi3t2hZANdRa6EDdi2r503h0Zmv-Ew23ceO0xihDTekikk_AjWiP_rfT2iVIMdiZvSmieMBy0O7gfH4vWvrTrkL5lhbZd_PtKnyr6WT4D4UqcDS85PEEE8je0SDHyYmktDUupMI9UtzsUu3__oXJr-27w1cFM3zqK1KyQzJ-SIcxKtcOPe7T4z7XRw6nw8jqGHwbA8BUZxOpm_g_BqdC2V61_knDFAnuAUI3ZMV-kCINdI_oe10A7Qi_C8cBXcE-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پاس گل رامین‌رضاییان در بازی امشب فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104601" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f291196ab1.mp4?token=Nj0UtnOiH_BwStyIbxp6YHQ1RBRKdJhJpROFspMhLT68F-PVYa1i2Xkg_ioZ-03z_HXJqMb-OlVzdlNEwZ1CuldvPpd2HvZsBYhEnvtCPG9eKCY5hSTgr8w7lU_7m7xQ_THcOJ-iql9fWwyMeA-6yzoTC8mGmouTLxhDN25VSurATLlGT5vy2cSj3NBVHXsANfH-Ho0QEFvkgvkqNYaqSCVyopIkCMgTm6LZKrk2iy8jR4po_O8zIuDxXrcXNvua2rre8PzIaxnQIO8I2tSsDShiW-KdY9a5DBNqY9XVC-skfa7RQLmP0tvvpAr9A3j7soa_G9X9VhGaAE-bwQ6PCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f291196ab1.mp4?token=Nj0UtnOiH_BwStyIbxp6YHQ1RBRKdJhJpROFspMhLT68F-PVYa1i2Xkg_ioZ-03z_HXJqMb-OlVzdlNEwZ1CuldvPpd2HvZsBYhEnvtCPG9eKCY5hSTgr8w7lU_7m7xQ_THcOJ-iql9fWwyMeA-6yzoTC8mGmouTLxhDN25VSurATLlGT5vy2cSj3NBVHXsANfH-Ho0QEFvkgvkqNYaqSCVyopIkCMgTm6LZKrk2iy8jR4po_O8zIuDxXrcXNvua2rre8PzIaxnQIO8I2tSsDShiW-KdY9a5DBNqY9XVC-skfa7RQLmP0tvvpAr9A3j7soa_G9X9VhGaAE-bwQ6PCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
خداداد عزیزی: بیرانوند از مهرماه سرباز است؟ قسم می خورم خبر ندارم/ ما علی بیرو را خواهیم داشت به امید خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104600" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5ClGRvbd501Br0dwkiT0nA6QeWTh-zqNNZN3_RpFg8fx252IKnFp5Cm-hJA6J2ZiYD8_cL-wN4zL8Y9uKt8kiAWyI90EddXh71ifruEr62DgXAukGbjAH8qLxFanc_zjfILLga4SjdkG2wiN9pgQ6YFInxXQsER-0pYA0BaKEpQymGn_UOxir8KhEVR1kuwrCbdDGqn3Kvu6TCkrtrwazMoCDX2bL0qiJurUXlur0aRwEEMajvSWGI4H2mLG-VLXaZoClo6a-k0XhI1CGqUqiB10MDtEebL94WGaQKUEI_l353rkLo4BmyWlBY2PneCUb3aRNroArLuKVAo7IoO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌اول پریمیرلیگ؛ ترکیب چلسی مقابل فولام؛ ساعت ۲۲:۳۰ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104599" target="_blank">📅 21:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa4d7c9.mp4?token=YGWv17qz2r-FXldF4nOX32IomTQHYQIRHx0xjcXV9mhafWLFwXv3Bt1rNskgrTmqC-ltkHuco2A0-NtVrQInFaxX2mZH-kkHR2dTQH1VAwN76f55gloGOoBgWfWpJyPLKLDEiIqJkA4MzS2vaby5SYjXDd64LjM_n-8MktOOmHu5lR1X61y7d9BmJuhz9eOmfKvN4Pi2CzOJzVzodBEB0xmMyHuY8E0r8HPCWxbPnHATwGU_kfeTlI11kI4F_ZSuSL_Ucif4-Zkhfo_jfHPFQwyDwMb3Y1fL0g6lSZ4oR1yIyypZpNMcor4jTNr6FQSCfDlN4H1KEFJPzRAj2xKh_oMuiSxU-KCI-umCFRAB_2oDqKEqNYvlGEnEcqv1Zlet_8_3-pDi0yOUap3HgV50hXX925HDe_9iIJiBcnRGjjTkbrsm-9_A0hLfSVg7Lx5y6ieITUMEBB0KW6IjKrr36BVXhuVGkKJfQTb9K0jno6TaRf2ezAai4TNH34TLe2s_WJKjSDkY2zMukDUtZqFaOhCKXGZmUkmL0cwY_7EMzbgTb5n_oa1juGHaTSSw6btt7ruifTDV0mFmE_644bduzvuWuOT7jjRmSUwUGbw6NHz7C_--HXtoze0zqrdKOxUFQriQYchmHASS_hXura5h8BrIX9Dqr_5vGSxooEhkhe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa4d7c9.mp4?token=YGWv17qz2r-FXldF4nOX32IomTQHYQIRHx0xjcXV9mhafWLFwXv3Bt1rNskgrTmqC-ltkHuco2A0-NtVrQInFaxX2mZH-kkHR2dTQH1VAwN76f55gloGOoBgWfWpJyPLKLDEiIqJkA4MzS2vaby5SYjXDd64LjM_n-8MktOOmHu5lR1X61y7d9BmJuhz9eOmfKvN4Pi2CzOJzVzodBEB0xmMyHuY8E0r8HPCWxbPnHATwGU_kfeTlI11kI4F_ZSuSL_Ucif4-Zkhfo_jfHPFQwyDwMb3Y1fL0g6lSZ4oR1yIyypZpNMcor4jTNr6FQSCfDlN4H1KEFJPzRAj2xKh_oMuiSxU-KCI-umCFRAB_2oDqKEqNYvlGEnEcqv1Zlet_8_3-pDi0yOUap3HgV50hXX925HDe_9iIJiBcnRGjjTkbrsm-9_A0hLfSVg7Lx5y6ieITUMEBB0KW6IjKrr36BVXhuVGkKJfQTb9K0jno6TaRf2ezAai4TNH34TLe2s_WJKjSDkY2zMukDUtZqFaOhCKXGZmUkmL0cwY_7EMzbgTb5n_oa1juGHaTSSw6btt7ruifTDV0mFmE_644bduzvuWuOT7jjRmSUwUGbw6NHz7C_--HXtoze0zqrdKOxUFQriQYchmHASS_hXura5h8BrIX9Dqr_5vGSxooEhkhe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تارتار سرمربی پرسپولیس:
دلیل بازی نکردن ارونوف و سرگیف؟ این به کادر فنی مربوط است و دلایل فنی داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104598" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c69ee8ec9.mp4?token=lHUwAbeQdIv7jSL_7naamI6nYrHocPSdGvjEikhK18lKJam0KkmMlRoblld2AsGOmlNbxWzwCT-EKCrjr3N8otCDzH_oTeHoAkJ6uNnm7qjorbI0othaWST4o-WB2ivIjelgaX3OUFC5UJZ2ntWvL6gERkv-qMrk9YTtdNUJFj1Kx9f10k5F5zFEiz4MwL-LQAhjj9QtAZBw4s5jwJyMyWaU_O1ZZdrPccEwuNjnIufk8EH4QtPRI4As506rv1TkKrjR8iwfCP17goJSp553mslhUuVRIhqVOgjylBDxU1O7ORuLUJasWdXHDd8E4R7GxaWHHd8FnwFyAQ-yOlkl0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c69ee8ec9.mp4?token=lHUwAbeQdIv7jSL_7naamI6nYrHocPSdGvjEikhK18lKJam0KkmMlRoblld2AsGOmlNbxWzwCT-EKCrjr3N8otCDzH_oTeHoAkJ6uNnm7qjorbI0othaWST4o-WB2ivIjelgaX3OUFC5UJZ2ntWvL6gERkv-qMrk9YTtdNUJFj1Kx9f10k5F5zFEiz4MwL-LQAhjj9QtAZBw4s5jwJyMyWaU_O1ZZdrPccEwuNjnIufk8EH4QtPRI4As506rv1TkKrjR8iwfCP17goJSp553mslhUuVRIhqVOgjylBDxU1O7ORuLUJasWdXHDd8E4R7GxaWHHd8FnwFyAQ-yOlkl0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❤️
تارتار: به خاطر شکست امروز از هواداران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104597" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=gWWWOPu0oXjworb_3-2CKvTvG0P_ZVsKpzWOx2lIdGHBNNCPQJ9LMaqjciMuWcWrHMmDKrdQUWUWomTe3Vdz0sCQzXUvfKN36vTiC7plVbTLzo6dSE9vn7ll8hD1RLV8CRUdy1TViibsMtU9RUGSNGT5vBBD7zXXwxgqQODAdGy86tUfVKMOma-bXhNUsr0ObBYr6P6MkDcgDgiYNk2FMJzXv03Sn18uZXOmM69RCQekojuU0gh3FO5iNL9WCvfOKNtSGOHuewhS1mVyXKjtDOePAkPG2lNLC7fQPh1yDYh1duuSl485PuhvQ_jFf-FMen2OX_-5BtuvWpntCit4tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=gWWWOPu0oXjworb_3-2CKvTvG0P_ZVsKpzWOx2lIdGHBNNCPQJ9LMaqjciMuWcWrHMmDKrdQUWUWomTe3Vdz0sCQzXUvfKN36vTiC7plVbTLzo6dSE9vn7ll8hD1RLV8CRUdy1TViibsMtU9RUGSNGT5vBBD7zXXwxgqQODAdGy86tUfVKMOma-bXhNUsr0ObBYr6P6MkDcgDgiYNk2FMJzXv03Sn18uZXOmM69RCQekojuU0gh3FO5iNL9WCvfOKNtSGOHuewhS1mVyXKjtDOePAkPG2lNLC7fQPh1yDYh1duuSl485PuhvQ_jFf-FMen2OX_-5BtuvWpntCit4tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
اسکات بِسِنت وزیر خزانه داری آمریکا:
🔴
«می‌خواهیم امروز به‌روشنی اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست.
🔴
اگر کسی معاملات ایران را تسهیل کند و بخشی از شبکه‌ای باشد که نفت ایران را به پول و سپس ابزاری برای سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهد گرفت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104596" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=APqzmW9luWZx0rZziH2y67Yq2DciZ_cio5wEv--_MHIgj9AdxbNGFUrxW76LikhE7Is1__1SG4Tq9pSwex6-qzea9cDHLVz5LbdiOd8PLwx2rCBAM3qDBYHZRUpJWpnErtqzpkK35I36pj42InU7YV-g7xVYO8TvOrE-iJQfQ2-1FdP80uu7h5X5VWaQhJESt6XV1vMotnlPA5Nwv0WQn3T8FFVXQWPHLOBwhRA0nUBF1vS6Xu8-ApnZ6uIU0wGZ7aBV0RKZNi5y74evG3RPCQgEFk1n7XFK6OODpF7NGwxxe70ulBMPXupMiba6ebl66DRcY159huakudFuly2awQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=APqzmW9luWZx0rZziH2y67Yq2DciZ_cio5wEv--_MHIgj9AdxbNGFUrxW76LikhE7Is1__1SG4Tq9pSwex6-qzea9cDHLVz5LbdiOd8PLwx2rCBAM3qDBYHZRUpJWpnErtqzpkK35I36pj42InU7YV-g7xVYO8TvOrE-iJQfQ2-1FdP80uu7h5X5VWaQhJESt6XV1vMotnlPA5Nwv0WQn3T8FFVXQWPHLOBwhRA0nUBF1vS6Xu8-ApnZ6uIU0wGZ7aBV0RKZNi5y74evG3RPCQgEFk1n7XFK6OODpF7NGwxxe70ulBMPXupMiba6ebl66DRcY159huakudFuly2awQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
🔴
«خطاب به سربازان عادی که از این حکومت حمایت می‌کنند:
🔴
وقتی پرداخت حقوق‌تان یکی پس از دیگری متوقف می‌شود یا به‌ظاهر فقط به تأخیر می‌افتد، از خود بپرسید آیا فرماندهان‌تان کشور را به سوی پیروزی می‌برند یا ویرانی.
🔴
به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به مردم خود شلیک نکنند.
🔴
و خطاب به کسانی که به تهران کمک کرده‌اند: هزینه آزمودن عزم واشنگتن را دست‌کم نگیرید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104595" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b198e5e16.mp4?token=IBZ09WvShcactpDriyo1ewyFMn4f4uAp3wjjVlC4NXNzWAHQ0ZldwUYzp1_K_moSMQnega7tfg4zgryHEsPeQ2wZfRx2563SHAiVUTcHmJZaVZLod-UWljlYP02CjDd3JZRRvsh9aQmukQCApbV6qjwiXcqA7LKgNyS1J6K_HokEAqUpNv4eFq5tMvvRXNt-Lkvtu-qOcq-7PI5avrGrB-YwjQtIEUMMrBOmWtsttLf9UUHPOhV5jeENZj0LJK2hZjvg1AiDgW4VpP7bRDxyiYPm6XjfFaPNA2KoocGhLGrNW57acGj1JoTDn4F0QhBEsMcsEX9sE0jYmSaC7Hfrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b198e5e16.mp4?token=IBZ09WvShcactpDriyo1ewyFMn4f4uAp3wjjVlC4NXNzWAHQ0ZldwUYzp1_K_moSMQnega7tfg4zgryHEsPeQ2wZfRx2563SHAiVUTcHmJZaVZLod-UWljlYP02CjDd3JZRRvsh9aQmukQCApbV6qjwiXcqA7LKgNyS1J6K_HokEAqUpNv4eFq5tMvvRXNt-Lkvtu-qOcq-7PI5avrGrB-YwjQtIEUMMrBOmWtsttLf9UUHPOhV5jeENZj0LJK2hZjvg1AiDgW4VpP7bRDxyiYPm6XjfFaPNA2KoocGhLGrNW57acGj1JoTDn4F0QhBEsMcsEX9sE0jYmSaC7Hfrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇮🇷
گل‌تماشایی گل‌گهر در بازی با چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104594" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZO_potB9iSP2GBP9zCTwlyHDpunrDa0V0a97JEAe4wy76U-c-Is4D8ks_LumwGEceUE6rDoS_xt4LTesKHTeM2HoblL8Z5jlUogHkENn-hFZQ0SdgbwLk7iL4gTc39yKwfmJk4MPIoLbwE_4nKeOrHCKBlA5b-3iVAp-hmdcWRb2JruNPj0t9fMs2LQzFPCH1u2qUPiVxUZCLbUiF4a_nnIAk3Lq6la_d4_uHCG0-3k4Xk9NO9gUsJHF6i3Lo9G-32yHfmtAjogwN1oDks2H_nP4CE0m0w1uuzqgMjOEkmDsFpszhMgE0n1K1C_xbW0ByWbLw0xK1B_An5tjsptfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
توییت کنایه‌آمیز استقلال بعد از باخت امشب تیم‌فوتبال پرسپولیس در تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104593" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c54496137.mp4?token=Jye-CaLJFOAWVIbcciYneQ70TKmaYJFhvQIfqvqv6N66YGCCEmH1vq52l4Ame_Md_ed_byyipVCNmwVld7rW-MATbkeL7rjs1dEWsFaQBcECn_mfmBGoQ5sN4irQc-UIhdI6quKT3Kds09ed8ZkjEExbVKN4DwU7L6-zNTc5VRYL3gixM7a9LaTOF8qSt0GONU5SdP0D1--3-uLMwEk7uMlvEIh7UsCIh3mSKmNCZGe0rwn-6OTtQO6_Pn-FPq3y--9g4ihqr-48L02LJC_AS5YXDar7i1qBHT54qHza5wunymWMK9nuSnBemmEpbP5YZCiL_Qcr00sYZq0o6Aj4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c54496137.mp4?token=Jye-CaLJFOAWVIbcciYneQ70TKmaYJFhvQIfqvqv6N66YGCCEmH1vq52l4Ame_Md_ed_byyipVCNmwVld7rW-MATbkeL7rjs1dEWsFaQBcECn_mfmBGoQ5sN4irQc-UIhdI6quKT3Kds09ed8ZkjEExbVKN4DwU7L6-zNTc5VRYL3gixM7a9LaTOF8qSt0GONU5SdP0D1--3-uLMwEk7uMlvEIh7UsCIh3mSKmNCZGe0rwn-6OTtQO6_Pn-FPq3y--9g4ihqr-48L02LJC_AS5YXDar7i1qBHT54qHza5wunymWMK9nuSnBemmEpbP5YZCiL_Qcr00sYZq0o6Aj4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
سوپرگل‌بخودی پشم‌ریزون ذوب‌آهن در بازی امشب مقابل ذوب‌آهن اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104592" target="_blank">📅 20:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXKq0rJmHVKm8-iI7P2pcDphKyYWSMIvv5ddMwHiVZaACfc47AlnOelpg3YdjZS-bQF3cHkExaFtuOBzRdIfymYLZegXqq91GDoerFQXDkHScGL97nvKzrYC4a4MesORwVSsO7rVc7MC9J4d9hdDz-mD4EmC9DMpc_0a6alBWFs1LvYwoE5uJFdFASlV2niMux1qLeesOdNZWGMbgoGiGs6oOAh0E-tzLLD19Z_WV3m18PMSlnj98TpSEnNOSbjJogzK27-nq9GCN9SePJ81Gozel5y9wiXfv8cR7wldVeWFdIlwI4zKUEe2NsZ--TZh1huTwy6sqg-71X-ldPANkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ نکونام با سبک خاص خودش در تبریز برنده شد؛ تارتار و ستاره‌هایش در اولین محک جدی با یک تیم نامدار ناکام ماندند!
🇮🇷
پرسپولیس
😏
-
😃
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104591" target="_blank">📅 20:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrp-zO1eabMOFTRJDf1rXvqCatx6uxGsx28SSd9uRog2x9BX5xrvYIp62mqpX3a_wpV7_TBzsYtd_VMrCbsYO5yxji7e9yjBI2IEPLSOqRTb1RtYCbTf6qeGz57uqxRdvdOAu-PDIR7jTD1grNuuWL4P1Q9HFBOOvaEwiWZyg8E20mM33jpKyoiEC6MMJPDSpmgHgHKj7X3jnKW_e_EQtXZTHesqUWSmkZBo0O4-NvPVAR3fQz9CSZEl8Ip_7uNvCL8j3XMFkNxbPACTWooGc6EhkqVWisl2970PClnYSPVS26KjUmqVZt_JT4zvPfMnByq4nWA4y5xn6I1zVrS8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ نکونام با سبک خاص خودش در تبریز برنده شد؛ تارتار و ستاره‌هایش در اولین محک جدی با یک تیم نامدار ناکام ماندند!
🇮🇷
پرسپولیس
😏
-
😃
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104590" target="_blank">📅 20:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه دانیال ایری(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104589" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1adda802a.mp4?token=IFrNQj2GIrRA6megOXx_xDGR0u52UvPlgW66FdeAeUFhsG5oU1bnGKnokv9KrVFx_TGNxLKagMQ_haQPhSE0XOZ7oNCG-oeortjtw76wUac42-BXc2Jrv3hanZctXZyq0nuqFxOVrZMAyxfXQEbObRtQXbDj5PzCDx6nktmq48ucCQlsBJgY-xmWY4zVIbUVr47s1ji5iPOgh1T2E4_LSvSREX3x_HeyUNbLXD36E2DMDrOlVWnJG5bVz3deRPwGArssBdgiDutoRNdNCjIufKko_ab3y_sgfuZQsvNhdgQQw-N_tgOpWkYZ8d53HDtAZtTgmwf43k1JfpkSYz6Bkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1adda802a.mp4?token=IFrNQj2GIrRA6megOXx_xDGR0u52UvPlgW66FdeAeUFhsG5oU1bnGKnokv9KrVFx_TGNxLKagMQ_haQPhSE0XOZ7oNCG-oeortjtw76wUac42-BXc2Jrv3hanZctXZyq0nuqFxOVrZMAyxfXQEbObRtQXbDj5PzCDx6nktmq48ucCQlsBJgY-xmWY4zVIbUVr47s1ji5iPOgh1T2E4_LSvSREX3x_HeyUNbLXD36E2DMDrOlVWnJG5bVz3deRPwGArssBdgiDutoRNdNCjIufKko_ab3y_sgfuZQsvNhdgQQw-N_tgOpWkYZ8d53HDtAZtTgmwf43k1JfpkSYz6Bkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه دانیال ایری(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104588" target="_blank">📅 20:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تراکتور زدددد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104587" target="_blank">📅 20:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104586" target="_blank">📅 20:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGKF5Al9WYBQumuPXvnlS4Op3PU7Hg7mNrKI06VzKFp2fINIGHYYX_TFjwT1pXUbZbPQPQN2hGJa0Mw4cvAYkOGtuplajr8pqFDSAon4s2HvH33p46VierXQssnCozuFeHcazXZaczf0jGBYyRz0MnFbT-9zrwAV4idKMG69c1dJSod0o-zg-KSn8HNfJVFmAbImyNLyUPaYbWpF3SlMlNGVpPAyVZdDyOhZ7UmDAX5YaocJLgX5TfCJz6gJ1vzcFPI_qbHkBO_l4dNUwTjzxGnhBdIIrV4iScGaWjudEDaRatgmBdxKj5xpba8ArV7sQALLbchJFmriswkgy2uXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: کودی‌گاکپو ستاره هلندی لیورپول در تیررس منچسترسیتی قرار گرفته و مذاکرات جدی در حال انجامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104585" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حداقل تماشاگرا راه میدادن بازی جذاب میشد
😐
۷۰ دقیقه کسشر خالص از صداوسیما پخش شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104584" target="_blank">📅 20:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇱
بنیامین‌نتانیاهو: در روزهای اخیر ایران تلاش کرد که یکی از اعضای خانواده‌ام را ترور کند که در نهایت ناموفق بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104583" target="_blank">📅 19:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef14eb37a.mp4?token=ADLdk1Am2G0qwKfSLVNEIk-X6ArBuCupCc9umF6jhYp2mcPrzvKQXtmAmuOyD8S3CluHvoZIxoL0uE10nL33yWE_eHNCr5K_FzdPhsTS5VgxaG2EcO24US1ePr-UbmHdaFZcUivbLMON-OB5CjExXXbhe3Uro7oIcN15Kn6HHobBstAYuQINNKmJClugNKsdGIGEvAjuV0lcACL2hpNFhMfr_AqGnXMn_JZimXBufedwkY9IwRVvQ25CU79zyNNUWmws3i8fU1JTOEfiBwz2iRuZ_5XUsWvkWe3IXt8gv9Jfjzrvbh01Ksx5DVkDPJarBUFzr8PKs5_6GBHDazGCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef14eb37a.mp4?token=ADLdk1Am2G0qwKfSLVNEIk-X6ArBuCupCc9umF6jhYp2mcPrzvKQXtmAmuOyD8S3CluHvoZIxoL0uE10nL33yWE_eHNCr5K_FzdPhsTS5VgxaG2EcO24US1ePr-UbmHdaFZcUivbLMON-OB5CjExXXbhe3Uro7oIcN15Kn6HHobBstAYuQINNKmJClugNKsdGIGEvAjuV0lcACL2hpNFhMfr_AqGnXMn_JZimXBufedwkY9IwRVvQ25CU79zyNNUWmws3i8fU1JTOEfiBwz2iRuZ_5XUsWvkWe3IXt8gv9Jfjzrvbh01Ksx5DVkDPJarBUFzr8PKs5_6GBHDazGCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
فرصت‌سوزی پشم‌ریزون امیرحسین حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104582" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f81fa46cd.mp4?token=IfUVu54WV6X4p0XATOl42ZOzbtM5Yyg27TwpHkks9WscD3eSrIXGqd82YB78amxit_hJ9Qx17stWfVJdL0TbazsmhIkGN8lgIdTWDKfpqQXNrzJqPDGPSI6NrQqGB8FQFXc7e1be7JjS36X5i9wMiNH1qhORleXQsniInC08dwdfL4GFDBlWFFX07hu30t4qin1KfO9PXPUlQ2kTJArhQ4C_0l7Y--ZM5VynfLGKxkov3fvoa_AOFzMpgRI8osNeo5w0RBS5MFX6uODvS6NBwkBEiS-YkE9QmAamgE2jL3H2L-kcZsE40N_zGkfgOInPj-SrumnOtxrtvCXZ1Zp8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f81fa46cd.mp4?token=IfUVu54WV6X4p0XATOl42ZOzbtM5Yyg27TwpHkks9WscD3eSrIXGqd82YB78amxit_hJ9Qx17stWfVJdL0TbazsmhIkGN8lgIdTWDKfpqQXNrzJqPDGPSI6NrQqGB8FQFXc7e1be7JjS36X5i9wMiNH1qhORleXQsniInC08dwdfL4GFDBlWFFX07hu30t4qin1KfO9PXPUlQ2kTJArhQ4C_0l7Y--ZM5VynfLGKxkov3fvoa_AOFzMpgRI8osNeo5w0RBS5MFX6uODvS6NBwkBEiS-YkE9QmAamgE2jL3H2L-kcZsE40N_zGkfgOInPj-SrumnOtxrtvCXZ1Zp8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
فرصت‌سوزی پشم‌ریزون علی‌علیپور
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104581" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek-iZmAvQinUuLsUIWcvGtEBwY6HHmob2WZllat4C6XwOqKFG7r9-oid4NuOxfMGR4X4uNGF0FrvuOxq0l3uqym1eydTp_bvROP1XizxG1Wrw0DFvUkPfQbAPAzuAHq6KbwV2o9AV-nLPr3FpeX3Ks2TCzsgouHh-izAZxSf8GOeA4kh936pOExNL_V5M_5f-FW_c2yTbz9za-W9fgMIz0LtUTTtbFX4PhdOuxvuBBsEpN2SoO3n6Iv2Q3j4X_AjmLgEmyfsMVQYV6fmarKc2_vL6vcEuD2Y8WgdjnH1hemQ7weLJ_FZ_lumjYE2tMQANHNZE_xqKE_V5zRi-pBbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
رامین‌رضاییان در ترکیب فولاد خوزستان مقابل نفت‌آبادان با شماره پیراهن 69
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104580" target="_blank">📅 19:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701c8571d2.mp4?token=bJcJkLrl6oeuvQA8NseKUPLbnD_EmblJW-YAjqd7y53ZTZ0e-ILQDpzFZyMFgCfQ0bpuMZNalss5FRdy_hAHwFWaSCf8LWvmL6J7DFGzIXXlMx6ZPTiSiiUUW1beMV9VQCk4IhvuyO197XSNn-sdNuSlNDYSFuRPM5hADTzf7P-XMfntwB_LLQvstiA95khypK3mJChXsSM6tbTLJH2sgHEFATjlq2f2SaMVYr3_lDoVSBCGEYZVh7Yn4juKkhgTRxZk6Z4aH0sdxhnUoGpxNsYtbROC73GlEEhBE6s3jhkdYDZ6w6M_6tF0vARJkIOntvnaaF6Qd9lwSbWC5q3BTHwZD9dO15h6ATrKF6ciXvsMYsgTp9IwdhDsJo1aIRr-nf90RS1Rt7pIGA0z8UX8hxMyqxDIB6WD5prF7MiQfGu2jf6qb5fhxTVdkIgcbqDakAALL5nr67A3GYpFj5nUj7aorRaaBjzppbhbPV4fbwgC_-MRdA3sn960EDG--Tuxc2xGEUbZHVeUtKoVp-lgzEaw5n_TivUDQjNzoGwTXIc-UwJyq9QuUmbFhve7X5W8tuBpvuF0zlLAEWKvlLwPg6F-gRlnJ7gFUI4N8kNEd3ytJx5pXRVeHSo3i0Y0mEt6plzJNJEhexdVO9WcuzL9v3ff-CPHp33gWMAAGg9Lq3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701c8571d2.mp4?token=bJcJkLrl6oeuvQA8NseKUPLbnD_EmblJW-YAjqd7y53ZTZ0e-ILQDpzFZyMFgCfQ0bpuMZNalss5FRdy_hAHwFWaSCf8LWvmL6J7DFGzIXXlMx6ZPTiSiiUUW1beMV9VQCk4IhvuyO197XSNn-sdNuSlNDYSFuRPM5hADTzf7P-XMfntwB_LLQvstiA95khypK3mJChXsSM6tbTLJH2sgHEFATjlq2f2SaMVYr3_lDoVSBCGEYZVh7Yn4juKkhgTRxZk6Z4aH0sdxhnUoGpxNsYtbROC73GlEEhBE6s3jhkdYDZ6w6M_6tF0vARJkIOntvnaaF6Qd9lwSbWC5q3BTHwZD9dO15h6ATrKF6ciXvsMYsgTp9IwdhDsJo1aIRr-nf90RS1Rt7pIGA0z8UX8hxMyqxDIB6WD5prF7MiQfGu2jf6qb5fhxTVdkIgcbqDakAALL5nr67A3GYpFj5nUj7aorRaaBjzppbhbPV4fbwgC_-MRdA3sn960EDG--Tuxc2xGEUbZHVeUtKoVp-lgzEaw5n_TivUDQjNzoGwTXIc-UwJyq9QuUmbFhve7X5W8tuBpvuF0zlLAEWKvlLwPg6F-gRlnJ7gFUI4N8kNEd3ytJx5pXRVeHSo3i0Y0mEt6plzJNJEhexdVO9WcuzL9v3ff-CPHp33gWMAAGg9Lq3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
🇮🇷
خلاصه نیمه اول مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104579" target="_blank">📅 19:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cabf9572.mp4?token=tAJEnGrB4cgFIO0vYeqmpDLbM0UUFa_zlyLvXmA6vox8IkdwWyHPsGbE2YK1hQjkmvDQ1Z_utQscgBbKcK-QBkUm0pbQ3tYFa7QqnGnftFyeUCx5FyT-7vWDp34HQDG2KrynqKuhRM7K4He8h9MElbYGdpFne8hGEkKE-jFGp7s2CI_0r_2wFheICQ6W_c9ICen7Q_u6_WKWLLLigkVJc_alQ8957MDDhtfXwINCsDc32VncBcnFVfgIPs7_T3ZWDsiNIP2LqRCl5koTbWMGk7ngTMCtld3A4g1EvBX9ZRdcM1VFPfoeH41mRjP_eqQ4nhttBEGO6XD5yacUBBAEww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cabf9572.mp4?token=tAJEnGrB4cgFIO0vYeqmpDLbM0UUFa_zlyLvXmA6vox8IkdwWyHPsGbE2YK1hQjkmvDQ1Z_utQscgBbKcK-QBkUm0pbQ3tYFa7QqnGnftFyeUCx5FyT-7vWDp34HQDG2KrynqKuhRM7K4He8h9MElbYGdpFne8hGEkKE-jFGp7s2CI_0r_2wFheICQ6W_c9ICen7Q_u6_WKWLLLigkVJc_alQ8957MDDhtfXwINCsDc32VncBcnFVfgIPs7_T3ZWDsiNIP2LqRCl5koTbWMGk7ngTMCtld3A4g1EvBX9ZRdcM1VFPfoeH41mRjP_eqQ4nhttBEGO6XD5yacUBBAEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مهدی تارتار، سرمربی پرسپولیس پیش از بازی با تراکتور در استادیوم خالی از تماشاگر سهند تبریز، مشغول مترکردن زمین و بررسی چمن استادیوم بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104578" target="_blank">📅 19:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7aIh576-T_GlNsISjb7Dh9weQnwWHtVH0t0RNLItXsO5nm404I90zfY0deKulBRFZuEoGzIADEiWFvh01dYW-xeVwpdwIIIIWLAfPOL9HH_SszTtriwhFtNCW94qELLvI42RFOdgxt8ro5r9EWxdCersfjY3PvXidQnjLzn3c9slEdqEzttlnSc8hPFHWnZFZRNoam6D1P6YoNQXf5PA2KqARN8jbv8Pm1gtRb2_lsSXvNFiz908m7wgk6pCMLzc3Pr24CwjR9zS2X4z3TqMoX5cUC7bmUQG0e96HMVcP1IxPFVzrHKWv8hzaX4UlUE5MWKx-i8BHmL7TF_vFklTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از ESPN :
⚽️
منچستریونایتد فقط به دنبال جذب بالده به صورت قرضی با بند خرید است اما بارسلونا می‌خواهد بالده را با مبلغی حدود ۳۰ تا ۴۰ میلیون یورو به فروش برساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104577" target="_blank">📅 18:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a390435aa.mp4?token=XT-bUKVu2IqHNv2QRFspQhVozzA4c5ObCDcWfxDhthL825CnkLO0QZgGt8yUNsdQ5uPRtAisy2hlgVuBBRrj5u5Gk6uBgwf4mV0FpQhWluVzB9mAMzr581Om-j8sjIyuD3DYzRL_9vvd6ElbPM8EFjIj7HvUWEKQAAVuaQpwFvx-ocYxwrteoQXWNC0XEkXZJi5TMAXnlfoBVD5m2Ea8rND7w9cS7G9040W_MCDcPlBQyOOEt6r4GiWnlxkvjplfIcpUttoaP21y-vFvTFfaweC6ZysSowtz1hqT6YTZpyf3bRLXDybfj47sG2a1Th48EFHZbsK8UQM1ic2lVF_07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a390435aa.mp4?token=XT-bUKVu2IqHNv2QRFspQhVozzA4c5ObCDcWfxDhthL825CnkLO0QZgGt8yUNsdQ5uPRtAisy2hlgVuBBRrj5u5Gk6uBgwf4mV0FpQhWluVzB9mAMzr581Om-j8sjIyuD3DYzRL_9vvd6ElbPM8EFjIj7HvUWEKQAAVuaQpwFvx-ocYxwrteoQXWNC0XEkXZJi5TMAXnlfoBVD5m2Ea8rND7w9cS7G9040W_MCDcPlBQyOOEt6r4GiWnlxkvjplfIcpUttoaP21y-vFvTFfaweC6ZysSowtz1hqT6YTZpyf3bRLXDybfj47sG2a1Th48EFHZbsK8UQM1ic2lVF_07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
خوش و بش گرم بازیکنان پرسپولیس و تراکتور در تونل ورزشگاه یادگار امام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104576" target="_blank">📅 18:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c210be91e5.mp4?token=n1Uukc4WRadDhr7EKPh2fHFD5x5gsDNRwc2ta8V4T7jss9W35TdxaMozvesHqp1ceYra22UaVuAD5vXuMmcy_Jy4yLuWoJoukMtD9NE5gd8XI3SQQqzYFbbpiHgVxJqMHRpddgmA3OJj4OpOHVRYUANlGypHxRC_xsbTT3TLiLuMMbOIfLA42_0RgjSs-zb98gvY95Rpbjl9hjab7zrnHGAIAOqtx674ZY3AYqGQgRRlwVRVa6JUiIjl7aMfqTDi-3O28KZC-7opsOB5G88MeHSF9Wt2Kk2pJ0ml8tL2--ncidczAyASDN6RGRa-2t1Jdzcjq5cSZzcUWkQ0taG_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c210be91e5.mp4?token=n1Uukc4WRadDhr7EKPh2fHFD5x5gsDNRwc2ta8V4T7jss9W35TdxaMozvesHqp1ceYra22UaVuAD5vXuMmcy_Jy4yLuWoJoukMtD9NE5gd8XI3SQQqzYFbbpiHgVxJqMHRpddgmA3OJj4OpOHVRYUANlGypHxRC_xsbTT3TLiLuMMbOIfLA42_0RgjSs-zb98gvY95Rpbjl9hjab7zrnHGAIAOqtx674ZY3AYqGQgRRlwVRVa6JUiIjl7aMfqTDi-3O28KZC-7opsOB5G88MeHSF9Wt2Kk2pJ0ml8tL2--ncidczAyASDN6RGRa-2t1Jdzcjq5cSZzcUWkQ0taG_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
باشگاه پرسپولیس با انتشار این کلیپ در آستانه دیدار با تراکتور نوشت: «ماموریت بعدی کسب سه امتیاز سوم
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104575" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631497f3c1.mp4?token=IHZbdnPb3T5ux9R18CvSG6usBqB38fFmvI5RgFh8r6Jd_ojQrNkGLFsqRINwffPLxU3xptlCHX1fXh9rUbTlseEDOnL-xtoNbEdXg-9IoiUrhh6qFMgTsubSgzClpULu-HgFEtv9_BBcFGnLLnBTxMKgONX2v20XEbRbfH8u4GbuS7MFIj-FrOI65hG-uVmeu4zjXHxsSgFLtgUMKwK_jfQo9MTP1mQpLvGyTaM6YxKy6GknG9_s6NDUpRMlY2mloCGoAW3ZL2lyOu8Kpb3aH-kQQRpKgifh1JmtDgEk7Jvyl2qxWcevFMVY417sjlOIWTRxoaKfywAXwwdkZa0zBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631497f3c1.mp4?token=IHZbdnPb3T5ux9R18CvSG6usBqB38fFmvI5RgFh8r6Jd_ojQrNkGLFsqRINwffPLxU3xptlCHX1fXh9rUbTlseEDOnL-xtoNbEdXg-9IoiUrhh6qFMgTsubSgzClpULu-HgFEtv9_BBcFGnLLnBTxMKgONX2v20XEbRbfH8u4GbuS7MFIj-FrOI65hG-uVmeu4zjXHxsSgFLtgUMKwK_jfQo9MTP1mQpLvGyTaM6YxKy6GknG9_s6NDUpRMlY2mloCGoAW3ZL2lyOu8Kpb3aH-kQQRpKgifh1JmtDgEk7Jvyl2qxWcevFMVY417sjlOIWTRxoaKfywAXwwdkZa0zBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
کمال کامیابی نیا: تراکتور، پرسپولیس ب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104574" target="_blank">📅 17:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏸
🇮🇷
ویدیو باشگاه استقلال از تقابل دیشب با سپاهان و برتری قاطع آبی‌پوشان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104573" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b36813ff.mp4?token=fkOh22avFEmlIx3noev_moRO9Mos9T4vSeeMypJzV28ui9mcKjJ74RyhW81OZdnrZq57CrZNorV9hgDd4n2mbyXsFQaR3daVsG0aUADsAp73vH1r2ogM3AG2NaPOCi3UO6utj8h-81Uxdt_mrfyGY2PpQ980oN6t6F5B3dKTTbUw_EACo-vTSImOHKoFAxDu8BkFauwY95slcKq2n0QU8kvu4gy1V2nkhtCu8buFFzANTDmUFYrJcZiijE7cT5wdB9_YuC_ETNXlEQ378wtJRfgH2Ougch14keZd95Zs8QJHiAoqzWKqvIji09xZKcbfa60fLbM2jtlPjcC-jQoxtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b36813ff.mp4?token=fkOh22avFEmlIx3noev_moRO9Mos9T4vSeeMypJzV28ui9mcKjJ74RyhW81OZdnrZq57CrZNorV9hgDd4n2mbyXsFQaR3daVsG0aUADsAp73vH1r2ogM3AG2NaPOCi3UO6utj8h-81Uxdt_mrfyGY2PpQ980oN6t6F5B3dKTTbUw_EACo-vTSImOHKoFAxDu8BkFauwY95slcKq2n0QU8kvu4gy1V2nkhtCu8buFFzANTDmUFYrJcZiijE7cT5wdB9_YuC_ETNXlEQ378wtJRfgH2Ougch14keZd95Zs8QJHiAoqzWKqvIji09xZKcbfa60fLbM2jtlPjcC-jQoxtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
❌
حرکت فوق‌العاده خشن و جنجالی در لیگ‌فوتبال اندونزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104572" target="_blank">📅 17:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgU5ymiojuuw8hwVH1Tg0sdeLKzC-nnzpKbphy-fyjZtXcevbtksSe8yBQTwCdr6A4h4xBmeKs87EAa1GrQgFUBJEuZnRjvaJbGV5F75nXRz6QzDeXaFD4mwCM_xyrgSj5Bzjdyl6tarZerA25ebt5pzGn1Tbas6kxNF1pzoYFq2dbaQ0A4uUv1uKKx4_NQ6g_GExViRBf-gljbptcmgGiU0fUxj4qzZfj-dNKHkNEJ40SIjzH-8fjDH9mCCppS7AkP0pGo70vP7FAvmwL7OHSjlbQqTsZK77y31DS0CMDKD77rZwXBKF0drptSTCGOoTmzPKrktiuUFvSlrzzSeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته سوم لیگ برتر ایران
🔴
تراکتور
🆚
پرسپولیس
🔴
⏰
ساعت ۱۸:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104571" target="_blank">📅 17:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب پرسپولیس مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104570" target="_blank">📅 17:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDiGE2d_zyr6w2db2ALskVvq7VVgtY2kkXxbv6jm1mIQD98HTcBt3mrY_w-2rFikvbGbSAHbbXLrFu6NPfHD0Opaf6y3RXlE4s49xK8SFvRDw3h9_au7WEKxFMw6i38lzZYbfKwaGBaTQyYVqETdzFPaN2dfeZWvWXIydYdM2HaD89Hbl-FR9_qRRyBs2tzWZlxuCdniFs3Q7ygEdUSPhPp1U3pOLhAL-UUmdmpD61yfv7MaaKrOBtLj5slg-il1BNf_u16Ec3eL5-Uddu53bBtb0ITvXtew12R7jZigeUqgzZj8JSKxjkT67yZ9w2jpeXcbIOa-4GaN_VUAynI-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ترکیب پرسپولیس مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104569" target="_blank">📅 17:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHmDrwjXmISRxy9Dy_9LNjd6z_AiCbhEE-xPRFzmwNHkFgww_Pvcn0-JMNw7t97NuXhXXFFJzDbDOcSwDNz_KMAxAwBi1mVl-PqIk2mdiWW9YTtMxC8tqx6PRhR-_vz8FoKrZWzMFbbPqtUZ_HuUWqPftxT6iNHObqzL4Ga4KA9xm-oqbxYTci1-RO4H40UKDlQMPfe_HPkijadynROwQ0DRJgXGn09ePx4O6mQkfDJB1ZftiFjtmD9G9gh4cQnXLU_QZ1nD3mJTcxBnbE-Af6MWWf5PSrUdqAZvv7qjZBg64aAuS4YEHHqrlWRcAdYt9ZXSBiJA_rnUCu79jb22HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ترکیب پرسپولیس مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104568" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
g2
فرم های ما رو از دست ندید...
⚽
@Tabanii_Mafia
@Tabanii_Mafia
⚽
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104567" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗮𝗯𝗮𝗻𝗶𝗶 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sunJXfE6AlE3x-2EZYCMhgHMYNTpgVXj2e9Rx6KHBJUaf3Y4XmcH3M4DSNdxs_syyMyjoYj9UPwBsYSCNHWKdmnyAlvCukOE3dlb0WJLAyFDVQtDtwDlfmnZ79yH-Rpy6Ob2BBmDKxbp4jL0MgDHio6GnZFWKgP4mjZpBBSqLb7jnodzf7F3TPe7rby63nIUzG3mr9UhKSVp31HrCDG9xTWsFvI43ppwYufINrzqNOsgFFpk_h3z-v0dcYYB3DebxlzYdBDHr086sGrysdf_8256IauMIHzswm08JbcowIMMvH6o4s_E1zONnZHwOjBnpUj8AZNcgZ5nLAXvW1Tzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104566" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVPehYX7cchpwOHBfid5Mj14QvSepmInUrOXBF8dlpGcq6zblFWc0NBjuLhHOrthGzGVnI0LB1cOrQeUJtvLYk_8Gdd33DrGxTDya5oCFea6y5s-kXYKOmYmdPEstPyouV56-sEQw8FeTVOSkCyfndkkkyN-XfMHu8ZJgY6oeARsujb8RqqqmWbeXy5OoZTlZgA3-b5cAS8Y3XPdqlC7bj0ST8J79WrFiux7bACr0kosv6yKP59IZcyhpv7U3M_6xaA8kQsVHYtvg9JopKmJOMLnnRn9bGJ-ld1jPFxYPzHlHPstmftnUZvu82ey6R88AvU3hCg-O36SCRDtwdQ0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب تراکتور برابر پرسپولیس
🔴
علیرضا بیرانوند، شجاع خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و شهریار مغانلو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104565" target="_blank">📅 17:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPE9g7pJ_C9PeS2h0_UBgrh-FEcHi2xAk5ooMGG0XCaNv-XLJZZY9EihWdbUHVvLTMDcvwbKxt2_eQAHVRe-o3QYhgyGGcMabHJ0NmUDqM1w4WAxBBMxqpiOgxUCwy7OwUmpw_iyElyOvXdqVP_QnL6E0aglQD3MS5LY3JVu_P2Z7NBW3FDXYMKqKOU96G8ZUHpL9WuQ2adb3nEUZ3lTPC1m-jOtBqynePGhLkBsiZivF6BzQoPRpLW46Us9DKbNr5SgLer5UCSZ4JDYH_nFkHga_au2s-qTHZUAsIWsLtWa5L-OfQiekNErb8fiKgAr2ANl_aYM97YoOEFUjNSKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚑
🇪🇸
براساس گزارش‌های غیررسمی منابع اسپانیایی، گاوی بدلیل مصدومیت در بازی امشب بارسلونا بین ۴ تا ۶ هفته غایبه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104564" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52484f1b05.mp4?token=OujQhx9T2vgA7vxTPXfdxN1q1q4DUV7KqmMFcnmVO1puTj3UB7wlL61dtUcld7w2iB26JH2i12hEz1XUKZUQ0GgMK_z_5ktZxJEm_MGN2RE2i8WX0xZDlA1JhOJikxIMKkawOlpL4R4sAE6j3Yf3lCkRHhoGhRPUJ9fV6nhpWmzhJKT_ZYYixk937XWCb985PTMBtMP1bq8xpiXZWYunm94MztWvGbRIV5Ttk-FqzUTUF130YQVwGxtvBPChratYXeKcp8SS--IWi8FDg2EMKMZNPlh0yoOkB6YRuKSX9KTG-PrkdoIv4tew84awb3EgtV_dpA86cpo-1veAeYnZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52484f1b05.mp4?token=OujQhx9T2vgA7vxTPXfdxN1q1q4DUV7KqmMFcnmVO1puTj3UB7wlL61dtUcld7w2iB26JH2i12hEz1XUKZUQ0GgMK_z_5ktZxJEm_MGN2RE2i8WX0xZDlA1JhOJikxIMKkawOlpL4R4sAE6j3Yf3lCkRHhoGhRPUJ9fV6nhpWmzhJKT_ZYYixk937XWCb985PTMBtMP1bq8xpiXZWYunm94MztWvGbRIV5Ttk-FqzUTUF130YQVwGxtvBPChratYXeKcp8SS--IWi8FDg2EMKMZNPlh0yoOkB6YRuKSX9KTG-PrkdoIv4tew84awb3EgtV_dpA86cpo-1veAeYnZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب گواردیولا و زلاتان به مدل موی جدید هالند
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104563" target="_blank">📅 16:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00fe39bb.mp4?token=IsX4h9gH1XT_E2FWDyDB48k3wd5YMikJPYkPtJKwjDYKKYyLucGjYqqBTHk0SardW9tDFYUTJGRHhGKd-URtKxXAb294_OhqRYwmw6tg8Nrx4a3o9osTLo9oiqhZYexE4gEXcErYIOpBxBydd7bTgsbNntdq6v_B3ruURMMUcomqdwL-haQIh3hIev81U7Cogy93NfKhSgkVwZTwU2rKxn5Ry0QX8HnKdxZ-lS63rADkPh-PHP36qdm9qsYnxU8jw4K7a89urHJSn-o5Qq8SfPAlAD_HMHtdFdVHsrGRONAqJBB4Dhszr4bKBNkQ6exlnxTLhisZe4KTu3Xz2ygkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00fe39bb.mp4?token=IsX4h9gH1XT_E2FWDyDB48k3wd5YMikJPYkPtJKwjDYKKYyLucGjYqqBTHk0SardW9tDFYUTJGRHhGKd-URtKxXAb294_OhqRYwmw6tg8Nrx4a3o9osTLo9oiqhZYexE4gEXcErYIOpBxBydd7bTgsbNntdq6v_B3ruURMMUcomqdwL-haQIh3hIev81U7Cogy93NfKhSgkVwZTwU2rKxn5Ry0QX8HnKdxZ-lS63rADkPh-PHP36qdm9qsYnxU8jw4K7a89urHJSn-o5Qq8SfPAlAD_HMHtdFdVHsrGRONAqJBB4Dhszr4bKBNkQ6exlnxTLhisZe4KTu3Xz2ygkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فصل جدید اروپا، سیس جدید بازیکنان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104562" target="_blank">📅 16:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb95f2a544.mp4?token=LJLxDr9pd77vcJlVgQ4nCisd-UCDSlOqpKHXvnpqFDydvRA-WZnWmOl3LceioKOpOUNlP9-zVPdBJhbDYxFhM9ay8jFgpsBtqemachfDga7RQN9OoWS3iFVIlW_Q1ZM15gJVjUV-3_DNgiOuILaSf7CvyJmouiloCB5LUS_-TLG8C1g2D_lpyZoNasUkoUCVFBaYhq8LPlWlixFJlb7nzeHWbXUM0RiJMjAgviYJX5SdDnUVbcTs0ghAyLLzDjzet19hbDiF4C1ldLK8Mmlq_bQKYRKrOybhB4xIcjP8vgvQFvobIACbRw-52Pqkwe2OTWF_PHWOxLlxEyRQ5LA2kZczJfU9XVn1bRtlPUOrJfOAdaEeMhNX0eD1K99P92aUJQvoAF4FtxKiJce7uMj95jvlYOG64iqGfri0--o8qH90lhOxWSTSp3QwU_aFMQ8v71QW4Lgd_RC5cCpukw6Jo2n4baSYf8gDru1Z5DpStw9NKoatk6lHIWUFR70ZCQYEUaRwlFHOHth2y2MSW3acMHCgPcG7TQ5WhJJLgTR1JHnlwcy7i8ClXQLRq_9pk5ykcz8o5S12a_66pVRBUHye_U3Cf2G70Iaagr7YsOSQo7zK9m5b2l6tDzPf68NMKFB8hKq1nUb7tDslE2xPozneQ7vp4_xQ0GFhURDTdJM7Ays" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb95f2a544.mp4?token=LJLxDr9pd77vcJlVgQ4nCisd-UCDSlOqpKHXvnpqFDydvRA-WZnWmOl3LceioKOpOUNlP9-zVPdBJhbDYxFhM9ay8jFgpsBtqemachfDga7RQN9OoWS3iFVIlW_Q1ZM15gJVjUV-3_DNgiOuILaSf7CvyJmouiloCB5LUS_-TLG8C1g2D_lpyZoNasUkoUCVFBaYhq8LPlWlixFJlb7nzeHWbXUM0RiJMjAgviYJX5SdDnUVbcTs0ghAyLLzDjzet19hbDiF4C1ldLK8Mmlq_bQKYRKrOybhB4xIcjP8vgvQFvobIACbRw-52Pqkwe2OTWF_PHWOxLlxEyRQ5LA2kZczJfU9XVn1bRtlPUOrJfOAdaEeMhNX0eD1K99P92aUJQvoAF4FtxKiJce7uMj95jvlYOG64iqGfri0--o8qH90lhOxWSTSp3QwU_aFMQ8v71QW4Lgd_RC5cCpukw6Jo2n4baSYf8gDru1Z5DpStw9NKoatk6lHIWUFR70ZCQYEUaRwlFHOHth2y2MSW3acMHCgPcG7TQ5WhJJLgTR1JHnlwcy7i8ClXQLRq_9pk5ykcz8o5S12a_66pVRBUHye_U3Cf2G70Iaagr7YsOSQo7zK9m5b2l6tDzPf68NMKFB8hKq1nUb7tDslE2xPozneQ7vp4_xQ0GFhURDTdJM7Ays" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری پشم‌ریزون از پیشنهادهای سایت شرط‌‌بندی به حنیف قبل از دربی؛ ۲میلیون دلار در ازای اخراج در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104561" target="_blank">📅 16:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b661cf3a6.mp4?token=io5RSoZ2KtrqD9lx4aY7cV-x3jW7Ih7QbE6u3Eb65_24vy9NIoGv4hBIDf0651V2468PsLmmkZWwuZtSY5bsRPA-FuD21f0LasDqNYCEIWuhTMcnNnKurBq_yw3S8hVlh3pm4BPtZSEahME_CCT8mWRPHW_G2bbRGLPnc78c1Jwfsk7YRgV6Nmzd7rHqkrFAOKNAxhEJcfzcvADcM3_e-LkjkuOA8Z9L_SJhs8IaNHyZ3UgIe3jbILg77PiiT51Ofg1fvlKGwlzQOAaEcGgy4UVsG58ZxAhAriZPK6S-XkztCaQ5t7xMPD_OsUY5LYrhSpUrxJW5bUFEwq3ehqrU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b661cf3a6.mp4?token=io5RSoZ2KtrqD9lx4aY7cV-x3jW7Ih7QbE6u3Eb65_24vy9NIoGv4hBIDf0651V2468PsLmmkZWwuZtSY5bsRPA-FuD21f0LasDqNYCEIWuhTMcnNnKurBq_yw3S8hVlh3pm4BPtZSEahME_CCT8mWRPHW_G2bbRGLPnc78c1Jwfsk7YRgV6Nmzd7rHqkrFAOKNAxhEJcfzcvADcM3_e-LkjkuOA8Z9L_SJhs8IaNHyZ3UgIe3jbILg77PiiT51Ofg1fvlKGwlzQOAaEcGgy4UVsG58ZxAhAriZPK6S-XkztCaQ5t7xMPD_OsUY5LYrhSpUrxJW5bUFEwq3ehqrU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحبت‌های مارسکا پس از بازی دیروز که نشون میده به دنبال جذب یه رودری جدید میگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104560" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES5PHTEMaQ43aXAPPyXOA4RMC6yYXt0LRADCIBeuFwsSC1bcShfbmGttP98TgffoDV8U40G9kIPfjXAVf6oxOGnKVZ51RfDUtHrV_2q8PMdUGPyZovR2A9q-mO6WvAcAZDwPBq8VRBsEwpWvkB0cYPQLBZVh1LYoYEChe50yZiBIk3gnIaE7Eq_bHto0WneHpuHmdaqVkCMnUnMNxIaszlC_bdkGZkFayZY_Shb1Mk2MNthB0cmN4Jk1IwEKQotC1ZvT1o_FB-uwEsbZFp5GQoXjFgrLG5fatFHNqClhohmt5Lu9M2N-l3KgpZGeiYk9Jg9AuIynHrDIKIbt3_i1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
ریدمان‌های اخیر اینترمیامی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104559" target="_blank">📅 15:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33aa33566a.mp4?token=kwD0881kVe1eScmrcoK6X9WuTbDLwmYfVwkkti6WbnS4K87YFTh6mlt1Z6fJdntvwZXtCYWqhz4I3kz0aHJbUHQHBkdvT7o6Q7uPgc0BBlS0TmfOpjdmaCcC_7xgzDHtAv7lj_Fm3ymsADcOUf_XuKiVZhNAsMkN-1_zZYW8xl58jXDH3-Sz0u2IdFsPSYuDJcQA2hhrK-x0zM5fpvHqmA1YNbiGvGGav3Ee49EgNB4im3pIgg3h7XfjI1AtUeKbBGVR7jf6MhZMtrKg3NN9b6Fr8xVo9HmZMDczYPj6cg0ZcFaEYG5U4oSgzJbZ_JqEDg36eZitw1s2SFLP110aOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33aa33566a.mp4?token=kwD0881kVe1eScmrcoK6X9WuTbDLwmYfVwkkti6WbnS4K87YFTh6mlt1Z6fJdntvwZXtCYWqhz4I3kz0aHJbUHQHBkdvT7o6Q7uPgc0BBlS0TmfOpjdmaCcC_7xgzDHtAv7lj_Fm3ymsADcOUf_XuKiVZhNAsMkN-1_zZYW8xl58jXDH3-Sz0u2IdFsPSYuDJcQA2hhrK-x0zM5fpvHqmA1YNbiGvGGav3Ee49EgNB4im3pIgg3h7XfjI1AtUeKbBGVR7jf6MhZMtrKg3NN9b6Fr8xVo9HmZMDczYPj6cg0ZcFaEYG5U4oSgzJbZ_JqEDg36eZitw1s2SFLP110aOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال مادرید خوسلوی جدیدش رو پیدا کرد.
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104558" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f93ddeaf.mp4?token=Vcv8j8HZaZ_JMAEms1lgIF9our4Imf3Tn237al0NfOA8Glxnf6uzv6jQvRHVqMvQP-q-U7kq0ZTQka57qj3QM2m31Ibiq3e5XHOe6ZUsVwDVrT-UDdJzBqYLw1LzZDNYhZ1urQpErA-WZi-s1ibmymJI5LLYKZjXa4QRVFU2w-B3TWmPCgAdO_to4esPxHsepeeDsoV5HnhtmQ4iNpaJ3F3AzxAZ6kykVV_D_6JHEFglVapWs02W06NTGt1YZUbxZXsl8arXTCgJWA1km8XX4cwo92Y938jaHEfoeTxXseJ03jiN22JK69wQRdgbv8TiKSojLZLB5Ody5iQvq_iyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f93ddeaf.mp4?token=Vcv8j8HZaZ_JMAEms1lgIF9our4Imf3Tn237al0NfOA8Glxnf6uzv6jQvRHVqMvQP-q-U7kq0ZTQka57qj3QM2m31Ibiq3e5XHOe6ZUsVwDVrT-UDdJzBqYLw1LzZDNYhZ1urQpErA-WZi-s1ibmymJI5LLYKZjXa4QRVFU2w-B3TWmPCgAdO_to4esPxHsepeeDsoV5HnhtmQ4iNpaJ3F3AzxAZ6kykVV_D_6JHEFglVapWs02W06NTGt1YZUbxZXsl8arXTCgJWA1km8XX4cwo92Y938jaHEfoeTxXseJ03jiN22JK69wQRdgbv8TiKSojLZLB5Ody5iQvq_iyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
عملکرد فوق ریدمان لامین‌یامال مقابل الچه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104557" target="_blank">📅 14:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c68f89986.mp4?token=bKwQCCuLfh1O6jyWZ1MiWPPGIMPWZsTZ-ReM6Bpb8Oj7y8UJGSrlU0GS-B0MHNjm1tjV1Cgy6DpoYVhx-IClEXtisncOmZMHg2Cn-u4odWCe5_2ZUBI9-tGlxlIgBTwBorA-M24h1Ae6sIBmr5eBOcyba4-n_YeYNyYnH4t39qOBl-q-mPLoZk7G33HJBph7iJG7AbajgblFk5GM-agOsXwzwAXdA6YVNh4nTQnTavvTE-XhbHL5j3id9khkRXYpdFSRIeVycn2YVaW53MGDZCj5iDHWYnPaZESmX_tLLz9Q2CAfT7bglZzpU8wHRZAftnW2eFom1hkTZ9teZV2OEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c68f89986.mp4?token=bKwQCCuLfh1O6jyWZ1MiWPPGIMPWZsTZ-ReM6Bpb8Oj7y8UJGSrlU0GS-B0MHNjm1tjV1Cgy6DpoYVhx-IClEXtisncOmZMHg2Cn-u4odWCe5_2ZUBI9-tGlxlIgBTwBorA-M24h1Ae6sIBmr5eBOcyba4-n_YeYNyYnH4t39qOBl-q-mPLoZk7G33HJBph7iJG7AbajgblFk5GM-agOsXwzwAXdA6YVNh4nTQnTavvTE-XhbHL5j3id9khkRXYpdFSRIeVycn2YVaW53MGDZCj5iDHWYnPaZESmX_tLLz9Q2CAfT7bglZzpU8wHRZAftnW2eFom1hkTZ9teZV2OEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تفاوت اعتراض رئال مادرید و بارسلونا از نگاه خاویر تباس رئیس لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104556" target="_blank">📅 14:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLhUEjlEQ1rcz1Vw1Qqi-59bfHXDrir-b-K4ug-2EZIpoej3rnv3ASfvkRza6Zf8eCUFLYhC2fCDU9h42vf5GSSs05uE7c-TKHKdgzOak0YCml0_lyMb6J9LB1hIz3xxEGVzNPQIN54Li2CwGQeVgxPxNGgpP65MA6wBN4FLrEMipUtDWvVqeFhHe1DbSxiwrojdUFuabAHEIOowKwXvNF2fAsanX2JkpfxZX_S8GnYIzPZtf7cQy-QGnZUPDun2AxS33JMkK2kWbvoYjUedTkWJ3qINeRY2WQvxiQSku2ZNaBmFVJfoMTR-952gV7qktNCbFX251CtnB2e7RO10Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سانسور ستاره لوگو باشگاه پرسپولیس در پوستر اعلامی باشگاه استقلال برای سه‌بازی آینده آبی‌پوشان پایتخت در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104555" target="_blank">📅 14:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8db78c81.mp4?token=RcL9QEAOysCZYJ-StV3n0VC128wigFVJajQUWEG6UpD2rt5P5LcfEJuaWpEVpDkBaFuI4_dq5eOOHE-5U80xlF-ZBHUWHwlb7IF3J2NFcV4WcFe1vKNt7n2609n476FTmB2fkhz0R9JqZOrx_FMPSatsi3g6qn2OaRn5SzDL0uJEyuezEtejg-6EIagmxi2WvzDQkeosKqbz6a9NXlp3iVcZcoFV0fHy12U2GEmEoT0VU1s3ZoIWwjeMMCgBj9h9R9XxHiCo0sTJ1o1SJtibmF-OQ6OYY3w8NWUyQy9Q6ikZPCv4pLm1wVbdKIRv_a3nqdIe2S8OImoQjubAzdF0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8db78c81.mp4?token=RcL9QEAOysCZYJ-StV3n0VC128wigFVJajQUWEG6UpD2rt5P5LcfEJuaWpEVpDkBaFuI4_dq5eOOHE-5U80xlF-ZBHUWHwlb7IF3J2NFcV4WcFe1vKNt7n2609n476FTmB2fkhz0R9JqZOrx_FMPSatsi3g6qn2OaRn5SzDL0uJEyuezEtejg-6EIagmxi2WvzDQkeosKqbz6a9NXlp3iVcZcoFV0fHy12U2GEmEoT0VU1s3ZoIWwjeMMCgBj9h9R9XxHiCo0sTJ1o1SJtibmF-OQ6OYY3w8NWUyQy9Q6ikZPCv4pLm1wVbdKIRv_a3nqdIe2S8OImoQjubAzdF0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هوادار ایرانی رئال‌مادرید بعد اولین بردشون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104554" target="_blank">📅 14:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7eelrN8mRfzjn01nCLQapAdMi-SuxrQulQASd9ZIJVBImC9z15wrROZF8XGd1ZKwI5-0o9AiDgN-KTiw1c6Y6wUAAh7axUcNSgzHJ4_qZG7Uo9NEdW9ahyJu6qc6gINRR54xKH-2K5ShsePZZ3mjlPr9kmyWUnuBoWzqWiA72LsiQD3HXxdxEXvU6hjGUgmBRnUikGSqjJYF4aX4P7MnBYfG4aeTBgElHMKXEsmBVh__IosF55dryQueeullhpU--mdVvja4Z7bBBNiFgORdGURXxj6fDOSqgkBwXyhOJcK5eaVMR5WsdC0A-VrYHI0IGkvIbDBimxPQZtjnbhzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔻
بیلدآلمان: باشگاه بارسلونا پرونده جذب احتمالی سرهو گیراسی مهاجم دورتمند را بدلیل دستمزد بالای این بازیکن منتفی می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104553" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=ca4iS1_YLX6VQkYRdLv1Tt0V7WfTUfgenjxSrV4xOq5s1DwQiYR6EQgabtq5dXOIqHXAZ9cAYOj_TXbpgV3TZjqQrIS7usIX4HjyfJHO4RTWdC_YXLJHx3cT28hbhpiKC6RyPNznwDAL3J38BLYAIMwahVqCmSj_cd1hfRcNpm-58ActdtnItFr2yrbyDb38KilNgb7govrL28tO002aIrkEashVvyoe-uKEPNM70K2GoHszQdqlkF9IuWyDvohBprjM1L4d-7rv-viiRemyCtTnOzKvTbbOaW1EYvDVWw-0puANA3A00jMHw48IDSTQnYxot8lrK8QVdfL6uwNSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=ca4iS1_YLX6VQkYRdLv1Tt0V7WfTUfgenjxSrV4xOq5s1DwQiYR6EQgabtq5dXOIqHXAZ9cAYOj_TXbpgV3TZjqQrIS7usIX4HjyfJHO4RTWdC_YXLJHx3cT28hbhpiKC6RyPNznwDAL3J38BLYAIMwahVqCmSj_cd1hfRcNpm-58ActdtnItFr2yrbyDb38KilNgb7govrL28tO002aIrkEashVvyoe-uKEPNM70K2GoHszQdqlkF9IuWyDvohBprjM1L4d-7rv-viiRemyCtTnOzKvTbbOaW1EYvDVWw-0puANA3A00jMHw48IDSTQnYxot8lrK8QVdfL6uwNSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
‼️
🇺🇸
پرچم تکان دادن عجیب و غریب ترامپ برای استارت یک مسابقه در واشنگتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104552" target="_blank">📅 13:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a81219a5.mp4?token=nSbbll0vA3OjiDmKA-cM5hApP7M55l2YeyPIhGxsAxMIoZ-PfNjBQeCKI5iR0unUGqheX5L-mA1VRSVZl11ff0Iq_c3SSt9bhBhVYawZOIsafgiaTLBKofDvYS7A0bUUyjzCzBBIfnQ4dNqHdlc4tGtNNj9OmIOPoZ8V-IjEpSmui0p7wKM8eMxqBxP6Nr-bw0eCasloDxJjGDAnwJ88kqsBiVklvnGBQuwfC3PJlddwPbtKqOI3NQMMxRKobSEVvWBjmdGpLEjInhX4DkYlwiBYwQp_9u24wYGShQGtHdXc2mPetO3FgWgiwUhX_q840aXKLQpHsfzkxF7ImxI_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a81219a5.mp4?token=nSbbll0vA3OjiDmKA-cM5hApP7M55l2YeyPIhGxsAxMIoZ-PfNjBQeCKI5iR0unUGqheX5L-mA1VRSVZl11ff0Iq_c3SSt9bhBhVYawZOIsafgiaTLBKofDvYS7A0bUUyjzCzBBIfnQ4dNqHdlc4tGtNNj9OmIOPoZ8V-IjEpSmui0p7wKM8eMxqBxP6Nr-bw0eCasloDxJjGDAnwJ88kqsBiVklvnGBQuwfC3PJlddwPbtKqOI3NQMMxRKobSEVvWBjmdGpLEjInhX4DkYlwiBYwQp_9u24wYGShQGtHdXc2mPetO3FgWgiwUhX_q840aXKLQpHsfzkxF7ImxI_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
زمانی که رائفی‌پور (آذرماه ۱۳۹۸) این صحبت‌های مضحک را بیان کرد، قیمت دلار حدود ۱۳ هزار تومان بود و حالا ۲ شهریور ۱۴۰۵ قیمت دلار از ۲۰۰ هزار تومان نیز عبور کرده است! یعنی بیش از ۱۵ برابر شده ..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104551" target="_blank">📅 13:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3040879b.mp4?token=UIfk5xyMiE2ry5cgMOqEWjURhZtfqSPC4mICrlHCHDvJcQsalM0EnPkyKKU6CX5UiRHoxW7HK--Aw8gwnR6lL1Vw54KI5KwGI2o-hv4n6UjUh9C1J1lzuhYuCjxAVsgak4so0GGt4Zi1iSKvNiwyvW6NtSQaH4wcZe7Zp1s2b4BvpI5KZ11LlGRYpM0hajmQ83q1zLB4gpKnoF4RkIrMWU4qBCJQOzHfDSK_PZWfO6sz7TQdVqmMhs_xsIwH_s5eH8SORH-d9_VnnZLvW_y0PGP4SGXQAf9uxwTmwIzigVROhmPCC0lB-o4zeT-WM5B5cw2dg0gzWYnRRs1_YJYO8yAyVlKfAbbH61DVrLuS3NaMeRQR3emsJ95eRmveLWYRN_r1i_FVv4GEzwj-4tsfhcOWZ5Y7JwvfQLFNhIwxJE8Nz3DU5p0yLCDxUgOwR-Wlpl1nOV4hQbLgRCZ8f_n_fiOpEqSp_2xeHn-E6N7ted-pNfb-040hJWEaF0hEvS-pu-ZbIy-Ju5n6B1w_2uHSULhcxB7bCRQG0UkHbR7Kl1BFMyT8hmasP4DJvVPM44tSrbB21uK8ZY5tDhfpXVLuW21WaQNheJDsyVL3DAMuKHROlMiQuRgsHyPG55qOpRWZ9fRmG4RKR-GBYGt8SDsQ3KiX0-o36Na-NMDyYm6mzB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3040879b.mp4?token=UIfk5xyMiE2ry5cgMOqEWjURhZtfqSPC4mICrlHCHDvJcQsalM0EnPkyKKU6CX5UiRHoxW7HK--Aw8gwnR6lL1Vw54KI5KwGI2o-hv4n6UjUh9C1J1lzuhYuCjxAVsgak4so0GGt4Zi1iSKvNiwyvW6NtSQaH4wcZe7Zp1s2b4BvpI5KZ11LlGRYpM0hajmQ83q1zLB4gpKnoF4RkIrMWU4qBCJQOzHfDSK_PZWfO6sz7TQdVqmMhs_xsIwH_s5eH8SORH-d9_VnnZLvW_y0PGP4SGXQAf9uxwTmwIzigVROhmPCC0lB-o4zeT-WM5B5cw2dg0gzWYnRRs1_YJYO8yAyVlKfAbbH61DVrLuS3NaMeRQR3emsJ95eRmveLWYRN_r1i_FVv4GEzwj-4tsfhcOWZ5Y7JwvfQLFNhIwxJE8Nz3DU5p0yLCDxUgOwR-Wlpl1nOV4hQbLgRCZ8f_n_fiOpEqSp_2xeHn-E6N7ted-pNfb-040hJWEaF0hEvS-pu-ZbIy-Ju5n6B1w_2uHSULhcxB7bCRQG0UkHbR7Kl1BFMyT8hmasP4DJvVPM44tSrbB21uK8ZY5tDhfpXVLuW21WaQNheJDsyVL3DAMuKHROlMiQuRgsHyPG55qOpRWZ9fRmG4RKR-GBYGt8SDsQ3KiX0-o36Na-NMDyYm6mzB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
🔥
سوپرگل پشم‌ریزون نامزد پوشکاش در بازی بامداد امروز در لیگ MLS
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104550" target="_blank">📅 13:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fdf775f7.mp4?token=QO-kKd8fjRXWTkO3ERmoBvxCRDsDNr0Yu-mnn74BW7BDAH_fzJ4nTzDIgW297TX9njq-UUmrcX3BjgsdtxlqgW2ro6flm7kkL6QLWCWcTaJeZ7Aa6KPkMlSnBSuGdYMqqv3HfYb4EZV46pJJnIsHORqy559d3pJUV8RbiM7C3P1HcAY5pYqB_tx3YGH3y6oHngeOoSwaelkDGMe9YlHbSBeS5MxJ18G4v6hfBu0a7uflHRCIM1sDJ-cshX8dvrRFoELMNWed3FNjwvqMC_kU_CpMLZyh2npTRb7lh2ug14GPJoOp5M5Iw_N6r0pb-7MDBGlC4y-H9ce8mrp5Mt0sGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fdf775f7.mp4?token=QO-kKd8fjRXWTkO3ERmoBvxCRDsDNr0Yu-mnn74BW7BDAH_fzJ4nTzDIgW297TX9njq-UUmrcX3BjgsdtxlqgW2ro6flm7kkL6QLWCWcTaJeZ7Aa6KPkMlSnBSuGdYMqqv3HfYb4EZV46pJJnIsHORqy559d3pJUV8RbiM7C3P1HcAY5pYqB_tx3YGH3y6oHngeOoSwaelkDGMe9YlHbSBeS5MxJ18G4v6hfBu0a7uflHRCIM1sDJ-cshX8dvrRFoELMNWed3FNjwvqMC_kU_CpMLZyh2npTRb7lh2ug14GPJoOp5M5Iw_N6r0pb-7MDBGlC4y-H9ce8mrp5Mt0sGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دومینیک سوبوسلای درباره بازی دیروز:
«صدای سوت داور را اصلاً نشنیدم؛ مجبور شدم کاملاً به او نگاه کنم تا ببینم اجازه حرکت دارم یا نه. در تمرینات پیش‌فصل روی پنالتی زدن تمرینات خیلی زیادی داشتم.
وقتی ۵۰ هزار نفر هوادار حریف علیه تو سوت میزنند، حتی صدای خودت را هم نمی‌شنوی! اما دقیقاً به خاطر همین چیزهاست که ما عاشق فوتبال هستیم؛ به خاطر همین است که من عاشق فوتبالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104549" target="_blank">📅 13:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
❌
🇮🇷
رستم‌آشورماتوف که در پایان بازی با لنگیدن از ورزشگاه خارج شد، مشکلی برای بازی بعدی استقلال مقابل فولاد خوزستان ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104548" target="_blank">📅 13:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
صحبت‌های جالب و شنیدنی نوید استاد‌رحیمی درباره فوتبال این‌روزهای پرسپولیس تارتار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104547" target="_blank">📅 12:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37beb95f52.mp4?token=cB2J7eRQ22Q1RSCXW7GsDuGCe37FtMiFWHr9ddJLn6XtMAi5NonuCFKkiNaAc4yd-WVMCfTzczSNOFv43DW49TI3aS9OWOvTQ8gBGsalzojV1rg6MMLlCDETGgvd7PQcUzUxKa9isyl2cgbeDeNBlUN2IzPZKLSgg6m6QoYUb9Q9Il07ra70FvaGsfSIeSLYpkywish7Q7dtAV7HtKNfkaywyZ7yoLy4MR6BFl4od_Tf8D_4LhbsKen-jkpFtGuo8xokmfsXe2Ih0pdRibqHH2SFybZp-cvIdjhco7w31-TixGZkHrnn8zTT6-VuLx9LYYzeP-hpDQDU2DPXGEOs-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37beb95f52.mp4?token=cB2J7eRQ22Q1RSCXW7GsDuGCe37FtMiFWHr9ddJLn6XtMAi5NonuCFKkiNaAc4yd-WVMCfTzczSNOFv43DW49TI3aS9OWOvTQ8gBGsalzojV1rg6MMLlCDETGgvd7PQcUzUxKa9isyl2cgbeDeNBlUN2IzPZKLSgg6m6QoYUb9Q9Il07ra70FvaGsfSIeSLYpkywish7Q7dtAV7HtKNfkaywyZ7yoLy4MR6BFl4od_Tf8D_4LhbsKen-jkpFtGuo8xokmfsXe2Ih0pdRibqHH2SFybZp-cvIdjhco7w31-TixGZkHrnn8zTT6-VuLx9LYYzeP-hpDQDU2DPXGEOs-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقابت فوق‌سمی و جالب فوتبال در مسابقات جهانی ربات‌های انسان نما در چین
😂
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104546" target="_blank">📅 12:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900aee1af2.mp4?token=pznOqPl7UydBCGPBSdvhDN9AWTu7lc2iBqPw5_aIoVhtick972pCAfv6yd1LiSiLq8GdWqzccdWg7nWQVjX8LrN2OTs3DAPKgBSfK9Z8fgMxenvuGANd3pQgWc7reD935WAb8nQS02CwUVh86Igx4cS8YDoE6aRO3xpZ2GaF_dAVuD_3TkNLwXcPX0GmdGogoIp3h18K9OlMzxw6CXsaPZ8od_6MkzLdWiDb9S8liE9gyanuZrnHhXOkkPKEeS2oEJMUrITuMf1KqbrtqmMpixCGUPENNL0oXrdlATrp1fEx5-MBy74r06hQJQVULelmWaTPmFrb6TMFQLWYn3dINw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900aee1af2.mp4?token=pznOqPl7UydBCGPBSdvhDN9AWTu7lc2iBqPw5_aIoVhtick972pCAfv6yd1LiSiLq8GdWqzccdWg7nWQVjX8LrN2OTs3DAPKgBSfK9Z8fgMxenvuGANd3pQgWc7reD935WAb8nQS02CwUVh86Igx4cS8YDoE6aRO3xpZ2GaF_dAVuD_3TkNLwXcPX0GmdGogoIp3h18K9OlMzxw6CXsaPZ8od_6MkzLdWiDb9S8liE9gyanuZrnHhXOkkPKEeS2oEJMUrITuMf1KqbrtqmMpixCGUPENNL0oXrdlATrp1fEx5-MBy74r06hQJQVULelmWaTPmFrb6TMFQLWYn3dINw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
نگاه خشمگین امیر عرب براقی، داور بازی حساس امروز به شعار یک هوادار در فرودگاه تبریز که او را داور پرسپولیسی خطاب میکند!⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104545" target="_blank">📅 11:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1r1Z7odJBT65KJmXcVUyyoQdqc2h2d_chhfx-Kdz6lTBbX1-BgU7MudhS_vj4TSELboZPcXBwI_qDSg7orztgKCBxwNZWmhmhaGstdKet7lXGZnj9Pd3KK308d5pQXH3SwO8JwAisK2P71ZucHOfQHp-bhtnqcfKtD9NT05jy8Sa-OHVBIIPtxOzPK1EH82mGBMRceagcd9cuq_VqlAQrvd3OUryG-lQd6qOrkaYcuYIzaM7hod4ZX9Td84HshJyrnMwpwWu12UAOoEHY4SNd1FM5LepFEaVVbO403JNNL3IWX0MamoMi5BUD3V_2fWTqxiZhXPxULYaDFvSbniEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
آخرین قیمت طلا و دلار و سکه در بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104544" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pos1S3OeVDeSA_XL_74Sp6sBuy889fh9Ado5FBI81gBEDd_BRB4iCcBlfJVVFqtwICqTHjioLib735TCEJ4iFnMGbgMYz83raKKihH_XBB3xeVibBQTHWixmxvemxEFkfVnXSvdoxHeXrVOyMow_Bjwm7XkHPuktIo5tB-bqCkxs8GLTsy5bMe7gBTcpcfmbmPFEskRBS5TRXKYh4vqqIWhKn-nbEmTJoQc04d_S0vowgggYvIWrM_vlKclfi4XgBPEJj9QOqlQJQh--_97bl3-EXDGZXQWmmISWDiPkzy496gzE2fY41X3NfiuNOkgGyVT7olyRe-2nB9TksRNS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
#فوووووری
از The Athletic:
⚠️
یک منبع نزدیک به مدیریت اتلتیکو به ما گفته اتلتیکو فقط در صورت پیشنهاد ۱۵۰ میلیون یورویی از آرسنال حاضر است آلوارز را بفروشد. خود بازیکن علاقه‌ای به آرسنال ندارد و فقط می‌خواهد به بارسلونا برود.
‼️
در اتلتیکو اتفاقات دیروز در واندا متروپولیتانو را «یک مسخره‌بازی» توصیف می‌کنند و امیدوارند بازار نقل‌وانتقالات هرچه زودتر تمام شود. منابع بارسلونا می‌گویند همچنان شرایط خولیان را زیر نظر دارند و آماده‌اند تا آخرین لحظه پنجره نقل‌وانتقالات منتظر بمانند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104543" target="_blank">📅 11:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m90J2h2yg9zsfOg_9rwcLCgyMxQFb7hYYp3rjmXZInc6nXqiwKNJgp7lTk_4JcNqeX1PT_A9P5rwh9V5MxjOHxR1PVyziByYIy5m1-lxSKIbzRfKrfdm-og9eEPfvPlHwDEYA9GT627p2QgFTGjGqAG9SwSUXoMA9N6pOmgnfrbohE2bd4l4lJxCMdZQO7TW3M-YAS9A_Wgx8KZv_XvMgl_lbhWajLx16SWSPVUGu3nRCy4JkNLzUERKwFVxyIeO221Ga0qK5-DLldTLklku8Z8zEWamsMfUU4Y6Ds8FhTt7KmUSnOS0OEfdcFC7a5cMvY248xxK_PaINAt-kCFBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سانسور ستاره لوگو باشگاه پرسپولیس در پوستر اعلامی باشگاه استقلال برای سه‌بازی آینده آبی‌پوشان پایتخت در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104542" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmudH6m4ZAz1WEjQCViJd24Q3lPe2AP3eog2cxcvW1mZrH3z_FFUinl4MjcGCTSqegoP-lvv8HHzCvVl8Z0RSjxLnFnGDaLljAEZuki_jOqC-orPyMrrhBZoNwazjvuME1KKRpGaVGOZsDQJqHSu-AHcfzFaaupH6GYebrkKWamMDHsXAN98jokpezURq1D4O9VoSjOzhcu3cgF0n3JiJD5TKrDkzjwmuZ6xQ8SzH6fTgkcJZK4yikrU9C6I3fZkEjVFmlMCidsi6XCqIH9VZBu07eKsenBSaMEdxNhCL-Qca_TrIxBHKUSQLkjWHHbH_jBETACwynjTRaDems1AHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104541" target="_blank">📅 11:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky9EolC0Mj86GZdB5wKOr6h9sb5kUSJx50Ipf38GkviV8ysZ5iZlZOp1_808wg9IJuigYi13W715CYljRlOhcEMq8zkmeEOO8dUMkDWhj3cZpX4fVLvEdM1NHr4SSbxPA0eocfIBC7Y-KsazdYehvbGWhJQnfq7Pc5TxvYKPdkdpx-3b_OMQQo2jC-Gvp3SCyQwuECu7tMfqkXFfCbOY8MYftJk0dexdrmq17VVgIpqXbsGBqCpcFmu_FgBnEjXfwflTRl7qAuZEZfY5JiOVEzG8ZDnftQKUebVGiu7iZtqw3gCLedigauXb0fTzo0tmUviajifRKFAtuiH0176QhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه پرسپولیس برای بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104540" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104539" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104539" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpEHFnFwyNXHnmFj6Yqz23RW8Zy8QplwdElIsi0T9pJRxqvLUXE5OpiiTSsZbeRNCxSULlLcNfrUJLBGUPi6XQGhRsWbEtXVSyZw9G6Z16heMaj7hxlwFYh1PFJZ3zhEqiOJH1nyqE2xMH9vqp_s79huzuKRMo8MZ9JHrGhJCOvFYvRF5scN6kdHPcnqQKSOq53N-7an50CUpb5OWxdVn0qxR3n54eNF_8-5De_zlj5mZmedpaAgTGWgPl46941C_p8FJhvroS0H3YKac_ptnDyz9TnJ2tQLc8nhbJJmeX-9X2Yyud-TT4W68ns5jGCh5KHDIZVAy1Z9RCeIM-uQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r2
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104538" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc944da41.mp4?token=bfZZntFYA1TwUIf1EHeTFRfc7GYtcmsKVyFPuJFDrOX-UH17vvAWIupHX8uiLpovO6qasqMeI2IP-3AjemWZlmBGdfhh4R1NJnK7VPidbPpwWIk1w34rJU4Bq4AyhCI2OzKEU_d_tt6JimWcLN19vvHnkkAoawtQMBUt4nkfV9LTmtJQ6qGZPBTq928pwbovuCclMxs4HBoxbKtigSj3mI2-dmzJ1GQjRALhlT8JudROI8ZBX2F0CidpnWnNS8UzDP9y-eBpWrBFdtj34xOeHWHrLOcBcUnu7cykDVh-Lm4vfxxGQ1MTA9_whUUADHpK42QruDqt9kB2_CWac_sDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc944da41.mp4?token=bfZZntFYA1TwUIf1EHeTFRfc7GYtcmsKVyFPuJFDrOX-UH17vvAWIupHX8uiLpovO6qasqMeI2IP-3AjemWZlmBGdfhh4R1NJnK7VPidbPpwWIk1w34rJU4Bq4AyhCI2OzKEU_d_tt6JimWcLN19vvHnkkAoawtQMBUt4nkfV9LTmtJQ6qGZPBTq928pwbovuCclMxs4HBoxbKtigSj3mI2-dmzJ1GQjRALhlT8JudROI8ZBX2F0CidpnWnNS8UzDP9y-eBpWrBFdtj34xOeHWHrLOcBcUnu7cykDVh-Lm4vfxxGQ1MTA9_whUUADHpK42QruDqt9kB2_CWac_sDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دوباره بیرانوند - پرسپولیس به هم رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104537" target="_blank">📅 11:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00277ae5ab.mp4?token=lcbFkS-axGhC0JmxeSDalzjyhZDhnXxZONtnC5ePaQrI6xKnxqQIIEUPrVwULybqQXZpXRuwAtSJAmOTkEDN25zqmSUYFt4-nqNi2AYHirQwdRls_O0-luty93YHZYrlIzB_4q50qEv0fetjlyFl3tK4w668c4Y7B3IRvf9CXuCYrU4CxJnBO7rW4CxzQmgOG65v96t3fyUOiZb3hCzOIcfZfSXAskHXxkup8pnZtU8oU4lM6FbtYJuMHDo_d8l2TzweQrN7Uf1WgTxJ_BdUqOrKNaqTx3xsqV423yGrYcXt2VtUU_Vu6agFdPGiPZEBDLKatF4sHwiME0xyQy40Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00277ae5ab.mp4?token=lcbFkS-axGhC0JmxeSDalzjyhZDhnXxZONtnC5ePaQrI6xKnxqQIIEUPrVwULybqQXZpXRuwAtSJAmOTkEDN25zqmSUYFt4-nqNi2AYHirQwdRls_O0-luty93YHZYrlIzB_4q50qEv0fetjlyFl3tK4w668c4Y7B3IRvf9CXuCYrU4CxJnBO7rW4CxzQmgOG65v96t3fyUOiZb3hCzOIcfZfSXAskHXxkup8pnZtU8oU4lM6FbtYJuMHDo_d8l2TzweQrN7Uf1WgTxJ_BdUqOrKNaqTx3xsqV423yGrYcXt2VtUU_Vu6agFdPGiPZEBDLKatF4sHwiME0xyQy40Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
ویدیو وایرال‌شده از تفاوت صحبت‌های تارتار و وحید هاشمیان در مطالبه‌گری از مدیریت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104536" target="_blank">📅 10:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e82f680d5.mp4?token=AtT9Rm48JOBllPrOKP__iUVwk7Gk9eldAsj0Oj6aHWg0TsMFi_N67FMJO7Ud_At4m9dmX2wyr7fR1j3JekzrGUnZ2nxgKnuBV3pzN8q9bR9bNShSeuLhnm-xTo_k9kvDd6cAEAJ6gbZlLvlCP9fN6TgXIo6P8sYJuUFeMiFcSF9TMnAue-I3t_IaxYqgC-kWRyWAh_MxoEBP91BSqymaJq8P5j7thVTbqpkVTrqZSOsrcpyUeZIUs9KAHsAvbrn34BUE3jsYQWhOX_Rzp0kQviY-SrOTFEemB6evhurk1IpCIE03qBWR36r5Awwk1rmoKJPL1zqAXkkAnp7OOg7jB7aqw3AIVsKfjtQQMPeqGgUJq3cA1Y888j2JsGhBn_aj03feVwkk-wx_DDSwG1KOQ-vZnU7EtcQ5z5uO9nN3I8JswSLMJJyYghh4B1wujlx4MBEtXVbeELDDfZH-0xiqAUxNPjtp93iL3caAVYmwPDYfTa8BkiNTZRT3-n2NycjKyt3zg0C2tUhqb646LrauiBB4a3fVqdKCPOTvoacmnc1Rfu0lQyHh4B8dvahXyOQyuTSV9UcFIcN5XMx6xB_RhFJcVhi21kXfBs9VXpWRM3dbWWedKRVlPy5kpcMseRNFWPiMtm7Bpn77CEmjlnwWlxfM_LocZzM8SkpBGL-HDUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e82f680d5.mp4?token=AtT9Rm48JOBllPrOKP__iUVwk7Gk9eldAsj0Oj6aHWg0TsMFi_N67FMJO7Ud_At4m9dmX2wyr7fR1j3JekzrGUnZ2nxgKnuBV3pzN8q9bR9bNShSeuLhnm-xTo_k9kvDd6cAEAJ6gbZlLvlCP9fN6TgXIo6P8sYJuUFeMiFcSF9TMnAue-I3t_IaxYqgC-kWRyWAh_MxoEBP91BSqymaJq8P5j7thVTbqpkVTrqZSOsrcpyUeZIUs9KAHsAvbrn34BUE3jsYQWhOX_Rzp0kQviY-SrOTFEemB6evhurk1IpCIE03qBWR36r5Awwk1rmoKJPL1zqAXkkAnp7OOg7jB7aqw3AIVsKfjtQQMPeqGgUJq3cA1Y888j2JsGhBn_aj03feVwkk-wx_DDSwG1KOQ-vZnU7EtcQ5z5uO9nN3I8JswSLMJJyYghh4B1wujlx4MBEtXVbeELDDfZH-0xiqAUxNPjtp93iL3caAVYmwPDYfTa8BkiNTZRT3-n2NycjKyt3zg0C2tUhqb646LrauiBB4a3fVqdKCPOTvoacmnc1Rfu0lQyHh4B8dvahXyOQyuTSV9UcFIcN5XMx6xB_RhFJcVhi21kXfBs9VXpWRM3dbWWedKRVlPy5kpcMseRNFWPiMtm7Bpn77CEmjlnwWlxfM_LocZzM8SkpBGL-HDUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
عملکرد درخشان یاسر‌آسانی در بازی‌دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104535" target="_blank">📅 10:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f1d85674.mp4?token=Itc7B4V--TR8QqqGs8QP5a41X8SwX3HwdPixghAkNIfvhdA1fQKHwnWh4-1eYlvEVP47Fg0ebkmd8pYMk5gBA_iOeRdj4ZogxgdX0S5Dw42Cq4YnJQQtJ0xwDdDWnsVYnaBS5VxoJQP8PEdIdzmaq6pTd-lgbW7XtGlYqtUdGMIC2Viu5wmC-qev9MC5O5f52HhFk1vOnZFi17uEV02Y7-1mYw8xk7_WDAaS07rh3tUdcrhJNWF7_vLMld-AeRpU37lh8BA7UX4rGEO_JZzDBbjPiUMr5VEY8SQodxkuCrtN_JcFRVqeL4VzmIOK4xveJ2cutn9nLuw6kyHzcXJbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f1d85674.mp4?token=Itc7B4V--TR8QqqGs8QP5a41X8SwX3HwdPixghAkNIfvhdA1fQKHwnWh4-1eYlvEVP47Fg0ebkmd8pYMk5gBA_iOeRdj4ZogxgdX0S5Dw42Cq4YnJQQtJ0xwDdDWnsVYnaBS5VxoJQP8PEdIdzmaq6pTd-lgbW7XtGlYqtUdGMIC2Viu5wmC-qev9MC5O5f52HhFk1vOnZFi17uEV02Y7-1mYw8xk7_WDAaS07rh3tUdcrhJNWF7_vLMld-AeRpU37lh8BA7UX4rGEO_JZzDBbjPiUMr5VEY8SQodxkuCrtN_JcFRVqeL4VzmIOK4xveJ2cutn9nLuw6kyHzcXJbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلمون واقعا تنگ شد آقای ابوطالب
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104534" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a3a57ef.mp4?token=Y7txw2esSLicSovpcb6QTGU9MRbARQhlxUMZHukPrrcZD7jbUOpE4CrwxofSwarKUmObm9Ba_T2rv13vtkKHT-H97ks5-jbLXiQe3QrN6dnBTQ4LR12LF3_dLaG5RAgPhbPz9NsAPRjOFxGF6JH9EljVMh-6QGM06PGqFnaoicnLBUguaAb_RSimeTumTq9k93pgvT8OGlHSyVHWeAkNUdbdHtOuqcfkz1YGn7stBXeQb90m2fGQKUyOm3QNFmmsE41lghIjkMOn-SDabulqDMPBbnfDacyBbhh7OT_b9XfGhzT9PpgM9OMPkbkFIDnegSnmM9Nt1HSze3ib-y238A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a3a57ef.mp4?token=Y7txw2esSLicSovpcb6QTGU9MRbARQhlxUMZHukPrrcZD7jbUOpE4CrwxofSwarKUmObm9Ba_T2rv13vtkKHT-H97ks5-jbLXiQe3QrN6dnBTQ4LR12LF3_dLaG5RAgPhbPz9NsAPRjOFxGF6JH9EljVMh-6QGM06PGqFnaoicnLBUguaAb_RSimeTumTq9k93pgvT8OGlHSyVHWeAkNUdbdHtOuqcfkz1YGn7stBXeQb90m2fGQKUyOm3QNFmmsE41lghIjkMOn-SDabulqDMPBbnfDacyBbhh7OT_b9XfGhzT9PpgM9OMPkbkFIDnegSnmM9Nt1HSze3ib-y238A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چه فصل سختی در انتظارته آقای مورینیو.
👀
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104533" target="_blank">📅 09:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d382f7b092.mp4?token=ixiDyX53-5SYZGFiVJCQocunrh1fxcEOUJJY9U8UncIzzFXnvuSiTQE8QFkcFNhwYdzU--MaZ_z9RW_wVAE6vDZVAIRix7t6RUz6RvlnfAcXQZxtzv9N1fc-IkI1FYlDlwXUSsIt-cVitGn8hIGqrLUo5NeF87iHC0vPinzJh9L1SG6ehN5aBR3zMvMsU14DRcGd42WZjdL_nU0ccZGqVsUfarscdJ1BT_nI7GMpSbS0ZR7Z0t8pjcAZd7f-x8tmzG0HjRF0IYGQPMIx2U3X-KpykmoMK0RZiLBPRCM1-LjFWHNYMdIrCNOubRTguZb7e0D2zd-cAzohiIHNofRVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d382f7b092.mp4?token=ixiDyX53-5SYZGFiVJCQocunrh1fxcEOUJJY9U8UncIzzFXnvuSiTQE8QFkcFNhwYdzU--MaZ_z9RW_wVAE6vDZVAIRix7t6RUz6RvlnfAcXQZxtzv9N1fc-IkI1FYlDlwXUSsIt-cVitGn8hIGqrLUo5NeF87iHC0vPinzJh9L1SG6ehN5aBR3zMvMsU14DRcGd42WZjdL_nU0ccZGqVsUfarscdJ1BT_nI7GMpSbS0ZR7Z0t8pjcAZd7f-x8tmzG0HjRF0IYGQPMIx2U3X-KpykmoMK0RZiLBPRCM1-LjFWHNYMdIrCNOubRTguZb7e0D2zd-cAzohiIHNofRVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104532" target="_blank">📅 09:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=urUavNAOWztV6pRXBGJHTDkuIVVsZUT_SrP2OFncQ2vL_lX_JSQaocBdQjqOoKhgSbUD1hJiE049XsBfwjn_ke5gy_TRVCO9YblCIl4nhtbQuNIWWU_QgoQIxC2UdcHKpG3Rb6pzCatAvyyk_UYrj-FmA5JWlJunTgVs6zEIx22deziYiXQJdsi9ExGE8ANyf8om92VYsXq3FEWr0o-75oLGCQaSOR9x4aSxdp7ZTDa78FOyMShTqaDv6GWZbLhto4lyRDsasn2DZ_1LQkaL-yRo1zC5k7JiYbUlxz__3RMd3A5iYJD6X4xuk5naDeQ7ppGXMJkym8e40AB1R6TGEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=urUavNAOWztV6pRXBGJHTDkuIVVsZUT_SrP2OFncQ2vL_lX_JSQaocBdQjqOoKhgSbUD1hJiE049XsBfwjn_ke5gy_TRVCO9YblCIl4nhtbQuNIWWU_QgoQIxC2UdcHKpG3Rb6pzCatAvyyk_UYrj-FmA5JWlJunTgVs6zEIx22deziYiXQJdsi9ExGE8ANyf8om92VYsXq3FEWr0o-75oLGCQaSOR9x4aSxdp7ZTDa78FOyMShTqaDv6GWZbLhto4lyRDsasn2DZ_1LQkaL-yRo1zC5k7JiYbUlxz__3RMd3A5iYJD6X4xuk5naDeQ7ppGXMJkym8e40AB1R6TGEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
درگیری فوق‌العاده خشن‌ بازیکنان شمس‌آذر و‌آلومینیوم اراک پس از پایان بازی امشب؛ چه فوشای ناموسی و عجیبی میدن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/104531" target="_blank">📅 02:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyfomJHvkuo2cwVcDkUNmSBbm6f2FutYmC37UOu8C834DkrLvZbgrwNFNeoGMc67_dUsn5lhltBxEHWwP4c6oTJAcpcPJdcC0JIWxc5_0mTo7QoUelllGNVvVbKFrgtU604GvwMtWNaMyMzGA2AThQJpDldUHFro3PiWHSAonLiFRs68ek9_wp2x11wFiww8QGj-Dw3im-rEssor-BSiS4JKCPVBKRNvbRGNiCK0313UFWccixBvhzg9aqVk7dTaAk_LM8Z6f3N6TaJGJnNfqxfGos5WGJj3QfNEjPh_uDzN-iORfd4-sZp1G3bSxh-kVeagYgffEcYdRcpjhL5-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇸
خایه‌کن اروپا؛ خط حمله بارسا بدون مهاجم‌ نوک و بدون لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/104530" target="_blank">📅 01:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0iuj1H8PfmOI3HtmjzrQJD_SLW-fAynPEiWNdBj1DGP8Mb0bEy7jz3De1IfjdoRc1OwoyYf37kkfq_DiGrTQgWp0WjS94awO8PjT8PNvse3Q3O4N9Wvwqsi-2zwiJGYZ9sqe1PQSuNDSshjaWgAw-IPTurtiVLvvkrzUevE8oLyZbpUFH5o7K3vKUxryHy-rfYAIjXP2fybyAg_ZFM95zE6nyqieHaoTW6Qvnas2WhU9DBJE4kEytHMpVjmxKSgP03H-GhC_bJjtt6rTfyrJZ5B75eo8ap8ljE5yP8-B2nv99qCjNQg4lua9QVH1DUuAsNmu4c6X51joagDDqhnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری از نیکولا‌شیرا: بارسلونا در ۷ روز پایانی نقل‌وانتقالات تلاش فراوانی برای جذب خولیان آلوارز انجام خواهد داد. این بازیکن با بارسلونا تا سال ۲۰۳۱ به توافق نهایی دست یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/104529" target="_blank">📅 01:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oDQ4Ug5ZbWWIrPmjctCcP43jGr51m4s9OkoQyTgcVGLRw3Kfw4SkJdccEA9LP6zhRslzHsX_t4U0ZM9kRVIBr5jyqwUSLx0CoztmqsARiji7b24aINSRHkSiChjNtrj1buTRPvHqLLm7S-AFI0uNSo7ddO85wSeasfXpO1flwvmAsMBSEpl5yHpnO4ZbKzVtJpZG2fH8vsLF0sQYDDvmHqyZASkI4-9570V2dyXmB2oW-8ImozbYWvi6IjRW7EtfP1KOhIJqfuoI8udX_6dcD3ZcGsQzL-qFGF4vduEGCnKsQ7WbYt6Xc83GnF8mZ414gDVs8te8-5VcD7doOJJmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از نیکولا‌شیرا: بارسلونا در ۷ روز پایانی نقل‌وانتقالات تلاش فراوانی برای جذب خولیان آلوارز انجام خواهد داد. این بازیکن با بارسلونا تا سال ۲۰۳۱ به توافق نهایی دست یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/104528" target="_blank">📅 01:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onu1BET1-MQ35S70V2T-QIDO0WU3GZ2dEIUETLRaE7DB9ly5K8xroLgqjY583zWX2OTgShxvfGgeiylM8F_92Z5QKfZ5VRoG-11AMVYIT6ekUb-rgrnvXLf37VZ_wFDQPBT30v9ecqkpo1hMHW3qR9q01S4MnpGAbL44euHF1VK9WQ9uLmD6QEQnWRichkzJOZZ1WPiOKejGYpWeLSA5A9M7-BuFAxtW6fFawfc9cf8-NThYoK4WGRZrwpqjfRuFMAEAaPG68rBSyGzxqDAYusbXTCyRzbNYHQyGbME8Deq62wwYrIR5In-5Jj72ECDG5cavfqe20GXoMYcF5aY5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚑
🇪🇸
براساس گزارش‌های غیررسمی منابع اسپانیایی، گاوی بدلیل مصدومیت در بازی امشب بارسلونا بین ۴ تا ۶ هفته غایبه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/104527" target="_blank">📅 01:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtM2OTEBzi08SQY-4Jg26v1Sgdx1wmzjSmgVZVZcbs_AlqCtwryLfaopXcj8tShbGCd2bATD-ReKhM1nHUKTz6OYE-VAkoDsGslN64WoGTA6V83LRw5LW9qlla3L7KfTka9cKd5RlR_AwWfRo5_Hd15xxLwaNcygZ2_3pmL-NyIIYEzjF5GE6BeSzpC_MPTlez3hezMV-998AbmOQZsY5h778n5BfPTaisSf2U166Da3XIGjx5zTiiyNxEkIRbXlprDmGWY9JYaibczf4xDaPGHcBX7KWQpdAPOXkqqPIzTkXKldK6EEjaP_lcVD2FcmqgAHFHjQL8Y12udiLMmgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
امار درخشان رافینیا مقابل الچه:
۲ گل
۱ پاس گل
۳ پاس کلیدی
۲ ایجاد موقعیت بزرگ گلزنی
۱ پنالتی کسب کرده
۱ موقعیت بزرگ از دس رفته
۲ دفع توپ
۲ باز پس گیری توپ
نمره ۹.۸
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104526" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2poESKKw4626TLG4oW4UFYQyMFjgd3IlKGAr_KwrFk9iXverzHvsiOscn_mjspr6d5VPaWGl-TPNnnxH0iOCdJ-ucU8qi8QLe1fav6AOKmI5oeBvVq7AUcDlN9yG9Son3aZ4-EfeGYWpPTc4aZcJKUgZWg_JHgagMG7RfKwxF0sKNgUPR_-EMlhNt8xE6pi8tpaqwVGSfub-P6z0JJtTWXOSwZa5Smiz2HSHJtWDiDIyinGag0nt6-alWfrorJi_mddC7k8ycJl9UfEud0bif_jGcQ_gOm5RBu9YV_s-tpvRU0cnaZM8_zUHOPynA55HripV4r3a4PuKpuqTn788g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌دوم‌
لالیگا؛ بارسلونا با گلباران الچه برای رقبا خط‌و‌نشان کشید
الچه صفر - بارسلونا پنج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104524" target="_blank">📅 01:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=j2R476T_EmZPZj9rbTssz9wntZwpb9BrSnozh6fV13Gk7LGW06Fw5B8JO5cJBHioUUp1bAsWy8WqVyyr5dm8b3b8I-EJE8ZFRlnj_z_XcVXF5mL_khJqhbAzXl3y2PN3HKbohOmZiwRS8KosjYrM6jgqhijagUga-p-y-YqBuTzsQ_Frzk0FQpd5tFxHgvdFZPSb2neVkAn7SScVODi1dA1Ib40NPvBfgzbiHBDzgAsYSPj0EbSYpqw9x_IhdHWWuUh4klKKQEMbf3qLKKu1U43ZtEVu3p4tcHDT7F9VNvGBt4kbMweGZGTUYYVqRpj2iduqtQpATlBpjZV7OtFlmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=j2R476T_EmZPZj9rbTssz9wntZwpb9BrSnozh6fV13Gk7LGW06Fw5B8JO5cJBHioUUp1bAsWy8WqVyyr5dm8b3b8I-EJE8ZFRlnj_z_XcVXF5mL_khJqhbAzXl3y2PN3HKbohOmZiwRS8KosjYrM6jgqhijagUga-p-y-YqBuTzsQ_Frzk0FQpd5tFxHgvdFZPSb2neVkAn7SScVODi1dA1Ib40NPvBfgzbiHBDzgAsYSPj0EbSYpqw9x_IhdHWWuUh4klKKQEMbf3qLKKu1U43ZtEVu3p4tcHDT7F9VNvGBt4kbMweGZGTUYYVqRpj2iduqtQpATlBpjZV7OtFlmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل پنجم بارسلونا مقابل الچه توسط فرمیییییین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104523" target="_blank">📅 00:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این الچه بنظر خیلییییییییییی بیش از حد تصور کیری میاد. دفاع کردن بلد نیستن اصن
😐
😐</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104522" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگلگل پنجم بارسلونا فرمین لوپز</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104521" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=WxfzNPj1pSC9PB_BdhVNQErSeqS2gcuVC5f2xcSW7t7BdVS5FGl7bNZ_M9uujrefXTLaOxb4OAm5dFVRWaYOrg5NipuoOJ_E9ELiTGItyIw-BF70QJx3qzqP2ya0k2lIddHgs1QM8dHQ5VnRdlJ51i_1P6k53ex5YYOAmlnmYTaZg79Y_3aqDimfjSKODT9NlvL54dmKPm98RfeHCuoFoWpsoNsnU2bI_bi1dpJb8U_M-METMJ-BS6yUawwzNgT2jLaV1xQh5K-joT450O54fkDATptYWwNrCVjg6xKAZrZuoU9LWBsi5O7cd55gFds5D0t-U7LgzGyBqx658kTxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=WxfzNPj1pSC9PB_BdhVNQErSeqS2gcuVC5f2xcSW7t7BdVS5FGl7bNZ_M9uujrefXTLaOxb4OAm5dFVRWaYOrg5NipuoOJ_E9ELiTGItyIw-BF70QJx3qzqP2ya0k2lIddHgs1QM8dHQ5VnRdlJ51i_1P6k53ex5YYOAmlnmYTaZg79Y_3aqDimfjSKODT9NlvL54dmKPm98RfeHCuoFoWpsoNsnU2bI_bi1dpJb8U_M-METMJ-BS6yUawwzNgT2jLaV1xQh5K-joT450O54fkDATptYWwNrCVjg6xKAZrZuoU9LWBsi5O7cd55gFds5D0t-U7LgzGyBqx658kTxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم بارسلونا مقابل الچه توسط فرمین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104520" target="_blank">📅 00:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104519" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104518" target="_blank">📅 00:35 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
