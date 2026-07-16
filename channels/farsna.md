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
<img src="https://cdn4.telesco.pe/file/VWO0aYo5UMUIwy2PHfdffMSbs8YezV9vByp1BbOH-Ox3ECudvjb2TsMBQ57IqFKCW_z4b6zkQx9pSaIBwRKj83s7yEd2WzZuNfK0r6d_hZ0OnnMUlvZo5MbrfphaAPqnPj9e-bQAUSpzGDiFL-pLlg4y4zuilH87_Rw1wMohHqmD6ke0GxFlt7HYw0YtDhfRD0RhstgSMeF_GktDpSheJuHjedIuPzYQjwT4S-0UlpAxE80DTk53CT0WrsSui5wwPpDXhzuf_70V2mwllCIuI-AnilgyCG25qiYwmZtww9wcF8J4fzRIiGTAKAL5ZO_XGfKkmIWW45b-x4WoecKkhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 15:44:21</div>
<hr>

<div class="tg-post" id="msg-450401">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fas7YeZMWplGc13A_JmnWiiIQgCS-Rf25Nwo4UyA9HkFG3jjLS3TAHR8fk0bzKZZynmivAZjC1iKmdXdtV92w4-Bq8zWFu2lPZ3MndeyVK_ZbXVbmTSKIxoE2jmPdZuTBnl8DBYWDbLu_ZQX_nQBqi3mMUiyza3AYmu7V0XgI6QUn7hLKwYNxU0ZOqjsocWUDfqENb1JQWCpBYGDQRV0gYEIrogOisnMSN-26AuomOF28ziKpu2fqYCMv2bSOGwaJtV1C2zF10GuiXr5vu8V2ytrowPNkgACVSNDTtvYbUi9o2D-nCgLWjFP0h96hYJk96CfR7AgLytXksUE2glDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arCwckFlQBXGpmePfwkT2jMBxZUUbG__WGPKzIEJJBhvfprc0iSCEzWGLyeX6PKAE9-9N-NyynBoZKYMR-z1edqP1P1ddIOFhg8vP6EDnlroLEDzUJnCOdrnmiN9RpQfEDOs4rj-ZaW_DmO9LUjA4MSRiV354CSvHUM-3ApgSo-1y0gtO8i_eU76e6sO5E0yXYY5vWfU67NFSqTx-K_8GPo8zNyNLRGmj7A71369K1jObKpHGtTJ8oZNqrUQqiLvQYiaO8yhPokoCsicUNiza9oLRJbe-BYqVPKQpUsGq0sFIZe0PO5HWUNnxOC9ZpbGWmkjj_Mrsr3c-Z4PkOiMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUpfUw34cUxV5XPu8RgkoIx0K-SpJOzgHeOM3TM61idZHFj9JyapxPPstJ-AvW34RfE3aJWbYhz-iiHj-VZcIDU73837_UfPNXTwfOVVYjEMwaDehMJNdk6IHnWnJdyI5H6jF3fknkaW5r5me3IOOCpYMJFt39C72AZf-X2zgKLieLKFKi4kt0HE--mwKDBGFXeZmZ9OLeg4BR4Vp9lQJzNYElQePnnWdBPS9zAY0xePt02qo6Cbvuf6Xk2swzhjIs1wgefVUiOR6OZ2WqKBwMGRVnVGUcTABGzXdmpJQMxKMMWn7th2qRdbwka27GIuWugZ_7R1aZ7efGjwnsPfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQLyR4YKAtsMpm4EX0N3H6iuqy9VhFpb3AD0BSf8Jzi6tdv_2AICy2v-nyDjS5H46yKW1s3dyCUiorXaI3IhV9SGtkVwUUdxb9qwFBSC_1ly7qjpHwYCLmdXWzONRupVi3RoUjwEzR-Hdn_xdT43ggaCeJ8iEhYD_BwbXj_6Z-c5IZAdStCyz25kOaxgVRgW2rWYMlHch1wAgSqkVb1Ak06-tjwYv1lAT8vuDz0H9hyWWygzBZUjv2GqBu49wuURnKL2u3ezVDtCYFTqOUQ32RMDZzXsV8621Ahd2_qX1oi7ybco8y3JOQW2K1YsvQRSLDi0A5DWq9mkTo4mLnGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIKXAN8YSHU4PPlbKKd97S2tVGumJjtaLaEFWuAP_irlA9qNgA3PforXhOmuxIDS5KMp0FuJf_hllEWoqn0WNtBX-yjEVN_Uapf74BbSEQYWafB71RAV55a7G4YDzC0QG6s31cepYnvzXysCSM--UDnJh6wiiVVLMk43UA7xUPWOKJU5JnwBZM7WjPyYMw25UND_JqvdAR-QrxWzdxfUabQIx_nBlRyR5OWko0h5mUZIEkj7kl2Aogmt5rjOv1vZFDPW8lPxlTHcZwae_GdM6jxSfoyiu_aPN_Jpp-ZlBxf-8B2DaEzQPbP3MhCFxHJkQFriXgkL1AKj8HjD-dbBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBlHb6OVqKqL9uZkFIzf2PKG9PnwfZl8HupUOh8E4M01jGjK497Hoj96lSKdKAczWHEp5xniUBsVZVkdVn0LVrmayUxvzylydhAYGHeIWTWgzvZhGgAyjn2eHoHCInFZUIi9MPf3SKIRsDQbXg-yW9847ADPY5JoZRM3aE0J4Qc4rALQNEzXZeRJBX2amuLwm59VuEqbY8vIUTiSuOtrDk-fVq9vFVFTC_a0xaPskhuZ1fNMFe0KrD6VERuaMtF6uj_8UPkrutrGOkltNjJten486UwPdJn6_tahBieRpsU7HCfnn9VBXhE2oov9pahhG4MqX3lrgiJmxbQNxCNxng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاش دلتان برای جنوب ایران می‌سوخت
🔹
در روزهای اخیر موجی جدید در شبکه‌های اجتماعی به‌راه افتاده که در ظاهر حمایت از جنوب است، اما باطنش چیز دیگری است.
🔹
«مردم مظلوم جنوب ایران دل ما پیش شماست»؛ اگر در استوری‌های اینستاگرامتان چشم بگردانید احتمالاً یکی در میان محتوایی شبیه به این را در صفحۀ سلبریتی‌ها خواهید دید.
🔹
همدلی و اتحاد بین ایرانیان همواره زبانزد بوده. خصوصاً در دوره‌های سختی این «یک پیکری» بیشتر نمود پیدا می‌کند؛ اما چرا همۀ این واکنش‌ها در شبکه‌های اجتماعی لزوماً به‌معنای حمایت از «جنوب ایران» نیست؟
🔹
بخشی از این واکنش‌ها از سوی کسانی منتشر شده که در ۵ ماه اخیر در قبال بمباران نظامی و غیرنظامی، زیرساخت و مناطق مسکونی سکوت کردند؛ آن‌ها نه شهادت کودکان دانش‌آموز میناب خَم به ابرویشان آورد و نه دلشان برای کودکان ورزشکار شهید لامرد لرزید. اگر هم حرفی می‌زدند درمورد قطع اینترنت بود.
🖼
در برخورد اول، یک سؤال پیش می‌آید:
🔸
چطور وقتی «تمام ایران» بمباران شد، سکوت کردند، حالا از «جنوب ایران» می‌گویند؟ یک استدلال پشیمانی و جبران است. اما چرا این فرضیه چندان مقبول نیست؟ چون در حرف‌هایشان خبری از مهاجم نیست؛ گویی در جنوب زلزله آمده یا جنگلی آتش‌گرفته.
🔗
ادامهٔ مطلب را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/450401" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450400">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb9b129d7.mp4?token=VuEsGiQofcYXh4sksUGwuBOEveSDi4MNIUkEjPfZJYm4IBbN3onrhvBbH07yquoTJJqODE2Tvua-1Wel7llXozVmh_zyFkCei_KyIeQr3X7MNEO8pxvxc8LCqw3dvMuYaI6yS-ziw0DZa36P-R57RRx4sVs-lFJ11ck6oObCqF7SoE6Ts7hGdl3tTogadzEoetnlgAoyH4_JsUZvt3EYwsb-KN3n0oVOd5ido9JauXY9wqNuzWLxjR3NV7onYFay7T87RToWI-zzKT9hrLLGHJApdBiF-x749iLm6kJBf2sbHkqAUYvrpxDTzxjzXZI1sZdcEBsGDmRvyQxUzsv0JqKljCd6v5AmlQM0Ci7O5hBU4hbxGb0PqztWAif5As4-Tf-dUCv3DOj3avmRAqjsRKzOZy6x2Po2TG9hlRhugTyh-WOhdS23lanrQIE6aUjPrlSBp9sqhAviaX35WuYKlIy26TBNpdVf-bbUGy3jrUwfIRCNLELeNEi1hEybb4h4h5i7-kYvsacOczWMGYqkXfHO87KNUSDYk47NGdObcnEakcOLRsdxbCFtomGr-A4n8gWcLLpHiD4dPoljKxNDVAn1tjuiPE3mMnVHkVWtYx-3bYbRi1ESUhWlP-1aLtu4M_UMxkq-8vOM5Mrh8lm34Jv7JxMapZwQmUxzIbRZx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb9b129d7.mp4?token=VuEsGiQofcYXh4sksUGwuBOEveSDi4MNIUkEjPfZJYm4IBbN3onrhvBbH07yquoTJJqODE2Tvua-1Wel7llXozVmh_zyFkCei_KyIeQr3X7MNEO8pxvxc8LCqw3dvMuYaI6yS-ziw0DZa36P-R57RRx4sVs-lFJ11ck6oObCqF7SoE6Ts7hGdl3tTogadzEoetnlgAoyH4_JsUZvt3EYwsb-KN3n0oVOd5ido9JauXY9wqNuzWLxjR3NV7onYFay7T87RToWI-zzKT9hrLLGHJApdBiF-x749iLm6kJBf2sbHkqAUYvrpxDTzxjzXZI1sZdcEBsGDmRvyQxUzsv0JqKljCd6v5AmlQM0Ci7O5hBU4hbxGb0PqztWAif5As4-Tf-dUCv3DOj3avmRAqjsRKzOZy6x2Po2TG9hlRhugTyh-WOhdS23lanrQIE6aUjPrlSBp9sqhAviaX35WuYKlIy26TBNpdVf-bbUGy3jrUwfIRCNLELeNEi1hEybb4h4h5i7-kYvsacOczWMGYqkXfHO87KNUSDYk47NGdObcnEakcOLRsdxbCFtomGr-A4n8gWcLLpHiD4dPoljKxNDVAn1tjuiPE3mMnVHkVWtYx-3bYbRi1ESUhWlP-1aLtu4M_UMxkq-8vOM5Mrh8lm34Jv7JxMapZwQmUxzIbRZx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایانی بر سیاه‌نمایی افراطی
اعتراف تاریخی استاد خودتحقیر: ما هم خسته شدیم از این همه سیاه‌نمایی کردن
به همراه اطلاعات و تصاویر کمتر دیده شده از ایران زیبا
@Fars_plus</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/450400" target="_blank">📅 15:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlFP8usjo2LzSo8_MtSzodh-_oWKTs-mEJRwsrWmtKkcwJY55oQTTjdYUEhDsLrlfG484SnYcTGqYkysGjroc0ZtPth40IJYrQKYE7qxj2LPBb0VhHLa0n8Nn9AkwxSp1RsparOgUpybhaZaS4EMGSg2E2c_-HLT-n6hwmR4PZVP3Zl7iOFQu4lzPliO8Sm6BJEpF7UGXufpkCZWnuEdK0uySh85gpPfnLQhI4kAHKcJT5WLS_tPxG93Djf4MWxNVZdOBLWEc4o0ayKiVyqHynLD0DINVZmGsAPF72nIVK_Nu73l5OmEV5_K91C-UOD8vfEAUK8yNGMltgBEOp7ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/450399" target="_blank">📅 15:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80691e93a.mp4?token=rEQzm-Fv-F7lmz2M0E6kUeTTZBpEu-HOm0Z_7X7bXu1dGxDgMZ48ZBxL4tPxsVkkyvmCwhVFZmMoB3VOVTTX7OKOgnnevIq1QyxVQQCcG1_352NltwLtTo1u5_VUORE3nLP_ocKLZwsRTSOrYdocCl_uzWxEfu0-FjXbuaj0S9oFhTGVUGBkE-wn0h5JPq3Lx_0-J79i9R38SVg5q86NDdCAhApP91pbJi83hoabVuE90RfugUPxG4udDqGCA2U34GhgAttI66zdn3bEiyKyT1M0UZT6UeESa1sAN_mt99T5rnA9r5AnNiDhllN7LNellf_wxc-VIrTrvLeVXu4IHH8lBlxc4b46d4Qga9iEQqqcUoGoGhV3itu77g7jqirqPOdNx4nDpEZN2H8-gupqdXG5mpPQXwSbuB2_BXoJOU4sNgVeeHxGYfEsiEoNw6UG9E19LxfJ7a41yJhNEFlwC2-3eIUc4KvKTQRzkr9k58Pn0xgMipTv0q0M0PrCDTlqNsVHco5pEZJslu3wjwFQvzpngjqFg1hdQ_AXQyfGgRllaf89Raj3fU6Yb5TsVo09BDzCI1l_Jj8XNHFFkzKeuD4FGSk0Va4ZFir4W2F4_XGwjZefx1qjRNRMQbDmbBo1Kg7UfYTlN-3B4ZiPYuvKfWQb_MqROuGwnrtvTv7GDqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80691e93a.mp4?token=rEQzm-Fv-F7lmz2M0E6kUeTTZBpEu-HOm0Z_7X7bXu1dGxDgMZ48ZBxL4tPxsVkkyvmCwhVFZmMoB3VOVTTX7OKOgnnevIq1QyxVQQCcG1_352NltwLtTo1u5_VUORE3nLP_ocKLZwsRTSOrYdocCl_uzWxEfu0-FjXbuaj0S9oFhTGVUGBkE-wn0h5JPq3Lx_0-J79i9R38SVg5q86NDdCAhApP91pbJi83hoabVuE90RfugUPxG4udDqGCA2U34GhgAttI66zdn3bEiyKyT1M0UZT6UeESa1sAN_mt99T5rnA9r5AnNiDhllN7LNellf_wxc-VIrTrvLeVXu4IHH8lBlxc4b46d4Qga9iEQqqcUoGoGhV3itu77g7jqirqPOdNx4nDpEZN2H8-gupqdXG5mpPQXwSbuB2_BXoJOU4sNgVeeHxGYfEsiEoNw6UG9E19LxfJ7a41yJhNEFlwC2-3eIUc4KvKTQRzkr9k58Pn0xgMipTv0q0M0PrCDTlqNsVHco5pEZJslu3wjwFQvzpngjqFg1hdQ_AXQyfGgRllaf89Raj3fU6Yb5TsVo09BDzCI1l_Jj8XNHFFkzKeuD4FGSk0Va4ZFir4W2F4_XGwjZefx1qjRNRMQbDmbBo1Kg7UfYTlN-3B4ZiPYuvKfWQb_MqROuGwnrtvTv7GDqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در موج‌های ۸، ۹ و ۱۰ عملیات نصر ۲ و در مراحل ۹ و ۱۰ عملیات صاعقه چه مواضعی از دشمن آمریکایی هدف گرفته شد؟
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/450398" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqFP_K-6nE89Uuej9IaanRrMeWCYXhNDxFStxKOSS8fIgRDlQcKfwVz13ojuxfXHm-YLE0XTH1BivkfWFzd8W-h4zmgXXBgChIgNZtPq9sLx1MaqMtvX_geOz3-T63PQbX73MsiTjG5eyB6cSbNg_p94h6KeQNqEdJevSHoRRJntIpAAksSwLtpChXejx0G-VUYaXlYs3pjm10XcKPZklCGScoRpdkfPZsUpKVeSkfqBPc1QTuWA5SoIk-z4LjI8-d1si9iif_2vbRq8hQ5jzsUhRNXOjv-vg7YV9k-KoJCxX-IQgIvD6zwVKOAMf7eDVI2mgQcAX47RrE72gpfj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش کویت از درگیری پدافند این کشور با پهپادهای «متخاصم» خبر داد
🔹
حساب رسمی ستاد کل ارتش کویت در شبکه اجتماعی ایکس دقایقی پیش اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/450397" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whg_uX2IGLaSFn5P3_3g4XwblLIwgBHe80e-yQueAc9ce7M4inl7GKDNqFnOr6hP6URhSp5hindUrdncs-AwspuTPi0reQGu_zgOLiWFq8jtBkX_pB06NEnUaWeZGIdzLFx7Lruj-az3JQYYVk3Vj8Ev6L5KmK1iNIDy8g_mWHG_NO_8fmd9oRI6Biyv1fms1q6Gl5H2HyC-gJ6f_cOTTVcDVZcQCRwlQ6_NqVP6mZcVchYEM0n1elBz92LTwclsaNL67Zx49H7pwYrC-arn61B5Ir7lqPPnN1loLSBdLEkVnOAwZKBk5TYfMj32FlHUqZafR7Jm-mI4Dn1hJmpytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورعلی هم پرسپولیسی شد
🔹
پویا پورعلی که در پست هافبک دفاعی به میدان می‌رود، با امضای قراردادی ۲ ساله به جمع سرخ‌پوشان پایتخت پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/450396" target="_blank">📅 14:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c91f64bd4.mp4?token=bcjU1K8e1Fko3MJmBVHj0pgYIa2Kr4lPEy9MPUSriMYwZfW_3u961j3jIQWJrwO_QZqHKEFNOV37qujT9ssvtVR34NFL45365kpSNN6RnotqOeY4KsAgzWzlFTJMTTwlZAuqdX14LIIexaq4GBibhw2-IagKzdSksGarXkWQ1YMlJOWkg2oTTkI3450KzTWYRpR9RP2mKb4fL3M8SaDGjhsGNG73n4Y4V6QTTCajA3_glPHERhP1hVtR7stHbuxre1mDiAjAAZ6NvcXX3pGPpXCVAL14c65GPhckkH3f41My1Gs-rmHcpD4faOpafpq1f28Pxd9c6Mrlmg3zmfVl_DmQkOUwLnLm55w8OIjupSMpA3sypdMCrUs_tmBsAFOEb-egIGVktH_5TDAOyaSeS_QrxpuIdz0jJiGFvQhwWTOu-9NJY4_ik3A-KXXnW5aJeP5hOy6AgW-eHJLXMJXNvWlCpTP9uZaLiJCv9yNZwLRmxy3Xq30-neTMkOamZg6GOvB0kV0smY23A59vHKG-xgVSmJD8uZVsQUTUXFN1PNd0W932ahi-1vXbhiqp8wM7CkZtBB8fK4OqV2BpnXojBBCqyGmAFrvnt_Rj3v2qBaPcfKUR2e20go_bkrY4vSuNxpPJIqtvzEfhkI6Czrn3uo0BxGlkiH0XUTmw7weVYVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c91f64bd4.mp4?token=bcjU1K8e1Fko3MJmBVHj0pgYIa2Kr4lPEy9MPUSriMYwZfW_3u961j3jIQWJrwO_QZqHKEFNOV37qujT9ssvtVR34NFL45365kpSNN6RnotqOeY4KsAgzWzlFTJMTTwlZAuqdX14LIIexaq4GBibhw2-IagKzdSksGarXkWQ1YMlJOWkg2oTTkI3450KzTWYRpR9RP2mKb4fL3M8SaDGjhsGNG73n4Y4V6QTTCajA3_glPHERhP1hVtR7stHbuxre1mDiAjAAZ6NvcXX3pGPpXCVAL14c65GPhckkH3f41My1Gs-rmHcpD4faOpafpq1f28Pxd9c6Mrlmg3zmfVl_DmQkOUwLnLm55w8OIjupSMpA3sypdMCrUs_tmBsAFOEb-egIGVktH_5TDAOyaSeS_QrxpuIdz0jJiGFvQhwWTOu-9NJY4_ik3A-KXXnW5aJeP5hOy6AgW-eHJLXMJXNvWlCpTP9uZaLiJCv9yNZwLRmxy3Xq30-neTMkOamZg6GOvB0kV0smY23A59vHKG-xgVSmJD8uZVsQUTUXFN1PNd0W932ahi-1vXbhiqp8wM7CkZtBB8fK4OqV2BpnXojBBCqyGmAFrvnt_Rj3v2qBaPcfKUR2e20go_bkrY4vSuNxpPJIqtvzEfhkI6Czrn3uo0BxGlkiH0XUTmw7weVYVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از درخواست حملهٔ نظامی تا اشک تمساح برای مردم جنوب!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/450395" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450394">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBr6KQAvdo8_ZQv0M6C84ZViWyd52GLjvozV7V6DB4Z4h_mqUwIsx7kMk9a4hLxHrHdKafVang404Q6XlLxaZDgCIUEubtiXIfZUx_o_7klsi9Y3ILbaMfRGXAG1xCVCQ1aw2omzEtuCJFVaHARHAjLoXl1E7ywUS8_WCd7H9ySoF6alHI9u7igV84pUhQpIq_I9zMXy4pLLQktxMAE1kYACKNyJjJzCUQWfHr2YrDBSu1FaEQw19DdFbeEzs2Tj1yuIeAYXnQDuYwLsssfd2l5WC1HRIGheIvPQGnvlt34Zo8GLq7cpuZh2Ic1GCwr9PrDbek5YY95Ft1o_DhMB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم گرامیداشت سردار شهید محمدسعید ایزدی فردا از ساعت ۱۷ تا ۱۹ در مسجد امام صادق(ع) واقع در میدان فلسطین تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/450394" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450393">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت رفاه اجتماعی: یارانهٔ تیرماه دهک‌های اول تا سوم واریز شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/450393" target="_blank">📅 14:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450392">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f343b822b4.mp4?token=l2_g46Q8c4c5z5f-RL-iemufwiM-a2AFmuq0KgjlbZYhXRjA214XbWfXSU0ZMAEbyWAO8o3HNQObAjzHWkR80yIz1hd-SXpZcRd-G5X_stIdNqQKkZEEyEG1xWbndzKrlhOrkttDX95GuHSDZcSsB2BDhV70X17astKP0K6HeQFRh5cwcJTyi-B2KB1CQuwTTBLGoZ5sMyMeHaBWFzblJvryrPpWao_pn9H_3kGYsj7Zsa2ILRVzDsDiw8Nuzf4c43wImeDODeOal1fwqgN_chmSVS__6FIk6h9iydeJo2iEckwGL2zqoAUf1Bhlk7uUCOSOMRhhdRQKdkkJr6lDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f343b822b4.mp4?token=l2_g46Q8c4c5z5f-RL-iemufwiM-a2AFmuq0KgjlbZYhXRjA214XbWfXSU0ZMAEbyWAO8o3HNQObAjzHWkR80yIz1hd-SXpZcRd-G5X_stIdNqQKkZEEyEG1xWbndzKrlhOrkttDX95GuHSDZcSsB2BDhV70X17astKP0K6HeQFRh5cwcJTyi-B2KB1CQuwTTBLGoZ5sMyMeHaBWFzblJvryrPpWao_pn9H_3kGYsj7Zsa2ILRVzDsDiw8Nuzf4c43wImeDODeOal1fwqgN_chmSVS__6FIk6h9iydeJo2iEckwGL2zqoAUf1Bhlk7uUCOSOMRhhdRQKdkkJr6lDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸ کشته و زخمی درپی حملات روسیه کی‌یف
🔹
مقامات اوکراینی می‌گویند که در حملات موشکی بامداد امروز به پایتخت اوکراین، حداقل ۲ نفر کشته و ۶ تن زخمی شدند.
🔹
رئیس اداره نظامی پایتخت اوکراین گفت که روسیه در این حمله از موشک‌های بالستیک استفاده کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/450392" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450391">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9b24b51.mp4?token=KNT9OAX8NQPh23g6Gy9qggohBFwB51PpkBHNI1pm2_tQMzb97sozUXQP157Ff2UjxD_rvl1p7xjcDaPt7bLMVW-jovA4WPKT2zE4_aO4705Is37B1gqne9jsc1BlEEwbE6BH6Z8rKvXLuyncGAHPsXN3prySCxfU5QAYT8jD01tm3YhfUWiSizJ6LqDF8Iio33za_ozuq0G7DhPligOSUVrIMJdOutMnEP8HYayu_GDbuPAldXZwJoivo-9SRuy2kZhiwFw6rRWwWI5NRXrQIE5XALDXPni8UjS1HHbdAsbTrOcCendxR62o4xR9UZmsxpLyIF6ERQPtNT1NmvW29g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9b24b51.mp4?token=KNT9OAX8NQPh23g6Gy9qggohBFwB51PpkBHNI1pm2_tQMzb97sozUXQP157Ff2UjxD_rvl1p7xjcDaPt7bLMVW-jovA4WPKT2zE4_aO4705Is37B1gqne9jsc1BlEEwbE6BH6Z8rKvXLuyncGAHPsXN3prySCxfU5QAYT8jD01tm3YhfUWiSizJ6LqDF8Iio33za_ozuq0G7DhPligOSUVrIMJdOutMnEP8HYayu_GDbuPAldXZwJoivo-9SRuy2kZhiwFw6rRWwWI5NRXrQIE5XALDXPni8UjS1HHbdAsbTrOcCendxR62o4xR9UZmsxpLyIF6ERQPtNT1NmvW29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: رادار کشف و کنترل هوایی و ایستگاه پمپاژ مخازن سوخت جنگنده‌های دشمن متجاوز در پایگاه شیخ عیسی بحرین به طور کامل منهدم گردید
🔹
مردم همیشه در میدان و بصیر ایران اسلامی! در پاسخ به جنایت ارتش کودک‌کش آمریکا در تجاوز به پایگاه‌های ساحلی و بعضی…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/450391" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV2-HNdIaW5k7T2C2EQZbyel7jGRJNb_2WjIyPZxORMDd2nPpxVmL4ol4IN3rZUhjLqAzo1bQHyFcawfyY0ByeiTk1b-fquP1QBdk5--m_XyCMt6xF0ezXYRxWhz63wP-FgzfifjEFKNsmUhOaXlZrf7NrHaSkm-H11VY1GUwVO4bFQDMQ6z96WqVjpZJ2fyLKwUgZ26fumIEYQn0d9WhABGO1BWFj6THeuU877Ma3Lx8TtpKG0Hsg4iqGSVAX49KTOdWQNSnZKCao3zCqLIX8q6HOpdHnjhgWHCMAmDGcFc8EyaOJKcIO93qcpUS3xyFauhYx7TRHVPv79qDeYXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع به پرسپولیس پیوست
🔹
محمدمهدی زارع، مدافع میانی ۲۳ سالهٔ احمدگروژنی روسیه، با عقد قراردادی ۴ ساله به پرسپولیس پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/450390" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gaDT1rIxQxLFQjcnAd5VCHlvAO2Sqt0jnLpCVmX6GpRjfrdZPllZixSkXW9ED-IPqKYZ4KtleOkFdZsKWbQfQ_T--uzCzX48OjJkCdRZGZcX5ikuz2UVzGHvCjCczWu6__ISqmWinMPUkDAzu1B5z2dcrIat-pBuNwy8B75PZ2scuw6--NO8PbeN99otFPuCmHzXJ16IpabE3_SPNfwhhtZrhaPHX9llTy25jQf2ztzt2RowpZT5p5M0s5XTQJRl7xMkSqvWoGSvIZ0FfKwYVtPCTWdwWCWK6LUIBtvB6DGRuEfGxebdRO72QUUKLObYpeCJ1Vh-2vO3NeajpXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد ناشناس بندر نفتی بصره را تعطیل کرد
🔹
شبکه‌های الجزیره و رویترز دقایقی پیش به‌نقل از منابع امنیتی و نفتی عراق گزارش دادند که یک نفتکش در بندر البصره هدف حملهٔ پهپادی قرار گرفته است.
🔹
اگرچه این حمله تلفات جانی یا خسارت جدی درپی نداشته، اما مقامات عراقی عملیات بارگیری و صادرات نفت از این بندر را به‌حالت تعلیق درآورده‌اند.
🔹
حدود ۹۰ درصد از صادرات نفت عراق از طریق این بندر و دیگر پایانه‌های بصره انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450389" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BItrkYM2vHbEFaPx7oaxrK-E3BzlbqD26D13CxfSoQDGUl_0Zsa7vZrY24X10K4Z4sVvcnX2KjNh5YWeJhMEhBdYPFWVhOsk_VPcYojrXUqfMbwZPqbpz7SKI2CIfDbrx0ZBm20-PXXs9dX5K1eQzUA9Bb8aOHJsK_6BEMCGidhLsPEhChMpMtwD1SuFr__QHCGAQb06xUf27Ti4bjN6hl-axDxNbuIIa0Cf9X_Lrh0CrWASco5dHVy8Jtq_9kpnZHffoO7VF1i6JGze9y0OP4U2ziq7y50ImIXyG_V0dm32K-8Vxm2oRGqpidNAev_SGKG4onCMpkXHnpsT6VMoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان والیبال ایران سهمیهٔ رقبت‌های جهانی را به‌دست آوردند
🔹
تیم ملی والیبال نوجوانان پسر ایران صبح امروز در چهارمین بازی خود در رقابت‌های والیبال قهرمانی زیر ۱۸ سال پسر آسیا به مصاف کرهٔ جنوبی رفت و ۳ بر یک این تیم را شکست داد؛ با این برد تیم ملی سهمیهٔ رقابت‌های جهانی سال ۲۰۲۷ را به‌دست آورد.
🔹
مرحلهٔ دوم حذفی مسابقات والیبال قهرمانی زیر ۱۸ سال آسیا فردا برگزار می‌شود و تیم ملی ایران به مصاف برندهٔ دیدار چین و پاکستان می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450388" target="_blank">📅 13:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDzUGrCsdekkokTo91FC-4jLBD44I91lQtSOPDaEDVrwO9xN2xZkc-Y5bm-bm19--MlSa4V_7_ZcZrB1cJSvi5GgBnQW-qsBf1RcihYvpC7Kaw86jaxPojwCoo31RJ_bj_3s2bXuswpD2EUQ7jH6WJwdgVrG3nt329XvDhM7TuLEDR16vUV73zY6B-AfUiAmQvs5XMMnf6Vt1paSlTFIydvjcveq8pw-wV0dkAnwKkT8J5dfUQfHDS4dio7rdOGIwUttpoy2Enc1K0RegGoMCrPmUTg-yWx7EuVU5WWmhWh7j9-yxymYt6tHFhv_H-i7qKnqUsA_vlD_5qfA4hLdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3jbET4sMnOidY-cIi5ZY18RZ59cPv8kIlGN5QxE9NJbv__FLDaLCQgd3qti61m2l07BPJmy-6YXsu2DkE47B4ew7F_CQZlZm1sVaHgirbgl6Lu9K_YM0cPxncnzPiw0CXWQ_8h3I1SFGIwMrd_AsDK9lW2uXWxlFehO0UQpnCfrAU2bmyjfo4dWFAWyDVk7rIq5zchtqHtw5_HKdKtkqPGd6VH1UCVmYY1vJSdbYnIZpJTGJbARkeyg72c8hLmsQQgi24dVU69wtJHTFz_R5B33FL5lp_iYvBSvWDLoErrEfYhloLOSmFiR_-oRlFw6eMOeNSXYPrId9gbxEyhLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RK2-HESVy8vxndKrx6qj49Vk3le1CQi2S0JbevoU7dE64r5SpTpvdc4TulFNYZg1KjuZ_AIGG11fzNZ79tcxiDqh6rmnwqNZD9AOPxXXZZiESX3rtKUskpRYI6zV0ziKyxCIsiciEZa9JEhstHgSNslnc_nSmlZR2KuzkAYWVxhjDNAOlMHUOKsezVLyQu0UvsSRnTJ9OGSGqUjAFLMwMknpg7C-pBj4wafaXzyCVtcFZbHuV0MZB-_YC5YeqkivzdLTeZ71bDyOiT9GptQy0j_NdHpOXCtNIyx50QKFNEJcgLjkCkyvtBBbg_MjmDOBPiX0rmJkbt1l6MQNEwYEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFs71UCTc8SMqt1CvjCxPN31eWAI49vaIKV-7rJbEktO9Lqi3NUAFacB9CR_5LiJlfQDu51ty9g55bL-YvHZb7HJS09vhFjr93pb1OU0q1lTTB2Iv002jzJOnIgsY1sNOWDRiUoFkRSrUyMI29E6Od4US11zsspXqVHyxeG8E1V-O5ai2CeSGz4j0SA1Fgc4lsod5X2W9bmZjRrldAp-FMvOEM1HfuAVOXVdqYbmVYeyEHUJwHXH5A9U9y9BiL53Egtejbe-XkhEuOrVF5gLfMHmPhU31g9Uv8UGzfbWLIdDvYAUndCEHvwN3nGNedOUu9jJTs4_CYz-qnvhSMjoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzZj8yXHthSge7N4-B1crGHX2i8rbYI4ErVkTZ2DIphnybWbKrGUFXqV8C8q86BPFGKx2Ssk1SqzV3e5Bs5HPAON6Z7jcTIE5KuHU_bCDEroQ1cUddbbYfwHMJ5mt9rrH5EQ3s_PpE2r_Hp2Z-Zk3SBPd0cZO-Lzmz7rU-MqjFxV-X8nYFVEJ4Yt6w8VIXJztyCdEo6hsAgAFLjaQ8Yu38JbgJPY9GyEL-npjWddoNCGgZpJfvcQR1zHX5tisrD3WeKLZtPS6IN3POLJimqtyabkqwkN4gSBUYRkqxHNXh6mrNR8-nqQq3QZMA5cWpnDEFOvlOEym8P9JxtgSt32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvJX36bfVFkzBqvgCgIFwwTjg-tvxpCemNGWLiM5opImZ4jeuY13_90PeJtVZ7FVhrGJbzevIuq767rNrYYwACs3u9VyJa0dTfnVAjWkF087JxOXBVqbEj2AwWTD9fE6ulfpgIC7sW6sfhKKgJFC3ktGTe75NwcBLWAlosqkvcS-6OWAlh3-a7otcY0vL-kOU9ROHrejyrPGVz2F_mYiJkFFnAR72nIxHU-1EKOPaHaYwlVa7l85ZqTgyOVnqEJBW0Gp8gdXP7z-apt3qqeyukZRL2KvK2UJBJ-iXunUoosuxI8Sb3O7rdjPCKsFD96Vf3UVK1YE-LzXrMJ_-9rDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3XrI5DMmmSEVcBsN-SPhUDa6gThh4IfgWLXHxgcCD-Yla4mhGlzIGyKZV01qkZ8LrbfsGoPnjXPCQ8-8su0D_Wnw1DkQeiX2T-UJPoM1rH-G5CxFeXkiwR6lXoc5sjDoJZjrPbOm5PQ7oGP0y_WLeDn2Yp1ooJvZSuQT7M7CkQBAyjTbQeEujuLXh3NvwHelb6Pvk-B_ak60h7mEts_CbmqDdJ-f9O4Tq6svND7s-QyjqrjLpQbI2FrrmbHB6Ts433ZCORZhI0aUUS4BicOWzTr3l0-2LtwNZfB5TAUrmfGWR8yuHGpz0bDHEIl-6wUNZVcTKfOLfelKdTGPl943Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کنکور کارشناسی ارشد در مشهد
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450381" target="_blank">📅 13:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7J2_ctsh3OdQKjXfEobYoNdvvmsO4l1tNvGM_nzkykoarUVhoPH1E9pOcA7gDjgZEKZpiUMivqk560xcyrYFetTag8M2DpvAiaaDUr9BY0FXP2dnqc4LMiokIBJBk7WLovDWTnPiQNIsAmVrBgy4D0K1e-JsIcdrl16l3FEPHR2G-FVnMT_eIirKKu_7h0yuU1PeQ3H6ovfgmQ75N_npXGk9jtV_h19mHvVaUU7cBOoP9vna5PR6e6CbqNdekJD2u_kwAmr0yNkdmgCFtndxZnUfN7IzcXRznvTl2JyQKbzgaSQrWI9wD63aEOLqYzXkopY68OCJEDy7H9dAX6M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدارک یمن برای بستن باب‌المندب به ادعای رسانه غربی
🔹
روزنامه انگلیسی تلگراف به نقل از «منابعی در یمن» مدعی شد که انصارالله «در حال آماده شدن برای بستن تنگه باب المندب» است.
🔹
این روزنامه هشدار داد: «هرگونه بسته شدن تنگه باب المندب، اقتصاد جهانی را به طور جدی مختل می‌کند و کشتیرانی را مجبور می‌کند تا یک مسیر انحرافی چند هفته‌ای را در مناطق جنوبی آفریقا طی کند که هزینه‌های اقتصاد جهانی را افزایش می‌دهد. این دو تنگه (باب المندب و هرمز) هرگز به طور همزمان بسته نشده‌اند. حوثی‌ها پیش از این نشان داده‌اند که قادر به بستن این آبراه هستند.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450380" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450379">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWUCAhhhY8eZVkRTj1rIE15hOw9xvZ2faA1R4b9t0LvnLxNmRcxcCcE7N9k6cUCcbYya1vJiJYFSF8de51XItwFT5gJbEkGRBRCLYKyPeHUP6F25nYhkqzva6-n0x2gnfFsIWhlCmf9SEY4pg0YHJgn0WTbIsngO-MaEYhqj8NuUge8x1MDQHhPceYeUcRoVSnEvCTB0Tu3jP-OCR8HXwSuR42odTEfNwCXSOX3AOyjoA7TgOiuLnAFZcdNw-sUYab5va2zvnv1I2zHySfBYLTEreq-nMpl7JOwCr3RnuAC5Rj1BbXBCoob6bhHU5RL_na1aclSXxNYgwXKGpoNQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والیبال نشستهٔ ایران بلیت لس‌آنجلس را رزرو کرد
🏐
تیم ملی والیبال نشستهٔ مردان ایران در مرحلهٔ نیمه‌نهایی چهاردهمین دورهٔ رقابت‌های قهرمانی جهان در چین، امروز به مصاف قزاقستان رفت و این حریف را با ارائه یک عملکرد مقتدرانه ۳ بر ۰ مغلوب کرد و ضمن صعود به فینال، سهمیهٔ حضور در بازی‌های پارالمپیک ۲۰۲۸ لس‌آنجلس را به‌دست آورد.
🏐
ایران از ساعت ۱۰:۳۰ فردا برای کسب نهمین قهرمانی خود در این رقابت‌ها به مصاف برندهٔ جدال بوسنی و برزیل خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450379" target="_blank">📅 13:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مهار آتش‌سوزی کارگاه قیر در حرم رضوی
🔹
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم مطهر رضوی آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
🔸
گفتنی‌ست کارگاه ساختمانی واقع در صحن غدیر حرم…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450378" target="_blank">📅 12:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b23efd0e.mp4?token=kD1echTPCwxnq9huG8ZcrU3QtM2RpR7ZL7A4nZaV6MegcZCAZY_uqIIQcIxNfU2OqyRhCErzmt5AkyuGWsHHhrNmnTWVK9-YZsmOjmmmV9leGNJ4WvGQ33Lpcs6modalkDHvRhFMiyH4iEZ50LaPYONKgf1j103ZG_QnGnbe1NFZ_frWep-TYRTqrjAlun6xmfbLGXtH9iQDMdLNTWeKnYKt517tvZAJFnfSfk-TS5IEDjNjN5YQLj-DdPxxwNvJv7snuQaubo6lLBP0EUvEzwksSXg_ytb0ARVQhl9RT1jcTobeeI8ymZ9FDi4puyIZnl0qkQZW9xxStguV5sDLsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b23efd0e.mp4?token=kD1echTPCwxnq9huG8ZcrU3QtM2RpR7ZL7A4nZaV6MegcZCAZY_uqIIQcIxNfU2OqyRhCErzmt5AkyuGWsHHhrNmnTWVK9-YZsmOjmmmV9leGNJ4WvGQ33Lpcs6modalkDHvRhFMiyH4iEZ50LaPYONKgf1j103ZG_QnGnbe1NFZ_frWep-TYRTqrjAlun6xmfbLGXtH9iQDMdLNTWeKnYKt517tvZAJFnfSfk-TS5IEDjNjN5YQLj-DdPxxwNvJv7snuQaubo6lLBP0EUvEzwksSXg_ytb0ARVQhl9RT1jcTobeeI8ymZ9FDi4puyIZnl0qkQZW9xxStguV5sDLsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حبیب امنیت
🔹
مستندی از شهید غیب‌پرور به‌مناسبت سالروز شهادت ایشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450377" target="_blank">📅 12:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مهار آتش‌سوزی کارگاه قیر در حرم رضوی
🔹
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم مطهر رضوی آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
🔸
گفتنی‌ست کارگاه ساختمانی واقع در صحن غدیر حرم مطهر آتش گرفته است و این موضوع ارتباطی با خود حرم ندارد و در کارگاه ساختمانی رواق امیرالمومنین(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450376" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf7PyQh53Tz_HFbsueVcfwdXx0wJjhbndLWzw-fMlO4ISUMMUb3Db_tHP1fXqPr3TH4jU5WPHG1YU1Wz0vJxB1Yhy9zg246YATnCsP6nrH4KYOK-ceAjmFBhprWlTy5NgQlF0ot20NYW5RJD7VqKmQugc-TQYnfb1m3v9BkFv2a2A2GFmA0mhD09KNEqNnxik95Ksq3bl8S16pg4p1ylrhQyXcSmfXMZ7Y37SlFfHmizi3cu71qiUda9T4VwbVb7VKu1qkauBUIFB4kQ2C6c11Zel3dwZ-f0_cFHClH_hZDXTUaiVrgl_DdvsNiafUbAZy2Tg-FXglXeI4mykKYQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضارب آمریکایی: می‌خواهم همه مسلمانان را بکشم
🔹
مرد ۴۸ ساله آمریکایی در ایالت یوتا با بیش از ۱۵ ضربه چاقو به یک فرد مسلمان حمله کرد و در بازجویی‌ها به پلیس گفت، قصد کشتن «همه مسلمانان» را دارد.
🔹
طبق گزارش برخی رسانه‌های محلی، پیتر مایکل لارسن روز دوشنبه به سید سهیل الدین نزدیک شده و نام و مذهب او را پرسیده و قبل از چاقوکشی، به او گفته که یک بطری آب می‌خواهد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450375" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">واکنش‌ها به برخورد با یک کارمند به‌دلیل امر به معروف در دانشگاه علامه
🔹
اخراج یکی از کارکنان دانشگاه علامه طباطبایی پس از تذکر به چند دانشجو دربارهٔ رعایت حجاب، واکنش‌هایی را در میان برخی فعالان دانشجویی، اساتید و چهره‌های رسانه‌ای برانگیخته است.
🔹
درپی انتشار…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450374" target="_blank">📅 12:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6eb1b5774.mp4?token=LLh6rK6Nqzyqa4cDlaNuf2gkhlGvyebxs2c7ptNeo4ZRRjVaFc67FDyaTwqb1fbhJed7F5h5yfBgliz21wnevMmQwpKn3VbnRjP92O6l-RexAJod3hfWeTtaUPz_tvBJlGoQhNPhmJwJJeOfdRiKwqK3D3JZP_itpjnxx8Ft-8Yz1JLoxLZl7td4RficHKc2EHK9MApsyZnRCFQpPfW_uEFJkS7mt5NDSO0einKH5ybsvKwQBCtuc-jwGHk9z9AEFNxt4TbQISW0vUOP_F-3HtIM_f77Wn1NVAqqE4fd6AMBD0vEFnKppSCK5X0GaBkSkEryw4ImuRykPrY7ugNnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6eb1b5774.mp4?token=LLh6rK6Nqzyqa4cDlaNuf2gkhlGvyebxs2c7ptNeo4ZRRjVaFc67FDyaTwqb1fbhJed7F5h5yfBgliz21wnevMmQwpKn3VbnRjP92O6l-RexAJod3hfWeTtaUPz_tvBJlGoQhNPhmJwJJeOfdRiKwqK3D3JZP_itpjnxx8Ft-8Yz1JLoxLZl7td4RficHKc2EHK9MApsyZnRCFQpPfW_uEFJkS7mt5NDSO0einKH5ybsvKwQBCtuc-jwGHk9z9AEFNxt4TbQISW0vUOP_F-3HtIM_f77Wn1NVAqqE4fd6AMBD0vEFnKppSCK5X0GaBkSkEryw4ImuRykPrY7ugNnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید شهیدان حاجی‌زاده و محمود باقری از شهر موشکی زیرزمینی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450373" target="_blank">📅 12:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sfey1ZJKluXiPXPO9BtyZJViUUfjM__I9VePIJvcLjYmQeuZzJ1UjwoTI0KwzjpDNPRLbKYXaWfFqpsYkAudw0RWQY-a_DASIiJ6392mTj9fu2dJXdohNsT4YI6HtOIC3kTeVvdVqGvp4fabjK8kJF0ebr5sKrfccOdpzVGDydqoTiPvNrt5bNE5dCawQNCzeg30HWxnkMDOrbRav-Dq6bS-e49B4fLPI8wzTQEa4k23KGoM1J3DxOOU01rAoZik8pOp_uAh0dA8wYnakpOz1G96VftkJOavft3sbjgndUSdgEJY9QzIiAEfSWxvQkzNkDBjSRM2ZZ9iucF4FpxBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها: اخراج کارمند دانشگاه علامه به‌دلیل تذکر حجاب را تا برخورد با مدیر دانشگاه پیگیری می‌کنیم
🔹
کرمی، معاون فرهنگی نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها، در واکنش به اخراج یکی از کارکنان دانشگاه علامه طباطبایی…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450372" target="_blank">📅 11:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Gv4mZKaViyEGjWNb747H1M5cjqN2a_MNvAqbAr0eB-xivwzqDugUI7KNNc2Yf1J1CTwyyEt6W_ZXpO8bGweHiMRsQO063T_6uGPBtrjkWBCjvVMlv4G6W0CQx1hvCsc9c2LJQ3MTwiw-8pB-NER2AxqXq8U44w-EbD2klHVVLAEeeGCmj0Yo9TPR9uyu7tNPaqA-HYRGLd6WxaddzTsNfyuXxWT5sMzEfPiMa9v364xz_oaJzCq8yRsRNb0JI9W0kJ6WmmOqatiUsAwrqVq2xYQcsetYFK3Gu-UgK8cAqMQtOBzr_vhyRxBMBt91p8gNrgY5D6v1WMXJZibU7eBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک محمولهٔ سلاح در سیستان‌و‌بلوچستان
🔹
فرمانده مرزبانی سیستان‌وبلوچستان: درپی توقیف محمولهٔ سلاح از قاچاقچیان که قصد انتقال آن به کشور را داشتند، ۱۵ کلت کمری، یک کلاش و ۱۸۶ فشنگ جنگی کشف شد.
🔹
تلاش برای دستگیری عوامل مرتبط با این پرونده ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450371" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انهدام مهمات باقی‌مانده از جنگ در شرق بندرعباس
🔹
سپاه هرمزگان: به‌دلیل انهدام کنترل‌شدهٔ مهمات باقی‌مانده از حملات دشمن در شرق بندرعباس از ساعت ۱۱:۳۰ تا ۱۴ امروز، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450370" target="_blank">📅 11:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984732b934.mp4?token=h65cDlW1dfWr9WMLt0opoXL_s7-Xv5Z9MtUyv8pSc8bVsbxq2RP41cv6Z_NEOnnqjJl5_wzIC1Mu2cS23BO6yrVK4FiDkEDnLVr7zgWObuHPcpc2ZZWYhJR3ykR4XEx0uNrgT-chigFlWyzF8PZsqDBafjF086wQFVB_2KOu5wdD_Ylw4GrZhIm-wuMGfBhGTDvDM-jHgG2tC9BnaVAK8p6SaNgh8ccPmcu6FEgUL4uytfTuAUW96z1NkJdyh0ZqLa2HxkTHh6EH9RKN9Rj3_BlCIErkz6jqZurKzlMgO6V0oaCMoqMwwQHJXtBWcN3aystLu6ylIv7k_SdH2fCzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984732b934.mp4?token=h65cDlW1dfWr9WMLt0opoXL_s7-Xv5Z9MtUyv8pSc8bVsbxq2RP41cv6Z_NEOnnqjJl5_wzIC1Mu2cS23BO6yrVK4FiDkEDnLVr7zgWObuHPcpc2ZZWYhJR3ykR4XEx0uNrgT-chigFlWyzF8PZsqDBafjF086wQFVB_2KOu5wdD_Ylw4GrZhIm-wuMGfBhGTDvDM-jHgG2tC9BnaVAK8p6SaNgh8ccPmcu6FEgUL4uytfTuAUW96z1NkJdyh0ZqLa2HxkTHh6EH9RKN9Rj3_BlCIErkz6jqZurKzlMgO6V0oaCMoqMwwQHJXtBWcN3aystLu6ylIv7k_SdH2fCzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات هوایی رژیم صهیونی به خیمهٔ آوارگان غزه
🔹
رسانه‌های فلسطینی از حملهٔ هوایی صبح امروز به خیمهٔ آوارگان در بندر غزه و شهادت یک شهروند به‌نام ریاض عروقی و زخمی‌شدن چندین کودک خبر دادند که همگی به مجمع پزشکی شفا انتقال یافتند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450369" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj4ORiMdyKTNvqApSa-OppS5m8Aj5DFw1tBngNpLb874sPp5DS47reF23XxCZlysYfnZriiQV6S5wxwm98wIKgTFZ6DSXSAWZx1QebrldVC9Bly7vs3wS_BRGJsPUcl0ldhEyFX_O0nq_0GufCvCfr2TJ8E-UHigPRz9PMiugfDI8dLMQxxo4vVQPXcXGGNKOiHzPGBa6w78lT6uRjLiNk09t15pVFkuUw6gXmvt6mDear5HsWQ0SAtnYIcgYDFz5SiYfKzrzBei-x72Usmm5qfiyxSz-FgBBg_ubpIQ8xuvGERMJQf1oUeBn_Rbjo6fEPcLIQuJxbwvETLOIAEYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم میکس مردان و زنان ایران قهرمان جهان شد
🔹
تیم ملی تکواندو میکس ایران صبح امروز با ترکیب هستی محمدی، باران نعمتی، محمدحسین یزدانی و امیرسینا بختیاری با شکست‌دادن مراکش، تایلند و روسیه قهرمان جهان شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450368" target="_blank">📅 10:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXUsYrBLE8PtdXhMPpNLZD3PW4LEt8gNrGHFUjP9OpXHWh47t-EdSh0gi-qQ3DaUAg7jE7xIUgNZ-mzQzVg5PAKpDXnad7LCQNEs7hbfBXfZ18A5817Qi25VQEm12g4Wi4JZNql57odCxHUW5o-O_kOOyOCs5kuolK35Hv7oizj4B_PhxdwXz5WSsAOAQlQiueVwwWl-81LeCmOyBKSKsqlG0ekqZB5UreqOFleptaCsrnfMGOpqf_s9F7y--aF9EGfYaFfO-z4TCeNvAc_RxS_pxfuPNrPqDYOAT_GotRdeb_z4Ei3U097zoogamdX97xdaVDRNc3X4eRVjoEVFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا حملات خود در ایران را به اسرائیل گزارش کرد
🔹
وزیر جنگ آمریکا در تماسی شبانه، اسرائیل کاتز همتای اسرائیلی خود را در جریان حملات علیه خاک ایران قرار داد.
🔹
دفتر وزارت جنگ رژیم صهیونیستی همچنین اعلام کرد که در این گفت‌وگو، کاتز بر باقی ماندن اسرائیل در لبنان، سوریه و غزه تاکید کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450367" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGAd-Dn4Pxh6GcCuZa-E6p5J9LMuaePhoQa1mkyvnS4nof2QHB0hiSM-pyQfoappYnSdtuKYG826AKkRv4by9F5ca5oZl3r0q9kbgKiQCV8RLHpJf79uRxPYKu3DqmElbQVr-ZH8L5VUcYyT088mQ4CEjEpqFGunMkU4VbM1rUH1e0oO8ZIHMVAleoPCQiIM5d20OCY15EyImojMlDZUIteaYkedvUqyn5rEbKew6AQ2IIWRyK4d9yeZ9QYTp_L0Jm730EBP0Ev4OBlHODFHeSw7o8THP854mUrefyVtjUZOeeLz4xkaWjNIRjVCoMiq0zngW6DeqyLxfyNv_Wjg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g09jTl10JfJPNbm2BUd1oo9I3Me3QKs94ZGGMEZewKngHarQqwzW7ug721x23HDPU2OVIKEC-TRp90B-Ked6hYn6Wwk2qzp6dDWTY-DJBV_LEXD8TDX_nboT5e0YO9FYDJT3-VtvciQc5eRmd8Scf0KniilCoaO1NJe_wVIBNcWnsugZjJM4qca6ImZ9-_qi9rsJvC749WqrOrMFfZyxbim-jnYVcBDX--1O2HtdqapyGurIJzhm4-zPjqyKHV2Qn6SdOfGa8-KNr7T7GQfxOEhD77ZXrWr2288RAL4wYkF9l01bDwU5JO_aKc--24N5oIkoABKbGK4d01HBGBr_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMj90t7rviGe6E93reDM0-CduV-T5UDiMmQGDpkPGZsPxIWLHKG2TgPLw1Y2_lWgZ5WAUT_-Ukwr6aE-jUW1fu3LdLNdOYx6NykGK2CDtIRyv0S47ERqnwAHQKagZGLHF9FC4J8VoMYwUeEeFE0V7xbfkj4kVtgmY4owtao7vvBj8yaGg1NzLQEq_NCKbBH1Iad-78-OZYCgaRyuHcQ8fDL4QYpKWVF5Z2FP8bvmajukWwuEby8D2UEDAkkgABIOv_FGA60jYs9mtEcTC0qZmWk3xKkiATUzI_GhqlUJ7r9B0KJ5kCsGRp1G4u2HoMBhlvw2qaZpzx6KMcKJ7DiZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F79MT0wWbsjKbK7GDTUS5YWsVUUC7FoH9EZA4iGa6MvVU_zYRa_30MJ_x9855Rq5auQ5klNYrSi8R0u5eUafbcaE50wTgykxTeY_7fpZIqIb48yUOvJ_EowNTsTfHPa5XCgeWpPIEK0uJfAht7U7ipuOk9qyAEYpSpFkIGQpTyStjnIKrSzft_qtQ_WztPqaPETaw8ICXHrbsDs-V-3c4OLAYdjhli9F3L4wpT7KZ6Jml5jZ7Ddic33lANPYpPXYjjT_7SgxnTNuyyFyfn55wbwkqK2DP80d7NcGpDgChKRfrKnq9eFap1tfC0s0LqtIwx4lE4cFdiUkIXvng__CjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZXIGPSi4r3pLwWvSDpO2qxSp0mIUhRpJq-xe_O2W9DnZvobMQqPfRdejtekSVEe7oHg1ywlFYKXWNhNEvFG0ThLuc7M_bLY6VXaZzASsu80jxsIFS-oVCOeC4f_2NO6EJ3uVL6vFA6JcUkfIlKPp_hnTiAn9ea8juM17P_NeqtyOA2iZqYeq-AmeFCDEtIFSwt3n8UmuZX73dRqAq8FANXEtjhXWYuVyfYs5yRPKTF1_c8XrKeh-mNcfnrY2C8e5Hmoo-I_0Un6tB4M2xRc0Du7-b8Hto1OgJXzqwKOAnABKWOzcBb3iYP2OnBVXboM1it5GjXbrYy6yF5D0FjFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Syyvq61diqQh21Nsrj84DVbJ08dha3eW-jLjyAIbGajro_Rpsm1ZaBzmlNnkVprcePIPfEEsqlH2n5JemNnawC6xiqiDkC3oOpJivDZ-F6cnc-Yx88g5Fjuuwl_A0SJJlT39gKdGId_uHzoWeOsLaYK8Kc0HB1U9JjJRwTdNRDVOryeQ5W-gx1AGRfJZxser-LBsh-SIBfv0LnuLzuxiheZn5njvtCLULiIAAZ5EX41u--7gK4bMq6nmOBudHXA3ooaa2g1Uo9Bp-Uc-uoB9bp5LSldgTqpq58sSRJOGpcejclGacyGaQGRYeNWdOLK7kd5qIbY1Lo4EfpZkLOhSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_IxKyrdhrzXpfI6zEX4sdcbaK43C7onAj0P_uU7nfEHII9ht3rCdbrVFhfzchnKPDMcZ-exz7K8KB77Z6hJv3ojL-O3h-BN_IY4kAWFFvyeshDHw1hJS4AwjhbzhWieh06X9LEHbNA-WqANfCCOwQutRMdDsx199EkAxRC2kLyhHZcQVXFLUnNRA8ENUB0WUhzsazIZZA9T_nL70G1X-itwl9Tra40Ai2oX1o4LH2DCoLuLMzsBcg4Cn_fPTm2TkSkdq2ssyChCWZdt9Qu9gkRv2Tgc0ifIKShctzcTn6_sj69-nr31C3YIaohOb7IYu4I7ZRXsjrr8iK2lzKlURQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت طالبی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450360" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آشپزی با چشم بسته روی آنتن زنده شبکه سه!
مهارت عجیب یک سرآشپز همه را شوکه کرد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450359" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#دعوتید
به بزرگترین سفره نذری حضرت رقیه سلام الله علیها
🎁
همراه با پخش گل سر و جوایز ویژه دختران
🎭
اجرای تئاتر “ خرابه شام”
🔰
قرعه کشی کمک هزینه اربعین برای ۱۰ نفر
اطلاعات بیشتر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450358" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450357" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0w7fm6HfoApSgsKUwp9INacUeaLvUuUCLa0T4XEh-3TbDk21lpZH47LY7HqlgM8XhOTN_sLipkb9Se6eyBCrwRqQqLbld-0MM6If_xYNz2y7P0rNxgBqSgIlwXghfncziQptIPhwXsXCSc33D4xjh3Rs4uSxTScnOC5fSwSJbNvm1st3rRokIATM2SE8W0qPGJz1E34phN7txz4rm_0ypdPHymvsTNjnMDLH6TeGOlR60XuwJVlD06n5Ij_ENyUIfpNxxXp4oQ7XsYl1TsjwAO_jzkgGsIvf2GFyU4DRdwEY48YkxvS7zkA7TaEh0QXYfXEH9GcDLwoQbY-RjVTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات سوسیس آزاد شد
🔹
وزارت صمت در نامه‌ای به دفتر صادرات گمرک جمهوری اسلامی ایران، رفع ممنوعیت صادرات سوسیس و محصولات مشابه را اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450356" target="_blank">📅 10:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmw8gv8fttvFz6BpOfXaWsHiZRKfM90sH6fdjC1csC0YCxUZJ1AULpXf1WxL4CBC1lNVtkCXLDFEqOxP3SJ8uddBIjD6VcGCw38L82wwCMOFKxjSn_GqW67aquiV29XrXT5Hp3HaZydZIQkjQdtIR2JbtLpXK8vFcKk33WP6cl6YNP2gou9kOI0A2xnxUF1vWnodHSeSO1QN2gIk8z-oe41Al2tVTPetGbgLTNZj8B5i3XPxgxcrAfQy3FM6HslkELx5Kb8hfsVQbywE5fnulWL9IOfX9FslFdciRww8ZX8L9CV30BdYudwp_CPgW3poie6TIAGi146tdbdzUY1R7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: در صورت تداوم تجاوز آمریکا، جنگ به عرصه‌های جدید کشیده خواهد شد
🔹
کشورهای فرامنطقه‌ای باید در تعامل با ایران بر پایهٔ احترام متقابل عمل کنند و نیروهای مسلح کشور نیز برای صیانت از امنیت و منافع ملی آمادگی کامل دارند.
🔹
ایران هیچ‌گونه تقابلی با کشورهای همسایه و اسلامی منطقه ندارد و همواره بر توسعهٔ همکاری‌ها و روابط برادرانه با کشورهای منطقه تأکید کرده است.
🔹
بخش مهمی از ظرفیت‌ها و قابلیت‌های نیروهای مسلح هنوز به‌نمایش گذاشته نشده است و در صورت تداوم هرگونه اقدام خصمانه علیه کشور، پاسخ ایران متناسب با شرایط و فراتر از پیش‌بینی‌های دشمن خواهد بود و عرصه‌های جدیدی از تقابل شکل خواهد گرفت.
🔹
نیروهای مسلح ایران حفاظت از امنیت، منافع و عزت ملت ایران را مأموریت اصلی خود می‌دانند و در این مسیر از هیچ تلاشی دریغ نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450355" target="_blank">📅 10:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0JbXJ7Cxs23wnZZX7w3QU-rxTCjwChAIgEj85tqw29sD7z-HVjg56OZhRQhigoYi40zqLobDu8P-F6mRtGZDTVu6hcjImeCrFeEmihyGCYKhKkwFCPlKP-tRJGizP3k24SfMmEDAkG1s8do2oN7O4rlSGGQZ88ilc_j7XGMaN09maqJJMxilBDCudbNTdv94wd-1EzGSxm-ubH-pVsbnBqsVmFs1PgMnuG6dLMWO4IGQfVhqVE570CjiOv4BSnECtFll-ufslWyyKl5yuWkpSBd5dC4m3EukDjozahJvRCVobJVSWRJL8NdY4o35sTr37r4De6L2woOtY8hXQtxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگداشت هفتمین شب تدفین رهبر شهید در حرم رضوی
🔹
آستان قدس رضوی: مراسم بزرگداشت هفتمین شب تدفین رهبر شهید انقلاب امروز همزمان با اقامهٔ نماز جماعت مغرب و عشاء در صحن پیامبر اعظم(ص) برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450354" target="_blank">📅 10:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsrJ-2jUvSR95rp0RIHvEGebzhTMdtQLQIXVJ09oMrv0qA0PN-xCXPny7kkVPvu3RFgDE9xjy2QCU_M6Pvgm78ahPtyDAsXrZGGdt6C2lyD6ADvYJ8tgigATMcym_HuXMAiUBUM7ShNGkk7OMdUri4ybqA-GJNs_CzBlDCXKVoAFBL1AtD_f83NzJJPF8klJo4IwxppFZjNVvSWcpbcnpewoWVcjZT6vZVDRo1zYrMCT2Swh8TV95SCbfvvtN6AItdkBadcbZ3sLCm11WPPXKGtSa6cegab_jzmXoCJPqR1UhECMfGPjKgBQnoJTc9NTQGCVUZkn5IE51L4-z0WdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفهٔ ۲۵ درصدی آمریکا علیه کالاهای وارداتی برزیل
🔹
وزیر خارجهٔ آمریکا اعلام کرد که به‌دستور ترامپ، تعرفهٔ‌ ۲۵ درصدی علیه اکثر کالاهای وارداتی برزیل اعمال می‌شود.
🔹
دیپلمات ارشد آمریکایی در توجیه این جنگ تعرفه‌ای مدعی شد که دولت برزیل در مذاکرات با آمریکا، حسن نیت نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450353" target="_blank">📅 09:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd585a60f2.mp4?token=SFc2-NwUVEbEC_RDbXMfcPWaru5V2oLrNWTwUj2dWHNc9Xg0qCdB2dWs_kiac8C4U6N5PDwIcmKnVL-ppbu8OAiSqyDgC1Ghng29fcXWjEj28o0Hz7wDEKY5kXqnIg3Y72qZemLr-BfraDgpM94yZSq8hovlKTYSXhswQuW-PWv3cg5UyTiv3R7y1q3fFEUi085SIUBijlh5OxsSGglr3r4GUs8luAkdZtZzC8pq6kU-_gPnvTcOl02OR7Ar_oAiANLupV4R1EvGChnJorStecJLsFIsl57wXYN_bpf9Ed_iAjY325twF2s7vHnsmAUl0wSzG3FEOX_iMyVaUdpKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd585a60f2.mp4?token=SFc2-NwUVEbEC_RDbXMfcPWaru5V2oLrNWTwUj2dWHNc9Xg0qCdB2dWs_kiac8C4U6N5PDwIcmKnVL-ppbu8OAiSqyDgC1Ghng29fcXWjEj28o0Hz7wDEKY5kXqnIg3Y72qZemLr-BfraDgpM94yZSq8hovlKTYSXhswQuW-PWv3cg5UyTiv3R7y1q3fFEUi085SIUBijlh5OxsSGglr3r4GUs8luAkdZtZzC8pq6kU-_gPnvTcOl02OR7Ar_oAiANLupV4R1EvGChnJorStecJLsFIsl57wXYN_bpf9Ed_iAjY325twF2s7vHnsmAUl0wSzG3FEOX_iMyVaUdpKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی قرارگاه خاتم‌الانبیا: زیرساخت بزنید همهٔ زیرساخت‌های منطقه را می‌زنیم
🔹
تحت هیچ شرایطی و به‌هیچ‌وجه به آمریکا به‌عنوان یک‌کشور بیگانه و فرامنطقه‌ای، اجازهٔ دخالت در تنگه هرمز را نمی‌دهیم. این، خط قرمزِ شکست‌ناپذیر ایران است.
🔹
در صورتی که تهدیدهای اخیر رئیس‌جمهورِ از تهی سرشارِ آمریکا، مبنی‌بر هدف‌قرار‌دادن زیرساخت‌های ایران اسلامی توسط ارتش متجاوز آن کشور عملی شود، همهٔ آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی ایران در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.
🔹
دشمن نادان بداند، لحظهٔ حماسه برای ما، لحظهٔ پرهیز نیست. آنچه از سوی نیروهای مسلح ایران رخ می‌دهد، ضربهٔ هم‌تراز نیست، ضربهٔ برتر است. ضرباتی که شدیدتر، گسترده‌تر و ویران‌کننده‌تر از همیشه خواهد بود. آتش خشم ملتی که هیچگاه تسلیم نشده، دامن متجاوز را خواهد سوزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450352" target="_blank">📅 09:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: مرکز ارتباطات ماهواره‌ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
🔹
مردم شریف کویت شب گذشته ارتش کودک کش آمریکا با حمله به نقاط متعدد در خوزستان از جمله محیط یک بیمارستان درمان…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450351" target="_blank">📅 09:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: رمپ نگهداری جنگنده‌های آمریکایی و مرکز فرماندهی و کنترل جدید آمریکا در غرب آسیا در الازرق اردن هدف موشک‌های بالستیک خیبرشکن قرار گرفت
🔹
مردم شریف و نجیب اردن! شب گذشته ارتش کودک‌کش آمریکا در یک تجاوز آشکار با استفاده از پایگاه های هوایی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450350" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450349" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwVtle4GNwZkR-Lt2C8uDAjNcHXkmzZhegMbTAK2Sl6FgoXFxg2EgTLgmqdTAbm834g8WfVf2PZzoKFrmDeMZn7npCR_SCYUD5VZSMaLVH4pAe7MDbm0X_EOMKeYstYvB3m7L66XyJi6USULKS_txRKNq3xGiEBM5rgPCmzJq47LZkxRnwy7KWRKAhSCAsc3I72EsF2tOd91WQMM88dch9iaE-XnosKiYbfXTxRpLbpajd1o4gm4coCZ8sgBE3WGKvfgDHAqdml1nNj7Ec4GUzOUA5BBfFCS3cdHx1bbAxRfAWBU8_geLzfQBJBf4HJjXnhT5M8Z43phTPINmevxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام نتایج نهایی کنکور کارشناسی ارشد تا نیمهٔ اول مهر
🔹
سازمان سنجش آموزش کشور: نتایج اولیهٔ کنکور کارشناسی ارشد امسال تا پایان مرداد و نتایج نهایی تا نیمهٔ نخست مهر اعلام می‌شود و پذیرفته‌شدگان در نیمهٔ نخست مهر وارد دانشگاه‌ها خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450348" target="_blank">📅 08:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حملهٔ بامدادی دشمن به کبودرآهنگ همدان
🔹
استانداری همدان: بامداد امروز نقاطی در کبودرآهنگ مورد حمله قرار گرفت که این حمله آسیب انسانی درپی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450347" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌ جزئیات حملۀ بامدادی آمریکا به سمنان
🔹
سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
🔹
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
🔹
خوشبختانه بخش‌های…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450346" target="_blank">📅 08:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450345" target="_blank">📅 08:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f57a8907.mp4?token=j9UnYYZCcr3T1ZkNAvf74_YKAuUAejPdjZb00vA3lzMQ8fUb7DCy_PEI6n-f-igFlav5skFkjoQdypPcELSm89IM11Jmpbh6TUg91PoS8clYPu777yYoLU1Dnh1-fhFDhw4JUeF1P3bBWyhLX0e1-wX2VEo6cJQZ_S_uo9UkvxeZnXFAn1Wpy-eZObspf09-PSOl8NRAjFC3tl93kFdt3mvuGZ441UAA8MSKufaU2KQxBqGatK8qOVIr4NsLyp2HE51ptDZ59_yUW9I_LXMrwfpi2eXdt5rweuq0u0522eW9ga87cQwFxJV0U7Nmv1u-i7ROVhCESgDPRwnJeeVncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f57a8907.mp4?token=j9UnYYZCcr3T1ZkNAvf74_YKAuUAejPdjZb00vA3lzMQ8fUb7DCy_PEI6n-f-igFlav5skFkjoQdypPcELSm89IM11Jmpbh6TUg91PoS8clYPu777yYoLU1Dnh1-fhFDhw4JUeF1P3bBWyhLX0e1-wX2VEo6cJQZ_S_uo9UkvxeZnXFAn1Wpy-eZObspf09-PSOl8NRAjFC3tl93kFdt3mvuGZ441UAA8MSKufaU2KQxBqGatK8qOVIr4NsLyp2HE51ptDZ59_yUW9I_LXMrwfpi2eXdt5rweuq0u0522eW9ga87cQwFxJV0U7Nmv1u-i7ROVhCESgDPRwnJeeVncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ پهپادی ارتش به سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن
🔹
پهپادهای انهدامی ارتش در مرحلۀ نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/450344" target="_blank">📅 07:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB0XFI8zE3Jr--ri3JfP_zXLtMW5HSxapOmxZ5-313UG7d37nkcVvCiHmZcD1Hy36PgE5270AK2PiLFDLjKb8FOETRxd9lGH8t5scKa1K5UuRRV_SutliH2btilY0b_XNS1oqNxhzYIZY2Wsev0JBqq50JdJQ56A4_2qmydyjCgqi83nsEo4uTCfyzimvGsOp1NRaiYTUJG_1ccErL5wjXLm3M20k1XhPvIKD0jLGUmOnv0IMe0ymxdN6XLzom1-5EKjOGG6hzKZulrwJT6nFBrhNopSDg14TnpVfiM6ptRnHWJrAzN_GzKi8w8hNo-faDzReCfWytiGFghuGiLfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: کنکور سراسری قطعا  ۲۹ و ۳۰ مرداد برگزار می‌شود</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450343" target="_blank">📅 07:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4Zh-XhLjLsy6rO2IZRWjL9WLdGWTykce3eZ2zdvg-0w_IX3TNPMwL8NUQK5a3W5Sqzs8iD1UuE0yFmoU2P73uVdYOR3PTvgtQPIPOvYB2PIe4tA_CXwj9dyCAqUPot8oAOvnFb03klNylUIE-_QciS7jGxaaxgWKN3mJKep7Z3c2MBizX_9TOTiQ5MD8TJrPL99-OzDgEZ--WcbaxJxKlNAc-33CCf-q6KX3NMcoOHCaSmuJnPdLALTkHtvfUFzK6q9i_YxrwRqtswTLvtR6vWuTN6vnVmtl_YPyACaEjziT_R3xjud-5Cj76EXMTjuPPPwKf6VR9SOwzyHMSrbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا برای حمله به کوبا آماده می‌شود
🔹
شبکۀ سی‌بی‌اس به نقل از مقام‌های آمریکایی گزارش داد که پنتاگون در حال آماده‌سازی برای حملۀ نظامی و تجاوز زمینی به کوبا است.
🔹
در این گزارش آمده: راهبردشناس‌های نظامی در هفته‌های اخیر طیف وسیعی از اقدامات احتمالی علیه جزیره (کوبا) را بررسی کرده‌اند، از جمله حملۀ هوایی ارتش که شامل هزاران سرباز آمریکایی می‌شود و توسط لشکر ۱۰۱ هوابرد انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450341" target="_blank">📅 07:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
شنیده شدن صدای ۲ انفجار در خرم‌آباد
🔹
دقایقی پیش مردم در خرم‌آباد ۲ صدای انفجار را در این شهرستان شنیدند.
🔹
هنوز محل دقیق و منشا این انفجارها مشخص نیست و تاکنون مسئولین استان در این خصوص اظهار نظری نداشته‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450340" target="_blank">📅 07:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmQ5-8-wDSdC_B0_5Susn507Xv5DBwM6TJFU403N8qaj3HNyGeaqQUz40Kcv-klpv-ZBzaI21v00JsgSarbFGP-yFdr8xI-P4qmbwitZb-xFBHBewXbUQNGeeUp0AntVB5Z91UJQM0xyKqUyIrbwdUvIilcptA0RoKbslL_GTVVqius8Gr2_eAKL21FKYTqhqbUEPviHdYxDQB4hxNkVrYO_8Y1qqyUbPuWcsHhPE9swoGj6usvnpHPFSx9i2WUYfMHiofvwQKUm5i6twrhEat3IYUns3NVa3HYlIdFsuaDPtFMKs3zWLZGjCaJxhxcfFA_AejUFiOY7JhsUka3rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون یک تغییر در دادگاه تلویزیون
🔹
برای مدت‌ها سریال‌های ژانر حقوقی تلویزیون از یک الگوی آشنا پیروی می‌کردند؛ روایت‌هایی دنباله‌دار که در آن وجه داستانی و درام ماجرا بر موضوع حقوقی غلبه می‌کرد و بار اصلی قصه را برعهده داشت.
🔹
با ورود «آقای قاضی» به آنتن تلویزیون، این فرمول دگرگون و با فرمت متفاوت داستان‌گویی و اپیزودیک، تجربه‌ای دیگر از ژانر حقوقی برای مخاطب عیان شد.
🔹
درواقع «آقای قاضی» نه ‌تنها فرمتی جدید برای روایت درام‌های دادگاهی در تلویزیون تعریف کرد، بلکه آموزش مفاهیم حقوقی را نیز در دل یک روایت قرار داد.
🔸
فصل سوم «آقای قاضی» با عنوان قاضی بیگی درحالی روی آنتن می‌رود که بهزاد خلج، بازیگر فصل‌های پیشین کرسی قضاوت خود را به مهدی بهرام‌بیگی خواهد داد.
🔹
سازندگان تصمیم بر این گرفته‌اند تا این نقش را با بازیگری تازه ادامه دهند. انتخابی که از یک‌سو می‌تواند به ایجاد تنوع در مجموعه کمک کند اما از سویی دیگر ریسک قابل ‌توجهی نیز به‌همراه دارد.
🔹
حال با ورود مهدی بهرام‌بیگی باید ببینیم قاضی بیگی چگونه از زیر سایۀ قاضی خلج در نظر تماشاگران بیرون خواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450339" target="_blank">📅 06:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec13e6c9e.mp4?token=cw0Ex9Uh6Egi1fJctRcpaYYmOTGhTeUx86xeA7BJMN6iEWflMc0PTx80O7hY0IQONXUdviasYg8st2gxOiFOfW8o3QFSlLfo03LksDECbxcOKhaJVeKPHiCw2hzs4ihTGvyn4QLsozCahyYXkZRqorlrJCTMNikdm5AaVc6yFLGnDefE0OGcZsQrrjAoO5eZYN7tQLWtOm_pEIrEFTUrIN8JCzMUqlASoEnJtdFJBzxf0h44mxzBVoC6ye_D4ifwKnq-pz6nLTnrxFb1yowGeKj5ZJwOrmDIQdfXY2FSuNretJkfyboOCnMvFUPsTv66P4wEQQKP_cw2l_t_N24uzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec13e6c9e.mp4?token=cw0Ex9Uh6Egi1fJctRcpaYYmOTGhTeUx86xeA7BJMN6iEWflMc0PTx80O7hY0IQONXUdviasYg8st2gxOiFOfW8o3QFSlLfo03LksDECbxcOKhaJVeKPHiCw2hzs4ihTGvyn4QLsozCahyYXkZRqorlrJCTMNikdm5AaVc6yFLGnDefE0OGcZsQrrjAoO5eZYN7tQLWtOm_pEIrEFTUrIN8JCzMUqlASoEnJtdFJBzxf0h44mxzBVoC6ye_D4ifwKnq-pz6nLTnrxFb1yowGeKj5ZJwOrmDIQdfXY2FSuNretJkfyboOCnMvFUPsTv66P4wEQQKP_cw2l_t_N24uzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام خمینی(ره): با فقط گفتن «عجِّل فرج» ظهور نزدیک نمی‌شود
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450338" target="_blank">📅 06:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1GzNBuWtIMMzCOBrWLUBDTD9MflYqcRfrMiSSM5hGPo_-H0d_X1NkuPsbbiep4h6jG-Tgs20Igv5VDLAHRCeD494NGo9LCm43EL0uQh17FwWiFCur2U8XFUucI_Zmc42BDmdMXs_PLng6MN5lo2AWmfEbjKmvhtW2ou2TgoEnxcoLarz6F217YRAqKV5g0e1PTd0qUO9R55tpqzBQIKZRzPbd9_yj3M0VNFCHa0uhehNauVNr3PBDVm2Pq_1NdEClIJGeD5j3-sl1psCKaQJzKZfWbnydFN8A0Gskq__aHdVS_z6DKc_lUcvCEY_OXfFTt92RjYbrr0NBx4O9oM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامۀ انگلیسی: یمن دریای سرخ را از دو سو محاصره می‌کند
🔹
روزنامۀ دیلی‌تلگراف مدعی شد یمنی‌ها به‌دنبال پیاده‌کردن سناریوی مشابه تسلط ایران بر تنگۀ هرمز در باب‌المندب و کنترل کرانۀ دیگر دریای سرخ هستند.
🔹
این اقدام که در راستای افزایش فشار بر اقتصاد جهانی و دولت ترامپ صورت می‌گیرد، هماهنگی نزدیکی با سومالی دارد تا کنترل هر دو سوی این آبراه استراتژیک را در دست گیرد.
🔹
گفته می‌شود حوثی‌ها، فناوری پهپادی را در اختیار افرادی در سومالی قرار می‌دهند. عملاً حوثی‌ها در حال تبدیل شدن به رهبران صحنه در منطقه هستند.
🔸
بر اساس این گزارش،‌ بسته شدن هم‌زمان دو تنگۀ هرمز و باب‌المندب که حدود ۱۰ تا ۱۲ درصد از تجارت سالانۀ دریایی جهان از آن عبور می‌کند، می‌تواند شوکی عظیم به بازار انرژی وارد کند و قیمت نفت را تا مرز ۲۰۰ دلار در هر بشکه افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450337" target="_blank">📅 06:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d3086b69.mp4?token=J1a0lEbdv81N9ck0UEEk1aYrEhNcZvcMdn8ya1wwYr2m2PVSa9Apgb5vsCb3lw8Nn1bd2LoZT7n2iS97rgu3nD_ZhSvWa6-D7fWXfpk0T4g75iqwFIb6N64kQKQawGjqvHlH_tU87yaKICh9mMeK0UVTNFI826-cw2C-kv8-Onljb8TLzvu6dBEPThyQY7h3UFpTAavBCmf3DdIArs6XjtmkrGcAh0yCr1xDTclacIBrxzC2cRviCj4Odvax7_ekHj5kgc1RHjk9gBad-EQPJOjeOlUkrgeC9lo1qKNV5bqcDQPfEL2oD-yagrbWCoOyWvjoLQM_LrC_K8v2eLojsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d3086b69.mp4?token=J1a0lEbdv81N9ck0UEEk1aYrEhNcZvcMdn8ya1wwYr2m2PVSa9Apgb5vsCb3lw8Nn1bd2LoZT7n2iS97rgu3nD_ZhSvWa6-D7fWXfpk0T4g75iqwFIb6N64kQKQawGjqvHlH_tU87yaKICh9mMeK0UVTNFI826-cw2C-kv8-Onljb8TLzvu6dBEPThyQY7h3UFpTAavBCmf3DdIArs6XjtmkrGcAh0yCr1xDTclacIBrxzC2cRviCj4Odvax7_ekHj5kgc1RHjk9gBad-EQPJOjeOlUkrgeC9lo1qKNV5bqcDQPfEL2oD-yagrbWCoOyWvjoLQM_LrC_K8v2eLojsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ پهپادی ارتش به سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن
🔹
پهپادهای انهدامی ارتش در مرحلۀ نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان نیروی زمینی ارتش شد، سایت راداری ثابت، سامانۀ ارتباط و مخازن سوخت ارتش تروریستی و کودک‌کش آمریکایی در پایگاه الازرق اردن را هدف قرار دادند.
🔹
این پایگاه محل استقرار سامانه‌های پدافند ضد موشکی و یکی از مهمترین مراکز راهبردی و فرماندهی نیروهای متجاوز آمریکایی در منطقۀ غرب آسیا محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450336" target="_blank">📅 05:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سپاه: رادار پیش‌هشدار سامانۀ C-RAM در پایگاه علی السالم کویت، و محل تجمع سربازان ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
🔹
سپاه: مردم غیور و بپاخاسته ایران؛ در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری(س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانۀ C-RAM را در پایگاه علی‌السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450335" target="_blank">📅 05:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سپاه: هیچ اصابتی در پارچین و پاکدشت رخ نداده است
🔹
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450334" target="_blank">📅 05:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450333" target="_blank">📅 05:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/450332" target="_blank">📅 04:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0d7cb43d.mp4?token=FRVRYJ8A4N9YTn6sBwhLi3ZyLfg-x57-7lSPSXppCzh2t_B1-L8PDKqSSEzFghP40q2_VQMMzK27kRoW8zn4FkGhAZKWseOQ4jSwYomSMGlMGkMpUbfOxQrUNMxgkWx3a_cqR-43qEsSTIpLyAjq44_-gRNxGkt_KE_nB7R0xbiSfM9czDTpVQpPjdLWrgvpfEZMTzXEtLO7fIQUabhWIejOYmQOnzLBVXPMBzib00ItV52L5acu0_qZF9yBdr_UKJ9yNiIqUcRG6ZULzITCugWei-xcmkC-PFkMC7lgWZ4uVhb9uJ2QWAIQPP9KC6HQbL4lPAGgb01A0wFUocYtxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0d7cb43d.mp4?token=FRVRYJ8A4N9YTn6sBwhLi3ZyLfg-x57-7lSPSXppCzh2t_B1-L8PDKqSSEzFghP40q2_VQMMzK27kRoW8zn4FkGhAZKWseOQ4jSwYomSMGlMGkMpUbfOxQrUNMxgkWx3a_cqR-43qEsSTIpLyAjq44_-gRNxGkt_KE_nB7R0xbiSfM9czDTpVQpPjdLWrgvpfEZMTzXEtLO7fIQUabhWIejOYmQOnzLBVXPMBzib00ItV52L5acu0_qZF9yBdr_UKJ9yNiIqUcRG6ZULzITCugWei-xcmkC-PFkMC7lgWZ4uVhb9uJ2QWAIQPP9KC6HQbL4lPAGgb01A0wFUocYtxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع محلی می‌گویند که انفجارهایی در پایگاه هوایی «موفق السلطی» در منطقه «الازرق» رخ داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450329" target="_blank">📅 04:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
شنیده شدن صدای ۲ انفجار در خرم‌آباد
🔹
دقایقی پیش مردم در خرم‌آباد ۲ صدای انفجار را در این شهرستان شنیدند.
🔹
هنوز محل دقیق و منشا این انفجارها مشخص نیست و تاکنون مسئولین استان در این خصوص اظهار نظری نداشته‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450328" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فعالیت پدافند‌ هوایی تهران برای مقابله با هواگردهای شناسایی دشمن  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450327" target="_blank">📅 04:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به خنداب
🔹
دقایقی پیش مردم شهر خنداب صدای دو انفجار ناشی از حملات دشمن آمریکایی شنیدند.
🔹
معاون استانداری مرکزی اعلام کرد که در ساعت ۳:۳۰ دقیقۀ بامداد نقطه‌ای در خارج از شهر خنداب هدف ۲ حملۀ هوایی دشمن قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450326" target="_blank">📅 04:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فعالیت پدافند‌ هوایی تهران برای مقابله با هواگردهای شناسایی دشمن
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450325" target="_blank">📅 04:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سپاه: یک فروند پهپاد MQ9 رهگیری و منهدم شد
🔹
دقایقی قبل یک فروند پهپاد MQ9 دشمن در آسمان اندیمشک توسط سامانۀ نوین پدافند هوایی هوافضای سپاه رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450324" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450323" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تصویب فروش تجهیزات نظامی آمریکا به کویت
🔹
در بحبوحۀ مشارکت کویت در تجاوزات جدید آمریکا به ایران، وزارت خارجۀ آمریکا اعلام کرد که مجوز فروش احتمالی تجهیزات و سیستم‌های پشتیبانی هواپیماهای نظامی سی-۱۷ به کویت را به ارزش تقریبی ۴۸۴ میلیون دلار صادر کرده است.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450322" target="_blank">📅 03:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آسمان جنوب عربستان بسته شد
🔹
عربستان سعودی به‌دنبال حملات دوشنبه‌شب نیروهای مسلح یمن به فرودگاه بین‌المللی ابها، ناچار به تمدید تعطیلی سه‌روزه فرودگاه کلیدی جنوب خود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450321" target="_blank">📅 03:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
منابع خبری از انفجارهای شدید در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/450320" target="_blank">📅 02:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxkc8AR2lys8uZvmRMjRtmwKXMGpEZFEWupIeg7xR58WCzvKC8S17NTQEkir8CCrAO8uEev8s8twjDjLcVtL6fSbvTcJ63MjrM1L225GSqxxZAqYByftA6hLlELgxI-LFWHyyax9z-T_K8bbkV_3RSDXFsNgO2fA0_J3iSLp-ASCelBilOorNc_wKecMTXAIGLxBx1quYJvxT1406fa_GtZt4UlzQ_YDdSD9gfscqWMz36eC7Z0gsWCkyj2d8YbF9Rd9jvC3SLF1FEZV12Wu-uDNmpY6LQcAM5SgQCEm5mchziZBuba95ht60D9b9uBrZykqOUHxaIHdwspBdjF1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب فروش تجهیزات نظامی آمریکا به کویت
🔹
در بحبوحۀ مشارکت کویت در تجاوزات جدید آمریکا به ایران، وزارت خارجۀ آمریکا اعلام کرد که مجوز فروش احتمالی تجهیزات و سیستم‌های پشتیبانی هواپیماهای نظامی سی-۱۷ به کویت را به ارزش تقریبی ۴۸۴ میلیون دلار صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/450319" target="_blank">📅 02:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
رسانه‌های محلی گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حملۀ هوایی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450318" target="_blank">📅 02:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtbJfbZYDruKcCrpCTwGJPlkoCD4fyjYM3PiECMgwSOrmnqK1eydYkSLTgp7WPcw_8JzpX7VQHYOJa18E668eeBaeh_4mg60iWrgmCgQwlIZR2kz4u5WY5r3PnV-V3G-soRUiPWjMOWF_Ycu-YlaLprlY24S-dJUaEV3VTxHG3_2kHpkrbHSV0Y-2RvWnl3bmj6oXkWlkdc-n8j1iCxD19ODyysmrnv49GhGgaIDoktrRRW7e8nx6FswfllhPjQXPo4RDBdKIH1ykiRutWAuAljvlFieeZEicNhETFgzqatOPrpoB_6rZrdJMC1U72-XNomEXrEcvO_NIbQrpgRROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ آزادی یک جاسوس آمریکایی از ایران
🔹
رئیس‌جمهور آمریکا مدعی شد که یک جاسوس زن آمریکایی که از حدود دو سال قبل در بازداشت ایران بود، آزاد شده است.
🔹
وی در ادامۀ ادعاهایش افزود که آن زن اکنون در سلامت کامل و در شرایط خوبی در خارج از ایران است، ‌و آمریکا از این اقدام حسن‌نیت ایران قدردانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450317" target="_blank">📅 02:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
رسانه‌های محلی گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حملۀ هوایی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450316" target="_blank">📅 02:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
حملات هوایی مجدد دشمن آمریکایی به بندرعباس
🔹
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت.
📝
گزارش‌های تکمیلی متعاقباً اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450315" target="_blank">📅 02:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📹
فیلم| اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450314" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450313">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4e8a0d0a.mp4?token=IqTOtLwImQci9HHfl2C2uLvFU-X7xippz_EG6LCA--TtTf3EHkycHar213CP6WmAxWleebapPPtcOaHIQouaOUtHKPBDfJLOxp1PHLyPLYry-TnyrpCsOlrKQ9lz1afX8p2KkFbfpN5_VPj1irKdpltgwwN5vVtKQPomylnipBkij9npk-q0FTAqp1DaT1F7VABqHJydgW60SfDIrIJ_EQP98wy9eVahoXUbKy_iY3v2JCICBWHXlNBugiFupLMGOSEt7qY1Atux3t7BHvSjpwWILHTosKbZzgkn4RMRG6Cq77iGTG9bGN7kdIRD5eprnRAyOiSxB0cApilhU349Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4e8a0d0a.mp4?token=IqTOtLwImQci9HHfl2C2uLvFU-X7xippz_EG6LCA--TtTf3EHkycHar213CP6WmAxWleebapPPtcOaHIQouaOUtHKPBDfJLOxp1PHLyPLYry-TnyrpCsOlrKQ9lz1afX8p2KkFbfpN5_VPj1irKdpltgwwN5vVtKQPomylnipBkij9npk-q0FTAqp1DaT1F7VABqHJydgW60SfDIrIJ_EQP98wy9eVahoXUbKy_iY3v2JCICBWHXlNBugiFupLMGOSEt7qY1Atux3t7BHvSjpwWILHTosKbZzgkn4RMRG6Cq77iGTG9bGN7kdIRD5eprnRAyOiSxB0cApilhU349Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
فیلم|
اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450313" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450312">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در ساعت ۵۷ دقیقۀ بامداد نقاطی در حوالی قشم نیز مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450312" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450311">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقوع چندین انفجار در کویت
🔹
منابع محلی از حمله به منافع اقتصادی و تأسیسات آمریکایی در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450311" target="_blank">📅 01:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450310">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b83f5a65.mp4?token=nAW_xPUIVvTGLLj74-ypGZ2V-cpwkAgfq8AWsHCSSaGjjgYrAcOehATPHT5kzhAnpBjdCmZYouGJitFDFpKMM4cG9fvEK_QCoFqwQaWbmhVNcitFtm1kBk05VWuZ-zuLMztmW9pgBGNKCDZB85buxPyGNNtRoOIMuecwe2mXWrwXq1oNBfd9uC-wgqBFr0FjVD1G4JQY8Q_1tO-6BK4-dlSg76dDr3T4wZ24lRgqdNeEOTXZ5KIj65S06zjHX3luTC-XSQ_zeiJwZqgZXpko87yZGIPZp4c75pvCNQKD96am6axs09Wbalh1XOlqw2Jr7HqnClk3i02UjIPjClrmsRafHie9gioNX-2WNu5fikXHPVS0I6vMrMaaf6pomcUayz6CAnowl3bNTMdxnj-ftWsXKPxGxkhNFLDF3uenvVUso-zDGg7cbfba3rCgYXYcavnwZ0Deel_BGoRu0IXt8Ar1ttGGjibuxropfIQDP6PdJwecxgHh8CLyN2DMEwRJxy_5dmp673vHdSeVN6HiVkY7CYUE-muqCSz9IF3OZ6FitYLhWgAwZWdu8BIRrYGuCY1sj1baywaME1h3K6yWhFTB2puQb68NgAtMOsR9rqjBPQQPKL5CdDKpcCp5nMW7rqLFaKQYprhYeHUEvMRbzSyZqUfsGc5fWWmH6cqXqe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b83f5a65.mp4?token=nAW_xPUIVvTGLLj74-ypGZ2V-cpwkAgfq8AWsHCSSaGjjgYrAcOehATPHT5kzhAnpBjdCmZYouGJitFDFpKMM4cG9fvEK_QCoFqwQaWbmhVNcitFtm1kBk05VWuZ-zuLMztmW9pgBGNKCDZB85buxPyGNNtRoOIMuecwe2mXWrwXq1oNBfd9uC-wgqBFr0FjVD1G4JQY8Q_1tO-6BK4-dlSg76dDr3T4wZ24lRgqdNeEOTXZ5KIj65S06zjHX3luTC-XSQ_zeiJwZqgZXpko87yZGIPZp4c75pvCNQKD96am6axs09Wbalh1XOlqw2Jr7HqnClk3i02UjIPjClrmsRafHie9gioNX-2WNu5fikXHPVS0I6vMrMaaf6pomcUayz6CAnowl3bNTMdxnj-ftWsXKPxGxkhNFLDF3uenvVUso-zDGg7cbfba3rCgYXYcavnwZ0Deel_BGoRu0IXt8Ar1ttGGjibuxropfIQDP6PdJwecxgHh8CLyN2DMEwRJxy_5dmp673vHdSeVN6HiVkY7CYUE-muqCSz9IF3OZ6FitYLhWgAwZWdu8BIRrYGuCY1sj1baywaME1h3K6yWhFTB2puQb68NgAtMOsR9rqjBPQQPKL5CdDKpcCp5nMW7rqLFaKQYprhYeHUEvMRbzSyZqUfsGc5fWWmH6cqXqe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
وضعیت بیمارستان شهید بقایی اهواز پس از حملۀ آمریکا
🔹
اصابت موشک‌های دشمن به نزدیکی بیمارستان شهید بقایی اهواز و هراس شدید بیماران، موجب آغاز تخلیۀ موقت کودکان مبتلا به سرطان شد.  عکس: محمد آهنگر @Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450310" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450309">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBOPiZwUH_nCNIyPDpKwUh1UpN64G146M_Eako9Z3EIYRfnyxLqT7w9JP04UNfrj_6KvGqFvMJnEk2HN89Yg-OcSqWx7s737iBhmJSvj25sTtCRxYQ1XJsvoMwES7DkUZe5YzkzEu2hNOuI86oesY4xQoQijf62DH8N3vXO_S3KjWdybFKkedm0-ycU0952X0b_cNnzimEhNyDU26P_t0gZKX2MWzUUxv7zT9CbfPP2Nsu2Hn7N2RInBavOqDknuNvq1avPp4LzSPhou2FocCoyF6O5uZTafYg_g7KFww0Ba5NCYcwFQUFix68HtzG4uv9i8b9pwY_gyPvY-qH96Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
🔹
دشمن تصور نکند می‌تواند معادلۀ فعلی نبرد را ادامه دهد و جنگ را فرسایشی کند.
🔹
عملیات‌های ایران فعلا متمرکز بر انهدام زیرساخت تهاجمی آمریکا در منطقه است. سپس گام‌های بعدی آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/450309" target="_blank">📅 01:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450303">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEHz-hJY9ieqiA1KIwCp2EFPh-X1xbBSmcauR3aQcY7JybeQlNWoNj-r_bb-aefBcILvHgKzTa7-Ef-H7i-CZlbYwv_A_t8ugZRSQfdgDAUkP9twelmJh_oaOQ-HFs2r1Y0gLjSdMdsvvcu8f5tOwl9m1nYnKOVmDmiAe0E5gPM28ieDXH__457WXz7u8sW57uzoGQneA8mL0d1yl8Eixs9HpgMrLcb0o3ITrQMkYOOfBEPQqEoY1ieTtnhQ0xAscHFKYlM7SBgjgiCJzVcqhawNcahsonQdjW7ynnbpKQDDPYrcvHPp7xlbRTF_qdKsaDGag6z6Zg-e0sbApMmttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzJmD4l8XLu3c5K5MlS-Fi8JZzy4WMf_n_uJxE6hrqKXgEaiIaldU-3Z9uM6FyMm2d_zIb-IQ0zE4o-wPgFCT2BW32QxNJ3mOZB3QhGdIfxkiZt09Ga4Rx636CXfdNlvcHX1fHWpOY0hIZgjQ3GppcC1pHaS-gCnrfLtX7mnYNOV7VYfhR_xyhtt_3NYCHsv3u2aZWW3fVv0IecrpH2lRX4u8pwheVFYJ2IEGc6V8_qJWATahNlyOMd2-dWrUpKVo9U2ujZWFyFRSyf-pWTBh7T6jm5YLWvgCMp_aLbH1UT1ZNCh3TFwEPr8tay03_n8fSpWRtb5NQVNDxw18JGHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB4Qcg47t8q9he5vspYs64xWS6DdmMjq3KE7uAG2j0tjC78jDjSHDReNG3Io_KNoWOWYw1BgmVwYeUD5HiSqsA5xcG8TmBnpdPzg1y6sq1Bq453CHVGXfGLqnH9MQVHVWx7cJ7UXI055SOvC45G5Uy_bbSr_OHs39VQl2szlRSGoGAGusf52gbFML9Ll6txPYpK395xmuVu-vx7KQXAJsNLcxZJummwZ1y0YQvaqH7l6reg2_9PNlmuiUhYbvC7u8rijKHdIYmoA91O0iwggKm8z5KyoDJK7NVvDmM9Ij7yArwu4IDg_AS_03eStTF_ELH9S-2s5OOeQQe34BnEKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0xDON0y2CcGZCVVALtE07iBGU8Q73QiRY_X7RrWaxGBlt8-Aj4SOqz_UdDg6LQOyZBsEPC0E_3vIkaiVbTzJcqZWUqSJTN9MjRcW1-BEtxgDuE4YLSVnt6W93znyU-GWWIY4486Lo4s9nFar5nPrR3MsgZ87g9kKPQ44D2ilyqdrTs-hWlBKuuY2uXD4-ALR6AEupKXwoir-K5v6h7ertDVgAHJZbyA1aLEGoH9KAHGXQ0K1-_8i_gBjSkDJOXcBj3pZhz7LpqxYjS04rY_ScKm22dset3TVD7weiMuskTaaSMT2W7VJN49Wii1vMbPIyl298gsHE_J_8KrxRB4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGe9MFeDCdzCyYcCy2QpW2iSYvN72iMuZAtpola4XxteFJmnikcXfN_AZ22AQgxhzEoS3qnq-QX1qKhjR6y93c8dU9lbLbGOtPOhxQj0L_4w063htb-vpEfkDw0fvqplwOLIAmwP6VDMaddA6Gh7Y5IALLVp7eppS_yrk7MNHFpJ0QZBiuF89N02jbYQqo9UluKy4JvziW2G7LvMg8qnXSk5emeZrxiINvQwWNbdiLzxN0KZsrUgBWyFNsLmaNfHjxmTZC8E__8MPUj1lszZspxP-02I5ufLiFgE3vsgFbzd7RMBJ5Aokp1bOyjjevpl8C6ikwJy2oMIElMQ-hLzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFI2FMNOWc1k3tQssAwdt2kpdWs-8WzbqRNdKU1piUHo72XcwMqTKxc2AR8H3ykonpoSfiTdJM4jP6rGQi0Xx7ZVXbJyhZFw3dKiDv0E2mGOMQoNE4NkVV_S_GMiZzcAoa5Tvp22UEZwaCfRm-njr7aUcShHfJQercV-Ze_At8RDGFVyrXMfxX8f1qjxV5IpGmi1ciSFdGYc36H9UhOiUyXjEnKvduW78d-5ImKnseN6y6p6LJO5SfkIRHJIQO2iSrwcI46SXjs7Zj26JdqMzUSHPmBUyeTRN6R9fCTHcyYKY5-fdcvNLXInnbYT-S5fbIdOHZgESJTaQqEQ-e3u-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وضعیت بیمارستان شهید بقایی اهواز پس از حملۀ آمریکا  @Farsna - Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/450303" target="_blank">📅 01:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450302">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به حوالی سیریک و قشم
🔹
دقایقی پیش مردم در سیریک و قشم صدای انفجارهایی ناشی از حملات دشمن آمریکایی شنیدند.
🔹
استانداری هرمزگان اعلام کرد در ساعت ۵۵ دقیقۀ بامداد نقطه‌ای در حوالی سیریک مورد حملۀ دشمن آمریکایی قرار گرفت.
🔹
همچنین در ساعت ۵۷ دقیقۀ بامداد نقاطی در حوالی قشم نیز مورد اصابت موشک‌‌های دشمن آمریکایی قرار گرفت.
📝
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/450302" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtaGlN_LssZzADvKZ0YEEHYjZ3G1bTuKohTiVpnS0N9Dov2FuuRsTJN2m3k3UbGaG0JkhBysTREX_qlkT4x7pcrUY9sQwVEcUxiRRVeOD1QpVA556SPfcFBZ0oX_NDsuFyPCqRXP29qkBTlWyliUaPpGATsqfESIDb1GKfRvryn2z_wl2PRpIzlOA9bdEPg1J-R5p6dwhS-VoorqKvYWWxQKAt23D7yI0xSt5Dqm5ndLNVQiSORuLFJf-0j8AYxT-FiNqPsKuTnHJXqNb0LKcOZFggX5HHKAPtlgBTc_0J2o4DIyqniP1Yohjn4WvCURVp-FAd0LbbZsAieKCUz55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: تنگۀ هرمز تا پذیرش نظام قانون‌مند ایران از سوی آمریکا بسته می‌ماند
🔹
سخنگوی ارتش: تا زمانی که آمریکا نظام قانون‌مند ایرانی را نپذیرد، و سازوکار مبتنی بر ارادۀ ایرانی بر تنگۀ هرمز حاکم نشود این تنگه بسته‌ خواهد ماند.
🔹
تمکین آمریکا به مفاد تفاهم‌نامه، دست برداشتن از شرارت‌ها و دشمن ستیزی، و حاکم شدن قوانین ایرانی راهکار بازگشایی تنگۀ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450301" target="_blank">📅 01:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03358f42e.mp4?token=IYuVhcSK6kVBm5etrIYwBUjzgpP-jrRdnIDy3WgGDzpo5X4V64Za96woNWrSIcX5ezmGjo7OILc_Vn__PITQn1VrsBiUdZhIblxnm6ofikTxYW51AGntRRz_jYIePiPaPCM0t9zAeMvXCRcfTFeEVWJi7s2z2y2KsMLxqgVOWEBz740jauBeXUnycaDAm83LhUyiWlGjEfwm7n91liB3stHygBglVNEkzBaec--FHyj-eM20EiSCQbwDI3nCU0kNcAZhUn3AuwVO4rlHawiGp2VtzBC92uIdlZKYXQRUK-AC3ce-vQYHoWkKUMrV5WB_k3t5qnjPGa5obVBVYeBRxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03358f42e.mp4?token=IYuVhcSK6kVBm5etrIYwBUjzgpP-jrRdnIDy3WgGDzpo5X4V64Za96woNWrSIcX5ezmGjo7OILc_Vn__PITQn1VrsBiUdZhIblxnm6ofikTxYW51AGntRRz_jYIePiPaPCM0t9zAeMvXCRcfTFeEVWJi7s2z2y2KsMLxqgVOWEBz740jauBeXUnycaDAm83LhUyiWlGjEfwm7n91liB3stHygBglVNEkzBaec--FHyj-eM20EiSCQbwDI3nCU0kNcAZhUn3AuwVO4rlHawiGp2VtzBC92uIdlZKYXQRUK-AC3ce-vQYHoWkKUMrV5WB_k3t5qnjPGa5obVBVYeBRxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌ همدستی کویت با آمریکا در حملۀ بامدادی به ایران
🔹
برخی منابع خبری مدعی شدند که تعدادی از موشک‌های آمریکایی شلیک شده به سمت ایران، از مبدأ کویت بوده است. @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450300" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Thp0K3qx3O0Q_f2hHSAMqWF0bub8mMCQUvmttknOjGXWYTF0i518E4o3qtvH4_01Z_UmMmvYBhExUNdVWjBoOLumLK-ns_ug2oJEg6XOwHOJgRtjupYiVPHMbncYMuxmw1-StuQUzHWmFIyV8OsB_PtDVFsvBLaPTi4Y8vcdkHSpe7x3-6HRyW_NKrhSzzoTrvLZvIcbId-wDcvFfvPYdTTSE59-oXuSG5UZTazKgDswGk6dwvJwKU25_KblDDLCaf9HEARtrm1Fm4ojyHIE0nlfK9Z4y3j5Atcbep3nECipKz8mlubMJBeNQyEjz20ea8SXraIiE7weY50YtPuEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhcJk6_c5GVT7Cl0SZGdNNb9vOmWXltpccPsVOQ-rp9iOmqRbKY5GavpHM6svDHHoscMwyr8z2MbxzycOEUhT1k-7JAwkiGnYi4W0LGGCvKf-JmcrhGCvQiiVo92q4xWo-FtlLu10bdqdjchsS52JgZ1f8ZSNUjerAa-FgImd4k2FgLYQ4FaOF9zPnyzFu0RLsIzlTF4PR_yi0H5MnWxo6TNkiW670Sv_rjlo3HaBgZGHF9HdDnpbpT1rc5-pCMLkJu4VRsEBOTyiWtyvN8qX5Vhy8R9mEKiAnFglqFUHzJZ9m-N0kO8TeL86mivQg-PA2vDY7GiBEz1ApbvnYTcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAfnWAPpLP_695qiZHBX_tIJ0O23PBGlSFgNNroAO9BzF_Xmhpw6ICmefrLW2mNd2vFmtTBPjOL66IAGt0sxQoV5gX7Al8tX8QKsNjs6bDOTOlVHXH8zhxpFAH6OinnQxsRk_JmHkzBIdrldVVmcA_a4WssIsgZ8oq7d_M_IZSRC5tquEnoQASWr-ovlWpv_zhPKuVXWmp9vc29KyV4qvZrRRdsomJoO3DGgfykKuqr98LUk2tGSNHtAtZMHcONqaEM3G39Lelp0PwXUvT3GeQ3kn3_Rv6Yqko2QPH9lymOehOgNUmHi2tDLp9kbcdgRyXKGriZ7njz2-MYsUt8LgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIj-zymKzwIGDGrCBpcosYxYQpIQFP-En-MTcTYiZfj0ITjnG3YKkcG_l8lLSfxLuC9CpguzFsc-qGL-aixonxcsUh2znacQ4iIFVL3M3S--o8KE1NdluMLVel-LaCdxnNDxtKdxQGFpNfJ0wi0p0PEUtr0XItL3g1fXP8_MH8InQm0MILX3DYpHAkWqaI-xbAGYUAlmJ3OxhwdC3TekCu4IOq2hKZZ4ELBulFNRFz648YVCiGDFjlkxtZdA3QRl86WGNZOqmTK73DwFsZxNlvynY7zMjB4oqzZClTdsZaUZeAd3o0n1fWmITAvjBeviyGS3LvhJEKS1hnRh2v0Slw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450296" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVkdcy7OQETR0tYB-ZoEm_e9mBZkszBNOVyuxE-VLE8ew3UXjDFuZepdVu4ll7nxGBh3-2xnHizJpEiVPPA5cYQV_atjMEbHEbQkNldI1CJbQ7Zdp_EBBfNOyY-VBi-ugNZLd9hH9jpC_ZnpMHQU7-H9B1x6efYUKpIjNKL5QTC-tIaQ60JfiUAqD4rNNbU_1pU9grX1WAf97DOQPMN-Az7RihvQipTy8AbcejLCAF3k2zR1yyttGBTdxNV3r3dKqVwU6iWaCV7qIq28qSAsRkYxC5R7k2Kz4sJ2RGQUJrEvMrkNEmdRrvGNWcYYjdESCfspIE70ECoHjlExXAw43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p79A7KyHsDLmmJiqJE6ea4eryEkRcbD1QWKO1SPvGXunExOXQiwtTkfnadK70IR1uZLs1lNym4DtJBtdrNjGQmLlw5iTOFV9YZQgt_h7LuHsK0A4J1JuLqETASyOaAW8iyg3t0W15B5YKrrdqaBhEtdugaPp3qNiXuKuJX6YwS2LjGUWjmZKqr16HsCFm198841rkEjHcBacQ6nqlaciv3re9H2LJqbYkbAy_X9mMsB2BAlqe_ansJM2cDGqvA0JgMYvaHTQ0fnk8bXgHJBYlV67zvyVXkTydRWUP0aIk0C9vtzzXDUg0IBLGEv8H_jVbrcDwZHOXpSsXI7ZUG0TSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nsi6_kdwca3WvKDT-DNy_p-fqphQyHTvpMcvky0MtUbtXrXFwomR9WowPZVAUKT9PxwK2INYYlBdlWA5_i2I4liWbioOEe_l8_eGTiYcu1_GBWs1o8ChRX1CTZWYCSzefWNZ6v7rEae7iTW-JVWqMBM31hKs8viywNyZaclsQnPiGxJQEMJgdeACtjVsuD_WUJeJtfNli71GUQGMvIrpJ1CxnBwqG6_vPjpIqYG92KGwJaYhacjqXh2-IGTTOhpnSJL9mGbomHv1sSNUVl_5yFXi_f9TcOBiLgp1r5EZOv-F4s-x8XOKm7eHkagOu5mT8zG7s3ZPmatagCJiCT_Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJcuPcwNy53VkYv5C0VfxqJxUUELpJqJ0q7yA43fc9YOdjn8DA_ebvgI6eVo98lH6Z4wQxRm6Q--bJgeOsoatKftR1PDqDfSoWw5cJ0hHbJJhiOJ-VVme82FwoKyNermW7VNvf4G21PyOvICelPkIDt3KAcRf01m3jc5apuW7Vmanuj4sU_vuMszK2KxSinI7fMzYt18oUlttUu4jX5ZqtPR96Uc_QfdU4PoAfsfZy8qRO3y1qEqQobZh-EtAbNzwQMPlXMMc3hmhIVH5pIgCcOY-KrwyPq2q4ZfgFFYGsF3sfhrlaYHuSfEPmY5kkn-6YV_F1AuOxylayZ6JDhoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6djBGOxSkyqRJpGKUzFAObBWLeq6rtCBxCwuGSlyCli3vGHrKpMrDJN2h_6VNMKhQodt_JAtMiZ6pLJ2Q8zMQB2Y9VXmC3oT36FXRizOfmkb4hbXOXEJmJMnchI2tvrS0PTT41A-abovOeB4kVoJxQYqZ1VWsvDHU7LHffmVVqU3CU3i3clgcRdAobYO8ZqAFhk5YwbyHSNzjY1tUDN5E_yrxnIedHxikB8oHl4ATPcO1KmW_nZ-z11JyibZFdXZiLFht-0fF0m4dB8VDtRtcYVpeoXqkIUcokaEaWcbKuzOzL4kKBdlDdtoOD5UNbBt5fYmJg2OKxxZwNNbu-JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hr5A7OY65ssFon-XjQwyHsmyu6OlZ9dTyrbru5bWj46CN2ZhF6WubMC3NIVDOQdfTzgTX_ciZYAKkJcygjx4xSIs34Nrx-mwF1mf_XcvDZabM2_bhK5JgdFqqCXbfkhy3l5yKWLTcYsDMCGDJE0bO1J6fHVEuRSxF0d7NGLCImpoKQ3aErr-1locFX1W3fNdK5LE82hBsYJwjL7Rz82-PTAmrn9CAt0Z80XAiNpYtX8xbNQDwoAssTmnJplT3R2bZM8m9eZnxOPQNkg-Q9t0N0JgEueyOuCczAsB_kn_LAI6qNLqWR59M4t-IuwuQcXDygZ2AvhfoGH-zsRKE18c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfMRkjarg2YplZqEZN_g0YMrkBTLnb3UHQiUxvuH5429THo0ArUbDxdgPiYdG0n7Z7SLmYrKkioo55f8zSv5fjx-VXCLh1ELogOYgMG-RH7x8C5iSypsIeZjqeoO3XTWwN8g7hn2UKM1wDcyma1obs-631XRaCYSjJLSWp7AnmisJpWxTNPMgDNx4CfoMAXMnb5RtAPoaufXVhhZB1UBBX4JukKXoLGiNie1zFwEx2pjG7oBNI3-qAsH7wFF_yNK_oadi7l-_Do75Cq0pNMFKxutqS-ogB_AY3VzRYH3K_8_y48hOyv8Y-gzXEPyY17HWPxnyUxB5OG9XuKNqK6sDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDaSMuJEo-K6jRT_UOI3bOvEYcKuWpMNRyJtxPz9rCo0PAq5M59L9I_H1uZ6RVFdhlx8Ap32KglyHAk0nJG8PaMdvCz_79r-EerohoD6J0epNHFdEA4z_s3ompY-_CltDSA-zxGOlhsVXslCEB7YScELOxBimSAS_7BKA-eGS7lPFyEUVWfeIgnWTtDLjBzodyFN5qk3CiNJgE58NCg0EFfuX0yc2nANdLZ1y5jF56nawKBDySsO96EttceTlx3xVzMkflLFB9mqPGG48UgvCIMAN9M4eCIseTNCW_kul8vYWVT6IRUzSqTNVYVSFtQ3GizbajKUHwMNXIhGDmXk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrGWq3yCEwjAnkey3MiSlLdxndlnpB8XFbosWTD1sS-V5QSeo-PBLEHy6hwanqx3n9pq8yQ3fG4P2Z1bJNFMfkhN0q232TKzFX1MzJ3QasFiu9BiCtXqRJfpL-ELt3_ixi13r3N-y1xhKA7IUGIqvicyhN7f0VQRzoh0GNpcS0hMk8T0d9wQlyRfqAiQZGSd29Uv1lUifI7ZtBQbyfV753B_JlrtlJ_riJYTgMarFYLVR-cMWv_wsYX7b63WrcJlzBg3Zy6N7obVKrFcMUiDJLGpaR9FLOmxkQaqQUu_o7qwRRvO2CoV52czdlaeIiOxkrwDp_Vf41OrsG_UFqrowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA2Lw7NkBo2CgsLW2l_G3LmDuF0uKJJQlt-WZmv_mFhHto3Fr81cdetU2n11qpNT788wa2y8iBUDc2Hms6uoXhdwvu1B3BnFS0IlOQ91IIaYnWn4xrrHhy3Phvpr8dGvmSwOz4h6olQHctrtlU6X5raL_2CDx0slrbkqw7CO0u1sui5wA7kjK2WgAMwCeMe5hLX5THrm-PfQYoKNjC0eLLelPuhT1hqAgJUDaLfWwpqDeqO8U0mWlsG2kkjc_Lo81tJdx_PWPoS08OE5MblewUJbvQMzMjbu5Jz3_ppLuZrcphxznyAzY9fHp2iSaDcfGZCVX4GV1f-sbrJMWaNqCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450286" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8606043dd.mp4?token=HCLMItSefSJqO18cWq2FjJ5K0aaIZ2t3oHSt1JfUolPiQDUUTWDbf_0EYgcu3pnCfSpejnKbuJpLiFM4W_-02tiDOPW5m4kxZuO6aUfWEMqvBdoA18h1SASy-d_6A1Q1lTG1HQr6y7XRKeoNSLRNzO80pDOSvWtYY06V4y3yk6U6dx-vM9ld6PKaFOeZJYIhvueXCBleXNhGS_7RpBKvX9BN9UfogGWEND2RvaRgyeXshTTweRjWyBic_vNag77udU5QU8T_lCcSC2gLutKuBIvsKSbF7g1rkrIQ_F2eyoS-GZWZ02G_Vn3ul1EQjmTnmA1JG915nCMUQYAou4FOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8606043dd.mp4?token=HCLMItSefSJqO18cWq2FjJ5K0aaIZ2t3oHSt1JfUolPiQDUUTWDbf_0EYgcu3pnCfSpejnKbuJpLiFM4W_-02tiDOPW5m4kxZuO6aUfWEMqvBdoA18h1SASy-d_6A1Q1lTG1HQr6y7XRKeoNSLRNzO80pDOSvWtYY06V4y3yk6U6dx-vM9ld6PKaFOeZJYIhvueXCBleXNhGS_7RpBKvX9BN9UfogGWEND2RvaRgyeXshTTweRjWyBic_vNag77udU5QU8T_lCcSC2gLutKuBIvsKSbF7g1rkrIQ_F2eyoS-GZWZ02G_Vn3ul1EQjmTnmA1JG915nCMUQYAou4FOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ رکن اساسی خونخواهی رهبر شهید
حجت‌الاسلام اختری، رئیس کمیته حمایت از انقلاب اسلامی مردم فلسطین در مراسم یادبود امام شهید که با حضور عراقی‌های مقیم ایران در حسینیه کربلایی‌ها برگزار شد، زمینه‌های اساسی خونخواهی آقای شهید ایران را تشریح کرد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450285" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=Z1nJK-6r66ACCjvTJzqIed0erphaGW_3T18RDpBX635T4gXQn3gNRiizGAtha9_zMlUyS8urMJjFBgfR_KBkB8CK5RMAUVn00gXhATF8qXB80XHW4TM-xGLmVf-ddY4mDVZV1imnOk3MjjUjr9yMtkTjK4GQxTXevD75OpJmsX7a88Ai6Mwt830M98TQtJUzZu199Gp8yJVsUw0N2J8Z27Y0oEVF7C4rrqFIST2sodqlDkvf4-9XDv9Zk2dsdln6cGSX7ynCSSn_kfY85CzJgeMyAH4Tyy4aw2LU_zdJNCQ2smg9J-l9lUOn7q142mJpsw7QL7xxiAePtvhFWYKZYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=Z1nJK-6r66ACCjvTJzqIed0erphaGW_3T18RDpBX635T4gXQn3gNRiizGAtha9_zMlUyS8urMJjFBgfR_KBkB8CK5RMAUVn00gXhATF8qXB80XHW4TM-xGLmVf-ddY4mDVZV1imnOk3MjjUjr9yMtkTjK4GQxTXevD75OpJmsX7a88Ai6Mwt830M98TQtJUzZu199Gp8yJVsUw0N2J8Z27Y0oEVF7C4rrqFIST2sodqlDkvf4-9XDv9Zk2dsdln6cGSX7ynCSSn_kfY85CzJgeMyAH4Tyy4aw2LU_zdJNCQ2smg9J-l9lUOn7q142mJpsw7QL7xxiAePtvhFWYKZYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
اصابت موشک‌های آمریکا به نزدیکی بیمارستان کودکان سرطانی اهواز
🔹
در ساعت گذشته مردم اهواز شاهد اصابت موشک‌های دشمن به مناطق مختلف این شهر بوده‌اند.
🔹
در یکی از این حملات چند فروند موشک به جنب بیمارستان بقایی که محل شیمی‌درمانی بیماران سرطانی خصوصا کودکان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450284" target="_blank">📅 00:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b6789fc6.mp4?token=XQf0AywWhAq1_fGzwtV-HZpGQOSYhpB3_82-C_e3vRyR65jQDpzMPhozUGz750nO2mFCTSJQ8zgJcJWpbna3R83gSJlLFfIWqNJFcQcaMbHt99Rx16Zp8gAeyRcDIdbAVDiFOnAPmCCa11c379QkgDlky8VFY4iaWhJe2vmvegI7CzqWw_KnqbBeAYLnlslCCbKGlwzsubrQNZ0OXHs07BpnoRtGQGy5cyHG9fZkixoy2Qvm7Wsup2WSqsSxdw0qFhlG6RCt5youh_RI-ikJ-bAC1DKjI9Q8ivIika9rcNetcp215_cNWqbEP787Pl54ozWfCT2yzXi1fJtTtThKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b6789fc6.mp4?token=XQf0AywWhAq1_fGzwtV-HZpGQOSYhpB3_82-C_e3vRyR65jQDpzMPhozUGz750nO2mFCTSJQ8zgJcJWpbna3R83gSJlLFfIWqNJFcQcaMbHt99Rx16Zp8gAeyRcDIdbAVDiFOnAPmCCa11c379QkgDlky8VFY4iaWhJe2vmvegI7CzqWw_KnqbBeAYLnlslCCbKGlwzsubrQNZ0OXHs07BpnoRtGQGy5cyHG9fZkixoy2Qvm7Wsup2WSqsSxdw0qFhlG6RCt5youh_RI-ikJ-bAC1DKjI9Q8ivIika9rcNetcp215_cNWqbEP787Pl54ozWfCT2yzXi1fJtTtThKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین گل دوم را هم زد
⚽️
آرژانتین ۲ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/450282" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI5HZMahOUepSeg5u-RDM3ttMN4V95Zhc_CVGOd0WrsdNsAeh3HmMkARC2VGVMrDpCB4eDPpgjw8136DBjQ6XcXW3nn_QXSUcOIkYwmnOl37VQl4gknSI8PvV6NyBdArnJoilyE1JZMypZ5-773ewkfasAmf8TMb0tdGjuAxXudgTsSRp844nP5SyXZ0lUuKKhikrCM2FBBH9Bkvj1B0N0bM1DgFqkChV-eaKef8p9hT2XrCvfwPqZ2dgBuuQ-_PMpx2-fw6Ki3Vq2WcXnLp9l1UrNC3r4LzhEQNCFJK6o-7sXKox3zwIH8nl-ggteQDw6yM5JIfXB8kqYjWEIBwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی اماراتی دیگر از جنوب تنگۀ هرمز برگشت خورد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که یک کشتی اماراتی ناگهان مسیر خود را از مسیر جنوبی تنگۀ هرمز تغییر داده و برگشته است.
🔸
شب‌های گذشته دو کشتی اماراتی هدف حملۀ موشک‌های ایران قرار گرفتند که این هدف‌گیری به توقف صادرات نفت بندر فجیرۀ امارات منجر شد.
🔸
سپاه پاسداران هم هشدار داد، حالا که آمریکا مسیر نفت و گاز به دنیا را ناامن می‌کند، مسیرهای صادراتی نفت و گاز خودش و هم‌پیمانانش بسته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450281" target="_blank">📅 00:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ad3bdc6d.mp4?token=P-vpmnbphm-i5tkQRDGh0DXQAcCVnhPc0tVDwgf1O_u0c8OXKdCRF8QperEx3AXEkcoiGGyAuVfcBPZVSk_9iewWpL5jsYq6i0I4ScTFNBtGSbKoexee4klPcTZ5AiKqqPOsZhhpuEugveApxRE_Inhf4--xnYw7HIGjm_clby1myHgl-shYjWnZFV_e_9GgSX6Kg43NnSYMK9nC5BJQPn5-3RsHA1JoOsN7yOMs8Le4OPE3V2dghrb_QYrVRO0mAw917dMh2jiRXfsGqJMzNmynHKb6pZkroY5wtfGkmUfsD5z3EuPZxfS4_C6RMKw9hq-WeOvZEvaXqMO0Sm_Osw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ad3bdc6d.mp4?token=P-vpmnbphm-i5tkQRDGh0DXQAcCVnhPc0tVDwgf1O_u0c8OXKdCRF8QperEx3AXEkcoiGGyAuVfcBPZVSk_9iewWpL5jsYq6i0I4ScTFNBtGSbKoexee4klPcTZ5AiKqqPOsZhhpuEugveApxRE_Inhf4--xnYw7HIGjm_clby1myHgl-shYjWnZFV_e_9GgSX6Kg43NnSYMK9nC5BJQPn5-3RsHA1JoOsN7yOMs8Le4OPE3V2dghrb_QYrVRO0mAw917dMh2jiRXfsGqJMzNmynHKb6pZkroY5wtfGkmUfsD5z3EuPZxfS4_C6RMKw9hq-WeOvZEvaXqMO0Sm_Osw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین بالاخره در دقیقه ۸۵ گل زد
⚽️
آرژانتین ۱ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450280" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWqsOZRwmuw1SrKvHqrsSGfKeSrBv-tdeeI4PNhNN2P7p2Vd2aWGEo2RAk5JW3ff4epTcE2s6JzQtjFZ2Yvm1DJbV6naAZHnrowMT_swD2DJ9o2HjhtPkzhbGpRiC5zSrZPnzfcF4IC7ALYzpZmiKy2s9cKAoBn1BAMRE7tG66mPXKaNO4qNh-Wo5E3aLU0LrHm_bFWORzumKqeIqRrC16CvQgO_MHANbuNHa1YC5MYcW6lg_4AGjxtGBNgflUEyclM8eQmisCnQzNNTxdvvNy4903Gdz-TeLpxzxV5yNJui9IXwzKV4BweWylq3YT1EK75F9VBIgQuxKBAxiHCrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: درپی حملات اخیر ایران و افزایش نگرانی‌های امنیتی در تنگۀ هرمز، کشتی‌های تجاری از تردد در مسیرهای تحت هدایت نیروهای آمریکایی خودداری می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450279" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e8e8d33a.mp4?token=ZMI0t7OhvukITLfH0sqTC-X5FrxPZPlYX5--yhs6m7IbS-EiosPQ7ZPlQgXZB2Pe3p5yRqKZho35F9RdyRWS-gf3hgLRpMWz2zTOmVj0E2oGfmqRqFxis_Mtng_zRU9kk85ypK1fco61jyYNJwTrXSP_efTb7jnfR9HM5eZfRC-YrCBKEMARBKanwW87gdFzeccir5pbmcVTQh4D1OwxYqtaqkBJKhIwKdH_Mk1abq3qeb5Vnhi2wQOzZ71aqemqCc7KeiiaLLk7nHvsM1NVKDyA0-QnevpWg6uJbUNQP_ONa9ZtHpBtPUM9WqSCGcsLM9h7DXakXSQy5ssAd2smwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e8e8d33a.mp4?token=ZMI0t7OhvukITLfH0sqTC-X5FrxPZPlYX5--yhs6m7IbS-EiosPQ7ZPlQgXZB2Pe3p5yRqKZho35F9RdyRWS-gf3hgLRpMWz2zTOmVj0E2oGfmqRqFxis_Mtng_zRU9kk85ypK1fco61jyYNJwTrXSP_efTb7jnfR9HM5eZfRC-YrCBKEMARBKanwW87gdFzeccir5pbmcVTQh4D1OwxYqtaqkBJKhIwKdH_Mk1abq3qeb5Vnhi2wQOzZ71aqemqCc7KeiiaLLk7nHvsM1NVKDyA0-QnevpWg6uJbUNQP_ONa9ZtHpBtPUM9WqSCGcsLM9h7DXakXSQy5ssAd2smwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازهم توپ آرژانتین گل نشد  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450278" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9641ee486.mp4?token=Op5wG278s3-XQAO07T8n66ueIiTSjywqqmGfwIelkD4MKz9yhGGpV-IBA0VP-_3udBvIJthZmr-2YnYOPn3NDTEtBVNI7lTS2VFMotjQRZNFbHXcGKRl3ZpTU05arWuffajf6rjDadh2EVN40l34pyf-mLNVOivSCg8zYXIubqG_fsFiZsNvZprSf8qOuxiHoGuca5xGY7PgnwfbuEUwtQ2MKNynMlXmBKqiMqMtzlPU733cL_O-rQ8TrPKw9JYN76K90kwbSP7XmcoUkzFNzJmGnz3_-s-KBdT3bpO3HAJ6iK4l5k8iBTEXTheo5sNSYAeWJrTnC3jUP9zMcdPNLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9641ee486.mp4?token=Op5wG278s3-XQAO07T8n66ueIiTSjywqqmGfwIelkD4MKz9yhGGpV-IBA0VP-_3udBvIJthZmr-2YnYOPn3NDTEtBVNI7lTS2VFMotjQRZNFbHXcGKRl3ZpTU05arWuffajf6rjDadh2EVN40l34pyf-mLNVOivSCg8zYXIubqG_fsFiZsNvZprSf8qOuxiHoGuca5xGY7PgnwfbuEUwtQ2MKNynMlXmBKqiMqMtzlPU733cL_O-rQ8TrPKw9JYN76K90kwbSP7XmcoUkzFNzJmGnz3_-s-KBdT3bpO3HAJ6iK4l5k8iBTEXTheo5sNSYAeWJrTnC3jUP9zMcdPNLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید توسط عراقی‌‎های مقیم تهران
@Farsba
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450277" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSkpReJsZ47a-qjK_1946HG6uExuGrqguH4ESdyotXIu2othQxZ2g4xKbbCir8pJm4JA24_BjlJVtb5pFAaEMl_rQF_tMgjgQrx0k1Ycl87vJlMluTzeagqEbIkA9J4bjiSRjNWKmZTIA64IvkeQJb8aead4eU3GnJOdQAhaDH-bu_eXikF5TDj7Lq9q42Fd97_TsbxBChA2uEWkx4MSadlGKHE4QQSr0kgBQ1gFymKqFjfuXuXAkIikZIJO6NwXsFhnzJny3zN9J25hGwqu5ZLOw0SxmJQTPeKjcXhtbnblZp705DIWj1D_g6WogABHv0QX5-qE2AUJqnBT_DTNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7uUj4c7_zZgToQDpGhC28IZvj402sKCwViVXT6moNMqgCQgGJzUrhmH962Y7pX-qP-dHcszrP1Vb4F5zurpEMRJbG2HJtfPyPuBJlA7WCdfXyOiutPoSHS_IdjMLC3x8IT6EEs4ojrrIfHo23Pu6LElbBBF885h3D0BQuo8i_0PIkNAFR8HQUDOS54Npr2kDYjLHJDdcRrwdh1wAmNbhCqPgfWKALmb8qVZDm1CFJcUa2BNpSVgqX6ZqpWaN2nT1x2aIpFd3akcK1_y4N2lub8zeqmIeKJx-AUwFdLYh3BdGEm5jV0ZsAgC61zmtVOYbpX9WbY5FyanOBQ5sWiJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUDedeBkOlb88IqjMqdTIM24nOmZ3wPNX3PyyajDlgklinPFPRtHciAfb3uYQ97J6NQjdxNS1NY4UBB6NL1WikuuA86pr6o7OH_UqiYDTUcTIIaj65hQ3VS8GF2MHs14O9km1EoywDo__-gxrnNPMNpIS9vNtBfGhrNtalRhaNYxzW7HWO1GmrqXr6YYOimerRZ8qiLfmS8Zk_-9rFFl_ZHc5TuvLJmYUyorVoRwiGhog9Mbhy_Ww3Rvq0Kd4B8zv7AjIhO31Kem2beTURIQkKAiJOtZu-889JAJ0RHtBX11r2Iqp81V_we70q_G2hZgnj6dm8DBcLD_SrZa42wjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYvAEPW-HsOxD4lgsU3gOSTpV-CmenUT5zRw3VG09dXZjajTCidOS5P2q196fyxbpPFJEm0Lt9Op_wTyfwmBe479BlCkIaMsu2b8j5mYL0UHdW6181GuMgW_2WUsi879o_GY5pTGhvBDJn9JVcjlMI5pO0v1KOk3SXqj55vrZMmLDl6YQIPsIbTAoe8-odF3iC39i7U-mNLCqM4U4NBkicCUkkbOlqMM-6xE50oSaiCWR-FfR4GYS-B_qcOCQ3Ju_-MsfUut6-Eck4serbIOY-0A4VL7Sc3YciLPxHuoJzCt9f4MA2bAML5LWOTSgf8gfptKpZDMq2axQvzfOrLJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از مهار تماشایی پیکفورد
@Sportfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450273" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc2e80471.mp4?token=uQGPARtkbpOSEmrMncFXE1n1uQzPwFS5VAQDIyTNmdI-Fs1cvnOibB9fNeJwG5cdSjVj1Evfhk0-WA5RSIsTyPDeb4B-_ZxIO12FeWObDdTTiKs76rSu9i8Ha-zEVqlOzDhjZ7oEOYqRiAm7EXb5mj986sVtlbP9wgZjeiEUVNNfDNyMP5qA3mXf22x3DMsK-3ObSuqA4YvsQR19iPWZF0gkwnycoqKt0uTW-Q5bQC_zVL5t5O6L4mVU7nhOFCKH83fvYxVHRjetx6OtUB4RCnXTx-pbIVsxTA07LBS82L6A4St9ZzSKEdmW-8eXaz1xQTK5ue1yotiIbXytk7iDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc2e80471.mp4?token=uQGPARtkbpOSEmrMncFXE1n1uQzPwFS5VAQDIyTNmdI-Fs1cvnOibB9fNeJwG5cdSjVj1Evfhk0-WA5RSIsTyPDeb4B-_ZxIO12FeWObDdTTiKs76rSu9i8Ha-zEVqlOzDhjZ7oEOYqRiAm7EXb5mj986sVtlbP9wgZjeiEUVNNfDNyMP5qA3mXf22x3DMsK-3ObSuqA4YvsQR19iPWZF0gkwnycoqKt0uTW-Q5bQC_zVL5t5O6L4mVU7nhOFCKH83fvYxVHRjetx6OtUB4RCnXTx-pbIVsxTA07LBS82L6A4St9ZzSKEdmW-8eXaz1xQTK5ue1yotiIbXytk7iDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان انگلیس، آرژانتین را در گل‌زنی ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450272" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
همزمان سازمان تروریستی سنتکام از آغاز حملات جدید به ایران خبر داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450271" target="_blank">📅 00:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78c8753d4.mp4?token=e-Aw6CrPJT47aUrX8mXrNe4Bzf4e-VIF4eui-F4l72mRKfuFZcWscqBzv_R-q353i3I8hdEZ9uuB1vxIAhEsdbN9xaJVACGzm-tvHLM6cjXh8pptXnmmdp6KV0mZtt9NNV3uusbBlOJmNj-3tuxMLjxgEKDb561ruV6P0THKlReSJK2A2mUKf7VIEZpy4Xw1iqzfmpmym3gbFh4yEXm-t6xoDp3bRsYNTe5GkFSdTTbO1NVf-wOuq__bKXDUZx5YsOq3CTAzrT7_2IEZc9DXao-McnBAzxDdbUfhUT-iPW7e49Z_e7IJCzqcZRuJbewCgUWWjRDDZlAWpGGUTDh_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78c8753d4.mp4?token=e-Aw6CrPJT47aUrX8mXrNe4Bzf4e-VIF4eui-F4l72mRKfuFZcWscqBzv_R-q353i3I8hdEZ9uuB1vxIAhEsdbN9xaJVACGzm-tvHLM6cjXh8pptXnmmdp6KV0mZtt9NNV3uusbBlOJmNj-3tuxMLjxgEKDb561ruV6P0THKlReSJK2A2mUKf7VIEZpy4Xw1iqzfmpmym3gbFh4yEXm-t6xoDp3bRsYNTe5GkFSdTTbO1NVf-wOuq__bKXDUZx5YsOq3CTAzrT7_2IEZc9DXao-McnBAzxDdbUfhUT-iPW7e49Z_e7IJCzqcZRuJbewCgUWWjRDDZlAWpGGUTDh_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول انگلیس به آرژانتین توسط گوردون در دقیقه ۵۵
⚽️
آرژانتین ۰ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450270" target="_blank">📅 00:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
منابع عربی: چندین صدای انفجار مجددا در اربیل عراق شنیده شد  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450269" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SShMxzij9jmuDIUIAiuAKeNnLenNWdBOHA4yH43S4PARCTiwMZ4bHu7L07sXkj36gcSsnWHEHXwHGqHnatrSNiuoesVWecs7bFKUmyT-D13DgvdveczeoabqXbgtQWNsWdikfKcjEz8aQoqIxvlT74KqFPtrjf_at7SoAbrJHjAjuByv-ZAr5GaUfwbpuhw2PMuFytaHPD9-SHT-YvCREf_qq2BDS5RQqlf9thhIUiCzXpl5iHqT9GlGsqCaprQ_E8WTZ6drkLKYEuKe-PtZBqDNCRDJ02jHJ0gGdw4ues4JFnyNv4waRbM89Aph4jErdXmVYZkzI2CR_a-CCTbWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شباهت دو تصویر از تقابل مسی و مارادونا با انگلیسی‌ها
@Sportfars</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/450268" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=r15MEnAuyg1QBhu2sOxw1gI6uyYOe5zJdNVuIhBdu45BSCdRF0y7wMtjGOz-1eyDCbSDP6EOL9oiWI0gEgTLpnwjD3u-FBPzbeFczFw8rjD9mAxI3LKDtfk6cizK0E0PsdT5bdjzlJkwTb-OTkRaqgfCD3GwpxR5t-VHgwl3I-RAt4TH398KaTCClpi3XdJQx6YHgRd89LwwOkqmh3r2LvvP5csnnyfGLfnXkhQ4GamO7OpsHSfoWOAEs4ka1dYGN0L0IAXch3pP9vxpGxOlVGQyUyeRbJgSgFNCEsRKIVNrV2OI-BHYRDxIkYm8BXYXMnn_l7RVzdSewNCQumX9ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=r15MEnAuyg1QBhu2sOxw1gI6uyYOe5zJdNVuIhBdu45BSCdRF0y7wMtjGOz-1eyDCbSDP6EOL9oiWI0gEgTLpnwjD3u-FBPzbeFczFw8rjD9mAxI3LKDtfk6cizK0E0PsdT5bdjzlJkwTb-OTkRaqgfCD3GwpxR5t-VHgwl3I-RAt4TH398KaTCClpi3XdJQx6YHgRd89LwwOkqmh3r2LvvP5csnnyfGLfnXkhQ4GamO7OpsHSfoWOAEs4ka1dYGN0L0IAXch3pP9vxpGxOlVGQyUyeRbJgSgFNCEsRKIVNrV2OI-BHYRDxIkYm8BXYXMnn_l7RVzdSewNCQumX9ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ آرزوهای خودش را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران به‌زودی شکست می‌خورد؛ آن‌ها خیلی زود شکست خواهند خورد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450267" target="_blank">📅 23:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ac9262df.mp4?token=RpFVUTbiYkfQYH2WjE8w7vzIfn-L_yKuL8BCvIsXE0oeAs8R9lmFLOM0NOfsgBDdUN4ctaGF2RkMH42plJ7WXLAr_1syaNS969MlF8AMwGeznd6LG6hvjxo0qb-wbjIsNKDhsmyVYAMinaH6cO2AO9LfMRlxgvqIbT9l9XMm5x_cDOoOOd5nZa1MU8OqPoQVS5uQFPIWp4-pZnLtQlrerHCIka1vVKTNkk_1rGely6KJp-6UhauSpZvILAZszdqhPoFOBpRxSnov7c4kwFpOFtDxcAhEIFSIj3pJ0b0FlMmDf9hvtOcxz-v72107wHFjR-RUnA1gU0Aye5co9v__eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ac9262df.mp4?token=RpFVUTbiYkfQYH2WjE8w7vzIfn-L_yKuL8BCvIsXE0oeAs8R9lmFLOM0NOfsgBDdUN4ctaGF2RkMH42plJ7WXLAr_1syaNS969MlF8AMwGeznd6LG6hvjxo0qb-wbjIsNKDhsmyVYAMinaH6cO2AO9LfMRlxgvqIbT9l9XMm5x_cDOoOOd5nZa1MU8OqPoQVS5uQFPIWp4-pZnLtQlrerHCIka1vVKTNkk_1rGely6KJp-6UhauSpZvILAZszdqhPoFOBpRxSnov7c4kwFpOFtDxcAhEIFSIj3pJ0b0FlMmDf9hvtOcxz-v72107wHFjR-RUnA1gU0Aye5co9v__eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول انگلیس به آرژانتین توسط گوردون در دقیقه ۵۵
⚽️
آرژانتین ۰ - ۱ انگلیس
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450266" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
