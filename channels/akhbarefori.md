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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-667982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0931f23b88.mp4?token=hpKG3G27ajOj8Ff4606fC1F15lCDFpPOSvCF2dG73uDYJ9giD29ezQ2bG-7BDF35BarRsBDGR5470LV-EujOHYwp9y1b_Vt7Nr85sL1hMqqsZcNBS7jAifcB_3UynEZmQ--c_mlEDbWmfcXLB3WmmHDPdXZ5tDo5cCy7kwo1U-5PsRSG6qB9HFJAfpeqvlJiqxLiT8EEsa64XXCKPSXi1um6_2ziXFTfSMlOcqgS3OFuswpvwguPlD6MBd3NWbXETYSIEjGL6QBptAGAieKjtwUUwLnyI0Kl4C-1_I73_-OgY0b3RXCl4B8yd4npu458H40GrstH80Dz9IbUsvBFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0931f23b88.mp4?token=hpKG3G27ajOj8Ff4606fC1F15lCDFpPOSvCF2dG73uDYJ9giD29ezQ2bG-7BDF35BarRsBDGR5470LV-EujOHYwp9y1b_Vt7Nr85sL1hMqqsZcNBS7jAifcB_3UynEZmQ--c_mlEDbWmfcXLB3WmmHDPdXZ5tDo5cCy7kwo1U-5PsRSG6qB9HFJAfpeqvlJiqxLiT8EEsa64XXCKPSXi1um6_2ziXFTfSMlOcqgS3OFuswpvwguPlD6MBd3NWbXETYSIEjGL6QBptAGAieKjtwUUwLnyI0Kl4C-1_I73_-OgY0b3RXCl4B8yd4npu458H40GrstH80Dz9IbUsvBFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مصر به آرژانتین توسط یاسر دقیقه ۱۱
🇦🇷
0️⃣
🏆
1️⃣
🇪🇬
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
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/667982" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4fc4f4f5.mp4?token=cMBqn1tpIZpe6o23yaDKgNO9s8pCcL5NzBINvgL3IHjkouGU-DdKFOAm8FsMggi7zRfFsI_qi_EPM9EHF_IMNkgiNOcttW3ey9Vx-M4c7NttNbE-uqMz2QowRuRB0RwqHnade_x975138mJA73KjeFU5Ac89PBFVIZIs_Opas8X5I54DGIItLcZo1_OclxAKpK6VHDgS4B8GzE3zeLk0viJV0lpthrzxmDG71r__epgx4PvnwU3xS2BLZSnnVWyqhXZCNsW-D7K7pNWwuYFKgTgxwseUcKQHZkm7k21uplrrBgznJNJZwhcbavXzhoSor9RRdtdFcgd6BKjTDGoBZxBVlwVnOUYUC0Q6MXuPe7AImJ0ya9G6VKnMpYYUtlCS9YL6NOMy4BwUwZk1Pxe03UOyJbv9WW0OQHieZgwfguBAchQ17p1mxNkegl1LViX35BcLmxwIkek58tPxBkuhJ_KNefJbiGfMjgrEnr5sdi40Q7uBgXCoroGB9pIurkuAT1p2WyUywwJiuLBJx4djQJ-psEjusFAPWwF1hZgYIotLrS2xDQsLvrCgEagMpFKRw449rL9AWga8_kBeQ2dJRPuOSbL8xvOhfdtCeaewO1AxZzMqY74D0EhJQGlA2YiA50sRpSfy3HOvUlLsOvsHwTAF6WSpRezB46onUtLKWks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4fc4f4f5.mp4?token=cMBqn1tpIZpe6o23yaDKgNO9s8pCcL5NzBINvgL3IHjkouGU-DdKFOAm8FsMggi7zRfFsI_qi_EPM9EHF_IMNkgiNOcttW3ey9Vx-M4c7NttNbE-uqMz2QowRuRB0RwqHnade_x975138mJA73KjeFU5Ac89PBFVIZIs_Opas8X5I54DGIItLcZo1_OclxAKpK6VHDgS4B8GzE3zeLk0viJV0lpthrzxmDG71r__epgx4PvnwU3xS2BLZSnnVWyqhXZCNsW-D7K7pNWwuYFKgTgxwseUcKQHZkm7k21uplrrBgznJNJZwhcbavXzhoSor9RRdtdFcgd6BKjTDGoBZxBVlwVnOUYUC0Q6MXuPe7AImJ0ya9G6VKnMpYYUtlCS9YL6NOMy4BwUwZk1Pxe03UOyJbv9WW0OQHieZgwfguBAchQ17p1mxNkegl1LViX35BcLmxwIkek58tPxBkuhJ_KNefJbiGfMjgrEnr5sdi40Q7uBgXCoroGB9pIurkuAT1p2WyUywwJiuLBJx4djQJ-psEjusFAPWwF1hZgYIotLrS2xDQsLvrCgEagMpFKRw449rL9AWga8_kBeQ2dJRPuOSbL8xvOhfdtCeaewO1AxZzMqY74D0EhJQGlA2YiA50sRpSfy3HOvUlLsOvsHwTAF6WSpRezB46onUtLKWks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگرهای خارجی همراه با ایرانیان فریاد ترامپ را بکش سر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/667981" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrvrUaH3fiDHQN_IPyVwkGieRCP0FQqztRlfS4q6aHr756beQ6pyX3dRzHxggswfmvPk1IhiosoO69076JvCafqG2uEuNkA1WH9CcI1WADqumVhC84YJqTGTsqKVFyS_5oxYXdHAvKl1XpWoVczzhr6Dzt-CeeZeULPcE2uJzQSGYS4fKmRLP5Jgjfns_XxCHpvvZCZK_Td5RRPnRxKmM0tacmrOhtiDMWt6TjxggEfQpmje4TP4DO16R8DrUCdunRoq4JSL3vML70dJc9O_Ppn_7FU6oim1s9vDQVEVht121f4_L8TkHlNIQuAiWterRncd7JDlQYzabDncKoJbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6MW4c6MIZPmHxoMWtA_QvDo264PjmPgfm08fe2gxt-dUgZIn9h9IZOx_BwQb9Xntsk9p4MNdJ8UfZFHAo-Dab7F6AQ5g_PUEle96UZuGUjMeYkGKaQoWtGMMpzbhX7xyaNeEgbokpC7JdXtZHWHU6MfJYrzc9Kf4325E-HIGxpKQe1B45HfUzWq4G4T7-Lj7qzCU6hDoNu3naddFVIRj5TPjnuLH07B5hGKR0s7Q50OEVFcwfE0WsxwDkwYIsiLxUOl1xw3TiAUiE39A8RKNCYft5nowhdLPzfp2TF0a_31-R2ENIAT9MyawsOv27L9Cl-5Qi9VCWO7QTO92TNkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNo9iTq0cS9BVVDbxTHCGHAlPlmFZliA-K1I4pfNGzYleHgF9yFsSkR53DFUTUtbIXY7cqHP8XSo6RC97WayI3rNrgm1-sKHa2VVjiTgSVWb8JT2ydpvCMEM4mhK4ymLVtHSTC3is8lPaic0a2NsqAI5tosbGWDyy_WRZWrXt8v7nWxqHbjW2wx7cEqpr_w82Cux2GjAXoGMKF8ViaZmhlQDY-zTkL7m0nQzmSNvrqS9evuUNEKHskaysoVvL3Mwn6GckXz6w0JPzvTpHRzv7Pqhaj-dHZQMo7t7bpMqTgNqQgWVEN1rpOvgikGz8hnMWy2eKcoLQdjYet3SSsUMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9y9N3pAgwv25JsDPPioj64R2oJkWXFx2AtVZxeh0et9AJLODUlnSnQoT3IPYJZ5fDiWWW-_ChqiJwqiLbnyMHtMy7cPYytMjEex_jpNa7s0hqr6izsYG0Y6A35wv3m8oLSzHXram8xZH8k2bRsir_mZYWoS8jycJHlWL-JgEem_DAHFdPdK2r4iT9Q5hXqQLlVKL9vBwZjC6ctKkav6EXsG_MaHyxDaw91TBclcgaG-YRQOPCi5YZB7j94KzSIQDssw9_5eW2dTAK-w5Xlz795n3Uwv6zH4gaG1E2ZnAlmG4IYIoRjIO-UG_hp2MNaolBYeXhV1iIq0tTCffeJCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG-kKfTNf2iYqdxIdz-XtES8nCNGxa70r8UkphiOBtITUL6bVfzJrayEBMNXG-6hVtNIwZENHP9esmZSoWbBIMp5N3zAHdlKAUsqJluKtUP0BlCAOcuLE-yD-IkeKkXUnzUB7xboS6opLtPsREjBEI4X-Uz0khtBlsSW_3Lsxh5VcF_ryHhInbFmseMLh58sVh_hFny4uRew9muKKMJ65dTbMnVkbsZ2DFsuGrr0vkKGfUf_S7oo2_kSmdo4WtQH9xqwsGAwAaovi_p1W5xFmy44R-BE-LhTfS_hPoXMFa7BtAGqTVWB4h4nDBnoMQPlD0AJBeW0q6G-8oibfNe32w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر محل ادای احترام به پیکر مطهر رهبر شهید در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/667976" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=r_gdLqpAS3b7hbnotBonrblLHEkEgsVnJWRQz6QngfsUK9BW-6flGhYReLXxV3lDoO5oXSpU63-hP5T1d9k_7ovt4J2qMMmcpyNtibsYgCFQticEKj-SJjFs9-WK54ADmf738CvPk32Z_6_yMBPixGLDO6yCOZL2C4ROS5rFkSoT5zi9PzNY_IuseoThBVC_dWvhutdAPHxr7UYdxvBgEtnLF4BjAUyV_gdMriwMG34DNekv8t6mrGATKM4X0kM0kASuYUwScq0aSORNNax_y1DoBM9mcn4Oya_fNzdf3N2f_Qg6dgH5bxOconSL-uoUL48Y-rozfNuNwaelORE0iQYA2QDErkxHSyVIX5CkqNOq-w3V-iJSkVxk7hOgFFrMjXniyj8sExO9iMUi196WP0ssuKGutqYnjb_M9sXN5sh-OeNm4yVAfHgKwSU9FBXNg5rLc8bzDe2XxJOXB5pzY1rHYaabpdgHFFbj-D0JFNQ7iVniIXRfGNXCybHvmCW4bvIQotBaX2j9Nrwt4bnv6RChZFOf3TvBstWaV_W0fb3Q3Vau_30XtB5Aw0jvvwYdBWaUwnOAEmbLYGrusQXyNcjwZ1KVot2MJ7pP_i_5lILFB4u67CY3RB4hoNfJ_XBIuyTr_gToCecH81IRXzgKQGk1xJwovELVq_hJBOWMu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=r_gdLqpAS3b7hbnotBonrblLHEkEgsVnJWRQz6QngfsUK9BW-6flGhYReLXxV3lDoO5oXSpU63-hP5T1d9k_7ovt4J2qMMmcpyNtibsYgCFQticEKj-SJjFs9-WK54ADmf738CvPk32Z_6_yMBPixGLDO6yCOZL2C4ROS5rFkSoT5zi9PzNY_IuseoThBVC_dWvhutdAPHxr7UYdxvBgEtnLF4BjAUyV_gdMriwMG34DNekv8t6mrGATKM4X0kM0kASuYUwScq0aSORNNax_y1DoBM9mcn4Oya_fNzdf3N2f_Qg6dgH5bxOconSL-uoUL48Y-rozfNuNwaelORE0iQYA2QDErkxHSyVIX5CkqNOq-w3V-iJSkVxk7hOgFFrMjXniyj8sExO9iMUi196WP0ssuKGutqYnjb_M9sXN5sh-OeNm4yVAfHgKwSU9FBXNg5rLc8bzDe2XxJOXB5pzY1rHYaabpdgHFFbj-D0JFNQ7iVniIXRfGNXCybHvmCW4bvIQotBaX2j9Nrwt4bnv6RChZFOf3TvBstWaV_W0fb3Q3Vau_30XtB5Aw0jvvwYdBWaUwnOAEmbLYGrusQXyNcjwZ1KVot2MJ7pP_i_5lILFB4u67CY3RB4hoNfJ_XBIuyTr_gToCecH81IRXzgKQGk1xJwovELVq_hJBOWMu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون اجرایی رئیس‌جمهور: رهبر شهید، جمهوری اسلامی را به گونه‌ای ساخت که در برابر تمام قدرت‌های جهان ایستاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/667975" target="_blank">📅 19:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dcddf39b.mp4?token=TS62WfjhFPm4qvZY0T_XZTDVJXbjHeylrtMKvNDaezL2EnUPejZ0hSx-nqYL4_htnHWj_ClHA55htf0QYqR7inEQwnyv4h3aIve729A-CMdIPN9oGGidfG27KKE09KfejpT2jVaNEElx3z6scysWUaN4YmwbePWi-j5ATjUNJWTHrQIKqlsUe__CIfM9zZqeuJXaoyM9hFN1JmCOSmRF0WsAN_Zsb53BjyGi8h12zy9btfXmcYsraL0MONrEJ5os4y2QiqruiPgv1Ap7uR0vDJN1TXJfz3SUotVZataKRJe9DA97-mmb1bcUeAVtn1oTQHHgnkc22hpBuPboN8CVWyu1lGxeq-VrU1RDPPm-qw8yMiGHKo_KaX7HZKBuWtsAKz-J4Pg1FxiZe8fB_lQz0lXsOaIOgF4HQskL5t7ZE9yMGAQWrVIns48rvcA-YB-nQORtvQQ8fMkW30pUj-ekhjU3L7Me_rNcY0EUF0F3AMIzAQmmd1k5b1jrLQfPiXiy_n69L9pNpSz1toJkuE6uO9qMmNKYiaQhKn29LTu36GdNd-S7aV6SFrBFUnvbeEyF9Qr225B_5JqpkHj7Ns4qR_VKu1JBRLytXI6gBbxxBU792Ho2Gt4-bh-zttlTkdDyIaZw4G8VKNPof8MS3UlPEmziDEGnfIgNVfp-bjgIk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dcddf39b.mp4?token=TS62WfjhFPm4qvZY0T_XZTDVJXbjHeylrtMKvNDaezL2EnUPejZ0hSx-nqYL4_htnHWj_ClHA55htf0QYqR7inEQwnyv4h3aIve729A-CMdIPN9oGGidfG27KKE09KfejpT2jVaNEElx3z6scysWUaN4YmwbePWi-j5ATjUNJWTHrQIKqlsUe__CIfM9zZqeuJXaoyM9hFN1JmCOSmRF0WsAN_Zsb53BjyGi8h12zy9btfXmcYsraL0MONrEJ5os4y2QiqruiPgv1Ap7uR0vDJN1TXJfz3SUotVZataKRJe9DA97-mmb1bcUeAVtn1oTQHHgnkc22hpBuPboN8CVWyu1lGxeq-VrU1RDPPm-qw8yMiGHKo_KaX7HZKBuWtsAKz-J4Pg1FxiZe8fB_lQz0lXsOaIOgF4HQskL5t7ZE9yMGAQWrVIns48rvcA-YB-nQORtvQQ8fMkW30pUj-ekhjU3L7Me_rNcY0EUF0F3AMIzAQmmd1k5b1jrLQfPiXiy_n69L9pNpSz1toJkuE6uO9qMmNKYiaQhKn29LTu36GdNd-S7aV6SFrBFUnvbeEyF9Qr225B_5JqpkHj7Ns4qR_VKu1JBRLytXI6gBbxxBU792Ho2Gt4-bh-zttlTkdDyIaZw4G8VKNPof8MS3UlPEmziDEGnfIgNVfp-bjgIk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیش از ۱۴ هزار نفر از اصحاب رسانه، خبرنگار، فیلمبردار، عکاس و فعال رسانه ای داخلی و خارجی در پوشش رسانه ای بدرقه آقای شهید ایران در حال فعالیت هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/667974" target="_blank">📅 19:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667972">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxpFzz7fKGS4LliUFfjuXiyJby9z8Vs0XUcjJVPKgeh6AA7_rZbOVWNJaJS0MMWtmFa23EveGwsJKq0iWg-xXi7pInDaCm2FK0aaXoXHEPWI-JnZyLbwY97YTfE5v1tSnOOzfdn3EpG1LBOuva2si5RRGSSnOAXdQ8FLaHwwRu-kkaW7Y0JZbmkFdMlvWTuViImFiSn9LSKUkbSHNzBIkb6ScnoS3FgJ1KTTVgL3pD0w5JUpCIiFY7yxfYZgLh5hHvEUA7ey_WhWUVczXLQoqAgrBaohUrKwgJ9eMWws57SsPd-V_hN9dKEZTYvNna126f1Aqk0-gYMwPvgdgBYuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhiI6Oop7FAHYsvUVyYqcJbWJXKQ0iOWe2OyYU9nljcNxP3DCfJz1EBYJPhJPHfQTC1exiVQ6jxoJIkVVmMYKOvqghEe1vvAcnStpFWINWhIVvNcspB4JTvVBrZqXRCTApu-87efxxCDs8q5-OhsEH3NPs31xMpUD7vXT9rTWqOqxe9HIDa2q2SOuQD9oUFUYxQ2QEOq6Ekafxim4rGkvmKOfRBVUEXqeGEAtSEACq2gxxr22vwnXU3yDxmQ7WAtBqjEKWwfUiiDKri4Yn65SHJMrRnv2nRqBkHRxsRfvh3tLkIRGqzKGE33FPzIIqOoqfyh8SdJIkHb0DDE6zfcNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدرقه باشکوه آقای شهید ایران از سوی شاعران پارسی‌گو
در حالی که ده‌ها هزار نفر از مردم در مصلای تهران به بدرقه آقای شهید ایران آمده‌بودند، در گوشه‌ای از شبستان اصلی مصلی بیش از ۳۰۰ شاعر در دو شبانه روز بی‌وقفه اشعاری را در رثای رهبر شهید انقلاب خواندند.
برگزاری چنین مراسم ادبی در سطح جهان از حیث تعداد شاعران و مدت زمان برگزاری مراسم بی‌سابقه است. نصابی جدید در برگزاری یک محفل ادبی در سطح جهان و عرض ادب شاعران ایران و کشورهای فارسی‌زبان به ایرانی‌ترین رهبر تاریخ.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/667972" target="_blank">📅 19:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667971">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8a5f57c9.mp4?token=jbiXcwhS4nk30kwIEQgLdLDx_XWBL3l83w8JPCU8AK6FPrW8iQcg5Xe3MtLMWWtBc0eIlHeMQpqBGzyZD9kQe4Hf-dX7KdDZz5t4DRC9nAxb1soeZx2njI7Wsx97Kn0a6MscMj4cY04J5ai_tLQePWC2lzCyBt9x2tzPBpk-4FxqkBbVHAN00xmROxLQvII2uHCwGd9oKSGCeDWnBnWQqxKv7RYc38X_Xkme5NFCIswmgTjCo5aM5b8GHa38i8WhqFlZObOM5Dk2lWlJijq7AXH2IRx3MxM30-T3d-jEa84-5ifu3lOhCHbe7JwlZ3yDzWxP_CNU_QaZkRhDRAj8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8a5f57c9.mp4?token=jbiXcwhS4nk30kwIEQgLdLDx_XWBL3l83w8JPCU8AK6FPrW8iQcg5Xe3MtLMWWtBc0eIlHeMQpqBGzyZD9kQe4Hf-dX7KdDZz5t4DRC9nAxb1soeZx2njI7Wsx97Kn0a6MscMj4cY04J5ai_tLQePWC2lzCyBt9x2tzPBpk-4FxqkBbVHAN00xmROxLQvII2uHCwGd9oKSGCeDWnBnWQqxKv7RYc38X_Xkme5NFCIswmgTjCo5aM5b8GHa38i8WhqFlZObOM5Dk2lWlJijq7AXH2IRx3MxM30-T3d-jEa84-5ifu3lOhCHbe7JwlZ3yDzWxP_CNU_QaZkRhDRAj8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت کاروان‌های عزادار موصل به سمت کربلا
🔹
کاروان‌های گسترده مردم موصل، برای شرکت در مراسم تشییع پیکر شهید آیت‌الله سید علی خامنه‌ای، راهی کربلای معلی شدند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/667971" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پزشکیان راهی نجف می‌شود
🔹
رئیس‌جمهور جهت حضور در آیین استقبال از پیکر مطهر رهبر شهید و دیدار با نخست‌وزیر عراق، تهران را به مقصد نجف ترک کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/667970" target="_blank">📅 19:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdWU6DcvkSKyH-qWK5a1vqsElft_j3DNLZIzhW4Rmyx2pOxCtvskavRb72WHhgbNNpcweBI7M2hdL2sSV83RDeifk8xZr3BPllN0wWcnCvzwGPCIeVNeuIV9bsxfoK8pmH_hY72EMkHS0_Lpg4SMoaHLVWokh6V-LpYa4IT_E_NMiD30oklXqp1AnLpHnO2YV42Gv1TMMU1l2hh7q3bFVg3iEogRw0ID10W-9Rb033oE3kgWM7SrHrsWiq_U8pEgSdq-YcwpJ0L0u7XL3aQgJjR5uciXg7ujDezlsfVEkSTmWxpcV25nC5LrVCpir4sNvXRg2DRV8cEdmCI_UaEDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/667969" target="_blank">📅 19:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66462b861.mp4?token=cTLDgcgDLi-XbXNPnijOibGjM3rPUW7BJkhq0Ixiw5RnUM9uMeJIqhfHN4kHfY1aURHFozk6XdCRM7piY53a6J2N7G4dMxsZvygov38VWnboPl7mxh3PIlm1jcrdIVfuKFkhHgtdrUVlDSNB2O_8sqktUUq78CYs8I1cZFibpjh2nHrhwRjqQ1ajUmHKDaCmC6Fg77Ru3TWLBY4OLBu5X0zoR7zSxBqyLdZ4CLQDeF24UmLApl7rmSoeldey5hEeZOu8Q4J5aLampwRXg2MnWQxJl3sYz3ku_tW9apEwTnuwg6d8ibvlqfcYStKWTW5RXZ-oBzWqdVr5FZLRodTEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66462b861.mp4?token=cTLDgcgDLi-XbXNPnijOibGjM3rPUW7BJkhq0Ixiw5RnUM9uMeJIqhfHN4kHfY1aURHFozk6XdCRM7piY53a6J2N7G4dMxsZvygov38VWnboPl7mxh3PIlm1jcrdIVfuKFkhHgtdrUVlDSNB2O_8sqktUUq78CYs8I1cZFibpjh2nHrhwRjqQ1ajUmHKDaCmC6Fg77Ru3TWLBY4OLBu5X0zoR7zSxBqyLdZ4CLQDeF24UmLApl7rmSoeldey5hEeZOu8Q4J5aLampwRXg2MnWQxJl3sYz3ku_tW9apEwTnuwg6d8ibvlqfcYStKWTW5RXZ-oBzWqdVr5FZLRodTEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراق در حال آماده‌ شدن برای تشییع پیکر مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/667968" target="_blank">📅 19:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
افزایش قیمت نفت در واکنش به اتفاقات اخیر تنگه هرمز/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667967" target="_blank">📅 19:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUGvOFfHsQuHoS3QJd-H0BcXlXzPvH1WwpEUwSPSbz8MTcaQ7WUcGdlvr6_yFWUYhexftP2YEdDtJO2woBd62Ee3nrnLApERbIf-tQRbcnh7ANsTvzZCy0pJ4ZTzZIQqeO_h_j4Z6LN7Iwr4zrKVygnS2qcSxACWZAkN8uyWJ7wI0Ml7v-UvrhHtHRn_lMYQxrQSeMrXQmL21C4yBmloCMZ-F67PGRMo-i_rvISXqawSu08zJeVvTcrG2JMxUHbeBh8Wh0Y0gck-4O99F2_kUx_m_wa0Ga4PaW5Kibc41zrsbwWVXyuQ-LPlfOiRSUFUZ-L025ib7tOMETUYeJiT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
استخاره با قرآن کریم
👇
👇
#رفع_مشکلات_شما_باذن_الله_تعالی
🆔
@estekhare114</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667966" target="_blank">📅 19:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d98d13b9.mp4?token=OQYFAVw3MxEGFBohIoktUeKiiC3eBBks3kWMqZr8b-_f0dOkRGp_q16TTE9ArXGzuslqqOuyQDEUyDa6fjP4zf5fFudZnBtA4IbCo77-1cjZNUvSqCyg40g1R_eDuU05QO0hT-1R_mhv-RSeoxbB023nnDeOlmM0ZFXh5RS9pbS9th8b4GZZTakEoymFuQuAxsBzY2S0zGzrPws4a6LLasDFttpVAnoDm0IChTKDY5UTn1-WpeFywLUvYzD8uNEDPgeqKXunYiT39vGmbKa62wKksYni3nmXAofNP3y8M-TnV8dBMGGdCgt7j7nreFwEKWClqH2LaF_Vbus_OC8QEJ6IoLYFDAr5jUP7WVXSdISCIsCbUkn0mnxAWW-kUBc-jHOx81745MnaFBoZVwN-gH3gTDDEfMG2SWmwukK6PIAzvPfbu2yuLO8YY0H_5Z1EWPdPpLlrSE2kZszyL1DcJH9i2J1_9no_Ci7VLf-uTuInfhvi9dH_ZxMI9_6bXAk5l0h9qaO26vjtNar3bRNnjPDj5d3yhFy-0813hPHJbMceHKu3RzDKzUnse9ChBALU5zVozMDkYYPB9akv2TPoxAfYdLNMs12exEd1DjcdvgzLpzlmS0ekykcAeftUcbD_Yn-KbfJ-qkTlQ4yw2tETdmFuE9vZTOQhC8zoOMftrS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d98d13b9.mp4?token=OQYFAVw3MxEGFBohIoktUeKiiC3eBBks3kWMqZr8b-_f0dOkRGp_q16TTE9ArXGzuslqqOuyQDEUyDa6fjP4zf5fFudZnBtA4IbCo77-1cjZNUvSqCyg40g1R_eDuU05QO0hT-1R_mhv-RSeoxbB023nnDeOlmM0ZFXh5RS9pbS9th8b4GZZTakEoymFuQuAxsBzY2S0zGzrPws4a6LLasDFttpVAnoDm0IChTKDY5UTn1-WpeFywLUvYzD8uNEDPgeqKXunYiT39vGmbKa62wKksYni3nmXAofNP3y8M-TnV8dBMGGdCgt7j7nreFwEKWClqH2LaF_Vbus_OC8QEJ6IoLYFDAr5jUP7WVXSdISCIsCbUkn0mnxAWW-kUBc-jHOx81745MnaFBoZVwN-gH3gTDDEfMG2SWmwukK6PIAzvPfbu2yuLO8YY0H_5Z1EWPdPpLlrSE2kZszyL1DcJH9i2J1_9no_Ci7VLf-uTuInfhvi9dH_ZxMI9_6bXAk5l0h9qaO26vjtNar3bRNnjPDj5d3yhFy-0813hPHJbMceHKu3RzDKzUnse9ChBALU5zVozMDkYYPB9akv2TPoxAfYdLNMs12exEd1DjcdvgzLpzlmS0ekykcAeftUcbD_Yn-KbfJ-qkTlQ4yw2tETdmFuE9vZTOQhC8zoOMftrS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید ایران با خانواده عازم نجف شدند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667965" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPjNFvTiFhX0UjKJN8s01PNa570pw6BQEMQJh6UMHsVfyYckgRWb1SCLAD9CRHu-G4LIhIBJ7b6sFfBibEUmI3rcHwhA-HKKo4HH-f2c05fhJRIS_ZCX-deDHi457OKXchgyth9ISgRxoCd3GHrWJTR4vwDaLMURJKXjOmFP4R2J4lruzz9w_XvnM-AThkT6CwJBjji5XfeT8voLYX7rLBG9SHiS2UZ_UXmtr4c_ydL1cJ7XXI89T62hH7Y3buKTHhKuriM01O8VjXNOAs9NbpQeCzp1LqWGor6l2363T0DAGAdgwCQHCQSorbS1eE66MNs4F5v-2RVV9Ez-LpI-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667964" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75695327d.mp4?token=fXj9GifYrv8WOi6Ww2GnVyWOEcBnBd_1m8kVC0UJhf0iiQu-q7MWAGg30Y1Hys2qM6jeGVHifuh6OlVZy9rMa9HN4WiBhdS2WC7axTz4JPnlGi8NDJFjhJ6awSCxb13-b3rjEIW1qk-G1OB50rlLhs50byGDtSjIGzYEgbzKyQI5e-D0m3hkgWHuMUMJ9k00j0wnSAR9pOpi5z7P0WFMfpXGJTQ3cQGe1rW50rihPTDElFyZmbWBTmDzhW908Ee35T7wH9_1ZSd_uqNy_-4GElg7vOf3yMrx7uZoJvIjLVxjdISi2YdBa74fYWZzxwnnI_MTZVKGHFBYCVhZNRMU5gjxcSzEwQDiAzbrTCrlLywA7Br6BpjPCGjwPdueJl_EE3KxeArQ98PFjLQfT4Z2w0MyO0QXyFsx5JIPQWjXPHbkM3KLgqah8J96A7VC9pcMi9rdeQrts4fRkO_vJRqudjDxQO069UVZXOGVAq-4o_4PjTsN-94u7evFDblExrxbVS4zhAwIgQ-O2jwJFQsbOjLzAnKMM6KlawXLlw24EPTPdCemeDISj39YnjFJRsuUpZTR7vs6MxSKCUN61M4mDlFJa0We_l7CWXmQ9JzuuW2F-ZaMJ5MDjBqwAam8BtCzkC8k2R-A4e_9_2A0W1aFfngCIk1k0Fi2GV4zujPItGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75695327d.mp4?token=fXj9GifYrv8WOi6Ww2GnVyWOEcBnBd_1m8kVC0UJhf0iiQu-q7MWAGg30Y1Hys2qM6jeGVHifuh6OlVZy9rMa9HN4WiBhdS2WC7axTz4JPnlGi8NDJFjhJ6awSCxb13-b3rjEIW1qk-G1OB50rlLhs50byGDtSjIGzYEgbzKyQI5e-D0m3hkgWHuMUMJ9k00j0wnSAR9pOpi5z7P0WFMfpXGJTQ3cQGe1rW50rihPTDElFyZmbWBTmDzhW908Ee35T7wH9_1ZSd_uqNy_-4GElg7vOf3yMrx7uZoJvIjLVxjdISi2YdBa74fYWZzxwnnI_MTZVKGHFBYCVhZNRMU5gjxcSzEwQDiAzbrTCrlLywA7Br6BpjPCGjwPdueJl_EE3KxeArQ98PFjLQfT4Z2w0MyO0QXyFsx5JIPQWjXPHbkM3KLgqah8J96A7VC9pcMi9rdeQrts4fRkO_vJRqudjDxQO069UVZXOGVAq-4o_4PjTsN-94u7evFDblExrxbVS4zhAwIgQ-O2jwJFQsbOjLzAnKMM6KlawXLlw24EPTPdCemeDISj39YnjFJRsuUpZTR7vs6MxSKCUN61M4mDlFJa0We_l7CWXmQ9JzuuW2F-ZaMJ5MDjBqwAam8BtCzkC8k2R-A4e_9_2A0W1aFfngCIk1k0Fi2GV4zujPItGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت آخرین سلام...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667963" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc227c095e.mp4?token=At3n8G7NLuIQDjhan6MVuBBBYOApL3QWKb1Y0Uvp8VBZT8Nge2dvr8bU5VgiQziMbJ0s6ivlwaoiyDbWS-VCy13SG_ei613dEmNuWEsHr_lD9AAyceMlkz8QHQXGDwY2tsrQrhIoflakIj2laeo_pbpy7FIsJuBEaeC7i95UJVNiaO__JPnPNymY_mLfijnS5Ily9g6fYVBw4mDHLTyz__ZWPgvgdiLc0og9mcw4JRCFKVbk0DGeUXrrtm6pwJ-_gk5M4Kputc5hXeh9MwIvdZ2z2qN1l5yowfviIsXuiMsus6C8M3LVRcDI9XlEbO-3BlOjKl720RyTv8w6e7z6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc227c095e.mp4?token=At3n8G7NLuIQDjhan6MVuBBBYOApL3QWKb1Y0Uvp8VBZT8Nge2dvr8bU5VgiQziMbJ0s6ivlwaoiyDbWS-VCy13SG_ei613dEmNuWEsHr_lD9AAyceMlkz8QHQXGDwY2tsrQrhIoflakIj2laeo_pbpy7FIsJuBEaeC7i95UJVNiaO__JPnPNymY_mLfijnS5Ily9g6fYVBw4mDHLTyz__ZWPgvgdiLc0og9mcw4JRCFKVbk0DGeUXrrtm6pwJ-_gk5M4Kputc5hXeh9MwIvdZ2z2qN1l5yowfviIsXuiMsus6C8M3LVRcDI9XlEbO-3BlOjKl720RyTv8w6e7z6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کهنسال عراقی: تحمل دیدن پیکر رهبر شهید انقلاب را ندارم؛ خواهم مُرد اگر پیکرشان را ببینم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667962" target="_blank">📅 18:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBGNQQ5JW_fAPDxBjgowLS32M91GkuGD-bv0fnyjFp47hkBtEHBdLOnrgVCYQGWMI_dlvD8vB4AN9OWMVU42M-IvfP9616Oc_ZO5sV0jom_VyIZOMiSLJPpdyGgDj3lX0FQwr-_sLxds-YwbjAP79bCgS6YpNCNz9bkgCCNw40D1IXli688mdjyKLAF9ZFT6CL2dhIKqr2kzrxNOlCxJaT8SqbpJ6E3JTc_wUCu8mFv-YAi81aa3d4hLH5W_dyCgSuHlmyEEf9krkd74vkCCnkNCpd2VKkf5urOJ_C6JRV1WIOW5f7sTIDvt8sB1F1NxawhZa4HKXvmGG36FfYYz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این قسمت تنگه هرمز می تواند باعث جنگ مجدد ایران و آمریکا شود
🔹
اگر آمریکا و ترامپ همچنان بر سیاست "توافق از طریق قدرت" تاکید داشته باشند و نظامی گری در آبهای جنوب ایران را دنبال کنند، احتمال وقوع جنگ یا درگیری دریایی میان ایران و آمریکا زیاد است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3228576</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667961" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0c62e445.mp4?token=IxGzt40c9EyCP-_Gjqg5WTpkU_MBLubAYVlQk49V4d2N6lHwsvdM32fivNfnAStKPMIcyAuMwzzFGRGsBbVnFRAemmZpLN5nXGVyEr08ibVDg59ydGirGx2-m7jtsAC9sT0kCku25cD7vJI9iILg1GZsra88ijUSofd4lhFiYlkAZe6nq72Bt7-6nvgnZIOpbGQUdD25hNl69pdwZ_XFwyZMHx2Z5ScA7mLcK6Q4t3tFclOn05W5PGX4TguaJhRZ1ze77BHuwJ1O5l4FPWUM0NVZ2w2lrMjE_aBJVxpW3VAMPKzBbjvdNZdpEcrahF7N0YuwSBpPgNAGZGEoieoBmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0c62e445.mp4?token=IxGzt40c9EyCP-_Gjqg5WTpkU_MBLubAYVlQk49V4d2N6lHwsvdM32fivNfnAStKPMIcyAuMwzzFGRGsBbVnFRAemmZpLN5nXGVyEr08ibVDg59ydGirGx2-m7jtsAC9sT0kCku25cD7vJI9iILg1GZsra88ijUSofd4lhFiYlkAZe6nq72Bt7-6nvgnZIOpbGQUdD25hNl69pdwZ_XFwyZMHx2Z5ScA7mLcK6Q4t3tFclOn05W5PGX4TguaJhRZ1ze77BHuwJ1O5l4FPWUM0NVZ2w2lrMjE_aBJVxpW3VAMPKzBbjvdNZdpEcrahF7N0YuwSBpPgNAGZGEoieoBmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج بخشی از ناوگان سوخت‌رسان تانکر آمریکا از اسرائیل
🔹
تصاویر ماهواره‌ای نشان می‌دهد از حدود ۷۰ فروند هواپیمای سوخت‌رسان مستقر در فرودگاه بن‌گوریون، ۳۲ فروند خارج شده و در حال حاضر حدود ۳۲ فروند دیگر در این فرودگاه باقی مانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/667960" target="_blank">📅 18:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
درب‌های حرم رضوی بسته نخواهد شد محل دقیق تدفین پس از تصمیم خانواده اعلام می‌شود   هوشمند، مسئول روابط عمومی ستاد بدرقه امام شهید در مشهد:
🔹
محل دقیق تدفین رهبر شهید، پس از تصمیم خانواده اعلام می‌شود؛ مکان انتخابی به‌گونه‌ای است که بانوان و آقایان به‌ترین…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/667959" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
نقشه راه وداع؛ سفر یار از تهران تا مشهد
🔹
از تهران و جمکران تا کربلا و مشهدش
چفیه بر دوشِ امت، بارِ هجران می‌بَرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/667958" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای دبیرکل ناتو: کشورهای اروپایی کمک بزرگی به آمریکا در تهاجم به ایران داشتند
ادعای دبیرکل ناتو:
🔹
امریکا احتمالا بدون استفاده از اروپا به‌عنوان یک سکوی بزرگ برای انتقال قدرت نظامی، نمی‌توانست عملیات علیه ایران را انجام دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/667957" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d8d13909.mp4?token=fSQxRkFpe0yb5gSH-9KxT5piIZ8-lWpPy-JeUp2l0VRJqNfsp76wKtbDqGhj_DPcASjmIKj_XY9s_C6TVJ1SxnQVZWU2ApzVd9kwRKkeM9vunvWZ7xYUpyQUaAkQIXjwZJXdvie8KXR_AfVvLgMZCPCMW0nr67e33T1QkFDi-Dd5ntswucP200CM2jF3-kXaVUUp53twAggqvngRHXjhlXbhAWtuyQNN4BtQrTl2jn97DDm1ILo6v13h6Ggl1eRtuQGR8jt-JomZKboffjesZ8uP5kgS8Fb3G1-UYEux-YbH1RA8T5FmmdK_5Aj-t2e9AWdbAkMtNALwUkaU81A6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d8d13909.mp4?token=fSQxRkFpe0yb5gSH-9KxT5piIZ8-lWpPy-JeUp2l0VRJqNfsp76wKtbDqGhj_DPcASjmIKj_XY9s_C6TVJ1SxnQVZWU2ApzVd9kwRKkeM9vunvWZ7xYUpyQUaAkQIXjwZJXdvie8KXR_AfVvLgMZCPCMW0nr67e33T1QkFDi-Dd5ntswucP200CM2jF3-kXaVUUp53twAggqvngRHXjhlXbhAWtuyQNN4BtQrTl2jn97DDm1ILo6v13h6Ggl1eRtuQGR8jt-JomZKboffjesZ8uP5kgS8Fb3G1-UYEux-YbH1RA8T5FmmdK_5Aj-t2e9AWdbAkMtNALwUkaU81A6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودنمایی پرچم ایران و عراق در خیابان‌های عراق در استقبال از تشییع رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667956" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXDKhxmhbyMQ4LhHnz5IlAoZ-ZBSSkIHQIGPohscRDDIt5-3vz5q47yL-SLNsB9JJW-fbWY2VIMxqQ5WDQyobpfk-Ruc2hKViP36o5s3mwC7Ywe2yy90dVBL8ROJ_Ygt5W3efBx43GkwAK0Gux4jU6rBSXaXxYWHFhv9iPUfT1V8bdmHa44Tn3IeqjlT6bXQ_Z-0H8twTzTlGbcqlrb0FgC0qMhPO2_qQkympYL2zK6NQ9mSb8fzbOOJ5L3WBQkCDmxXp7HOj6wMT9ei_q0VcBvMLohDQdhZ6fagyPLnOvy3zL15azJglmhAOd34Y1U2ZNBpeKwfYq7RocYjHiD9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسیب به یک نفتکش در پی اصابت پرتابه ناشناس در تنگه هرمز  سازمان UKMTO:
🔹
یک نفتکش در پی اصابت پرتابه‌ای ناشناس دچار آسیب ساختاری شده است؛ این حادثه تلفات یا آلودگی زیست‌محیطی نداشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667955" target="_blank">📅 18:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06f7a165e.mp4?token=acE3uBAAsNktrE6GT8j9ARgSqLAQ_KSIuojGkf4ilbYQfTQ53GQmj5B35q47zdq4ZSOaprRt3Z9sndoR39_eyhV7RG2hkSNMd3tRm6QZA2ThqXATUraz0DNztOwFdv_GqSOruaf0XrpjwPpxs_6J86t9g9g21_Lu4F-nQrTh7xc9i_gI1j6Vje2c920jyOLH_EgYfV-FAUBxN3ljugf1zA_G1opmyigGBcFvGPgvY588txMyXbCa9D7lwZlZUvu_nufdenEj1czmCtFu4dujZfdufJ_pH80uro_PR5KSTcRXJ4ShCnXXRCo4PJm-7_UNjinm1jnBYy4dI9vvMYHZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06f7a165e.mp4?token=acE3uBAAsNktrE6GT8j9ARgSqLAQ_KSIuojGkf4ilbYQfTQ53GQmj5B35q47zdq4ZSOaprRt3Z9sndoR39_eyhV7RG2hkSNMd3tRm6QZA2ThqXATUraz0DNztOwFdv_GqSOruaf0XrpjwPpxs_6J86t9g9g21_Lu4F-nQrTh7xc9i_gI1j6Vje2c920jyOLH_EgYfV-FAUBxN3ljugf1zA_G1opmyigGBcFvGPgvY588txMyXbCa9D7lwZlZUvu_nufdenEj1czmCtFu4dujZfdufJ_pH80uro_PR5KSTcRXJ4ShCnXXRCo4PJm-7_UNjinm1jnBYy4dI9vvMYHZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی شبکه «الجزیره» از تشییع میلیونی رهبر شهید در شهر قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/667954" target="_blank">📅 18:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d4fb6fd0.mp4?token=kEn3Fn9-46w5ImzBaoB1r6RmsPxGqQMvqpsz2YbLjx1jX0HfTEiePxG_Zp9UQgjJTVSxlBD1SccQsVosLY82jds6_SdCiWXfGX6AWF68RbOGjAfjEXtgVACJrNwCEfrHyJNEHL1Bh44602DrrY2f6vnEo9y8YXye92tWjM_hm1sf4XSDLHVUo-gtsmZsxphWlhOUwT9qRz4I5qHLpP-ylqVQpjVt4ZpXCdPJDbMlzSJQNFogDLD9GrLVNTB6ql1oBbzdckMqdQzb1d7T89TRAE2zUoLicfZcl2xc31fzU9yqi1xLMbNav9ohcW_RlGhKfkT6MjQ1CDtbWzGG-iT6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d4fb6fd0.mp4?token=kEn3Fn9-46w5ImzBaoB1r6RmsPxGqQMvqpsz2YbLjx1jX0HfTEiePxG_Zp9UQgjJTVSxlBD1SccQsVosLY82jds6_SdCiWXfGX6AWF68RbOGjAfjEXtgVACJrNwCEfrHyJNEHL1Bh44602DrrY2f6vnEo9y8YXye92tWjM_hm1sf4XSDLHVUo-gtsmZsxphWlhOUwT9qRz4I5qHLpP-ylqVQpjVt4ZpXCdPJDbMlzSJQNFogDLD9GrLVNTB6ql1oBbzdckMqdQzb1d7T89TRAE2zUoLicfZcl2xc31fzU9yqi1xLMbNav9ohcW_RlGhKfkT6MjQ1CDtbWzGG-iT6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با انتظار و اندوه آماده خدمتیم...
🔹
روایت موکب‌دار عراقی از آمادگی برای خدمت به شرکت‌کنندگان در تشییع امام مجاهد شهید در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/667953" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مسیر تشییع رهبر شهید انقلاب در عراق
🔹
مراسم تشییع در نجف در مسیری حدود ۵ کیلومتر و در کربلا در مسیری نزدیک به ۷ کیلومتر برگزار خواهد شد. همچنین پیکر مطهر در مسیر زمینی نجف تا کربلا، در امتداد مسیر پیاده‌روی اربعین، در نقاط مختلف با استقبال عشایر عراقی روبه‌رو خواهد شد؛ استقبالی که نمادی از ارادت، وفاداری و همبستگی مردم عراق با این شخصیت برجسته جهان اسلام خواهد بود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/667952" target="_blank">📅 18:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrIfwBZzBnma0F3_En0NBxzbup7Lf2eeZTC2ZVPQWvRnK3oLgUT4MfugK6XbbqMbQ9R2qumdDwCeJ2PQAwqu3Yp0d8lchkinJEgcwT9rKKil24yLg84UfFXGAQ7MnpQqzBNYtAfgdeCFAijIN0efXE6Vb53tvCG4IImEuv6BAnexT3Fgslq8ykaIFVI2ZsIIO9ASburZHLn7N2dJH8A_tiav_CNqJP0boDjCoJmhUy8fGkifEGqGE9t2WYnTPl1rTO47aoVFGS4xh-LOZJ3lqdTXzqPbV5D0CipccnpEQlUyaz2Js-DvYZanxiVSgw9mufRnMjLuEK0YmAoLoY72og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛ «بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافی است آخرین جمله، پیام یا حرفی را که دوست داشتید به رهبر شهید بگویید را در قالب یک فایل صوتی (ویس) برای ما ارسال کنید.
▪️
صدای شما، بخشی از بدرقه ماندگار مردم با رهبر شهید خواهد بود و می‌تواند روایتگر عشق، دلتنگی و وفاداری شما باشد.
▪️
فایل‌های صوتی خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667951" target="_blank">📅 17:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCSRJCo9XY7xGHFoOvr8rAByBYMv1G2s_QVwHlRpq6-LMYNzV2XMdUK1AP1mP2L6OqcDxvYtuQH_hXh-quAK-F5oq34KeVxBul5Jw8Drc8OeH-WPYjpELLrRmf1nzQvHH6wEiqBg5pBEKKQXgxAKg3NNvETI-yDO0F4Ii9TEdX6MVxqZ0ic_6aRTnogBmhgIgHPt6qU670IbhOXY6mMG7fCR2m-ktj8SP5NnwvFiy4RF8bOG6GX9ei3A7tSxeI4I8FCtO8YGfNMvjKeFCQDS2U-cTC4eekptxMF_3Rf4SgtQbt5Okch-v5RqJo_oBqO3fR2iitUOYyEtypHGrtzoQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی رهبر شهید نشان داد این ملت همچنان پای خون شهدا ایستاده است؛ همان مسیری که هر سال در اربعین از عاشورا تا ظهور تمرین می‌شود
🔹
حالا نوبت مسئولان جمهوری اسلامی است؛ خونخواهی رهبر شهید نباید در حد شعار بماند، بلکه باید متناسب با این مطالبه عظیم ملت پیگیری و محقق شود.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/667950" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIbxnzxU2YUDZG2QC3EPGblMCT5jtRDkPt-fiCpm75j4HBunyyf-Dr0WtRUdjwoccA-zGHn2P8BLmucpbpK4ZoZF6PV3WG5GOx37-jWPZt0apTJ643PUt_5wS_z1kVCyiaP79c7mAUQ_2qBQBuLImUz4RDpGetxPoxkFtgCAS-N5dg7-rNkqvcO88VhdnRoRlRBuu7FxHJ0ozBuE2xOq5TscSaWAHBpJSgGI1e5T7xaLtT-RaSoyMkRQ81uzKcqcXlCxujnwEDrV1gkBK389FfpNsZKvYX-x3YfP5OS_FcG9gir-ThSwH4MY9izDlQ4a11fNyYFFih6DTRazmhGmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1ZZRIhgJGpiupeZs7l3ZAZwPEFXURENg56Y_Ek2_2t-HRf4qdOl7djJTRyc64iVWUjWfupnCBQH6YcIh_pWE425Chc5TWxwIrIf85a3iSyPj0nqdQ8ak45dYvw_wmUy2ze272B5ORjMB05mMIt8nsFr2jCZIlg6z7xl_gW8ny4KUph6PeWkMOPLsbErGVge6oCZAWAemSg_Ud0TZHgB4MS-ngrMrOVw3hX9zUFvv7roa2hBq-vzcFjOFnY86jz0U0xQXMMeM5cshMO19W2nQvda61K_bsyS2HVu3Z-28V02NVwJhR4IvGinXAzy36NoGZ_58-U89ymK_sQp6g6ITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnSnYMAmpIeBlgFsybeDB7UJCwzA-ey1isvH61Yp7WXK7yC-9cOqx91tESg0Hm4ee4ucZLuUMzQDnyFfP3uxI55GtgZowN04OJDpt05edxzcANTpd-UaXTam88HsjIznzU1OlanxPBE13x9i8lVUxdM5Jvy0CBQDpZXBJt5KtvzhAFmnp7Pfyolh7JmPDcyPInk8CqJi7g7S6LHNMXHWRXtaFYHsLr9TpmTl26HzEJg5xjv6k2CipxlANUeyvOUF5r-1pX8FZhuYHdv65RUq7J8-I7t52iLT3p6bxouYyKzKOFan9hfO4Q_YueC-cHO0PeD4o0MO7Pxb_G4BjmrCmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جام جهانی؛ حسرت مشترک رونالدو، نیمار و مودریچ
🔹
کریستیانو رونالدو، نیمار و لوکا مودریچ با وجود افتخارات بی‌شمار ملی و باشگاهی، در فتح جام جهانی فوتبال ناکام ماندند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667947" target="_blank">📅 17:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVRWI0fcASUouRXZd_0y-6DnSQ6deX-41xBj16xrYa6Zi07FSIS1Ls5vv4vvQFuRscgBm-kTETrcmcW6SbSvvo0cQbhKUFkOjRWZBMS8JoEFqd7aaSc0W7g5i8mKnBiKoay0RFtyHD2IcyY-TSX8VhpqtcGql7GJOUwJwjaKhbf13grr6FlnWrHeQGuo8o5cxtBcLanEvSFvHwPZitsAjP7Q_ph4kuWVcjdAgZ17C1FnrNvj-PECWWDYb2E0zic_fvQjBU0cHgnhaMaeh08odEXo84vRc5lFD0purd3wY7iNXYsHcYrvkxPue0NH-cqGNm5WMaJLwA69Na88q7nb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
رویترز تصاویر ماهواره‌ای از تشییع رهبر شهید را منتشر کرد
🔹
‏آن‌هایی که تا دیروز اصرار داشتند تصاویر تشییع را «کم‌جمعیت» جا بزنند، حالا با انتشار تصاویر ماهواره‌ای توسط رویترز کار سخت‌تری برای انکار واقعیت دارند!
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667946" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: پاسخ ایران به تجاوز، قاطع و متناسب خواهد بود
🔹
سردار طلایی‌نیک تأکید کرد ایران همزمان با پیگیری مقتدرانه دیپلماسی، به هرگونه تجاوز یا عبور از خطوط قرمز، پاسخی قاطع و متناسب خواهد داد.
🔹
وی افزود انسجام ملی، پشتوانه این اقتدار دفاعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667945" target="_blank">📅 17:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46f4e28af.mp4?token=kxsorSOywGx_d4IcZr1GXbxg8E6cqT2144LYTqje-rSQJ9zWer5Uyq4J5cyu1fNWKyr9BY9yh-WHngvTkWHalvRJhZ-NDqaZmnPQuzjKOX5moNPZ_TjDpxArv3O733QnYBTkFUjLCixglTg_J35wN5wLGDGCIayGtRgPfjlG1I4VTVsS6UGzQGkiUFtIA7ZmmoG2b5AzPEerh71ibIxkZticWJgu1Si6fq41FNIkRnI5o_RhtiwKxmxgdoWTb3e_7KHcpnzdIbEpxK98jHjQjAIDw51XLFBYBp4PqtTQV16CTtFWesDuui4VdBnQ4blINPC11aeFodMaXtlAgp375kR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46f4e28af.mp4?token=kxsorSOywGx_d4IcZr1GXbxg8E6cqT2144LYTqje-rSQJ9zWer5Uyq4J5cyu1fNWKyr9BY9yh-WHngvTkWHalvRJhZ-NDqaZmnPQuzjKOX5moNPZ_TjDpxArv3O733QnYBTkFUjLCixglTg_J35wN5wLGDGCIayGtRgPfjlG1I4VTVsS6UGzQGkiUFtIA7ZmmoG2b5AzPEerh71ibIxkZticWJgu1Si6fq41FNIkRnI5o_RhtiwKxmxgdoWTb3e_7KHcpnzdIbEpxK98jHjQjAIDw51XLFBYBp4PqtTQV16CTtFWesDuui4VdBnQ4blINPC11aeFodMaXtlAgp375kR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد فعال رسانه کنیایی از سکوت جهانی در برابر حمله به دانشگاه‌های ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667944" target="_blank">📅 17:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823df792ac.mp4?token=WdIUwGPS2SsJcdjXD_5TWzcO8oeHIJu2RJpajg36SBpA4pYAFqHTnsw3-jSGO6SOOKfMftmrJ6C-axgGrIA2np3-LqXWS-F7DGwAXt6-fcHvfk-ZDoADE3neKLBfGPhZs4rCX_mMzskjWhU1IDlkB0kl3xfoYldNKEPMZJj9lsQfC_MQ8K4_4swGkYOqxQbTqy4QooVzCVInBa3CSo578mQ1M4WPgDfmMFe15jiBWgp-C_KzdnXFvGgwWtlBvt5eqML9UK_v8XO-ivvwJPAo23gnaURxkd_EzfCFY04yKfEP5j8iXVyWyZ5yfro5PGNzb6tZ8RUASFoa4SNzia6mHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823df792ac.mp4?token=WdIUwGPS2SsJcdjXD_5TWzcO8oeHIJu2RJpajg36SBpA4pYAFqHTnsw3-jSGO6SOOKfMftmrJ6C-axgGrIA2np3-LqXWS-F7DGwAXt6-fcHvfk-ZDoADE3neKLBfGPhZs4rCX_mMzskjWhU1IDlkB0kl3xfoYldNKEPMZJj9lsQfC_MQ8K4_4swGkYOqxQbTqy4QooVzCVInBa3CSo578mQ1M4WPgDfmMFe15jiBWgp-C_KzdnXFvGgwWtlBvt5eqML9UK_v8XO-ivvwJPAo23gnaURxkd_EzfCFY04yKfEP5j8iXVyWyZ5yfro5PGNzb6tZ8RUASFoa4SNzia6mHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667943" target="_blank">📅 17:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
ایلام: چهارشنبه
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه و چهارشنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران: سه‌شنبه و چهارشنبه
🔹
هرمزگان: سه‌شنبه
🔹
کاشان و آران و بیدگل: سه‌شنبه
🔹
مرکزی: سه‌شنبه
🔹
خراسان شمالی: چهارشنبه
🔹
بوشهر: سه‌شنبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/667942" target="_blank">📅 17:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM1le3U4qbxRQBoM0JRQjEJDTAX4vGcMKJw4l5-nPe_--1wAO2MwFjtptKA5L0dMyVdWMxaeHs3XNA9lp8ibLF0WHxTbp5GIne3NPPGglWKKQETmM2du36gYUfj8zO7XNueX7tMoBjFd-0rjhgLl-u0yxU3BcLPRKuxMk9VUWzaak-PRMse3d4nfubuFK7DKawHFySDvVa7pNpAu7FPEHJGJ6uvvV5SfgY4xoJzrFthwzw62CNIsPFo-RNpcDXkKeur0Lcd_1MPxjlcnkWjBI5HkLR6hcGzRIXnLiJUgKEtBztpAKjPpv2usJMomcZB2UZoPd2-bzSOJezhffpG-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین، شریک اول تجاری اکثر کشورهای جهان
🔹
چین اکنون بزرگترین شریک تجاری ۱۵۱ کشور یا تقریباً ۷۳٪ از جهان است.
🔹
این کشورها ۴.۶ تریلیون دلار تجارت دوجانبه با چین دارند، در حالی که این رقم برای ۵۷ کشوری که تجارت بیشتری با آمریکا دارند، ۳ تریلیون دلار است.
🔹
ایالات متحده همچنان در آمریکای شمالی و بخش‌هایی از اروپا قوی‌ترین است، در حالی که چین در آسیا، آفریقا و بخش عمده‌ای از آمریکای جنوبی تسلط دارد.
@amarfact</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667936" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199917ddae.mp4?token=FqaH984TF6PFN6lJyl9qlDYHpCq8q7iA3Prv_RN4goxzAWIJ5L5gWO3h4fIYARTV4InjrSqXkbVWoCrZTTrJD8cMQC5hw5J_SkJ9s4lWTTizs2DSaon55aRf1VkHy7uRr7080D_aw7LRERxzJoXtWecMQObkdyYZtZi42xwm0Qkhh6JW7WoRgGezcLeHcQQ8t7sFkm5b65xWXYFK2HzVw3B7k_unNiBZjPgmXeASidwdySRwuKWrCNU7ysMR1mHj_PK4RsdjTqMVZ3xhyliLH4OokLIYCaYbb0wmPacHTxwLja248PENtcmgBgtz1xQPe8kJhrXOYXiZr5fmSQM_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199917ddae.mp4?token=FqaH984TF6PFN6lJyl9qlDYHpCq8q7iA3Prv_RN4goxzAWIJ5L5gWO3h4fIYARTV4InjrSqXkbVWoCrZTTrJD8cMQC5hw5J_SkJ9s4lWTTizs2DSaon55aRf1VkHy7uRr7080D_aw7LRERxzJoXtWecMQObkdyYZtZi42xwm0Qkhh6JW7WoRgGezcLeHcQQ8t7sFkm5b65xWXYFK2HzVw3B7k_unNiBZjPgmXeASidwdySRwuKWrCNU7ysMR1mHj_PK4RsdjTqMVZ3xhyliLH4OokLIYCaYbb0wmPacHTxwLja248PENtcmgBgtz1xQPe8kJhrXOYXiZr5fmSQM_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آماد‌ه‌سازی مسیر تشییع پیکر امام شهید ایران، در شهر نجف
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667935" target="_blank">📅 17:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307de30ab.mp4?token=KvBNRGOrFLHm1phpAdpikin0K-ZRK6yj0WRA0KsZSC-8gCh6awJcLEs6nVFRZO-0X7cuxD6y_KcFWCsAPuNcFamt03GX7GCvwl8IivDkUAgnbfYG9SGVV8MFLyiX3fDzr8NQIp6IIJuJv7TtajCh0aElbIPmkJ4XCFPerQIosMwz1HLWCxdrFcs0wa9M59bCOgMDCLWy6YeafKh2LUYw9OqpNhgbve245ts0nBCEcAi60F8wrrfTiFyIoyScEmvqHgsVjpOU0Bv_Y60vwtSWsOgXJHsNvqE9ga4MmjwvuyvvB2P2dDCUk4G7unxtdYKFtmVm-mzbvDojV2IVJsnTtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307de30ab.mp4?token=KvBNRGOrFLHm1phpAdpikin0K-ZRK6yj0WRA0KsZSC-8gCh6awJcLEs6nVFRZO-0X7cuxD6y_KcFWCsAPuNcFamt03GX7GCvwl8IivDkUAgnbfYG9SGVV8MFLyiX3fDzr8NQIp6IIJuJv7TtajCh0aElbIPmkJ4XCFPerQIosMwz1HLWCxdrFcs0wa9M59bCOgMDCLWy6YeafKh2LUYw9OqpNhgbve245ts0nBCEcAi60F8wrrfTiFyIoyScEmvqHgsVjpOU0Bv_Y60vwtSWsOgXJHsNvqE9ga4MmjwvuyvvB2P2dDCUk4G7unxtdYKFtmVm-mzbvDojV2IVJsnTtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: اروپایی‌ها به ما بدهکارند
🔹
اروپایی‌ها باید از ارزش‌های اصلی‌شان، یعنی حاکمیت قانون در عرصه بین‌المللی و حقوق بشردوستانه بین‌المللی، دفاع می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667934" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT2mM6EIsj8b1eYHXCOFlKzVMgdqdbUpnEYie9XkFOiq_8bXTkhP_QL9q_hrfNtOLuTTNZUhRWVEI2z99tURi2D4fR9nNq1XdbJgZGZdG5nrUzFyuugr7YP1G5JI0iUdlTA-r_hesnRy1DR5S1A7158CTYR4KMlyPj7eCj6Bu_7bQxpFQdxTSrGlHrHsMPjhE9U-WKrIyHyWTrWsqwdayq6vkz7X6FIx3NfKLNmJ7C7RYcTbHuAHU0x2xDP9NQ2ThYkwcFIJSDip7Y_oLo_lmZGeFIp7YzkYB1r-SNR1YHyYv8VZbW2yk8RReXQPAgveM0mMCIAlYdQ1WeLDCG0B_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فغانی؛ داور فینال جام جهانی ۲۰۲۶
ادعای سی‌بی‌اس:
🔹
علیرضا فغانی، قضاوت دیدار نهایی رقابت‌های جام جهانی ۲۰۲۶ را بر عهده خواهد داشت.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667933" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGgWEgmEWxEU_ZdzviBEPSXQxSW7raHXwtgveswKVOqspkqkxgcjBkoHfuH5XmJW8vBnhn1uLq2Ospv1BjncAbNguMqrd-QJB06oFT5pdtS_fFpHItUnuaAKzN4iOo1BiIgcveLpKezRyoPpE8Ly3vjWH-pZsyFExA1e-7ZdvtcDo1FNSeHnKWhSugHGlnGxG58wtPFrp5oY5i42Las0Jve6oQUcD20t4c1qTD59S2YcDAnDoR9ri8XtCJdrUkn3oI_uIkW8ZH_0oLwqDzX8oUYosYgJVEHy7v4IIv_EnRk65v5XwlLNAVVWctRoFqMtDfe89EGeDJHgUH33sGaldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسیب به یک نفتکش در پی اصابت پرتابه ناشناس در تنگه هرمز
سازمان UKMTO:
🔹
یک نفتکش در پی اصابت پرتابه‌ای ناشناس دچار آسیب ساختاری شده است؛ این حادثه تلفات یا آلودگی زیست‌محیطی نداشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667932" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLZ99yqcpSsQc7NdBFWJIc_TaPGTa1DIUPR00_TVCuxiTqsdxnCglNUekVW-mKK9RfP-Dc6AsrMWsC_AnvHfs7M9EAg2XjVyixsyGK4ZF8wawWKR1vgkYA6TCyZRfKLJyOjEtZko7h-B-6TpGCI41frreAXNpQTZ5a9MxorTdB98OqRQS-8eduzFfLAsTWLpGpV3mZgdODKnNoidNbkZC_XTaFo6imEp7TA1AaFUz6ReXf7thf0fsl4wEFzp4EPyGJEwvWym2wQbg9hFJSd_ar0_o8ttuLwrw1xNc7Qj3vRI6mtOvnsmYjaMN5yJKvqL3PBxbqfIq2FXNv0Kqw1U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسمان قم میزبان طواف پیکر پاک مرجع شهید شیعه، بر گرد مضجع شریف کریمه اهل بیت حضرت فاطمه معصومه سلام‌الله‌علیها
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667931" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ4vdbaQrDrHx_PnFVBnVb84_IMaiIKoZNTt8PryaCGPrUmQroKQXdhzKBwVFn_m2V77-rJ5SAxaShJ2BpzB9CNDNYp6yOeMPHuzHxfRY-4_BJ3RjE7hjFrMSWfTGm-uLiBZRtBcIOT-BrwyJpeNIkbUZH3kAVAliXe3udOWH3EXHBlyMvwRLhE_6lC-tuD3CnQXOcgvWk_2gm_2nrt3wuea5yOLSvmt2BqLt305CiPGXlgQZkPPnHJA1UTV5wiS27aXoNUuF1TirzGl63S9j49JypuAKV7s3q-OxTHBIWuBYJUzygrKtOr3Ri4bSucCa2QOEDJOFZ2fRB_vcmmV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: اتحاد ملی و خوداتکایی، میراث ۳۷ ساله رهبر شهید
🔹
اسماعیل بقایی، سخنگوی وزارت امور خارجه، با رد روایت‌های غرب، ملت ایران را تمدن‌ساز و مقاوم خواند؛ وی تأکید کرد که ایرانیان تحت هدایت ۳۷ ساله رهبر شهید، به سطحی بی‌سابقه از اتحاد و اعتمادبه‌نفس در برابر فشارهای خارجی دست یافته‌اند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667930" target="_blank">📅 16:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb25b6c43c.mp4?token=rr7it7N-lNOhxkU1MqPUkZoatyJ_m3glSPMDxCLMxkoh5rKaabxVBtqQHbcz72teGiVpvN9yGfyEHkJd8TvSzUca6Q7FTZS6O4ToeptWpuGu-inryI_rJY2PsQ2lhcwKzdNXrb0MivOCJVH0f-HDrwQKIOocjkQdMOw54ZmHTAJoSsRA7cWPDfweQ6GAaaLmjodURItYABv_DVHxn_y7vDM_Jt0hJbKmgysPYsw1ivJ4UneRG0R9L9zpiOtlOCmpM0EZGzy6Ik-0TdyZNVf2Z0vW9C9GZl9vT1RCPKp4ZXkmBC0lFUaTZa27hZSzH03R6_3MFRvuHTtsx0BMB2lA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb25b6c43c.mp4?token=rr7it7N-lNOhxkU1MqPUkZoatyJ_m3glSPMDxCLMxkoh5rKaabxVBtqQHbcz72teGiVpvN9yGfyEHkJd8TvSzUca6Q7FTZS6O4ToeptWpuGu-inryI_rJY2PsQ2lhcwKzdNXrb0MivOCJVH0f-HDrwQKIOocjkQdMOw54ZmHTAJoSsRA7cWPDfweQ6GAaaLmjodURItYABv_DVHxn_y7vDM_Jt0hJbKmgysPYsw1ivJ4UneRG0R9L9zpiOtlOCmpM0EZGzy6Ik-0TdyZNVf2Z0vW9C9GZl9vT1RCPKp4ZXkmBC0lFUaTZa27hZSzH03R6_3MFRvuHTtsx0BMB2lA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: من از ناتو خیلی ناامید شده‌ام، ناتو [در رابطه با ایران] با ما رفتار خوبی نداشت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667929" target="_blank">📅 16:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به افسران تشریفات ارتش ترکیه: مرحبا عسگر (آفرین سرباز)
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667928" target="_blank">📅 16:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعاهای تکراری ترامپ: ما توانایی‌های نظامی ایران را از بین بردیم و این کشور هرگز به سلاح هسته‌ای دست نخواهد یافت
🔹
من ۸ جنگ را متوقف کردم و معتقدم نهمی را نیز تمام خواهم کرد و امیدوارم که به‌زودی به جنگ اوکراین پایان دهیم./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667927" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای ترامپ: ترکیه به لطف من در جنگ با ایران درگیر نشد و آن‌ها نمی‌خواهند ایران به سلاح هسته‌ای دست پیدا کند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667926" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خودرو در دمشق همزمان با سفر ماکرون
🔹
انفجار شدید یک خودرو در نزدیکی هتل «فورسیزن» دمشق و برخاستن ستون‌های دود از این محل، همزمان با سفر رئیس‌جمهور فرانسه به سوریه گزارش شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667925" target="_blank">📅 16:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای اردوغان درباره تلاش ترکیه برای میانجی‌گری در روابط ایران و آمریکا  اردوغان:
🔹
ترکیه تمام تلاش خود را برای بهبود روابط ایران و آمریکا و پیشبرد صلح جهانی به کار خواهد گرفت.
🔹
وی همچنین از برنامه‌اش برای گفتگو با ترامپ درباره غزه و امیدواری به دریافت جنگنده‌های…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667924" target="_blank">📅 16:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667923">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ترامپ: احتمالا با اردوغان درباره ایران هم صحبت می‌کنیم/ روابط ما با ترکیه در بهترین دوران خود است #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667923" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667922">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667922" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حمید گروگان، از کتابی که موجب شد اشک‌های رهبر شهید انقلاب جاری شود
🔹
در قاب《پشت جلد》از شبکه نسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667921" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667920" target="_blank">📅 16:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تعطیلی سراسری عراق همزمان با مراسم تشییع قائد شهید امت
🔹
علی فالح الزیدی، نخست‌وزیر عراق، دستور تعطیلی رسمی ادارات و مراکز دولتی این کشور را برای فردا چهارشنبه صادر کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667919" target="_blank">📅 16:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
ایلام: چهارشنبه
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه و چهارشنبه
🔹
سمنان: سه‌شنبه…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667917" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش قدرت هوایی ترکیه در آسمان آنکارا؛ جنگنده‌ها بر فراز ترامپ و اردوغان پرواز کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667916" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c99b8b38d.mp4?token=o7T929SgThYuYVv7lvFUyXG-ECTc_79OpYmRaZDKkv-bz5nnov7ZOs_N7ZaXsRHThKKO3arpu12_d34nQ8aNW5QiWTO3Xd2abMHeJbT3BtF2WTbDDsxdOu2x94p_svVVq879KB7V7eup2Gi3lFO0dECfKZd0PzNAZ8M_WI2ITesnzaAWL-4zwG5ywl92W_uS5XP0cwLV01XaLElTkxeAw69d4nPgfg3N24uH6rljXsNsYsgD_TkabJU0fPCEQg0OurfcIAAcmJvYZsD57xYN3Cn20LT9mLdeUwIjoW6OZNr1016mwRi_Y6xpycNyXDJ4QouZQdsgoesl1HqOakmPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c99b8b38d.mp4?token=o7T929SgThYuYVv7lvFUyXG-ECTc_79OpYmRaZDKkv-bz5nnov7ZOs_N7ZaXsRHThKKO3arpu12_d34nQ8aNW5QiWTO3Xd2abMHeJbT3BtF2WTbDDsxdOu2x94p_svVVq879KB7V7eup2Gi3lFO0dECfKZd0PzNAZ8M_WI2ITesnzaAWL-4zwG5ywl92W_uS5XP0cwLV01XaLElTkxeAw69d4nPgfg3N24uH6rljXsNsYsgD_TkabJU0fPCEQg0OurfcIAAcmJvYZsD57xYN3Cn20LT9mLdeUwIjoW6OZNr1016mwRi_Y6xpycNyXDJ4QouZQdsgoesl1HqOakmPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ترکیه به کشوری بسیار قدرتمند از نظر نظامی تبدیل شده است /مردم نمی‌دانند که این کشور در واقع چقدر قدرتمند است. آن‌ها سربازان بسیار خوبی دارند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667915" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تلویزیون العربی به نقل از منابع: لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده است. هیأت لبنانی به طرف آمریکایی اطلاع داده که بر حفظ مذاکرات در واشنگتن پافشاری دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667914" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
درب‌های حرم رضوی بسته نخواهد شد
محل دقیق تدفین پس از تصمیم خانواده اعلام می‌شود
هوشمند، مسئول روابط عمومی ستاد بدرقه امام شهید در مشهد:
🔹
محل دقیق تدفین رهبر شهید، پس از تصمیم خانواده اعلام می‌شود؛ مکان انتخابی به‌گونه‌ای است که بانوان و آقایان به‌ترین شکل امکان زیارت همزمان داشته باشند.
🔹
هنوز درباره اقامه‌کننده نماز بر پیکر ایشان تصمیم نهایی گرفته نشده، ولی نماز در حرم رضوی برگزار می‌شود.
🔹
تدفین اعضای خانواده در کنار ایشان برنامه‌ریزی شده، اما تصمیم نهایی با خانواده است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667913" target="_blank">📅 16:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رویترز به نقل از برخی منابع امنیتی دریایی خبر داد که یک نفتکش حامل نفت خام در نزدیکی عمان آسیب دیده است  رویترز همچنان مدعی شد:
🔹
نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667912" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8qk0n4ez5t4tOH3G-yA2h5haOm3FQUf5exfvH8_h_39OaUGits_OQq3uBkmMWF3AbV8n0EM5mCChOMHFk1cJJ2nbFp281LvKMbug9sP7UGJi_8VEL0t4LsTJZqOwNEFYgwg1iE_WosPqkPRnKDrS9o7ArDDObNwdvxB1kPQT-hI9eLjExzMUwpXbsFyaJYNUCYo3lfB8UUcW9r4_lPz_q-CXFyA1MFcRgy0ebGJVO6AQeNKfg2XOOuPqG8-jikDbxc1dUKYJydq7oi-xWVsf9UvR5slQchhguaFGQc4ISXEdt07g4PkpZoPYMx-vQQTQFOG51nBuYeI9Lxii24W9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه فیلمساز ایرلندی به حماقت آمریکا و اسرائیل بابت جنگ با ایران
تایک هیکی، نویسنده فیلمساز و کنشگر ایرلندی:
🔹
«آن‌ها تلاش کردند ایران را دچار تفرقه کنند؛ اما بی‌رحمی و حماقتشان نه‌تنها ایران، بلکه تمامی آزادی‌خواهان جهان را با هم متحد کرد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667911" target="_blank">📅 15:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
جزئیات جدید از حادثه برای یک نفتکش در نزدیکی عمان   صداوسیما:
🔹
به گفته برخی منابع، نفتکش «الرقایات» متعلق به قطر، قصد داشت با حمایت نیروی دریایی آمریکا از مسیر عمانی در تنگۀ هرمز عبور کند، که پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667910" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667909">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=sQZtTVa5yYUXwScvsc5SRhSDNWpRWtUFHyrnddAttUxaqRY4xRU9OmkTXdG5hXDfOQeIo-Vn_aF3guzpCmX5-IS9dkgkDgUbEEIvOuBZI4KiMJx3rBrVwh7fRIYaYu5OWV6jJhtL3OfBYyd0CIiI2xJ4G6i12gBCnIjWztjNTBxHO8IhtL_Evd6cmdoPH8ppqfoKeRkM6cE113YU5YhL9MPkbMp9_I1Q4OIqioqd7kzQaEEdMjZcMfHulRBJaC8Pz2ezPT-wUzx4eqabFoXIvOdmPfUGsalhrFMJ3tiMlKdDO8b5dbxceehI934VNMFYWaKM7xhoW2e1RTFLOvCLXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=sQZtTVa5yYUXwScvsc5SRhSDNWpRWtUFHyrnddAttUxaqRY4xRU9OmkTXdG5hXDfOQeIo-Vn_aF3guzpCmX5-IS9dkgkDgUbEEIvOuBZI4KiMJx3rBrVwh7fRIYaYu5OWV6jJhtL3OfBYyd0CIiI2xJ4G6i12gBCnIjWztjNTBxHO8IhtL_Evd6cmdoPH8ppqfoKeRkM6cE113YU5YhL9MPkbMp9_I1Q4OIqioqd7kzQaEEdMjZcMfHulRBJaC8Pz2ezPT-wUzx4eqabFoXIvOdmPfUGsalhrFMJ3tiMlKdDO8b5dbxceehI934VNMFYWaKM7xhoW2e1RTFLOvCLXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مراسم تشییع رهبر شهید، نماد اقتدار و عزت ایران است
🔹
هم‌زمان که همهٔ ما سوگواریم، با تمام وجود به روش و منش رهبرمان افتخار می‌کنیم.
🔹
ایران امروز مقتدرتر و سربلندتر از هر زمان دیگری ایستاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667909" target="_blank">📅 15:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667908">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667908" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه باشکوه طلوع خورشید در پل خواجو‌ اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667907" target="_blank">📅 15:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJd8HLpNBaLpFqHdxvrHxXYfU_lD-VsaloaoWNAvENwbOHHsromDHZZqyIZrm8MbXqbWCnpxiBb37cpz2Ce75q0COmO7psS5y2QwmwY8SUc1E2bemDGXwk3KAgwtTvXR3838jUwuvUHyYgvw47vWlRnqCOsRDXAHaY4MX0eyrEtA8hWPD11gi8T0-MOGprog3aen4DlqXfAWE5T1Wy2HbJjwJ-lRlSrj9C5DD5IznuN_YGcqsYoYnK5mqPAovoJiXHSUXZSTAJnVt2r39dSLpfPqi-f9tbv8kwDqX4ELgfy1GH10YesOvmNadVc7Lb9qZsjzAjdd80erS5I0L5BylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/667906" target="_blank">📅 15:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تلویزیون العربی به نقل از منابع: لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده است. هیأت لبنانی به طرف آمریکایی اطلاع داده که بر حفظ مذاکرات در واشنگتن پافشاری دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/667904" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روزگار سیاه آمریکای حذف شده باوجود رانت «کاخ سفید»/ شیاطین سرخ مقتدرانه به یک‌چهارم رسیدند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/667902" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2963d22c1b.mp4?token=Q-7VKz48ur4QTwLKbtwhR76W82zGUelPqfN29pzbxGHM4zRk6TnVmufk08pvnKRmP3_zjX5ni_TqTYnF0baDxa5SaVBUXQ-GWCUxI5dkXJNqAw_FM9jE8tgnoH30kTimCbz_c-hx0FOoEBp10fFmPtLuEyrqFTEW_CgUWYHBxTxpYSamUtNjFyx10GGzABrAvccUIFnUIew0OLry519DV5lBHKANSbv8OsVPx1r-xKWqVAnDlIrvu8-Zd0vZoS_u9T53NCmTTc13rtBn7fyWViRebo4Erpabg0R5MsAuoDkpDpO_V5y4mCAZiEMuYzNLrhqlNGqyYG06FryuSuB9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2963d22c1b.mp4?token=Q-7VKz48ur4QTwLKbtwhR76W82zGUelPqfN29pzbxGHM4zRk6TnVmufk08pvnKRmP3_zjX5ni_TqTYnF0baDxa5SaVBUXQ-GWCUxI5dkXJNqAw_FM9jE8tgnoH30kTimCbz_c-hx0FOoEBp10fFmPtLuEyrqFTEW_CgUWYHBxTxpYSamUtNjFyx10GGzABrAvccUIFnUIew0OLry519DV5lBHKANSbv8OsVPx1r-xKWqVAnDlIrvu8-Zd0vZoS_u9T53NCmTTc13rtBn7fyWViRebo4Erpabg0R5MsAuoDkpDpO_V5y4mCAZiEMuYzNLrhqlNGqyYG06FryuSuB9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از پیکر مطهر رهبر شهید انقلاب در لحظات ابتدایی حرکت در مسیر تشییع قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/667901" target="_blank">📅 15:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران: سه‌شنبه و چهارشنبه
🔹
هرمزگان: سه‌شنبه
🔹
کاشان و آران و بیدگل: سه‌شنبه
🔹
مرکزی: سه‌شنبه
🔹
خراسان شمالی: چهارشنبه
🔹
بوشهر: سه‌شنبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/667900" target="_blank">📅 15:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwgUJAmvOvSauVLeJOi-HXC71I5-Dr5xIfQzzJVPDYqdqOUDbnFprSdKLPHVuUyqVAdQs4DFrFZDtqEsbyggN2j6QpokqAcyCHLWZ9Ze88J2JwYVUIkZAqTlM9gckfBp_Ba59WHPb41zLxa-UCTTCTw86uccfVkzhq8JKCTmqk-KoGiZbMO7x5DtaCm0azK_QNaipEhzx3cWppRBJwoXGMfpyVhsY8AbMgxQBuvxh7J8p02WqqqaPTz_rTO9cGoel6YLScJgXGU0WqFvKdUGFcfGaN5Yyg054_eCJ5DaqSkWaQS8cflv_ae1cGFXiLMBSIHn0d4riwswn-bWVMP0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWdxaPrR9qxWy7uLAVQolYGXP5wLJkJdjpPieuT8Egw0F8LcABkyYG4grhO0fuynb15FMG4MY7VVOttgO4ss8UBFifcoYUTI2BqGK2ayvTgR5ADvMKvfkYBNIu_OXl5ta3bEq3GWwxBXTdSG2mXpDzY5nm4R6D_WvoMPFNouX7zBV9s7Suxqg-BU2Di3dgoGBHmCVzb1BadAsSGRH41VwX48GREri0M19goKcXuAJ3Ga3b2ojNDYCDNbqT0InuyGzW2rECjhRt0xeAciVak7rzOx5UXe5_jF3uxk0KPot2mN4seoTV91TsdI5uK2s0O3t8eaSDB4CBq_7a7ToeJ9OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/667898" target="_blank">📅 15:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667897">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مراسم تشییع پیکر شهید رهبر انقلاب فردا ساعت ۶.۳۰ صبح به وقت ایران در نجف آغاز میشود.
🔹
لاوروف: امیدواریم مذاکرات، تنگه هرمز را به شرایط قبل از جنگ برگرداند
🔹
راهداری: مردم بلیت اتوبوس بازگشت از قم و مشهد را از قبل تهیه کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/667897" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی خلجی، روزنامه‌نگار و تحلیلگر سیاسی در بی‌بی‌سی: آقای خامنه‌ای قهرمان شبکه‌سازی هم در داخل و هم در خارج از کشور بود. ما قرار نیست اگر از واقعیت خوشمان نیامد چشمانمان را بر آن ببندیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/667896" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwmkdKww2ZbahGkHJQFEw0pSNmUwPH5RfKtP0PHbcq5fiQLrOpr-cXxT1oC8EkoIh2lA9DghPxF9rU0wl6dzinSsHFDL7MoPaHkoydBxTkDaEUw8mO5XEJ53jAmHuH91s1YvIrcTkr3egrmo8FYRgM1I2fwO-OjbWRF7yZFdYqENVEnV2m7UvrIiJNUVN0jWqDadv86cx8yWRf0lebpAJwS_lwy5sogCOCcNdM0OEEis5tIvVo_pDAhyHWJjzQMwabkefnh4-KC9AluI80ar6tmjxg2shgCZYtYlcyJgESQfpYFB8OVANbUcFCmrpWiqvqwJynVocSTQD2io1AYJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری پرچم سرخ مهران غفوریان برای خونخواهی آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/667894" target="_blank">📅 15:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667893">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb8e46b00.mp4?token=fF1RdyfJwHJIRHC6-BliF4ruXBKnqooLAAdNURtRrPYESJhmyN5wsjlT5I5KjLkqUJ1bnt7DfYL-ZVDKg2lNyF5UuFjt6-339h-J0Ej7XatsMsRbEaFhhNKPN6yl5IKuszb_fDZ8hergxpA5RV1h5FVnvHSgN8HayKhqCReGo91O9UgunnrsdInqgTZuec9Gmtrcn4KcWw8LDDq1oUESvrhCwhW3fOFXdy0LT5lZG-SLaUqPgbbewb9zozhlF-HzPE9UBRKoZ03Dt-jiQyrhe1whkmf9gA9zPLNKzoiQ80IFRfcIavzXlhOiHwzagMzQ8AfSz1qK_qFvnknIHrwuRzJKhYVFgxyWPM6nbiBUlwoRUEQBcayaKtvKWtQmkRUrzD2AWsUZ52wu2X8Dg3SO2sUTi0mTSsvlfEfdCJQZ4lkrNw1xaquljaRYtdgR93k6_4C0y2NBXo4e0ud3BGdzszm2Xf8LhdBwO1sYiv0cKQ0KQizOQtBNGsppzSqx3k0H10r4b7zVKqPTIBceiXIvU8WbnXkEjE5H53AuH6YF-GBflfSU106wozrEGQ865kgiD9Gwx8cO1NdXgoRiKv56BBiSrp7-3JzXR1GcZFPuqTwn2-D8ZuHRal1O5xoM30ObVG82ckza3_BqPptGhPx0qjWCFJVx0u1r_qGHEwZtyPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb8e46b00.mp4?token=fF1RdyfJwHJIRHC6-BliF4ruXBKnqooLAAdNURtRrPYESJhmyN5wsjlT5I5KjLkqUJ1bnt7DfYL-ZVDKg2lNyF5UuFjt6-339h-J0Ej7XatsMsRbEaFhhNKPN6yl5IKuszb_fDZ8hergxpA5RV1h5FVnvHSgN8HayKhqCReGo91O9UgunnrsdInqgTZuec9Gmtrcn4KcWw8LDDq1oUESvrhCwhW3fOFXdy0LT5lZG-SLaUqPgbbewb9zozhlF-HzPE9UBRKoZ03Dt-jiQyrhe1whkmf9gA9zPLNKzoiQ80IFRfcIavzXlhOiHwzagMzQ8AfSz1qK_qFvnknIHrwuRzJKhYVFgxyWPM6nbiBUlwoRUEQBcayaKtvKWtQmkRUrzD2AWsUZ52wu2X8Dg3SO2sUTi0mTSsvlfEfdCJQZ4lkrNw1xaquljaRYtdgR93k6_4C0y2NBXo4e0ud3BGdzszm2Xf8LhdBwO1sYiv0cKQ0KQizOQtBNGsppzSqx3k0H10r4b7zVKqPTIBceiXIvU8WbnXkEjE5H53AuH6YF-GBflfSU106wozrEGQ865kgiD9Gwx8cO1NdXgoRiKv56BBiSrp7-3JzXR1GcZFPuqTwn2-D8ZuHRal1O5xoM30ObVG82ckza3_BqPptGhPx0qjWCFJVx0u1r_qGHEwZtyPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار شیخ علی الخطیب، نایب رئیس مجلس اعلای اسلامی شیعیان لبنان با سید عباس عراقچی وزیر امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/667893" target="_blank">📅 15:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز: جمعیت کثیری در تشییع آیت‌الله خامنه‌ای در قم شرکت کردند
🔹
شبکه رویترز با انتشار تصاویری از حضور گسترده مردم ایران در خیابان‌های قم اعلام کرد «جمعیت کثیری در تشییع آیت‌الله خامنه‌ای، رهبر فقید ایران در شهر قم شرکت کردند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/667892" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی در اجلاس ناتو: ماهانه حدود ۳۰ هزار نیروی روسی را از بین می‌بریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667891" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نجف مهیای میزبانی از قائد شهید امت می‌شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/667890" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667889">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvRb1OaqAeoHi2jQiEZwYFjWkiGlvNn8jvRcUcw1sKZ2vDodoy6DxI8hzhjvtYPtbE3VxZ8lGncsOA8nmloVJ32wZdSFd_B1wxcCFyrRRLg8ubs21-j8je-v0Ul_QFU49zHhiN4iNUDOZgMTFLrf-JzwZ9gddohkAr90PTZKDDOtMhce9B2_-ENdPtjp8cV44VXBlFjqxGvA5nzLAkWcUjQ3oIEytpAwrKW5A1d__OUMz3D9f-6B0v2sP6DIUehG6qEuy-imPgvC9mo2rllUylTvakGrrB28GyQnbL7mapLaLvIRxY0nE_xlezX0M4kZEFpzoce7a-U6FB59KEfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمامهٔ مشکی‌ات ماندگار شد ای آقای شهید ایران...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/667889" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667888">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی   #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/667888" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667884">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdEW1muYEdQpqbGndjYXTFdbG9HAL6cv-OhWd40yWEOtQEgAHptTt7dwQuhujGuGzBXBGrzjnz-8nt1WEAipSVfmikFtlj3gBNDabgHFUCVY3XMrrTJpGXetYFIt_5QMjT4LKtkhlihl8boQYBMR20QHpDRgidxk5w38IeDUgYk3k66BD3AJFCpd9jGtqa4E3A02bDunlFjXxW8IyWPyzeU3CeCB--WbwEfD7GxZT9Z-PV8cSyylynnS48wCWi0O6O_TYAAej-o3FWDq96l3ikR5b1ELiNois4QohcaNC1Dz1Sz2NCcb7YhdrtF2ouNNJ_CDpZc7J6gs9laALGAegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzn7UJe2iT-VqyCBUwuNZWjRpRCjI03BL9FGNJGFVK2DdICw1E9smUQiow7K7rJlGEB2Z6AZSzort77rKG9MYK6BCXsrpCcjVaDgHUysSxCbNvGmZwC0gBdrXiHNHWAhUmztn5SxwupRWHbbU5Jt7cuRbNRGk55efO6sXbWc10FKFJb1O5v5jR5_2A28XtufPxk8jyUeHuFSKJehiWX-WRafVF2-O-RX2KnTR0jzd_fwCNYuB98RRsPMs9AQ0u1wm73cqwv7EnbAsraWcwluj9lSdDn1u8PxPGfEVWGTEf1DLekwS_iOrSvVTdvWGaLO6EznRncUdI8i60B1a1eWvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز حرکت کاروان‌های پیاده‌روی اربعین از رأس‌البیشه؛ جنوبی‌ترین نقطه عراق به مقصد کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/667884" target="_blank">📅 14:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667883">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه: در ترکیه خواستار تعقیب قاتلان رهبر شهید هستند
حامد خسروشاهی، کارشناس مسائل منطقه:
🔹
شهادت رهبر انقلاب، در ترکیه بازتاب وسیعی داشت و هیمنه ابرقدرتی آمریکا و اسرائیل در ذهن ترک‌ها فرو ریخت و ترک‌ها معتقدند امام شهیدمان با زیرکی توانست موضوع موشکی را به پیشران نظامی و سپاهیان تبدیل کند.
🔹
ترکیه یکی از شرکای راهبردی پروژه اف‌۳۵ بود اما پس از جنگ اخیر پایگاه مردمی خود را به سمت پروژه‌های موشکی و پهپادی بومی سوق داد و خود را مدیون رهبر شهیدمان می‌دانند.
🔹
در ترکیه احزاب اسلامی بیانیه داده‌اند که نباید اجازه داد قاتل رهبر شهیدمان با حاشیه امن به کشورهای اسلامی سفر کند و نباید این جنایت عادی‌سازی شود.
🔹
رهبری تأکید کردند که باید پرونده شهادت امام شهیدمان را در مجامع بین‌المللی و دادگاه‌ها پیگیری کرد و از اهمال در این زمینه در گذشته انتقاد کردند.
🔹
رأی دیوان بین‌المللی لاهه باعث شده نتانیاهو از سفر به کشورهای اروپایی حذر کند که این اتفاق باید برای سران آمریکا نیز بیفتد، هرچند امید کمی هست اما باید پیگیری حقوقی ادامه یابد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/667883" target="_blank">📅 14:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNDsn4NIhLZBr8GmEEKcXxnHqLQTyGfKlOQHMzs8KwQLgkP2b6jIKr7cOAA8tLO7VH6sCmcA10bCg5FdaokvzUOaqsR5Q8KPjhPTb_oamMH62GmsxNadfBKwDUAa3dQw7idE9v081uHQbgf_nC-MOc_VRdGiupRND_TE7mt_Q3GqeyLiS0PmR46Ed-6_1MZeWG7Nbzc535-hH25eI9gyqlY-hHWTmZGWvCD2QSv-YpUafk621Qn7jfA_Tt0cGpPaklkAfckAIsDOurPQEYkCMxPz9slcPEYrc4NJnHAvRiSn1bD0_sJhgbSx9T8QgSwFsenBDVIodGPsed3BBnIglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htkXCYWXljam3yc8iXH_zOx4FH-xYW1_q36-cYUcUSvn7arPXBqnj--r8jW-T5_89p9c5-S3HfIv9RUk9g0h8HWdijx6-y1qsUB9-QDCnP49PsxLbxoMvXRr8iDYlr6r0qVooRXlCZ1p3Nm1Y2oJYymLzLgknwF2xACteniTYpkNvH76SJdMy2zp3JZpfrpoaucwU1RZ6ckHFqAybfVlQd-_jEMJfbdgLSh8qMUlCZ29eq5zuxXO4dSgLmdU1UEUbYac7Hde8qECHU3-SnQCZPRnYaHDB8v9UXkY9rVnk_MwFTeYnxGXoPh5IGs3fZdBU6Z94Rr_eMzSv08P88InjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYsOwX6yc7-9QWOKqKo8xTJf-_hmUNXBJ6GlfFMFZz0I3ZkjBGSVZNQ-UHWRixFGmui1ziOmyYfpZ7pu05mMM6O1AUCstPkOe3B4HNTmuzsaRYsIZosVmnkIuUCJH1oInslN2MRTdoWEm8scAfsxZfv0FNnt7gC5KK9td3BY1GvGMZntX2yMHFhJn0Gxk1f50bBCU83rSdGr_UWY7FEPdsU-DOFqukLt1O_Fqh6RrzugRRkQldWftqtWdSKA29UQT_0KQve8QcqmISMIf3l3iALw1ss3cz166df14yMB-jcHApORaUI0vRG38R90zcPVPfgzruIYcUVtTnBk2oQ7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j37H85Fo-ZydDNeAl_Kgqn0Ci1eaCiRGGmdMKSzfyJnwqWXd-XPweoH5xyq9-y6_466uq58RSBSg2znp-oPildqrInV6Jc2NYTKuWm3nQ_icSTB00yk1dx9QU8DWZ4OiegIO8yEHPwJwvjZDUb1duv62yOWGC5KNn1t4oucP4NluZuOh0rynqCQumXvY3-n5PQCBN5VgPrr7QBX_ufz-5yQJ0l0YbxDp4maTViXimtpwQHcloDBjej-h9xcsLCuFChj62dQ3YiXEFuq3r5vwlDY2AjQEvph9zQutsCJ7wp_nPe6HP6HXtOR7ivpeYUn_HqnosK8ZgTgn82TS97M8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP_9gj3a5jYjXFxfWKvYTlu6uy33cYON95YlRZKO34iEKFVKSLplgWu4C63KWIqPIHadOvhVz_h5QM2vk7P8TcUWF--WSKlojILx4EpSpsg4IPtFS0GansqNljn9MX74LrzsYP-FvJ-_ERzjrh-3-Xq865oM4f0UFd4AtQEUodrdQOZHbyxWfZdCVwep1ZWn48wrMlVHBOuHoyZklLRlRQcZSmb1ZZ4UNvuNMnsuxENo5lW4ImvxB5nqKbNJeCJNnwSn3McvgwCUHu3EvZG7oSqAvdxJX4q_3e7sPC5btuYM3gE59VeUbi0jqMWqZ6EfplEOQcSKaDmRt4ZZSkEAuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلسکوپ جیمز وب در چهار سالگی خود تصاویری حیرت‌انگیز از کهکشان قنطورس ای ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667878" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667877" target="_blank">📅 14:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین‌الحرمین: حال‌وهوای شهر کربلا، آماده مراسم تشییع پیکر رهبر شهید است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/667876" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه بوشهر، فعالیت خود را از روز شنبه ۲۰ تیر از سر می‌گیرد.
🔹
فارن‌پالیسی: مهار ایران شکست خورد/ خلیج فارس به‌ سوی نظم امنیتی تازه می‌رود
🔹
امروز در حاشیه اجلاس سران ناتو در آنکارا، نشستی درباره تنگه هرمز برگزار شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/667875" target="_blank">📅 14:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نسرین جاپلقی که در سانحه بسیار سخت تصادف جاده‌ای، روح‌شان از جسم جدا شده و به خاطر رؤیت روح مادرشان و فضای بسیار زیبا و دلنشین برزخ با وجود درک سختی دنیای فرزندانشان بعد از مرگ ایشان، باز هم تمایلی به بازگشت نداشتند اما با نذر و نیاز بازماندگان به دنیا بازمی‌گردند اما همسر و برادرزاده ایشان در آن سانحه از دنیا می‌روند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نسرین چاپلقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/667874" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nir2H0RTs8DL6gHgkYBX0pNLdvOPkde6tBjxdlBiX7rDVEuYc1CaiHrSg_SshXFrvwElDk7Hriahy5dSzBjcmXjLn0eTD7wuFPtAXvu8Q4QexqjztnqWZukMDEshpd3hrtPGqwMcxN0WFVsxx1SAGOsG4c46XcAtVa-1SPmD5-1WXgI4coeQ2nEpZQbwUlv-_o9uja-LlJDE6AYjv45GBo-SOT-jby55Tp4XOXDgkxl9KktQVvrfPyJKfR5AFPF7C4U0lCCWSI6KgaVMbXB1x-IfXE5nE7qgMIi4Zo7HF1HtWwvLukGxxwQYyT_-TA2Vump3AgVjBSDlc9jzoLHIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه
؛
امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/667873" target="_blank">📅 14:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7UsLf3zWN76bkdsbihUbBcAZAON19JWSdU-KIUTM1kWvr7_uJY5PfUuYukbsH9VLalmmWXLsxdRrDBTD0lP82IRy--cqlO0RmhFvITPqTlMSKD3JbfNN8RBeks-9_Ex-MxZ257jugb1dC7NtYgkzus6iJtQLALRCPo5t84qsEdHGkQw9lo4Rr7MCa4QYZoqOJX8-UKuwH5rtfWDqq_X6uZV7B3Ez4Az2MLNTAYe0ZvSSH5-7RkYB0F36wDMEo3ckqZXPIguJPuMljqsko4ehV-ZI3TLsaM2x2JpgjaJfNHcw1tOp9SabrBB2_fS2oTsiOmfGjIQMz0a3Wu2H2UWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk-_lhli8FhaceI3tAp_N0l-4_WxHpH5LXpt-ng5JTNwwILlN18UXeH0UNz9Me60_X_Rynyz5Q9Z8-5BlLip1QwRqDV3P1Bux5cZKoOIgx5toVjwIs9EkKGsxUVoYEWZdz1WtZHbKBt_007-j2roDO3tdq9Qf8LOvAMYXkwNGEBemaxrz8OObUpezHukcs1YuIJGRTeRMvO8U3viPajmnA-Y4k6v7cYZaqTgBsvdLdMbEOb2ofKhPdQDtGyxvRTUhTEpbUcFoTD3Q1KBQxX_7DmGlY2aHaAmpOtWpM05ybymAlxInwuEkAZnCBT0KXZ6fV4073NHcgdQYWHjGMtZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l68hoHEqcHRRyqa5WlH6289lbD3F8rvObLYnJCyh6HhwLFzqMZGmGv9juTRylxRSaqYsDwlk7lUQHIrPAU9Pi8TIXioUs80kEo_7-jttbphnKF4vRDJRr0Usw2we9f5ahzCJDlAqLwsGFHmiLoPfNusjNKJIkviKxPC8faya7EvVy0UrOZqW0fl8i_RwNd4a27eGT6jyuXGv7jChyh_XEHmuiRH6jg2vpz5vZyHzAsfhnsFCwbdoNsN11imXXg374V-Om5-tGXvqDkZ0spZSbThrsOJ19RLgY_dX4muGalEQLZf6SrPxrgxAMH5tdmwK2m9XqfiJ0iEUja9s_VNlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERNDbZGpjoBssCQnUXdatEeVThELh_f9K6btmxVsGwa-ClB5EHXFuc6fRpk6PHeliRRJTx34MWdUMP2QT_4Zrz1f5823Guvu2M7lZkLp7F_1u-iOngfXN_8hUor14ZovetB-Jcq-uzyWuUU7EsyGKZUQcoBLSO3lW34FF14eg0kaxyD3RnMQ-R74RWasSP8YlXeeLutv495AGPXxSlV80i1IrswOlw001Y_3ebkPdq1mPD5PVVKEIXXQitRgA76fJzwUeFf5nPqTB0pMkkKtYRqi_A7ijJ6lLcUeWo6lXSHREV2EPjy7HrgOIPzivr01JsvuhCWoaKbwBszvsDEBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kg2sts6EVINr1slCwqcOGGqsKpHQzLf2exvFLIUXANkdBNyroiepN6KDm5dOmHPC2OtbIyUMtdDW_YdFRSTr8xVIw4osdO_7ziodwbot1fu9ys77UxYIpjAFM8SrfCRXJlYY0pAswhg_Auf20HiAFxMYQbyvaCXyVg7Z1yPJuhtowLW_hGl15Yfo6z5glHJBaTvkIKpNwWd4X14AqVtAdfZ2Bt57IYtJCATMdp_vWruWd-5emKxkZ1CyDdskGleRIQa5h4Z3_IgT42jsQPvkw2OHdZoPG-gThv9qBEXTKNAcuVTaYNW0hPUvxCrXdLSUUqGvWN6TYzME7N2I59Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4107eRJIfDPIALZs7ubGPnw4fBDFNvGuYBV4ddIVqXysz1Zu4mc7_cAasw_qDkrMbPNemfJi8MAxIvFb17PI1sqb1i56B8xk-4Nd5L3vLup-NTLYcrsxVrjUUNmijpkSMl2b2NLAYtZ9vkFZHonVfDl_IslmSQEeWviJmQX92Gvw-rHpnBBG3ZGZcAEySM6BldT61PmVs6Q-9wULaCWY2N2L0cZfQhv5apLgoylgcKE2bfcwnpNnK9H0m4ydI4gz1F6JeL2zNlHVcAUUTkvhb-27Pa0ntLjtTRckrsm4Lmtss0TYa9Pul75H55TIWyEXXAeaEkAtCURTqUnDsDl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY9JvQg4D1BiJXtjz3Xnm-sKU78UTDoXX0TVE5y2ejLGPS1PolrU2tkIgmE841iVxcW-lIi2oT7RXE4y9et9_sBEv0CcdU3ZQHlJ9dcpTeAm0GU-Sv1RFYcMymgXWwmCM56W0xdv0MWFFwtrSr451bRpa_gSKRkhls3VxjulJWSIaee9-HpKmLWAMyIpTtoaItuqmmF2PCBQv6jjgJPm_QApLrRyph-k-J_okot2M1W_C1Pymup5Ycvb7ez3NP4B7_UkjU0EooiI2gNpsbrTtRvMQejeffsWH2vaJHyGpWgBK2MWXb-n2o4i3TfAvcGIVbRhmCRak_NBWU2bJzaR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqVP9dGUhYQMIrDLaNqMy-FnojZLXb3BS6w5kw5LjhVqxM4n5HBkV-_cqp6GsvSYVvMH0UWNt4kkVOfiPHJWbYyO1IZ63G7zwxDkNimgT2_Xp2_HjG5jSKaNaEyyqP6LQHwc1fIUZ_EkSFrY8kQbN2R_yq8bfDi-vQwSt405-h-5meSrDwWsblhdHZmziGk95hfPrf6nLdb5CqkJcwcL15iONB4G9AlDhHbV8EK1HGvT9zyd8i169j2VsjYVmkYNBs441fBFwmc7FSaxwFIUr7cGSiX7Mnr--H4NDwR_I75gLJVUf66HHXTwTp1SyKILufXrfSd8EuPY47kPREpShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2iMQ2ngHmq2Xg3d5kdmh69tqMe8Zx7w2lfx8ffap9pN6m2yHl2if8GxlPDygaHjYjMprnlGJVmLcHHHwOerpO4eXPiiOjJxBPuf3rHHCsRTmiJqtzdxsHUTmsyntMJhIWjrIlBv3e-PFAAKqs18HIOV2RLV3Tfs0cAt0DWkwNe8H0WLXzH282Hpy9X9aWOPACIHJUx0kVELQwz4rrqlSRjR64_dVN2H_cKbRk35iSjD4_3ZETqabJcXwRl9lLYODEAojiLJY8vU0RtSsomR42SqeBT6wz7HajxvyGqPHYhKGaq6ey9O7z5w5xAvaGXouecu4xeoNyp8DnkrqCPWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRqnWeHQEAjG1uHeg7Gn_oODSgkyWETqBflGFAgDXZmvFAdp3wCZvun6EpaJpZNS-mqpT9hzZ_GjFrvzSxUfHEoEMyEdoPwShRSOUFYrTJKRTf-4TwYg1-64jKp0aYxa_dBHzjb0n6uk_gt919qJLEibfBRwGQqvK90L7-vFRr8l8f07oWGtWy-Xtum_QAbY2UyGauiMdgtk1JhyqlCQNlA_NYDEe5_7qf28pmHHlwEv39aSm2T9vgpiRwVMSTVBQrwrZsnUhTFxEqe1voVaTi7jtf2PNhXwM7CUbmRHXuPuVxqALBg7qjDqfY-sJdBSFzLkwBZAFk37SEJ0eaGk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات وداع با رهبر شهید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/667863" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زائر تشییع رهبر شهید: امیدواریم مسئولین کاری بکنند که حداقل در دنیا باب نشود که رهبر یک کشوری را از آن بگیری و هیچ هزینه‌ای بابتش پرداخت نکنی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/667862" target="_blank">📅 13:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ بر آمریکای جکسون هینکل فعال رسانه‌ای آمریکایی در تجمعات شبانه تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/667861" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667860">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ناو «آبراهام لینکلن» از خلیج عمان خارج شد
🔹
تصاویر ماهواره‌ای تحلیل‌ شده توسط شبکه الجزیره نشان می‌دهد ناو هواپیمابر آمریکایی «یو‌اس‌اس آبراهام لینکلن» در دو هفته گذشته خلیج عمان را ترک کرده و حدود ۲۰۷ کیلومتر به سمت جنوب حرکت کرده است. بر اساس این داده‌ها، این ناو اکنون در موقعیت جدیدی در دریای عرب مستقر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/667860" target="_blank">📅 13:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اطلاعیه شماره یک ستاد استقبال و تشییع آقای شهید ایران در مشهد
🔹
جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم‌مطهر به‌ صورت مستمر و بدون وقفه برقرار خواهد بود و محدودیت‌های تشرف، صرفاً در صحن‌ها و رواق‌های مرکزی، از ظهر چهارشنبه ۱۷ تیر به‌صورت تدریجی تا پایان مراسم تدفین اعمال می‌شود.
🔹
تردد از تمامی مسیرهای منتهی به مشهد مقدس به‌صورت عادی و بدون هیچ‌گونه محدودیت برقرار خواهد بود.
🔹
مسیر قطعی استقبال و تشییع، خیابان امام رضا (علیه‌السلام) تا حرم مطهر رضوی خواهد بود و تمامی مسیرهای پیرامونی این خیابان برای حضور گسترده مردم آماده میزبانی است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/667859" target="_blank">📅 13:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی در آلمان در گرامیداشت یاد و خاطره‌ آقای شهید ایران برگزار شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/667858" target="_blank">📅 13:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فرزند شهید نصرالله: شهادت رهبران، انگیزه انتقام را دوچندان کرد
سید جواد نصرالله در حاشیه مراسم وداع:
🔹
پیوند پدرم با رهبر شهید عمیق و معنوی بود؛ این شهادت‌ها، عزم مقاومت را راسخ‌تر و آتش انتقام از دشمن را شعله‌ورتر کرده است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667857" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است
🔹
نماز در حرم مطهر برگزار می‌شود و خیابان های شمالی هم محدوده نماز هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667856" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۶ میانبر کاربردی برای افزایش سرعت نگارش با Word
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667855" target="_blank">📅 13:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNMPjlMjHbhHy0yN9L8QecbnpdNOPW1SjOZb5BIVZpOigUbEIO2iw0ngGfw_qb3ExFeIDm7L06Qeqh9vV6ulOj9OIHn_xK1nVhvk89nDTLIKYOexA4UDc6MRYlv61ZHjJRCnZzsaEbTO4v3dG6XUcz-rrfGt-Z8JspC-HxAsPuC00zdlQdseqBWcDT_yEHyhA7pz2SGkEr0FeU8R4sDIgkC2H12ybMm_GoCgVwqb_IhDl5LdnRs5Tz5KZfla7iOH4BLSP_1uCLVundvNPeqx-s0tBxIC_8mbYe3hefEme-zTNGSfzlLDX2BvhoOtk8ASNXfA6b9lC0Bw5NOpJWVAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسماعیل قاآنی: تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق مشت های در هم گره شده دو ملت دربرابر فتنه های آمریکایی را محکم‌تر و خط سرخ خونخواهی را پررنگ‌تر خواهد ساخت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/667854" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDLb_koEzPME_pBseGf2NuT7f5S4Jj9_100d5oLEDfzVdCzv4ozp7c3vGhXHsro9LKsLBT8KyKEuGpI7wzfwGIbUbRV_q_qm5d0IoLxQF_XsvFDnaENp-5xArHKIZFMiCJW4usOivddqiTpXxbkDCQfzo5h4drd8XxlVscUZIQUghvQI7499bvpy6RkZ0x-MZrga8w_lkQ--ObUdx-AB5duXiJ2KUyRSQ7D3JgLL22G52J_isvF6qlaGAHc7vgJK1tXkwbTQwuj46_Q6QDnE2EzPOQa7Q-I7AtHawYcFIPwys-vjtbxUNCouWEzGAXt-XjQn_hgEioTzYtEspk-B7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران با رشد ۱۲۲ هزار واحدی، برای نخستین بار وارد کانال ۵.۳ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/667853" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667851">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: دو کشتی تجاری توسط سپاه پاسداران مورد اصابت قرار گرفتند و خسارات قابل توجهی متحمل شدند، اما هیچ زخمی گزارش نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/667851" target="_blank">📅 13:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667850">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عمان  سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/667850" target="_blank">📅 12:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667849">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راشاتودی: سیل میلیونی جمعیت در قم برای وداع با رهبر شهید
🔹
شبکه راشاتودی با انتشار تصاویر هوایی از مراسم قم، حضور بی‌سابقه و سیل‌آسای جمعیت برای وداع با آیت‌الله خامنه‌ای را بازتاب داد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667849" target="_blank">📅 12:54 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
